---
title: '"--cpu-priority=0" still not being honored. '
source_url: https://github.com/xmrig/xmrig/issues/3422
author: ghost
assignees: []
labels:
- question
created_at: '2024-02-14T18:06:08+00:00'
updated_at: '2024-02-21T20:38:55+00:00'
type: issue
status: closed
closed_at: '2024-02-21T20:38:55+00:00'
---

# Original Description
After using "--cpu-priority=0" at the end of my command line - however the top command reveals this has done nothing.

after some basic research I saw this issue was referenced in the past and "closed as fixed"

https://github.com/xmrig/xmrig/issues/2351

I am not able to get the command to work. 

# Discussion History
## ghost | 2024-02-14T18:13:16+00:00
Actually after more testing, it is being honored, but --cpu-priority=0 is giving the process NI of 5 when 19 should be expected based on comments in the above mentioned issue.

--cpu-priority=1 gives NI of 0

--cpu-priority=2 gives NI of -5

after testing --cpu-priority=0 NI 5 has proven not sufficient to prevent cpu disruptions to other processes in my usecase. Ideally we want 19, not 5. 

## ghost | 2024-02-14T18:16:06+00:00
I found a personal workaround by prefixing the command with nice -n 19 in ubuntu 

## SChernykh | 2024-02-14T18:19:29+00:00
https://github.com/xmrig/xmrig/blob/master/src/base/kernel/Platform_unix.cpp#L118

NI 5 is for cpu-priority 1. cpu-priority 0 should be 19, and that value goes directly to `setpriority(PRIO_PROCESS, 0, prio);` system call.

## SChernykh | 2024-02-14T18:22:24+00:00
Please check the niceness of individual threads in htop, like in this comment: https://github.com/xmrig/xmrig/issues/2351#issuecomment-844030660
Mining threads should have NI 19, but the regular `top` will show 5 because main thread is 5.

## ghost | 2024-02-14T18:30:31+00:00
![image](https://github.com/xmrig/xmrig/assets/117243445/061035c8-4476-4c60-a3e4-15e53f0c651f)

Yes I do see that. Would using -n 19 do anything to help my issue? I have another process running which is still online however its not responding fast enough and its causing service disruptions. Since the process itself uses almost no cpu, im hoping to have both the miner and the process running.

So far using --cpu-priority=0 does not seem extreme enough to limit the miner from causing disruptions of the other process. 


## SChernykh | 2024-02-14T18:34:46+00:00
Increase priority of that other process? Maybe also use 1 less mining thread, so you always have at least 1 available CPU core.

## ghost | 2024-02-14T18:50:30+00:00
I think that is part of the problem. Is it possible to mine with half a core? lol

## ghost | 2024-02-14T18:51:32+00:00
thanks for your time and quick assistance, I will close this issue because the parameter seems to be working as intended.

# Action History
- Created by: ghost | 2024-02-14T18:06:08+00:00
- Closed at: 2024-02-21T20:38:55+00:00
