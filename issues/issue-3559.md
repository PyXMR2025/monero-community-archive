---
title: monerod doesn't verify blocks, can't find transactions and quits
source_url: https://github.com/monero-project/monero/issues/3559
author: Adreik
assignees: []
labels:
- invalid
created_at: '2018-04-05T12:50:16+00:00'
updated_at: '2019-04-16T23:17:31+00:00'
type: issue
status: closed
closed_at: '2019-04-16T23:17:31+00:00'
---

# Original Description
-Launched monerod.exe on a windows 10, 64 bit machine via powershell (".\monerod.exe --log-level 1"), from the release binary (verified hashes)

-All but the very first block has a PoW of <0000000000000000000000000000000000000000000000000000000000000000>

-Many transactions are "not found" in the database.

-monerod quits unexpectedly without any error messages etc (sometimes hangs rather than quitting)

-Example log file (debug level 1): https://drive.google.com/open?id=1PgyUTcyijarygJU74hIjvtxd8vUggpPM

-I have tested it with version 11.1 as well and the similar issue occurs.

-EDIT: Have tested it on two computers; issue persists.

-EDIT2: starting with a "--fast-block-sync 0" flag gets rid of the PoW issue, but not the missing transaction issue or the sudden unexpected crash.

EDIT 3: transactions appear to be findable with print_tx, however the log of them being added occurs before the log of them not being found.

Example log of daemon claiming transaction to be missing, then saying it's added to the transaction pool, and then saying it's missing:

`
2018-04-05 12:30:38.831	[P2P9]	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:2087	transaction with hash beb76a82ea17400cd6d7f595f70e1667d2018ed8f5a78d1ce07484222618c3cd not found in db
2018-04-05 12:30:38.831	[P2P9]	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:2087	transaction with hash beb76a82ea17400cd6d7f595f70e1667d2018ed8f5a78d1ce07484222618c3cd not found in db
2018-04-05 12:30:38.831	[P2P9]	INFO 	txpool	src/cryptonote_core/tx_pool.cpp:307	Transaction added to pool: txid <beb76a82ea17400cd6d7f595f70e1667d2018ed8f5a78d1ce07484222618c3cd> bytes: 776 fee/byte: 1288.66
2018-04-05 12:30:38.831	[P2P9]	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:2087	transaction with hash beb76a82ea17400cd6d7f595f70e1667d2018ed8f5a78d1ce07484222618c3cd not found in db
`

EDIT 4: Judging by the fact that wallet CLI software continues to increase in blocks, when monerod.exe appears to freeze/halt it sometimes is only affects logging and feedback of monerod.exe; it won't respond or show signs of life but it seems to be downloading blocks regardless, just without showing status updates or responding to the interactive commands. However, at other times monerod.exe will actually crash, with powershell showing c:\path\wallet-directory> and monerod.exe disappearing from task manager.

# Discussion History
## moneromooo-monero | 2018-04-07T14:35:27+00:00
PoW being reported as 00..00 is because it's not calculated in fast sync mode, as you found out.
The tx not found is informative. It's not an error.

For the crash, you need to get us a stack trace of the crash. "WinDbg" might help.


## Adreik | 2018-04-07T23:20:49+00:00
I'm not sure how to do that, sorry.

I can tell you that there's no monero daemon v 12.0 logs in event viewer (There is one from when I was trying to run version 10, and there is a "program hang" error for the GUI wallet that was in version 12)

## moneromooo-monero | 2018-05-16T10:38:12+00:00
Re-reading this, there seems to be several wrong assumptions, then two valid bugs:

- monerod quits without being asked to
- monerod output stops, though the program continues running

The first one might be out of memory (I'm not sure how to tell on Windows) or a monero bug. There's apparently no message, so probably not a crash.
The second one I've heard about before, and it's a Windows bug AFAIK.


## moneromooo-monero | 2018-11-04T12:48:05+00:00
Can you try again with 0.13.0.4 ?

## Adreik | 2018-11-08T11:50:30+00:00
I haven't had this issue in 0.13.0.4 so far.

## moneromooo-monero | 2019-04-16T23:07:05+00:00
Mostly misunderstandings, so I'lll close. Reopen new bugs if anything does not actually work. One bug per problem please.

+invalid

# Action History
- Created by: Adreik | 2018-04-05T12:50:16+00:00
- Closed at: 2019-04-16T23:17:31+00:00
