---
title: monero-wallet-rpc lost transaction
source_url: https://github.com/monero-project/monero/issues/7531
author: xinyijun
assignees: []
labels: []
created_at: '2021-03-12T10:25:05+00:00'
updated_at: '2021-04-06T18:23:19+00:00'
type: issue
status: closed
closed_at: '2021-04-06T18:23:19+00:00'
---

# Original Description
it's the same issue as #6297, but this time we lost more than 90 deposit transaction("type": "in"), while last time we only lost 1 transaction.

recently we upgrade our monero-wallet-rpc to v0.17.1.9, and more than 90 of our users reported that their deposits were NOT recorded. we asked some of them for transaction keys and verified that they did deposit to us.

we did following steps to find all the lost transactions:

1. we delete files in ~/.shared-ringdb and the wallet file.
2. we run RPC rescan_blockchain, after rescan, we still lost 57 transactions.
3. we run RPC rescan_blockchain the 2nd time, after rescan, we still lost 20 transactions.
4. we run RPC rescan_blockchain the 3rd time, after rescan, we still lost 6 transactions.
5. we run RPC rescan_blockchain the 4th time, after rescan, we find all lost transactions.

we tried other versions and also found some transactions were lost, we guess this may be related to network between monero-wallet-rpc and node, please help to investigate it, thanks.

# Discussion History
## selsta | 2021-03-15T12:53:43+00:00
Are you running your own node?

## xinyijun | 2021-03-17T10:03:54+00:00
> Are you running your own node?

yes, we run our own node.

## moneromooo-monero | 2021-03-19T21:58:31+00:00
How many in transactions do you have on that wallet, roughly ? It's to get an idea of how often it happens.

## moneromooo-monero | 2021-03-19T22:31:41+00:00
Testing here, I ran rescan_blockchain five times on monero-wallet-rpc, nohting  seems missed. grep "Received money:" in the logs shows 31245 lines, and:

cat build/Linux/crash/release/bin/monero-wallet-rpc.log-* build/Linux/crash/release/bin/monero-wallet-rpc.log | awk '/Calling RPC method rescan_blockchain/{if (C) print C; C=0}/Received money:/{++C}END{print C}'
6249
6249
6249
6249
6249

Also, are there any errors in the wallet or daemon logs corresponding to roughly where the missing transactions are ?

## moneromooo-monero | 2021-04-06T18:23:19+00:00
Resolved offline.

# Action History
- Created by: xinyijun | 2021-03-12T10:25:05+00:00
- Closed at: 2021-04-06T18:23:19+00:00
