---
title: Segmentation Fault Ubuntu 20 / AMD A12-9720P
source_url: https://github.com/xmrig/xmrig/issues/2255
author: proPonent
assignees: []
labels:
- bug
- need feedback
created_at: '2021-04-13T00:19:51+00:00'
updated_at: '2025-06-16T20:01:01+00:00'
type: issue
status: closed
closed_at: '2025-06-16T20:01:01+00:00'
---

# Original Description
Compiled and ran on multiple intel machines, tried same binary on AMD cpu and got segmentation fault, compiled on AMD machine and got segmentation fault. Precompiled binary version 6.8.0 works fine on same machine.

`###@###~/xmrig-6.11.2$ sudo ./xmrig
 * ABOUT        XMRig/6.11.2 gcc/9.3.0
 * LIBS         libuv/1.34.2 OpenSSL/1.1.1f hwloc/2.1.0
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          AMD A12-9720P RADEON R7, 12 COMPUTE CORES 4C+8G (1) 64-bit AES
                L2:2.0 MB L3:0.0 MB 4C/4T NUMA:1
 * MEMORY       5.1/7.3 GB (69%)
Segmentation fault
`

# Discussion History
## proPonent | 2021-04-13T00:25:00+00:00
Precompiled binary also fails in same way, but with added message about hwloc.

`[2021-04-12 19:23:57.331] hwloc auto configuration for algorithm "cn-heavy/0" failed.
 * ABOUT        XMRig/6.11.2 gcc/7.5.0
 * LIBS         libuv/1.41.0 OpenSSL/1.1.1j hwloc/2.4.1
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          AMD A12-9720P RADEON R7, 12 COMPUTE CORES 4C+8G (1) 64-bit AES
                L2:2.0 MB L3:0.0 MB 4C/4T NUMA:1
 * MEMORY       5.1/7.3 GB (70%)
Segmentation fault
`

## xmrig | 2021-04-13T11:52:25+00:00
Try disable DMI via command line option `--no-dmi` or config option `"dmi": false,`. If it helps please show the output of `dmidecode -t 17` command.
Thank you.


## Lonnegan | 2021-04-13T21:47:29+00:00
Apart from the bug, it is not useful to run cn/heavy on and AMD Excavator based CPU. These CPUs have only 1 MB last level cache per module, whereas cn/heavy uses a scratchpad size of 4 MB. Even 1 thread overloads the LLC of this CPU and requires slow DRAM accesses.

I'd try to mine something which fits into the 1 MB LLC of each module, e.g. Wownero (1 MB per thread, so you can run 2 threads on this CPU w/o flooding the cache) or rx/arq (256 KB per thread, so you can run all 4 threads).

## proPonent | 2021-04-13T23:20:15+00:00
This is configured to be mining XMR (Monero). I'm not sure why the CN/Heavy thing came up. As I understand XMR uses RX not CN/Heavy. Is XMR suited for this CPU or is Wownero better?

## proPonent | 2021-04-13T23:24:39+00:00


I don't see a change when using the --no-dmi option:
`
###@###:~/xmrig-6.11.2$ sudo ./xmrig --no-dmi
 * ABOUT        XMRig/6.11.2 gcc/9.3.0
 * LIBS         libuv/1.34.2 OpenSSL/1.1.1f hwloc/2.1.0
 * HUGE PAGES   supported
 * 1GB PAGES    supported
 * CPU          AMD A12-9720P RADEON R7, 12 COMPUTE CORES 4C+8G (1) 64-bit AES
                L2:2.0 MB L3:0.0 MB 4C/4T NUMA:1
 * MEMORY       5.3/7.3 GB (72%)
Segmentation fault
`


## proPonent | 2021-04-13T23:25:13+00:00
Let me know if there is anything else to try or any stats you want me to check.

## proPonent | 2021-04-13T23:26:49+00:00
In case it still helps...

