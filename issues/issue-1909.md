---
title: 'warning: ‘coinbase’ may be used uninitialized in this function'
source_url: https://github.com/monero-project/monero/issues/1909
author: ghost
assignees: []
labels: []
created_at: '2017-03-22T12:26:46+00:00'
updated_at: '2017-03-22T21:16:58+00:00'
type: issue
status: closed
closed_at: '2017-03-22T21:16:58+00:00'
---

# Original Description
Building on 64-bit ARMv8, Ubuntu 16.04 
```
[ 49%] Building CXX object src/cryptonote_core/CMakeFiles/obj_cryptonote_core.dir/tx_pool.cpp.o
/home/nodey/monero/src/cryptonote_core/tx_pool.cpp: In member function ‘bool cryptonote::tx_memory_pool::fill_block_template(cryptonote::block&, size_t, uint64_t, size_t&, uint64_t&, uint8_t)’:
/home/nodey/monero/src/cryptonote_core/tx_pool.cpp:695:31: warning: ‘coinbase’ may be used uninitialized in this function [-Wmaybe-uninitialized]
       best_coinbase = coinbase;
```

# Discussion History
## assylias | 2017-03-22T12:33:10+00:00
Probably solved by this PR: https://github.com/monero-project/monero/pull/1905

## ghost | 2017-03-22T21:16:58+00:00
Thanks - will close

# Action History
- Created by: ghost | 2017-03-22T12:26:46+00:00
- Closed at: 2017-03-22T21:16:58+00:00
