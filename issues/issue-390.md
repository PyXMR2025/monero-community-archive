---
title: '[beta] Stressnet node not syncing after restart'
source_url: https://github.com/seraphis-migration/monero/issues/390
author: ComputeryPony
assignees: []
labels: []
created_at: '2026-05-16T00:41:20+00:00'
updated_at: '2026-05-27T16:26:07+00:00'
type: issue
status: closed
closed_at: '2026-05-27T16:26:07+00:00'
---

# Original Description
Similar to #313 I am currently running a beta stressnet node now, with an open port.
I needed to poweroff my machine troubleshoot an unrelated issue, the stressnet node was currently in the middle of what appeared to be a large re-org, as there were many "Alternative block added" messages printing out. I issued `exit` to the stressnet node but after 3 minutes it hadn't stopped so I went ahead and shutdown without stopping it cleanly.
On restart an hour or 2 later I noticed that the node is now no longer syncing and it stuck at height 3002495.
`monerod` doesn't print anything about a corrupt database and while the daemon hadn't been shutdown cleanly, the system was still powered off correctly so I don't suspect file corruption of the database.

Output of `sync_info`:
```
Height: 3002495, target: 3002495 (100%)
Downloading at 508 kB/s
16 peers
Remote Host                        Peer_ID   State   Prune_Seed          Height  DL kB/s, Queued Blocks / MB
116.203.98.127:28080      d940758ee2484199  synchronizing     183       3002718  0 kB/s, 0 blocks / 0 MB queued
177.40.35.26:37280        e198a0a7b4396411  synchronizing     182       3003147  0 kB/s, 0 blocks / 0 MB queued
71.31.209.128:43918       c059ecc5c44c93f0  synchronizing     0         3002996  0 kB/s, 0 blocks / 0 MB queued
204.76.203.25:38494       f5d9d91aa7ba2df5  synchronizing     0         3002918  0 kB/s, 0 blocks / 0 MB queued
208.123.187.228:38242     1ecf353398d85b18  synchronizing     183       3002753  0 kB/s, 0 blocks / 0 MB queued
88.99.195.15:28282        dbf6707292210d04  synchronizing     184       3003258  0 kB/s, 0 blocks / 0 MB queued
73.92.185.10:56192        e9e6b9687e8286ae  synchronizing     182       3002676  0 kB/s, 1 blocks / 1.18332 MB queued
194.58.47.153:36848       c74bd919f94bfc32  standby           187       3003329  6 kB/s, 0 blocks / 0 MB queued
148.63.215.132:12288      11494782ea1770fc  synchronizing     0         3002562  0 kB/s, 0 blocks / 0 MB queued
208.123.187.151:37342     73e31dab6d0075fd  synchronizing     182       3003029  0 kB/s, 0 blocks / 0 MB queued
142.182.174.111:21759     aff67defac4e1c1f  normal            180       2158677  0 kB/s, 0 blocks / 0 MB queued
35.134.24.149:45834       112a59b4f59b98a4  normal            185       1920510  0 kB/s, 0 blocks / 0 MB queued
185.141.216.147:54646     93346c905492cccb  normal            186       3002383  0 kB/s, 0 blocks / 0 MB queued
14.100.107.228:50456      51d1182eeb30f9cf  normal            0         3002383  1 kB/s, 0 blocks / 0 MB queued
88.72.112.39:61223        dde78a5b94141d8b  synchronizing     186       3003329  501 kB/s, 1 blocks / 4.90472 MB queued
205.197.212.198:59228     2297e15ff5a4cd71  normal            0         1546963  0 kB/s, 0 blocks / 0 MB queued
833 spans, 1006.03 MB
[moooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo]
88.72.112.39:61223        1/185 (3002495 - 3002495, 4904 kB)  503 kB/s (0.04)
208.123.187.228:40966     1/185 (3002496 - 3002496, 4932 kB)  6406 kB/s (0.89)
208.123.187.228:40966     1/185 (3002497 - 3002497, 4927 kB)  844 kB/s (0.89)
208.123.187.228:40966     1/185 (3002498 - 3002498, 4928 kB)  25057 kB/s (0.89)
208.123.187.228:40966     1/185 (3002499 - 3002499, 4928 kB)  16707 kB/s (0.89)
208.123.187.228:40966     1/185 (3002500 - 3002500, 4889 kB)  2792 kB/s (0.89)
208.123.187.228:40966     1/185 (3002501 - 3002501, 4801 kB)  15368 kB/s (0.89)
116.203.98.127:28080      1/185 (3002502 - 3002502, 4837 kB)  198 kB/s (0.01)
194.58.47.153:55392       1/185 (3002503 - 3002503, 4781 kB)  2131 kB/s (0.15)
truncated here, lots of entries
```

# Discussion History
## nahuhh | 2026-05-16T00:48:50+00:00
> 88.72.112.39:61223        1/185 (3002495 - 3002495, 4904 kB)  503 kB/s (0.04)

