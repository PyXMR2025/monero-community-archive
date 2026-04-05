---
title: STOPS MINING
source_url: https://github.com/xmrig/xmrig/issues/541
author: tremmorkeep
assignees: []
labels:
- bug
created_at: '2018-04-11T13:21:47+00:00'
updated_at: '2018-11-05T15:09:35+00:00'
type: issue
status: closed
closed_at: '2018-11-05T15:09:35+00:00'
---

# Original Description
Every now and then I get a status of 'Dev donation complete' and my miner(s) go idle...I dont have money wrapped up into hardware to have the not mine....please advise


# Discussion History
## L1LjSHX | 2018-04-11T14:06:43+00:00
version miner? 2.6.0 beta 1 have "bug" with donation

## tremmorkeep | 2018-04-11T15:14:19+00:00
2.5.2 ...and it happens on all my hardware, CPU and GPU.


## xmrig | 2018-04-11T18:28:54+00:00
Please show log or make screenshot, it's pretty strange. When donation active, connection to user pool is still active and switching happen immediately, for mining part it's like usual job.
Thank you.

## tremmorkeep | 2018-04-11T18:30:14+00:00
K, next time it happens I’ll grab the screen.

Mining on 5 different boxes.  Main box is a threadripper 1950x with 2x Nvidia GeForce 1070ti’s

 

From: xmrig <notifications@github.com> 
Sent: Wednesday, April 11, 2018 12:29 PM
To: xmrig/xmrig <xmrig@noreply.github.com>
Cc: tremmorkeep <mmontgomery@powerconnect.com>; Author <author@noreply.github.com>
Subject: Re: [xmrig/xmrig] STOPS MINING (#541)

 

Please show log or make screenshot, it's pretty strange. When donation active, connection to user pool is still active and switching happen immediately, for mining part it's like usual job.
Thank you.

—
You are receiving this because you authored the thread.
Reply to this email directly, view it on GitHub <https://github.com/xmrig/xmrig/issues/541#issuecomment-380551115> , or mute the thread <https://github.com/notifications/unsubscribe-auth/AeTqYs3Zkh_lVdGwbwlfY0Ch2R3iZjiGks5tnkttgaJpZM4TQBLG> .  <https://github.com/notifications/beacon/AeTqYkgMNLkhGccBOsjpToPH9xHABpEeks5tnkttgaJpZM4TQBLG.gif> 



## tremmorkeep | 2018-04-21T13:32:44+00:00
![image](https://user-images.githubusercontent.com/31779426/39084645-16319f86-4536-11e8-8f4d-f6dffadfe263.png)
so...I know its a low hashrate...congratulations it hit your hashes..and didnt mine for me all night...thanks...thats awesome


## xmrig | 2018-04-21T13:57:56+00:00
Looks like https://github.com/xmrig/xmrig/issues/478 not complete fixed in 2.5.2, connection to your pool died before donation start, hashare **n/a**, try use v2.5.0.
Thank you.

## tremmorkeep | 2018-04-26T13:41:11+00:00
Yes using 2.5.0 now. On vacation. Switching to dual miner upon return

On Sat, Apr 21, 2018, 6:58 AM xmrig <notifications@github.com> wrote:

> Looks like #478 <https://github.com/xmrig/xmrig/issues/478> not complete
> fixed in 2.5.2, connection to your pool died before donation start, hashare
> *n/a*, try use v2.5.0.
> Thank you.
>
> —
> You are receiving this because you authored the thread.
> Reply to this email directly, view it on GitHub
> <https://github.com/xmrig/xmrig/issues/541#issuecomment-383297464>, or mute
> the thread
> <https://github.com/notifications/unsubscribe-auth/AeTqYgox9qHMKGJDcMWigDiRUUb0zupOks5tqzrpgaJpZM4TQBLG>
> .
>


# Action History
- Created by: tremmorkeep | 2018-04-11T13:21:47+00:00
- Closed at: 2018-11-05T15:09:35+00:00
