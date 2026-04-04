---
title: monerod crashed while trying to sync for the first time , with the error segmentation
  fault  ,
source_url: https://github.com/monero-project/monero/issues/2911
author: altafhussain1
assignees: []
labels: []
created_at: '2017-12-11T21:31:43+00:00'
updated_at: '2017-12-25T18:08:24+00:00'
type: issue
status: closed
closed_at: '2017-12-25T18:08:24+00:00'
---

# Original Description
2017-12-11 21:29:48.091	    7f8cefb6f740	INFO 	global	src/daemon/main.cpp:282	Monero 'Helium Hydra' (v0.11.0.0-release)
2017-12-11 21:29:48.091	    7f8cefb6f740	INFO 	global	src/daemon/protocol.h:55	Initializing cryptonote protocol...
2017-12-11 21:29:48.091	    7f8cefb6f740	INFO 	global	src/daemon/protocol.h:60	Cryptonote protocol initialized OK
2017-12-11 21:29:48.092	    7f8cefb6f740	INFO 	global	src/daemon/p2p.h:63	Initializing p2p server...
2017-12-11 21:29:49.818	    7f8cefb6f740	INFO 	global	src/daemon/p2p.h:68	P2p server initialized OK
2017-12-11 21:29:49.818	    7f8cefb6f740	INFO 	global	src/daemon/rpc.h:58	Initializing core rpc server...
2017-12-11 21:29:49.818	    7f8cefb6f740	INFO 	global	contrib/epee/include/net/http_server_impl_base.h:70	Binding on 127.0.0.1:18081
2017-12-11 21:29:49.818	    7f8cefb6f740	INFO 	global	src/daemon/rpc.h:63	Core rpc server initialized OK on port: 18081
2017-12-11 21:29:49.818	    7f8cefb6f740	INFO 	global	src/daemon/core.h:73	Initializing core...
2017-12-11 21:29:49.819	    7f8cefb6f740	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:321	Loading blockchain from folder /root/.bitmonero/lmdb ...
2017-12-11 21:29:49.819	    7f8cefb6f740	WARN 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1155	LMDB memory map needs to be resized, doing that now.
2017-12-11 21:29:49.820	    7f8cefb6f740	INFO 	global	src/blockchain_db/lmdb/db_lmdb.cpp:494	LMDB Mapsize increased.  Old: 8773MiB, New: 9797MiB
Segmentation fault (core dumped)


# Discussion History
## altafhussain1 | 2017-12-11T21:36:37+00:00

