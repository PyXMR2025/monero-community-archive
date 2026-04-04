---
title: blockchain_blackball.cpp does not compile with clang 5 (binding dereferenced
  null pointer to reference)
source_url: https://github.com/monero-project/monero/issues/3497
author: m2049r
assignees: []
labels: []
created_at: '2018-03-25T22:20:12+00:00'
updated_at: '2018-04-12T13:16:56+00:00'
type: issue
status: closed
closed_at: '2018-04-12T13:16:56+00:00'
---

# Original Description
Android clang version 5.0.300080 :
```C
[ 96%] Building CXX object src/blockchain_utilities/CMakeFiles/blockchain_blackball.dir/blockchain_blackball.cpp.o
/opt/android/monero/src/blockchain_utilities/blockchain_blackball.cpp:256:28: error: binding
      dereferenced null pointer to reference has undefined behavior [-Werror,-Wnull-dereference]
  tx_memory_pool m_mempool(*(Blockchain*)NULL);
                           ^~~~~~~~~~~~~~~~~~
1 error generated.
```
This compiles warning-free on gcc (Ubuntu 5.4.0-6ubuntu1~16.04.9) 5.4.0 20160609 (which is wrong).

# Discussion History
## moneromooo-monero | 2018-03-26T09:07:00+00:00
Does it work with:
```
Blockchain *blockchain = NULL;
tx_memory_pool m_mempool(*blockchain);
```


## m2049r | 2018-03-26T12:38:36+00:00
Well, that works.

But looking at the ```tx_pool.cpp``` & ```blockchain.cpp``` code, using NULL here doesn't seem right as they both rely on this being non-NULL.

## moneromooo-monero | 2018-03-26T15:01:36+00:00
Nope, magic :)

## m2049r | 2018-03-26T15:56:47+00:00
lol - that's exactly what it looks like!  :)

## moneromooo-monero | 2018-04-12T13:06:36+00:00
https://github.com/monero-project/monero/pull/3618
sorry, I'd forgot about this.

## moneromooo-monero | 2018-04-12T13:11:09+00:00
+resolved

# Action History
- Created by: m2049r | 2018-03-25T22:20:12+00:00
- Closed at: 2018-04-12T13:16:56+00:00
