---
title: CL_INVALID_KERNEL_NAME
source_url: https://github.com/xmrig/xmrig/issues/1242
author: Amf1k
assignees: []
labels: []
created_at: '2019-10-14T08:52:30+00:00'
updated_at: '2019-11-22T06:17:19+00:00'
type: issue
status: closed
closed_at: '2019-11-22T06:17:19+00:00'
---

# Original Description
![error](https://user-images.githubusercontent.com/4735986/66739142-7f965680-ee89-11e9-9196-9965ebf8d456.PNG)

Config
```
{
  "api": {
    "id": null,
    "worker-id": null
  },
  "http": {
    "enabled": false,
    "host": "127.0.0.1",
    "port": 0,
    "access-token": null,
    "restricted": true
  },
  "autosave": true,
  "background": false,
  "colors": true,
  "randomx": {
    "init": -1,
    "numa": true
  },
  "cpu": {
    "enabled": false
  },
  "opencl": {
    "enabled": true,
    "cache": true,
    "loader": null,
    "platform": "AMD",
    "cn-heavy": [
      {
        "index": 0,
        "intensity": 16,
        "worksize": 8,
        "strided_index": [1, 2],
        "threads": [-1, -1],
        "unroll": 8
      }
    ],
    "cn-lite": [
      {
        "index": 0,
        "intensity": 280,
        "worksize": 8,
        "strided_index": [1, 2],
        "threads": [-1, -1],
        "unroll": 8
      }
    ],
    "cn-pico": [
      {
        "index": 0,
        "intensity": 1000,
        "worksize": 8,
        "strided_index": [2, 2],
        "threads": [-1, -1],
        "unroll": 8
      }
    ],
    "cn/2": [
      {
        "index": 0,
        "intensity": 120,
        "worksize": 8,
        "strided_index": [2, 2],
        "threads": [-1, -1],
        "unroll": 8
      }
    ],
    "cn/gpu": [
      {
        "index": 0,
        "intensity": 312,
        "worksize": 8,
        "threads": [-1],
        "unroll": 1
      }
    ],
    "rx": [
      {
        "index": 0,
        "intensity": 128,
        "worksize": 8,
        "threads": [-1, -1],
        "bfactor": 6,
        "gcn_asm": false,
        "dataset_host": true
      }
    ],
    "cn/0": false,
    "cn-lite/0": false
  },
  "donate-level": 5,
  "donate-over-proxy": 1,
  "log-file": null,
  "pools": [
    {
      "algo": null,
      "coin": "monero",
      "url": "randomx-benchmark.xmrig.com:7777",
      "user": "47wcnDjCDdjATivqH9GjC92jH9Vng7LCBMMxFmTV1Ybf5227MXhyD2gXynLUa9zrh5aPMAnu5npeQ2tLy8Z4pH7461vk6uo",
      "pass": "x",
      "rig-id": null,
      "nicehash": false,
      "keepalive": false,
      "enabled": true,
      "tls": false,
      "tls-fingerprint": null,
      "daemon": false
    }
  ],
  "print-time": 60,
  "retries": 5,
  "retry-pause": 5,
  "syslog": false,
  "user-agent": null,
  "watch": true
}

```

# Discussion History
## Wacholek | 2019-11-03T17:18:12+00:00
I have the same but using 6xHD6990. Windows 7 and 14.4 catalyst driver. The same on CNR algo. 
No problem on xmrig-amd v.2.14.6.

## Amf1k | 2019-11-21T10:00:16+00:00
@xmrig hi! will there be some solution? or is this normal behavior?

## Wacholek | 2019-11-21T10:36:20+00:00
On new 5.0.1 there is different behavior. @Amf1k try new version and post if it is ok. 

![image](https://user-images.githubusercontent.com/38529376/69330290-f118b000-0c52-11ea-9af2-bbcdf031cf88.png)



## Wacholek | 2019-11-21T10:56:01+00:00
On CN/R algo works ok.


## Amf1k | 2019-11-22T06:17:19+00:00
oh.... its fixed. sorry

# Action History
- Created by: Amf1k | 2019-10-14T08:52:30+00:00
- Closed at: 2019-11-22T06:17:19+00:00
