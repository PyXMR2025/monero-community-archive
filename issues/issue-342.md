---
title: 'crashes when DNS resolving temporary failure '
source_url: https://github.com/xmrig/xmrig/issues/342
author: zzh1996
assignees: []
labels:
- libuv
created_at: '2018-01-16T16:17:21+00:00'
updated_at: '2018-11-05T14:42:51+00:00'
type: issue
status: closed
closed_at: '2018-11-05T14:42:51+00:00'
---

# Original Description
When my network is temporarily not working, xmrig cannot resolve the domain name of my mining pool. It will crash.
```
src/unix/getaddrinfo.c:91: uv__getaddrinfo_translate_error: Assertion `!"u
nknown EAI_* error code"' failed.
Aborted (core dumped)
```

# Discussion History
## xmrig | 2018-01-17T11:25:04+00:00
Please provide more details what OS and libuv version did you use, etc.
Thank you.

# Action History
- Created by: zzh1996 | 2018-01-16T16:17:21+00:00
- Closed at: 2018-11-05T14:42:51+00:00
