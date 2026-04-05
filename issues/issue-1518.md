---
title: failed to allocate RandomX datasets and cpu cant bind memory but i have 300gb
  of free ram
source_url: https://github.com/xmrig/xmrig/issues/1518
author: km7670672
assignees: []
labels:
- question
created_at: '2020-01-26T18:39:14+00:00'
updated_at: '2022-06-10T16:23:33+00:00'
type: issue
status: closed
closed_at: '2020-02-23T23:26:46+00:00'
---

# Original Description
failed to allocate RandomX datasets and cpu cant bind memory but i have 300gb of free ram

My cpu is intel xeon gold 5118 i have 2 of them in one server but i dont knew how to fix it 

# Discussion History
## SChernykh | 2020-01-27T08:36:52+00:00
Can you post your config and miner console full output?

## km7670672 | 2020-01-27T10:47:04+00:00
 
2020-01-27 10:45:18 (278 KB/s) - 'xmrig-5.5.1-xenial-x64.tar.gz.1' saved [4380571/4380571]
 
xmrig-5.5.1/
xmrig-5.5.1/config.json
xmrig-5.5.1/SHA256SUMS
xmrig-5.5.1/xmrig-notls
xmrig-5.5.1/xmrig
* ABOUT XMRig/5.5.1 gcc/5.4.0
* LIBS libuv/1.34.0 OpenSSL/1.1.1d hwloc/2.1.0
* HUGE PAGES supported
* 1GB PAGES disabled
* CPU Intel(R) Xeon(R) Gold 5118 CPU @ 2.30GHz (2) x64 AES
L2:24.0 MB L3:33.0 MB 24C/48T NUMA:2
* MEMORY 45.5/125.6 GB (36%)
* DONATE 1%
* ASSEMBLY auto:intel
* POOL #1 eu-de02.miningrigrentals.com:3333 algo rx/sfx
* COMMANDS hashrate, pause, resume
* OPENCL disabled
* CUDA disabled
[2020-01-27 10:45:20.754] net use pool eu-de02.miningrigrentals.com:3333 TLSv1.2 165.227.153.169
[2020-01-27 10:45:20.754] net fingerprint (SHA-256): "af48a22249072cc5e508a28cf24612d06c1c583672f36c705b13a126c8da50fa"
[2020-01-27 10:45:20.754] net new job from eu-de02.miningrigrentals.com:3333 diff 175004 algo rx/0 height 2020367
[2020-01-27 10:45:20.756] msr msr kernel module is not available
[2020-01-27 10:45:20.757] rx init datasets algo rx/0 (48 threads) seed a3a2a9049d3bc86d...
[2020-01-27 10:45:20.757] rx #0 skipped (can't bind memory)
[2020-01-27 10:45:20.757] rx #1 skipped (can't bind memory)
[2020-01-27 10:45:20.757] rx #0 allocated 256 MB huge pages 0% +JIT (0 ms)
[2020-01-27 10:45:20.757] rx failed to allocate RandomX datasets, switching to slow mode (1 ms)
[2020-01-27 10:45:21.625] rx #0 dataset ready (867 ms)
[2020-01-27 10:45:21.625] cpu use profile rx (24 threads) scratchpad 2048 KB
[2020-01-27 10:45:21.627] CPU #00 warning: "can't bind memory"
[2020-01-27 10:45:21.648] CPU #02 warning: "can't bind memory"
[2020-01-27 10:45:21.668] CPU #04 warning: "can't bind memory"
[2020-01-27 10:45:21.688] CPU #06 warning: "can't bind memory"
[2020-01-27 10:45:21.708] CPU #08 warning: "can't bind memory"
[2020-01-27 10:45:21.728] CPU #10 warning: "can't bind memory"
[2020-01-27 10:45:21.749] CPU #12 warning: "can't bind memory"
[2020-01-27 10:45:21.769] CPU #14 warning: "can't bind memory"
[2020-01-27 10:45:21.789] CPU #16 warning: "can't bind memory"
[2020-01-27 10:45:21.809] CPU #18 warning: "can't bind memory"
[2020-01-27 10:45:21.829] CPU #20 warning: "can't bind memory"
[2020-01-27 10:45:21.849] CPU #22 warning: "can't bind memory"
[2020-01-27 10:45:21.870] CPU #01 warning: "can't bind memory"
[2020-01-27 10:45:21.890] CPU #03 warning: "can't bind memory"
[2020-01-27 10:45:21.910] CPU #05 warning: "can't bind memory"
[2020-01-27 10:45:21.930] CPU #07 warning: "can't bind memory"
[2020-01-27 10:45:21.950] CPU #09 warning: "can't bind memory"
[2020-01-27 10:45:21.970] CPU #11 warning: "can't bind memory"
[2020-01-27 10:45:21.991] CPU #13 warning: "can't bind memory"
[2020-01-27 10:45:22.011] CPU #15 warning: "can't bind memory"
[2020-01-27 10:45:22.031] CPU #17 warning: "can't bind memory"
[2020-01-27 10:45:22.051] CPU #19 warning: "can't bind memory"
[2020-01-27 10:45:22.072] CPU #21 warning: "can't bind memory"
[2020-01-27 10:45:22.092] CPU #23 warning: "can't bind memory"
[2020-01-27 10:45:22.092] cpu READY threads 24/24 (24) huge pages 0% 0/24 memory 49152 KB (466 ms)

