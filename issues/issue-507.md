---
title: support haven coin
source_url: https://github.com/xmrig/xmrig/issues/507
author: Allin1920
assignees: []
labels: []
created_at: '2018-04-06T10:47:15+00:00'
updated_at: '2018-11-05T13:21:05+00:00'
type: issue
status: closed
closed_at: '2018-11-05T13:21:05+00:00'
---

# Original Description
You can support haven coin?
https://github.com/havenprotocol
This coin has updated the new POW
I very much hope you can support haven coin
Xmr-stak has been supported haven
but,i don't like xmr-stak.
I like xmrig more

# Discussion History
## tonyxjoseph | 2018-04-06T11:00:56+00:00
checked the beta version
hash rate went down from 400 to 100
will it be this slow ?

## Allin1920 | 2018-04-06T22:20:16+00:00
My CPU dropped from 250H to 80H 

## Allin1920 | 2018-04-06T22:20:44+00:00
 * VERSIONS:     XMRig/2.6.0-beta1 libuv/1.19.2 gcc/7.3.0
 * HUGE PAGES:   available, enabled
 * CPU:          Intel(R) Xeon(R) CPU E3-1231 v3 @ 3.40GHz (1) x64 AES-NI
 * CPU L2/L3:    1.0 MB/8.0 MB
 * THREADS:      4, cryptonight-heavy, av=1, donate=1%
 * POOL #1:      pool.sumokoin.com:3333
 * COMMANDS:     hashrate, pause, resume
[2018-04-07 06:18:15] use pool pool.sumokoin.com:3333 192.99.32.219
[2018-04-07 06:18:15] new job from pool.sumokoin.com:3333 diff 2000
[2018-04-07 06:18:23] speed 2.5s/60s/15m 80.3 n/a n/a H/s max: 80.5 H/s
[2018-04-07 06:18:55] accepted (1/0) diff 2000 (394 ms)
[2018-04-07 06:19:18] speed 2.5s/60s/15m 97.3 81.9 n/a H/s max: 85.6 H/s

## Allin1920 | 2018-04-06T22:23:10+00:00
@xmrig 
what is the cryptonight-heavy.
what 80H-100h? why?
This is not good for CPU miner
But my GPU rx470 660H

## xmrig | 2018-04-07T08:23:09+00:00
@Allin1920 You should run only 2 threads on your CPU hashrate will be better, each cryptonight-heavy thread required 4 MB of cache (instead of 2 MB) and right new algorithm designed to move balance on GPU side.
Thank you.

## PlasidoDomingo | 2018-04-13T13:41:35+00:00
yep my old home processor 2 core is faster on e5-2565L v4
can someone help me set the second processor
stands on the ubuntu system
my old core 2 is on xp and goes faster
on ubuntu e5-2565L v4
I did apt-get upgrade apt-get update
I entered sysctl -w vm.nr_hugepages = 128
  sudo apt-get install git libcurl4-openssl-dev build-essential libjansson-dev autotools-dev automake
here are the results
the strange thing is that when I mixed in config.json in windows xp and later I went back to the normal settings the mixing speed dropped from 22.5 h / s to 17-18 only what I changed was treads = 2
mixing speed without settings was 9.5 h / s
I changed treads = 2 and it was 22.5 h / s
later, I changed other things without growth just the opposite
I returned to the treads = 2 setting and I have 17.5 h / s, I know that this is a historic CPU and nothing else can be extracted from it
but the problem is this e5-2565L v4 which I would not change the power falls instead of growing
yes I read and studied the mass of pages I used different settings as others recommended but no result

