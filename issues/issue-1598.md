---
title: 'MDB_NOTFOUND: No matching key/data pair found'
source_url: https://github.com/monero-project/monero/issues/1598
author: moneroexamples
assignees: []
labels: []
created_at: '2017-01-20T02:30:39+00:00'
updated_at: '2025-04-23T14:34:44+00:00'
type: issue
status: closed
closed_at: '2017-04-04T23:04:29+00:00'
---

# Original Description
Recently. i've been getting frequenty those errors. 
```
2017-01-20 02:27:13.718	    7fcf21340b80	WARN 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:71	Error attempting to retrieve a hard fork version at height 1227592 from the db: MDB_NOTFOUND: No matching key/data pair found
terminate called after throwing an instance of 'cryptonote::DB_ERROR'
  what():  Error attempting to retrieve a hard fork version at height 1227592 from the db: MDB_NOTFOUND: No matching key/data pair found
```

The problem is that once this error occurs, daemon will not work anymore. It just crashes with the error shown below, and resycing of the blockchain is required, or recovering it from the backup, if someone has.

```
2017-01-20 02:29:31.384	    7f0bc8290780	WARN 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:71	Error attempting to retrieve a hard fork version at height 1227592 from the db: MDB_NOTFOUND: No matching key/data pair found
2017-01-20 02:29:31.387	    7f0bc8290780	FATAL	daemon	src/daemon/daemon.cpp:147	Uncaught exception! Error attempting to retrieve a hard fork version at height 1227592 from the db: MDB_NOTFOUND: No matching key/data pair found
```

Has anyone experienced this issue? What is the cause of it?

# Discussion History
## moneromooo-monero | 2017-01-20T19:01:12+00:00
Are you running this on Windows, and did your OS crash ?

## moneroexamples | 2017-01-21T01:32:43+00:00
No. I use  Linux (Majnaro now). Had this issue on two boxes. In all cases I just restored my blockchain from backup, and it was working for a while, till it crashed again. But after last time, I decided to resync it from scratch, and see how it goes with fresh blockchain. 

Do you know what does it mean? Is it corrupted lmdb data files or something else? 

## moneromooo-monero | 2017-01-21T11:10:28+00:00
It seems corrupt. You might be able to restore by popping N blocks (blockchain_import --pop-blocks N) and restarting.

## moneroexamples | 2017-01-22T00:20:13+00:00
Its same on freshly sync block from scrached. Worked for a one day, and then this error:

```
2017-01-22 08:15:53.960	[P2P0]	WARN 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:71Failed to add tx blob to db transaction: MDB_KEYEXIST: Key/data pair already exists
2017-01-22 08:15:53.964	[P2P0]	ERROR	blockchain	src/cryptonote_core/blockchain.cpp:3309	Error adding block with hash: <d922236c6ac32625df8d245d85953ac575b4312162342abf49c8d4eb2e28860b> to blockchain, what = Failed to add tx blob to db transaction: MDB_KEYEXIST: Key/data pair already exists
2017-01-22 08:16:23.125	[RPC0]	ERROR	blockchain	src/cryptonote_core/blockchain.cpp:2029	internal error, transaction from block not found
2017-01-22 08:16:35.800	[P2P8]	WARN 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:71Failed to add tx blob to db transaction: MDB_KEYEXIST: Key/data pair already exists
2017-01-22 08:16:35.803	[P2P8]	ERROR	blockchain	src/cryptonote_core/blockchain.cpp:3309	Error adding block with hash: <b75571fa17787ad0c0fb051f60e2db3fee8fe04cc6d78b25ab2955ab1375aa10> to blockchain, what = Failed to add tx blob to db transaction: MDB_KEYEXIST: Key/data pair already exists
2017-01-22 08:17:53.208	[RPC1]	ERROR	blockchain	src/cryptonote_core/blockchain.cpp:2029	internal error, transaction from block not found
```

And daemon wont work anymore at all like before. 

Btw these errors started occurring maybe 1 week ago. So my guess is that some changes in marged pull requests at that time cause this.

