---
title: Xmrig spontaneously closes
source_url: https://github.com/xmrig/xmrig/issues/2464
author: MrWolf080
assignees: []
labels: []
created_at: '2021-06-29T11:30:14+00:00'
updated_at: '2021-06-30T20:31:32+00:00'
type: issue
status: closed
closed_at: '2021-06-30T20:31:32+00:00'
---

# Original Description
Thi is a situation that I observe constantly

` * ABOUT        XMRig/6.12.2 gcc/10.1.0

 * LIBS         libuv/1.41.0 OpenSSL/1.1.1k hwloc/2.4.1
 * HUGE PAGES   permission granted
 * 1GB PAGES    unavailable
 * CPU          Intel(R) Xeon(R) CPU E5-2678 v3 @ 2.50GHz (1) 64-bit AES
                L2:3.0 MB L3:30.0 MB 12C/24T NUMA:1
 * MEMORY       6.2/15.8 GB (39%)
                DIMM_A1: 4 GB DDR4 @ 2133 MHz TSD4/4GB
                DIMM_B1: 4 GB DDR4 @ 2133 MHz TSD4/4GB
                DIMM_C1: 4 GB DDR4 @ 2133 MHz TSD4/4GB
                DIMM_D1: 4 GB DDR4 @ 2133 MHz TSD4/4GB
 * MOTHERBOARD  HUANANZHI - X99-TF
 * DONATE       1%
 * ASSEMBLY     auto:intel
 * POOL #1      xao.pool.mine2gether.com:2227 algo cn/xao
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled
[2021-06-29 14:22:39.725]  net      use pool xao.pool.mine2gether.com:2227  138.
201.129.138
[2021-06-29 14:22:39.727]  net      new job from xao.pool.mine2gether.com:2227 d
iff 2500 algo cn/xao height 0
[2021-06-29 14:22:39.728]  cpu      use profile  *  (14 threads) scratchpad 2048
 KB
Для продолжения нажмите любую клавишу . . .`

cmd: 
@echo off
xmrig.exe -o xao.pool.mine2gether.com:2227 -u ... -p ... -k -a cn/xao -t 14 
pause

it does not depend on the cmd parameters. restarting the pc helps but not for long
Another variant:

 * ABOUT        XMRig/6.12.2 gcc/10.1.0
 * LIBS         libuv/1.41.0 OpenSSL/1.1.1k hwloc/2.4.1
 * HUGE PAGES   permission granted
 * 1GB PAGES    unavailable
 * CPU          Intel(R) Xeon(R) CPU E5-2678 v3 @ 2.50GHz (1) 64-bit AES
                L2:3.0 MB L3:30.0 MB 12C/24T NUMA:1
 * MEMORY       6.3/15.8 GB (40%)
                DIMM_A1: 4 GB DDR4 @ 2133 MHz TSD4/4GB
                DIMM_B1: 4 GB DDR4 @ 2133 MHz TSD4/4GB
                DIMM_C1: 4 GB DDR4 @ 2133 MHz TSD4/4GB
                DIMM_D1: 4 GB DDR4 @ 2133 MHz TSD4/4GB
 * MOTHERBOARD  HUANANZHI - X99-TF
 * DONATE       1%
 * ASSEMBLY     auto:intel
 * POOL #1      xao.pool.mine2gether.com:2227 algo cn/xao
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled
[2021-06-29 14:40:50.054]  net      use pool xao.pool.mine2gether.com:2227  138.
201.129.138
[2021-06-29 14:40:50.056]  net      new job from xao.pool.mine2gether.com:2227 d
iff 2500 algo cn/xao height 0
[2021-06-29 14:40:50.057]  cpu      use profile  *  (14 threads) scratchpad 2048
 KB
