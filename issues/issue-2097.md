---
title: Laptop i5 msr preset causing blue screen.
source_url: https://github.com/xmrig/xmrig/issues/2097
author: alanhasgari
assignees: []
labels: []
created_at: '2021-02-12T06:47:14+00:00'
updated_at: '2021-04-12T14:15:57+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:15:57+00:00'
---

# Original Description
I have been dealing with this since early v5...

I'm not a big techie, but was tired of getting bluescreens on Windows when I launch xmrig after reboot...

Just recently dove into custom msr values, and noticed if I set wrmsr to 12, I no longer got blue screens after reboot...

My cpu is an i5-2520m. 12 results in no blue screens while other numbers gave less than acceptable hash rates or cause sporadic reboots...

Whatever the intel default value is doesn't seem appropriate for the older gen i5 mobile cpus... Any chance to create a separate preset for mobile chips? or maybe change the preset for the normies and let enthusiasts set their own msr values?

# Discussion History
## SChernykh | 2021-02-12T08:48:25+00:00
MSR mod on Intel uses officially documented register, so any value between 0-15 shouldn't result in a blue screen. I think your notebook is just unstable or overheating. Mining on a notebook is generally not recommended.

## ghost | 2021-02-12T09:07:29+00:00
What bsod says when it is show?

## alanhasgari | 2021-02-12T20:44:41+00:00
It's a memory management error, and laptop is not overheating or
overclocked. It never goes above 50% usage and temps remain well below
thermal limits (never above 58°C)...

It's got 16GB of RAM, and this is the second intel system I've had this
issue with; the other was an i7-4770R NUC with 32GB of RAM...

Both systems had the OS reinstalled, latest drivers, everything I could
possibly do to correct the behavior before messing with MSR... On the i7,
if I ran XMRig within 5 minutes of booting, it would bluescreen. The i5
laptop, I'd have to wait 15+mins before launching XMRig, even then it was
roughly a 50/50 chance of bluescreen...

On Fri, Feb 12, 2021, 4:07 AM ScardracS <notifications@github.com> wrote:

> What bsod says when it is show?
>
> —

## alanhasgari | 2021-02-13T04:54:48+00:00
> MSR mod on Intel uses officially documented register, so any value between 0-15 shouldn't result in a blue screen. I think your notebook is just unstable or overheating. Mining on a notebook is generally not recommended.

My laptop is stable on everything except xmrig with default msr preset... Same with my i7 nuc...

I am just saying that the default value is causing an issue somewhere that results in xmrig triggering a blue screen in these two systems. Manually setting them solves the issue. So, for the best out of box experience, perhaps the preset should be different or a preset should be added for mobile cpus... Recommended or not, I know many that mine Monero on laptops, and some mine kawpow on integrated nvidia gpus...

## xmrig | 2021-02-13T05:03:13+00:00
> Manually setting them solves the issue.

What exactly do you mean by this? Another value for the MSR register is stable or you disable MSR mod.
Thank you.

## SChernykh | 2021-02-13T06:40:19+00:00
Many mine Monero on laptops, but you're the first in over a year to report blue screens with MSR mod. I don't think it's MSR mod, but rather something with your laptops.

## alanhasgari | 2021-02-13T06:58:00+00:00
> > Manually setting them solves the issue.
> 
> What exactly do you mean by this? Another value for the MSR register is stable or you disable MSR mod.
> Thank you.

Manually setting my two systems to anything other than the preset seems to solve the problem to some degree... For instance, the i5 system is completely stable at 12 with decent hashrate, while my i7 was better off at 13... No more blue screens for memory management,...

I can't explain it, as I understand very little about the more intricate details of what goes on... I'm just trying to figure out why this is... The rest of my systems are AMD and have never had issues like these. 

## alanhasgari | 2021-02-13T06:58:53+00:00
> Many mine Monero on laptops, but you're the first in over a year to report blue screens with MSR mod. I don't think it's MSR mod, but rather something with your laptops.

Then what do you believe it could be? I'd be happy to try other methods to resolve this. I ask because no other application causes the bluescreen... Only after a reboot, when I launch xmrig after logging in, do I get a bluescreen for memory management.

## SChernykh | 2021-02-13T07:04:50+00:00
Can you try to boot Linux on them and try mining there?

## alanhasgari | 2021-02-13T10:43:11+00:00
As I said before, I'm not a big techie... I wouldn't really know where
to start with getting a Linux distro booted and fetching xmrig for it... I
use Windows because I sometimes like to use idleminer with xmrig so that
the systems can be used and only mine when idle...

On Sat, Feb 13, 2021, 2:05 AM SChernykh <notifications@github.com> wrote:

> Can you try to boot Linux on them and try mining there?
>
> —
> You are receiving this because you authored the thread.
> Reply to this email directly, view it on GitHub
> <https://github.com/xmrig/xmrig/issues/2097#issuecomment-778574592>, or
> unsubscribe
> <https://github.com/notifications/unsubscribe-auth/ABHZ5P7PGV4CVQC22GAS6UDS6YQCHANCNFSM4XQFM7QQ>
> .
>


## ghost | 2021-02-13T14:29:26+00:00
> As I said before, I'm not a big techie... I wouldn't really know where
> to start with getting a Linux distro booted and fetching xmrig for it... I
> use Windows because I sometimes like to use idleminer with xmrig so that
> the systems can be used and only mine when idle...
> 
> On Sat, Feb 13, 2021, 2:05 AM SChernykh <notifications@github.com> wrote:
> 
> > Can you try to boot Linux on them and try mining there?
> >
> > —
> > You are receiving this because you authored the thread.
> > Reply to this email directly, view it on GitHub
> > <https://github.com/xmrig/xmrig/issues/2097#issuecomment-778574592>, or
> > unsubscribe
> > <https://github.com/notifications/unsubscribe-auth/ABHZ5P7PGV4CVQC22GAS6UDS6YQCHANCNFSM4XQFM7QQ>
> > .
> >
> 

Use linux is really easy. If you don't know where to start it's better for you to try with Ubuntu, Fedora or Manjaro

## Cregrant | 2021-02-17T15:04:58+00:00
I can catch a blue screen with or without admin rights (msr mod enabled).

![17-02-2021 215442](https://user-images.githubusercontent.com/62436046/108221890-d7725b00-716a-11eb-9a45-245233c89831.jpg)


## alanhasgari | 2021-02-17T20:10:11+00:00
That's a different error than I get.

# Action History
- Created by: alanhasgari | 2021-02-12T06:47:14+00:00
- Closed at: 2021-04-12T14:15:57+00:00
