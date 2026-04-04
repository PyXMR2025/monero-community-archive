---
title: get_transfer_by_txid response missing destinations field
source_url: https://github.com/monero-project/monero/issues/5992
author: tmoravec
assignees: []
labels: []
created_at: '2019-10-16T14:05:40+00:00'
updated_at: '2019-11-14T07:15:47+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
The response of `get_transfer_by_txid` wallet call is missing the `destinations` field. Additionally, it contains one duplicate field: `subaddr_index` and `subaddr_indices` which appear to be the same.

I can try to fix this. `incoming_transfers` gets the destinations right, so the information should be already present in the wallet.

# Discussion History
## xiphon | 2019-11-11T14:03:31+00:00
> The response of `get_transfer_by_txid` wallet call is missing the `destinations` field.

The wallet provides `destinations` only for outgoing transfers. Use `amount` and `address` for incoming payments.

> Additionally, it contains one duplicate field: `subaddr_index` and `subaddr_indices` which appear to be the same.

`subaddr_indices` contains extended information, e.g. when you spend multiple outputs from different subaddresses.

## tmoravec | 2019-11-14T07:15:16+00:00
> The wallet provides `destinations` only for outgoing transfers. Use `amount` and `address` for incoming payments.

Yes, that's how it is implemented currently. It has several problems, though:

1. It's inconsistent between outgoing and incoming transfers.
2. It's not in line with the documentation.
3. The information is available in the wallet anyway.

These three points lead me to believe this is a bug that _could_ be fixed. Note that I'm not trying to put more work on anyone's plate and offer to fix this together with https://github.com/monero-project/monero/issues/5993 which I need to do anyway.

# Action History
- Created by: tmoravec | 2019-10-16T14:05:40+00:00
