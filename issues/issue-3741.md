---
title: BACKDOOR | HACKER | MINER
source_url: https://github.com/xmrig/xmrig/issues/3741
author: RyukoHQ
assignees: []
labels:
- av
created_at: '2025-12-07T10:42:59+00:00'
updated_at: '2026-01-19T20:19:34+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
found that crap on my server and i cant find solution to unninstall that wonderfull software. Everytime i kill/delete, it gets back. 

Miner hackers now opensouce github thing? 

# Discussion History
## SChernykh | 2025-12-07T14:42:57+00:00
This is a legitimate miner software. How people use it (maliciously or not), is on them. If hackers used curl to download xmrig, would you call curl a backdoor as well? Fix your server and stop complaining.

## SChernykh | 2025-12-07T14:59:03+00:00
> Everytime i kill/delete, it gets back.

XMRig doesn't have this functionality. This is something else in your server. I'd suggest a complete reinstall.

## user0-07161 | 2025-12-07T17:27:13+00:00
what the hell do you want us to do? we are not here to help you protect your server.

## RyukoHQ | 2025-12-07T18:46:27+00:00
> what the hell do you want us to do? we are not here to help you protect your server.

Maybe any advise on how to get rid of it? Uninstall guide or something? Or you are clear only to type crap? 

## SChernykh | 2025-12-07T19:02:21+00:00
> Or you are clear only to type crap?

Crap is what you did in the first post here. You were told already - your server is vulnerable to something, it got hacked. At this point, a clean reinstall of a fresh OS with all updates is needed. And you need to check what credentials leaked from that server (maybe some other servers need attention too).

## user0-07161 | 2025-12-07T19:02:28+00:00
@RyukoHQ theres no installer, and therefore no uninstall guide! if someone installed xmrig on your device you are on your own

## geekwilliams | 2025-12-07T19:09:52+00:00
> Maybe any advise on how to get rid of it? Uninstall guide or something? Or you are clear only to type crap? 

Most cryptojackers use their own software and tools to maliciously get a miner onto your system.

Xmrig does not have an installer on its own.  

Without knowing more about your system and what **_YOU_** did to get cryptojacked, none of us can help you.  

Also, a change in your attitude would be nice.  Xmrig is free and open source.  It's not anyone here's fault you don't know how to secure a server.  

## whizzbbig | 2025-12-07T23:16:47+00:00
> > what the hell do you want us to do? we are not here to help you protect your server.
> 
> Maybe any advise on how to get rid of it? Uninstall guide or something? Or you are clear only to type crap?

Properly clean your server from these type of `sex.sh`, `kal.tar.gz`, `system-update-service` also from your project base as well

if you're a next user install this package `fix-react2shell-next` to install the patched version

remove your project's .next, lock file, node_modules and re-install and re-build your app

this will fix the issue of respawning and your server will be fully-cured from the cryptominer malware

follow this blog for more info: https://nextjs.org/blog/CVE-2025-66478

## PPPDUD | 2025-12-08T22:16:46+00:00
I would advise you to back up your data and nuke it out of orbit. There's a thousand places where a malicious cryptominer could hide and it's not a good idea to play whack-a-mole with this stuff.

>It's not anyone here's fault you don't know how to secure a server.

You don't know that. They might have made an honest mistake, and being hostile to people with real problems will not get anyone very far. For all we know, they could have been affected by a supply-chain attack or a poorly-timed package update.

> > > what the hell do you want us to do? we are not here to help you protect your server.
> > 
> > 
> > Maybe any advise on how to get rid of it? Uninstall guide or something? Or you are clear only to type crap?
> 
> Properly clean your server from these type of `sex.sh`, `kal.tar.gz`, `system-update-service` also from your project base as well
> 
> if you're a next user install this package `fix-react2shell-next` to install the patched version
> 
> remove your project's .next, lock file, node_modules and re-install and re-build your app
> 
> this will fix the issue of respawning and your server will be fully-cured from the cryptominer malware
> 
> follow this blog for more info: https://nextjs.org/blog/CVE-2025-66478

How do you know that they were developing software? They might have been self-hosting something.

