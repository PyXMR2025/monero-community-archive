---
title: v2.8.1 and autodetect hardware
source_url: https://github.com/xmrig/xmrig/issues/787
author: trasherdk
assignees: []
labels:
- review later
created_at: '2018-10-09T09:52:08+00:00'
updated_at: '2019-08-02T12:11:42+00:00'
type: issue
status: closed
closed_at: '2019-08-02T12:11:42+00:00'
---

# Original Description
It looks like ver. 2.8.1 is not as good to detect hardware as previous versions.

OS is Slackware 14.2 x64 Kernel 4.4.157

On 2.6.4 I was getting 4 threads, but only get 3 threads on 2.8.1, using only 6MB L3 memory.

So, version 2.8.1 updates config.json, adding threads config, where it was `threads: null` before,
and for some reason only wants 3 threads.

v2.6.4: `speed 10s/60s/15m 258.6 259.3 n/a H/s max 260.6 H/s` 4 threads.

v2.8.1: `speed 10s/60s/15m 215.7 214.2 n/a H/s max 215.7 H/s` 3 threads.

Adding one more thread to config.json, brings things back on par'ish.

v2.8.1: `speed 10s/60s/15m 255.1 257.9 n/a H/s max 259.7 H/s` 4 threads.

v2.8.1$ ./xmrig 
 * ABOUT        XMRig/2.8.1-dev gcc/5.5.0
 * LIBS         libuv/1.20.3 OpenSSL/1.0.2p microhttpd/0.9.59 
 * CPU          Intel(R) Xeon(R) CPU E3-1230 v5 @ 3.40GHz (1) x64 AES
 * CPU L2/L3    1.0 MB/8.0 MB
 * THREADS      3, cryptonight, donate=1%
 * ASSEMBLY     auto:intel
 * POOL #1      pool.monero.hashvault.pro:5555 variant auto
 * COMMANDS     hashrate, pause, resume
 READY (CPU) threads 3(3) huge pages 3/3 100% memory 6.0 MB

v2.6.4$ ./xmrig
  * VERSIONS     XMRig/2.6.4 libuv/1.20.3 gcc/5.5.0
  * CPU          Intel(R) Xeon(R) CPU E3-1230 v5 @ 3.40GHz (1) x64 AES-NI
  * CPU L2/L3    1.0 MB/8.0 MB
  * THREADS      4, cryptonight, av=0, donate=1%
  * POOL #1      pool.monero.hashvault.pro:5555 variant 1
  * POOL #2      pool.supportxmr.com:5555 variant 1
  * COMMANDS     hashrate, pause, resume
 use pool pool.monero.hashvault.pro:5555 145.239.0.75
 new job from pool.monero.hashvault.pro:5555 diff 20000 algo cn/1
 READY (CPU) threads 4(4) huge pages 4/4 100% memory 8.0 MB


# Discussion History
## xmrig | 2018-10-09T10:18:44+00:00
Is hyper threading disabled? how many cores available in system 4 or 8?
Thank you.

## trasherdk | 2018-10-09T10:55:30+00:00
CPU Intel(R) Xeon(R) CPU E3-1230 v5 @ 3.40GHz (1) x64 AES-NI
It's 4 cores, 8 threads, 8MB L3 memory.
I can't see if hyper threading is enabled or not, but I would guess it is.

## xmrig | 2018-10-09T11:01:29+00:00
`cat /proc/cpuinfo | grep -c vendor_id` or run `top` and press `1`.
First command show number of logical CPUs.

## trasherdk | 2018-10-10T05:43:37+00:00
Well, cpuinfo said 8, and 4 of 8 threads are used by xmrig.

	
	1  [|||||||||||||||||||||||||||||||    76.0%]   5  [|||||||||||||                      31.2%]
	2  [||                                  2.0%]   6  [||||||||||||||||||||||||||||||||||100.0%]
	3  [||||||||||||||||||||||||||||||||||100.0%]   7  [|                                   1.3%]
	4  [||||||||||||||||||||||||||||||||||100.0%]   8  [||                                  1.3%]
	Mem[|||||||||||||||||||||||||    17.0G/31.2G]   Tasks: 34, 254 thr; 5 running
	Swp[                                0K/2.00G]   Load average: 4.30 4.20 4.18 
	                                              Uptime: 13 days, 23:20:35
	
Most of the time, it's doing 260H/s on CN/1:
`speed 10s/60s/15m 261.1 212.6 252.6 H/s max 263.2 H/s`


# Action History
- Created by: trasherdk | 2018-10-09T09:52:08+00:00
- Closed at: 2019-08-02T12:11:42+00:00
