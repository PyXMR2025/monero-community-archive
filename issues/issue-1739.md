---
title: Xmrig killed after allocating memory when using Intel Xeon Gold 6130
source_url: https://github.com/xmrig/xmrig/issues/1739
author: tatatata-group
assignees: []
labels:
- question
created_at: '2020-06-23T05:42:47+00:00'
updated_at: '2020-08-19T01:11:27+00:00'
type: issue
status: closed
closed_at: '2020-08-19T01:11:27+00:00'
---

# Original Description
 * ABOUT        XMRig/5.11.3 gcc/5.4.0
 * LIBS         libuv/1.38.0 OpenSSL/1.1.1g hwloc/2.2.0
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          Intel(R) Xeon(R) Gold 6130 CPU @ 2.10GHz (1) x64 AES
                L2:4.0 MB L3:88.0 MB 4C/4T NUMA:1
 * MEMORY       21.4/31.4 GB (68%)
 * DONATE       1%
 * ASSEMBLY     auto:intel
 * POOL #1      xmr.f2pool.com:13531 algo auto
 * COMMANDS     hashrate, pause, resume
 * OPENCL       disabled
 * CUDA         disabled
[2020-06-23 05:41:44.112]  net  use pool xmr.f2pool.com:13531  47.101.30.124
[2020-06-23 05:41:44.112]  net  new job from xmr.f2pool.com:13531 diff 32768 algo rx/0 height 2126713
[2020-06-23 05:41:44.112]  cpu  use argon2 implementation AVX2
[2020-06-23 05:41:44.119]  msr  msr kernel module is not available
[2020-06-23 05:41:44.119]  rx   init dataset algo rx/0 (3 threads) seed b6505d9163d9ad23...
[2020-06-23 05:41:44.120]  rx   allocated 2336 MB (2080+256) huge pages 0% 0/1168 +JIT (1 ms)
**Killed**

# Discussion History
## xmrig | 2020-06-23T06:04:58+00:00
`Killed` means application was killed by OOM killer it might be due your virtual machine settings.
Thank you.

# Action History
- Created by: tatatata-group | 2020-06-23T05:42:47+00:00
- Closed at: 2020-08-19T01:11:27+00:00
