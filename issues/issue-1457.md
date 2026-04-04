---
title: Error when compiling on Ubuntu 16.04 (vultr 2gb ram)
source_url: https://github.com/monero-project/monero/issues/1457
author: pmitchev
assignees: []
labels: []
created_at: '2016-12-15T00:47:51+00:00'
updated_at: '2016-12-26T07:12:19+00:00'
type: issue
status: closed
closed_at: '2016-12-25T08:48:34+00:00'
---

# Original Description
I got the following error when I compile the latest version from master:
http://pastebin.com/PR8epe8M

# Discussion History
## ghost | 2016-12-15T01:27:51+00:00
@pmitchev Can you try `sudo apt-get install -y liblzma-dev` and report back if that works? 

## pmitchev | 2016-12-15T02:42:44+00:00
no success

## ghost | 2016-12-15T11:29:09+00:00
So even with liblzma the build still fails?

If so, uninstall libunwind and liblzma and try again - you just won't be able to get stack traces but it should build. We'll chalk this one up to yet another libunwind issue. 

## moneromooo-monero | 2016-12-15T22:50:11+00:00
It's probably the same again and again :)

## ghost | 2016-12-18T12:09:07+00:00
@moneromooo-monero Is there any alternative stack trace tool/library available which we could just bundle with monerod?

For example, I found this header-only library:

https://github.com/bombela/backward-cpp/blob/master/README.md

## ghost | 2016-12-24T23:52:11+00:00
@pmitchev @moneromooo-monero has submitted PR #1494 to address this issue. Would you mind testing and reporting back inside #1494? Thanks!

# Action History
- Created by: pmitchev | 2016-12-15T00:47:51+00:00
- Closed at: 2016-12-25T08:48:34+00:00
