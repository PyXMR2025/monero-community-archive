---
title: Assertion failed on Apple M1
source_url: https://github.com/xmrig/xmrig/issues/2890
author: eparra
assignees: []
labels: []
created_at: '2022-01-23T21:33:00+00:00'
updated_at: '2022-01-25T14:54:00+00:00'
type: issue
status: closed
closed_at: '2022-01-25T14:54:00+00:00'
---

# Original Description
**Bug**

[2022-01-22 07:45:55.108]  opencl   KawPow program for period 705259 compiled (1009ms)
Assertion failed: (uv__has_active_reqs(req->loop)), function uv__queue_done, file src/threadpool.c, line 327.
zsh: abort      ./xmrig

**Hardware and SW**

 * ABOUT        XMRig/6.16.2 clang/12.0.5
 * LIBS         libuv/1.42.0 OpenSSL/1.1.1l hwloc/2.5.0
 * HUGE PAGES   unavailable
 * 1GB PAGES    unavailable
 * CPU          Apple M1 (1) 64-bit AES
                L2:8.0 MB L3:0.0 MB 8C/8T NUMA:1
 * MEMORY       15.0/16.0 GB (94%)
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       #0 Apple/OpenCL 1.2 (Nov 13 2021 00:45:09)
 * OPENCL GPU   #0 n/a Apple M1 1000 MHz cu:8 mem:2048/10922 MB
 * CUDA         disabled



# Discussion History
# Action History
- Created by: eparra | 2022-01-23T21:33:00+00:00
- Closed at: 2022-01-25T14:54:00+00:00
