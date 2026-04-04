---
title: Regression in Monero daemon RPC interface
source_url: https://github.com/monero-project/monero/issues/6258
author: bartMarinissen
assignees: []
labels: []
created_at: '2019-12-20T13:09:00+00:00'
updated_at: '2020-05-16T16:02:00+00:00'
type: issue
status: closed
closed_at: '2020-05-16T16:01:59+00:00'
---

# Original Description
The following pull request: https://github.com/monero-project/monero/pull/5964/ Introduced a regression into the RPC interface of the Monero daemon.

Specifically, after this commit the get_block command now returns an empty string in the root field .miner_tx_hash in the response. The same data can still be found at .block_header.miner_tx_hash, but this was an interface change. I've since fixed my import scripts to handle this.

# Discussion History
## moneromooo-monero | 2019-12-20T14:24:55+00:00
https://github.com/monero-project/monero/pull/6259 should fix it.

## moneromooo-monero | 2020-05-16T16:01:59+00:00
Fixed

# Action History
- Created by: bartMarinissen | 2019-12-20T13:09:00+00:00
- Closed at: 2020-05-16T16:01:59+00:00
