---
title: System Unresponsiveness
source_url: https://github.com/monero-project/monero-gui/issues/1573
author: WalkingGlitch
assignees: []
labels: []
created_at: '2018-09-28T07:55:09+00:00'
updated_at: '2019-07-04T07:38:29+00:00'
type: issue
status: closed
closed_at: '2019-07-04T07:38:29+00:00'
---

# Original Description
On a multicore Windows 10 1709 64 bit system, running the monero-gui with the monero-daemon causes the system to constantly (every several seconds) cause the system to become completely unresponsive for up to 30 seconds. System is completely unresponsive this includes; hardware (USB and PS/2) polling, GPU polling, and networking. I've had the GPU drivers restart a few times presumably because it timed out. LAN polling also fails while the system is unresponsive.

This happens anytime both the GUI and Daemon are running. If the blockchain is fully synced, the unresponsiveness occurs every time a block is found on the network. This happens regardless of how the daemon is started, or whether it was running before or after the GUI was opened.

To me this seems like the application is obtaining a global kernel lock at maximum priority, and not relinquishing it, even to the kernel, until it's done. Then for some reason the Windows kernel is refusing to preempt it.

# Discussion History
## WalkingGlitch | 2018-09-28T10:29:00+00:00
Also Happens inside of a 64 bit Linux virtual machine, however, the host is insulated as expected. I would recommend this as a workaround for anyone with the capability.

## rbrunner7 | 2018-09-28T10:46:00+00:00
> On a multicore Windows ...

What do you mean with this? Does the machine have several CPU chips in distinct sockets?

## WalkingGlitch | 2018-09-28T10:48:43+00:00
> > On a multicore Windows ...
> 
> What do you mean with this? Does the machine have several CPU chips in distinct sockets?

>**multicore** Windows 10 1709 64 bit **system**


## rbrunner7 | 2018-09-28T10:55:59+00:00
> multicore Windows 10 1709 64 bit system

Sorry, not sure what you mean with this answer.

I was just looking for something that might be special in your case because I find it interesting that we don't have similar reports all over the place. I would say *single*-core systems are definitely a thing of the past, show me a PC running Windows 10 that hasn't at least a 2-core or 4-core CPU.

That's why I was wondering whether you might have exceptionally powerful hardware, let's say with 4 XEON CPU chips, giving something like 64 cores in total or so, and whether Boost thread and lock handling might have a problem exactly with such machines.

Anyway, how many cores did you configure for that Linux VM?

## WalkingGlitch | 2018-09-28T11:37:17+00:00
> > multicore Windows 10 1709 64 bit system
> 
> Sorry, not sure what you mean with this answer.
> 
> I was just looking for something that might be special in your case because I find it interesting that we don't have similar reports all over the place. I would say _single_-core systems are definitely a thing of the past, show me a PC running Windows 10 that hasn't at least a 2-core or 4-core CPU.
> 
> That's why I was wondering whether you might have exceptionally powerful hardware, let's say with 4 XEON CPU chips, giving something like 64 cores in total or so, and whether Boost thread and lock handling might have a problem exactly with such machines.
> 
> Anyway, how many cores did you configure for that Linux VM?

I see your point of view. Just wanted to be specific that it wasn't a CPU contention issue. I'm running a Ryzen 1700, 8 cores, 16 threads.

As for the VM, I gave it 1536MB of RAM and 2 cores on 1 CPU. Syncing in the VM is definitely a lot slower than native hardware, but I'm not surprised. I have mine setup to share the bitmonero folder on the physical drive so I didn't have to copy/redownload the blockchain; as a consequence I noticed fuse uses a lot of CPU time on the guest.

## dEBRUYNE-1 | 2019-07-03T17:38:28+00:00
Can you check whether this is still an issue with GUI v0.14.1.0?



## WalkingGlitch | 2019-07-04T07:38:29+00:00
> Can you check whether this is still an issue with GUI v0.14.1.0?

It is no longer an issue.

# Action History
- Created by: WalkingGlitch | 2018-09-28T07:55:09+00:00
- Closed at: 2019-07-04T07:38:29+00:00
