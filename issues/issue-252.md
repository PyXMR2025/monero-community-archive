---
title: 'wallet-rpc: clarify get_transfers "pending"'
source_url: https://github.com/monero-project/monero-docs/issues/252
author: plowsof
assignees: []
labels: []
created_at: '2025-12-22T03:40:17+00:00'
updated_at: '2025-12-22T05:54:54+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
pending seems to be for displaying unconfirmed `outgoing` transactions. not incoming. get_transfers will display transactions with < 10 confs if pending is set to false.

https://github.com/monero-project/monero/issues/8140#issuecomment-3680262886

i have not sanity checked this by sending get_transfer calls with various combinations to confirm (out:true with pending:true and false while watching what is displayed as the confirmations creep up)

confirmed pending:true / false has no effect on incoming tx's with N confirmations

# Discussion History
## nahuhh | 2025-12-22T05:47:48+00:00
Sounds correct. I think pending and failed are for outgoing-only.

Not sure how `pool` behaves, whether its the entire pool, or if its unconfirmed txs destined fir the wallet


## plowsof | 2025-12-22T05:54:54+00:00
Pool only shows the txs belonging to the wallet with "in" true, ive not tested any out txs though

# Action History
- Created by: plowsof | 2025-12-22T03:40:17+00:00
