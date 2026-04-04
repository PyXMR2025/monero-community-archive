---
title: get_transaction_pool RPC may give too much information in restricted RPC mode
source_url: https://github.com/monero-project/monero/issues/2590
author: moneromooo-monero
assignees: []
labels: []
created_at: '2017-10-06T10:42:21+00:00'
updated_at: '2017-11-14T12:53:18+00:00'
type: issue
status: closed
closed_at: '2017-11-14T12:53:18+00:00'
---

# Original Description
Some things like last_relay_time or relayed might be better off omitted if running in restricted RPC mode.

# Discussion History
# Action History
- Created by: moneromooo-monero | 2017-10-06T10:42:21+00:00
- Closed at: 2017-11-14T12:53:18+00:00
