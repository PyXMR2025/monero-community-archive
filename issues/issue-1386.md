---
title: xmrig 5.1.1 config “priority” No effect
source_url: https://github.com/xmrig/xmrig/issues/1386
author: alexblock2019
assignees: []
labels:
- bug
created_at: '2019-12-05T07:09:52+00:00'
updated_at: '2020-02-09T10:42:57+00:00'
type: issue
status: closed
closed_at: '2020-02-09T10:42:57+00:00'
---

# Original Description
update xmrig 5.1.1
MSVC/2017 Compile version
windows（7+10） “priority” set 0 and 1 is No effect，maybe bug？

# Discussion History
## xmrig | 2019-12-06T05:41:33+00:00
v5.1.1 sets priority to main miner thread to one level higher that worker threads, example with `"priority": 0,`
![nFraGEI](https://user-images.githubusercontent.com/27528955/70298794-65437e00-1825-11ea-8215-2f70e7668693.png)


## alexblock2019 | 2019-12-06T06:14:31+00:00
> v5.1.1 sets priority to main miner thread to one level higher that worker threads, example with `"priority": 0,`
> ![nFraGEI](https://user-images.githubusercontent.com/27528955/70298794-65437e00-1825-11ea-8215-2f70e7668693.png)

thank！
So only the priority of the main miner thread remain the same, does the worker thread take effect?

## xmrig | 2019-12-06T06:21:22+00:00
For worker threads nothing changed all works exactly same as before.
For main thread used +1 priority, for example if config set `0` main thread use `1`, 1 -> 2, etc.

# Action History
- Created by: alexblock2019 | 2019-12-05T07:09:52+00:00
- Closed at: 2020-02-09T10:42:57+00:00