Does this entry change after some time?
Since you dont have any gaps in your download queue, the fact that it downloaded all of those spans (it should normally be limited) tells me that monerod is still likely looking for the next span. So the 495 on the span is probably no-good. Only lvl 2 logs will tell.

How does your cpu usage look?

Any interesting logs while its not syncing that block?

## nahuhh | 2026-05-16T00:52:02+00:00
As you can probably tell, there is quite a bad netsplit on stressnet atm. Most peers are on different heights

## ComputeryPony | 2026-05-16T00:53:04+00:00
Yeah, that entry appears to change to different IPs when running the command repeatedly.

I still see spikes of CPU usage even in this state, htop shows monerod sitting at 1% for a bit then jumping up to 600% for several seconds before dropping back down.

While idling I see lots of blocked/unblocked messages and "Sync data returned a new top block candidate" very frequently. I'm seeing the ban messages every couple seconds right now.

## nahuhh | 2026-05-16T00:55:49+00:00
edited original message to add "Since you dont have any gaps in your download queue, the fact that it downloaded all of those spans (it should normally be limited) tells me that monerod is still likely looking for the next span. So the 495 on the span is probably no-good. Only lvl 2 logs will tell."

## ComputeryPony | 2026-05-16T00:56:58+00:00
I'll get some level 2 logs. Unfortunately it's been in this state for about 20 hours so I don't think at this point it's going to recover on it's own.

## ComputeryPony | 2026-05-16T01:07:03+00:00
I should mention I am on commit d1adfbba21cdde7cec4b732ae4682ac44ee79167.