## moneromooo-monero | 2017-01-22T10:06:30+00:00
Do you have https://github.com/monero-project/monero/pull/1584 ?

## hyc | 2017-01-22T13:54:12+00:00
What git revision is the source you built from?

## moneroexamples | 2017-01-22T21:05:15+00:00
@moneromooo-monero 

Yes I have #1584. 

@hyc 
I always run the latest monero development version. 

## kumrzz | 2017-01-31T03:51:49+00:00
I cloned the git and built on 11jan2017 (no issues with that build) but did the same thing on the latest version of the github repo(new VM) but am getting these exact same errors `MDB_NOTFOUND: No matching key/data pair found` ... the timing and nature of these errors cannot be a coincidence: pretty sure something in the repo has fessed up around mid-Jan.

## hyc | 2017-01-31T09:26:38+00:00
@moneroexamples That is not an answer. The "latest" version keeps changing. I asked you for a specific git revision ID.

## moneroexamples | 2017-02-14T08:52:28+00:00
It happened again. The error occured and lmdb seems to be corrupted as  daemon wont start. Need to resync from scrach or get blockchain from backup.

Monero version: v0.10.1.0-cb54eeaa

```
2017-02-14 16:49:56.650	    7ff41283bd80	WARN 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:71	Error attempting to retrieve a hard fork version at height 1244280 from the db: MDB_NOTFOUND: No matching key/data pair found
2017-02-14 16:49:56.651	    7ff41283bd80	FATAL	daemon	src/daemon/daemon.cpp:149	Uncaught exception! Error attempting to retrieve a hard fork version at height 1244280 from the db: MDB_NOTFOUND: No matching key/data pair found
```



## amiuhle | 2017-02-28T00:39:36+00:00
I just stumbled over the same error getting `monerod` running in a Docker container.

I'm trying to run the following `docker-compose.yml`:

```yml
version: '2'
services:
  monerod:
    build: ./monero
    entrypoint: ['monerod', '--testnet']
```

in this directory:  
https://github.com/amiuhle/monero-docker/tree/fd1347573c8fd6a71f4c0c8b4f5d5e5227a82917

