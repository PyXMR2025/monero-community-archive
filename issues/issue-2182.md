---
title: Radeon RX570 detection / OpenCL error
source_url: https://github.com/xmrig/xmrig/issues/2182
author: rfuegen
assignees: []
labels: []
created_at: '2021-03-14T21:43:38+00:00'
updated_at: '2021-03-14T21:55:25+00:00'
type: issue
status: closed
closed_at: '2021-03-14T21:55:25+00:00'
---

# Original Description
there are two RX570 GPUs in my rig, but xmrig  seems to detect four:

 * ABOUT        XMRig/6.8.0-mo1 gcc/4.8.5
 * LIBS         libuv/1.40.0 
 * HUGE PAGES   supported
 * 1GB PAGES    unavailable
 * CPU          AMD Ryzen 9 3900X 12-Core Processor (1) 64-bit AES
                threads:24
 * MEMORY       4.1/15.4 GB (27%)
 * DONATE       1%
 * ASSEMBLY     auto:ryzen
 * POOL #1      gulf.moneroocean.stream:10032 algo auto
 * COMMANDS     'h' hashrate, 'p' pause, 'r' resume, 's' results, 'c' connection
 * ADL          press e for health report
 * OPENCL       #0 AMD Accelerated Parallel Processing/OpenCL 2.1 AMD-APP (3110.6)
 * OPENCL GPU   #0 01:00.0 Radeon RX 570 Series (Ellesmere) 1366 MHz cu:32 mem:4048/8178 MB
 * OPENCL GPU   #1 0a:00.0 Radeon RX 570 Series (Ellesmere) 1366 MHz cu:32 mem:4048/8172 MB
 * CUDA         disabled
[2021-03-14 22:18:37.786]  benchmk   STARTING ALGO PERFORMANCE CALIBRATION (with 20 seconds round) 
[2021-03-14 22:18:37.786]  benchmk   Algo cn/r Preparation 
[2021-03-14 22:18:37.786]  cpu      use profile  *  (24 threads) scratchpad 2048 KB
[2021-03-14 22:18:37.789]  opencl   use profile  cn/2  (4 threads) scratchpad 2048 KB
|  # | GPU |  BUS ID | INTENSITY | WSIZE | MEMORY | NAME
*|  0 |   0 | 01:00.0 |       768 |     8 |   1536 | Radeon RX 570 Series (Ellesmere)
|  1 |   0 | 01:00.0 |       768 |     8 |   1536 | Radeon RX 570 Series (Ellesmere)
|  2 |   1 | 0a:00.0 |       768 |     8 |   1536 | Radeon RX 570 Series (Ellesmere)
|  3 |   1 | 0a:00.0 |       768 |     8 |   1536 | Radeon RX 570 Series (Ellesmere)*
[2021-03-14 22:18:38.343]  cpu      READY threads 24/24 (24) huge pages 100% 24/24 memory 49152 KB (557 ms)
[2021-03-14 22:18:38.375]  opencl   READY threads 4/4 (586 ms)

is this just a display issue or are there 2 threads per GPU? in "OPENCL GPU" lines, two cards are correctly detected.

with rebench-algo: true and cpu: enabled: true, xmrig crashes right after start:

[2021-03-14 22:18:38.343]  cpu      READY threads 24/24 (24) huge pages 100% 24/24 memory 49152 KB (557 ms)
[2021-03-14 22:18:38.375]  opencl   READY threads 4/4 (586 ms)
[2021-03-14 22:18:38.407]  opencl   error CL_INVALID_KERNEL_NAME when calling clCreateKernel for kernel cn1_1000
[2021-03-14 22:18:38.408]  opencl   thread #3 failed with error CL_INVALID_KERNEL_NAME
[2021-03-14 22:18:38.470]  opencl   error CL_INVALID_KERNEL_NAME when calling clCreateKernel for kernel cn1_1000
[2021-03-14 22:18:38.470]  opencl   thread #0 failed with error CL_INVALID_KERNEL_NAME
[2021-03-14 22:18:38.474]  opencl   error CL_INVALID_KERNEL_NAME when calling clCreateKernel for kernel cn1_1000
[2021-03-14 22:18:38.474]  opencl   thread #2 failed with error CL_INVALID_KERNEL_NAME
[2021-03-14 22:18:38.552]  opencl   error CL_INVALID_KERNEL_NAME when calling clCreateKernel for kernel cn1_1000
[2021-03-14 22:18:38.552]  opencl   thread #1 failed with error CL_INVALID_KERNEL_NAME
[2021-03-14 22:18:38.746]  signal   Ctrl+C received, exiting
Segmentation fault (core dumped)

OS is Centos8 kernel 4.18.0-240.10.1.el8_3.x86_64
amd-gpu-pro is 20-20-1089974

when mining XHV on CPU+2*GPU, power and fan speed do not match as reported by xmrig (above) and sensors (below):

[2021-03-14 22:40:56.063]  opencl   #0 01:00.0   0W  0C    0RPM 0/0MHz
[2021-03-14 22:40:56.063]  opencl   #1 0a:00.0  61W 48C 1154RPM 600/2000MHz
[2021-03-14 22:40:56.063]  miner    speed 10s/60s/15m 2267.4 2331.2 n/a H/s max 2430.0 H/s

amdgpu-pci-0100
Adapter: PCI adapter
vddgfx:       +0.95 V  
fan1:        1198 RPM  (min =    0 RPM, max = 4500 RPM)
edge:         +46.0°C  (crit = +94.0°C, hyst = -273.1°C)
power1:       71.24 W  (cap = 135.00 W)

amdgpu-pci-0a00
Adapter: PCI adapter
vddgfx:       +0.95 V  
fan1:        1286 RPM  (min =    0 RPM, max = 4500 RPM)
edge:         +45.0°C  (crit = +94.0°C, hyst = -273.1°C)
power1:       60.19 W  (cap = 135.00 W)

I'm not that worried about what is printed on the screen, but would like to run a full rebench for CPU+GPU.

tnx

# Discussion History
## SChernykh | 2021-03-14T21:51:19+00:00
> there are two RX570 GPUs in my rig, but xmrig seems to detect four:

It detects two GPUs, uses two threads per GPU. 2*2=4

> with rebench-algo: true and cpu: enabled: true, xmrig crashes right after start:

This is MoneroOcean version, not stock XMRig. Report it to MoneroOcean.

# Action History
- Created by: rfuegen | 2021-03-14T21:43:38+00:00
- Closed at: 2021-03-14T21:55:25+00:00
