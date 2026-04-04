---
title: monerod v0.10.3.1 does not sync
source_url: https://github.com/monero-project/monero/issues/1947
author: ElLamparto
assignees: []
labels: []
created_at: '2017-04-01T07:00:24+00:00'
updated_at: '2017-09-28T02:53:08+00:00'
type: issue
status: closed
closed_at: '2017-08-09T10:24:13+00:00'
---

# Original Description
The previous monerod version worked perfectly but suddenly it stopped syncing.

1. When I was 3 days behind, I installed v0.10.3.1 - no syncing
2. I ran monero-blockchain-import --pop-blocks 3000: it put me 6 days behind, but still no syncing.

Attached is level 1 log.
Debian 8 32bit, DB on a local HDD.

What happened and what can I do to fix it?

[ml1.txt.zip](https://github.com/monero-project/monero/files/887437/ml1.txt.zip)


# Discussion History
## moneromooo-monero | 2017-04-01T10:15:44+00:00
Unclear. You don't seem to be receiving blocks in the first place. Try deleting ~/.bitmonero/p2pstate.bin while monerod is not running.

## ElLamparto | 2017-04-01T16:52:37+00:00
I've removed ~/.bitmonero/p2pstate.bin --> no change.
[bitmonero.log.zip](https://github.com/monero-project/monero/files/887802/bitmonero.log.zip)

Then I removed all files, except lmdb directory --> no change.

Finally I removed ~/.bitmonero --> it immediately started synchronizing (from scratch).

I suppose there may be a problem with the DB after all.
Is there a way to verify the database?


## ElLamparto | 2017-04-01T18:11:04+00:00
UPDATE: My happiness did not last. Syncing from scratch stopped.
[bitmonero.log.zip](https://github.com/monero-project/monero/files/887860/bitmonero.log.zip)

I could send you ~/.bitmonero directory, maybe you could recreate the problem.
But how? It has 29.3 MB (zipped).



## moneromooo-monero | 2017-04-01T18:53:37+00:00
The first few times the daemon restarts, it seems pretty quick, so there's no indication that it had stopped syncing. Try running with this extra option:

  --log-level 1,\*msg\*:INFO

This will give more logs about what the P2P layer is doing.


## ElLamparto | 2017-04-01T20:36:27+00:00
Here is the log with --log-level 1,msg:INFO. Hopefully you will see something.
[bitmonero.log.zip](https://github.com/monero-project/monero/files/887942/bitmonero.log.zip)

I'm copying the whole Monero stuff over to another machine. We will see...



## moneromooo-monero | 2017-04-02T08:16:22+00:00
I meant \*msg\*, github has a nasty tendency to remove stars and add italics instead.
I fixed the comment above.

## moneromooo-monero | 2017-04-02T08:24:14+00:00
Still, the "Failed to do_send()" messages indicate some kind of networking problem, but it's not clear what. Maybe something more verbose:

--log-level 1,\*msg'*:INFO,\*net\*:DEBUG




## ElLamparto | 2017-04-02T08:36:12+00:00
1. You were right. I resumed syncing from scratch and it works (so far).
2. I put monerod (with the DB -7 days) on another machine, let it run for the night and no block was added.

## ElLamparto | 2017-04-02T11:41:10+00:00
Here is the log.

[bitmonero.log.zip](https://github.com/monero-project/monero/files/888333/bitmonero.log.zip)

Since the syncing from scratch works, the problem is somehow related to the database contents/size. The p2p layer should not have anything in common with the database, but maybe there is a memory corruption in the DB part that affects p2p? I wonder what you will find in the log...

## moneromooo-monero | 2017-04-02T12:00:49+00:00
That log shows that your node is connecting properly, then requests a set of blocks, but never gets a response. This means that you seem to be right about it being related to the database contents. It looks like the node you are requesting from does not like the request and may be ignoring it. Without seeing what the other node logs, it's hard to tell right now what the problem is. Is the zip file of the db too large to attach to github ?

## ElLamparto | 2017-04-02T15:46:57+00:00
It could be true, especially that in the past I often saw in the terminal a trace like "invalid block received, closing connection". On the other hand, I executed [monero-blockchain-import --pop-blocks 3000], so potentially invalid contents should have been deleted.

data.mdb has 13.5 GB, github allows up to 10MB zip...

uTox is quite reliable in transferring large files. Otherwise there are online services, but I have never use them. Any suggestions?

## moneromooo-monero | 2017-04-03T13:15:15+00:00
Try to run monerod again (with the broken blockchain), adding:

--add-exclusive-node  163.172.182.165:18080 --log-level 1,\*net\*:DEBUG,\*throttle\*:ERROR

Then, after it stops again, please post the log again. I'll get the other logs from that node.


## ElLamparto | 2017-04-03T18:30:53+00:00
Just finished. 
[bitmonero.log.zip](https://github.com/monero-project/monero/files/890985/bitmonero.log.zip)

My IP address ends with 137.116


## ElLamparto | 2017-04-05T07:47:39+00:00
I've attempted to sync from scratch and it got stuck at 6.6%. Restart did not help.

## moneromooo-monero | 2017-04-09T22:43:49+00:00
Comparing the two daemon logs, it looks like it might be a timeout, though there is no telltale message about this. Your daemon seems to have a fairly low bandwidth limiter, and blocks a lot when sending. Is this correct, and does the syncing work when removing that limit ?

## ElLamparto | 2017-04-10T08:57:36+00:00
The limit is --limit-rate-up 10 --limit-rate-down 50. The previous monerod version was running happily with that limit.

I removed that limit and the first 50 minutes nothing happened and then:

2017-04-10 10:38:15.136 [P2P1]  WARN    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:71   Failed to add tx blob to db transaction: MDB_KEYEXIST: Key/data pair already exists
2017-04-10 10:38:15.228 [P2P1]  ERROR   blockchain      src/cryptonote_core/blockchain.cpp:3383 Error adding block with hash: <425995a3ae61578a2d9a7eebfeb109915b0d9c1dbc4029c0fb1369d542261d1c> to blockchain, what = Failed to add tx blob to db transaction: MDB_KEYEXIST: Key/data pair already exists
2017-04-10 10:38:25.797 [P2P3]  ERROR   blockchain      src/cryptonote_core/blockchain.cpp:3383 Error adding block with hash: <425995a3ae61578a2d9a7eebfeb109915b0d9c1dbc4029c0fb1369d542261d1c> to blockchain, what = Attempting to add transaction that's already in the db (tx id 2359199)
2017-04-10 10:38:37.388 [P2P8]  ERROR   blockchain      src/cryptonote_core/blockchain.cpp:3383 Error adding block with hash: <425995a3ae61578a2d9a7eebfeb109915b0d9c1dbc4029c0fb1369d542261d1c> to blockchain, what = Attempting to add transaction that's already in the db (tx id 2359199)
2017-04-10 10:38:51.681 [P2P2]  ERROR   blockchain      src/cryptonote_core/blockchain.cpp:3383 Error adding block with hash: <425995a3ae61578a2d9a7eebfeb109915b0d9c1dbc4029c0fb1369d542261d1c> to blockchain, what = Attempting to add transaction that's already in the db (tx id 2359199)
2017-04-10 10:39:18.387 [P2P6]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:293     [89.252.28.26:18080 OUT] Sync data returned a new top block candidate: 1273817 -> 1285488 [Your node is 11671 blocks (16 days) behind]
SYNCHRONIZATION started
2017-04-10 10:39:49.765 [P2P8]  ERROR   blockchain      src/cryptonote_core/blockchain.cpp:3383 Error adding block with hash: <425995a3ae61578a2d9a7eebfeb109915b0d9c1dbc4029c0fb1369d542261d1c> to blockchain, what = Attempting to add transaction that's already in the db (tx id 2359199)


## moneromooo-monero | 2017-04-10T17:56:30+00:00
That's a bug that was caused by running 0.10.3. You should be able to fix by exporting the db, then reimporting it again (using monero-blockchain-export, remove lmdb directory, and monero-blockchain-import --verify 0).

The 50 minutes of nothing sounds really odd. Something, somewhere, seems to be going extremely slowly. What's happening while it spends these 50 minutes ? Run top, and look at the third line, where there is a line starting with "%Cpu(s)". Does it have a significant percentage in the "wa" column ? Do you have a hard disk (as opposed to SSD), and/or little RAM ?

## ElLamparto | 2017-04-11T13:40:55+00:00
I am sorry for not being precise.
During the 50 minutes I got more or less regularly "Sync data returned a new top block candidate: [...]", but never "Synced".

The machine is 100% ok . I will export/import blockchain to fix the DB and then retry to synchronize (with and without the bandwidth limit.).


## moneromooo-monero | 2017-04-12T18:36:10+00:00
If you're not getting the Synced message, then it means either:
- it's really, really slow
or:
- blocks are rejected

If you were using 0.10.3.0, it's likely it's put your db in a state which would cause the rejections (and export/import will fix it).

## moneromooo-monero | 2017-04-12T18:41:38+00:00
(though your logs did not show blocks being rejected before, so....)

## DJCrashdummy | 2017-04-16T12:27:15+00:00
i suffer a very similar (or the same) problem, except i **never used a other version than 0.10.3.1** before (for this try/machine/instance).

i just started `monerod` and after more than one or two days i noticed it will take more than hundred days to catch up, so i looked a little bit around and dove a little bit deeper into the monero-topic... since i "had enough time". :-/
i found a tutorial to ["speed up initial blockchain sync"](https://www.monero.how/tutorial-how-to-speed-up-initial-blockchain-sync), so i thought the slow initial syncing is normal (just wondered why it is not mentioned at the official site) and imported the `blockchain.raw`.
after some fiddling around it was done, the import ended successful and i started `monerod` again. but nothing happened, just the mentioned `Sync data returned a new top block candidate:...` and counts up the number of blocks (and days) i'm behind!
after a lot of more reading, to be on the "safe" side i forwarded port 18080 and 18081, tried limits and a bunch of other things (removed `p2pstate.bin` or everything except `data.mdb`), but nothing changed.

so i removed `.bitmonero` completely, started from scratch and it works/syncs again.
**BUT** i guess it gets slower and slower: `Synced`-messages gets less and less and `Sync data returned a new top block candidate:...` increases.
and when i try to extrapolate the required time to finish with the metrics of the `status`-command _(for sure i added the uptimes)_ my impressions got verified: at the beginning it would take approximate 7 to 9 hours, but after more than 3 hours and 5% (70000 blocks) it increased continuous to more than 50 hours to finish.

_btw: i'm running this on a headless raspberry pi 2, so may this be a cause? - but i never read, it is not possible to run a node on a rapberry, so i thought i'll give it a shot._

## DJCrashdummy | 2017-04-16T12:30:36+00:00
btw: regarding `monero-blockchain-import`... what is to expect from `--batch-size <arg>`?
there is no description in the `--help` and it seems to be faster, the higher it is (with more ram used).

## moneromooo-monero | 2017-04-16T12:47:03+00:00
18081 is the RPC port, you typically don't want it public. P2P only needs 18080 open.

50 hours on a raspberry pi doesn't seem outrageous to me.

--batch-size N is the number of blocks after which LMDB will sync, and this is a slow operation. As you found, increasing it speeds up at the cost of RAM. If you increase past usable RAM, it'll slow down again.

Early blocks are faster because there's very little activity on those, so most are empty.


## DJCrashdummy | 2017-04-16T13:44:23+00:00
> 18081 is the RPC port, you typically don't want it public. P2P only needs 18080 open.

i know, i just wanted to point out i've done everything possible and impossible i can think of...

> 50 hours on a raspberry pi doesn't seem outrageous to me.

ok, but it increases continuous (after 4 hours and 6,2% at block ~80000 it increased to 65 hours). and as mentioned, at the first attempt after one day it rose to ~140 **days** = 3360 hours!
--> i hope you don't want to tell me that syncing nearly half a year is (although on a raspberry pi) usual?!?

> --batch-size N is the number of blocks after which LMDB will sync, and this is a slow operation. As you found, increasing it speeds up at the cost of RAM. If you increase past usable RAM, it'll slow down again.

@moneromooo-monero: thank you for the info and clarification.

## moneromooo-monero | 2017-04-16T14:54:13+00:00
Well, you might be better off syncing elsewhere and copying the database to the raspberry pi. I don't really have a good idea of how much time it takes, hyc should know.

## hyc | 2017-04-16T18:13:29+00:00
I haven't run my pi on mainnet in several months. The last time I used it was only on testnet. If I get a chance I'll put together a current binary and see how it goes.

## ElLamparto | 2017-04-17T16:36:24+00:00
hyc, full monero node on the pi?? On the pi you can run btc/ltc.
It seems to me that the minimum requirements for monero are:
1. A helium-cooled supercomputer,
2. A fast data storage center,
3. A double fiberglass Internet connection,
4. A lot o luck.

Seriously I exported/imported the DB and the import took nearly 2 days! With the source/destination on two physical drives.

Whatever was being done, with the raw file of 7GB it should not have taken more than 10-15min. Bad DB design and/or bad SQL queries - I do not see other explanation.

Finally monerod started synchronizing - slooooowly (but I had some 'synced' messages at last).

Those issues should be resolved, especially if someone is dreaming of i2p....

## fluffypony | 2017-04-17T17:09:34+00:00
@ElLamparto I'm running it just fine on a Raspberry Pi 3, several other ARM devices, and an Intel Atom.

We don't use SQL, so there are no "bad SQL queries". What you are definitely seeing is the result of the verification that occurs when you're importing the raw blockchain. This is not only CPU intensive, but it also requires hitting various indices to check, for instance, if a key image has already been used. This is naturally slow on a Raspberry Pi, but 2 days to import and FULLY validate 3 years of blockchain history is really not bad.

You can run the import with ```--verify 0``` next time, which skips the verification step.

## ElLamparto | 2017-04-18T10:28:18+00:00
@fluffypony , I used Intel Core 4 with -verify 0, and a SSD disc for the raw and a HD for the DB. And it took nearly 2 days. The CPU usage was < 1% and the memory usage < 300MB.

Anyway it is syncing now and if I am lucky enough to get to 100%, I will make a backup of the DB and put two armed guards next to it (so no more the export/import horror). And I will close this ticket.

@moneromooo-monero, it seems that the reason for not syncing was a corrupted database. Thank you very much for your analysis and help.

General remark: imho the synchronization process should be improved. It is very slow, it stops unexpectedly for eg. 2 hours, then it resumes...  (once it is at 100%, it works fine).

## fluffypony | 2017-04-18T11:21:31+00:00
@ElLamparto given that your memory and CPU wasn't taking a beating, the issue is definitely disk related. Here's a video of me doing an export / delete / import (with verify 0) on a modern SSD: http://sendvid.com/ou1y3slj

Export start: Tue Apr 18 12:34:39 SAST 2017
Export end:   Tue Apr 18 12:43:07 SAST 2017
**Total export time: 8 mins, 28 secs**

Import start: Tue Apr 18 12:43:32 SAST 2017
Import end:   Tue Apr 18 12:56:30 SAST 2017
**Total import time: 12 mins, 58 seconds**

## ElLamparto | 2017-04-19T09:33:20+00:00
Slowly but painlessly I arrived at 100%. It is holding.

## ElLamparto | 2017-05-09T08:17:54+00:00
Yes, monerod worked correctly for the past 20 days. There were a couple of reboots due to the OS security updates -> no problem.

Yesterday I had some maintenance work and I took monerod offline for about 6 hours (save + exit).
After restart, monerod does not sync any more (again!). Checked with the client: 0 blocks within last 10 hours.

As it worked fine within the last 20 days (including restarts) , it is not a problem of the machine, neither Internet connection. There must be a nasty bug in monerod....

What now?





## ElLamparto | 2017-05-13T08:12:08+00:00
UPDATE: monerod started syncing, 200-400 blocks a day.
However after restart with --block-sync-size 20, it synced quickly up to 100%.

I leave this ticket open, since in my opinion, it should work out of the box without any special parameters.

## glv2 | 2017-06-01T12:24:52+00:00
I just encountered a similar issue twice in the last two weeks (with monerod 0.10.3.1 on GNU/Linux x86-64). It seems to happen when there is a series of big blocks in the chain.

I started the daemon which had the chain up to block 1322222. The daemon indicated that the current block height was 1322850. The daemon printed regularly the message indicating that there was a new top block, but the sync process did not progress any more.

I let the daemon work for two hours, it downloaded something like 2 GB of data, but the sync process was still at block 1322222.

Restarting the daemon with the default *block-sync-size* (200) lead to the same result.
But when restarting the daemon with a lower *block-sync-size* (20), the sync process started working again, and within 30 minutes synchronized up to block 1322916 (top block at the time).


## glv2 | 2017-06-02T09:02:13+00:00
I think the problem comes from the default 2 minutes timeout for requests to peers (```P2P_DEFAULT_INVOKE_TIMEOUT```). When synchronising, if a request to get *block-sync-size* missing blocks needs more than 2 minutes (because of a small bandwidth and big blocks), the request will get killed by the timeout every time and the sync process enters in an infinite loop:

 1 - connect to a peer (```COMMAND_HANDSHAKE```)
 2 - request info on the peer's chain (```NOTIFY_REQUEST_CHAIN```)
 3 - request *block-sync-size* blocks (```NOTIFY_REQUEST_GET_OBJECTS```)
 4 - request killed by timeout after 2 minutes (```COMMAND_TIMED_SYNC invoke failed```)
 5 - drop connection to peer (```CLOSE CONNECTION```)
 6 - back to step 1

For example, a request to get 200 blocks of 300 kB each with an internet connection having a maximum download capacity lesser than 500 kB/s will never work, because it can't get the 60 MB in less than 2 minutes.

The issue can be reproduced by starting the daemon with a low *limit-rate-down* parameter.
The obvious workaround is to start the daemon with a *block-sync-size* parameter smaller than the 200 default value.

Maybe there would be a way to specify a different request timeout when sending the ```NOTIFY_REQUEST_GET_OBJECTS``` request in the ```request_missing_object``` function...

## moneromooo-monero | 2017-06-04T11:34:52+00:00
Thanks, that's an interesting finding.

## hyc | 2017-06-04T22:03:06+00:00
The patch in PR #2073 should fix this. But it's only lightly tested, please review and feedback.

## moneromooo-monero | 2017-08-09T10:13:25+00:00
+resolved

## ElLamparto | 2017-08-09T19:36:22+00:00
For the record: The synchro is still inefficient. I had to shut down monerod for 7 days and after 'uptime 1d 8h 37m 40s', 'Your node is 246 blocks (0 days) behind'.

## moneromooo-monero | 2017-08-15T12:17:25+00:00
Try current master, which is much friendlier to network capacity, which I believe is your bottleneck if you're stil using aggressive throttling.

## Satlinker | 2017-09-05T17:24:37+00:00
Similar problem: only "new block candidates" are reported and 10201 blocks behind. Next message 10202 blocks behind etc. But if I restart monerod, then it's suddenly 9960 blocks behind. So the sync works slowly without correct reporting.
I ran netstat to check the ports and get always a close_wait status. Could that be a problem?
 Proto  Lokale Adresse         Remoteadresse          Status
 TCP    192.168.178.25:52467   i19-les02-ntr-176-186-167-11:18080  HERGESTELLT
 TCP    192.168.178.25:54861   c-69-181-119-183:18080  SCHLIESSEN_WARTEN
 TCP    192.168.178.25:61120   201-79-171-100:18080   HERGESTELLT
 TCP    192.168.178.25:61308   92-75-15-51:18080      HERGESTELLT

Error messages in log_level 1:
2017-09-06 10:07:37.101 [P2P7]  ERROR   net.p2p src/p2p/net_node.inl:819        [82.36.142.104:18080 OUT] COMMAND_TIMED_SYNC invoke failed. (-3, LEVIN_ERROR_CONNECTION_DESTROYED)2017-09-06 10:08:09.819 [P2P3]  ERROR   net.p2p src/p2p/net_node.inl:819        [179.157.60.200:18080 OUT] COMMAND_TIMED_SYNC invoke failed. (-4, LEVIN_ERROR_CONNECTION_TIMEDOUT)
2017-09-06 10:08:09.819 [P2P7]  ERROR   net.p2p src/p2p/net_node.inl:819        [94.23.4.63:18080 OUT] COMMAND_TIMED_SYNC invoke failed. (-4, LEVIN_ERROR_CONNECTION_TIMEDOUT)
2017-09-06 10:09:36.085 [P2P3]  ERROR   net.p2p src/p2p/net_node.inl:819        [179.157.60.200:18080 OUT] COMMAND_TIMED_SYNC invoke failed. (-3, LEVIN_ERROR_CONNECTION_DESTROYED)
2017-09-06 10:11:18.259 [P2P3]  ERROR   net.p2p src/p2p/net_node.inl:819        [46.4.120.155:8180 OUT] COMMAND_TIMED_SYNC invoke failed. (-4, LEVIN_ERROR_CONNECTION_TIMEDOUT)
2017-09-06 10:11:18.259 [P2P1]  ERROR   net.p2p src/p2p/net_node.inl:819        [188.68.58.97:18080 OUT] COMMAND_TIMED_SYNC invoke failed. (-4, LEVIN_ERROR_CONNECTION_TIMEDOUT)
2017-09-06 10:11:18.259 [P2P0]  ERROR   net.p2p src/p2p/net_node.inl:819        [188.32.190.182:18080 OUT] COMMAND_TIMED_SYNC invoke failed. (-4, LEVIN_ERROR_CONNECTION_TIMEDOUT)
2017-09-06 10:11:18.259 [P2P6]  ERROR   net.p2p src/p2p/net_node.inl:819        [90.120.78.16:18080 OUT] COMMAND_TIMED_SYNC invoke failed. (-4, LEVIN_ERROR_CONNECTION_TIMEDOUT)
2017-09-06 10:11:18.259 [P2P5]  ERROR   net.p2p src/p2p/net_node.inl:819        [78.46.223.90:18080 OUT] COMMAND_TIMED_SYNC invoke failed. (-4, LEVIN_ERROR_CONNECTION_TIMEDOUT)
2

I use monerod and the gui version on the same database, but not to the same time.


## Satlinker | 2017-09-09T08:22:18+00:00
It's definately a problem of the internet connection, because it works on another WLAN.

## relativecoder | 2017-09-28T02:53:08+00:00
I had a similar issue and doing the export then import and restarting the daemon appears to have fixed it for me.  I previously tried deleting the chain and restarting but it would get stuck around 90% complete.

One thing for others to note the commands to do this are run through the command line and if your data dir isn't in the default place like mine you do need to specify it such as

\monero-blockchain-export.exe --data-dir YOUR_PATH_HERE
\monero-blockchain-import.exe --data-dir YOUR_PATH_HERE verify 0

# Action History
- Created by: ElLamparto | 2017-04-01T07:00:24+00:00
- Closed at: 2017-08-09T10:24:13+00:00
