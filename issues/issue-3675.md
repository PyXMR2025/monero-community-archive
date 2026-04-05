---
title: With the new 6.22.3 and 6.23.0 the hashrate of rx/0 is lower on Ryzen 1700X
source_url: https://github.com/xmrig/xmrig/issues/3675
author: jfikar
assignees: []
labels:
- bug
- randomx
created_at: '2025-06-19T08:25:49+00:00'
updated_at: '2025-06-28T10:23:51+00:00'
type: issue
status: closed
closed_at: '2025-06-28T10:23:51+00:00'
---

# Original Description
I think it is related to #3646. I have Ryzen 1700X (8 cores, 16 threads, 16MB L3) and previous versions of xmrig used 8 of 16 cores.

The new versions 6.22.3 and 6.23.0 want to use 10 of 16 cores. But the hashrate for rx/0 is lower:

```
# of cores                  hashrate H/s
7                            4295
8                            4707
9                            4368
10                           4017
``` 

```
 * ABOUT        XMRig/6.23.0 gcc/14.2.0 (built for Linux x86-64, 64 bit)
 * LIBS         libuv/1.51.0 OpenSSL/3.0.16 hwloc/2.12.1
 * HUGE PAGES   supported
 * 1GB PAGES    supported
 * CPU          AMD Ryzen 7 1700X Eight-Core Processor (1) 64-bit AES
                L2:4.0 MB L3:16.0 MB 8C/16T NUMA:1
 * MEMORY       4.9/31.3 GB (16%)
 * DONATE       1%
 * ASSEMBLY     auto:ryzen
 ```

# Discussion History
## Flussig29 | 2025-06-20T09:48:14+00:00
I'm seeing issues like this also with 3900x, even the fix for the 5600g gets lower hash on 6.23.
i'm back to 6.22.2 for all rigs now until this gets sorted.

## SChernykh | 2025-06-20T09:50:52+00:00
3900x shouldn't be affected by this, because auto-config will always use all 24 threads.

## Flussig29 | 2025-06-20T09:53:35+00:00
it might be a hiveos thing then, as i updated all rigs to latest build and all the 3900x would noit start to mine even after reboot. I then went and manually set flight sheet to use 6.22.2 and they all started to mine again.

## Flussig29 | 2025-06-20T09:54:43+00:00
all the 5600g did mine, however their hashrate was previously around 4.7 dropped to 4.1, upon going back to 6.22.2 hash back to normal

# Action History
- Created by: jfikar | 2025-06-19T08:25:49+00:00
- Closed at: 2025-06-28T10:23:51+00:00
