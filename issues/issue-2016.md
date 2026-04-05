---
title: GPU mining crash
source_url: https://github.com/xmrig/xmrig/issues/2016
author: zephyr91
assignees: []
labels: []
created_at: '2020-12-31T19:48:16+00:00'
updated_at: '2021-01-10T01:10:02+00:00'
type: issue
status: closed
closed_at: '2021-01-10T01:10:02+00:00'
---

# Original Description
I've got my old 2010 notebook Vostro3300 to work for mining a bit of monero and was doing good with CPU, then I configured the GPU drivers over Bumblebee (integrated+dedicated cards) and tried to make XMRIG to work on it with OpenCL
- it detects fine the GPU and its details (Geforce 310M)
- it crashes after the "dataset ready"

- OS: Debian Linux 10

**To Reproduce**
Starting the process makes it happen

#
#### Config ####
#
{
    "api": {
        "id": null,
        "worker-id": null
    },
    "http": {
        "enabled": false,
        "host": "127.0.0.1",
        "port": 0,
        "access-token": null,
        "restricted": true
    },
    "autosave": true,
    "background": false,
    "colors": true,
    "title": true,
    "randomx": {
        "init": -1,
        "init-avx2": -1,
        "mode": "auto",
        "1gb-pages": false,
        "rdmsr": true,
        "wrmsr": true,
        "cache_qos": false,
        "numa": true,
        "scratchpad_prefetch_mode": 1
    },
    "cpu": {
        "enabled": true,
        "huge-pages": true,
        "huge-pages-jit": false,
        "hw-aes": null,
        "priority": 5,
        "memory-pool": false,
        "yield": true,
        "asm": true,
        "argon2-impl": null,
        "astrobwt-max-size": 550,
        "astrobwt-avx2": false,
        "argon2": [0, 1, 2],
        "astrobwt": [0, 2, 1, 3],
        "cn": [
            [1, 0],
            [1, 1]
        ],
        "cn-heavy": [
            [1, 0]
        ],
        "cn-lite": [
            [1, 0],
            [1, 1],
            [1, 2]
        ],
        "cn-pico": [
            [2, 0],
            [2, 2],
            [2, 1],
            [2, 3]
        ],
        "rx": [0, 1],
        "rx/arq": [0, 2, 1, 3],
        "rx/wow": [0, 1, 2],
        "cn/0": false,
        "cn-lite/0": false,
        "rx/keva": "rx/wow"
    },
    "opencl": {
        "enabled": true,
        "cache": true,
        "loader": null,
        "platform": "NVIDIA",
        "adl": true,
        "kawpow": [
            {
                "index": 0,
                "intensity": 524288,
                "worksize": 256,
                "threads": [-1]
            }
        ],
        "rx": [
            {
                "index": 0,
                "intensity": 64,
                "worksize": 8,
                "threads": [-1],
                "bfactor": 6,
                "gcn_asm": false,
                "dataset_host": true
            }
        ],
        "rx/arq": [
            {
                "index": 0,
                "intensity": 896,
                "worksize": 8,
                "threads": [-1],
                "bfactor": 6,
                "gcn_asm": false,
                "dataset_host": true
            }
        ],
        "rx/wow": [
            {
                "index": 0,
                "intensity": 192,
                "worksize": 8,
                "threads": [-1],
                "bfactor": 6,
                "gcn_asm": false,
                "dataset_host": true
            }
        ],
        "cn/0": false,
        "cn-lite/0": false
    },
    "cuda": {
        "enabled": false,
        "loader": null,
        "nvml": true
    },
    "log-file": "xmrig.out",
    "donate-level": 1,
    "donate-over-proxy": 1,
    "pools": [
        {
            "algo": null,
            "coin": null,
            "url": "pool.supportxmr.com:443",
            "rig-id": null,
            "nicehash": false,
            "keepalive": true,
            "enabled": true,
            "tls": true,
            "tls-fingerprint": null,
            "daemon": false,
            "socks5": null,
            "self-select": null
        }
    ],
    "retries": 5,
    "retry-pause": 5,
    "print-time": 60,
    "health-print-time": 60,
    "syslog": false,
    "tls": {
        "enabled": false,
        "protocols": null,
        "cert": null,
        "cert_key": null,
        "ciphers": null,
        "ciphersuites": null,
        "dhparam": null
    },
    "user-agent": null,
    "verbose": 1,
    "watch": true,
    "pause-on-battery": false
}

