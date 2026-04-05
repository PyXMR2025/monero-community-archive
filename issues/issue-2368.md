---
title: Pause XMRIG while another Program run
source_url: https://github.com/xmrig/xmrig/issues/2368
author: Unbrecht
assignees: []
labels: []
created_at: '2021-05-12T05:13:25+00:00'
updated_at: '2021-06-08T06:59:18+00:00'
type: issue
status: closed
closed_at: '2021-05-21T20:20:12+00:00'
---

# Original Description
Hello, 

i want to pause mining when other program run like Videorendering or something else. 
For that, i start a new thread t6() from main and check all 500ms if running a selected program.
My problem is, i cant call the non static method isEnabled from Miner.cpp. With right calling `xmrig::Miner miner;
miner.setEnabled(true);` it wont work while calling a delete function.
Can you please help me or exist a easyer way without changing xmrig? Thank you very much.

The changed xmrig.cpp:
[xmrig.zip](https://github.com/xmrig/xmrig/files/6463547/xmrig.zip)

Umbrecht

# Discussion History
## Spudz76 | 2021-05-13T13:18:48+00:00
There is the pause-on-battery feature which may be an example of how to do what you want (flagging to setEnabled that mining should be paused based upon some event elsewhere).

## Fleettelematicssystem | 2021-06-07T22:34:52+00:00
did you manage to solve this?

## Unbrecht | 2021-06-08T06:59:18+00:00
More or less..
I add my function to the timer and this check all one second if run. That works great. 
But i start XMRIG with the Windows Task-Scheduler with the option "Execute independently of the user login" and that don´t work. The problem is, processes running as a service can no longer use FindWindow. The alternate is EnumProcesses but i only got it to run on 32bit. XMRIG should be run on 64bit and so far i couldn´t find a way to run EnumProcesses on 64bit.

# Action History
- Created by: Unbrecht | 2021-05-12T05:13:25+00:00
- Closed at: 2021-05-21T20:20:12+00:00
