---
title: '[Bug] `core_tests` failed on linux'
source_url: https://github.com/monero-project/monero/issues/9105
author: qnfm
assignees:
- '0xFFFC0000'
labels:
- bug
- tests
- reproduction needed
- more info needed
created_at: '2023-12-25T22:02:41+00:00'
updated_at: '2024-02-13T17:19:02+00:00'
type: issue
status: closed
closed_at: '2024-02-13T17:19:02+00:00'
---

# Original Description
I have built the project on both my own wsl(archlinux/ubuntu) and aws ec2. But the core_tests keeps failing and throw `Segmentation fault (core dumped)`

Branch:
- master
- release-v0.18


EC2-env:
- platform: aws ec2
- OS: linux debian
- arch: x64
- build tool: cmake gcc

command:
```bash
sudo apt update && sudo apt install build-essential cmake pkg-config libssl-dev libzmq3-dev libunbound-dev libsodium-dev libunwind8-dev liblzma-dev libreadline6-dev libexpat1-dev libpgm-dev qttools5-dev-tools libhidapi-dev libusb-1.0-0-dev libprotobuf-dev protobuf-compiler libudev-dev libboost-chrono-dev libboost-date-time-dev libboost-filesystem-dev libboost-locale-dev libboost-program-options-dev libboost-regex-dev libboost-serialization-dev libboost-system-dev libboost-thread-dev python3 ccache doxygen graphviz
git clone --recursive https://github.com/monero-project/monero
cd monero
cmake -GNinja -S. -Bbuild -DBUILD_TESTS=ON && cmake --build build
cd build/tests/core_tests
./core_tests
```


# Discussion History
## 0xFFFC0000 | 2023-12-25T22:06:34+00:00
Can you enable the log and put here the detailed output? I believe something like this would do it for you after building:

```
$ctest -R core_tests --debug
```



## qnfm | 2023-12-25T23:06:03+00:00
> Can you enable the log and put here the detailed output? I believe something like this would do it for you after building:
> 
> ```
> $ctest -R core_tests --debug
> ```


/home/username/sda/lsf/cmake-3.21.2/Source/cmCTest.cxx:420 Here: 420

/home/username/sda/lsf/cmake-3.21.2/Source/cmCTest.cxx:706 UpdateCTestConfiguration  from :/home/username/dev/monero/build/tests/core_tests/DartConfiguration.tcl

/home/username/sda/lsf/cmake-3.21.2/Source/cmCTest.cxx:432 Here: 432

/home/username/sda/lsf/cmake-3.21.2/Source/cmCTest.cxx:3001 * Read custom CTest configuration directory: /home/username/dev/monero/build/tests/core_tests

/home/username/sda/lsf/cmake-3.21.2/Source/cmCTest.cxx:3004 * Check for file: /home/username/dev/monero/build/tests/core_tests/CTestCustom.cmake

/home/username/sda/lsf/cmake-3.21.2/Source/cmCTest.cxx:3024 * Check for file: /home/username/dev/monero/build/tests/core_tests/CTestCustom.ctest

/home/username/sda/lsf/cmake-3.21.2/Source/cmCTest.cxx:706 UpdateCTestConfiguration  from :/home/username/dev/monero/build/tests/core_tests/DartConfiguration.tcl

/home/username/sda/lsf/cmake-3.21.2/Source/CTest/cmCTestTestHandler.cxx:401 Test project /home/username/dev/monero/build/tests/core_tests

/home/username/sda/lsf/cmake-3.21.2/Source/CTest/cmCTestTestHandler.cxx:1761 Constructing a list of tests

/home/username/sda/lsf/cmake-3.21.2/Source/CTest/cmCTestTestHandler.cxx:2424 Add test: core_tests

/home/username/sda/lsf/cmake-3.21.2/Source/CTest/cmCTestTestHandler.cxx:2468 Set test directory: /home/username/dev/monero/build/tests/core_tests

/home/username/sda/lsf/cmake-3.21.2/Source/CTest/cmCTestTestHandler.cxx:1813 Done constructing a list of tests

/home/username/sda/lsf/cmake-3.21.2/Source/CTest/cmCTestTestHandler.cxx:957 Updating test list for fixtures

/home/username/sda/lsf/cmake-3.21.2/Source/CTest/cmCTestTestHandler.cxx:1182 Added 0 tests to meet fixture requirements

/home/username/sda/lsf/cmake-3.21.2/Source/cmCTest.cxx:306    Current_Time: Dec 26 07:04 CST

/home/username/sda/lsf/cmake-3.21.2/Source/cmCTest.cxx:306    Current_Time: Dec 26 07:04 CST

/home/username/sda/lsf/cmake-3.21.2/Source/CTest/cmCTestMultiProcessHandler.cxx:1411 Checking test dependency graph...

/home/username/sda/lsf/cmake-3.21.2/Source/CTest/cmCTestMultiProcessHandler.cxx:1440 Checking test dependency graph end

/home/username/sda/lsf/cmake-3.21.2/Source/CTest/cmCTestMultiProcessHandler.cxx:168 test 1