#
#### Miner Output ####
#
 * ABOUT        XMRig/6.7.0 gcc/5.4.0
 * LIBS         libuv/1.40.0 OpenSSL/1.1.1i hwloc/2.4.0
 * HUGE PAGES   supported
 * 1GB PAGES    unavailable
 * CPU          Intel(R) Core(TM) i5 CPU M 560 @ 2.67GHz (1) 64-bit AES
                L2:0.5 MB L3:3.0 MB 2C/4T NUMA:1
 * MEMORY       2.8/5.6 GB (49%)
 * DONATE       1%
 * ASSEMBLY     auto:intel
 * POOL #1      pool.supportxmr.com:443 algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
[2020-12-31 16:28:42.664]  config   configuration saved to: "moneyfarm.json"
 * ADL          disabled (failed to load ADL)
 * OPENCL       #0 NVIDIA CUDA/OpenCL 1.1 CUDA 6.5.51
 * OPENCL GPU   #0 01:00.0 GeForce 310M 1530 MHz cu:2 mem:128/511 MB
 * CUDA         disabled
[2020-12-31 16:28:43.243]  net      use pool pool.supportxmr.com:443 TLSv1.2 104.140.201.42
[2020-12-31 16:28:43.243]  net      new job from pool.supportxmr.com:443 diff 50000 algo rx/0 height 2264462
[2020-12-31 16:28:43.243]  cpu      use argon2 implementation SSSE3
[2020-12-31 16:28:43.250]  msr      msr kernel module is not available
[2020-12-31 16:28:43.250]  msr      FAILED TO APPLY MSR MOD, HASHRATE WILL BE LOW
[2020-12-31 16:28:43.250]  randomx  init dataset algo rx/0 (4 threads) seed 64b3ef81a40e2501...
[2020-12-31 16:28:43.250]  randomx  allocated 2336 MB (2080+256) huge pages 0% 0/1168 +JIT (1 ms)
 - CONNECTION
 * pool address     pool.supportxmr.com:443 (104.140.201.42) TLSv1.2
 * algorithm        rx/0
 * difficulty       50000
 * connection time  3s
[2020-12-31 16:28:52.762] no any results yet
[2020-12-31 16:28:57.681]  net      new job from pool.supportxmr.com:443 diff 76272 algo rx/0 height 2264462
[2020-12-31 16:28:57.682] no any results yet
[2020-12-31 16:28:59.733] no any results yet
[2020-12-31 16:29:00.587] no any results yet
[2020-12-31 16:29:01.641]  randomx  dataset ready (18391 ms)
[2020-12-31 16:29:01.642]  cpu      use profile  rx  (2 threads) scratchpad 2048 KB
[2020-12-31 16:29:01.644]  cpu      READY threads 2/2 (2) huge pages 0% 0/2 memory 4096 KB (2 ms)
[2020-12-31 16:29:01.690]  opencl   use profile  rx  (1 thread) scratchpad 2048 KB
|  # | GPU |  BUS ID | INTENSITY | WSIZE | MEMORY | NAME
|  0 |   0 | 01:00.0 |        64 |     8 |    128 | GeForce 310M
|    CPU # | AFFINITY | 10s H/s | 60s H/s | 15m H/s |
|        0 |        0 |     n/a |     n/a |     n/a |
|        1 |        1 |     n/a |     n/a |     n/a |
|        - |        - |     n/a |     n/a |     n/a |
| OPENCL # | AFFINITY | 10s  H/s | 60s  H/s | 15m  H/s |
|        0 |       -1 |      n/a |      n/a |      n/a | #0 01:00.0 GeForce 310M
|        - |        - |      n/a |      n/a |      n/a |
[2020-12-31 16:29:01.860]  miner    speed 10s/60s/15m n/a n/a n/a H/s max n/a H/s
[2020-12-31 16:29:01.860] SIGSEGV at (nil)
Aborted

