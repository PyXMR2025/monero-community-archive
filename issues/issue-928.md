---
title: cn/gpu (cryptonight-gpu) algorithm support
source_url: https://github.com/xmrig/xmrig/issues/928
author: xmrig
assignees:
- xmrig
labels:
- enhancement
created_at: '2019-02-08T10:54:44+00:00'
updated_at: '2019-02-19T03:10:33+00:00'
type: issue
status: closed
closed_at: '2019-02-19T03:10:33+00:00'
---

# Original Description
In version 2.11 added support for new algorithm `cryptonight/gpu`, short alias `cn/gpu` (original name `cryptonight-gpu`), for upcoming [Ryo currency](https://ryo-currency.com) fork on February 14.

This algorithm very different, it heavy use floating point operations to hurt FPGAs and general purpose CPUs, hashrate balanced between AMD and NVIDIA GPUs, memory requirements decreased, core and power usage increased.

Only 3 things remaining from original cryptonight:
1. The name.
2. Scratchpad size (2 MB).
3. Implode scratchpad method (used cryptonight-heavy).

### Notes
* Because of change scratchpad size (from 4 to 2 MB) miner will not automatically switch algorithm when fork happen, users must manually do it.
* All miners support switch algorithm in runtime to/from other `cn/*` variants, but generally it not so good idea, because optimal settings for `cn/gpu` is different.
* Mining code based on reference implementation, used in xmr-stak (Ryo and xmr-stak it's same people)
* Multihash mode (also known as low_power_mode) for CPU mining not supported.

### Release
* https://github.com/xmrig/xmrig/releases/tag/v2.11.0
* https://github.com/xmrig/xmrig-amd/releases/tag/v2.11.0
* https://github.com/xmrig/xmrig-nvidia/releases/tag/v2.11.0
* https://github.com/xmrig/xmrig-proxy/releases/tag/v2.11.0

# Discussion History
## xmrig | 2019-02-08T11:00:12+00:00
Sample configuration to test new algorithm:
```json
{
    "algo": "cryptonight",
    ...
    "pools": [
        {
            "url": "tnpool.ryo-currency.com:3333",
            "user": "RYoTr42cFt7f6V1EFpAESwMTat74xGiTKEt37PSmGAznX7SMkEz5iLNFMoLbwJCqhrAfAb5Jd3HKqUK3i6SoBaZQKHZrFWmz3jM",
            "pass": "x",
            "rig-id": null,
            "nicehash": false,
            "keepalive": false,
            "variant": "gpu",
            "tls": false,
            "tls-fingerprint": null
        }
    ],
    ...
}
```

## Bathmat | 2019-02-10T19:21:30+00:00
Has there been any benchmarking done? I ran some quick tests, but haven't tried messing with configs/gpu settings much yet. Hashrate for RX470/570/480/580 was between 500-600 h/s with "standard" cn/2 config settings: 
```
        {
            "index": 0,
            "intensity": 896,
            "worksize": 8,
            "strided_index": 2,
            "mem_chunk": 2,
            "unroll": 8,
            "comp_mode": false,
            "affine_to_cpu": false
        },
        {
            "index": 0,
            "intensity": 896,
            "worksize": 8,
            "strided_index": 2,
            "mem_chunk": 2,
            "unroll": 8,
            "comp_mode": false,
            "affine_to_cpu": false
        },
```
```
[2019-02-10 13:17:40] #00, GPU #00 Radeon RX 580 Series (Ellesmere), i:896 (8/256), si:2/2, u:8, cu:36
[2019-02-10 13:17:40]              1.75/3.95/8 GB
[2019-02-10 13:17:40] #01, GPU #00 Radeon RX 580 Series (Ellesmere), i:896 (8/256), si:2/2, u:8, cu:36
[2019-02-10 13:17:40]              1.75/3.95/8 GB
[2019-02-10 13:17:40] #02, GPU #01 Radeon (TM) RX 480 Graphics (Ellesmere), i:896 (8/256), si:2/2, u:8, cu:36
[2019-02-10 13:17:40]              1.75/3.75/4 GB
[2019-02-10 13:17:40] #03, GPU #01 Radeon (TM) RX 480 Graphics (Ellesmere), i:896 (8/256), si:2/2, u:8, cu:36
[2019-02-10 13:17:40]              1.75/3.75/4 GB
[2019-02-10 13:17:41] #04, GPU #02 Radeon RX 570 Series (Ellesmere), i:896 (8/256), si:2/2, u:8, cu:32
[2019-02-10 13:17:41]              1.75/3.75/4 GB
[2019-02-10 13:17:41] #05, GPU #02 Radeon RX 570 Series (Ellesmere), i:896 (8/256), si:2/2, u:8, cu:32
[2019-02-10 13:17:41]              1.75/3.75/4 GB
[2019-02-10 13:17:41] #06, GPU #03 Radeon (TM) RX 470 Graphics (Ellesmere), i:896 (8/256), si:2/2, u:8, cu:32
[2019-02-10 13:17:41]              1.75/3.75/4 GB
[2019-02-10 13:17:41] #07, GPU #03 Radeon (TM) RX 470 Graphics (Ellesmere), i:896 (8/256), si:2/2, u:8, cu:32
[2019-02-10 13:17:41]              1.75/3.75/4 GB
```
```
| THREAD | GPU | 10s H/s | 60s H/s | 15m H/s |
|      0 |   0 |   318.2 |   316.8 |     n/a |
|      1 |   0 |   307.3 |   316.2 |     n/a |
|      2 |   1 |   300.5 |   304.2 |     n/a |
|      3 |   1 |   308.3 |   304.0 |     n/a |
|      4 |   2 |   302.8 |   273.1 |     n/a |
|      5 |   2 |   266.0 |   267.6 |     n/a |
|      6 |   3 |   267.6 |   257.1 |     n/a |
|      7 |   3 |   261.5 |   255.7 |     n/a |
[2019-02-10 13:20:21] speed 10s/60s/15m 2332.1 2294.7 n/a H/s max 2366.7 H/s
```

# Action History
- Created by: xmrig | 2019-02-08T10:54:44+00:00
- Closed at: 2019-02-19T03:10:33+00:00
