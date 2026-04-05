---
title: AMD EPYC 7R32
source_url: https://github.com/xmrig/xmrig/issues/1956
author: PostGresSQL
assignees: []
labels:
- question
created_at: '2020-11-26T06:58:55+00:00'
updated_at: '2021-04-12T14:34:21+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:34:21+00:00'
---

# Original Description
Hi there.

I am using nicehash and the msr mod wont apply to the XMrig miner.
I've tried the reddit post solution for windows with noting coming from it.
This is the reddit post  , i know this is designed to help those with ryzen chipsets.

https://www.reddit.com/r/MoneroMining/comments/e9tuvd/randomx_boost_guide_for_ryzen_on_windows_9100_hs/

I also tried running it on admin , and installing the C++ 2016 rest.
Without any luck , is there more i can do or should i lay this with nicehash?
this is what i see i use XMrig trough nicehash.
Operating System : Windows server 2016 base.
![Screenshot_14](https://user-images.githubusercontent.com/22871127/100317775-2c179700-2fbd-11eb-976a-e43b2719631c.png)


# Discussion History
## xmrig | 2020-11-26T07:36:26+00:00
MSR is not available for virtual/cloud machines.
Thank you.

## PostGresSQL | 2020-11-26T07:41:02+00:00
> MSR is not available for virtual/cloud machines.
> Thank you.

I am using my own servers i got about 12 of these, its not on cloud.
I am using the IBM Linux one with spring instances.

Since i have full control over these machines , can i do anything to fix the issue?

## xmrig | 2020-11-26T07:59:23+00:00
Ok, in other words, MSR works only on physical not virtualized hardware, as I know 7R32 CPU exclusively created for Amazon AWS and not available for others.

Take a look at this: https://xmrig.com/benchmark?cpu=AMD+EPYC+7R32 both submits have different threads/cache configuration and you 3rd.

## PostGresSQL | 2020-11-26T08:05:08+00:00


> Ok, in other words, MSR works only on physical not virtualized hardware, as I know 7R32 CPU exclusively created for Amazon AWS and not available for others.
> 
> Take a look at this: https://xmrig.com/benchmark?cpu=AMD+EPYC+7R32 both submits have different threads/cache configuration and you 3rd.

What if i told you i whas jeff bezos..and i own these?

## SChernykh | 2020-11-26T10:37:16+00:00
These are AWS instances, they are virtualized. You can only run MSR mod on physical hardware, not in a VM. Either this, or this Windows Server 2016 version doesn't allow WinRing0x64.sys to work.

Edit: in the first post you say Windows Server 2016, then you say IBM Linux. What OS do you use? Is IBM Linux used as hypervisor for Windows? Then it won't work of course.

## Lonnegan | 2020-11-26T13:45:34+00:00
Windows Server 2016 is not the problem, I'm running some Ryzens with Server 2016 and 2019 and the MSR mod works.

You are right, that EPYC 7R32 was intended for Amazon (AWS) exclusivly, as the 7V12 was for Microsoft (Azure), but despite of that they've found the way to retailers somehow. Those guys for example got some, as well:
https://www.planet3dnow.de/cms/57428-amd-epyc-7v12-bei-planet3dnow/

But even if you own these servers, you have to run them "bare metal". Most modern servers I know run virtualized, even if only one instance is running; ESXi, vSphere, Proxmox VE, or whatever. Under these circumstances, MSR mod doesn't work. You have to run your Windows Server 2016 directly on the hardware.

Is it possible, that the MSR fix only works on Ryzens, not on EPYCs?

## SChernykh | 2020-11-26T13:50:44+00:00
It works on all Zen/Zen2/Zen3 CPUs, but only on the real hardware, not in a VM. Also, maybe this IBM Linux doesn't allow access to MSR registers.

## Spudz76 | 2020-12-04T09:35:04+00:00
At the very least, run it on the actual hardware (IBM Linux) not in a VM.
I run xmrig in the Hypervisor environment (non-VM) on Proxmox for example (which is just a Debian mod).

# Action History
- Created by: PostGresSQL | 2020-11-26T06:58:55+00:00
- Closed at: 2021-04-12T14:34:21+00:00
