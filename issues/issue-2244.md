---
title: Device specification do not work on config.json
source_url: https://github.com/xmrig/xmrig/issues/2244
author: Jhobean
assignees: []
labels:
- question
created_at: '2021-04-07T14:36:29+00:00'
updated_at: '2021-04-12T13:30:41+00:00'
type: issue
status: closed
closed_at: '2021-04-12T13:30:41+00:00'
---

# Original Description
**Describe the bug**
I have 3 GPU on my computer, I only need to use the second one on XMRIG. I added the device # on the Cuda setting:
```
    "cuda": {
        "enabled": true,
	    "devices":1,
        "loader": null,
        "nvml": true,
        "cn/0": false,
        "cn-lite/0": false,
        "panthera": false,
        "astrobwt": false
    },
```

When i'm doing this, I use GPU0 to mine with Phoenix Miner. XMrig try to acces GPu0 and bloc the minning.

**To Reproduce**
Specific a device on the cuda setting

**Expected behavior**
Xmrig should ignore all other GPU that you do not list on the setting.

**Required data**
 - Miner log as text or screenshot
 - Config file or command line (without wallets)
 - OS: Windows 10
 - For GPU related issues: information about GPUs and driver version.

![image](https://user-images.githubusercontent.com/51728381/113884614-1bf29e00-978d-11eb-8b61-99e512a4f2af.png)


# Discussion History
## SChernykh | 2021-04-07T14:40:47+00:00
There is no such setting `"devices"`. Open config.json after xmrig fills it in, find the algorithm you need and remove entries for GPUs you don't want to use with xmrig.

## Jhobean | 2021-04-07T20:24:23+00:00
Its a feature that can be implemented?  If I use command line to lauch it will work?

## Spudz76 | 2021-04-10T01:43:51+00:00
Yes I have used command line `--cuda-devices=1,2` to ignore GPU0 before.

There just isn't a json element mapped to it.

It may not work except in autoconfig, if your config file has index:0 defined I think it mines on it anyway.

# Action History
- Created by: Jhobean | 2021-04-07T14:36:29+00:00
- Closed at: 2021-04-12T13:30:41+00:00
