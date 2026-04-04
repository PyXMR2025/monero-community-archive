---
title: Build errors (and warnings), cannot build
source_url: https://github.com/monero-project/monero/issues/3797
author: c50a326
assignees: []
labels: []
created_at: '2018-05-12T04:14:51+00:00'
updated_at: '2018-09-09T12:24:47+00:00'
type: issue
status: closed
closed_at: '2018-09-09T12:24:47+00:00'
---

# Original Description
This is on Archlinux with GCC 8.1.0.

Just following the build instructions, with `make -j8`:
```
mkdir -p build/release
cd build/release && cmake -D BUILD_TESTS=ON -D CMAKE_BUILD_TYPE=release ../.. && make
-- The C compiler identification is GNU 8.1.0
-- The CXX compiler identification is GNU 8.1.0
-- Check for working C compiler: /usr/bin/cc
-- Check for working C compiler: /usr/bin/cc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting C compile features - done
-- Check for working CXX compiler: /usr/bin/c++
-- Check for working CXX compiler: /usr/bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Building without build tag
-- Could not find DEVELOPER_LOCAL_TOOLS in env (not required)
-- BOOST_IGNORE_SYSTEM_PATHS defaults to OFF
-- Could not find DEVELOPER_LIBUNBOUND_OLD in env (not required)
-- Building for a 64-bit system
-- Building internal libraries as static
-- Could not find DATABASE in env (not required unless you want to change database type from default: lmdb)
-- Using LMDB as default DB type
-- Stack trace on exception enabled (using easylogging++)
-- Looking for pthread.h
-- Looking for pthread.h - found
-- Looking for pthread_create
-- Looking for pthread_create - not found
-- Check if compiler accepts -pthread
-- Check if compiler accepts -pthread - yes
-- Found Threads: TRUE  
-- Found OpenSSL: /usr/lib/libcrypto.so (found version "1.1.0h") 
-- Using OpenSSL include dir at /usr/include
-- Found PkgConfig: /usr/bin/pkg-config (found version "0.29.2") 
-- Checking for module 'libpcsclite'
--   No package 'libpcsclite' found
-- Could NOT find PCSC (missing: PCSC_LIBRARY PCSC_INCLUDE_DIR) 
-- Looking for memset_s in c
-- Looking for memset_s in c - not found
-- Looking for explicit_bzero in c
-- Looking for explicit_bzero in c - found
-- Looking for strptime
-- Looking for strptime - found
-- Found MiniUPnPc: /usr/include/miniupnpc  
-- Found miniupnpc API version 17
-- Using shared miniupnpc found at /usr/include/miniupnpc
-- Looking for libunbound
-- Found libunbound include (unbound.h) in /usr/include
-- Found libunbound shared library
-- Using 64-bit LMDB from source tree
-- Building on x86_64 for native
-- Performing Test _Wformat_c
-- Performing Test _Wformat_c - Success
-- Performing Test _Wformat_cxx
-- Performing Test _Wformat_cxx - Success
-- Performing Test _Wformat_security_c
-- Performing Test _Wformat_security_c - Success
-- Performing Test _Wformat_security_cxx
-- Performing Test _Wformat_security_cxx - Success
-- Performing Test _fstack_protector_c
-- Performing Test _fstack_protector_c - Success
-- Performing Test _fstack_protector_cxx
-- Performing Test _fstack_protector_cxx - Success
-- Performing Test _fstack_protector_strong_c
-- Performing Test _fstack_protector_strong_c - Success
-- Performing Test _fstack_protector_strong_cxx
-- Performing Test _fstack_protector_strong_cxx - Success
-- Looking for -pie linker flag
-- Looking for -pie linker flag - found
-- Looking for -Wl,-z,relro linker flag
-- Looking for -Wl,-z,relro linker flag - found
-- Looking for -Wl,-z,now linker flag
-- Looking for -Wl,-z,now linker flag - found
-- Looking for -Wl,-z,noexecstack linker flag
-- Looking for -Wl,-z,noexecstack linker flag - found
-- Looking for -Wl,-z,noexecheap linker flag
-- Looking for -Wl,-z,noexecheap linker flag - not found
-- Using C security hardening flags:  -Wformat -Wformat-security -fstack-protector -fstack-protector-strong
-- Using C++ security hardening flags:  -Wformat -Wformat-security -fstack-protector -fstack-protector-strong
-- Using linker security hardening flags:  -pie -Wl,-z,relro -Wl,-z,now -Wl,-z,noexecstack
-- AES support enabled
-- Found Boost Version: 106600
-- Looking for rl_copy_text
-- Looking for rl_copy_text - found
-- Looking for rl_filename_completion_function
-- Looking for rl_filename_completion_function - found
-- Found readline library at: /usr
-- Found Git: /usr/bin/git
-- Found GTest: /usr/lib/libgtest.so  
-- Found Doxygen: /usr/bin/doxygen (found version "1.8.14") found components:  doxygen dot 
-- Performing Test HAVE_C11
-- Performing Test HAVE_C11 - Success
-- Configuring done
-- Generating done
-- Build files have been written to: /home/c50a326/github/monero/build/release
make[1]: Entering directory '/home/c50a326/github/monero/build/release'
make[2]: Entering directory '/home/c50a326/github/monero/build/release'
make[3]: Entering directory '/home/c50a326/github/monero/build/release'
make[3]: Entering directory '/home/c50a326/github/monero/build/release'
make[3]: Entering directory '/home/c50a326/github/monero/build/release'
make[3]: Entering directory '/home/c50a326/github/monero/build/release'
make[3]: Entering directory '/home/c50a326/github/monero/build/release'
make[3]: Entering directory '/home/c50a326/github/monero/build/release'
make[3]: Entering directory '/home/c50a326/github/monero/build/release'
Scanning dependencies of target generate_translations_header
make[3]: Leaving directory '/home/c50a326/github/monero/build/release'
Scanning dependencies of target genversion
make[3]: Leaving directory '/home/c50a326/github/monero/build/release'
Scanning dependencies of target easylogging
make[3]: Leaving directory '/home/c50a326/github/monero/build/release'
make[3]: Entering directory '/home/c50a326/github/monero/build/release'
make[3]: Entering directory '/home/c50a326/github/monero/build/release'
Scanning dependencies of target lmdb
make[3]: Leaving directory '/home/c50a326/github/monero/build/release'
Scanning dependencies of target obj_ringct_basic
make[3]: Leaving directory '/home/c50a326/github/monero/build/release'
make[3]: Entering directory '/home/c50a326/github/monero/build/release'
[  1%] Creating directories for 'generate_translations_header'
Scanning dependencies of target obj_cncrypto
make[3]: Leaving directory '/home/c50a326/github/monero/build/release'
make[3]: Entering directory '/home/c50a326/github/monero/build/release'
make[3]: Entering directory '/home/c50a326/github/monero/build/release'
Scanning dependencies of target obj_ringct
make[3]: Leaving directory '/home/c50a326/github/monero/build/release'
make[3]: Entering directory '/home/c50a326/github/monero/build/release'
make[3]: Entering directory '/home/c50a326/github/monero/build/release'
make[3]: Entering directory '/home/c50a326/github/monero/build/release'
[  2%] Generating ../version.cpp
[  3%] Building C object external/db_drivers/liblmdb/CMakeFiles/lmdb.dir/mdb.c.o
Scanning dependencies of target obj_device
make[3]: Leaving directory '/home/c50a326/github/monero/build/release'
[  3%] Building CXX object external/easylogging++/CMakeFiles/easylogging.dir/easylogging++.cc.o
-- You are currently on commit c29890c2
make[3]: Entering directory '/home/c50a326/github/monero/build/release'
-- The most recent tag was at c29890c2
-- You are building a tagged release
make[3]: Leaving directory '/home/c50a326/github/monero/build/release'
[  3%] Building CXX object src/ringct/CMakeFiles/obj_ringct_basic.dir/rctOps.cpp.o
[  3%] Building CXX object src/device/CMakeFiles/obj_device.dir/device.cpp.o
[  3%] Building CXX object src/ringct/CMakeFiles/obj_ringct.dir/rctSigs.cpp.o
[  3%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/aesb.c.o
[  3%] Built target genversion
[  3%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/blake256.c.o
[  3%] No download step for 'generate_translations_header'
[  4%] No patch step for 'generate_translations_header'
[  4%] No update step for 'generate_translations_header'
[  4%] Performing configure step for 'generate_translations_header'
[  5%] Building CXX object src/ringct/CMakeFiles/obj_ringct_basic.dir/rctTypes.cpp.o
-- The C compiler identification is GNU 8.1.0
[  6%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/chacha.c.o
-- The CXX compiler identification is GNU 8.1.0
[  6%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/crypto-ops-data.c.o
-- Check for working C compiler: /usr/bin/cc
[  7%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/crypto-ops.c.o
-- Check for working C compiler: /usr/bin/cc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting C compile features - done
-- Check for working CXX compiler: /usr/bin/c++
In file included from /home/c50a326/github/monero/src/device/device.hpp:48,
                 from /home/c50a326/github/monero/src/device/device.cpp:30:
/home/c50a326/github/monero/src/crypto/chacha.h: In function ‘void crypto::generate_chacha_key(const void*, size_t, crypto::chacha_key&)’:
/home/c50a326/github/monero/src/crypto/chacha.h:76:46: error: ‘void* memcpy(void*, const void*, size_t)’ writing to an object of non-trivially copyable type ‘using chacha_key = tools::scrubbed_arr<unsigned char, 32>’ {aka ‘struct tools::scrubbed<std::array<unsigned char, 32> >’}; use copy-assignment or copy-initialization instead [-Werror=class-memaccess]
     memcpy(&key, pwd_hash.data(), sizeof(key));
                                              ^
In file included from /home/c50a326/github/monero/src/crypto/crypto.h:44,
                 from /home/c50a326/github/monero/src/device/device.hpp:47,
                 from /home/c50a326/github/monero/src/device/device.cpp:30:
/home/c50a326/github/monero/contrib/epee/include/memwipe.h:53:10: note: ‘using chacha_key = tools::scrubbed_arr<unsigned char, 32>’ {aka ‘struct tools::scrubbed<std::array<unsigned char, 32> >’} declared here
   struct scrubbed : public T {
          ^~~~~~~~
In file included from /home/c50a326/github/monero/src/device/device.hpp:48,
                 from /home/c50a326/github/monero/src/device/device.cpp:30:
/home/c50a326/github/monero/src/crypto/chacha.h: In function ‘void crypto::generate_chacha_key_prehashed(const void*, size_t, crypto::chacha_key&)’:
/home/c50a326/github/monero/src/crypto/chacha.h:83:46: error: ‘void* memcpy(void*, const void*, size_t)’ writing to an object of non-trivially copyable type ‘using chacha_key = tools::scrubbed_arr<unsigned char, 32>’ {aka ‘struct tools::scrubbed<std::array<unsigned char, 32> >’}; use copy-assignment or copy-initialization instead [-Werror=class-memaccess]
     memcpy(&key, pwd_hash.data(), sizeof(key));
                                              ^
In file included from /home/c50a326/github/monero/src/crypto/crypto.h:44,
                 from /home/c50a326/github/monero/src/device/device.hpp:47,
                 from /home/c50a326/github/monero/src/device/device.cpp:30:
/home/c50a326/github/monero/contrib/epee/include/memwipe.h:53:10: note: ‘using chacha_key = tools::scrubbed_arr<unsigned char, 32>’ {aka ‘struct tools::scrubbed<std::array<unsigned char, 32> >’} declared here
   struct scrubbed : public T {
          ^~~~~~~~
-- Check for working CXX compiler: /usr/bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
[  7%] Building CXX object src/crypto/CMakeFiles/obj_cncrypto.dir/crypto.cpp.o
[  7%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/groestl.c.o
-- Detecting CXX compile features - done
lrelease version 5.10.1
-- Configuring done
-- Generating done
-- Build files have been written to: /home/c50a326/github/monero/build/release/translations
[  7%] Performing build step for 'generate_translations_header'
make[4]: Entering directory '/home/c50a326/github/monero/build/release/translations'
cc1plus: all warnings being treated as errors
make[3]: *** [src/device/CMakeFiles/obj_device.dir/build.make:63: src/device/CMakeFiles/obj_device.dir/device.cpp.o] Error 1
make[3]: Leaving directory '/home/c50a326/github/monero/build/release'
make[5]: Entering directory '/home/c50a326/github/monero/build/release/translations'
make[6]: Entering directory '/home/c50a326/github/monero/build/release/translations'
Scanning dependencies of target generate_translations_header
make[6]: Leaving directory '/home/c50a326/github/monero/build/release/translations'
make[6]: Entering directory '/home/c50a326/github/monero/build/release/translations'
[ 50%] Building C object CMakeFiles/generate_translations_header.dir/generate_translations_header.c.o
[100%] Linking C executable generate_translations_header
Updating 'monero.qm'...
    Generated 0 translation(s) (0 finished and 0 unfinished)
    Ignored 737 untranslated source text(s)
Updating 'monero_fr.qm'...
    Generated 737 translation(s) (737 finished and 0 unfinished)
Updating 'monero_it.qm'...
    Generated 380 translation(s) (376 finished and 4 unfinished)
    Ignored 357 untranslated source text(s)
Updating 'monero_sv.qm'...
    Generated 737 translation(s) (737 finished and 0 unfinished)
make[2]: *** [CMakeFiles/Makefile2:3262: src/device/CMakeFiles/obj_device.dir/all] Error 2
make[2]: *** Waiting for unfinished jobs....
make[3]: Entering directory '/home/c50a326/github/monero/build/release'
[  7%] Building C object external/db_drivers/liblmdb/CMakeFiles/lmdb.dir/midl.c.o
[  8%] Generating stagenet_blocks.o
Generating embedded translations header
[  8%] Generating blocks.o
[  8%] Generating testnet_blocks.o
make[6]: Leaving directory '/home/c50a326/github/monero/build/release/translations'
[100%] Built target generate_translations_header
make[5]: Leaving directory '/home/c50a326/github/monero/build/release/translations'
Scanning dependencies of target blocks
make[3]: Leaving directory '/home/c50a326/github/monero/build/release'
make[3]: Entering directory '/home/c50a326/github/monero/build/release'
make[4]: Leaving directory '/home/c50a326/github/monero/build/release/translations'
[  8%] Building C object src/blocks/CMakeFiles/blocks.dir/blockexports.c.o
[  8%] Performing install step for 'generate_translations_header'

In file included from /home/c50a326/github/monero/src/serialization/crypto.h:37,
                 from /home/c50a326/github/monero/src/cryptonote_basic/cryptonote_basic.h:44,
                 from /home/c50a326/github/monero/src/cryptonote_basic/cryptonote_basic_impl.h:33,
                 from /home/c50a326/github/monero/src/cryptonote_basic/cryptonote_format_utils.h:33,
                 from /home/c50a326/github/monero/src/ringct/rctSigs.cpp:37:
/home/c50a326/github/monero/src/crypto/chacha.h: In function ‘void crypto::generate_chacha_key(const void*, size_t, crypto::chacha_key&)’:
/home/c50a326/github/monero/src/crypto/chacha.h:76:46: error: ‘void* memcpy(void*, const void*, size_t)’ writing to an object of non-trivially copyable type ‘using chacha_key = tools::scrubbed_arr<unsigned char, 32>’ {aka ‘struct tools::scrubbed<std::array<unsigned char, 32> >’}; use copy-assignment or copy-initialization instead [-Werror=class-memaccess]
     memcpy(&key, pwd_hash.data(), sizeof(key));
                                              ^
In file included from /home/c50a326/github/monero/src/crypto/crypto.h:44,
                 from /home/c50a326/github/monero/src/ringct/rctSigs.h:48,
                 from /home/c50a326/github/monero/src/ringct/rctSigs.cpp:35:
/home/c50a326/github/monero/contrib/epee/include/memwipe.h:53:10: note: ‘using chacha_key = tools::scrubbed_arr<unsigned char, 32>’ {aka ‘struct tools::scrubbed<std::array<unsigned char, 32> >’} declared here
   struct scrubbed : public T {
          ^~~~~~~~
In file included from /home/c50a326/github/monero/src/serialization/crypto.h:37,
                 from /home/c50a326/github/monero/src/cryptonote_basic/cryptonote_basic.h:44,
                 from /home/c50a326/github/monero/src/cryptonote_basic/cryptonote_basic_impl.h:33,
                 from /home/c50a326/github/monero/src/cryptonote_basic/cryptonote_format_utils.h:33,
                 from /home/c50a326/github/monero/src/ringct/rctSigs.cpp:37:
/home/c50a326/github/monero/src/crypto/chacha.h: In function ‘void crypto::generate_chacha_key_prehashed(const void*, size_t, crypto::chacha_key&)’:
/home/c50a326/github/monero/src/crypto/chacha.h:83:46: error: ‘void* memcpy(void*, const void*, size_t)’ writing to an object of non-trivially copyable type ‘using chacha_key = tools::scrubbed_arr<unsigned char, 32>’ {aka ‘struct tools::scrubbed<std::array<unsigned char, 32> >’}; use copy-assignment or copy-initialization instead [-Werror=class-memaccess]
     memcpy(&key, pwd_hash.data(), sizeof(key));
                                              ^
In file included from /home/c50a326/github/monero/src/crypto/crypto.h:44,
                 from /home/c50a326/github/monero/src/ringct/rctSigs.h:48,
                 from /home/c50a326/github/monero/src/ringct/rctSigs.cpp:35:
/home/c50a326/github/monero/contrib/epee/include/memwipe.h:53:10: note: ‘using chacha_key = tools::scrubbed_arr<unsigned char, 32>’ {aka ‘struct tools::scrubbed<std::array<unsigned char, 32> >’} declared here
   struct scrubbed : public T {
          ^~~~~~~~
[  8%] Linking C static library libblocks.a
[  8%] Completed 'generate_translations_header'
[  8%] Building C object src/ringct/CMakeFiles/obj_ringct_basic.dir/rctCryptoOps.c.o
make[3]: Leaving directory '/home/c50a326/github/monero/build/release'
[  8%] Built target generate_translations_header
[  8%] Building CXX object src/ringct/CMakeFiles/obj_ringct_basic.dir/bulletproofs.cc.o
make[3]: Leaving directory '/home/c50a326/github/monero/build/release'
[  8%] Built target blocks
[  9%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/hash-extra-blake.c.o
[  9%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/hash-extra-groestl.c.o
[  9%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/hash-extra-jh.c.o
[ 10%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/hash-extra-skein.c.o
[ 10%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/hash.c.o
[ 10%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/jh.c.o
[ 11%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/keccak.c.o
[ 11%] Linking C static library liblmdb.a
make[3]: Leaving directory '/home/c50a326/github/monero/build/release'
[ 11%] Built target lmdb
[ 11%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/oaes_lib.c.o
[ 11%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/random.c.o
[ 12%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/skein.c.o
[ 12%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/slow-hash.c.o
[ 13%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/tree-hash.c.o
make[3]: Leaving directory '/home/c50a326/github/monero/build/release'
[ 13%] Built target obj_cncrypto
make[3]: Leaving directory '/home/c50a326/github/monero/build/release'
[ 13%] Built target obj_ringct_basic
[ 14%] Linking CXX static library libeasylogging.a
make[3]: Leaving directory '/home/c50a326/github/monero/build/release'
[ 14%] Built target easylogging
cc1plus: all warnings being treated as errors
make[3]: *** [src/ringct/CMakeFiles/obj_ringct.dir/build.make:63: src/ringct/CMakeFiles/obj_ringct.dir/rctSigs.cpp.o] Error 1
make[3]: Leaving directory '/home/c50a326/github/monero/build/release'
make[2]: *** [CMakeFiles/Makefile2:906: src/ringct/CMakeFiles/obj_ringct.dir/all] Error 2
make[2]: Leaving directory '/home/c50a326/github/monero/build/release'
make[1]: *** [Makefile:141: all] Error 2
make[1]: Leaving directory '/home/c50a326/github/monero/build/release'
make: *** [Makefile:65: release-all] Error 2
```

