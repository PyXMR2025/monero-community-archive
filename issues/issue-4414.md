---
title: '[Bug][Linux] Monerod built from monero-gui repo do not work'
source_url: https://github.com/monero-project/monero-gui/issues/4414
author: not-a-money-printer
assignees: []
labels: []
created_at: '2025-02-24T13:52:23+00:00'
updated_at: '2025-02-24T18:08:12+00:00'
type: issue
status: closed
closed_at: '2025-02-24T18:08:12+00:00'
---

# Original Description
The monerod binary built from monero-gui repo using docker method do not work, after start it just stuck indefinitely at reading blockchain. Only the monerod binary from main repo is working

2025-02-24 13:18:41.290	I Monero 'Fluorine Fermi' (v0.18.3.4-release)
2025-02-24 13:18:41.290	I Initializing cryptonote protocol...
2025-02-24 13:18:41.290	I Cryptonote protocol initialized OK
2025-02-24 13:18:41.290	I Initializing core...
2025-02-24 13:18:41.291	I Loading blockchain from folder /home/user/.bitmonero/lmdb ...   <--- Stuck at here

# Discussion History
## selsta | 2025-02-24T13:53:46+00:00
Did you build it using the Dockerfile? If yes, this is known and the dockerfile is only for building monero-wallet-gui. I will add a note to the README.

## not-a-money-printer | 2025-02-24T14:22:52+00:00
Yes I build using dockerfile, please do add a note to readme

## selsta | 2025-02-24T15:11:58+00:00
#4415

# Action History
- Created by: not-a-money-printer | 2025-02-24T13:52:23+00:00
- Closed at: 2025-02-24T18:08:12+00:00
