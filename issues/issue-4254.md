---
title: Solo mining resulting in crashing Daemon immediately Windows 11 Pro
source_url: https://github.com/monero-project/monero-gui/issues/4254
author: tommyboy0
assignees: []
labels: []
created_at: '2023-12-18T22:21:26+00:00'
updated_at: '2024-12-11T10:17:58+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
After synchronizing my wallet, I went to try & start mining in solo mode resulting in the network losing connection & goes into a loop of trying to reconnect to the network. I believe the node is crashing because I am able to manually start it again. Once I restart the node manually, I change the settings, resulting in the same issue or I get a message stating 'Mining temporarily suspended.'. I have this issue weather I am using half or all of my CPU's threads..  When I try to use the "Background mining" thread, I seem to be having the same issue. Let me know what information I can provide that would be helpful.
Thank you!

# Discussion History
## selsta | 2023-12-19T04:34:23+00:00
What kind of PC hardware do you have? (CPU / RAM / etc.). Also do you have an anti virus installed?

## tommyboy0 | 2023-12-19T05:03:06+00:00
Intel i7-10750H CPU
Nvidia RTX 2060 GPU
64 GB Ram
PC Brand: MSI
Virus software is just the standard Windows Defender. 
I have my computer set to Developer mode

> What kind of PC hardware do you have? (CPU / RAM / etc.). Also do you have an anti virus installed?



## tommyboy0 | 2023-12-19T05:04:51+00:00
> What kind of PC hardware do you have? (CPU / RAM / etc.). Also do you have an anti virus installed?

By the way when I run P2Pool it seems to run as planned but nothing goes into my wallet. I have been running it for a few hours now.. What am I doing wrong, I have no issue just using it this way. 

## RFITSCorp | 2023-12-28T01:02:04+00:00
I'm having this same issue.
z690-pro mb. i9-13900k. 64gb ripjaw. ssd, etc.

Worked perfect solo before. I've been mining p2pool for a bit but decided to go back and it's just not working anymore. If I type "status" fast enough or have it run through the GUI, it appears to be mining for a second or so but that's it.

No errors of any sort that I can see from the GUI nor console. I'm trying to see if I can get one to pop but not yet.

Windows 11 also. Latest. Reinstalled, all cache/etc wiped and retried.

EDIT: All AV killed BTW. monerod just appears to crash. It simply exits with no message after it displays the list of threads mining unless I'm fast enough to get in a 'status' or alike which shows it mining fine, until it quits. I don't think I can add anything more helpful as of now.

## selsta | 2023-12-28T01:09:30+00:00
Can you start monerod.exe from cmd and then enter "start_mining address" and see if it crashes?

## 737simpilot | 2023-12-28T07:59:22+00:00
I'm getting the same thing on my end running Windows 10. Hardware is as follows:

i7 7700

Gigabyte Z270X Gaming K7

16GB RAM

RTX 3060

NVMe HDD

I do keep seeing this in the error log which may or may not be related or part of another issue. 

`WARNING	frontend	src/wallet/api/wallet.cpp:411	Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations`

I also see a lot of this:

`WARNING	wallet.wallet2	src/wallet/wallet2.cpp:2224	Transaction extra has unsupported format: <001143fa710c0046c1ae04f47858eddee9f2c5f10ed93506b745440d2173ebdb>`

That string of 64 characters is always different. 

I'm running monerod.exe and the GUI with Admin rights in compatibility mode.  The wallet is portable and is in the root of C drive. `C:\wallet\monero-gui-v0.18.3.1`

## 737simpilot | 2023-12-28T09:09:44+00:00
I ran monerod.exe (start_mining) in the command line and had errors as well. After constant testing it appears the errors happen more often if you use more than 3 or 4 threads. 

Here are the two errors I caught. 

