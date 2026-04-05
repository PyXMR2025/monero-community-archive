---
title: 'xmrig: ./src/threadpool.c:329: uv__queue_done: Assertion `uv__has_active_reqs(req->loop)''
  failed'
source_url: https://github.com/xmrig/xmrig/issues/3287
author: ThWuensche
assignees: []
labels:
- bug
- kawpow
created_at: '2023-06-19T06:07:59+00:00'
updated_at: '2025-06-16T19:58:20+00:00'
type: issue
status: closed
closed_at: '2025-06-16T19:58:20+00:00'
---

# Original Description
I'm seeing repeated program failures when trying to mine ravencoin with xmrig on a platform with four AMD Radeon VII GPUs.

That's the system information dumped on the start of xmrig:

```
./xmrig 
 * ABOUT        XMRig/6.19.3 gcc/10.2.1
 * LIBS         libuv/1.40.0 OpenSSL/1.1.1n hwloc/2.4.1
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          AMD Ryzen 9 3900X 12-Core Processor (1) 64-bit AES
                L2:6.0 MB L3:64.0 MB 12C/24T NUMA:1
 * MEMORY       10.0/62.8 GB (16%)
 * DONATE       1%
 * ASSEMBLY     auto:ryzen
 * POOL #1      rvn.2miners.com:6060 coin Ravencoin
 * COMMANDS     hashrate, pause, resume, results, connection
 * ADL          press e for health report
 * OPENCL       #0 AMD Accelerated Parallel Processing/OpenCL 2.1 AMD-APP (3423.0)
 * OPENCL GPU   #0 03:00.0 AMD Radeon VII (gfx906:sramecc+:xnack-) 1801 MHz cu:60 mem:13912/16368 MB
 * OPENCL GPU   #1 09:00.0 AMD Radeon VII (gfx906:sramecc+:xnack-) 1801 MHz cu:60 mem:13912/16368 MB
 * OPENCL GPU   #2 11:00.0 AMD Radeon VII (gfx906:sramecc+:xnack-) 1801 MHz cu:60 mem:13912/16368 MB
 * OPENCL GPU   #3 14:00.0 AMD Radeon VII (gfx906:sramecc+:xnack-) 1801 MHz cu:60 mem:13912/16368 MB
 * CUDA         disabled
[2023-06-19 07:58:31.308]  net      use pool rvn.2miners.com:6060  51.89.99.172
[2023-06-19 07:58:31.315]  net      new job from rvn.2miners.com:6060 diff 4295M algo kawpow height 2849227
[2023-06-19 07:58:31.315]  opencl   use profile  kawpow  (4 threads) scratchpad 32 KB
|  # | GPU |  BUS ID | INTENSITY | WSIZE | MEMORY | NAME
|  0 |   0 | 03:00.0 |  15728640 |   256 |   4119 | AMD Radeon VII (gfx906:sramecc+:xnack-)
|  1 |   1 | 09:00.0 |  15728640 |   256 |   4119 | AMD Radeon VII (gfx906:sramecc+:xnack-)
|  2 |   2 | 11:00.0 |  15728640 |   256 |   4119 | AMD Radeon VII (gfx906:sramecc+:xnack-)
|  3 |   3 | 14:00.0 |  15728640 |   256 |   4119 | AMD Radeon VII (gfx906:sramecc+:xnack-)
[2023-06-19 07:58:32.096]  opencl   READY threads 4/4 (781 ms)

```
And after some time it fails with (please note that is from an earlier run, as indicated by the timestamps):

