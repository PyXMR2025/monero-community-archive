---
title: 'macOS: readline broken with torsocks (Ctrl-C is ignored)'
source_url: https://github.com/monero-project/monero/issues/3223
author: heptathlon
assignees: []
labels: []
created_at: '2018-02-01T21:56:29+00:00'
updated_at: '2022-04-08T14:35:42+00:00'
type: issue
status: closed
closed_at: '2022-04-08T14:35:41+00:00'
---

# Original Description
When starting latest master "monerod" ("DNS_PUBLIC=tcp torsocks monerod") on macOS the programme can not be stopped with Ctrl-C anymore. This worked fine with the most recent release but doesn't with the current master. Ctrl-C doesn't do anything (not shows "^C") with the master version. This may be related to readline support in monero which was adjusted since the latest release. The only solution is to hard kill monerod but then the whole terminal session must be reset with "reset", otherwise nothing really works (arrow key broken, enter broken usw)

I am not an expert unfortunately but will help to resolve this problem.

# Discussion History
## jtgrassie | 2018-02-02T12:45:54+00:00
The only readline changes since last release IIRC is changes in detecting it's presence in cmake while building. Nothing changed as far as the code.
Have you tried building and disabling readline to confirm it is readline related or are you just guessing it's readline related?

## heptathlon | 2018-02-02T17:45:42+00:00
Works fine without readline. Issue definitely caused by builds with readline.
Latest official macOS binary is not build with it, that's why it works just fine there.

## jtgrassie | 2018-02-02T17:52:17+00:00
That's misleading as latest official builds are very different to master. 


## heptathlon | 2018-02-02T18:27:46+00:00
It is broken using latest master ** with ** readline but works fine when built ** without ** readline.

## jtgrassie | 2018-02-02T18:40:45+00:00
If you follow the thread on a PR for this, you'll see the issue is far more involved unfortunately. 

## vtnerd | 2018-02-02T19:36:22+00:00
I have seen this issue without readline support. I atached gdb to the process and have 3 stack traces of every thread in the process, but I have yet to go through them. Looks to be some deadlock - every thread is waiting for a lock or waiting for some event to occur. The issue is probably in the `Blockchain` class, but that is just a rough guess.

I'll try to get the logs up to some pastebin shortly.

## vtnerd | 2018-02-02T19:37:18+00:00
@jtgrassie This is discussing `monerod`, and there is a PR against `monero-wallet-cli`. Is there another PR for this in `monerod`?

## jtgrassie | 2018-02-02T21:05:26+00:00
@vtnerd no, apologies. I got confused between this in the wallet ^C issue. But as you point out, readline not the issue with this one either it seems.

## moneromooo-monero | 2018-02-18T19:19:30+00:00
Should be fixed by #3249, can you confirm ?

## heptathlon | 2018-02-18T20:12:08+00:00
@moneromooo-monero issue is fixed now.

## heptathlon | 2018-02-18T20:17:39+00:00
Was able to reproduce it again, must wait for "The daemon will start synchronizing with the network." message, then Ctrl-C does not work. I am so sorry for spam.

## jtgrassie | 2018-02-18T22:16:13+00:00
@heptathlon when you say "does not work" do you mean it doesn't exit or it crashes?

## moneromooo-monero | 2018-02-18T23:39:35+00:00
If it's the daemon, it's quite likely it's exiting, but just waiting on a timeout on a connection.

## heptathlon | 2018-02-19T00:17:40+00:00
@jtgrassie @moneromooo-monero please see my initial bug description here https://github.com/monero-project/monero/issues/3223#issue-293697884
Pressing Ctrl-C does not do anything. Monero does not exit then.
After kill -9 monerod stops but the terminal window is unusable: arrow key dont work. I am sure it is related to readline because without it everything works fine like with latest stable release.
Please reproduce with torsocks and readline.

## jtgrassie | 2018-02-19T00:39:08+00:00
@heptathlon have you actually done a build of master without readline to confirm that is the issue? Just testing against the last release wont give you a true result. The fact you state ^C does nothing, suggests its the signal handler that has had stuff done on it since last release too.

## heptathlon | 2018-02-19T10:14:18+00:00
> have you actually done a build of master without readline to confirm that is the issue?

https://github.com/monero-project/monero/issues/3223#issuecomment-362665852

> but just waiting on a timeout on a connection

You might be correct. BUt then there still is the other problem which makes the terminal unusable after monerod exits.

## jtgrassie | 2018-02-19T12:25:00+00:00
What command did you use to build w/out readline? 

I question the readline assumption for a number of reasons, one of them being vtnerd's comment:
https://github.com/monero-project/monero/issues/3223#issuecomment-362684635

Also, can you do a debug build and post a backtrace after hitting ^C please.

Lastly, do you get the same result when not running through torsocks?
 

## heptathlon | 2018-02-19T18:03:20+00:00
> What command did you use to build w/out readline?

I removed these lines https://github.com/monero-project/monero/blob/master/CMakeLists.txt#L810-L821

> Lastly, do you get the same result when not running through torsocks?

Everything is fine without torsocks. I use torsocks often and had no problems with it except now.

> Also, can you do a debug build and post a backtrace after hitting ^C please.

I will be able to do that tomorrow.

## selsta | 2022-04-08T14:35:41+00:00
No reply from the author and no other replies, closing.

Also it's recommended to use `--proxy` now instead of `torsocks`.

# Action History
- Created by: heptathlon | 2018-02-01T21:56:29+00:00
- Closed at: 2022-04-08T14:35:41+00:00
