---
title: Segmentation fault on monerod in Ubuntu 17.04 (backtrace included)
source_url: https://github.com/monero-project/monero/issues/2490
author: demrepofdave
assignees: []
labels: []
created_at: '2017-09-20T08:54:58+00:00'
updated_at: '2017-09-22T09:48:26+00:00'
type: issue
status: closed
closed_at: '2017-09-22T09:48:26+00:00'
---

# Original Description
I believe this could be the same issue as #2449.

I upgraded my monero binaries to the latest v0.11 release binary and ran monerod to resync.
About 20 minutes in the sync seemed to stall (sorry I do not have any screencaps of that), just messages informing me when a new block had been added to the top of the blockchain.

Left for 20 minutes.  Then exited monerod and ran again, at which point I got a segfault.

I have built the v0.11 branch with debug and ran monerod with gdb and captured the crash..
```
GNU gdb (Ubuntu 7.12.50.20170314-0ubuntu1.1) 7.12.50.20170314-git
Copyright (C) 2017 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
and "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
<http://www.gnu.org/software/gdb/documentation/>.
For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from ./monerod...done.
(gdb) run
Starting program: /home/dmorrison/code/monero/build/debug/bin/monerod 
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
2017-09-20 08:35:05.489	    7ffff7fca100	INFO 	global	src/daemon/main.cpp:282	Monero 'Helium Hydra' (v0.11.0.0-1a73843c)
2017-09-20 08:35:05.489	    7ffff7fca100	INFO 	global	src/daemon/protocol.h:55	Initializing cryptonote protocol...
2017-09-20 08:35:05.489	    7ffff7fca100	INFO 	global	src/daemon/protocol.h:60	Cryptonote protocol initialized OK
[New Thread 0x7fffefe4b700 (LWP 12692)]
[New Thread 0x7fffef94a700 (LWP 12693)]
2017-09-20 08:35:05.490	    7ffff7fca100	INFO 	global	src/daemon/p2p.h:63	Initializing p2p server...
[New Thread 0x7fffef449700 (LWP 12694)]
[New Thread 0x7fffeec48700 (LWP 12695)]
[New Thread 0x7fffee447700 (LWP 12696)]
[New Thread 0x7fffedc46700 (LWP 12697)]
[Thread 0x7fffeec48700 (LWP 12695) exited]
[Thread 0x7fffef449700 (LWP 12694) exited]
[Thread 0x7fffee447700 (LWP 12696) exited]
[Thread 0x7fffedc46700 (LWP 12697) exited]
2017-09-20 08:35:13.259	    7ffff7fca100	INFO 	global	src/daemon/p2p.h:68	P2p server initialized OK
2017-09-20 08:35:13.259	    7ffff7fca100	INFO 	global	src/daemon/rpc.h:58	Initializing core rpc server...
2017-09-20 08:35:13.259	    7ffff7fca100	INFO 	global	contrib/epee/include/net/http_server_impl_base.h:70	Binding on 127.0.0.1:18081
2017-09-20 08:35:13.259	    7ffff7fca100	INFO 	global	src/daemon/rpc.h:63	Core rpc server initialized OK on port: 18081
2017-09-20 08:35:13.259	    7ffff7fca100	INFO 	global	src/daemon/core.h:73	Initializing core...
2017-09-20 08:35:13.260	    7ffff7fca100	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:321	Loading blockchain from folder /home/dmorrison/.bitmonero/lmdb ...
2017-09-20 08:35:13.306	    7ffff7fca100	WARN 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1155	LMDB memory map needs to be resized, doing that now.
2017-09-20 08:35:13.306	    7ffff7fca100	INFO 	global	src/blockchain_db/lmdb/db_lmdb.cpp:494	LMDB Mapsize increased.  Old: 37888MiB, New: 38912MiB
2017-09-20 08:35:27.326	    7ffff7fca100	INFO 	global	src/blockchain_db/lmdb/db_lmdb.cpp:578	[batch] DB resize needed
2017-09-20 08:35:27.327	    7ffff7fca100	INFO 	global	src/blockchain_db/lmdb/db_lmdb.cpp:494	LMDB Mapsize increased.  Old: 38912MiB, New: 39936MiB
[New Thread 0x7fffedc46700 (LWP 12699)]
2017-09-20 08:35:40.179	    7ffff7fca100	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:419	Loading checkpoints
2017-09-20 08:35:40.609	    7ffff7fca100	WARN 	net.dns	src/common/dns_utils.cpp:487	WARNING: no two valid MoneroPulse DNS checkpoint records were received
2017-09-20 08:35:41.085	    7ffff7fca100	INFO 	global	src/daemon/core.h:78	Core initialized OK
2017-09-20 08:35:41.086	    7ffff7fca100	INFO 	global	src/daemon/rpc.h:68	Starting core rpc server...
[New Thread 0x7fffee447700 (LWP 12700)]
[New Thread 0x7fffeec48700 (LWP 12701)]
2017-09-20 08:35:41.086	[SRV_MAIN]	INFO 	global	src/daemon/rpc.h:73	Core rpc server started ok
[New Thread 0x7fffef449700 (LWP 12702)]
[New Thread 0x7fffed244700 (LWP 12703)]
[New Thread 0x7fffeca43700 (LWP 12704)]
[New Thread 0x7fffdffff700 (LWP 12705)]
[New Thread 0x7fffdf7fe700 (LWP 12706)]
2017-09-20 08:35:41.100	[SRV_MAIN]	INFO 	global	src/daemon/p2p.h:78	Starting p2p net loop...
[New Thread 0x7fffdeffd700 (LWP 12707)]
[New Thread 0x7fffde7fc700 (LWP 12708)]
[New Thread 0x7fffde2fb700 (LWP 12709)]
[New Thread 0x7fffdddfa700 (LWP 12710)]
[New Thread 0x7fffdd8f9700 (LWP 12711)]
[New Thread 0x7fffdd3f8700 (LWP 12712)]
[New Thread 0x7fffdcef7700 (LWP 12713)]
[New Thread 0x7fffdc9f6700 (LWP 12714)]
[New Thread 0x7ff613ffe700 (LWP 12715)]
[New Thread 0x7ff613afd700 (LWP 12716)]
[New Thread 0x7ff6135fc700 (LWP 12717)]
2017-09-20 08:35:42.101	[P2P1]	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:1256	
**********************************************************************
The daemon will start synchronizing with the network. This may take a long time to complete.

You can set the level of process detailization* through "set_log <level|categories>" command*,
where <level> is between 0 (no details) and 4 (very verbose), or custom category based levels (eg, *:WARNING)

Use the "help" command to see the list of available commands.
**********************************************************************

2017-09-20 08:35:42.371	[P2P1]	WARN 	net.dns	src/common/dns_utils.cpp:487	WARNING: no two valid MoneroPulse DNS checkpoint records were received
2017-09-20 08:35:43.168	[P2P5]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:305	[90.149.55.202:18080 OUT] Sync data returned a new top block candidate: 1389801 -> 1403044 [Your node is 13243 blocks (18 days) behind] 
SYNCHRONIZATION started

Thread 18 "monerod" received signal SIGSEGV, Segmentation fault.
[Switching to Thread 0x7fffde2fb700 (LWP 12709)]
__memcmp_sse4_1 () at ../sysdeps/x86_64/multiarch/memcmp-sse4.S:1525
1525	../sysdeps/x86_64/multiarch/memcmp-sse4.S: No such file or directory.
```

