---
title: Xmrig appeared to be "killed" and huge pages allocation is 0%
source_url: https://github.com/xmrig/xmrig/issues/2649
author: ghost
assignees: []
labels: []
created_at: '2021-10-26T05:31:58+00:00'
updated_at: '2021-11-09T06:10:58+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
![unknown-37.png](https://user-images.githubusercontent.com/12180913/138814715-2fe40e42-8e58-4ac5-89e5-9378c1b6026d.png)


# Discussion History
## Spudz76 | 2021-10-26T07:32:30+00:00
Surprised it works with gcc-5 still, I would use only gcc-7 or newer if possible.

I would say the config file is broken, what does it contain?  Launch args?  How is xmrig a shell script?

## ghost | 2021-10-26T19:21:41+00:00
I actually run xmrig with the default config @Spudz76 

Does it nolonger work with the detault conf?

## DeeDeeRanged | 2021-11-04T11:40:13+00:00
Have you enabled msr in grub? Maybe thats why msr and hugepages, need to run as root, are not working.

## ghost | 2021-11-06T20:03:24+00:00
Yeah i dont think i have. Is there any way to run it without changing grub? Just curious :)
@DeeDeeRanged 

## DeeDeeRanged | 2021-11-07T01:33:03+00:00
@Footsiefat 
In /etc/default grub add change the follwing:
GRUB_CMDLINE_LINUX_DEFAULT="quiet"
GRUB_CMDLINE_LINUX="msr.allow_writes=on"

run sudo update-grub.

MSR has been default disable in the kernel on linux.
Which distro are you running as gcc-5 is ancient by now.

## ghost | 2021-11-07T01:47:01+00:00
Its a vps so i probably cant acess grub thats why :/ @DeeDeeRanged 

## DeeDeeRanged | 2021-11-07T12:53:12+00:00
@Footsiefat 
Thats probably also the reason you cannot get hugepages. AFAIK msr and hugepages do not work with vps.

## ghost | 2021-11-08T22:06:03+00:00
@DeeDeeRanged  Thanks for the info! Just out of curiousity any there any way to make this work without having hugepages enabled?

## Spudz76 | 2021-11-09T06:10:58+00:00
I would imagine it's killing anything that allocated 3GB of any page size of memory.  Most VPS have limits like that.  If it didn't kill it for using too much memory then it would kill it for CPU hogging shortly after.

# Action History
- Created by: ghost | 2021-10-26T05:31:58+00:00
