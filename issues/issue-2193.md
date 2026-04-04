---
title: Cursor inside prompt in monero-wallet-cli
source_url: https://github.com/monero-project/monero/issues/2193
author: moneromooo-monero
assignees: []
labels: []
created_at: '2017-07-23T09:10:20+00:00'
updated_at: '2018-11-07T15:25:18+00:00'
type: issue
status: closed
closed_at: '2018-11-07T15:25:18+00:00'
---

# Original Description
In monero-wallet-cli, I got the cursor on a new line to reliably end up within the prompt, leading the typing a command erase part of the prompt:

[wallet 9vpern]: balance
Balance: 1.978693000000, unlocked balance: 1.978693000000
[wbalancevpern]: 
Balance: 1.978693000000, unlocked balance: 1.978693000000
[wallet 9vpern]: 

It's not visible here, but the cursor is currently blinking over the a in the last line, so it's happened twice in a row in the example above.

Pressing enter and a fake command "fixed" the position.

This is using all the latest merged readline patches.


# Discussion History
## moneromooo-monero | 2017-07-23T10:03:28+00:00
Possibly related: I typed a command, and did not get a prompt on next line. The command was executed fine, and the next command did yield a prompt:

[wallet 9vpern]: set_log 2
balance
Balance: 1.957414080000, unlocked balance: 1.957414080000
[wallet 9vpern]: 


## moneromooo-monero | 2017-07-24T10:17:11+00:00
That second one (no prompt) happens reliably for "set_log 2". Possibly when a command has no output.

## jtgrassie | 2017-07-24T10:56:43+00:00
I'll take a look. 

## moneromooo-monero | 2017-07-24T12:51:31+00:00
Manual "refresh" in monero-wallet-cli is also wonky wrt the prompt. This uses \r to overwrite the counter. Make sure you have a lot of blocks to refresh so you can see it.

## jtgrassie | 2017-07-24T14:00:33+00:00
#2197 should fix the empty prompt issue. I haven't managed to test the refresh one yet.

## moneromooo-monero | 2017-08-17T20:01:08+00:00
Very easy to repro with the new (no daemon) and (out of sync) prompt changes.
Run wallet without dameon. Start daemon. Press enter. This will invariably screw up the prompt, will be usually be OK after a second enter.

Still also wonky with manual refresh, though a bit differently:
create new wallet with a running daemon, it will start refreshing. ^C to stop refresh. Run "refresh". You'll see the prompt hide the "X/Y" count, leading you to believe you can run commands when you actually can't.

## jtgrassie | 2017-08-18T11:54:13+00:00
I get the same results with and without readline enabled for that use case.

## moneromooo-monero | 2017-08-18T13:45:46+00:00
I just recompiled without readline, and it looks good. It only looks wonky (The X/Y counter being hidden by an overeager prompt, and the next prompt being mangled with the cursor halfway in the prompt) with readline.

## jtgrassie | 2017-08-18T13:57:33+00:00
Odd. I'll try on a Linux box.

## moneromooo-monero | 2018-10-12T21:05:18+00:00
https://github.com/monero-project/monero/pull/4573

## moneromooo-monero | 2018-11-07T14:31:08+00:00
+resolved

# Action History
- Created by: moneromooo-monero | 2017-07-23T09:10:20+00:00
- Closed at: 2018-11-07T15:25:18+00:00
