---
title: RandomX algorithm testing and benchmarking.
source_url: https://github.com/xmrig/xmrig/issues/1111
author: xmrig
assignees:
- xmrig
labels:
- META
created_at: '2019-08-10T12:29:58+00:00'
updated_at: '2019-09-28T17:43:07+00:00'
type: issue
status: closed
closed_at: '2019-09-28T17:43:07+00:00'
---

# Original Description
2 RandomX variants available for testing on real pools or daemons:

1. RandomXL (`rx/loki`) for Loki, most close to reference RandomX, but slower.
2. RandomWOW (`rx/wow`) for Wownero, faster, L2/L3 memory requirements reduced twice, used different threads settings.

If you want test reference RandomX in miner (2.99.5+) you can use **randomx-benchmark.xmrig.com:7777**
Minimum config for test:
```json
{
    "pools": [
        {
            "url": "randomx-benchmark.xmrig.com:7777"
        }
    ]
}
```

Name for algorithm is `rx/test` to avoid potential conflicts in future.

If you feel miner auto configuration is wrong, please provide details:
1. Miner output.
2. Config file.
3. `topology.xml`, can be obtained by `./xmrig --export-topology` or `xmrig.exe --export-topology`.

# Discussion History
## 2010phenix | 2019-08-10T14:15:37+00:00
@xmrig You do muuuch attention to RandomX, вoes this mean that Monero is likely switch to this algorithm type in October?


## xmrig | 2019-08-10T14:57:02+00:00
https://www.reddit.com/r/MoneroMining/comments/cm58fh/real_world_randomx_testing_and_results/ew1xhlx/

Originally I don't think to implement RandomX so soon as it now, but other algorithm variants was come and it changed all plans. I will make 3.0 release on next week (CPU only), then continue original plan. And sorry, if RandomX is next algorithm there will no update for classic miner.
Thank you.

## 2010phenix | 2019-08-11T09:03:01+00:00
Yes I know @xmrig to big and to hard changes for classic..
Am look on Evo, you do this.. as say - eyes fear, hands do work ;).
Thx man!

## Oliverluck | 2019-08-22T06:50:24+00:00
I just got this error msg. Sorry if i'm very noob. What could be wrong?