I have attached full backtraces for all threads in the backtrace.txt file.

The interesting part of the backtrace is the following....
```
#0  __memcmp_sse4_1 () at ../sysdeps/x86_64/multiarch/memcmp-sse4.S:1525
#1  0x00007ffff65952f5 in cryptonote::Blockchain::handle_block_to_main_chain (this=this@entry=0x555558566848, bl=..., id=..., bvc=...) at /home/dmorrison/code/monero/src/cryptonote_core/blockchain.cpp:3361
#2  0x00007ffff659b996 in cryptonote::Blockchain::add_new_block (this=this@entry=0x555558566848, bl_=..., bvc=...) at /home/dmorrison/code/monero/src/cryptonote_core/blockchain.cpp:3508
#3  0x00007ffff65bc08c in cryptonote::core::add_new_block (this=this@entry=0x555558566750, b=..., bvc=...) at /home/dmorrison/code/monero/src/cryptonote_core/cryptonote_core.cpp:1079
```

I will look at the code myself if I get time, but I've got to get on with my day job now.

Thanks,

Dave
[backtrace.txt](https://github.com/monero-project/monero/files/1317139/backtrace.txt)


# Discussion History
## moneromooo-monero | 2017-09-20T09:39:47+00:00
Yes, I've seen that same trace before. And yours has the actual line of the crash, that helps a lot,  thanks! Will fix.

## demrepofdave | 2017-09-20T09:45:23+00:00
Sure, no probs.

## moneromooo-monero | 2017-09-20T09:48:40+00:00
https://github.com/monero-project/monero/pull/2492

## demrepofdave | 2017-09-20T13:07:00+00:00
Hi moneromooo.

Tested the fix and there is no crash now, thanks.

However my daemon is still stuck on sync, but that is another issue.

Dave

## moneromooo-monero | 2017-09-20T13:50:59+00:00
Restart with --log-level 1, and wait till you get some sync related errors.

## moneromooo-monero | 2017-09-22T09:46:51+00:00
+resolved

# Action History
- Created by: demrepofdave | 2017-09-20T08:54:58+00:00
- Closed at: 2017-09-22T09:48:26+00:00
