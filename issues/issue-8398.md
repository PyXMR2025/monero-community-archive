---
title: '`get_tx_key` should support `raw_monero_tx blob` as input'
source_url: https://github.com/monero-project/monero/issues/8398
author: SamsungGalaxyPlayer
assignees: []
labels: []
created_at: '2022-06-21T18:22:05+00:00'
updated_at: '2022-07-23T06:01:05+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
![image](https://user-images.githubusercontent.com/12520755/174866822-aa166e51-8d1d-4a43-b43f-4e997964d3ad.png)

When using `--do-not-relay` mode for monero-wallet-cli, it exports a raw_monero_tx blog and displays the txid, but not the tx_key. Ideally, `get_tx_key` can support importing the blob to calculate the tx_key.

Current: `get_tx_key <txid>`

Desired: `get_tx_key (<txid> | <raw_monero_tx blob>)`

# Discussion History
## LeoNero | 2022-06-21T18:30:07+00:00
I am down to try to explore and discuss the issue, and tackle it this weekend.

## MexicanTakeout | 2022-07-23T05:58:04+00:00
I don't understand your screenshot example. In that `get_tx_key <txid>` should return the `tx_key`, but we have an error?

# Action History
- Created by: SamsungGalaxyPlayer | 2022-06-21T18:22:05+00:00
