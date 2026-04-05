---
title: 'Process Improvement: Accepted Share show GPU #'
source_url: https://github.com/xmrig/xmrig/issues/1791
author: Vestibule22
assignees: []
labels:
- enhancement
- opencl
- CUDA
created_at: '2020-07-29T04:09:59+00:00'
updated_at: '2021-04-12T14:52:35+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:52:35+00:00'
---

# Original Description
Requesting a process improvement to include GPU# for accepted share in xmrig.  That way we will know how each GPU is performing and know if settings need to be adjusted for each GPU

# Discussion History
## cyberlink1 | 2020-09-16T12:13:20+00:00
I would add that the API needs Accepted Shares(per C/GPU)/submitted Shares(per C/GPU)/Watts per GPU/Temperature per GPU

These are standard in most of the miners API's.

## xmrig | 2020-09-16T13:13:01+00:00
Watts/Temperature per GPU available via `GET /2/backends`.
Thank you.

## cyberlink1 | 2020-09-16T18:05:34+00:00
I dont see it.

```
curl http://localhost:4028/2/backends
{
    "id": "064e2c5942aaf146",
    "worker_id": "mining-rig-amd",
    "version": "2.14.6",
    "kind": "amd",
    "ua": "XMRig-AMD/2.14.6 (Linux x86_64) libuv/1.31.0 gcc/5.4.0",
    "cpu": {
        "brand": "AMD FX(tm)-8300 Eight-Core Processor           ",
        "aes": true,
        "x64": true,
        "sockets": 1
    },
    "algo": "cryptonight/gpu",
    "hugepages": false,
    "donate_level": 1,
    "hashrate": {
        "total": [
            1011.76,
            1013.01,
            1013.17
        ],
        "highest": 1196.25,
        "threads": [
            [
                249.55,
                243.68,
                249.4
            ],
            [
                250.32,
                254.21,
                250.04
            ],
            [
                256.17,
                257.61,
                257.19
            ],
            [
                255.71,
                257.49,
                256.54
            ]
        ]
    },
    "results": {
        "diff_current": 47414,
        "shares_good": 5676,
        "shares_total": 5676,
        "avg_time": 38,
        "hashes_total": 217453368,
        "best": [
            100907718,
            63811033,
            56779505,
            41113321,
            38814860,
            30114186,
            28831886,
            24720029,
            19567220,
            19475970
        ],
        "error_log": []
    },
    "connection": {
        "pool": "pool.ryo-currency.com:3333",
        "uptime": 219751,
        "ping": 244,
        "failures": 0,
        "error_log": []
    }
}
```


Command line used to start XMRig

./xmrig-amd --url pool.ryo-currency.com:3333 --user \<my wallet\> --rig-id=\<my rig id\> --pass x --donate-level 1 --algo=cryptonight/gpu --api-port=4028


## xmrig | 2020-09-16T19:03:09+00:00
This endpoint for GPUs available since v5.
Thank you.

## cyberlink1 | 2020-09-16T19:37:26+00:00
xmrig-6.3.2

./xmrig --no-cpu --url pool.ryo-currency.com:3333 --user \<my wallet\> --rig-id=\<my rig id\> --pass x --donate-level 1 --algo=cn/gpu --http-port=4028 --opencl

[2020-09-16 14:25:47.095]  net      pool.ryo-currency.com:3333 unknown algorithm, make sure you set "algo" or "coin" option

but the new version does not seem to know about the cn/gpu so Im using the older version. 

Can you recommend the right algo or a more current version that supports the cn/gpu algo?

## xmrig | 2020-09-16T20:24:01+00:00
Latest version with `cn/gpu` support is 5.9.0 or 5.11.3 if you enable it on compile time you can also use this fork https://github.com/MoneroOcean/xmrig/

## cyberlink1 | 2020-09-16T22:40:21+00:00
Ok, 5.9.0 is up. Though it is returning 0's for the health check I can at least work with it to pull the data from the API. Ill work on the plugin and get it pulling the stats for the newer versions.

```
                "health": {
                    "temperature": 0,
                    "power": 0,
                    "clock": 0,
                    "mem_clock": 0,
                    "rpm": 0
                }

```
Was the cn/gpu algo removed after 5.9.0 for a reason?


# Action History
- Created by: Vestibule22 | 2020-07-29T04:09:59+00:00
- Closed at: 2021-04-12T14:52:35+00:00
