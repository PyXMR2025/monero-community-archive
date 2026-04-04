---
title: Compiling monero v0.12 Ubuntu 16.04 gtest Error
source_url: https://github.com/monero-project/monero/issues/3506
author: blockchainbuzz
assignees: []
labels:
- invalid
created_at: '2018-03-27T19:20:18+00:00'
updated_at: '2018-06-12T05:57:33+00:00'
type: issue
status: closed
closed_at: '2018-03-27T23:32:45+00:00'
---

# Original Description
I am new with with gtest. I had the following error. What does the error means? Any idea idea how to solve it?

[ 84%] Linking CXX executable unit_tests
/usr/bin/ld: /usr/lib/gcc/x86_64-linux-gnu/5/../../../../lib/libgtest.a(gtest-all.cc.o): relocation R_X86_64_32 against `.rodata' can not be used when making a shared object; recompile with -fPIC
/usr/lib/gcc/x86_64-linux-gnu/5/../../../../lib/libgtest.a: error adding symbols: Bad value
collect2: error: ld returned 1 exit status
tests/unit_tests/CMakeFiles/unit_tests.dir/build.make:1205: recipe for target 'tests/unit_tests/unit_tests' failed
make[3]: *** [tests/unit_tests/unit_tests] Error 1


# Discussion History
## moneromooo-monero | 2018-03-27T20:07:10+00:00
As the error says: you need a libgtest compiled with -fPIC. Uninstalling your own will cause the embedded one to be used, and that one does.

## blockchainbuzz | 2018-03-27T22:20:09+00:00
thanks problem is solved by compiled libgtest with -fPIC. 
add following lines in libgtest cmake file:
```
`set(CMAKE_C_FLAGS` "${CMAKE_C_FLAGS} -fPIC")
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS}-fPIC")``
```

## moneromooo-monero | 2018-03-27T23:24:55+00:00
+invalid

## bymagnum | 2018-06-03T00:39:30+00:00
help!

where did you insert these lines? I can't compile properly

## T37RA | 2018-06-12T05:14:25+00:00
For Ubuntu(Debian?)

apt-get install libgtest-dev
cd /usr/src/gtest
vim CMakeCache.txt
Change **`CMAKE_CXX_FLAGS:STRING=`** to **`CMAKE_CXX_FLAGS:STRING=-fPIC`**
Change **`CMAKE_C_FLAGS:STRING=`** to **`CMAKE_C_FLAGS:STRING=-fPIC`**
write and quit
cmake .
make
mv libg* /usr/lib/

That should clear the error and allow you to compile monero


## bymagnum | 2018-06-12T05:57:33+00:00
Thanks a lot!
It Worked!

# Action History
- Created by: blockchainbuzz | 2018-03-27T19:20:18+00:00
- Closed at: 2018-03-27T23:32:45+00:00