## toverux | 2025-12-09T01:04:30+00:00
Happened to me right now and this was made possible by the recent CVE 10.0 in Next.js: https://nextjs.org/blog/CVE-2025-66478
This allows remote code execution. Given the timing of your post, chances are you're being injected xmrig the same way.
Check whether you have a Next.js app running on your server. If it's your app, upgrade the framework. If it's not, check for updates for the app.
If the app was containerized, a simple update should get rid of it, if not, yeah, "nuke it out of orbit" like it was said above.

> ah crypto didn't made us all rich nor it did change anything into the financial power structures, but it did cause a lot of damage and consumed a lot of power. use you skills for something that doesn't have a net negative impact on humanity.

## whizzbbig | 2025-12-09T07:38:36+00:00
> I would advise you to back up your data and nuke it out of orbit. There's a thousand places where a malicious cryptominer could hide and it's not a good idea to play whack-a-mole with this stuff.
> 
> > It's not anyone here's fault you don't know how to secure a server.
> 
> You don't know that. They might have made an honest mistake, and being hostile to people with real problems will not get anyone very far. For all we know, they could have been affected by a supply-chain attack or a poorly-timed package update.
> 
> > > > what the hell do you want us to do? we are not here to help you protect your server.
> > > 
> > > 
> > > Maybe any advise on how to get rid of it? Uninstall guide or something? Or you are clear only to type crap?
> > 
> > 
> > Properly clean your server from these type of `sex.sh`, `kal.tar.gz`, `system-update-service` also from your project base as well
> > if you're a next user install this package `fix-react2shell-next` to install the patched version
> > remove your project's .next, lock file, node_modules and re-install and re-build your app
> > this will fix the issue of respawning and your server will be fully-cured from the cryptominer malware
> > follow this blog for more info: https://nextjs.org/blog/CVE-2025-66478
> 
> How do you know that they were developing software? They might have been self-hosting something.

I've found these files and disguised docker consuming more than 95% of my CPU they have the system named backdoor files in the root which trigger the shell script on every reboot and every hour

It was re-spawning, as there was a file at `usr/local/bin` path named as system

I've completely removed the malicous malware from the server and cured my client's server, the structure is too complicated that most of the time it is a no go to nuke the whole server out and restart from scratch

## PPPDUD | 2025-12-10T14:14:10+00:00
> > I would advise you to back up your data and nuke it out of orbit. There's a thousand places where a malicious cryptominer could hide and it's not a good idea to play whack-a-mole with this stuff.
> > > It's not anyone here's fault you don't know how to secure a server.
> > 
> > 
> > You don't know that. They might have made an honest mistake, and being hostile to people with real problems will not get anyone very far. For all we know, they could have been affected by a supply-chain attack or a poorly-timed package update.
> > > > > what the hell do you want us to do? we are not here to help you protect your server.
> > > > 
> > > > 
> > > > Maybe any advise on how to get rid of it? Uninstall guide or something? Or you are clear only to type crap?
> > > 
> > > 
> > > Properly clean your server from these type of `sex.sh`, `kal.tar.gz`, `system-update-service` also from your project base as well
> > > if you're a next user install this package `fix-react2shell-next` to install the patched version
> > > remove your project's .next, lock file, node_modules and re-install and re-build your app
> > > this will fix the issue of respawning and your server will be fully-cured from the cryptominer malware
> > > follow this blog for more info: https://nextjs.org/blog/CVE-2025-66478
> > 
> > 
> > How do you know that they were developing software? They might have been self-hosting something.
> 
> I've found these files and disguised docker consuming more than 95% of my CPU they have the system named backdoor files in the root which trigger the shell script on every reboot and every hour
> 
> It was re-spawning, as there was a file at `usr/local/bin` path named as system
> 
> I've completely removed the malicous malware from the server and cured my client's server, the structure is too complicated that most of the time it is a no go to nuke the whole server out and restart from scratch

Do you remember the name of the Docker container? It might be useful for fixing issues like this in the future.

## dong4j | 2025-12-12T13:12:45+00:00
Today I happened to deal with a case where a server was maliciously used for crypto mining due to a Next.js vulnerability. Fortunately, my server is macOS — XMRig was only downloaded and never actually ran.

