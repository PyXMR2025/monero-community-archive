---
title: 'Monero-wallet-cli: Says mined funds are locked even when they aren’t '
source_url: https://github.com/monero-project/monero/issues/5975
author: SomaticFanatic
assignees: []
labels: []
created_at: '2019-10-10T13:26:16+00:00'
updated_at: '2019-10-11T01:01:18+00:00'
type: issue
status: closed
closed_at: '2019-10-11T01:01:18+00:00'
---

# Original Description
I’m mining on testnet and mined a fair amount of testnet XMR. When I open my wallet after a few days away, monero-wallet-cli will say a loooong list of things like this:

Height 1245678, txid <123456abcde>, 5.175835, idx 0/0
NOTE: This transaction is locked, see details with: show_transfer efghi09876

The issue is that it is saying this for both locked and unlocked mined XMR. So some of the more recently mined XMR is indeed locked for 60 blocks or whatever, but the message also exists for mined XMR thousands of blocks back, which are very much unlocked. 

Is it possible to have the “Note: This transaction is locked” message for only mined XMR that is actually locked?

# Discussion History
## moneromooo-monero | 2019-10-10T16:37:21+00:00
They're locked at the time. The message should probably be removed for coinbase txes though.

## SomaticFanatic | 2019-10-10T18:10:20+00:00
Right. Locked at the time. But logging into my wallet after many days away displays the message even though the funds have long been unlocked. Or maybe I’m not understanding something.

## moneromooo-monero | 2019-10-10T18:13:01+00:00
Yes, that it's saying that at the time its blockchain hasn't progressed past the block the tx is in.

## moneromooo-monero | 2019-10-10T18:32:54+00:00
https://github.com/monero-project/monero/pull/5977

# Action History
- Created by: SomaticFanatic | 2019-10-10T13:26:16+00:00
- Closed at: 2019-10-11T01:01:18+00:00
