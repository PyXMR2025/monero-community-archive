---
title: Raspberry Pi 4B crashes when running xmrig
source_url: https://github.com/xmrig/xmrig/issues/3104
author: GYKgamer
assignees: []
labels:
- question
created_at: '2022-08-05T18:03:28+00:00'
updated_at: '2022-12-13T14:25:07+00:00'
type: issue
status: closed
closed_at: '2022-12-13T14:25:07+00:00'
---

# Original Description
When running command "xmrig" it would start as normal, but after a few seconds my raspberry pi will crash (see screenshot and video)

Running "xmrig --stress" crashes my raspberry pi
Running xmrig at one core doesn't crash but instead a segfault occurs
Running the app "Geekbench" (a CPU-intensive program) does not crash my raspberry pi
Trying to change the xmrig binary doesn't work either

Here is also where I got my help https://github.com/Botspot/pi-apps/issues/2096

https://user-images.githubusercontent.com/41442793/183134784-0207ac45-01a0-41e6-9aa4-d0cfc684a295.mp4

![image](https://user-images.githubusercontent.com/41442793/183134796-3daad81b-ed6b-4553-a67d-c2e2bcf648ec.png)



# Discussion History
## SChernykh | 2022-08-05T19:13:30+00:00
This is MoneroOcean version in your video, please test with the original xmrig. In any case, it shouldn't cause full system crash unless your Pi is unstable.

## GYKgamer | 2022-08-05T19:54:11+00:00
I only use the MonerOcean pool? I don't know of any MonerOcean xmrig versions. All files come from this github page.

## SChernykh | 2022-08-05T20:01:39+00:00
XMRig/6.18.0-mo1 (version can be seen in the video) is not a file from this github page, it's MoneroOcean fork.

## SChernykh | 2022-08-05T20:04:22+00:00
Oh, I know why. You run your Pi in 32-bit mode, it is not supported by XMRig on ARM. Install 64-bit OS to mine properly.

## Botspot | 2022-08-28T01:55:14+00:00
> Oh, I know why. You run your Pi in 32-bit mode, it is not supported by XMRig on ARM. Install 64-bit OS to mine properly.

@SChernykh, so you [fixed](https://github.com/xmrig/xmrig/issues/2895#issuecomment-1133113854) xmrig to run on armhf systems, but when users encounter problems on it, you say armhf is not supported?

## GYKgamer | 2022-08-28T05:42:17+00:00
Oh hi @Botspot , Thanks for reminding me that this post existed. Now whenever I run "xmrig" (arm64) I get a segmentation Fault
![image](https://user-images.githubusercontent.com/41442793/187059422-8e2654a8-ba63-45a0-96a7-42b15f9b207a.png)


## SChernykh | 2022-08-28T09:28:05+00:00
@Botspot it is not supported because we never test it on 32-bit ARM. That one time I had to install 32-bit OS on my RPi to fix this crash, and then I had to install back my regular 64-bit OS. I spent half of the day doing it (and lost all my RPi software setup in the process). Also, RandomX doesn't have JIT for 32-bit ARM so it will be very very slow (less than 1 h/s) - one more reason to not support 32 bit.

@GYKgamer this is MoneroOcean version, ask in their github. If you manage to get this crash in the official XMRig version, post it in a new issue.

# Action History
- Created by: GYKgamer | 2022-08-05T18:03:28+00:00
- Closed at: 2022-12-13T14:25:07+00:00
