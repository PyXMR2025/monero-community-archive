---
title: '`scan_tx` causes extra transfers with fee=0'
source_url: https://github.com/monero-project/monero/issues/8531
author: woodser
assignees: []
labels: []
created_at: '2022-08-23T13:24:00+00:00'
updated_at: '2024-01-03T05:06:27+00:00'
type: issue
status: closed
closed_at: '2024-01-03T05:06:27+00:00'
---

# Original Description
Calling `scan_txs` with already scanned tx ids causes `get_transfers` to start returning erroneous transfers with fee=0, which causes downstream errors reconciling the information reported from the wallet for libraries / applications.

It's accompanied with this output in monero-wallet-rpc, but this is probably expected:

2022-08-21 13:21:40.823	E Public key fdfa07f837a16a90d733fceb55581c0c0f8c6ba3574ef928738512083c65622a from received 35.173300860152 output already exists with spent 35.173300860152 in tx <ea6c9edae116224a5494e78bbeafc5508cc11734bc8e6e36a9784c6b7dcf160f>, received output ignored

# Discussion History
## j-berman | 2022-09-10T03:06:25+00:00
I'm not seeing how to repro extra transfers with fee=0, but I can repro extra transfers with amount=0 and see what's causing that.

Are you certain the issue is extra transfers with fee=0 and not amount=0?

[This code](https://github.com/j-berman/monero/commit/7db2aa914e252c6a1bd83e80c3accb0d36e40e2a) should prevent the amount=0 issue, though I don't think it's a complete solution as is (and is possibly incorrect still since it re-calls `on_money_received` every `scan_tx` which might cause issues downstream... fwiw I think a complete solution wouldn't re-call `process_new_transaction` with txs that have already been processed).

## selsta | 2024-01-03T05:06:27+00:00
Should be fixed with #8566

# Action History
- Created by: woodser | 2022-08-23T13:24:00+00:00
- Closed at: 2024-01-03T05:06:27+00:00
