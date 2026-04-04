---
title: Monero ARMv8 stalls on Raspberry Pi 4
source_url: https://github.com/monero-project/monero/issues/6313
author: TheRoarkster
assignees: []
labels: []
created_at: '2020-01-30T19:47:43+00:00'
updated_at: '2020-01-31T18:29:57+00:00'
type: issue
status: closed
closed_at: '2020-01-31T18:29:56+00:00'
---

# Original Description
I downloaded the ARMv8 for the Raspberry Pi 4 and ran `./monerod --stagenet --block-sync-size 10 --detach --data-dir /mnt/Encrypted_USB/Monero/` to start syncing.  Monero created a directory `stagenet` in the data directory denoted.  In the `lmdb` subdiretory, the `data.mdb` file stalls at 16384 bytes.

Here is the log from : 
`tail -f /mnt/Encrypted_USB/Monero/stagenet/bitmonero.log`
```
2020-01-30 19:35:56.593	      7fb62b8010	INFO	logging	contrib/epee/src/mlog.cpp:273New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
2020-01-30 19:35:56.594	      7fb62b8010	INFO	global	src/daemon/main.cpp:271	Monero 'Carbon Chamaeleon' (v0.15.0.1-release)
2020-01-30 19:35:56.594	      7fb62b8010	INFO	msgwriter	src/common/scoped_message_writer.h:102	Forking to background...
2020-01-30 19:35:56.596	      7fb62b8010	WARNING	daemon	src/daemon/executor.cpp:61	Monero 'Carbon Chamaeleon' (v0.15.0.1-release) Daemonised
2020-01-30 19:35:56.596	      7fb62b8010	INFO	global	src/daemon/protocol.h:53	Initializing cryptonote protocol...
2020-01-30 19:35:56.596	      7fb62b8010	INFO	global	src/daemon/protocol.h:58	Cryptonote protocol initialized OK
2020-01-30 19:35:56.598	      7fb62b8010	INFO	global	src/daemon/core.h:63	Initializing core...
2020-01-30 19:35:56.599	      7fb62b8010	INFO	global	src/cryptonote_core/cryptonote_core.cpp:506	Loading blockchain from folder /mnt/Encrypted_USB/Monero/stagenet/lmdb ...
2020-01-30 19:35:56.599	      7fb62b8010	WARNING	global	src/blockchain_db/lmdb/db_lmdb.cpp:1318	The blockchain is on a rotating drive: this will be very slow, use an SSD if possible
```
The USB used for the database is v3.0 and is in the Pi's USB 3.0 slot.  




# Discussion History
## vtnerd | 2020-01-31T00:04:59+00:00
Ping @hyc @TheCharlatan in case the build information is incorrect.

The Armv8 build uses AES crypto-extensions, and the [Raspberry Pi 4 does not come with those additional instructions](https://www.raspberrypi.org/forums/viewtopic.php?t=243410). So you should be stuck at the genesis block.

You will probably need a custom build for the RPi4 or switch the OS/ABI entirely.

## hyc | 2020-01-31T10:59:01+00:00
@vtnerd is correct.

## TheRoarkster | 2020-01-31T18:29:56+00:00
That is unfortunate.   But appreciate the knowledge.  

# Action History
- Created by: TheRoarkster | 2020-01-30T19:47:43+00:00
- Closed at: 2020-01-31T18:29:56+00:00
