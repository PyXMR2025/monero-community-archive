---
title: Cannot reconnect to blockchain 90% downloaded
source_url: https://github.com/monero-project/monero/issues/6953
author: guyferguson
assignees: []
labels: []
created_at: '2020-10-31T08:44:48+00:00'
updated_at: '2021-08-13T07:06:15+00:00'
type: issue
status: closed
closed_at: '2021-08-13T07:06:15+00:00'
---

# Original Description
Hello,
I am happy to start a fresh sync, just raising this in case it helps improve code.
Running W10 machine. Blockchain being saved to drive with 39GB spare after 70GB downloaded.
I ran my initial sync from guiwallet for around 18 hours,, got to 70.22G (89%).  I was saving chain to non-default dir for space reasons.
Then - a storm here in Brisbane, brief power outage, restart machine, restart guiwallet.exe, 'Daemon failed to start, timed out after 120 seconds...
GUI log just says   
```
[31/10/2020 18:31] 2020-10-31 08:31:23.679 I Monero 'Oxygen Orion' (v0.17.1.1-release) 
Error: Couldn't connect to daemon: 127.0.0.1:18081
```
I've tried portforwarding 18081 to this machine, I must admit I am not confident of my TP-Link VR 1600 router's ability to port forward..Shields Up says it's still blocked.
So I shut down guiwallet, try monerod instead.   Using --data-dir, the logs tell me to use --db-salvage.  I do that, raise logs to level 4:
```
2020-10-31 08:24:03.150	420	INFO	logging	contrib/epee/src/mlog.cpp:273	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
2020-10-31 08:24:03.150	420	INFO	logging	contrib/epee/src/mlog.cpp:273	New log categories: *:TRACE
2020-10-31 08:24:03.151	420	INFO	global	src/daemon/main.cpp:293	Monero 'Oxygen Orion' (v0.17.1.1-release)
2020-10-31 08:24:03.152	420	INFO	daemon	src/daemon/main.cpp:355	Moving from main() into the daemonize now.
2020-10-31 08:24:03.152	420	INFO	global	src/daemon/protocol.h:53	Initializing cryptonote protocol...
2020-10-31 08:24:03.153	420	INFO	global	src/daemon/protocol.h:58	Cryptonote protocol initialized OK
2020-10-31 08:24:03.154	420	TRACE	blockchain	src/cryptonote_core/blockchain.cpp:102	Blockchain::Blockchain
2020-10-31 08:24:03.154	420	INFO	global	src/daemon/core.h:63	Initializing core...
2020-10-31 08:24:03.155	420	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1280	BlockchainLMDB::BlockchainLMDB
2020-10-31 08:24:03.155	420	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1687	BlockchainLMDB::get_db_name
2020-10-31 08:24:03.156	420	INFO	global	src/cryptonote_core/cryptonote_core.cpp:515	Loading blockchain from folder H:\ProgramData\bitmonero\lmdb ...
2020-10-31 08:24:03.156	420	DEBUG	cn	src/cryptonote_core/cryptonote_core.cpp:543	option: fast
2020-10-31 08:24:03.157	420	DEBUG	cn	src/cryptonote_core/cryptonote_core.cpp:543	option: async
2020-10-31 08:24:03.157	420	DEBUG	cn	src/cryptonote_core/cryptonote_core.cpp:543	option: 250000000bytes
2020-10-31 08:24:03.157	420	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1322	BlockchainLMDB::open
2020-10-31 08:24:03.159	420	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:592	BlockchainLMDB::need_resize
2020-10-31 08:24:03.159	420	DEBUG	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:608	DB map size:     80142200832
2020-10-31 08:24:03.160	420	DEBUG	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:609	Space used:      71894757376
2020-10-31 08:24:03.162	420	DEBUG	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:610	Space remaining: 8247443456
2020-10-31 08:24:03.162	420	DEBUG	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:611	Size threshold:  0
2020-10-31 08:24:03.162	420	DEBUG	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:613	Percent used: 89.7090  Percent threshold: 90.0000
2020-10-31 08:24:03.163	420	DEBUG	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1483	Setting m_height to: 0
```
Then monerod in CLI just quits, no more logs, no CLI error, not sure if there is some other log location to look at.

