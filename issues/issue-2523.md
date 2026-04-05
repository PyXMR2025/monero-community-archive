---
title: Motherboard info is unavailable
source_url: https://github.com/xmrig/xmrig/issues/2523
author: BMitrovic17
assignees: []
labels: []
created_at: '2021-08-08T16:52:29+00:00'
updated_at: '2021-08-24T22:59:56+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
**Describe the bug**
Upon starting xmrig.exe we have the header identifying info regarding the settings and hardware. For some reason my motherboard is not detected?

**To Reproduce**
start the xmrig and wait :D

**Expected behavior**
Show the info regarding mobo

**Required data**
 - OS: latest Windows 10 using XMRig/6.13.1 MSVC/2019

![107](https://user-images.githubusercontent.com/25082525/128639364-e505f8c6-3c4a-4d70-bd0e-c3681a7f9dcf.png)



Motherboard in question is [Asus ROG STRIX Z590-E GAMING WIFI](https://rog.asus.com/ca-en/motherboards/rog-strix/rog-strix-z590-e-gaming-wifi-model/)

![108](https://user-images.githubusercontent.com/25082525/128639406-6139e621-2b61-4b37-89c5-3ede68c58454.png)


# Discussion History
## DeeDeeRanged | 2021-08-20T09:43:50+00:00
Probably the same info when you run msinfo in windows.

## Deep0310 | 2021-08-20T09:47:00+00:00
Please don't send message again you know

Pada tanggal Jum, 20 Agt 2021 16.44, DeeDeeRanged ***@***.***>
menulis:

> Probably the same info when you run msinfo in windows.
>
> —
> You are receiving this because you are subscribed to this thread.
> Reply to this email directly, view it on GitHub
> <https://github.com/xmrig/xmrig/issues/2523#issuecomment-902572133>, or
> unsubscribe
> <https://github.com/notifications/unsubscribe-auth/AU22PXWGUYCQYWVKL32TSYDT5YPW3ANCNFSM5BYU6K6A>
> .
> Triage notifications on the go with GitHub Mobile for iOS
> <https://apps.apple.com/app/apple-store/id1477376905?ct=notification-email&mt=8&pt=524675>
> or Android
> <https://play.google.com/store/apps/details?id=com.github.android&utm_campaign=notification-email>
> .
>


## vBm | 2021-08-23T03:17:20+00:00
> Probably the same info when you run msinfo in windows.

I can confirm that. I have exact same cpu and mobo.

![110](https://user-images.githubusercontent.com/80596/130385337-e24213d5-bb74-4846-8be7-6e17e52e2e6f.png)


So maybe read BaseBoard info instead of System ?

## Spudz76 | 2021-08-24T01:08:25+00:00
It's doing it because you are in `VM` mode.

Exact logic [is here](https://github.com/xmrig/xmrig/blob/master/src/Summary.cpp#L165) and it uses System if you're a VM and Board for when you aren't.

So it will show the proper board name if you manage to get `VM` flag to turn off.

## vBm | 2021-08-24T01:28:12+00:00
@Spudz76 In my case that doesn't make sense since I'm not running XMrig from VM. However "Hardware virtualization" is enabled.

I see that VM checker was added in https://github.com/xmrig/xmrig/commit/41a9bddd5937a9035eb874752a85e433ee90420f.

Am I missing something?

## Spudz76 | 2021-08-24T22:59:56+00:00
I do not know exactly what flips your hardware into VM mode, but installing things like VirtualPC or whatever has been known to do so (it doesn't leave the hypervisor alone it makes another VM bubble for it also, dumbly).  Other virtualization like QEMU in Linux don't do that, the hypervisor is not in VM mode at all while it runs actual VMs in VM mode (like "normal").

So it's not just that virtualization is enabled but which hypervisor you've installed, I think.  You might be able to disable the services for that hypervisor when you aren't using it to avoid having it flip your main OS into VM mode.

# Action History
- Created by: BMitrovic17 | 2021-08-08T16:52:29+00:00
