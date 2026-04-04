---
title: monero-blockchain-import stalls after importing a few blocks
source_url: https://github.com/monero-project/monero/issues/2323
author: benma
assignees: []
labels: []
created_at: '2017-08-22T06:58:52+00:00'
updated_at: '2017-11-14T20:34:10+00:00'
type: issue
status: closed
closed_at: '2017-11-14T20:32:29+00:00'
---

# Original Description
Running this command:

```sh
$ ./monero-blockchain-import --input-file blockchain.raw --resume 1 --batch-size 1 --log-level 2  --block-sync-size 1 > log
```

The tool imports a few blocks (314 between my latest two attempts) and then just stops all activity.

The last few lines of the log are always like this:

```
2017-08-22 06:18:45.269	    7f3254598740	INFO 	blockchain	src/cryptonote_core/blockchain.cpp:3410	+++++ BLOCK SUCCESSFULLY ADDED
id:	<b3b91d302b995ecefd99a667ffa800eacd3c965f2dc8f726364bdf1afad0074a>
PoW:	<9c4deed3453e89d2ea0c9da9a16efe521589b15f201090506cbd9b1000000000>
HEIGHT 1207379, difficulty:	4842901915
block reward: 9.248600000000(9.239924160000 + 0.008675840000), coinbase_blob_size: 248, cumulative size: 3360, 26(0/21)ms
2017-08-22 06:18:45.269	    7f3254598740	DEBUG	bcutil	src/blockchain_utilities/blockchain_import.cpp:390	chunk_size: 8674
2017-08-22 06:18:45.269	    7f3254598740	DEBUG	bcutil	src/blockchain_utilities/blockchain_import.cpp:412	Total bytes read: 3977260360
2017-08-22 06:18:45.270	    7f3254598740	DEBUG	bcutil	src/blockchain_utilities/blockchain_import.cpp:450	loading block number 1207380
2017-08-22 06:18:45.270	    7f3254598740	DEBUG	bcutil	src/blockchain_utilities/blockchain_import.cpp:453	block prev_id: <b3b91d302b995ecefd99a667ffa800eacd3c965f2dc8f726364bdf1afad0074a>

block 1207380 / 13812402017-08-22 06:18:45.270	    7f3254598740	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:554	[check_and_resize_for_batch] checking DB size
2017-08-22 06:18:45.270	    7f3254598740	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:608	[get_estimated_batch_size] m_height: 1207380  block_start: 1206880  block_stop: 1207379
2017-08-22 06:18:45.270	    7f3254598740	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:636	average block size across recent 500 blocks: 10224
2017-08-22 06:18:45.270	    7f3254598740	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:640	estimated average block size for batch: 10224
2017-08-22 06:18:45.270	    7f3254598740	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:561	calculated batch size: 230040000
2017-08-22 06:18:45.270	    7f3254598740	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:570	increase size: 536870912
2017-08-22 06:18:45.270	    7f3254598740	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:518	DB map size:     16799526912
2017-08-22 06:18:45.270	    7f3254598740	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:519	Space used:      9970929664
2017-08-22 06:18:45.270	    7f3254598740	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:520	Space remaining: 6828597248
2017-08-22 06:18:45.270	    7f3254598740	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:521	Size threshold:  230040000
2017-08-22 06:18:45.270	    7f3254598740	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:523	Percent used: 0.5935  Percent threshold: 0.8000
```

I used monero built from source (`git describe` returns `v0.10.3.1-489-g4466b6d1`).

Related: when syncing from peers, it also stalls after a while, even with a small block-sync-size (the raw blockchain import was my attempt at working around it).

# Discussion History
## moneromooo-monero | 2017-08-22T09:27:03+00:00
Seems to work here (though I replaced log level 2 with 1 to avoid the slowness due to the huge amount of logs).
Maybe addition is just very slow ?
Try running gdb on the running process and check the stacks to see what it's doing afer it wedges:

```
gdb monero-blockchain-import `pidof monero-blockchain-import`
thread apply all bt
Press enter as needed to go through the entire output
q
```

Then post the (multi page) output of this.

## benma | 2017-08-24T09:25:13+00:00
Thanks.

It's now about slowness, before it gets stuck, blocks are added at a good pace, and when I restart, it continues at the same pace until it gets stuck again. So it is not about a particular block.

I am a bit unfamiliar with gdb, but here is the output after:

```
(gdb) thread apply all bt

Thread 9 (Thread 0x7faa346a2700 (LWP 7670)):
#0  0x00007fae229a71ad in pthread_cond_wait@@GLIBC_2.3.2 () from /usr/lib/libpthread.so.0
#1  0x0000003033b91a08 in boost::asio::io_service::run() ()
#2  0x00007fae24c04a6f in ?? () from /usr/lib/libboost_thread.so.1.64.0
#3  0x00007fae229a1049 in start_thread () from /usr/lib/libpthread.so.0
#4  0x00007fae226e1f0f in clone () from /usr/lib/libc.so.6

Thread 8 (Thread 0x7faa33ea1700 (LWP 7669)):
#0  0x00007fae229a71ad in pthread_cond_wait@@GLIBC_2.3.2 () from /usr/lib/libpthread.so.0
#1  0x0000003033b91a08 in boost::asio::io_service::run() ()
#2  0x00007fae24c04a6f in ?? () from /usr/lib/libboost_thread.so.1.64.0
#3  0x00007fae229a1049 in start_thread () from /usr/lib/libpthread.so.0
#4  0x00007fae226e1f0f in clone () from /usr/lib/libc.so.6

Thread 7 (Thread 0x7faa336a0700 (LWP 7668)):
#0  0x00007fae229a71ad in pthread_cond_wait@@GLIBC_2.3.2 () from /usr/lib/libpthread.so.0
#1  0x0000003033b91a08 in boost::asio::io_service::run() ()
#2  0x00007fae24c04a6f in ?? () from /usr/lib/libboost_thread.so.1.64.0
#3  0x00007fae229a1049 in start_thread () from /usr/lib/libpthread.so.0
#4  0x00007fae226e1f0f in clone () from /usr/lib/libc.so.6

Thread 6 (Thread 0x7faa32e9f700 (LWP 7667)):
#0  0x00007fae229a36bc in __pthread_mutex_lock_full () from /usr/lib/libpthread.so.0
#1  0x0000003033bffba8 in mdb_txn_renew0 ()
#2  0x0000003033c00604 in mdb_txn_begin ()
#3  0x0000003033be198f in cryptonote::BlockchainLMDB::block_rtxn_start(MDB_txn**, cryptonote::mdb_txn_cursors**) const ()
#4  0x0000003033be92d0 in cryptonote::BlockchainLMDB::get_output_key(unsigned long const&, std::vector<unsigned long, std::allocator<unsigned long> > const&, std::vector<cryptonote::output_data_t, std::allocator<cryptonote::output_data_t> >&, bool) ()
#5  0x0000003033b64a0c in cryptonote::Blockchain::output_scan_worker(unsigned long, std::vector<unsigned long, std::allocator<unsigned long> > const&, std::vector<cryptonote::output_data_t, std::allocator<cryptonote::output_data_t> >&, std::unordered_map<crypto::hash, cryptonote::transaction, std::hash<crypto::hash>, std::equal_to<crypto::hash>, std::allocator<std::pair<crypto::hash const, cryptonote::transaction> > >&) const ()
#6  0x0000003033b8aae6 in boost::asio::detail::completion_handler<boost::_bi::bind_t<void, boost::_mfi::cmf4<void, cryptonote::Blockchain, unsigned long, std::vector<unsigned long, std::allocator<unsigned long> > const&, std::vector<cryptonote::output_data_t, std::allocator<cryptonote::output_data_t> >&, std::unordered_map<crypto::hash, cryptonote::transaction, std::hash<crypto::hash>, std::equal_to<crypto::hash>, std::allocator<std::pair<crypto::hash const, cryptonote::transaction> > >&>, boost::_bi::list5<boost::_bi::value<cryptonote::Blockchain*>, boost::_bi::value<unsigned long>, boost::_bi::value<std::reference_wrapper<std::vector<unsigned long, std::allocator<unsigned long> > const> >, boost::_bi::value<std::reference_wrapper<std::vector<cryptonote::output_data_t, std::allocator<cryptonote::output_data_t> > > >, boost::_bi::value<std::reference_wrapper<std::unordered_map<crypto::hash, cryptonote::transaction, std::hash<crypto::hash>, std::equal_to<crypto::hash>, std::allocator<std::pair<crypto::hash const, cryptonote::transaction> > > > > > > >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) ()
#7  0x0000003033b91a80 in boost::asio::io_service::run() ()
#8  0x00007fae24c04a6f in ?? () from /usr/lib/libboost_thread.so.1.64.0
#9  0x00007fae229a1049 in start_thread () from /usr/lib/libpthread.so.0
#10 0x00007fae226e1f0f in clone () from /usr/lib/libc.so.6

Thread 5 (Thread 0x7faa34ea3700 (LWP 1585)):
#0  0x00007fae229a71ad in pthread_cond_wait@@GLIBC_2.3.2 () from /usr/lib/libpthread.so.0
#1  0x0000003033b91a08 in boost::asio::io_service::run() ()
#2  0x00007fae24c04a6f in ?? () from /usr/lib/libboost_thread.so.1.64.0
#3  0x00007fae229a1049 in start_thread () from /usr/lib/libpthread.so.0
#4  0x00007fae226e1f0f in clone () from /usr/lib/libc.so.6

Thread 4 (Thread 0x7fae1edec700 (LWP 1584)):
#0  0x00007fae229a71ad in pthread_cond_wait@@GLIBC_2.3.2 () from /usr/lib/libpthread.so.0
#1  0x0000003033c8c63d in tools::thread_group::data::run() ()
#2  0x00007fae24c04a6f in ?? () from /usr/lib/libboost_thread.so.1.64.0
---Type <return> to continue, or q <return> to quit---
#3  0x00007fae229a1049 in start_thread () from /usr/lib/libpthread.so.0
#4  0x00007fae226e1f0f in clone () from /usr/lib/libc.so.6

Thread 3 (Thread 0x7fae1f5ed700 (LWP 1583)):
#0  0x00007fae229a71ad in pthread_cond_wait@@GLIBC_2.3.2 () from /usr/lib/libpthread.so.0
#1  0x0000003033c8c63d in tools::thread_group::data::run() ()
#2  0x00007fae24c04a6f in ?? () from /usr/lib/libboost_thread.so.1.64.0
#3  0x00007fae229a1049 in start_thread () from /usr/lib/libpthread.so.0
#4  0x00007fae226e1f0f in clone () from /usr/lib/libc.so.6

Thread 2 (Thread 0x7fae1fdee700 (LWP 1582)):
#0  0x00007fae229a71ad in pthread_cond_wait@@GLIBC_2.3.2 () from /usr/lib/libpthread.so.0
#1  0x0000003033c8c63d in tools::thread_group::data::run() ()
#2  0x00007fae24c04a6f in ?? () from /usr/lib/libboost_thread.so.1.64.0
#3  0x00007fae229a1049 in start_thread () from /usr/lib/libpthread.so.0
#4  0x00007fae226e1f0f in clone () from /usr/lib/libc.so.6

Thread 1 (Thread 0x7fae25a88740 (LWP 1581)):
#0  0x00007fae229a71ad in pthread_cond_wait@@GLIBC_2.3.2 () from /usr/lib/libpthread.so.0
#1  0x00007fae24c0e558 in boost::condition_variable::wait(boost::unique_lock<boost::mutex>&) () from /usr/lib/libboost_thread.so.1.64.0
#2  0x00007fae24c04f9d in boost::thread::join_noexcept() () from /usr/lib/libboost_thread.so.1.64.0
#3  0x0000003033b94732 in boost::thread_group::join_all() ()
#4  0x0000003033b8a106 in cryptonote::Blockchain::prepare_handle_incoming_blocks(std::__cxx11::list<cryptonote::block_complete_entry, std::allocator<cryptonote::block_complete_entry> > const&) ()
#5  0x0000003033b9dc47 in cryptonote::core::prepare_handle_incoming_blocks(std::__cxx11::list<cryptonote::block_complete_entry, std::allocator<cryptonote::block_complete_entry> > const&) ()
#6  0x0000003033b371f3 in check_flush(cryptonote::core&, std::__cxx11::list<cryptonote::block_complete_entry, std::allocator<cryptonote::block_complete_entry> >&, bool) ()
#7  0x0000003033b3a25c in import_from_file(cryptonote::core&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, unsigned long) ()
#8  0x0000003033b304af in main ()
```


