---
title: Cannot connect to peers or sync with monerod-0.15.0.1
source_url: https://github.com/monero-project/monero/issues/6250
author: pkreuzt
assignees: []
labels: []
created_at: '2019-12-18T10:15:37+00:00'
updated_at: '2024-08-10T23:04:00+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
When running monerod (log-level 1) I see lots of "connect failed" to peers and seeds, and some:

 "COMMAND_HANDSHAKE invoke failed. (-3, LEVIN_ERROR_CONNECTION_DESTROYED)"

Sync is not succeeding. Also there is a weird "found new version" in the output, I'm already running 0.15.0.1:

Found new version 0.15.0.1 with hash 083a3862f554a2e5157686d7a8075557dfd6f07de08069cac91017c17739750b

Log attached.

[bitmonero.log](https://github.com/monero-project/monero/files/3977821/bitmonero.log)


# Discussion History
## moneromooo-monero | 2019-12-18T10:59:29+00:00
For the update notification, this seems odd. Can you try with this patch and post what the extra output is ?

```
diff --git a/src/cryptonote_core/cryptonote_core.cpp b/src/cryptonote_core/cryptonote_core.cpp
index 521f71c07..89e8a4ae8 100644
--- a/src/cryptonote_core/cryptonote_core.cpp
+++ b/src/cryptonote_core/cryptonote_core.cpp
@@ -1766,6 +1766,7 @@ namespace cryptonote
     if (!tools::check_updates(software, buildtag, version, hash))
       return false;
 
+MGINFO("tools::vercmp(" << version << ", " << MONERO_VERSION << "): " << tools::vercmp(version.c_str(), MONERO_VERSION));
     if (tools::vercmp(version.c_str(), MONERO_VERSION) <= 0)
     {
       m_update_available = false;
```

## moneromooo-monero | 2019-12-18T11:00:09+00:00
If you don't know to to apply patches, just add the line withe a + (but do not include the + itself) at the right place in src/cryptonote_core/cryptonote_core.cpp and rebuild.

## pkreuzt | 2019-12-18T11:05:06+00:00
But I'm using the official binary linux-x64 version downloaded from GitHub. And of course, the SHA256 sum is correct.

## moneromooo-monero | 2019-12-18T12:16:48+00:00
https://github.com/monero-project/monero/pull/6251 should fix the wrong update being selected.

## moneromooo-monero | 2019-12-18T12:37:03+00:00
About the connection problems, does it still happen ? The seeds were apparently being moved around, and I can connect from a fresh state now.
The connection destroyed messages are ok.

## pkreuzt | 2019-12-18T14:06:48+00:00
It seems to be related to the blockchain. If I backup it to another location and start from the beginning, it begins syncing correctly. Is it common to have connection issues if the blockchain is corrupted or something?

## moneromooo-monero | 2019-12-18T14:25:49+00:00
Odd. This could be the case if you're running an old version of monero, but you said you're running 0.15.0.1, which is recent. However, it also tells you 0.15.0.1 is an update to your version. Are you sure you're not running some bastard version that claims to be 0.15.0.1 but is in fact older ?

## moneromooo-monero | 2019-12-18T14:45:23+00:00
What does "status" say in monerod ?

## pkreuzt | 2019-12-18T14:51:03+00:00
Well, I downloaded it from this same place and checked the signed hash of the tar.bz2 file on https://web.getmonero.org/downloads/hashes.txt .

Status command reports:

`Height: 1991442/1991442 (100.0%) on mainnet, not mining, net hash 940.85 MH/s, v12, up to date, 0(out)+0(in) connections, uptime 0d 0h 0m 54s`

## moneromooo-monero | 2019-12-18T15:02:20+00:00
That looks right.
Try exiting monerod, deleting ~/.bitmonero/p2pstate.bin, and restarting monerod.
This will purge old peers. This should not prevent connection to seeds though. Let's see if that fixes it.

## pkreuzt | 2019-12-18T15:08:59+00:00
I have already tried that, no difference.

## moneromooo-monero | 2019-12-18T15:13:18+00:00
Really odd. If the reason was a corrupt chain, you'd expect connections to succeed, and then peers to ban you when they receive bad data. I have no idea what coiuld be happening currently. Try a level 2 log for a few minutes, maybe there'll be something that gives a clue there.

## pkreuzt | 2019-12-18T15:25:56+00:00
Here it is:

[bitmonero.log](https://github.com/monero-project/monero/files/3979104/bitmonero.log)


## moneromooo-monero | 2019-12-18T15:45:06+00:00
Are you connecting via tor ?

## pkreuzt | 2019-12-18T15:49:20+00:00
I usually do, but not this time. I had to sync from an old backup at about 85% and doing it via tor was too slow.

## moneromooo-monero | 2019-12-18T15:55:51+00:00
The possible reason I was seeing is the nodes you were connecting to already had connections from that exit node, so were dropping new ones. Now I'm really out of ideas.

## pkreuzt | 2019-12-19T20:30:13+00:00
News on this, I discarded blockchain and synced again from that old backup, but this time with:

`$ monerod --db-sync-mode safe`

Now it's working well so far. So definitely it was some weird corruption issue. This can be closed now.

## moneromooo-monero | 2019-12-19T20:32:54+00:00
I would be *very* surprised if that was the reason.

If you restart from the backup again, without --db-sync-mode safe, does it work ?

## pkreuzt | 2019-12-19T23:13:51+00:00
It does.

## moneromooo-monero | 2019-12-20T00:28:14+00:00
This seems points to transient (though fairly long lived) network issues.

## pkreuzt | 2019-12-28T21:02:08+00:00
Interestingly, the daemon seems to work only with an old p2pstate.bin file. If I delete it (which is recommended when using Tor) then I get those "connect failed" messages and the newly created p2pstate seems empty with only 32 byte size.

## moneromooo-monero | 2019-12-30T15:52:26+00:00
That's helpful.
p2pstate.bin contains a list of known peers.
If you delete it, monerod will know no peers but the hardcoded seeds and any you give on the command line. If none of the seeds are reachable, then monerod cannot find the monero network, and will write an empty p2pstate.bin file since it could not find any new peers.
Deleting p2pstate.bin means you forgot any "marker" peer someone might have sent you (ie, they send some node a non-monero peer, then check later if it gets tried by another node, then they know it's the same node). This seems like a long shot spying technique though.

## pkreuzt | 2020-01-03T19:10:04+00:00
I've been syncing from scratch again (with --db-sync-mode safe) and making some periodic tests, cleanly stopping monerod and erasing p2pstate.bin (after saving it apart) to verify it keeps syncing and writing a valid file. For some reason, after sync state reaches >99% if monerod is stopped it no longer works without a p2pstate. As I said before, it writes an empty (32 byte) file. This happens on 2 different systems (Debian testing and Mageia 7, both x64 and freshly installed). Restoring latest p2pstate.bin file makes it connect and sync again. No one else has this problem?

## moneromooo-monero | 2020-01-03T19:43:40+00:00
Am I understanding right that whether the daemon is close to up to date or not is a good predictor of whether it will succesfully connect to peers ?

## pkreuzt | 2020-01-03T19:56:35+00:00
That's it. But only if starting without a valid p2pstate.bin file.

## moneromooo-monero | 2020-01-03T20:04:28+00:00
That's very interesting. I'm seeing that too. Thanks for the repro case.

## Cactii1 | 2022-07-20T20:39:38+00:00
@moneromooo-monero considering Monero is at v0.18, do you think this very old issue should still be open?

## selsta | 2022-07-20T20:40:59+00:00
Quite sure this issue still exist, will keep it open.

## thisIsNotTheFoxUrLookingFor | 2024-08-10T03:34:43+00:00
It does exist. I deleted my p2pstate.bin and i am at 96% sync and now it just syncs nothing

`Height: 3102820/3211830 (96.6%) on mainnet, not mining, net hash 2.16 GH/s, v16, 62(out)+4(in) connections, uptime 0d 0h 10m 9s`

just sits there not syncing.

I have spent about a month and deleted the chain 3 times trying to get synced, i am about ready to give up and call Monero a doomed project.

In polar opposite I pull > 600GB of Bitcoin blockchain fine overnight.

**Edit** oh yea awesome I just got 5 blocks and there is only 3.7 months left untill I am fully synced....

`2024-08-10 03:34:12.640 I Synced 3102825/3211830 (96%, 109005 left, 0% of total synced, estimated 3.7 months left)`

63 peers out and 7 in, what can be the reason for this? The appliance is an 8 core i3-N305 and it is not bottlenecked monerod is barely using it.

it kinda seems like every block it receives it rescans the entire blockchain again or something silly, disk activity is high I can hear the drives thrashing about.

## selsta | 2024-08-10T17:55:04+00:00
@pkreuzt what kind of hardware do you have? where is your blockchain saved? also can you open a new issue? this here is unrelated

## thisIsNotTheFoxUrLookingFor | 2024-08-10T23:02:31+00:00
@selsta I'm running on a [i3-N305](https://www.intel.com/content/www/us/en/products/sku/231805/intel-core-i3n305-processor-6m-cache-up-to-3-80-ghz/specifications.html), 32GB DDR5 RAM, it is a NAS. The blockchain is on a RAIDZ1 (4x16TB HDD) and the raid is mounted locally on the NAS so it is not accesses by monerod over network share or anything like this. monerod is running in debian bookworm.

Ok I will make new issue

# Action History
- Created by: pkreuzt | 2019-12-18T10:15:37+00:00
