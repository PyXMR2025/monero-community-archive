---
title: 'Solo mining to daemon with cn-heavy/xhv gives job error: "Invalid block template
  received from daemon.'
source_url: https://github.com/xmrig/xmrig/issues/3107
author: downystreet
assignees: []
labels:
- question
- wontfix
created_at: '2022-08-12T21:01:15+00:00'
updated_at: '2022-12-13T14:22:57+00:00'
type: issue
status: closed
closed_at: '2022-12-13T14:22:57+00:00'
---

# Original Description
xmrig version. 6.18.0
Mining algo: cn-heavy/xhv
url: 127.0.0.1:17750
daemon: true

When trying to solo mine xhv/haven with the daemon using these settings I get the error job error: "Invalid block template received from daemon. When I mine using a pool I don't run into this issue and the miner works normally. Only when trying to solo mine do I get this error. 

# Discussion History
## SChernykh | 2022-08-12T21:28:44+00:00
Solo mining is only supported for Monero and Wownero.

## downystreet | 2022-08-12T22:05:15+00:00
Alright, thanks.

# Action History
- Created by: downystreet | 2022-08-12T21:01:15+00:00
- Closed at: 2022-12-13T14:22:57+00:00
