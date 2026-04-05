---
title: The program runs for a while and the CPU cannot compute
source_url: https://github.com/xmrig/xmrig/issues/2560
author: yangdongyang123456
assignees: []
labels: []
created_at: '2021-08-26T04:01:33+00:00'
updated_at: '2021-08-26T20:17:11+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Linux server, the program runs for a while, the CPU has no computing power, how is it? The following is the log information

![image](https://user-images.githubusercontent.com/89564295/130898377-ecf48aa6-60f3-4878-a95b-aa326ed11f32.png)


# Discussion History
## Spudz76 | 2021-08-26T05:15:51+00:00
If running xmrig underneath another miner-manager app it might be restarting xmrig for not having any results in a while. Like a watchdog feature?

Running xmrig directly from a commandline should never jump from benchmarking to initial startup.  It may also be crashing at panthera, where wrapper script relaunches it, and if the `stderr` pipe is not included you might not see the crash message.

Seems like a wrapper/script sort of issue.  Unless the C3Pool fork has done something very differently.

## yangdongyang123456 | 2021-08-26T05:55:22+00:00
[root@k8s-master1 c3pool]# tail -400f xmrig.log 
 * ABOUT        XMRig/6.14.1-C3Pool gcc/9.3.0
 * LIBS         libuv/1.41.0 OpenSSL/1.1.1k hwloc/2.4.1
 * HUGE PAGES   supported
 * 1GB PAGES    supported
 * CPU          Intel Xeon E3-12xx v2 (Ivy Bridge) (8) 64-bit AES VM
                L2:32.0 MB L3:0.0 MB 8C/8T NUMA:1
 * MEMORY       33.4/62.8 GB (53%)
                DIMM 0: 16 GB RAM @ 0 MHz DIMM 0
                DIMM 1: 16 GB RAM @ 0 MHz DIMM 1
                DIMM 2: 16 GB RAM @ 0 MHz DIMM 2
                DIMM 3: 16 GB RAM @ 0 MHz DIMM 3
 * MOTHERBOARD  Red Hat - KVM
 * DONATE       0%
 * ASSEMBLY     auto:intel
 * POOL #1      mine.c3pool.com:17777 algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
[2021-08-26 11:11:23.878]  config   configuration saved to: "/root/c3pool/config.json"
[2021-08-26 11:11:23.878]  benchmk   STARTING ALGO PERFORMANCE CALIBRATION (with 20 seconds round) 
[2021-08-26 11:11:23.878]  benchmk   Algo cn/r Preparation 
[2021-08-26 11:11:23.878]  cpu      use profile  cn  (8 threads) scratchpad 2048 KB
[2021-08-26 11:11:26.272]  cpu      READY threads 8/8 (8) huge pages 100% 8/8 memory 16384 KB (2394 ms)
[2021-08-26 11:11:26.291]  benchmk   Algo cn/r Starting test 
[2021-08-26 11:11:46.392]  benchmk   Algo cn/r hashrate: 86.136435 
[2021-08-26 11:11:46.392]  benchmk   Algo cn-lite/1 Preparation 
[2021-08-26 11:11:46.461]  cpu      stopped (68 ms)
[2021-08-26 11:11:46.461]  cpu      use profile  cn-lite  (8 threads) scratchpad 1024 KB
[2021-08-26 11:11:46.527]  cpu      READY threads 8/8 (8) huge pages 100% 8/8 memory 8192 KB (66 ms)
[2021-08-26 11:11:46.529]  benchmk   Algo cn-lite/1 Starting test 
[2021-08-26 11:12:06.592]  benchmk   Algo cn-lite/1 hashrate: 371.918094 
[2021-08-26 11:12:06.592]  benchmk   Algo cn-heavy/xhv Preparation 
[2021-08-26 11:12:06.673]  msr      cannot read MSR 0x000001a4
[2021-08-26 11:12:06.673]  msr      FAILED TO APPLY MSR MOD, HASHRATE WILL BE LOW
[2021-08-26 11:12:06.699]  cpu      stopped (25 ms)
[2021-08-26 11:12:06.699]  cpu      use profile  cn-heavy  (8 threads) scratchpad 4096 KB
[2021-08-26 11:12:07.139]  cpu      READY threads 8/8 (8) huge pages 100% 16/16 memory 32768 KB (440 ms)
[2021-08-26 11:12:07.235]  benchmk   Algo cn-heavy/xhv Starting test 
[2021-08-26 11:12:24.262]  miner    speed 10s/60s/15m 75.27 n/a n/a H/s max 76.04 H/s
[2021-08-26 11:12:27.287]  benchmk   Algo cn-heavy/xhv hashrate: 76.963406 
[2021-08-26 11:12:27.287]  benchmk   Algo cn-pico Preparation 
[2021-08-26 11:12:27.377]  cpu      stopped (89 ms)
[2021-08-26 11:12:27.377]  cpu      use profile  cn-pico  (8 threads) scratchpad 256 KB
[2021-08-26 11:12:27.402]  benchmk   Algo cn-pico Starting test 
[2021-08-26 11:12:27.406]  cpu      READY threads 8/8 (16) huge pages 100% 8/8 memory 4096 KB (30 ms)
[2021-08-26 11:12:47.405]  benchmk   Algo cn-pico hashrate: 2380.048554 
[2021-08-26 11:12:47.405]  benchmk   Algo cn/ccx Preparation 
[2021-08-26 11:12:47.411]  cpu      stopped (5 ms)
[2021-08-26 11:12:47.411]  cpu      use profile  cn  (8 threads) scratchpad 2048 KB
[2021-08-26 11:12:49.899]  benchmk   Algo cn/ccx Starting test 
[2021-08-26 11:12:50.405]  cpu      READY threads 8/8 (8) huge pages 100% 8/8 memory 16384 KB (2995 ms)
[2021-08-26 11:13:09.948]  benchmk   Algo cn/ccx hashrate: 194.240838 
[2021-08-26 11:13:09.948]  benchmk   Algo cn/gpu Preparation 
[2021-08-26 11:13:10.701]  benchmk   Algo cn/gpu Starting test 
[2021-08-26 11:13:24.633]  miner    speed 10s/60s/15m 21.68 n/a n/a H/s max 199.7 H/s
[2021-08-26 11:13:31.312]  benchmk   Algo cn/gpu hashrate: 21.572940 
[2021-08-26 11:13:31.312]  benchmk   Algo argon2/chukwav2 Preparation 
[2021-08-26 11:13:31.312]  cpu      use argon2 implementation SSSE3
[2021-08-26 11:13:31.669]  cpu      stopped (356 ms)
[2021-08-26 11:13:31.669]  cpu      use profile  argon2  (8 threads) scratchpad 1024 KB
[2021-08-26 11:13:31.681]  cpu      READY threads 8/8 (8) huge pages 100% 8/8 memory 8192 KB (12 ms)
[2021-08-26 11:13:31.682]  benchmk   Algo argon2/chukwav2 Starting test 
[2021-08-26 11:13:51.694]  benchmk   Algo argon2/chukwav2 hashrate: 1594.064597 
[2021-08-26 11:13:51.694]  benchmk   Algo astrobwt Preparation 
[2021-08-26 11:13:51.700]  cpu      stopped (6 ms)
[2021-08-26 11:13:51.700]  cpu      use profile  astrobwt  (8 threads) scratchpad 20480 KB
[2021-08-26 11:13:52.025]  cpu      READY threads 8/8 (8) huge pages 100% 80/80 memory 163840 KB (325 ms)
[2021-08-26 11:13:52.053]  benchmk   Algo astrobwt Starting test 
[2021-08-26 11:14:12.213]  benchmk   Algo astrobwt hashrate: 121.861925 
[2021-08-26 11:14:12.213]  benchmk   Algo rx/0 Preparation 
[2021-08-26 11:14:12.241]  cpu      stopped (28 ms)
[2021-08-26 11:14:12.249]  msr      cannot read MSR 0x000001a4
[2021-08-26 11:14:12.249]  msr      FAILED TO APPLY MSR MOD, HASHRATE WILL BE LOW
[2021-08-26 11:14:12.250]  randomx  init dataset algo rx/0 (8 threads) seed 0000000000000000...
[2021-08-26 11:14:17.051]  randomx  failed to allocate RandomX dataset using 1GB pages
[2021-08-26 11:14:17.662]  randomx  allocated 2336 MB (2080+256) huge pages 100% 1168/1168 +JIT (5412 ms)
[2021-08-26 11:14:26.227]  randomx  dataset ready (8566 ms)
[2021-08-26 11:14:26.227]  cpu      use profile  rx  (8 threads) scratchpad 2048 KB
[2021-08-26 11:14:26.231]  cpu      READY threads 8/8 (8) huge pages 100% 8/8 memory 16384 KB (4 ms)
[2021-08-26 11:14:26.264]  benchmk   Algo rx/0 Starting test 
[2021-08-26 11:14:46.277]  benchmk   Algo rx/0 hashrate: 552.335279 
[2021-08-26 11:14:46.277]  benchmk   Algo rx/graft Preparation 
[2021-08-26 11:14:46.285]  cpu      stopped (7 ms)
[2021-08-26 11:14:46.285]  randomx  init dataset algo rx/graft (8 threads) seed 0000000000000000...
[2021-08-26 11:14:54.036]  randomx  dataset ready (7751 ms)
[2021-08-26 11:14:54.036]  cpu      use profile  rx  (8 threads) scratchpad 2048 KB
[2021-08-26 11:14:54.039]  cpu      READY threads 8/8 (8) huge pages 100% 8/8 memory 16384 KB (3 ms)
[2021-08-26 11:14:54.106]  benchmk   Algo rx/graft Starting test 
[2021-08-26 11:15:14.142]  benchmk   Algo rx/graft hashrate: 534.721499 
[2021-08-26 11:15:14.142]  benchmk   Algo rx/arq Preparation 
[2021-08-26 11:15:14.165]  cpu      stopped (22 ms)
[2021-08-26 11:15:14.165]  randomx  init dataset algo rx/arq (8 threads) seed 0000000000000000...
[2021-08-26 11:15:21.742]  randomx  dataset ready (7577 ms)
[2021-08-26 11:15:21.743]  cpu      use profile  rx/wow  (8 threads) scratchpad 256 KB
[2021-08-26 11:15:21.759]  cpu      READY threads 8/8 (8) huge pages 100% 8/8 memory 2048 KB (16 ms)
[2021-08-26 11:15:21.763]  benchmk   Algo rx/arq Starting test 
[2021-08-26 11:15:25.376]  miner    speed 10s/60s/15m n/a n/a n/a H/s max n/a H/s
[2021-08-26 11:15:41.764]  benchmk   Algo rx/arq hashrate: 3654.828202 
[2021-08-26 11:15:41.764]  benchmk   Algo panthera Preparation 
[2021-08-26 11:15:41.767]  cpu      stopped (2 ms)
[2021-08-26 11:15:41.767]  randomx  init dataset algo panthera (8 threads) seed 0000000000000000...
[2021-08-26 11:15:42.092]  randomx  dataset ready (324 ms)
[2021-08-26 11:15:42.092]  cpu      use profile  panthera  (8 threads) scratchpad 256 KB
[2021-08-26 11:15:42.095]  cpu      READY threads 8/8 (8) huge pages 100% 8/8 memory 2048 KB (2 ms)
[2021-08-26 11:15:42.123]  benchmk   Algo panthera Starting test 
[2021-08-26 11:16:02.127]  benchmk   Algo panthera hashrate: 1491.046183 
[2021-08-26 11:16:02.127]  benchmk   ALGO PERFORMANCE CALIBRATION COMPLETE 
[2021-08-26 11:16:02.129]  config   configuration saved to: "/root/c3pool/config.json"
[2021-08-26 11:16:25.596]  miner    speed 10s/60s/15m n/a n/a n/a H/s max 1491.0 H/s
[2021-08-26 11:17:25.757]  miner    speed 10s/60s/15m n/a n/a n/a H/s max 1491.0 H/s
[2021-08-26 11:18:25.927]  miner    speed 10s/60s/15m n/a n/a n/a H/s max 1491.0 H/s
[2021-08-26 11:19:26.108]  miner    speed 10s/60s/15m n/a n/a n/a H/s max 1491.0 H/s
[2021-08-26 11:20:26.303]  miner    speed 10s/60s/15m n/a n/a n/a H/s max 1491.0 H/s
[2021-08-26 11:21:26.519]  miner    speed 10s/60s/15m n/a n/a n/a H/s max 1491.0 H/s
[2021-08-26 11:22:26.778]  miner    speed 10s/60s/15m n/a n/a n/a H/s max 1491.0 H/s
[2021-08-26 11:23:26.940]  miner    speed 10s/60s/15m n/a n/a n/a H/s max 1491.0 H/s
[2021-08-26 11:24:27.110]  miner    speed 10s/60s/15m n/a n/a n/a H/s max 1491.0 H/s
[2021-08-26 11:25:27.282]  miner    speed 10s/60s/15m n/a n/a n/a H/s max 1491.0 H/s
[2021-08-26 11:26:27.463]  miner    speed 10s/60s/15m n/a n/a n/a H/s max 1491.0 H/s
[2021-08-26 11:27:27.695]  miner    speed 10s/60s/15m n/a n/a n/a H/s max 1491.0 H/s
[2021-08-26 11:28:27.949]  miner    speed 10s/60s/15m n/a n/a n/a H/s max 1491.0 H/s
[2021-08-26 11:29:28.116]  miner    speed 10s/60s/15m n/a n/a n/a H/s max 1491.0 H/s
[2021-08-26 11:30:28.293]  miner    speed 10s/60s/15m n/a n/a n/a H/s max 1491.0 H/s
[2021-08-26 11:31:28.486]  miner    speed 10s/60s/15m n/a n/a n/a H/s max 1491.0 H/s
[2021-08-26 11:32:28.715]  miner    speed 10s/60s/15m n/a n/a n/a H/s max 1491.0 H/s
[2021-08-26 11:33:28.971]  miner    speed 10s/60s/15m n/a n/a n/a H/s max 1491.0 H/s
[2021-08-26 11:34:29.142]  miner    speed 10s/60s/15m n/a n/a n/a H/s max 1491.0 H/s
[2021-08-26 11:35:29.316]  miner    speed 10s/60s/15m n/a n/a n/a H/s max 1491.0 H/s
[2021-08-26 11:36:29.508]  miner    speed 10s/60s/15m n/a n/a n/a H/s max 1491.0 H/s
[2021-08-26 11:37:29.741]  miner    speed 10s/60s/15m n/a n/a n/a H/s max 1491.0 H/s
[2021-08-26 11:38:29.964]  miner    speed 10s/60s/15m n/a n/a n/a H/s max 1491.0 H/s
[2021-08-26 11:39:30.132]  miner    speed 10s/60s/15m n/a n/a n/a H/s max 1491.0 H/s
[2021-08-26 11:40:30.309]  miner    speed 10s/60s/15m n/a n/a n/a H/s max 1491.0 H/s
[2021-08-26 11:41:30.490]  miner    speed 10s/60s/15m n/a n/a n/a H/s max 1491.0 H/s

## yangdongyang123456 | 2021-08-26T05:56:37+00:00
Thought it was the whole log, there is no solution

## xmrig | 2021-08-26T06:48:41+00:00
This is a third party fork and `panthera` is an unsupported algorithm, we can't provide support for it.
Thank you.

## Spudz76 | 2021-08-26T20:17:11+00:00
Technically true, although it would be supported if you ever accepted the PR's :)

# Action History
- Created by: yangdongyang123456 | 2021-08-26T04:01:33+00:00