This isn’t XMRig’s fault. The problem lies with Next.js and the people who abuse open-source projects like this. Still, I want to punish the person behind this malicious mining attempt. Below is some information about them — is it possible to get their wallet banned?

```
--url pool.supportxmr.com:8080 --user 89Zr4vPaS8yTYRQE54tK1QGKRpsYZ6eJJYynfpfBf1zmLHECaskMPwd3wuTnQ4SYQ7QLkwVN8ur2QTQi9wkKMaCr2iXKa7j --pass sx --donate-level 0
```

This person is absolutely disgusting — they even refused to donate any of their earnings back to the project.

## PPPDUD | 2025-12-12T14:02:00+00:00
> Today I happened to deal with a case where a server was maliciously used for crypto mining due to a Next.js vulnerability. Fortunately, my server is macOS — XMRig was only downloaded and never actually ran.
> 
> This isn’t XMRig’s fault. The problem lies with Next.js and the people who abuse open-source projects like this. Still, I want to punish the person behind this malicious mining attempt. Below is some information about them — is it possible to get their wallet banned?
> 
> ```
> --url pool.supportxmr.com:8080 --user 89Zr4vPaS8yTYRQE54tK1QGKRpsYZ6eJJYynfpfBf1zmLHECaskMPwd3wuTnQ4SYQ7QLkwVN8ur2QTQi9wkKMaCr2iXKa7j --pass sx --donate-level 0
> ```
> 
> This person is absolutely disgusting — they even refused to donate any of their earnings back to the project.

First of all, I don't think that banning them is a good idea. They seem to have already modified XMRig to disable donations; I wouldn't put it beyond them to just ignore your updates and refuse to compile them. If SupportXMR wanted to give them a hard time, they would just use another address.

As for the donations, wouldn't you prefer that XMRig _doesn't_ take advantage of you to earn money? @SChernykh is certain to have profited massively by the use of their cryptominer, and I doubt that it's _harming them_ to continue maintaining it for the minority of people who don't donate.

## ghost | 2026-01-13T05:37:01+00:00
See also https://github.com/xmrig/xmrig/issues/3754

## UnixCro | 2026-01-13T07:39:55+00:00
> This is a legitimate miner software. How people use it (maliciously or not), is on them. If hackers used curl to download xmrig, would you call curl a backdoor as well? Fix your server and stop complaining.

😂😂😂😂😂



## UnixCro | 2026-01-13T07:49:21+00:00
You can misuse anything in this world that wasn't intended for a specific purpose, like a kitchen knife, for example…

## UnixCro | 2026-01-13T18:45:15+00:00
I don't understand at all what xmrig has to do with this? Their server is insecure; it can open all sorts of pornographic content or delete everything. Is xmrig also to blame here?

## PPPDUD | 2026-01-13T19:23:34+00:00
> I don't understand at all what xmrig has to do with this? Their server is insecure; it can open all sorts of pornographic content or delete everything. Is xmrig also to blame here?

I think that the idea is that XMRig was used to cryptomine on their machine, which irked them, so they came here to ask for help.

## UnixCro | 2026-01-13T19:56:04+00:00
> > I don't understand at all what xmrig has to do with this? Their server is insecure; it can open all sorts of pornographic content or delete everything. Is xmrig also to blame here?
> 
> I think that the idea is that XMRig was used to cryptomine on their machine, which irked them, so they came here to ask for help.

Is he simply asking for help, or is he insulting us and blaming xmrig because his server is insecure due to xmrig?



## PPPDUD | 2026-01-13T20:25:54+00:00
> > > I don't understand at all what xmrig has to do with this? Their server is insecure; it can open all sorts of pornographic content or delete everything. Is xmrig also to blame here?
> > 
> > 
> > I think that the idea is that XMRig was used to cryptomine on their machine, which irked them, so they came here to ask for help.
> 
> Is he simply asking for help, or is he insulting us and blaming xmrig because his server is insecure due to xmrig?

They might not be coming with the best attitude, but it's probably just because they got hacked. Imagine if your device had an unauthorized cryptominer on it; would you freak out? I certainly would.

## UnixCro | 2026-01-13T20:32:23+00:00
And why are we now being blamed for the insecurity of his server and even insulted?

If I get beaten up, are the doctors to blame?

