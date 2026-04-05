---
title: issue with compiled xmrig
source_url: https://github.com/xmrig/xmrig/issues/261
author: chri121
assignees: []
labels:
- bug
created_at: '2017-12-13T07:17:31+00:00'
updated_at: '2019-08-02T12:45:08+00:00'
type: issue
status: closed
closed_at: '2019-08-02T12:45:08+00:00'
---

# Original Description
Hello, i got the follwing problem:

i compiled it with vs2017 and if I start the xmrig.exe, it closes right after the start without any error code. 

I tried to debug it says "File: minkernel\crts\ucrt\src\appcrt\stdio\fdopen.cpp
Line 29
Expression: _osfile(fh) & FOPEN

The precompiled binaries work without any other issue.


# Discussion History
## xmrig | 2017-12-16T12:06:54+00:00
Looks like same issue, just in wrong place https://github.com/fireice-uk/xmr-stak/issues/296
Release builds not affected.
Thank you.

# Action History
- Created by: chri121 | 2017-12-13T07:17:31+00:00
- Closed at: 2019-08-02T12:45:08+00:00
