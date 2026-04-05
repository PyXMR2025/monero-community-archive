---
title: Even Odd NUMA affinity?
source_url: https://github.com/xmrig/xmrig/issues/191
author: dwright1542
assignees: []
labels:
- NUMA
created_at: '2017-11-08T02:30:49+00:00'
updated_at: '2019-08-02T12:38:30+00:00'
type: issue
status: closed
closed_at: '2019-08-02T12:38:30+00:00'
---

# Original Description
How to specify even and odd CPU's in Linux to xmrig? It's easy when it's 0-11 and 12-23. These are 0,2,4,6,8,10,12,14,16,18,20,22 and 1,3,5,7,9,11,13,15,17,19,21,23... Opteron 6238 CPU's.

# Discussion History
## xmrig | 2017-11-10T02:49:31+00:00
`0,2,4,6,8,10,12,14,16,18,20,22` `0x555555` https://i.imgur.com/XyChITh.png
`1,3,5,7,9,11,13,15,17,19,21,23` `0xAAAAAA`

if you use config file value should in quotes as string `"0x555555"` or as number in decimal form.
Not sure it will work correctly with NUMA nodes, still have issues with it, check roadmap #106
Thank you.

## xmrig | 2019-07-29T02:19:14+00:00
If this issue still actual, please check v2.99.2-beta release #1077.
Thank you.

# Action History
- Created by: dwright1542 | 2017-11-08T02:30:49+00:00
- Closed at: 2019-08-02T12:38:30+00:00
