---
title: Winx64,on HDD,cli 0.14.0.2,sync full local node very slow when after near 73%~75%,
  about 20 blocks per minute
source_url: https://github.com/monero-project/monero/issues/5587
author: x151973
assignees: []
labels: []
created_at: '2019-05-29T23:04:48+00:00'
updated_at: '2021-09-21T10:57:00+00:00'
type: issue
status: closed
closed_at: '2021-09-21T10:57:00+00:00'
---

# Original Description
`SYNCHRONIZATION started
2019-05-29 23:00:57.023 [P2P2]  INFO    global  src/cryptonote_protocol/cryptono
te_protocol_handler.inl:1179    [1;33m[95.216.204.211:59006 INC]  Synced 179780
3/1845566 (97% 47763 blocks remaining)[0m
2019-05-29 23:01:31.814 [P2P2]  INFO    global  src/cryptonote_protocol/cryptono
te_protocol_handler.inl:1179    [1;33m[95.216.204.211:59006 INC]  Synced 179782
3/1845566 (97% 47743 blocks remaining)[0m
2019-05-29 23:02:11.684 [P2P2]  INFO    global  src/cryptonote_protocol/cryptono
te_protocol_handler.inl:1179    [1;33m[95.216.204.211:59006 INC]  Synced 179784
3/1845566 (97% 47723 blocks remaining)[0m
`
This takes about 5days, is that normal on HDD, or faster on SSD?
Is there any option on cli I missed?

# Discussion History
## moneromooo-monero | 2019-05-29T23:12:28+00:00
HDD is pretty slow. 0.14.0.2 has old sync code though. It'll be faster with SSD, and it'll be faster with 0.14.1.0, which should be around already, so... soon. 20 blocks per minute is crazy slow though. Is the bottleneck CPU, I/O or otherwise ?

## x151973 | 2019-05-30T23:05:14+00:00
@moneromooo-monero WD ent HDD,AMD x945 3.0Mhz. After some googling there is few similar issues, condition var, but the "20 blocks" is common, will try new version when it done

## moneromooo-monero | 2019-06-15T11:00:03+00:00
0.14.1.0 is out now.
If it still happens, run top and paste what should be the third line from the top, the one with a "wa" field.
Better to paste a few instances of this, say, 10 seconds apart.


## x151973 | 2019-06-21T01:28:58+00:00
Updated new 0.14.1.0, function worked, but hard to say fast or slow.I'll spend another 70GB test it later.

## x151973 | 2019-06-21T11:13:01+00:00
After about 10 hours, issue replayed
```
2019-06-21 07:51:59.733 I [1;33mSynced 1220008/1861616 (65%, 641608 left)[0m
2019-06-21 07:52:00.883 I [1;33mSynced 1220108/1861616 (65%, 641508 left)[0m
2019-06-21 07:52:45.580 I [1;33mSynced 1220208/1861617 (65%, 641409 left)[0m
2019-06-21 07:52:46.339 I [1;33mSynced 1220308/1861617 (65%, 641309 left)[0m
2019-06-21 07:52:47.594 I [1;33mSynced 1220408/1861617 (65%, 641209 left)[0m
2019-06-21 07:52:48.142 I [1;33mSynced 1220508/1861617 (65%, 641109 left)[0m
2019-06-21 07:53:33.337 I [1;33mSynced 1220608/1861617 (65%, 641009 left)[0m
2019-06-21 07:53:35.986 I [1;33mSynced 1220708/1861617 (65%, 640909 left)[0m
2019-06-21 07:53:38.781 I [1;33mSynced 1220808/1861617 (65%, 640809 left)[0m
2019-06-21 07:53:44.184 I [1;33mSynced 1220908/1861617 (65%, 640709 left)[0m
2019-06-21 07:53:47.091 I [1;33mSynced 1221008/1861617 (65%, 640609 left)[0m
2019-06-21 07:54:02.110 I [193.148.16.219:56774 INC] Sync data returned a new to
p block candidate: 1221008 -> 1861618 [Your node is 640610 blocks (889 days) beh
ind]
SYNCHRONIZATION started
2019-06-21 07:54:03.641 I [1;33mSynced 1221028/1861618 (65%, 640590 left)[0m
2019-06-21 07:54:13.007 I [1;33mSynced 1221048/1861618 (65%, 640570 left)[0m
2019-06-21 07:54:27.103 I [1;33mSynced 1221068/1861618 (65%, 640550 left)[0m
2019-06-21 07:54:27.448 I [1;33mSynced 1221088/1861618 (65%, 640530 left)[0m
2019-06-21 07:54:37.338 I [1;33mSynced 1221108/1861618 (65%, 640510 left)[0m
2019-06-21 07:54:37.529 I [1;33mSynced 1221128/1861618 (65%, 640490 left)[0m
2019-06-21 07:54:37.738 I [1;33mSynced 1221148/1861618 (65%, 640470 left)[0m
2019-06-21 07:54:52.501 I [1;33mSynced 1221168/1861618 (65%, 640450 left)[0m
2019-06-21 07:54:52.716 I [1;33mSynced 1221188/1861618 (65%, 640430 left)[0m
2019-06-21 07:54:52.992 I [1;33mSynced 1221208/1861618 (65%, 640410 left)[0m
```
This time is at 65%, "20 blocks" issue begin.

## moneromooo-monero | 2019-06-21T16:09:00+00:00
Is the issue that one span of blocks took 45 seconds ? If so, it's probably that the daemon did not have those blocks yet, and was waiting to receive them. The download runs in parallel to the block addition. You can see what spans you have with "sync_info". There's a line betewen "[]" which displays which future blocks you have and which are still missing. The best case is when it start with "m" (matching height with what we need") followed by a lot of "o". The "." means the span has been requested, but not received yet. If you have a "." at the start, it means the daemon is waiting on the network.

## x151973 | 2019-06-21T20:45:03+00:00
Here is log [bitmonero.log](https://github.com/monero-project/monero/files/3315976/bitmonero.log)


## x151973 | 2021-09-21T10:57:00+00:00
Long time, after reading some docs, it seems this process is normal(sync from 0 first very fast, slower at almost complete)
`--fast-block-sync`
[https://monerodocs.org/interacting/monerod-reference/](url)

closed.

# Action History
- Created by: x151973 | 2019-05-29T23:04:48+00:00
- Closed at: 2021-09-21T10:57:00+00:00
