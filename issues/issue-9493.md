---
title: Failed to construct transaction
source_url: https://github.com/monero-project/monero/issues/9493
author: SystemVll
assignees: []
labels:
- question
- wallet
created_at: '2024-09-28T14:21:54+00:00'
updated_at: '2025-07-15T14:20:21+00:00'
type: issue
status: closed
closed_at: '2024-09-28T18:13:38+00:00'
---

# Original Description
![image](https://github.com/user-attachments/assets/64bf9e51-3532-4f3b-8181-1fc02965f0c8)

I get an error message when i try to send money, i want to send $300, but it ask me to send smaller amounts,
the max that i can send without seeing this error is $6. Is there an other way instead of sending 50 transaction of $6 ?

# Discussion History
## selsta | 2024-09-28T17:08:58+00:00
Do you have a lot of inputs from mining? If yes, you first have to consolidate your inputs before sending a transaction.

## kevin0t | 2024-09-28T18:05:37+00:00
send your whole balance to your own address or subaddres , (caled a churn transaction) so that you have a single utxo to spend

# Action History
- Created by: SystemVll | 2024-09-28T14:21:54+00:00
- Closed at: 2024-09-28T18:13:38+00:00
