---
title: Rejected Shares for RandomX - Intel Xeon Phi 7220P
source_url: https://github.com/xmrig/xmrig/issues/1164
author: Josevora
assignees: []
labels: []
created_at: '2019-09-05T13:19:13+00:00'
updated_at: '2021-05-12T23:00:06+00:00'
type: issue
status: closed
closed_at: '2019-10-15T20:10:10+00:00'
---

# Original Description
I'm having constant Rejects with my Intel Phis...
Other Algos run normally.

Same config file (except for number of cores) runs on different system.

x86_64 based CoCPU, binary from repo (xmrig-3.1.0-xenial-x64.tar.gz)

didn't try cross compiling yet, will try today.

What other infos you need to help me out on this?

Thank you.

# Discussion History
## xmrig | 2019-09-05T14:08:23+00:00
Please show miner output from beginning.
Thank you.

## Josevora | 2019-09-05T22:12:58+00:00
I had to disassemble the Rig, will buy new parts tomorrow and assemble again.

## Josevora | 2019-09-07T22:22:27+00:00
```
root@mic0:/home/Mining/xmrig# ./xmrig-notls
 * ABOUT        XMRig/3.1.1 gcc/5.4.0
 * LIBS         libuv/1.31.0 hwloc/2.0.4
 * CPU          Intel(R) Xeon Phi(TM) CoCPU 7220 @ 1.20GHz (1) x64 AES
                L2:34.0 MB L3:0.0 MB 68C/272T NUMA:1
 * DONATE       5%
 * ASSEMBLY     intel
 * POOL #1      wow.majanetwork.com:7070 algo rx/wow
 * POOL #2      loki.majanetwork.com:6667 algo rx/loki
 * POOL #3      xtnc.majanetwork.com:4646 algo cn-pico
 * POOL #4      xmr.majanetwork.com:4111 algo cn/r
 * COMMANDS     hashrate, pause, resume
[2019-09-07 22:17:42.383] use pool wow.majanetwork.com:7070  202.179.136.175
[2019-09-07 22:17:42.384] new job from wow.majanetwork.com:7070 diff 25000 algo rx/wow
[2019-09-07 22:17:42.384]  rx   init dataset algo rx/wow (272 threads) seed ecea85471e74cb85...
[2019-09-07 22:17:42.384]  cpu  use profile  rx/wow  (272 threads) scratchpad 1024 KB
[2019-09-07 22:17:42.384]  rx   #0 allocate 2336 MB (2080+256) for RandomX dataset & cache
[2019-09-07 22:17:42.744]  rx   #0 allocate done huge pages 1168/1168 100% +JIT (360 ms)
[2019-09-07 22:17:43.010]  cpu  READY threads 272(272) huge pages 272/272 100% memory 278528 KB (626 ms)
[2019-09-07 22:17:48.292]  rx   #0 init done (5908 ms)
[2019-09-07 22:17:50.165] rejected (0/1) diff 25000 "Rejected share: invalid result" (1626 ms)
[2019-09-07 22:17:52.266] rejected (0/2) diff 25000 "Rejected share: invalid result" (247 ms)
[2019-09-07 22:17:53.355] rejected (0/3) diff 25000 "Rejected share: invalid result" (246 ms)
[2019-09-07 22:18:01.985] rejected (0/4) diff 25000 "Rejected share: invalid result" (246 ms)
[2019-09-07 22:18:02.588] speed 10s/60s/15m 7012.8 n/a n/a H/s max 7012.8 H/s
[2019-09-07 22:18:02.850] rejected (0/5) diff 25000 "Rejected share: invalid result" (246 ms)
[2019-09-07 22:18:05.935] rejected (0/6) diff 25000 "Rejected share: invalid result" (246 ms)
[2019-09-07 22:18:06.150] rejected (0/7) diff 25000 "Rejected share: invalid result" (251 ms)
[2019-09-07 22:18:09.588] rejected (0/8) diff 25000 "Rejected share: invalid result" (247 ms)
[2019-09-07 22:18:14.708] Ctrl+C received, exiting
[2019-09-07 22:18:14.777]  cpu  stopped (68 ms)
root@mic0:/home/Mining/xmrig#`
```

## Josevora | 2019-09-07T22:28:01+00:00
rx/loki doesn't even start:
```

