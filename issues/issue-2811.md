---
title: '[Windows, 6.16.2] Pause-on-active doesn''t work without console output'
source_url: https://github.com/xmrig/xmrig/issues/2811
author: electroape
assignees: []
labels: []
created_at: '2021-12-15T10:38:37+00:00'
updated_at: '2021-12-15T15:48:40+00:00'
type: issue
status: closed
closed_at: '2021-12-15T15:48:40+00:00'
---

# Original Description
On Windows, pause-on-active doesn't work (doesn't pause on machine activity) when miner is launched from 'NT Authority/SYSTEM' account, i.e either as a service or from task scheduler using system account as a task starter.

# Discussion History
## electroape | 2021-12-15T10:40:57+00:00
* or as 'NT Authority/LOCAL SERVICE' or '.../NETWORK SERVICE' either.

## electroape | 2021-12-15T10:53:44+00:00
Disregard that, it doesn't work when there's no console window. I.e if "background" is enabled or it's ran as service or task.

## Spudz76 | 2021-12-15T15:11:08+00:00
The [function being used just doesn't work then](https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-getlastinputinfo#remarks) and there is no fixing it, by design, thanks Windows.

## electroape | 2021-12-15T15:48:37+00:00
> The [function being used just doesn't work then](https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-getlastinputinfo#remarks) and there is no fixing it, by design, thanks Windows.

Neat ... thanks Windows indeed.

# Action History
- Created by: electroape | 2021-12-15T10:38:37+00:00
- Closed at: 2021-12-15T15:48:40+00:00
