---
title: build help for ubuntu 16.04 gtest missing -fPIC
source_url: https://github.com/monero-project/monero/issues/3688
author: kenken64
assignees: []
labels: []
created_at: '2018-04-23T11:48:18+00:00'
updated_at: '2019-11-20T21:07:08+00:00'
type: issue
status: closed
closed_at: '2018-04-23T13:24:52+00:00'
---

# Original Description
[ 80%] Linking CXX executable unit_tests
/usr/bin/ld: /usr/lib/gcc/x86_64-linux-gnu/5/../../../../lib/libgtest.a(gtest-all.cc.o): relocation R_X86_64_32 against `.rodata' can not be used when making a shared object; recompile with -fPIC
/usr/lib/gcc/x86_64-linux-gnu/5/../../../../lib/libgtest.a: error adding symbols: Bad value
collect2: error: ld returned 1 exit status
tests/unit_tests/CMakeFiles/unit_tests.dir/build.make:1205: recipe for target 'tests/unit_tests/unit_tests' failed


# Discussion History
## dEBRUYNE-1 | 2018-04-23T11:50:03+00:00
Your error message explains how to resolve this issue:

    against `.rodata' can not be used when making a shared object; recompile with -fPIC


## kenken64 | 2018-04-23T13:16:55+00:00
[ 63%] Linking CXX executable net_load_tests_clt
/usr/bin/ld: /usr/lib/gcc/x86_64-linux-gnu/5/../../../../lib/libgtest.a(gtest-all.cc.o): relocation R_X86_64_32 against `.rodata' can not be used when making a shared object; recompile with -fPIC
/usr/lib/gcc/x86_64-linux-gnu/5/../../../../lib/libgtest.a: error adding symbols: Bad value
collect2: error: ld returned 1 exit status
tests/net_load_tests/CMakeFiles/net_load_tests_clt.dir/build.make:128: recipe for target 'tests/net_load_tests/net_load_tests_clt' failed
make[3]: *** [tests/net_load_tests/net_load_tests_clt] Error 1
make[3]: Leaving directory '/media/kenneth/b13ae9f7-5727-4bc0-94fe-77d72079f2ee/monero/build/release'
CMakeFiles/Makefile2:4625: recipe for target 'tests/net_load_tests/CMakeFiles/net_load_tests_clt.dir/all' failed
make[2]: *** [tests/net_load_tests/CMakeFiles/net_load_tests_clt.dir/all] Error 2
make[2]: *** Waiting for unfinished jobs....
make[3]: Leaving directory '/media/kenneth/b13ae9f7-5727-4bc0-94fe-77d72079f2ee/monero/build/release'
[ 63%] Built target wallet
make[3]: Leaving directory '/media/kenneth/b13ae9f7-5727-4bc0-94fe-77d72079f2ee/monero/build/release'


## kenken64 | 2018-04-23T13:17:22+00:00
yeah -fPIC where to pass this argument ? make -fPIC

## kenken64 | 2018-04-23T13:20:35+00:00
Reading package lists... Done
Building dependency tree       
Reading state information... Done
libgtest-dev is already the newest version (1.7.0-4ubuntu1).
0 upgraded, 0 newly installed, 0 to remove and 32 not upgraded.
-- Configuring done
-- Generating done
-- Build files have been written to: /usr/src/gtest
/usr/bin/cmake -H/usr/src/gtest -B/usr/src/gtest --check-build-system CMakeFiles/Makefile.cmake 0
/usr/bin/cmake -E cmake_progress_start /usr/src/gtest/CMakeFiles /usr/src/gtest/CMakeFiles/progress.marks
make -f CMakeFiles/Makefile2 all
make[1]: Entering directory '/usr/src/gtest'
make -f CMakeFiles/gtest.dir/build.make CMakeFiles/gtest.dir/depend
make[2]: Entering directory '/usr/src/gtest'
cd /usr/src/gtest && /usr/bin/cmake -E cmake_depends "Unix Makefiles" /usr/src/gtest /usr/src/gtest /usr/src/gtest /usr/src/gtest /usr/src/gtest/CMakeFiles/gtest.dir/DependInfo.cmake --color=
make[2]: Leaving directory '/usr/src/gtest'
make -f CMakeFiles/gtest.dir/build.make CMakeFiles/gtest.dir/build
make[2]: Entering directory '/usr/src/gtest'
[ 25%] Building CXX object CMakeFiles/gtest.dir/src/gtest-all.cc.o
/usr/bin/c++    -I/usr/src/gtest/include -I/usr/src/gtest  -fPIC   -fPIC -Wall -Wshadow -DGTEST_HAS_PTHREAD=1 -fexceptions -Wextra -Wno-unused-parameter -Wno-missing-field-initializers -o CMakeFiles/gtest.dir/src/gtest-all.cc.o -c /usr/src/gtest/src/gtest-all.cc
[ 50%] Linking CXX static library libgtest.a
/usr/bin/cmake -P CMakeFiles/gtest.dir/cmake_clean_target.cmake
/usr/bin/cmake -E cmake_link_script CMakeFiles/gtest.dir/link.txt --verbose=1
/usr/bin/ar qc libgtest.a  CMakeFiles/gtest.dir/src/gtest-all.cc.o
/usr/bin/ranlib libgtest.a
make[2]: Leaving directory '/usr/src/gtest'
[ 50%] Built target gtest
make -f CMakeFiles/gtest_main.dir/build.make CMakeFiles/gtest_main.dir/depend
make[2]: Entering directory '/usr/src/gtest'
cd /usr/src/gtest && /usr/bin/cmake -E cmake_depends "Unix Makefiles" /usr/src/gtest /usr/src/gtest /usr/src/gtest /usr/src/gtest /usr/src/gtest/CMakeFiles/gtest_main.dir/DependInfo.cmake --color=
make[2]: Leaving directory '/usr/src/gtest'
make -f CMakeFiles/gtest_main.dir/build.make CMakeFiles/gtest_main.dir/build
make[2]: Entering directory '/usr/src/gtest'
[ 75%] Building CXX object CMakeFiles/gtest_main.dir/src/gtest_main.cc.o
/usr/bin/c++    -I/usr/src/gtest/include -I/usr/src/gtest  -fPIC   -fPIC -Wall -Wshadow -DGTEST_HAS_PTHREAD=1 -fexceptions -Wextra -Wno-unused-parameter -Wno-missing-field-initializers -o CMakeFiles/gtest_main.dir/src/gtest_main.cc.o -c /usr/src/gtest/src/gtest_main.cc
[100%] Linking CXX static library libgtest_main.a
/usr/bin/cmake -P CMakeFiles/gtest_main.dir/cmake_clean_target.cmake
/usr/bin/cmake -E cmake_link_script CMakeFiles/gtest_main.dir/link.txt --verbose=1
/usr/bin/ar qc libgtest_main.a  CMakeFiles/gtest_main.dir/src/gtest_main.cc.o
/usr/bin/ranlib libgtest_main.a
make[2]: Leaving directory '/usr/src/gtest'
[100%] Built target gtest_main
make[1]: Leaving directory '/usr/src/gtest'
/usr/bin/cmake -E cmake_progress_start /usr/src/gtest/CMakeFiles 0


## kenken64 | 2018-04-23T13:20:53+00:00
[25%] Building CXX object CMakeFiles/gtest.dir/src/gtest-all.cc.o
/usr/bin/c++ -I/usr/src/gtest/include -I/usr/src/gtest -fPIC -fPIC -Wall -Wshadow -DGTEST_HAS_PTHREAD=1 -fexceptions -Wextra -Wno-unused-parameter -Wno-missing-field-initializers -o CMakeFiles/gtest.dir/src/gtest-all.cc.o -c /usr/src/gtest/src/gtest-all.cc

## kenken64 | 2018-04-23T13:24:52+00:00
//Flags used by the compiler during all build types.
CMAKE_CXX_FLAGS:STRING=-fPIC


## aventadorm | 2019-11-20T21:07:08+00:00
Was this an issue with googletest being compiled without -fPIC ?

# Action History
- Created by: kenken64 | 2018-04-23T11:48:18+00:00
- Closed at: 2018-04-23T13:24:52+00:00
