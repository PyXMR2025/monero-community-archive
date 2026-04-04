---
title: 'variable ringsize parameter in wallet but ringsize isn''t variable '
source_url: https://github.com/monero-project/monero/issues/4375
author: Gingeropolous
assignees: []
labels:
- invalid
created_at: '2018-09-13T16:06:34+00:00'
updated_at: '2018-10-01T11:24:54+00:00'
type: issue
status: closed
closed_at: '2018-10-01T11:24:54+00:00'
---

# Original Description
Balance: 506.500000000000, unlocked balance: 506.500000000000
[wallet 9v4vTV]: address
0  9v4vTVwqZzfjCFyPi7b9Uv1hHntJxycC4XvRyEscqwtq8aycw5xGpTxFyasurgf2KRBfbdAJY4AVcemL1JCegXU4EZfMtaz  Primary address (used)
[wallet 9v4vTV]: transfer 20 9v4vTVwqZzfjCFyPi7b9Uv1hHntJxycC4XvRyEscqwtq8aycw5xGpTxFyasurgf2KRBfbdAJY4AVcemL1JCegXU4EZfMtaz 40
Wallet password: 
Error: ring size 20 is too large, maximum is 11
[wallet 9v4vTV]: transfer 5 9v4vTVwqZzfjCFyPi7b9Uv1hHntJxycC4XvRyEscqwtq8aycw5xGpTxFyasurgf2KRBfbdAJY4AVcemL1JCegXU4EZfMtaz 40
Wallet password: 
Error: ring size 5 is too small, minimum is 11
[wallet 9v4vTV]: 


# Discussion History
## moneromooo-monero | 2018-09-14T09:00:34+00:00
Actually this is still needed for the case where you're spending pre-rct outputs.

## moneromooo-monero | 2018-10-01T11:22:03+00:00
I'll leave as is since it's needed in pre rct corner cases.

+invalid

# Action History
- Created by: Gingeropolous | 2018-09-13T16:06:34+00:00
- Closed at: 2018-10-01T11:24:54+00:00
