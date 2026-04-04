---
title: Rescanning the blockchain deletes outgoing payment info (tx secret keys & destinations)
source_url: https://github.com/monero-project/monero/issues/2177
author: kenshi84
assignees: []
labels: []
created_at: '2017-07-17T01:07:53+00:00'
updated_at: '2017-07-17T15:21:58+00:00'
type: issue
status: closed
closed_at: '2017-07-17T15:21:58+00:00'
---

# Original Description
I was surprised to find out that doing `rescan_bc` deletes all the information about outgoing transfers, including the tx secret keys and the destination addresses. This is because the command triggers `wallet2::rescan_blockchain()` which then triggers `wallet2::clear()` which is currently defined as:
```c++
bool wallet2::clear()
{
  m_blockchain.clear();
  m_transfers.clear();
  m_key_images.clear();
  m_pub_keys.clear();
  m_unconfirmed_txs.clear();    // this deletes the info about pending outgoing transfers
  m_payments.clear();
  m_tx_keys.clear();            // this deletes the tx secret keys
  m_confirmed_txs.clear();      // this deletes the info about outgoing transfers
  m_local_bc_height = 1;
  return true;
}
```
It makes sense to clear other data (blockchain, transfers, key images, pub keys, etc) which can be fully recovered from the blockchain, but deleting those unrecoverable data during `rescan_bc` doesn't make sense to me. Can't we leave them intact during rescanning?

At least there should be a clear warning message to tell the user that some data will be lost by `rescan_bc` (it's the same effect as deleting the wallet cache file).

# Discussion History
## moneromooo-monero | 2017-07-17T10:15:00+00:00
The user is NOT supposed to run rescan_bc unless the wallet is badly screwed up. However, the internet being what it is, it's started being a voodoo step that people will do at first glance of "what should I do now". I thought about keeping things like tx keys etc, but I've not done it so far because it'd encourage running this even more, and since rescan_bc is intended to end up with a *different* state, you'd end up with stale data. In fact, I might even remove rescan_bc altogether.

## kenshi84 | 2017-07-17T15:21:58+00:00
Got it. Closing.

# Action History
- Created by: kenshi84 | 2017-07-17T01:07:53+00:00
- Closed at: 2017-07-17T15:21:58+00:00
