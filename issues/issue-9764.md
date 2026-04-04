---
title: Need help urgently..
source_url: https://github.com/monero-project/monero/issues/9764
author: xioney1263
assignees: []
labels:
- more info needed
created_at: '2025-02-01T15:00:01+00:00'
updated_at: '2025-12-19T14:55:01+00:00'
type: issue
status: closed
closed_at: '2025-12-19T14:55:01+00:00'
---

# Original Description
I tried to sync with the blockchain, but it doesn't work. I managed to sync up to block 3216307, and then it stops syncing.

I’ve tried switching the internet, turning off the firewall, and testing with another computer, but it still doesn’t work.

Here’s a video about the problem. Let me know if you guys can help me.

https://github.com/user-attachments/assets/19761a9f-86bf-4e51-b996-3725e67a4d8a

# Discussion History
## selsta | 2025-02-02T19:38:01+00:00
Can you explain what you mean with "testing another computer"? Did you try to sync from scratch on a different computer or did you copy it? At what point did it get stuck?

## xioney1263 | 2025-02-02T20:45:28+00:00
Sure I have try new network with other router Brant and I did not copy it to new pc I resync it Everytime when I try and I have tested the blockchain.raw from moneros website and that Dident work also its stoping in the end like the database is corrupted like from 10.5 months away to 3 months away

Let me know what I should test next or do you have solution?

Thanks 
Xy

## selsta | 2025-02-03T10:36:57+00:00
So it does not stop at the same time but at different times? once 10.5 months away and one time 3 months away after resycing? Did both computers you tried use Ubuntu?

## xioney1263 | 2025-02-03T12:46:54+00:00
Not the same time but it’s stops when it will be about to finish som times it stops 83% and 95 it can be anything I’m runing on the server Ubuntu 22.04.5 and yes the both pc have the same Ubuntu 

If you want I can try newer Ubuntu?

## tczee36 | 2025-02-06T20:00:48+00:00
try using a remote node?

## dbee01 | 2025-02-07T16:48:44+00:00
Are you running out of space? 

## Gingeropolous | 2025-02-08T01:16:23+00:00
To me this looks like you've found yourself connected to bad peers. There are multiple ways to correct this. One such way is to delete p2pstate.bin from the .bitmonero directory, but that is frowned upon. You can also add a priority node. For example, you can add the xmrchain.net node, which is 176.9.0.187 . Or any other node you trust. You can actually pick and choose random nodes from monero.fail , though those aren't guaranteed to be trustworthy either. 

## charlesmigel | 2025-02-09T02:18:20+00:00
@Gingeropolous 

im the same person and i tested it i get this    pool@pool-database:~/monero-x86_64-linux-gnu-v0.18.3.4$ ./monerod --add-priority-node 176.9.0.187
2025-02-09 02:16:39.764 I Monero 'Fluorine Fermi' (v0.18.3.4-release)
2025-02-09 02:16:39.764 I Initializing cryptonote protocol...
2025-02-09 02:16:39.764 I Cryptonote protocol initialized OK
2025-02-09 02:16:39.765 I Initializing core...
2025-02-09 02:16:39.765 I Loading blockchain from folder /home/pool/.bitmonero/lmdb ...
2025-02-09 02:16:39.950 E Transaction spends at least one output which is too young
2025-02-09 02:16:39.972 E Transaction spends at least one output which is too young
2025-02-09 02:16:40.260 E Transaction spends at least one output which is too young
2025-02-09 02:16:40.303 E Transaction spends at least one output which is too young
2025-02-09 02:16:40.319 I Loading checkpoints
2025-02-09 02:16:40.319 I Core initialized OK
2025-02-09 02:16:40.319 I Initializing p2p server...
2025-02-09 02:16:40.323 I p2p server initialized OK
2025-02-09 02:16:40.323 I Initializing core RPC server...
2025-02-09 02:16:40.323 I Binding on 127.0.0.1 (IPv4):18081
2025-02-09 02:16:40.324 I core RPC server initialized OK on port: 18081
2025-02-09 02:16:40.324 I Starting core RPC server...
2025-02-09 02:16:40.324 I core RPC server started ok
2025-02-09 02:16:40.325 I Starting p2p net loop...
2025-02-09 02:16:41.325 I 
2025-02-09 02:16:41.325 I **********************************************************************
2025-02-09 02:16:41.325 I The daemon will start synchronizing with the network. This may take a long time to complete.
2025-02-09 02:16:41.325 I 
2025-02-09 02:16:41.325 I You can set the level of process detailization through "set_log <level|categories>" command,
2025-02-09 02:16:41.325 I where <level> is between 0 (no details) and 4 (very verbose), or custom category based levels (eg, *:WARNING).
2025-02-09 02:16:41.325 I 
2025-02-09 02:16:41.325 I Use the "help" command to see the list of available commands.
2025-02-09 02:16:41.325 I Use "help <command>" to see a command's documentation.
2025-02-09 02:16:41.325 I **********************************************************************
2025-02-09 02:16:41.419 I [176.9.0.187:18080 OUT] Sync data returned a new top block candidate: 3255382 -> 3343527 [Your node is 88145 blocks (4.0 months) behind] 
2025-02-09 02:16:41.419 I SYNCHRONIZATION started

