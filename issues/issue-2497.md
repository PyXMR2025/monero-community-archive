---
title: Failed to load NVML
source_url: https://github.com/xmrig/xmrig/issues/2497
author: goose-ws
assignees: []
labels: []
created_at: '2021-07-26T13:57:41+00:00'
updated_at: '2021-08-20T10:45:37+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I'm using xmrig on Debian 10, running as root. I've built/enabled CUDA; however, my nvml fails to load when I start xmrig. The `nvidia-smi` package is installed/available/working. Any ideas how to fix NVML for xmrig? Does it even really matter?

```
 * ABOUT        XMRig/6.13.1 gcc/8.3.0
 * LIBS         libuv/1.24.1 OpenSSL/1.1.1d hwloc/1.11.12
 * HUGE PAGES   supported
 * 1GB PAGES    supported
 * CPU          Intel(R) Xeon(R) CPU E5-2670 0 @ 2.60GHz (2) 64-bit AES
                L2:4.0 MB L3:40.0 MB 16C/32T NUMA:2
 * MEMORY       92.2/94.4 GB (98%)
                P1-DIMMA1: 4 GB DDR3 @ 1066 MHz 18JSF51272PZ-1G4D
                P1-DIMMA2: 4 GB DDR3 @ 1066 MHz 18JSF51272PZ-1G4M
                P1-DIMMA3: 4 GB DDR3 @ 1066 MHz 18JSF51272PZ-1G4M
                P1-DIMMB1: 4 GB DDR3 @ 1066 MHz 18JSF51272PZ-1G6M
                P1-DIMMB2: 4 GB DDR3 @ 1066 MHz 18JSF51272PZ-1G9K
                P1-DIMMB3: 4 GB DDR3 @ 1066 MHz 18JSF51272PZ-1G9K
                P1-DIMMC1: 4 GB DDR3 @ 1066 MHz 18JSF51272PZ-1G4D
                P1-DIMMC2: 4 GB DDR3 @ 1066 MHz 18JSF51272PZ-1G6M
                P1-DIMMC3: 4 GB DDR3 @ 1066 MHz 18JSF51272PZ-1G6M
                P1-DIMMD1: 4 GB DDR3 @ 1066 MHz 18JSF51272PZ-1G6M
                P1-DIMMD2: 4 GB DDR3 @ 1066 MHz 18JSF51272PZ-1G9K
                P1-DIMMD3: 4 GB DDR3 @ 1066 MHz 18JSF51272PZ-1G4D
                P2-DIMME1: 4 GB DDR3 @ 1066 MHz 18JSF51272PZ-1G9K
                P2-DIMME2: 4 GB DDR3 @ 1066 MHz 18JSF51272PZ-1G9K
                P2-DIMME3: 4 GB DDR3 @ 1066 MHz 18JSF51272PZ-1G4M
                P2-DIMMF1: 4 GB DDR3 @ 1066 MHz 18JSF51272PZ-1G9K
                P2-DIMMF2: 4 GB DDR3 @ 1066 MHz 18JSF51272PZ-1G4M
                P2-DIMMF3: 4 GB DDR3 @ 1066 MHz 18JSF51272PZ-1G9K
                P2-DIMMG1: 4 GB DDR3 @ 1066 MHz 18JSF51272PZ-1G4M
                P2-DIMMG2: 4 GB DDR3 @ 1066 MHz 18JSF51272PZ-1G4M
                P2-DIMMG3: 4 GB DDR3 @ 1066 MHz 18JSF51272PZ-1G4M
                P2-DIMMH1: 4 GB DDR3 @ 1066 MHz 18JSF51272PZ-1G4D
                P2-DIMMH2: 4 GB DDR3 @ 1066 MHz 18JSF51272PZ-1G4D
                P2-DIMMH3: 4 GB DDR3 @ 1066 MHz 18JSF51272PZ-1G4D
 * MOTHERBOARD  Supermicro - X9DRi-LN4+/X9DR3-LN4+
 * DONATE       3%
 * ASSEMBLY     auto:intel
 * POOL #1      gulf.moneroocean.stream:10128 algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         11.4/11.4/6.12.0
 * NVML         disabled (failed to load NVML)
 * CUDA GPU     #0 05:00.0 Quadro P400 1252/2005 MHz smx:2 arch:61 mem:1967/2000 MB

root@Vergil:~# nvidia-smi
Mon Jul 26 09:57:06 2021
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 470.57.02    Driver Version: 470.57.02    CUDA Version: 11.4     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                               |                      |               MIG M. |
|===============================+======================+======================|
|   0  Quadro P400         Off  | 00000000:05:00.0 Off |                  N/A |
| 47%   62C    P0    N/A /  N/A |    295MiB /  2000MiB |    100%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+

+-----------------------------------------------------------------------------+
| Processes:                                                                  |
|  GPU   GI   CI        PID   Type   Process name                  GPU Memory |
|        ID   ID                                                   Usage      |
|=============================================================================|
|    0   N/A  N/A     12817      C   /root/xmrig/build/xmrig           289MiB |
+-----------------------------------------------------------------------------+
root@Vergil:~#
```

# Discussion History
## Spudz76 | 2021-07-27T03:10:19+00:00
Should have these packages installed for the build:
`cuda-command-line-tools-11-4 cuda-minimal-build-11-4 cuda-nvml-dev-11-4 cuda-nvrtc-dev-11-4`

And then `nvidia-driver-470 nvidia-settings` also.

I use these CMake options (same for you since that P400 is also an `arch:61`):

```
  -DCUDA_TOOLKIT_ROOT_DIR=/usr/local/cuda-11.4
  -DCMAKE_BUILD_TYPE=Release
  -DCMAKE_VERBOSE_MAKEFILE=ON
  -DCUDA_VERBOSE_BUILD=ON
  -DCUDA_SHOW_REGISTER=ON
  -DCUDA_ARCH=61
```

## DeeDeeRanged | 2021-08-20T10:43:48+00:00
Looking at you nvidia driver version 470.57.02-2 you installed the driver directly from Nvidia or from sid. Buster version is 460.73.01-1bpo10+1, bullseye is 460.91.03-1 and sid is 470.57.02-2. Cuda toolkit nvidia-cuda-toolkit buster is version 11.2.2-2bpo10+1, bullseye 11.2.2-3 and sid 11.3.1-3. Any reason to have such a mixed system?
I am running Debian testing/bookworm with nvidia-driver 470.57.02-02 and nvidia-cuda-toolkit 11.2.2-3 and have build the xmrig-cuda.so with those drivers. I have only installed the drivers from the repositories. The nvidia-cuda-toolkit should have pulled in all that is needed. Bulding it on Debian cmake -DCUDA_TOOLKIT_ROOT_DIR=/usr/lib/nvidia-cuda-toolkit.
Debian doesn't put it in /usr/local.

# Action History
- Created by: goose-ws | 2021-07-26T13:57:41+00:00
