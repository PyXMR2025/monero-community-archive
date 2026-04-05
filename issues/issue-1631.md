---
title: Software leads to frequent bluescreen
source_url: https://github.com/xmrig/xmrig/issues/1631
author: CharlesWithC
assignees: []
labels: []
created_at: '2020-04-03T15:16:55+00:00'
updated_at: '2020-04-10T13:03:09+00:00'
type: issue
status: closed
closed_at: '2020-04-10T13:03:09+00:00'
---

# Original Description
My computer often blue screen with an error code: ATTEMPTED_EXECUTE_NOEXECUTE_MEMORY when I runned xmrig for some time (sometimes a few minutes and sometimes many hours.)

I starts xmrig as a System task with Task Scheduler at system startup. I've already used xmrig for two months and this issue started occuring frequently these days, but I didn't replace the program file. My computer never blue screens when xmrig is stopped. By the way, my network adapter often stops working these days and it seems because of xmrig too.

xmrig version: 5.5.3
os version: windows 10 18363.720
I mine randomx with 4/4 threads with xmrig. I don't mine gpu coins.

# Discussion History
## Lonnegan | 2020-04-05T11:05:47+00:00
Looks like your hardware has a problem. Try memtest and/or Prime95 for a few hours to test if your PC is stable or if there's a problem.

## CharlesWithC | 2020-04-06T13:49:24+00:00
My computer stucked at 11xxx mb when testing memtest. The mouse can't move and I can't control anything. Is that normal?

## Lonnegan | 2020-04-06T14:06:59+00:00
Obviously that's NOT normal! ;-) Perhaps a defective RAM module. If there are more than one RAM modules in your PC, turn it off, take one module out and try again. If it still freezes, put it in again and take the other one out. If you are lucky, just one module is defective and you can move on without it meanwhile till you have a replacement module.

## CharlesWithC | 2020-04-06T14:12:07+00:00
Ok. I will test it some time later. I have two memory modules and the second one was installed a year ago. I hope there is only something wrong with the old one

## CharlesWithC | 2020-04-06T14:15:07+00:00
My first test was with xmrig on and there is only 3xxx mb free memory. (I have 2x8000 mb memory in total) And everything was good.(But a bit slow) So I think there is something wrong with only one memory module

## CharlesWithC | 2020-04-07T10:50:34+00:00
I tested both of my memory chip and both of them made memtest stucked. I waited for some time this time and after 5 minutes the software told me unable to allocate memory because other programs or keneral has used the memory.
I runned the hardware diagnose at start up and there is nothing wrong too.
I guess there is something wrong with my **** windows system. I'm going to re-install the system some time in the future and test it.

## CharlesWithC | 2020-04-07T10:51:20+00:00
I guess the network adapter (auto shutdown) issue is also caused by the OS. 

## CharlesWithC | 2020-04-07T10:59:28+00:00
But I still think the issues are related to xmrig in a way. When I don't run xmrig, nothing is wrong.

## CharlesWithC | 2020-04-07T11:25:41+00:00
Maybe my version is too low. I'm going to update to 5.10.0

## Lonnegan | 2020-04-07T13:34:14+00:00
How can Windows be the cause for your stability problems? Memtest boots from CD or USB stick, completely without Windows. Or which Memtest have you used?

## CharlesWithC | 2020-04-07T13:58:31+00:00
I used two memtests, one is a windows software and the other is Lenovo Diagnose (press f10 at startup to enter). The software stucked and the Diagnose passed the test (so nothing is wrong with my memory chips). I found Windows is really strange because it can't boot when I changed the order of my memory chips (but both of them are plugged in correctly)🤔
I think windows causes my stability problem because my system doesn't work well even before I started using xmrig and I often faces some issues. And there are so many system tasks (I can run Linux very fast on my computer but I'm not going to use it because some software doesn't support Linux). My computer dies every year for some joking issues. (Last time my computer suddenly can't open any software or files (not because of virus) and I have to flash drive C and reinstall Windows)

## CharlesWithC | 2020-04-07T13:59:22+00:00
I updated the xmrig and there are no issues till now. Let's see if my computer will bluescreen again in the future 

## CharlesWithC | 2020-04-10T13:03:09+00:00
My computer bluescreens with xmrig off. Hardware issue confirmed.
But I guess xmrig killed my hardware.

# Action History
- Created by: CharlesWithC | 2020-04-03T15:16:55+00:00
- Closed at: 2020-04-10T13:03:09+00:00
