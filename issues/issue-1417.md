---
title: GPU no longer starts mining after updating to Radeon 19.12.2
source_url: https://github.com/xmrig/xmrig/issues/1417
author: mbranchick
assignees: []
labels:
- bug
created_at: '2019-12-14T20:07:33+00:00'
updated_at: '2021-04-12T15:09:33+00:00'
type: issue
status: closed
closed_at: '2021-04-12T15:09:33+00:00'
---

# Original Description
**Describe the bug**
Mining never starts on GPU's.  Miner indicates that OCL is ready, but hashrate is reported as n/a forever.  No increase in power consumption from GPU is observed either.  

**To Reproduce**
Install radeon driver 19.12.2 and attempt to mine randomx algo with GPU

**Expected behavior**
Miner should start and report hashrate.

**Required data**
 - Miner log as text or screenshot: [LOG_no-GPU-Hashrate.txt](https://github.com/xmrig/xmrig/files/3964292/LOG_no-GPU-Hashrate.txt)
 - Config file or command line (without wallets): [config.txt](https://github.com/xmrig/xmrig/files/3964294/config.txt)
 - OS: Windows 10
 - GPU: Vega 56 Radeon; Adrenaline 2020 version 19.12.2 (released on 12/4/2019)

**Additional context**
Other Algo's mine fine like cn/gpu for example, only trying to mine random x causes the problem


# Discussion History
## dedizones | 2019-12-15T09:18:42+00:00
hello, we have all the same concerns, me with my 280x others with 560/570/580, some say to put more virtual memory in Windows, others to put a single core in RX of the configuration file  , and other dataset_host true but it is haphazard luck ... I have about twenty 280x that no longer runs ... and by putting other AMD drivers it does not change.

## SChernykh | 2019-12-15T10:10:33+00:00
It's a driver issue. I can't even debug it because it crashes inside amdocl64.dll when it tries to compile `randomx_init` kernel. Use older driver version for now.

## dedizones | 2019-12-15T10:58:50+00:00
> It's a driver issue. I can't even debug it because it crashes inside amdocl64.dll when it tries to compile `randomx_init` kernel. Use older driver version for now.

the problem if we look at several issues, a lot we have a hashrate problem at zero N / A and many are AMD cards, I find myself in a dead end with my AMD 280x, for my part I tried everything and did nothing  it loads at 99% but with a hashrate at zero I tested all the AMD drivers.

## SChernykh | 2019-12-15T11:55:48+00:00
There are indeed several issues that all result in no hashrate, but this one is unfixable from XMRig side - AMD need to update their driver.

## mbranchick | 2019-12-19T00:32:13+00:00
Confirmed the issue is still present in the 19.2.3 release that went live on 12/16/19

## RGlabs84 | 2019-12-24T04:24:47+00:00
last time i saw something like this, the intensity was too high, that same thing would happen on my vega in TRM until it was adjusted proper(CNR), hwinfo graphing shows an attempt to start mining with opencl, youll see both threads start, one cycle max then 0 the other cycle max then 0, same issues, yes i get its a different miner, i for one cant even get the json to work(just get a screen flicker and close out) and am using all command lines, wish there was one to set intensity for gpu, also i dont under stand why aff for gpu is negaitve value.

## SChernykh | 2020-02-04T22:28:30+00:00
I've just tested #1536 and it works with 19.12.2 and 20.2.1 drivers. Next release will have this fix.

## RGlabs84 | 2020-02-07T05:20:07+00:00
@SChernykh That would be great, but im confused, in your own issues #1535 and #1536 , you claim that it works here, but in #1535 you state that it does NOT work,and it #1536 its added to code commit, SO
For clarity, does the fix work and re-enable(fix ocl) mining on AMD?
and if YES, Then,
When can we expect this release? it obviously a much needed fixed for plenty of us!

## SChernykh | 2020-02-07T06:27:45+00:00
#1535 doesn't work, #1536 works.

# Action History
- Created by: mbranchick | 2019-12-14T20:07:33+00:00
- Closed at: 2021-04-12T15:09:33+00:00
