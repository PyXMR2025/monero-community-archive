---
title: '1GB PAGES unavailable #confused'
source_url: https://github.com/xmrig/xmrig/issues/3076
author: STUKguy
assignees: []
labels: []
created_at: '2022-06-21T22:59:28+00:00'
updated_at: '2023-07-10T13:25:43+00:00'
type: issue
status: closed
closed_at: '2022-06-22T09:46:25+00:00'
---

# Original Description
Apologies if this has been answered somewhere else before and I'm just looking in the wrong place (in this group i did a search for 1gb which came back with result but the OP closed there post with out an answer)

I have a quad core CPU "Intel(R) Core(TM) i5-2400 CPU @ 3.10GHz (1)" with 16GB of RAM, i am trying to enable 1GB Pages but it doesn't seem to work.

I found this guide https://forum.garudalinux.org/t/how-to-enable-1gb-hugepages-support-for-xmrig/4198/6 i did what one of the helpers suggested but it didn't work

`
GRUB_DEFAULT=0
GRUB_TIMEOUT=5
GRUB_DISTRIBUTOR=`lsb_release -i -s 2> /dev/null || echo Debian`
GRUB_CMDLINE_LINUX_DEFAULT="quiet"
GRUB_CMDLINE_LINUX="hugepagesz=1GB hugepages=6"
`
i still get "1GB PAGES unavailable" after reboot

The i found this https://github.com/xmrig/xmrig/issues/1411 
but when i run "ls -Al /sys/devices/system/node/node*/hugepages/*1048*/" i get 
`ls: cannot access '/sys/devices/system/node/node*/hugepages/*1048*/': No such file or directory`

This is the full Xmrig out put
` * ABOUT        XMRig/6.17.0 gcc/10.2.1
 * LIBS         libuv/1.40.0 OpenSSL/1.1.1n hwloc/2.4.1
 * HUGE PAGES   supported
 * 1GB PAGES    unavailable
 * CPU          Intel(R) Core(TM) i5-2400 CPU @ 3.10GHz (1) 64-bit AES
                L2:1.0 MB L3:6.0 MB 4C/4T NUMA:1
 * MEMORY       0.9/15.5 GB (6%)
                DIMM_A0: 4 GB DDR3 @ 1333 MHz HP698650-154-KEB  
                DIMM_A1: 4 GB DDR3 @ 1333 MHz HP698650-154-KEB  
                DIMM_B0: 4 GB DDR3 @ 1333 MHz HP698650-154-KEB  
                DIMM_B1: 4 GB DDR3 @ 1333 MHz HP698650-154-KEB  
 * MOTHERBOARD  Dell Inc. - 0D28YY
 * DONATE       1%
 * ASSEMBLY     auto:intel
 * POOL #1      gulf.moneroocean.stream:10128 algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled`

Please can someone point me in the correct (and preferably easy) direction

# Discussion History
## Spudz76 | 2022-06-22T05:53:29+00:00
i5-2400 has only cpuflags `aes, avx, osxsave, sse2, ssse3, sse4.1, popcnt` which does not include `pdpe1gb` thus no 1GB pages support in the silicon.  It will never work.

## STUKguy | 2022-06-22T09:46:25+00:00
> i5-2400 has only cpuflags `aes, avx, osxsave, sse2, ssse3, sse4.1, popcnt` which does not include `pdpe1gb` thus no 1GB pages support in the silicon. It will never work.

That's a shame, but Thank you soo much

## Inzimam-Tariq | 2023-07-10T13:25:43+00:00
and what about the i7 11 Gen 
11th Gen Intel(R) Core(TM) i7-1165G7 @ 2.80GHz (1) 64-bit AES
                L2:5.0 MB L3:12.0 MB 4C/8T NUMA:1
 * MEMORY       6.0/31.7 GB (19%)
                Bottom-Slot 1(left): 16 GB DDR4 @ 3200 MHz TEAMGROUP-SD4-3200
                Bottom-Slot 2(right): 16 GB DDR4 @ 3200 MHz TEAMGROUP-SD4-3200

# Action History
- Created by: STUKguy | 2022-06-21T22:59:28+00:00
- Closed at: 2022-06-22T09:46:25+00:00