```
monerod_1  | 2017-02-28 00:31:07.265        7f7cd3265740        INFO    global  contrib/epee/src/mlog.cpp:145   New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,global:INFO,verify:FATAL,stacktrace:INFO
monerod_1  | 2017-02-28 00:31:07.265        7f7cd3265740        INFO    global  src/daemon/main.cpp:282 Monero 'Wolfram Warptangent' (v0.10.2.1-release)
monerod_1  | 2017-02-28 00:31:07.266        7f7cd3265740        INFO    global  src/daemon/protocol.h:55        Initializing cryptonote protocol...
monerod_1  | 2017-02-28 00:31:07.266        7f7cd3265740        INFO    global  src/daemon/protocol.h:60        Cryptonote protocol initialized OK
monerod_1  | 2017-02-28 00:31:07.266        7f7cd3265740        INFO    global  src/daemon/p2p.h:63     Initializing p2p server...
monerod_1  | 2017-02-28 00:31:11.272        7f7cd3265740        INFO    global  src/daemon/p2p.h:68     P2p server initialized OK
monerod_1  | 2017-02-28 00:31:11.272        7f7cd3265740        INFO    global  src/daemon/rpc.h:58     Initializing core rpc server...
monerod_1  | 2017-02-28 00:31:11.272        7f7cd3265740        INFO    global  contrib/epee/include/net/http_server_impl_base.h:70     Binding on 127.0.0.1:28081
monerod_1  | 2017-02-28 00:31:11.273        7f7cd3265740        INFO    global  src/daemon/rpc.h:63     Core rpc server initialized OK on port: 28081
monerod_1  | 2017-02-28 00:31:11.273        7f7cd3265740        INFO    global  src/daemon/core.h:73    Initializing core...
monerod_1  | 2017-02-28 00:31:11.274        7f7cd3265740        INFO    global  src/cryptonote_core/cryptonote_core.cpp:316     Loading blockchain from folder /root/.bitmonero/testnet/lmdb ...
monerod_1  | 2017-02-28 00:31:11.277        7f7cd3265740        WARN    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:71   Error attempting to retrieve a hard fork version at height 0 from the db: MDB_NOTFOUND: No matching key/data pair found
monerod_1  | 2017-02-28 00:31:11.410        7f7cd3265740        INFO    global  src/daemon/core.h:78    Core initialized OK
monerod_1  | 2017-02-28 00:31:11.410        7f7cd3265740        INFO    global  src/daemon/rpc.h:68     Starting core rpc server...
monerod_1  | 2017-02-28 00:31:11.410    [SRV_MAIN]      INFO    global  src/daemon/rpc.h:73     Core rpc server started ok
monerod_1  | 2017-02-28 00:31:11.411    [SRV_MAIN]      INFO    global  src/daemon/p2p.h:78     Starting p2p net loop...
monerod_1  | 2017-02-28 00:31:11.411    [SRV_MAIN]      INFO    global  src/daemon/p2p.h:80     p2p net loop stopped
monerod_1  | 2017-02-28 00:31:11.411    [SRV_MAIN]      INFO    global  src/daemon/rpc.h:78     Stopping core rpc server...
monerod_1  | 2017-02-28 00:31:11.411    [SRV_MAIN]      INFO    global  src/daemon/daemon.cpp:145       Node stopped.
monerod_1  | 2017-02-28 00:31:11.411    [SRV_MAIN]      INFO    global  src/daemon/rpc.h:90     Deinitializing rpc server...
monerod_1  | 2017-02-28 00:31:11.411    [SRV_MAIN]      INFO    global  src/daemon/p2p.h:90     Deinitializing p2p...
monerod_1  | 2017-02-28 00:31:12.412    [SRV_MAIN]      INFO    global  src/daemon/core.h:89    Deinitializing core...
monerod_1  | 2017-02-28 00:31:12.418    [SRV_MAIN]      INFO    global  src/daemon/protocol.h:77        Stopping cryptonote protocol...
monerod_1  | 2017-02-28 00:31:12.418    [SRV_MAIN]      INFO    global  src/daemon/protocol.h:81        Cryptonote protocol stopped successfully
monerod_1  | Daemon stopped successfully
```

I'm still struggling with Docker, so maybe I'm just doing something wrong, but I thought this might pin down the problem.

## hyc | 2017-02-28T01:31:29+00:00
That's pretty weird, because if you ever get this error message "Error attempting to retrieve a hard fork version at height 0" the next thing you *should* see is "The DB has no hard fork info, reparsing from start" and that message isn't here.

## amiuhle | 2017-02-28T11:14:27+00:00
> I'm still struggling with Docker, so maybe I'm just doing something wrong

Yeah, I think that's the case. My problem doesn't seem to be related to this issue, so never mind.

## spaquin | 2017-03-02T01:47:53+00:00
I obtain the same issue on a fresh install on OpenBSD 6.0 (yes, with some patching)

