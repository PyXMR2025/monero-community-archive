---
title: '[aarch64/Manjaro]  monerod dies after completing sync'
source_url: https://github.com/monero-project/monero/issues/7950
author: Dendrocalamus64
assignees: []
labels: []
created_at: '2021-09-17T18:01:06+00:00'
updated_at: '2021-10-11T18:00:36+00:00'
type: issue
status: closed
closed_at: '2021-10-11T18:00:36+00:00'
---

# Original Description
Still running on a Rockpro64, 4GB RAM model, OS: Latest Manjaro ARM release.
Monero version: Monero 'Oxygen Orion' (v0.17.2.3-release)

Sync completes successfully, but as soon as monerod starts trying to run in earnest, it dies.  If there are new blocks to sync after it's restarted, it syncs those, then dies again.

EDIT: Running it interactively, instead of with --detach, it gives an error message:
```
/usr/include/c++/10.2.0/bits/stl_vector.h:1045: std::vector<_Tp, _Alloc>::reference std::vector<_Tp, _Alloc>::operator[](std::vector<_Tp, _Alloc>::size_type) [with _Tp = cryptonote::block; _Alloc = std::allocator<cryptonote::block>; std::vector<_Tp, _Alloc>::reference = cryptonote::block&; std::vector<_Tp, _Alloc>::size_type = long unsigned int]: Assertion '__builtin_expect(__n < this->size(), true)' failed.
Aborted
```

Starting at log level 2, there is consistent output at the end of the log file each time.  Typical example:
```
2021-09-17 17:40:11.390 [P2P1]  DEBUG   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:694  [get_estimated_batch_size] m_height: 2451516  block_start: 2451016  block_stop: 2451515
2021-09-17 17:40:11.390 [P2P1]  DEBUG   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:735  estimated average block size for batch: 22731
2021-09-17 17:40:11.390 [P2P1]  DEBUG   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:647  calculated batch size: 511447488
2021-09-17 17:40:11.390 [P2P1]  DEBUG   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:656  increase size: 536870912
2021-09-17 17:40:11.390 [P2P1]  DEBUG   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:608  DB map size:     51948479488
2021-09-17 17:40:11.390 [P2P1]  DEBUG   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:609  Space used:      41427308544
2021-09-17 17:40:11.390 [P2P1]  DEBUG   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:610  Space remaining: 10521170944
2021-09-17 17:40:11.390 [P2P1]  DEBUG   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:611  Size threshold:  511447488
2021-09-17 17:40:11.390 [P2P1]  DEBUG   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:613  Percent used: 79.7469  Percent threshold: 90.0000
2021-09-17 17:40:11.390 [P2P1]  DEBUG   blockchain      src/cryptonote_core/blockchain.cpp:4949 block_batches: 0
```

