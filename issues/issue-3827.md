---
title: Not mined transaction is still in mempool after 7 days
source_url: https://github.com/monero-project/monero/issues/3827
author: Atrides
assignees: []
labels: []
created_at: '2018-05-17T23:18:01+00:00'
updated_at: '2022-07-20T20:36:52+00:00'
type: issue
status: closed
closed_at: '2022-07-20T20:36:52+00:00'
---

# Original Description
Funds in old wallet blocked due to "double spend"
```
[wallet 4xxxx]: sweep_all 8 XXXXXXXXXXXXXXXXXX
Wallet password: 
No payment id is included with this transaction. Is this okay?  (Y/Yes/N/No): Y

Transaction 1/1:
Spending from address index 0
Sweeping XXXXXX for a total fee of XXXXXXX.  Is this okay?  (Y/Yes/N/No): Y

Error: transaction <c6dad4c7f40853ede950d6151951b58582777fb00c5e19ff0f568cb183fc776c> was rejected by daemon with status: Failed
Error: Reason: double spend
```
This old wallet not used already 10 days, last successful transaction was 12 days ago.
The old transaction was not mined, after 12 days is still in mempool of all daemons and blocks inputs:
```
print_tx 40277f035540a63de2e7fe664fb60b2147b5513a902f6b15d16e3794ed234945
Found in pool
```


# Discussion History
## moneromooo-monero | 2018-05-18T07:08:37+00:00
In monerod, type: print_pool_sh
Then paste the entry relating to that particular tx.

## Atrides | 2018-05-18T09:02:57+00:00
Here is receive time 20 hours ago, but transaction was send on "2018-05-05 02:40:08"
```
id: 40277f035540a63de2e7fe664fb60b2147b5513a902f6b15d16e3794ed234945
blob_size: 44719
fee: 0.032882080000
fee/byte: 0.000000735304
receive_time: 1526561040 (20 hours ago)
relayed: 1526633968 (30 seconds ago)
do_not_relay: F
kept_by_block: T
double_spend_seen: T
max_used_block_height: 0
max_used_block_id: 0000000000000000000000000000000000000000000000000000000000000000
last_failed_height: 0
last_failed_id: 0000000000000000000000000000000000000000000000000000000000000000
```

## moneromooo-monero | 2018-05-18T10:57:53+00:00
Looks like a peer is resending them after the "don't resend" period. So to avoid this we might need to keep track of all txes we dropped and never accept them again.

## moneromooo-monero | 2018-10-09T11:39:41+00:00
That's not it: some other node found a block with this tx in (kept_by_block: T), and your node rejected that block, but kept its txes in reserve.

## Cactii1 | 2022-07-20T20:34:29+00:00
Abandoned support request - propose to close.

## selsta | 2022-07-20T20:36:52+00:00
If this issue happens again please comment or open a new issue.

# Action History
- Created by: Atrides | 2018-05-17T23:18:01+00:00
- Closed at: 2022-07-20T20:36:52+00:00
