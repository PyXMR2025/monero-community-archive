---
title: --restricted-rpc does not allow transfer (testnet)
source_url: https://github.com/monero-project/monero/issues/3484
author: m2049r
assignees: []
labels: []
created_at: '2018-03-23T07:05:01+00:00'
updated_at: '2018-03-24T09:45:42+00:00'
type: issue
status: closed
closed_at: '2018-03-24T09:45:42+00:00'
---

# Original Description
when running ```monerod --restricted-rpc```, ```monero-wallet-cli``` can sync but not transfer.
```
[wallet A2WSSD]: transfer A2RJ1VpwWJ37sGzLSph1YGfTkBgxuy4dHepMum6vL8zNQBAtU8NLYawNWJZVeSDoNaj4ngNWMjLYj1aUcD25Jrt95p8keZX 0.5
Wallet password: 
No payment id is included with this transaction. Is this okay?  (Y/Yes/N/No): y
Error: no connection to daemon. Please make sure daemon is running.
Error: There was an error, which could mean the node may be trying to get you to retry creating a transaction, and zero in on which outputs you own. Or it could be a bona fide error. It may be prudent to disconnect from this node, and not try to send a tranasction immediately. Alternatively, connect to another node so the original node cannot correlate information.
[wallet A2WSSD]: 
```

when running without ```--restricted-rpc```, transfer works just fine.

# Discussion History
## Admiral-Noisy-Bottom | 2018-03-23T07:43:40+00:00
My reading of the --restriced-rpc is that it allows read-only access. Transfer would be a read-write I would have thought. I could be wrong, I'm kind of new to Monero.

## moneromooo-monero | 2018-03-23T10:45:58+00:00
That's the new output distribution RPC which is fairly heavy, and needed for the mitigations.

## Lafudoci | 2018-03-23T10:56:46+00:00
@moneromooo-monero  So how can I safely provide public node for others without `--restricted-rpc` ?

## moneromooo-monero | 2018-03-23T11:05:01+00:00
https://github.com/monero-project/monero/pull/3486

## moneromooo-monero | 2018-03-23T11:05:22+00:00
It was not intended, see above patch which fixes it.

## m2049r | 2018-03-24T09:45:42+00:00
confirmed.

# Action History
- Created by: m2049r | 2018-03-23T07:05:01+00:00
- Closed at: 2018-03-24T09:45:42+00:00
