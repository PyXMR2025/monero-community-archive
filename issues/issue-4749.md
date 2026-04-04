---
title: Don't silently ignore invalid arguments in monerod.conf
source_url: https://github.com/monero-project/monero/issues/4749
author: jlopp
assignees: []
labels: []
created_at: '2018-10-28T17:41:13+00:00'
updated_at: '2018-10-29T22:03:13+00:00'
type: issue
status: closed
closed_at: '2018-10-29T22:03:13+00:00'
---

# Original Description
I ran into an issue where I was confused about my peer counts because I had set "out-peers=20" in monerod.conf rather than "out_peers=20"

This is a common problem in cryptocurrency nodes; Bitcoin Core only fixed it recently via https://github.com/bitcoin/bitcoin/pull/13112



# Discussion History
## jlopp | 2018-10-29T22:03:13+00:00
Confirmed that monero exits when invalid parameters are in conf file; it was my conf file that was named incorrectly and thus not being read.

# Action History
- Created by: jlopp | 2018-10-28T17:41:13+00:00
- Closed at: 2018-10-29T22:03:13+00:00