And also i deleted the p2pstate.bin


and is geting blocked all ips let me know

## selsta | 2025-02-09T10:18:04+00:00
Blocking all IPs is often a sign of corrupted blockchain, but it's not clear currently what causes the blockchain to corrupt. Did you force shutdown your computer inbetween? Do you sync to a network storage?

## charlesmigel | 2025-02-09T21:52:59+00:00
i have not an corrupted blockchain i have resync about 10 times with other network and pc and OS

i use nvme to storage the blockchain and the PC have been on all time

## charlesmigel | 2025-02-10T03:50:29+00:00
2025-02-10 02:14:56.408 [P2P2]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1697    Synced 2014336/334>
2025-02-10 02:14:56.444 [P2P2]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1697    Synced 2014356/334>
2025-02-10 02:14:56.482 [P2P2]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1697    Synced 2014376/334>
2025-02-10 02:14:56.526 [P2P2]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1697    Synced 2014396/334>
2025-02-10 02:14:56.571 [P2P2]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1697    Synced 2014416/334>
2025-02-10 02:14:56.632 [P2P2]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1697    Synced 2014436/334>
2025-02-10 02:14:56.670 [P2P2]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1697    Synced 2014456/334>
2025-02-10 02:14:56.709 [P2P2]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1697    Synced 2014476/334>
2025-02-10 02:14:56.716 [P2P2]  WARNING blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:75   Failed to get top block ha>
2025-02-10 02:14:56.719 [P2P2]  ERROR   blockchain      src/cryptonote_core/blockchain.cpp:4477 Error adding block with hash: <f67>
2025-02-10 02:15:00.650 [P2P1]  ERROR   blockchain.db   src/blockchain_db/blockchain_db.cpp:1034        Failed to get tx meta from>
2025-02-10 02:15:00.650 [P2P1]  ERROR   blockchain.db   src/blockchain_db/blockchain_db.cpp:1034        Failed to get tx meta from>
2025-02-10 02:15:00.650 [P2P1]  ERROR   blockchain.db   src/blockchain_db/blockchain_db.cpp:1034        Failed to get tx meta from>
2025-02-10 02:15:00.650 [P2P1]  ERROR   blockchain.db   src/blockchain_db/blockchain_db.cpp:1034        Failed to get tx meta from>
2025-02-10 02:15:00.650 [P2P1]  ERROR   blockchain.db   src/blockchain_db/blockchain_db.cpp:1034        Failed to get tx meta from>
2025-02-10 02:15:00.650 [P2P1]  ERROR   blockchain.db   src/blockchain_db/blockchain_db.cpp:1034        Failed to get tx meta from>
2025-02-10 02:15:00.650 [P2P1]  ERROR   blockchain.db   src/blockchain_db/blockchain_db.cpp:1034        Failed to get tx meta from>
2025-02-10 02:15:00.650 [P2P1]  ERROR   blockchain.db   src/blockchain_db/blockchain_db.cpp:1034        Failed to get tx meta from>
2025-02-10 02:15:00.650 [P2P1]  ERROR   blockchain.db   src/blockchain_db/blockchain_db.cpp:1034        Failed to get tx meta from>
2025-02-10 02:15:00.650 [P2P1]  ERROR   blockchain.db   src/blockchain_db/blockchain_db.cpp:1034        Failed to get tx meta from>
2025-02-10 02:15:00.650 [P2P1]  ERROR   blockchain.db   src/blockchain_db/blockchain_db.cpp:1034        Failed to get tx meta from>
2025-02-10 02:15:00.650 [P2P1]  ERROR   blockchain.db   src/blockchain_db/blockchain_db.cpp:1034        Failed to get tx meta from>
2025-02-10 02:15:00.650 [P2P1]  ERROR   blockchain.db   src/blockchain_db/blockchain_db.cpp:1034        Failed to get tx meta fr                THIS is the log from .bitmonero

## Cjdzo430 | 2025-04-20T11:10:34+00:00
> I tried to sync with the blockchain, but it doesn't work. I managed to sync up to block 3216307, and then it stops syncing.
> 
> I’ve tried switching the internet, turning off the firewall, and testing with another computer, but it still doesn’t work.
> 
> Here’s a video about the problem. Let me know if you guys can help me.
> 
>  Screencast.from.01.02.2025.15.56.08.webm

Have you resolved it?

# Action History
- Created by: xioney1263 | 2025-02-01T15:00:01+00:00
- Closed at: 2025-12-19T14:55:01+00:00
