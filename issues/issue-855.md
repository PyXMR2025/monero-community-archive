---
title: blockchain_import --verify 1 fails with `transaction too big`
source_url: https://github.com/monero-project/monero/issues/855
author: radfish
assignees: []
labels:
- arm
created_at: '2016-06-01T15:30:09+00:00'
updated_at: '2016-09-17T19:10:17+00:00'
type: issue
status: closed
closed_at: '2016-09-17T19:10:17+00:00'
---

# Original Description
v0.9.4.0-a837c9c on armv7h (built by @hyc)
./hyc-build/blockchain_import --input blockchain.raw --data-dir /usr/share/monero/bitmonero.imported.verified --database lmdb#nosync --verify 1

```
block 56090 / 1059026
2016-Jun-01 07:57:47.043201 Error attempting to retrieve an output pubkey from the dbMDB_TXN_FULL: Transaction has too many dirty pages - transaction too big
2016-Jun-01 07:57:47.131817 Output does not exist! amount = 100000000
2016-Jun-01 07:57:47.619652 Error attempting to retrieve an output pubkey from the dbMDB_TXN_FULL: Transaction has too many dirty pages - transaction too big
2016-Jun-01 07:57:47.619869 Output does not exist! amount = 100000000
2016-Jun-01 07:57:47.939636 Error attempting to retrieve an output pubkey from the dbMDB_TXN_FULL: Transaction has too many dirty pages - transaction too big
2016-Jun-01 07:57:47.939869 Output does not exist! amount = 100000000
2016-Jun-01 07:57:48.257176 Failed to add block to blockchain, verification failed, height = 56097
2016-Jun-01 07:57:48.257377 skipping rest of file
2016-Jun-01 07:57:48.384142 Number of blocks imported: 56095
2016-Jun-01 07:57:48.384352 Finished at block: 56096  total blocks: 56097
```

Workarounds for this are (A) --verify 0, or (B) decrease batch size

A similar error happened on auto-migration (blockchain conversion after upgrading bitmonerod) again on armv7h.

UPDATE: identical error happened on armv7 during sync from networked (from scratch) on block #954508.


# Discussion History
## radfish | 2016-06-23T20:29:30+00:00
FYI, with `MDB_IDL_LOGN 16` and even `--batch 10`  still same problem on armv7h:

