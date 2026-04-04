---
title: 'simplewallet: set subaddress-lookahead does not work after wallet creation'
source_url: https://github.com/monero-project/monero/issues/8980
author: benevanoff
assignees: []
labels:
- bug
- in progress
- easy
created_at: '2023-08-31T17:00:14+00:00'
updated_at: '2025-07-10T12:20:55+00:00'
type: issue
status: closed
closed_at: '2025-07-10T12:20:55+00:00'
---

# Original Description
# Description

While attempting to resolve #8954, I first tried to understand fully how it is implemented in the cli since woodser linked to the code snippet where it shows that there are class member variables `m_subaddress_lookahead_major` and `m_subaddress_lookahead_minor` that gets updated and saved to the wallet cache, but this made me realize that the `m_subaddresses` table of `m_wallet` is never actually updated and prompted me to test it, finding that it does not actually make the wallet "look ahead" any further.

# User Impact

Users that have used many subaddresses may not be able to find their e-notes after restoring from their seed when adjusting the lookahead with `set subaddress-lookahead`

# How to Reproduce

1. create a new wallet: `wallet_1`
2. run `set` - this will show the lookahead set to the default, 50:200
3. `set subaddress-lookahead 50:300`
4. run `set` again - this will now show 50:300
5. (optional) close and reopen the wallet then run `set` again to confirm the change has persisted
6. export the wallet seed and create a new wallet by restoring from the seed to create `wallet_2`
7. in `wallet_2`, run `address new` 300 times
8. run `address all`
9. copy one of the subaddresses from the 210-290 range
10. send some moneroj from a different wallet to that address from step 9.
11. wait until the transaction is confirmed
12. open and refresh `wallet_1` and `wallet_2`
13. you will see a new transaction in `wallet_2` but not `wallet_1`
14. run `set` in each wallet one more time to confirm that the subaddress-lookahead should be the same (they will both display 50:300) but they are in fact different, evidenced by the balance difference indicating that `wallet_1`'s subaddress pubkey hashtable has not been properly updated to "lookahead" past the 200th subaddress to the 300th subaddress.

# How to Fix

Modify `wallet2::set_subaddress_lookahead` to actually expand/shrink the `m_subaddresses` class member variable based on the input.

# Discussion History
# Action History
- Created by: benevanoff | 2023-08-31T17:00:14+00:00
- Closed at: 2025-07-10T12:20:55+00:00
