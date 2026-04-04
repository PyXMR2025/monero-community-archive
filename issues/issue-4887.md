---
title: Transaction not found in db when a block is added to blockchain
source_url: https://github.com/monero-project/monero/issues/4887
author: nox956
assignees: []
labels:
- invalid
created_at: '2018-11-22T09:27:19+00:00'
updated_at: '2018-11-22T11:25:09+00:00'
type: issue
status: closed
closed_at: '2018-11-22T11:25:09+00:00'
---

# Original Description
When a block is found on the network it may packed with transaction(s), which is normal, but I notice if a transaction is not added to my node's txpool beforehand, it will take longer time of my node to add the block to blockchain, especially when multiple unknown transactions were added to that block, as you can see in the following log.

```
2018-11-22 08:06:22.020 [P2P2]  INFO    blockchain.db.lmdb[6Csrc/blockchain_db/lmdb/db_lmdb.cpp:2240 transaction with hash dd28158f924181e33ba8c97ce072b54a8510e23a63d11640b07f9302e4171bfb not found in db
2018-11-22 08:06:22.026 [P2P2]  INFO    blockchain.db.lmdb[6Csrc/blockchain_db/lmdb/db_lmdb.cpp:2240 transaction with hash 5805bb24744e67f8975d528631a6cf23f7e8ead05e3b49d878fcf298d0def8cc not found in db
2018-11-22 08:06:22.032 [P2P2]  INFO    blockchain.db.lmdb[6Csrc/blockchain_db/lmdb/db_lmdb.cpp:2240 transaction with hash 462adad0d136680a5a25ecea826ca5ce2b5ad3c5cff73bd0fcef0530c64bf74a not found in db
2018-11-22 08:06:22.038 [P2P2]  INFO    blockchain.db.lmdb[6Csrc/blockchain_db/lmdb/db_lmdb.cpp:2240 transaction with hash a4219d1e6e55a228306fc40e737bb58d6c1b8eae64ac6bcec5e59c31dd5beeb2 not found in db
2018-11-22 08:06:22.044 [P2P2]  INFO    blockchain.db.lmdb[6Csrc/blockchain_db/lmdb/db_lmdb.cpp:2240 transaction with hash ac2b3b30767c44617022e33689d2fbfa9e9015a20064dd8bf557372967788998 not found in db
2018-11-22 08:06:22.050 [P2P2]  INFO    blockchain.db.lmdb[6Csrc/blockchain_db/lmdb/db_lmdb.cpp:2240 transaction with hash 80a46e2cb45bbf3ed75bcc5ec60d71efc973952176fdeba0e219db3e061afba9 not found in db
2018-11-22 08:06:22.058 [P2P2]  INFO    blockchain.db.lmdb[6Csrc/blockchain_db/lmdb/db_lmdb.cpp:2240 transaction with hash 22e716301d1a28047411c64f66837e381009eabbe8b18c711f904f3590453cb3 not found in db
2018-11-22 08:06:22.066 [P2P2]  INFO    blockchain.db.lmdb[6Csrc/blockchain_db/lmdb/db_lmdb.cpp:2240 transaction with hash 98a7c31c440471fe3e48b0d189a37387e729ed0b03d2ceb98e63e46590f9a9b9 not found in db
2018-11-22 08:06:22.071 [P2P2]  INFO    blockchain.db.lmdb[6Csrc/blockchain_db/lmdb/db_lmdb.cpp:2240 transaction with hash 29ed11e599fb6eb55cd225ace0d236e1da2571b532c717f8fc45f3611a10f3a4 not found in db
2018-11-22 08:06:22.079 [P2P2]  INFO    blockchain.db.lmdb[6Csrc/blockchain_db/lmdb/db_lmdb.cpp:2240 transaction with hash eb191a1ef289320e5751a45a638b607a40d2172ae0069120d417011f7a6e5da1 not found in db
2018-11-22 08:06:22.087 [P2P2]  INFO    blockchain.db.lmdb[6Csrc/blockchain_db/lmdb/db_lmdb.cpp:2240 transaction with hash 0a72e216b2a3a6b0dbaa7e252f65fab7ad3febeec924c67ad5d93d429e9e16d7 not found in db
2018-11-22 08:06:22.093 [P2P2]  INFO    blockchain.db.lmdb[6Csrc/blockchain_db/lmdb/db_lmdb.cpp:2240 transaction with hash dd89c3534225072bd621664776fbbe2a94eaee70a124edac9bef9a3e90cb100c not found in db
2018-11-22 08:06:22.099 [P2P2]  INFO    blockchain.db.lmdb[6Csrc/blockchain_db/lmdb/db_lmdb.cpp:2240 transaction with hash e865bbee61a8e478aa4317c1420a8a8541ce1cc5c8cff962a26f6051d7a31d8d not found in db
2018-11-22 08:06:22.107 [P2P2]  INFO    blockchain.db.lmdb[6Csrc/blockchain_db/lmdb/db_lmdb.cpp:2240 transaction with hash 58092a14def759817d5192e35674c3712b5594548110924af023b8d53fa6e7a2 not found in db
2018-11-22 08:06:22.113 [P2P2]  INFO    blockchain.db.lmdb[6Csrc/blockchain_db/lmdb/db_lmdb.cpp:2240 transaction with hash dcd61017ac5e95368d8148da9f822e7bf1e2b499d0cc602e241d0108a0f1f90d not found in db
2018-11-22 08:06:22.119 [P2P2]  INFO    blockchain.db.lmdb[6Csrc/blockchain_db/lmdb/db_lmdb.cpp:2240 transaction with hash 52d22a200b08aa6d273eb0e4478bade2669eb777831d3246f2c405f35e8cb239 not found in db
2018-11-22 08:06:22.133 [P2P2]  INFO    blockchain.db.lmdb[6Csrc/blockchain_db/lmdb/db_lmdb.cpp:2240 transaction with hash 64f7d7dd6eb2830371e20c80c9ba2161ecc2a5463a9ed632ea8990be24351feb not found in db
2018-11-22 08:06:22.141 [P2P2]  INFO    blockchain[6Csrc/cryptonote_core/blockchain.cpp:3538 +++++ BLOCK SUCCESSFULLY ADDED
id:[5C<2c647bf7870916c33f5aa8647e827579751396fecbb8315498ae9158701d5201>
PoW:[4C<211eef3d8cbb2fb86722739687cd6124687a363ec8c840feb3d31d1000000000>
HEIGHT 1710482, difficulty:[5C54414073458
block reward: 3.546387254681(3.543714951817 + 0.002672302864), coinbase_weight: 94, cumulative weight: 112400, 233(0/30)ms
```

I understand it might not be possible to know all transactions, but is there any way that can improve it, like connect to more peers? Because I am running my node on a slower device, when a block is not packed with lots of unknown transactions it works just fine, and I really hope it can keep that way.

Thanks!

# Discussion History
## moneromooo-monero | 2018-11-22T11:20:23+00:00
Yes. The more peers are connected to you, the more likely you are to be told of a tx in time. Of course, if your network connection is very slow, too many peers might actually slow things down in the extreme case. This log doesn't seeo to be missing blocks though.

Anyway, this is a bug tracker. Please don't fill it with non bug or related please.

+invalid


# Action History
- Created by: nox956 | 2018-11-22T09:27:19+00:00
- Closed at: 2018-11-22T11:25:09+00:00
