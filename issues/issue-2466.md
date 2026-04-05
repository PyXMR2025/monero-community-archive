---
title: Is it possible to recompile `xmrig` and statically link the dlls into the executable
  that way I don't need admin rights?
source_url: https://github.com/xmrig/xmrig/issues/2466
author: Joe23232
assignees: []
labels: []
created_at: '2021-06-30T13:31:03+00:00'
updated_at: '2025-06-16T19:18:30+00:00'
type: issue
status: closed
closed_at: '2025-06-16T19:18:30+00:00'
---

# Original Description
Is it possible to recompile `xmrig` and statically link the dlls into the executable that way I don't need admin rights to get all the optimization? As I was getting this issue when running without admin rights on Windows?

![image](https://user-images.githubusercontent.com/34926497/123969073-338f9a80-d9fb-11eb-9d9d-fd29e0c6d1e8.png)

Which would lower my optimization quite a bit?

# Discussion History
## Spudz76 | 2021-06-30T18:10:26+00:00
Nope, you don't have access to load the "driver" for ring0 which is required for MSR accesses, as anyone other than Administrator.

You could try installing Open Hardware Monitor which also installs a Ring0 driver in a more permanent way, and xmrig *might* be able to access MSR that way as regular user then.  There is no support for installing the Ring0 as a service-driver like the more complicated installer for OHM does.

## Joe23232 | 2021-07-01T08:15:02+00:00
@Spudz76 What is OHM?

## Spudz76 | 2021-07-01T15:13:57+00:00
Open Hardware Monitor

## Joe23232 | 2021-07-27T12:12:42+00:00
Lol how is this illegal?

## Spudz76 | 2021-07-27T17:01:16+00:00
Most of the time these type of questions are looking to bypass requirements so that it works as a worm (without admin privileges)

Same with "how to run as a service, invisible, stop mining when system is touched by a human", etc

## Joe23232 | 2021-07-28T22:34:15+00:00
@Spudz76 Its for my own computer, so I am not too sure how would that be illegal.

## Spudz76 | 2021-07-29T19:10:36+00:00
You're not, but 99% of people who ask this question are.

## Joe23232 | 2021-07-29T23:24:43+00:00
@Spudz76 Interesting, so have you personally experienced people asking these kinds of questions and later to be found out they were doing something illegal?

## Spudz76 | 2021-07-31T20:42:58+00:00
No, but there are about two reasons to do it that aren't, and 1000000000 reasons that are shady, so it's just suspicious without context of your asking all sorts of other questions that aren't nefarious, but simply curious.

I'm sure vf-whoever posted without knowing your question history like I do.  I also would have responded the same had this been your first question.  To them, it was your first question, the first one they saw.

There is no penalty for being a scumbag we just prefer to not help if that's the end goal (making trojans and worms / hiding miners from the boss / hiding miners from anyone).  And that's the assumed end goal because there isn't much of a reason to bypass requirements if you're the admin of your own computer mining with permission (because then it doesn't need to hide and can have Admin rights no problem, right?)

## Spudz76 | 2021-07-31T20:49:21+00:00
The only other reason to bypass admin (if it was even possible) was because you're overparanoid of running things as Admin.  This project as long as you got the code from github is 10000000% safe to run as admin, assuming you've not configured it badly (open to config writes from any IP worldwide without password token, etc).  And even then it would only be a problem for the xmrig process.

Granted maybe there hasn't been as much buffer-exploit fuzzing as other projects get (openssl, etc) but then also for things like that we just use openssl rather than rewriting the wheel.  Most of the code isn't putting user provided data into buffers thus can't really be overflowed, except the API section, but that doesn't seem to have bad code (buffer ranges are checked, also uses an httpd dependency written and tested elsewhere).  There just aren't many gaps to be concerned about, thus avoiding Admin is literally pointless.  Maybe two reasons was a bit overestimating, haha.

## Joe23232 | 2021-08-01T01:40:50+00:00
@Spudz76  Right I see, I just wanted to start up everytime I start my PC (I know how to do this) but without asking for admin rights before executing, I just want to do it all in the background on my computer, that is all. I hope I clarified some things.

## Spudz76 | 2021-08-01T18:58:10+00:00
I haven't had Windows ask for privileges ever, since I turn off UAC prompting as like step 2 of an installation, and my user account is an Administator anyway.  And then it doesn't ask anymore.

## Joe23232 | 2021-08-01T22:23:32+00:00
Doesn't that make you more vulnerable to other programs that can just run
as admin? I only wanted to turn it off for xmrig.

On Mon, Aug 2, 2021 at 4:58 AM Tony Butler ***@***.***> wrote:

> I haven't had Windows ask for privileges ever, since I turn off UAC
> prompting as like step 2 of an installation, and my user account is an
> Administator anyway. And then it doesn't ask anymore.
>
> —
> You are receiving this because you authored the thread.
> Reply to this email directly, view it on GitHub
> <https://github.com/xmrig/xmrig/issues/2466#issuecomment-890569163>, or
> unsubscribe
> <https://github.com/notifications/unsubscribe-auth/AIKO7IOVJAXBLAAHDPZD6V3T2WKMZANCNFSM47SLCKWA>
> .
>


## Spudz76 | 2021-08-02T19:51:54+00:00
I've never had a problem only gained all the 3 second interruptions I've saved.  Virus protection is rather strong already considering xmrig won't even get the the UAC if it wasn't whitelisted.  UAC is only for when you have run something you aren't sure about, but you shouldn't be doing that anyway as Admin, so UAC is just a fence for those who don't know what Admin means or don't vet their programs or fall for fake programs that claim impossible benefits.  If you clicked yes on the UAC prompt, which you'd probably always do, then why even have it pop up?

I've literally never had one pop when I didn't cause it and also wanted the thing I launched to run, which led me to removing the fence.  I don't even think it catches Services or other things launched outside of the shell (task scheduler, etc).

I also have never run Win10 as I'm stlll on Win7 considering I hate the direction they went (away from good-old-plain-looking WinXP, added too much themery and "quick tips" and "wizard junk" that I don't want on my screen).

## Joe23232 | 2021-08-02T23:39:50+00:00
I will take that into consideration, thanks.

> I also have never run Win10 as I'm stlll on Win7 considering I hate the direction they went (away from good-old-plain-looking WinXP, added too much themery and "quick tips" and "wizard junk" that I don't want on my screen).

Yeah I gotta admit that, plus Windows 10 is just too bloated. It is slow and constantly taking up too much system resources whereas Windows 7 is light, it is much quicker etc. Plus you have classic theme which takes up even less system resources, and they got rid of in Windows 10 which makes no sense. Windows 7 feels like a light linux distro.

Plus you run Windows 7 vs Windows 10 on VirtualBox, Win7 is really buttery smooth, its very quick and things just happen immediately. On Windows 10 its very laggy, slow and constantly wasting so much system resources and it is painful to use.

# Action History
- Created by: Joe23232 | 2021-06-30T13:31:03+00:00
- Closed at: 2025-06-16T19:18:30+00:00