#
#### GPU CLINFO ####
#
Number of platforms                               1
  Platform Name                                   NVIDIA CUDA
  Platform Vendor                                 NVIDIA Corporation
  Platform Version                                OpenCL 1.1 CUDA 6.5.51
  Platform Profile                                FULL_PROFILE
  Platform Extensions                             cl_khr_byte_addressable_store cl_khr_icd cl_khr_gl_sharing cl_nv_compiler_options cl_nv_device_attribute_query cl_nv_pragma_unroll cl_nv_copy_opts 
  Platform Extensions function suffix             NV

  Platform Name                                   NVIDIA CUDA
Number of devices                                 1
  Device Name                                     GeForce 310M
  Device Vendor                                   NVIDIA Corporation
  Device Vendor ID                                0x10de
  Device Version                                  OpenCL 1.0 CUDA
  Driver Version                                  340.108
  Device OpenCL C Version                         OpenCL C 1.1 
  Device Type                                     GPU
  Device Topology (NV)                            PCI-E, 01:00.0
  Device Profile                                  FULL_PROFILE
  Device Available                                Yes
  Compiler Available                              Yes
  Max compute units                               2
  Max clock frequency                             1530MHz
  Compute Capability (NV)                         1.2
  Max work item dimensions                        3
  Max work item sizes                             512x512x64
  Max work group size                             512
  Preferred work group size multiple              32
  Warp size (NV)                                  32
  Preferred / native vector sizes                 
    char                                                 1 / 1       
    short                                                1 / 1       
    int                                                  1 / 1       
    long                                                 1 / 1       
    half                                                 0 / 0        (n/a)
    float                                                1 / 1       
    double                                               0 / 0        (n/a)
  Half-precision Floating-point support           (n/a)
  Single-precision Floating-point support         (core)
    Denormals                                     No
    Infinity and NANs                             Yes
    Round to nearest                              Yes
    Round to zero                                 Yes
    Round to infinity                             Yes
    IEEE754-2008 fused multiply-add               Yes
    Support is emulated in software               No
    Correctly-rounded divide and sqrt operations  No
  Double-precision Floating-point support         (n/a)
  Address bits                                    32, Little-Endian
  Global memory size                              536608768 (511.8MiB)
  Error Correction support                        No
  Max memory allocation                           134217728 (128MiB)
  Unified memory for Host and Device              No
  Integrated memory (NV)                          No
  Minimum alignment for any data type             128 bytes
  Alignment of base address                       2048 bits (256 bytes)
  Global Memory cache type                        None
  Image support                                   Yes
    Max number of samplers per kernel             16
    Max 2D image size                             4096x16383 pixels
    Max 3D image size                             2048x2048x2048 pixels
    Max number of read image args                 128
    Max number of write image args                8
  Local memory type                               Local
  Local memory size                               16384 (16KiB)
  Registers per block (NV)                        16384
  Max number of constant args                     9
  Max constant buffer size                        65536 (64KiB)
  Max size of kernel argument                     4352 (4.25KiB)
  Queue properties                                
    Out-of-order execution                        Yes
    Profiling                                     Yes
  Profiling timer resolution                      1000ns
  Execution capabilities                          
    Run OpenCL kernels                            Yes
    Run native kernels                            No
    Kernel execution timeout (NV)                 No
  Concurrent copy and kernel execution (NV)       Yes
    Number of async copy engines                  1
  Device Extensions                               cl_khr_byte_addressable_store cl_khr_icd cl_khr_gl_sharing cl_nv_compiler_options cl_nv_device_attribute_query cl_nv_pragma_unroll cl_nv_copy_opts  cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics 

NULL platform behavior
  clGetPlatformInfo(NULL, CL_PLATFORM_NAME, ...)  NVIDIA CUDA
  clGetDeviceIDs(NULL, CL_DEVICE_TYPE_ALL, ...)   Success [NV]
  clCreateContext(NULL, ...) [default]            Success [NV]
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_DEFAULT)  No platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_CPU)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_GPU)  No platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_ACCELERATOR)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_CUSTOM)  Invalid device type for platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_ALL)  No platform

ICD loader properties
  ICD loader Name                                 OpenCL ICD Loader
  ICD loader Vendor                               OCL Icd free software
  ICD loader Version                              2.2.12
  ICD loader Profile                              OpenCL 2.2


