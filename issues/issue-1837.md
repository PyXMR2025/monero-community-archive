---
title: 6.3.3 low hashrate i7-4770
source_url: https://github.com/xmrig/xmrig/issues/1837
author: jututt
assignees: []
labels: []
created_at: '2020-09-16T09:48:10+00:00'
updated_at: '2020-09-16T11:47:04+00:00'
type: issue
status: closed
closed_at: '2020-09-16T11:47:04+00:00'
---

# Original Description
On latest 6.3.3 I'm getting around 1250 H/s with cpu frequency locked at 2500 MHz.
With 6.3.1 I was getting around 1700 H/s at the same 2500 Mhz frequency.
BTW I'm also around 3° C down on temperature CPU Core / Package.
![1](https://user-images.githubusercontent.com/29811680/93321386-62dd6e00-f812-11ea-926e-9d6f07b8b773.png)


# Discussion History
## SChernykh | 2020-09-16T11:16:06+00:00
`huge pages 0% 0/1168` is the reason. Try starting xmrig right after reboot.

## jututt | 2020-09-16T11:47:04+00:00
Thank you, a simple reboot solved my issue

# Action History
- Created by: jututt | 2020-09-16T09:48:10+00:00
- Closed at: 2020-09-16T11:47:04+00:00
