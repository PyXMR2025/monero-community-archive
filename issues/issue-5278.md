---
title: Very low hashrate in CLI/GUI miner
source_url: https://github.com/monero-project/monero/issues/5278
author: JustFranz
assignees: []
labels: []
created_at: '2019-03-13T11:44:13+00:00'
updated_at: '2020-05-17T14:47:49+00:00'
type: issue
status: closed
closed_at: '2020-05-17T14:47:49+00:00'
---

# Original Description
OS: Win 10
CPU 3770K stock clocks. It is a 4c 8t cpu with 8 MB cache.

1 thread - 11-14 H/s mostly stable at 14
2 threads 21-28 H/s mostly stable at 27-28
3 threads 32-41 H/s seems to be mostly at 38-39, but unstable
4 threads 37-44 H/s unstable in that range, mostly around 38-40 H/s, sometimes dips into mid and low 30s

With XMRig I get ~65 H/s per thread for a total of 260 H/s. There is no instability and hashes do not go down as I use more threads.

# Discussion History
## moneromooo-monero | 2019-03-13T12:11:23+00:00
Pool miners work a lot of speed, so they'll likely always be faster.

You can try these too:

#5252 
https://github.com/moneromooo-monero/bitmonero/commits/minerad2

The first one will speed up a bit. The second one might, let me know whether it does.
Also make sure you have the env var MONERO_USE_CNV4_JIT set to 1.
The second patch has a "auto" setting for number of threads, ie:
start_mining ADDRESS auto
It will try to find the best number of mining threads.

## JustFranz | 2019-03-13T13:14:49+00:00
Using MONERO_USE_CNV4_JIT = 1 improved it 2X but H/s is still 40-45% of XMRig and unstable.

1 thread 28-31 H/s seems to be mostly stable at 29-30 H/s
2 threads 54-58 H/s mostly at 57-58 H/s
3 threads 83-90 H/s unstable in that range with dips into low 70s
4 threads 99-107 H/s stableish in the 100-104 range with some dips into mid 90s and mid 80s
5 threads 87-92 H/s with dips into mid 70s
6 threads 80-87 H/s stableish at 86-87 H/s, saw dips to 30, mid 50s and 0 (flukes?) otherwise stableish
7 threads 84-88 H/s very stable 
8 threads 89-91 H/s very stable

The GUI detects the optimal threads correctly at 4, so this is not needed https://github.com/moneromooo-monero/bitmonero/commit/8298f42e9d9c4d81792d7ab344efbe424e9b9ba2

The stabilization as more cores/threads are loaded would indicate some scheduler/core pinning issue? So this should help? https://github.com/moneromooo-monero/bitmonero/commit/25eea61a030bc08f7e1d4b26349c01cde5ce3841

Or the individual threads bouncing around averages out the displayed H/s? I don't know.

I did not try #5252 or the 2 other changes, unless there is a binary with the changes implemented? I'd like to try it out to get to the bottom of this.

Why isn't MONERO_USE_CNV4_JIT = 1 set automatically? Manually adding environment variables that you need to find on the internet is so user unfriendly.

I'm going to do tests with XMRig to see if increasing threads will reduce performance of other threads or how it behaves.

## moneromooo-monero | 2019-03-13T13:17:11+00:00
It's not default because it might be buggy.

## JustFranz | 2019-03-13T15:24:02+00:00
XMRig 15 minute test
1 thread 77 H/s
2 threads 2x78 H/s
3 threads 3x 77 H/s
4 threads 4 x 65 H/s (3x77 = 231 4x65=260)

I'll edit post with 5 6 7 and 8 thread results

5 threads 
45 + 50 + 50 + 52 + 51 = 248 H/s

I won't continue with 6 7 8

Maybe there should be a notice in GUI and CLI that hashrates with dedicated mining software will be several times higher. I've seen newbies post abnormally low hashrates before. Maybe for some it would have been worth it to join a pool and idle mine with the CPU, got them more involved with Monero. 

Right now in my case the official miner with default settings is 6.5 x slower than an out of the box XMRig hashrate. Should the option to mine with GUI even be there with such a large difference?

Is there a way to see per thread hashrate in the cli /gui miner?

## moneromooo-monero | 2019-03-13T17:04:34+00:00
The difference used to be nowhere that large IIRC.

You want the option to mine with monerod, otherwise you're not really strengthening the network, the pool op is deciding whether you do.

Given the large gap in performance, it's worth looking at speeding it up I think.


## moneromooo-monero | 2020-05-17T14:47:49+00:00
Given we now use randomx, I'm going to close this. Reopen a new bug if you still have large performance gaps using randomx (say, 10%), which should not be the case.

# Action History
- Created by: JustFranz | 2019-03-13T11:44:13+00:00
- Closed at: 2020-05-17T14:47:49+00:00
