---
title: 'M1 says "auto:intel" and averages at 500-600H/s. '
source_url: https://github.com/xmrig/xmrig/issues/2327
author: esaruoho
assignees: []
labels: []
created_at: '2021-04-29T08:02:55+00:00'
updated_at: '2021-04-29T08:37:07+00:00'
type: issue
status: closed
closed_at: '2021-04-29T08:37:07+00:00'
---

# Original Description
I'm wondering why my M1, after running xmrig wizard, runs auto:intel and says 500-600H/s instead of the 2300H/s that most are reporting.

What am I missing?

# Discussion History
## snipeTR | 2021-04-29T08:16:11+00:00
More info please.
Command, version, vb...

## SChernykh | 2021-04-29T08:17:08+00:00
Double check that you downloaded `xmrig-6.12.1-macos-arm64.tar.gz` from releases and not `macos-x64`

## esaruoho | 2021-04-29T08:27:59+00:00
i've used homebrew to get xmrig, the command i use is xmrig. terminal is running native instead of rosetta.

```
 * ABOUT        XMRig/6.12.1 clang/12.0.0
 * LIBS         libuv/1.41.0 OpenSSL/1.1.1k hwloc/2.4.1
 * HUGE PAGES   supported
 * 1GB PAGES    unavailable
 * CPU          VirtualApple @ 2.50GHz (1) 64-bit AES
                L2:32.0 MB L3:0.0 MB 8C/8T NUMA:1
 * MEMORY       15.8/16.0 GB (98%)
 * DONATE       5%
 * ASSEMBLY     auto:intel
 * POOL #1      monerohash.com:9999 algo rx/0
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled
```

## SChernykh | 2021-04-29T08:29:39+00:00
It clearly says `VirtualApple` so you're running x86 code in rosetta.

## esaruoho | 2021-04-29T08:30:57+00:00
> It clearly says `VirtualApple` so you're running x86 code in rosetta.

thanks! i'll re-install homebrew using non-rosetta terminal. don't know why i messed up like this. thanks for the heads up!

## esaruoho | 2021-04-29T08:37:07+00:00
Thank you VERY much!

```
|    CPU # | AFFINITY | 10s H/s | 60s H/s | 15m H/s |
|        0 |        0 |   278.9 |     n/a |     n/a |
|        1 |        1 |   285.4 |     n/a |     n/a |
|        2 |        2 |   278.2 |     n/a |     n/a |
|        3 |        3 |   278.9 |     n/a |     n/a |
|        4 |        4 |   277.4 |     n/a |     n/a |
|        5 |        5 |   278.4 |     n/a |     n/a |
|        6 |        6 |   280.1 |     n/a |     n/a |
|        7 |        7 |   280.7 |     n/a |     n/a |
|        - |        - |  2237.9 |     n/a |     n/a |
```

now it's working like it should. i'll close this ticket :)


# Action History
- Created by: esaruoho | 2021-04-29T08:02:55+00:00
- Closed at: 2021-04-29T08:37:07+00:00
