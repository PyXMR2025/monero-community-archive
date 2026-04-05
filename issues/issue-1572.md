---
title: FreeBSD 12.1 on Dual AMD 6376 throws errors
source_url: https://github.com/xmrig/xmrig/issues/1572
author: agentpatience
assignees: []
labels: []
created_at: '2020-02-29T01:45:53+00:00'
updated_at: '2021-07-11T01:21:45+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:59:45+00:00'
---

# Original Description
I am not a new user to FreeBSD but when I try to compile XMRIG using GCC 9 on a dual AMD Opteron 6376 based server I get this output:

root@AMD6376:~/xmrig/build # ./xmrig --donate-level 1 -o pool.supportxmr.com:443 -u 41rJ5pGVTdH2h22xgDr8tWPjGXaTLZXehA5DUX5cxDKdgkAVahtVx7zFTWYYYh5mJ1fCwgKP4q1fQMrxW7PNDBDwTz45Rfm -p AMD6376 -k --tls
 * ABOUT        XMRig/5.7.0 gcc/9.2.0
 * LIBS         libuv/1.34.0 OpenSSL/1.1.1d-freebsd hwloc/1.11.11
 * HUGE PAGES   supported
 * 1GB PAGES    unavailable
 * CPU          AMD Opteron(tm) Processor 6376 (2) x64 AES
                L2:32.0 MB L3:24.0 MB 32C/32T NUMA:4
 * MEMORY       2.1/23.9 GB (9%)
 * DONATE       5%
 * ASSEMBLY     auto:bulldozer
 * POOL #1      pool.supportxmr.com:443 algo auto
 * COMMANDS     hashrate, pause, resume
 * OPENCL       disabled
 * CUDA         disabled
[2020-02-28 13:36:35.934]  net  use pool pool.supportxmr.com:443 TLSv1.2 104.140.244.186
[2020-02-28 13:36:35.934]  net  fingerprint (SHA-256): "676f843ef4cda0f72578b7589eedb13f4ca79f636b6a4e57eb38847c8f679d93"
[2020-02-28 13:36:35.934]  net  new job from pool.supportxmr.com:443 diff 50000 algo rx/0 height 2043878
[2020-02-28 13:36:35.934]  rx   init datasets algo rx/0 (32 threads) seed 1d0ca5277b4b47e8...
[2020-02-28 13:36:35.935]  rx   #0 skipped (can't bind memory)
[2020-02-28 13:36:35.935]  rx   #3 skipped (can't bind memory)
[2020-02-28 13:36:35.935]  rx   #2 skipped (can't bind memory)
[2020-02-28 13:36:35.935]  rx   #1 skipped (can't bind memory)
[2020-02-28 13:36:36.069]  rx   #0 allocated  256 MB huge pages 100% +JIT (133 ms)
[2020-02-28 13:36:36.069]  rx   failed to allocate RandomX datasets, switching to slow mode (134 ms)
[2020-02-28 13:36:38.075]  rx   #0 dataset ready (2007 ms)
[2020-02-28 13:36:38.075]  cpu  use profile  rx  (28 threads) scratchpad 2048 KB
[2020-02-28 13:36:38.077] CPU #00 warning: "can't bind memory"
[2020-02-28 13:36:38.099] CPU #01 warning: "can't bind memory"
[2020-02-28 13:36:38.121] CPU #02 warning: "can't bind memory"
[2020-02-28 13:36:38.143] CPU #03 warning: "can't bind memory"
[2020-02-28 13:36:38.165] CPU #04 warning: "can't bind memory"
[2020-02-28 13:36:38.187] CPU #05 warning: "can't bind memory"
[2020-02-28 13:36:38.209] CPU #06 warning: "can't bind memory"
[2020-02-28 13:36:38.231] CPU #08 warning: "can't bind memory"
[2020-02-28 13:36:38.253] CPU #09 warning: "can't bind memory"
[2020-02-28 13:36:38.275] CPU #10 warning: "can't bind memory"
[2020-02-28 13:36:38.297] CPU #11 warning: "can't bind memory"
[2020-02-28 13:36:38.319] CPU #12 warning: "can't bind memory"
[2020-02-28 13:36:38.341] CPU #13 warning: "can't bind memory"
[2020-02-28 13:36:38.363] CPU #14 warning: "can't bind memory"
[2020-02-28 13:36:38.385] CPU #16 warning: "can't bind memory"
[2020-02-28 13:36:38.407] CPU #17 warning: "can't bind memory"
[2020-02-28 13:36:38.429] CPU #18 warning: "can't bind memory"
[2020-02-28 13:36:38.451] CPU #19 warning: "can't bind memory"
[2020-02-28 13:36:38.473] CPU #20 warning: "can't bind memory"
[2020-02-28 13:36:38.495] CPU #21 warning: "can't bind memory"
[2020-02-28 13:36:38.517] CPU #22 warning: "can't bind memory"
[2020-02-28 13:36:38.539] CPU #24 warning: "can't bind memory"
[2020-02-28 13:36:38.561] CPU #25 warning: "can't bind memory"
[2020-02-28 13:36:38.583] CPU #26 warning: "can't bind memory"
[2020-02-28 13:36:38.605] CPU #27 warning: "can't bind memory"
[2020-02-28 13:36:38.627] CPU #28 warning: "can't bind memory"
[2020-02-28 13:36:38.649] CPU #29 warning: "can't bind memory"
[2020-02-28 13:36:38.671] CPU #30 warning: "can't bind memory"
[2020-02-28 13:36:38.674]  cpu  READY threads 2

I am wondering what I am doing wrong as the same routine works on a dual Xeon E5-2699 V4. I have all main memory channels populated with DDR3 ECC server ram.

[2020-02-28 13:41:47.807] speed 10s/60s/15m 615.6 615.6 n/a H/s max 615.9 H/s

Only a small fraction of hashrate the bare metal system is capable of. I am wondering if a bios setting isn't right?

# Discussion History
## xmrig | 2020-02-29T09:38:26+00:00
Hard to say... `can't bind memory` error usually mean NUMA node has no local memory, but errors too many and you confirm configuration is correct, also miner can't allocate memory for RandomX dataset (2080 MB per NUMA node), but you have more than enough memory installed. It looks very strange.

Try disable [NUMA](https://github.com/xmrig/xmrig/blob/master/src/config.json#L22) and/or [huge pages](https://github.com/xmrig/xmrig/blob/master/src/config.json#L26).
Thank you.

## agentpatience | 2020-02-29T14:51:32+00:00
Ok I am going to try resetting bios to optimal defaults and reinstalling I notice when I recompile I see a warning FWIW
![D1BF29CC-3C45-4F73-8B12-E90F1D337443](https://user-images.githubusercontent.com/36264810/75609732-0b2b1f80-5ad9-11ea-9408-dda81ffa5121.jpeg)
 

## agentpatience | 2020-02-29T17:07:06+00:00
Seems to be OS related... Manjaro is working on the same system. 5300+ h/S.

## ValoWaking | 2020-03-01T00:17:42+00:00
just try openBSD...

## whsyu | 2020-03-07T11:13:33+00:00
how about using ports/pkg? (clang though)
https://www.freshports.org/net-p2p/xmrig/

## xq0404 | 2021-07-11T01:21:45+00:00
> 
> 
> Seems to be OS related... Manjaro is working on the same system. 5300+ h/S.

exactly.   It works fine under Windows 10, but not under Ubuntu or Fedora

# Action History
- Created by: agentpatience | 2020-02-29T01:45:53+00:00
- Closed at: 2021-04-12T14:59:45+00:00
