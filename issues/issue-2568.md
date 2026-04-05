---
title: 'error while mining '
source_url: https://github.com/xmrig/xmrig/issues/2568
author: sachinvupparige
assignees: []
labels: []
created_at: '2021-08-30T07:11:51+00:00'
updated_at: '2022-07-21T08:55:24+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
 * ABOUT        XMRig/6.14.1 MSVC/2019

 * LIBS         libuv/1.41.0 OpenSSL/1.1.1k hwloc/2.4.1

 * HUGE PAGES   unavailable

 * 1GB PAGES    unavailable

 * CPU          Intel(R) Core(TM) i3-7100U CPU @ 2.40GHz (1) 64-bit AES

                L2:0.5 MB L3:3.0 MB 2C/4T NUMA:1

 * MEMORY       3.3/3.9 GB (86%)

                Bottom-Slot 1(left): 4 GB DDR4 @ 2133 MHz M471A5244CB0-CTD    

                Bottom-Slot 2(right): <empty>

 * MOTHERBOARD  HP - 84B2

 * DONATE       1%

 * ASSEMBLY     auto:intel

 * POOL #1      rx.unmineable.com:3333 algo rx/0

 * COMMANDS     'h' hashrate, 'p' pause, 'r' resume, 's' results, 'c' connection

 * HTTP API     127.0.0.1:60070 

 * OPENCL       disabled

 * CUDA         disabled

[2021-08-30 00:03:17.264]  net      rx.unmineable.com:3333 read error: "connection reset by peer"

[2021-08-30 00:03:23.255]  net      rx.unmineable.com:3333 read error: "connection reset by peer"

[2021-08-30 00:03:29.306]  net      rx.unmineable.com:3333 read error: "connection reset by peer"

[2021-08-30 00:03:35.353]  net      rx.unmineable.com:3333 read error: "connection reset by peer"

[2021-08-30 00:03:40.404]  net      rx.unmineable.com:3333 read error: "connection reset by peer"



# Discussion History
## SChernykh | 2021-08-30T07:22:24+00:00
`connection reset by peer` means the server you're trying to connect to is down or has banned you. It's not an xmrig bug.

## 0xSoliski | 2022-07-20T09:50:53+00:00
> `connection reset by peer` means the server you're trying to connect to is down or has banned you. It's not an xmrig bug.

I have been trying to mine on a pool from XMRig and I get the same response "connection reset by peer". However, I can connect to the same pool using another miner software. If the pool banned me, wouldn't they ban the wallet used or something? Why does it only affect one mining software? Is there an identifier the pool can take a look at other than the wallet address?

## SChernykh | 2022-07-20T13:54:45+00:00
It can be that you connect to a TLS port with TLS off in XMRig, or vice versa. Check your pool's help page and check XMRig config.

## 0xSoliski | 2022-07-21T08:55:24+00:00
> 

This was exactly the problem! Thanks!

# Action History
- Created by: sachinvupparige | 2021-08-30T07:11:51+00:00
