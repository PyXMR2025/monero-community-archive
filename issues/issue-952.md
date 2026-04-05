---
title: 'Entry.cpp:52:16: error: ‘printf’ was not declared in this scope'
source_url: https://github.com/xmrig/xmrig/issues/952
author: ghost
assignees: []
labels:
- bug
created_at: '2019-02-26T18:49:57+00:00'
updated_at: '2019-03-06T13:23:43+00:00'
type: issue
status: closed
closed_at: '2019-03-06T13:23:42+00:00'
---

# Original Description
xmrig-2.13.1/src/base/kernel/Entry.cpp: In function ‘int showVersion()’:
xmrig-2.13.1/src/base/kernel/Entry.cpp:52:16: error: ‘printf’ was not declared in this scope
     " with GCC");
                ^
xmrig-2.13.1/src/base/kernel/Entry.cpp: In static member function ‘static int xmrig::Entry::exec(const xmrig::Process&, xmrig::Entry::Id)’:
xmrig-2.13.1/src/base/kernel/Entry.cpp:109:21: error: ‘printf’ was not declared in this scope
         printf(usage);

(this fixed it in my case)

$ diff -C 2 Entry.cpp.1 Entry.cpp
*** Entry.cpp.1 2019-02-25 08:23:59.000000000 -0600
--- Entry.cpp   2019-02-26 12:40:47.798949824 -0600
***************
*** 42,45 ****
--- 42,46 ----
  #include "version.h"

+ #include <stdio.h>

  static int showVersion()

fedora 24 gcc version 6.3.1 20161221 (Red Hat 6.3.1-1) (GCC)


# Discussion History
## marcel1974 | 2019-03-01T05:35:07+00:00
I had to add #include <cstdio> to  src/base/kernel/Entry.cpp
I still need Ubuntu 15.10 support. It was building fine up to xmrig-2.8.3

## xmrig | 2019-03-01T15:24:08+00:00
Fixed in [dev](https://github.com/xmrig/xmrig/commits/dev) branch.
Thank you.

## xmrig | 2019-03-06T13:23:42+00:00
Fixed in v2.14.0 https://github.com/xmrig/xmrig/releases/tag/v2.14.0

# Action History
- Created by: ghost | 2019-02-26T18:49:57+00:00
- Closed at: 2019-03-06T13:23:42+00:00
