---
title: --max-cpu-usage issue
source_url: https://github.com/xmrig/xmrig/issues/1100
author: martinalebachew
assignees: []
labels:
- question
created_at: '2019-08-05T11:31:50+00:00'
updated_at: '2019-08-05T11:52:08+00:00'
type: issue
status: closed
closed_at: '2019-08-05T11:52:07+00:00'
---

# Original Description
using
`xmrig.exe --url=pool.supportxmr.com:5555 --user=#replaceme1 --pass=#replaceme2 --threads=5 --cpu-priority=5 --max-cpu-usage=80 --donate-level=0%`

but getting
`xmrig.exe: unknown option -- max-cpu-usage=80`

# Discussion History
## klamas1 | 2019-08-05T11:47:48+00:00
Problem probably due --donate-level=0%
;)

## xmrig | 2019-08-05T11:52:07+00:00
Option `--max-cpu-usage` was deprecated and now removed.
Thank you.

# Action History
- Created by: martinalebachew | 2019-08-05T11:31:50+00:00
- Closed at: 2019-08-05T11:52:07+00:00