And with `CFLAGS="-Wno-error" CXXFLAGS="-Wno-error"`:
```
mkdir -p build/release
cd build/release && cmake -D BUILD_TESTS=ON -D CMAKE_BUILD_TYPE=release ../.. && make
-- The C compiler identification is GNU 8.1.0
-- The CXX compiler identification is GNU 8.1.0
-- Check for working C compiler: /usr/bin/cc
-- Check for working C compiler: /usr/bin/cc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting C compile features - done
-- Check for working CXX compiler: /usr/bin/c++
-- Check for working CXX compiler: /usr/bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Building without build tag
-- Could not find DEVELOPER_LOCAL_TOOLS in env (not required)
-- BOOST_IGNORE_SYSTEM_PATHS defaults to OFF
-- Could not find DEVELOPER_LIBUNBOUND_OLD in env (not required)
-- Building for a 64-bit system
-- Building internal libraries as static
-- Could not find DATABASE in env (not required unless you want to change database type from default: lmdb)
-- Using LMDB as default DB type
-- Stack trace on exception enabled (using easylogging++)
-- Looking for pthread.h
-- Looking for pthread.h - found
-- Looking for pthread_create
-- Looking for pthread_create - not found
-- Check if compiler accepts -pthread
-- Check if compiler accepts -pthread - yes
-- Found Threads: TRUE  
-- Found OpenSSL: /usr/lib/libcrypto.so (found version "1.1.0h") 
-- Using OpenSSL include dir at /usr/include
-- Found PkgConfig: /usr/bin/pkg-config (found version "0.29.2") 
-- Checking for module 'libpcsclite'
--   No package 'libpcsclite' found
-- Could NOT find PCSC (missing: PCSC_LIBRARY PCSC_INCLUDE_DIR) 
-- Looking for memset_s in c
-- Looking for memset_s in c - not found
-- Looking for explicit_bzero in c
-- Looking for explicit_bzero in c - found
-- Looking for strptime
-- Looking for strptime - found
-- Found MiniUPnPc: /usr/include/miniupnpc  
-- Found miniupnpc API version 17
-- Using shared miniupnpc found at /usr/include/miniupnpc
-- Looking for libunbound
-- Found libunbound include (unbound.h) in /usr/include
-- Found libunbound shared library
-- Using 64-bit LMDB from source tree
-- Building on x86_64 for native
-- Performing Test _Wformat_c
-- Performing Test _Wformat_c - Success
-- Performing Test _Wformat_cxx
-- Performing Test _Wformat_cxx - Success
-- Performing Test _Wformat_security_c
-- Performing Test _Wformat_security_c - Success
-- Performing Test _Wformat_security_cxx
-- Performing Test _Wformat_security_cxx - Success
-- Performing Test _fstack_protector_c
-- Performing Test _fstack_protector_c - Success
-- Performing Test _fstack_protector_cxx
-- Performing Test _fstack_protector_cxx - Success
-- Performing Test _fstack_protector_strong_c
-- Performing Test _fstack_protector_strong_c - Success
-- Performing Test _fstack_protector_strong_cxx
-- Performing Test _fstack_protector_strong_cxx - Success
-- Looking for -pie linker flag
-- Looking for -pie linker flag - found
-- Looking for -Wl,-z,relro linker flag
-- Looking for -Wl,-z,relro linker flag - found
-- Looking for -Wl,-z,now linker flag
-- Looking for -Wl,-z,now linker flag - found
-- Looking for -Wl,-z,noexecstack linker flag
-- Looking for -Wl,-z,noexecstack linker flag - found
-- Looking for -Wl,-z,noexecheap linker flag
-- Looking for -Wl,-z,noexecheap linker flag - not found
-- Using C security hardening flags:  -Wformat -Wformat-security -fstack-protector -fstack-protector-strong
-- Using C++ security hardening flags:  -Wformat -Wformat-security -fstack-protector -fstack-protector-strong
-- Using linker security hardening flags:  -pie -Wl,-z,relro -Wl,-z,now -Wl,-z,noexecstack
-- AES support enabled
-- Found Boost Version: 106600
-- Looking for rl_copy_text
-- Looking for rl_copy_text - found
-- Looking for rl_filename_completion_function
-- Looking for rl_filename_completion_function - found
-- Found readline library at: /usr
-- Found Git: /usr/bin/git
-- Found GTest: /usr/lib/libgtest.so  
-- Found Doxygen: /usr/bin/doxygen (found version "1.8.14") found components:  doxygen dot 
-- Performing Test HAVE_C11
-- Performing Test HAVE_C11 - Success
-- Configuring done
-- Generating done
-- Build files have been written to: /home/c50a326/github/monero/build/release
make[1]: Entering directory '/home/c50a326/github/monero/build/release'
make[2]: Entering directory '/home/c50a326/github/monero/build/release'
make[3]: Entering directory '/home/c50a326/github/monero/build/release'
make[3]: Entering directory '/home/c50a326/github/monero/build/release'
make[3]: Entering directory '/home/c50a326/github/monero/build/release'
make[3]: Entering directory '/home/c50a326/github/monero/build/release'
make[3]: Entering directory '/home/c50a326/github/monero/build/release'
make[3]: Entering directory '/home/c50a326/github/monero/build/release'
make[3]: Entering directory '/home/c50a326/github/monero/build/release'
Scanning dependencies of target genversion
make[3]: Leaving directory '/home/c50a326/github/monero/build/release'
Scanning dependencies of target easylogging
make[3]: Leaving directory '/home/c50a326/github/monero/build/release'
Scanning dependencies of target generate_translations_header
Scanning dependencies of target lmdb
make[3]: Leaving directory '/home/c50a326/github/monero/build/release'
make[3]: Leaving directory '/home/c50a326/github/monero/build/release'
make[3]: Entering directory '/home/c50a326/github/monero/build/release'
make[3]: Entering directory '/home/c50a326/github/monero/build/release'
Scanning dependencies of target obj_cncrypto
make[3]: Leaving directory '/home/c50a326/github/monero/build/release'
make[3]: Entering directory '/home/c50a326/github/monero/build/release'
[  1%] Creating directories for 'generate_translations_header'
make[3]: Entering directory '/home/c50a326/github/monero/build/release'
make[3]: Entering directory '/home/c50a326/github/monero/build/release'
make[3]: Entering directory '/home/c50a326/github/monero/build/release'
Scanning dependencies of target obj_device
make[3]: Leaving directory '/home/c50a326/github/monero/build/release'
[  2%] Building C object external/db_drivers/liblmdb/CMakeFiles/lmdb.dir/mdb.c.o
[  2%] Building CXX object external/easylogging++/CMakeFiles/easylogging.dir/easylogging++.cc.o
[  2%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/aesb.c.o
make[3]: Entering directory '/home/c50a326/github/monero/build/release'
Scanning dependencies of target obj_ringct
make[3]: Leaving directory '/home/c50a326/github/monero/build/release'
make[3]: Entering directory '/home/c50a326/github/monero/build/release'
Scanning dependencies of target obj_ringct_basic
make[3]: Leaving directory '/home/c50a326/github/monero/build/release'
[  2%] Building CXX object src/device/CMakeFiles/obj_device.dir/device.cpp.o
make[3]: Entering directory '/home/c50a326/github/monero/build/release'
[  3%] Generating ../version.cpp
[  3%] Building CXX object src/ringct/CMakeFiles/obj_ringct.dir/rctSigs.cpp.o
[  3%] Building CXX object src/ringct/CMakeFiles/obj_ringct_basic.dir/rctOps.cpp.o
-- You are currently on commit c29890c2
-- The most recent tag was at c29890c2
-- You are building a tagged release
make[3]: Leaving directory '/home/c50a326/github/monero/build/release'
[  3%] Built target genversion
[  4%] Building CXX object src/ringct/CMakeFiles/obj_ringct_basic.dir/rctTypes.cpp.o
[  4%] No download step for 'generate_translations_header'
[  5%] No patch step for 'generate_translations_header'
[  5%] No update step for 'generate_translations_header'
[  5%] Performing configure step for 'generate_translations_header'
[  5%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/blake256.c.o
-- The C compiler identification is GNU 8.1.0
-- The CXX compiler identification is GNU 8.1.0
[  6%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/chacha.c.o
-- Check for working C compiler: /usr/bin/cc
[  6%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/crypto-ops-data.c.o
-- Check for working C compiler: /usr/bin/cc -- works
-- Detecting C compiler ABI info
[  7%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/crypto-ops.c.o
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting C compile features - done
-- Check for working CXX compiler: /usr/bin/c++
-- Check for working CXX compiler: /usr/bin/c++ -- works
-- Detecting CXX compiler ABI info
In file included from /home/c50a326/github/monero/src/device/device.hpp:48,
                 from /home/c50a326/github/monero/src/device/device.cpp:30:
/home/c50a326/github/monero/src/crypto/chacha.h: In function ‘void crypto::generate_chacha_key(const void*, size_t, crypto::chacha_key&)’:
/home/c50a326/github/monero/src/crypto/chacha.h:76:46: error: ‘void* memcpy(void*, const void*, size_t)’ writing to an object of non-trivially copyable type ‘using chacha_key = tools::scrubbed_arr<unsigned char, 32>’ {aka ‘struct tools::scrubbed<std::array<unsigned char, 32> >’}; use copy-assignment or copy-initialization instead [-Werror=class-memaccess]
     memcpy(&key, pwd_hash.data(), sizeof(key));
                                              ^
In file included from /home/c50a326/github/monero/src/crypto/crypto.h:44,
                 from /home/c50a326/github/monero/src/device/device.hpp:47,
                 from /home/c50a326/github/monero/src/device/device.cpp:30:
/home/c50a326/github/monero/contrib/epee/include/memwipe.h:53:10: note: ‘using chacha_key = tools::scrubbed_arr<unsigned char, 32>’ {aka ‘struct tools::scrubbed<std::array<unsigned char, 32> >’} declared here
   struct scrubbed : public T {
          ^~~~~~~~
In file included from /home/c50a326/github/monero/src/device/device.hpp:48,
                 from /home/c50a326/github/monero/src/device/device.cpp:30:
/home/c50a326/github/monero/src/crypto/chacha.h: In function ‘void crypto::generate_chacha_key_prehashed(const void*, size_t, crypto::chacha_key&)’:
/home/c50a326/github/monero/src/crypto/chacha.h:83:46: error: ‘void* memcpy(void*, const void*, size_t)’ writing to an object of non-trivially copyable type ‘using chacha_key = tools::scrubbed_arr<unsigned char, 32>’ {aka ‘struct tools::scrubbed<std::array<unsigned char, 32> >’}; use copy-assignment or copy-initialization instead [-Werror=class-memaccess]
     memcpy(&key, pwd_hash.data(), sizeof(key));
                                              ^
In file included from /home/c50a326/github/monero/src/crypto/crypto.h:44,
                 from /home/c50a326/github/monero/src/device/device.hpp:47,
                 from /home/c50a326/github/monero/src/device/device.cpp:30:
/home/c50a326/github/monero/contrib/epee/include/memwipe.h:53:10: note: ‘using chacha_key = tools::scrubbed_arr<unsigned char, 32>’ {aka ‘struct tools::scrubbed<std::array<unsigned char, 32> >’} declared here
   struct scrubbed : public T {
          ^~~~~~~~
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
make[3]: Entering directory '/home/c50a326/github/monero/build/release'
[  8%] Generating stagenet_blocks.o
[  8%] Generating blocks.o
[  8%] Generating testnet_blocks.o
Scanning dependencies of target blocks
make[3]: Leaving directory '/home/c50a326/github/monero/build/release'
make[3]: Entering directory '/home/c50a326/github/monero/build/release'
[  8%] Building C object src/blocks/CMakeFiles/blocks.dir/blockexports.c.o
[  8%] Building CXX object src/crypto/CMakeFiles/obj_cncrypto.dir/crypto.cpp.o
-- Detecting CXX compile features - done
[  8%] Linking C static library libblocks.a
lrelease version 5.10.1
-- Configuring done
-- Generating done
-- Build files have been written to: /home/c50a326/github/monero/build/release/translations
[  8%] Performing build step for 'generate_translations_header'
make[4]: Entering directory '/home/c50a326/github/monero/build/release/translations'
cc1plus: all warnings being treated as errors
make[5]: Entering directory '/home/c50a326/github/monero/build/release/translations'
make[6]: Entering directory '/home/c50a326/github/monero/build/release/translations'
Scanning dependencies of target generate_translations_header
make[6]: Leaving directory '/home/c50a326/github/monero/build/release/translations'
make[6]: Entering directory '/home/c50a326/github/monero/build/release/translations'
make[3]: Leaving directory '/home/c50a326/github/monero/build/release'
[ 50%] Building C object CMakeFiles/generate_translations_header.dir/generate_translations_header.c.o
[  8%] Built target blocks
make[3]: Entering directory '/home/c50a326/github/monero/build/release'
[100%] Linking C executable generate_translations_header
Updating 'monero.qm'...
    Generated 0 translation(s) (0 finished and 0 unfinished)
    Ignored 737 untranslated source text(s)
Updating 'monero_fr.qm'...
Scanning dependencies of target obj_checkpoints
    Generated 737 translation(s) (737 finished and 0 unfinished)
make[3]: Leaving directory '/home/c50a326/github/monero/build/release'
make[3]: Entering directory '/home/c50a326/github/monero/build/release'
Updating 'monero_it.qm'...
    Generated 380 translation(s) (376 finished and 4 unfinished)
    Ignored 357 untranslated source text(s)
Updating 'monero_sv.qm'...
    Generated 737 translation(s) (737 finished and 0 unfinished)
[  9%] Building CXX object src/checkpoints/CMakeFiles/obj_checkpoints.dir/checkpoints.cpp.o
Generating embedded translations header
make[6]: Leaving directory '/home/c50a326/github/monero/build/release/translations'
[100%] Built target generate_translations_header
make[5]: Leaving directory '/home/c50a326/github/monero/build/release/translations'
make[4]: Leaving directory '/home/c50a326/github/monero/build/release/translations'
[  9%] Performing install step for 'generate_translations_header'

[  9%] Completed 'generate_translations_header'
make[3]: Leaving directory '/home/c50a326/github/monero/build/release'
[  9%] Built target generate_translations_header
make[3]: Entering directory '/home/c50a326/github/monero/build/release'
Scanning dependencies of target obj_cryptonote_basic
make[3]: Leaving directory '/home/c50a326/github/monero/build/release'
make[3]: Entering directory '/home/c50a326/github/monero/build/release'
[ 10%] Building CXX object src/cryptonote_basic/CMakeFiles/obj_cryptonote_basic.dir/account.cpp.o
In file included from /home/c50a326/github/monero/src/serialization/crypto.h:37,
                 from /home/c50a326/github/monero/src/cryptonote_basic/cryptonote_basic.h:44,
                 from /home/c50a326/github/monero/src/cryptonote_basic/cryptonote_basic_impl.h:33,
                 from /home/c50a326/github/monero/src/cryptonote_basic/cryptonote_format_utils.h:33,
                 from /home/c50a326/github/monero/src/ringct/rctSigs.cpp:37:
/home/c50a326/github/monero/src/crypto/chacha.h: In function ‘void crypto::generate_chacha_key(const void*, size_t, crypto::chacha_key&)’:
/home/c50a326/github/monero/src/crypto/chacha.h:76:46: error: ‘void* memcpy(void*, const void*, size_t)’ writing to an object of non-trivially copyable type ‘using chacha_key = tools::scrubbed_arr<unsigned char, 32>’ {aka ‘struct tools::scrubbed<std::array<unsigned char, 32> >’}; use copy-assignment or copy-initialization instead [-Werror=class-memaccess]
     memcpy(&key, pwd_hash.data(), sizeof(key));
                                              ^
In file included from /home/c50a326/github/monero/src/crypto/crypto.h:44,
                 from /home/c50a326/github/monero/src/ringct/rctSigs.h:48,
                 from /home/c50a326/github/monero/src/ringct/rctSigs.cpp:35:
/home/c50a326/github/monero/contrib/epee/include/memwipe.h:53:10: note: ‘using chacha_key = tools::scrubbed_arr<unsigned char, 32>’ {aka ‘struct tools::scrubbed<std::array<unsigned char, 32> >’} declared here
   struct scrubbed : public T {
          ^~~~~~~~
In file included from /home/c50a326/github/monero/src/serialization/crypto.h:37,
                 from /home/c50a326/github/monero/src/cryptonote_basic/cryptonote_basic.h:44,
                 from /home/c50a326/github/monero/src/cryptonote_basic/cryptonote_basic_impl.h:33,
                 from /home/c50a326/github/monero/src/cryptonote_basic/cryptonote_format_utils.h:33,
                 from /home/c50a326/github/monero/src/ringct/rctSigs.cpp:37:
/home/c50a326/github/monero/src/crypto/chacha.h: In function ‘void crypto::generate_chacha_key_prehashed(const void*, size_t, crypto::chacha_key&)’:
/home/c50a326/github/monero/src/crypto/chacha.h:83:46: error: ‘void* memcpy(void*, const void*, size_t)’ writing to an object of non-trivially copyable type ‘using chacha_key = tools::scrubbed_arr<unsigned char, 32>’ {aka ‘struct tools::scrubbed<std::array<unsigned char, 32> >’}; use copy-assignment or copy-initialization instead [-Werror=class-memaccess]
     memcpy(&key, pwd_hash.data(), sizeof(key));
                                              ^
In file included from /home/c50a326/github/monero/src/crypto/crypto.h:44,
                 from /home/c50a326/github/monero/src/ringct/rctSigs.h:48,
                 from /home/c50a326/github/monero/src/ringct/rctSigs.cpp:35:
/home/c50a326/github/monero/contrib/epee/include/memwipe.h:53:10: note: ‘using chacha_key = tools::scrubbed_arr<unsigned char, 32>’ {aka ‘struct tools::scrubbed<std::array<unsigned char, 32> >’} declared here
   struct scrubbed : public T {
          ^~~~~~~~
[ 10%] Building C object external/db_drivers/liblmdb/CMakeFiles/lmdb.dir/midl.c.o
[ 10%] Linking C static library liblmdb.a
make[3]: Leaving directory '/home/c50a326/github/monero/build/release'
[ 10%] Built target lmdb
make[3]: Entering directory '/home/c50a326/github/monero/build/release'
Scanning dependencies of target obj_cryptonote_core
make[3]: Leaving directory '/home/c50a326/github/monero/build/release'
make[3]: Entering directory '/home/c50a326/github/monero/build/release'
[ 10%] Building CXX object src/cryptonote_core/CMakeFiles/obj_cryptonote_core.dir/blockchain.cpp.o
[ 10%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/groestl.c.o
[ 10%] Building C object src/ringct/CMakeFiles/obj_ringct_basic.dir/rctCryptoOps.c.o
[ 10%] Building CXX object src/ringct/CMakeFiles/obj_ringct_basic.dir/bulletproofs.cc.o
[ 11%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/hash-extra-blake.c.o
[ 11%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/hash-extra-groestl.c.o
[ 11%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/hash-extra-jh.c.o
[ 12%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/hash-extra-skein.c.o
[ 12%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/hash.c.o
[ 12%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/jh.c.o
In file included from /home/c50a326/github/monero/src/serialization/crypto.h:37,
                 from /home/c50a326/github/monero/src/cryptonote_basic/cryptonote_basic.h:44,
                 from /home/c50a326/github/monero/src/cryptonote_basic/account.h:33,
                 from /home/c50a326/github/monero/src/cryptonote_basic/account.cpp:34:
/home/c50a326/github/monero/src/crypto/chacha.h: In function ‘void crypto::generate_chacha_key(const void*, size_t, crypto::chacha_key&)’:
/home/c50a326/github/monero/src/crypto/chacha.h:76:46: error: ‘void* memcpy(void*, const void*, size_t)’ writing to an object of non-trivially copyable type ‘using chacha_key = tools::scrubbed_arr<unsigned char, 32>’ {aka ‘struct tools::scrubbed<std::array<unsigned char, 32> >’}; use copy-assignment or copy-initialization instead [-Werror=class-memaccess]
     memcpy(&key, pwd_hash.data(), sizeof(key));
                                              ^
In file included from /home/c50a326/github/monero/src/crypto/chacha.h:42,
                 from /home/c50a326/github/monero/src/serialization/crypto.h:37,
                 from /home/c50a326/github/monero/src/cryptonote_basic/cryptonote_basic.h:44,
                 from /home/c50a326/github/monero/src/cryptonote_basic/account.h:33,
                 from /home/c50a326/github/monero/src/cryptonote_basic/account.cpp:34:
/home/c50a326/github/monero/contrib/epee/include/memwipe.h:53:10: note: ‘using chacha_key = tools::scrubbed_arr<unsigned char, 32>’ {aka ‘struct tools::scrubbed<std::array<unsigned char, 32> >’} declared here
   struct scrubbed : public T {
          ^~~~~~~~
In file included from /home/c50a326/github/monero/src/serialization/crypto.h:37,
                 from /home/c50a326/github/monero/src/cryptonote_basic/cryptonote_basic.h:44,
                 from /home/c50a326/github/monero/src/cryptonote_basic/account.h:33,
                 from /home/c50a326/github/monero/src/cryptonote_basic/account.cpp:34:
/home/c50a326/github/monero/src/crypto/chacha.h: In function ‘void crypto::generate_chacha_key_prehashed(const void*, size_t, crypto::chacha_key&)’:
/home/c50a326/github/monero/src/crypto/chacha.h:83:46: error: ‘void* memcpy(void*, const void*, size_t)’ writing to an object of non-trivially copyable type ‘using chacha_key = tools::scrubbed_arr<unsigned char, 32>’ {aka ‘struct tools::scrubbed<std::array<unsigned char, 32> >’}; use copy-assignment or copy-initialization instead [-Werror=class-memaccess]
     memcpy(&key, pwd_hash.data(), sizeof(key));
                                              ^
In file included from /home/c50a326/github/monero/src/crypto/chacha.h:42,
                 from /home/c50a326/github/monero/src/serialization/crypto.h:37,
                 from /home/c50a326/github/monero/src/cryptonote_basic/cryptonote_basic.h:44,
                 from /home/c50a326/github/monero/src/cryptonote_basic/account.h:33,
                 from /home/c50a326/github/monero/src/cryptonote_basic/account.cpp:34:
/home/c50a326/github/monero/contrib/epee/include/memwipe.h:53:10: note: ‘using chacha_key = tools::scrubbed_arr<unsigned char, 32>’ {aka ‘struct tools::scrubbed<std::array<unsigned char, 32> >’} declared here
   struct scrubbed : public T {
          ^~~~~~~~
[ 13%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/keccak.c.o
[ 13%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/oaes_lib.c.o
/home/c50a326/github/monero/src/cryptonote_basic/account.cpp: In member function ‘void cryptonote::account_base::create_from_viewkey(const cryptonote::account_public_address&, const secret_key&)’:
/home/c50a326/github/monero/src/cryptonote_basic/account.cpp:160:34: error: ‘void* memset(void*, int, size_t)’ clearing an object of non-trivial type ‘using secret_key = struct tools::scrubbed<crypto::ec_scalar>’ {aka ‘struct tools::scrubbed<crypto::ec_scalar>’}; use assignment or value-initialization instead [-Werror=class-memaccess]
     memset(&fake, 0, sizeof(fake));
                                  ^
In file included from /home/c50a326/github/monero/src/crypto/chacha.h:42,
                 from /home/c50a326/github/monero/src/serialization/crypto.h:37,
                 from /home/c50a326/github/monero/src/cryptonote_basic/cryptonote_basic.h:44,
                 from /home/c50a326/github/monero/src/cryptonote_basic/account.h:33,
                 from /home/c50a326/github/monero/src/cryptonote_basic/account.cpp:34:
/home/c50a326/github/monero/contrib/epee/include/memwipe.h:53:10: note: ‘using secret_key = struct tools::scrubbed<crypto::ec_scalar>’ {aka ‘struct tools::scrubbed<crypto::ec_scalar>’} declared here
   struct scrubbed : public T {
          ^~~~~~~~
[ 13%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/random.c.o
[ 14%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/skein.c.o
In file included from /home/c50a326/github/monero/src/serialization/crypto.h:37,
                 from /home/c50a326/github/monero/src/cryptonote_basic/cryptonote_basic.h:44,
                 from /home/c50a326/github/monero/src/cryptonote_basic/cryptonote_basic_impl.h:33,
                 from /home/c50a326/github/monero/src/cryptonote_core/blockchain.cpp:37:
/home/c50a326/github/monero/src/crypto/chacha.h: In function ‘void crypto::generate_chacha_key(const void*, size_t, crypto::chacha_key&)’:
/home/c50a326/github/monero/src/crypto/chacha.h:76:46: error: ‘void* memcpy(void*, const void*, size_t)’ writing to an object of non-trivially copyable type ‘using chacha_key = tools::scrubbed_arr<unsigned char, 32>’ {aka ‘struct tools::scrubbed<std::array<unsigned char, 32> >’}; use copy-assignment or copy-initialization instead [-Werror=class-memaccess]
     memcpy(&key, pwd_hash.data(), sizeof(key));
                                              ^
In file included from /home/c50a326/github/monero/src/crypto/chacha.h:42,
                 from /home/c50a326/github/monero/src/serialization/crypto.h:37,
                 from /home/c50a326/github/monero/src/cryptonote_basic/cryptonote_basic.h:44,
                 from /home/c50a326/github/monero/src/cryptonote_basic/cryptonote_basic_impl.h:33,
                 from /home/c50a326/github/monero/src/cryptonote_core/blockchain.cpp:37:
/home/c50a326/github/monero/contrib/epee/include/memwipe.h:53:10: note: ‘using chacha_key = tools::scrubbed_arr<unsigned char, 32>’ {aka ‘struct tools::scrubbed<std::array<unsigned char, 32> >’} declared here
   struct scrubbed : public T {
          ^~~~~~~~
In file included from /home/c50a326/github/monero/src/serialization/crypto.h:37,
                 from /home/c50a326/github/monero/src/cryptonote_basic/cryptonote_basic.h:44,
                 from /home/c50a326/github/monero/src/cryptonote_basic/cryptonote_basic_impl.h:33,
                 from /home/c50a326/github/monero/src/cryptonote_core/blockchain.cpp:37:
/home/c50a326/github/monero/src/crypto/chacha.h: In function ‘void crypto::generate_chacha_key_prehashed(const void*, size_t, crypto::chacha_key&)’:
/home/c50a326/github/monero/src/crypto/chacha.h:83:46: error: ‘void* memcpy(void*, const void*, size_t)’ writing to an object of non-trivially copyable type ‘using chacha_key = tools::scrubbed_arr<unsigned char, 32>’ {aka ‘struct tools::scrubbed<std::array<unsigned char, 32> >’}; use copy-assignment or copy-initialization instead [-Werror=class-memaccess]
     memcpy(&key, pwd_hash.data(), sizeof(key));
                                              ^
In file included from /home/c50a326/github/monero/src/crypto/chacha.h:42,
                 from /home/c50a326/github/monero/src/serialization/crypto.h:37,
                 from /home/c50a326/github/monero/src/cryptonote_basic/cryptonote_basic.h:44,
                 from /home/c50a326/github/monero/src/cryptonote_basic/cryptonote_basic_impl.h:33,
                 from /home/c50a326/github/monero/src/cryptonote_core/blockchain.cpp:37:
/home/c50a326/github/monero/contrib/epee/include/memwipe.h:53:10: note: ‘using chacha_key = tools::scrubbed_arr<unsigned char, 32>’ {aka ‘struct tools::scrubbed<std::array<unsigned char, 32> >’} declared here
   struct scrubbed : public T {
          ^~~~~~~~
[ 15%] Linking CXX static library libeasylogging.a
make[3]: Leaving directory '/home/c50a326/github/monero/build/release'
[ 15%] Built target easylogging
[ 15%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/slow-hash.c.o
[ 16%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/tree-hash.c.o
make[3]: Entering directory '/home/c50a326/github/monero/build/release'
Scanning dependencies of target obj_multisig
make[3]: Leaving directory '/home/c50a326/github/monero/build/release'
make[3]: Entering directory '/home/c50a326/github/monero/build/release'
[ 16%] Building CXX object src/multisig/CMakeFiles/obj_multisig.dir/multisig.cpp.o
make[3]: Leaving directory '/home/c50a326/github/monero/build/release'
[ 16%] Built target obj_cncrypto
make[3]: Entering directory '/home/c50a326/github/monero/build/release'
Scanning dependencies of target obj_blockchain_db
make[3]: Leaving directory '/home/c50a326/github/monero/build/release'
make[3]: Entering directory '/home/c50a326/github/monero/build/release'
[ 16%] Building CXX object src/blockchain_db/CMakeFiles/obj_blockchain_db.dir/blockchain_db.cpp.o
cc1plus: all warnings being treated as errors
make[3]: *** [src/ringct/CMakeFiles/obj_ringct.dir/build.make:63: src/ringct/CMakeFiles/obj_ringct.dir/rctSigs.cpp.o] Error 1
make[3]: Leaving directory '/home/c50a326/github/monero/build/release'
make[2]: *** [CMakeFiles/Makefile2:906: src/ringct/CMakeFiles/obj_ringct.dir/all] Error 2
make[2]: *** Waiting for unfinished jobs....
[ 16%] Building CXX object src/cryptonote_basic/CMakeFiles/obj_cryptonote_basic.dir/cryptonote_basic_impl.cpp.o
cc1plus: all warnings being treated as errors
make[3]: *** [src/cryptonote_basic/CMakeFiles/obj_cryptonote_basic.dir/build.make:63: src/cryptonote_basic/CMakeFiles/obj_cryptonote_basic.dir/account.cpp.o] Error 1
make[3]: *** Waiting for unfinished jobs....
make[3]: *** [src/device/CMakeFiles/obj_device.dir/build.make:63: src/device/CMakeFiles/obj_device.dir/device.cpp.o] Error 1
make[3]: *** Waiting for unfinished jobs....
[ 16%] Building CXX object src/device/CMakeFiles/obj_device.dir/device_default.cpp.o
[ 16%] Building CXX object src/blockchain_db/CMakeFiles/obj_blockchain_db.dir/lmdb/db_lmdb.cpp.o
In file included from /home/c50a326/github/monero/src/serialization/crypto.h:37,
                 from /home/c50a326/github/monero/src/cryptonote_basic/cryptonote_basic.h:44,
                 from /home/c50a326/github/monero/src/cryptonote_basic/account.h:33,
                 from /home/c50a326/github/monero/src/multisig/multisig.cpp:33:
/home/c50a326/github/monero/src/crypto/chacha.h: In function ‘void crypto::generate_chacha_key(const void*, size_t, crypto::chacha_key&)’:
/home/c50a326/github/monero/src/crypto/chacha.h:76:46: error: ‘void* memcpy(void*, const void*, size_t)’ writing to an object of non-trivially copyable type ‘using chacha_key = tools::scrubbed_arr<unsigned char, 32>’ {aka ‘struct tools::scrubbed<std::array<unsigned char, 32> >’}; use copy-assignment or copy-initialization instead [-Werror=class-memaccess]
     memcpy(&key, pwd_hash.data(), sizeof(key));
                                              ^
In file included from /home/c50a326/github/monero/src/crypto/crypto.h:44,
                 from /home/c50a326/github/monero/src/multisig/multisig.cpp:31:
/home/c50a326/github/monero/contrib/epee/include/memwipe.h:53:10: note: ‘using chacha_key = tools::scrubbed_arr<unsigned char, 32>’ {aka ‘struct tools::scrubbed<std::array<unsigned char, 32> >’} declared here
   struct scrubbed : public T {
          ^~~~~~~~
In file included from /home/c50a326/github/monero/src/serialization/crypto.h:37,
                 from /home/c50a326/github/monero/src/cryptonote_basic/cryptonote_basic.h:44,
                 from /home/c50a326/github/monero/src/cryptonote_basic/account.h:33,
                 from /home/c50a326/github/monero/src/multisig/multisig.cpp:33:
/home/c50a326/github/monero/src/crypto/chacha.h: In function ‘void crypto::generate_chacha_key_prehashed(const void*, size_t, crypto::chacha_key&)’:
/home/c50a326/github/monero/src/crypto/chacha.h:83:46: error: ‘void* memcpy(void*, const void*, size_t)’ writing to an object of non-trivially copyable type ‘using chacha_key = tools::scrubbed_arr<unsigned char, 32>’ {aka ‘struct tools::scrubbed<std::array<unsigned char, 32> >’}; use copy-assignment or copy-initialization instead [-Werror=class-memaccess]
     memcpy(&key, pwd_hash.data(), sizeof(key));
                                              ^
In file included from /home/c50a326/github/monero/src/crypto/crypto.h:44,
                 from /home/c50a326/github/monero/src/multisig/multisig.cpp:31:
/home/c50a326/github/monero/contrib/epee/include/memwipe.h:53:10: note: ‘using chacha_key = tools::scrubbed_arr<unsigned char, 32>’ {aka ‘struct tools::scrubbed<std::array<unsigned char, 32> >’} declared here
   struct scrubbed : public T {
          ^~~~~~~~
make[3]: Leaving directory '/home/c50a326/github/monero/build/release'
[ 16%] Built target obj_ringct_basic
[ 16%] Building CXX object src/cryptonote_core/CMakeFiles/obj_cryptonote_core.dir/cryptonote_core.cpp.o
In file included from /home/c50a326/github/monero/src/serialization/crypto.h:37,
                 from /home/c50a326/github/monero/src/cryptonote_basic/cryptonote_basic.h:44,
                 from /home/c50a326/github/monero/src/blockchain_db/blockchain_db.h:40,
                 from /home/c50a326/github/monero/src/blockchain_db/blockchain_db.cpp:32:
/home/c50a326/github/monero/src/crypto/chacha.h: In function ‘void crypto::generate_chacha_key(const void*, size_t, crypto::chacha_key&)’:
/home/c50a326/github/monero/src/crypto/chacha.h:76:46: error: ‘void* memcpy(void*, const void*, size_t)’ writing to an object of non-trivially copyable type ‘using chacha_key = tools::scrubbed_arr<unsigned char, 32>’ {aka ‘struct tools::scrubbed<std::array<unsigned char, 32> >’}; use copy-assignment or copy-initialization instead [-Werror=class-memaccess]
     memcpy(&key, pwd_hash.data(), sizeof(key));
                                              ^
In file included from /home/c50a326/github/monero/contrib/epee/include/string_tools.h:48,
                 from /home/c50a326/github/monero/src/blockchain_db/blockchain_db.cpp:31:
/home/c50a326/github/monero/contrib/epee/include/memwipe.h:53:10: note: ‘using chacha_key = tools::scrubbed_arr<unsigned char, 32>’ {aka ‘struct tools::scrubbed<std::array<unsigned char, 32> >’} declared here
   struct scrubbed : public T {
          ^~~~~~~~
In file included from /home/c50a326/github/monero/src/serialization/crypto.h:37,
                 from /home/c50a326/github/monero/src/cryptonote_basic/cryptonote_basic.h:44,
                 from /home/c50a326/github/monero/src/blockchain_db/blockchain_db.h:40,
                 from /home/c50a326/github/monero/src/blockchain_db/blockchain_db.cpp:32:
/home/c50a326/github/monero/src/crypto/chacha.h: In function ‘void crypto::generate_chacha_key_prehashed(const void*, size_t, crypto::chacha_key&)’:
/home/c50a326/github/monero/src/crypto/chacha.h:83:46: error: ‘void* memcpy(void*, const void*, size_t)’ writing to an object of non-trivially copyable type ‘using chacha_key = tools::scrubbed_arr<unsigned char, 32>’ {aka ‘struct tools::scrubbed<std::array<unsigned char, 32> >’}; use copy-assignment or copy-initialization instead [-Werror=class-memaccess]
     memcpy(&key, pwd_hash.data(), sizeof(key));
                                              ^
In file included from /home/c50a326/github/monero/contrib/epee/include/string_tools.h:48,
                 from /home/c50a326/github/monero/src/blockchain_db/blockchain_db.cpp:31:
/home/c50a326/github/monero/contrib/epee/include/memwipe.h:53:10: note: ‘using chacha_key = tools::scrubbed_arr<unsigned char, 32>’ {aka ‘struct tools::scrubbed<std::array<unsigned char, 32> >’} declared here
   struct scrubbed : public T {
          ^~~~~~~~
In file included from /home/c50a326/github/monero/src/device/device.hpp:48,
                 from /home/c50a326/github/monero/src/device/device_default.hpp:32,
                 from /home/c50a326/github/monero/src/device/device_default.cpp:33:
/home/c50a326/github/monero/src/crypto/chacha.h: In function ‘void crypto::generate_chacha_key(const void*, size_t, crypto::chacha_key&)’:
/home/c50a326/github/monero/src/crypto/chacha.h:76:46: error: ‘void* memcpy(void*, const void*, size_t)’ writing to an object of non-trivially copyable type ‘using chacha_key = tools::scrubbed_arr<unsigned char, 32>’ {aka ‘struct tools::scrubbed<std::array<unsigned char, 32> >’}; use copy-assignment or copy-initialization instead [-Werror=class-memaccess]
     memcpy(&key, pwd_hash.data(), sizeof(key));
                                              ^
In file included from /home/c50a326/github/monero/src/crypto/crypto.h:44,
                 from /home/c50a326/github/monero/src/device/device.hpp:47,
                 from /home/c50a326/github/monero/src/device/device_default.hpp:32,
                 from /home/c50a326/github/monero/src/device/device_default.cpp:33:
/home/c50a326/github/monero/contrib/epee/include/memwipe.h:53:10: note: ‘using chacha_key = tools::scrubbed_arr<unsigned char, 32>’ {aka ‘struct tools::scrubbed<std::array<unsigned char, 32> >’} declared here
   struct scrubbed : public T {
          ^~~~~~~~
In file included from /home/c50a326/github/monero/src/device/device.hpp:48,
                 from /home/c50a326/github/monero/src/device/device_default.hpp:32,
                 from /home/c50a326/github/monero/src/device/device_default.cpp:33:
/home/c50a326/github/monero/src/crypto/chacha.h: In function ‘void crypto::generate_chacha_key_prehashed(const void*, size_t, crypto::chacha_key&)’:
/home/c50a326/github/monero/src/crypto/chacha.h:83:46: error: ‘void* memcpy(void*, const void*, size_t)’ writing to an object of non-trivially copyable type ‘using chacha_key = tools::scrubbed_arr<unsigned char, 32>’ {aka ‘struct tools::scrubbed<std::array<unsigned char, 32> >’}; use copy-assignment or copy-initialization instead [-Werror=class-memaccess]
     memcpy(&key, pwd_hash.data(), sizeof(key));
                                              ^
In file included from /home/c50a326/github/monero/src/crypto/crypto.h:44,
                 from /home/c50a326/github/monero/src/device/device.hpp:47,
                 from /home/c50a326/github/monero/src/device/device_default.hpp:32,
                 from /home/c50a326/github/monero/src/device/device_default.cpp:33:
/home/c50a326/github/monero/contrib/epee/include/memwipe.h:53:10: note: ‘using chacha_key = tools::scrubbed_arr<unsigned char, 32>’ {aka ‘struct tools::scrubbed<std::array<unsigned char, 32> >’} declared here
   struct scrubbed : public T {
          ^~~~~~~~
In file included from /home/c50a326/github/monero/src/serialization/crypto.h:37,
                 from /home/c50a326/github/monero/src/cryptonote_basic/cryptonote_basic.h:44,
                 from /home/c50a326/github/monero/src/cryptonote_basic/cryptonote_basic_impl.h:33,
                 from /home/c50a326/github/monero/src/cryptonote_basic/cryptonote_basic_impl.cpp:34:
/home/c50a326/github/monero/src/crypto/chacha.h: In function ‘void crypto::generate_chacha_key(const void*, size_t, crypto::chacha_key&)’:
/home/c50a326/github/monero/src/crypto/chacha.h:76:46: error: ‘void* memcpy(void*, const void*, size_t)’ writing to an object of non-trivially copyable type ‘using chacha_key = tools::scrubbed_arr<unsigned char, 32>’ {aka ‘struct tools::scrubbed<std::array<unsigned char, 32> >’}; use copy-assignment or copy-initialization instead [-Werror=class-memaccess]
     memcpy(&key, pwd_hash.data(), sizeof(key));
                                              ^
In file included from /home/c50a326/github/monero/src/crypto/chacha.h:42,
                 from /home/c50a326/github/monero/src/serialization/crypto.h:37,
                 from /home/c50a326/github/monero/src/cryptonote_basic/cryptonote_basic.h:44,
                 from /home/c50a326/github/monero/src/cryptonote_basic/cryptonote_basic_impl.h:33,
                 from /home/c50a326/github/monero/src/cryptonote_basic/cryptonote_basic_impl.cpp:34:
/home/c50a326/github/monero/contrib/epee/include/memwipe.h:53:10: note: ‘using chacha_key = tools::scrubbed_arr<unsigned char, 32>’ {aka ‘struct tools::scrubbed<std::array<unsigned char, 32> >’} declared here
   struct scrubbed : public T {
          ^~~~~~~~
In file included from /home/c50a326/github/monero/src/serialization/crypto.h:37,
                 from /home/c50a326/github/monero/src/cryptonote_basic/cryptonote_basic.h:44,
                 from /home/c50a326/github/monero/src/cryptonote_basic/cryptonote_basic_impl.h:33,
                 from /home/c50a326/github/monero/src/cryptonote_basic/cryptonote_basic_impl.cpp:34:
/home/c50a326/github/monero/src/crypto/chacha.h: In function ‘void crypto::generate_chacha_key_prehashed(const void*, size_t, crypto::chacha_key&)’:
/home/c50a326/github/monero/src/crypto/chacha.h:83:46: error: ‘void* memcpy(void*, const void*, size_t)’ writing to an object of non-trivially copyable type ‘using chacha_key = tools::scrubbed_arr<unsigned char, 32>’ {aka ‘struct tools::scrubbed<std::array<unsigned char, 32> >’}; use copy-assignment or copy-initialization instead [-Werror=class-memaccess]
     memcpy(&key, pwd_hash.data(), sizeof(key));
                                              ^
In file included from /home/c50a326/github/monero/src/crypto/chacha.h:42,
                 from /home/c50a326/github/monero/src/serialization/crypto.h:37,
                 from /home/c50a326/github/monero/src/cryptonote_basic/cryptonote_basic.h:44,
                 from /home/c50a326/github/monero/src/cryptonote_basic/cryptonote_basic_impl.h:33,
                 from /home/c50a326/github/monero/src/cryptonote_basic/cryptonote_basic_impl.cpp:34:
/home/c50a326/github/monero/contrib/epee/include/memwipe.h:53:10: note: ‘using chacha_key = tools::scrubbed_arr<unsigned char, 32>’ {aka ‘struct tools::scrubbed<std::array<unsigned char, 32> >’} declared here
   struct scrubbed : public T {
          ^~~~~~~~
In file included from /home/c50a326/github/monero/src/serialization/crypto.h:37,
                 from /home/c50a326/github/monero/src/cryptonote_basic/cryptonote_basic.h:44,
                 from /home/c50a326/github/monero/src/blockchain_db/blockchain_db.h:40,
                 from /home/c50a326/github/monero/src/blockchain_db/lmdb/db_lmdb.h:31,
                 from /home/c50a326/github/monero/src/blockchain_db/lmdb/db_lmdb.cpp:28:
/home/c50a326/github/monero/src/crypto/chacha.h: In function ‘void crypto::generate_chacha_key(const void*, size_t, crypto::chacha_key&)’:
/home/c50a326/github/monero/src/crypto/chacha.h:76:46: error: ‘void* memcpy(void*, const void*, size_t)’ writing to an object of non-trivially copyable type ‘using chacha_key = tools::scrubbed_arr<unsigned char, 32>’ {aka ‘struct tools::scrubbed<std::array<unsigned char, 32> >’}; use copy-assignment or copy-initialization instead [-Werror=class-memaccess]
     memcpy(&key, pwd_hash.data(), sizeof(key));
                                              ^
In file included from /home/c50a326/github/monero/src/crypto/chacha.h:42,
                 from /home/c50a326/github/monero/src/serialization/crypto.h:37,
                 from /home/c50a326/github/monero/src/cryptonote_basic/cryptonote_basic.h:44,
                 from /home/c50a326/github/monero/src/blockchain_db/blockchain_db.h:40,
                 from /home/c50a326/github/monero/src/blockchain_db/lmdb/db_lmdb.h:31,
                 from /home/c50a326/github/monero/src/blockchain_db/lmdb/db_lmdb.cpp:28:
/home/c50a326/github/monero/contrib/epee/include/memwipe.h:53:10: note: ‘using chacha_key = tools::scrubbed_arr<unsigned char, 32>’ {aka ‘struct tools::scrubbed<std::array<unsigned char, 32> >’} declared here
   struct scrubbed : public T {
          ^~~~~~~~
In file included from /home/c50a326/github/monero/src/serialization/crypto.h:37,
                 from /home/c50a326/github/monero/src/cryptonote_basic/cryptonote_basic.h:44,
                 from /home/c50a326/github/monero/src/blockchain_db/blockchain_db.h:40,
                 from /home/c50a326/github/monero/src/blockchain_db/lmdb/db_lmdb.h:31,
                 from /home/c50a326/github/monero/src/blockchain_db/lmdb/db_lmdb.cpp:28:
/home/c50a326/github/monero/src/crypto/chacha.h: In function ‘void crypto::generate_chacha_key_prehashed(const void*, size_t, crypto::chacha_key&)’:
/home/c50a326/github/monero/src/crypto/chacha.h:83:46: error: ‘void* memcpy(void*, const void*, size_t)’ writing to an object of non-trivially copyable type ‘using chacha_key = tools::scrubbed_arr<unsigned char, 32>’ {aka ‘struct tools::scrubbed<std::array<unsigned char, 32> >’}; use copy-assignment or copy-initialization instead [-Werror=class-memaccess]
     memcpy(&key, pwd_hash.data(), sizeof(key));
                                              ^
In file included from /home/c50a326/github/monero/src/crypto/chacha.h:42,
                 from /home/c50a326/github/monero/src/serialization/crypto.h:37,
                 from /home/c50a326/github/monero/src/cryptonote_basic/cryptonote_basic.h:44,
                 from /home/c50a326/github/monero/src/blockchain_db/blockchain_db.h:40,
                 from /home/c50a326/github/monero/src/blockchain_db/lmdb/db_lmdb.h:31,
                 from /home/c50a326/github/monero/src/blockchain_db/lmdb/db_lmdb.cpp:28:
/home/c50a326/github/monero/contrib/epee/include/memwipe.h:53:10: note: ‘using chacha_key = tools::scrubbed_arr<unsigned char, 32>’ {aka ‘struct tools::scrubbed<std::array<unsigned char, 32> >’} declared here
   struct scrubbed : public T {
          ^~~~~~~~
cc1plus: all warnings being treated as errors
make[3]: *** [src/multisig/CMakeFiles/obj_multisig.dir/build.make:63: src/multisig/CMakeFiles/obj_multisig.dir/multisig.cpp.o] Error 1
make[3]: Leaving directory '/home/c50a326/github/monero/build/release'
make[2]: *** [CMakeFiles/Makefile2:1364: src/multisig/CMakeFiles/obj_multisig.dir/all] Error 2
[ 17%] Building CXX object src/cryptonote_core/CMakeFiles/obj_cryptonote_core.dir/tx_pool.cpp.o
In file included from /home/c50a326/github/monero/src/serialization/crypto.h:37,
                 from /home/c50a326/github/monero/src/cryptonote_basic/cryptonote_basic.h:44,
                 from /home/c50a326/github/monero/src/cryptonote_protocol/cryptonote_protocol_defs.h:35,
                 from /home/c50a326/github/monero/src/cryptonote_protocol/cryptonote_protocol_handler_common.h:34,
                 from /home/c50a326/github/monero/src/cryptonote_core/cryptonote_core.h:39,
                 from /home/c50a326/github/monero/src/cryptonote_core/cryptonote_core.cpp:38:
/home/c50a326/github/monero/src/crypto/chacha.h: In function ‘void crypto::generate_chacha_key(const void*, size_t, crypto::chacha_key&)’:
/home/c50a326/github/monero/src/crypto/chacha.h:76:46: error: ‘void* memcpy(void*, const void*, size_t)’ writing to an object of non-trivially copyable type ‘using chacha_key = tools::scrubbed_arr<unsigned char, 32>’ {aka ‘struct tools::scrubbed<std::array<unsigned char, 32> >’}; use copy-assignment or copy-initialization instead [-Werror=class-memaccess]
     memcpy(&key, pwd_hash.data(), sizeof(key));
                                              ^
In file included from /home/c50a326/github/monero/contrib/epee/include/string_tools.h:48,
                 from /home/c50a326/github/monero/src/cryptonote_core/cryptonote_core.cpp:34:
/home/c50a326/github/monero/contrib/epee/include/memwipe.h:53:10: note: ‘using chacha_key = tools::scrubbed_arr<unsigned char, 32>’ {aka ‘struct tools::scrubbed<std::array<unsigned char, 32> >’} declared here
   struct scrubbed : public T {
          ^~~~~~~~
In file included from /home/c50a326/github/monero/src/serialization/crypto.h:37,
                 from /home/c50a326/github/monero/src/cryptonote_basic/cryptonote_basic.h:44,
                 from /home/c50a326/github/monero/src/cryptonote_protocol/cryptonote_protocol_defs.h:35,
                 from /home/c50a326/github/monero/src/cryptonote_protocol/cryptonote_protocol_handler_common.h:34,
                 from /home/c50a326/github/monero/src/cryptonote_core/cryptonote_core.h:39,
                 from /home/c50a326/github/monero/src/cryptonote_core/cryptonote_core.cpp:38:
/home/c50a326/github/monero/src/crypto/chacha.h: In function ‘void crypto::generate_chacha_key_prehashed(const void*, size_t, crypto::chacha_key&)’:
/home/c50a326/github/monero/src/crypto/chacha.h:83:46: error: ‘void* memcpy(void*, const void*, size_t)’ writing to an object of non-trivially copyable type ‘using chacha_key = tools::scrubbed_arr<unsigned char, 32>’ {aka ‘struct tools::scrubbed<std::array<unsigned char, 32> >’}; use copy-assignment or copy-initialization instead [-Werror=class-memaccess]
     memcpy(&key, pwd_hash.data(), sizeof(key));
                                              ^
In file included from /home/c50a326/github/monero/contrib/epee/include/string_tools.h:48,
                 from /home/c50a326/github/monero/src/cryptonote_core/cryptonote_core.cpp:34:
/home/c50a326/github/monero/contrib/epee/include/memwipe.h:53:10: note: ‘using chacha_key = tools::scrubbed_arr<unsigned char, 32>’ {aka ‘struct tools::scrubbed<std::array<unsigned char, 32> >’} declared here
   struct scrubbed : public T {
          ^~~~~~~~
cc1plus: all warnings being treated as errors
make[3]: *** [src/blockchain_db/CMakeFiles/obj_blockchain_db.dir/build.make:63: src/blockchain_db/CMakeFiles/obj_blockchain_db.dir/blockchain_db.cpp.o] Error 1
make[3]: *** Waiting for unfinished jobs....
[ 17%] Building CXX object src/cryptonote_core/CMakeFiles/obj_cryptonote_core.dir/cryptonote_tx_utils.cpp.o
cc1plus: all warnings being treated as errors
make[3]: *** [src/device/CMakeFiles/obj_device.dir/build.make:76: src/device/CMakeFiles/obj_device.dir/device_default.cpp.o] Error 1
make[3]: Leaving directory '/home/c50a326/github/monero/build/release'
make[2]: *** [CMakeFiles/Makefile2:3262: src/device/CMakeFiles/obj_device.dir/all] Error 2
cc1plus: all warnings being treated as errors
make[3]: *** [src/cryptonote_basic/CMakeFiles/obj_cryptonote_basic.dir/build.make:76: src/cryptonote_basic/CMakeFiles/obj_cryptonote_basic.dir/cryptonote_basic_impl.cpp.o] Error 1
make[3]: Leaving directory '/home/c50a326/github/monero/build/release'
make[2]: *** [CMakeFiles/Makefile2:1107: src/cryptonote_basic/CMakeFiles/obj_cryptonote_basic.dir/all] Error 2
In file included from /home/c50a326/github/monero/src/serialization/crypto.h:37,
                 from /home/c50a326/github/monero/src/cryptonote_basic/cryptonote_basic.h:44,
                 from /home/c50a326/github/monero/src/cryptonote_basic/cryptonote_basic_impl.h:33,
                 from /home/c50a326/github/monero/src/cryptonote_core/tx_pool.h:44,
                 from /home/c50a326/github/monero/src/cryptonote_core/tx_pool.cpp:36:
/home/c50a326/github/monero/src/crypto/chacha.h: In function ‘void crypto::generate_chacha_key(const void*, size_t, crypto::chacha_key&)’:
/home/c50a326/github/monero/src/crypto/chacha.h:76:46: error: ‘void* memcpy(void*, const void*, size_t)’ writing to an object of non-trivially copyable type ‘using chacha_key = tools::scrubbed_arr<unsigned char, 32>’ {aka ‘struct tools::scrubbed<std::array<unsigned char, 32> >’}; use copy-assignment or copy-initialization instead [-Werror=class-memaccess]
     memcpy(&key, pwd_hash.data(), sizeof(key));
                                              ^
In file included from /home/c50a326/github/monero/contrib/epee/include/string_tools.h:48,
                 from /home/c50a326/github/monero/src/cryptonote_core/tx_pool.h:41,
                 from /home/c50a326/github/monero/src/cryptonote_core/tx_pool.cpp:36:
/home/c50a326/github/monero/contrib/epee/include/memwipe.h:53:10: note: ‘using chacha_key = tools::scrubbed_arr<unsigned char, 32>’ {aka ‘struct tools::scrubbed<std::array<unsigned char, 32> >’} declared here
   struct scrubbed : public T {
          ^~~~~~~~
In file included from /home/c50a326/github/monero/src/serialization/crypto.h:37,
                 from /home/c50a326/github/monero/src/cryptonote_basic/cryptonote_basic.h:44,
                 from /home/c50a326/github/monero/src/cryptonote_basic/cryptonote_basic_impl.h:33,
                 from /home/c50a326/github/monero/src/cryptonote_core/tx_pool.h:44,
                 from /home/c50a326/github/monero/src/cryptonote_core/tx_pool.cpp:36:
/home/c50a326/github/monero/src/crypto/chacha.h: In function ‘void crypto::generate_chacha_key_prehashed(const void*, size_t, crypto::chacha_key&)’:
/home/c50a326/github/monero/src/crypto/chacha.h:83:46: error: ‘void* memcpy(void*, const void*, size_t)’ writing to an object of non-trivially copyable type ‘using chacha_key = tools::scrubbed_arr<unsigned char, 32>’ {aka ‘struct tools::scrubbed<std::array<unsigned char, 32> >’}; use copy-assignment or copy-initialization instead [-Werror=class-memaccess]
     memcpy(&key, pwd_hash.data(), sizeof(key));
                                              ^
In file included from /home/c50a326/github/monero/contrib/epee/include/string_tools.h:48,
                 from /home/c50a326/github/monero/src/cryptonote_core/tx_pool.h:41,
                 from /home/c50a326/github/monero/src/cryptonote_core/tx_pool.cpp:36:
/home/c50a326/github/monero/contrib/epee/include/memwipe.h:53:10: note: ‘using chacha_key = tools::scrubbed_arr<unsigned char, 32>’ {aka ‘struct tools::scrubbed<std::array<unsigned char, 32> >’} declared here
   struct scrubbed : public T {
          ^~~~~~~~
In file included from /home/c50a326/github/monero/src/serialization/crypto.h:37,
                 from /home/c50a326/github/monero/src/cryptonote_basic/cryptonote_basic.h:44,
                 from /home/c50a326/github/monero/src/cryptonote_basic/cryptonote_basic_impl.h:33,
                 from /home/c50a326/github/monero/src/cryptonote_basic/cryptonote_format_utils.h:33,
                 from /home/c50a326/github/monero/src/cryptonote_core/cryptonote_tx_utils.h:32,
                 from /home/c50a326/github/monero/src/cryptonote_core/cryptonote_tx_utils.cpp:37:
/home/c50a326/github/monero/src/crypto/chacha.h: In function ‘void crypto::generate_chacha_key(const void*, size_t, crypto::chacha_key&)’:
/home/c50a326/github/monero/src/crypto/chacha.h:76:46: error: ‘void* memcpy(void*, const void*, size_t)’ writing to an object of non-trivially copyable type ‘using chacha_key = tools::scrubbed_arr<unsigned char, 32>’ {aka ‘struct tools::scrubbed<std::array<unsigned char, 32> >’}; use copy-assignment or copy-initialization instead [-Werror=class-memaccess]
     memcpy(&key, pwd_hash.data(), sizeof(key));
                                              ^
In file included from /home/c50a326/github/monero/contrib/epee/include/string_tools.h:48,
                 from /home/c50a326/github/monero/src/cryptonote_core/cryptonote_tx_utils.cpp:33:
/home/c50a326/github/monero/contrib/epee/include/memwipe.h:53:10: note: ‘using chacha_key = tools::scrubbed_arr<unsigned char, 32>’ {aka ‘struct tools::scrubbed<std::array<unsigned char, 32> >’} declared here
   struct scrubbed : public T {
          ^~~~~~~~
In file included from /home/c50a326/github/monero/src/serialization/crypto.h:37,
                 from /home/c50a326/github/monero/src/cryptonote_basic/cryptonote_basic.h:44,
                 from /home/c50a326/github/monero/src/cryptonote_basic/cryptonote_basic_impl.h:33,
                 from /home/c50a326/github/monero/src/cryptonote_basic/cryptonote_format_utils.h:33,
                 from /home/c50a326/github/monero/src/cryptonote_core/cryptonote_tx_utils.h:32,
                 from /home/c50a326/github/monero/src/cryptonote_core/cryptonote_tx_utils.cpp:37:
/home/c50a326/github/monero/src/crypto/chacha.h: In function ‘void crypto::generate_chacha_key_prehashed(const void*, size_t, crypto::chacha_key&)’:
/home/c50a326/github/monero/src/crypto/chacha.h:83:46: error: ‘void* memcpy(void*, const void*, size_t)’ writing to an object of non-trivially copyable type ‘using chacha_key = tools::scrubbed_arr<unsigned char, 32>’ {aka ‘struct tools::scrubbed<std::array<unsigned char, 32> >’}; use copy-assignment or copy-initialization instead [-Werror=class-memaccess]
     memcpy(&key, pwd_hash.data(), sizeof(key));
                                              ^
In file included from /home/c50a326/github/monero/contrib/epee/include/string_tools.h:48,
                 from /home/c50a326/github/monero/src/cryptonote_core/cryptonote_tx_utils.cpp:33:
/home/c50a326/github/monero/contrib/epee/include/memwipe.h:53:10: note: ‘using chacha_key = tools::scrubbed_arr<unsigned char, 32>’ {aka ‘struct tools::scrubbed<std::array<unsigned char, 32> >’} declared here
   struct scrubbed : public T {
          ^~~~~~~~
make[3]: Leaving directory '/home/c50a326/github/monero/build/release'
[ 17%] Built target obj_checkpoints
cc1plus: all warnings being treated as errors
make[3]: *** [src/blockchain_db/CMakeFiles/obj_blockchain_db.dir/build.make:76: src/blockchain_db/CMakeFiles/obj_blockchain_db.dir/lmdb/db_lmdb.cpp.o] Error 1
make[3]: Leaving directory '/home/c50a326/github/monero/build/release'
make[2]: *** [CMakeFiles/Makefile2:1469: src/blockchain_db/CMakeFiles/obj_blockchain_db.dir/all] Error 2
cc1plus: all warnings being treated as errors
make[3]: *** [src/cryptonote_core/CMakeFiles/obj_cryptonote_core.dir/build.make:89: src/cryptonote_core/CMakeFiles/obj_cryptonote_core.dir/tx_pool.cpp.o] Error 1
make[3]: *** Waiting for unfinished jobs....
cc1plus: all warnings being treated as errors
make[3]: *** [src/cryptonote_core/CMakeFiles/obj_cryptonote_core.dir/build.make:102: src/cryptonote_core/CMakeFiles/obj_cryptonote_core.dir/cryptonote_tx_utils.cpp.o] Error 1
cc1plus: all warnings being treated as errors
make[3]: *** [src/cryptonote_core/CMakeFiles/obj_cryptonote_core.dir/build.make:76: src/cryptonote_core/CMakeFiles/obj_cryptonote_core.dir/cryptonote_core.cpp.o] Error 1
cc1plus: all warnings being treated as errors
make[3]: *** [src/cryptonote_core/CMakeFiles/obj_cryptonote_core.dir/build.make:63: src/cryptonote_core/CMakeFiles/obj_cryptonote_core.dir/blockchain.cpp.o] Error 1
make[3]: Leaving directory '/home/c50a326/github/monero/build/release'
make[2]: *** [CMakeFiles/Makefile2:1260: src/cryptonote_core/CMakeFiles/obj_cryptonote_core.dir/all] Error 2
make[2]: Leaving directory '/home/c50a326/github/monero/build/release'
make[1]: *** [Makefile:141: all] Error 2
make[1]: Leaving directory '/home/c50a326/github/monero/build/release'
make: *** [Makefile:65: release-all] Error 2
```

