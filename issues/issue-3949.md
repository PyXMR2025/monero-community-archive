---
title: monerod crashing when using with the USX GUI wallet
source_url: https://github.com/monero-project/monero/issues/3949
author: ManfredKarrer
assignees: []
labels: []
created_at: '2018-06-06T21:33:12+00:00'
updated_at: '2022-03-16T15:44:44+00:00'
type: issue
status: closed
closed_at: '2022-03-16T15:44:44+00:00'
---

# Original Description
I get monerod crashing when using with the GUI wallet.
I use latest version (0.12). At the last crash it shows a "Segmentation fault: 11" in the console.
Any idea?

# Discussion History
## moneromooo-monero | 2018-06-06T22:47:46+00:00
Enable core dumps ("echo core | sudo tee /proc/sys/kernel/core_pattern" and "ulimit -c unlimited"), then run monerod again. After a crash: "gdb /path/to/monerod /path/to/core/file". Then, when in gdb: bt full. Then paste the outpuf of that last command here.

## dEBRUYNE-1 | 2018-06-07T17:12:55+00:00
@ManfredKarrer - Are you using GUI v0.12.0.0 in combination with `monerod` v0.12.2.0? 

## ManfredKarrer | 2018-06-07T19:31:52+00:00
@dEBRUYNE-1 
Yes.
I have now monerod solo running (with  --max-concurrency 1) and it has not crashed. So might be related to the combination with the GUI.

## moneromooo-monero | 2018-06-07T19:43:21+00:00
Then please use the crashing combination. A monerod crash is bad, even if "mismatched".


## ManfredKarrer | 2018-06-07T21:35:11+00:00
Got again a "Segmentation fault: 11" with running monerod without the  --max-concurrency 1 option.
I remember that this was already a problem 1-2 years ago. In the meantime it seemed that it was working without that option.

## moneromooo-monero | 2018-06-08T07:38:10+00:00
Did you forget to post the stack trace from gdb ?

## ManfredKarrer | 2018-06-08T09:46:51+00:00
I am on OSX, so the above commands don't work. 

Just got another Segmentation fault: 11 while running with  --max-concurrency 1.

## moneromooo-monero | 2018-06-08T11:29:51+00:00
Try lldb instead, I think it's got similar commands.

## moneromooo-monero | 2018-06-09T12:08:46+00:00
If you're unable to get a stack trace with lldb or other, then try this patch set: https://github.com/monero-project/monero/pull/3642

If you apply those two on top of what you have, a crash should print a stack trace in the log.


## ManfredKarrer | 2018-06-09T13:35:35+00:00
Updated monerod to 0.12.2.0 and with that it finally worked...

## moneromooo-monero | 2018-06-09T13:56:32+00:00
It would still be good to know what happened where. The crash may well still be around, just not triggered by that change.


## moneromooo-monero | 2018-06-18T08:45:01+00:00
Oh, since you're using Mac, you might need --max-concurrency 1. There's some kind of threading lib bug on Mac.

## ManfredKarrer | 2018-06-19T12:32:41+00:00
Latest software runs not stable... The buggy one before was also crashing with --max-concurrency 1

## moneromooo-monero | 2018-12-18T12:47:12+00:00
If there's no stack trace or any other clue, I'll just close this.


## ManfredKarrer | 2018-12-19T11:50:03+00:00
Have not seen any issue anymore since a while.

## moneromooo-monero | 2018-12-21T20:30:45+00:00
With another version, presumably ?

# Action History
- Created by: ManfredKarrer | 2018-06-06T21:33:12+00:00
- Closed at: 2022-03-16T15:44:44+00:00