[2021-06-29 14:40:54.014]  cpu      READY threads 14/14 (14) huge pages 0% 0/14
memory 28672 KB (3957 ms)
[2021-06-29 14:41:00.335]  cpu      accepted (1/0) diff 2500 (340 ms)
[2021-06-29 14:41:00.630]  cpu      accepted (2/0) diff 2500 (400 ms)
[2021-06-29 14:41:07.460]  cpu      accepted (3/0) diff 2500 (351 ms)
[2021-06-29 14:41:18.611]  net      new job from xao.pool.mine2gether.com:2227 d
iff 3750 algo cn/xao height 0
[2021-06-29 14:41:30.889]  cpu      accepted (4/0) diff 3750 (411 ms)
[2021-06-29 14:41:31.228]  net      new job from xao.pool.mine2gether.com:2227 d
iff 3750 algo cn/xao height 0
[2021-06-29 14:41:41.284]  cpu      accepted (5/0) diff 3750 (502 ms)
[2021-06-29 14:41:48.612]  net      new job from xao.pool.mine2gether.com:2227 d
iff 5625 algo cn/xao height 0
[2021-06-29 14:41:50.061]  miner    speed 10s/60s/15m 71.14 n/a n/a H/s max 72.5
2 H/s
[2021-06-29 14:42:02.887]  cpu      accepted (6/0) diff 5625 (382 ms)
[2021-06-29 14:42:50.063]  miner    speed 10s/60s/15m 263.4 235.7 n/a H/s max 26
3.8 H/s
[2021-06-29 14:42:58.598]  cpu      accepted (7/0) diff 5625 (363 ms)
[2021-06-29 14:43:00.698]  cpu      accepted (8/0) diff 5625 (366 ms)
[2021-06-29 14:43:40.756]  cpu      accepted (9/0) diff 5625 (377 ms)
[2021-06-29 14:43:50.067]  miner    speed 10s/60s/15m 259.8 260.4 n/a H/s max 26
4.5 H/s
[2021-06-29 14:43:50.294]  cpu      accepted (10/0) diff 5625 (376 ms)
[2021-06-29 14:43:51.945]  cpu      accepted (11/0) diff 5625 (405 ms)
[2021-06-29 14:43:54.604]  cpu      accepted (12/0) diff 5625 (370 ms)
[2021-06-29 14:44:16.206]  cpu      accepted (13/0) diff 5625 (573 ms)
[2021-06-29 14:44:18.616]  net      new job from xao.pool.mine2gether.com:2227 d
iff 8438 algo cn/xao height 0
Для продолжения нажмите любую клавишу . . .

Works about 2-3 minutes and closed.
Also i noticed that sometimes even if I use 14 threads the processor is 100 loaded. (hashrate was 71) xmrig prosses loads as much as it needs but the remaining resources are loaded by the process MicrosoftHost.exe. I stopped it and hashrate become 263 (on theese logs).
If I use 24 threads, then rebooting helps and it doest close

# Discussion History
## Lonnegan | 2021-06-30T08:07:49+00:00
First of all, it's not useful to use 24 threads. cn/xao uses 2 MB scratchpad per thread. Your Intel cpu has just 30 MB last level cache, which is enough for 14 threads. If you use more, the system has to access to slow DRAM, which slows mining performance down.

I'd counter check with an other algo/coin. Wasn't aware that Alloy (cn/xao) is still alive. I'd try a still maintained coin to find out, if there is a bug in the mining software regarding xao (which is only used for Alloy) or if there's a problem with your system.

## MrWolf080 | 2021-06-30T10:44:59+00:00
 I used cn/xao like an example. My problem doesn't depends on algorithm or settings like cpu-affinity etc. I tried a lot of parameters so i think this is problem with system. I can describe it like I can mine with 24 threads and it works, but if i use less (i tested it close to cache parameters 13,14,15 threads then 2 variants:
1) xmrig closes
2) xmrig become mine on 24 threads (but on program enabled for example 14). I see hashrate for 14 threads like i use 24.
For example, hash on 14 threads about 10h/s per thread (all good)
on 24 threads about 5 h/s
on 14 with my problem - 5h/s and program shows that 14 threads works, but cpu loaded on all threads I described it on first post.

## Spudz76 | 2021-06-30T18:07:08+00:00
I would stop using the `-t` option at all, especially if you're telling it `14` like it would do anyway.  It probably messes things up by generating a "*" profile instead of separate customized ones.

## MrWolf080 | 2021-06-30T20:31:23+00:00
This is also unuseful. The problem solved. I have a virus miner which works with xmrig. 

# Action History
- Created by: MrWolf080 | 2021-06-29T11:30:14+00:00
- Closed at: 2021-06-30T20:31:32+00:00
