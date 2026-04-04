---
title: '2023-08-03 16:24:08.046 9972 INFO global src/daemon/main.cpp:296 Monero ''Fluorine
  Fermi'' (v0.18.2.2-release) 2023-08-03 16:24:11.144 9972 ERROR msgwriter src/common/scoped_message_writer.h:102
  Error: Couldn''t connect to daemon: 127.0.0.1:18081'
source_url: https://github.com/monero-project/monero-gui/issues/4204
author: diamondsteel259
assignees: []
labels: []
created_at: '2023-08-03T16:48:24+00:00'
updated_at: '2023-08-03T17:32:36+00:00'
type: issue
status: closed
closed_at: '2023-08-03T17:32:36+00:00'
---

# Original Description
Hi @selsta im currently exercising the same problem however im not running 2 wallets i simply opened up xmrig while the blockchain was downloading on the GUI. I'm still quite new at all of this but when i closed my GUI and opened xmrig and let that run for a while my pc shut off due to power outages in my sh1t country south africa. When i powered it on again and opened everything up daemon wouldnt connect and all i got from log was.

2023-08-03 16:24:08.046 9972 INFO global src/daemon/main.cpp:296 Monero 'Fluorine Fermi' (v0.18.2.2-release)
2023-08-03 16:24:11.144 9972 ERROR msgwriter src/common/scoped_message_writer.h:102 Error: Couldn't connect to daemon: 127.0.0.1:18081
2023-08-03 16:24:14.212 2280 INFO logging contrib/epee/src/mlog.cpp:273 New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
2023-08-03 16:24:14.212 2280 INFO global src/daemon/main.cpp:296 Monero 'Fluorine Fermi' (v0.18.2.2-release)
2023-08-03 16:24:17.031 2280 ERROR msgwriter src/common/scoped_message_writer.h:102 Error: Couldn't connect to daemon: 127.0.0.1:18081
2023-08-03 16:28:35.666 10740 INFO logging contrib/epee/src/mlog.cpp:273 New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
2023-08-03 16:28:35.666 10740 INFO global src/daemon/main.cpp:296 Monero 'Fluorine Fermi' (v0.18.2.2-release)
2023-08-03 16:28:35.666 10740 INFO global src/daemon/protocol.h:53 Initializing cryptonote protocol...
2023-08-03 16:28:35.666 10740 INFO global src/daemon/protocol.h:58 Cryptonote protocol initialized OK
2023-08-03 16:28:35.666 10740 INFO global src/daemon/core.h:64 Initializing core...
2023-08-03 16:28:35.666 10740 INFO global src/cryptonote_core/cryptonote_core.cpp:523 Loading blockchain from folder C:\Program Files\Monero GUI Wallet\p2pool\lmdb ...
2023-08-03 16:28:35.728 10740 WARNING blockchain.db.lmdb src/blockchain_db/lmdb/db_lmdb.cpp:75 Failed to open db handle for m_blocks : MDB_CORRUPTED: Located page was wrong type - you may want to start with --db-salvage
2023-08-03 16:28:35.728 10740 INFO global src/daemon/protocol.h:75 Stopping cryptonote protocol...
2023-08-03 16:28:35.728 10740 INFO global src/daemon/protocol.h:79 Cryptonote protocol stopped successfully
2023-08-03 16:28:35.728 10740 ERROR daemon src/daemon/main.cpp:364 Exception in main! Failed to open db handle for m_blocks : MDB_CORRUPTED: Located page was wrong type - you may want to start with --db-salvage
2023-08-03 16:28:37.647 10256 INFO logging contrib/epee/src/mlog.cpp:273 New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
2023-08-03 16:28:37.647 10256 INFO global src/daemon/main.cpp:296 Monero 'Fluorine Fermi' (v0.18.2.2-release)

Please help.

# Discussion History
## selsta | 2023-08-03T16:50:52+00:00
It seems the blockchain corrupted from the power outage. Do you have a backup of the blockchain? If not, you have to delete the blockchain and resync from scratch.

If you are a Windows users see here: https://monero.stackexchange.com/questions/1146/where-is-the-blockchain-saved-in-windows

On Linux / Mac the blockchain is stored by default at `~/.bitmonero/lmdb/`

## diamondsteel259 | 2023-08-03T17:29:49+00:00
is there anyway i can down load the blockchain faster as i had it running for 3 days and only had 68888 blocks to go

## diamondsteel259 | 2023-08-03T17:30:16+00:00
Thank you very much after response of question you can close the issue

## selsta | 2023-08-03T17:32:32+00:00
It should be faster if the blockchain is stored on an SSD. Otherwise you have to wait.

If power loss is a frequent issue I would recommend to make a backup from time to time. Also look into pruning if you want the blockchain to use less space.

# Action History
- Created by: diamondsteel259 | 2023-08-03T16:48:24+00:00
- Closed at: 2023-08-03T17:32:36+00:00