## PPPDUD | 2026-01-13T21:24:53+00:00
> And why are we now being blamed for the insecurity of his server and even insulted?
> 
> If I get beaten up, are the doctors to blame?

No, but it is reasonable for a doctor to expect a patient who is stressed and perhaps is not targeting their actions towards the correct people, so long as the patient doesn't inflict damage upon the doctor.

## UnixCro | 2026-01-13T22:36:32+00:00
> > And why are we now being blamed for the insecurity of his server and even insulted?
> > If I get beaten up, are the doctors to blame?
> 
> No, but it is reasonable for a doctor to expect a patient who is stressed and perhaps is not targeting their actions towards the correct people, so long as the patient doesn't inflict damage upon the doctor.

You're absolutely right, doctors try to calm their patients. But xmrig isn't a hospital … And the developers of xmrig are not doctors …

## ghost | 2026-01-14T05:48:56+00:00
https://github.com/xmrig/xmrig/issues/3754#issue-3807188719

@geekwilliams WTF why did you thumb down my report? I'm just citing a fact that this piece of software is being used by malware.

> Is xmrig also to blame here?

Yes because you can fix this by code;

1. On first launch, display X Window (just like qBittorrent software, which display legal notice dialog on first use)
2. The user must press Agree to continue using it

Apparently your software can be launched without consent. This is a problem.

Another problem is you guys already know the bad actor's XMR login ID & password, so why not ban him already?


## user0-07161 | 2026-01-14T06:25:47+00:00
@un1ntend3d you "solution" has several issues:
a. it can be bypassed by removing the dialog from the code, and
b. doesn't allow people to run the miner on devices which don't run an x server software

"banning" the user is impossible as well, as they can just patch xmrig to remove the ban

## ghost | 2026-01-14T06:49:25+00:00
Just wanted to share some quotes from professional;

### "This is cryptomining malware"

and

### "Yes, it is malware."

you can read full report at https://malwaresourcecode.com/home/my-projects/write-ups/r-piratedgames-drama.-is-it-malware-yes.-is-it-cool-malware-no

## geekwilliams | 2026-01-14T06:52:54+00:00
> https://github.com/xmrig/xmrig/issues/3754#issue-3807188719
> 
> @geekwilliams WTF why did you thumb down my report? I'm just citing a fact that this piece of software is being used by malware.
> 

Your assertion that it is xmrig's maintainer's fault it's being used in malware is false.  

> > Is xmrig also to blame here?
> 
> Yes because you can fix this by code;
> 
> 1. On first launch, display X Window (just like qBittorrent software, which display legal notice dialog on first use)
> 2. The user must press Agree to continue using it
> 

Great.  Submit a pull request.  

> Apparently your software can be launched without consent. This is a problem.
>

xmrig does not run by itself magically.  It must be invoked.  If a user downloads and runs malware that just so happens to use xmrig to mine, then the user still invoked the parent process that started xmrig. That action, by definition, is consent.  

If a server is (unfortunately) infected with malware that contains xmrig via an exploit in another application, like the Next.js vulnerability mentioned, that malware was still not developed by, and is not the responsibility of, the maintainers here.  


I'm not sure how many other ways we can say this to get you and the rest of the dissenters in this thread to understand.  Do not come to this repository creating issues for malware. Malware is outside the scope of the developer's concerns here.  


> Another problem is you guys already know the bad actor's XMR login ID & password, so why not ban him already?
> 

You clearly know nothing about xmrig, or mining in general.  This repository is not the place to discuss banning users. xmrig does not work that way. If you wish, you can reach out to pools that you've determined malware is mining on, but good luck getting them to do anything about it, since they are independent of contributors here. None of that makes your machine more secure against malware, and you're better off spending your angst implementing better security measures to prevent infection in the first place.  

I strongly suggest you read xmrig documentation to better understand the developer's goals with the software, and their broader mission before you post anything else unhelpfull on this thread.  

## xmrig | 2026-01-14T07:18:34+00:00
The miner is open source, so anyone, with or without skills, can make many changes, including ripping off any "consent". The only "solution" is make the miner closed sourced, which is not going to happen in any possible case.

