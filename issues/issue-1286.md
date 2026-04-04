---
title: can't exit monerod on 2012 server
source_url: https://github.com/monero-project/monero/issues/1286
author: gbb0330
assignees: []
labels: []
created_at: '2016-11-01T02:18:49+00:00'
updated_at: '2016-12-15T16:05:41+00:00'
type: issue
status: closed
closed_at: '2016-12-15T16:05:41+00:00'
---

# Original Description
there is a problem with gracefully closing monerod.exe on 2012 server and 2012 server core. should be easy to reproduce, i can successfully and consistently reproduce the problem on 3 different servers.

the problem occurs if you type exit in the daemon, or if you use curl to send stop_daemon command.
the daemon hangs at p2p net loop stopped until the enter key is pressed.
see screenshot below

http://imgur.com/a/yE42B

as soon as the enter key is presses the daemon closes as expected. this creates a problem with scheduled tasks for example, i can't gracefully close the daemon unless i am physically present to press enter.


# Discussion History
## moneromooo-monero | 2016-11-01T12:52:30+00:00
Are you a Windows coder ? I think I know more or less what the problem is, and how to fix it. I just need a Windows coder to find the right Windows API to replace a POSIX one, and test it :)


## gbb0330 | 2016-11-01T20:34:15+00:00
unfortunately i am not a coder. just a sys admin


## ghost | 2016-11-05T14:30:03+00:00
Maybe @vtnerd could help us out here?


## vtnerd | 2016-11-07T12:54:13+00:00
This would currently not be a priority for me, but I can try to look at it. I have only have Windows 8 with VS 2013/2015, so I have to first get mingw installed. @moneromooo-monero what POSIX function needs replacing?


## moneromooo-monero | 2016-11-07T21:16:21+00:00
1 - make sure you can reliably enough repro the bug, as it's apparently random-ish

2 - I'm not sure this is the reason, but it looks likely to me

3 - look in contrib/epee/include/console_handler.h, in wait_stdin_data, there's a select call ("wait till there's something to read on the fd we're passing"), which means the Linux implementation will not get into std::getline (blocking) if there's nothing to input. I think if we get into getline, the thread blocks till enter is pressed. So the trick is to replace select.


## gbb0330 | 2016-11-08T22:17:46+00:00
here is a direct link to 2012 server core that you can use to test with (no license required). in case you need it:

http://care.dlservice.microsoft.com/dl/download/3/4/7/347A95F0-A63C-492F-BE43-F376AE30C9FE/9200.16384.WIN8_RTM.120725-1247_X64FRE_SERVERHYPERCORE_EN-US-HRM_SHV_X64FRE_EN-US_DV5.ISO


## gbb0330 | 2016-11-09T20:37:10+00:00
confirming bug is random-ish, but its easy to reproduce, at least on my servers it happens very often.


## moneromooo-monero | 2016-11-17T22:35:53+00:00
I had a look on ddg and came up with https://github.com/monero-project/monero/pull/1353. Apparently it works.


## luigi1111 | 2016-12-15T16:05:41+00:00
Fixed by #1353 (if found to be untrue, please reopen/open a new issue).

# Action History
- Created by: gbb0330 | 2016-11-01T02:18:49+00:00
- Closed at: 2016-12-15T16:05:41+00:00
