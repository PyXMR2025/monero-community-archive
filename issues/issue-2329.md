---
title: Xmrig kepping runnig
source_url: https://github.com/xmrig/xmrig/issues/2329
author: Lordcreos
assignees: []
labels: []
created_at: '2021-04-29T16:17:01+00:00'
updated_at: '2021-05-03T01:46:51+00:00'
type: issue
status: closed
closed_at: '2021-05-03T01:46:51+00:00'
---

# Original Description
I have a
this using xmrig
to mine on a vps
but when I close  putty the process is finished
there is some way to fix that problem?

# Discussion History
## SChernykh | 2021-04-29T16:25:07+00:00
`"background": true,` in config.json or add `-B` to the command line if you use command line.

## gamethrower | 2021-04-29T16:47:47+00:00
I wonder what hosting allows mining on VPS.

# Action History
- Created by: Lordcreos | 2021-04-29T16:17:01+00:00
- Closed at: 2021-05-03T01:46:51+00:00
