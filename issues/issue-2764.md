---
title: Segmentation fault (core dumped)
source_url: https://github.com/xmrig/xmrig/issues/2764
author: felix920506
assignees: []
labels: []
created_at: '2021-11-30T16:35:28+00:00'
updated_at: '2023-02-03T19:55:38+00:00'
type: issue
status: closed
closed_at: '2023-02-03T19:55:38+00:00'
---

# Original Description
**Describe the bug**
Miner ends with error "Segmentation fault (core dumped)" when ran under linux

**To Reproduce**
1. run the miner

**Expected behavior**
the miner should start mining

**Required data**
 - Miner log
![image](https://user-images.githubusercontent.com/25688628/144087393-b4da5019-f0c3-482a-8da6-76f272d13e1b.png)
 - Config file or command line (without wallets)
https://pastebin.com/0qXn3QXy
 - Ubuntu 21.10 Server



# Discussion History
## SChernykh | 2021-11-30T17:36:37+00:00
Fixed in https://github.com/xmrig/xmrig/pull/2751

# Action History
- Created by: felix920506 | 2021-11-30T16:35:28+00:00
- Closed at: 2023-02-03T19:55:38+00:00
