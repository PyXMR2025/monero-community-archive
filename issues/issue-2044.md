---
title: Can't launch Daemon on macOS with v0.14.0.0 ?!
source_url: https://github.com/monero-project/monero-gui/issues/2044
author: krrkrr
assignees: []
labels: []
created_at: '2019-03-29T12:00:53+00:00'
updated_at: '2019-03-31T12:35:48+00:00'
type: issue
status: closed
closed_at: '2019-03-31T12:35:47+00:00'
---

# Original Description
Hi...

I'm on a mac 2012 on Sierra (10.12) and I had no pb with the previous version on the monero wallet. When I try to launch the v0.14.0.0, I can't connect to the daemon... because it crashes.

If I try to launch the daemon manually, I got this:

> 2019-03-29 11:57:39.037	  0x7fffa0135380	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:469	Loading blockchain from folder /Users/insextcl/.bitmonero/lmdb ...
2019-03-29 11:57:39.149	  0x7fffa0135380	WARN 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:76	Failed to find txpool tx blob to match metadata
2019-03-29 11:57:39.149	  0x7fffa0135380	FATAL	daemon	src/daemon/daemon.cpp:207	Uncaught exception! Failed to find txpool tx blob to match metadata


What can I do ?

Thanks !!

# Discussion History
## dEBRUYNE-1 | 2019-03-29T13:09:17+00:00
That typically indicates a corrupted blockchain. I'd advise to delete `data.mdb` from `/Users/insextcl/.bitmonero/lmdb` and perform a blockchain resync from scratch. As a side note, did you incur an unexpected shutdown (e.g. power outage or system crash) whilst `monerod` was running? 


## krrkrr | 2019-03-29T23:51:58+00:00
I've deleted data.mdb ... and re-sync from scratch... now, several hours, the daemon can't launch itself again... errors are:
2019-03-29 23:49:15.534	  0x7fffa0135380	FATAL	net	contrib/epee/include/net/abstract_tcp_server2.inl:856	Error starting server: bind: Address already in use
2019-03-29 23:49:15.536	  0x7fffa0135380	INFO 	global	src/daemon/core.h:103	Deinitializing core...
2019-03-29 23:49:15.536	  0x7fffa0135380	ERROR	daemon	src/daemon/core.h:108	Failed to deinitialize core...
2019-03-29 23:49:15.536	  0x7fffa0135380	INFO 	global	src/daemon/protocol.h:75	Stopping cryptonote protocol...
2019-03-29 23:49:15.536	  0x7fffa0135380	INFO 	global	src/daemon/protocol.h:79	Cryptonote protocol stopped successfully
2019-03-29 23:49:15.536	  0x7fffa0135380	ERROR	daemon	src/daemon/main.cpp:295	Exception in main! Failed to initialize p2p server.



## selsta | 2019-03-30T00:16:46+00:00
It means a daemon is already running on your system. You can exit the daemon with `./monerod exit` or you can restart your Mac.

## krrkrr | 2019-03-30T00:17:14+00:00
OK... I get it... for some reason, the daemon doesn't quit normally... I had to force-quit it. The sync process is going on... 

## krrkrr | 2019-03-30T00:18:08+00:00
but anyway, for some reason, the wallet was unable to connect to the daemon... until I force-quit and then re-launch the daemon... 

## krrkrr | 2019-03-31T12:35:47+00:00
ok it's done.

# Action History
- Created by: krrkrr | 2019-03-29T12:00:53+00:00
- Closed at: 2019-03-31T12:35:47+00:00
