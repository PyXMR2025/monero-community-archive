---
title: Compile error mingw64
source_url: https://github.com/xmrig/xmrig/issues/164
author: SAYONARABOYZ
assignees: []
labels:
- libuv
created_at: '2017-10-21T20:32:06+00:00'
updated_at: '2018-03-14T23:20:33+00:00'
type: issue
status: closed
closed_at: '2018-03-14T23:20:33+00:00'
---

# Original Description
make[2]: *** No rule to make target 'C://gcc/libuv/x64/lib/libuv.a', needed by 'xmrig.exe'. Stop.
What a problem?

# Discussion History
## xmrig | 2017-10-22T05:16:54+00:00
Probably because of `//`. Thank you.

# Action History
- Created by: SAYONARABOYZ | 2017-10-21T20:32:06+00:00
- Closed at: 2018-03-14T23:20:33+00:00
