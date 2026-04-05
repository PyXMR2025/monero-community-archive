---
title: Hashrate drops off after random time period
source_url: https://github.com/xmrig/xmrig/issues/582
author: bpg2001bpg
assignees: []
labels: []
created_at: '2018-04-23T18:26:24+00:00'
updated_at: '2019-03-17T16:31:26+00:00'
type: issue
status: closed
closed_at: '2019-03-17T16:31:26+00:00'
---

# Original Description

![xmrig](https://user-images.githubusercontent.com/38667164/39143561-1b01aaca-46e3-11e8-8f84-7b8393ccfea8.JPG)

[Config.zip](https://github.com/xmrig/xmrig/files/1939406/Config.zip)

Hello, I could use some assistance figuring out why my hashrate drops off. 
The miner will mine consistently at 150H/S for a period time and then drop down to about 15-20.

The period of time that it mines consistently at 150 is variable. I've watched it hash for several hours without problems, but inevitably it will drop. As you can see in the picture, this time it was only a few minutes.

I have attached my config.json and system info.




# Discussion History
## xmrig | 2018-04-23T18:36:36+00:00
You run miner in virtual environment, hashrate vary dependent on your neighbors. If in other virtual machines someone run high intensivity CPU tasks, you hashrate will drop. Also may possible is your CPU usage throttled by hypervisor.
Thank you.

## bpg2001bpg | 2018-04-23T20:45:36+00:00
Thank you for the quick response. You are right about the virtual environment. I don't think the issue is related to neighbors because of the behavior. I have several VMs running the miner, both windows and ubuntu, and all exhibit the same behavior: Mine for some time at around 150, then drop down to 15-20. The hash rate doesn't ever increase after, unless, I stop them, wait for some time and then start them again. I don't think azure throttles VM CPU loads, but that might be what is happening. Do you have any suggestions for miner configuration or computer settings (either windows or ubuntu) that may help, or optimize? Thanks again.

## DeadManWalkingTO | 2019-03-17T13:43:39+00:00
Runing miner in virtual environment like AWS have limitations such as  [CPU Credits](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/burstable-credits-baseline-concepts.html).

I think this issue can be closed.
Thank you!

# Action History
- Created by: bpg2001bpg | 2018-04-23T18:26:24+00:00
- Closed at: 2019-03-17T16:31:26+00:00
