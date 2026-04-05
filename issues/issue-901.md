---
title: Cryptic error when running with default config
source_url: https://github.com/xmrig/xmrig/issues/901
author: duzenko
assignees: []
labels: []
created_at: '2018-12-30T07:53:05+00:00'
updated_at: '2019-03-17T16:33:53+00:00'
type: issue
status: closed
closed_at: '2019-03-17T16:33:53+00:00'
---

# Original Description
```
 * ABOUT        XMRig-NVIDIA/2.8.4 MSVC/2015
 * LIBS         libuv/1.23.0 CUDA/8.0 OpenSSL/1.1.1 microhttpd/0.9.59
 * CPU          Intel(R) Core(TM)2 Duo CPU     E7200  @ 2.53GHz x64 -AES
 * GPU #0       PCI:0000:03:00 GeForce GTX 1060 3GB @ 1708/4004 MHz 26x27 6x25 arch:61 SMX:9
 * GPU #1       PCI:0000:04:00 GeForce GTX 1060 3GB @ 1835/4004 MHz 26x27 6x25 arch:61 SMX:9
 * GPU #2       PCI:0000:05:00 GeForce GTX 1060 3GB @ 1759/4004 MHz 26x27 6x25 arch:61 SMX:9
 * ALGO         cryptonight, donate=5%
 * POOL #1      donate.v2.xmrig.com:3333 variant auto
 * COMMANDS     hashrate, health, pause, resume
[2018-12-30 09:49:44] use pool donate.v2.xmrig.com:3333  195.201.11.112
[2018-12-30 09:49:44] new job from donate.v2.xmrig.com:3333 diff 1000225 algo cn/2
[CUDA] Error gpu [CUDA] Error gpu 02: <: <cryptonight_extra_cpu_finalcryptonight_extra_cpu_final>:>:391391 " "unspecified launch failureunspecified launch failure""

```

# Discussion History
## DeadManWalkingTO | 2019-03-17T15:51:39+00:00
**CPU Miner**
For [xmrig-nvidia](https://github.com/xmrig/xmrig-nvidia) please use [xmrig-nvidia/issues](https://github.com/xmrig/xmrig-nvidia/issues).

I think this issue can be closed.
Thank you!

# Action History
- Created by: duzenko | 2018-12-30T07:53:05+00:00
- Closed at: 2019-03-17T16:33:53+00:00