[https://i.ibb.co/MB26bhL/error-msg.jpg](url)

## xmrig | 2019-08-22T09:15:23+00:00
@Oliverluck Current Monero algorithm is `cn/r` if you want test (not actually mine) reference RandomX you should use randomx-benchmark.xmrig.com:7777.

## Oliverluck | 2019-08-23T20:51:36+00:00
> @Oliverluck Current Monero algorithm is `cn/r` if you want test (not actually mine) reference RandomX you should use randomx-benchmark.xmrig.com:7777.

Thanks lot i got the double h/s on my single kabini

## qutimqqcom | 2019-08-30T21:17:25+00:00
how to disable --randomx-no-numa  use config file ?
try to check miner bench without Non-Uniform Memory Access

## xmrig | 2019-08-30T22:30:51+00:00
@qutimqqcom https://github.com/xmrig/xmrig/blob/master/src/config.json#L19

## qutimqqcom | 2019-08-31T11:13:11+00:00
"numa": false
but   nothing changes
 * CPU          Intel(R) Core(TM) i7-4790 CPU @ 3.60GHz (1) x64 AES
                L2:1.0 MB L3:8.0 MB 4C/8T **NUMA:1**


## xmrig | 2019-08-31T11:26:46+00:00
@qutimqqcom this is detected count of NUMA nodes, your system is single node/UMA machine, this option does not concern you at all, miner will use only one dataset.
Thank you.

## qutimqqcom | 2019-08-31T11:55:03+00:00
may be  i not  undestand but
numa   =  true \false
i see no changes

 * ABOUT        XMRig/3.1.1 gcc/7.4.1
 * LIBS         libuv/1.8.0 hwloc/1.10.1
 * CPU          Intel(R) Xeon(R) CPU E7- 8830 @ 2.13GHz (8) x64 AES
                L2:16.0 MB L3:192.0 MB 64C/64T NUMA:4


## xmrig | 2019-08-31T12:27:58+00:00
`NUMA:4` this is detected count, this number for information and this is algorithm independent.

Difference with `"numa":true` you will see lines like:
```
rx   #0 allocate 2336 MB (2080+256) for RandomX dataset & cache
rx   #0 allocate done huge pages 1168/1168 100% +JIT (769 ms)
rx   #0 init done (3222 ms)
```
4 times (one dataset per node), 9344 MB total.

With `false` you will see it only once.


## qutimqqcom | 2019-09-01T20:21:32+00:00
vm.nr_hugepages
How to calculate how much is needed for optimal performance?


[2019-09-02 06:33:48.332]  cpu  use profile  defyx  (4 threads) scratchpad 256 KB
[2019-09-02 06:33:48.332]  rx   #0 allocate 2336 MB (2080+256) for RandomX dataset & cache
[2019-09-02 06:33:48.374]  rx   #0 allocate done huge pages **128/1168 11%** +JIT (42 ms)
[2019-09-02 06:33:48.376]  cpu  READY threads 4(4) huge pages 4/4 100% memory 1024 KB (44 ms)


## xmrig | 2019-09-02T02:02:08+00:00
@qutimqqcom https://github.com/xmrig/xmrig/issues/1077#issuecomment-515836516

## CrazyBoyFeng | 2019-09-07T04:04:44+00:00
Is there any way to limit the speed that xmrig writing dataset into pagefiles (a.k.a virtual memory or virtual RAM) on Windows? Or use the light mode dataset of the rx-algo?
I hava a 4GB physical RAM Windows PC. When I benchmak the rx-algo, it allocates 2336MB, rather a lot of RAM usage. Then the process try to copy the dataset to the virtual RAM (pagefiles). As we know, the pagefiles are on the harddisks, and the I/O speed of harddisks is very low. So the effect is that, the I/O stream of harddisk is occupied by xmrig.exe, so that the Windows system is stuck for a long time (tens of minutes with mine) and the PC is completely unusable.

## latency0ms | 2019-09-23T14:22:26+00:00
Gday, I need some help testing / tweaking RandomX mining performance on my dual Xeon E5-2680 v2, 2 x 8GB DDR3 rig.

XMRIG Version 3.1.0.

HugePages are:

```
HugePages_Total:    2400
HugePages_Free:       52
HugePages_Rsvd:        0
HugePages_Surp:        0
```
I am able to run:

`sudo ./xmrig -a rx/test -o stratum+tcp://randomx-benchmark.xmrig.com:7777 -k -r 5 --asm=AUTO --donate-level=1 --print-time=5 --threads=12 --log-file=/var/log/xmrig_rxtest.log`

I only get around 4k H/s - this should be at least double, how can I enable / configure NUMA support from the command line?

Thank you.


## xmrig | 2019-09-23T14:58:44+00:00
@latency0ms just remove `--threads=12` and miner will use 20 threads (10 per CPU) with proper CPU/NUMA bindings, unlike cryptonight (you have enough L3 cache for 12 threads per CPU) your CPUs limited by L2 cache.
Thank you.

## latency0ms | 2019-09-23T15:27:52+00:00
I removed `--threads=12` and still getting around 4k:

```
 * ABOUT        XMRig/3.1.0 gcc/5.4.0
 * LIBS         libuv/1.31.0 OpenSSL/1.1.1c hwloc/2.0.4
 * CPU          Intel(R) Xeon(R) CPU E5-2680 v2 @ 2.80GHz (2) x64 AES
                L2:5.0 MB L3:50.0 MB 20C/40T NUMA:2
 * DONATE       1%
 * ASSEMBLY     auto:intel
 * POOL #1      stratum+tcp://randomx-benchmark.xmrig.com:7777 algo rx/test
 * COMMANDS     hashrate, pause, resume
[2019-09-23 15:25:28.146] use pool randomx-benchmark.xmrig.com:7777  178.128.242.134
[2019-09-23 15:25:28.146] new job from randomx-benchmark.xmrig.com:7777 diff 1000225 algo rx/test height 365228
[2019-09-23 15:25:28.146]  rx   init datasets algo rx/test (40 threads) seed 695fde15537e3f2e...
[2019-09-23 15:25:28.147]  cpu  use profile  rx  (20 threads) scratchpad 2048 KB
[2019-09-23 15:25:28.202]  rx   #0 allocate 2336 MB (2080+256) for RandomX dataset & cache
[2019-09-23 15:25:28.706]  rx   #0 allocate done huge pages 1168/1168 100% +JIT (559 ms)
[2019-09-23 15:25:28.770]  cpu  READY threads 20(20) huge pages 20/20 100% memory 40960 KB (624 ms)
[2019-09-23 15:25:33.151] speed 10s/60s/15m n/a n/a n/a H/s max n/a H/s
[2019-09-23 15:25:33.304]  rx   #0 init done (5158 ms)
[2019-09-23 15:25:33.336]  rx   #1 allocate 2336 MB (2080+256) for RandomX dataset & cache
[2019-09-23 15:25:33.836]  rx   #1 allocate done huge pages 1168/1168 100% +JIT (532 ms)
[2019-09-23 15:25:38.154] speed 10s/60s/15m n/a n/a n/a H/s max n/a H/s
[2019-09-23 15:25:38.380]  rx   #1 init done (5075 ms)
[2019-09-23 15:25:43.158] speed 10s/60s/15m n/a n/a n/a H/s max n/a H/s
[2019-09-23 15:25:48.161] speed 10s/60s/15m n/a n/a n/a H/s max n/a H/s
[2019-09-23 15:25:53.165] speed 10s/60s/15m 4050.6 n/a n/a H/s max 4050.6 H/s
[2019-09-23 15:25:57.474] accepted (1/0) diff 1000225 (15 ms)
[2019-09-23 15:25:58.168] speed 10s/60s/15m 4051.2 n/a n/a H/s max 4051.2 H/s
|    CPU THREAD | AFFINITY | 10s H/s | 60s H/s | 15m H/s |
|             0 |        0 |   201.2 |     n/a |     n/a |
|             1 |        1 |   202.2 |     n/a |     n/a |
|             2 |        2 |   202.9 |     n/a |     n/a |
|             3 |        3 |   202.9 |     n/a |     n/a |
|             4 |        4 |   203.0 |     n/a |     n/a |
|             5 |        5 |   203.0 |     n/a |     n/a |
|             6 |        6 |   203.0 |     n/a |     n/a |
|             7 |        7 |   203.0 |     n/a |     n/a |
|             8 |        8 |   203.0 |     n/a |     n/a |
|             9 |        9 |   203.0 |     n/a |     n/a |
|            10 |       10 |   201.6 |     n/a |     n/a |
|            11 |       11 |   201.7 |     n/a |     n/a |
|            12 |       12 |   201.7 |     n/a |     n/a |
|            13 |       13 |   201.7 |     n/a |     n/a |
|            14 |       14 |   202.9 |     n/a |     n/a |
|            15 |       15 |   201.7 |     n/a |     n/a |
|            16 |       16 |   203.3 |     n/a |     n/a |
|            17 |       17 |   203.2 |     n/a |     n/a |
|            18 |       18 |   203.3 |     n/a |     n/a |
|            19 |       19 |   203.3 |     n/a |     n/a |
```

Compared to other benchmarks with the same CPU, it seems that only one CPU is being used?!

## xmrig | 2019-09-23T15:58:47+00:00
What OS do you use?

1. Please run `./xmrig --export-topology` and share resulting `topology.xml`
2. Show output of `lscpu`.

And better do it in separated issue, it looks like bug and really only one CPU used.
Thank you.

## xmrig | 2019-09-28T17:43:07+00:00
RandomX migration guide #1204

# Action History
- Created by: xmrig | 2019-08-10T12:29:58+00:00
- Closed at: 2019-09-28T17:43:07+00:00
