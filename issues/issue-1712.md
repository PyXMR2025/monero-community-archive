---
title: Crash on OpenCL enable Intel Plataform
source_url: https://github.com/xmrig/xmrig/issues/1712
author: gilandriani
assignees: []
labels: []
created_at: '2020-06-05T10:48:07+00:00'
updated_at: '2020-08-28T16:36:23+00:00'
type: issue
status: closed
closed_at: '2020-08-28T16:36:23+00:00'
---

# Original Description
**Describe the bug**
When opencl enable xmrig crash affter:  ocl  GPU #0 compiling...
free(): invalid pointer
Abortado


**To Reproduce**
$xmrig --opencl --opencl-platform=Intel -o xmr.luxor.tech:700 -u xxxx.ntbkN -p x -k --verbose --coin monero -a rx/0
 * ABOUT        XMRig/5.11.2/ gcc/9.3.0
 * LIBS         libuv/1.34.2 OpenSSL/1.1.1f hwloc/2.1.0
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          Intel(R) Core(TM) i5-7300U CPU @ 2.60GHz (1) x64 AES
                L2:0.5 MB L3:3.0 MB 2C/4T NUMA:1
 * MEMORY       5.3/15.5 GB (34%)
 * DONATE       0%
 * ASSEMBLY     auto:intel
 * POOL #1      xmr.luxor.tech:700 coin monero
 * COMMANDS     hashrate, pause, resume
 * ADL          disabled (failed to load ADL)
 * OPENCL       #0 Intel(R) OpenCL HD Graphics/OpenCL 2.1 
 * OPENCL GPU   #0 n/a Intel(R) Gen9 HD Graphics NEO 1100 MHz cu:24 mem:4095/12715 MB
 * CUDA         disabled
[2020-06-05 07:38:56.556]  net  use pool xmr.luxor.tech:700  34.107.237.122
[2020-06-05 07:38:56.557]  net  new job from xmr.luxor.tech:700 diff 5000 algo rx/0 height 2113923
[2020-06-05 07:38:56.557]  cpu  use argon2 implementation AVX2
[2020-06-05 07:38:56.560]  msr  0x000001a4:0x000000000000000f -> 0x000000000000000f
[2020-06-05 07:38:56.560]  msr  register values for "intel" preset has been set successfully (3 ms)
[2020-06-05 07:38:56.560]  rx   init dataset algo rx/0 (4 threads) seed 99a7b45a7f0d7fe9...
[2020-06-05 07:38:56.929]  rx   allocated 2336 MB (2080+256) huge pages 100% 1168/1168 +JIT (369 ms)
[2020-06-05 07:39:04.134]  net  new job from xmr.luxor.tech:700 diff 5000 algo rx/0 height 2113923
[2020-06-05 07:39:12.385]  rx   dataset ready (15456 ms)
[2020-06-05 07:39:12.385]  cpu  use profile  rx  (2 threads) scratchpad 2048 KB
[2020-06-05 07:39:12.407]  cpu  READY threads 2/2 (2) huge pages 100% 2/2 memory 4096 KB (22 ms)
[2020-06-05 07:39:12.429]  ocl  use profile  rx  (1 thread) scratchpad 2048 KB
|  # | GPU |  BUS ID |    I |  W | SI | MC |  U |  MEM | NAME
|  0 |   0 |     n/a |  384 |  8 |  0 |  - |  8 |  768 | Intel(R) Gen9 HD Graphics NEO
[2020-06-05 07:39:13.175]  ocl  GPU #0 compiling...
free(): invalid pointer
Abortado

**Expected behavior**
runnig low but running

**Required data**
 - Miner log as text or screenshot
