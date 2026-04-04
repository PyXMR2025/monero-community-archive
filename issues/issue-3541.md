---
title: Compile errors and exit on Ubuntu 16.04
source_url: https://github.com/monero-project/monero/issues/3541
author: 78bash
assignees: []
labels: []
created_at: '2018-04-03T07:35:43+00:00'
updated_at: '2019-11-19T02:52:01+00:00'
type: issue
status: closed
closed_at: '2018-04-05T07:18:41+00:00'
---

# Original Description
Running make on Ubuntu 16.04 eventually returns:

Building CXX object contrib/epee/src/CMakeFiles/epee.dir/connection_basic.cpp.o
c++: internal compiler error: Killed (program cc1plus)
Please submit a full bug report,
with preprocessed source if appropriate.
See <file:///usr/share/doc/gcc-5/README.Bugs> for instructions.
src/rpc/CMakeFiles/obj_rpc.dir/build.make:62: recipe for target 'src/rpc/CMakeFiles/obj_rpc.dir/core_rpc_server.cpp.o' failed
make[3]: *** [src/rpc/CMakeFiles/obj_rpc.dir/core_rpc_server.cpp.o] Error 4
make[3]: Leaving directory '/usr/local/src/monero/build/release'
CMakeFiles/Makefile2:1617: recipe for target 'src/rpc/CMakeFiles/obj_rpc.dir/all' failed
make[2]: *** [src/rpc/CMakeFiles/obj_rpc.dir/all] Error 2
make[2]: *** Waiting for unfinished jobs....
[ 31%] Building CXX object contrib/epee/src/CMakeFiles/epee.dir/network_throttle-detail.cpp.o
[ 31%] Linking CXX static library libepee.a
make[3]: Leaving directory '/usr/local/src/monero/build/release'
[ 33%] Built target epee
make[3]: Leaving directory '/usr/local/src/monero/build/release'
[ 34%] Built target obj_wallet
make[2]: Leaving directory '/usr/local/src/monero/build/release'
Makefile:138: recipe for target 'all' failed
make[1]: *** [all] Error 2
make[1]: Leaving directory '/usr/local/src/monero/build/release'
Makefile:64: recipe for target 'release-all' failed
make: *** [release-all] Error 2
root@minemonero:/usr/local/src/monero# Entering directory '/usr/local/src/monero/build/release'
Entering: command not found

I performed a `git clean -f` and tried again, eventually coming across:
[ 67%] Linking CXX executable net_load_tests_clt
/usr/bin/ld: /usr/lib/gcc/x86_64-linux-gnu/5/../../../../lib/libgtest.a(gtest-all.cc.o): relocation R_X86_64_32 against `.rodata' can not be used when making a shared object; recompile with -fPIC
/usr/lib/gcc/x86_64-linux-gnu/5/../../../../lib/libgtest.a: error adding symbols: Bad value
collect2: error: ld returned 1 exit status
tests/net_load_tests/CMakeFiles/net_load_tests_clt.dir/build.make:129: recipe for target 'tests/net_load_tests/net_load_tests_clt' failed
make[3]: *** [tests/net_load_tests/net_load_tests_clt] Error 1
make[3]: Leaving directory '/usr/local/src/monero/build/release'
CMakeFiles/Makefile2:4473: recipe for target 'tests/net_load_tests/CMakeFiles/net_load_tests_clt.dir/all' failed
make[2]: *** [tests/net_load_tests/CMakeFiles/net_load_tests_clt.dir/all] Error 2
make[2]: *** Waiting for unfinished jobs....
[ 67%] Building CXX object tests/core_tests/CMakeFiles/core_tests.dir/ring_signature_1.cpp.o
[ 68%] Building CXX object tests/core_tests/CMakeFiles/core_tests.dir/transaction_tests.cpp.o
[ 68%] Building CXX object tests/core_tests/CMakeFiles/core_tests.dir/tx_validation.cpp.o
[ 68%] Linking CXX executable net_load_tests_srv
make[3]: Leaving directory '/usr/local/src/monero/build/release'
[ 68%] Built target net_load_tests_srv
[ 68%] Building CXX object tests/core_tests/CMakeFiles/core_tests.dir/v2_tests.cpp.o
[ 69%] Building CXX object tests/core_tests/CMakeFiles/core_tests.dir/rct.cpp.o
[ 69%] Linking CXX executable core_tests
make[3]: Leaving directory '/usr/local/src/monero/build/release'
[ 69%] Built target core_tests
make[2]: Leaving directory '/usr/local/src/monero/build/release'
Makefile:138: recipe for target 'all' failed
make[1]: *** [all] Error 2
make[1]: Leaving directory '/usr/local/src/monero/build/release'
Makefile:64: recipe for target 'release-all' failed
make: *** [release-all] Error 2

Help!

# Discussion History
## moneromooo-monero | 2018-04-03T10:39:27+00:00
 /usr/bin/ld: /usr/lib/gcc/x86_64-linux-gnu/5/../../../../lib/libgtest.a(gtest-all.cc.o): relocation R_X86_64_32 against `.rodata' can not be used when making a shared object; recompile with -fPIC

This tells you what you need to do. You can also uninstall libgtest-dev, and monero can use its internal copy, which builds with -fPIC.

## arcoso | 2018-04-04T00:59:32+00:00
Yeah I get all kinds of errors asking to recompile different files with -fPIC too.  
This really should be fixed or made into a script to compile all dependencies correctly for building.  - Could it be included in the makefile somehow?   
Or at least list everything we need to compile in a certain way, in the build instructions - if this is going to be the standard build environment from now on?

## moneromooo-monero | 2018-04-04T09:56:42+00:00
The README.md file lists dependencies. If any are missing, please point them out and they'll be added. To compile third party software, check their own README/INSTALL files. There will soon be a new way to build monero and deps though (see #3430).

## arcoso | 2018-04-04T16:23:20+00:00
The new way looks good!  Looking forward to it. 

## 78bash | 2018-04-05T07:18:41+00:00
I purged `libgtest-dev` from my system, ran `make CXXFLAGS=-fPIC CFLAGS=-fPIC` and everything compiled super smoothly.

Thanks @moneromooo-monero and the other champs for the help.

EDIT: Don't forget to `rm -rf build/` before recompiling.

## xiphon | 2019-11-19T02:44:07+00:00
Do you have `libboost-all-dev` installed?

# Action History
- Created by: 78bash | 2018-04-03T07:35:43+00:00
- Closed at: 2018-04-05T07:18:41+00:00
