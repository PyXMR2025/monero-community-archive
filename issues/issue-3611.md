---
title: Index out of bounds of hashchain
source_url: https://github.com/monero-project/monero/issues/3611
author: mmitech
assignees: []
labels: []
created_at: '2018-04-11T18:50:06+00:00'
updated_at: '2018-04-28T13:33:14+00:00'
type: issue
status: closed
closed_at: '2018-04-28T13:33:14+00:00'
---

# Original Description
I am trying to sync Monero and get it to work for the last couple of days, I checked up the journalctl today and found this:

```
Apr 11 18:44:27 monero-wallet-rpc[28083]: 2018-04-11 18:44:27.433            7fb59ec25740        ERROR        wallet.wallet2        src/wallet/wallet2.cpp:2288        pull_blocks failed, try_count=3
Apr 11 18:44:27 monero-wallet-rpc[28083]: 2018-04-11 18:44:27.433            7fb59ec25740        ERROR        wallet.rpc        src/wallet/wallet_rpc_server.cpp:2990        Wallet initialization failed: Index out of bounds of hashchain
```
Wallet rpc would crash after this. (v0.12.0.0-master-release)

# Discussion History
## moneromooo-monero | 2018-04-12T06:07:26+00:00
This can happen if the wallet tries to reorg past a checkpoint, which should never happen, except if you've been on a fork for quite a long time and it only resolved then. Was this the case ?


## mmitech | 2018-04-12T06:25:38+00:00
I have no idea if this was the case, it could be possible since I am doing this on testnet and it seems like chaos there.



## moneromooo-monero | 2018-04-12T07:46:37+00:00
Do you still have a wallet+cache showing this happening ?

## moneromooo-monero | 2018-04-28T11:43:37+00:00
Probably fixed in https://github.com/monero-project/monero/pull/3716/commits/9875f126bde384123458e9967a58652caf4dd437


## mmitech | 2018-04-28T13:33:14+00:00
Thanks, It is working now, I wanted to update you on the issue right away, but for the life of me, I can't remember what I did.

# Action History
- Created by: mmitech | 2018-04-11T18:50:06+00:00
- Closed at: 2018-04-28T13:33:14+00:00