/home/username/sda/lsf/cmake-3.21.2/Source/CTest/cmCTestRunTest.cxx:503     Start 1: core_tests

/home/username/sda/lsf/cmake-3.21.2/Source/CTest/cmCTestRunTest.cxx:670 
1: Test command: /home/username/dev/monero/build/tests/core_tests/core_tests "--generate_and_play_test_data"

/home/username/sda/lsf/cmake-3.21.2/Source/cmCTest.cxx:306    Current_Time: Dec 26 07:04 CST

/home/username/sda/lsf/cmake-3.21.2/Source/CTest/cmCTestRunTest.cxx:736 1: Test timeout computed to be: 10000000

/home/username/sda/lsf/cmake-3.21.2/Source/CTest/cmCTestRunTest.cxx:888 1/1 Test #1: core_tests .......................
/home/username/sda/lsf/cmake-3.21.2/Source/CTest/cmCTestRunTest.cxx:892 Testing core_tests ... 
/home/username/sda/lsf/cmake-3.21.2/Source/CTest/cmCTestRunTest.cxx:237 ***Exception: SegFault  0.26 sec

/home/username/sda/lsf/cmake-3.21.2/Source/cmCTest.cxx:306    Current_Time: Dec 26 07:04 CST

/home/username/sda/lsf/cmake-3.21.2/Source/cmCTest.cxx:306    Current_Time: Dec 26 07:04 CST

/home/username/sda/lsf/cmake-3.21.2/Source/cmCTest.cxx:306    Current_Time: Dec 26 07:04 CST

/home/username/sda/lsf/cmake-3.21.2/Source/CTest/cmCTestTestHandler.cxx:605 
0% tests passed, 1 tests failed out of 1

/home/username/sda/lsf/cmake-3.21.2/Source/CTest/cmCTestTestHandler.cxx:617 
Total Test time (real) =   0.26 sec

/home/username/sda/lsf/cmake-3.21.2/Source/CTest/cmCTestTestHandler.cxx:656 
The following tests FAILED:

/home/username/sda/lsf/cmake-3.21.2/Source/CTest/cmCTestTestHandler.cxx:674 	  1 - core_tests (SEGFAULT)

/home/username/sda/lsf/cmake-3.21.2/Source/cmCTest.cxx:2907 Running a test(s) failed returning : 8


## selsta | 2023-12-25T23:33:30+00:00
Can you start core_tests in gdb and share a backtrace?

## 0xFFFC0000 | 2023-12-26T08:37:49+00:00
Two other things I am suspicious of. 

1. Running `core_tests` without any initialization, I believe does not work. For example, if I run `./core_tests` it does print: 
```
$ >> ./core_tests 
2023-12-26 08:35:04.770	E Wrong arguments
```

3. When you run `ctest -R core_tests --debug` it should dump much more dump than only CMake. I f the `core_tests` runs. This means for some reason it gets SIGSEGV at the very beginning. 

## qnfm | 2023-12-26T12:46:43+00:00
Before I check with gdb, I changed the build option `CMAKE_BUILD_TYPE` to Debug, it gave me the expected test output.
```bash
cmake -GNinja -S. -Bbuild -DCMAKE_BUILD_TYPE=Debug -DBUILD_TESTS=ON && cmake --build build
```
The `core_tests --generate_and_play_test_data` finally produce the right output.

Without the flag, the backtrace is 
```
Reading symbols from ./core_tests...done.
(gdb) run
Starting program: /home/hfutzny/Music/monero/build/tests/core_tests/core_tests --generate_and_play_test_data
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".

Program received signal SIGSEGV, Segmentation fault.
0x00005555556899fa in main ()
(gdb) backtrace
#0  0x00005555556899fa in main ()
(gdb) 

```

