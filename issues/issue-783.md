---
title: build error on linux centos
source_url: https://github.com/xmrig/xmrig/issues/783
author: 0xman
assignees: []
labels:
- question
created_at: '2018-10-08T18:04:59+00:00'
updated_at: '2019-03-17T16:32:25+00:00'
type: issue
status: closed
closed_at: '2019-03-17T16:32:25+00:00'
---

# Original Description
Hey can you explain to me what this error means http://prntscr.com/l3oqx0

# Discussion History
## xmrig | 2018-10-08T18:12:00+00:00
What your compiler version? Minimum reported working version is gcc 4.9. You compiler too old and not support `-Ofast`, you can edit this file https://github.com/xmrig/xmrig/blob/master/cmake/flags.cmake#L16 and replace `-Ofast` to `-O2` and try again, but better use newer compiler.
Thank you.

## 0xman | 2018-10-10T19:55:09+00:00
how do i compile with out microhttpd/0.9.44
OpenSSL/1.0.2g
?

## xmrig | 2018-10-10T22:12:32+00:00
`-DWITH_HTTPD=OFF -DWITH_TLS=OFF`

## 0xman | 2018-10-10T23:13:33+00:00
what's this av=0 ? http://prntscr.com/l4mxvq isnt supposed to be av=1 ?

## DeadManWalkingTO | 2019-03-17T14:23:41+00:00
I think this issue can be closed.
Thank you!

# Action History
- Created by: 0xman | 2018-10-08T18:04:59+00:00
- Closed at: 2019-03-17T16:32:25+00:00
