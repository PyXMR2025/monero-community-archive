---
title: daemon gets wedged during initial sync
source_url: https://github.com/monero-project/monero/issues/1443
author: cardoe
assignees: []
labels: []
created_at: '2016-12-13T05:09:36+00:00'
updated_at: '2018-01-04T13:52:14+00:00'
type: issue
status: closed
closed_at: '2017-09-29T22:06:20+00:00'
---

# Original Description
The monerod daemon will stop receiving new blocks and happily report it is still synchronizing but never change the height for hours. A simple restart of the daemon will get it going again for a few thousand blocks before the issue crops up again. I've provided logs to @moneromooo-monero. I was using v0.10.0 on Linux and on Mac OSX. I've got a 1gb link. The Linux machine has 16gb RAM on a HDD and the Mac has 8gb on a HDD. I've checked iostat and the daemon is generating hardly any I/O (in fact if I turn off the logging it doesn't generate any).

# Discussion History
## ghost | 2016-12-13T05:27:16+00:00
It might be helpful if you could paste some of your monerod log using https://paste.fedoraproject.org/, perhaps with log level at 2.

## cardoe | 2016-12-13T17:28:05+00:00
https://dev.gentoo.org/~cardoe/files/bitmonero.log

## ghost | 2016-12-13T21:52:02+00:00
@cardoe Afraid I don't have a definite answer for you, but would you mind upgrading to 0.10.1, deleting your blockchain directory and starting again? It's got fixes for threading, database stuff etc. 

Please report back either way.

## cardoe | 2016-12-15T04:46:26+00:00
Well been running 0.10.1 for over a day now. It hasn't gotten stuck entirely yet but its syncing very slowly. Its much faster to get the raw blockchain file and import it contrary to what the website says. The only oddity I've noticed is getting this from different runs of `monerod status`.
```
Height: 214555/1201605 (17.9%) on mainnet, not mining, net hash 23.13 MH/s, v1, up to date, 8+0 connections
```

Now wait ~30 minutes...
```
Height: 217995/235755 (92.5%) on mainnet, not mining, net hash 27.34 MH/s, v1, up to date, 8+0 connections
```

Another ~15 minutes...
```
Height: 219813/1201650 (18.3%) on mainnet, not mining, net hash 22.29 MH/s, v1, up to date, 8+0 connections
```

## ghost | 2016-12-15T05:27:28+00:00
And this is after deleting your database and starting over? How much free space does your disk drive have? What is your CPU/RAM utilization? Does your network have any particular issues or firewall policies, like with the port that the Monero program is using?

## ghost | 2016-12-15T11:32:04+00:00
@xmr-eric's quiestions are quite relevant. Your sync shouldn't be this slow.

## cardoe | 2016-12-15T16:14:09+00:00
Nothing super exciting from a CPU or memory usage standpoint. These are both sorted with the biggest consumer at the top, which is monerod.
```
  PID USER     PRI  NI  VIRT   RES   SHR S CPU% MEM%   TIME+  Command
70235 cardoe    46   0 3638M  573M     0 U  2.0  7.0  0:01.98 ./monerod --detach
```

As far as disk space goes, there's 134GB.
```
Filesystem      Size   Used  Avail Capacity iused      ifree %iused  Mounted on
/dev/disk0s2   465Gi  331Gi  134Gi    72% 2007061 4292960218    0%   /
```
This machine is directly connected to AT&T's crummy Pace Gateway that must be used for their gigabit service.

## cardoe | 2016-12-15T16:15:05+00:00
It should note that this is on a 2011 Mac Mini. 2.3ghz Core i5 with 8gb RAM.

## gituser | 2016-12-20T20:03:38+00:00
It seems I'm having the same issue, but on the testnet network.

monerod is syncing forever, stuck at 
`Height: 810170/860338 (94.2%) on testnet, not mining, net hash 323 H/s, v5, up to date, 7+0 connections`

i'm using latest version `v0.10.1` in VM with 4gb memory and plenty of diskspace and yes i've tried syncing from scratch.

the block count changes but very very slow (like 3-4 blocks per 15 minutes).

EDIT: it seems it has to do something with recent testnet fork(s). i'm no longer can use my old wallets. is there any way to restore them if i don't know the seed, but only password? 

