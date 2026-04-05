---
title: freeBSD assertion failure  267
source_url: https://github.com/xmrig/xmrig/issues/3465
author: yueehndnx
assignees: []
labels: []
created_at: '2024-04-18T10:32:06+00:00'
updated_at: '2024-05-21T21:21:38+00:00'
type: issue
status: closed
closed_at: '2024-04-22T15:26:59+00:00'
---

# Original Description
Describe the bug
After build, unable to launch XMRIG. Getting following error:
Assertion failed: (errno == EINTR), function uv__io_poll, file src/unix/kqueue.c, line 267.
Expected behavior
Expected miner to begin mining with config.json parameters And turn on the background. If the background is turned off, the error will not occur
![捕获](https://github.com/xmrig/xmrig/assets/153787441/3751fa5b-777f-4c9d-bec1-fc4a2f3a9aa3)


# Discussion History
## SChernykh | 2024-04-18T17:20:15+00:00
Please try advanced build https://xmrig.com/docs/miner/build/freebsd and also build the original XMRig source code, not the MO version (this repository is for the original XMRig).

## ARPABoy | 2024-05-10T21:43:04+00:00
Same behaviour here compiled with advanced build:
```
/usr/local/bin/xmrig --version
XMRig 6.21.3
 built on May 10 2024 with clang 16.0.6 (https://github.com/llvm/llvm-project.git llvmorg-16.0.6-0-g7cbf1a259152)
 features: 64-bit AES

libuv/1.48.0
OpenSSL/3.0.13
hwloc/2.10.0
```

```
freebsd-version -kru
14.0-RELEASE-p6
14.0-RELEASE-p6
14.0-RELEASE-p6
```

```
uname -a
FreeBSD CidoniaMensae.alfaexploit.com 14.0-RELEASE-p6 FreeBSD 14.0-RELEASE-p6 #0: Tue Mar 26 20:26:20 UTC 2024     root@amd64-builder.daemonology.net:/usr/obj/usr/src/amd64.amd64/sys/GENERIC amd64
```

## hollytiger | 2024-05-21T21:21:37+00:00
got same issue/error msg on mac os 12,7,5
solved by disabling background in config.json



# Action History
- Created by: yueehndnx | 2024-04-18T10:32:06+00:00
- Closed at: 2024-04-22T15:26:59+00:00
