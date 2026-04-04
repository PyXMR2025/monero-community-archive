---
title: build error!
source_url: https://github.com/monero-project/monero/issues/4989
author: jarven-zhang
assignees: []
labels: []
created_at: '2018-12-17T06:54:05+00:00'
updated_at: '2018-12-18T04:14:49+00:00'
type: issue
status: closed
closed_at: '2018-12-18T04:14:49+00:00'
---

# Original Description
the log is this:
```
[ 95%] Linking CXX executable unit_tests
/usr/bin/ld: /usr/lib/gcc/x86_64-linux-gnu/5/../../../../lib/libgtest.a(gtest-all.cc.o): relocation R_X86_64_32 against `.rodata' can not be used when making a shared object; recompile with -fPIC
/usr/lib/gcc/x86_64-linux-gnu/5/../../../../lib/libgtest.a: error adding symbols: Bad value
collect2: error: ld returned 1 exit status
tests/unit_tests/CMakeFiles/unit_tests.dir/build.make:1544: recipe for target 'tests/unit_tests/unit_tests' failed
make[3]: *** [tests/unit_tests/unit_tests] Error 1
make[3]: Leaving directory '/home/jarven/monero/monero/build/Linux/_HEAD_detached_at_v0.13.0.4_/release'
CMakeFiles/Makefile2:4568: recipe for target 'tests/unit_tests/CMakeFiles/unit_tests.dir/all' failed
make[2]: *** [tests/unit_tests/CMakeFiles/unit_tests.dir/all] Error 2
make[2]: Leaving directory '/home/jarven/monero/monero/build/Linux/_HEAD_detached_at_v0.13.0.4_/release'
Makefile:138: recipe for target 'all' failed
make[1]: *** [all] Error 2
make[1]: Leaving directory '/home/jarven/monero/monero/build/Linux/_HEAD_detached_at_v0.13.0.4_/release'
Makefile:85: recipe for target 'release-all' failed
make: *** [release-all] Error 2
jarven@ubuntu:~/monero/monero$ make -fPIC
make: PIC: No such file or directory
make: *** No rule to make target 'PIC'.  Stop.
```
How to deal with this problem?

# Discussion History
## dEBRUYNE-1 | 2018-12-17T07:42:07+00:00
The error is fairly self-explanatory, i.e., you have to recompile the dependency with -fPIC. 

## jarven-zhang | 2018-12-17T09:46:23+00:00
> dependency

how to recompile the dependency with -fPIC? make -fPIC ?

## danrmiller | 2018-12-17T16:28:08+00:00
Try :

CFLAGS="-fPIC" CXXFLAGS="-fPIC" make

## jarven-zhang | 2018-12-18T01:35:48+00:00
> Try :
> 
> CFLAGS="-fPIC" CXXFLAGS="-fPIC" make

I did , but it does not work. there is the  log of this command:
```
[ 78%] Linking CXX executable unit_tests
/usr/bin/ld: /usr/lib/gcc/x86_64-linux-gnu/5/../../../../lib/libgtest.a(gtest-all.cc.o): relocation R_X86_64_32 against `.rodata' can not be used when making a shared object; recompile with -fPIC
/usr/lib/gcc/x86_64-linux-gnu/5/../../../../lib/libgtest.a: error adding symbols: Bad value
collect2: error: ld returned 1 exit status
tests/unit_tests/CMakeFiles/unit_tests.dir/build.make:1544: recipe for target 'tests/unit_tests/unit_tests' failed
make[3]: *** [tests/unit_tests/unit_tests] Error 1
make[3]: Leaving directory '/home/jarven/monero/monero/build/Linux/_HEAD_detached_at_v0.13.0.4_/release'
CMakeFiles/Makefile2:4568: recipe for target 'tests/unit_tests/CMakeFiles/unit_tests.dir/all' failed
make[2]: *** [tests/unit_tests/CMakeFiles/unit_tests.dir/all] Error 2
make[2]: Leaving directory '/home/jarven/monero/monero/build/Linux/_HEAD_detached_at_v0.13.0.4_/release'
Makefile:138: recipe for target 'all' failed
make[1]: *** [all] Error 2
make[1]: Leaving directory '/home/jarven/monero/monero/build/Linux/_HEAD_detached_at_v0.13.0.4_/release'
Makefile:85: recipe for target 'release-all' failed
make: *** [release-all] Error 2

```

## danrmiller | 2018-12-18T02:24:43+00:00
Those are the flags you need for building the dependencies. For this error you can just remove your system's gtest and the one included in monero will be built and you won't have to worry about that.

## jarven-zhang | 2018-12-18T02:28:36+00:00
> Those are the flags you need for building the dependencies. For this error you can just remove your system's gtest and the one included in monero will be built and you won't have to worry about that.

ok, I see. I'll try that, thanks very much!

## jarven-zhang | 2018-12-18T04:14:49+00:00
I removed the libgtest
```
sudo apt-get remove libgtest-dev 
```
and then I compiled successfully

# Action History
- Created by: jarven-zhang | 2018-12-17T06:54:05+00:00
- Closed at: 2018-12-18T04:14:49+00:00
