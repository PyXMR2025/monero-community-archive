---
title: Icon of XMRig.exe doesnt show anymore on Taskbar
source_url: https://github.com/xmrig/xmrig/issues/2541
author: Shai0Hulud
assignees: []
labels: []
created_at: '2021-08-14T20:25:25+00:00'
updated_at: '2021-08-14T20:47:56+00:00'
type: issue
status: closed
closed_at: '2021-08-14T20:46:42+00:00'
---

# Original Description
XMRig 6.14.0 / 6.14.1 GCC
Windows 10 64 Bit Pro

Hi!

Before last update (before 6.14.0?) when running XMRig.exe (I used GCC version if that matters), the XMRig Icon was used for it on Taskbar. 

Now it's this generic "i dont have an Icon" Icon ^^

![image](https://user-images.githubusercontent.com/82765139/129459202-b95b57ca-7160-466e-b0a8-a44580fe1707.png)


XMRig 6.12.0 GCC looks like it should look:

![image](https://user-images.githubusercontent.com/82765139/129459213-23407b32-0c13-41da-9d7e-4665bdf3d9fa.png)


# Discussion History
## Shai0Hulud | 2021-08-14T20:37:49+00:00
Okay, I need to add something as somebody else told me that his XMRig 6.14.0/.1 GCC does show the icon on the taskbar.

I need to add that I am running XMRig.exe from a parent folder using a batch file with start-command:

Like "start XMRig\xmrig.exe -c XMRig\config_Monero-XMR.json"

If I run the above command without start-command, it does show the icon.

Is this now something special about windows?

I prefer using "start" as it doesnt leave an empty cmd-window open once I allowed XMRig to start with Admin-Rights.

## Shai0Hulud | 2021-08-14T20:46:42+00:00
Okay, Topic can be closed. It's neither Windows nor the start-command itself.

I somehow started Evolution with "start "Evolution" xmrig\xmrig.exe ..." to name the Window "Evolution"

Which isnt necessary, cause I usually set the title tag in config.json accordingly anyway. Don't know why I did this with the new Evolution batch file I created today. Usually I only do this when running my CLI wallets to be able to see immediately which wallet cli is which.


## Shai0Hulud | 2021-08-14T20:47:56+00:00
Bug was sitting in front of monitor. Running the batchfile with:

start "Name of Program Window" xmrig\xmrig.exe prevents Icon being shown properly.

start xmrig\xmrig.exe is perfectly fine!

My bad!

# Action History
- Created by: Shai0Hulud | 2021-08-14T20:25:25+00:00
- Closed at: 2021-08-14T20:46:42+00:00