```
block 166160 / 10590262016-Jun-23 18:06:18.712655 Error attempting to retrieve an output pubkey from the dbMDB_TXN_FULL: Transaction has too many dirty pages - transaction too big
2016-Jun-23 18:06:18.730508 Exception: cryptonote::DB_ERROR
2016-Jun-23 18:06:18.730685 Unwinded call stack:
2016-Jun-23 18:06:18.751036      1                  0xf5874 __cxa_throw + 0x84
2016-Jun-23 18:06:18.754987      2                  0x12e108 void (anonymous namespace)::throw0<cryptonote::DB_ERROR>(cryptonote::DB_ERROR const&) [clone .constprop.349] + 0xd8
2016-Jun-23 18:06:18.756010      3                  0x1136dc cryptonote::BlockchainLMDB::get_output_key(unsigned long long const&, std::vector<unsigned long long, std::allocator<unsigned long long> > const&, std::vector<cryptonote::output_data_t, std::allocator<cryptonote::output_data_t> >&) + 0x464
2016-Jun-23 18:06:18.756996      4                  0xa1e14 cryptonote::Blockchain::check_tx_input(cryptonote::txin_to_key const&, crypto::hash const&, std::vector<crypto::signature, std::allocator<crypto::signature> > const&, std::vector<crypto::public_key, std::allocator<crypto::public_key> >&, unsigned long long*) + 0x4d0
2016-Jun-23 18:06:18.757967      5                  0xa496c cryptonote::Blockchain::check_tx_inputs(cryptonote::transaction const&, cryptonote::tx_verification_context&, unsigned long long*) + 0x6c0
2016-Jun-23 18:06:18.758933      6                  0xa6bf4 cryptonote::Blockchain::check_tx_inputs(cryptonote::transaction const&, unsigned long long&, crypto::hash&, cryptonote::tx_verification_context&, bool) + 0x200
2016-Jun-23 18:06:18.759864      7                  0x14041c cryptonote::tx_memory_pool::add_tx(cryptonote::transaction const&, crypto::hash const&, unsigned int, cryptonote::tx_verification_context&, bool, bool, unsigned char) + 0x574
2016-Jun-23 18:06:18.760832      8                  0x14162c cryptonote::tx_memory_pool::add_tx(cryptonote::transaction const&, cryptonote::tx_verification_context&, bool, bool, unsigned char) + 0x7c
2016-Jun-23 18:06:18.764842      9                  0x6a0a4 int import_from_file<fake_core_db>(fake_core_db&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, unsigned long long) + 0x127c
2016-Jun-23 18:06:18.766557     10                  0x51cf8 main + 0x3038
2016-Jun-23 18:06:18.815714     11                  0xb6db2cbc __libc_start_main + 0x114
2016-Jun-23 18:06:18.817084     12                  0x5a750 _start + 0x2c
2016-Jun-23 18:06:18.822322 Output does not exist! amount = 8000000000
2016-Jun-23 18:06:18.825674 DB error attempting to fetch block index from hashMDB_TXN_FULL: Transaction has too many dirty pages - transaction too big
2016-Jun-23 18:06:18.825779 Exception: cryptonote::DB_ERROR
2016-Jun-23 18:06:18.825856 Unwinded call stack:
2016-Jun-23 18:06:18.826972      1                  0xf5874 __cxa_throw + 0x84
2016-Jun-23 18:06:18.828074      2                  0x12e108 void (anonymous namespace)::throw0<cryptonote::DB_ERROR>(cryptonote::DB_ERROR const&) [clone .constprop.349] + 0xd8
2016-Jun-23 18:06:18.829051      3                  0x104398 cryptonote::BlockchainLMDB::block_exists(crypto::hash const&) const + 0x370
2016-Jun-23 18:06:18.830007      4                  0xa072c cryptonote::Blockchain::have_block(crypto::hash const&) const + 0x114
2016-Jun-23 18:06:18.830998      5                  0x96598 cryptonote::Blockchain::add_new_block(cryptonote::block const&, cryptonote::block_verification_context&) + 0x170
2016-Jun-23 18:06:18.832142      6                  0x697a8 int import_from_file<fake_core_db>(fake_core_db&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, unsigned long long) + 0x980
2016-Jun-23 18:06:18.833084      7                  0x51cf8 main + 0x3038
2016-Jun-23 18:06:18.875850      8                  0xb6db2cbc __libc_start_main + 0x114
2016-Jun-23 18:06:18.876884      9                  0x5a750 _start + 0x2c
2016-Jun-23 18:06:18.877442 exception while reading from file, height=166161: DB error attempting to fetch block index from hashMDB_TXN_FULL: Transaction has too many dirty pages - transaction too big
2016-Jun-23 18:06:18.881343 Closing IO Service.
```


## hyc | 2016-06-24T10:57:24+00:00
Sorry, I can now confirm that there is still a TXN_FULL error happening on 32bit import even with PR#857 in place.


## radfish | 2016-09-17T18:40:52+00:00
@hyc I can confirm that with f5c7905 the whole blockchain imported successfully on armv7:

```
bitmonero-import --data-dir /usr/share/monero/bitmonero.import.855/ --verify 1 --resume 1 --input-file /usr/share/monero/blockchain.raw
```

Please PR that patch if it's not yet merged. Thanks for fixing this!


## hyc | 2016-09-17T18:53:35+00:00
All the referenced patches have been PR'd and merged already.


# Action History
- Created by: radfish | 2016-06-01T15:30:09+00:00
- Closed at: 2016-09-17T19:10:17+00:00
