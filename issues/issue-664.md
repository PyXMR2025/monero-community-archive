---
title: Not able to run and create a release Visual Studio 2015
source_url: https://github.com/xmrig/xmrig/issues/664
author: mikegscott
assignees: []
labels:
- question
created_at: '2018-05-29T23:23:10+00:00'
updated_at: '2018-06-17T18:01:07+00:00'
type: issue
status: closed
closed_at: '2018-06-17T18:01:07+00:00'
---

# Original Description
I built the XMRig in visual studio 2015. I did both debug and release. When I clicked "F5" or "Local Windows Debugger" I get an error saying "Unable to start the program C: ... \ALL_BUILD.   Access is  Denied." 

How can I resolve this issue? 

# Discussion History
## 2010phenix | 2018-05-30T11:03:15+00:00
add miner to Exclusion in Antivirus... and all be good ;-)

## ganapathy-mani | 2018-06-01T21:49:46+00:00
I disabled all the antiviruses and deactivated Windows Firewall. But it still says "Access Denied". I rand the visual studio as an administrator. 

## xmrig | 2018-06-01T21:55:13+00:00
Right click on xmrig in Solution Explorer and choice `Set as StartUp Project`.
Thank you.

## ganapathy-mani | 2018-06-01T23:51:36+00:00
Great ! it did compile. But when I ran it said 

> The thread 0x66c has exited with code 2 (0x2).
> The thread 0x43c has exited with code 2 (0x2).
> The thread 0x4b0 has exited with code 2 (0x2).
> The thread 0xa50 has exited with code 2 (0x2).
> The thread 0x1da4 has exited with code 2 (0x2).
> The program '[6856] xmrig.exe' has exited with code 2 (0x2).

Is it possible to set up a local mining pool with the generated XMRig solution? 

# Action History
- Created by: mikegscott | 2018-05-29T23:23:10+00:00
- Closed at: 2018-06-17T18:01:07+00:00
