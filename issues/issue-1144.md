---
title: Problems with database, re-syncing the blockchain and duplicate log entries
  since upgrading to 10.0
source_url: https://github.com/monero-project/monero/issues/1144
author: ghost
assignees: []
labels: []
created_at: '2016-09-27T23:41:42+00:00'
updated_at: '2016-09-29T11:59:40+00:00'
type: issue
status: closed
closed_at: '2016-09-29T11:59:40+00:00'
---

# Original Description
Was running 9.4.0 pulling down regular PRs. Decided to backup my `.bitmonero` directory and start to sync from scratch with 10.0. I'm on a 64-bit Odroid C2 ARMv8 system with a 128Gb SD card for the data directory.

Got to about 400k blocks then had to `monerod exit` and restart later, where the problems began, as detailed in #1128:

```
2016-Sep-26 22:11:40.807598 Initializing cryptonote protocol...
2016-Sep-26 22:11:40.807651 Cryptonote protocol initialized OK
2016-Sep-26 22:11:40.808516 Initializing p2p server...
2016-Sep-26 22:11:41.111194 Set limit-up to 2048 kB/s
2016-Sep-26 22:11:41.111406 Set limit-down to 8192 kB/s
2016-Sep-26 22:11:41.111493 Set limit-up to 2048 kB/s
2016-Sep-26 22:11:41.111630 Set limit-down to 8192 kB/s
2016-Sep-26 22:11:41.118196 Binding on 192.168.0.21:18080
2016-Sep-26 22:11:41.118658 Net service bound to 192.168.0.21:18080
2016-Sep-26 22:11:41.118705 Attempting to add IGD port mapping.
2016-Sep-26 22:11:42.272478 Added IGD port mapping.
2016-Sep-26 22:11:42.272623 P2p server initialized OK
2016-Sep-26 22:11:42.272881 Initializing core rpc server...
2016-Sep-26 22:11:42.273044 Binding on 127.0.0.1:18081
2016-Sep-26 22:11:42.273437 Core rpc server initialized OK on port: 18081
2016-Sep-26 22:11:42.273492 Initializing core...
2016-Sep-26 22:11:42.274189 Loading blockchain from folder /home/XXXXX/.bitmonero/lmdb ...
2016-Sep-26 22:11:42.274278 option: fast
2016-Sep-26 22:11:42.274312 option: async
2016-Sep-26 22:11:42.274340 option: 1000
2016-Sep-26 22:11:42.275109 Failed to drop m_hf_starting_heights: MDB_NOTFOUND: No matching key/data pair found
2016-Sep-26 22:11:42.275553 Error opening database: Failed to drop m_hf_starting_heights: MDB_NOTFOUND: No matching key/data pair found
2016-Sep-26 22:11:42.275625 Deinitializing rpc server...
2016-Sep-26 22:11:42.275920 Deinitializing p2p...
2016-Sep-26 22:11:42.284355 Deinitializing core...
2016-Sep-26 22:11:42.285239 Closing IO Service.
2016-Sep-26 22:11:42.285444 Failed to deinitialize core...
2016-Sep-26 22:11:42.285554 Deinitializing cryptonote_protocol...
```

So I pulled in #1123 and #1128 and deleted my directory to sync from scratch again. Now getting

```
2016-Sep-28 00:37:11.006107 BlockchainLMDB::BlockchainLMDB
2016-Sep-28 00:37:11.006152 BlockchainLMDB::get_db_name
2016-Sep-28 00:37:11.006185 Loading blockchain from folder /home/nodey/.bitmonero/lmdb ...
2016-Sep-28 00:37:11.006268 option: fast
2016-Sep-28 00:37:11.006301 option: async
2016-Sep-28 00:37:11.006331 option: 1000
2016-Sep-28 00:37:11.006377 BlockchainLMDB::open
2016-Sep-28 00:37:11.006729 BlockchainLMDB::need_resize
2016-Sep-28 00:37:11.006773 DB map size:     5368709120
2016-Sep-28 00:37:11.006805 Space used:      3238404096
2016-Sep-28 00:37:11.006835 Space remaining: 2130305024
2016-Sep-28 00:37:11.006864 Size threshold:  0
2016-Sep-28 00:37:11.006894 Percent used: 0.6032  Percent threshold: 0.8000
2016-Sep-28 00:37:11.007256 Failed to query m_blocks: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2016-Sep-28 00:37:11.007616 mdb_txn_safe: destructor
2016-Sep-28 00:37:11.007656 mdb_txn_safe: m_txn not NULL in destructor - calling mdb_txn_abort()
2016-Sep-28 00:37:11.007744 Error opening database: Failed to query m_blocks: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2016-Sep-28 00:37:11.007814 Deinitializing rpc server...
2016-Sep-28 00:37:11.008162 Deinitializing p2p...
2016-Sep-28 00:37:11.013814 [0.0.0.0:0 OUT]~async_protocol_handler()
2016-Sep-28 00:37:11.014328 Deinitializing core...
2016-Sep-28 00:37:11.014972 Blockchain::deinit
2016-Sep-28 00:37:11.015027 Closing IO Service.
2016-Sep-28 00:37:11.015192 Failed to deinitialize core...
2016-Sep-28 00:37:11.015306 Deinitializing cryptonote_protocol...
```

Also note the duplicate log entries when starting up:

```
2016-Sep-28 00:37:09.447855 Monero 'Wolfram Warptangent' (v0.10.0.0-e01a9ea)
2016-Sep-28 00:37:09.448502 Forking to background...
2016-Sep-28 00:37:09.450089 Monero 'Wolfram Warptangent' (v0.10.0.0-e01a9ea
```

Is this starting two instances, or is the first one main.cpp  and the second one daemon.cpp?

```
2016-Sep-27 00:20:27.826062 Set limit-up to 2048 kB/s
2016-Sep-27 00:20:27.826273 Set limit-down to 8192 kB/s
2016-Sep-27 00:20:27.826362 Set limit-up to 2048 kB/s
2016-Sep-27 00:20:27.826498 Set limit-down to 8192 kB/s
```

Why is it setting these limits twice?

Hope this makes some sense...I had no problems at all with firing up 0.9.4 and syncing from scratch. Now 10.0 seems to hog my connection and eventually stop syncing requiring a monerod exit, a restart and then I get database problems.


# Discussion History
## ghost | 2016-09-28T00:57:19+00:00
OK, I've figured out the first of the duplicate log entry issues and have submitted #1145 to make things clearer in future. I still can't figure out the other duplicate issue but will keep looking.

My bigger concern is the database issue though, if anyone can figure out what's happening here? @hyc - have you come across anything like this before?


## moneromooo-monero | 2016-09-28T07:19:41+00:00
How many monerod processes are you running when this happens ?


## ghost | 2016-09-28T11:08:15+00:00
Should be just the one. I've got max-concurrency set to one and I only call monerod once. 


## moneromooo-monero | 2016-09-28T11:41:02+00:00
It would be nice to know, however.


## ghost | 2016-09-28T13:01:02+00:00
Is there any easy way to tell?


## moneromooo-monero | 2016-09-28T14:01:50+00:00
ps u


## ghost | 2016-09-28T15:25:15+00:00
OK, there's only one process running with:

```
ps -ef | grep monero
```

Which is `monerod --detach`


## ghost | 2016-09-29T11:59:40+00:00
Closing...will keep testing and open a new issue if it seems persistent


# Action History
- Created by: ghost | 2016-09-27T23:41:42+00:00
- Closed at: 2016-09-29T11:59:40+00:00
