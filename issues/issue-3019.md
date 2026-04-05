---
title: KILLED??? zsh error? supposed to use bash LINUX KALI
source_url: https://github.com/xmrig/xmrig/issues/3019
author: elonlvl
assignees: []
labels: []
created_at: '2022-04-15T01:56:05+00:00'
updated_at: '2025-06-28T10:40:09+00:00'
type: issue
status: closed
closed_at: '2025-06-28T10:40:09+00:00'
---

# Original Description
$ ./xmrig
 * ABOUT        XMRig/6.17.0 gcc/5.4.0
 * LIBS         libuv/1.43.0 OpenSSL/1.1.1m hwloc/2.7.0
 * HUGE PAGES   supported
 * 1GB PAGES    unavailable
 * CPU          Intel(R) Xeon(R) CPU X5550 @ 2.67GHz (1) 64-bit -AES
                L2:1.0 MB L3:8.0 MB 4C/4T NUMA:1
 * MEMORY       1.9/2.9 GB (67%)
 * DONATE       1%
 * ASSEMBLY     auto:none
 * POOL #1      rx.unmineable.com:3333 algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled (failed to load OpenCL runtime)
 * CUDA         disabled
[2022-04-14 21:44:05.360]  net      use pool rx.unmineable.com:3333  139.59.164.251
[2022-04-14 21:44:05.382]  net      new job from rx.unmineable.com:3333 diff 100001 algo rx/0 height 2602119 (4 tx)                                                                 
[2022-04-14 21:44:05.382]  cpu      use argon2 implementation SSSE3
[2022-04-14 21:44:06.583]  randomx  init dataset algo rx/0 (4 threads) seed 0de1f9117624f187...                                                                                     
[2022-04-14 21:44:06.621]  randomx  allocated 2336 MB (2080+256) huge pages 11% 128/1168 +JIT (38 ms)                                                                               
zsh: killed     ./xmrig


# Discussion History
## Spudz76 | 2022-04-15T05:16:49+00:00
Out of memory.

## bitmastercoin | 2022-04-16T05:11:30+00:00
what is memory ? like RAM?


## bitmastercoin | 2022-04-16T05:12:06+00:00
i am elonlvl, btw @Spudz76 


## Spudz76 | 2022-04-16T08:33:42+00:00
Yes

```
MEMORY 1.9/2.9 GB (67%)
```

You need 2080+256 = 2336MB of free RAM at least.

## bitmastercoin | 2022-04-17T03:51:56+00:00
finally i got my ram aligned . i am not sure but i have like 12 slots for RAM And all i had to do was rearrange some of the units into different slots and look now. ::
MEMORY       3.3/8.7 GB (38%)
its not much , but better than it was.. i may be able to rearrange it even better because if im not mistaken with 4 - 2GB RAM DDR3 and 1 -4GB RAM and 5 -1GB RAM doesnt that equal . 17 GB of ram???

# Action History
- Created by: elonlvl | 2022-04-15T01:56:05+00:00
- Closed at: 2025-06-28T10:40:09+00:00
