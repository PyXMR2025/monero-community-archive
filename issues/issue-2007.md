---
title: Please show payment ID when signing and broadcasting transactions
source_url: https://github.com/monero-project/monero/issues/2007
author: moneronoob
assignees: []
labels: []
created_at: '2017-04-26T00:28:43+00:00'
updated_at: '2017-08-07T18:06:17+00:00'
type: issue
status: closed
closed_at: '2017-08-07T18:06:17+00:00'
---

# Original Description
I use this process when using a cold wallet to sign transactions:

https://monero.stackexchange.com/questions/2160/how-do-i-use-cold-transaction-signing

Before signing or broadcasting a transaction, it tells you the amount being spent, the fee, the recipient address, the change amount, and  the change address, and then it asks you to verify it. It would be extremely nice if it also showed the payment ID as well, so that you can verify that too and make sure you haven't made any silly mistakes.

# Discussion History
## moneromooo-monero | 2017-07-24T12:14:16+00:00
https://github.com/monero-project/monero/pull/2196 does this, though encrypted payment ids are just shown to be present, as they can't be decrypted. This is something which could be improved later.

## moneromooo-monero | 2017-08-07T17:41:13+00:00
Encrypted payment ids are now shown also.

+resolved

# Action History
- Created by: moneronoob | 2017-04-26T00:28:43+00:00
- Closed at: 2017-08-07T18:06:17+00:00
