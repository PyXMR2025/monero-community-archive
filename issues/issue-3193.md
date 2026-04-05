---
title: 'after building can''t run '
source_url: https://github.com/xmrig/xmrig/issues/3193
author: iexek
assignees: []
labels: []
created_at: '2023-01-08T05:49:42+00:00'
updated_at: '2023-01-08T05:52:21+00:00'
type: issue
status: closed
closed_at: '2023-01-08T05:52:21+00:00'
---

# Original Description
[2023-01-08 08:43:42.250] no valid configuration found, try https://xmrig.com/wizard
I make all config files but can't run. what i need to do?

# Discussion History
## iexek | 2023-01-08T05:52:20+00:00
Solved. I can't run because i just write ./xmrig, solve: ./xmrig -o 127.0.0.1:18081 -a rx/0 -u WALLETADRESS --daemon

# Action History
- Created by: iexek | 2023-01-08T05:49:42+00:00
- Closed at: 2023-01-08T05:52:21+00:00
