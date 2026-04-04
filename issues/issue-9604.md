---
title: 'Need help with repairing the corrupted Blockchain while syncing. '
source_url: https://github.com/monero-project/monero/issues/9604
author: imnotadev-ineedhelp
assignees: []
labels: []
created_at: '2024-12-08T04:04:08+00:00'
updated_at: '2024-12-10T11:07:30+00:00'
type: issue
status: closed
closed_at: '2024-12-10T11:07:30+00:00'
---

# Original Description
I was syncing the block chain at prune mode, I think. Cause using the GUI wallet when I set the custome location for the node, it told me it needs 50gb empty space. So I thought and still believe that it look at my available space and suggest me to prune automatically. But while I was syncing, I got a blackout. So checked the log it was at 98%. But now when I run the syncing from GUI it shows me error. So, I but the monerod.exe flags manually on CMD and got the log down below. After doing some research it feels like my block chain got corrupt. But found no fix, hance now I'm here. Please help, I was downloading for straight 3 days. Here is the log,

    C:\\Program Files\\Monero GUI Wallet>.\\monerod.exe --db-salvage --log-level=1 --data-dir=D:\\xmr-bc --db-sync-mode=safe:sync
    2024-12-07 11:33:32.692 I Monero 'Fluorine Fermi' (v0.18.3.4-release)
    2024-12-07 11:33:32.693 I Moving from main() into the daemonize now.
    2024-12-07 11:33:32.694 I Initializing cryptonote protocol...
    2024-12-07 11:33:32.695 I Cryptonote protocol initialized OK
    2024-12-07 11:33:32.697 I Initializing core...
    2024-12-07 11:33:32.697 I Loading blockchain from folder D:\\xmr-bc\\lmdb ...
    2024-12-07 11:33:32.710 I Threshold met (percent-based)
    2024-12-07 11:33:32.712 W LMDB memory map needs to be resized, doing that now.
    2024-12-07 11:33:32.714 I LMDB Mapsize increased.  Old: 88622MiB, New: 89646MiB
    2024-12-07 11:33:32.715 W Failed to commit a transaction to the db: MDB\_CORRUPTED: Located page was wrong type
    2024-12-07 11:33:32.716 E Error opening database: Failed to commit a transaction to the db: MDB\_CORRUPTED: Located page was wrong type
    2024-12-07 11:33:32.716 I Stopping cryptonote protocol...
    2024-12-07 11:33:32.716 I Cryptonote protocol stopped successfully
    2024-12-07 11:33:32.717 E Exception in main! Failed to initialize core

# Discussion History
## imnotadev-ineedhelp | 2024-12-08T13:37:50+00:00
Wow scamming on official github repo 🤣

## imnotadev-ineedhelp | 2024-12-08T14:13:37+00:00
I tried this, is there anything else I can do?
```
PS C:\Program Files\Monero GUI Wallet> .\monerod.exe --data-dir D:\xmr-bc --db-salvage --log-level 4 --offline
2024-12-08 14:12:14.167 I Monero 'Fluorine Fermi' (v0.18.3.4-release)
2024-12-08 14:12:14.167 I Moving from main() into the daemonize now.
2024-12-08 14:12:14.183 I Initializing cryptonote protocol...
2024-12-08 14:12:14.183 I Cryptonote protocol initialized OK
2024-12-08 14:12:14.183 T Blockchain::Blockchain
2024-12-08 14:12:14.183 I Initializing core...
2024-12-08 14:12:14.183 T BlockchainLMDB::BlockchainLMDB
2024-12-08 14:12:14.183 T BlockchainLMDB::get_db_name
2024-12-08 14:12:14.183 I Loading blockchain from folder D:\xmr-bc\lmdb ...
2024-12-08 14:12:14.183 D option: fast
2024-12-08 14:12:14.183 D option: async
2024-12-08 14:12:14.183 D option: 250000000bytes
2024-12-08 14:12:14.183 T BlockchainLMDB::open
2024-12-08 14:12:14.183 T BlockchainLMDB::need_resize
2024-12-08 14:12:14.183 D DB map size:     92927610880
2024-12-08 14:12:14.183 D Space used:      83642712064
2024-12-08 14:12:14.183 D Space remaining: 9284898816
2024-12-08 14:12:14.193 D Size threshold:  0
2024-12-08 14:12:14.193 D Percent used: 90.0085  Percent threshold: 90.0000
2024-12-08 14:12:14.193 I Threshold met (percent-based)
2024-12-08 14:12:14.193 W LMDB memory map needs to be resized, doing that now.
2024-12-08 14:12:14.193 T BlockchainLMDB::do_resize
2024-12-08 14:12:14.193 I LMDB Mapsize increased.  Old: 88622MiB, New: 89646MiB
2024-12-08 14:12:14.193 D Setting m_height to: 0
2024-12-08 14:12:14.193 W Failed to commit a transaction to the db: MDB_CORRUPTED: Located page was wrong type
2024-12-08 14:12:14.193 T mdb_txn_safe: destructor
2024-12-08 14:12:14.193 E Error opening database: Failed to commit a transaction to the db: MDB_CORRUPTED: Located page was wrong type
2024-12-08 14:12:14.193 T BlockchainLMDB::~BlockchainLMDB
2024-12-08 14:12:14.193 T Miner has received stop signal
2024-12-08 14:12:14.193 T Not mining - nothing to stop
2024-12-08 14:12:14.193 T Blockchain::deinit
2024-12-08 14:12:14.193 T Stopping blockchain read/write activity
2024-12-08 14:12:14.193 I Stopping cryptonote protocol...
2024-12-08 14:12:14.193 I Cryptonote protocol stopped successfully
2024-12-08 14:12:14.193 E Exception in main! Failed to initialize core
```

## selsta | 2024-12-08T14:19:25+00:00
Unfortunately you will likely have to re-sync from scratch, if `--db-salvage` does not work and if there's no backup then there is no other solution.

Power loss during the initial sync causes a blockchain corruption most of the time.

## imnotadev-ineedhelp | 2024-12-08T14:21:36+00:00
So don't you think the it's kind of dumb that it claims to be the one who breaks all other problem, but not this simple one which is I have all the data but I can't recover it :| 

## selsta | 2024-12-08T15:14:57+00:00
If you have frequent issues with power outages you can add `--db-sync-mode safe`, which will result in a slower sync but should prevent corruption.

## imnotadev-ineedhelp | 2024-12-08T15:47:05+00:00
Bro how can I verify if a database pruned or not? 

# Action History
- Created by: imnotadev-ineedhelp | 2024-12-08T04:04:08+00:00
- Closed at: 2024-12-10T11:07:30+00:00