## moneromooo-monero | 2017-08-24T10:52:38+00:00
Looks like https://github.com/monero-project/monero/issues/2180

Are you on Arch ?

## benma | 2017-08-24T14:49:33+00:00
Yes I am! I will try to run it from a Dockerfile or VM soon.

## hyc | 2017-08-25T06:51:40+00:00
I just got this. Pretty much the same backtrace, with a couple more threads since this is a quad-core machine. Unfortunately I was running a release build, not debug. Will see if it happens again with debug binary.
````
Attaching to process 2493
[New LWP 2494]
[New LWP 2495]
[New LWP 2496]
[New LWP 2497]
[New LWP 22487]
[New LWP 22488]
[New LWP 22489]
[New LWP 22490]
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/usr/lib/libthread_db.so.1".
0x00007f31230b81ad in pthread_cond_wait@@GLIBC_2.3.2 () from /usr/lib/libpthread.so.0
(gdb) info thr
  Id   Target Id         Frame 
* 1    Thread 0x7f31260fa240 (LWP 2493) "monero-blockcha" 0x00007f31230b81ad in pthread_cond_wait@@GLIBC_2.3.2 ()
   from /usr/lib/libpthread.so.0
  2    Thread 0x7f3120742700 (LWP 2494) "monero-blockcha" 0x00007f31230b81ad in pthread_cond_wait@@GLIBC_2.3.2 ()
   from /usr/lib/libpthread.so.0
  3    Thread 0x7f311ff41700 (LWP 2495) "monero-blockcha" 0x00007f31230b81ad in pthread_cond_wait@@GLIBC_2.3.2 ()
   from /usr/lib/libpthread.so.0
  4    Thread 0x7f311f740700 (LWP 2496) "monero-blockcha" 0x00007f31230b81ad in pthread_cond_wait@@GLIBC_2.3.2 ()
   from /usr/lib/libpthread.so.0
  5    Thread 0x7f2ed43ca700 (LWP 2497) "monero-blockcha" 0x00007f31230b81ad in pthread_cond_wait@@GLIBC_2.3.2 ()
   from /usr/lib/libpthread.so.0
  6    Thread 0x7f2ed17c3700 (LWP 22487) "monero-blockcha" 0x00007f31230b46bc in __pthread_mutex_lock_full ()
   from /usr/lib/libpthread.so.0
  7    Thread 0x7f2ed27c5700 (LWP 22488) "monero-blockcha" 0x00007f31230b46bc in __pthread_mutex_lock_full ()
   from /usr/lib/libpthread.so.0
  8    Thread 0x7f2ed0fc2700 (LWP 22489) "monero-blockcha" 0x00007f31230b81ad in pthread_cond_wait@@GLIBC_2.3.2 ()
   from /usr/lib/libpthread.so.0
  9    Thread 0x7f2ed1fc4700 (LWP 22490) "monero-blockcha" 0x00007f31230b46bc in __pthread_mutex_lock_full ()
   from /usr/lib/libpthread.so.0
(gdb) thr apply all bt

Thread 9 (Thread 0x7f2ed1fc4700 (LWP 22490)):
#0  0x00007f31230b46bc in __pthread_mutex_lock_full () from /usr/lib/libpthread.so.0
#1  0x000000962b332778 in mdb_txn_renew0 ()
#2  0x000000962b3331d4 in mdb_txn_begin ()
#3  0x000000962b314b76 in cryptonote::BlockchainLMDB::block_rtxn_start(MDB_txn**, cryptonote::mdb_txn_cursors**) const ()
#4  0x000000962b31c2ce in cryptonote::BlockchainLMDB::get_output_key(unsigned long const&, std::vector<unsigned long, std::allocator<unsigned long> > const&, std::vector<cryptonote::output_data_t, std::allocator<cryptonote::output_data_t> >&, bool) ()
#5  0x000000962b299cfc in cryptonote::Blockchain::output_scan_worker(unsigned long, std::vector<unsigned long, std::allocator<unsigned long> > const&, std::vector<cryptonote::output_data_t, std::allocator<cryptonote::output_data_t> >&, std::unordered_map<crypto::hash, cryptonote::transaction, std::hash<crypto::hash>, std::equal_to<crypto::hash>, std::allocator<std::pair<crypto::hash const, cryptonote::transaction> > >&) const ()
#6  0x000000962b2bf146 in boost::asio::detail::completion_handler<boost::_bi::bind_t<void, boost::_mfi::cmf4<void, cryptonote::Blockchain, unsigned long, std::vector<unsigned long, std::allocator<unsigned long> > const&, std::vector<cryptonote::output_data_t, std::allocator<cryptonote::output_data_t> >&, std::unordered_map<crypto::hash, cryptonote::transaction, std::hash<crypto::hash>, std::equal_to<crypto::hash>, std::allocator<std::pair<crypto::hash const, cryptonote::transaction> > >&>, boost::_bi::list5<boost::_bi::value<cryptonote::Blockchain*>, boost::_bi::value<unsigned long>, boost::_bi::value<std::reference_wrapper<std::vector<unsigned long, std::allocator<unsigned long> > const> >, boost::_bi::value<std::reference_wrapper<std::vector<cryptonote::output_data_t, std::allocator<cryptonote::output_data_t> > > >, boost::_bi::value<std::reference_wrapper<std::unordered_map<crypto::hash, cryptonote::transaction, std::hash<crypto::hash>, std::equal_to<crypto::hash>, std::allocator<std::pair<crypto::hash const, cryptonote::transaction> > > > > > > >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) ()
#7  0x000000962b2c5fd8 in boost::asio::io_service::run() ()
#8  0x00007f3125265a6f in ?? () from /usr/lib/libboost_thread.so.1.64.0
#9  0x00007f31230b2049 in start_thread () from /usr/lib/libpthread.so.0
#10 0x00007f3122df0f0f in clone () from /usr/lib/libc.so.6

Thread 8 (Thread 0x7f2ed0fc2700 (LWP 22489)):
#0  0x00007f31230b81ad in pthread_cond_wait@@GLIBC_2.3.2 () from /usr/lib/libpthread.so.0
#1  0x000000962b2c5f60 in boost::asio::io_service::run() ()
#2  0x00007f3125265a6f in ?? () from /usr/lib/libboost_thread.so.1.64.0
#3  0x00007f31230b2049 in start_thread () from /usr/lib/libpthread.so.0
#4  0x00007f3122df0f0f in clone () from /usr/lib/libc.so.6

