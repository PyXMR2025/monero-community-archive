---
title: weird wallet behavior on testnet
source_url: https://github.com/monero-project/monero/issues/4374
author: Gingeropolous
assignees: []
labels: []
created_at: '2018-09-13T15:14:39+00:00'
updated_at: '2018-09-14T13:25:21+00:00'
type: issue
status: closed
closed_at: '2018-09-14T13:25:21+00:00'
---

# Original Description
Refresh done, blocks received: 1                                
Untagged accounts:
          Account               Balance      Unlocked balance                 Label
 *       0 9v4vTV        6.500000000000        6.500000000000       Primary account
----------------------------------------------------------------------------------
          Total        6.500000000000        6.500000000000
Currently selected account: [0] Primary account
Tag: (No tag assigned)
Balance: 6.500000000000, unlocked balance: 6.500000000000
Background refresh thread started
Password needed - use the refresh command
[wallet 9v4vTV]: refresh
Starting refresh...
Enter password (output received): 
Refresh done, blocks received: 0                                
Currently selected account: [0] Primary account
Tag: (No tag assigned)
Balance: 6.500000000000, unlocked balance: 6.500000000000
Password needed - use the refresh command
[wallet 9v4vTV]: refresh
Starting refresh...
Enter password (output received): 
Refresh done, blocks received: 0                                
Currently selected account: [0] Primary account
Tag: (No tag assigned)
Balance: 6.500000000000, unlocked balance: 6.500000000000
Password needed - use the refresh command
[wallet 9v4vTV]: refresh
Starting refresh...
Enter password (output received): 
Refresh done, blocks received: 0                                
Currently selected account: [0] Primary account
Tag: (No tag assigned)
Balance: 6.500000000000, unlocked balance: 6.500000000000
Password needed - use the refresh command
[wallet 9v4vTV]: 


so the wallet thinks it has new info so wants a password, but then nothing changes. i'm betting the wallet sees that there's a transaction in the mempool maybe?

# Discussion History
## moneromooo-monero | 2018-09-13T20:49:58+00:00
Yes.

## moneromooo-monero | 2018-09-14T08:27:23+00:00
https://github.com/monero-project/monero/pull/4376

## Gingeropolous | 2018-09-14T13:25:21+00:00
i assume this works because moneromooooooooooooooo

# Action History
- Created by: Gingeropolous | 2018-09-13T15:14:39+00:00
- Closed at: 2018-09-14T13:25:21+00:00
