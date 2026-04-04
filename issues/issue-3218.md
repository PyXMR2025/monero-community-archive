---
title: Segmentation fault when pressing Ctrl-C in prompt for password
source_url: https://github.com/monero-project/monero/issues/3218
author: heptathlon
assignees: []
labels: []
created_at: '2018-01-31T22:37:22+00:00'
updated_at: '2018-02-18T20:15:59+00:00'
type: issue
status: closed
closed_at: '2018-02-18T20:15:59+00:00'
---

# Original Description
1.) Start monero-wallet-cli and unlock wallet with your password
2.) Run 'password' command (will ask for your password again)
3.) __Do not enter your password__. Press Ctrl-C instead

Output is:

Wallet password:
Error: invalid password
Error: Your original password was incorrect.
Segmentation fault: 11

# Discussion History
## moneromooo-monero | 2018-02-01T14:14:54+00:00
Does https://github.com/monero-project/monero/pull/3222 fix it ? I could not repro the segfault here.

## jtgrassie | 2018-02-02T12:47:46+00:00
@moneromooo-monero I can confirm I never had a segfault with the reported steps either.

## vtnerd | 2018-02-02T23:57:32+00:00
https://paste.debian.net/1008610/

One of the stack traces is too large, and the other is for something else.

## moneromooo-monero | 2018-02-18T19:18:45+00:00
Should be fixed by https://github.com/monero-project/monero/pull/3249, can you confirm ?

## heptathlon | 2018-02-18T20:15:59+00:00
@moneromooo-monero thanks, fixed.

# Action History
- Created by: heptathlon | 2018-01-31T22:37:22+00:00
- Closed at: 2018-02-18T20:15:59+00:00
