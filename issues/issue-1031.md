---
title: In 2.14.4 Masari stopped working
source_url: https://github.com/xmrig/xmrig/issues/1031
author: sergneo
assignees: []
labels: []
created_at: '2019-06-10T07:01:54+00:00'
updated_at: '2019-08-02T12:53:01+00:00'
type: issue
status: closed
closed_at: '2019-08-02T12:53:01+00:00'
---

# Original Description
>  * ABOUT        XMRig-NVIDIA/2.14.4 MSVC/2015
>  * LIBS         libuv/1.29.1 CUDA/9.20 OpenSSL/1.1.1b microhttpd/0.9.63
>  * CPU          Intel(R) Core(TM) i5-4460  CPU @ 3.20GHz x64 AES
>  * GPU #0       PCI:0000:01:00 GeForce GTX 760 @ 1071/3004 MHz 53x18 8x25 arch:3
> 0 SMX:6 MEM:1942/2048 MiB
>  * ALGO         cryptonight/msr, donate=1%
>  * POOL #1      masari.ingest.cryptoknight.cc:3333 variant msr
>  * API BIND     0.0.0.0:82
>  * COMMANDS     hashrate, health, pause, resume
> [2019-06-10 09:57:30] use pool masari.ingest.cryptoknight.cc:3333  masari.ingest.cryptoknight.cc
> [2019-06-10 09:57:30] new job from masari.ingest.cryptoknight.cc:3333 diff 2000 algo cn/msr
> [2019-06-10 09:57:32] rejected (0/1) diff 2000 "Bad share" (89 ms)
> [2019-06-10 09:57:33] rejected (0/2) diff 2000 "Bad share" (299 ms)
> [2019-06-10 09:57:33] rejected (0/3) diff 2000 "Bad share" (509 ms)

Only bad shares, on 2.14.3 everything works

# Discussion History
# Action History
- Created by: sergneo | 2019-06-10T07:01:54+00:00
- Closed at: 2019-08-02T12:53:01+00:00
