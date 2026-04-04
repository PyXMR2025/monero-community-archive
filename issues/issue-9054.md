---
title: monerod killed with SIGSEGV after loading blockchain (Segmentation fault after
  "setting m_height") on archlinux
source_url: https://github.com/monero-project/monero/issues/9054
author: ketiv17
assignees: []
labels: []
created_at: '2023-11-04T19:28:02+00:00'
updated_at: '2023-11-16T17:24:26+00:00'
type: issue
status: closed
closed_at: '2023-11-16T17:24:26+00:00'
---

# Original Description
Hey, I'm running on archlinux x86_64, kernel 6.5.9-arch2-1, i3-3220, 16G RAM, >450G of free space on partition
I was in about 70% of syncing blockchain when monerod started refusing to start
(it manages to start normally when I let it sync from scratch)
done with monero v0.18.3.1 (downloaded from monero downloads)

monerod --log-level 4:
```
./monerod --data-dir ../.bitmonero/ --log-level 4
2023-11-04 18:36:26.705	I Monero 'Fluorine Fermi' (v0.18.3.1-release)
2023-11-04 18:36:26.705	I Moving from main() into the daemonize now.
2023-11-04 18:36:26.705	I Initializing cryptonote protocol...
2023-11-04 18:36:26.705	I Cryptonote protocol initialized OK
2023-11-04 18:36:26.706	T Blockchain::Blockchain
2023-11-04 18:36:26.706	I Initializing core...
2023-11-04 18:36:26.706	T BlockchainLMDB::BlockchainLMDB
2023-11-04 18:36:26.706	T BlockchainLMDB::get_db_name
2023-11-04 18:36:26.706	I Loading blockchain from folder ../.bitmonero/lmdb ...
2023-11-04 18:36:26.706	D option: fast
2023-11-04 18:36:26.706	D option: async
2023-11-04 18:36:26.706	D option: 250000000bytes
2023-11-04 18:36:26.706	T BlockchainLMDB::open
2023-11-04 18:36:26.706	W The blockchain is on a rotating drive: this will be very slow, use an SSD if possible
2023-11-04 18:36:26.706	T BlockchainLMDB::need_resize
2023-11-04 18:36:26.707	D DB map size:     141752623104
2023-11-04 18:36:26.707	D Space used:      127185866752
2023-11-04 18:36:26.707	D Space remaining: 14566756352
2023-11-04 18:36:26.707	D Size threshold:  0
2023-11-04 18:36:26.707	D Percent used: 89.7238  Percent threshold: 90.0000
2023-11-04 18:36:26.707	D Setting m_height to: 2506395
Segmentation fault (core dumped)
```

bitmonero.log (lines related to last run):
```
2023-11-04 18:36:26.705     7f6a638957c0        INFO    logging contrib/epee/src/mlog.cpp:273   New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
2023-11-04 18:36:26.705     7f6a638957c0        INFO    logging contrib/epee/src/mlog.cpp:273   New log categories: *:TRACE
2023-11-04 18:36:26.705     7f6a638957c0        INFO    global  src/daemon/main.cpp:309 Monero 'Fluorine Fermi' (v0.18.3.1-release)
2023-11-04 18:36:26.705     7f6a638957c0        INFO    daemon  src/daemon/main.cpp:371 Moving from main() into the daemonize now.
2023-11-04 18:36:26.705     7f6a638957c0        INFO    global  src/daemon/protocol.h:53        Initializing cryptonote protocol...
2023-11-04 18:36:26.705     7f6a638957c0        INFO    global  src/daemon/protocol.h:58        Cryptonote protocol initialized OK
2023-11-04 18:36:26.706     7f6a638957c0        TRACE   blockchain      src/cryptonote_core/blockchain.cpp:105  Blockchain::Blockchain
2023-11-04 18:36:26.706     7f6a638957c0        INFO    global  src/daemon/core.h:64    Initializing core...
2023-11-04 18:36:26.706     7f6a638957c0        TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:1307 BlockchainLMDB::BlockchainLMDB
2023-11-04 18:36:26.706     7f6a638957c0        TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:1686 BlockchainLMDB::get_db_name
2023-11-04 18:36:26.706     7f6a638957c0        INFO    global  src/cryptonote_core/cryptonote_core.cpp:523     Loading blockchain from folder ../.bitmonero/lmdb ...
2023-11-04 18:36:26.706     7f6a638957c0        DEBUG   cn      src/cryptonote_core/cryptonote_core.cpp:551     option: fast
2023-11-04 18:36:26.706     7f6a638957c0        DEBUG   cn      src/cryptonote_core/cryptonote_core.cpp:551     option: async
2023-11-04 18:36:26.706     7f6a638957c0        DEBUG   cn      src/cryptonote_core/cryptonote_core.cpp:551     option: 250000000bytes
2023-11-04 18:36:26.706     7f6a638957c0        TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:1329 BlockchainLMDB::open
2023-11-04 18:36:26.706     7f6a638957c0        WARNING global  src/blockchain_db/lmdb/db_lmdb.cpp:1354 The blockchain is on a rotating drive: this will be very slow, use an SSD if possible
2023-11-04 18:36:26.706     7f6a638957c0        TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:620  BlockchainLMDB::need_resize
2023-11-04 18:36:26.707     7f6a638957c0        DEBUG   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:636  DB map size:     141752623104
2023-11-04 18:36:26.707     7f6a638957c0        DEBUG   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:637  Space used:      127185866752
2023-11-04 18:36:26.707     7f6a638957c0        DEBUG   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:638  Space remaining: 14566756352
2023-11-04 18:36:26.707     7f6a638957c0        DEBUG   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:639  Size threshold:  0
2023-11-04 18:36:26.707     7f6a638957c0        DEBUG   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:641  Percent used: 89.7238  Percent threshold: 90.0000
2023-11-04 18:36:26.707     7f6a638957c0        DEBUG   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:1482 Setting m_height to: 2506395
```

