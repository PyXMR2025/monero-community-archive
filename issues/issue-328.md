---
title: Pause/resume/hashrate problem
source_url: https://github.com/xmrig/xmrig/issues/328
author: Sinner181
assignees: []
labels: []
created_at: '2018-01-09T02:05:30+00:00'
updated_at: '2019-08-02T12:46:44+00:00'
type: issue
status: closed
closed_at: '2019-08-02T12:46:44+00:00'
---

# Original Description
Hi, 
when a external command was submitted to your application, I receive an unlimted loop.

with sendmessage or postmessage only work correcly RESUME function ("r" char).

PAUSE and HASHRATE generate an unlimits row like:
[2018-01-09 03:02:09] paused, press r to resume 
[2018-01-09 03:02:09] paused, press r to resume 
[2018-01-09 03:02:09] paused, press r to resume 
[2018-01-09 03:02:09] paused, press r to resume 
[2018-01-09 03:02:09] paused, press r to resume 
[2018-01-09 03:02:09] paused, press r to resume 
[2018-01-09 03:02:10] paused, press r to resume 
[2018-01-09 03:02:10] paused, press r to resume 
[2018-01-09 03:02:10] paused, press r to resume 
[2018-01-09 03:02:10] paused, press r to resume 

I've try with normal cmd.exe and sendmessage/postmessage send correctly only one char, your application goes in a infinite loop and crash after some minutes.

Can you fix? repeat, ONLY Resume work correctly if sendmessage/postmessage send an "r" char.
Thanks.

  

# Discussion History
## xmrig | 2018-01-09T05:44:59+00:00
Can you provide minimum working code how you use sendmessage/postmessage to able me reproduce the issue.
Thank you.

## Sinner181 | 2018-01-09T12:55:14+00:00
A simple PostMessage function:

PostMessage(hwnd, WM_CHAR, $50 ,0 );   (where $50 is P char)

See screenshot, thanks.

![loop](https://user-images.githubusercontent.com/35245293/34721810-8ad338b4-f544-11e7-884b-79d90f183f4f.jpg)


## Sinner181 | 2018-01-09T12:57:06+00:00
If I send 

PostMessage(hwnd, WM_CHAR, $52 ,0 ); (where $52 is R char)

it work correctly and no loop appears.

## Sinner181 | 2018-01-10T13:15:10+00:00
No news?

## xmrig | 2018-01-10T15:59:08+00:00
Probably you send `P` char very often in loop or something. Anyway I added guard, now it should be not a issue. Please check.

## Sinner181 | 2018-01-10T16:38:50+00:00
No, I'm sure to send only one char P without any loop. (I'm programmer since 20 years ;)

Please see below:
![resume work](https://user-images.githubusercontent.com/35245293/34783674-71becd8c-f62c-11e7-9c8e-35e0783c524b.jpg)

I press P with keyboard (and work), I send "R" char with postmessage and work correctly.

If I replace "R" char with "P" char in SAME function, your application goes in infinite loop.

"P" and "H" char sended with postmessage generate an infinite loop......

If I Send with the same function "P" or "R" or "H" in cmd.exe, it show only ONE char sended.

Problem persist...

I can't continue my project if you don't resolve this bug.
thanks.

## xmrig | 2018-01-10T17:01:44+00:00
Problem still persist after this https://github.com/xmrig/xmrig/commit/e6540229cba5bdb52c3a80615bb0f5266f63d4db commit?

## Sinner181 | 2018-01-10T17:16:54+00:00
I'm not using your source, I need a new release with this fix....

I use yours xmrig64.exe  xmrig32.exe directly.

Is possible?

## Sinner181 | 2018-01-11T01:25:14+00:00
Can you rebuild application please? I don't want install other application....thanks.

## Mila432 | 2018-01-11T13:48:33+00:00
@Sinner181 nice troll
>I'm programmer since 20 years
>can’t even compile the source 

## Sinner181 | 2018-01-11T14:18:02+00:00
What mean? I'm delphi programmer.... I don't want install other softwares in my computer....it's simple.

## Sinner181 | 2018-01-11T14:18:36+00:00
There is a bug in this software, and is not mine =)

## Sinner181 | 2018-01-12T12:49:47+00:00
Thanks, now work correctly! =)
(I set 2% fee for you in my application)
See you, bye

## Sinner181 | 2018-01-23T03:20:53+00:00
Hi, there is the same problem with

Nvidia cuda 8
Nvidia cuda 9
AMD 32bit
AMD 64bit

I'm  trying to add in my project but is impossible with this issue.
Can you fix like xmrig cpu version? Binary release too if possible.

Thank you!

# Action History
- Created by: Sinner181 | 2018-01-09T02:05:30+00:00
- Closed at: 2019-08-02T12:46:44+00:00
