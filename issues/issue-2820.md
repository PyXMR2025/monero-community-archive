---
title: '[BUG] "Error: Not enough money in unlocked balance" whilst unlocked balance
  > transfer amount '
source_url: https://github.com/monero-project/monero/issues/2820
author: dEBRUYNE-1
assignees: []
labels: []
created_at: '2017-11-15T14:48:57+00:00'
updated_at: '2017-11-15T18:23:45+00:00'
type: issue
status: closed
closed_at: '2017-11-15T18:23:45+00:00'
---

# Original Description
For information, this occurs when testing moneromooo's `try_tx` (#2800) branch. The transaction sent to the wallet was included in block 1040479. The error occurs when trying to send after 1040489 is mined. It works when trying to send after 1040490 is mined. Logs for clarification:

    [wallet 9x7hjA]: refresh
    Starting refresh...
    Refresh done, blocks received: 0                                
    Currently selected account: [0] Primary account
    Balance: 28.000000000000, unlocked balance: 28.000000000000
    [wallet 9x7hjA]: transfer A3ymYaEGwEgP7CTiAdPa2jHgYGrjsSgmoPHRAu9bGAnbBLpgirq7vbtdZwHaS58DVAgpXRnuFKW7qQgLsqJMJ8CEA59bb7jgJBw6k9fgVj 8
    Wallet password: ****
    Error: Not enough money in unlocked balance
    [wallet 9x7hjA]: transfer A3ymYaEGwEgP7CTiAdPa2jHgYGrjsSgmoPHRAu9bGAnbBLpgirq7vbtdZwHaS58DVAgpXRnuFKW7qQgLsqJMJ8CEA59bb7jgJBw6k9fgVj 8
    Wallet password: ****
    
    Transaction 1/1:
    Spending from address index 0
    Sending 8.000000000000.  The transaction fee is 0.019654320000
    Is this okay?  (Y/Yes/N/No): Y

EDIT: I can't reproduce this on master. 

# Discussion History
## dEBRUYNE-1 | 2017-11-15T18:23:45+00:00
According to @moneromooo-monero this is solved in master. Therefore, I am closing this issue. 

# Action History
- Created by: dEBRUYNE-1 | 2017-11-15T14:48:57+00:00
- Closed at: 2017-11-15T18:23:45+00:00
