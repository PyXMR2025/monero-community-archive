---
title: 32 bit Compiling succeed but xmrig crashes
source_url: https://github.com/xmrig/xmrig/issues/1062
author: itaBlackHawk
assignees: []
labels:
- bug
- need feedback
created_at: '2019-07-16T20:27:15+00:00'
updated_at: '2019-08-09T10:10:26+00:00'
type: issue
status: closed
closed_at: '2019-08-09T10:10:26+00:00'
---

# Original Description
Hi Everyone,
I just tried to compile & run xmrig on an old 32-bit thin client, running a fresh install of 18.04.2 LTS (GNU/Linux 4.15.0-54-generic i686).

Compiling runs fine and with no error, but when I try to run xmrig it just prints

> Floating point exception

and quits.
the only trace I could find in log/syslog was

ubuntu kernel: [ 7140.306871] traps: xmrig[9612] trap divide error ip:5d225f sp:bfad66d0 error:0 in xmrig[40a000+330000]

I tried compiled without any flags as well as with

> cmake -DCMAKE_CXX_FLAGS=-m32 -DCMAKE_C_FLAGS=-m32 .

same result: no error on compiling, still doesn't run (--help works still)
any idea? the thin client of course got very limited hardware, HD is 2 Gb in total and RAM is 1 GB, could it depend on that?

thank you for the support. 

# Discussion History
## itaBlackHawk | 2019-07-25T11:21:27+00:00
If any data more is needed to debug, please don't hesitate to ask for it.. I'll try again in the next days and with the new versions to see if something changes 

## xmrig | 2019-08-02T11:37:48+00:00
https://github.com/xmrig/xmrig/commit/718be7e9aa89b163077d40cf0e6cd63dae7d2757 this commit should fix crash.
Thank you.

## itaBlackHawk | 2019-08-02T16:40:52+00:00
works like a charm! thank you!

# Action History
- Created by: itaBlackHawk | 2019-07-16T20:27:15+00:00
- Closed at: 2019-08-09T10:10:26+00:00
