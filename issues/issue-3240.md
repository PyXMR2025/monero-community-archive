---
title: MDB_CURSOR_FULL during initial sync which apparently corrupted the database
source_url: https://github.com/monero-project/monero/issues/3240
author: romlok
assignees: []
labels: []
created_at: '2018-02-07T13:02:42+00:00'
updated_at: '2018-02-12T14:24:31+00:00'
type: issue
status: closed
closed_at: '2018-02-12T14:24:31+00:00'
---

# Original Description
I've been slowly syncing the blockchain for the past few days, and monerod just hit an error that caused it to stop in its tracks:

```MDB_CURSOR_FULL: Internal error - cursor stack limit reached```
```log
...
2018-02-07 12:10:32.054 [P2P5]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154    [90.66.140.71:18080 OUT]  Synced 1387250/1504301
2018-02-07 12:10:33.512 [P2P5]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154    [90.66.140.71:18080 OUT]  Synced 1387270/1504302
2018-02-07 12:10:33.535 [P2P5]  WARN    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:72   DB error attempting to fetch transaction index from hash a958b2be95b6d2e00a99e0b34e636a586301955cde7904d0484f5335c9e8db32: MDB_CURSOR_FULL: Internal error - cursor stack limit reached                                 
2018-02-07 12:10:33.601 [P2P5]  ERROR   cn      src/cryptonote_core/cryptonote_core.cpp:662     Exception at [core::handle_incoming_txs()], what=DB error attempting to fetch transaction index from hash a958b2be95b6d2e00a99e0b34e636a586301955cde7904d0484f5335c9e8db32: MDB_CURSOR_FULL: Internal error - cursor stack limit reached                                                                        
2018-02-07 12:10:33.601 [P2P5]  WARN    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:72   Failed to open cursor: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid                                                  
2018-02-07 12:10:33.605 [P2P5]  ERROR   cn      src/cryptonote_core/cryptonote_core.cpp:1138    Exception at [core::handle_incoming_block()], what=Failed to open cursor: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid       
2018-02-07 12:10:33.620 [P2P5]  ERROR   cn      src/cryptonote_core/cryptonote_core.cpp:662     Exception at [core::handle_incoming_txs()], what=Error finding txpool tx meta: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid  
2018-02-07 12:10:33.620 [P2P5]  WARN    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:72   Failed to open cursor: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid                                                  
2018-02-07 12:10:33.625 [P2P5]  ERROR   cn      src/cryptonote_core/cryptonote_core.cpp:1138    Exception at [core::handle_incoming_block()], what=Failed to open cursor: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid       
2018-02-07 12:10:33.630 [P2P5]  ERROR   cn      src/cryptonote_core/cryptonote_core.cpp:662     Exception at [core::handle_incoming_txs()], what=Error finding txpool tx meta: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid  ...
...
```

As soon as I noticed that all it was doing was outputting `MDB_BAD_TXN` errors, I told monerod to `exit`. Once it had stopped successfully, I tried to `--db-salvage`, but with no luck:

```MDB_INVALID: File is not an LMDB file```
```log
$ ./monerod --db-salvage  
2018-02-07 12:17:39.260     7f182f13fbc0        INFO    global  src/daemon/main.cpp:279 Monero 'Helium Hydra' (v0.11.1.0-release)                               
2018-02-07 12:17:39.260     7f182f13fbc0        INFO    global  src/daemon/protocol.h:55        Initializing cryptonote protocol...                             
2018-02-07 12:17:39.260     7f182f13fbc0        INFO    global  src/daemon/protocol.h:60        Cryptonote protocol initialized OK                              
2018-02-07 12:17:39.261     7f182f13fbc0        INFO    global  src/daemon/p2p.h:63     Initializing p2p server...                                              
2018-02-07 12:17:43.496     7f182f13fbc0        INFO    global  src/daemon/p2p.h:68     P2p server initialized OK                                               
2018-02-07 12:17:43.497     7f182f13fbc0        INFO    global  src/daemon/rpc.h:58     Initializing core rpc server...                                         
2018-02-07 12:17:43.497     7f182f13fbc0        INFO    global  contrib/epee/include/net/http_server_impl_base.h:70     Binding on 127.0.0.1:18081              
2018-02-07 12:17:43.497     7f182f13fbc0        INFO    global  src/daemon/rpc.h:63     Core rpc server initialized OK on port: 18081                           
2018-02-07 12:17:43.497     7f182f13fbc0        INFO    global  src/daemon/core.h:73    Initializing core...                                                    
2018-02-07 12:17:43.497     7f182f13fbc0        INFO    global  src/cryptonote_core/cryptonote_core.cpp:323     Loading blockchain from folder /home/mel/.bitmonero/lmdb ...                                                                    
2018-02-07 12:17:43.498     7f182f13fbc0        WARN    blockchain.db.lmdb     src/blockchain_db/lmdb/db_lmdb.cpp:72    Failed to open lmdb environment: MDB_INVALID: File is not an LMDB file                                                  
2018-02-07 12:17:43.528     7f182f13fbc0        ERROR   cn      src/cryptonote_core/cryptonote_core.cpp:399     Error opening database: Failed to open lmdb environment: MDB_INVALID: File is not an LMDB file                                  
2018-02-07 12:17:43.528     7f182f13fbc0        INFO    global  src/daemon/rpc.h:90     Deinitializing rpc server...                                            
2018-02-07 12:17:43.528     7f182f13fbc0        INFO    global  src/daemon/p2p.h:90     Deinitializing p2p...                                                   
2018-02-07 12:17:43.533     7f182f13fbc0        INFO    global  src/daemon/core.h:89    Deinitializing core...                                                  
2018-02-07 12:17:43.536     7f182f13fbc0        ERROR   daemon  src/daemon/core.h:94    Failed to deinitialize core...                                          
2018-02-07 12:17:43.536     7f182f13fbc0        INFO    global  src/daemon/protocol.h:77        Stopping cryptonote protocol...                                 
2018-02-07 12:17:43.537     7f182f13fbc0        INFO    global  src/daemon/protocol.h:81        Cryptonote protocol stopped successfully
```

I'm using Debian Testing, and the monerod supplied with the latest monero-gui (v0.11.1.0-release).
In case it matters, I was also syncing onto a relatively slow (5400rpm) HDD, which is at a constant 100% activity while syncing.

# Discussion History
## hyc | 2018-02-07T22:46:51+00:00
Your hard drive is corrupted. MDB_INVALID means the magic numbers at the very beginning of the file don't match the expected values. Ordinarily there's no way for these numbers to be corrupted; nothing overwrites them once they're created. Only conclusion is that the actual storage medium has failed.

## romlok | 2018-02-12T14:24:31+00:00
Thanks, I thought the age of the hardware might have something to do with it. The SMART data says the drive is fine, but SMART ain't all that smart.

Might be nice if db-salvage could try and fix this though? I mean, if you're running db-salvage against a file (especially in the default location), it should be a fair assumption to make that the file is/was an appropriate database.

# Action History
- Created by: romlok | 2018-02-07T13:02:42+00:00
- Closed at: 2018-02-12T14:24:31+00:00
