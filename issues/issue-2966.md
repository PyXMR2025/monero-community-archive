---
title: Nicehash XMRig always causing Windows 10 bluescreen every few minutes of mining
source_url: https://github.com/xmrig/xmrig/issues/2966
author: calvinvalerian
assignees: []
labels: []
created_at: '2022-03-13T06:41:39+00:00'
updated_at: '2022-03-20T14:30:48+00:00'
type: issue
status: closed
closed_at: '2022-03-20T14:30:48+00:00'
---

# Original Description
Even I have tried reinstall my Windows 10 x64 and install the drivers from orginal CD came from the motherboard.

# Discussion History
## ghost | 2022-03-13T12:41:40+00:00
Get a clean install of Windows 10, fully update it, and try using the drivers provided on the manufacturer's website instead

## Lonnegan | 2022-03-15T22:03:55+00:00
And do some stability tests. Run something like Prime95 for a few hours and check if your system is stable at all.

## calvinvalerian | 2022-03-17T05:17:43+00:00
@Lonnegan just ran Prime95 for 25 minutes and I got bluescreen Stop code: MEMORY MANAGEMENT

## calvinvalerian | 2022-03-17T05:45:52+00:00
@uwu-as-a-service done what you told me to do and still I get bluescreen stop code: KERNEL SECURITY CHECK FAILURE

## calvinvalerian | 2022-03-17T05:49:07+00:00
With CPU Disabled I never get bluescreen for the entire 30 days
![Screenshot (91)](https://user-images.githubusercontent.com/18316781/158745243-1a8866c3-a070-4cdc-ba7a-255baabf83c2.png)
 

## Lonnegan | 2022-03-17T06:20:00+00:00
Ok, when you get blue screens running CPU stability tests like Prime95, your PC is NOT stable! Getting MEMORY MANAGEMENT errors may indicate, you have a defective RAM module or too much overclocked RAM or too much overclocked CPU or the CPU is getting too hot.

Check if your system (CPU clock, DRAM clock) is running as specified and check the CPU temperature with tools like HWMonitor running Prime95. 

If everything is ok and the bluescreens still occur, take one of the DRAM modules out of your system and check again. If still BSOD, put it in again and take the other one out.

You have to find out where the weak point of your system is.

## calvinvalerian | 2022-03-20T14:30:47+00:00
Wow you are right about the overclock RAM.. I have RAM OC software installed that came with the motherboard CD driver https://www.asrock.com/MB/Intel/H310CM-DVS/index.asp#Download

the name is ASRock A-Tuning utility ver:3.0.220

I have uninstalled it and I have ran NiceHash xmrig for a day without any bluescreen

# Action History
- Created by: calvinvalerian | 2022-03-13T06:41:39+00:00
- Closed at: 2022-03-20T14:30:48+00:00
