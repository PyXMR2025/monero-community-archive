---
title: 'Exception in main! boost::filesystem::unique_path: Function not implemented'
source_url: https://github.com/monero-project/monero/issues/7630
author: frankwalter1301
assignees: []
labels: []
created_at: '2021-03-24T19:19:14+00:00'
updated_at: '2022-02-19T00:16:52+00:00'
type: issue
status: closed
closed_at: '2022-02-19T00:16:52+00:00'
---

# Original Description

# ./monerod
[1616613392] libunbound[23599:0] error: nettle random(yarrow) cannot initialize, getentropy failed: Function not implemented
2021-03-24 19:16:32.590 W libunbound was not built with threads enabled - crashes may occur
2021-03-24 19:16:32.614 I Monero 'Oxygen Orion' (v0.17.1.9-unknown)
2021-03-24 19:16:32.615 I Initializing cryptonote protocol...
2021-03-24 19:16:32.617 I Cryptonote protocol initialized OK
2021-03-24 19:16:32.625 I Initializing core...
2021-03-24 19:16:32.630 I Loading blockchain from folder /home/root/.bitmonero/lmdb ...
2021-03-24 19:16:32.632 W The blockchain is on a rotating drive: this will be very slow, use an SSD if possible
2021-03-24 19:16:32.696 I Stopping cryptonote protocol...
2021-03-24 19:16:32.703 I Cryptonote protocol stopped successfully
2021-03-24 19:16:32.710 E Exception in main! boost::filesystem::unique_path: Function not implemented


I get this error by simply starting monerod installed from debian bullseye repositories. The machine has an armel architecture and is too underpowered to compile monerod by itself.

# Discussion History
## moneromooo-monero | 2021-03-24T19:34:44+00:00
Do you have a stack trace ? It should log one in the log file if you've built with unwind.

## moneromooo-monero | 2021-03-25T09:25:42+00:00
https://github.com/monero-project/monero/pull/7634 should fix it.

# Action History
- Created by: frankwalter1301 | 2021-03-24T19:19:14+00:00
- Closed at: 2022-02-19T00:16:52+00:00
