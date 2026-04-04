---
title: Failure to detect readline on Fedora
source_url: https://github.com/monero-project/monero/issues/2992
author: eklitzke
assignees: []
labels:
- duplicate
created_at: '2017-12-22T21:24:25+00:00'
updated_at: '2017-12-25T17:56:23+00:00'
type: issue
status: closed
closed_at: '2017-12-25T17:56:23+00:00'
---

# Original Description
Monero fails to detect GNU Readline on my computer (Fedora 27). I spent some time looking at this, and the issue is that on my computer linking with -lreadline also requires linking with -ltinfo. I'm not that proficient with CMake, but I think the right thing to do in FindReadline.cmake is:

 * Try compiling the readline test program with just -lreadline
 * If that fails, try compiling with -lreadline and -lcurses
 * If that fails, try compiling with -lreadline and -ltinfo

This would also allow removing the OpenBSD-specific logic introduced in #2874

# Discussion History
## moneromooo-monero | 2017-12-22T22:29:14+00:00
https://github.com/monero-project/monero/issues/2919 (WIP)

## moneromooo-monero | 2017-12-25T17:48:48+00:00
+duplicate

# Action History
- Created by: eklitzke | 2017-12-22T21:24:25+00:00
- Closed at: 2017-12-25T17:56:23+00:00
