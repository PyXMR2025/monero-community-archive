---
title: Block cumulative size is too big
source_url: https://github.com/monero-project/monero/issues/1926
author: ddyzhang
assignees: []
labels: []
created_at: '2017-03-25T23:45:02+00:00'
updated_at: '2017-03-31T17:25:52+00:00'
type: issue
status: closed
closed_at: '2017-03-31T17:25:52+00:00'
---

# Original Description
Following error message found in the logs after upgrading to v0.10.3.0 on one of my win64 machines:
`Block cumulative size is too big: 227915964163754343, expected less than 131522`

Daemon will not sync past block 1274262 and appears to be rejecting and then banning any node attempting to relay the next block.

All of my other machines appear to be fine. Upgraded straight from 0.10.2.1, no resync performed.

See the level 4 log file here (warning, large text file): https://derekzhang.org/uploads/monero.log

# Discussion History
## moneromooo-monero | 2017-03-26T01:28:54+00:00
Probably fixed  by https://github.com/monero-project/monero/pull/1927

## schnerchi | 2017-03-26T08:03:31+00:00
are there any reports for this from other OS than win64?

## fluffypony | 2017-03-26T08:08:06+00:00
@schnerchi someone on IRC reported having it on macOS, but considering we've only had 2 reports of it it's either environmental or isolated. If you're not seeing it then it doesn't matter:)

## schnerchi | 2017-03-26T08:09:06+00:00
I am asking if I can test against it. mac os and ubuntu avail..

## fluffypony | 2017-03-26T08:09:38+00:00
@schnerchi yes, please do :)

## schnerchi | 2017-03-26T08:10:09+00:00
okay.. trying your release builds then....

## moneromooo-monero | 2017-03-26T09:26:37+00:00
If you can build your own, and get the same problem, can you please do this:
- edit src/cryptonote_basic/cryptonote_format_utils.cpp
- line 46, uncomment the line: // #define ENABLE_HASH_CASH_INTEGRITY_CHECK

Then try again and see if you get integrity check fails in the log, and post the log if so.

## jakefb | 2017-03-26T09:29:27+00:00
I'm having this issue too on Debian 8.7 64 bit. When I upgrade to v0.10.3.0 it worked at first and I was able to send a transaction, but when sending a second transaction I accidentally killed the daemon so it didn't successfully send and since then had this issue persistently

`2017-03-26 09:25:43.447	[P2P7]	ERROR	cn	src/cryptonote_basic/cryptonote_basic_impl.cpp:114	Block cumulative size is too big: 6691072190604965985, expected less than 131274`

## adot23 | 2017-03-31T13:06:36+00:00
I experienced this with a docker build of v0.10.3.0. It appears to be fixed for v0.10.3.1.

## ddyzhang | 2017-03-31T17:25:52+00:00
No new reports of this issue in v0.10.3.1, appears to be fixed by #1927.

# Action History
- Created by: ddyzhang | 2017-03-25T23:45:02+00:00
- Closed at: 2017-03-31T17:25:52+00:00