Thread 7 (Thread 0x7f2ed27c5700 (LWP 22488)):
#0  0x00007f31230b46bc in __pthread_mutex_lock_full () from /usr/lib/libpthread.so.0
#1  0x000000962b332778 in mdb_txn_renew0 ()
#2  0x000000962b3331d4 in mdb_txn_begin ()
#3  0x000000962b314b76 in cryptonote::BlockchainLMDB::block_rtxn_start(MDB_txn**, cryptonote::mdb_txn_cursors**) const ()
#4  0x000000962b31c2ce in cryptonote::BlockchainLMDB::get_output_key(unsigned long const&, std::vector<unsigned long, std::allocator<unsigned long> > const&, std::vector<cryptonote::output_data_t, std::allocator<cryptonote::output_data_t> >&, bool) ()
#5  0x000000962b299cfc in cryptonote::Blockchain::output_scan_worker(unsigned long, std::vector<unsigned long, std::allocator<unsigned long> > const&, std::vector<cryptonote::output_data_t, std::allocator<cryptonote::output_data_t> >&, std::unordered_map<crypto::hash, cryptonote::transaction, std::hash<crypto::hash>, std::equal_to<crypto::hash>, std::allocator<std::pair<crypto::hash const, cryptonote::transaction> > >&) const ()
#6  0x000000962b2bf146 in boost::asio::detail::completion_handler<boost::_bi::bind_t<void, boost::_mfi::cmf4<void, cryptonote::Blockchain, unsigned long, std::vector<unsigned long, std::allocator<unsigned long> > const&, std::vector<cryptonote::output_data_t, std::allocator<cryptonote::output_data_t> >&, std::unordered_map<crypto::hash, cryptonote::transaction, std::hash<crypto::hash>, std::equal_to<crypto::hash>, std::allocator<std::pair<crypto::hash const, cryptonote::transaction> > >&>, boost::_bi::list5<boost::_bi::value<cryptonote::Blockchain*>, boost::_bi::value<unsigned long>, boost::_bi::value<std::reference_wrapper<std::vector<unsigned long, std::allocator<unsigned long> > const> >, boost::_bi::value<std::reference_wrapper<std::vector<cryptonote::output_data_t, std::allocator<cryptonote::output_data_t> > > >, boost::_bi::value<std::reference_wrapper<std::unordered_map<crypto::hash, cryptonote::transaction, std::hash<crypto::hash>, std::equal_to<crypto::hash>, std::allocator<std::pair<crypto::hash const, cryptonote::transaction> > > > > > > >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) ()
#7  0x000000962b2c5fd8 in boost::asio::io_service::run() ()
#8  0x00007f3125265a6f in ?? () from /usr/lib/libboost_thread.so.1.64.0
#9  0x00007f31230b2049 in start_thread () from /usr/lib/libpthread.so.0
#10 0x00007f3122df0f0f in clone () from /usr/lib/libc.so.6

Thread 6 (Thread 0x7f2ed17c3700 (LWP 22487)):
#0  0x00007f31230b46bc in __pthread_mutex_lock_full () from /usr/lib/libpthread.so.0
#1  0x000000962b332778 in mdb_txn_renew0 ()
#2  0x000000962b3331d4 in mdb_txn_begin ()
#3  0x000000962b314b76 in cryptonote::BlockchainLMDB::block_rtxn_start(MDB_txn**, cryptonote::mdb_txn_cursors**) const ()
#4  0x000000962b31c2ce in cryptonote::BlockchainLMDB::get_output_key(unsigned long const&, std::vector<unsigned long, std::allocator<unsigned long> > const&, std::vector<cryptonote::output_data_t, std::allocator<cryptonote::output_data_t> >&, bool) ()
#5  0x000000962b299cfc in cryptonote::Blockchain::output_scan_worker(unsigned long, std::vector<unsigned long, std::allocator<unsigned long> > const&, std::vector<cryptonote::output_data_t, std::allocator<cryptonote::output_data_t> >&, std::unordered_map<crypto::hash, cryptonote::transaction, std::hash<crypto::hash>, std::equal_to<crypto::hash>, std::allocator<std::pair<crypto::hash const, cryptonote::transaction> > >&) const ()
#6  0x000000962b2bf146 in boost::asio::detail::completion_handler<boost::_bi::bind_t<void, boost::_mfi::cmf4<void, cryptonote::Blockchain, ---Type <return> to continue, or q <return> to quit---
unsigned long, std::vector<unsigned long, std::allocator<unsigned long> > const&, std::vector<cryptonote::output_data_t, std::allocator<cryptonote::output_data_t> >&, std::unordered_map<crypto::hash, cryptonote::transaction, std::hash<crypto::hash>, std::equal_to<crypto::hash>, std::allocator<std::pair<crypto::hash const, cryptonote::transaction> > >&>, boost::_bi::list5<boost::_bi::value<cryptonote::Blockchain*>, boost::_bi::value<unsigned long>, boost::_bi::value<std::reference_wrapper<std::vector<unsigned long, std::allocator<unsigned long> > const> >, boost::_bi::value<std::reference_wrapper<std::vector<cryptonote::output_data_t, std::allocator<cryptonote::output_data_t> > > >, boost::_bi::value<std::reference_wrapper<std::unordered_map<crypto::hash, cryptonote::transaction, std::hash<crypto::hash>, std::equal_to<crypto::hash>, std::allocator<std::pair<crypto::hash const, cryptonote::transaction> > > > > > > >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) ()
#7  0x000000962b2c5fd8 in boost::asio::io_service::run() ()
#8  0x00007f3125265a6f in ?? () from /usr/lib/libboost_thread.so.1.64.0
#9  0x00007f31230b2049 in start_thread () from /usr/lib/libpthread.so.0
#10 0x00007f3122df0f0f in clone () from /usr/lib/libc.so.6

Thread 5 (Thread 0x7f2ed43ca700 (LWP 2497)):
#0  0x00007f31230b81ad in pthread_cond_wait@@GLIBC_2.3.2 () from /usr/lib/libpthread.so.0
#1  0x000000962b2c5f60 in boost::asio::io_service::run() ()
#2  0x00007f3125265a6f in ?? () from /usr/lib/libboost_thread.so.1.64.0
#3  0x00007f31230b2049 in start_thread () from /usr/lib/libpthread.so.0
#4  0x00007f3122df0f0f in clone () from /usr/lib/libc.so.6

Thread 4 (Thread 0x7f311f740700 (LWP 2496)):
#0  0x00007f31230b81ad in pthread_cond_wait@@GLIBC_2.3.2 () from /usr/lib/libpthread.so.0
#1  0x000000962b3bcd5d in tools::thread_group::data::run() ()
#2  0x00007f3125265a6f in ?? () from /usr/lib/libboost_thread.so.1.64.0
#3  0x00007f31230b2049 in start_thread () from /usr/lib/libpthread.so.0
#4  0x00007f3122df0f0f in clone () from /usr/lib/libc.so.6

Thread 3 (Thread 0x7f311ff41700 (LWP 2495)):
#0  0x00007f31230b81ad in pthread_cond_wait@@GLIBC_2.3.2 () from /usr/lib/libpthread.so.0
#1  0x000000962b3bcd5d in tools::thread_group::data::run() ()
#2  0x00007f3125265a6f in ?? () from /usr/lib/libboost_thread.so.1.64.0
#3  0x00007f31230b2049 in start_thread () from /usr/lib/libpthread.so.0
#4  0x00007f3122df0f0f in clone () from /usr/lib/libc.so.6

Thread 2 (Thread 0x7f3120742700 (LWP 2494)):
#0  0x00007f31230b81ad in pthread_cond_wait@@GLIBC_2.3.2 () from /usr/lib/libpthread.so.0
#1  0x000000962b3bcd5d in tools::thread_group::data::run() ()
#2  0x00007f3125265a6f in ?? () from /usr/lib/libboost_thread.so.1.64.0
#3  0x00007f31230b2049 in start_thread () from /usr/lib/libpthread.so.0
#4  0x00007f3122df0f0f in clone () from /usr/lib/libc.so.6

Thread 1 (Thread 0x7f31260fa240 (LWP 2493)):
#0  0x00007f31230b81ad in pthread_cond_wait@@GLIBC_2.3.2 () from /usr/lib/libpthread.so.0
#1  0x00007f312526f558 in boost::condition_variable::wait(boost::unique_lock<boost::mutex>&) () from /usr/lib/libboost_thread.so.1.64.0
#2  0x00007f3125265f9d in boost::thread::join_noexcept() () from /usr/lib/libboost_thread.so.1.64.0
#3  0x000000962b2c8c52 in boost::thread_group::join_all() ()
#4  0x000000962b2be73b in cryptonote::Blockchain::prepare_handle_incoming_blocks(std::__cxx11::list<cryptonote::block_complete_entry, std::allocator<cryptonote::block_complete_entry> > const&) ()
#5  0x000000962b2d1faf in cryptonote::core::prepare_handle_incoming_blocks(std::__cxx11::list<cryptonote::block_complete_entry, std::allocator<cryptonote::block_complete_entry> > const&) ()
#6  0x000000962b26cefb in check_flush(cryptonote::core&, std::__cxx11::list<cryptonote::block_complete_entry, std::allocator<cryptonote::block_complete_entry> >&, bool) ()
#7  0x000000962b26fe83 in import_from_file(cryptonote::core&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, unsigned long) ()
#8  0x000000962b2661eb in main ()
(gdb) 
````



## benma | 2017-08-27T11:06:21+00:00
I confirm that running `monero-blockchain-import` and `monerod` with Docker works fine. So it indeed is something about Arch or the environment.

## hyc | 2017-08-28T15:13:47+00:00
I tried multiple times to reproduce this hang with my debug build but it always ran to completion without hanging. So there's something flaky with optimized binaries in the release build, and it seems particular to Arch and/or gcc 7.1.1.

## hyc | 2017-09-07T11:21:58+00:00
I was able to reproduce this hang in a debug build of monerod. Here's the trace and relevant info:
````
(gdb) info thr
  Id   Target Id         Frame 
  1    Thread 0x7fd32d38bb80 (LWP 4130) "monerod" 0x00007fd32a7301ad in pthread_cond_wait@@GLIBC_2.3.2 () from /usr/lib/libpthread.so.0
  2    Thread 0x7fd327dba700 (LWP 4131) "monerod" 0x00007fd32a7301ad in pthread_cond_wait@@GLIBC_2.3.2 () from /usr/lib/libpthread.so.0
  3    Thread 0x7fd3278b9700 (LWP 4132) "monerod" 0x00007fd32a7301ad in pthread_cond_wait@@GLIBC_2.3.2 () from /usr/lib/libpthread.so.0
  4    Thread 0x7fd3273b8700 (LWP 4133) "monerod" 0x00007fd32a7301ad in pthread_cond_wait@@GLIBC_2.3.2 () from /usr/lib/libpthread.so.0
  5    Thread 0x7fd3256b4700 (LWP 4138) "monerod" 0x00007fd32a7301ad in pthread_cond_wait@@GLIBC_2.3.2 () from /usr/lib/libpthread.so.0
  6    Thread 0x7fd325eb5700 (LWP 4139) "monerod" 0x00007fd32a7301ad in pthread_cond_wait@@GLIBC_2.3.2 () from /usr/lib/libpthread.so.0
  7    Thread 0x7fd3266b6700 (LWP 4140) "monerod" 0x00007fd32a469473 in epoll_wait () from /usr/lib/libc.so.6
  8    Thread 0x7fd326eb7700 (LWP 4141) "monerod" 0x00007fd32a460fd3 in select () from /usr/lib/libc.so.6
  9    Thread 0x7fd324b1a700 (LWP 4142) "monerod" 0x00007fd32a7301ad in pthread_cond_wait@@GLIBC_2.3.2 () from /usr/lib/libpthread.so.0
  10   Thread 0x7fd31f7fe700 (LWP 4144) "monerod" 0x00007fd32a7301ad in pthread_cond_wait@@GLIBC_2.3.2 () from /usr/lib/libpthread.so.0
  11   Thread 0x7fd31e3fa700 (LWP 4148) "monerod" 0x00007fd32a73354c in __lll_lock_wait () from /usr/lib/libpthread.so.0
  12   Thread 0x7fd31caf5700 (LWP 4153) "monerod" 0x00007fd32a73354c in __lll_lock_wait () from /usr/lib/libpthread.so.0
  13   Thread 0x7fc733fff700 (LWP 14141) "monerod" 0x00007fd32a7301ad in pthread_cond_wait@@GLIBC_2.3.2 () from /usr/lib/libpthread.so.0
