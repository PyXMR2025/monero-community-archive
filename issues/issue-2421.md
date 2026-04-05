---
title: XMRig "Killed" After Successful Start
source_url: https://github.com/xmrig/xmrig/issues/2421
author: chaoticchord
assignees: []
labels: []
created_at: '2021-06-02T19:54:45+00:00'
updated_at: '2022-02-12T07:12:19+00:00'
type: issue
status: closed
closed_at: '2021-06-10T15:30:09+00:00'
---

# Original Description
Using XMRig with Unmineable on Ubuntu 21.04. XMRig launches just fine, displays the "new job" messaging two or three times, and then drops. Have tried both the json and direct command methods of launching it and nothing seems to work. Any thoughts?

Note: Pretty green when it comes to mining, appreciate the patience.

# Discussion History
## SChernykh | 2021-06-02T20:05:39+00:00
We need a bit more information. What CPU is it? Can you screenshot xmrig output from the beginning until it's killed and post it here?

## Spudz76 | 2021-06-03T13:11:39+00:00
Check dmesg for messages from OOMKiller

When the system runs out of memory it finds the highest memory-using thing and kills it, and says what it did in dmesg.

## chaoticchord | 2021-06-03T20:59:11+00:00
Appreciate the replies. Its an older system I was just playing around with to try out XMRig. Its a Pentium Dual Core and 3GB of RAM. Looks like OOM is nuking the process. So I just have to figure out how to stop it from doing that.

## Spudz76 | 2021-06-04T13:10:08+00:00
RandomX algos require 3GB free after booting.  It would run other algos if you cross-mine.

## chaoticchord | 2021-06-07T12:49:07+00:00
Determined the issue. Ubuntu was automatically killing the process because of OOM. Reconfigured it to stop panicking when it "thinks" its out of memory, and now XMrig is running just fine... and actually outperforming a newer i3 box running a stripped down Win7 install. Thanks for the assist.

## UnixCro | 2021-12-24T13:56:46+00:00
Greetings,

I have the same problem.  I have a number of old smartphones that I no longer use and instead of reselling them I prefer to mean by that, but some smartphones cause me some problems such as the Samsung Galaxy S8.  But where exactly is the problem here?  XMRig starts up without any problems, but after a while it will stop. I turned off all kinds of power saving options. The phone restarted and all other apps deactivated. 

