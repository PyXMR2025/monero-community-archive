---
title: Lost Power @ 1602195/1625219 Blocks Synced; Now monerod.exe will not finish
  the sync..
source_url: https://github.com/monero-project/monero/issues/4181
author: deathd0tcom
assignees: []
labels: []
created_at: '2018-07-26T20:37:12+00:00'
updated_at: '2023-08-23T11:54:57+00:00'
type: issue
status: closed
closed_at: '2021-08-13T04:29:29+00:00'
---

# Original Description
This morning I left for work & I was this far along: 1416372/1624799

So I left the daemon syncing so when I got home it would be fully synced; unfortunately I apparently lost power about 2 hours before I got home. When checking the log, it clearly shows the last blocks that were synced. Here are the last few rows from bitmonero:
[P2P7]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[84.30.154.111:18080 OUT]  Synced 1602115/1625218[0m
[P2P7]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[84.30.154.111:18080 OUT]  Synced 1602135/1625218[0m
[P2P7]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[84.30.154.111:18080 OUT]  Synced 1602155/1625218[0m
[P2P7]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[84.30.154.111:18080 OUT]  Synced 1602175/1625219[0m
[P2P7]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[84.30.154.111:18080 OUT]  Synced 1602195/1625219[0m

But when I run monerod.exe, I get this error: 
INFO    global  src/daemon/core.h:86    Initializing core...
INFO    global  src/cryptonote_core/cryptonote_core.cpp:427     Loading blockchain from folder C:\ProgramData\bitmonero\lmdb ...
WARN    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:75   Attempt to get block from height 1592035 failed -- block not in db
FATAL   daemon  src/daemon/daemon.cpp:194       Uncaught exception! Attempt to get block from height 1592035 failed -- block not in db

I thought I was saving my progress the last 3 days when I used the command 'bc_save' since it returned 'Blockchain saved." in green text. Does anyone have any suggestions that I should follow so that I can avoid restarting the sync from the beginning? PS- I've been using the CLI on Windows. Thanks in advance!!

# Discussion History
## moneromooo-monero | 2018-07-26T21:02:48+00:00
Try running with "--db-salvage". If this does not help, then you need to resync. If you are likely to lose power, run with "--db-sync-mode safe", which will be slower.
And if takes more than three days to sync, use a SSD if you have one, they're *much* faster.

## deathd0tcom | 2018-07-26T21:30:14+00:00
--db-salvage does nothing.. so the time spent syncing over 1.6 million blocks was all for naught? there MUST be something that I can do to return to where i was... or at least to the block that it cannot find?

## moneromooo-monero | 2018-09-09T12:46:43+00:00
monero does not store block by block, it'd be unusably slow for use.
You have to resync, or restart from an earlier backup.
There was a bug setting safe mode, which is fixed in current release. This will not help if it breaks while in fast mode (ie, when doing the initial sync), but should prevent any such problems when the daemon's just keeping up with an already synced chain.

## tkalfaoglu | 2023-08-23T11:53:07+00:00
5 years later.. still the same problem..

2023-08-23 11:51:28.992 I Monero 'Fluorine Fermi' (v0.18.2.2-release)
2023-08-23 11:51:28.993 I Initializing cryptonote protocol...
2023-08-23 11:51:28.993 I Cryptonote protocol initialized OK
2023-08-23 11:51:28.995 I Initializing core...
2023-08-23 11:51:28.995 I Loading blockchain from folder /home/turgut/.bitmonero/lmdb ...
2023-08-23 11:51:29.065 W Attempt to get block from height 1711412 failed -- block not in db
2023-08-23 11:51:29.069 I Stopping cryptonote protocol...
2023-08-23 11:51:29.070 I Cryptonote protocol stopped successfully
2023-08-23 11:51:29.071 E Exception in main! Attempt to get block from height 1711412 failed -- block not in db



## selsta | 2023-08-23T11:54:57+00:00
@tkalfaoglu try to resync from scratch and make periodical backups if you frequently have power outages

# Action History
- Created by: deathd0tcom | 2018-07-26T20:37:12+00:00
- Closed at: 2021-08-13T04:29:29+00:00
