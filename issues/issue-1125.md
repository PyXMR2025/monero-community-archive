---
title: I use the same PC and same config to benchmark the new version
source_url: https://github.com/xmrig/xmrig/issues/1125
author: willwill85
assignees: []
labels:
- question
created_at: '2019-08-18T05:17:09+00:00'
updated_at: '2019-09-28T17:51:00+00:00'
type: issue
status: closed
closed_at: '2019-09-28T17:51:00+00:00'
---

# Original Description
I find 3.0 is 180H and 2.14 is 240H
So what is the different？


# Discussion History
## xmrig | 2019-08-18T06:54:12+00:00
Please provide full details including config file or command line and miner output, right now I can't help you. Also please note different algorithms has different hashrate.
Thank you.

## willwill85 | 2019-08-18T12:05:36+00:00
./xmrig-notls --print-time 20 --donate-level 1 --max-cpu-usage 99 --cpu-priority 3 -o xmr.f2pool.com:13531 -u 44CqdnqaQkmYo64r3W94JQBTEkGeVA5vs62VKsMVvv3TEF8hz2xC6BCGPN7mBRZvrj4qAnyQAJeQfK2nRpb1yLtWAphHzvS -p x -k

## xmrig | 2019-08-18T12:25:55+00:00
1. Hashrate is same, because in both cases you mine `cn/r` pool tell algorithm, so your local option `algo` has no effect, but miner show used algorithm for each job.
2. Please show miner output from both versions, I can't confirm performance difference with same settings.

## willwill85 | 2019-08-18T13:25:44+00:00
OK，I find use the same config，the thread number is different.
and for 2.14.4 version ,the cpu info is different.(3.0 is x64 AES,  2.14.4 is x64 AES AVX2)

### 3.0:
 * ABOUT        XMRig/3.0.0 gcc/5.4.0
 * LIBS         libuv/1.31.0 hwloc/2.0.4
 * CPU          Intel(R) Xeon(R) Platinum 8163 CPU @ 2.50GHz (1) **x64 AES**
                L2:4.0 MB L3:33.0 MB 4C/8T NUMA:1
 * DONATE       5%
 * ASSEMBLY     auto:intel
 * POOL #1      pool.minexmr.com:4444 algo cn/r
 * COMMANDS     hashrate, pause, resume
[2019-08-18 21:21:15.975] use pool pool.minexmr.com:4444  37.59.44.93
[2019-08-18 21:21:15.975] new job from pool.minexmr.com:4444 diff 15000 algo cn/r height 1903523
[2019-08-18 21:21:15.975]  cpu  use profile  cn  **(4 threads)** scratchpad 2048 KB
[2019-08-18 21:21:16.834]  cpu  READY threads 4(4) huge pages 0/4 0% memory 8192 KB (859 ms)
[2019-08-18 21:21:29.140] new job from pool.minexmr.com:4444 diff 15000 algo cn/r height 1903524
[2019-08-18 21:21:35.343] new job from pool.minexmr.com:4444 diff 15000 algo cn/r height 1903525
[2019-08-18 21:21:36.945] accepted (1/0) diff 15000 (327 ms)
[2019-08-18 21:22:16.013] speed 10s/60s/15m 180.6 n/a n/a H/s max 180.8 H/s


### 2.14.4:
 * ABOUT        XMRig/2.14.4 gcc/4.8.5
 * LIBS         libuv/1.30.1 microhttpd/0.9.33 
 * CPU          Intel(R) Xeon(R) Platinum 8163 CPU @ 2.50GHz (1) **x64 AES AVX2**
 * CPU L2/L3    4.0 MB/33.0 MB
 * THREADS      8, cryptonight/r, av=0, donate=5%
 * ASSEMBLY     auto:intel
 * POOL #1      pool.minexmr.com:4444 variant r
 * COMMANDS     hashrate, pause, resume
[2019-08-18 21:23:33] use pool pool.minexmr.com:4444  37.59.45.174 
[2019-08-18 21:23:33] new job from pool.minexmr.com:4444 diff 15000 algo cn/r height 1903526
[2019-08-18 21:23:34] READY (CPU) **threads 8(8**) huge pages 0/8 0% memory 16384 KB
[2019-08-18 21:24:22] accepted (1/0) diff 15000 (333 ms)
[2019-08-18 21:24:37] speed 10s/60s/15m 223.5 223.4 n/a H/s max 223.6 H/s



## xmrig | 2019-08-18T13:51:00+00:00
Okay you use a virtual machine, hwloc topology may inaccurate in this case, please run `./xmrig --export-topology` and attach `topology.xml` to this issue, it helps understand why autoconfig choice 4 threads instead of 8.

1. If you add option `-t 8` it should restore hashrate.
2. Information about AVX2 now hidden because most of algorithm not use it.

# Action History
- Created by: willwill85 | 2019-08-18T05:17:09+00:00
- Closed at: 2019-09-28T17:51:00+00:00
