---
title: Process automatically gets killed
source_url: https://github.com/xmrig/xmrig/issues/2370
author: abhibagul
assignees: []
labels: []
created_at: '2021-05-12T11:44:41+00:00'
updated_at: '2021-05-13T13:12:17+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
This is the log data

>  * ABOUT        XMRig/6.12.1 gcc/5.4.0
>  * LIBS         libuv/1.41.0 OpenSSL/1.1.1j hwloc/2.4.1
>  * HUGE PAGES   supported
>  * 1GB PAGES    disabled
>  * CPU          Intel(R) Xeon(R) Platinum 8259CL CPU @ 2.50GHz (1) 64-bit AES VM
>                 L2:1.0 MB L3:35.8 MB 1C/2T NUMA:1
>  * MEMORY       2.0/7.6 GB (27%)
>  * DONATE       1%
>  * ASSEMBLY     auto:intel
>  * POOL #1      rx.unmineable.com:3333 algo rx/0
>  * COMMANDS     hashrate, pause, resume, results, connection
>  * OPENCL       disabled
>  * CUDA         disabled
> [2021-05-12 11:39:17.017]  net      use pool rx.unmineable.com:3333  139.59.102.100
> [2021-05-12 11:39:17.018]  net      new job from rx.unmineable.com:3333 diff 100001 algo rx/0 height 2359235
> [2021-05-12 11:39:17.018]  cpu      use argon2 implementation AVX-512F
> [2021-05-12 11:39:17.027]  msr      msr kernel module is not available
> [2021-05-12 11:39:17.027]  msr      FAILED TO APPLY MSR MOD, HASHRATE WILL BE LOW
> [2021-05-12 11:39:17.027]  randomx  init dataset algo rx/0 (2 threads) seed d2e97cf50201e5f9...
> [2021-05-12 11:39:17.029]  randomx  allocated 2336 MB (2080+256) huge pages 0% 0/1168 +JIT (1 ms)
> [2021-05-12 11:39:17.978]  net      new job from rx.unmineable.com:3333 diff 100001 algo rx/0 height 2359235
> [2021-05-12 11:39:32.978]  net      new job from rx.unmineable.com:3333 diff 100001 algo rx/0 height 2359235
> [2021-05-12 11:39:37.779]  net      new job from rx.unmineable.com:3333 diff 100001 algo rx/0 height 2359236

and after that, it shows killed.

# Discussion History
## Spudz76 | 2021-05-13T13:12:17+00:00
Probably because cloud mining doesn't work.

# Action History
- Created by: abhibagul | 2021-05-12T11:44:41+00:00
