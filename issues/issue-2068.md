---
title: 'xmrig: src/threadpool.c:329: uv__queue_done: Assertion `uv__has_active_reqs(req->loop)''
  failed.'
source_url: https://github.com/xmrig/xmrig/issues/2068
author: minzak
assignees: []
labels: []
created_at: '2021-01-28T15:27:38+00:00'
updated_at: '2021-04-12T14:18:36+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:18:36+00:00'
---

# Original Description
Fresh miner and old errors, similar to this https://github.com/xmrig/xmrig/issues/1836

```
./xmrig
 * ABOUT        XMRig/6.7.0 gcc/8.3.0
 * LIBS         libuv/1.24.1 OpenSSL/1.1.1d hwloc/1.11.12
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          Intel(R) Core(TM) i5-7400 CPU @ 3.00GHz (1) 64-bit AES
                L2:1.0 MB L3:6.0 MB 4C/4T NUMA:1
 * MEMORY       3.7/15.6 GB (24%)
 * DONATE       1%
 * ASSEMBLY     auto:intel
 * POOL #1      stratum+ssl://stratum.ravenminer.com:13838 algo kawpow
 * COMMANDS     hashrate, pause, resume, results, connection
 * HTTP API     0.0.0.0:33865 
 * ADL          press e for health report
 * OPENCL       #0 AMD Accelerated Parallel Processing/OpenCL 2.1 AMD-APP (3143.9)
 * OPENCL GPU   #0 03:00.0 Radeon RX 580 Series (Ellesmere) 1411 MHz cu:36 mem:3839/4090 MB
 * OPENCL GPU   #1 07:00.0 Radeon RX 580 Series (Ellesmere) 1411 MHz cu:36 mem:3839/4090 MB
 * OPENCL GPU   #2 09:00.0 Radeon RX 580 Series (Ellesmere) 1411 MHz cu:36 mem:3839/4090 MB
 * OPENCL GPU   #3 0a:00.0 Radeon RX 580 Series (Ellesmere) 1411 MHz cu:36 mem:3839/4090 MB
 * OPENCL GPU   #4 0b:00.0 Radeon RX 580 Series (Ellesmere) 1411 MHz cu:36 mem:3839/4090 MB
 * OPENCL GPU   #5 0c:00.0 Radeon RX 580 Series (Ellesmere) 1411 MHz cu:36 mem:3839/4090 MB
 * OPENCL GPU   #6 0d:00.0 Radeon RX 580 Series (Ellesmere) 1411 MHz cu:36 mem:3839/4090 MB
 * OPENCL GPU   #7 0e:00.0 Radeon RX 580 Series (Ellesmere) 1411 MHz cu:36 mem:3839/4090 MB
 * OPENCL GPU   #8 0f:00.0 Radeon RX 580 Series (Ellesmere) 1430 MHz cu:36 mem:7935/8186 MB
 * OPENCL GPU   #9 10:00.0 Radeon RX 580 Series (Ellesmere) 1430 MHz cu:36 mem:7935/8186 MB
[2021-01-28 15:52:13.746]  net      use pool stratum.ravenminer.com:13838 TLSv1.2 3.122.71.171
[2021-01-28 15:52:13.746]  net      fingerprint (SHA-256): "4de3045a227e2b29579a1b84e58ecd85403d8e0ced51a5dd20ab694b330c73ca"
[2021-01-28 15:52:13.747]  net      new job from stratum.ravenminer.com:13838 diff 431M algo kawpow height 1601946
[2021-01-28 15:52:13.747]  opencl   use profile  kawpow  (10 threads) scratchpad 32 KB
|  # | GPU |  BUS ID | INTENSITY | WSIZE | MEMORY | NAME
|  0 |   0 | 03:00.0 |   9437184 |   256 |   2770 | Radeon RX 580 Series (Ellesmere)
|  1 |   1 | 07:00.0 |   9437184 |   256 |   2770 | Radeon RX 580 Series (Ellesmere)
|  2 |   2 | 09:00.0 |   9437184 |   256 |   2770 | Radeon RX 580 Series (Ellesmere)
|  3 |   3 | 0a:00.0 |   9437184 |   256 |   2770 | Radeon RX 580 Series (Ellesmere)
|  4 |   4 | 0b:00.0 |   9437184 |   256 |   2770 | Radeon RX 580 Series (Ellesmere)
|  5 |   5 | 0c:00.0 |   9437184 |   256 |   2770 | Radeon RX 580 Series (Ellesmere)
|  6 |   6 | 0d:00.0 |   9437184 |   256 |   2770 | Radeon RX 580 Series (Ellesmere)
|  7 |   7 | 0e:00.0 |   9437184 |   256 |   2770 | Radeon RX 580 Series (Ellesmere)
|  8 |   8 | 0f:00.0 |   9437184 |   256 |   2770 | Radeon RX 580 Series (Ellesmere)
|  9 |   9 | 10:00.0 |   9437184 |   256 |   2770 | Radeon RX 580 Series (Ellesmere)
[2021-01-28 15:52:14.629]  opencl   READY threads 10/10 (881 ms)
[2021-01-28 15:52:14.937]  opencl   KawPow program for period 533982 compiled (308ms)
[2021-01-28 15:52:15.249]  opencl   KawPow program for period 533983 compiled (312ms)

...

[2021-01-28 16:12:14.751]  opencl   #9 10:00.0   0W  0C    0RPM 0/0MHz
[2021-01-28 16:12:14.752]  miner    speed 10s/60s/15m 115.3 115.8 105.8 MH/s max 120.5 MH/s
[2021-01-28 16:12:22.396]  opencl   accepted (112/0) diff 1087M (45 ms)
[2021-01-28 16:12:27.921]  opencl   accepted (113/0) diff 1087M (45 ms)
[2021-01-28 16:12:30.018]  net      new job from stratum.ravenminer.com:13838 diff 1087M algo kawpow height 1601963
[2021-01-28 16:12:32.027]  opencl   accepted (114/0) diff 1087M (44 ms)
[2021-01-28 16:12:36.025]  net      new job from stratum.ravenminer.com:13838 diff 1087M algo kawpow height 1601964
[2021-01-28 16:12:36.333]  opencl   KawPow program for period 533989 compiled (305ms)
[2021-01-28 16:12:41.807]  opencl   KawPow program for period 533989 compiled (303ms)
[2021-01-28 16:12:42.106]  opencl   KawPow program for period 533989 compiled (300ms)
[2021-01-28 16:12:42.405]  opencl   KawPow program for period 533989 compiled (299ms)
[2021-01-28 16:12:42.705]  opencl   KawPow program for period 533989 compiled (299ms)
[2021-01-28 16:12:43.005]  opencl   KawPow program for period 533989 compiled (300ms)
[2021-01-28 16:12:43.305]  opencl   KawPow program for period 533989 compiled (301ms)
[2021-01-28 16:12:43.354]  opencl   accepted (115/0) diff 1087M (45 ms)
[2021-01-28 16:12:43.605]  opencl   KawPow program for period 533989 compiled (300ms)
[2021-01-28 16:12:43.900]  opencl   KawPow program for period 533989 compiled (295ms)
[2021-01-28 16:12:44.199]  opencl   KawPow program for period 533989 compiled (299ms)
[2021-01-28 16:13:02.473]  opencl   accepted (116/0) diff 1087M (44 ms)
[2021-01-28 16:13:14.800]  opencl   #0 03:00.0  96W 56C 1899RPM 1080/2040MHz
[2021-01-28 16:13:14.800]  opencl   #1 07:00.0  94W 56C 1964RPM 1080/2040MHz
[2021-01-28 16:13:14.801]  opencl   #2 09:00.0  93W 55C 1923RPM 1100/2080MHz
[2021-01-28 16:13:14.801]  opencl   #3 0a:00.0  96W 54C 1911RPM 1100/2080MHz
[2021-01-28 16:13:14.801]  opencl   #4 0b:00.0  93W 54C 1942RPM 1100/2080MHz
[2021-01-28 16:13:14.802]  opencl   #5 0c:00.0  95W 53C 1952RPM 1100/2080MHz
[2021-01-28 16:13:14.802]  opencl   #6 0d:00.0   0W  0C    0RPM 0/0MHz
[2021-01-28 16:13:14.802]  opencl   #7 0e:00.0   0W  0C    0RPM 0/0MHz
[2021-01-28 16:13:14.802]  opencl   #8 0f:00.0   0W  0C    0RPM 0/0MHz
[2021-01-28 16:13:14.802]  opencl   #9 10:00.0   0W  0C    0RPM 0/0MHz
[2021-01-28 16:13:16.063]  net      new job from stratum.ravenminer.com:13838 diff 1087M algo kawpow height 1601965
xmrig: src/threadpool.c:329: uv__queue_done: Assertion `uv__has_active_reqs(req->loop)' failed.
Aborted
```



# Discussion History
# Action History
- Created by: minzak | 2021-01-28T15:27:38+00:00
- Closed at: 2021-04-12T14:18:36+00:00
