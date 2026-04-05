---
title: 'Windows Server 2016 Core: background, max-cpu-usage not working'
source_url: https://github.com/xmrig/xmrig/issues/183
author: fogoat
assignees: []
labels: []
created_at: '2017-10-30T07:43:07+00:00'
updated_at: '2017-11-27T00:36:29+00:00'
type: issue
status: closed
closed_at: '2017-11-27T00:36:29+00:00'
---

# Original Description
_xmr-stak-cpu_ failed to run for me on Windows Server 2016 core. **xmrig** (gcc & msvc) just okay out of the box. some parameters thought are causing me issues. 

-B and --background is sort of working. xmrig decides to hide the command prompt (or alternative shell) window. xmrig can't run as a daemon when I use the --background parameter? I need to use Task Manager and create another command prompt Window.

I also had to use `--no-color` parameter otherwise some odd movement within the command prompt windows was detected. It is as if I were repositioning the window area manually

Finally, max-cpu-usage seems to be ignored. I tried `--max-cpu-usage=50`, but Task Manager showed vCPU using near 100%. I don't know if this is because it is virtual machine and vCPU is throttled sometimes.

# Discussion History
## xmrig | 2017-11-02T15:01:38+00:00
`-B and --background`
Right it just hide window, it no a Windows Service.

`--no-color`
Some times colors can cause issues, actually I surprised never has problem on regular Windows.

`max-cpu-usage`
How many cores in your virtual machine? Miner required run at least one thread, not possible to throttle it.

## fogoat | 2017-11-02T16:56:16+00:00
Server core uses an alternative she'll I think. I think it is called logonui.exe ?

If I use CMD.exe I think there is no problem with colors.

I have one core on VM. 

## xmrig | 2017-11-02T17:04:43+00:00
On one core no way to use 50% CPU.

# Action History
- Created by: fogoat | 2017-10-30T07:43:07+00:00
- Closed at: 2017-11-27T00:36:29+00:00
