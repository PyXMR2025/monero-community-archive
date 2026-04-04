---
title: daemon output color problem
source_url: https://github.com/monero-project/monero/issues/1934
author: SnaiLiuS
assignees: []
labels:
- bug
created_at: '2017-03-27T20:56:15+00:00'
updated_at: '2021-08-13T04:09:53+00:00'
type: issue
status: closed
closed_at: '2021-08-13T04:09:53+00:00'
---

# Original Description
Screenshot shows the problem:

![default](https://cloud.githubusercontent.com/assets/22018711/24377602/94159504-1348-11e7-902e-15629f328bbf.png)


# Discussion History
## anonimal | 2017-03-27T21:22:37+00:00
Color capable terminal? OS? Distro?

## iDunk5400 | 2017-03-27T21:54:41+00:00
That does not look like a recent Windows 10, probably Windows 7 or 8/8.1. So even if I PRed a possible solution, it would not work for you.

![image](https://cloud.githubusercontent.com/assets/20195079/24379718/94747c68-1348-11e7-9f75-698faaf8a1f0.png)


## SnaiLiuS | 2017-03-28T04:39:11+00:00
Bad dreams guys: windows vista 6.0.6002 here. 

daemon 0.10.3.1

btw, wallet-cli colorization is ok, only daemon color is broken since 0.10.1.0+ release

## anonimal | 2017-03-28T17:20:06+00:00
>windows vista 6.0.6002
>0.10.1.0+

I don't see Vista in easylogging++'s [compatability list](https://github.com/muflihun/easyloggingpp#compatibility).

## hyc | 2017-03-28T18:18:27+00:00
http://monero.stackexchange.com/questions/3705/monero-win-x64-v0-10-2-1-cli-questions

## tikwanleap | 2017-03-30T21:47:57+00:00
I have the same problem in Windows 10 64 bit since 0.10.1.0 release. Still happening in latest 0.10.3.1 release.

In hyc's stackexchange answer (https://superuser.com/questions/413073/windows-console-with-ansi-colors-handling/1050078) there is a mention of needing to call the SetConsoleMode function to get this working in Windows: https://msdn.microsoft.com/en-us/library/windows/desktop/ms686033(v=vs.85).aspx

I think the value that needs to be passed to the SetConsoleMode function is this:
    ENABLE_VIRTUAL_TERMINAL_PROCESSING
    0x0004

Also I noticed that only monerod.exe is missing colors except for when I type "status". The monero-wallet.cli.exe has correct colors.

## tikwanleap | 2017-03-30T22:07:57+00:00
Could it be related to this issue?
https://github.com/muflihun/easyloggingpp/issues/363

## tikwanleap | 2017-04-01T06:38:32+00:00
This looks like the solution.

https://github.com/bin-build/bin/commit/e4a038bb7f89b51f3eb794b83da6fa054d48900b

Apparently Windows 10 had ansi color support enabled by default at one point but more recent versions have it disabled by default.

The application needs to programmatically enable ansi color support.

## moneromooo-monero | 2017-07-24T12:35:58+00:00
Any coder with Windows want to make a patch based on the above ? :)

## dEBRUYNE-1 | 2018-01-08T12:29:36+00:00
+bug

## dEBRUYNE-1 | 2018-01-08T12:33:58+00:00
+help wanted

## moneromooo-monero | 2018-10-20T22:44:39+00:00
Fixed for some versions of Windows.



## ghost | 2019-06-25T12:34:36+00:00
Vista is "dead" since 2 years:

https://support.microsoft.com/en-za/help/22882/windows-vista-end-of-support

So possibly its not worth to spend resources to make cosmetic things work for it.

Issue should be closable.


## moneromooo-monero | 2019-07-05T19:02:27+00:00
Ah, I fixed it anwyay, since it was small stuff on top of other work I needed to do.
See https://github.com/monero-project/monero/pull/5688
I'll close this when it gets merged.

# Action History
- Created by: SnaiLiuS | 2017-03-27T20:56:15+00:00
- Closed at: 2021-08-13T04:09:53+00:00