2017-03-01 20:42:20.607        0x2705652f4e0        INFO    global  contrib/epee/src/mlog.cpp:145   New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,global:INFO,verify:FATAL,stacktrace:INFO
2017-03-01 20:42:20.608     0x2705652f4e0        ERROR   default contrib/epee/src/mlog.cpp:179   Invalid numerical log level: 5
2017-03-01 20:42:20.608     0x2705652f4e0        INFO    global  src/daemon/main.cpp:282 Monero 'Wolfram Warptangent' (v0.10.2.1-release)
2017-03-01 20:42:20.608     0x2705652f4e0        INFO    global  src/daemon/protocol.h:55        Initializing cryptonote protocol...
2017-03-01 20:42:20.608     0x2705652f4e0        INFO    global  src/daemon/protocol.h:60        Cryptonote protocol initialized OK
2017-03-01 20:42:20.609     0x2705652f4e0        INFO    global  src/daemon/p2p.h:63     Initializing p2p server...
2017-03-01 20:42:24.266     0x2705652f4e0        INFO    global  src/daemon/p2p.h:68     P2p server initialized OK
2017-03-01 20:42:24.268     0x2705652f4e0        INFO    global  src/daemon/rpc.h:58     Initializing core rpc server...
2017-03-01 20:42:24.268     0x2705652f4e0        INFO    global  contrib/epee/include/net/http_server_impl_base.h:70     Binding on 127.0.0.1:18081
2017-03-01 20:42:24.268     0x2705652f4e0        INFO    global  src/daemon/rpc.h:63     Core rpc server initialized OK on port: 18081
2017-03-01 20:42:24.268     0x2705652f4e0        INFO    global  src/daemon/core.h:73    Initializing core...
2017-03-01 20:42:24.269     0x2705652f4e0        INFO    global  src/cryptonote_core/cryptonote_core.cpp:316     Loading blockchain from folder /var/monero/lmdb ...
2017-03-01 20:42:24.279     0x2705652f4e0        WARN    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:71   Error attempting to retrieve a hard fork version at height 0 from the db: MDB_NOTFOUND: No matching key/data pair found
2017-03-01 20:42:24.337     0x2705652f4e0        ERROR   blockchain      src/cryptonote_core/blockchain.cpp:3360 Error adding block with hash: <418015bb9ae982a1975da7d79277c2705727a56894ba0fb246adaabb1f4632e3> to blockchain, what = Error adding hard fork version to db transaction: MDB_NOTFOUND: No matching key/data pair found
2017-03-01 20:42:24.341     0x2705652f4e0        WARN    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:71   Attempt to get hash from height 0 failed -- hash not in db
2017-03-01 20:42:24.342     0x2705652f4e0        FATAL   daemon  src/daemon/daemon.cpp:150       Uncaught exception! Attempt to get hash from height 0 failed -- hash not in db
2017-03-01 20:42:24.343     0x2705652f4e0        INFO    global  src/daemon/rpc.h:90     Deinitializing rpc server...
2017-03-01 20:42:24.344     0x2705652f4e0        INFO    global  src/daemon/p2p.h:90     Deinitializing p2p...
2017-03-01 20:42:24.346     0x2705652f4e0        INFO    global  src/daemon/core.h:89    Deinitializing core...
2017-03-01 20:42:24.351     0x2705652f4e0        INFO    global  src/daemon/protocol.h:77        Stopping cryptonote protocol...
2017-03-01 20:42:24.352     0x2705652f4e0        INFO    global  src/daemon/protocol.h:81        Cryptonote protocol stopped successfully


## Kukunin | 2017-03-04T16:31:34+00:00
To workaround monero run in docker, use `-i` flag on `docker run`; or `stdin_open: true` option for `docker-compose`

## moneroexamples | 2017-04-04T23:04:29+00:00
I close it, as it seems to be ok now. Havent had this problem for a while now.

## ghost | 2017-06-09T22:50:21+00:00
This is a request to re-open.
Compiled from git using commit `fa489a2` and built using `make -j 12` on 12 cores and 20GB of RAM, and have received the same issue.

Pardon the image, as I cannot paste from ESXi.
http://imgur.com/a/pZqAp
@moneroexamples @monero-project 


## MoroccanMalinois | 2017-08-28T00:50:38+00:00
@ghost :  It's actually a warning and not an error, because it's a new data-dir.

## fafato1 | 2025-04-22T05:32:53+00:00
2025-04-22 05:32:33.709 I Loading blockchain from folder "C:\ProgramData\bitmonero\lmdb-pruned" ...
2025-04-22 05:32:33.797 W Error attempting to retrieve a hard fork version at height 320879 from the db: MDB_NOTFOUND: No matching key/data pair found
2025-04-22 05:32:33.863 E Exception at [Pruning error], what=Error attempting to retrieve a hard fork version at height 320879 from the db: MDB_NOTFOUND: No matching key/data pair found

I'm having this issue!

## selsta | 2025-04-23T14:34:42+00:00
@fafato1 this appears to be a corrupt database, please delete the blockchain and sync from scratch

# Action History
- Created by: moneroexamples | 2017-01-20T02:30:39+00:00
- Closed at: 2017-04-04T23:04:29+00:00
