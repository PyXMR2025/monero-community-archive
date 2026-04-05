---
title: Kowpow issue...
source_url: https://github.com/xmrig/xmrig/issues/1767
author: needhelp101
assignees: []
labels: []
created_at: '2020-07-08T17:13:19+00:00'
updated_at: '2020-07-09T18:14:51+00:00'
type: issue
status: closed
closed_at: '2020-07-09T18:14:51+00:00'
---

# Original Description
Hi, 

So trying to test out some Kowpow mining and keep getting hit with this error..

 * ASSEMBLY     auto:intel
 * POOL #1      solo-rvn.2miners.com:7070 algo kawpow
 * COMMANDS     hashrate, pause, resume
 * OPENCL       disabled (failed to load OpenCL runtime)
 * CUDA         disabled
[2020-07-08 19:12:00.950]  net      use pool solo-rvn.2miners.com:7070  51.89.96.116
[2020-07-08 19:12:00.951] [solo-rvn.2miners.com:7070] incompatible/disabled algorithm "kawpow" detected, reconnect
[2020-07-08 19:12:00.951]  net      no active pools, stop mining

using xmrig 6.2.2

Any help would be great... thanks 

# Discussion History
## snipeTR | 2020-07-08T20:16:08+00:00
try this config.json
{
    "autosave": true,
    "donate-level": 1,
    "cpu": true,
    "opencl": false,
    "cuda": false,
    "pools": [
        {
            "coin": "raven",
            "algo": "kawpow",
            "url": "solo-rvn.2miners.com:7070",
            "user": "your wallet adress",
            "pass": "x",
            "tls": false,
            "keepalive": true,
            "nicehash": false
        }
    ]
}

## needhelp101 | 2020-07-08T20:21:38+00:00
same problem, am confused as hell other miners work just fine and seems to be xmrig on its own having an issue

## Spudz76 | 2020-07-09T02:39:11+00:00
I thought kawpow/rvn is GPU only in general.  It is GPU only with xmrig at least...
https://github.com/xmrig/xmrig/pull/1694

## STSMiner | 2020-07-09T04:46:37+00:00
> 
> 
> I thought kawpow/rvn is GPU only in general. It is GPU only with xmrig at least...
> #1694

The issue is with AMD cards, the app fails with the algo and then fails to load the OpenCL part.


    ASSEMBLY auto:intel
    POOL #1 solo-rvn.2miners.com:7070 algo kawpow
    COMMANDS hashrate, pause, resume
    OPENCL disabled (failed to load OpenCL runtime)
    CUDA disabled
    [2020-07-08 19:12:00.950] net use pool solo-rvn.2miners.com:7070 51.89.96.116
    [2020-07-08 19:12:00.951] [solo-rvn.2miners.com:7070] incompatible/disabled algorithm "kawpow" detected, reconnect
    [2020-07-08 19:12:00.951] net no active pools, stop mining



## snipeTR | 2020-07-09T05:52:37+00:00
![image](https://user-images.githubusercontent.com/31975916/87002074-86a48800-c1c1-11ea-81e9-2ca3239bc670.png)



## needhelp101 | 2020-07-09T06:40:44+00:00
I can clearly see that, but works perfectly fine on all other miners.. and only seems to have an issue with XMRig

## needhelp101 | 2020-07-09T06:41:41+00:00
so why is it failing, when on all the others it opens fine and runs... recompiled, updated, added, reinstalled a million times by now & still same issue only with XMRig

## snipeTR | 2020-07-09T17:28:38+00:00
https://github.com/xmrig/xmrig-cuda

## needhelp101 | 2020-07-09T17:45:02+00:00
i got amd cards... why would i be using cuda ???

## xmrig | 2020-07-09T18:02:08+00:00
This error means the miner failed to load **OpenCL.dll** (Windows) or **libOpenCL.so** (Linux) try find it in your system, make sure `"loader"` in `"opencl"` object set to `null`.
Thank you.

## needhelp101 | 2020-07-09T18:14:48+00:00
heh, perfect thank you for the help xD

# Action History
- Created by: needhelp101 | 2020-07-08T17:13:19+00:00
- Closed at: 2020-07-09T18:14:51+00:00