```
[2023-06-19 01:07:11.451]  net      new job from rvn.2miners.com:6060 diff 4295M algo kawpow height 2848814
[2023-06-19 01:07:24.438]  opencl   accepted (46/0) diff 4295M (25 ms)
[2023-06-19 01:07:48.617]  opencl   #0 03:00.0  91W 60C 2213RPM 853/850MHz
[2023-06-19 01:07:48.617]  opencl   #1 09:00.0  90W 58C 2215RPM 805/350MHz
[2023-06-19 01:07:48.618]  opencl   #2 11:00.0  89W 60C 2053RPM 809/850MHz
[2023-06-19 01:07:48.618]  opencl   #3 14:00.0  89W 59C 2501RPM 814/850MHz
[2023-06-19 01:07:48.618]  miner    speed 10s/60s/15m 68.89 69.65 69.54 MH/s max 74.43 MH/s
[2023-06-19 01:08:18.114]  net      new job from rvn.2miners.com:6060 diff 4295M algo kawpow height 2848815
[2023-06-19 01:08:18.429]  opencl   KawPow program for period 949606 compiled (313ms)
[2023-06-19 01:08:18.743]  opencl   KawPow program for period 949606 compiled (312ms)
[2023-06-19 01:08:19.060]  opencl   KawPow program for period 949606 compiled (317ms)
xmrig: ./src/threadpool.c:329: uv__queue_done: Assertion `uv__has_active_reqs(req->loop)' failed.

```
I have seen the same issue mentioned on an earlier issue report, but there it's marked as done and the issue was closed.

Please let me know whether you need more information to sort out the problem.

Best regards, Thomas


# Discussion History
## SChernykh | 2023-06-19T06:31:02+00:00
Yes, I can confirm. It's a bug in how XMRig uses libuv to precompile KawPow programs. I'll try to fix it today.

## SChernykh | 2023-06-19T06:33:47+00:00
It also seems that you compiled XMRig with a very old libuv version `libuv/1.40.0` - the latest available version is `1.45.0`. You can try to recompile it with the latest version.

## SChernykh | 2023-06-19T10:36:15+00:00
This is fixed in #3288. You can compile dev branch after it's merged.

## ThWuensche | 2023-06-19T12:00:04+00:00
Thanks a lot for the quick reaction! I will apply and build it in the evening.

## koitsu | 2023-07-27T22:32:27+00:00
Edit: sorry for the noise, my issue looks more like https://github.com/xmrig/xmrig/issues/2800 so I'll comment there.


## Apetree100122 | 2024-01-02T12:25:10+00:00
./xmrig 
 * ABOUT       
 *  XMRig/6.19.3 gcc/10.2.1
 * LIBS    
 *      libuv/1.40.0 
 * OpenSSL/1.1.1
 * n hwloc/2.4.1
 * HUGE PAGES   
 * supported
 * 1GB PAGES   
 *  disabled
 * CPU          
 * AMD Ryzen 9 3900X 
 * 12-Core Processor (1) 64-bit 
 * AES
              
  L2:6.0 MB L3:64.0 MB 12C/24T NUMA:1
 * MEMORY       10.0/62.8 GB (16%)
 * DONATE   
 *     1% * ASSEMBLY     
 * auto:ryzen
 * POOL #1    
 * rvn.2miners.com:6060 
 * coin Ravencoin
 * COMMANDS     
 * hashrate,
 *  pause, resume, r
 * esults, connection
 * ADL     
 *      press e for health report
 * OPENCL       #0 
 * AMD Accelerated Parallel Processing/
 * OpenCL 2.1 AMD-APP (3423.0)
 * OPENCL GPU   #0 03:00.0 
 * AMD Radeon VII (gfx906:sramecc+:xnack-) 
 * 1801 MHz cu:60 mem:13912/16368 MB
 * OPENCL GPU   #1 09:00.0 AMD Radeon VII (
 * gfx906:sramecc+:xnack-) 1801 MHz cu:60 mem:13912/16368 MB
 * OPENCL GPU   #2 11:00.0 AMD Radeon VII (gfx906:sramecc+:xnack-) 
 * 1801 MHz cu:60 mem:13912/16368 MB
 * OPENCL GPU   #3 14:00.0 AMD Radeon VII
 *  (gfx906:sramecc+:xnack-) 1801 MHz cu:60 mem:13912/16368 MB
 * CUDA         di
 * sabled
[2023-06-19 07:58:31.308]  net    
  use pool rvn.2miners.com:6060  51.89.99.172
[2023-06-19 07:58:31.315]  net 
     new job from rvn.2miners.com:6060 diff
 4295M algo kawpow height 2849227
[2023-06-19 07:58:31.315]  opencl   
use profile  kawpow  (4 threads) scratchpad 32 KB
|  # | GPU |  BUS ID | INTENSITY | 
WSIZE | MEMORY | NAME
|  0 |   0 | 03:00.0 | 
 15728640 |   256 | 
  4119 | AMD Radeon VII (gfx906:sramecc+:xnack-)
|  1 |   1 | 09:00.0 |  15728640 |   256 |   4
119 | AMD Radeon VII (gfx906:sramecc+:xnack-)
|  2 |   2 | 11:00.0 |  15728640 |   256 |   4119 | AMD
 Radeon VII (gfx906:sramecc+:xnack-)
|  3 |   3 | 14:00.0 |  15728640 |   256 |   4119 | AMD Radeon VII (
gfx906:sramecc+:xnack-)
[2023-06-19 07:58:32.096] 
 opencl   READY threads 4/4 (781 ms)


## Apetree100122 | 2024-01-02T12:27:01+00:00
[2023-06-19 01:07:11.451]  net     
 new job from rvn.
2min.
ers.com:6060 diff 4295M alg
o kawpow 
height 2848814
[2023-06-19 01:07:2
4.438]  opencl   accep
ted (46/0) diff 4295M (25 
ms)
[2023-06-19 01:07:48.617]  opencl   
#0 03:00.0  91W 60C 2213RPM 853/850MHz
[2023-06-19 01:07:48.617]  opencl   #1 09:00.0  90W 58C
 2215RPM 805/350MHz
[2023-06-19 01:07:48.618]  opencl   #2 11:00.0  89W 60C 2053R
PM 809/850MHz
[2023-06-19 01:07:48.618]  opencl   #3 14:00.0  89W 59C 2501RPM 814/85
0MHz
[2023-06-19 01:07:48.618]  miner    speed 10s/60s/15m 68.
89 69.65 69.54 MH/s max 74.43 MH/s
[2023-06-19 01:08:18.114]  net      
new job from rvn.2miners.com:6060 diff 4295M algo kawpow height 2848815
[2023-06-19 01:08:18.429]
  opencl   KawPow program for period 949606 compiled (313ms)
[2023-06-19 01:08:18.743]  opencl   
KawPow program for period 949606 compiled (312ms)
[2023-06-19 01:08:19.060] 
 opencl   KawPow program for peri.od 949606 compiled (317ms)
xmrig: .
/src/threadpool.c:329: uv__q
ueue_done: Assertion `uv__has_active_reqs(req->
loop)' failed.


