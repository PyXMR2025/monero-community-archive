---
title: XMRig RTM RVN in the same computer causes some graphics cards to stop mining.
source_url: https://github.com/xmrig/xmrig/issues/2774
author: CidiRome
assignees: []
labels: []
created_at: '2021-12-02T18:30:46+00:00'
updated_at: '2021-12-15T14:53:10+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Hi.
I'm using XMRig to mine Raven and Raptoreum.
My configuration consist of 2x 3060LHR, 1x 3070LHR and 1x AMD R5 3600.
The 3070LHR is being used by a Flux Miner;
The 2 3060LHR are being used by XMRig to mine Raven;
And the Ryzen 5 3600 is being used by XMRig to mine Raptoreum;
The issue I have is that, at least one of the 3060LHR stops mining when XMRig in mining Raptoreum, some times both (specially on startup of the XMRig that mines RVN after the other is already running).
The picture I'm attaching shows 1 3060 stopping mining when I resume the Raptoreum mining in the other XMRig window and also shows that is start mining again when I pause the Raptoreum mining (Can be seen by the power taken by each graphics card).
Please note that the version in the picture is 6.16.1, but I already tested with 6.16.2 and the result is the same.
Cheers.
![image](https://user-images.githubusercontent.com/39540049/144481132-a22bb1e4-a3e1-4973-8c63-4c0ce37be7ee.png)


# Discussion History
## SChernykh | 2021-12-02T19:09:38+00:00
Set XMRig priority to 0: `--cpu-priority=0` in command line.

## CidiRome | 2021-12-02T20:14:21+00:00
> Set XMRig priority to 0: `--cpu-priority=0` in command line.

And should I use that option in the GPU or CPU miner?
What is that option in config.json if I need to use it in the GPU miner?
Note: For GPU miner I'm using config.json, but for CPU I'm using command line because I don't have an example of config.json for RTM.
Cheers.

## SChernykh | 2021-12-02T20:16:16+00:00
This is for CPU miner.

## CidiRome | 2021-12-02T20:26:08+00:00
> This is for CPU miner.

Won't it cause poor hash rate?
I would also like to use config.json for RTM mining, where can I find examples? And what it the option for --cpu-priority=0 in config.json?
Cheers.

## SChernykh | 2021-12-02T20:29:46+00:00
Hash rate will be almost the same. If you use config.json, find `"priority": null,` there and change it to `"priority": 0,`
Example pool config for RTM:
```
    "pools": [
        {
            "algo": "ghostrider",
            "coin": null,
            "url": "raptoreumemporium.com:3008",
            "user": "YOUR_WALLET_ADDRESS",
            "pass": "x",
...
        }
    ],
```

## CidiRome | 2021-12-02T20:46:59+00:00
Thank you.

"--cpu-priority=0" seems to solve the problem.

Off topic: XMRig is my preferred miner, is there any chance that it could be mining FLUX in the near future?

Cheers.

## Spudz76 | 2021-12-02T23:29:54+00:00
There is at least some reference code for OpenCL for [ZelHash Equihash 125/4](https://github.com/RunOnFlux/ZelHash-reference-miner)

All other implementations seem closed-source so that means you use lolMiner or Gminer for it.  Can't really implement a thing if it's not well-documented and/or has reference code visible ("borrowable").

## CidiRome | 2021-12-02T23:59:06+00:00
Hummm, I see...
Yet, how did the other miners do it?
I'm using miniZ to mine FLUX, but would prefer this one for that too.
Cheers.

# Action History
- Created by: CidiRome | 2021-12-02T18:30:46+00:00