![img](https://i.imgur.com/y1WISH6.jpeg)

## selsta | 2023-12-29T06:00:24+00:00
@737simpilot can you try to download monerod.exe from this version and confirm that it also crashes? This was from before we did some code changes.

https://github.com/monero-project/monero/releases/tag/v0.18.1.2

## 737simpilot | 2023-12-29T15:38:19+00:00
Doesn't appear to have errors in that version.

## selsta | 2023-12-30T18:58:47+00:00
@737simpilot thank you, can you also test https://github.com/monero-project/monero/releases/tag/v0.18.2.2 ?

## 737simpilot | 2024-01-03T14:51:39+00:00
I'll test this sometime today or tomorrow when I have time. Thanks.

## RFITSCorp | 2024-01-03T14:54:12+00:00
Programmer here, all the time in the world, offered help. I see these pages from arch linux issues to this with problems that take forever to get resolved and it's clear why - lack of communication. I'd offer free help and funds but I didn't get a response to my last question. Peace. Good luck with your ... project.

## nahuhh | 2024-01-03T14:57:00+00:00
> Programmer here, all the time in the world, offered help. I see these pages from arch linux issues to this with problems that take forever to get resolved and it's clear why - lack of communication. I'd offer free help and funds but I didn't get a response to my last question. Peace. Good luck with your ... project.

>I also see a lot of this:
>
>WARNING wallet.wallet2 src/wallet/wallet2.cpp:2224 Transaction extra has unsupported format: <001143fa710c0046c1ae04f47858eddee9f2c5f10ed93506b745440d2173ebdb>
>
>That string of 64 characters is always different.

You can ignore this



## selsta | 2024-01-03T15:06:24+00:00
@RFITSCorp you didn't ask a question, you simply stated that you also have the same issue. Fixing bugs that can't be reproduced on our side is difficult so I'm trying to find out in which version this got introduced.

If you want to help then try the two linked versions in the previous comment and check if they crash or not.

## 737simpilot | 2024-01-07T11:41:08+00:00
No errors in 0.18.2.2

## selsta | 2024-01-09T12:19:58+00:00
@737simpilot can you also try to download monerod.exe from https://github.com/monero-project/monero/releases/tag/v0.18.3.1 instead of the one bundled with the GUI?

## 737simpilot | 2024-01-09T12:44:10+00:00
I've been testing monerod.exe independently. Can I actually replace the monerod.exe in my wallet now with an old one? Or is that not a good idea?

In either case, firing off monerod.exe from my current wallet with the current code exhibits Windows errors shown in the pic above, where's the ones you're having me test do not. I verify this by firing off the monerod.exe program many times to rule out anything. I've also have been running them directly from the C drive.

## selsta | 2024-01-09T12:45:12+00:00
Did you try the monerod.exe one from the v0.18.3.1 link above? Does it work?

## 737simpilot | 2024-01-09T12:45:50+00:00
Doing that now. It's updating the block chain as it's 2 days old now.

## 737simpilot | 2024-01-09T13:21:52+00:00
Got an error in v0.18.3.1.

## 737simpilot | 2024-01-09T13:27:33+00:00
Tried the 32 bit version and get this. Is that normal?

![img](https://i.postimg.cc/GhhP5ZMF/cmd.jpg)

## selsta | 2024-01-09T13:52:23+00:00
If you have 64bit Windows make sure to use the 64bit version.

Last test, can you try the latest development version by scrolling down on the following link and downloading the "Win64" file?

https://github.com/monero-project/monero/actions/runs/7454870884

## 737simpilot | 2024-01-18T11:02:28+00:00
Got an error with that version. 

## selsta | 2024-01-18T14:51:22+00:00
@737simpilot Please also test this version: https://github.com/selsta/monero/actions/runs/7569980391

This now has reverted the only RandomX related change between v0.18.2.2 and v0.18.3.1. If this doesn't crash we at least know which change causes the issue, if it does crash we have to look somewhere else.

## 737simpilot | 2024-02-23T07:56:36+00:00
Hi. Sorry, I'm just now seeing your message. Tested that version and no errors. 

## SChernykh | 2024-02-23T17:26:55+00:00
@737simpilot How exactly do you start mining? Do you add `--start-mining WALLET` to monerod command line, or do you run `start_mining WALLET` in monerod console when it's fully synced?

## 737simpilot | 2024-02-24T09:34:44+00:00
start_mining WALLET ID in the console. 

## SChernykh | 2024-02-24T09:54:13+00:00
This commit should hopefully fix it: https://github.com/SChernykh/monero/commit/e95f2b0b5476f055d23918f6f8fffc4fa0df17a8
I'll give a link for you to test as soon as binaries are built by CI.

## selsta | 2024-02-24T12:34:21+00:00
@737simpilot Can you test the "Win64" file from this version? It includes the fix from @SChernykh.

https://github.com/SChernykh/monero/actions/runs/8029758573

## 737simpilot | 2024-02-26T14:28:39+00:00
Got an error.





![img](https://i.postimg.cc/N0rvGyZh/1.jpg)



![img](https://i.postimg.cc/5NchpNHp/2.jpg)

## TerraGuy | 2024-08-02T13:21:43+00:00
I also have a problem where I experience disconnection if I mine with more than 3 threads on my Intel i5 12500H/Win11/0.18.3.3

If I start with 4 threads it sometimes works, sometimes disconnects within a minute. With more threads it always disconnects quickly. With 3 threads, it is still working now after 24 hours. But only with a disappointing 1.4kH/s max. I have 12 cores, so I should be able to get some more! 

Random guess: might it be that the problem lies in the fact the processor has 2 types of cores, 4 performance cores and 8 efficiency cores, instead of 1 type of cores?

## selsta | 2024-08-14T21:41:14+00:00
@TerraGuy did you try out mining with for example xmrig?

## Russnyw | 2024-08-17T14:25:28+00:00
Hi, I am also getting the mining temporarily suspended and then it disconnects. I re connect to the daemon and try again. if I sue p2pool it works. but in solo I works on 3 threads,  but more than that and i get the above behavior. I have a ryzen 5950x which has 64mb l3 cache so I should be able to used all cores?
Edit -I did specify a diffenet ssd drive for the blockchain (thought it was gonna be a massive file), not sure if that makes a difference? is it better to have ti on same drive? is a standard sdd better or would nvme help?
Thanks!

## jtsmith0101 | 2024-10-08T09:10:04+00:00
I have these issues too.  Win 11 Pro, i7-12700H, Norton 360.  

Upon crashes of the daemon, I intermittently receive messages from Norton blocking unauthorized access (Process Data).

Logs only show me when my miner processes start, then crashes without additional messaging.

I'm successful solo mining on single thread.  Mostly successful using 2.  I start getting inconsistent behavior with 3 threads.  More than that and the daemon is most suredly going to crash.

## 737simpilot | 2024-10-08T15:05:48+00:00
That's an entirely different issue in of its self since you are using (privacy invading) anti-virus software which can and will cause issues for all kinds of things. 

I don't run any anti-virus (gasp) and I have issues with crashing. It may be my OS configuration or something in the code. As I was testing each version there was one or two versions that did not crash. And by not crashing I tested various thread affinities too.

## jtsmith0101 | 2024-10-08T20:04:57+00:00
The Norton logs are info only, not action.  I'm thinking it may be a
Windows configuration issue.

On Wed, 9 Oct 2024, 02:06 Aaron, ***@***.***> wrote:

> That's an entirely different issue in of its self since you are using
> anti-virus software which can and will cause issues for all kinds of things.
>
> I don't run any anti-virus (gasp) and I have issues with crashing. It may
> be my OS configuration or something in the code. As I was testing each
> version there was one or two versions that did not crash.
>
> —
> Reply to this email directly, view it on GitHub
> <https://github.com/monero-project/monero-gui/issues/4254#issuecomment-2400111800>,
> or unsubscribe
> <https://github.com/notifications/unsubscribe-auth/ACPVG7FZ72UM5GPJPVUA2ODZ2PYGFAVCNFSM6AAAAABA2G5ICOVHI2DSMVQWIX3LMV43OSLTON2WKQ3PNVWWK3TUHMZDIMBQGEYTCOBQGA>
> .
> You are receiving this because you are subscribed to this thread.Message
> ID: ***@***.***>
>


## jtsmith0101 | 2024-10-09T00:20:34+00:00
Is someone actively working on this issue?

## selsta | 2024-10-11T13:01:25+00:00
It appears this is a compiler bug and we can't easily upgrade the compiler we use for release builds at the moment.

## Average-GH-Enjoyer | 2024-12-11T10:16:55+00:00
I have the connecting/disconnected loop when I start solo mining with the GUI. Fresh Windows install, new wallet, allowed both Firewall popups, no anti-virus running. It doesn't matter how many threads I set, the issue is the same. Sometimes I get a few seconds of mining, and sometimes it instantly goes into the reconnection loop.

GUI version: 0.18.3.4-unknown (Qt 5.15.14)
Embedded Monero version: 0.18.3.4-unknown
Wallet restore height: 3280805
Wallet mode: Advanced mode (Local node)
Graphics mode: OpenGL

# Action History
- Created by: tommyboy0 | 2023-12-18T22:21:26+00:00
