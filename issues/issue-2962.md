---
title: Failed with error, unsupported algorith on CUDA
source_url: https://github.com/xmrig/xmrig/issues/2962
author: Flurk2818
assignees: []
labels: []
created_at: '2022-03-11T00:28:19+00:00'
updated_at: '2022-03-11T11:02:37+00:00'
type: issue
status: closed
closed_at: '2022-03-11T11:02:36+00:00'
---

# Original Description
**Describe the bug**
Hey, so I am mining DERO with the Astrobwt/v2 algorithm. my CPU works fine, but my GPU won't start. 
![image](https://user-images.githubusercontent.com/101371592/157777921-1bcf1275-7918-458b-aa0d-97536974b6aa.png)


I'm using a GTX1080

"cuda": {
        "enabled": true,
        "loader": null,
        "nvml": true,
        "astrobwt": [
            {
                "index": 0,
                "threads": 32,
                "blocks": 11,
                "bfactor": 6,
                "bsleep": 25,
                "affinity": -1
            }
        ],
        "astrobwt/v2": [
            {
                "index": 0,
                "threads": 32,
                "blocks": 11,
                "bfactor": 6,
                "bsleep": 25,
                "affinity": -1,
                "dataset_host": false
            }

"pools": [
        {
            "algo": "astrobwt/v2",
            "coin": "DERO",
            "url": "daemon+wss://minernode1.dero.io:10100",
            "user": "xxx",
            "enabled": true,
            "tls": true,
            "wss": true,
            "tls-fingerprint": null,
            "daemon": true,
            "socks5": null,
            "daemon-poll-interval": 1000,
            "daemon-zmq-port": -1
        }

I have updated my drivers and windows, rebooted pc, but nothing seems to work. 

I'm sorry if I messed up this report, the first time on GitHub. I just wanna MINE!


# Discussion History
## Spudz76 | 2022-03-11T06:31:55+00:00
Only available in `dev` branch so it isn't in compiled releases.  You must checkout the [`dev` branch from `xmrig-cuda`](https://github.com/xmrig/xmrig-cuda/tree/dev) and build that to use pre-release features.

## Flurk2818 | 2022-03-11T11:02:36+00:00
Ah thank you, i downloaded dev branches but apparently didn't compile it. A friend did so for me and now it works!

# Action History
- Created by: Flurk2818 | 2022-03-11T00:28:19+00:00
- Closed at: 2022-03-11T11:02:36+00:00
