---
title: 'win-x64-v0.12.0.0 / command line wallet / password prompt does not accept
  any input '
source_url: https://github.com/monero-project/monero/issues/3553
author: TheNec
assignees: []
labels: []
created_at: '2018-04-04T16:59:10+00:00'
updated_at: '2018-04-06T09:23:59+00:00'
type: issue
status: closed
closed_at: '2018-04-06T09:23:59+00:00'
---

# Original Description
1. You are now synchronized with the network. You may now start monero-wallet-cli...
2. Starting monero-wallet-cli...
3. Enter Wallet file name...
4. Wallet and key files found, loading...

It is not possible to enter a password. Neither manual keyboard input nor pasting works.

# Discussion History
## moneromooo-monero | 2018-04-04T17:52:45+00:00
Do you get the password prompt displayed ?
Does it work if you give --password "yourpasswordhere" ?



## TheNec | 2018-04-04T20:37:58+00:00
Thanks for your reply.

The password prompt is displayed and I tried it again and it works. The Problem is and I don't know if it is a bug or expected behavior that in the recent version there are no asterisks shown when entering a password and it seems that I have made a mistake when I entered it -.-

## moneromooo-monero | 2018-04-04T20:53:39+00:00
They were removed to avoid leaking password length IIRC. So...it's fine ?

## TheNec | 2018-04-04T21:00:39+00:00
Yeah thanks!

Perhaps this could be added to the release notes :)

# Action History
- Created by: TheNec | 2018-04-04T16:59:10+00:00
- Closed at: 2018-04-06T09:23:59+00:00
