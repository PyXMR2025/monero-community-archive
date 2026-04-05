---
title: No build instructions for Clear Linux
source_url: https://github.com/xmrig/xmrig/issues/3101
author: Proulx-S
assignees: []
labels: []
created_at: '2022-07-29T20:44:42+00:00'
updated_at: '2022-07-29T20:44:52+00:00'
type: issue
status: closed
closed_at: '2022-07-29T20:44:52+00:00'
---

# Original Description
This seems to work, i.e. it built on my Clear Linux Server v36700:
```
1. sudo swupd bundle-add c-basic devpkg-libuv devpkg-openssl hwloc devpkg-hwloc # not sure if hwloc is needed
2. git clone https://github.com/xmrig/xmrig.git
3. mkdir xmrig/build && cd xmrig/build
4. cmake ..
5. make -j$(nproc)
```
Note that only the first step is different from the build instructions for Ubuntu.
Note that the MSR thing was not working (but I did not even try to debug it).

# Discussion History
# Action History
- Created by: Proulx-S | 2022-07-29T20:44:42+00:00
- Closed at: 2022-07-29T20:44:52+00:00