* 14   Thread 0x7fc758c11700 (LWP 14142) "monerod" 0x00007fd32a72c6bc in __pthread_mutex_lock_full () from /usr/lib/libpthread.so.0
  15   Thread 0x7fc759412700 (LWP 14143) "monerod" 0x00007fd32a72c6bc in __pthread_mutex_lock_full () from /usr/lib/libpthread.so.0
  16   Thread 0x7fc7337fe700 (LWP 14144) "monerod" 0x00007fd32a7301ad in pthread_cond_wait@@GLIBC_2.3.2 () from /usr/lib/libpthread.so.0
(gdb) thr apply all bt 5

Thread 16 (Thread 0x7fc7337fe700 (LWP 14144)):
#0  0x00007fd32a7301ad in pthread_cond_wait@@GLIBC_2.3.2 () from /usr/lib/libpthread.so.0
#1  0x0000005af41d722c in boost::asio::detail::posix_event::wait<boost::asio::detail::scoped_lock<boost::asio::detail::posix_mutex> > (lock=..., this=0x7fd3181baab8) at /usr/include/boost/asio/detail/posix_event.hpp:106
#2  boost::asio::detail::task_io_service::do_run_one (ec=..., this_thread=..., lock=..., this=<optimized out>) at /usr/include/boost/asio/detail/impl/task_io_service.ipp:380
#3  boost::asio::detail::task_io_service::run (ec=..., this=0x7fd3181baa60) at /usr/include/boost/asio/detail/impl/task_io_service.ipp:149
#4  boost::asio::io_service::run (this=<optimized out>) at /usr/include/boost/asio/impl/io_service.ipp:59
(More stack frames follow...)

Thread 15 (Thread 0x7fc759412700 (LWP 14143)):
#0  0x00007fd32a72c6bc in __pthread_mutex_lock_full () from /usr/lib/libpthread.so.0
#1  0x0000005af42487ab in mdb_txn_renew0 (txn=0x7fc7240009b0) at /home/software/bitmonero/external/db_drivers/liblmdb/mdb.c:2878
#2  0x0000005af424906f in mdb_txn_begin (env=0x5af8c01810, parent=0x0, flags=131072, ret=0x7fc7240008e0) at /home/software/bitmonero/external/db_drivers/liblmdb/mdb.c:3096
#3  0x0000005af418cf18 in cryptonote::lmdb_txn_begin (txn=0x7fc7240008e0, flags=131072, parent=0x0, env=0x5af8c01810) at /home/software/bitmonero/src/blockchain_db/lmdb/db_lmdb.cpp:414
#4  cryptonote::BlockchainLMDB::block_rtxn_start (this=0x5af8bfb4a0, mtxn=0x7fc7594119e0, mcur=0x7fc7594119e8) at /home/software/bitmonero/src/blockchain_db/lmdb/db_lmdb.cpp:2694
(More stack frames follow...)

Thread 14 (Thread 0x7fc758c11700 (LWP 14142)):
#0  0x00007fd32a72c6bc in __pthread_mutex_lock_full () from /usr/lib/libpthread.so.0
#1  0x0000005af42487ab in mdb_txn_renew0 (txn=0x7fc7380009d0) at /home/software/bitmonero/external/db_drivers/liblmdb/mdb.c:2878
#2  0x0000005af424906f in mdb_txn_begin (env=0x5af8c01810, parent=0x0, flags=131072, ret=0x7fc738000950) at /home/software/bitmonero/external/db_drivers/liblmdb/mdb.c:3096
#3  0x0000005af418cf18 in cryptonote::lmdb_txn_begin (txn=0x7fc738000950, flags=131072, parent=0x0, env=0x5af8c01810) at /home/software/bitmonero/src/blockchain_db/lmdb/db_lmdb.cpp:414
#4  cryptonote::BlockchainLMDB::block_rtxn_start (this=0x5af8bfb4a0, mtxn=0x7fc758c109e0, mcur=0x7fc758c109e8) at /home/software/bitmonero/src/blockchain_db/lmdb/db_lmdb.cpp:2694
(More stack frames follow...)

Thread 13 (Thread 0x7fc733fff700 (LWP 14141)):
#0  0x00007fd32a7301ad in pthread_cond_wait@@GLIBC_2.3.2 () from /usr/lib/libpthread.so.0
#1  0x0000005af41d722c in boost::asio::detail::posix_event::wait<boost::asio::detail::scoped_lock<boost::asio::detail::posix_mutex> > (lock=..., this=0x7fd3181baab8) at /usr/include/boost/asio/detail/posix_event.hpp:106
#2  boost::asio::detail::task_io_service::do_run_one (ec=..., this_thread=..., lock=..., this=<optimized out>) at /usr/include/boost/asio/detail/impl/task_io_service.ipp:380
#3  boost::asio::detail::task_io_service::run (ec=..., this=0x7fd3181baa60) at /usr/include/boost/asio/detail/impl/task_io_service.ipp:149
#4  boost::asio::io_service::run (this=<optimized out>) at /usr/include/boost/asio/impl/io_service.ipp:59
(More stack frames follow...)

Thread 12 (Thread 0x7fd31caf5700 (LWP 4153)):
#0  0x00007fd32a73354c in __lll_lock_wait () from /usr/lib/libpthread.so.0
#1  0x00007fd32a72c976 in pthread_mutex_lock () from /usr/lib/libpthread.so.0
#2  0x0000005af3fe56b9 in boost::recursive_mutex::lock (this=<optimized out>) at /usr/include/boost/thread/pthread/recursive_mutex.hpp:113
#3  0x0000005af41af068 in epee::critical_section::lock (this=0x5af8be3148) at /home/software/bitmonero/contrib/epee/include/syncobj.h:100
#4  epee::critical_region_t<epee::critical_section>::critical_region_t (cs=..., this=<synthetic pointer>) at /home/software/bitmonero/contrib/epee/include/syncobj.h:133
(More stack frames follow...)

Thread 11 (Thread 0x7fd31e3fa700 (LWP 4148)):
#0  0x00007fd32a73354c in __lll_lock_wait () from /usr/lib/libpthread.so.0
#1  0x00007fd32a72c976 in pthread_mutex_lock () from /usr/lib/libpthread.so.0
#2  0x0000005af3fe56b9 in boost::recursive_mutex::lock (this=<optimized out>) at /usr/include/boost/thread/pthread/recursive_mutex.hpp:113
#3  0x0000005af41f2865 in epee::critical_section::lock (this=0x5af8be3058) at /home/software/bitmonero/contrib/epee/include/syncobj.h:100
#4  epee::critical_region_t<epee::critical_section>::critical_region_t (cs=..., this=0x7fd31e3f8fa0) at /home/software/bitmonero/contrib/epee/include/syncobj.h:133
(More stack frames follow...)

Thread 10 (Thread 0x7fd31f7fe700 (LWP 4144)):
#0  0x00007fd32a7301ad in pthread_cond_wait@@GLIBC_2.3.2 () from /usr/lib/libpthread.so.0
#1  0x0000005af3fd27d5 in boost::condition_variable::wait (this=0x7fd3181cb798, m=...) at /usr/include/boost/thread/pthread/condition_variable.hpp:76
#2  0x00007fd32b8fdf9d in boost::thread::join_noexcept() () from /usr/lib/libboost_thread.so.1.64.0
#3  0x0000005af41d82e5 in boost::thread::join (this=0x7fd3181c6d80) at /usr/include/boost/thread/detail/thread.hpp:773
#4  boost::thread_group::join_all (this=this@entry=0x7fd31f7fbfb0) at /usr/include/boost/thread/detail/thread_group.hpp:119
(More stack frames follow...)

Thread 9 (Thread 0x7fd324b1a700 (LWP 4142)):
#0  0x00007fd32a7301ad in pthread_cond_wait@@GLIBC_2.3.2 () from /usr/lib/libpthread.so.0
#1  0x0000005af3fd27d5 in boost::condition_variable::wait (this=this@entry=0x5af8c3d778, m=...) at /usr/include/boost/thread/pthread/condition_variable.hpp:76
#2  0x0000005af3fd3a83 in epee::async_stdin_reader::get_line (line="", this=0x5af8c3d620) at /home/software/bitmonero/contrib/epee/include/console_handler.h:85
#3  epee::async_console_handler::run<bool epee::async_console_handler::run<boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::command_handler, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&>, boost::_bi::list2<boost::_bi::value<epee::console_handlers_binder*>, boost::arg<1> > > >(boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::command_handler, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&>, boost::_bi::list2<boost::_bi::value<epee::console_handlers_binder*>, boost::arg<1> > >, std::function<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > ()>, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::function<void ()>)::{lambda(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&)#1}>(std::function<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > ()>, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, bool epee::async_console_handler::run<boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::command_handler, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&>, boost::_bi::list2<boost::_bi::value<epee::console_handlers_binder*>, boost::arg<1> > > >(boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::command_handler, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&>, boost::_bi::list2<boost::_bi::value<epee::console_handlers_binder*>, boost::arg<1> > >, std::function<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > ()>, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::function<void ()>)::{lambda(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&)#1} const&, std::function<void ()>) (this=this@entry=0x5af8c3d620, prompt=..., usage="Monero 'Helium Hydra' (v0.11.0.0-release)\nCommands: \n  alt_chain_info          Print information about alternative chains\n  ban", ' ' <repeats 21 times>, "Ban a given IP for a time\n  bans", ' ' <repeats 20 times>..., cmd_handler=..., exit_handler=...) at /home/software/bitmonero/contrib/epee/include/console_handler.h:350
#4  0x0000005af3fd42fa in epee::async_console_handler::run<boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::command_handler, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&>, boost::_bi::list2<boost::_bi::value<epee::console_handlers_binder*>, boost::arg<1> > > >(boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::command_handler, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&>, boost::_bi::list2<boost::_bi::value<epee::console_handlers_binder*>, boost::arg<1> > >, std::function<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > ()>, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::function<void ()>) (exit_handler=..., usage="Monero 'Helium Hydra' (v0.11.0.0-release)\nCommands: \n  alt_chain_info          Print information about alternative chains\n  ban", ' ' <repeats 21 times>, "Ban a given IP for a time\n  bans", ' ' <repeats 20 times>..., prompt=..., ch_handler=..., this=0x5af8c3d620) at /home/software/bitmonero/contrib/epee/include/console_handler.h:302
(More stack frames follow...)

