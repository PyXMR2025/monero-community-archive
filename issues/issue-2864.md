---
title: 'Terminal quits without any '
source_url: https://github.com/xmrig/xmrig/issues/2864
author: ktalebian
assignees: []
labels: []
created_at: '2022-01-15T00:49:50+00:00'
updated_at: '2023-08-04T22:56:50+00:00'
type: issue
status: closed
closed_at: '2023-08-04T22:56:50+00:00'
---

# Original Description
**Describe the bug**
When I try to run the application, I get the following:

```
Last login: Fri Jan 14 16:45:43 on ttys001
/Applications/xmrig/xmrig ; exit;

~ 
➜ /Applications/xmrig/xmrig ; exit;
 * ABOUT        XMRig/6.16.2 clang/10.0.0
 * LIBS         libuv/1.41.0 OpenSSL/1.1.1k hwloc/2.5.0
 * HUGE PAGES   supported
 * 1GB PAGES    unavailable
 * CPU          Intel(R) Core(TM) i7-9750H CPU @ 2.60GHz (1) 64-bit AES
                L2:1.5 MB L3:12.0 MB 6C/12T NUMA:1
 * MEMORY       13.5/16.0 GB (85%)
[1]    27630 killed     /Applications/xmrig/xmrig
Saving session...completed.

[Process completed]
```

Nothing else is explained - I have no idea why this is not working. Help is appreciated.


# Discussion History
## SChernykh | 2022-01-15T17:17:03+00:00
`MEMORY       13.5/16.0 GB (85%)`
Maybe you don't have enough free memory and system's OOM killer terminates XMRig because of that.

## UnixCro | 2022-01-28T12:50:08+00:00
Duplicate of https://github.com/xmrig/xmrig/issues/2421
Thank you

# Action History
- Created by: ktalebian | 2022-01-15T00:49:50+00:00
- Closed at: 2023-08-04T22:56:50+00:00
