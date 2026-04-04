---
title: '"make" again builds even  if  no changes in  source code'
source_url: https://github.com/monero-project/monero/issues/5767
author: yakitorifoodie
assignees: []
labels: []
created_at: '2019-07-20T19:22:20+00:00'
updated_at: '2019-08-19T17:27:45+00:00'
type: issue
status: closed
closed_at: '2019-08-19T17:27:45+00:00'
---

# Original Description
"make" again builds even  if  no changes in  source code. how to avoid it?

# Discussion History
## trasherdk | 2019-07-21T17:20:07+00:00
This is how long time a `make` took on my box:
```
monero-build$ date;make;date
Sun Jul 21 19:15:02 CEST 2019
[  4%] Built target generate_translations_header
[ 11%] Built target libminiupnpc-static
[ 12%] Built target lmdb
[ 13%] Built target easylogging
[ 13%] Built target epee_readline
[ 21%] Built target epee
[ 21%] Built target genversion
[ 21%] Built target obj_version
[ 22%] Built target version
[ 32%] Built target obj_common
[ 43%] Built target obj_cncrypto
[ 43%] Built target cncrypto
[ 44%] Built target common
[ 45%] Built target obj_device
[ 47%] Built target obj_ringct_basic
[ 47%] Built target ringct_basic
[ 50%] Built target blocks
[ 50%] Built target device
[ 50%] Built target obj_ringct
[ 50%] Built target obj_checkpoints
[ 51%] Built target checkpoints
[ 53%] Built target obj_cryptonote_basic
[ 53%] Built target cryptonote_basic
[ 54%] Built target ringct
[ 56%] Built target obj_cryptonote_core
[ 56%] Built target obj_multisig
[ 56%] Built target multisig
[ 58%] Built target obj_blockchain_db
[ 59%] Built target blockchain_db
[ 60%] Built target cryptonote_core
[ 62%] Built target obj_lmdb_lib
[ 62%] Built target lmdb_lib
[ 65%] Built target obj_net
[ 66%] Built target net
[ 67%] Built target obj_mnemonics
[ 68%] Built target mnemonics
[ 70%] Built target obj_rpc
[ 70%] Built target obj_rpc_base
[ 72%] Built target rpc_base
[ 73%] Built target obj_p2p
[ 73%] Built target p2p
[ 74%] Built target obj_cryptonote_protocol
[ 74%] Built target cryptonote_protocol
[ 74%] Built target rpc
[ 75%] Built target obj_daemon_messages
[ 76%] Built target obj_daemon_rpc_server
[ 77%] Built target obj_serialization
[ 77%] Built target serialization
[ 78%] Built target daemon_messages
[ 78%] Built target daemon_rpc_server
[ 81%] Built target obj_wallet
[ 81%] Built target obj_device_trezor
[ 81%] Built target device_trezor
[ 81%] Built target wallet
[ 82%] Built target obj_daemonizer
[ 83%] Built target daemonizer
[ 84%] Built target wallet_rpc_server
[ 86%] Built target simplewallet
[ 87%] Built target gen_multisig
[ 90%] Built target daemon
[ 91%] Built target blockchain_usage
[ 92%] Built target blockchain_blackball
[ 93%] Built target blockchain_export
[ 94%] Built target blockchain_stats
[ 94%] Built target blockchain_ancestry
[ 95%] Built target blockchain_depth
[ 96%] Built target blockchain_prune_known_spent_data
[ 98%] Built target blockchain_import
[100%] Built target blockchain_prune
Sun Jul 21 19:15:04 CEST 2019
```
About 2 seconds.
I didn't do the cmake part first, but I didn't change anything in source.


## moneromooo-monero | 2019-08-19T17:14:41+00:00
What does get rebuilt exactly ? What make command line are you using ?

## yakitorifoodie | 2019-08-19T17:27:45+00:00
i'm no longer working on that. I will be closing it. Sorry.

# Action History
- Created by: yakitorifoodie | 2019-07-20T19:22:20+00:00
- Closed at: 2019-08-19T17:27:45+00:00