Thread 8 (Thread 0x7fd326eb7700 (LWP 4141)):
#0  0x00007fd32a460fd3 in select () from /usr/lib/libc.so.6
#1  0x0000005af3fd2c64 in epee::async_stdin_reader::wait_stdin_data (this=0x5af8c3d620) at /home/software/bitmonero/contrib/epee/include/console_handler.h:169
#2  epee::async_stdin_reader::reader_thread_func (this=0x5af8c3d620) at /home/software/bitmonero/contrib/epee/include/console_handler.h:206
#3  0x0000005af3fcd777 in std::__invoke_impl<void, void (epee::async_stdin_reader::*&)(), epee::async_stdin_reader*&> (__t=<optimized out>, __f=<optimized out>) at /usr/include/c++/7.1.1/bits/invoke.h:73
#4  std::__invoke<void (epee::async_stdin_reader::*&)(), epee::async_stdin_reader*&> (__fn=<optimized out>) at /usr/include/c++/7.1.1/bits/invoke.h:95
(More stack frames follow...)

Thread 7 (Thread 0x7fd3266b6700 (LWP 4140)):
#0  0x00007fd32a469473 in epoll_wait () from /usr/lib/libc.so.6
#1  0x0000005af3ffc7be in boost::asio::detail::epoll_reactor::run (ops=..., block=<optimized out>, this=0x5af8bf6860) at /usr/include/boost/asio/detail/impl/epoll_reactor.ipp:416
#2  boost::asio::detail::task_io_service::do_run_one (ec=..., this_thread=..., lock=..., this=<optimized out>) at /usr/include/boost/asio/detail/impl/task_io_service.ipp:356
#3  boost::asio::detail::task_io_service::run (ec=..., this=0x5af8bf6780) at /usr/include/boost/asio/detail/impl/task_io_service.ipp:149
#4  boost::asio::io_service::run (this=<optimized out>) at /usr/include/boost/asio/impl/io_service.ipp:59
(More stack frames follow...)

Thread 6 (Thread 0x7fd325eb5700 (LWP 4139)):
#0  0x00007fd32a7301ad in pthread_cond_wait@@GLIBC_2.3.2 () from /usr/lib/libpthread.so.0
#1  0x0000005af3ffcb89 in boost::asio::detail::posix_event::wait<boost::asio::detail::scoped_lock<boost::asio::detail::posix_mutex> > (lock=..., this=0x5af8bf67d8) at /usr/include/boost/asio/detail/posix_event.hpp:106
#2  boost::asio::detail::task_io_service::do_run_one (ec=..., this_thread=..., lock=..., this=<optimized out>) at /usr/include/boost/asio/detail/impl/task_io_service.ipp:380
#3  boost::asio::detail::task_io_service::run (ec=..., this=0x5af8bf6780) at /usr/include/boost/asio/detail/impl/task_io_service.ipp:149
#4  boost::asio::io_service::run (this=<optimized out>) at /usr/include/boost/asio/impl/io_service.ipp:59
(More stack frames follow...)

Thread 5 (Thread 0x7fd3256b4700 (LWP 4138)):
#0  0x00007fd32a7301ad in pthread_cond_wait@@GLIBC_2.3.2 () from /usr/lib/libpthread.so.0
#1  0x0000005af41d722c in boost::asio::detail::posix_event::wait<boost::asio::detail::scoped_lock<boost::asio::detail::posix_mutex> > (lock=..., this=0x5af8be47e8) at /usr/include/boost/asio/detail/posix_event.hpp:106
#2  boost::asio::detail::task_io_service::do_run_one (ec=..., this_thread=..., lock=..., this=<optimized out>) at /usr/include/boost/asio/detail/impl/task_io_service.ipp:380
#3  boost::asio::detail::task_io_service::run (ec=..., this=0x5af8be4790) at /usr/include/boost/asio/detail/impl/task_io_service.ipp:149
#4  boost::asio::io_service::run (this=<optimized out>) at /usr/include/boost/asio/impl/io_service.ipp:59
(More stack frames follow...)

Thread 4 (Thread 0x7fd3273b8700 (LWP 4133)):
#0  0x00007fd32a7301ad in pthread_cond_wait@@GLIBC_2.3.2 () from /usr/lib/libpthread.so.0
#1  0x0000005af422f8b6 in boost::condition_variable::wait (m=..., this=0x5af8be3be8) at /usr/include/boost/thread/pthread/condition_variable.hpp:76
#2  boost::condition_variable::wait<tools::thread_group::data::run()::<lambda()> > (pred=..., m=..., this=0x5af8be3be8) at /usr/include/boost/thread/pthread/condition_variable_fwd.hpp:129
#3  tools::thread_group::data::run (this=0x5af8be3bc0) at /home/software/bitmonero/src/common/thread_group.cpp:128
#4  0x0000005af4231579 in boost::_mfi::mf0<void, tools::thread_group::data>::operator() (p=<optimized out>, this=<optimized out>) at /usr/include/boost/bind/mem_fn_template.hpp:49
(More stack frames follow...)

Thread 3 (Thread 0x7fd3278b9700 (LWP 4132)):
#0  0x00007fd32a7301ad in pthread_cond_wait@@GLIBC_2.3.2 () from /usr/lib/libpthread.so.0
#1  0x0000005af422f8b6 in boost::condition_variable::wait (m=..., this=0x5af8be3be8) at /usr/include/boost/thread/pthread/condition_variable.hpp:76
#2  boost::condition_variable::wait<tools::thread_group::data::run()::<lambda()> > (pred=..., m=..., this=0x5af8be3be8) at /usr/include/boost/thread/pthread/condition_variable_fwd.hpp:129
#3  tools::thread_group::data::run (this=0x5af8be3bc0) at /home/software/bitmonero/src/common/thread_group.cpp:128
#4  0x0000005af4231579 in boost::_mfi::mf0<void, tools::thread_group::data>::operator() (p=<optimized out>, this=<optimized out>) at /usr/include/boost/bind/mem_fn_template.hpp:49
(More stack frames follow...)

Thread 2 (Thread 0x7fd327dba700 (LWP 4131)):
#0  0x00007fd32a7301ad in pthread_cond_wait@@GLIBC_2.3.2 () from /usr/lib/libpthread.so.0
#1  0x0000005af422f8b6 in boost::condition_variable::wait (m=..., this=0x5af8be3be8) at /usr/include/boost/thread/pthread/condition_variable.hpp:76
#2  boost::condition_variable::wait<tools::thread_group::data::run()::<lambda()> > (pred=..., m=..., this=0x5af8be3be8) at /usr/include/boost/thread/pthread/condition_variable_fwd.hpp:129
#3  tools::thread_group::data::run (this=0x5af8be3bc0) at /home/software/bitmonero/src/common/thread_group.cpp:128
#4  0x0000005af4231579 in boost::_mfi::mf0<void, tools::thread_group::data>::operator() (p=<optimized out>, this=<optimized out>) at /usr/include/boost/bind/mem_fn_template.hpp:49
(More stack frames follow...)

