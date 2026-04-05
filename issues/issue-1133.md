---
title: 'xmrig 3.1: syslog regression'
source_url: https://github.com/xmrig/xmrig/issues/1133
author: k0ste
assignees: []
labels:
- bug
created_at: '2019-08-22T12:17:19+00:00'
updated_at: '2019-08-27T04:45:16+00:00'
type: issue
status: closed
closed_at: '2019-08-27T04:45:16+00:00'
---

# Original Description
```
-- Logs begin at Thu 2019-02-14 08:06:08 +07. --
Aug 22 19:12:07 WorkStation systemd[1]: Starting XMRig Daemon for xmrig...
Aug 22 19:12:07 WorkStation xmrig[3901]:  * ABOUT        XMRig/3.1.0 gcc/9.1.0
Aug 22 19:12:07 WorkStation xmrig[3901]:  * LIBS         libuv/1.30.1 OpenSSL/1.1.1c hwloc/1.11.12
Aug 22 19:12:07 WorkStation xmrig[3901]:  * CPU          Intel(R) Core(TM) i7-8565U CPU @ 1.80GHz (1) x64 AES
Aug 22 19:12:07 WorkStation xmrig[3901]:                 L2:1.0 MB L3:8.0 MB 4C/4T NUMA:1
Aug 22 19:12:07 WorkStation xmrig[3901]:  * DONATE       5%
Aug 22 19:12:07 WorkStation xmrig[3901]:  * ASSEMBLY     auto:intel
Aug 22 19:12:07 WorkStation xmrig[3901]:  * POOL #1      monero.napaster.name:14433 algo cn/r
Aug 22 19:12:07 WorkStation xmrig[3901]:  * COMMANDS     hashrate, pause, resume
Aug 22 19:12:07 WorkStation systemd[1]: Started XMRig Daemon for xmrig.
Aug 22 19:12:08 WorkStation xmrig[3901]: nero.napaster.name:14433 TLSv1.2 51.15.55.162
Aug 22 19:12:08 WorkStation xmrig[3901]:  (SHA-256): "c38886efdee542ebd99801b75c75d3498d97978bbcdec07c7271cb19729e014f"
Aug 22 19:12:08 WorkStation xmrig[3901]: m monero.napaster.name:14433 diff 120001 algo cn/r height 1906400
Aug 22 19:12:08 WorkStation xmrig[3901]: rofile  *  (1 threads) scratchpad 2048 KB
Aug 22 19:12:08 WorkStation xmrig[3901]:  threads 1(1) huge pages 1/1 100% memory 2048 KB (495 ms)
Aug 22 19:12:14 WorkStation xmrig[3901]: m monero.napaster.name:14433 diff 120001 algo cn/r height 1906400
Aug 22 19:13:08 WorkStation xmrig[3901]: 0s/15m 76.1 n/a n/a H/s max 83.4 H/s
Aug 22 19:13:14 WorkStation xmrig[3901]: m monero.napaster.name:14433 diff 120001 algo cn/r height 1906400
Aug 22 19:13:32 WorkStation systemd[1]: Stopping XMRig Daemon for xmrig...
Aug 22 19:13:32 WorkStation xmrig[3901]: eived, exiting
Aug 22 19:13:32 WorkStation systemd[1]: xmrig@xmrig.service: Main process exited, code=dumped, status=11/SEGV
Aug 22 19:13:32 WorkStation systemd[1]: xmrig@xmrig.service: Failed with result 'core-dump'.
Aug 22 19:13:32 WorkStation systemd[1]: Stopped XMRig Daemon for xmrig.
```

First ~12 symbols of each string is eaten.

# Discussion History
## xmrig | 2019-08-22T12:56:26+00:00
Confirmed. Thank you.

## xmrig | 2019-08-22T17:16:42+00:00
Fixed in dev branch.

# Action History
- Created by: k0ste | 2019-08-22T12:17:19+00:00
- Closed at: 2019-08-27T04:45:16+00:00
