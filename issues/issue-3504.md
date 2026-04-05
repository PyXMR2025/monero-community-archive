---
title: NVIDIA CUDA error in Arch linux
source_url: https://github.com/xmrig/xmrig/issues/3504
author: liberteryen
assignees: []
labels: []
created_at: '2024-06-28T19:22:24+00:00'
updated_at: '2025-06-18T22:39:03+00:00'
type: issue
status: closed
closed_at: '2025-06-18T22:39:03+00:00'
---

# Original Description
xmrig does not use cuda


➜  xmrig git:(master) ✗ xmrig --version
XMRig 6.21.3
 built on Apr 24 2024 with GCC 13.2.1
 features: 64-bit AES

libuv/1.48.0
OpenSSL/3.2.1
hwloc/2.10.0

I tried the one in the arch linux repositories and the manually compiled version (latest)
 command
 xmrig --threads=16 --url=MONEROD --user=wallet --coin monero  --cuda --proxy=socks5://127.0.0.1:9050       --tls --1gb-pages

OUTPUT:
Driver does not support CUDA 12.5 API! Update your nVidia driver!
 * ABOUT        XMRig/6.21.3 gcc/13.2.1 (built for Linux x86-64, 64 bit)
 * LIBS         libuv/1.48.0 OpenSSL/3.2.1 hwloc/2.10.0
 * HUGE PAGES   supported
 * 1GB PAGES    supported
 * CPU          12th Gen Intel(R) Core(TM) i7-12650H (1) 64-bit AES
                L2:9.5 MB L3:24.0 MB 10C/16T NUMA:1
 * MEMORY       6.2/31.1 GB (20%)
 * DONATE       1%
 * ASSEMBLY     auto:intel
 * POOL #1      hashvault.com:18081 coin Monero
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
Driver does not support CUDA 12.5 API! Update your nVidia driver!
 * CUDA         disabled (no devices)


cuda was installed both with the runfile and from the arch linux repositories and tested separately.

Detected 1 CUDA Capable device(s)

Device 0: "NVIDIA GeForce RTX 3050 Laptop GPU"
  CUDA Driver Version / Runtime Version          12.4 / 12.5
  CUDA Capability Major/Minor version number:    8.6
  Total amount of global memory:                 3895 MBytes (4084137984 bytes)
  (16) Multiprocessors, (128) CUDA Cores/MP:     2048 CUDA Cores
  GPU Max Clock rate:                            1500 MHz (1.50 GHz)
  Memory Clock rate:                             6001 Mhz
  Memory Bus Width:                              128-bit
  L2 Cache Size:                                 1572864 bytes
  Maximum Texture Dimension Size (x,y,z)         1D=(131072), 2D=(131072, 65536), 3D=(16384, 16384, 16384)
  Maximum Layered 1D Texture Size, (num) layers  1D=(32768), 2048 layers
  Maximum Layered 2D Texture Size, (num) layers  2D=(32768, 32768), 2048 layers
  Total amount of constant memory:               65536 bytes
  Total amount of shared memory per block:       49152 bytes
  Total number of registers available per block: 65536
  Warp size:                                     32
  Maximum number of threads per multiprocessor:  1536
  Maximum number of threads per block:           1024
  Max dimension size of a thread block (x,y,z): (1024, 1024, 64)
  Max dimension size of a grid size    (x,y,z): (2147483647, 65535, 65535)
  Maximum memory pitch:                          2147483647 bytes
  Texture alignment:                             512 bytes
  Concurrent copy and kernel execution:          Yes with 2 copy engine(s)
  Run time limit on kernels:                     Yes
  Integrated GPU sharing Host Memory:            No
  Support host page-locked memory mapping:       Yes
  Alignment requirement for Surfaces:            Yes
  Device has ECC support:                        Disabled
  Device supports Unified Addressing (UVA):      Yes
  Device supports Compute Preemption:            Yes
  Supports Cooperative Kernel Launch:            Yes
  Supports MultiDevice Co-op Kernel Launch:      Yes
  Device PCI Domain ID / Bus ID / location ID:   0 / 1 / 0
  Compute Mode:
     < Default (multiple host threads can use ::cudaSetDevice() with device simultaneously) >

deviceQuery, CUDA Driver = CUDART, CUDA Driver Version = 12.4, CUDA Runtime Version = 12.5, NumDevs = 1, Device0 = NVIDIA GeForce RTX 3050 Laptop GPU
Result = PASS

 
 


# Discussion History
## SChernykh | 2024-06-28T20:35:46+00:00
> Driver does not support CUDA 12.5 API

I guess this is the problem, 12.4 < 12.5:

> CUDA Driver Version = 12.4

## liberteryen | 2024-07-03T19:23:06+00:00
> > Driver does not support CUDA 12.5 API
> 
> I guess this is the problem, 12.4 < 12.5:
> 
> > CUDA Driver Version = 12.4

but I nstalled 
```bash 
1 extra/cuda 12.5.0-1 (1.7 GiB 4.7 GiB) (Kuruldu)
    NVIDIA's GPU programming toolkit
```
    

## AlpineVibrations | 2024-08-13T00:08:59+00:00
> > > Driver does not support CUDA 12.5 API
> > 
> > 
> > I guess this is the problem, 12.4 < 12.5:
> > > CUDA Driver Version = 12.4
> 
> but I nstalled
> 
> ```shell
> 1 extra/cuda 12.5.0-1 (1.7 GiB 4.7 GiB) (Kuruldu)
>     NVIDIA's GPU programming toolkit
> ```

did you ever figure this out?

# Action History
- Created by: liberteryen | 2024-06-28T19:22:24+00:00
- Closed at: 2025-06-18T22:39:03+00:00
