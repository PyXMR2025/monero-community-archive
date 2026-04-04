---
title: looping inclusion from one project to another?
source_url: https://github.com/monero-project/monero/issues/4541
author: calidion
assignees: []
labels: []
created_at: '2018-10-09T17:27:12+00:00'
updated_at: '2018-10-16T16:41:01+00:00'
type: issue
status: closed
closed_at: '2018-10-16T16:41:01+00:00'
---

# Original Description
```
contrib/epee/include/net/abstract_tcp_server2.inl:54:96: fatal error: ../../../../src/cryptonote_core/cryptonote_core.h
```
what is the level epee belongs to?
`crypto` is based on `epee`.
while `epee` is based on `cryptonote_core` and `cryptonote_protocol` which are both based on `crypto` module.
it's quite confusing.



# Discussion History
## moneromooo-monero | 2018-10-09T18:06:17+00:00
Known, I'll get it fixed someday. core depends on epee.

## moneromooo-monero | 2018-10-12T16:26:31+00:00
https://github.com/monero-project/monero/pull/4572

## calidion | 2018-10-13T04:36:08+00:00
@moneromooo-monero 

why it fails into some categories?

## moneromooo-monero | 2018-10-13T09:08:36+00:00
Can you rephrase that ?

## calidion | 2018-10-13T09:29:57+00:00
I mean these builds:

https://build.getmonero.org/builders/monero-linux-armv7/builds/1699

https://build.getmonero.org/builders/monero-linux-armv8/builds/813


## moneromooo-monero | 2018-10-13T10:18:20+00:00
Click on "stdio" in the fiurst link, gets you to https://build.getmonero.org/builders/monero-linux-armv7/builds/1699/steps/compile/logs/stdio
At the end of the file, it shows:
g++: error: missing argument to ‘-march=’

## calidion | 2018-10-13T10:51:38+00:00
how to fixed this problem?

## moneromooo-monero | 2018-10-13T12:40:12+00:00
For this one, apply PR 4565.

## calidion | 2018-10-14T07:32:09+00:00
Does this mean after pr 4565 is being merged, these errors will disappear?

## moneromooo-monero | 2018-10-16T16:38:57+00:00
+resolved

# Action History
- Created by: calidion | 2018-10-09T17:27:12+00:00
- Closed at: 2018-10-16T16:41:01+00:00