if i try to run rescan_bc it hangs on ```[wallet]: rescan_bc
Starting refresh...
Height 809760 / 810179```

EDIT2: it seems the only way is to restore through wallet seed, but balance is now 0!

I hope this won't be the case for mainnet when this fork will occur.

## ghost | 2016-12-20T21:46:24+00:00
@gituser You got it. The testnet was forked at some point. You're on the correct fork AFAIK. My testnet height is currently 810200/860338. And yes, I lost all my testnet coins when the fork happened. Nothing a little testnet mining couldn't fix.

## ElLamparto | 2017-01-04T08:35:20+00:00
@cardoe, I had similar problem, fixed by setting band limits: --limit-rate-up 10 --limit-rate-down 500.

Now I am always at 100% and the daemon runs OK (except of random segfaults...).
Monerod does not like to be throttled by the connection max. bandwidth. Too low limits will not work either. A bit of fine tuning is required. 


## DJCrashdummy | 2017-04-16T12:47:19+00:00
i suffer the same issue with `monerod` 0.10.3.1 as mentioned here: https://github.com/monero-project/monero/issues/1947#issuecomment-294349121

this two issues seem related for me...

## moneromooo-monero | 2017-08-15T22:36:22+00:00
Lower download limits should not impair sync anymore with latest master.

## moneromooo-monero | 2017-09-20T21:10:18+00:00
Is anyone here sitll getting this with 0.11.0.0 ?  It's now preventing timeouts while still getting data.

## ElLamparto | 2017-09-21T17:57:35+00:00
With 0.11.0.0 I have no more problems.

## moneromooo-monero | 2017-09-29T22:00:32+00:00
Thanks. With that report and the change meant to fix it, I think it's safe to say it's now fixed.

+resolved

## xyzzy42 | 2018-01-03T10:09:05+00:00
limit **up** doesn't seem to be working for me with 0.11.0.0.  If set to a small value like 10, **downloading** effectively stops and monerod loses sync and just gets further behind.  Setting it back to a high value like 2000 will allow download to resume again.

## ElLamparto | 2018-01-03T19:19:52+00:00
I run it with -limit-rate-up 10 --limit-rate-down 50 --block-sync-size 20.
It works perfectly.

## xyzzy42 | 2018-01-04T13:52:14+00:00
Here's a log of what I see.  After having been synced, monerod can't keep up and gets two blocks behind:
```
2018-01-04 13:35:31.291 [P2P0]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:305     [172.73.254.4:35396 INC] Sync data returned a new top block candidate: 1479779 -> 1479781 [Your node is 2 blocks (0 days) behind]
SYNCHRONIZATION started
2018-01-04 13:36:03.982 [P2P1]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:305     [36.35.166.97:18080 OUT] Sync data returned a new top block candidate: 1479779 -> 1479781 [Your node is 2 blocks (0 days) behind]
SYNCHRONIZATION started
sync_info
Height: 1479779, target: 1479781 (99.9999%)
Downloading at 23 kB/s
10 peers
```
It's been over 30 seconds, just from those two log messages, and still 2 blocks behind.  While sync_info shows the download rate as 23 kB/s, actual traffic measurement has it at more like 2 to 3 kB/s.  Now I'll increase the limit_up:
```
limit_up 2000
Set limit-up to 2000 kB/s
2018-01-04 13:36:38.551 [P2P2]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154    [36.35.166.97:18080 OUT]  Synced 1479781/1479781
2018-01-04 13:36:38.564 [P2P2]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1521    SYNCHRONIZED OK
2018-01-04 13:36:39.777 [P2P3]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1521    SYNCHRONIZED OK
sync_info
Height: 1479781, target: 1479781 (100%)
Downloading at 321 kB/s
9 peers
```
It manages to sync within seconds of raising the upload limit.  The download speed has increased by a factor of ten.  Watching a traffic monitor, I see the download rate hit the limit of my link when the upload limit is raised.  It quickly syncs and then drops back down.


# Action History
- Created by: cardoe | 2016-12-13T05:09:36+00:00
- Closed at: 2017-09-29T22:06:20+00:00
