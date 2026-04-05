---
title: Segmentation Fault (core dumped) on Ubuntu 19.10 or upgraded 18.04 to 5.4 RC1
source_url: https://github.com/xmrig/xmrig/issues/1250
author: jims23211
assignees: []
labels:
- need feedback
created_at: '2019-10-24T19:25:36+00:00'
updated_at: '2021-04-12T15:31:25+00:00'
type: issue
status: closed
closed_at: '2021-04-12T15:31:25+00:00'
---

# Original Description
Just a heads up, but running xmrig on the newer ubuntu release (19.10) or 5.4 RC1 or greater will generate "Segmentation Fault (core dumped) after running for 20 minutes or more.  I compile the xmrig code on both systems.  Same result.

# Discussion History
## xmrig | 2019-10-25T08:34:24+00:00
Please provide full information, config file, miner log (at least start and end right before crash)
Thank you.

## jims23211 | 2019-10-28T13:31:43+00:00
Gathering requested information.

## jims23211 | 2019-10-28T19:46:47+00:00
miner@amd3900x:~/xmrig/build$ uname -a
Linux amd3900x 5.4.0-050400rc1-lowlatency #201909301433 SMP PREEMPT Mon Sep 30 18:52:46 UTC 2019 x86_64 x86_64 x86_64 GNU/Linux

[debug.zip](https://github.com/xmrig/xmrig/files/3780370/debug.zip)

Please find attached zip file with hopefully requested data.

Jim

## jims23211 | 2019-10-28T20:01:14+00:00
Update I also have a core dump and kern.log.  If you want the core dump, I will need a place to upload it to, compressed its over 2.5G zipped.  Attached is the kern.log

[kern.zip](https://github.com/xmrig/xmrig/files/3780430/kern.zip)


## xmrig | 2019-10-28T20:10:37+00:00
It might be overclocking issue, especially memory clocks/timing, try reset memory settings to default and check it again.
Thank you.

## jims23211 | 2019-10-28T20:35:07+00:00
Question is why does this not occur on 18.04 when running the overclock settings?  Only reason I was looking at the 5.4 was to monitor cpu temps since 18.04 does not have the right monitoring drivers.


## lss4 | 2019-11-20T08:13:53+00:00
As what I wrote on #1266, it seems the latest 5.4 kernel RCs (from rc6 onwards) might have issues with xmrig.

I'm using latest Manjaro Testing and xmrig segfaults after about an hour of mining with 5.4-rc6 kernel (and higher). With 5.3.11 kernel I do not get any segfault after more than 20 hours of consecutive mining (even with ocl enabled for Radeon RX 5700 XT, although the hashrate from ocl is quite unstable). The CPU is a single EPYC 7551 (not engineering sample). Before 5.4-rc6 kernel I never had any issue with xmrig. Also, I do not use any overclock options.

I think we need to confirm whether upstream changes in the 5.4 kernel is the culprit, and report this issue to the kernel bugzilla instead if it's indeed the case.

EDIT: Since the transition to RandomX I haven't encountered a single segfault, with latest xmrig releases and kernels.

# Action History
- Created by: jims23211 | 2019-10-24T19:25:36+00:00
- Closed at: 2021-04-12T15:31:25+00:00
