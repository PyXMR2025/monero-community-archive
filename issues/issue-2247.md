---
title: segmentation fault on openbsd
source_url: https://github.com/xmrig/xmrig/issues/2247
author: swrangsar
assignees: []
labels:
- wontfix
created_at: '2021-04-08T10:05:05+00:00'
updated_at: '2021-04-12T13:29:46+00:00'
type: issue
status: closed
closed_at: '2021-04-12T13:29:46+00:00'
---

# Original Description
managed to compile xmrig on openbsd with -DMAP_POPULATE=0 -DMAP_HUGETLB=0 but as soon as it is run, xmrig seg faults and dumps core

# Discussion History
## SChernykh | 2021-04-08T11:45:24+00:00
XMRig doesn't support OpenBSD, it hasn't been tested there. Even if you manage to compile, it'll likely crash and even if it runs, there's no support for huge pages and thread affinity in OpenBSD which will result in poor performance.

## xmrig | 2021-04-08T16:31:34+00:00
CMake option `-DWITH_SECURE_JIT=ON` might help, but as answered above OpenBSD is not really supported.
Thank you.

# Action History
- Created by: swrangsar | 2021-04-08T10:05:05+00:00
- Closed at: 2021-04-12T13:29:46+00:00
