---
title: Wallet (auto)save not working / Wrong filename
source_url: https://github.com/monero-project/monero/issues/7214
author: TheNec
assignees: []
labels: []
created_at: '2020-12-28T12:35:57+00:00'
updated_at: '2021-10-06T02:40:34+00:00'
type: issue
status: closed
closed_at: '2021-10-06T02:40:34+00:00'
---

# Original Description
The wallet's name is "wallet" but according to the log it can't write to "wallet".new

As the last write date to the file is 2019-11-25 the problem started most probably with v0.15.0.

Thank you in advance and best regards!

# Discussion History
## moneromooo-monero | 2020-12-28T13:00:33+00:00
Are you *sure* you have enough space, permissions on that directory, etc ?

## TheNec | 2020-12-28T13:48:29+00:00
Thanks for your quick response!

_Sure_ is such a big word... ;)

Last year I installed/changed from CLI to GUI including moving the wallet files from former installation path at %programdata% to %programfiles%. So on the one hand if I start the software as admin it indeed works now but on the other hand the log message is misleading and/or a hint would be very nice. Also the CLI still searches for wallet files in the installation directory.

So this may be a low priority feature request or bug report.

## moneromooo-monero | 2020-12-28T19:56:48+00:00
What is the actual message that's misleading ?

## TheNec | 2020-12-31T17:48:43+00:00
The Error saving wallet.new and failed to generate wallet keys.new look like that the software has problems with the filename and not that it is a permission problem.

## selsta | 2021-10-06T02:40:34+00:00
Permission issue was resolved by issue creator.

# Action History
- Created by: TheNec | 2020-12-28T12:35:57+00:00
- Closed at: 2021-10-06T02:40:34+00:00