If we extend the malware logic to the absolute, then if XMRig is malware, Next.js is malware (a backdoor), and whatever "next" next is malware, including the underlying OS. If we do not stop here, bytes/bits is malware, we definitely should stop using "thinking machines".
Thank you.

## PPPDUD | 2026-01-14T14:16:55+00:00
> [@un1ntend3d](https://github.com/un1ntend3d) you "solution" has several issues: a. be bypassed by removing the dialog from the code, and b. doesn't allow people to run the miner on devices which don't run an x server software
> 
> "banning" the user is impossible as well, as they can just patch xmrig to remove the ban

You want to restrict user freedoms and destroy Monero's security? Sure, go ahead, write your own fork that wraps everything in disclaimers and gives X11 users an unfair advantage. But the stock XMRig is _free software_, meaning that it's the user's responsibility to create safeguards.

## PPPDUD | 2026-01-14T14:19:38+00:00
> Just wanted to share some quotes from professional;
> 
> ### "This is cryptomining malware"
> and
> 
> ### "Yes, it is malware."
> you can read full report at https://malwaresourcecode.com/home/my-projects/write-ups/r-piratedgames-drama.-is-it-malware-yes.-is-it-cool-malware-no

That brief report is regarding a piece of malware that relies on XMRig, not XMRig itself. If I compiled a piece of malware that used glibc, would you call glibc malware too?

## PPPDUD | 2026-01-14T14:20:44+00:00
> > > And why are we now being blamed for the insecurity of his server and even insulted?
> > > If I get beaten up, are the doctors to blame?
> > 
> > 
> > No, but it is reasonable for a doctor to expect a patient who is stressed and perhaps is not targeting their actions towards the correct people, so long as the patient doesn't inflict damage upon the doctor.
> 
> You're absolutely right, doctors try to calm their patients. But xmrig isn't a hospital … And the developers of xmrig are not doctors …

Then why are you applying that analogy if it starts to break down in this situation?

## allisonmeow | 2026-01-18T03:34:11+00:00
lol laugh at this idiot

## PPPDUD | 2026-01-18T19:42:02+00:00
> lol laugh at this idiot

What if that were you? You certainly wouldn't want other GitHub users to call _you_ an idiot, would you?

## allisonmeow | 2026-01-18T22:48:49+00:00
> > lol laugh at this idiot
> 
> What if that were you? You certainly wouldn't want other GitHub users to call _you_ an idiot, would you?

well i guess not

aaaaaanyway just some uncommon advice here: most malware is not super sophisticated (this guy only has 10 kh/s theyre definitely a newbie) contrary to most advice you don't need to throw your computer away, you should probably search for systemd units, cron jobs or rc.d/rc.local services. obviously start with `ps aux` and checking the name of the binary that's starting the miner and then use `grep` in said files, as well as anything that runs `curl` or `wget`.

source: i do this stuff all the time (specifically with miners and other nasty malware)

## Eliot6001 | 2026-01-19T20:16:42+00:00
> aaaaaanyway just some uncommon advice here: most malware is not super sophisticated (this guy only has 10 kh/s theyre definitely a newbie) contrary to most advice you don't need to throw your computer away, you should probably search for systemd units, cron jobs or rc.d/rc.local services. obviously start with `ps aux` and checking the name of the binary that's starting the miner and then use `grep` in said files, as well as anything that runs `curl` or `wget`.
> 
> source: i do this stuff all the time (specifically with miners and other nasty malware)

(At first, i overestimated it in my head assumed a self-replication process at the very least. but after reading, it seemed like a lazy code.)


I assume OP is expecting a "uninstaller" or a script to remove it and he's avoiding tinkering so, yeah it's a pain;
but solid advice. 

so improving on your answer here is a small list to follow:

- systemd service / timer
- cron (/etc/cron.*, root crontab)
- user-level persistence (~/.bashrc, ~/.profile)
- LD_PRELOAD tricks
- dropping a copy somewhere dumb like /usr/local/bin and re-fetching with curl
- abusing legit-looking names (kworker, dbus-daemon, CHECK TOP)

If somehow its more advanced, check `dpkg -V` for hashes (assuming its ubuntu) and reinstall whatever is not of resemblance.

# Action History
- Created by: RyukoHQ | 2025-12-07T10:42:59+00:00
