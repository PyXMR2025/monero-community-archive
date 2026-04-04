---
title: Problem with Install
source_url: https://github.com/monero-project/monero/issues/3586
author: CoFix
assignees: []
labels:
- invalid
created_at: '2018-04-09T06:05:49+00:00'
updated_at: '2018-06-20T09:17:06+00:00'
type: issue
status: closed
closed_at: '2018-06-20T09:17:06+00:00'
---

# Original Description
I am using ubuntu16.04. And i installed this depen..

sudo apt-get install build-essential cmake pkg-config libboost-all-dev libssl-dev libzmq3-dev libunbound-dev libsodium-dev libminiupnpc-dev libunwind8-dev liblzma-dev libreadline6-dev libldns-dev libexpat1-dev libgtest-dev doxygen graphviz

I am getting this error

[ 75%] Linking CXX executable net_load_tests_clt
/usr/bin/ld: /usr/lib/gcc/x86_64-linux-gnu/5/../../../../lib/libgtest.a(gtest-all.cc.o): relocation R_X86_64_32 against `.rodata' can not be used when making a shared object; recompile with -fPIC
/usr/lib/gcc/x86_64-linux-gnu/5/../../../../lib/libgtest.a: error adding symbols: Bad value
collect2: error: ld returned 1 exit status
tests/net_load_tests/CMakeFiles/net_load_tests_clt.dir/build.make:129: recipe for target 'tests/net_load_tests/net_load_tests_clt' failed
make[3]: *** [tests/net_load_tests/net_load_tests_clt] Error 1
make[3]: Leaving directory '/home/monero/monero/build/release'
CMakeFiles/Makefile2:4547: recipe for target 'tests/net_load_tests/CMakeFiles/net_load_tests_clt.dir/all' failed
make[2]: *** [tests/net_load_tests/CMakeFiles/net_load_tests_clt.dir/all] Error 2
make[2]: *** Waiting for unfinished jobs....
[ 76%] Building CXX object tests/functional_tests/CMakeFiles/functional_tests.dir/transactions_generation_from_blockchain.cpp.o
[ 77%] Linking CXX executable performance_tests
make[3]: Leaving directory '/home/monero/monero/build/release'
[ 77%] Built target performance_tests
[ 77%] Linking CXX executable functional_tests
make[3]: Leaving directory '/home/monero/monero/build/release'
[ 77%] Built target functional_tests
[ 77%] Linking CXX executable core_proxy
make[3]: Leaving directory '/home/monero/monero/build/release'
[ 77%] Built target core_proxy
make[2]: Leaving directory '/home/monero/monero/build/release'
Makefile:138: recipe for target 'all' failed
make[1]: *** [all] Error 2
make[1]: Leaving directory '/home/monero/monero/build/release'
Makefile:64: recipe for target 'release-all' failed
make: *** [release-all] Error 2


What i make mistake?

# Discussion History
## moneromooo-monero | 2018-04-09T09:39:37+00:00
It tells you what to do: build libgtest with -fPIC. Or you can uninstall your system libgtest and monero will use its internal one.

## moneromooo-monero | 2018-06-20T08:57:43+00:00
+invalid

# Action History
- Created by: CoFix | 2018-04-09T06:05:49+00:00
- Closed at: 2018-06-20T09:17:06+00:00