# Discussion History
## moneromooo-monero | 2018-05-12T08:37:32+00:00
Does this help ?


```
diff --git a/contrib/epee/include/memwipe.h b/contrib/epee/include/memwipe.h
index 0d8f491..776ed91 100644
--- a/contrib/epee/include/memwipe.h
+++ b/contrib/epee/include/memwipe.h
@@ -65,6 +65,9 @@ namespace tools {
                     "T cannot be auto-scrubbed. T must be trivially destructable.");
       memwipe(this, sizeof(T));
     }
+
+    T* operator&() { return this; }
+    const T* operator&() const { return this; }
   };
 
   template<typename T>
diff --git a/src/device/device_default.cpp b/src/device/device_default.cpp
index 0071f7d..48600cb 100644
--- a/src/device/device_default.cpp
+++ b/src/device/device_default.cpp
@@ -229,7 +229,7 @@ namespace hw {
         }
 
         bool device_default::sc_secret_add(crypto::secret_key &r, const crypto::secret_key &a, const crypto::secret_key &b) {
-            sc_add(&r, &a, &b);
+            sc_add((unsigned char*)&r, (const unsigned char*)&a, (const unsigned char*)&b);
             return true;
         }
 
```

## moneroexamples | 2018-05-12T08:37:52+00:00
Same here. Arch and gcc 8.1.
A workaround is not treating `class-memaccess` warnings as errors:
```
make clean # remove old build
make CXXFLAGS="-Wno-error=class-memaccess" CFLAGS="-Wno-error=class-memaccess"
```

