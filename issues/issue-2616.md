---
title: Transaction has too low ring size while mining
source_url: https://github.com/monero-project/monero/issues/2616
author: thaoms
assignees: []
labels:
- invalid
created_at: '2017-10-09T13:53:49+00:00'
updated_at: '2017-10-09T15:00:26+00:00'
type: issue
status: closed
closed_at: '2017-10-09T15:00:26+00:00'
---

# Original Description
Im getting these errors in my logs while running the daemon and mining.

Im pretty new to this so I'm not sure of these are ignorable.

`2017-10-09 13:52:07.720	[P2P4]	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:523	Percent used: 0.4488  Percent threshold: 0.8000
2017-10-09 13:52:07.728	[P2P4]	ERROR	verify	src/cryptonote_core/blockchain.cpp:2475	Tx <fe70cbac14a42069c346350f0c577120ebc81ac5e8185376eedbbed3569512bd> has too low ring size (3), and no unmixable inputs
2017-10-09 13:52:07.729	[P2P4]	ERROR	verify	src/cryptonote_core/blockchain.cpp:2475	Tx <9e6eaa6957e5a144208b64c133052c88d71f7b45b23cbcd6d5d4c176f4c0ad6d> has too low ring size (3), and no unmixable inputs
2017-10-09 13:52:07.729	[P2P4]	ERROR	verify	src/cryptonote_core/blockchain.cpp:2475	Tx <09e153055260108a614c53a136e8ac20c9dc563e724523d2cad0eca0de37d1e7> has too low ring size (3), and no unmixable inputs`

# Discussion History
## SamsungGalaxyPlayer | 2017-10-09T14:12:49+00:00
Are you using the latest 0.11.0.0 Helium Hydra release?

## thaoms | 2017-10-09T14:25:56+00:00
Yes, Monero 'Helium Hydra' (v0.11.0.0-release)


## thaoms | 2017-10-09T14:32:23+00:00
Never mind, fixed it with  'flush_txpool'

## moneromooo-monero | 2017-10-09T14:54:58+00:00
It's telling you why it's not mining them. These logs aren't enabled by default.

+invalid


# Action History
- Created by: thaoms | 2017-10-09T13:53:49+00:00
- Closed at: 2017-10-09T15:00:26+00:00
