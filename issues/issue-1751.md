---
title: Unable to generate genesis block!
source_url: https://github.com/monero-project/monero/issues/1751
author: nathansenn90
assignees: []
labels:
- invalid
created_at: '2017-02-19T13:04:12+00:00'
updated_at: '2020-12-06T11:50:58+00:00'
type: issue
status: closed
closed_at: '2017-08-13T16:00:12+00:00'
---

# Original Description
I am trying to run some experiments on my network using a monero clone but i'm unable to get the new genesis block to generate  
> 2017-02-19 14:43:39.891 4544    INFO    global  src/daemon/main.cpp:280 Monero 'Wolfram Warptangent' (v0.10.1.0-4b604b8)
2017-02-19 14:43:39.894 4544    INFO    global  src/daemon/protocol.h:55        Initializing cryptonote protocol...
2017-02-19 14:43:39.895 4544    INFO    global  src/daemon/protocol.h:60        Cryptonote protocol initialized OK
2017-02-19 14:43:39.898 4544    INFO    global  src/daemon/p2p.h:63     Initializing p2p server...
2017-02-19 14:43:41.362 4544    INFO    global  src/daemon/p2p.h:68     P2p server initialized OK
2017-02-19 14:43:41.363 4544    INFO    global  src/daemon/rpc.h:58     Initializing core rpc server...
2017-02-19 14:43:41.365 4544    INFO    global  src/daemon/rpc.h:63     Core rpc server initialized OK on port: 15306
2017-02-19 14:43:41.366 4544    INFO    global  src/daemon/core.h:74    Initializing core...
2017-02-19 14:43:41.370 4544    INFO    global  src/cryptonote_core/cryptonote_core.cpp:327     Loading blockchain from folder C:\ProgramData\Superior\lmdb ...
2017-02-19 14:43:41.421 4544    ERROR   blockchain      src/cryptonote_core/blockchain.cpp:334  Failed to add genesis block to blockchain
2017-02-19 14:43:41.422 4544    WARN    checkpoints     src/cryptonote_basic/checkpoints.cpp:266     WARNING: no two valid MoneroPulse DNS checkpoint records were received
2017-02-19 14:43:41.423 4544    WARN    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:71   batch transactions not enabled
2017-02-19 14:43:41.423 4544    FATAL   daemon  src/daemon/daemon.cpp:149       Uncaught exception! batch transactions not enabled
2017-02-19 14:43:41.424 4544    INFO    global  src/daemon/rpc.h:90     Deinitializing rpc server...
2017-02-19 14:43:41.425 4544    INFO    global  src/daemon/p2p.h:90     Deinitializing p2p...
2017-02-19 14:43:41.426 4544    INFO    global  src/daemon/core.h:90    Deinitializing core...
2017-02-19 14:43:41.477 4544    INFO    global  src/daemon/protocol.h:77        Stopping cryptonote protocol...
2017-02-19 14:43:41.478 4544    INFO    global  src/daemon/protocol.h:81        Cryptonote protocol stopped successfully



# Discussion History
## ghost | 2017-02-19T17:14:50+00:00
Please repeat at log level 2 

## nathansenn90 | 2017-02-19T18:20:27+00:00
C:\xampp\htdocs\superiorcoin\build\release\bin>Daemond set_log 2
2017-02-19 18:19:25.036 7228    ERROR   msgwriter       src/common/scoped_message_writer.h:94   Error: Couldn't connect to daemon
Error: Couldn't connect to daemon

## ghost | 2017-02-20T09:24:10+00:00
Correct syntax is `monerod --log-level=2`

And I don't think we should be supporting questions about building a clone coin on this issue tracker. 
The following stack exchange article may be of interest:

http://monero.stackexchange.com/questions/2886/how-can-i-create-a-new-monero-genesis-block

## moneroexamples | 2017-02-20T21:37:32+00:00
Maybe this will help you. It shows how to make private monero testnet network for playing around with monero indepnedently of its real mainnet and public testnet:

- https://github.com/moneroexamples/private-testnet



## nathansenn90 | 2017-02-21T17:09:02+00:00
How are these numbers in the genesis_tx hashed and how would i go about modifying them?

> version
01
unlock time (varint, height, 60 here)
3c
vin length (value in)
01
vin #1 (of 1) type (gen, 0xff)
ff
height for gen input
00
vout length (value out)
01
output #1 (of 1) amount (17592186044415 as varint)
ffffffffffff03
output #1 type (to key, 0x02)
02
output #1 key (32 bytes)
9b2e4c0281c0b02e7c53291a94d1d0cbff8883f8024f5142ee494ffbbd088071
extra length in bytes (varint, here 33)
21
extra pubkey tag (0x01)
01
transaction pubkey (32 bytes)
7767aafcde9be00dcfd098715ebcf7f410daebc582fda69d24a28e9d0bc890d1

## ghost | 2017-02-21T20:47:33+00:00
We can't help you with this. Please ask on stack exchange.

## moneromooo-monero | 2017-08-13T15:45:04+00:00
+invalid
+resolved

## uwxpro | 2020-03-30T01:25:07+00:00
> We can't help you with this. Please ask on stack exchange.

The correct reply is not that we can't help but no one wants to help you with this, because most people here pretend to know but they dont!!

## trasherdk | 2020-03-30T05:01:50+00:00
All the information is already on stack exchange.

Go to [Monero Genesis transaction & nonce - clarification](https://monero.stackexchange.com/questions/9917/monero-genesis-transaction-nonce-clarification)

Start from there, and the linked answers. It's not impossible. If I could do it, anybody can.

PS: **When asking for help, it's not a good idea to be rude.**

## IvRRimum | 2020-12-06T11:50:57+00:00
> How are these numbers in the genesis_tx hashed and how would i go about modifying them?
> 
> > version
> > 01
> > unlock time (varint, height, 60 here)
> > 3c
> > vin length (value in)
> > 01
> > vin #1 (of 1) type (gen, 0xff)
> > ff
> > height for gen input
> > 00
> > vout length (value out)
> > 01
> > output #1 (of 1) amount (17592186044415 as varint)
> > ffffffffffff03
> > output #1 type (to key, 0x02)
> > 02
> > output #1 key (32 bytes)
> > 9b2e4c0281c0b02e7c53291a94d1d0cbff8883f8024f5142ee494ffbbd088071
> > extra length in bytes (varint, here 33)
> > 21
> > extra pubkey tag (0x01)
> > 01
> > transaction pubkey (32 bytes)
> > 7767aafcde9be00dcfd098715ebcf7f410daebc582fda69d24a28e9d0bc890d1

For others 3c(unlock time) is meant as hexadecimal. 60 = 3c in HEX.
Spent some time on this...

# Action History
- Created by: nathansenn90 | 2017-02-19T13:04:12+00:00
- Closed at: 2017-08-13T16:00:12+00:00