$xmrig --opencl --opencl-platform=Intel -o xmr.luxor.tech:700 -u xxxx.ntbkN -p x -k --verbose --coin monero -a rx/0
 * ABOUT        XMRig/5.11.2_GA gcc/9.3.0
 * LIBS         libuv/1.34.2 OpenSSL/1.1.1f hwloc/2.1.0
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          Intel(R) Core(TM) i5-7300U CPU @ 2.60GHz (1) x64 AES
                L2:0.5 MB L3:3.0 MB 2C/4T NUMA:1
 * MEMORY       5.3/15.5 GB (34%)
 * DONATE       0%
 * ASSEMBLY     auto:intel
 * POOL #1      xmr.luxor.tech:700 coin monero
 * COMMANDS     hashrate, pause, resume
 * ADL          disabled (failed to load ADL)
 * OPENCL       #0 Intel(R) OpenCL HD Graphics/OpenCL 2.1 
 * OPENCL GPU   #0 n/a Intel(R) Gen9 HD Graphics NEO 1100 MHz cu:24 mem:4095/12715 MB
 * CUDA         disabled
[2020-06-05 07:38:56.556]  net  use pool xmr.luxor.tech:700  34.107.237.122
[2020-06-05 07:38:56.557]  net  new job from xmr.luxor.tech:700 diff 5000 algo rx/0 height 2113923
[2020-06-05 07:38:56.557]  cpu  use argon2 implementation AVX2
[2020-06-05 07:38:56.560]  msr  0x000001a4:0x000000000000000f -> 0x000000000000000f
[2020-06-05 07:38:56.560]  msr  register values for "intel" preset has been set successfully (3 ms)
[2020-06-05 07:38:56.560]  rx   init dataset algo rx/0 (4 threads) seed 99a7b45a7f0d7fe9...
[2020-06-05 07:38:56.929]  rx   allocated 2336 MB (2080+256) huge pages 100% 1168/1168 +JIT (369 ms)
[2020-06-05 07:39:04.134]  net  new job from xmr.luxor.tech:700 diff 5000 algo rx/0 height 2113923
[2020-06-05 07:39:12.385]  rx   dataset ready (15456 ms)
[2020-06-05 07:39:12.385]  cpu  use profile  rx  (2 threads) scratchpad 2048 KB
[2020-06-05 07:39:12.407]  cpu  READY threads 2/2 (2) huge pages 100% 2/2 memory 4096 KB (22 ms)
[2020-06-05 07:39:12.429]  ocl  use profile  rx  (1 thread) scratchpad 2048 KB
|  # | GPU |  BUS ID |    I |  W | SI | MC |  U |  MEM | NAME
|  0 |   0 |     n/a |  384 |  8 |  0 |  - |  8 |  768 | Intel(R) Gen9 HD Graphics NEO
[2020-06-05 07:39:13.175]  ocl  GPU #0 compiling...
free(): invalid pointer
Abortado

 - Config file or command line (without wallets) --> On command line
 - OS: [e.g. Windows] LINUX UBUNTU 20.04
 - For GPU related issues: information about GPUs and driver version.
GPU: 
       *-display
             descrição: VGA compatible controller
             produto: HD Graphics 620
             fabricante: Intel Corporation
             ID físico: 2
             informações do barramento: pci@0000:00:02.0
             versão: 02
             largura: 64 bits
             clock: 33MHz
             capacidades: pciexpress msi pm vga_controller bus_master cap_list rom
             configuração: driver=i915 latency=0
             recursos: irq:130 memória:eb000000-ebffffff memória:a0000000-afffffff porta de E/S:f000(tamanho=64) memória:c0000-dffff
[clinfo.txt](https://github.com/xmrig/xmrig/files/4735558/clinfo.txt)
[xmrig_print_platforms.txt](https://github.com/xmrig/xmrig/files/4735559/xmrig_print_platforms.txt)


**Additional context**
Add any other context about the problem here.


# Discussion History
## xmrig | 2020-08-28T16:36:23+00:00
#1816 

# Action History
- Created by: gilandriani | 2020-06-05T10:48:07+00:00
- Closed at: 2020-08-28T16:36:23+00:00
