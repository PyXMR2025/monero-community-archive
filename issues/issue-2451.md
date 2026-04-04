---
title: Monero Deamon Crashing (v0.11.0.0)
source_url: https://github.com/monero-project/monero/issues/2451
author: MelioraCogito
assignees: []
labels: []
created_at: '2017-09-16T00:56:37+00:00'
updated_at: '2017-09-22T10:06:21+00:00'
type: issue
status: closed
closed_at: '2017-09-22T10:06:21+00:00'
---

# Original Description
Windows 10 64-bit (with latest updates) Monero v0.11.0.0

After working without issue for about 18 hours after installing it on Sep 14th, I stopped the process (normally) on the morning of the 15th to free up resources.  About midday I restarted Monero from the GUI and everything appeared to be fine.  Got the appropriate message when the daemon was started and it started synchronizing with the network.  About 10 seconds later a Windows message pops up telling me Monerod.exe has stopped working.  Tried restarting form the GUI a couple times with the same result.
Then I tried starting the daemon from file explorer (double click in the executable), DOS window pops up and everything seems to fine, until it tries to synchronize with the network... ±10 sec later Windows again reports the daemon has stopped working.

Now normally I would just uninstall to program, clean the registry of any relics, and reinstall it.  However, this version didn't come with a setup.exe which would have installed it with all the registry keys, (after unpacking the zip file and noticing the absence of a setup.exe, I simply assumed the installation was simply a matter of copying the contents of the folder to my Program Files directory and creating a shortcut to my desktop, which did seem to work).  Problem is, I'm not sure where the synchronized data files are kept – I've looked in all the usual places, my \appdata sub-folders (all).  I really don't want to go through another 24 hours or more downloading a fresh set of synchronized data, not to mention restoring my wallet.

Any suggestions would be helpful.

I've attached a screen cap of the DOS window and an edited version of my GUI log file – just removed the superfluous verbose log inputs which have little relevance to the issue.  I did include the GUI shutdown log record when I first stopped Monero this morning, before restarting it some four hours later.

![2017-09-15 - monero daemon initlization](https://user-images.githubusercontent.com/11810277/30507787-42969fd4-9a3e-11e7-9409-018419cd2cea.png)

[monero-wallet-gui.zip](https://github.com/monero-project/monero/files/1307999/monero-wallet-gui.zip)



# Discussion History
## MelioraCogito | 2017-09-16T01:40:49+00:00
Okay, so I didn't check all the "usual places" i.e. the \Program Data\bitmonero folder.
It would seem either the data.mdb or lock.mdb files were corrupted?!?
I've renamed the old \imdb folder and restarted the synchronization process – the daemon seems to be working fine.
Interesting...

## moneromooo-monero | 2017-09-16T09:42:41+00:00
That doesn't look like a crash, just that the daemon stil hasn't finished syncing. With 0.11.0.0, this syncing is a lot more efficient than before, which means there is very little time left for the daemon to process RPC requests, and RPC thus can time out easily. The solution to that is to wait.

However, the "Windows message pops up telling me Monerod.exe has stopped working" kinda seems like a crash or similar. In that case, I'd need a stack trace to see where it crashed. Windbg allows getting stack traces on windows.

## unrealwill | 2017-09-17T15:39:48+00:00
I am on ubuntu 16.04 and I have the same problem too with v0.11.0.0.

WARN 	net.dns	src/common/dns_utils.cpp:487	WARNING: no two valid MoneroPulse DNS checkpoint records were received
2017-09-17 15:31:13.390	[P2P0]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:305	[96.43.143.234:18080 OUT] Sync data returned a new top block candidate: 1288623 -> 1401157 [Your node is 112534 blocks (156 days) behind] 
SYNCHRONIZATION started
**SEGFAULT Core Dumped**

It crashes also on the same block **1288623**.

I deleted the database and then retried and got the same error.

## unrealwill | 2017-09-17T15:52:07+00:00
I runned once more monerod --log-level=4 

2017-09-17 15:48:42.849	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:976	Miner tx hash: <0683dd5ea38fa83fe9e8a23f87b3b09645dc134558f106dea45a0d0438589aef>
2017-09-17 15:48:42.849	[P2P5]	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:2001	BlockchainLMDB::tx_exists

**2017-09-17 15:48:42.849	[P2P5]	INFO 	blockchain.db.lmdb	src/blockchain_db /lmdb/db_lmdb.cpp:2027	transaction with hash b177b6898937e62ab4df3085a23621cf4e48b5fe0c61ae2807c47d3ecf58a1a1 not found in db**


2017-09-17 15:48:42.849	[P2P5]	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:2545	BlockchainLMDB::batch_start
2017-09-17 15:48:42.849	[P2P5]	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1578	BlockchainLMDB::get_txpool_tx_meta
2017-09-17 15:48:42.849	[P2P5]	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1597	BlockchainLMDB::get_txpool_tx_blob
2017-09-17 15:48:42.849	[P2P5]	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1548	BlockchainLMDB::remove_txpool_tx
Segmentation fault (core dumped)

## moneromooo-monero | 2017-09-18T11:03:39+00:00
If you're on Ubuntu, then please supply a stack trace of the crash.

## lkleen | 2017-09-19T18:18:53+00:00
crash reproducer for Windows 7 64 bit 
- free space on drive C: 76 kB
- start monerod.exe from D:\monero-gui-0.11.0.0 (using the default data dir C:\ProgramData\bitmonero)
- crash

I've saved a dump file, please let me know if I should upload it somewhere

## moneromooo-monero | 2017-09-19T19:22:53+00:00
I wouldn't do anything with a windows dump, but I would do something with the stack trace for the crash, which should be obtainable from this dump file ?

Trying here on Linux with 60 kB free, I get errors commit DB transactions, but no crash, and all seems to work well otherwise.

## lkleen | 2017-09-20T09:06:39+00:00
To get a helpful stack trace I need the symbol file (.pdb) from the same build. Without it I can just see a nullpointer exception in the strlen method.

## TheMrMcBee | 2017-09-20T20:50:34+00:00
Like others, on Ubuntu 17.04 I'm seeing the following:

2017-09-20 20:39:16.302	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:305	[149.202.171.122:18080 OUT] Sync data returned a new top block candidate: 1288623 -> 1403447 [Your node is 114824 blocks (159 days) behind] 
SYNCHRONIZATION started

Thread 17 "monerod" received signal SIGSEGV, Segmentation fault.
[Switching to Thread 0x7fffdfafe700 (LWP 6559)]
__memcmp_sse4_1 () at ../sysdeps/x86_64/multiarch/memcmp-sse4.S:1525
1525	../sysdeps/x86_64/multiarch/memcmp-sse4.S: No such file or directory.

The debug back trace is attached as dump.out.  An attempt to extract any useful data is attached as debug.txt

[dump.txt](https://github.com/monero-project/monero/files/1319210/dump.txt)

[debug.txt](https://github.com/monero-project/monero/files/1319207/debug.txt)


## moneromooo-monero | 2017-09-20T20:57:48+00:00
fixed in https://github.com/monero-project/monero/pull/2492

## moneromooo-monero | 2017-09-22T09:44:57+00:00
+resolved

# Action History
- Created by: MelioraCogito | 2017-09-16T00:56:37+00:00
- Closed at: 2017-09-22T10:06:21+00:00