## SChernykh | 2020-01-27T11:09:13+00:00
Try to run xmrig as root, if it doesn't help - disable NUMA in config.

## km7670672 | 2020-01-27T11:23:29+00:00
I have already tried to run as root not helped and how can i disable numa in the config i think i have tried but also doesnt worked

## km7670672 | 2020-01-27T11:29:16+00:00
* ABOUT XMRig/5.5.1 gcc/5.4.0
* LIBS libuv/1.34.0 OpenSSL/1.1.1d hwloc/2.1.0
* HUGE PAGES supported
* 1GB PAGES disabled
* CPU Intel(R) Xeon(R) Gold 5118 CPU @ 2.30GHz (2) x64 AES
L2:24.0 MB L3:33.0 MB 24C/48T NUMA:2
* MEMORY 45.5/125.6 GB (36%)
* DONATE 1%
* ASSEMBLY auto:intel
* POOL #1 eu-de02.miningrigrentals.com:3333 algo rx/sfx
* COMMANDS hashrate, pause, resume
* OPENCL disabled
* CUDA disabled
[2020-01-27 11:27:38.722] net use pool eu-de02.miningrigrentals.com:3333 TLSv1.2 165.227.153.169
[2020-01-27 11:27:38.722] net fingerprint (SHA-256): "af48a22249072cc5e508a28cf24612d06c1c583672f36c705b13a126c8da50fa"
[2020-01-27 11:27:38.722] net new job from eu-de02.miningrigrentals.com:3333 diff 175004 algo rx/0 height 2020381
[2020-01-27 11:27:38.725] msr msr kernel module is not available
[2020-01-27 11:27:38.725] rx init dataset algo rx/0 (48 threads) seed a3a2a9049d3bc86d...
[2020-01-27 11:27:38.725] rx allocated 2336 MB (2080+256) huge pages 0% 0/1168 +JIT (0 ms)
[2020-01-27 11:27:40.978] rx dataset ready (2252 ms)
[2020-01-27 11:27:40.978] cpu use profile rx (24 threads) scratchpad 2048 KB
[2020-01-27 11:27:40.980] CPU #00 warning: "can't bind memory"
[2020-01-27 11:27:41.000] CPU #02 warning: "can't bind memory"
[2020-01-27 11:27:41.020] CPU #04 warning: "can't bind memory"
[2020-01-27 11:27:41.041] CPU #06 warning: "can't bind memory"
[2020-01-27 11:27:41.061] CPU #08 warning: "can't bind memory"
[2020-01-27 11:27:41.081] CPU #10 warning: "can't bind memory"
[2020-01-27 11:27:41.102] CPU #12 warning: "can't bind memory"
[2020-01-27 11:27:41.122] CPU #14 warning: "can't bind memory"
[2020-01-27 11:27:41.142] CPU #16 warning: "can't bind memory"
[2020-01-27 11:27:41.162] CPU #18 warning: "can't bind memory"
[2020-01-27 11:27:41.182] CPU #20 warning: "can't bind memory"
[2020-01-27 11:27:41.202] CPU #22 warning: "can't bind memory"
[2020-01-27 11:27:41.223] CPU #01 warning: "can't bind memory"
[2020-01-27 11:27:41.243] CPU #03 warning: "can't bind memory"
[2020-01-27 11:27:41.263] CPU #05 warning: "can't bind memory"
[2020-01-27 11:27:41.283] CPU #07 warning: "can't bind memory"
[2020-01-27 11:27:41.303] CPU #09 warning: "can't bind memory"
[2020-01-27 11:27:41.324] CPU #11 warning: "can't bind memory"
[2020-01-27 11:27:41.344] CPU #13 warning: "can't bind memory"
[2020-01-27 11:27:41.364] CPU #15 warning: "can't bind memory"
[2020-01-27 11:27:41.384] CPU #17 warning: "can't bind memory"
[2020-01-27 11:27:41.405] CPU #19 warning: "can't bind memory"
[2020-01-27 11:27:41.425] CPU #21 warning: "can't bind memory"
[2020-01-27 11:27:41.445] CPU #23 warning: "can't bind memory"
[2020-01-27 11:27:41.446] cpu READY threads 24/24 (24) huge pages 0% 0/24 memory 49152 KB (468 ms)
[2020-01-27 11:27:56.093] cpu accepted (1/0) diff 175004 (298 ms)
| CPU # | AFFINITY | 10s H/s | 60s H/s | 15m H/s |
| 0 | 0 | 262.3 | n/a | n/a |
| 1 | 2 | 263.9 | n/a | n/a |
| 2 | 4 | 267.2 | n/a | n/a |
| 3 | 6 | 268.5 | n/a | n/a |
| 4 | 8 | 264.2 | n/a | n/a |
| 5 | 10 | 267.5 | n/a | n/a |
| 6 | 12 | 273.2 | n/a | n/a |
| 7 | 14 | 265.2 | n/a | n/a |
| 8 | 16 | 264.5 | n/a | n/a |
| 9 | 18 | 262.0 | n/a | n/a |
| 10 | 20 | 272.9 | n/a | n/a |
| 11 | 22 | 263.2 | n/a | n/a |
| 12 | 1 | 266.2 | n/a | n/a |
| 13 | 3 | 250.2 | n/a | n/a |
| 14 | 5 | 269.4 | n/a | n/a |
| 15 | 7 | 266.7 | n/a | n/a |
| 16 | 9 | 267.8 | n/a | n/a |
| 17 | 11 | 266.7 | n/a | n/a |
| 18 | 13 | 252.2 | n/a | n/a |
| 19 | 15 | 265.3 | n/a | n/a |
| 20 | 17 | 268.7 | n/a | n/a |
| 21 | 19 | 265.3 | n/a | n/a |
| 22 | 21 | 267.7 | n/a | n/a |
| 23 | 23 | 266.4 | n/a | n/a |
| - | - | 6367.3 | n/a | n/a |
[2020-01-27 11:28:11.461] speed 10s/60s/15m 6367.3 n/a n/a H/s max 6381.2 H/s