VERSIONS: XMRig/2.6.0-beta2 libuv/1.15.0 gcc/7.2.0
HUGE PAGES: available, disabled
CPU: Intel(R) Pentium(R) Dual CPU E2160 @ 1.80GHz (1) -x64
I
CPU L2/L3: 1.0 MB/0.0 MB
THREADS: 2, cryptonight-lite, av=4, donate=5%
POOL #1: 118.31.18.78:3333
COMMANDS: hashrate, pause, resume
[2018-04-13 14:16:07] use pool 118.31.18.78:3333 118.31.18.78
[2018-04-13 14:16:07] new job from 118.31.18.78:3333 diff 2000
[2018-04-13 14:16:10] new job from 118.31.18.78:3333 diff 2000
[2018-04-13 14:16:22] new job from 118.31.18.78:3333 diff 1333
[2018-04-13 14:16:29] new job from 118.31.18.78:3333 diff 1333
[2018-04-13 14:16:46] new job from 118.31.18.78:3333 diff 1333
[2018-04-13 14:16:52] new job from 118.31.18.78:3333 diff 444
[2018-04-13 14:16:58] new job from 118.31.18.78:3333 diff 444
[2018-04-13 14:17:08] accepted (1/0) diff 444 (453 ms)
[2018-04-13 14:17:08] new job from 118.31.18.78:3333 diff 444
[2018-04-13 14:17:09] speed 2.5s/60s/15m n/a 16.9 n/a H/s max: 16.1 H/s
[2018-04-13 14:17:22] new job from 118.31.18.78:3333 diff 296
[2018-04-13 14:17:22] new job from 118.31.18.78:3333 diff 296
[2018-04-13 14:17:26] accepted (2/0) diff 296 (449 ms)
[2018-04-13 14:17:38] accepted (3/0) diff 296 (461 ms)
[2018-04-13 14:17:46] accepted (4/0) diff 296 (373 ms)
[2018-04-13 14:18:10] speed 2.5s/60s/15m n/a 15.1 n/a H/s max: 16.1 H/s
[2018-04-13 14:18:20] accepted (5/0) diff 296 (444 ms)
[2018-04-13 14:18:22] new job from 118.31.18.78:3333 diff 201
[2018-04-13 14:18:23] new job from 118.31.18.78:3333 diff 201
[2018-04-13 14:18:32] new job from 118.31.18.78:3333 diff 201
[2018-04-13 14:18:36] new job from 118.31.18.78:3333 diff 201
[2018-04-13 14:18:45] accepted (6/0) diff 201 (501 ms)
[2018-04-13 14:18:52] new job from 118.31.18.78:3333 diff 100
[2018-04-13 14:18:54] accepted (7/0) diff 100 (457 ms)
[2018-04-13 14:18:56] accepted (8/0) diff 100 (450 ms)
[2018-04-13 14:19:05] accepted (9/0) diff 100 (2264 ms)
[2018-04-13 14:19:05] accepted (10/0) diff 100 (2575 ms)
[2018-04-13 14:19:10] speed 2.5s/60s/15m n/a 15.8 n/a H/s max: 19.8 H/s
[2018-04-13 14:19:12] new job from 118.31.18.78:3333 diff 100
[2018-04-13 14:19:15] new job from 118.31.18.78:3333 diff 100
[2018-04-13 14:19:16] new job from 118.31.18.78:3333 diff 100
[2018-04-13 14:19:26] new job from 118.31.18.78:3333 diff 100
[2018-04-13 14:19:34] accepted (11/0) diff 100 (332 ms)
[2018-04-13 14:19:42] accepted (12/0) diff 100 (463 ms)
[2018-04-13 14:19:43] accepted (13/0) diff 100 (451 ms)
[2018-04-13 14:19:46] new job from 118.31.18.78:3333 diff 100
[2018-04-13 14:19:51] accepted (14/0) diff 100 (441 ms)
[2018-04-13 14:19:52] accepted (15/0) diff 100 (440 ms)
[2018-04-13 14:19:52] accepted (16/0) diff 100 (887 ms)
[2018-04-13 14:19:53] new job from 118.31.18.78:3333 diff 149
[2018-04-13 14:19:59] accepted (17/0) diff 149 (498 ms)
[2018-04-13 14:20:01] new job from 118.31.18.78:3333 diff 149
[2018-04-13 14:20:04] accepted (18/0) diff 149 (465 ms)
[2018-04-13 14:20:07] accepted (19/0) diff 149 (439 ms)
[2018-04-13 14:20:10] speed 2.5s/60s/15m n/a 14.6 n/a H/s max: 19.8 H/s
[2018-04-13 14:20:12] new job from 118.31.18.78:3333 diff 149
[2018-04-13 14:20:24] accepted (20/0) diff 149 (437 ms)
[2018-04-13 14:20:28] new job from 118.31.18.78:3333 diff 149
[2018-04-13 14:20:33] accepted (21/0) diff 149 (1350 ms)
[2018-04-13 14:20:42] accepted (22/0) diff 149 (2467 ms)
[2018-04-13 14:20:51] accepted (23/0) diff 149 (431 ms)
[2018-04-13 14:21:10] speed 2.5s/60s/15m n/a 16.4 n/a H/s max: 19.8 H/s
[2018-04-13 14:21:14] accepted (24/0) diff 149 (443 ms)
[2018-04-13 14:21:17] accepted (25/0) diff 149 (428 ms)
[2018-04-13 14:21:19] accepted (26/0) diff 149 (433 ms)
[2018-04-13 14:21:25] accepted (27/0) diff 149 (457 ms)
[2018-04-13 14:21:36] accepted (28/0) diff 149 (420 ms)
[2018-04-13 14:21:36] accepted (29/0) diff 149 (800 ms)
[2018-04-13 14:21:39] accepted (30/0) diff 149 (452 ms)
[2018-04-13 14:21:40] accepted (31/0) diff 149 (688 ms)
[2018-04-13 14:21:41] new job from 118.31.18.78:3333 diff 149
[2018-04-13 14:21:42] accepted (32/0) diff 149 (419 ms)
XMRig/2.6.0-beta2 libuv/1.19.2 gcc/5.4.0
HUGE PAGES: available, enabled
CPU: Intel(R) Xeon(R) CPU E5-2650L v4 @ 1.70GHz (1) x64 AES-NI
CPU L2/L3: 0.2 MB/35.0 MB
THREADS: 1, cryptonight-lite, av=2, donate=5%, affinity=0x1
POOL #1: 118.31.18.78:3333
COMMANDS: hashrate, pause, resume
[2018-04-13 14:01:25] use pool 118.31.18.78:3333 118.31.18.78
[2018-04-13 14:01:25] new job from 118.31.18.78:3333 diff 2000
[2018-04-13 14:01:29] new job from 118.31.18.78:3333 diff 2000
[2018-04-13 14:01:32] new job from 118.31.18.78:3333 diff 2000
[2018-04-13 14:02:02] new job from 118.31.18.78:3333 diff 541
[2018-04-13 14:02:25] accepted (1/0) diff 541 (766 ms)
[2018-04-13 14:02:28] speed 2.5s/60s/15m 11.3 13.0 n/a H/s max: 17.4 H/s
[2018-04-13 14:02:32] new job from 118.31.18.78:3333 diff 246
[2018-04-13 14:02:37] new job from 118.31.18.78:3333 diff 246
[2018-04-13 14:02:46] new job from 118.31.18.78:3333 diff 246
[2018-04-13 14:03:02] new job from 118.31.18.78:3333 diff 100
[2018-04-13 14:03:15] accepted (2/0) diff 100 (290 ms)
[2018-04-13 14:03:16] new job from 118.31.18.78:3333 diff 100
[2018-04-13 14:03:28] new job from 118.31.18.78:3333 diff 100
[2018-04-13 14:03:28] speed 2.5s/60s/15m n/a 13.4 n/a H/s max: 17.6 H/s
[2018-04-13 14:03:39] accepted (3/0) diff 100 (769 ms)
[2018-04-13 14:03:40] new job from 118.31.18.78:3333 diff 100
[2018-04-13 14:03:49] accepted (4/0) diff 100 (312 ms)
[2018-04-13 14:03:50] accepted (5/0) diff 100 (815 ms)
[2018-04-13 14:04:04] accepted (6/0) diff 100 (303 ms)
[2018-04-13 14:04:13] new job from 118.31.18.78:3333 diff 100
[2018-04-13 14:04:18] accepted (7/0) diff 100 (325 ms)
[2018-04-13 14:04:20] new job from 118.31.18.78:3333 diff 100
[2018-04-13 14:04:21] accepted (8/0) diff 100 (798 ms)
[2018-04-13 14:04:29] speed 2.5s/60s/15m 18.4 13.2 n/a H/s max: 17.6 H/s
[2018-04-13 14:04:50] accepted (9/0) diff 100 (476 ms)
[2018-04-13 14:04:52] accepted (10/0) diff 100 (576 ms)
[2018-04-13 14:04:56] accepted (11/0) diff 100 (815 ms)
[2018-04-13 14:05:13] accepted (12/0) diff 100 (482 ms)
[2018-04-13 14:05:21] new job from 118.31.18.78:3333 diff 100
[2018-04-13 14:05:23] accepted (13/0) diff 100 (830 ms)
[2018-04-13 14:05:24] accepted (14/0) diff 100 (411 ms)
[2018-04-13 14:05:26] new job from 118.31.18.78:3333 diff 100
[2018-04-13 14:05:29] speed 2.5s/60s/15m 11.8 13.3 n/a H/s max: 17.6 H/s

# Action History
- Created by: Allin1920 | 2018-04-06T10:47:15+00:00
- Closed at: 2018-11-05T13:21:05+00:00
