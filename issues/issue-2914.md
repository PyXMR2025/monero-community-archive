---
title: Cannot use POCL
source_url: https://github.com/xmrig/xmrig/issues/2914
author: kayshinonome
assignees: []
labels: []
created_at: '2022-01-31T21:15:00+00:00'
updated_at: '2022-01-31T21:15:00+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
**Describe the bug**
I cannot use the OpenCL platform POCL in this program.

**To Reproduce**
Run the program with OpenCL enabled

**Expected behavior**
The POCL platform to be loaded and ran with this tool

**Required data**

Initial log:
```sh
 * ABOUT        XMRig/6.16.3 gcc/11.2.0
 * LIBS         libuv/1.43.0 OpenSSL/1.1.1m hwloc/2.7.0
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          AMD Ryzen 3 3250U with Radeon Graphics (1) 64-bit AES
                L2:1.0 MB L3:4.0 MB 2C/4T NUMA:1
 * MEMORY       2.6/5.8 GB (45%)
 * DONATE       0%
 * ASSEMBLY     auto:ryzen
 * POOL #1      stratum+ssl://randomx.xmrig.com:443 algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled (failed to load OpenCL runtime)
 * CUDA         disabled
 ```
Command line:
`./xmrig --stress --opencl`

Uname
`Linux 14-dk1xxx 5.15.0-3-amd64 #1 SMP Debian 5.15.15-1 (2022-01-18) x86_64 GNU/Linux`

**Additional context**
POCL should enable OpenCL for my cpu, but it cannot load the runtime (I checked my installation with hashcat, and that worked)


# Discussion History
# Action History
- Created by: kayshinonome | 2022-01-31T21:15:00+00:00
