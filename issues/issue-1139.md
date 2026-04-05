---
title: 3.1.0 how to set CPU usage？
source_url: https://github.com/xmrig/xmrig/issues/1139
author: expressups
assignees: []
labels: []
created_at: '2019-08-26T05:07:41+00:00'
updated_at: '2019-09-28T17:51:28+00:00'
type: issue
status: closed
closed_at: '2019-09-28T17:51:28+00:00'
---

# Original Description
"max-cpu-usage": 50,
How should arrays be set？

# Discussion History
## xmrig | 2019-08-26T11:44:57+00:00
You can change threads count in cpu object https://github.com/xmrig/xmrig/blob/master/doc/CPU.md
Main reason why this option removed is most of users don't ever understand how this option works (or not works), but likely this option will come back with new less confusing name, together with OpenCL backend.
Thank you.

## expressups | 2019-08-26T16:15:52+00:00
My usage scenarios are more complex, maybe multi-core cpus, maybe multiple cpus, and I try to set up threads, but it doesn't always work well. You can add a friendlier option.

## qutimqqcom | 2019-08-26T17:53:36+00:00
threads works  well 
        "cn/r":{
            "intensity": 1,
            "threads": 48,
            "affinity": -1
            },

but   intensity, has no effect
        "rx/loki":{
            "intensity": 2,
            "threads": 2,
            "affinity": -1
            },


## qutimqqcom | 2019-08-28T12:01:10+00:00
so  need  set up cpu usage  whitout  set number of threads
hardware  has different   cpu  units
multiply deploying

"max-cpu-usage": 50  or other precent,
still   best chalange

## shubell | 2019-09-03T06:13:42+00:00
Well this option was a necessity for my environment where i have different a different cpu on every rig and have one startup script for everyone.

## MrCook1es | 2019-09-03T13:49:29+00:00
@xmrig 

I always use 50% on different systems and it works well.
For me it is fundamental to use a percentage value, so as not to have to personalize each combination by setting the number of threads by hand.

What parameter should I set in the new config.json file layout to have 50% CPU usage?

## CrazyBoyFeng | 2019-09-07T03:18:10+00:00
if you are using multi-core cpu, maybe set the affinity mask of xmrig.exe process can help you.

on windows:
`start /affinity 0xAAAAAAAAAAAAAAAA xmrig.exe`
`0xA` is the hex form of binary `1010`, it means just use the 2nd and 4th core for the process. so the command above means only use half of my cores.
i dont know how many cores you have. i have 64, so i need 64 bits mask (16 hex digits "A") for the mask.

on linux please `man taskset` or `taskset -h`

## xmrig | 2019-09-28T17:51:28+00:00
`max-cpu-usage` option reverted back in v4.2 with new name, please read docs carefully https://github.com/xmrig/xmrig/blob/beta/doc/CPU_MAX_USAGE.md

# Action History
- Created by: expressups | 2019-08-26T05:07:41+00:00
- Closed at: 2019-09-28T17:51:28+00:00
