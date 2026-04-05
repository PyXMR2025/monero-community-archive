---
title: GPU compute error (and why less than full MHz?)
source_url: https://github.com/xmrig/xmrig/issues/1812
author: nolash
assignees: []
labels:
- bug
created_at: '2020-08-15T21:04:58+00:00'
updated_at: '2020-08-27T07:11:57+00:00'
type: issue
status: closed
closed_at: '2020-08-27T07:11:57+00:00'
---

# Original Description
**Describe the bug**

Not sure if it's a bug, but I compiled to 6.3.1, and started getting "GPU compute error." Did not have them previously, my last version was fetched and compiled in may.

**To Reproduce**
Steps to reproduce the behavior.

Run with cuda, nothing more.

**Expected behavior**

...

**Required data**
 - Miner log as text or screenshot

```
 * ABOUT        XMRig/6.3.1 gcc/10.1.0
 * LIBS         libuv/1.38.1 OpenSSL/1.1.1g hwloc/2.2.0
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          Intel(R) Celeron(R) CPU G3900 @ 2.80GHz (1) x64 AES
                L2:0.5 MB L3:2.0 MB 2C/2T NUMA:1
 * MEMORY       1.0/15.5 GB (7%)
 * DONATE       1%
 * ASSEMBLY     auto:intel
 * POOL #1      de.minexmr.com:7777 algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         11.0/11.0/6.3.0
 * NVML         11.450.57/450.57 press e for health report
 * CUDA GPU     #0 01:00.0 GeForce GTX 1080 Ti 1683/5505 MHz smx:28 arch:61 mem:11035/11178 MB
 * CUDA GPU     #1 04:00.0 GeForce GTX 1060 6GB 1771/4004 MHz smx:10 arch:61 mem:6009/6078 MB
[2020-08-15 22:39:22.756]  net      use pool de.minexmr.com:7777  94.130.165.87
[2020-08-15 22:39:22.757]  net      new job from de.minexmr.com:7777 diff 175004 algo rx/0 height 2165208
[2020-08-15 22:39:22.757]  cpu      use argon2 implementation SSSE3
[2020-08-15 22:39:22.772]  msr      msr kernel module is not available
[2020-08-15 22:39:22.772]  msr      FAILED TO APPLY MSR MOD, HASHRATE WILL BE LOW
[2020-08-15 22:39:22.772]  randomx  init dataset algo rx/0 (2 threads) seed 270c0cfdd8c22818...
[2020-08-15 22:39:22.773]  randomx  allocated 2336 MB (2080+256) huge pages 0% 0/1168 +JIT (1 ms)
[2020-08-15 22:39:29.420]  net      new job from de.minexmr.com:7777 diff 175004 algo rx/0 height 2165209
[2020-08-15 22:39:37.891]  randomx  dataset ready (15118 ms)
[2020-08-15 22:39:37.891]  cpu      use profile  rx  (1 thread) scratchpad 2048 KB
[2020-08-15 22:39:37.893]  cpu      READY threads 1/1 (1) huge pages 0% 0/1 memory 2048 KB (2 ms)
[2020-08-15 22:39:37.911]  nvidia   use profile  rx  (2 threads) scratchpad 2048 KB
|  # | GPU |  BUS ID | INTENSITY | THREADS | BLOCKS | BF |  BS | MEMORY | NAME
|  0 |   0 | 01:00.0 |      1792 |      32 |     56 |  0 |   0 |   3584 | GeForce GTX 1080 Ti
|  1 |   1 | 04:00.0 |       640 |      32 |     20 |  0 |   0 |   1280 | GeForce GTX 1060 6GB
[2020-08-15 22:39:38.660]  nvidia   READY threads 2/2 (748 ms)
[2020-08-15 22:40:37.954]  nvidia   #0 01:00.0 171W 81C 1911/5005 MHz fan0:0%
[2020-08-15 22:40:37.957]  nvidia   #1 04:00.0  69W 76C 1898/3802 MHz fan0:43%
[2020-08-15 22:40:37.957]  miner    speed 10s/60s/15m 1436.8 n/a n/a H/s max 1439.8 H/s
[2020-08-15 22:41:38.006]  nvidia   #0 01:00.0 220W 82C 1911/5005 MHz fan0:0%
[2020-08-15 22:41:38.008]  nvidia   #1 04:00.0  61W 77C 1898/3802 MHz fan0:46%
[2020-08-15 22:41:38.008]  miner    speed 10s/60s/15m 1433.4 1434.4 n/a H/s max 1439.8 H/s
[2020-08-15 22:41:43.145]  net      new job from de.minexmr.com:7777 diff 107143 algo rx/0 height 2165210
[2020-08-15 22:42:17.134]  net      new job from de.minexmr.com:7777 diff 107143 algo rx/0 height 2165211
[2020-08-15 22:42:26.786]  nvidia   GPU #1 COMPUTE ERROR
[2020-08-15 22:42:38.041]  nvidia   #0 01:00.0 169W 83C 1911/5005 MHz fan0:0%
[2020-08-15 22:42:38.043]  nvidia   #1 04:00.0  60W 76C 1898/3802 MHz fan0:47%
[2020-08-15 22:42:38.043]  miner    speed 10s/60s/15m 1434.5 1416.8 n/a H/s max 1439.8 H/s
[2020-08-15 22:43:06.536]  nvidia   GPU #0 COMPUTE ERROR
[2020-08-15 22:43:19.951]  nvidia   GPU #0 COMPUTE ERROR
[2020-08-15 22:43:38.087]  nvidia   #0 01:00.0 220W 83C 1911/5005 MHz fan0:0%
[2020-08-15 22:43:38.089]  nvidia   #1 04:00.0  82W 76C 1898/3802 MHz fan0:48%
[2020-08-15 22:43:38.089]  miner    speed 10s/60s/15m 1420.0 1429.4 n/a H/s max 1439.8 H/s
[2020-08-15 22:44:02.640]  nvidia   GPU #0 COMPUTE ERROR
[2020-08-15 22:44:38.121]  nvidia   #0 01:00.0 196W 84C 1911/5005 MHz fan0:0%
[2020-08-15 22:44:38.125]  nvidia   #1 04:00.0  83W 76C 1898/3802 MHz fan0:49%
[2020-08-15 22:44:38.125]  miner    speed 10s/60s/15m 1431.5 1427.4 n/a H/s max 1439.8 H/s
[2020-08-15 22:44:38.538]  nvidia   GPU #0 COMPUTE ERROR
[2020-08-15 22:45:38.181]  nvidia   #0 01:00.0 211W 84C 1911/5005 MHz fan0:0%
[2020-08-15 22:45:38.183]  nvidia   #1 04:00.0  82W 76C 1898/3802 MHz fan0:49%
[2020-08-15 22:45:38.184]  miner    speed 10s/60s/15m 1427.0 1427.7 n/a H/s max 1439.8 H/s
[2020-08-15 22:46:06.326]  net      new job from de.minexmr.com:7777 diff 71429 algo rx/0 height 2165212
[2020-08-15 22:46:38.202]  nvidia   #0 01:00.0 180W 84C 1911/5005 MHz fan0:0%
[2020-08-15 22:46:38.207]  nvidia   #1 04:00.0  70W 76C 1898/3802 MHz fan0:49%
[2020-08-15 22:46:38.207]  miner    speed 10s/60s/15m 1426.2 1425.7 n/a H/s max 1439.8 H/s
[2020-08-15 22:46:48.867]  nvidia   GPU #0 COMPUTE ERROR
[2020-08-15 22:47:04.657]  nvidia   GPU #0 COMPUTE ERROR
[2020-08-15 22:47:08.262]  cpu      accepted (1/0) diff 71429 (26 ms)
[2020-08-15 22:47:08.945]  net      new job from de.minexmr.com:7777 diff 47619 algo rx/0 height 2165213
[2020-08-15 22:47:09.159]  nvidia   GPU #0 COMPUTE ERROR
[2020-08-15 22:47:17.923]  nvidia   GPU #1 COMPUTE ERROR
[2020-08-15 22:47:26.500]  nvidia   GPU #1 COMPUTE ERROR
[2020-08-15 22:47:38.234]  nvidia   #0 01:00.0 215W 84C 1885/5005 MHz fan0:0%
[2020-08-15 22:47:38.236]  nvidia   #1 04:00.0  47W 76C 1898/3802 MHz fan0:50%
[2020-08-15 22:47:38.237]  miner    speed 10s/60s/15m 1422.4 1424.7 n/a H/s max 1439.8 H/s
[2020-08-15 22:47:54.196]  nvidia   GPU #0 COMPUTE ERROR
[2020-08-15 22:48:00.971]  nvidia   GPU #0 COMPUTE ERROR
[2020-08-15 22:48:17.813]  nvidia   GPU #1 COMPUTE ERROR
[2020-08-15 22:48:34.743]  net      new job from de.minexmr.com:7777 diff 25000 algo rx/0 height 2165214
[2020-08-15 22:48:38.275]  nvidia   #0 01:00.0 207W 83C 1898/5005 MHz fan0:0%
[2020-08-15 22:48:38.279]  nvidia   #1 04:00.0  82W 76C 1898/3802 MHz fan0:50%
[2020-08-15 22:48:38.279]  miner    speed 10s/60s/15m 1414.8 1405.9 n/a H/s max 1439.8 H/s
[2020-08-15 22:48:43.520]  nvidia   GPU #1 COMPUTE ERROR
[2020-08-15 22:49:31.211]  nvidia   GPU #0 COMPUTE ERROR
[2020-08-15 22:49:32.035]  net      new job from de.minexmr.com:7777 diff 25000 algo rx/0 height 2165215
[2020-08-15 22:49:37.978]  nvidia   GPU #0 COMPUTE ERROR
[2020-08-15 22:49:38.331]  nvidia   #0 01:00.0 218W 84C 1898/5005 MHz fan0:0%
[2020-08-15 22:49:38.333]  nvidia   #1 04:00.0  60W 76C 1898/3802 MHz fan0:50%
[2020-08-15 22:49:38.333]  miner    speed 10s/60s/15m 1424.6 1424.0 n/a H/s max 1439.8 H/s
[2020-08-15 22:49:40.688]  cpu      accepted (2/0) diff 25000 (34 ms)
[2020-08-15 22:49:47.542]  cpu      accepted (3/0) diff 25000 (32 ms)
[2020-08-15 22:49:56.718]  cpu      accepted (4/0) diff 25000 (31 ms)
[2020-08-15 22:50:00.651]  cpu      accepted (5/0) diff 25000 (37 ms)
[2020-08-15 22:50:31.615]  cpu      accepted (6/0) diff 25000 (29 ms)
[2020-08-15 22:50:38.351]  nvidia   #0 01:00.0 201W 83C 1847/5005 MHz fan0:0%
[2020-08-15 22:50:38.354]  nvidia   #1 04:00.0  82W 76C 1898/3802 MHz fan0:50%
[2020-08-15 22:50:38.354]  miner    speed 10s/60s/15m 1425.0 1424.8 n/a H/s max 1439.8 H/s
[2020-08-15 22:50:43.569]  net      new job from de.minexmr.com:7777 diff 25000 algo rx/0 height 2165216
[2020-08-15 22:50:52.370]  nvidia   GPU #0 COMPUTE ERROR
[2020-08-15 22:51:02.623]  cpu      accepted (7/0) diff 25000 (33 ms)
[2020-08-15 22:51:10.404]  nvidia   GPU #0 COMPUTE ERROR
[2020-08-15 22:51:28.170]  cpu      accepted (8/0) diff 25000 (31 ms)
[2020-08-15 22:51:30.702]  nvidia   GPU #0 COMPUTE ERROR
[2020-08-15 22:51:34.765]  nvidia   GPU #1 COMPUTE ERROR
[2020-08-15 22:51:38.399]  nvidia   #0 01:00.0 219W 84C 1898/5005 MHz fan0:0%
[2020-08-15 22:51:38.401]  nvidia   #1 04:00.0  70W 76C 1898/3802 MHz fan0:50%
[2020-08-15 22:51:38.401]  miner    speed 10s/60s/15m 1423.4 1423.4 n/a H/s max 1439.8 H/s
[2020-08-15 22:51:59.402]  cpu      accepted (9/0) diff 25000 (32 ms)
[2020-08-15 22:52:27.203]  nvidia   GPU #0 COMPUTE ERROR
[2020-08-15 22:52:33.979]  nvidia   GPU #0 COMPUTE ERROR
[2020-08-15 22:52:37.259]  cpu      accepted (10/0) diff 25000 (28 ms)
[2020-08-15 22:52:38.437]  nvidia   #0 01:00.0 165W 84C 1885/5005 MHz fan0:0%
[2020-08-15 22:52:38.439]  nvidia   #1 04:00.0  60W 77C 1898/3802 MHz fan0:50%
[2020-08-15 22:52:38.440]  miner    speed 10s/60s/15m 1420.5 1421.3 n/a H/s max 1439.8 H/s
[2020-08-15 22:52:45.282]  nvidia   GPU #0 COMPUTE ERROR
[2020-08-15 22:53:12.442]  nvidia   GPU #0 COMPUTE ERROR
[2020-08-15 22:53:20.097]  net      new job from de.minexmr.com:7777 diff 25000 algo rx/0 height 2165217
[2020-08-15 22:53:38.508]  nvidia   #0 01:00.0 208W 84C 1860/5005 MHz fan0:0%
[2020-08-15 22:53:38.511]  nvidia   #1 04:00.0  83W 77C 1898/3802 MHz fan0:50%
[2020-08-15 22:53:38.511]  miner    speed 10s/60s/15m 1422.7 1422.2 n/a H/s max 1439.8 H/s
[2020-08-15 22:53:46.260]  nvidia   GPU #0 COMPUTE ERROR
[2020-08-15 22:53:57.518]  nvidia   GPU #0 COMPUTE ERROR
[2020-08-15 22:53:58.183]  nvidia   GPU #1 COMPUTE ERROR
[2020-08-15 22:54:15.551]  nvidia   GPU #0 COMPUTE ERROR
[2020-08-15 22:54:26.863]  nvidia   GPU #0 COMPUTE ERROR
[2020-08-15 22:54:38.558]  nvidia   #0 01:00.0 218W 84C 1898/5005 MHz fan0:0%
[2020-08-15 22:54:38.561]  nvidia   #1 04:00.0  79W 77C 1898/3802 MHz fan0:50%
[2020-08-15 22:54:38.561]  miner    speed 10s/60s/15m 1423.9 1404.4 326.5 H/s max 1439.8 H/s
[2020-08-15 22:54:44.367]  cpu      accepted (11/0) diff 25000 (34 ms)
[2020-08-15 22:54:44.926]  nvidia   GPU #0 COMPUTE ERROR
[2020-08-15 22:55:00.683]  nvidia   GPU #0 COMPUTE ERROR
[2020-08-15 22:55:02.325]  nvidia   GPU #1 COMPUTE ERROR
[2020-08-15 22:55:14.278]  nvidia   GPU #0 COMPUTE ERROR
[2020-08-15 22:55:21.080]  nvidia   GPU #0 COMPUTE ERROR
[2020-08-15 22:55:38.611]  nvidia   #0 01:00.0 219W 84C 1898/5005 MHz fan0:0%
[2020-08-15 22:55:38.613]  nvidia   #1 04:00.0  62W 77C 1898/3802 MHz fan0:50%
[2020-08-15 22:55:38.613]  miner    speed 10s/60s/15m 1423.7 1422.7 1422.3 H/s max 1439.8 H/s
[2020-08-15 22:55:45.905]  nvidia   GPU #0 COMPUTE ERROR
[2020-08-15 22:56:01.722]  nvidia   GPU #0 COMPUTE ERROR
[2020-08-15 22:56:01.726]  nvidia   GPU #0 COMPUTE ERROR
[2020-08-15 22:56:03.994]  nvidia   GPU #0 COMPUTE ERROR
[2020-08-15 22:56:29.442]  cpu      accepted (12/0) diff 25000 (30 ms)
[2020-08-15 22:56:38.643]  nvidia   #0 01:00.0 169W 84C 1898/5005 MHz fan0:0%
[2020-08-15 22:56:38.647]  nvidia   #1 04:00.0  60W 77C 1898/3802 MHz fan0:51%
[2020-08-15 22:56:38.647]  miner    speed 10s/60s/15m 1422.1 1421.6 1421.5 H/s max 1439.8 H/s
[2020-08-15 22:57:10.861]  nvidia   GPU #1 COMPUTE ERROR
[2020-08-15 22:57:11.749]  nvidia   GPU #0 COMPUTE ERROR
[2020-08-15 22:57:16.258]  nvidia   GPU #0 COMPUTE ERROR
[2020-08-15 22:57:22.605]  cpu      accepted (13/0) diff 25000 (30 ms)
[2020-08-15 22:57:25.776]  net      new job from de.minexmr.com:7777 diff 25000 algo rx/0 height 2165218
[2020-08-15 22:57:38.671]  nvidia   #0 01:00.0 196W 84C 1860/5005 MHz fan0:0%
[2020-08-15 22:57:38.682]  nvidia   #1 04:00.0  66W 77C 1898/3802 MHz fan0:51%
[2020-08-15 22:57:38.683]  miner    speed 10s/60s/15m 1421.7 1422.3 1421.8 H/s max 1439.8 H/s
[2020-08-15 22:58:03.673]  nvidia   GPU #0 COMPUTE ERROR
[2020-08-15 22:58:06.497]  nvidia   GPU #1 COMPUTE ERROR
[2020-08-15 22:58:21.735]  nvidia   GPU #0 COMPUTE ERROR
[2020-08-15 22:58:23.629]  nvidia   GPU #1 COMPUTE ERROR
[2020-08-15 22:58:37.548]  nvidia   GPU #0 COMPUTE ERROR
[2020-08-15 22:58:38.535]  net      new job from de.minexmr.com:7777 diff 25000 algo rx/0 height 2165219
[2020-08-15 22:58:38.721]  nvidia   #0 01:00.0 211W 84C 1885/5005 MHz fan0:0%
[2020-08-15 22:58:38.724]  nvidia   #1 04:00.0  83W 77C 1898/3802 MHz fan0:51%
[2020-08-15 22:58:38.724]  miner    speed 10s/60s/15m 1422.0 1422.3 1421.3 H/s max 1439.8 H/s
[2020-08-15 22:58:55.021]  signal   Ctrl+C received, exiting
[2020-08-15 22:58:55.023]  cpu      stopped (2 ms)
[2020-08-15 22:58:55.934]  nvidia   stopped (912 ms)
```

 - Config file or command line (without wallets)