## qnfm | 2023-12-26T13:00:02+00:00
How about change this [part](https://github.com/monero-project/monero/blob/ac02af92867590ca80b2779a7bbeafa99ff94dcb/src/CMakeLists.txt#L117C2-L119)
```cmake
if(BUILD_DEBUG_UTILITIES)
  add_subdirectory(debug_utilities)
endif()
```
into 

```cmake
if(BUILD_DEBUG_UTILITIES OR BUILD_TESTS)
  add_subdirectory(debug_utilities)
endif()
```

## 0xFFFC0000 | 2023-12-28T20:15:23+00:00
This doesn't look like correct to me. Can you use `list` command in gdb to show which line exactly the SIGSEGV happens?

## qnfm | 2023-12-31T10:38:42+00:00
> This doesn't look like correct to me. Can you use `list` command in gdb to show which line exactly the SIGSEGV happens?

Here is the output:
```
hfutzny@hfutzny-SYS-4029GP-TRT2:/tmp/monero$ gdb --args build/tests/core_tests/core_tests --generate_and_play_test_data
Reading symbols from build/tests/core_tests/core_tests...done.
(gdb) run
Starting program: /tmp/monero/build/tests/core_tests/core_tests --generate_and_play_test_data
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".

Program received signal SIGSEGV, Segmentation fault.
0x000055555566e8ea in main ()
(gdb) list
1	<built-in>: No such file or directory.
(gdb) backtrace 
#0  0x000055555566e8ea in main ()
(gdb) 
```

## 0xFFFC0000 | 2024-01-04T06:22:24+00:00
It still doesn't make sense to me. Looks like a linking/library issue for some reason. I will take  a look at this.

## ghost | 2024-01-14T02:50:03+00:00
(cfdm^+1/2e+lt1)* = dtt^2 +1/2-4/3.15.dmb
GPI + K3.105^n = R^2*.rsc
dt= 2/3 -icsg8 . pi^2*.int
gu=dd1t1cs^2d2-DT9t'*.lk
Ka = rc^muv^sh2-pu^2/Eccp^8''*.zip
W1^3/2 + d1t1 . w^3/2 = $LUNC + target 300dsh ($0.023)
RB + MAF = Eo - d1t1 . wrs^2|/^o,313 

## 0xFFFC0000 | 2024-02-13T12:44:04+00:00
Once you had a chance, please run:
```
ldd tests/core_tests/core_tests
```
in your build folder and put the output here. 

## qnfm | 2024-02-13T16:46:22+00:00
It seems the latest commit(059028a) worked.
Here is the output of ldd command:
```
        linux-vdso.so.1 (0x00007ffe2bdd6000)
        libboost_program_options.so.1.74.0 => /lib/x86_64-linux-gnu/libboost_program_options.so.1.74.0 (0x00007fee5a35f000)
        libhidapi-libusb.so.0 => /lib/x86_64-linux-gnu/libhidapi-libusb.so.0 (0x00007fee5a354000)
        libboost_serialization.so.1.74.0 => /lib/x86_64-linux-gnu/libboost_serialization.so.1.74.0 (0x00007fee5a312000)
        libunbound.so.8 => /lib/x86_64-linux-gnu/libunbound.so.8 (0x00007fee5a22d000)
        libboost_filesystem.so.1.74.0 => /lib/x86_64-linux-gnu/libboost_filesystem.so.1.74.0 (0x00007fee5a20d000)
        libboost_thread.so.1.74.0 => /lib/x86_64-linux-gnu/libboost_thread.so.1.74.0 (0x00007fee5a1e9000)
        libboost_chrono.so.1.74.0 => /lib/x86_64-linux-gnu/libboost_chrono.so.1.74.0 (0x00007fee5a1de000)
        libboost_regex.so.1.74.0 => /lib/x86_64-linux-gnu/libboost_regex.so.1.74.0 (0x00007fee5a0eb000)
        libssl.so.3 => /lib/x86_64-linux-gnu/libssl.so.3 (0x00007fee5a047000)
        libcrypto.so.3 => /lib/x86_64-linux-gnu/libcrypto.so.3 (0x00007fee59c04000)
        libsodium.so.23 => /lib/x86_64-linux-gnu/libsodium.so.23 (0x00007fee59bac000)
        libprotobuf.so.23 => /lib/x86_64-linux-gnu/libprotobuf.so.23 (0x00007fee598e7000)
        libusb-1.0.so.0 => /lib/x86_64-linux-gnu/libusb-1.0.so.0 (0x00007fee598c9000)
        libstdc++.so.6 => /lib/x86_64-linux-gnu/libstdc++.so.6 (0x00007fee5969d000)
        libm.so.6 => /lib/x86_64-linux-gnu/libm.so.6 (0x00007fee595b6000)
        libgcc_s.so.1 => /lib/x86_64-linux-gnu/libgcc_s.so.1 (0x00007fee59596000)
        libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007fee5936d000)
        /lib64/ld-linux-x86-64.so.2 (0x00007fee5b555000)
        libevent-2.1.so.7 => /lib/x86_64-linux-gnu/libevent-2.1.so.7 (0x00007fee59317000)
        libhogweed.so.6 => /lib/x86_64-linux-gnu/libhogweed.so.6 (0x00007fee592cf000)
        libnettle.so.8 => /lib/x86_64-linux-gnu/libnettle.so.8 (0x00007fee59289000)
        libgmp.so.10 => /lib/x86_64-linux-gnu/libgmp.so.10 (0x00007fee59207000)
        libicui18n.so.70 => /lib/x86_64-linux-gnu/libicui18n.so.70 (0x00007fee58ed8000)
        libicuuc.so.70 => /lib/x86_64-linux-gnu/libicuuc.so.70 (0x00007fee58cdd000)
        libz.so.1 => /lib/x86_64-linux-gnu/libz.so.1 (0x00007fee58cbf000)
        libudev.so.1 => /lib/x86_64-linux-gnu/libudev.so.1 (0x00007fee58c95000)
        libicudata.so.70 => /lib/x86_64-linux-gnu/libicudata.so.70 (0x00007fee57077000)
```

## 0xFFFC0000 | 2024-02-13T17:18:46+00:00
I am closing this issue as you confirmed the issue is not present anymore. 

# Action History
- Created by: qnfm | 2023-12-25T22:02:41+00:00
- Closed at: 2024-02-13T17:19:02+00:00