Edit. This works around `class-memaccess`. But there are other issues as well.

## moneroexamples | 2018-05-12T08:48:37+00:00
@moneromooo-monero 

Your patch seems to solve `class-memaccess` problem. 
But there is another one:

```
/home/mwo/monero/src/crypto/crypto.cpp: In static member function ‘static crypto::secret_key crypto::crypto_ops::generate_keys(crypto::public_key&, crypto::secret_key&, const secret_key&, bool)’:
/home/mwo/monero/src/crypto/crypto.cpp:127:17: error: cannot convert ‘crypto::ec_scalar*’ to ‘unsigned char*’
     sc_reduce32(&sec);  // reduce in case second round of keys (sendkeys)
                 ^~~~
In file included from /home/mwo/monero/src/crypto/crypto.cpp:69:
/home/mwo/monero/src/crypto/crypto-ops.h:145:18: note:   initializing argument 1 of ‘void crypto::sc_reduce32(unsigned char*)’
 void sc_reduce32(unsigned char *);
                  ^~~~~~~~~~~~~~~
/home/mwo/monero/src/crypto/crypto.cpp:129:32: error: cannot convert ‘crypto::ec_scalar*’ to ‘const unsigned char*’
     ge_scalarmult_base(&point, &sec);
                                ^~~~
In file included from /home/mwo/monero/src/crypto/crypto.cpp:69:
/home/mwo/monero/src/crypto/crypto-ops.h:118:34: note:   initializing argument 2 of ‘void crypto::ge_scalarmult_base(crypto::ge_p3*, const unsigned char*)’
 void ge_scalarmult_base(ge_p3 *, const unsigned char *);
                                  ^~~~~~~~~~~~~~~~~~~~~
/home/mwo/monero/src/crypto/crypto.cpp: In static member function ‘static bool crypto::crypto_ops::secret_key_to_public_key(const secret_key&, crypto::public_key&)’:
/home/mwo/monero/src/crypto/crypto.cpp:142:18: error: cannot convert ‘const crypto::ec_scalar*’ to ‘const unsigned char*’
     if (sc_check(&sec) != 0) {
                  ^~~~
In file included from /home/mwo/monero/src/crypto/crypto.cpp:69:
/home/mwo/monero/src/crypto/crypto-ops.h:151:14: note:   initializing argument 1 of ‘int crypto::sc_check(const unsigned char*)’
 int sc_check(const unsigned char *);
              ^~~~~~~~~~~~~~~~~~~~~
/home/mwo/monero/src/crypto/crypto.cpp:145:32: error: cannot convert ‘const crypto::ec_scalar*’ to ‘const unsigned char*’
     ge_scalarmult_base(&point, &sec);
                                ^~~~
In file included from /home/mwo/monero/src/crypto/crypto.cpp:69:
/home/mwo/monero/src/crypto/crypto-ops.h:118:34: note:   initializing argument 2 of ‘void crypto::ge_scalarmult_base(crypto::ge_p3*, const unsigned char*)’
 void ge_scalarmult_base(ge_p3 *, const unsigned char *);
                                  ^~~~~~~~~~~~~~~~~~~~~
/home/mwo/monero/src/crypto/crypto.cpp: In static member function ‘static bool crypto::crypto_ops::generate_key_derivation(const crypto::public_key&, const secret_key&, crypto::key_derivation&)’:
/home/mwo/monero/src/crypto/crypto.cpp:158:28: error: cannot convert ‘const crypto::ec_scalar*’ to ‘const unsigned char*’
     ge_scalarmult(&point2, &key2, &point);
                            ^~~~~
In file included from /home/mwo/monero/src/crypto/crypto.cpp:69:
/home/mwo/monero/src/crypto/crypto-ops.h:130:29: note:   initializing argument 2 of ‘void crypto::ge_scalarmult(crypto::ge_p2*, const unsigned char*, const crypto::ge_p3*)’
 void ge_scalarmult(ge_p2 *, const unsigned char *, const ge_p3 *);
                             ^~~~~~~~~~~~~~~~~~~~~
/home/mwo/monero/src/crypto/crypto.cpp: In static member function ‘static void crypto::crypto_ops::derive_secret_key(const crypto::key_derivation&, std::size_t, const secret_key&, crypto::secret_key&)’:
/home/mwo/monero/src/crypto/crypto.cpp:202:12: error: cannot convert ‘crypto::ec_scalar*’ to ‘unsigned char*’
     sc_add(&derived_key, &base, &scalar);
            ^~~~~~~~~~~~
In file included from /home/mwo/monero/src/crypto/crypto.cpp:69:
/home/mwo/monero/src/crypto/crypto-ops.h:146:13: note:   initializing argument 1 of ‘void crypto::sc_add(unsigned char*, const unsigned char*, const unsigned char*)’
 void sc_add(unsigned char *, const unsigned char *, const unsigned char *);
             ^~~~~~~~~~~~~~~
/home/mwo/monero/src/crypto/crypto.cpp: In static member function ‘static void crypto::crypto_ops::generate_signature(const crypto::hash&, const crypto::public_key&, const secret_key&, crypto::signature&)’:
/home/mwo/monero/src/crypto/crypto.cpp:257:31: error: cannot convert ‘const crypto::ec_scalar*’ to ‘const unsigned char*’
     sc_mulsub(&sig.r, &sig.c, &sec, &k);
                               ^~~~
In file included from /home/mwo/monero/src/crypto/crypto.cpp:69:
/home/mwo/monero/src/crypto/crypto-ops.h:148:56: note:   initializing argument 3 of ‘void crypto::sc_mulsub(unsigned char*, const unsigned char*, const unsigned char*, const unsigned char*)’
 void sc_mulsub(unsigned char *, const unsigned char *, const unsigned char *, const unsigned char *);
                                                        ^~~~~~~~~~~~~~~~~~~~~
/home/mwo/monero/src/crypto/crypto.cpp: In static member function ‘static void crypto::crypto_ops::generate_tx_proof(const crypto::hash&, const crypto::public_key&, const crypto::public_key&, const boost::optional<crypto::public_key>&, const crypto::public_key&, const secret_key&, crypto::signature&)’:
/home/mwo/monero/src/crypto/crypto.cpp:350:31: error: cannot convert ‘const crypto::ec_scalar*’ to ‘const unsigned char*’
     sc_mulsub(&sig.r, &sig.c, &r, &k);
                               ^~
In file included from /home/mwo/monero/src/crypto/crypto.cpp:69:
/home/mwo/monero/src/crypto/crypto-ops.h:148:56: note:   initializing argument 3 of ‘void crypto::sc_mulsub(unsigned char*, const unsigned char*, const unsigned char*, const unsigned char*)’
 void sc_mulsub(unsigned char *, const unsigned char *, const unsigned char *, const unsigned char *);
                                                        ^~~~~~~~~~~~~~~~~~~~~
/home/mwo/monero/src/crypto/crypto.cpp: In static member function ‘static void crypto::crypto_ops::generate_key_image(const crypto::public_key&, const secret_key&, crypto::key_image&)’:
/home/mwo/monero/src/crypto/crypto.cpp:454:28: error: cannot convert ‘const crypto::ec_scalar*’ to ‘const unsigned char*’
     ge_scalarmult(&point2, &sec, &point);
                            ^~~~
In file included from /home/mwo/monero/src/crypto/crypto.cpp:69:
/home/mwo/monero/src/crypto/crypto-ops.h:130:29: note:   initializing argument 2 of ‘void crypto::ge_scalarmult(crypto::ge_p2*, const unsigned char*, const crypto::ge_p3*)’
 void ge_scalarmult(ge_p2 *, const unsigned char *, const ge_p3 *);
                             ^~~~~~~~~~~~~~~~~~~~~
/home/mwo/monero/src/crypto/crypto.cpp: In static member function ‘static void crypto::crypto_ops::generate_ring_signature(const crypto::hash&, const crypto::key_image&, const crypto::public_key* const*, std::size_t, const secret_key&, std::size_t, crypto::signature*)’:
/home/mwo/monero/src/crypto/crypto.cpp:533:53: error: cannot convert ‘const crypto::ec_scalar*’ to ‘const unsigned char*’
     sc_mulsub(&sig[sec_index].r, &sig[sec_index].c, &sec, &k);
                                                     ^~~~
In file included from /home/mwo/monero/src/crypto/crypto.cpp:69:
/home/mwo/monero/src/crypto/crypto-ops.h:148:56: note:   initializing argument 3 of ‘void crypto::sc_mulsub(unsigned char*, const unsigned char*, const unsigned char*, const unsigned char*)’
 void sc_mulsub(unsigned char *, const unsigned char *, const unsigned char *, const unsigned char *);
```

