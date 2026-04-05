---
title: 'Solo mining GUUS Error: job error: "Invalid block template received from daemon"'
source_url: https://github.com/xmrig/xmrig/issues/3613
author: MaxQuatro
assignees: []
labels:
- question
created_at: '2025-01-06T10:42:18+00:00'
updated_at: '2025-06-16T15:14:31+00:00'
type: issue
status: closed
closed_at: '2025-06-16T15:14:31+00:00'
---

# Original Description
**Describe the bug**
Solo mining Guus Error: job error: "Invalid block template received from daemon.
xmrig with "algo": "randomx"
job error: "Invalid block template received from daemon"

**To Reproduce**
Steps to reproduce the behavior.

**Expected behavior**
xmrig should start solo mining GUUS from daemon


**Required data**
 - XMRig version 6.22.2

C:\NiceHash\xmrig-6.22.2>C:\NiceHash\xmrig-6.22.2\xmrig.exe -a randomx --url 127.0.0.1:22222 --cpu-priority=0 --user WALLET --daemon
 * ABOUT        XMRig/6.22.2 MSVC/2019 (built for Windows x86-64, 64 bit)
 * LIBS         libuv/1.49.2 OpenSSL/3.0.15 hwloc/2.11.2
 * HUGE PAGES   permission granted
 * 1GB PAGES    unavailable
 * CPU          Intel(R) Xeon(R) CPU E5-4657L v2 @ 2.40GHz (1) 64-bit AES VM
                L2:3.0 MB L3:30.0 MB 12C/24T NUMA:1
 * MEMORY       14.1/31.9 GB (44%)
                Node0_Dimm0: 8 GB DDR3 @ 1866 MHz 99U5471-052.A
                Node0_Dimm1: 8 GB DDR3 @ 1866 MHz 99U5471-052.A
                Node0_Dimm2: 8 GB DDR3 @ 1866 MHz 99U5471-052.A
                Node0_Dimm3: 8 GB DDR3 @ 1866 MHz 99U5471-052.A
 * MOTHERBOARD  Gigabyte Technology Co., Ltd. - To be filled by O.E.M.
 * DONATE       1%
 * ASSEMBLY     auto:intel
 * POOL #1      127.0.0.1:22222 algo rx/0
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled
[2025-01-06 13:38:54.624]  net      127.0.0.1:22222 job error: "Invalid block template received from daemon."

# Discussion History
## SChernykh | 2025-01-06T12:44:45+00:00
What is GUUS? Solo mining is only supported for Monero, Wownero, Zephyr and Townforge coins.

## MaxQuatro | 2025-01-07T08:47:46+00:00
> What is GUUS? Solo mining is only supported for Monero, Wownero, Zephyr and Townforge coins.

Okay, I see. [GUUS](https://guus.website/) is not supported by XMRig. On rplant, XMRig is listed for guus as a recommended miner. Mining is done using the randomx algorithm, so I thought they were "automatically" compatible. Moreover, there was a similar XMRig error on the Zephyr. If it doesn't bother you, please consider the question. After all, one way or another guus will mine XMRig. Thanks for your attention!

## SChernykh | 2025-01-07T12:37:08+00:00
XMRig supports RandomX, and it can mine GUUS in a pool. But to support solo mining, additional changes are required. Zephyr changed something as well, it worked before.

# Action History
- Created by: MaxQuatro | 2025-01-06T10:42:18+00:00
- Closed at: 2025-06-16T15:14:31+00:00
