---
title: ' Failed to open lmdb environment: Permission denied'
source_url: https://github.com/monero-project/monero/issues/3790
author: 5-digits
assignees: []
labels:
- invalid
created_at: '2018-05-09T16:35:31+00:00'
updated_at: '2025-12-20T17:43:48+00:00'
type: issue
status: closed
closed_at: '2018-09-09T12:32:49+00:00'
---

# Original Description
when trying to execute the monerod Testnet Node 

./monerod --testnet

```
2018-05-09 16:33:44.450     7f06f53d7740        INFO    global  src/daemon/main.cpp:280 Monero 'Lithium Luna' (v0.12.0.0-master-release)
2018-05-09 16:33:44.450     7f06f53d7740        INFO    global  src/daemon/protocol.h:53        Initializing cryptonote protocol...
2018-05-09 16:33:44.450     7f06f53d7740        INFO    global  src/daemon/protocol.h:58        Cryptonote protocol initialized OK
2018-05-09 16:33:44.451     7f06f53d7740        INFO    global  src/daemon/p2p.h:63     Initializing p2p server...
2018-05-09 16:33:48.456     7f06f53d7740        INFO    global  src/daemon/p2p.h:68     p2p server initialized OK
2018-05-09 16:33:48.457     7f06f53d7740        INFO    global  src/daemon/rpc.h:63     Initializing core RPC server...
2018-05-09 16:33:48.457     7f06f53d7740        INFO    global  contrib/epee/include/net/http_server_impl_base.h:76     Binding on 127.0.0.1:28081
2018-05-09 16:33:48.457     7f06f53d7740        INFO    global  src/daemon/rpc.h:69     core RPC server initialized OK on port: 28081
2018-05-09 16:33:48.457     7f06f53d7740        INFO    global  src/daemon/core.h:86    Initializing core...
2018-05-09 16:33:48.458     7f06f53d7740        INFO    global  src/cryptonote_core/cryptonote_core.cpp:427     Loading blockchain from folder /var/lib/monero/testnet/lmdb ...
2018-05-09 16:33:48.458     7f06f53d7740        WARN    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:75   **Failed to open lmdb environment: Permission denied**
2018-05-09 16:33:48.463     7f06f53d7740        ERROR   cn      src/cryptonote_core/cryptonote_core.cpp:503     Error opening database: Failed to open lmdb environment: Permission denied
2018-05-09 16:33:48.464     7f06f53d7740        INFO    global  src/daemon/rpc.h:96     Deinitializing core RPC server...
2018-05-09 16:33:48.464     7f06f53d7740        INFO    global  src/daemon/p2p.h:90     Deinitializing p2p...
2018-05-09 16:33:52.469     7f06f53d7740        INFO    global  src/daemon/core.h:103   Deinitializing core...
2018-05-09 16:33:52.472     7f06f53d7740        ERROR   daemon  src/daemon/core.h:108   Failed to deinitialize core...
2018-05-09 16:33:52.473     7f06f53d7740        INFO    global  src/daemon/protocol.h:75        Stopping cryptonote protocol...
2018-05-09 16:33:52.473     7f06f53d7740        INFO    global  src/daemon/protocol.h:79        Cryptonote protocol stopped successfully

```
I'm using Ubuntu 16 as OS

# Discussion History
## moneromooo-monero | 2018-05-09T16:50:57+00:00
Are you *really* sure you have permissions to there ?

## 5-digits | 2018-05-09T17:01:29+00:00
yes i'm the root
 when run it on mainnet network, it works fine 


## moneromooo-monero | 2018-05-09T17:07:02+00:00
What filesystem is that on ?

## moneromooo-monero | 2018-05-09T17:12:26+00:00
Also:
ls -ld /var/lib/monero
ls -l /var/lib/monero
ls -l /var/lib/monero/lmdb
ls -l /var/lib/monero/testnet
ls -l /var/lib/monero/testnet/lmdb

## 5-digits | 2018-05-11T09:33:47+00:00
Hi @moneromooo-monero  i'v change the permission so it start syncing from Zero
But i'm already fully download the blockchain


## moneromooo-monero | 2018-07-19T21:43:33+00:00
Is this still happening ? If so, send the output of the commands above. Otherwise I'll close it.

## 5-digits | 2018-07-20T09:56:56+00:00
Thanks @moneromooo-monero,  i resolve my issue by following the commands you post

## moneromooo-monero | 2018-07-20T13:37:31+00:00
That's scary, because those commands should not change the state of the filesystem (much).

## moneromooo-monero | 2018-09-09T12:16:45+00:00
Probably some permission thing that's unrelated to monero, we'll likely never know.

+invalid

## ychaxel | 2025-12-20T17:43:48+00:00
i have a similar issue: loading blockchain from folder /var/lib/monero/bitmonero/stagenet/lmdb ...
failed to open lmdb environment: Permission denied

# Action History
- Created by: 5-digits | 2018-05-09T16:35:31+00:00
- Closed at: 2018-09-09T12:32:49+00:00