root@mic0:/home/Mining/xmrig# ./xmrig-notls
 * ABOUT        XMRig/3.1.1 gcc/5.4.0
 * LIBS         libuv/1.31.0 hwloc/2.0.4
 * CPU          Intel(R) Xeon Phi(TM) CoCPU 7220 @ 1.20GHz (1) x64 AES
                L2:34.0 MB L3:0.0 MB 68C/272T NUMA:1
 * DONATE       5%
 * ASSEMBLY     intel
 * POOL #1      wow.majanetwork.com:7070 algo rx/wow
 * POOL #2      loki.majanetwork.com:6667 algo rx/loki
 * POOL #3      xtnc.majanetwork.com:4646 algo cn-pico
 * POOL #4      xmr.majanetwork.com:4111 algo cn/r
 * COMMANDS     hashrate, pause, resume
[2019-09-07 22:27:01.783] Ctrl+C received, exiting
[2019-09-07 22:27:01.783]  cpu  stopped (0 ms)
root@mic0:/home/Mining/xmrig#

```

## Josevora | 2019-09-07T22:32:46+00:00
cn-pico is OK:

```
root@mic0:/home/Mining/xmrig# ./xmrig-notls
 * ABOUT        XMRig/3.1.1 gcc/5.4.0
 * LIBS         libuv/1.31.0 hwloc/2.0.4
 * CPU          Intel(R) Xeon Phi(TM) CoCPU 7220 @ 1.20GHz (1) x64 AES
                L2:34.0 MB L3:0.0 MB 68C/272T NUMA:1
 * DONATE       5%
 * ASSEMBLY     intel
 * POOL #1      wow.majanetwork.com:7070 algo rx/wow
 * POOL #2      loki.majanetwork.com:6667 algo rx/loki
 * POOL #3      xtnc.majanetwork.com:4646 algo cn-pico
 * POOL #4      xmr.majanetwork.com:4111 algo cn/r
 * COMMANDS     hashrate, pause, resume
[2019-09-07 22:31:39.773] use pool xtnc.majanetwork.com:4646  202.179.136.175
[2019-09-07 22:31:39.774] new job from xtnc.majanetwork.com:4646 diff 100001 algo cn-pico
[2019-09-07 22:31:39.774]  cpu  use profile  cn-pico  (272 threads) scratchpad 256 KB
[2019-09-07 22:31:40.050]  cpu  READY threads 272(272) huge pages 272/272 100% memory 69632 KB (276 ms)
[2019-09-07 22:31:55.829] accepted (1/0) diff 100001 (221 ms)
[2019-09-07 22:31:58.518] new job from xtnc.majanetwork.com:4646 diff 160003 algo cn-pico
[2019-09-07 22:31:59.851] speed 10s/60s/15m 15623.8 n/a n/a H/s max 15624.9 H/s
[2019-09-07 22:32:05.123] accepted (2/0) diff 160003 (219 ms)
[2019-09-07 22:32:10.377] accepted (3/0) diff 160003 (216 ms)
[2019-09-07 22:32:11.072] accepted (4/0) diff 160003 (216 ms)
[2019-09-07 22:32:15.869] accepted (5/0) diff 160003 (216 ms)
[2019-09-07 22:32:19.043] accepted (6/0) diff 160003 (216 ms)
[2019-09-07 22:32:19.935] speed 10s/60s/15m 15625.6 n/a n/a H/s max 15626.5 H/s
[2019-09-07 22:32:23.216] Ctrl+C received, exiting
[2019-09-07 22:32:23.277]  cpu  stopped (59 ms)
root@mic0:/home/Mining/xmrig#
```

## Josevora | 2019-09-07T22:39:26+00:00
cn/r is also OK:

```
root@mic0:/home/Mining/xmrig# ./xmrig-notls
 * ABOUT        XMRig/3.1.1 gcc/5.4.0
 * LIBS         libuv/1.31.0 hwloc/2.0.4
 * CPU          Intel(R) Xeon Phi(TM) CoCPU 7220 @ 1.20GHz (1) x64 AES
                L2:34.0 MB L3:0.0 MB 68C/272T NUMA:1
 * DONATE       5%
 * ASSEMBLY     intel
 * POOL #1      wow.majanetwork.com:7070 algo rx/wow
 * POOL #2      loki.majanetwork.com:6667 algo rx/loki
 * POOL #3      xtnc.majanetwork.com:4646 algo cn-pico
 * POOL #4      xmr.majanetwork.com:4111 algo cn/r
 * COMMANDS     hashrate, pause, resume
