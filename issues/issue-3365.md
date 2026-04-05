---
title: can`t bind memory
source_url: https://github.com/xmrig/xmrig/issues/3365
author: Obled1
assignees: []
labels: []
created_at: '2023-11-21T16:26:40+00:00'
updated_at: '2025-06-18T22:32:54+00:00'
type: issue
status: closed
closed_at: '2025-06-18T22:32:54+00:00'
---

# Original Description
Problem, miner not working. Log:

"* ABOUT        XMRig/6.20.0 gcc/11.2.0
 * LIBS         libuv/1.44.2 OpenSSL/1.1.1s hwloc/2.9.0
 * HUGE PAGES   permission granted
 * 1GB PAGES    unavailable
 * CPU          AMD EPYC 7R12 48-Core Processor (2) 64-bit AES
                L2:48.0 MB L3:384.0 MB 96C/192T NUMA:2
 * MEMORY       10.2/511.9 GB (2%)
                P1-DIMMA1: 32 GB DDR4 @ 2933 MHz M393A4K40BB2-CTD
                P1-DIMMB1: 32 GB DDR4 @ 2933 MHz M393A4K40BB2-CTD
                P1-DIMMC1: 32 GB DDR4 @ 2933 MHz M393A4K40BB2-CTD
                P1-DIMMD1: 32 GB DDR4 @ 2933 MHz M393A4K40BB2-CTD
                P1-DIMME1: 32 GB DDR4 @ 2933 MHz M393A4K40BB2-CTD
                P1-DIMMF1: 32 GB DDR4 @ 2933 MHz M393A4K40BB2-CTD
                P1-DIMMG1: 32 GB DDR4 @ 2933 MHz M393A4K40BB2-CTD
                P1-DIMMH1: 32 GB DDR4 @ 2933 MHz M393A4K40BB2-CTD
                P2-DIMMA1: 32 GB DDR4 @ 2933 MHz M393A4K40BB2-CTD
                P2-DIMMB1: 32 GB DDR4 @ 2933 MHz M393A4K40BB2-CTD
                P2-DIMMC1: 32 GB DDR4 @ 2933 MHz M393A4K40BB2-CTD
                P2-DIMMD1: 32 GB DDR4 @ 2933 MHz M393A4K40BB2-CTD
                P2-DIMME1: 32 GB DDR4 @ 2933 MHz M393A4K40BB2-CTD
                P2-DIMMF1: 32 GB DDR4 @ 2933 MHz M393A4K40BB2-CTD
                P2-DIMMG1: 32 GB DDR4 @ 2933 MHz M393A4K40BB2-CTD
                P2-DIMMH1: 32 GB DDR4 @ 2933 MHz M393A4K40BB2-CTD
 * MOTHERBOARD  Supermicro - H11DSi
 * DONATE       1%
 * ASSEMBLY     auto:ryzen
 * POOL # 1      de.zephyr.herominers.com:1123 algo rx/0
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled
[2023-11-21 19:07:24.924]  net      use pool de.zephyr.herominers.com:1123  46.4.40.166
[2023-11-21 19:07:24.925]  net      new job from de.zephyr.herominers.com:1123 diff 120001 algo rx/0 height 125075
[2023-11-21 19:07:24.926]  cpu      use argon2 implementation AVX2
[2023-11-21 19:07:27.979]  msr      register values for "ryzen_17h" preset have been set successfully (3052 ms)
[2023-11-21 19:07:27.980]  randomx  init datasets algo rx/0 (192 threads) seed e354a769597c6c19...
[2023-11-21 19:07:27.981]  randomx  # 0 skipped (can't bind memory)
[2023-11-21 19:07:27.982]  randomx  # 1 skipped (can't bind memory)
[2023-11-21 19:07:27.983]  randomx  # 0 allocated  256 MB huge pages 100% +JIT (0 ms)
[2023-11-21 19:07:27.984]  randomx  failed to allocate RandomX datasets, switching to slow mode (3 ms)
[2023-11-21 19:07:28.359]  randomx  # 0 dataset ready (375 ms)
[2023-11-21 19:07:28.360]  cpu      use profile  rx  (192 threads) scratchpad 2048 KB
[2023-11-21 19:07:28.367] CPU # 00 warning: "can't bind memory"
[2023-11-21 19:07:28.367] CPU # 05 warning: "can't bind memory"
[2023-11-21 19:07:28.368] CPU # 09 warning: "can't bind memory"
[2023-11-21 19:07:28.369] CPU # 14 warning: "can't bind memory"
[2023-11-21 19:07:28.369] CPU # 22 warning: "can't bind memory"
[2023-11-21 19:07:28.370] CPU # 01 warning: "can't bind memory"
[2023-11-21 19:07:28.371] CPU # 07 warning: "can't bind memory"
[2023-11-21 19:07:28.372] CPU # 06 warning: "can't bind memory"
[2023-11-21 19:07:28.373] CPU # 08 warning: "can't bind memory"
[2023-11-21 19:07:28.373] CPU # 18 warning: "can't bind memory"
[2023-11-21 19:07:28.374] CPU # 79 warning: "can't bind memory"
[2023-11-21 19:07:28.375] CPU # 04 warning: "can't bind memory"...."
how to fix it?

# Discussion History
## Obled1 | 2023-11-21T16:29:05+00:00
Win 11 pro for Workstation 23h2 build 22631.2428

## geekwilliams | 2023-11-21T18:15:42+00:00
Do you have virtualization based security enabled on that machine? Also holy wow that's a lot of memory

Sent from my iSlippers


On Nov 21, 2023, at 9:29 AM, Obled1 ***@***.***> wrote:

﻿

Win 11 pro for Worckstation 23h2 build 22631.2428

—
Reply to this email directly, view it on GitHub<https://github.com/xmrig/xmrig/issues/3365#issuecomment-1821258801>, or unsubscribe<https://github.com/notifications/unsubscribe-auth/AG7SNTLHN5QC3TVINVKHVUDYFTJG5AVCNFSM6AAAAAA7U3TO52VHI2DSMVQWIX3LMV43OSLTON2WKQ3PNVWWK3TUHMYTQMRRGI2TQOBQGE>.
You are receiving this because you are subscribed to this thread.Message ID: ***@***.***>


## Obled1 | 2023-11-21T18:51:57+00:00
> Do you have virtualization based security enabled on that machine? Also holy wow that's a lot of memory
>

I`m tried with Enabled and Disabled. How should I do it?

