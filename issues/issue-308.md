---
title: Correctly terminate mining process
source_url: https://github.com/xmrig/xmrig/issues/308
author: ManOfFlash
assignees: []
labels:
- bug
created_at: '2018-01-01T16:24:29+00:00'
updated_at: '2021-11-13T16:45:46+00:00'
type: issue
status: closed
closed_at: '2018-11-05T07:06:08+00:00'
---

# Original Description
I launch xmrig.exe from batch file via task scheduler. When i need full power of my PC i kill a xmrig.exe process by task scheduler. Is correct way of ending process exists?

# Discussion History
## thyTwilightGoth | 2018-01-02T08:37:23+00:00
Yes there is a proper way to stop it just press the button combination of Ctrl-c in the window it's running in and it will stop!

## ManOfFlash | 2018-01-02T08:53:56+00:00
Problem is that there is no program window when it launched by itself task scheduler (on PC power up event)

## xmrig | 2018-01-02T17:03:52+00:00
Not so good stop process like this, but for CPU miner it's ok, should be no negative effects, except you can fail to allocate huge pages after some time since system start if you use it.
Thank you.

## ManOfFlash | 2018-01-03T05:46:57+00:00
My rig FX-8350 + RX560 working together. 
So i have OpenCL miner launched by this way too. And 1 of 4 times when i kill it with task manager my monitor go black screen (suspend?) and computer totally freezes, power cycle helping (box has no reset button :( ). Yeah, ATI historically make bad VGA drivers but reliable hardware, that do not die after 5 years because of humidity inside chip.
  

## xmrig | 2018-01-03T06:16:39+00:00
Okay, for GPU not property process exit may cause various negative effects for both AMD/NVIDIA cards.
I mark this issue as bug, probably just need add `CTRL_CLOSE_EVENT` handler, need check it.
Thank you.

## xmrig | 2018-01-03T06:34:31+00:00
Actually handler already added, but not work as expected.

## 2010phenix | 2018-01-03T21:41:41+00:00
he use over task scheduler...
process is Service us i understand...
need only stop schedule task, no?

## ManOfFlash | 2018-01-04T07:21:09+00:00
my _ByTaskXMRGPU.cmd_:
```
@echo off
set exe=MNR_xmrig-amd.exe
:m1
%~dp0\%exe%
GOTO m1
pause
```
So if exe crashed it being relaunched. (Miner exe can work days or can be found not launched by undefined cause. More investigation needed)
My stop plan
1. Finish task in task manager applet
2. Terminate exe by taskmgr.exe

Yes, task sheduler can be setupped for restarting task, but in this case i must disable task when i need full computer power (or finished task relaunches it self). Accidentally i can forget to enable task after using full PC power. So if computer restarted, disabled miner task not get launched.

## mightmay | 2021-03-02T06:42:51+00:00
Hi, how can I properly exit XMrig in linux?
Is `Ctrl + C` the proper way of closing XMrig ?
Thanks

## seantibb | 2021-11-13T16:43:09+00:00
I installed xmrig using the powershell script for setting up miners via https://moneroocean.stream/. The setup didn't start the miner as I got an error. I launched xmrig.exe in the command prompt and things were working well.

I needed to use my pc, but xmrig was consuming 96% CPU. I did the `CTRL  + C` method and the command prompt window closed ... all good, so I thought! Not so ... xmrig.exe was still running per Task Manager and consuming over 90% CPU again. I tried killing the xmrig.exe process multiple times in Task Manager, but it just kept respawning. 

As of 13 Nov 2021, the method I found to stop the xmrig.exe process was as follows:

1. Open services.msc
2. Locate the service named "moneroocean_miner"
3. Stop the service

This service is not provided by xmrig.exe, but rather [install path]\nssm.exe. For good measure, I also changed the startup type from Automatic to Manual so I can control this in the future better.

Hope this helps!

# Action History
- Created by: ManOfFlash | 2018-01-01T16:24:29+00:00
- Closed at: 2018-11-05T07:06:08+00:00
