---
title: 'Improvements: Precisely and strict control max-cpu-usage option'
source_url: https://github.com/xmrig/xmrig/issues/381
author: hgs81
assignees: []
labels:
- wontfix
created_at: '2018-02-02T14:13:59+00:00'
updated_at: '2018-11-05T07:11:12+00:00'
type: issue
status: closed
closed_at: '2018-11-05T07:11:12+00:00'
---

# Original Description
Hi, xmrig team!
Thanks for your great effort.
I would like to add this awesome feature.
I found that max-cpu-usage option is only used for thread count calculation.
Is there any way to precisely control maximum CPU usage?
For example, if other processes are using 10% cpu and max-cpu-usage is 50%, then xmrig can be automatically configured to use exactly 40%.
And if current cpu level is 60%, xmrig pauses mining, etc.
So cpu usage could really <= 50%.
Can you control mining algorithm speed or add some sleeps so that it can not exceed desired cpu usage?
Thanks.

# Discussion History
## RansomFuck | 2018-02-12T22:31:06+00:00
Set process priority hight from other process

# Action History
- Created by: hgs81 | 2018-02-02T14:13:59+00:00
- Closed at: 2018-11-05T07:11:12+00:00
