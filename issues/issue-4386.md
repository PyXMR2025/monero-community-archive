---
title: Creating+Installing GUI advanced Wallet from Trezor Safe-3 on new MacBook(w
  M4 chip)
source_url: https://github.com/monero-project/monero-gui/issues/4386
author: Kurt555
assignees: []
labels: []
created_at: '2024-12-17T17:53:42+00:00'
updated_at: '2025-02-19T18:07:52+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Installing a GUI wallet for the 1st time, on a brand new dedicated crypto computer.  (Despite knowing nothing about computers, a video on youtube convinced me to use "Advanced mode" because she said it had LESS problems..)  I went to getmonero.org and after selecting "advanced", I proceeded to click whatever buttons the GUI wallet recommended.. (without customizing anything)                                         I created the wallet from a Trezor safe-3, and it was synchronizing beautifully for about a day (90% of the bar filled up with red -indicating that it was synchronizing..) but this last 10% of the bar will not fill up (it has been MORE than another 24 hours [in addition to the original 24 hours]  I do have fast internet and its wired direct into computer.  Here is the confusing part.  (Previously the "Daemon Blocks Remaining" number was DECREASING (going down from 833909 to 827651 etc etc) then it got down around 16,000 and NOW THE DAEMON BLOCKS REMAINING are going *UP*...  from 16,818 to 16,830 to 16,853, 16, 857, left it running overnight again, the next morning 17,151, now 17,340..

(My only *GUESS* is that maybe at one point it said it got disconnected ether because my WIFI quit for a minute or maybe it happened when I let the screen go to sleep once about 24 hours into it, but then the red bar re-appeared and it went back to telling me that it was "waiting for it to finish synching",  but at some point after that,(it may have been many hours later), I noticed the numbers started going in the wrong direction.  -not sure why.  but I could use some help.  AND if anyone answers, please consider that I REALLY do not know anything about computers.  So the more detailed your explanation or instructions.., the more likely it will be that I will understand it. (Like if you say "click" don't assume you know that I will mean that is supposed to mean "double-click"..)  Don't assume I know ANYTHING about how to store something or access something or open anything... ('m not even sure I know how to use "GitHub" properly, or what GitHub even is, but here I am..)  Just pretend that I am borderline retarded and hopefully I'll be able to follow along :)   

 THANK YOU *VERY* MUCH if U can help.

# Discussion History
## selsta | 2024-12-17T17:56:13+00:00
Can you go to Settings -> Log and enter "status" into the textbox and share the output?

## Kurt555 | 2024-12-17T18:32:54+00:00
OK..  top part says "log level" "0" then the bottom part I will have to copy and past a bunch of stuff and put it in my email to transfer it from my crypto computer to this one.. hold on...

## Kurt555 | 2024-12-17T18:34:33+00:00
when I scrolled the daemon log up to show me the top part: it says in RED... "ERROR couldn't connect to Daemon" and then a bunch of numbers and dots..


## selsta | 2024-12-17T18:36:03+00:00
I need the output of the status command

## Kurt555 | 2024-12-17T18:37:32+00:00
Where would I find the output of the status command?  it does not say anything like that in the daemon log.  Dang someones at door I will have to take a break and come back to this in about an hour maybe... sorry to cut out now.. long story..



## selsta | 2024-12-17T18:38:43+00:00
Did you enter "status" into the textbox and then press enter?

## Kurt555 | 2024-12-17T18:39:59+00:00
  I'll be back as soon as possible but I have to deal with something for a few hours maybe..  thanks so much.

## Kurt555 | 2024-12-17T23:49:03+00:00
I found the textbox underneath the daemon log and typed in "status."  Underneath the word "status" this is what it said...
[12/17/24 18:13] 2024-12-17 22:13:00.737 I Monero 'Fluorine Fermi' (v0.18.3.4-release)
Height: 3287710/3305214 (99.5%) on mainnet, not mining, net hash 3.24 GH/s, v16, 13(out)+141(in) connections, uptime 1d 7h 25m 48s

## selsta | 2024-12-17T23:50:25+00:00
So far everything looks correct. Can you keep your computer open and plugged in and do the same in an hour (or later) and share the output of status again?

## Kurt555 | 2024-12-17T23:52:16+00:00
Sure I can do that but there is something that looks strange to me which is that it says uptime 1d 7h... but I've had my computer on for about 3 days...  the 1 day 7 hours sounds like the time period when it WAS making progress with the synchronization, and since then...  no progress..     (THANKS VERY MUCH FOR THE GREAT HELP btw!!!)


## Kurt555 | 2024-12-18T01:19:32+00:00
(part 2). ok here is the new status at least an hour later..
>>> status
[12/17/24 21:17] 2024-12-18 01:17:41.767 I Monero 'Fluorine Fermi' (v0.18.3.4-release)
Height: 3287710/3305300 (99.5%) on mainnet, not mining, net hash 3.24 GH/s, v16, 12(out)+143(in) connections, uptime 1d 10h 30m 30s

## selsta | 2024-12-18T01:21:29+00:00
It's stuck for some reason. Do you have enough storage remaining?

## Kurt555 | 2024-12-18T01:33:12+00:00
It is a brand new computer with nothing else on it.  It says 877 GB available of 994 GB

## selsta | 2024-12-18T01:34:33+00:00
Can you try to restart your computer and see if it gets higher than 3287710?

## Kurt555 | 2024-12-18T13:44:07+00:00
I tried to restart the computer and it told me I had to close Monero GUI before I could restart it, but for some reason just asking the computer to re-start caused my curser to start spinning out whenever I hover it over Monero GUI.  (which it wasn't doing previously)  Now I'm going to have to force quit Monero GUI cuz the curser won't stop spinning out (curser turns into spinning rainbow thing when I try to close it)

## selsta | 2025-02-19T18:07:50+00:00
Did you manage to figure out the issue?

# Action History
- Created by: Kurt555 | 2024-12-17T17:53:42+00:00
