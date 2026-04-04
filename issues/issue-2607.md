---
title: Invalid mutex used in mdb_txn_renew0
source_url: https://github.com/monero-project/monero/issues/2607
author: moneromooo-monero
assignees: []
labels: []
created_at: '2017-10-08T12:44:06+00:00'
updated_at: '2017-10-31T13:00:59+00:00'
type: issue
status: closed
closed_at: '2017-10-31T13:00:59+00:00'
---

# Original Description
I got this running core tests. I saw this once before, and at the time the debug info was unavailable, so it's rare.
```
Program terminated with signal SIGSEGV, Segmentation fault.
#0  0x000079e97806cde0 in pthread_mutex_lock () from /lib64/libpthread.so.0
[Current thread is 1 (Thread 0x79e972526700 (LWP 28148))]
Missing separate debuginfos, use: dnf debuginfo-install glibc-2.24-9.fc25.x86_64 keyutils-libs-1.5.9-8.fc24.x86_64 krb5-libs-1.14.4-8.fc25.x86_64 libcom_err-1.43.3-1.fc25.x86_64 libgcc-6.4.1-1.fc25.x86_64 libicu-57.1-5.fc25.x86_64 libselinux-2.5-13.fc25.x86_64 libstdc++-6.4.1-1.fc25.x86_64 miniupnpc-2.0-2.fc25.x86_64 ncurses-libs-6.0-6.20160709.fc25.x86_64 openssl-libs-1.0.2k-1.fc25.x86_64 pcre-8.41-1.fc25.x86_64 readline-6.3-8.fc24.x86_64 system-python-libs-3.5.3-6.fc25.x86_64 unbound-libs-1.6.3-1.fc25.x86_64 zlib-1.2.8-10.fc24.x86_64
(gdb) bt
#0  0x000079e97806cde0 in pthread_mutex_lock () from /lib64/libpthread.so.0
#1  0x000079e97b73bd2d in mdb_txn_renew0 (txn=0x79e8e4001a20) at /home/user/src/bitmonero/external/db_drivers/liblmdb/mdb.c:2878
#2  0x000079e97b73c1c7 in mdb_txn_renew (txn=0x79e8e4001a20) at /home/user/src/bitmonero/external/db_drivers/liblmdb/mdb.c:2988
#3  0x000079e97ba5c254 in cryptonote::lmdb_txn_renew (txn=0x79e8e4001a20)
    at /home/user/src/bitmonero/src/blockchain_db/lmdb/db_lmdb.cpp:424
#4  0x000079e97ba49e91 in cryptonote::BlockchainLMDB::block_rtxn_start (this=0x1481c00, mtxn=0x79e972525798, mcur=0x79e972525790)
    at /home/user/src/bitmonero/src/blockchain_db/lmdb/db_lmdb.cpp:2705
#5  0x000079e97ba4032d in cryptonote::BlockchainLMDB::height (this=0x1481c00)
    at /home/user/src/bitmonero/src/blockchain_db/lmdb/db_lmdb.cpp:1981
#6  0x000079e97ca2a679 in cryptonote::Blockchain::is_within_compiled_block_hash_area (this=0x7fff95b5a3b8)
    at /home/user/src/bitmonero/src/cryptonote_core/blockchain.h:957
#7  0x000079e97ca1fa93 in cryptonote::core::handle_incoming_tx_post (this=0x7fff95b5a2c0, 
    tx_blob="\001\000\001\002\377\265\377\003\001\000r|\006]\032H\256\030QEK\211i\022'\236\021^\225h\246\001\023\221\"\220\024\356cf\236\236\001\377\337\301\376\352\376\003\002\177\001\302o\314t@h\025\354\313\066\366\210Q\032\326#S\020\064\341 ?\263:,\251>+9\356!\001\365\234\002|N\205<H9\365\361\353|\362\215V\223\060\242\301y\b\255\237IΙm}υ\v\n\365\351hۋ$\375\204%\237z0`]\336Y\262\307Ue8|&\265b9e\312R]\001\027\324c\231+\370o-4E\361\061\213E*SI3+`\217\v\203\060&46\227\373\315M\003", tvc=..., tx=..., tx_hash=..., tx_prefixt_hash=..., 
    keeped_by_block=true, relayed=false, do_not_relay=false) at /home/user/src/bitmonero/src/cryptonote_core/cryptonote_core.cpp:563
#8  0x000079e97ca2010d in cryptonote::core::<lambda()>::operator()(void) const (__closure=0x79e8e4000e40)
    at /home/user/src/bitmonero/src/cryptonote_core/cryptonote_core.cpp:626
#9  0x000079e97ca26fe5 in std::_Function_handler<void(), cryptonote::core::handle_incoming_txs(const std::__cxx11::list<std::__cxx11::basic_string<char> >&, std::vector<cryptonote::tx_verification_context>&, bool, bool, bool)::<lambda()> >::_M_invoke(const std::_Any_data &) (
    __functor=...) at /usr/include/c++/6.4.1/functional:1731
#10 0x000079e97a94e9e0 in std::function<void ()>::operator()() const (this=0x79e972525c88) at /usr/include/c++/6.4.1/functional:2127
#11 0x000079e97a94d8dd in tools::threadpool::run (this=0x79e97cd0da40 <tools::threadpool::getInstance()::instance>)
    at /home/user/src/bitmonero/src/common/threadpool.cpp:109
#12 0x000079e97a95112b in boost::_mfi::mf0<void, tools::threadpool>::operator() (this=0x14867b8, 
    p=0x79e97cd0da40 <tools::threadpool::getInstance()::instance>) at /home/user/boost_1_59_0/boost/bind/mem_fn_template.hpp:49
#13 0x000079e97a95108e in boost::_bi::list1<boost::_bi::value<tools::threadpool*> >::operator()<boost::_mfi::mf0<void, tools::threadpool>, boost::_bi::list0> (this=0x14867c8, f=..., a=...) at /home/user/boost_1_59_0/boost/bind/bind.hpp:255
#14 0x000079e97a950f73 in boost::_bi::bind_t<void, boost::_mfi::mf0<void, tools::threadpool>, boost::_bi::list1<boost::_bi::value<tools::threadpool*> > >::operator() (this=0x14867b8) at /home/user/boost_1_59_0/boost/bind/bind.hpp:895
#15 0x000079e97a950e4e in boost::detail::thread_data<boost::_bi::bind_t<void, boost::_mfi::mf0<void, tools::threadpool>, boost::_bi::list1<boost::_bi::value<tools::threadpool*> > > >::run (this=0x1486600) at /home/user/boost_1_59_0/boost/thread/detail/thread.hpp:116
#16 0x000079e978b39adf in thread_proxy () from /home/user/boost_1_59_install/lib/libboost_thread.so.1.59.0
#17 0x000079e97806a73a in start_thread () from /lib64/libpthread.so.0
#18 0x000079e977da4e0f in clone () from /lib64/libc.so.6
(gdb) up
#1  0x000079e97b73bd2d in mdb_txn_renew0 (txn=0x79e8e4001a20) at /home/user/src/bitmonero/external/db_drivers/liblmdb/mdb.c:2878
2878					if (LOCK_MUTEX(rc, env, rmutex))
(gdb) li
2873						if (rc)
2874							return rc;
2875						env->me_live_reader = 1;
2876					}
2877	
2878					if (LOCK_MUTEX(rc, env, rmutex))
2879						return rc;
2880					nr = ti->mti_numreaders;
2881					for (i=0; i<nr; i++)
2882						if (ti->mti_readers[i].mr_pid == 0)
(gdb) print rmutex
$1 = (mdb_mutexref_t) 0x4fc3b144
(gdb) print *rmutex
Cannot access memory at address 0x4fc3b144
(gdb) print env
$2 = (MDB_env *) 0x14c1240
(gdb) print *env
$3 = {me_fd = 2013650504, me_lfd = 31209, me_mfd = 2013650504, me_flags = 31209, me_psize = 1338224580, me_os_psize = 0, 
  me_maxreaders = 1338224640, me_close_readers = 0, me_numdbs = 1338224700, me_maxdbs = 0, me_pid = 1338224760, 
  me_path = 0x4fc3b0b4 <error: Cannot access memory at address 0x4fc3b0b4>, 
  me_map = 0x4fc3b0f0 <error: Cannot access memory at address 0x4fc3b0f0>, me_txns = 0x4fc3b12c, me_metas = {0x4fc3b168, 0x4fc3b1a4}, 
  me_pbuf = 0x4fc3b1e0, me_txn = 0x4fc3b21c, me_txn0 = 0x4fc3b258, me_mapsize = 1338225300, me_size = 1338225360, me_maxpg = 1338225420, 
  me_dbxs = 0x4fc3b348, me_dbflags = 0x4fc3b384, me_dbiseqs = 0x4fc3b3c0, me_txkey = 1338225660, me_pgoldest = 1338225720, me_pgstate = {
    mf_pghead = 0x4fc3b474, mf_pglast = 1338225840}, me_dpages = 0x4fc3b4ec, me_free_pgs = 0x4fc3b528, me_dirty_list = 0x4fc3b564, 
  me_maxfree_1pg = 1338226080, me_nodemax = 0, me_live_reader = 1338226140, me_userctx = 0x4fc3b618, me_assert_func = 0x4fc3b654}
(gdb) print *txn
$4 = {mt_parent = 0x0, mt_child = 0x0, mt_next_pgno = 184293, mt_txnid = 145524, mt_env = 0x14c1240, mt_free_pgs = 0x0, 
  mt_loose_pgs = 0x0, mt_loose_count = 0, mt_spill_pgs = 0x0, mt_u = {dirty_list = 0x0, reader = 0x0}, mt_dbxs = 0x149e2d0, 
  mt_dbs = 0x79e8e4001aa8, mt_dbiseqs = 0x1512d30, mt_cursors = 0x0, 
  mt_dbflags = 0x79e8e4001ec8 "\b\030\030\032\032\032\032\032\032\032\032\032\032", mt_numdbs = 0, mt_flags = 131073, mt_dirty_room = 0}
(gdb) up 2
#3  0x000079e97ba5c254 in cryptonote::lmdb_txn_renew (txn=0x79e8e4001a20)
    at /home/user/src/bitmonero/src/blockchain_db/lmdb/db_lmdb.cpp:424
424	  int res = mdb_txn_renew(txn);
(gdb) up
#4  0x000079e97ba49e91 in cryptonote::BlockchainLMDB::block_rtxn_start (this=0x1481c00, mtxn=0x79e972525798, mcur=0x79e972525790)
    at /home/user/src/bitmonero/src/blockchain_db/lmdb/db_lmdb.cpp:2705
2705	    if (auto mdb_res = lmdb_txn_renew(m_tinfo->m_ti_rtxn))
(gdb) print *m_tinfo
Could not find operator*.
(gdb) print m_tinfo
$5 = {cleanup = {px = 0x1483dd0, pn = {pi_ = 0x14857e0}}}


```

# Discussion History
## hyc | 2017-10-08T13:46:16+00:00
Summarizing from IRC - the txn and env pointers appear to be invalid. Since they're coming from a thread_specific_ptr it seems that the thread specific memory is getting trashed somehow.

## moneromooo-monero | 2017-10-31T13:00:59+00:00
Since this is only secondary damage without plausible way to work back to the original problem, I'll close that.

# Action History
- Created by: moneromooo-monero | 2017-10-08T12:44:06+00:00
- Closed at: 2017-10-31T13:00:59+00:00