Thread 1 (Thread 0x7fd32d38bb80 (LWP 4130)):
#0  0x00007fd32a7301ad in pthread_cond_wait@@GLIBC_2.3.2 () from /usr/lib/libpthread.so.0
#1  0x0000005af3fd27d5 in boost::condition_variable::wait (this=0x5af8c3a168, m=...) at /usr/include/boost/thread/pthread/condition_variable.hpp:76
#2  0x00007fd32b8fdf9d in boost::thread::join_noexcept() () from /usr/lib/libboost_thread.so.1.64.0
#3  0x0000005af409cd44 in boost::thread::join (this=0x5af8c3b5b0) at /usr/include/boost/thread/detail/thread.hpp:773
#4  epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::run_server (this=this@entry=0x5af8be3fb8, threads_count=threads_count@entry=10, wait=wait@entry=true, attrs=...) at /home/software/bitmonero/contrib/epee/include/net/abstract_tcp_server2.inl:830
(More stack frames follow...)
(gdb) bt
#0  0x00007fd32a72c6bc in __pthread_mutex_lock_full () from /usr/lib/libpthread.so.0
#1  0x0000005af42487ab in mdb_txn_renew0 (txn=0x7fc7380009d0) at /home/software/bitmonero/external/db_drivers/liblmdb/mdb.c:2878
#2  0x0000005af424906f in mdb_txn_begin (env=0x5af8c01810, parent=0x0, flags=131072, ret=0x7fc738000950) at /home/software/bitmonero/external/db_drivers/liblmdb/mdb.c:3096
#3  0x0000005af418cf18 in cryptonote::lmdb_txn_begin (txn=0x7fc738000950, flags=131072, parent=0x0, env=0x5af8c01810) at /home/software/bitmonero/src/blockchain_db/lmdb/db_lmdb.cpp:414
#4  cryptonote::BlockchainLMDB::block_rtxn_start (this=0x5af8bfb4a0, mtxn=0x7fc758c109e0, mcur=0x7fc758c109e8) at /home/software/bitmonero/src/blockchain_db/lmdb/db_lmdb.cpp:2694
#5  0x0000005af41a5621 in cryptonote::BlockchainLMDB::get_output_key (this=0x5af8bfb4a0, amount=@0x7fc758c10c98: 90000000, offsets=std::vector of length 5, capacity 8 = {...}, outputs=std::vector of length 0, capacity 0, allow_partial=<optimized out>) at /home/software/bitmonero/src/blockchain_db/lmdb/db_lmdb.cpp:2913
#6  0x0000005af41ae746 in cryptonote::Blockchain::output_scan_worker (this=<optimized out>, amount=<optimized out>, offsets=..., outputs=..., txs=...) at /home/software/bitmonero/src/cryptonote_core/blockchain.cpp:3645
#7  0x0000005af41de198 in boost::_mfi::cmf4<void, cryptonote::Blockchain, unsigned long, std::vector<unsigned long, std::allocator<unsigned long> > const&, std::vector<cryptonote::output_data_t, std::allocator<cryptonote::output_data_t> >&, std::unordered_map<crypto::hash, cryptonote::transaction, std::hash<crypto::hash>, std::equal_to<crypto::hash>, std::allocator<std::pair<crypto::hash const, cryptonote::transaction> > >&>::call<cryptonote::Blockchain* const, unsigned long, std::vector<unsigned long, std::allocator<unsigned long> > const, std::vector<cryptonote::output_data_t, std::allocator<cryptonote::output_data_t> >, std::unordered_map<crypto::hash, cryptonote::transaction, std::hash<crypto::hash>, std::equal_to<crypto::hash>, std::allocator<std::pair<crypto::hash const, cryptonote::transaction> > > > (b4=std::unordered_map with 0 elements, b3=std::vector of length 0, capacity 0, b2=std::vector of length 5, capacity 8 = {...}, b1=<synthetic pointer>: <optimized out>, u=@0x7fc758c10d70: 0x5af8be3138, this=0x7fc758c10d60) at /usr/include/boost/bind/mem_fn_template.hpp:561
#8  boost::_mfi::cmf4<void, cryptonote::Blockchain, unsigned long, std::vector<unsigned long, std::allocator<unsigned long> > const&, std::vector<cryptonote::output_data_t, std::allocator<cryptonote::output_data_t> >&, std::unordered_map<crypto::hash, cryptonote::transaction, std::hash<crypto::hash>, std::equal_to<crypto::hash>, std::allocator<std::pair<crypto::hash const, cryptonote::transaction> > >&>::operator()<cryptonote::Blockchain*> (a4=..., a3=..., a2=..., a1=90000000, u=@0x7fc758c10d70: 0x5af8be3138, this=<optimized out>) at /usr/include/boost/bind/mem_fn_template.hpp:571
#9  boost::_bi::list5<boost::_bi::value<cryptonote::Blockchain*>, boost::_bi::value<unsigned long>, boost::_bi::value<std::reference_wrapper<std::vector<unsigned long, std::allocator<unsigned long> > const> >, boost::_bi::value<std::reference_wrapper<std::vector<cryptonote::output_data_t, std::allocator<cryptonote::output_data_t> > > >, boost::_bi::value<std::reference_wrapper<std::unordered_map<crypto::hash, cryptonote::transaction, std::hash<crypto::hash>, std::equal_to<crypto::hash>, std::allocator<std::pair<crypto::hash const, cryptonote::transaction> > > > > >::operator()<boost::_mfi::cmf4<void, cryptonote::Blockchain, unsigned long, std::vector<unsigned long, std::allocator<unsigned long> > const&, std::vector<cryptonote::output_data_t, std::allocator<cryptonote::output_data_t> >&, std::unordered_map<crypto::hash, cryptonote::transaction, std::hash<crypto::hash>, std::equal_to<crypto::hash>, std::allocator<std::pair<crypto::hash const, cryptonote::transaction> > >&>, boost::_bi::list0> (a=<synthetic pointer>..., f=..., this=0x7fc758c10d70) at /usr/include/boost/bind/bind.hpp:531
#10 boost::_bi::bind_t<void, boost::_mfi::cmf4<void, cryptonote::Blockchain, unsigned long, std::vector<unsigned long, std::allocator<unsigned long> > const&, std::vector<cryptonote::output_data_t, std::allocator<cryptonote::output_data_t> >&, std::unordered_map<crypto::hash, cryptonote::transaction, std::hash<crypto::hash>, std::equal_to<crypto::hash>, std::allocator<std::pair<crypto::hash const, cryptonote::transaction> > >&>, boost::_bi::list5<boost::_bi::value<cryptonote::Blockchain*>, boost::_bi::value<unsigned long>, boost::_bi::value<std::reference_wrapper<std::vector<unsigned long, std::allocator<unsigned long> > const> >, boost::_bi::value<std::reference_wrapper<std::vector<cryptonote::output_data_t, std::allocator<cryptonote::output_data_t> > > >, boost::_bi::value<std::reference_wrapper<std::unordered_map<crypto::hash, cryptonote::transaction, std::hash<crypto::hash>, std::equal_to<crypto::hash>, std::allocator<std::pair<crypto::hash const, cryptonote::transaction> > > > > > >::operator() (this=0x7fc758c10d60) at /usr/include/boost/bind/bind.hpp:1294
#11 boost::asio::asio_handler_invoke<boost::_bi::bind_t<void, boost::_mfi::cmf4<void, cryptonote::Blockchain, unsigned long, std::vector<unsigned long, std::allocator<unsigned long> > const&, std::vector<cryptonote::output_data_t, std::allocator<cryptonote::output_data_t> >&, std::unordered_map<crypto::hash, cryptonote::transaction, std::hash<crypto::hash>, std::equal_to<crypto::hash>, std::allocator<std::pair<crypto::hash const, cryptonote::transaction> > >&>, boost::_bi::list5<boost::_bi::value<cryptonote::Blockchain*>, boost::_bi::value<unsigned long>, boost::_bi::value<std::reference_wrapper<std::vector<unsigned long, std::allocator<unsigned long> > const> >, boost::_bi::value<std::reference_wrapper<std::vector<cryptonote::output_data_t, std::allocator<cryptonote::output_data_t> > > >, boost::_bi::value<std::reference_wrapper<std::unordered_map<crypto::hash, cryptonote::transaction, std::hash<crypto::hash>, std::equal_to<crypto::hash>, std::allocator<std::pair<crypto::hash const, cryptonote::transaction> > > > > > > > (function=...) at /usr/include/boost/asio/handler_invoke_hook.hpp:69
#12 boost_asio_handler_invoke_helpers::invoke<boost::_bi::bind_t<void, boost::_mfi::cmf4<void, cryptonote::Blockchain, unsigned long, std::vector<unsigned long, std::allocator<unsigned long> > const&, std::vector<cryptonote::output_data_t, std::allocator<cryptonote::output_data_t> >&, std::unordered_map<crypto::hash, cryptonote::transaction, std::hash<crypto::hash>, std::equal_to<crypto::hash>, std::allocator<std::pair<crypto::hash const, cryptonote::transaction> > >&>, boost::_bi::list5<boost::_bi::value<cryptonote::Blockchain*>, boost::_bi::value<unsigned long>, boost::_bi::value<std::reference_wrapper<std::vector<unsigned long, std::allocator<unsigned long> > const> >, boost::_bi::value<std::reference_wrapper<std::vector<cryptonote::output_data_t, std::allocator<cryptonote::output_data_t> > > >, boost::_bi::value<std::reference_wrapper<std::unordered_map<crypto::hash, cryptonote::transaction, std::hash<crypto::hash>, std::equal_to<crypto::hash>, std::allocator<std::pair<crypto::hash const, cryptonote::transaction> > > > > > >, boost::_bi::bind_t<void, boost::_mfi::cmf4<void, cryptonote::Blockchain, unsigned long, std::vector<unsigned long, std::allocator<unsigned long> > const&, std::vector<cryptonote::output_data_t, std::allocator<cryptonote::output_data_t> >&, std::unordered_map<crypto::hash, cryptonote::transaction, std::hash<crypto::hash>, std::equal_to<crypto::hash>, std::allocator<std::pair<crypto::hash const, cryptonote::transaction> > >&>, boost::_bi::list5<boost::_bi::value<cryptonote::Blockchain*>, boost::_bi::value<unsigned long>, boost::_bi::value<std::reference_wrapper<std::vector<unsigned long, std::allocator<unsigned long> > const> >, boost::_bi::value<std::reference_wrapper<std::vector<cryptonote::output_data_t, std::allocator<cryptonote::output_data_t> > > >, boost::_bi::value<std::reference_wrapper<std::unordered_map<crypto::hash, cryptonote::transaction, std::hash<crypto::hash>, std::equal_to<crypto::hash>, std::allocator<std::pair<crypto::hash const, cryptonote::transaction> > > > > > > > (context=..., function=...) at /usr/include/boost/asio/detail/handler_invoke_helpers.hpp:37
#13 boost::asio::detail::completion_handler<boost::_bi::bind_t<void, boost::_mfi::cmf4<void, cryptonote::Blockchain, unsigned long, std::vector<unsigned long, std::allocator<unsigned long> > const&, std::vector<cryptonote::output_data_t, std::allocator<cryptonote::output_data_t> >&, std::unordered_map<crypto::hash, cryptonote::transaction, std::hash<crypto::hash>, std::equal_to<crypto::hash>, std::allocator<std::pair<crypto::hash const, cryptonote::transaction> > >&>, boost::_bi::list5<boost::_bi::value<cryptonote::Blockchain*>, boost::_bi::value<unsigned long>, boost::_bi::value<std::reference_wrapper<std::vector<unsigned long, std::allocator<unsigned long> > const> >, boost::_bi::value<std::reference_wrapper<std::vector<cryptonote::output_data_t, std::allocator<cryptonote::output_data_t> > > >, boost::_bi::value<std::reference_wrapper<std::unordered_map<crypto::hash, cryptonote::transaction, std::hash<crypto::hash>, std::equal_to<crypto::hash>, std::allocator<std::pair<crypto::hash const, cryptonote::transaction> > > > > > > >::do_complete (owner=<optimized out>, base=<optimized out>) at /usr/include/boost/asio/detail/completion_handler.hpp:68
#14 0x0000005af41d6fdf in boost::asio::detail::task_io_service_operation::complete (bytes_transferred=0, ec=..., owner=..., this=0x7fd3181bb140) at /usr/include/boost/asio/detail/task_io_service_operation.hpp:38
#15 boost::asio::detail::task_io_service::do_run_one (ec=..., this_thread=..., lock=..., this=<optimized out>) at /usr/include/boost/asio/detail/impl/task_io_service.ipp:372
#16 boost::asio::detail::task_io_service::run (ec=..., this=0x7fd3181baa60) at /usr/include/boost/asio/detail/impl/task_io_service.ipp:149
#17 boost::asio::io_service::run (this=<optimized out>) at /usr/include/boost/asio/impl/io_service.ipp:59
#18 0x0000005af41d363b in boost::_mfi::mf0<unsigned long, boost::asio::io_service>::operator() (p=<optimized out>, this=<optimized out>) at /usr/include/boost/bind/mem_fn_template.hpp:49
#19 boost::_bi::list1<boost::_bi::value<boost::asio::io_service*> >::operator()<unsigned long, boost::_mfi::mf0<unsigned long, boost::asio::io_service>, boost::_bi::list0> (a=<synthetic pointer>..., f=..., this=<optimized out>) at /usr/include/boost/bind/bind.hpp:249
#20 boost::_bi::bind_t<unsigned long, boost::_mfi::mf0<unsigned long, boost::asio::io_service>, boost::_bi::list1<boost::_bi::value<boost::asio::io_service*> > >::operator() (this=<optimized out>) at /usr/include/boost/bind/bind.hpp:1294
#21 boost::detail::thread_data<boost::_bi::bind_t<unsigned long, boost::_mfi::mf0<unsigned long, boost::asio::io_service>, boost::_bi::list1<boost::_bi::value<boost::asio::io_service*> > > >::run (this=<optimized out>) at /usr/include/boost/thread/detail/thread.hpp:116
#22 0x00007fd32b8fda6f in ?? () from /usr/lib/libboost_thread.so.1.64.0
#23 0x00007fd32a72a049 in start_thread () from /usr/lib/libpthread.so.0
#24 0x00007fd32a468f0f in clone () from /usr/lib/libc.so.6
(gdb) thr 15
[Switching to thread 15 (Thread 0x7fc759412700 (LWP 14143))]
#0  0x00007fd32a72c6bc in __pthread_mutex_lock_full () from /usr/lib/libpthread.so.0
(gdb) bt
#0  0x00007fd32a72c6bc in __pthread_mutex_lock_full () from /usr/lib/libpthread.so.0
#1  0x0000005af42487ab in mdb_txn_renew0 (txn=0x7fc7240009b0) at /home/software/bitmonero/external/db_drivers/liblmdb/mdb.c:2878
#2  0x0000005af424906f in mdb_txn_begin (env=0x5af8c01810, parent=0x0, flags=131072, ret=0x7fc7240008e0) at /home/software/bitmonero/external/db_drivers/liblmdb/mdb.c:3096
#3  0x0000005af418cf18 in cryptonote::lmdb_txn_begin (txn=0x7fc7240008e0, flags=131072, parent=0x0, env=0x5af8c01810) at /home/software/bitmonero/src/blockchain_db/lmdb/db_lmdb.cpp:414
#4  cryptonote::BlockchainLMDB::block_rtxn_start (this=0x5af8bfb4a0, mtxn=0x7fc7594119e0, mcur=0x7fc7594119e8) at /home/software/bitmonero/src/blockchain_db/lmdb/db_lmdb.cpp:2694
#5  0x0000005af41a5621 in cryptonote::BlockchainLMDB::get_output_key (this=0x5af8bfb4a0, amount=@0x7fc759411c98: 8000000000, offsets=std::vector of length 10, capacity 16 = {...}, outputs=std::vector of length 0, capacity 0, allow_partial=<optimized out>) at /home/software/bitmonero/src/blockchain_db/lmdb/db_lmdb.cpp:2913
#6  0x0000005af41ae746 in cryptonote::Blockchain::output_scan_worker (this=<optimized out>, amount=<optimized out>, offsets=..., outputs=..., txs=...) at /home/software/bitmonero/src/cryptonote_core/blockchain.cpp:3645
#7  0x0000005af41de198 in boost::_mfi::cmf4<void, cryptonote::Blockchain, unsigned long, std::vector<unsigned long, std::allocator<unsigned long> > const&, std::vector<cryptonote::output_data_t, std::allocator<cryptonote::output_data_t> >&, std::unordered_map<crypto::hash, cryptonote::transaction, std::hash<crypto::hash>, std::equal_to<crypto::hash>, std::allocator<std::pair<crypto::hash const, cryptonote::transaction> > >&>::call<cryptonote::Blockchain* const, unsigned long, std::vector<unsigned long, std::allocator<unsigned long> > const, std::vector<cryptonote::output_data_t, std::allocator<cryptonote::output_data_t> >, std::unordered_map<crypto::hash, cryptonote::transaction, std::hash<crypto::hash>, std::equal_to<crypto::hash>, std::allocator<std::pair<crypto::hash const, cryptonote::transaction> > > > (b4=std::unordered_map with 0 elements, b3=std::vector of length 0, capacity 0, b2=std::vector of length 10, capacity 16 = {...}, b1=<synthetic pointer>: <optimized out>, u=@0x7fc759411d70: 0x5af8be3138, this=0x7fc759411d60) at /usr/include/boost/bind/mem_fn_template.hpp:561
#8  boost::_mfi::cmf4<void, cryptonote::Blockchain, unsigned long, std::vector<unsigned long, std::allocator<unsigned long> > const&, std::vector<cryptonote::output_data_t, std::allocator<cryptonote::output_data_t> >&, std::unordered_map<crypto::hash, cryptonote::transaction, std::hash<crypto::hash>, std::equal_to<crypto::hash>, std::allocator<std::pair<crypto::hash const, cryptonote::transaction> > >&>::operator()<cryptonote::Blockchain*> (a4=..., a3=..., a2=..., a1=8000000000, u=@0x7fc759411d70: 0x5af8be3138, this=<optimized out>) at /usr/include/boost/bind/mem_fn_template.hpp:571
#9  boost::_bi::list5<boost::_bi::value<cryptonote::Blockchain*>, boost::_bi::value<unsigned long>, boost::_bi::value<std::reference_wrapper<std::vector<unsigned long, std::allocator<unsigned long> > const> >, boost::_bi::value<std::reference_wrapper<std::vector<cryptonote::output_data_t, std::allocator<cryptonote::output_data_t> > > >, boost::_bi::value<std::reference_wrapper<std::unordered_map<crypto::hash, cryptonote::transaction, std::hash<crypto::hash>, std::equal_to<crypto::hash>, std::allocator<std::pair<crypto::hash const, cryptonote::transaction> > > > > >::operator()<boost::_mfi::cmf4<void, cryptonote::Blockchain, unsigned long, std::vector<unsigned long, std::allocator<unsigned long> > const&, std::vector<cryptonote::output_data_t, std::allocator<cryptonote::output_data_t> >&, std::unordered_map<crypto::hash, cryptonote::transaction, std::hash<crypto::hash>, std::equal_to<crypto::hash>, std::allocator<std::pair<crypto::hash const, cryptonote::transaction> > >&>, boost::_bi::list0> (a=<synthetic pointer>..., f=..., this=0x7fc759411d70) at /usr/include/boost/bind/bind.hpp:531
#10 boost::_bi::bind_t<void, boost::_mfi::cmf4<void, cryptonote::Blockchain, unsigned long, std::vector<unsigned long, std::allocator<unsigned long> > const&, std::vector<cryptonote::output_data_t, std::allocator<cryptonote::output_data_t> >&, std::unordered_map<crypto::hash, cryptonote::transaction, std::hash<crypto::hash>, std::equal_to<crypto::hash>, std::allocator<std::pair<crypto::hash const, cryptonote::transaction> > >&>, boost::_bi::list5<boost::_bi::value<cryptonote::Blockchain*>, boost::_bi::value<unsigned long>, boost::_bi::value<std::reference_wrapper<std::vector<unsigned long, std::allocator<unsigned long> > const> >, boost::_bi::value<std::reference_wrapper<std::vector<cryptonote::output_data_t, std::allocator<cryptonote::output_data_t> > > >, boost::_bi::value<std::reference_wrapper<std::unordered_map<crypto::hash, cryptonote::transaction, std::hash<crypto::hash>, std::equal_to<crypto::hash>, std::allocator<std::pair<crypto::hash const, cryptonote::transaction> > > > > > >::operator() (this=0x7fc759411d60) at /usr/include/boost/bind/bind.hpp:1294
#11 boost::asio::asio_handler_invoke<boost::_bi::bind_t<void, boost::_mfi::cmf4<void, cryptonote::Blockchain, unsigned long, std::vector<unsigned long, std::allocator<unsigned long> > const&, std::vector<cryptonote::output_data_t, std::allocator<cryptonote::output_data_t> >&, std::unordered_map<crypto::hash, cryptonote::transaction, std::hash<crypto::hash>, std::equal_to<crypto::hash>, std::allocator<std::pair<crypto::hash const, cryptonote::transaction> > >&>, boost::_bi::list5<boost::_bi::value<cryptonote::Blockchain*>, boost::_bi::value<unsigned long>, boost::_bi::value<std::reference_wrapper<std::vector<unsigned long, std::allocator<unsigned long> > const> >, boost::_bi::value<std::reference_wrapper<std::vector<cryptonote::output_data_t, std::allocator<cryptonote::output_data_t> > > >, boost::_bi::value<std::reference_wrapper<std::unordered_map<crypto::hash, cryptonote::transaction, std::hash<crypto::hash>, std::equal_to<crypto::hash>, std::allocator<std::pair<crypto::hash const, cryptonote::transaction> > > > > > > > (function=...) at /usr/include/boost/asio/handler_invoke_hook.hpp:69
#12 boost_asio_handler_invoke_helpers::invoke<boost::_bi::bind_t<void, boost::_mfi::cmf4<void, cryptonote::Blockchain, unsigned long, std::vector<unsigned long, std::allocator<unsigned long> > const&, std::vector<cryptonote::output_data_t, std::allocator<cryptonote::output_data_t> >&, std::unordered_map<crypto::hash, cryptonote::transaction, std::hash<crypto::hash>, std::equal_to<crypto::hash>, std::allocator<std::pair<crypto::hash const, cryptonote::transaction> > >&>, boost::_bi::list5<boost::_bi::value<cryptonote::Blockchain*>, boost::_bi::value<unsigned long>, boost::_bi::value<std::reference_wrapper<std::vector<unsigned long, std::allocator<unsigned long> > const> >, boost::_bi::value<std::reference_wrapper<std::vector<cryptonote::output_data_t, std::allocator<cryptonote::output_data_t> > > >, boost::_bi::value<std::reference_wrapper<std::unordered_map<crypto::hash, cryptonote::transaction, std::hash<crypto::hash>, std::equal_to<crypto::hash>, std::allocator<std::pair<crypto::hash const, cryptonote::transaction> > > > > > >, boost::_bi::bind_t<void, boost::_mfi::cmf4<void, cryptonote::Blockchain, unsigned long, std::vector<unsigned long, std::allocator<unsigned long> > const&, std::vector<cryptonote::output_data_t, std::allocator<cryptonote::output_data_t> >&, std::unordered_map<crypto::hash, cryptonote::transaction, std::hash<crypto::hash>, std::equal_to<crypto::hash>, std::allocator<std::pair<crypto::hash const, cryptonote::transaction> > >&>, boost::_bi::list5<boost::_bi::value<cryptonote::Blockchain*>, boost::_bi::value<unsigned long>, boost::_bi::value<std::reference_wrapper<std::vector<unsigned long, std::allocator<unsigned long> > const> >, boost::_bi::value<std::reference_wrapper<std::vector<cryptonote::output_data_t, std::allocator<cryptonote::output_data_t> > > >, boost::_bi::value<std::reference_wrapper<std::unordered_map<crypto::hash, cryptonote::transaction, std::hash<crypto::hash>, std::equal_to<crypto::hash>, std::allocator<std::pair<crypto::hash const, cryptonote::transaction> > > > > > > > (context=..., function=...) at /usr/include/boost/asio/detail/handler_invoke_helpers.hpp:37
#13 boost::asio::detail::completion_handler<boost::_bi::bind_t<void, boost::_mfi::cmf4<void, cryptonote::Blockchain, unsigned long, std::vector<unsigned long, std::allocator<unsigned long> > const&, std::vector<cryptonote::output_data_t, std::allocator<cryptonote::output_data_t> >&, std::unordered_map<crypto::hash, cryptonote::transaction, std::hash<crypto::hash>, std::equal_to<crypto::hash>, std::allocator<std::pair<crypto::hash const, cryptonote::transaction> > >&>, boost::_bi::list5<boost::_bi::value<cryptonote::Blockchain*>, boost::_bi::value<unsigned long>, boost::_bi::value<std::reference_wrapper<std::vector<unsigned long, std::allocator<unsigned long> > const> >, boost::_bi::value<std::reference_wrapper<std::vector<cryptonote::output_data_t, std::allocator<cryptonote::output_data_t> > > >, boost::_bi::value<std::reference_wrapper<std::unordered_map<crypto::hash, cryptonote::transaction, std::hash<crypto::hash>, std::equal_to<crypto::hash>, std::allocator<std::pair<crypto::hash const, cryptonote::transaction> > > > > > > >::do_complete (owner=<optimized out>, base=<optimized out>) at /usr/include/boost/asio/detail/completion_handler.hpp:68
#14 0x0000005af41d6fdf in boost::asio::detail::task_io_service_operation::complete (bytes_transferred=0, ec=..., owner=..., this=0x7fd3181fcf80) at /usr/include/boost/asio/detail/task_io_service_operation.hpp:38
#15 boost::asio::detail::task_io_service::do_run_one (ec=..., this_thread=..., lock=..., this=<optimized out>) at /usr/include/boost/asio/detail/impl/task_io_service.ipp:372
#16 boost::asio::detail::task_io_service::run (ec=..., this=0x7fd3181baa60) at /usr/include/boost/asio/detail/impl/task_io_service.ipp:149
#17 boost::asio::io_service::run (this=<optimized out>) at /usr/include/boost/asio/impl/io_service.ipp:59
#18 0x0000005af41d363b in boost::_mfi::mf0<unsigned long, boost::asio::io_service>::operator() (p=<optimized out>, this=<optimized out>) at /usr/include/boost/bind/mem_fn_template.hpp:49
#19 boost::_bi::list1<boost::_bi::value<boost::asio::io_service*> >::operator()<unsigned long, boost::_mfi::mf0<unsigned long, boost::asio::io_service>, boost::_bi::list0> (a=<synthetic pointer>..., f=..., this=<optimized out>) at /usr/include/boost/bind/bind.hpp:249
#20 boost::_bi::bind_t<unsigned long, boost::_mfi::mf0<unsigned long, boost::asio::io_service>, boost::_bi::list1<boost::_bi::value<boost::asio::io_service*> > >::operator() (this=<optimized out>) at /usr/include/boost/bind/bind.hpp:1294
#21 boost::detail::thread_data<boost::_bi::bind_t<unsigned long, boost::_mfi::mf0<unsigned long, boost::asio::io_service>, boost::_bi::list1<boost::_bi::value<boost::asio::io_service*> > > >::run (this=<optimized out>) at /usr/include/boost/thread/detail/thread.hpp:116
#22 0x00007fd32b8fda6f in ?? () from /usr/lib/libboost_thread.so.1.64.0
#23 0x00007fd32a72a049 in start_thread () from /usr/lib/libpthread.so.0
#24 0x00007fd32a468f0f in clone () from /usr/lib/libc.so.6
(gdb) frame 1
#1  0x0000005af42487ab in mdb_txn_renew0 (txn=0x7fc7240009b0) at /home/software/bitmonero/external/db_drivers/liblmdb/mdb.c:2878
2878					if (LOCK_MUTEX(rc, env, rmutex))
(gdb) p *env
$7 = {me_fd = 17, me_lfd = 16, me_mfd = 18, me_flags = 813760512, me_psize = 4096, me_os_psize = 4096, me_maxreaders = 126, me_close_readers = 15, me_numdbs = 16, me_maxdbs = 22, me_pid = 4130, me_path = 0x5af8c01770 "/home/hyc/.bitmonero/lmdb", me_map = 0x7fc759413000 "", me_txns = 0x7fd32d3b3000, me_metas = {0x7fc759413010, 0x7fc759414010}, me_pbuf = 0x5af8c01df0, me_txn = 0x5af8c02e00, me_txn0 = 0x5af8c02e00, me_mapsize = 50176352256, me_size = 0, me_maxpg = 12250086, me_dbxs = 0x5af8c01960, me_dbflags = 0x5af8c017a0, me_dbiseqs = 0x5af8c01d90, me_txkey = 3, me_pgoldest = 45011, me_pgstate = {mf_pghead = 0x0, mf_pglast = 0}, me_dpages = 0x7fd318212530, me_free_pgs = 0x7fd32d23f018, me_dirty_list = 0x7fd324cb3010, me_maxfree_1pg = 509, me_nodemax = 2038, me_live_reader = 1, me_userctx = 0x0, me_assert_func = 0x0}
(gdb) p *env->me_txns
$8 = {mt1 = {mtb = {mtb_magic = 3203383518, mtb_format = 65537, mtb_txnid = 45036, mtb_numreaders = 15, mtb_rmutex = {{__data = {__lock = -2147483648, __count = 1, __owner = 0, __nusers = 0, __kind = 144, __spins = 0, __elision = 0, __list = {__prev = 0x0, __next = 0x0}}, __size = "\000\000\000\200\001", '\000' <repeats 11 times>, "\220", '\000' <repeats 22 times>, __align = 6442450944}}}, pad = "\336\300\357\276\001\000\001\000\354\257\000\000\000\000\000\000\017\000\000\000\000\000\000\000\000\000\000\200\001", '\000' <repeats 11 times>, "\220", '\000' <repeats 22 times>}, mt2 = {mt2_wmutex = {{__data = {__lock = 4144, __count = 1, __owner = 4144, __nusers = 1, __kind = 144, __spins = 0, __elision = 0, __list = {__prev = 0x7fd31f7fe9e0, __next = 0x7fd31f7fe9e0}}, __size = "0\020\000\000\001\000\000\000\060\020\000\000\001\000\000\000\220\000\000\000\000\000\000\000\340\351\177\037\323\177\000\000\340\351\177\037\323\177\000", __align = 4294971440}}, pad = "0\020\000\000\001\000\000\000\060\020\000\000\001\000\000\000\220\000\000\000\000\000\000\000\340\351\177\037\323\177\000\000\340\351\177\037\323\177", '\000' <repeats 25 times>}, mti_readers = {{mru = {mrx = {mrb_txnid = 18446744073709551615, mrb_pid = 4130, mrb_tid = 140544973519744}, pad = "\377\377\377\377\377\377\377\377\"\020\000\000\000\000\000\000\200\273\070-\323\177", '\000' <repeats 41 times>}}}}
(gdb) 
````
The hang is when attempting to lock the LMDB reader mutex. But inspection shows that that mutex actually has no owner at the moment, so the lock attempt should have already succeeded. This appears to be a glibc bug.

## hyc | 2017-09-07T11:42:30+00:00
Confirmed, this is a glibc bug https://sourceware.org/bugzilla/show_bug.cgi?id=21778 introduced in glibc 2.25 and fixed in 2.26.

## moneromooo-monero | 2017-11-14T19:46:09+00:00
We can't do much about this, but the newest monero now warns if you're running glibc 2.25, so I'll call that fixed :)

+resolved

## benma | 2017-11-14T20:34:10+00:00
@hyc huge props for tracking this down! Amazing work.

# Action History
- Created by: benma | 2017-08-22T06:58:52+00:00
- Closed at: 2017-11-14T20:32:29+00:00
