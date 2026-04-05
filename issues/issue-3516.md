---
title: 'Abysmal (< 1 H/s) Hashrate On Linux (5.15) Mint Suddenly '
source_url: https://github.com/xmrig/xmrig/issues/3516
author: a-p-jo
assignees: []
labels: []
created_at: '2024-07-26T22:15:08+00:00'
updated_at: '2025-06-16T19:38:54+00:00'
type: issue
status: closed
closed_at: '2025-06-16T19:38:54+00:00'
---

# Original Description
**Describe the bug**
I am suddenly getting hashrates between 0.63 to 0.74 H/s where I would get 640 to 730 H/s earlier (1000x slower). Initially, it would go away after a few reboots but now it won't.

**To Reproduce**
Use Linux Mint 21.3 (currently with kernel 5.15.0-117-generic). My CPU is a i3-6006U, unsure if that matters.

**Required data**
 - XMRig version
    - Latest: https://github.com/xmrig/xmrig/releases/download/v6.21.3/xmrig-6.21.3-linux-static-x64.tar.gz


# Discussion History
## geekwilliams | 2024-07-27T01:38:38+00:00
Are you running out of memory on that system?  Are you also using MSR mods? 

## a-p-jo | 2024-07-27T02:40:59+00:00
> Are you running out of memory on that system? Are you also using MSR mods?

Yes, MSR mods are running.

I don't think I'm running out of memory. It's the same amount of RAM as before and no new software (apart from kernel update maybe). When I first set the machine up it would run out of ram if the Desktop Environment was running simultaneously. The way this happened was that xmrig would get killed by the OOM killer. Since that's not the case anymore (I'm not running a DE and there is no OOM killing of xmrig) I don't think memory is a concern. 

## a-p-jo | 2024-07-27T03:42:40+00:00
It seems to be that something changed in 5.15.0-116-generic

I booted with the kernel before that (5.15.0-113-generic) and everything works just fine. 

## geekwilliams | 2024-07-27T08:29:40+00:00
I would agree with that sentiment.  There are [quite a few posts](https://forums.linuxmint.com/viewtopic.php?t=424497&start=20) on a few different forums about the move from 5.15.0-113 to 5.15.0-116 breaking VirtualBox.  Its likely they made some breaking change that effects all applications running close to hardware.  

## a-p-jo | 2024-07-28T11:15:47+00:00
@geekwilliams anything that can be done apart from just sitting on an older kernel? It would be nice to not have a perpetually online device miss out on security updates.

## geekwilliams | 2024-07-28T20:12:28+00:00
Good thinking.  Have you tried something newer than 5.15.0-116? 

## a-p-jo | 2024-07-28T23:45:37+00:00
@geekwilliams The Mint devs recently released upgrade instructions for 22, which uses 6.8.0-39 as of now. This issue is still present with that kernel. Or rather, I should say it spuriously goes away now and then. Ordinarily it's present, but once every (insert random number) reboots, it goes away. 

## a-p-jo | 2024-07-29T18:28:30+00:00
Linux Mint Forum Discussion: https://forums.linuxmint.com/viewtopic.php?t=425563

Bug filed in Ubuntu tracker: https://bugs.launchpad.net/ubuntu/+source/xmrig/+bug/2074520

# Action History
- Created by: a-p-jo | 2024-07-26T22:15:08+00:00
- Closed at: 2025-06-16T19:38:54+00:00