[7698ac235f5c3474bfc7147e5a2ef9fa.tar.gz](https://github.com/monero-project/monero/files/1549467/7698ac235f5c3474bfc7147e5a2ef9fa.tar.gz) Strace


## altafhussain1 | 2017-12-11T21:37:34+00:00
Dec 12 02:59:49 altaf-hussain kernel: [ 7065.893457] monerod[13307]: segfault at 54d6a90 ip 00007f8cecd8b390 sp 00007ffe8f857198 error 4 in libc-2.23.so[7f8cecc35000+1c0000]


## altafhussain1 | 2017-12-11T21:41:54+00:00
P.S I have already tried compiling the pull #2492  , didnt work for me 

## moneromooo-monero | 2017-12-11T22:32:18+00:00
Try with the current 0.11.1.0, a few crashes and sync failures were fixed.

## altafhussain1 | 2017-12-12T05:10:40+00:00
Still won't work , 

2017-12-12 05:08:02.656	    7fc385d7b740	INFO 	global	src/daemon/main.cpp:279	Monero 'Helium Hydra' **(v0.11.1.0-release)**
2017-12-12 05:08:02.657	    7fc385d7b740	INFO 	global	src/daemon/protocol.h:55	Initializing cryptonote protocol...
2017-12-12 05:08:02.657	    7fc385d7b740	INFO 	global	src/daemon/protocol.h:60	Cryptonote protocol initialized OK
2017-12-12 05:08:02.685	    7fc385d7b740	INFO 	global	src/daemon/p2p.h:63	Initializing p2p server...
2017-12-12 05:08:04.161	    7fc385d7b740	INFO 	global	src/daemon/p2p.h:68	P2p server initialized OK
2017-12-12 05:08:04.161	    7fc385d7b740	INFO 	global	src/daemon/rpc.h:58	Initializing core rpc server...
2017-12-12 05:08:04.162	    7fc385d7b740	INFO 	global	contrib/epee/include/net/http_server_impl_base.h:70	Binding on 127.0.0.1:18081
2017-12-12 05:08:04.162	    7fc385d7b740	INFO 	global	src/daemon/rpc.h:63	Core rpc server initialized OK on port: 18081
2017-12-12 05:08:04.162	    7fc385d7b740	INFO 	global	src/daemon/core.h:73	Initializing core...
2017-12-12 05:08:04.162	    7fc385d7b740	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:323	Loading blockchain from folder /root/.bitmonero/lmdb ...
2017-12-12 05:08:04.163	    7fc385d7b740	WARN 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1155	LMDB memory map needs to be resized, doing that now.
2017-12-12 05:08:04.163	    7fc385d7b740	INFO 	global	src/blockchain_db/lmdb/db_lmdb.cpp:494	LMDB Mapsize increased.  Old: 8773MiB, New: 9797MiB
Segmentation fault (core dumped)


## moneromooo-monero | 2017-12-12T08:31:11+00:00
Please make sure you've got cores enabled:
ulimit -c unlimited
echo core | sudo tee /proc/sys/kernel/core_pattern
If you have a core already, it's good. If not, run those two commands and try again to get a core. Then:
gdb /path/to/monerod core*
Then, in gdb:
bt
Then paste the output of this. It's likely a corrupt database.


## altafhussain1 | 2017-12-12T17:45:50+00:00
GNU gdb (Ubuntu 7.11.1-0ubuntu1~16.5) 7.11.1
Copyright (C) 2016 Free Software Foundation, Inc.
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
Reading symbols from /root/monero-v0.11.1.0/monerod...done.
[New LWP 2917]
[New LWP 2918]
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
Core was generated by `./monerod'.
Program terminated with signal SIGSEGV, Segmentation fault.
#0  __memmove_ssse3 () at ../sysdeps/x86_64/multiarch/memcpy-ssse3.S:114
114	../sysdeps/x86_64/multiarch/memcpy-ssse3.S: No such file or directory.
[Current thread is 1 (Thread 0x7fa68f8f0740 (LWP 2917))]
-----> please find the output from the core file above .

## moneromooo-monero | 2017-12-13T09:42:16+00:00
You don't seem to have run the bt command.

## altafhussain1 | 2017-12-13T17:28:42+00:00
Type "apropos word" to search for commands related to "word"...
Reading symbols from /root/monero-v0.11.1.0/monerod...done.
[New LWP 2917]
[New LWP 2918]
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
Core was generated by `./monerod'.
Program terminated with signal SIGSEGV, Segmentation fault.
#0  __memmove_ssse3 () at ../sysdeps/x86_64/multiarch/memcpy-ssse3.S:114
114	../sysdeps/x86_64/multiarch/memcpy-ssse3.S: No such file or directory.
[Current thread is 1 (Thread 0x7fa68f8f0740 (LWP 2917))]
(gdb) bt
#0  __memmove_ssse3 () at ../sysdeps/x86_64/multiarch/memcpy-ssse3.S:114
#1  0x0000000000908caf in mdb_node_add ()
#2  0x000000000090b40e in mdb_cursor_put.part ()
#3  0x000000000090efde in mdb_txn_commit ()
#4  0x00000000007d792f in cryptonote::mdb_txn_safe::commit(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) ()
#5  0x00000000007f1654 in cryptonote::BlockchainLMDB::open(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, int) ()
#6  0x00000000008341a9 in cryptonote::core::init(boost::program_options::variables_map const&, cryptonote::test_options const*) ()
#7  0x000000000063cd10 in daemonize::t_daemon::run(bool) ()
#8  0x000000000073f91a in daemonize::t_executor::run_interactive(boost::program_options::variables_map const&) ()
#9  0x0000000000741d4c in bool daemonizer::daemonize<daemonize::t_executor>(int, char const**, daemonize::t_executor&&, boost::program_options::variables_map const&) ()
#10 0x0000000000611bc7 in main ()
(gdb) 

-------> I kinda missed it , here you go again

## hyc | 2017-12-13T18:36:47+00:00
Yeah, DB corrupted. You could try to restart using the `--db-salvage` option, that might help get past this. If not you'll have to delete the DB and start over. You should use the `--db-sync-mode=safe` option on all future invocations.

## altafhussain1 | 2017-12-14T18:20:16+00:00
Thanks so much it worked , thank god i didn't had to download the whole DB again.

## moneromooo-monero | 2017-12-25T17:48:13+00:00
+resolved

# Action History
- Created by: altafhussain1 | 2017-12-11T21:31:43+00:00
- Closed at: 2017-12-25T18:08:24+00:00