## moneromooo-monero | 2018-05-12T08:55:21+00:00
How about this one instead:

```
diff --git a/src/crypto/chacha.h b/src/crypto/chacha.h
index 7a12093..2b3ed80 100644
--- a/src/crypto/chacha.h
+++ b/src/crypto/chacha.h
@@ -73,14 +73,14 @@ namespace crypto {
     static_assert(sizeof(chacha_key) <= sizeof(hash), "Size of hash must be at least that of chacha_key");
     tools::scrubbed_arr<char, HASH_SIZE> pwd_hash;
     crypto::cn_slow_hash(data, size, pwd_hash.data(), 0/*variant*/, 0/*prehashed*/);
-    memcpy(&key, pwd_hash.data(), sizeof(key));
+    memcpy(&unwrap(key), pwd_hash.data(), sizeof(key));
   }
 
   inline void generate_chacha_key_prehashed(const void *data, size_t size, chacha_key& key) {
     static_assert(sizeof(chacha_key) <= sizeof(hash), "Size of hash must be at least that of chacha_key");
     tools::scrubbed_arr<char, HASH_SIZE> pwd_hash;
     crypto::cn_slow_hash(data, size, pwd_hash.data(), 0/*variant*/, 1/*prehashed*/);
-    memcpy(&key, pwd_hash.data(), sizeof(key));
+    memcpy(&unwrap(key), pwd_hash.data(), sizeof(key));
   }
 
   inline void generate_chacha_key(std::string password, chacha_key& key) {
```