## SChernykh | 2024-01-02T12:30:13+00:00
@Apetree100122 
You're running `XMRig/6.19.3` This bug was fixed in a later release. Update your XMRig.

## Apetree100122 | 2024-01-02T12:32:28+00:00
 pr
ess 
e for health report[2023-06-19 01:0
7:11.451]  net      
new job from rvn.2miners.com:6060 diff 4295M al.go
 kawpow heig
ht 2848
814
[2023-0
6-19 01:07:24.43
8]  opencl   accept
ed (46/0) diff 4295M (25 ms)
[2023-06-19 01:07:48.617k
]  opencl   #0 03:00.0  91W 60C 2213RP
M 853/850MHz
[2023-06-19 01:07:
48.617]  opencl   #1 09:00.0  90W 
58C 2215RPM 80
5/350MHz
[2023-06-19 01:07:48.618]  opencl   #2 11:00.0
  89W 60C 2053RPM 809/850MHz
[2023-06-19 01:07:48.618]  open
cl   #3 14:00.0  89W 59C 2501R
PM 814/850MHz
[2023-06-19 0
1:07:48.618]  miner    speed 10s/60s/15m 
68.89 69.65 69.54 MH/s max 74.
43 MH/s
[2023-06-19 01:08:18.114]  net      new job .
from rvn.2miners.com:6060 diff 4295M alg
o kawpow height 2848815
[2023-06-19 01:08:1
8.429]  opencl   KawPow program for p
eriod 949606 compiled (313ms)
[2023-06-19 01:08:18.743]  opencl   KawPow prog
ram for period 949606 compiled (312m 
s)2023-06-19 01:08:19.0
60]  
opencl   KawPow program for 
period 949606 compiled (31
7ms)
xmrig: ./src/threadpool.c:
32 
9: uv__queue_done: Assertion `uv__has_active_reqs(req->loop)' failed../xmrig 
 * ABOUT        XMRig/6.19
 * .3 gcc/
 * 10.2.1
 * LIBS         libuv/1.40.0 O
 * penSSL/
 * 1.1.1n hwloc/2.4.1
 * HUGE PAG
 * ES   supported
 * 1GB PAGES    disabled
 * CPU          AMD Ry
 * zen 9 3900X 12-Core Processor (1) 64-bit AES
                L2:6.0 MB L3:64.0 MB 
12C/24T NUMA:1
 * MEMORY       10.0
 * /6 * 2.8 GB (16%)
* DO
 * NATE        1 * %* ASSEMBLY      * auto:ryzen
 * POOL #1      rvn.2miners.com:6
 * 060 coin Ravencoin
 * COMMANDS     hashrate, pause, resume, results, connection
 * ADL          press e for health
 *  report
 * OPE
 * NCL       #0 AMD Accelerated
 *  Parallel Processing/OpenCL 2.1 AMD-AP
 * P (3423.0)
 * OPEN.CL GPU   #0 03:00.0xnack-a
 * deon VII (gfx906:sramecc+:xnack-) 1801 MHz cu:60
 *  mem:13912/16
 * 368 MB
 * OPENCL GPU   #1 09:00.0 AMD Rade
 * on VII (gfx906:sramecc+:xnack-) 1801 MHz cu:60 mem:13912/16368 MB
 * OPENCL GPU   #2 11:00.0 AMD Radeon VII
 *  (gfx906:sramecc+:xnac
 * k-) 1801 MHz cu:60 mem:13912/16368 MB
 * OPENCL GPU   #3 14:00.0 AMD Radeon VII (gfx906:sramecc+:xnack-) 1801 MHz cu:60 mem:13912/16368 MB
 * CUDA         disabled
[2023-06-19 07:58:31.308]  net      use pool rvn.2m
iners.com:6060  51.89.99.172
[2023-06-19 07:58:31.315]  net      new job from rvn.2miners.com:6060 diff 4295M algo kawpow height 2849227
[2023-06-19 07:58:31.315]  opencl  
 use profile  kawpow  (4 threads) scratchpad 32 KB
|  # | GPU |  BUS ID | INTENSITY | WSIZE | MEMORY | NAME
|  0 |   
0 | 03:00.0 |  15728640 |   256 |   4119 | AMD Radeon VII (gfx906:sramecc+:xnack-)
|  1 | .
  1 | 09:00.0 |  15728640 |   256 |   
4119 | AMD Radeon VII (gfx906:sramecc+
:xnack-)
|  2 |   2 | 11:00.0 |  15728640 |   
256 |   4119 | AMD Radeon VII
 (gfx906:sramecc+:xnack-)
|  3 |   3 | 14:00.0 |  15728640 |   256 |   41
19 | AMD Radeon VII (gfx906:sramecc+:xnack-)
[2023-06-19 07:58:32.096]  opencl 
  READY threads 4/4 (78
1 ms)


# Action History
- Created by: ThWuensche | 2023-06-19T06:07:59+00:00
- Closed at: 2025-06-16T19:58:20+00:00
