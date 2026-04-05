---
title: v2.9.1 seg faults on Ubuntu
source_url: https://github.com/xmrig/xmrig/issues/906
author: MoneroOcean
assignees: []
labels:
- bug
created_at: '2019-01-15T22:43:56+00:00'
updated_at: '2019-01-16T02:34:28+00:00'
type: issue
status: closed
closed_at: '2019-01-16T02:34:28+00:00'
---

# Original Description
```
# ./xmrig
 * ABOUT        XMRig/2.9.1 gcc/7.3.0
 * LIBS         libuv/1.18.0 OpenSSL/1.1.0g microhttpd/0.9.59
 * CPU          Intel Xeon Processor (Skylake, IBRS) (1) x64 AES
 * CPU L2/L3    4.0 MB/16.0 MB
 * THREADS      1, cryptonight, av=0, donate=5%
 * ASSEMBLY     auto:intel
 * POOL #1      donate.v2.xmrig.com:3333 variant auto
 * COMMANDS     hashrate, pause, resume
[2019-01-15 23:15:28] configuration saved to: "/root/xmrig/build/x/xmrig/config.json"
[2019-01-15 23:15:28] use pool donate.v2.xmrig.com:3333  195.201.11.73
[2019-01-15 23:15:28] new job from donate.v2.xmrig.com:3333 diff 1000225 algo cn/2
Segmentation fault (core dumped)
```

# Discussion History
## MoneroOcean | 2019-01-15T22:44:27+00:00
This happens with prebuilt Linux version of xmrig as well.

## SChernykh | 2019-01-15T23:09:59+00:00
@MoneroOcean https://github.com/xmrig/xmrig/pull/907 should fix it, can you check?

## MoneroOcean | 2019-01-15T23:19:20+00:00
@SChernykh Yes, looks like it helps!


## xmrig | 2019-01-16T02:34:28+00:00
v2.9.2 with the fix, released.
Thank you.

# Action History
- Created by: MoneroOcean | 2019-01-15T22:43:56+00:00
- Closed at: 2019-01-16T02:34:28+00:00
