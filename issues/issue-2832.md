---
title: '## Supported platforms'
source_url: https://github.com/xmrig/xmrig/issues/2832
author: matheusbach
assignees: []
labels: []
created_at: '2021-12-22T16:39:47+00:00'
updated_at: '2024-08-27T23:57:31+00:00'
type: issue
status: closed
closed_at: '2024-08-27T23:57:31+00:00'
---

# Original Description
## Supported platforms
* OpenCL for AMD GPUs
* CUDA for NVIDIA GPUs with [CUDA plugin](https://github.com/xmrig/xmrig-cuda)

## Notes
* All credits for open source implementation to [@SChernykh](https://github.com/SChernykh).
* Release marked as beta, because KawPow algorithm and network protocol is very different from earlier supported.
* Configuration fully compatible with previous version.
* Since network protocol is different, algorithm negotiation and algorithm switching are not supported for KawPow.

## Configuration

Minimum config file:
```json
{
    "autosave": true,
    "cpu": false,
    "opencl": true,
    "cuda": true,
    "pools": [
        {
            "algo": "kawpow",
            "url": "stratum.ravenminer.com:3838",
            "user": "RVN_WALLET",
            "pass": "x",
            "tls": false
        }
    ]
}
```

Or classical command line: `--no-cpu --opencl --cuda -o stratum.ravenminer.com:3838 -a kawpow -u RVN_WALLET`

_Originally posted by @xmrig in https://github.com/xmrig/xmrig/issues/1694#issuecomment-638310915_

# Discussion History
## matheusbach | 2021-12-22T16:46:04+00:00
As the kawpow algorithm is only mined via GPU, to unify the mining via CPU of another algorithm I suggest creating a new parameter in the pools: ```backends```

```json
{
    "autosave": true,
    "cpu": false,
    "opencl": true,
    "cuda": true,
    "pools": [
        {
            "algo": "kawpow",
            "url": "stratum.ravenminer.com:3838",
            "user": "RVN_WALLET",
            "pass": "x",
            "tls": false,
            "backends": [ "cpu", "cuda", "opencl" ]
        }
    ]
}
```

default value: ```all```

## matheusbach | 2021-12-22T16:51:08+00:00
That way user can through the configuration file define multiple algorithms to run simultaneously for each backend.

Example:
```json
{
    "autosave": true,
    "cpu": true,
    "opencl": true,
    "cuda": true,
    "pools": [
        {
            "algo": "kawpow",
            "url": "stratum.ravenminer.com:3838",
            "user": "RVN_WALLET",
            "pass": "x",
            "tls": false,
            "backends": [ "cuda", "opencl" ]
        },
        {
            "algo": "rx/0",
            "url": "anymonerominingpool.com:3838",
            "user": "XMR_WALLET",
            "pass": "x",
            "tls": true,
            "backends": [ "cpu" ]
        },
    ]
}
```

and add other fallback pools for each selected backend

## Spudz76 | 2021-12-22T20:07:49+00:00
No thanks, you can simply run a separate xmrig per backend and do every one of those things.

# Action History
- Created by: matheusbach | 2021-12-22T16:39:47+00:00
- Closed at: 2024-08-27T23:57:31+00:00
