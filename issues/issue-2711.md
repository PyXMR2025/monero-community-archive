---
title: Segmentation fault error plz help me
source_url: https://github.com/xmrig/xmrig/issues/2711
author: Sichanak
assignees: []
labels: []
created_at: '2021-11-22T13:11:14+00:00'
updated_at: '2021-11-23T22:16:17+00:00'
type: issue
status: open
closed_at: null
---

# Original Description

![Screenshot_20211122-163656](https://user-images.githubusercontent.com/94844596/142868253-916a1171-53b1-4b24-b9a1-7b95c289f6e1.png)

Did you anybody know what is problem?and help me to fix it 

# Discussion History
## SChernykh | 2021-11-22T13:54:52+00:00
The problems are:
- Not enough memory (RandomX needs 2 GB)
- 32-bit CPU (not supported for RandomX)

## Lonnegan | 2021-11-23T22:16:17+00:00
Try mining something else instead of RandomX, e.g. cn/upx or astrobwt.

# Action History
- Created by: Sichanak | 2021-11-22T13:11:14+00:00
