---
title: building monero from master
source_url: https://github.com/monero-project/monero/issues/4292
author: normoes
assignees: []
labels: []
created_at: '2018-08-22T13:05:05+00:00'
updated_at: '2018-08-23T15:34:04+00:00'
type: issue
status: closed
closed_at: '2018-08-23T15:34:04+00:00'
---

# Original Description
When trying to build monero form master, the error shown below occurs.

`cmake version 3.7.2`

What can be the cause of this?


```
[ 93%] Building CXX object tests/unit_tests/CMakeFiles/unit_tests.dir/threadpool.cpp.o
[ 93%] Building CXX object tests/unit_tests/CMakeFiles/unit_tests.dir/hardfork.cpp.o
[ 93%] Building CXX object tests/unit_tests/CMakeFiles/unit_tests.dir/unbound.cpp.o
[ 94%] Building CXX object tests/unit_tests/CMakeFiles/unit_tests.dir/uri.cpp.o
[ 94%] Building CXX object tests/unit_tests/CMakeFiles/unit_tests.dir/varint.cpp.o
[ 94%] Building CXX object tests/unit_tests/CMakeFiles/unit_tests.dir/ringct.cpp.o
[ 95%] Building CXX object tests/unit_tests/CMakeFiles/unit_tests.dir/output_selection.cpp.o
[ 95%] Building CXX object tests/unit_tests/CMakeFiles/unit_tests.dir/vercmp.cpp.o
[ 95%] Building CXX object tests/unit_tests/CMakeFiles/unit_tests.dir/ringdb.cpp.o
/monero/tests/unit_tests/ringdb.cpp: In function 'crypto::chacha_key generate_chacha_key()':
/monero/tests/unit_tests/ringdb.cpp:50:96: error: no matching function for call to 'generate_chacha_key(std::__cxx11::string, crypto::chacha_key&)'
 generate_chacha_key(std::string((const char*)&password, sizeof(password)), chacha_key);
                                                                                      ^
In file included from /monero/tests/unit_tests/ringdb.cpp:41:0:
/monero/src/crypto/chacha.h:72:15: note: candidate: void crypto::generate_chacha_key(const void*, size_t, crypto::chacha_key&, uint64_t)
   inline void generate_chacha_key(const void *data, size_t size, chacha_key& key, uint64_t kdf_rounds) {
               ^~~~~~~~~~~~~~~~~~~
/monero/src/crypto/chacha.h:72:15: note:   candidate expects 4 arguments, 2 provided
/monero/src/crypto/chacha.h:90:15: note: candidate: void crypto::generate_chacha_key(std::__cxx11::string, crypto::chacha_key&, uint64_t)
   inline void generate_chacha_key(std::string password, chacha_key& key, uint64_t kdf_rounds) {
               ^~~~~~~~~~~~~~~~~~~
/monero/src/crypto/chacha.h:90:15: note:   candidate expects 3 arguments, 2 provided
tests/unit_tests/CMakeFiles/unit_tests.dir/build.make:1142: recipe for target 'tests/unit_tests/CMakeFiles/unit_tests.dir/ringdb.cpp.o' failed
make[3]: *** [tests/unit_tests/CMakeFiles/unit_tests.dir/ringdb.cpp.o] Error 1
make[3]: Leaving directory '/monero/build/release'
CMakeFiles/Makefile2:4417: recipe for target 'tests/unit_tests/CMakeFiles/unit_tests.dir/all' failed
make[2]: *** [tests/unit_tests/CMakeFiles/unit_tests.dir/all] Error 2
make[2]: Leaving directory '/monero/build/release'
Makefile:138: recipe for target 'all' failed
make[1]: *** [all] Error 2
make[1]: Leaving directory '/monero/build/release'
Makefile:72: recipe for target 'release-all' failed
make: *** [release-all] Error 2
```

# Discussion History
## moneromooo-monero | 2018-08-22T13:16:01+00:00
#4272

## normoes | 2018-08-22T13:19:14+00:00
Thanks, I will give it a try as soon as it is merged.

## normoes | 2018-08-23T12:58:29+00:00
After pulling today, everything works as expected. Thank you.

What makes me think: #4272 still is open.

## iDunk5400 | 2018-08-23T15:29:20+00:00
#4131

## normoes | 2018-08-23T15:34:04+00:00
Ok, that seems to explain it.

# Action History
- Created by: normoes | 2018-08-22T13:05:05+00:00
- Closed at: 2018-08-23T15:34:04+00:00
