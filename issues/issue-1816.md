---
title: OpenCL error in Arch
source_url: https://github.com/xmrig/xmrig/issues/1816
author: phenax
assignees: []
labels: []
created_at: '2020-08-25T13:24:15+00:00'
updated_at: '2020-08-25T15:25:27+00:00'
type: issue
status: closed
closed_at: '2020-08-25T15:25:27+00:00'
---

# Original Description
**Describe the bug**
Getting an error using opencl.
```
Abort was called at 110 line in file:
/build/intel-compute-runtime/src/compute-runtime-20.30.17454/opencl/source/os_interface/linux/drm_command_stream.inl
```

**To Reproduce**
Not sure.

**Required data**
 - **OS:** Artix Linux (Arch)
 - **Graphics:** Intel UHD Graphics 620
```
$ xmrig --coin monero -o {url} -u {user} -p {pass} --opencl --opencl-platform=0

 * ABOUT        XMRig/6.3.1 gcc/10.1.0
 * LIBS         libuv/1.38.1 OpenSSL/1.1.1g hwloc/2.2.0
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          Intel(R) Core(TM) i7-8565U CPU @ 1.80GHz (1) x64 AES
                L2:1.0 MB L3:8.0 MB 4C/8T NUMA:1
 * MEMORY       4.3/31.2 GB (14%)
 * DONATE       1%
 * ASSEMBLY     auto:intel
 * POOL #1      {url} coin monero
 * COMMANDS     hashrate, pause, resume, results, connection
 * ADL          disabled (failed to load ADL)
 * OPENCL       #0 Intel(R) OpenCL HD Graphics/OpenCL 2.1
 * OPENCL GPU   #0 n/a Intel(R) Gen9 HD Graphics NEO 1150 MHz cu:24 mem:4095/25536 MB
 * CUDA         disabled
[2020-08-25 18:28:32.582]  net      use pool xmr.pool.minergate.com:45700  49.12.80.39
[2020-08-25 18:28:32.582]  net      new job from xmr.pool.minergate.com:45700 diff 1000 algo rx/0 height 2172178
[2020-08-25 18:28:32.582]  cpu      use argon2 implementation AVX2
[2020-08-25 18:28:32.597]  msr      register values for "intel" preset has been set successfully (15 ms)
[2020-08-25 18:28:32.597]  randomx  init dataset algo rx/0 (8 threads) seed {}...
[2020-08-25 18:28:32.763]  randomx  allocated 2336 MB (2080+256) huge pages 100% 1168/1168 +JIT (166 ms)
[2020-08-25 18:28:37.293]  randomx  dataset ready (4530 ms)
[2020-08-25 18:28:37.293]  cpu      use profile  *  (7 threads) scratchpad 2048 KB
[2020-08-25 18:28:37.414]  cpu      READY threads 7/7 (7) huge pages 100% 7/7 memory 14336 KB (121 ms)
[2020-08-25 18:28:37.434]  opencl   use profile  rx  (1 thread) scratchpad 2048 KB
|  # | GPU |  BUS ID | INTENSITY | WSIZE | MEMORY | NAME
|  0 |   0 |     n/a |       384 |     8 |    768 | Intel(R) Gen9 HD Graphics NEO
[2020-08-25 18:28:38.569]  cpu      accepted (1/0) diff 1000 (187 ms)
[2020-08-25 18:28:38.722]  opencl   READY threads 1/1 (360 ms)
[2020-08-25 18:28:39.272]  cpu      accepted (2/0) diff 1000 (211 ms)
[2020-08-25 18:28:39.869]  cpu      accepted (3/0) diff 1000 (160 ms)
[2020-08-25 18:28:40.682]  cpu      accepted (4/0) diff 1000 (234 ms)
[2020-08-25 18:28:40.682]  cpu      accepted (5/0) diff 1000 (200 ms)
[2020-08-25 18:28:40.769]  cpu      accepted (6/0) diff 1000 (179 ms)
[2020-08-25 18:28:41.172]  cpu      accepted (7/0) diff 1000 (160 ms)
[2020-08-25 18:28:41.268]  cpu      accepted (8/0) diff 1000 (232 ms)
Abort was called at 110 line in file:
/build/intel-compute-runtime/src/compute-runtime-20.30.17454/opencl/source/os_interface/linux/drm_command_stream.inl
```

**Additional context**
I've built xmrig from source and I'm using [`intel-compute-runtime`](https://www.archlinux.org/packages/community/x86_64/intel-compute-runtime/) package.


# Discussion History
## SChernykh | 2020-08-25T15:12:03+00:00
RandomX OpenCL code has never been tested on Intel HD graphics, it's not a supported configuration. Moreover, even if it works, it'll only slow down CPU cores and you'll have lower hashrate than without it. It's best to remove OpenCL from command line.

## phenax | 2020-08-25T15:25:27+00:00
Alright. Thanks for the quick response!

# Action History
- Created by: phenax | 2020-08-25T13:24:15+00:00
- Closed at: 2020-08-25T15:25:27+00:00
