---
title: Xmrig  Improvements
source_url: https://github.com/xmrig/xmrig/issues/1468
author: sakorc
assignees: []
labels: []
created_at: '2019-12-28T17:22:25+00:00'
updated_at: '2021-04-12T15:06:43+00:00'
type: issue
status: closed
closed_at: '2021-04-12T15:06:43+00:00'
---

# Original Description
Xmrig shows GPU temperature and health but should be added to show CPU temperature as this is also important.
Thank You

# Discussion History
## xmrig | 2019-12-28T19:57:37+00:00
Recent discussion about this https://www.reddit.com/r/MoneroMining/comments/eggny2/add_cpu_temperature_to_xmrig/

## sakorc | 2019-12-28T20:13:31+00:00
If xmrig 5.3 is available cpu temperature, how to enable it in config file?
Using windows 7 / 64 bit

## trasherdk | 2019-12-29T02:11:38+00:00
Not `xmrig 5.3` but [Linux Kernel 5.4](https://itsfoss.com/linux-kernel-5-4/)

## SChernykh | 2019-12-29T09:43:23+00:00
There is no unified interface to get CPU temperatures, this is why programs like CoreTemp/RealTemp exist for Windows and lm-sensors for Linux. It's much much bigger task than it seems, I'm not sure if it's worth it compared to just running CoreTemp/RealTemp alongside XMRig.

## x151973 | 2019-12-30T02:07:49+00:00
Try to use hwinfo64 instead, will effect some hashrate 

# Action History
- Created by: sakorc | 2019-12-28T17:22:25+00:00
- Closed at: 2021-04-12T15:06:43+00:00