![DC92E0C4-36B7-4786-B2F8-EBB802A59AEE](https://user-images.githubusercontent.com/70098046/147357279-9a7b436d-939b-4af6-b953-b91070821dd3.jpeg)
![D17C4069-247C-4689-B982-93733565B95F](https://user-images.githubusercontent.com/70098046/147357286-a78c2d88-0687-4d69-aa55-f71586d38106.jpeg)

Are there certain XMRig parameters that can end this behavior.  I've already used the `—cpu-priority=1` and `-t 4` parameters, but it doesn't help.

Any ideas?


## Spudz76 | 2021-12-25T04:48:52+00:00
Not enough memory, probably killed by OOMkiller.

## UnixCro | 2021-12-25T05:27:31+00:00
@Spudz76 

Thanks for the hint.  Is there any parameter in XMRig that ensures that this process is no longer killed by the OOM.  I think without root it is not feasible to deactivate the OOM.

What I think is a shame, however, is that the XMRig does not notice that the operating system has little RAM available and is not taking any action.  As for example with my Fire 7. It only has 1 GB of RAM here but XMRig thought about it.

![1BE00472-BDF1-4838-9B0C-1CE43F5B785F](https://user-images.githubusercontent.com/70098046/147378003-ecd0df77-a8ae-419a-9184-ab139cced8c8.jpeg)


>not enough for memory RandomX dataset
failed to allocate RandomX dataset, switching to slow mode.

Well you can say.  With the S8, XMRig was able to distribute the memory but was killed because the kernel found it too much and with the Fire 7 it was not possible at all, so it was switched directly to the slower mode.  But this is exactly where you can build on.  Question 1. How exactly do I now switch to slow mode on my S8?

Mi 10
![3E1A2437-F6BF-48E4-9A81-176BBF0636E1](https://user-images.githubusercontent.com/70098046/147378069-66433181-cffe-4761-b7b4-ea4d1c2d2f5b.jpeg)

But I have to say that XMRig does a really good job on devices that have 8 GB of RAM.  Thanks to you dear developers.  As I mentioned before, no miner has worked too flawlessly when it comes to mining Monero.

And I ask everyone who reads this comment.  If you want to mine.  Best to do without anything that is 4 GB or less.  I haven't tested 6GB yet, but with 8GB it shouldn't be a problem with XMRig!  Don't get a 4GB device !!



## UnixCro | 2021-12-25T11:08:43+00:00
Solved: After a long research, I was able to solve the problem.  XMRig uses `2080 MB + 256 MB = 2336 MB + (2048 KB * Threads)` in RAM.

> 2080 MB per NUMA node for dataset, 1 NUMA node usually equal to 1 CPU socket, the miner show number of nodes on startup.
256 MB for cache on first NUMA node.
256 KB of L2 cache and 2 MB of L3 cache per 1 mining thread.

Since this "fast mode" needs too much, it is killed by the OOM.  XMRig has a parameter `--randomx-mode=light` which forces the slow mode and only occupies `256 MB` in RAM. I am happy to have solved this problem.  

Merry Christmas !

## trgcyln | 2022-02-11T12:03:17+00:00
> Solved: After a long research, I was able to solve the problem. XMRig uses `2080 MB + 256 MB = 2336 MB + (2048 KB * Threads)` in RAM.
> 
> > 2080 MB per NUMA node for dataset, 1 NUMA node usually equal to 1 CPU socket, the miner show number of nodes on startup.
> > 256 MB for cache on first NUMA node.
> > 256 KB of L2 cache and 2 MB of L3 cache per 1 mining thread.
> 
> Since this "fast mode" needs too much, it is killed by the OOM. XMRig has a parameter `--randomx-mode=light` which forces the slow mode and only occupies `256 MB` in RAM. I am happy to have solved this problem.
> 
> Merry Christmas !

![Screenshot_7](https://user-images.githubusercontent.com/15324844/153588229-119bdcf1-f948-49f8-b2fa-ca0323ce2db3.png)

I tried it but it doesn't work  for me.

## chaoticchord | 2022-02-11T12:09:25+00:00
Didn’t realize people were still commenting on this. 

I just ended up disabling OOM Killer by adding “vm.oom-kill = 0” to /etc/sysctl.conf.

also added the line “vm.overcommit_memory = 2”

fixed my issues. 

## UnixCro | 2022-02-11T12:43:40+00:00
> I tried it but it doesn't work for me.

Move the config.json away from the folder and solve the whole thing with parameters.  In my pictures are examples.

BTW: The solution to the OOM Killer only affects Unix operating systems and not Windows

## trgcyln | 2022-02-11T14:37:42+00:00
vm.oom-kill = 0
vm.overcommit_memory = 2

I did both changes and restarted.
removed config.json and added "--randomx-mode=light" parameter. 
still killed.


## chaoticchord | 2022-02-11T14:40:26+00:00
I don’t have access to the PCs I was doing the configs on anymore, unfortunately but I may have the configuration file laying around somewhere. If I find it, I’ll upload it so that you can take a look. Can’t quite remember what else was changed to make it work. 

## trgcyln | 2022-02-11T14:46:08+00:00
thanks.

## Spudz76 | 2022-02-11T22:44:14+00:00
You either need more memory (two sticks good for dual-channel speed gains anyway) or you need to really strip the heck out of Windows to make it waste less but I doubt it will ever get small enough to fit the 2.1GB dataset, maybe with Win7 fully lightened but probably never with Win10.  4GB total is just too small for Windows when you need 2.1GB for an app.

Might barely work in Linux, but similarly fully stripped (console only, no services except xmrig, etc -- lots of work).

## UnixCro | 2022-02-12T07:12:19+00:00
> You either need more memory (two sticks good for dual-channel speed gains anyway) or you need to really strip the heck out of Windows to make it waste less but I doubt it will ever get small enough to fit the 2.1GB dataset, maybe with Win7 fully lightened but probably never with Win10. 4GB total is just too small for Windows when you need 2.1GB for an app.
> 
> Might barely work in Linux, but similarly fully stripped (console only, no services except xmrig, etc -- lots of work).

Hello Tony, nice again that an expert reports.  I don't know much about XMRig in terms of memory allocation and we both know that from the issue I posted on XMRig at the time.  But when I look at the screenshot of the affected person, I see 0.5/3.1 Gb occupied.  So Windows only uses 0.5 Gb as I understand it.  The remaining 2.6 GB would be enough for XMRig's fast mode (2336 MB+ threads *2MB), and the slow mode (256 MB) can only work because it's so little.  Apparently it still gets killed though, I think because XMRig writes something conspicuously into RAM that the OS is suspicious of and kills it.

# Action History
- Created by: chaoticchord | 2021-06-02T19:54:45+00:00
- Closed at: 2021-06-10T15:30:09+00:00