Log level 3:
```
2021-09-17 17:48:26.132 [P2P2]  TRACE   blockchain      src/cryptonote_core/blockchain.cpp:4886 Blockchain::prepare_handle_incoming_blocks
2021-09-17 17:48:26.132 [P2P2]  TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:3769 BlockchainLMDB::batch_start
2021-09-17 17:48:26.133 [P2P2]  TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:639  BlockchainLMDB::check_and_resize_for_batch
2021-09-17 17:48:26.133 [P2P2]  TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:640  [check_and_resize_for_batch] checking DB size
2021-09-17 17:48:26.133 [P2P2]  TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:671  BlockchainLMDB::get_estimated_batch_size
2021-09-17 17:48:26.133 [P2P2]  TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:2945 BlockchainLMDB::height
2021-09-17 17:48:26.133 [P2P2]  TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:3944 BlockchainLMDB::block_rtxn_start
2021-09-17 17:48:26.133 [P2P2]  TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:389  mdb_txn_safe: destructor
2021-09-17 17:48:26.134 [P2P2]  DEBUG   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:694  [get_estimated_batch_size] m_height: 2451516  block_start: 2451016  block_stop: 2451515
2021-09-17 17:48:26.134 [P2P2]  DEBUG   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:735  estimated average block size for batch: 22690
2021-09-17 17:48:26.134 [P2P2]  DEBUG   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:647  calculated batch size: 510524992
2021-09-17 17:48:26.134 [P2P2]  DEBUG   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:656  increase size: 536870912
2021-09-17 17:48:26.134 [P2P2]  TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:592  BlockchainLMDB::need_resize
2021-09-17 17:48:26.134 [P2P2]  DEBUG   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:608  DB map size:     51948479488
2021-09-17 17:48:26.135 [P2P2]  DEBUG   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:609  Space used:      41427308544
2021-09-17 17:48:26.135 [P2P2]  DEBUG   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:610  Space remaining: 10521170944
2021-09-17 17:48:26.135 [P2P2]  DEBUG   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:611  Size threshold:  510524992
2021-09-17 17:48:26.135 [P2P2]  DEBUG   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:613  Percent used: 79.7469  Percent threshold: 90.0000
2021-09-17 17:48:26.135 [P2P2]  TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:3806 batch transaction: begin
2021-09-17 17:48:26.135 [P2P2]  TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:2945 BlockchainLMDB::height
2021-09-17 17:48:26.136 [P2P2]  DEBUG   blockchain      src/cryptonote_core/blockchain.cpp:4949 block_batches: 0
2021-09-17 17:48:26.136 [P2P2]  TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:2915 BlockchainLMDB::top_block_hash
2021-09-17 17:48:26.136 [P2P2]  TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:2945 BlockchainLMDB::height
2021-09-17 17:48:26.136 [P2P2]  TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:2864 BlockchainLMDB::get_block_hash_from_height
2021-09-17 17:48:26.137 [P2P2]  TRACE   blockchain      src/cryptonote_core/blockchain.cpp:2767 Blockchain::have_block_unlocked
2021-09-17 17:48:26.137 [P2P2]  TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:2404 BlockchainLMDB::block_exists
2021-09-17 17:48:26.138 [P2P2]  TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:2415 Block with hash dbb615d9bc9918d906ec68445ec93b73bc6d3107f3c1bad71ef53afca2bed4e8 not found in db
2021-09-17 17:48:26.138 [P2P2]  TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:4430 BlockchainLMDB:: get_alt_block
2021-09-17 17:48:26.139 [P2P2]  TRACE   blockchain      src/cryptonote_core/blockchain.cpp:2767 Blockchain::have_block_unlocked
2021-09-17 17:48:26.139 [P2P2]  TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:2404 BlockchainLMDB::block_exists
2021-09-17 17:48:26.140 [P2P2]  TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:2415 Block with hash db0c6cbf2b5d7641aeb91192775efe2ef13155eb8b5de408bbfb0b5fa0b57e00 not found in db
2021-09-17 17:48:26.140 [P2P2]  TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:4430 BlockchainLMDB:: get_alt_block
2021-09-17 17:48:26.141 [P2P2]  TRACE   blockchain      src/cryptonote_core/blockchain.cpp:2767 Blockchain::have_block_unlocked
2021-09-17 17:48:26.141 [P2P2]  TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:2404 BlockchainLMDB::block_exists
2021-09-17 17:48:26.141 [P2P2]  TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:2415 Block with hash 81b4f43ffadec3308c5f6f00701ed4c84b2867b7df800d5bb96687ae0893510c not found in db
2021-09-17 17:48:26.141 [P2P2]  TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:4430 BlockchainLMDB:: get_alt_block
2021-09-17 17:48:26.143     fff347afde10        TRACE   blockchain      src/cryptonote_core/blockchain.cpp:746  Blockchain::get_block_id_by_height
2021-09-17 17:48:26.143     fff347afde10        TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:2864 BlockchainLMDB::get_block_hash_from_height
2021-09-17 17:48:26.143     fff347ffee10        TRACE   blockchain      src/cryptonote_core/blockchain.cpp:746  Blockchain::get_block_id_by_height
2021-09-17 17:48:26.143     fff347ffee10        TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:2864 BlockchainLMDB::get_block_hash_from_height
2021-09-17 17:48:26.144     fff347ffee10        TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:3944 BlockchainLMDB::block_rtxn_start
```

# Discussion History
## hyc | 2021-09-17T18:08:38+00:00
Works fine on my rockpro64 with armbian.

## Dendrocalamus64 | 2021-09-19T10:18:21+00:00
Well, it's not working on Manjaro.

It dies with SIGABRT.  I rebuilt it with debug symbols.  Here's a backtrace from the core dump:
```
#0  0x0000ffffb22cd6c8 in raise () from /usr/lib/libc.so.6
#1  0x0000ffffb22ba1cc in abort () from /usr/lib/libc.so.6
#2  0x0000aaaad1ee3610 in std::__replacement_assert (__file=__file@entry=0xaaaad2656230 "/usr/include/c++/10.2.0/bits/stl_vector.h", __line=__line@entry=1045, 
    __function=__function@entry=0xaaaad26e7618 "std::vector<_Tp, _Alloc>::reference std::vector<_Tp, _Alloc>::operator[](std::vector<_Tp, _Alloc>::size_type) [with _Tp = cryptonote::bl
ock; _Alloc = std::allocator<cryptonote::block>; std::vector<_Tp"..., __condition=__condition@entry=0xaaaad2656088 "__builtin_expect(__n < this->size(), true)")
    at /usr/include/c++/10.2.0/aarch64-unknown-linux-gnu/bits/c++config.h:457
#3  0x0000aaaad2363448 in std::vector<cryptonote::block, std::allocator<cryptonote::block> >::operator[] (this=<optimized out>, __n=1)
    at /usr/include/c++/10.2.0/bits/stl_vector.h:1045
#4  std::vector<cryptonote::block, std::allocator<cryptonote::block> >::operator[] (this=0xfff3947c8ca0, this=0xfff3947c8ca0, __n=1) at /usr/include/c++/10.2.0/bits/stl_vector.h:1043
#5  cryptonote::Blockchain::prepare_handle_incoming_blocks (this=this@entry=0xaaaad4ccf220, blocks_entry=std::vector of length 1, capacity 1 = {...}, 
    blocks=std::vector of length 1, capacity 1 = {...}) at /usr/src/debug/monero/src/cryptonote_core/blockchain.cpp:5009
#6  0x0000aaaad23890e8 in cryptonote::core::prepare_handle_incoming_blocks (this=0xaaaad4ccf080, blocks_entry=std::vector of length 1, capacity 1 = {...}, 
    blocks=std::vector of length 1, capacity 1 = {...}) at /usr/src/debug/monero/src/cryptonote_core/cryptonote_core.cpp:1537
#7  0x0000aaaad231e188 in cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::try_add_next_blocks (this=this@entry=0xaaaad4ccedf0, context=...)
    at /usr/src/debug/monero/src/cryptonote_protocol/cryptonote_protocol_handler.inl:1505
etc
```

