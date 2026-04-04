---
title: Blockhain rollback
source_url: https://github.com/monero-project/monero/issues/3669
author: khelle
assignees: []
labels: []
created_at: '2018-04-19T10:24:12+00:00'
updated_at: '2018-04-19T11:34:48+00:00'
type: issue
status: closed
closed_at: '2018-04-19T11:34:48+00:00'
---

# Original Description
When using utility of `monero-blockchain-import --pop-blocks=X` is it needed to clean any additional stuff for wallets data? Or does it clean both full-node and rpc-wallet info? My case is that I received some payments on altchain and hope the rollback will flush wallet info on this invalid payments as well. Will it?

# Discussion History
## moneromooo-monero | 2018-04-19T10:33:38+00:00
It will not by itself. Notice you don't give it any wallet password :)
However, when the wallet refreshes and reorgs from that daemon, it *should* do this. I don't think it's tested a lot with large reorgs, but if it fails you can always delete the cache.

## khelle | 2018-04-19T11:34:48+00:00
So it should reorganize the data itself, but there is possibility to have wrong cache. Ok, thanks for answer. I checked the transfers database and seems the cache has been also cleared. My wallet do not report altchain txs anymore.

# Action History
- Created by: khelle | 2018-04-19T10:24:12+00:00
- Closed at: 2018-04-19T11:34:48+00:00