strace ./monerod --data-dir ../.bitmonero/ --log-level 4:
[strace.txt](https://github.com/monero-project/monero/files/13257478/strace.txt)

gdb (without debuginfo):
```
Program terminated with signal SIGSEGV, Segmentation fault.
#0  0x00007f6a6393fae6 in ?? () from /usr/lib/libc.so.6
(gdb) bt
#0  0x00007f6a6393fae6 in ?? () from /usr/lib/libc.so.6
#1  0x0000556cb9136ca9 in mdb_node_add ()
#2  0x0000556cb913bc0a in mdb_cursor_put ()
#3  0x0000556cb913dd57 in mdb_txn_commit ()
#4  0x0000556cb90eb092 in cryptonote::mdb_txn_safe::commit(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) ()
#5  0x0000556cb912dd0c in cryptonote::BlockchainLMDB::open(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, int) ()
#6  0x0000556cb8ea78d4 in cryptonote::core::init(boost::program_options::variables_map const&, cryptonote::test_options const*, std::function<epee::span<unsigned char const> const (cryptonote::network_type)> const&, bool) ()
#7  0x0000556cb8b78950 in daemonize::t_core::t_core(boost::program_options::variables_map const&) ()
#8  0x0000556cb8ba09d3 in daemonize::t_internals::t_internals(boost::program_options::variables_map const&) ()
#9  0x0000556cb8b2406e in daemonize::t_daemon::t_daemon(boost::program_options::variables_map const&, unsigned short) ()
#10 0x0000556cb8ba2054 in daemonize::t_executor::run_interactive(boost::program_options::variables_map const&) ()
#11 0x0000556cb8ba56be in bool daemonizer::daemonize<daemonize::t_executor>(int, char const**, daemonize::t_executor&&, boost::program_options::variables_map const&) ()
#12 0x0000556cb8aee98a in main ()
(gdb) 

```

gdb (with debuginfo):
```
Program terminated with signal SIGSEGV, Segmentation fault.
#0  __memcpy_sse2_unaligned_erms () at ../sysdeps/x86_64/multiarch/memmove-vec-unaligned-erms.S:523
523      VMOVU -VEC_SIZE(%rsi, %rdx), %VMM(8)                                                                                                                                                 
(gdb) bt
#0  __memcpy_sse2_unaligned_erms () at ../sysdeps/x86_64/multiarch/memmove-vec-unaligned-erms.S:523
#1  0x0000556cb9136ca9 in mdb_node_add ()
#2  0x0000556cb913bc0a in mdb_cursor_put ()
#3  0x0000556cb913dd57 in mdb_txn_commit ()
#4  0x0000556cb90eb092 in cryptonote::mdb_txn_safe::commit(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) ()
#5  0x0000556cb912dd0c in cryptonote::BlockchainLMDB::open(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, int) ()
#6  0x0000556cb8ea78d4 in cryptonote::core::init(boost::program_options::variables_map const&, cryptonote::test_options const*, std::function<epee::span<unsigned char const> const (cryptonote::network_type)> const&, bool) ()
#7  0x0000556cb8b78950 in daemonize::t_core::t_core(boost::program_options::variables_map const&) ()
#8  0x0000556cb8ba09d3 in daemonize::t_internals::t_internals(boost::program_options::variables_map const&) ()
#9  0x0000556cb8b2406e in daemonize::t_daemon::t_daemon(boost::program_options::variables_map const&, unsigned short) ()
#10 0x0000556cb8ba2054 in daemonize::t_executor::run_interactive(boost::program_options::variables_map const&) ()
#11 0x0000556cb8ba56be in bool daemonizer::daemonize<daemonize::t_executor>(int, char const**, daemonize::t_executor&&, boost::program_options::variables_map const&) ()
#12 0x0000556cb8aee98a in main ()
(gdb) 
```

(all of the above was done with latest glibc 2.38-7)
every other program that requires qlibc runs fine (even monerod when it starts from scratch)
I tried troubleshooting and googling as much as a newbie can, but nothing fixed it.
given the errors I don't think it's a corrupt blockchain (--db-salvage results in the same error), but feel free to correct me.

issue #https://github.com/monero-project/monero-gui/issues/4233 looks similar

Thanks in advance.

# Discussion History
## selsta | 2023-11-05T01:20:21+00:00
What kind of storage do you have? Did you have a power outage during sync or something similar that could have caused corruption of the database?

## ketiv17 | 2023-11-05T07:39:56+00:00
its an old HDD Seagate momentus 750GB, I don't recall any power outages, and it was always turned off by cron sending exit^M to the screen it was running on.

## ketiv17 | 2023-11-16T17:24:26+00:00
I'm syncing the blockchain from scratch, the fact that this error only affects this blockchain does mean that there is something wrong with the blockchain, just the sort of error seemed kinda weird to me,

# Action History
- Created by: ketiv17 | 2023-11-04T19:28:02+00:00
- Closed at: 2023-11-16T17:24:26+00:00
