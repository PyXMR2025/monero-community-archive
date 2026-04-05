---
title: The xmrig priority setting does not work.
source_url: https://github.com/xmrig/xmrig/issues/2930
author: paolosezart
assignees: []
labels:
- question
created_at: '2022-02-13T15:13:15+00:00'
updated_at: '2022-04-03T08:08:22+00:00'
type: issue
status: closed
closed_at: '2022-04-03T08:08:22+00:00'
---

# Original Description
Version xmrig 6.16.4, when run from the command line with the `--cpu-priority 1` parameter, the priority of the process xmrig.exe it remains "normal", although it should be "very low". The same with the `--cpu-priority 0` parameter
Tested on Windows 7 and windows 10
![CPU_priorety](https://user-images.githubusercontent.com/38177890/153759531-3a23eadd-e4e9-4ccc-8a89-4b6e1637bd2e.jpg)

It also doesn't help to edit the registry to:
```
[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\xmrig.exe\PerfOptions]
"CpuPriorityClass"=dword:00000001
```

What could be the problem?

P.S. When setting the parameter 
`"priority": 0`
in config.json process priority setting works correctly

# Discussion History
## SChernykh | 2022-02-13T18:20:00+00:00
Your command line options get overridden by config.json if you have it in the same folder.

## paolosezart | 2022-02-14T08:22:52+00:00
> Your command line options get overridden by config.json if you have it in the same folder.

This is logical, but I was asking about the command line. What does config.json have to do with it?

## SChernykh | 2022-02-14T08:25:52+00:00
It has everything to do with it. CPU priority is set in config.json too.

## paolosezart | 2022-02-14T08:27:57+00:00
That is, it is impossible to set a priority via the command line? Although there is such a command

## SChernykh | 2022-02-14T08:30:29+00:00
You can set it via command line if you don't have config.json in the folder. Either use command line, or config.json, but not both.

## paolosezart | 2022-02-14T08:32:08+00:00
Thank you, friend.
But config.json I do not use in this case and it is not in the xmrig folder at all. That's why I asked the question

## paolosezart | 2022-02-14T11:47:48+00:00
It turned out to be very simple. The parameter "--cpu-priority 0" when running from the command line or bat file, must be specified at the very end.
It's strange, it doesn't seem to have happened before

## Spudz76 | 2022-02-14T22:48:25+00:00
Oh yeah, that was already known, you just reminded me.

# Action History
- Created by: paolosezart | 2022-02-13T15:13:15+00:00
- Closed at: 2022-04-03T08:08:22+00:00