**Additional context**
Noticed that after the crash I see that the O.S doesn't release the RAM and it stay pined and on syslog it gives OOM.

Dec 31 16:44:54 host1 kernel: [ 1598.742403] Out of memory: Kill process 1979 (xmrig) score 269 or sacrifice child
Dec 31 16:44:54 host1 kernel: [ 1598.742494] Killed process 1979 (xmrig) total-vm:2894456kB, anon-rss:589492kB, file-rss:12680kB, shmem-rss:0kB
Dec 31 16:44:54 host1 kernel: [ 1599.166676] NVRM: failed to copy out ioctl data
Dec 31 16:44:54 host1 kernel: [ 1599.166684] NVRM: nvidia_frontend_ioctl: minor 0, module->ioctl failed, error -14
Dec 31 16:44:55 host1 kernel: [ 1599.500403] oom_reaper: reaped process 1979 (xmrig), now anon-rss:0kB, file-rss:13324kB, shmem-rss:0kB



# Discussion History
## Lonnegan | 2021-01-01T12:07:38+00:00
You shouldn't mine Monero (algo RandomX) with a GPU. RandomX is a pure CPU algo, even high end GPUs perform completely bad in RandomX (which was a design target of RandomX). Mine Monero with the CPU and let the GPU idle, because the 310M is so weak that it's not worth to invest time and electricity. Even with a good GPU algo you'd only mine a few Cent per week with this GPU!

## SChernykh | 2021-01-01T13:49:08+00:00
You need to free up more memory before starting XMRig, or you'll keep getting OOM killer triggered even with GPU disabled.

## Lonnegan | 2021-01-01T14:08:02+00:00
@zephyr91 I've just recognized that even your CPU is not ideal for Monero mining, because the L3 cache of your CPU is too small. You should consider to mine Wownero via CPU. With that algo you can at least work with 3 threads, whereas with Monero the cache is just 2/3 filled with 1 thread and already  flooded with 2 threads.

## zephyr91 | 2021-01-01T15:51:58+00:00
So wownero in this hardware would be more worthy? Any place i can find basic configurations to start with wownero mining in xmrig or pools?

Thanks in advance for the help

## Lonnegan | 2021-01-01T16:03:07+00:00
It's not worth mining with your hardware, neither Monero, nor Wownero. Far too little hashrate with far too much power consumption. So you won't get rich with this. ;)

But for testing and playing around, Wownero would be best for your CPU. Here you can find pools (incl. config help for each), links to the project website (incl. wallet), to project's Github, to exchanges supporting Wownero, ...
https://miningpoolstats.stream/wownero

## zephyr91 | 2021-01-01T18:22:21+00:00
Currently with my 3 notebooks I'm getting 1.1MH/S on monero, two of them were just there in the closet so i think that with the combined power it could give me few moneros/wowneros.

I'm just not sure how to check how much power those 3 would consume. 

## Lonnegan | 2021-01-01T23:08:54+00:00
Ok, you get 1,100 H/s in Monero with your 3 laptops. Not bad, but one single Ryzen 9 PC hashes at about 14,000 H/s  consuming not much more power than your 3 laptops since your Core i5-560M are 35 W TDP parts.

If you really want to mine for profit and not just for fun or due to technical curiosity you should not mine with that hardware but build real mining rigs or at least use modern PC hardware.

If you want to find out which algo is more profitable with your hardware, first mine Monero and note the hashrates and then mine Wownero and note the hashrates.

Hashvault has a pool for Monero and Wownero and a profit calculator in each dashboard. There you can put in your hashrate values and check which coin gives YOU more profit.
https://monero.hashvault.pro/en/dashboard
https://wownero.hashvault.pro/en/dashboard

At the moment mining at 1,100 H/s your Monero profit is 0.08 USD per day: minus power consumtion! I don't know your Wownero hashrate, so I can't check it.

The next thing is: when you mine on a pool like supportxmr.com, which has a minimum payment height of 0.1 XMR it'll take you half a year of 24/7 mining with your 3 laptops to reach the first payment.

# Action History
- Created by: zephyr91 | 2020-12-31T19:48:16+00:00
- Closed at: 2021-01-10T01:10:02+00:00