## moneroexamples | 2018-05-12T10:00:00+00:00
@moneromooo-monero 

Based on your patches, changes in few other places were also needed. I made this patch:

https://paste.fedoraproject.org/paste/Prk4VBMrSNX1cXrzx8EuEg

With this patch Monero at least compiles, but I don't know if these changes are correct. 

But still have to switch off `class-memaccess` as rapidjson blows up anyway for this reason as well. 



## moneromooo-monero | 2018-05-12T10:17:59+00:00
That looks right. The first patch is unneeded though, the second one was a separate attempt. Please run the unit tests to make sure, Preferably with valgrind.


## moneroexamples | 2018-05-12T10:38:33+00:00
Ok. But I wont be able to do it today though. 

## moneromooo-monero | 2018-05-12T11:09:32+00:00
I've done it on GCC < 8, works fine.

## moneroexamples | 2018-05-13T03:17:19+00:00
I run the test with that patch and one unit test fails

```
Running tests...
Test project /home/mwo/monero/build/release
      Start  1: hash-target
 1/13 Test  #1: hash-target ......................   Passed    0.05 sec
      Start  2: core_tests
 2/13 Test  #2: core_tests .......................   Passed  1908.99 sec
      Start  3: cncrypto
 3/13 Test  #3: cncrypto .........................   Passed    8.60 sec
      Start  4: unit_tests
 4/13 Test  #4: unit_tests .......................***Failed   16.95 sec
      Start  5: difficulty
 5/13 Test  #5: difficulty .......................   Passed    0.02 sec
      Start  6: hash-fast
 6/13 Test  #6: hash-fast ........................   Passed    0.01 sec
      Start  7: hash-slow
 7/13 Test  #7: hash-slow ........................   Passed    0.08 sec
      Start  8: hash-slow-1
 8/13 Test  #8: hash-slow-1 ......................   Passed    0.10 sec
      Start  9: hash-tree
 9/13 Test  #9: hash-tree ........................   Passed    0.01 sec
      Start 10: hash-extra-blake
10/13 Test #10: hash-extra-blake .................   Passed    0.01 sec
      Start 11: hash-extra-groestl
11/13 Test #11: hash-extra-groestl ...............   Passed    0.01 sec
      Start 12: hash-extra-jh
12/13 Test #12: hash-extra-jh ....................   Passed    0.01 sec
      Start 13: hash-extra-skein
13/13 Test #13: hash-extra-skein .................   Passed    0.01 sec

92% tests passed, 1 tests failed out of 13

Total Test time (real) = 1935.37 sec

The following tests FAILED:
	  4 - unit_tests (Failed)
Errors while running CTest
make[1]: *** [Makefile:98: test] Error 8
make[1]: Leaving directory '/home/mwo/monero/build/release'
make: *** [Makefile:61: release-test] Error 2
```


