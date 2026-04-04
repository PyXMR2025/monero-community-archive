---
title: 'make debug-test failed to build: easylogging++'
source_url: https://github.com/monero-project/monero/issues/1660
author: tdprime
assignees: []
labels: []
created_at: '2017-02-01T19:34:24+00:00'
updated_at: '2017-08-08T14:58:53+00:00'
type: issue
status: closed
closed_at: '2017-08-08T14:58:53+00:00'
---

# Original Description
I sync'd with master this morning.  On Ubuntu 16.04, make debug-test

[ 60%] Linking CXX executable hash-target-tests
../src/cryptonote_core/libcryptonote_core.so: undefined reference to `el::base::utils::s_currentHost[abi:cxx11]'
../src/cryptonote_core/libcryptonote_core.so: undefined reference to `el::base::elStorage'
../src/cryptonote_core/libcryptonote_core.so: undefined reference to `el::base::utils::s_currentUser[abi:cxx11]'
collect2: error: ld returned 1 exit status
tests/CMakeFiles/hash-target-tests.dir/build.make:109: recipe for target 'tests/hash-target-tests' failed
make[3]: *** [tests/hash-target-tests] Error 1

# Discussion History
## tdprime | 2017-02-05T13:17:59+00:00
I have a pull request that addresses this issue, 
[fix depency on libepee.a for debug-test build #1676](https://github.com/monero-project/monero/pull/1676)


## moneromooo-monero | 2017-08-08T11:00:16+00:00
The patch seems not to have been merged. Was this fixed another way, or still happening ?

## tdprime | 2017-08-08T14:58:53+00:00
Looks like the real cause of this issue was fixed with #1688.

# Action History
- Created by: tdprime | 2017-02-01T19:34:24+00:00
- Closed at: 2017-08-08T14:58:53+00:00