But i again doesnt mine on all threads 

## SChernykh | 2020-01-27T15:27:45+00:00
24 threads is correct for dual Xeon Gold 5118. You should enable huge pages, maybe this is why you get "can't bind memory" errors.

## Spudz76 | 2020-01-27T20:33:17+00:00
Check `ulimit -l` and ensure it has not been turned down to moronic low levels.
Check hugepages.
What OS - I'm going to go ahead and guess CentOS since it's usually the one with moronic low defaults and "secure" as in won't run anything.

## km7670672 | 2020-01-28T10:06:50+00:00
Check result is 64 and od is ubuntu 16.4 lts

## xmrig | 2020-02-01T09:17:14+00:00
`"can't bind memory"` error means NUMA node where CPU located has no local memory, please check memory sticks installed in correct slots.
Thank you.

## kidigital101 | 2021-01-05T08:41:43+00:00
overheating 
shutdown 
open pc 
clean heatsink and fan 
cpu or memory burning up

## lexo-mfleuti | 2022-06-10T16:23:33+00:00
I fiddled with this now for several hours and the solution is most probably not software related. I documented it here:
https://www.lexo.ch/blog/2022/06/solved-xmrig-cpu-xx-warning-cant-bind-memory-xmrig-does-not-run-on-all-cpu-cores/

Hope this helps!

# Action History
- Created by: km7670672 | 2020-01-26T18:39:14+00:00
- Closed at: 2020-02-23T23:26:46+00:00
