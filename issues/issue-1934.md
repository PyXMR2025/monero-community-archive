---
title: Very high CPU usage when GPU mining (Nvidia drivers 457.09, Windows10)
source_url: https://github.com/xmrig/xmrig/issues/1934
author: RainbowMiner
assignees: []
labels:
- bug
created_at: '2020-11-07T10:29:57+00:00'
updated_at: '2021-04-12T14:35:30+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:35:30+00:00'
---

# Original Description
**Describe the bug**
I have experienced very high CPU usage (80-100%) when mining any GPU algorithm on 6 x Nvidia GTX1070, when using driver version 457.09. After rolling back the drivers to 441.41, the CPU usage is back to normal (sub 1%).

**To Reproduce**
Install Nvidia drivers 457.09 and mine any GPU algorithm (of course, use `--no-cpu` parameter)
I have tried Xmrig v6.5.0 and v6.4.0 - both end up with the high CPU usage.

**Expected behavior**
CPU usage should be sub 1%

**Required data**
 - Miner log as text or screenshot
    n/a since miner runs just normal. Only, the systems comes to a crawl with CPU load 80-100%

 - Config file or command line (without wallets):

Problem occurs with all GPU mining algorithms. I picked CryptoNightHeavy as example.

`xmrig.exe --cuda --cuda-loader=xmrig-cuda.dll --cuda-devices=0,1,2,3,4,5 --no-nvml --config=config_CryptoNightHeavy_GTX1070-012345_1.json --algo=cn-heavy/0 -o stratum+tcp://cryptonight_heavy.mine.zergpool.com:4455 -u mywalletaddressremoved -p x,c=BTC,mc=NBR --keepalive --no-cpu --http-enabled --http-host=127.0.0.1 --http-port=35001`

config_CryptoNightHeavy_GTX1070-012345_1.json:
```
{
  "api": {
    "id": null,
    "worker-id": null
  },
  "background": false,
  "colors": true,
  "randomx": {
    "init": -1,
    "numa": true
  },
  "donate-level": 1,
  "log-file": null,
  "print-time": 5,
  "retries": 5,
  "retry-pause": 1,
  "cuda": {
    "enabled": true,
    "loader": "xmrig-cuda.dll",
    "nvml": false,
    "cn-heavy": [
      {
        "index": 0,
        "threads": 14,
        "blocks": 45,
        "bfactor": 6,
        "bsleep": 25,
        "affinity": -1
      },
      {
        "index": 1,
        "threads": 14,
        "blocks": 45,
        "bfactor": 6,
        "bsleep": 25,
        "affinity": -1
      },
      {
        "index": 2,
        "threads": 14,
        "blocks": 45,
        "bfactor": 6,
        "bsleep": 25,
        "affinity": -1
      },
      {
        "index": 3,
        "threads": 14,
        "blocks": 45,
        "bfactor": 6,
        "bsleep": 25,
        "affinity": -1
      },
      {
        "index": 4,
        "threads": 14,
        "blocks": 45,
        "bfactor": 6,
        "bsleep": 25,
        "affinity": -1
      },
      {
        "index": 5,
        "threads": 14,
        "blocks": 45,
        "bfactor": 6,
        "bsleep": 25,
        "affinity": -1
      }
    ]
  },
  "autosave": false
}
```

 - OS: Windows10
 - CPU: Intel(R) Pentium(R) CPU G4560 @ 3.50GHz
 - RAM: 8GB
 - Windows swap file @ 64GB
 - For GPU related issues: 6 x Nvidia GTX1070, driver version 457.09



# Discussion History
# Action History
- Created by: RainbowMiner | 2020-11-07T10:29:57+00:00
- Closed at: 2021-04-12T14:35:30+00:00