I have looked (in github) at what follows  line 1483 of db_lmdb.pp, and looked at the above  log. I have tried my daemon startings ecveral times, the outcome is consistent, as above.
monerod.exe --data-dir H:\ProgramData\bitmonero --log-level 4

Any ideas?
Thanks,
Guy,Brisbane,Australia

# Discussion History
## guyferguson | 2020-10-31T08:52:13+00:00
FYI - Debug Info from gui:
'''
GUI version: 0.17.1.1-33afd0b (Qt 5.9.9)
Embedded Monero version: 0.17.1.1-33afd0bb8
Wallet path: E:\crypto\Monero\wallets\GuyF\GuyF
Wallet restore height: 2198811
Wallet log path: C:\Users\GuyF\AppData\Roaming\monero-wallet-gui\monero-wallet-gui.log
Wallet mode: Advanced modeOpenGL
'''

## dEBRUYNE-1 | 2020-10-31T14:07:08+00:00
>Then - a storm here in Brisbane, brief power outage, restart machine, restart guiwallet.exe, 'Daemon failed to start, timed out after 120 seconds...

A power outage (i.e. unexpected shutdown) during the initial sync will cause the blockchain to corrupt. Alas, a resync from scratch will thus be required, which can be triggered by simply deleting `data.mdb`

## moneromooo-monero | 2020-10-31T14:07:48+00:00
Start again, wait for a couple minutes, then run sync_info. See whether all your peers are in this list: https://gui.xmr.pm/files/block.txt

If so, exit monerod, delete p2pstate.bin (it'll be in the .bitmonero directory where your chain is, not sure where it is on windows), and restart monerod.

## guyferguson | 2020-10-31T22:35:33+00:00
Thanks both of you.
OK, @moneromooo-monero - when you say 'start again', do you mean 'after deleting data.mdb' as @dEBRUYNE-1 said? I am guessing so, as monerod run from CLI just quits almost immediately (as per initial post).
If so, then can you clarify what the purpose of doing a sync_info is?   Is it to confirm the process id working properly?
Lastly - so it's better to get the blockchain from CLI daemon rather than GUI the first time? I think I may've read that you can 'preserve' the chain at various points by executing monerod exit...is that true of the initial download?   
Thanks for all your help, I am only 2 days into using xmr.

## dEBRUYNE-1 | 2020-11-01T13:58:12+00:00
>Lastly - so it's better to get the blockchain from CLI daemon rather than GUI the first time? I

Doesn't particularly matter, although some prefer to run `monerod.exe` separately. 

>I think I may've read that you can 'preserve' the chain at various points by executing monerod exit...is that true of the initial download?

The chain will be properly save if one exits `monerod.exe` by typing `exit`, yes. However, in case an unexpected shutdown occurs after `monerod.exe` is started again, the blockchain will still corrupt (unless it was fully in sync during the 'crash'). 

## moneromooo-monero | 2020-11-01T21:44:32+00:00
My intent was to check whether most of your peers are known malicious (they prevent you from downloading the chain from them).

## tendermonster | 2021-01-19T11:09:40+00:00
why is this still not marked as solved ? 

## guyferguson | 2021-01-19T12:30:21+00:00
Hi,
I don't think I can do that, with m,y permissions.  bc corrupted again this week, 'wrong page'. At 115GB I don't see myself doing a fourth full download.  I guess most in the community are aware of this obstacle to new users.

## selsta | 2021-08-13T07:06:15+00:00
@guyferguson Note that you can download a pruned blockchain (`--prune-blockchain`) that is only 35GB. Also you can set `--db-sync-mode safe` that will protect against db corruptions.

# Action History
- Created by: guyferguson | 2020-10-31T08:44:48+00:00
- Closed at: 2021-08-13T07:06:15+00:00
