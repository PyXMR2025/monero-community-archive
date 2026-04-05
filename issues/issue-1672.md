---
title: 'connect error: "operation canceled"'
source_url: https://github.com/xmrig/xmrig/issues/1672
author: kamael0909
assignees: []
labels: []
created_at: '2020-05-08T07:07:30+00:00'
updated_at: '2020-08-29T04:22:12+00:00'
type: issue
status: closed
closed_at: '2020-08-29T04:22:12+00:00'
---

# Original Description
OS：Ubuntu 18.04 LTS 

* ABOUT XMRig/5.11.1 gcc/5.4.0
* LIBS libuv/1.34.0 OpenSSL/1.1.1d hwloc/2.1.0
* HUGE PAGES supported
* 1GB PAGES disabled
* CPU Intel(R) Xeon(R) Gold 6266C CPU @ 3.00GHz (2) x64 AES
L2:32.0 MB L3:60.5 MB 32C/64T NUMA:2
* MEMORY 7.5/251.9 GB (3%)
* DONATE 5%
* ASSEMBLY auto:intel
* POOL #1 xmr.f2pool.com:13531 algo auto
* COMMANDS hashrate, pause, resume
* OPENCL disabled
* CUDA disabled
[2020-05-08 02:51:43.988] [xmr.f2pool.com:13531] connect error: "operation canceled"
[2020-05-08 02:52:09.016] [xmr.f2pool.com:13531] connect error: "operation canceled"



# Discussion History
## 0xman | 2020-06-15T15:48:03+00:00
Having the same issue

## SChernykh | 2020-06-16T07:52:41+00:00
The same issue as in can't connect to xmr.f2pool.com:13531? Try other pools, maybe your provider blocks some connections. In this case, pools that enable mining to ports 80 or 443 might work better.

## david-serrano | 2020-06-24T08:28:36+00:00
having this same issue as of last night, tried using the latest release, and also ports 5555 and 443, with tls and without, with worker name as password and without, but nothing seems to work..
This happens on two miners running on windows, however a miner running on Mac is perfectly fine.

just to clarify, this one is for support.xmr:5555, i've also tried 8080 and 443 with no luck, both on command line args and in config.json

# Action History
- Created by: kamael0909 | 2020-05-08T07:07:30+00:00
- Closed at: 2020-08-29T04:22:12+00:00