## geekwilliams | 2023-11-21T19:04:35+00:00
I'm seeing an older thread that indicates this may be an issue with how memory is installed in the system.  Here is one site that was mentioned: https://www.lexo.ch/blog/2022/06/solved-xmrig-cpu-xx-warning-cant-bind-memory-xmrig-does-not-run-on-all-cpu-cores/

The site has a lot of ads, but may be helpful?

Sent from my iSlippers


On Nov 21, 2023, at 11:52 AM, Obled1 ***@***.***> wrote:

﻿

Do you have virtualization based security enabled on that machine? Also holy wow that's a lot of memory
…
Sent from my iSlippers On Nov 21, 2023, at 9:29 AM, Obled1 @.> wrote: ﻿ Win 11 pro for Worckstation 23h2 build 22631.2428 — Reply to this email directly, view it on GitHub<#3365 (comment)<https://github.com/xmrig/xmrig/issues/3365#issuecomment-1821258801>>, or unsubscribehttps://github.com/notifications/unsubscribe-auth/AG7SNTLHN5QC3TVINVKHVUDYFTJG5AVCNFSM6AAAAAA7U3TO52VHI2DSMVQWIX3LMV43OSLTON2WKQ3PNVWWK3TUHMYTQMRRGI2TQOBQGE. You are receiving this because you are subscribed to this thread.Message ID: @.>

I`m tryed with Enabled and Disabled

—
Reply to this email directly, view it on GitHub<https://github.com/xmrig/xmrig/issues/3365#issuecomment-1821475275>, or unsubscribe<https://github.com/notifications/unsubscribe-auth/AG7SNTLGO77CKCO6M6VX5NTYFTZ5RAVCNFSM6AAAAAA7U3TO52VHI2DSMVQWIX3LMV43OSLTON2WKQ3PNVWWK3TUHMYTQMRRGQ3TKMRXGU>.
You are receiving this because you commented.Message ID: ***@***.***>


## Obled1 | 2023-11-21T19:09:38+00:00
> I'm seeing an older thread that indicates this may be an issue with how memory is installed in the system. Here is one site that was mentioned: >
All 16 slots are full))



## geekwilliams | 2023-11-21T19:28:20+00:00
A couple other things to check: 
1) memory integrity in core isolation setting OFF
2) also disable virtual machine platform 

Guide is [here](https://support.microsoft.com/en-us/windows/options-to-optimize-gaming-performance-in-windows-11-a255f612-2949-4373-a566-ff6f3f474613)

## Obled1 | 2023-11-21T19:53:53+00:00
1. Core isolation Off
2. VMP off

## Obled1 | 2023-11-21T19:56:02+00:00
Hyper-V off

## geekwilliams | 2023-11-22T01:13:42+00:00
Dang. Someone smarter than me will have to chime in on this. But I really want to know what the solution is. Sorry man 

## SChernykh | 2023-11-22T12:55:38+00:00
You should try Windows 10 or Linux. It's something wrong with drivers on Windows 11, at least for this CPU. I can't even find EPYC 7R12 on AMD's website.

## SlavisaBakic | 2023-11-24T12:00:25+00:00
> Win 11 pro for Workstation 23h2 build 22631.2428

EPYC 7R12 is not officialy supported CPU on W11. It is only supported on Windows Server edition according to Microsoft documentation.

https://learn.microsoft.com/en-us/windows-hardware/design/minimum/supported/windows-11-supported-amd-processors
https://learn.microsoft.com/en-us/windows-hardware/design/minimum/windows-processor-requirements

In any case, install Linux distro without GUI like Ubuntu Server 22.04 LTS with HWE and take advantage of 1GiB pages unavailable on Windows for 1-5% higher hashrate.

# Action History
- Created by: Obled1 | 2023-11-21T16:26:40+00:00
- Closed at: 2025-06-18T22:32:54+00:00
