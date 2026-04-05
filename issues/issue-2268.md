---
title: Can't use xmrig with  Cygwin
source_url: https://github.com/xmrig/xmrig/issues/2268
author: tradesmart844
assignees: []
labels:
- question
- wontfix
created_at: '2021-04-15T14:25:05+00:00'
updated_at: '2022-04-03T14:52:44+00:00'
type: issue
status: closed
closed_at: '2022-04-03T14:52:44+00:00'
---

# Original Description
I tried Linux xmrig binary as well build from source in cygwin on windows 10 machine. Unable start xmrig in cygwin. Has anyone tried this & got success?

# Discussion History
## Spudz76 | 2021-04-15T23:29:52+00:00
I believe msys64 is the only non-MSVC windows compiler supported, and even then it barely ever works.

I have never gotten cygwin64 to build successfully.  Nor msys64 actually.  I just stick to the free MSVS2019 Build Tools since that always works fine.

Cygwin is not for straight up running Linux apps, it's for compiling vanilla Linux app code on Windows without making it MSVC aware - but when something uses the memory functions for hugepages it's unsupported (unless it's partially windows aware... and cygwin gcc doesn't set any windows-related compiler defines to act as if it's Linux, by default).  Have not figured out proper workarounds.

## tradesmart844 | 2021-04-16T09:05:35+00:00
Yes you are correct, while building it on cygwin64, cmake was complaining about that.

# Action History
- Created by: tradesmart844 | 2021-04-15T14:25:05+00:00
- Closed at: 2022-04-03T14:52:44+00:00