From `#7` onwards it can come from somewhere else:
```
#7  0x0000aaaac525e72c in cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::handle_notify_new_fluffy_block (this=this@entry=0xaaaad7ebfdf0, command=command@entry=2008, 
    arg=..., context=...) at /usr/src/debug/monero/src/cryptonote_protocol/cryptonote_protocol_handler.inl:778
```

I checked the last 10 core dumps. `#7` is usually `try_add_next_blocks`, sometimes `handle_notify_new_fluffy_block`, and the vector length is 1 or 2.

## mgonzalezm | 2021-09-25T18:50:15+00:00
I'm getting the same error, but running on Linux x86_64 same version Monero 'Oxygen Orion' (v0.17.2.3-release)

`/usr/include/c++/11.2.0/bits/stl_vector.h:1045: std::vector<_Tp, _Alloc>::reference std::vector<_Tp, _Alloc>::operator[](std::vector<_Tp, _Alloc>::size_type) [with _Tp = cryptonote::block; _Alloc = std::allocator<cryptonote::block>; std::vector<_Tp, _Alloc>::reference = cryptonote::block&; std::vector<_Tp, _Alloc>::size_type = long unsigned int]: Assertion '__n < this->size()' failed.
Aborted`

The failed assertion makes me think that there is an out-of-bound indexed access to a vector.




## selsta | 2021-09-25T19:03:34+00:00
@Dendrocalamus64 @mgonzalezm Can you apply this patch and get a backtrace again?

```patch
 CMakeLists.txt | 2 ++
 1 file changed, 2 insertions(+)

diff --git a/CMakeLists.txt b/CMakeLists.txt
index bb019e178..fb371764b 100644
--- a/CMakeLists.txt
+++ b/CMakeLists.txt
@@ -995,12 +995,14 @@ else()
     set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fvisibility=default -DGTEST_HAS_TR1_TUPLE=0")
   endif()
 
+  #[=[[
   set(DEBUG_FLAGS "-g3")
   if(CMAKE_C_COMPILER_ID STREQUAL "GNU" AND NOT (CMAKE_C_COMPILER_VERSION VERSION_LESS 4.8))
     set(DEBUG_FLAGS "${DEBUG_FLAGS} -Og ")
   else()
     set(DEBUG_FLAGS "${DEBUG_FLAGS} -O0 ")
   endif()
+  ]]=]
 
   # At least some CLANGs default to not enough for monero
   set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -ftemplate-depth=900")
```

## selsta | 2021-09-25T19:08:22+00:00
More reports: https://github.com/monero-project/monero/issues/7253#issuecomment-898647272 and https://github.com/monero-project/monero/issues/7253#issuecomment-898651146

## mgonzalezm | 2021-09-25T23:49:39+00:00
@selsta with the patch applied and a debug build now apparently the process is running OK 
contrary to before when it failed almost immediately ( it was a release build ).

I'll report back if it fail again

## selsta | 2021-09-26T12:04:13+00:00
#7975 should solve the issue

## Dendrocalamus64 | 2021-09-28T13:18:03+00:00
My update:
I put in a different emmc and installed armbian, specifically Debian Buster, stable, no desktop, kernel 5.10.60.
I copied over the contents of /var/lib/monero from the Manjaro install to test whether the blockchain was corrupted.
Monerod as built on armbian ran fine on armbian with the same copy of the blockchain.
Didn't try building with optimizations off because mgonzalezm had already reported it makes the error disappear, and building from scratch takes several hours.
I did apply the patch in #7975, and the daemon is no longer aborting on Manjaro.

# Action History
- Created by: Dendrocalamus64 | 2021-09-17T18:01:06+00:00
- Closed at: 2021-10-11T18:00:36+00:00