## moneromooo-monero | 2018-05-13T09:42:41+00:00
You can check which one fails by running: build/release/tests/unit_tests/unit_tests.
If it's one of the DNS ones, it can be ignored.

## moneroexamples | 2018-05-14T07:50:42+00:00
@moneromooo-monero 

Quite a few of them fails. Details here

https://paste.fedoraproject.org/paste/fPAx9yAkGur-rfUbOUAK1Q

## moneromooo-monero | 2018-05-14T10:06:05+00:00
Looks like just one, which is the DNS one. It's fine.

## moneroexamples | 2018-05-14T11:02:26+00:00
@moneromooo-monero 

Cool. If you don't mind, later I can prepare pull request with the patch?

## moneromooo-monero | 2018-05-14T13:27:45+00:00
They're already PRed as 3800 and 3801. If you prefer another attribution, feel free to PR a replacement.

## moneroexamples | 2018-05-14T23:55:48+00:00
@moneromooo-monero 

No problem. Its good that the PR to address this issues has already been made.

## anonimal | 2018-05-24T00:58:49+00:00
JFTR: build still fails on gcc 8.1.0 (Arch Linux) against new tag [v0.12.1.0](https://github.com/monero-project/monero/releases/tag/v0.12.1.0):

```
monero/src/cryptonote_basic/account.cpp:160:34: error: ‘void* memset(void*, int, size_t)’ clearing an object of non-trivial type ‘using secret_key = struct tools::scrubbed<crypto::ec_
scalar>’ {aka ‘struct tools::scrubbed<crypto::ec_scalar>’}; use assignment or value-initialization instead [-Werror=class-memaccess]                                                                             
     memset(&fake, 0, sizeof(fake))
```

## moneromooo-monero | 2018-05-24T08:18:51+00:00
https://github.com/monero-project/monero/pull/3851

Please confirm, I don't have GCC 8.1.

## anonimal | 2018-05-24T18:19:50+00:00
Against #3851:

```
Scanning dependencies of target obj_daemon_messages
[ 32%] Building CXX object src/rpc/CMakeFiles/obj_daemon_messages.dir/message.cpp.o
In file included from /home/anonimal/monero/src/rpc/message.h:31,
                 from /home/anonimal/monero/src/rpc/message.cpp:29:
/home/anonimal/monero/external/rapidjson/document.h: In instantiation of ‘void rapidjson::GenericValue<Encoding, Allocator>::SetObjectRaw(rapidjson::GenericValue<Encoding, Allocator>::Member*, rapidjson::SizeType, Allocator&) [with Encoding = rapidjson::UTF8<>; Allocator = rapidjson::MemoryPoolAllocator<>; rapidjson::GenericValue<Encoding, Allocator>::Member = rapidjson::GenericMember<rapidjson::UTF8<>, rapidjson::MemoryPoolAllocator<> >; rapidjson::SizeType = unsigned int]’:
/home/anonimal/monero/external/rapidjson/document.h:2363:9:   required from ‘bool rapidjson::GenericDocument<Encoding, Allocator, StackAllocator>::EndObject(rapidjson::SizeType) [with Encoding = rapidjson::UTF8<>; Allocator = rapidjson::MemoryPoolAllocator<>; StackAllocator = rapidjson::CrtAllocator; rapidjson::SizeType = unsigned int]’
/home/anonimal/monero/external/rapidjson/document.h:1784:50:   required from ‘bool rapidjson::GenericValue<Encoding, Allocator>::Accept(Handler&) const [with Handler = rapidjson::GenericDocument<rapidjson::UTF8<> >; Encoding = rapidjson::UTF8<>; Allocator = rapidjson::MemoryPoolAllocator<>]’
/home/anonimal/monero/external/rapidjson/document.h:2414:13:   required from ‘rapidjson::GenericValue<Encoding, Allocator>::GenericValue(const rapidjson::GenericValue<Encoding, SourceAllocator>&, Allocator&) [with SourceAllocator = rapidjson::MemoryPoolAllocator<>; Encoding = rapidjson::UTF8<>; Allocator = rapidjson::MemoryPoolAllocator<>]’
/home/anonimal/monero/src/rpc/message.cpp:179:50:   required from here
/home/anonimal/monero/external/rapidjson/document.h:1952:24: error: ‘void* memcpy(void*, const void*, size_t)’ writing to an object of type ‘rapidjson::GenericValue<rapidjson::UTF8<> >::Member’ {aka ‘struct rapidjson::GenericMember<rapidjson::UTF8<>, rapidjson::MemoryPoolAllocator<> >’} with no trivial copy-assignment; use copy-assignment instead [-Werror=class-memaccess]
             std::memcpy(m, members, count * sizeof(Member));
             ~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from /home/anonimal/monero/src/rpc/message.h:31,
                 from /home/anonimal/monero/src/rpc/message.cpp:29:
/home/anonimal/monero/external/rapidjson/document.h:71:8: note: ‘rapidjson::GenericValue<rapidjson::UTF8<> >::Member’ {aka ‘struct rapidjson::GenericMember<rapidjson::UTF8<>, rapidjson::MemoryPoolAllocator<> >’} declared here
 struct GenericMember {
        ^~~~~~~~~~~~~
In file included from /home/anonimal/monero/src/rpc/message.h:31,
                 from /home/anonimal/monero/src/rpc/message.cpp:29:
/home/anonimal/monero/external/rapidjson/document.h: In instantiation of ‘void rapidjson::GenericValue<Encoding, Allocator>::SetArrayRaw(rapidjson::GenericValue<Encoding, Allocator>*, rapidjson::SizeType, Allocator&) [with Encoding = rapidjson::UTF8<>; Allocator = rapidjson::MemoryPoolAllocator<>; rapidjson::SizeType = unsigned int]’:
/home/anonimal/monero/external/rapidjson/document.h:2371:9:   required from ‘bool rapidjson::GenericDocument<Encoding, Allocator, StackAllocator>::EndArray(rapidjson::SizeType) [with Encoding = rapidjson::UTF8<>; Allocator = rapidjson::MemoryPoolAllocator<>; StackAllocator = rapidjson::CrtAllocator; rapidjson::SizeType = unsigned int]’
/home/anonimal/monero/external/rapidjson/document.h:1792:49:   required from ‘bool rapidjson::GenericValue<Encoding, Allocator>::Accept(Handler&) const [with Handler = rapidjson::GenericDocument<rapidjson::UTF8<> >; Encoding = rapidjson::UTF8<>; Allocator = rapidjson::MemoryPoolAllocator<>]’
/home/anonimal/monero/external/rapidjson/document.h:2414:13:   required from ‘rapidjson::GenericValue<Encoding, Allocator>::GenericValue(const rapidjson::GenericValue<Encoding, SourceAllocator>&, Allocator&) [with SourceAllocator = rapidjson::MemoryPoolAllocator<>; Encoding = rapidjson::UTF8<>; Allocator = rapidjson::MemoryPoolAllocator<>]’
/home/anonimal/monero/src/rpc/message.cpp:179:50:   required from here
/home/anonimal/monero/external/rapidjson/document.h:1939:24: error: ‘void* memcpy(void*, const void*, size_t)’ writing to an object of type ‘class rapidjson::GenericValue<rapidjson::UTF8<> >’ with no trivial copy-assignment; use copy-assignment or copy-initialization instead [-Werror=class-memaccess]
             std::memcpy(e, values, count * sizeof(GenericValue));
             ~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/home/anonimal/monero/external/rapidjson/document.h:540:7: note: ‘class rapidjson::GenericValue<rapidjson::UTF8<> >’ declared here
 class GenericValue {
       ^~~~~~~~~~~~
cc1plus: all warnings being treated as errors
make[2]: *** [src/rpc/CMakeFiles/obj_daemon_messages.dir/build.make:63: src/rpc/CMakeFiles/obj_daemon_messages.dir/message.cpp.o] Error 1
make[1]: *** [CMakeFiles/Makefile2:1756: src/rpc/CMakeFiles/obj_daemon_messages.dir/all] Error 2
make[1]: *** Waiting for unfinished jobs....
```

## moneromooo-monero | 2018-05-24T20:28:45+00:00
https://github.com/janisozaur/rapidjson/commit/20f8604ee6cd078c1cb2346148c69c0c2c160db2

## anonimal | 2018-05-24T20:38:13+00:00
@moneromooo-monero do we track his repo or https://github.com/Tencent/rapidjson?

## moneromooo-monero | 2018-05-24T21:38:45+00:00
I've no idea.

## anonimal | 2018-05-25T01:58:44+00:00
With the rapidjson patch applied:

```
[100%] Building CXX object src/daemon/CMakeFiles/daemon.dir/rpc_command_executor.cpp.o
/home/anonimal/monero/src/daemon/rpc_command_executor.cpp: In member function ‘bool daemonize::t_rpc_command_executor::print_transaction_pool_stats()’:
/home/anonimal/monero/src/daemon/rpc_command_executor.cpp:976:54: error: ‘void* memset(void*, int, size_t)’ clearing an object of type ‘struct cryptonote::txpool_stats’ with no trivial copy-assignment; use assignment or value-initialization instead [-Werror=class-memaccess]
     memset(&res.pool_stats, 0, sizeof(res.pool_stats));
                                                      ^
In file included from /home/anonimal/monero/src/common/rpc_client.h:35,
                 from /home/anonimal/monero/src/daemon/rpc_command_executor.h:44,
                 from /home/anonimal/monero/src/daemon/rpc_command_executor.cpp:34:
/home/anonimal/monero/src/rpc/core_rpc_server_commands_defs.h:1541:10: note: ‘struct cryptonote::txpool_stats’ declared here
   struct txpool_stats
          ^~~~~~~~~~~~
cc1plus: all warnings being treated as errors
```

## moneromooo-monero | 2018-05-25T10:49:56+00:00
Fixed too. Use -k to get all of them at once.

## moneromooo-monero | 2018-06-20T08:52:46+00:00
All fixed in current master. I'll close if nothing more gets reported soon.

## moneromooo-monero | 2018-09-09T12:17:07+00:00
+resolved

# Action History
- Created by: c50a326 | 2018-05-12T04:14:51+00:00
- Closed at: 2018-09-09T12:24:47+00:00