Level 2 log: [output.log.gz](https://github.com/user-attachments/files/27838657/output.log.gz)

## nahuhh | 2026-05-16T01:18:00+00:00
fwiw, my seed nodes sync_info looks wildly different to yours (all peers at 3353)


```
Height: 3003354, target: 3003354 (100%)
Downloading at 0 kB/s
10 peers
Remote Host                        Peer_ID   State   Prune_Seed          Height  DL kB/s, Queued Blocks / MB
100.14.80.141:41852       fdf4b5d9b03aec23  normal            0         3003354  0 kB/s, 0 blocks / 0 MB queued
37.19.199.143:24449       168fa66c43c5986d  normal            186       3003353  0 kB/s, 0 blocks / 0 MB queued
216.128.11.5:19942        df37b788977b9857  normal            0         3003353  0 kB/s, 0 blocks / 0 MB queued
84.115.211.241:49866      90d64c344097a178  normal            0         3003353  0 kB/s, 0 blocks / 0 MB queued
204.76.203.25:52370       f5d9d91aa7ba2df5  normal            0         3003354  0 kB/s, 0 blocks / 0 MB queued
148.63.215.132:38914      11494782ea1770fc  normal            0         3003353  0 kB/s, 0 blocks / 0 MB queued
193.32.248.241:43840      5b4005345eff9fc1  normal            180       3003353  0 kB/s, 0 blocks / 0 MB queued
88.72.112.39:64765        dde78a5b94141d8b  normal            186       3003354  0 kB/s, 0 blocks / 0 MB queued
186.176.37.131:36302      93871c1a20587327  normal            0         3003353  0 kB/s, 0 blocks / 0 MB queued
177.40.35.26:51550        e198a0a7b4396411  normal            182       3003353  0 kB/s, 0 blocks / 0 MB queued
0 spans, 0 MB
[]
```



## ComputeryPony | 2026-05-16T01:18:20+00:00
```
2026-05-16 00:58:44.394 [P2P3]  ERROR   verify  src/cryptonote_core/blockchain.cpp:4846 Block with id: <e0b1e737f7ecc49f6ac22515346320f472f1f1737877eb11fc3828a666068a9c> has incorrect miner transaction
```
I do see this repeated several times in that log file after it looks like it verified 690 txs.
It appears to be verifying the same txs over and over before getting caught on this error.

## nahuhh | 2026-05-16T01:19:34+00:00
> ```
> 2026-05-16 00:58:44.394 [P2P3]  ERROR   verify  src/cryptonote_core/blockchain.cpp:4846 Block with id: <e0b1e737f7ecc49f6ac22515346320f472f1f1737877eb11fc3828a666068a9c> has incorrect miner transaction
> ```
> I do see this repeated several times in that log file after it looks like it verified 690 txs.
> It appears to be verifying the same txs over and over before getting caught on this error.

this is a known issue / currently under investigation, likely caused by new stressnet scaling

## ComputeryPony | 2026-05-16T01:19:35+00:00
I don't appear to have the `e0b1e737f7ecc49f6ac22515346320f472f1f1737877eb11fc3828a666068a9c` transaction though?
print_tx doesn't find it.
Wouldn't that be coming from a peer then, and in that case, how did the peer allow the bad tx to get included?

EDIT: Ah, so this is a new issue then.

## nahuhh | 2026-05-16T01:20:32+00:00
> I don't appear to have the `e0b1e737f7ecc49f6ac22515346320f472f1f1737877eb11fc3828a666068a9c` transaction though?
> print_tx doesn't find it.
> Wouldn't that be coming from a peer then, and in that case, how did the peer allow the bad tx to get included?

that a block id, try `print_block`

## ComputeryPony | 2026-05-16T01:20:48+00:00
```
print_block e0b1e737f7ecc49f6ac22515346320f472f1f1737877eb11fc3828a666068a9c
Error: Unsuccessful --
```

## ComputeryPony | 2026-05-16T01:23:00+00:00
If this is what is stopping my node from advancing then I take it attempting a re-sync would be useless as it would get stuck on the same transaction.

In which case I will need to wait for the issue to be fixed.

## nahuhh | 2026-05-16T01:23:54+00:00
> Wouldn't that be coming from a peer then, and in that case, how did the peer allow the bad tx to get included?

broken scaling allowed bad blocks to be produced, but seemingly cant be synced by peers

## ComputeryPony | 2026-05-16T01:31:55+00:00
Is there any use keeping my node as is to help investigate a fix for the scaling bug or am I free to attempt to force it to sync?

I plan on just commenting out the offending tx check and letting it sync up before re-enabling it.

## nahuhh | 2026-05-16T01:53:36+00:00
Commenting out the check isnt going to fix it. you need to get on the right chain

1. Create a backup of the db, in case its leter needed for diag
2. Start monerod with `--offline`
3. `pop_blocks 200` and `flush_txpool`
4. Restart monerod with `--add-exclusive-node=185.141.216.177:28180 --in-peers=0`

it should then sync

## ComputeryPony | 2026-05-16T04:38:57+00:00
Ok, so after poping the blocks and clearing the txpool I can sync for a while with your node.

After a bit my node starts to block your node:
```
2026-05-16 04:19:25.658 I Synced 3002375/3003464 (99%, 1089 left)
2026-05-16 04:19:28.560 I Synced 3002376/3003464 (99%, 1088 left)
2026-05-16 04:19:31.444 I Synced 3002377/3003464 (99%, 1087 left)
2026-05-16 04:19:34.709 I Synced 3002378/3003464 (99%, 1086 left)
2026-05-16 04:19:36.377 I Synced 3002379/3003464 (99%, 1085 left)
2026-05-16 04:19:40.700 I Synced 3002380/3003464 (99%, 1084 left)
2026-05-16 04:19:43.621 I Synced 3002381/3003464 (99%, 1083 left)
2026-05-16 04:19:46.956 I Synced 3002382/3003464 (99%, 1082 left)
2026-05-16 04:19:49.889 I Synced 3002383/3003464 (99%, 1081 left)
2026-05-16 04:19:52.657 W monerod is now disconnected from the network
2026-05-16 04:19:54.385 I [185.141.216.177:28180 OUT] Sync data returned a new top block candidate: 3002383 -> 3003464 [Your node is 1081 blocks (1.5 days) behind] 
2026-05-16 04:19:54.385 I SYNCHRONIZATION started
2026-05-16 04:19:57.811 I Host 185.141.216.177 blocked.
2026-05-16 04:19:57.812 W monerod is now disconnected from the network
2026-05-16 04:21:57.542 I Host 185.141.216.177 unblocked.
2026-05-16 04:21:57.592 I [185.141.216.177:28180 OUT] Sync data returned a new top block candidate: 3002383 -> 3003465 [Your node is 1082 blocks (1.5 days) behind] 
2026-05-16 04:21:57.592 I SYNCHRONIZATION started
2026-05-16 04:22:01.120 I Host 185.141.216.177 blocked.
2026-05-16 04:22:01.121 W monerod is now disconnected from the network
print_height 
3002383
2026-05-16 04:24:01.730 I Host 185.141.216.177 unblocked.
2026-05-16 04:24:09.703 I [185.141.216.177:28180 OUT] Sync data returned a new top block candidate: 3002383 -> 3003467 [Your node is 1084 blocks (1.5 days) behind] 
2026-05-16 04:24:09.703 I SYNCHRONIZATION started
2026-05-16 04:24:12.538 I Host 185.141.216.177 blocked.
2026-05-16 04:24:12.538 W monerod is now disconnected from the network
```

Sure enough after turning on log-level 2 I can see it's because of an invalid coinbase tx again. Curiously though after restarting the node, it syncs past the point it was previously stuck at.

I was under the assumption the bug in the scaling code was somehow allowing invalid transactions to be accepted on chain but this seems to indicate that something is corrupting the tx before getting sent to a peer as otherwise I shouldn't be getting different coinbase txs from the same node for the same block height by just restarting my node.

## nahuhh | 2026-05-16T04:48:36+00:00
Very interesting that it blocks the exclusive node, but allows the sync to continue on a subsequent run. Sounds like a consensus issue? Hopefullybwe can reproduce this reliably and get it figured out

## j-berman | 2026-05-27T16:26:07+00:00
Should be resolved by v2.0 (#393)

# Action History
- Created by: ComputeryPony | 2026-05-16T00:41:20+00:00
- Closed at: 2026-05-27T16:26:07+00:00
