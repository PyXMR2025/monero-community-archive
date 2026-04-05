---
title: Error while doing make
source_url: https://github.com/xmrig/xmrig/issues/3217
author: Adinfauzan
assignees: []
labels: []
created_at: '2023-02-26T06:17:29+00:00'
updated_at: '2025-06-18T22:46:08+00:00'
type: issue
status: closed
closed_at: '2025-06-18T22:46:08+00:00'
---

# Original Description
![IMG_20230226_130834](https://user-images.githubusercontent.com/94809433/221395405-9d814de4-3d75-457d-8172-fc6b9729012d.jpg)

## Bug Script
I did after cmake and I made this what happened, I did this in termux, I hope this can be resolved soon so that in the future it can be used again.

# Discussion History
## SChernykh | 2023-02-26T08:59:48+00:00
It didn't detect that you're building for ARM. What's the output of `uname -a` command?

You can try to build with `cmake .. -DARM_TARGET=7 -DWITH_HWLOC=OFF`

# Action History
- Created by: Adinfauzan | 2023-02-26T06:17:29+00:00
- Closed at: 2025-06-18T22:46:08+00:00
