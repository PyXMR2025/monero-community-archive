---
title: 'rpc wallet: histogram reports no unlocked rct outputs, not even ours'
source_url: https://github.com/monero-project/monero/issues/4904
author: mmorrell
assignees: []
labels: []
created_at: '2018-11-25T21:26:30+00:00'
updated_at: '2018-11-26T15:09:18+00:00'
type: issue
status: closed
closed_at: '2018-11-26T01:31:34+00:00'
---

# Original Description
I'm using a modified `monero-wallet-rpc` with the required confirmations to unlock reduced to 1.

e.g. `#define CRYPTONOTE_DEFAULT_TX_SPENDABLE_AGE             1`

Frequently when I try to call `transfer` using `monero-wallet-rpc` I get the message: "histogram reports no unlocked rct outputs, not even ours".

Is this expected and/or is there a workaround? For now, I am using retry logic. When it eventually succeeds, all the ring members are from the same date, consistently.

# Discussion History
## moneromooo-monero | 2018-11-26T00:29:16+00:00
What commit hashes are you running for both monero-wallet-rpc and monerod ?

Why are you modifying this ? This not only wrecks *your* privacy, but to a lesser extent that of others too. It is irresponsible.


## moneromooo-monero | 2018-11-26T15:09:18+00:00
You found the issue, since you closed this ?

# Action History
- Created by: mmorrell | 2018-11-25T21:26:30+00:00
- Closed at: 2018-11-26T01:31:34+00:00