`/usr/src/xmrig/build/xmrig --cuda --cuda-loader=/usr/src/xmrig-cuda/build/libxmrig-cuda.so -o de.minexmr.com:7777 --cuda-devices=0,1 --donate-level=1% -l /var/log/xmrig.log`

 - OS

linux 5.8.1

 - For GPU related issues: information about GPUs and driver version.

archlinux nividia driver package: nvidia 450.57-9
using xmrig-cude 6.3.0 / cuda 11.0.2-1

**Additional context**

Also curious why the full speed of the GPU CPUs arent being used, ie:

`1683/5505 MHz`

...? 


# Discussion History
## Vestibule22 | 2020-08-16T02:27:31+00:00
Same here and I reported my issue but it is with AMD GPUs.  Its been a little over 2 weeks and havent heard anything nor has it been assigned.  Not sure what is going on.  Not matter what settings I put on my GPUs I keep getting them.  But its random on the GPU and has gone through all of them as I thought it might have just been one going bad.  Hoping they can address this soon and get an update out.  Im missing out on a good amount of money based on the number of errors I have got since this update.

## SChernykh | 2020-08-19T07:32:50+00:00
@nolash the last version that didn't have errors, do you still have it? Can you try it and check if it doesn't produce errors?

## nolash | 2020-08-19T11:25:32+00:00
@SChernykh sadly it doesn't seem to work anymore after os upgrade (of cuda, I guess)...

## SChernykh | 2020-08-19T11:37:27+00:00
I guess CUDA 11 compiler doesn't like RandomX CUDA source code, I'll check it.

## SChernykh | 2020-08-19T12:27:35+00:00
@nolash I suspect that something is broken in the new driver. All CUDA versions don't work for me with the latest driver on Windows, and they worked before. Try to switch back to older driver version until it's fixed in XMRig.

## SChernykh | 2020-08-19T13:08:11+00:00
After a bit more investigation I found that `xmrig-cuda 6.2.1` plugin works fine, you can use it for now. Only `6.3.0` is broken.

## xmrig | 2020-08-20T06:46:53+00:00
Fixed https://github.com/xmrig/xmrig-cuda/releases/tag/v6.3.1
Thank you.

## nolash | 2020-08-27T07:11:57+00:00
tried it out now and looks good.

THanks @xmrig @SChernykh 

# Action History
- Created by: nolash | 2020-08-15T21:04:58+00:00
- Closed at: 2020-08-27T07:11:57+00:00
