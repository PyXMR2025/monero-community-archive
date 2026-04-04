---
title: Allow increasing default connection timeout from 30 minutes
source_url: https://github.com/monero-project/monero/issues/8835
author: woodser
assignees: []
labels:
- feature
- proposal
created_at: '2023-05-02T20:29:59+00:00'
updated_at: '2023-12-07T21:23:07+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Currently the default connection timeout is [30 minutes](https://github.com/monero-project/monero/blob/a2e8d1d4271df1591786b8d92516455488ee82fd/contrib/epee/include/net/abstract_tcp_server2.inl#L60), so wallets with a longer refresh period will disconnect from the daemon.  This causes the next several requests to the wallet to fail, until it reconnects to the daemon automatically.

This issue requests allowing the default timeout to be overridden, so applications handling many wallets can set a longer refresh period (e.g. 1 hour or 1 day) to minimize resource consumption without the next requests failing.

# Discussion History
# Action History
- Created by: woodser | 2023-05-02T20:29:59+00:00
