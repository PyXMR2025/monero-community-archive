---
title: Linux-AMD Processor-cannot set MSR 0xc0011021 to 0x001c000200000040
source_url: https://github.com/xmrig/xmrig/issues/3359
author: Ranchdad86
assignees: []
labels: []
created_at: '2023-11-16T20:15:51+00:00'
updated_at: '2025-06-18T22:18:11+00:00'
type: issue
status: closed
closed_at: '2025-06-18T22:18:11+00:00'
---

# Original Description
**Describe the bug**
Linux-AMD Processor-cannot set MSR 0xc0011021 to 0x001c000200000040

**To Reproduce**
sudo ./xmrig



OS-Latest Ubuntu  Cinnamon (also have the same issue in latest linux mint cinnamon -edge). 

* ABOUT        XMRig/6.20.0 gcc/9.4.0
 * LIBS         libuv/1.44.2 OpenSSL/1.1.1s hwloc/2.9.0
 * HUGE PAGES   supported
 * 1GB PAGES    supported
 * CPU          AMD Ryzen 7 5700X 8-Core Processor (1) 64-bit AES
                L2:4.0 MB L3:32.0 MB 8C/16T NUMA:1
 * MEMORY       5.6/62.7 GB (9%)
                DIMM_A0: <empty>
                DIMM_A1: 32 GB DDR4 @ 3600 MHz CMK64GX4M2D3600C18
                DIMM_B0: <empty>
                DIMM_B1: 32 GB DDR4 @ 3600 MHz CMK64GX4M2D3600C18
 * MOTHERBOARD  ASRock - B450M Pro4-F R2.0
 * DONATE       5%
 * ASSEMBLY     auto:ryzen
 * POOL #1      americas.mining-dutch.nl:9997 algo ghostrider
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled
[2023-11-16 13:08:46.477]  net      use pool americas.mining-dutch.nl:9997  15.235.43.55
[2023-11-16 13:08:46.579]  net      new job from americas.mining-dutch.nl:9997 diff 65536 algo ghostrider height 135948
[2023-11-16 13:08:46.580]  msr      cannot set MSR 0xc0011021 to 0x001c000200000040
[2023-11-16 13:08:46.580]  msr      FAILED TO APPLY MSR MOD, HASHRATE WILL BE LOW

**Additional context**
Tried multiple options to fix nothing has worked so far. Works fine on windows as admin, and works on my other linux machines using the same JSON file


# Discussion History
## Ranchdad86 | 2023-11-16T20:28:42+00:00
I also tried "wrmsr": "-a 0xc0011020:0x4480000000", in the json. Same result.



## SChernykh | 2023-11-16T20:38:10+00:00
Did you try to run `sudo randomx_boost.sh`? https://github.com/xmrig/xmrig/blob/dev/scripts/randomx_boost.sh

## Ranchdad86 | 2023-11-16T21:05:34+00:00
Detected Zen3 CPU
wrmsr: open: Permission denied
wrmsr: open: Permission denied
wrmsr: open: Permission denied
wrmsr: open: Permission denied
MSR register values for Zen3 applied


## SChernykh | 2023-11-16T21:12:36+00:00
I don't know, try to run `sudo modprobe msr allow_writes=on` and then `sudo randomx_boost.sh`

## Ranchdad86 | 2023-11-16T21:18:52+00:00
xxx-LXD:~/Desktop/Miners/xmrig-6.20.0$ sudo modprobe msr allow_writes=on

[sudo] password for xxx:        
       
xxx-LXD:~/Desktop/Miners/xmrig-6.20.0$ sudo ./randomx_boost.sh

Detected Zen3 CPU
wrmsr: pwrite: Operation not permitted



## SChernykh | 2023-11-16T21:20:47+00:00
They probably disabled it in kernel, or you're running it inside a VM (maybe even without knowing it). Try older Ubuntu versions.

## Ranchdad86 | 2023-11-17T03:43:14+00:00
I'm running ubuntu 23.10 and mint 21.2 both with newer kernels.  let me see if using 22.04 makes a difference

## Ranchdad86 | 2023-11-17T04:03:46+00:00
No dice. Rolled back to 5.19 and still won't work


## SlavisaBakic | 2023-11-18T11:41:26+00:00
Can you try to run XMrig as root (without using sudo)?

## zebcarnell | 2023-12-21T16:16:54+00:00
> No dice. Rolled back to 5.19 and still won't work

Secure boot needs to be off
SELinux, if you have it, needs to be off or permissive


# Action History
- Created by: Ranchdad86 | 2023-11-16T20:15:51+00:00
- Closed at: 2025-06-18T22:18:11+00:00
