---
title: 'xmrig 2.8.0-rc: dry-run option is not listed in ''help'''
source_url: https://github.com/xmrig/xmrig/issues/770
author: k0ste
assignees: []
labels:
- bug
created_at: '2018-10-03T07:49:07+00:00'
updated_at: '2018-10-08T18:53:04+00:00'
type: issue
status: closed
closed_at: '2018-10-08T18:53:04+00:00'
---

# Original Description
```
[k0ste@WorkStation bin]$ ./xmrig --version ; ./xmrig --help | grep -i dry
XMRig 2.8.0-rc
 built on Oct  3 2018 with GCC 8.2.1
 features: 64-bit AES

libuv/1.23.1
microhttpd/0.9.59
OpenSSL/1.1.1
[k0ste@WorkStation bin]$ 
```

# Discussion History
## xmrig | 2018-10-08T18:53:04+00:00
Fixed in https://github.com/xmrig/xmrig/commit/dda8157a7bab1317227028da644d1949291f225f and https://github.com/xmrig/xmrig/commit/023062b2f13920410124a94565d04cfc65bee3eb.

# Action History
- Created by: k0ste | 2018-10-03T07:49:07+00:00
- Closed at: 2018-10-08T18:53:04+00:00
