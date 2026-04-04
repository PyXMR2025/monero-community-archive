---
title: Accounts and seeds
source_url: https://github.com/monero-project/monero/issues/8160
author: ghost
assignees: []
labels: []
created_at: '2022-01-27T17:17:51+00:00'
updated_at: '2022-02-01T19:26:00+00:00'
type: issue
status: closed
closed_at: '2022-02-01T19:26:00+00:00'
---

# Original Description
Sorry for the beginner question but if I generate a new account for the monero-wallet-cli does that mean i have to make a new backup everytime of the seed? I noticed that recovering from my seed only recovers the first account in the wallet. 
Would apriciate any input

# Discussion History
## ndorf | 2022-01-28T17:58:05+00:00
No, all of the accounts and subaddresses in the same wallet are derived from the same seed. You only need the one.

Have you ever received any transactions to the second (or subsequent) accounts? If not, they won't show up when you restore, but your wallet still controls them. If you then make a "new" account it will be the same one as you had before.

Note, however, that any labels you set on the account won't be preserved if you restore from the seed. If you need those, you would have to back up the actual wallet files. This also applies to certain other metadata, for example the destination address of any transactions you've sent.

# Action History
- Created by: ghost | 2022-01-27T17:17:51+00:00
- Closed at: 2022-02-01T19:26:00+00:00
