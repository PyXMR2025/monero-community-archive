---
title: monerod(1) cannot work with bg
source_url: https://github.com/monero-project/monero/issues/3789
author: papadave66
assignees: []
labels: []
created_at: '2018-05-09T15:25:16+00:00'
updated_at: '2018-05-09T16:05:56+00:00'
type: issue
status: closed
closed_at: '2018-05-09T16:05:56+00:00'
---

# Original Description
and i cannot use ` monerod < /dev/null >> log-file 2>&1 ` because this program thinks i pressed ctrl+d... so what should i do. I think a daemon should not be designed as interactive. isn't it.

# Discussion History
## Low-power | 2018-05-09T15:37:13+00:00
I think this is same issue in #3777

## papadave66 | 2018-05-09T16:05:53+00:00
` --non-interactive ` is cool .you guys can try it

# Action History
- Created by: papadave66 | 2018-05-09T15:25:16+00:00
- Closed at: 2018-05-09T16:05:56+00:00
