---
title: ARM Cortex-A72 64-bit can't enable 1GB PAGES
source_url: https://github.com/xmrig/xmrig/issues/2271
author: TylerMMcFarlane
assignees: []
labels:
- arm
created_at: '2021-04-15T21:45:59+00:00'
updated_at: '2022-04-05T01:07:25+00:00'
type: issue
status: closed
closed_at: '2022-04-03T14:46:46+00:00'
---

# Original Description
**Describe the bug**
I can't get 1GB pages enabled.

**To Reproduce**
I have made a custom kernel with Linux for a Raspberry Pi 4 I have pre allocated 4 1GB hugepages in addition to 1168 2MB hugepages. I can attach if required just let me know.

**Expected behavior**
I was expecting the disabled 

**Screeenshots**
<img width="368" alt="Screenshot2" src="https://user-images.githubusercontent.com/82615933/114941107-a052ba00-9e3a-11eb-9f37-2d976fddbeb5.PNG">
<img width="619" alt="Screenshot3" src="https://user-images.githubusercontent.com/82615933/114941110-a183e700-9e3a-11eb-8aca-330c6b46721e.PNG">
<img width="609" alt="Screenshot1" src="https://user-images.githubusercontent.com/82615933/114941111-a183e700-9e3a-11eb-8337-367d2789ef55.PNG">


# Discussion History
## TylerMMcFarlane | 2021-04-15T21:48:33+00:00
Hello, this is my first time using GitHub & Linux. Just let me know if I need to attach more info/ what info. Thanks.

## SChernykh | 2021-04-15T22:44:04+00:00
Either add `--randomx-1gb-pages` to the command line or use config.json instead of command line options.

## Spudz76 | 2021-04-15T23:15:12+00:00
The code for ARM sets the feature flag (`FLAG_PDPE1GB`) only when the miner can open the sysfs file at `/sys/kernel/mm/hugepages/hugepages-1048576kB/nr_hugepages`; with x86_64 there is an actual flag in `/proc/cpuinfo` so this sysfs check is emulating that.

What does `cat /sys/kernel/mm/hugepages/hugepages-1048576kB/nr_hugepages` do?  I see you are running as root so it would be weird if it were permission related... maybe that doesn't exist for some reason (sysfs related kernel options missing in your custom build?)

Also if the above doesn't exist for some reason check for the alternate location with:
`grep . /sys/devices/system/node/node*/hugepages/hugepages-1048576kB/nr_hugepages`

Might as well include output of `cat /proc/cpuinfo` for completeness.

## TylerMMcFarlane | 2021-04-16T08:11:52+00:00
> Either add `--randomx-1gb-pages` to the command line or use config.json instead of command line options.

It's work!!, I added  `--randomx-1gb-pages` to the command line. The hashrate is amazing but it's been fun trying to optimise it. Thanks for the help!!

![image](https://user-images.githubusercontent.com/82615933/114992869-200c7300-9e93-11eb-82f6-6feae5a02b56.png)


## Shai0Hulud | 2021-04-19T12:25:30+00:00
> > Either add `--randomx-1gb-pages` to the command line or use config.json instead of command line options.
> 
> It's work!!, I added `--randomx-1gb-pages` to the command line. The hashrate is amazing but it's been fun trying to optimise it. Thanks for the help!!
> 
> ![image](https://user-images.githubusercontent.com/82615933/114992869-200c7300-9e93-11eb-82f6-6feae5a02b56.png)

I see that the hashrate is still as high/low as before.

What is the size of the L2 cache of your A72?

Scratchpad size per thread is 2048KB, if all threads combined dont fit inside the L2 Cache, hashrate suffers a LOT!

Wikipedia says something about 512 to 4096 L3 cache size, so 2 threads would be maximum? Just try it out!

According to https://xmrig.com/benchmark, an A72 can reach 100H/s for a single thread!

Or try another coin/algorithm ^^

Edit: AES is not active either, as far as I can see...

Editedit: According to your XM Rig, it cant detect any Cache at all?

## TylerMMcFarlane | 2021-04-19T20:11:54+00:00
> > > Either add `--randomx-1gb-pages` to the command line or use config.json instead of command line options.
> > 
> > 
> > It's work!!, I added `--randomx-1gb-pages` to the command line. The hashrate is amazing but it's been fun trying to optimise it. Thanks for the help!!
> > ![image](https://user-images.githubusercontent.com/82615933/114992869-200c7300-9e93-11eb-82f6-6feae5a02b56.png)
> 
> I see that the hashrate is still as high/low as before.
> 
Unfortunately it's 1MiB so I think I don't have enough space for even 1.  
> What is the size of the L2 cache of your A72?
> 
> Scratchpad size per thread is 2048KB, if all threads combined dont fit inside the L2 Cache, hashrate suffers a LOT!
> 
> Wikipedia says something about 512 to 4096 L3 cache size, so 2 threads would be maximum? Just try it out!
> 
> According to https://xmrig.com/benchmark, an A72 can reach 100H/s for a single thread!
> 
> Or try another coin/algorithm ^^
> 
Again from what I've found on the raspberry pi 4, it doesn't have a AES
> Edit: AES is not active either, as far as I can see...
> 
> Editedit: According to your XM Rig, it cant detect any Cache at all?

I think 105H/s is the quickest for the chip I'm using, it's been fun optimizing this far. Any other subjections just should, thanks for the help  



## Shai0Hulud | 2021-04-20T05:53:46+00:00
> it's been fun optimizing this far. 

Yeah, I can relate to that. ^^ 

> Again from what I've found on the raspberry pi 4, it doesn't have a AES

Still I'm confused as this A72 seems to have AES: [https://xmrig.com/benchmark/63bxi6](https://xmrig.com/benchmark/63bxi6), but googling for ARM chips, they seem to be something like construction kits. ^^ Or surprise Kinder Eggs ^^

## Spudz76 | 2022-04-05T01:07:25+00:00
> Still I'm confused as this A72 seems to have AES

Yes some do, but the Raspberry Pi Foundation refuses to pay the AES licensing thus their CPUs never have it.  AES is a separately licensed feature, available for use, but not when the system integrator doesn't pay for it.

Similar to how many low power and cheaper Intels have all the silicon in them for AES but then just have the flag shut off.  L55xx xeons for example, or many i3/i5.

# Action History
- Created by: TylerMMcFarlane | 2021-04-15T21:45:59+00:00
- Closed at: 2022-04-03T14:46:46+00:00
