---
title: Block found, coin missing
source_url: https://github.com/monero-project/monero/issues/2763
author: thawwed
assignees: []
labels: []
created_at: '2017-11-06T00:07:26+00:00'
updated_at: '2017-11-06T01:39:23+00:00'
type: issue
status: closed
closed_at: '2017-11-06T01:39:23+00:00'
---

# Original Description
Block found, transaction shows payment sent to pool wallet, but pool wallet not received anything?  Is something wrong with my wallet-rpc?

My original problem was referenced to Electroneum; however, this is also the same issue with my Monero pool as well.

Blockchain is synced. Daemon is synced. Wallet is synced. Transaction links to wallet in blockexplorer. But still, there's no XMR. What's the deal?

# Discussion History
## moneromooo-monero | 2017-11-06T00:08:24+00:00
And does it happen with current code AND a wallet created with current code ?

## thawwed | 2017-11-06T00:11:05+00:00
Yes. Server was setup yesterday about 24 hours ago to be more precise, and it was setup using git clone. I'm new to linux, so if it sounds like it, it is. Everything functions perfectly until a block is found.

Like I said, transaction matches my pool wallet in the blockexplorer, but no matter how many times I sync the wallet or rebuild it from keys, there is no remnant of the transaction. The wallet works fine too, because I have sent XMR to it no problem from another wallet and received easily.


## moneromooo-monero | 2017-11-06T00:12:22+00:00
Then:
- remove the cache file (FOO if the keys is FOO.keys)
- run the wallet with --log-level 2
- post the log to fpaste.org


## moneromooo-monero | 2017-11-06T00:12:45+00:00
And include the txid of the coinbase you've found.

## thawwed | 2017-11-06T01:39:20+00:00
Problem solved. Had to rebuild wallet using mnemonic seed. Something was bugged with the original. After the rebuild everything processed perfectly.

# Action History
- Created by: thawwed | 2017-11-06T00:07:26+00:00
- Closed at: 2017-11-06T01:39:23+00:00
