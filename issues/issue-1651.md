---
title: cost large memory when build on raspberry ubuntu?
source_url: https://github.com/xmrig/xmrig/issues/1651
author: esrrhs
assignees: []
labels:
- arm
created_at: '2020-04-20T11:27:41+00:00'
updated_at: '2020-11-02T17:19:03+00:00'
type: issue
status: closed
closed_at: '2020-11-02T17:19:03+00:00'
---

# Original Description
I found it use a large memory to build RxDataset.cpp, is this normal?

# uname -a
Linux ubuntu 5.3.0-1022-raspi2 #24-Ubuntu SMP Fri Mar 27 21:32:13 UTC 2020 aarch64 aarch64 aarch64 GNU/Linux

# make
[  3%] Built target argon2
[  3%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxDataset.cpp.o

# top
  PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND                                                                                                                                 
 2431 root      20   0 2748644 656504   1484 D  12.9  70.7  17:21.48 cc1plus 

# Discussion History
## xmrig | 2020-11-02T13:02:04+00:00
This issue should be fixed in dev branch https://github.com/xmrig/xmrig/pull/1926
Thank you.

# Action History
- Created by: esrrhs | 2020-04-20T11:27:41+00:00
- Closed at: 2020-11-02T17:19:03+00:00
