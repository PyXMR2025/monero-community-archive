---
title: Error using v3.1.1!
source_url: https://github.com/xmrig/xmrig/issues/1161
author: ttsite
assignees: []
labels:
- question
created_at: '2019-09-04T00:45:37+00:00'
updated_at: '2019-09-04T01:22:31+00:00'
type: issue
status: closed
closed_at: '2019-09-04T01:20:32+00:00'
---

# Original Description
 * ABOUT        XMRig/3.1.1 MSVC/2017
 * LIBS         libuv/1.31.0 OpenSSL/1.1.1c hwloc/2.0.4
 * HUGE PAGES   permission granted
 * CPU          Intel(R) Xeon(R) CPU E3-1230 v3 @ 3.30GHz (2) x64 AES
                L2:0.5 MB L3:16.0 MB 4C/4T NUMA:1
 * DONATE       5%
 * ASSEMBLY     auto:intel
 * POOL #1      pool.minexmr.com:7777 algo auto
 * COMMANDS     hashrate, pause, resume
[2019-09-04 08:44:56.489] [pool.minexmr.com:7777] Unknown/unsupported algorithm
"(null)" detected, reconnect
[2019-09-04 08:44:56.493] [pool.minexmr.com:7777] login error code: 6
[2019-09-04 08:45:02.536] [pool.minexmr.com:7777] Unknown/unsupported algorithm
"(null)" detected, reconnect
[2019-09-04 08:45:02.544] [pool.minexmr.com:7777] login error code: 6

# Discussion History
## xmrig | 2019-09-04T00:50:22+00:00
You must specify `-a cn/r` or `"algo": "cn/r"` in pools object.
Thank you.

## xday3 | 2019-09-04T00:50:31+00:00
Add in your config "algo": "cn/r" if you are mining xmr...if not try to use the correct algo for the coin what you are mining.

## xmrig | 2019-09-04T01:20:32+00:00
#1160 

## ttsite | 2019-09-04T01:22:31+00:00
Thank you! We have solved the problem as you said.

# Action History
- Created by: ttsite | 2019-09-04T00:45:37+00:00
- Closed at: 2019-09-04T01:20:32+00:00
