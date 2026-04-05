---
title: xmrig-cuda-6.21.0-cuda11_4-win64 fails on Nvidia GDDR6 card
source_url: https://github.com/xmrig/xmrig/issues/3446
author: Pythdevver
assignees: []
labels: []
created_at: '2024-03-15T07:57:28+00:00'
updated_at: '2025-06-18T22:16:08+00:00'
type: issue
status: closed
closed_at: '2025-06-18T22:16:08+00:00'
---

# Original Description
**Describe the bug**
Latest cuda+xmrig bundle fails on latest Nvidia card with these lines:

```miner    KawPow light cache for epoch 431 calculated (2338ms)
Program compile log: nvrtc: error: invalid value for --gpu-architecture (-arch)
  nvidia   KawPow failed to initialize DAG: <KawPow_build_program>:197 "NVRTC_ERROR_INVALID_OPTION"
```

**To Reproduce**
Run `xmrig.exe --no-cpu --cuda --cuda-loader=xmrig-cuda.dll -o stratum.ravenminer.com:3838 -a kawpow -u RAVEN_wallet_ID` with xmrig-cuda.dll from xmrig-cuda-6.21.0-cuda11_4-win64.zip and with xmrig.exe from xmrig-6.21.1-msvc-win64.zip

**Expected behavior**
Start of mining

**Required data**
 - Miner log as text:

```
 * ABOUT        XMRig/6.21.1 MSVC/2019 (built for Windows x86-64, 64 bit)
 * LIBS         libuv/1.44.2 OpenSSL/1.1.1s hwloc/2.9.0
 * HUGE PAGES   permission granted
 * 1GB PAGES    unavailable
 * CPU          AMD Ryzen 9 7945HX with Radeon Graphics (1) 64-bit AES
                L2:16.0 MB L3:64.0 MB 16C/32T NUMA:1
 * MEMORY       5.5/15.7 GB (35%)
                DIMM_A0: 16 GB DDR5 @ 5200 MHz KF556S40IB-16
 * MOTHERBOARD  LENOVO - LNVNB161216
 * DONATE       1%
 * ASSEMBLY     auto:ryzen
 * POOL #1      stratum.ravenminer.com:3838 algo kawpow
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         11.4/12.1/6.21.0
 * NVML         12.532.10/532.10 press e for health report
 * CUDA GPU     #0 01:00.0 NVIDIA GeForce RTX 4060 Laptop GPU 1890/8001 MHz smx:24 arch:89 mem:7107/8187 MB
[2024-03-14 20:07:21.322]  net      use pool stratum.ravenminer.com:3838
[2024-03-14 20:07:21.426]  net      new job from stratum.ravenminer.com:3838 diff 862M algo kawpow height 3234469
[2024-03-14 20:07:21.426]  nvidia   use profile  kawpow  (1 thread) scratchpad 32 KB
|  # | GPU |  BUS ID | INTENSITY | THREADS | BLOCKS | BF |  BS | MEMORY | NAME
|  0 |   0 | 01:00.0 |  12582912 |     256 |  49152 |  6 |  25 |   4472 | NVIDIA GeForce RTX 4060 Laptop GPU
[2024-03-14 20:07:21.593]  nvidia   READY threads 1/1 (166 ms)
[2024-03-14 20:07:23.931]  miner    KawPow light cache for epoch 431 calculated (2338ms)
Program compile log: nvrtc: error: invalid value for --gpu-architecture (-arch)

[2024-03-14 20:07:38.462]  nvidia   KawPow failed to initialize DAG: <KawPow_build_program>:197 "NVRTC_ERROR_INVALID_OPTION"
[2024-03-14 20:07:42.796]  net      new job from stratum.ravenminer.com:3838 diff 862M algo kawpow height 3234470
[2024-03-14 20:08:01.565]  net      new job from stratum.ravenminer.com:3838 diff 862M algo kawpow height 3234471
[2024-03-14 20:08:05.869]  signal   Ctrl+C received, exiting
[2024-03-14 20:08:05.873]  nvidia   stopped (4 ms)

```

 - Config file or command line (without wallets):
`xmrig.exe --no-cpu --cuda --cuda-loader=xmrig-cuda.dll -o stratum.ravenminer.com:3838 -a kawpow -u RAVEN_wallet_ID`

 - OS: Windows 11 Home
 - For GPU related issues: information about GPUs and driver version:
NVIDIA GeForce RTX 4060 Laptop, Nvidia driver 532.10

**Additional context**
none

# Discussion History
## SChernykh | 2024-03-15T08:48:47+00:00
You should use `xmrig-cuda-6.21.0-cuda12_3-win64.zip` to have support for RTX 4000 cards. I just checked and it works with my RTX 4060.

## Pythdevver | 2024-03-15T08:53:50+00:00
> You should use `xmrig-cuda-6.21.0-cuda12_3-win64.zip` to have support for RTX 4000 cards. I just checked and it works with my RTX 4060.

Thank you for a fast answer!
What is your Nvidia driver version? I answer you about the driver version because laptops are very picky about VGA drivers. Maybe I'll have to retry many versions to find a bluescreen-free version.

## SChernykh | 2024-03-15T09:10:39+00:00
It's my desktop PC. Driver version is 546.33, but I think it's better to just use the latest driver from NVIDIA.

## pythdeverr | 2024-03-16T07:11:35+00:00
@SChernykh
I've downloaded Nvidia driver ver. 551.76 for laptops and your advice has worked, thanks.
Now I'm getting ~15MH/sec while mining Ravencoin and my gpu is 57 °C on average.

This issue can be closed as fixed.

BTW, what is your RTX 4060 Desktop hashrate for RVN? And how hot is it? Thank you anyway.

# Action History
- Created by: Pythdevver | 2024-03-15T07:57:28+00:00
- Closed at: 2025-06-18T22:16:08+00:00
