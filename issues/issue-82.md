---
title: 'GPU #1: an illegal memory access was encountered cryptonight_extra_cpu_final
  line 247'
source_url: https://github.com/xmrig/xmrig/issues/82
author: kolet
assignees: []
labels: []
created_at: '2017-09-01T12:45:53+00:00'
updated_at: '2017-10-02T11:58:37+00:00'
type: issue
status: closed
closed_at: '2017-10-02T11:58:37+00:00'
---

# Original Description
![image](https://user-images.githubusercontent.com/17353839/29970238-762d56a2-8f2c-11e7-9b91-fd71ba659b01.png)


cant get it started ..

config file is this

`{
    "algo": "cryptonight",
    "background": false,
    "colors": true,
    "donate-level": 5,
    "log-file": null,
    "print-time": 60,
    "retries": 5,
    "retry-pause": 5,
    "threads": [
        {
            "index": 0,
            "threads": 32,
            "blocks": 45,
            "bfactor": 6,
            "bsleep": 25
        },
        {
            "index": 1,
            "threads": 32,
            "blocks": 45,
            "bfactor": 6,
            "bsleep": 25
        }
    ],
    "pools": [
        {
            "url": "pool.minexmr.com:4444",
            "user": "xxxxxxxx.xxxxx",
            "pass": "x",
            "keepalive": true,
            "nicehash": false
        }
    ]
}`


installed latest driver at the time 385.41
and tested out 384.76 

the card is a super jetstream from palit 1070 8GB, with micron memory

# Discussion History
## xmrig | 2017-09-02T00:45:54+00:00
Very strange should work fine with these options, please check work with single card and try change `threads` count. There no others miners working in same time?

## kolet | 2017-09-02T16:33:57+00:00
not working with 1 or 6 or 2..
and no other miners is runing at the same time

# Action History
- Created by: kolet | 2017-09-01T12:45:53+00:00
- Closed at: 2017-10-02T11:58:37+00:00
