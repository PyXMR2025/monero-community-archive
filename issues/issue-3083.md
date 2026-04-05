---
title: msr kernel not available, failed to apply msr module
source_url: https://github.com/xmrig/xmrig/issues/3083
author: Dober-I
assignees: []
labels: []
created_at: '2022-07-06T10:45:32+00:00'
updated_at: '2022-07-06T16:08:04+00:00'
type: issue
status: closed
closed_at: '2022-07-06T16:08:04+00:00'
---

# Original Description
I ran my miners with Ubuntu and other is Debian in WSL, tried everything I could find online to fix this issue but nothing works, yes I run the xmrig with sudo

* ABOUT        XMRig/6.17.0 gcc/10.2.1
 * LIBS         libuv/1.40.0 OpenSSL/1.1.1n hwloc/2.4.1
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz (1) 64-bit AES VM
                L2:0.5 MB L3:3.0 MB 2C/4T NUMA:1
 * MEMORY       2.7/7.7 GB (35%)
 * DONATE       1%
 * ASSEMBLY     auto:intel
 * POOL #1      gulf.moneroocean.stream:10128 algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled
[2022-07-06 11:36:41.355]  net      use pool gulf.moneroocean.stream:10128  199.247.0.216
[2022-07-06 11:36:41.355]  net      new job from gulf.moneroocean.stream:10128 diff 128001 algo rx/0 height 2661284 (1 tx)
[2022-07-06 11:36:41.355]  cpu      use argon2 implementation AVX2
[2022-07-06 11:36:41.365]  msr      msr kernel module is not available
[2022-07-06 11:36:41.366]  msr      FAILED TO APPLY MSR MOD, HASHRATE WILL BE LOW

# Discussion History
# Action History
- Created by: Dober-I | 2022-07-06T10:45:32+00:00
- Closed at: 2022-07-06T16:08:04+00:00
