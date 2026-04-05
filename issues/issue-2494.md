---
title: teamredminer hash drops when used in conjunction with xmrig 6.13.1
source_url: https://github.com/xmrig/xmrig/issues/2494
author: Macacul
assignees: []
labels: []
created_at: '2021-07-24T14:18:40+00:00'
updated_at: '2021-07-24T15:29:23+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Hi,
I experience an hash drop (20 - 25%) for teamredminer when I use this version of xmrig (6.13.1) . Can somebody to help me?
Thanx.

# Discussion History
## SChernykh | 2021-07-24T14:40:43+00:00
Set `cpu-priority` to 0 in config.json, or add `--cpu-priority 0` to the command line if you use command line.

## Macacul | 2021-07-24T15:29:22+00:00
thanx, now working good

# Action History
- Created by: Macacul | 2021-07-24T14:18:40+00:00
