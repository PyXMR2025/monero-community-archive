---
title: Set max. CPU load
source_url: https://github.com/xmrig/xmrig/issues/3337
author: fohnbit
assignees: []
labels: []
created_at: '2023-09-22T07:36:57+00:00'
updated_at: '2025-06-16T19:56:40+00:00'
type: issue
status: closed
closed_at: '2025-06-16T19:56:40+00:00'
---

# Original Description
Hello!

Is it possible to set the max CPU load? I would like to run in the background and should max 15% CPU load.

# Discussion History
## geekwilliams | 2023-09-22T07:45:08+00:00
Please look over the comments under the item max-threads-hint on the xmrig documentation page [here](https://xmrig.com/docs/miner/config/cpu).  Your ability to set an exact usage depends on a couple of things noted there

## fohnbit | 2023-09-22T07:59:25+00:00
Thank you.

But I´m not sure if my config is correct, when I not use autosave.
I use now this;
`{
    "autosave": false,
    "cpu": {
		"enabled": true,
		"max-threads-hint": 15
	},
    "opencl": false,
    "cuda": false,
    "pools": [
        {
            "url": "xmrpool.eu:9999",
            "user": "----",
            "keepalive": true,
            "tls": true
        }
    ]
}`

I reduce the CPU from 80% to 30%. But did with this the miner correct working?

EDIT:
I found also:
pause-on-active

What did mean "Enable or disable pause mine when the user is active"? When is a user active? When logged in, when moving mouse?

Thank you!

## geekwilliams | 2023-09-22T08:47:35+00:00
Happy to help. 

I believe your parameters are correct. There is a limitation with the "max-threads-hint", in that you need to pick a percentage that equals the the target thread count divided by the total thread count. For example, if you have 4 threads, then your options are 25%, 50%, 75%, and 100%. Any other percentage chosen is less likely have the intended effect. 

The "pause-on-active" parameter allows xmrig to monitor for user input (keyboard and mouse) and pause when the user is active. There is a timeout you can set so that xmrig will not continue to mine until after a certain period. This feature only works on windows for now. 

- If the xmrig executable is used in a windows service context via NSSM or similar utility, it does not have the ability to monitor user input and thus the pause-on-active parameter has no effect. 
- If "background": true, and xmrig is running in user space then the pause-on-active feature works normally. 

## fohnbit | 2023-09-24T20:17:05+00:00
Thank you!

Well, when I set "max-threads-hint" to 1, even my workstation has 25% CPU Load, while my server just 5% had.
Is it not possible to set a lower CPU usage on my workstation, or is this the minimum CPU Load for mining?

Edit:
Just a question about threads. When I run this command:
wmic cpu get NumberOfCores,NumberOfLogicalProcessors

I get:
`NumberOfCores  NumberOfLogicalProcessors  

8              16`

Which one is the info for threads?

## geekwilliams | 2023-09-25T07:08:48+00:00
You can only set the utilization percentage to match the number of threads you want to use devided by the total number of threads available, (multiplied by 100 for percentage). 

Does your workstation have 2 cores and 4 threads? If so, then the lowest utilization you can get to is 25% mining on one thread. 

With the wmic command, you're looking for the MumberOfLogicalProcessors value. That tells you how many threads are available on your system. In the case of your output '8 16', the cpu has 8 cores and 16 threads. If you only want to use one mining thread on a 16 thread machine, that would be equal to about 6% cpu utilization.

## fohnbit | 2023-09-25T07:28:21+00:00
Thank you. So "NumberOfLogicalProcessors" are the "threads". 

## fohnbit | 2023-09-25T08:37:17+00:00
Just a small second question:
It seems it made no difference in CPU load, if I use on my 16 thread CPU:
"max-threads-hint": 1
or
"max-threads-hint": 6

The CPU load is always around 15%-17%

So when I set to all workstations
"max-threads-hint": 1
it seems it use the lowest CPU load.

Maybe you can confirm, that the mining with 1 are same effective as with 6 (CPU load ist the same)

## SChernykh | 2023-09-25T08:46:16+00:00
`max-threads-hint` only works when xmrig auto-generates thread configs for each algorithm, so you need to find `rx` line in config.json and delete it before changing `max-threads-hint`.

# Action History
- Created by: fohnbit | 2023-09-22T07:36:57+00:00
- Closed at: 2025-06-16T19:56:40+00:00
