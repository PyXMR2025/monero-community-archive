---
title: 'Wallet2: store wallet path as UTF-16 on windows'
source_url: https://github.com/monero-project/monero/issues/1390
author: Jaqueeee
assignees: []
labels:
- enhancement
created_at: '2016-11-29T16:37:41+00:00'
updated_at: '2018-05-10T17:24:52+00:00'
type: issue
status: closed
closed_at: '2018-05-10T17:24:52+00:00'
---

# Original Description
On Windows, wallet path needs to be saved in UTF-16 to support non-ascii characters. https://github.com/monero-project/monero-core/issues/199

Proposed solution:

Convert input strings from UTF-8 -> UTF-16
Port all std/boost::fstream to windows CreateFile() that accepts UTF-16 wchar_t as input.

boost::fstream supports wstring input but not with Mingw:
https://svn.boost.org/trac/boost/ticket/9968

Note: lmdb already use createFile()
https://github.com/monero-project/monero/blob/master/external/db_drivers/liblmdb/mdb.c#L4802-L4810

# Discussion History
## moneromooo-monero | 2016-11-29T19:40:41+00:00
Rewriting boost stuff sounds crazy. Surely Windows isn't that crappy and we're missing something...

## ghost | 2016-11-29T20:02:25+00:00
Maybe this would help:

http://www.boost.org/doc/libs/1_52_0/libs/locale/doc/html/charset_handling.html

Using boost.locale to convert character sets?

## Jaqueeee | 2016-11-29T20:45:56+00:00
AFAICT the problem is not boost but Mingw. But we should probably just ask a win dev. 
I've spent some hours already without success . Tried this in particular:
http://www.boost.org/doc/libs/1_52_0/libs/locale/doc/html/default_encoding_under_windows.html


## sanderfoobar | 2017-12-01T14:24:51+00:00
2 cents:

Boost (perhaps incombination with mingw) has a bug here. The offending lines are (could be more):

https://github.com/monero-project/monero/blob/master/src/wallet/wallet2.cpp#L2608-L2616
https://github.com/monero-project/monero/blob/master/src/wallet/wallet2.cpp#L2739
https://github.com/monero-project/monero/blob/master/src/wallet/wallet2.cpp#L2750
https://github.com/monero-project/monero/blob/master/src/wallet/wallet2.cpp#L2759

Maybe just use `CreateFileW` when on Windows in a `ifdef win32`, just like lmdb does as previously mentioned: [example](https://github.com/monero-project/monero/blob/master/external/db_drivers/liblmdb/mdb.c#L4819-L4826)

As for checking if a file exists; this can be done via `CreateFileW` as well - by opening a file in read-only mode and read the status back (should give a 'file does not exist' status).

So, I propose to not use boost but `CreateFileW` when on windows, `open` on unix.



## dEBRUYNE-1 | 2018-01-08T12:44:26+00:00
+enhancement

## sanderfoobar | 2018-05-10T16:44:20+00:00
Fixed in [monero-gui #1141](https://github.com/monero-project/monero-gui/pull/1141)

+resolved

## dEBRUYNE-1 | 2018-05-10T17:20:54+00:00
+resolved

# Action History
- Created by: Jaqueeee | 2016-11-29T16:37:41+00:00
- Closed at: 2018-05-10T17:24:52+00:00
