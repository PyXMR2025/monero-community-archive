---
title: XMrig + Stellite = reject shares? please Help
source_url: https://github.com/xmrig/xmrig/issues/731
author: nicsan85
assignees: []
labels:
- question
created_at: '2018-08-05T05:51:47+00:00'
updated_at: '2018-08-13T19:04:09+00:00'
type: issue
status: closed
closed_at: '2018-08-13T19:04:09+00:00'
---

# Original Description
Dear XMrig owner & Friends, 
i need help please, 
is it possible to mining Stellite (XTL) with XMrig Amd 2.7.3 ?

or did i put the wrong algo?
already put :
cryptonight
cryptonight-lite
cn-lite
cn-litev7
stellite
stellitev7

and the shares always reject : https://ibb.co/j345GK

heres the config :

    "algo": "cryptonight-lite",
    "api": {
        "port": 0,
        "access-token": null,
        "worker-id": null,
        "ipv6": false,
        "restricted": true
    },
    "background": false,
    "cache": true,
    "colors": true,
    "donate-level": 1,
    "log-file": null,
    "opencl-platform": 0,
    "opencl-loader": "OpenCL.dll",
    "pools": [
        {
            "url": "xtl.miningpool.id:8805",
            "user": "SEiStP7SMy1bvjkWc9dd1t2v1Et5q2DrmaqLqFTQQ9H7JKdZuATcPHUbUL3bRjxzxTDYitHsAPqF8Ee CLw3bW8ARe8rYc1eGiRC4Kww3e37HP",
            "pass": "JANGKRIKBOSS!!",
            "rig-id": null,
            "nicehash": false,
            "keepalive": true,
            "variant": 1
        }
    ],
    "print-time": 60,
    "retries": 5,
    "retry-pause": 5,
    "threads": [
        {
            "index": 0,
            "intensity": 1430,
            "worksize": 8,
            "strided_index": 1,
            "mem_chunk": 2,
            "comp_mode": true,
            "affine_to_cpu": false
        },

can anybody help me?

thanks in advance

# Discussion History
## snipeTR | 2018-08-05T07:45:26+00:00
first please censor adress and pass and pool adress.

## snipeTR | 2018-08-05T07:51:09+00:00

![image](https://user-images.githubusercontent.com/31975916/43683973-aa12e720-989f-11e8-97cd-f96c61132607.png)


your adress with space¿

## xmrig | 2018-08-05T09:33:41+00:00
Key options for mine Stellite `algo` and `variant`:
```json
{
  "algo": "cryptonight",
  ...
  "pools": [
    {
      "url": "...",
      "variant": "xtl",
      ...
    }
 ],
 ...
}
```
More details https://github.com/xmrig/xmrig/blob/master/doc/ALGORITHMS.md
Thank you.

## nicsan85 | 2018-08-06T12:37:16+00:00
ok problm solved!! many thanks Xmrig & dear friends!!

# Action History
- Created by: nicsan85 | 2018-08-05T05:51:47+00:00
- Closed at: 2018-08-13T19:04:09+00:00
