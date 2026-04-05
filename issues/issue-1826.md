---
title: Low Hashrate performence on a Xeon dual cpu platform
source_url: https://github.com/xmrig/xmrig/issues/1826
author: intelljames
assignees: []
labels:
- randomx
created_at: '2020-09-09T11:36:17+00:00'
updated_at: '2021-04-12T14:49:23+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:49:23+00:00'
---

# Original Description
My minner have dual Xeon Gold 6230R with hex channel 128GB RAM, but the hash rate is about 20K H/s
![image](https://user-images.githubusercontent.com/14022949/92593067-1acec080-f2d3-11ea-8342-f69f4c973627.png)

I totally have L1 3.3MB,  L2 52MB,  L3 71.5MB.

All settings are automatically set by the xmrig, I can get about 15K hashrate on the a AMD 3900X platform, the hashrate of dual 6230R should be much higher than this, but why I got 20KH/s only ?

# Discussion History
## xmrig | 2020-09-09T12:09:06+00:00
Please show the result of `h` to view per thread hashrate and how many memory channels you actually use? a typical single DDR4 channel is limited to about 4000-6000 H/s in other words how you exactly install the 128 GB RAM?

Even if you achieve 500 H/s per thread, it will be only 26 kH/s, Intel is not the best for RandomX mining.
Thank you.

## Lonnegan | 2020-09-09T19:31:07+00:00
Intel desktop CPUs have an inclusive cache management. Means: copies of the L1 and L2 cache are in the L3 cache, as well (different to AMD's exclusive caches). That's why you aren't allowed to add the different cache stages on an Intel plattform. You just can look at the last level cache. So, on a Core i7 system with 8 MB L3 cache, you just can run 4 threads (2 MB scratchpad size each). On an Intel desktop plattform!

The younger HEDT and server CPUs instead have different cache layouts with mesh and victim caches. Means: the L2 cache is not a fast just 256 KB small cache, but a 1024 KB huge but slower buffer. But 1024 KB is to small for RandomX, where each scratchpad has a size of 2048 KB. So the even slower victim L3 cache has to be looked at. It's just 35.75 MB per CPU or 71.5 MB for both CPUs.

A single Ryzen 9 3950X already has 64 MB L3 cache. And it has much higher core frequencies. So the dual Intel system cannot be much faster than the 3950X due to the limited last level cache.

With 1 MB L2 cache per core, you should consider to mine a coin with smaller scratchpad size. Wownero e.g. has 1 MB scratchpad size, which would fit perfectly into the fast L2 caches of your Xeon :)

## intelljames | 2020-09-11T08:27:51+00:00
> Please show the result of `h` to view per thread hashrate and how many memory channels you actually use? a typical single DDR4 channel is limited to about 4000-6000 H/s in other words how you exactly install the 128 GB RAM?
> 
> Even if you achieve 500 H/s per thread, it will be only 26 kH/s, Intel is not the best for RandomX mining.
> Thank you.

@xmrig 
Thanks for the reply, this is a screenshot of my RAM test , is it possible that the thread settings are the problem? I have a total of 71.5 MB of level 3 cache, is it better to use 30 threads? But I have tried 30 threads and the hashrate is 9 kH/s, very confused.
![微信截图_20200910212156](https://user-images.githubusercontent.com/14022949/92892848-b7b46980-f44b-11ea-8f36-53769eb053ad.png)
![微信截图_20200911162245](https://user-images.githubusercontent.com/14022949/92892858-ba16c380-f44b-11ea-8263-6e92202abda8.png)


## SlavisaBakic | 2020-09-11T16:43:19+00:00
I think that your threads configuration is problem.

One CPU have 35.75MiB L3 cache. Since XMRig require 2MiB last level cache per thread that mean that you can have 15 threads per CPU running. You could also have 16th thread per CPU with remaining 1.75MiB L3 cache per CPU.

Line "rx": [3] under "cpu" in config.json should look like (pay attention to HyperThreading logical CPUs and fact that one CPU have 26 cores/52 logical CPUs):
"rx": [0, 2, 4, ..., 30, 52, 54, 56, ..., 82] 
Replace "..." with corresponding array.

If that is dedicated machine for mining, consider installing Ubuntu Server 20.04 without GUI.


EDIT: Numbers in brackets are vCPU "IDs" you can see in Task Manager.

## SChernykh | 2020-09-11T19:50:06+00:00
> One CPU have 35.75MiB L3 cache. Since XMRig require 2MiB last level cache per thread

This is not entirely correct with this CPU. Intel Xeon (Cascade Lake) has non-inclusive victim L3 cache, which means total amount of L2+L3 defines how many threads can be run.

@intelljames 
Have you seen better hashrate on any similar system? 20 kh/s is rather good for Intel Xeon CPUs, they're not very efficient on RandomX.

## intelljames | 2020-09-11T19:52:47+00:00
@SlavisaBakic Thanks for your suggestion, I did what you said and when I got to 82, the hashrate was around 16kH, then I tried 84 86 and the total was increasing in about 17~18, 

> I think that your threads configuration is problem.
> 
> One CPU have 35.75MiB L3 cache. Since XMRig require 2MiB last level cache per thread that mean that you can have 15 threads per CPU running. You could also have 16th thread per CPU with remaining 1.75MiB L3 cache per CPU.
> 
> Line "rx": [3] under "cpu" in config.json should look like (pay attention to HyperThreading logical CPUs and fact that one CPU have 26 cores/52 logical CPUs):
> "rx": [0, 2, 4, ..., 30, 52, 54, 56, ..., 82]
> Replace "..." with corresponding array.
> 
> If that is dedicated machine for mining, consider installing Ubuntu Server 20.04 without GUI.
> 
> EDIT: Numbers in brackets are vCPU "IDs" you can see in Task Manager.



## intelljames | 2020-09-11T20:06:44+00:00
@SChernykh I got a dual E5-2667V2 system, it can get about 8kH/s, There are 52 threads involved in mining (6230R) according to XMRIG's automatic settings, and I think this thread setting is probably fine (see my tweaks for threads), while the dual 2667v2 system only have 20 threads, and given the IPC differences between the two CPUs, I wonder if 20kH/s is a bit low?

## SlavisaBakic | 2020-09-12T09:24:50+00:00
> 
> 
> @SlavisaBakic Thanks for your suggestion, I did what you said and when I got to 82, the hashrate was around 16kH, then I tried 84 86 and the total was increasing in about 17~18,
> 
> > I think that your threads configuration is problem.
> > One CPU have 35.75MiB L3 cache. Since XMRig require 2MiB last level cache per thread that mean that you can have 15 threads per CPU running. You could also have 16th thread per CPU with remaining 1.75MiB L3 cache per CPU.
> > Line "rx": [3] under "cpu" in config.json should look like (pay attention to HyperThreading logical CPUs and fact that one CPU have 26 cores/52 logical CPUs):
> > "rx": [0, 2, 4, ..., 30, 52, 54, 56, ..., 82]
> > Replace "..." with corresponding array.
> > If that is dedicated machine for mining, consider installing Ubuntu Server 20.04 without GUI.
> > EDIT: Numbers in brackets are vCPU "IDs" you can see in Task Manager.

How much RAM sticks you have?

You could also experiment with different settings for:
Dell Reliable Memory Technology (RMT)
and
System Isochronous Mode

https://www.dell.com/support/manuals/ba/en/babsdt1/precision-7920-workstation/precision_7920_om_pub/performance?guid=guid-7e45e537-e5f0-434e-b1d8-dc50cdfa993b&lang=en-us

# Action History
- Created by: intelljames | 2020-09-09T11:36:17+00:00
- Closed at: 2021-04-12T14:49:23+00:00
