---
title: '[BUG] Somewhat erroneous error message ("Error: Not enough money in overall
  balance")'
source_url: https://github.com/monero-project/monero/issues/2821
author: dEBRUYNE-1
assignees: []
labels: []
created_at: '2017-11-15T14:54:55+00:00'
updated_at: '2017-11-15T18:23:53+00:00'
type: issue
status: closed
closed_at: '2017-11-15T18:23:53+00:00'
---

# Original Description
For information, this occurs when testing moneromooo's `try_tx` (#2800) branch. In my opinion, the error message should refer to the unlocked balance, not to the overall balance, since the overall balance > transfer amount in this scenario. Logs for clarification:

    [wallet 9x7hjA]: balance
    Currently selected account: [0] Primary account
    Balance: 19.980345680000, unlocked balance: 17.000000000000
    [wallet 9x7hjA]: transfer 9tH6XmQnKyAP7CTiAdPa2jHgYGrjsSgmoPHRAu9bGAnbBLpgirq7vbtdZwHaS58DVAgpXRnuFKW7qQgLsqJMJ8CE7CfaMZe 18
    Wallet password: ****
    No payment id is included with this transaction. Is this okay?  (Y/Yes/N/No): Y
    Error: Not enough money in overall balance

EDIT: Master shows a correct error message.

# Discussion History
## dEBRUYNE-1 | 2017-11-15T18:23:53+00:00
According to @moneromooo-monero this is solved in master. Therefore, I am closing this issue. 

# Action History
- Created by: dEBRUYNE-1 | 2017-11-15T14:54:55+00:00
- Closed at: 2017-11-15T18:23:53+00:00