[2019-09-07 22:36:05.735] use pool xmr.majanetwork.com:4111  202.179.136.175
[2019-09-07 22:36:05.735] new job from xmr.majanetwork.com:4111 diff 25000 algo cn/r height 1918173
[2019-09-07 22:36:05.736]  cpu  use profile  cn  (272 threads) scratchpad 2048 KB
[2019-09-07 22:36:15.264]  cpu  READY threads 272(272) huge pages 272/272 100% memory 557056 KB (9528 ms)
[2019-09-07 22:36:25.778] speed 10s/60s/15m 953.9 n/a n/a H/s max 953.9 H/s
[2019-09-07 22:36:27.244] new job from xmr.majanetwork.com:4111 diff 25000 algo cn/r height 1918174
[2019-09-07 22:36:33.353] accepted (1/0) diff 25000 (243 ms)
[2019-09-07 22:36:45.848] speed 10s/60s/15m 952.8 n/a n/a H/s max 953.9 H/s
[2019-09-07 22:36:48.233] new job from xmr.majanetwork.com:4111 diff 50000 algo cn/r height 1918174
[2019-09-07 22:37:05.926] speed 10s/60s/15m 952.9 n/a n/a H/s max 953.9 H/s
[2019-09-07 22:37:26.038] speed 10s/60s/15m 952.8 952.8 n/a H/s max 953.9 H/s
[2019-09-07 22:37:38.695] new job from xmr.majanetwork.com:4111 diff 50000 algo cn/r height 1918175
[2019-09-07 22:37:46.170] speed 10s/60s/15m 951.8 952.7 n/a H/s max 953.9 H/s
[2019-09-07 22:38:03.130] accepted (2/0) diff 50000 (242 ms)
[2019-09-07 22:38:06.294] speed 10s/60s/15m 951.5 952.2 n/a H/s max 953.9 H/s
[2019-09-07 22:38:18.238] new job from xmr.majanetwork.com:4111 diff 33333 algo cn/r height 1918175
[2019-09-07 22:38:26.412] speed 10s/60s/15m 951.5 951.8 n/a H/s max 953.9 H/s
[2019-09-07 22:38:41.466] Ctrl+C received, exiting
[2019-09-07 22:38:41.734]  cpu  stopped (266 ms)
root@mic0:/home/Mining/xmrig#

```

## Josevora | 2019-09-07T22:44:58+00:00
btw i know i'm using all 272 Threads, I Know i should be using only the cores calculated by "Cache/Scrachpad", but I don't know why I'm getting more Hashrate using all all the way!

There's room for a lot of optimizations, but i don't think it'll be worth it for you, but it is for me. So I'm going to try simple things first, I'll compile it FOR the Phi, and then try to mess with the code!

## SChernykh | 2019-09-08T13:37:24+00:00
@Josevora Can you try to run RandomX benchmark: https://github.com/tevador/RandomX/releases and see if it outputs correct result with this command line:
```
./randomx-benchmark --mine --jit --largePages --init 272 --threads 272 --nonces 1000
```

## Josevora | 2019-09-09T01:33:42+00:00
Hello again,

I've managed to make it work. Thank you!

For future reference and to help others, this is how o did it:

I Had to define a value for init, here:

```
"randomx": {
        "init": 16,
        "numa": true
    },
```
instead of the auto value `-1` that comes with it... (I've used `16`)

After that, it ran smoothly!

Just a question and you may close this:
Do you think it's possible to get more hashrate on this?, since LukMiner was pulling +2000H from the original CN algo?  
(speculating) 2000H/s on CN would translate to ~1800H on CN/r , that times ~8 for RandomX = ~14400H/s

## SChernykh | 2019-09-09T06:19:09+00:00
It should be fixed in https://github.com/xmrig/xmrig/pull/1166
As for hashrate, RandomX is not Cryptonight, your Xeon Phi is probably limited by the amount of computations per core.

## sammy007 | 2019-10-15T19:52:13+00:00
@Josevora, just curious what hashrate you anaged to achieve?

## Josevora | 2019-10-15T20:09:07+00:00
~7000H/s...
It's a fine number, but South of what I was expecting... Still have the Phi tho... So I may try something later and share if worth it.

## Aprrentice | 2020-01-12T10:32:29+00:00
> I'm having constant Rejects with my Intel Phis...
> Other Algos run normally.
> 
> Same config file (except for number of cores) runs on different system.
> 
> x86_64 based CoCPU, binary from repo (xmrig-3.1.0-xenial-x64.tar.gz)
> 
> didn't try cross compiling yet, will try today.
> 
> What other infos you need to help me out on this?
> 
> Thank you.

Hello.

I hope you can help me here.
I have 4 x100 Phi card on Windows.
How can I use  those cards with XMRIG? Please note that I simply config the config fil and launch the application, am not a coder but have good computer knowledge.
thanks

## ps2chiper | 2021-05-12T23:00:06+00:00
I hope they update this thread with support for the x100 series of cards. 

# Action History
- Created by: Josevora | 2019-09-05T13:19:13+00:00
- Closed at: 2019-10-15T20:10:10+00:00
