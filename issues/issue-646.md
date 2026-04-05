---
title: unknown error
source_url: https://github.com/xmrig/xmrig/issues/646
author: iks13
assignees: []
labels: []
created_at: '2018-05-22T13:00:35+00:00'
updated_at: '2018-05-22T13:02:38+00:00'
type: issue
status: closed
closed_at: '2018-05-22T13:02:38+00:00'
---

# Original Description
I have GeForce GTX 750Ti.
Config:
{
    "algo": "cryptonight",
    "background": false,
    "colors": true,
    "donate-level": 1,
    "log-file": null,
    "print-time": 60,
    "retries": 999,
    "retry-pause": 5,
    "threads": [
        {
            "index": 0,
            "threads": 32,
            "blocks": 20,
            "bfactor": 8,
            "bsleep": 100,
            "affine_to_cpu": false
        }
    ],
    "pools": [
        {
            "url": "_server_:3333",
            "user": "_wallet_",
            "pass": "x",
            "keepalive": true,
            "nicehash": false,
            "variant": -1
        }
    ],
    "api": {
        "port": 0,
        "access-token": null,
        "worker-id": null
    }
}

After start:
 * VERSIONS:     XMRig/2.6.1 libuv/1.19.2 CUDA/9.10 MSVC/2015
 * CPU:                  Intel(R) Core(TM) i5-2500 CPU @ 3.30GHz x64 AES-NI
 * GPU #0:       GeForce GTX 750 Ti @ 1084/2700 MHz 32x20 8x100 arch:50 SMX:5
 * ALGO:         cryptonight, donate=5%
 * POOL #1:      _server_:3333
 * COMMANDS:     hashrate, health, pause, resume
[2018-05-22 15:59:42] use pool _server_:3333 192.168.0.30
[2018-05-22 15:59:42] new job from _server_:3333 diff 181659
[CUDA] Error gpu 0: <cryptonight_extra_cpu_final>:373 "unknown error"

# Discussion History
# Action History
- Created by: iks13 | 2018-05-22T13:00:35+00:00
- Closed at: 2018-05-22T13:02:38+00:00
