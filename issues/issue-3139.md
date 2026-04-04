---
title: Ubuntu 18.04.2 ~/.cache clearance causing blockchain sync issues?
source_url: https://github.com/monero-project/monero-gui/issues/3139
author: prometx
assignees: []
labels: []
created_at: '2020-10-08T05:44:36+00:00'
updated_at: '2021-01-15T11:39:34+00:00'
type: issue
status: closed
closed_at: '2021-01-15T11:39:34+00:00'
---

# Original Description
I have had a lot of problems syncing the monero blockchain reliably. I keep the blockchain on an external drive, and synced it from scratch a couple of days ago, and now am having a good deal of trouble again. It's dawned on me though that this *may* be related to my home user .cache directory?

I backup my homedir regularly, and to try to shave a little space off the backup size, I clear the ~/.cache directory. I checked there after my latest sync fail, and see this directory tree...   

`~/.cache/monero-project/monero-core/qmlcache/
`
I'm wondering if my troubles might lie in monerod & monero-wallet-gui, perhaps, storing some data here that helps it to corroborate lmdb  data; or something similar?

Please let me know if you think this is the case.

Best, 

# Discussion History
## selsta | 2020-10-08T10:03:45+00:00
Can you be more specific of what exactly your issue is?

## prometx | 2020-10-09T00:59:02+00:00
Here is a portion of, what seem to be, the relevant log lines:

