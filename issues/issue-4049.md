---
title: 'Wrong Device Status : SW=6911 (EXPECT=9000, MASK=ffff)'
source_url: https://github.com/monero-project/monero/issues/4049
author: stoffu
assignees: []
labels: []
created_at: '2018-06-25T07:43:09+00:00'
updated_at: '2019-05-27T01:12:05+00:00'
type: issue
status: closed
closed_at: '2018-10-09T11:24:55+00:00'
---

# Original Description
With macOS Sierra 10.12.6, previously I was able to make transactions using Ledger Nano S following this installation guide:

- https://monero.stackexchange.com/questions/8438/how-do-i-make-my-macos-detect-my-ledger-nano-s-when-plugged-in/

However, recently I realized that I get the following error when I try to transfer coins:

> Error: unexpected error: Wrong Device Status : SW=6911 (EXPECT=9000, MASK=ffff)

I get the error both with the current master ffab67004 and the latest release v0.12.2.0. The wallet can correctly recognize incoming transfers. I don't know since exactly when this problem started to show up.


# Discussion History
## dnaleor | 2018-06-26T20:56:09+00:00
Got a similar error when trying to help a friend installing his ledger on his Mac (10.11.6) using the GUI 12.0

> Can't create transaction: unexpected error: Wrong Device Status : SW=6a80 (EXPECT=9000, MASK=ffff)

edit: I did follow the exact same guide.

edit: initialization works, connecting works, when hitting "send" in the GUI the transaction does show up on the ledger. After confirming fee and address however, this error is thrown.

cc @cslashm

## tficharmers | 2018-07-05T13:11:24+00:00
0.12.1.0 works with Ledger for me on a Mac. Doesn't work on Windows though.

## cslashm | 2018-07-05T13:20:36+00:00
6a80 means SW_WRONG_DATA
6911 is weird

do you have APDU log ?

## stoffu | 2018-07-06T07:18:51+00:00
Hmm, after a while of not trying Ledger, just now I found it suddenly working. Maybe restarting the computer a few times helped? I'll report if I see the same error again.

## moneromooo-monero | 2018-10-09T11:11:08+00:00
Since libpcsc-lite is now removed, this is moot. There are other bugs about new ledger comms failure with libhidapi :)

+resolved

## heapxor | 2019-03-04T13:44:23+00:00
how was thet resolved? i am getting same error.

## krtschmr | 2019-05-27T01:12:05+00:00
same error

win10, gui 14.0, cli 14.0

# Action History
- Created by: stoffu | 2018-06-25T07:43:09+00:00
- Closed at: 2018-10-09T11:24:55+00:00
