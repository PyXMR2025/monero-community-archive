---
title: this stupid 8700k goes idle?
source_url: https://github.com/xmrig/xmrig/issues/1538
author: PredatorOCX
assignees: []
labels:
- stability
created_at: '2020-02-06T01:57:15+00:00'
updated_at: '2020-08-31T05:47:42+00:00'
type: issue
status: closed
closed_at: '2020-08-31T05:47:42+00:00'
---

# Original Description
so i have an Intel CPU 8700K which used to has as high as 4500 h/s, but all of a sudden, it will go to a "stand by mode" if i leave the PC

what i want to mean is, if i'm doing whatever stuff on my PC the miner works ok, like 4000 h/s avergae, but if i leave the PC on but i'm far from my keyboard the miner goes down on hashrate all of a sudden, like if it's going "idle".

i checked the windows power plan and verified that seems to not be the problem, but i cannot figure out what's going on here.

i have another rig working 24h doing 18.5 kh/s right now, a threaripper 2990WX which i have my issues with before, but i let that one alone and works great now, i have the same operating sistem (windows 10) and same settings besides the threads and the 8700k was doing great untill a few weeks since it started to behave like this

anyone has had the same issue before? any tip will be welcome

thanks in advance



# Discussion History
## PredatorOCX | 2020-02-06T02:00:56+00:00
it toggles and dip all the way from 4000 h/s to 400 h/s or even 200 h/s and when i "wake" it up, i mean, it may have been all night with a 300 h/s average and when i sit down in front of this idiot and open the firefox or something it goes all the way up to 4000 h/s again

## SChernykh | 2020-02-06T09:51:45+00:00
Try to set `"priority":2` in cpu section in config.json.

## FrankS71 | 2020-02-07T13:32:44+00:00
Same problem with i7-2600K and i7-3770 on version 5.5.3.0. It trottle down to around 350-500H/s after some time when you lock Windows. When you log into Windows again it speed up to normal H/s.

## GjBrutello | 2020-02-07T21:04:16+00:00
try to launch with the batch file:
```
@echo off
cd /d "%~dp0" 
start "" xmrig.exe 
PING -n 1 -w 1000 127.0.0.1 > nul 
wmic process where name="xmrig.exe" call setpriority 32 
goto :eof

## cryptonius | 2020-02-11T02:58:16+00:00
The priority option is broken. It eventually slows down mining for every CPU.

## Spudz76 | 2020-03-23T06:37:40+00:00
Win10 patch 19xx changed cpu scheduler, try `-1` for all threads because core binding is broken (at least for AMD based stuff, maybe also some effect on Intel).

Sounds very much the same as in #1506 of course assuming you're using RandomX

## xmrig | 2020-08-31T05:47:42+00:00
https://xmrig.com/docs/miner/randomx-stability-troubleshooting-guide

# Action History
- Created by: PredatorOCX | 2020-02-06T01:57:15+00:00
- Closed at: 2020-08-31T05:47:42+00:00