`promet@shivux:/media/promet/WD1/Crypto/Monero/monero-gui-v0.16.0.3$ ./monerod --data-dir ./
2020-10-09 00:55:43.639	I Monero 'Nitrogen Nebula' (v0.16.0.3-release)
2020-10-09 00:55:43.639	I Initializing cryptonote protocol...
2020-10-09 00:55:43.639	I Cryptonote protocol initialized OK
2020-10-09 00:55:43.640	I Initializing core...
2020-10-09 00:55:43.640	I Loading blockchain from folder ./lmdb ...
2020-10-09 00:55:43.640	W The blockchain is on a rotating drive: this will be very slow, use an SSD if possible
2020-10-09 00:55:43.729	I Loading checkpoints
2020-10-09 00:55:43.729	I Core initialized OK
2020-10-09 00:55:43.729	I Initializing p2p server...
2020-10-09 00:55:43.737	I p2p server initialized OK
2020-10-09 00:55:43.737	I Initializing core RPC server...
2020-10-09 00:55:43.737	I Binding on 127.0.0.1 (IPv4):18081
2020-10-09 00:55:44.648	I core RPC server initialized OK on port: 18081
2020-10-09 00:55:44.648	I Starting core RPC server...
2020-10-09 00:55:44.648	I core RPC server started ok
2020-10-09 00:55:44.649	I Starting p2p net loop...
2020-10-09 00:55:45.650	I 
2020-10-09 00:55:45.650	I **********************************************************************
2020-10-09 00:55:45.650	I The daemon will start synchronizing with the network. This may take a long time to complete.
2020-10-09 00:55:45.650	I 
2020-10-09 00:55:45.650	I You can set the level of process detailization through "set_log <level|categories>" command,
2020-10-09 00:55:45.650	I where <level> is between 0 (no details) and 4 (very verbose), or custom category based levels (eg, *:WARNING).
2020-10-09 00:55:45.650	I 
2020-10-09 00:55:45.650	I Use the "help" command to see the list of available commands.
2020-10-09 00:55:45.650	I Use "help <command>" to see a command's documentation.
2020-10-09 00:55:45.650	I **********************************************************************
2020-10-09 00:55:54.323	I [47.185.74.58:18080 OUT] Sync data returned a new top block candidate: 2202074 -> 2204170 [Your node is 2096 blocks (2.9 days) behind] 
2020-10-09 00:55:54.323	I SYNCHRONIZATION started
2020-10-09 00:55:57.838	W Error attempting to retrieve an output pubkey from the dbMDB_PAGE_NOTFOUND: Requested page not found
2020-10-09 00:55:57.851	W Failed to open cursor: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2020-10-09 00:55:57.851	E Exception at [core::handle_incoming_txs()], what=Failed to open cursor: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2020-10-09 00:55:58.158	W Failed to query m_blocks: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2020-10-09 00:55:58.158	E Exception at [core::handle_incoming_block()], what=Failed to query m_blocks: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2020-10-09 00:55:58.164	W Failed to open cursor: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2020-10-09 00:55:58.164	E Exception at [core::handle_incoming_txs()], what=Failed to open cursor: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2020-10-09 00:55:58.164	W DB error attempting to fetch block index from hashMDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2020-10-09 00:55:58.165	E Exception at [add_new_block], what=DB error attempting to fetch block index from hashMDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2020-10-09 00:55:58.165	W Failed to commit a transaction to the db: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2020-10-09 00:55:58.165	E Exception in cleanup_handle_incoming_blocks: Failed to commit a transaction to the db: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2020-10-09 00:55:58.166	W monerod is now disconnected from the network
2020-10-09 00:56:03.387	I [24.51.193.168:18080 OUT] Sync data returned a new top block candidate: 2202074 -> 2204170 [Your node is 2096 blocks (2.9 days) behind] 
2020-10-09 00:56:03.388	I SYNCHRONIZATION started
2020-10-09 00:56:13.379	W Error attempting to retrieve an output pubkey from the dbMDB_PAGE_NOTFOUND: Requested page not found
2020-10-09 00:56:13.391	W Failed to open cursor: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2020-10-09 00:56:13.392	E Exception at [core::handle_incoming_txs()], what=Failed to open cursor: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2020-10-09 00:56:13.392	W DB error attempting to fetch block index from hashMDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2020-10-09 00:56:13.392	E Exception at [add_new_block], what=DB error attempting to fetch block index from hashMDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2020-10-09 00:56:13.392	W Failed to commit a transaction to the db: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2020-10-09 00:56:13.392	E Exception in cleanup_handle_incoming_blocks: Failed to commit a transaction to the db: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2020-10-09 00:56:30.887	W Error attempting to retrieve an output pubkey from the dbMDB_PAGE_NOTFOUND: Requested page not found
2020-10-09 00:56:30.898	W Failed to open cursor: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2020-10-09 00:56:30.898	E Exception at [core::handle_incoming_txs()], what=Failed to open cursor: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2020-10-09 00:56:30.898	W DB error attempting to fetch block index from hashMDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2020-10-09 00:56:30.898	E Exception at [add_new_block], what=DB error attempting to fetch block index from hashMDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2020-10-09 00:56:30.899	W Failed to commit a transaction to the db: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2020-10-09 00:56:30.899	E Exception in cleanup_handle_incoming_blocks: Failed to commit a transaction to the db: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2020-10-09 00:56:44.547	W Error attempting to retrieve an output pubkey from the dbMDB_PAGE_NOTFOUND: Requested page not found
2020-10-09 00:56:44.562	W Failed to open cursor: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2020-10-09 00:56:44.563	E Exception at [core::handle_incoming_txs()], what=Failed to open cursor: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2020-10-09 00:56:44.563	W DB error attempting to fetch block index from hashMDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2020-10-09 00:56:44.563	E Exception at [add_new_block], what=DB error attempting to fetch block index from hashMDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2020-10-09 00:56:44.563	W Failed to commit a transaction to the db: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2020-10-09 00:56:44.563	E Exception in cleanup_handle_incoming_blocks: Failed to commit a transaction to the db: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2020-10-09 00:57:05.609	W Error attempting to retrieve an output pubkey from the dbMDB_PAGE_NOTFOUND: Requested page not found
2020-10-09 00:57:05.620	W Failed to open cursor: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2020-10-09 00:57:05.620	E Exception at [core::handle_incoming_txs()], what=Failed to open cursor: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2020-10-09 00:57:05.620	W DB error attempting to fetch block index from hashMDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2020-10-09 00:57:05.620	E Exception at [add_new_block], what=DB error attempting to fetch block index from hashMDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2020-10-09 00:57:05.620	W Failed to commit a transaction to the db: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2020-10-09 00:57:05.620	E Exception in cleanup_handle_incoming_blocks: Failed to commit a transaction to the db: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2020-10-09 00:57:17.424	W Error attempting to retrieve an output pubkey from the dbMDB_PAGE_NOTFOUND: Requested page not found
2020-10-09 00:57:17.439	W Failed to open cursor: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2020-10-09 00:57:17.439	E Exception at [core::handle_incoming_txs()], what=Failed to open cursor: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2020-10-09 00:57:17.439	W DB error attempting to fetch block index from hashMDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2020-10-09 00:57:17.439	E Exception at [add_new_block], what=DB error attempting to fetch block index from hashMDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2020-10-09 00:57:17.439	W Failed to commit a transaction to the db: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2020-10-09 00:57:17.439	E Exception in cleanup_handle_incoming_blocks: Failed to commit a transaction to the db: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2020-10-09 00:57:19.701	W Error attempting to retrieve an output pubkey from the dbMDB_PAGE_NOTFOUND: Requested page not found
2020-10-09 00:57:19.715	W Failed to open cursor: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2020-10-09 00:57:19.715	E Exception at [core::handle_incoming_txs()], what=Failed to open cursor: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2020-10-09 00:57:19.715	W DB error attempting to fetch block index from hashMDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2020-10-09 00:57:19.715	E Exception at [add_new_block], what=DB error attempting to fetch block index from hashMDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2020-10-09 00:57:19.716	W Failed to commit a transaction to the db: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2020-10-09 00:57:19.716	E Exception in cleanup_handle_incoming_blocks: Failed to commit a transaction to the db: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
`



## selsta | 2020-10-09T01:01:35+00:00
Did you plug out your external hard drive during sync / use in general?

## prometx | 2020-10-09T01:59:11+00:00
No, this drive auto-mounts at boot and remains mounted as a matter of course...

## selsta | 2020-10-17T02:17:00+00:00
~/.cache should not be related at all to blockchain sync issues. What you are describing is usually the result of force shutdown computer or plugging out hard disk during sync.

## xiphon | 2021-01-15T11:39:34+00:00
Disk cache is disabled since v0.17.1.7.

# Action History
- Created by: prometx | 2020-10-08T05:44:36+00:00
- Closed at: 2021-01-15T11:39:34+00:00
