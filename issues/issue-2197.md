---
title: Help with multi core
source_url: https://github.com/xmrig/xmrig/issues/2197
author: yanke1311
assignees: []
labels:
- question
created_at: '2021-03-21T02:24:14+00:00'
updated_at: '2021-04-12T13:51:36+00:00'
type: issue
status: closed
closed_at: '2021-04-12T13:51:36+00:00'
---

# Original Description
**Describe the bug**
I set max-threads-hint = 100
and my machine has two cpu-core
but I found that when binary is running , it can only run with one cpu



**Expected behavior**
I need it run with all two cores

**Required data**
 - OS: centos 8

**Additional context**
![图片](https://user-images.githubusercontent.com/23717792/111891677-930b0100-8a2f-11eb-8978-9f59c27b28c2.png)
pic below is total usage, only 50%:
![图片](https://user-images.githubusercontent.com/23717792/111891707-c3eb3600-8a2f-11eb-8f3a-c2f22dbe7e42.png)




# Discussion History
## SChernykh | 2021-03-21T08:49:46+00:00
Most likely your CPU doesn't have enough cache to run 2 mining threads. Also, your machine has less than 2 GB RAM, it can't run RandomX at full speed. Read https://xmrig.com/docs/miner/randomx-optimization-guide for more information.

# Action History
- Created by: yanke1311 | 2021-03-21T02:24:14+00:00
- Closed at: 2021-04-12T13:51:36+00:00
