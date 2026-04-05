---
title: Is it possible to compile it for Android ARM processors using Windows?
source_url: https://github.com/xmrig/xmrig/issues/2633
author: Joe23232
assignees: []
labels: []
created_at: '2021-10-17T04:26:32+00:00'
updated_at: '2021-11-02T22:51:37+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Hi, is it possible to compile it for Android ARM processors using Windows? If so, how would I do this?

# Discussion History
## LinuxHeki | 2021-10-19T17:30:05+00:00
No, you need to compile it on Android ARM processor.

## Spudz76 | 2021-10-19T20:37:12+00:00
Might be possible, but very very difficult.  And you'd have to manually and correctly preset/force all the features that cmake and the compiler would normally detect while running on-device.

I tried it with Android SDK but gave up.

## Guitarhero98 | 2021-11-02T12:52:13+00:00
how are you guys .. does anyone have any suggestions/solutions for me .. i have a problem when mining xmrig on android it always crashes/out of the termux apk .. even though i have 3GB of ram capacity on my cellphone, but can't run the xmrig ??

## LinuxHeki | 2021-11-02T12:58:33+00:00
I have same issue. For 10s it works normaly, then freezes for 5s and than it crashes.

## Spudz76 | 2021-11-02T22:51:37+00:00
RandomX requires 2.1GB minimum itself, even 4GB is tight for xmrig+OS to have room.

Other algos probably work.

Unless it's assuming the task has hung or gone into an endless loop because of the crazy 101% load.  Similar to Windows TDP with GPUs (doesn't respond, kills it, even though it wasn't responding due to doing work).

# Action History
- Created by: Joe23232 | 2021-10-17T04:26:32+00:00
