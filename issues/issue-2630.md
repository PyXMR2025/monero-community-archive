---
title: 'OpenCL backend problems '
source_url: https://github.com/xmrig/xmrig/issues/2630
author: ppllgg42
assignees: []
labels: []
created_at: '2021-10-14T18:38:55+00:00'
updated_at: '2021-10-19T17:42:47+00:00'
type: issue
status: closed
closed_at: '2021-10-19T17:42:47+00:00'
---

# Original Description
Hi, 

I have 3 gpus, however I want to run XMRig on just one of them, specifically gpu #2. When I go to pass the OpenCL devices argument in the command line,
$ sudo ./xmrig --opencl-devices=2  
XMRig still uses all 3 of my gpus. Using v6.15.2 on Ubuntu. 

Am I passing this argument incorrectly? How do I select a single gpu? 

Thanks

# Discussion History
## Spudz76 | 2021-10-14T19:02:13+00:00
If you already have a `config.json` with definitions in it, command line args don't override it.  The commandline options are hints to the autoconfigurator, which doesn't run again unless there are no definitions.

You have to delete the opencl algo configurations, then use the commandline option to select just the one.  Or just go in and delete the other two indexes out of every algo definition.

## Spudz76 | 2021-10-14T19:03:31+00:00
Also reasonably sure that option is numbered from zero.  So `=2` is the third GPU...

## ppllgg42 | 2021-10-14T19:10:38+00:00
Awesome, I see that I benchmarked with 3 gpus and have indices for each in config.json. I'll get rid of the ones I don't need, thanks for the help!

## LinuxHeki | 2021-10-19T17:37:48+00:00
I think you can close the issue now...

# Action History
- Created by: ppllgg42 | 2021-10-14T18:38:55+00:00
- Closed at: 2021-10-19T17:42:47+00:00
