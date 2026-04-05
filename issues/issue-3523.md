---
title: Xmrig 6.21.3 is not even recognising the --cuda option
source_url: https://github.com/xmrig/xmrig/issues/3523
author: TournelHenry
assignees: []
labels:
- question
created_at: '2024-08-02T14:36:32+00:00'
updated_at: '2024-12-30T13:42:07+00:00'
type: issue
status: closed
closed_at: '2024-08-02T17:02:12+00:00'
---

# Original Description
Xmrig 6.21.3 does not seem to support CUDA even though the documentation claims it does. The command line doesn't even recognise the `--cuda` option or the `--cuda-loader` option anymore
![Screenshot from 2024-08-02 15-30-33](https://github.com/user-attachments/assets/3a75960a-f878-4817-9504-6208a80a386d)


# Discussion History
## SChernykh | 2024-08-02T16:02:56+00:00
Did you build the binary yourself, or is it an official binary? XMRig can only say that `--cuda` is an unknown option, if it was compiled without CUDA support. I just checked an official Windows binary (yes, I know it's not the same), and it works fine:
```
xmrig.exe -o 127.0.0.1:3333 --cuda
 * ABOUT        XMRig/6.21.3 MSVC/2019 (built for Windows x86-64, 64 bit)
 * LIBS         libuv/1.48.0 OpenSSL/3.0.13 hwloc/2.10.0
 * HUGE PAGES   permission granted
 * 1GB PAGES    unavailable
 * CPU          AMD Ryzen 9 7950X 16-Core Processor (1) 64-bit AES
                L2:16.0 MB L3:64.0 MB 16C/32T NUMA:1
 * MEMORY       3.3/31.7 GB (10%)
                DIMM_A1: 16 GB DDR5 @ 6000 MHz F5-6400J3239G16G
                DIMM_B1: 16 GB DDR5 @ 6000 MHz F5-6400J3239G16G
 * MOTHERBOARD  ASUSTeK COMPUTER INC. - ROG CROSSHAIR X670E GENE
 * DONATE       1%
 * ASSEMBLY     auto:ryzen
 * POOL #1      127.0.0.1:3333 algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         11.4/12.3/6.17.0
 * NVML         12.546.33/546.33 press e for health report
 * CUDA GPU     #0 01:00.0 NVIDIA GeForce RTX 4060 2490/8501 MHz smx:24 arch:89 mem:6677/8187 MB
```

## TournelHenry | 2024-08-02T16:24:09+00:00
I'm using the Linux Binary from https://xmrig.com/download .
Just noticed the top says "Static, CPU only".
So, maybe that's means, no cuda support.
I'll try to build mine myself *(if I can figure it out 😂)* to test.

## SChernykh | 2024-08-02T16:31:15+00:00
Yes, static Linux binary works only with CPU. There are dynamic binaries for Ubuntu, but if they don't work on your distro, you'll have to compile XMRig yourself.

## TournelHenry | 2024-08-02T17:02:12+00:00
Just built mine.
It's recognising the `--cuda` option now. Now to fix the bug of xmrig not detecting my gpu 🤣.
**Conclusion:** The official Linux Binary is CPU only.

## TournelHenry | 2024-08-03T22:53:56+00:00
Just an update for others on Debian having getting the _cuda disabled (no devices)_ error.
For Debian devices with a CPU and an added Nvidia GPU, you also have to install "nvidia-prime" _(also called "nvidia-primus" or "nvidia optimus". Search https://packages.debian.org to find the precise name)_
Sources/Discussions here;
- [Question about the issue on Debian Forums](https://forums.debian.net/viewtopic.php?t=155273)
- [Question about the issue on Nvidia Dev Forum](https://forums.developer.nvidia.com/t/newly-installed-drivers-are-not-found-when-nvidia-smi-is-called/82686)
- [NVIDIA Optimus on Debian Wiki](https://wiki.debian.org/NVIDIA%20Optimus)

# Action History
- Created by: TournelHenry | 2024-08-02T14:36:32+00:00
- Closed at: 2024-08-02T17:02:12+00:00