`sudo dmidecode -t 17
# dmidecode 3.2
Getting SMBIOS data from sysfs.
SMBIOS 3.0.0 present.

Handle 0x0044, DMI type 17, 40 bytes
Memory Device
        Array Handle: 0x0042
        Error Information Handle: Not Provided
        Total Width: 64 bits
        Data Width: 64 bits
        Size: No Module Installed
        Form Factor: SODIMM
        Set: None
        Locator: DIMM 0
        Bank Locator: CHANNEL A
        Type: DDR4
        Type Detail: None
        Speed: Unknown
        Manufacturer: A1_Manufacturer0
        Serial Number: A1_SerialNum0
        Asset Tag: A1_AssetTagNum0
        Part Number: A1_PartNum0
        Rank: Unknown
        Configured Memory Speed: Unknown
        Minimum Voltage: Unknown
        Maximum Voltage: Unknown
        Configured Voltage: Unknown

Handle 0x0045, DMI type 17, 40 bytes
Memory Device
        Array Handle: 0x0042
        Error Information Handle: Not Provided
        Total Width: 64 bits
        Data Width: 64 bits
        Size: No Module Installed
        Form Factor: SODIMM
        Set: None
        Locator: <BAD INDEX>
        Bank Locator: <BAD INDEX>
        Type: <OUT OF SPEC>
        Type Detail: None
        Speed: Unknown
        Manufacturer: <BAD INDEX>
        Serial Number: <BAD INDEX>
        Asset Tag: <BAD INDEX>
        Part Number: <BAD INDEX>
        Rank: Unknown
        Configured Memory Speed: Unknown
        Minimum Voltage: Unknown
        Maximum Voltage: Unknown
        Configured Voltage: Unknown

Handle 0x0046, DMI type 17, 40 bytes
Memory Device
        Array Handle: 0x0042
        Error Information Handle: Not Provided
        Total Width: 64 bits
        Data Width: 64 bits
        Size: No Module Installed
        Form Factor: SODIMM
        Set: None
        Locator: DIMM 0
        Bank Locator: CHANNEL B
        Type: DDR4
        Type Detail: None
        Speed: Unknown
        Manufacturer: A1_Manufacturer2
        Serial Number: A1_SerialNum2
        Asset Tag: A1_AssetTagNum2
        Part Number: A1_PartNum2
        Rank: Unknown
        Configured Memory Speed: Unknown
        Minimum Voltage: Unknown
        Maximum Voltage: Unknown
        Configured Voltage: Unknown

Handle 0x0047, DMI type 17, 40 bytes
Memory Device
        Array Handle: 0x0042
        Error Information Handle: Not Provided
        Total Width: 64 bits
        Data Width: 64 bits
        Size: 8192 MB
        Form Factor: SODIMM
        Set: None
        Locator: DIMM 1
        Bank Locator: CHANNEL B
        Type: DDR4
        Type Detail: Synchronous Unbuffered (Unregistered)
        Speed: 2400 MT/s
        Manufacturer: <BAD INDEX>
        Serial Number: 1244033C
        Asset Tag: A1_AssetTagNum3
        Part Number: RMSA3260MH78HAF-2666
        Rank: 1
        Configured Memory Speed: 1866 MT/s
        Minimum Voltage: 1.5 V
        Maximum Voltage: 1.5 V
        Configured Voltage: 1.5 V
`

## Lonnegan | 2021-04-13T23:50:49+00:00
> This is configured to be mining XMR (Monero). I'm not sure why the CN/Heavy thing came up. As I understand XMR uses RX not CN/Heavy. Is XMR suited for this CPU or is Wownero better?

Well, the error log says "cn/heavy". That's why I thought you wanted to mine cn/heavy.

rx/monero has a scratchpad size of 2 MB per thread. So bigger than the LLC. I'd try Wownero or ArQma.

## Spudz76 | 2021-04-15T23:39:58+00:00
Messages from before the first version/about header are from the autoconfigurator - so it's complaining there is not enough cache to do any cn-heavy threads, normal (unless compiled without it).

# Action History
- Created by: proPonent | 2021-04-13T00:19:51+00:00
- Closed at: 2025-06-16T20:01:01+00:00
