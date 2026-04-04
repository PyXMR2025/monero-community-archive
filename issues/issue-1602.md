---
title: 'Daemon: Already mined tx still present in mempool'
source_url: https://github.com/monero-project/monero/issues/1602
author: iDunk5400
assignees: []
labels: []
created_at: '2017-01-21T16:02:35+00:00'
updated_at: '2017-04-10T22:08:20+00:00'
type: issue
status: closed
closed_at: '2017-04-10T22:08:20+00:00'
---

# Original Description
I noticed that there is a transaction in my daemon's mempool which has already been mined. It appears like this in the output of `print_pool_sh`:
```
id: 884527f07ee3d67489dc3834eda4357d80f4ec370c31f3a61d4338593b61076a
blob_size: 1073
fee: 0.010000000000
receive_time: 1484965490 (12 hours ago)
relayed: 1484994370 (4 hours ago)
do_not_relay: F
kept_by_block: F
max_used_block_height: 1228288
max_used_block_id: 13f56ff9d221be2543502063be4640d8f1fc5ba056b93f0786b85ea350d253d9
last_failed_height: 0
last_failed_id: 0000000000000000000000000000000000000000000000000000000000000000
```

However, the transaction appears to be mined as shown on this block explorer:
[Block view](https://xmrchain.net/block/1228346)
[Tx view](https://xmrchain.net/search?value=884527f07ee3d67489dc3834eda4357d80f4ec370c31f3a61d4338593b61076a)

My daemon was 71ac698 at the time the tx was received, 39aaea8 presently.


# Discussion History
## iDunk5400 | 2017-01-22T09:05:20+00:00
The transaction is not in my daemon's mempool any more. It appears to have been dropped after ~24 hours in the mempool.

## moneromooo-monero | 2017-03-25T16:48:49+00:00
Might be fixed by https://github.com/monero-project/monero/pull/1911/commits/aaeb164cf6fa5ff4c8631dd77e434c3259d6b14e if you had killed your dameon (and thus it hadn't saved the txpool). If not, then not :)

# Action History
- Created by: iDunk5400 | 2017-01-21T16:02:35+00:00
- Closed at: 2017-04-10T22:08:20+00:00
