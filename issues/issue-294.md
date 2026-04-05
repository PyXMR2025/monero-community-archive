---
title: compile xmrig x86
source_url: https://github.com/xmrig/xmrig/issues/294
author: velosipeds
assignees: []
labels: []
created_at: '2017-12-26T06:45:45+00:00'
updated_at: '2018-11-05T07:05:33+00:00'
type: issue
status: closed
closed_at: '2018-11-05T07:05:33+00:00'
---

# Original Description
Hello!
Please help me to compile mining client xmrig version for x32 windows always this error
#if !defined(_M_IX86) && !defined(_M_X64)
#error This header is specific to X86 and X64 targets
#endif 

my platform Windows 8.1 x64
Visual Studio 2015 

# Discussion History
## xmrig | 2017-12-28T08:28:36+00:00
You sure this is the error? Miner should build fine with msvc2015, but is MSYS2 preferred for x86 builds.
Thank you.

# Action History
- Created by: velosipeds | 2017-12-26T06:45:45+00:00
- Closed at: 2018-11-05T07:05:33+00:00
