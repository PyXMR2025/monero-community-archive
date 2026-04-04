---
title: Building under Solaris aka SunOS (OpenIndiana Hipster 2017.04)
source_url: https://github.com/monero-project/monero/issues/2625
author: acid-jack
assignees: []
labels: []
created_at: '2017-10-10T11:37:23+00:00'
updated_at: '2017-11-14T20:16:29+00:00'
type: issue
status: closed
closed_at: '2017-11-14T20:16:29+00:00'
---

# Original Description
Hello.
I'm trying to build monero under this OS with illumos kernel.
Now I'm stuck at 90% before which I had to do many dirty hacks. Maybe you will merge them to the code later after some reworking. And FYI, I'm not a C-programmer.

0. Preparation.
```
pkg install git cmake gcc-49 pkg-config system/header <don't remember all packages>
wget https://raw.githubusercontent.com/zeromq/cppzmq/master/zmq.hpp -O /usr/include/zmq.hpp
git clone https://github.com/monero-project/monero.git
```

And here are my build iterations of **cd monero && make**

- Iteration 1
Result:
```
make[3]: Entering directory '/root/monero.build/build/release'
[  1%] Building C object external/miniupnpc/CMakeFiles/libminiupnpc-static.dir/igd_desc_parse.c.o
In file included from /usr/include/stdio.h:37:0,
                 from /root/monero.build/external/miniupnpc/igd_desc_parse.c:10:
/usr/include/sys/feature_tests.h:400:2: error: #error "Compiler or options invalid; UNIX 03 and POSIX.1-2001 applications       require the use of c99"
 #error "Compiler or options invalid; UNIX 03 and POSIX.1-2001 applications \
  ^
make[3]: *** [external/miniupnpc/CMakeFiles/libminiupnpc-static.dir/build.make:63: external/miniupnpc/CMakeFiles/libminiupnpc-static.dir/igd_desc_parse.c.o] Error 1
make[3]: Leaving directory '/root/monero.build/build/release'
make[2]: *** [CMakeFiles/Makefile2:150: external/miniupnpc/CMakeFiles/libminiupnpc-static.dir/all] Error 2
make[2]: Leaving directory '/root/monero.build/build/release'
make[1]: *** [Makefile:141: all] Error 2
make[1]: Leaving directory '/root/monero.build/build/release'
make: *** [Makefile:63: release-all] Error 2
```
Solution:
Add next code in file external/miniupnpc/CMakeLists.txt in block `if (NOT WIN32)` line 35
```
  if (CMAKE_SYSTEM_NAME MATCHES "(SunOS|Solaris)")
    add_definitions (-D__EXTENSIONS__ -std=c99)
  endif ()
```

- Iterarion 2
Result:
```
[  5%] Building C object external/unbound/CMakeFiles/unbound.dir/services/cache/dns.c.o
In file included from /root/monero.build/build/release/external/unbound/config.h:1173:0,
                 from /root/monero.build/external/unbound/services/cache/dns.c:41:
/root/monero.build/external/unbound/compat/fake-rfc2553.h:52:0: warning: "_SS_MAXSIZE" redefined
 # define _SS_MAXSIZE 128 /* Implementation specific max size */
 ^
In file included from /usr/include/sys/socket.h:48:0,
                 from /root/monero.build/build/release/external/unbound/config.h:918,
                 from /root/monero.build/external/unbound/services/cache/dns.c:41:
/usr/include/sys/socket_impl.h:70:0: note: this is the location of the previous definition
 #define _SS_MAXSIZE 256 /* Implementation specific max size */
 ^
In file included from /root/monero.build/build/release/external/unbound/config.h:1173:0,
                 from /root/monero.build/external/unbound/services/cache/dns.c:41:
/root/monero.build/external/unbound/compat/fake-rfc2553.h:54:8: error: redefinition of ‘struct sockaddr_storage’
 struct sockaddr_storage {
        ^
In file included from /usr/include/sys/socket.h:48:0,
                 from /root/monero.build/build/release/external/unbound/config.h:918,
                 from /root/monero.build/external/unbound/services/cache/dns.c:41:
/usr/include/sys/socket_impl.h:96:8: note: originally defined here
 struct sockaddr_storage {
        ^
In file included from /usr/include/sys/socket.h:48:0,
                 from /root/monero.build/build/release/external/unbound/config.h:918,
                 from /root/monero.build/external/unbound/services/cache/dns.c:41:
/usr/include/sys/socket_impl.h:96:8: note: originally defined here
 struct sockaddr_storage {
        ^
In file included from /root/monero.build/build/release/external/unbound/config.h:1173:0,
                 from /root/monero.build/external/unbound/services/cache/dns.c:41:
/root/monero.build/external/unbound/compat/fake-rfc2553.h:68:8: error: redefinition of ‘struct in6_addr’
 struct in6_addr {
        ^
In file included from /usr/include/sys/socket.h:53:0,
                 from /root/monero.build/build/release/external/unbound/config.h:918,
                 from /root/monero.build/external/unbound/services/cache/dns.c:41:
/usr/include/netinet/in.h:105:8: note: originally defined here
 struct in6_addr {
        ^
/root/monero.build/external/unbound/compat/fake-rfc2553.h:69:10: error: expected ‘:’, ‘,’, ‘;’, ‘}’ or ‘__attribute__’ before ‘.’ toke
n
  uint8_t s6_addr[16];
          ^
In file included from /root/monero.build/build/release/external/unbound/config.h:1173:0,
                 from /root/monero.build/external/unbound/services/cache/dns.c:41:
/root/monero.build/external/unbound/compat/fake-rfc2553.h:74:8: error: redefinition of ‘struct sockaddr_in6’
 struct sockaddr_in6 {
        ^
In file included from /usr/include/sys/socket.h:53:0,
                 from /root/monero.build/build/release/external/unbound/config.h:918,
                 from /root/monero.build/external/unbound/services/cache/dns.c:41:
/usr/include/netinet/in.h:419:8: note: originally defined here
 struct sockaddr_in6 {
        ^
In file included from /root/monero.build/build/release/external/unbound/config.h:1173:0,
                 from /root/monero.build/external/unbound/services/cache/dns.c:41:
/root/monero.build/external/unbound/compat/fake-rfc2553.h:136:8: error: redefinition of ‘struct addrinfo’
 struct addrinfo {
        ^
In file included from /root/monero.build/external/unbound/compat/fake-rfc2553.h:45:0,
                 from /root/monero.build/build/release/external/unbound/config.h:1173,
                 from /root/monero.build/external/unbound/services/cache/dns.c:41:
/usr/include/netdb.h:112:8: note: originally defined here
 struct addrinfo {
        ^
*** Error code 1
The following command caused the error:
cd /root/monero.build/build/release/external/unbound && /usr/bin/gcc -DAUTO_INITIALIZE_EASYLOGGINGPP -DBLOCKCHAIN_DB=DB_LMDB -DDEFAULT
_DB_TYPE=\"lmdb\" -DPER_BLOCK_CHECKPOINT -D_GNU_SOURCE -I/root/monero.build/external/easylogging++ -I/root/monero.build/src -I/root/mo
nero.build/contrib/epee/include -I/root/monero.build/external -I/root/monero.build/external/unbound -I/root/monero.build/build/release
/external/unbound -DNDEBUG -Ofast -o CMakeFiles/unbound.dir/services/cache/dns.c.o   -c /root/monero.build/external/unbound/services/c
ache/dns.c
<EXCLUDED>
```
Problem in redefinition of structures sockaddr_storage, in6_addr, sockaddr_in6 and addrinfo in external/unbound/compat/fake-rfc2553.h after system headers in /usr/include. I studied structures in fake-rfc2553.h and decided to exclude them at all.
So I commented out next code in `external/unbound/config.h.cmake.in`:
```
#ifndef HAVE_GETADDRINFO
struct sockaddr_storage;
#include "compat/fake-rfc2553.h"
#endif
```
and next code in `external/unbound/CMakeLists.txt`:
```
if (NOT HAVE_GETADDRINFO)
  list(APPEND compat_src
    compat/fake-rfc2553.c)
endif ()
```
- Iteration 3
Result:
```
[ 30%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/chacha8.c.o
In file included from /root/monero.build/src/common/int-util.h:33:0,
                 from /root/monero.build/src/crypto/chacha8.c:12:
/root/monero.build/src/common/int-util.h:206:1: error: static assertion failed: "BYTE_ORDER is undefined. Perhaps, GNU extensions are
not enabled"
 static_assert(false, "BYTE_ORDER is undefined. Perhaps, GNU extensions are not enabled");
 ^
In file included from /root/monero.build/src/crypto/chacha8.c:12:0:
/root/monero.build/src/common/int-util.h:209:5: warning: "BYTE_ORDER" is not defined [-Wundef]
 #if BYTE_ORDER == LITTLE_ENDIAN
     ^
<SIMILAR ERRORS EXCLUDED>
cc1: all warnings being treated as errors
*** Error code 1
The following command caused the error:
cd /root/monero.build/build/release/src/crypto && /usr/bin/gcc -DAUTO_INITIALIZE_EASYLOGGINGPP -DBLOCKCHAIN_DB=DB_LMDB -DDEFAULT_DB_TY
PE=\"lmdb\" -DMINIUPNP_STATICLIB -DPER_BLOCK_CHECKPOINT -DSTATICLIB -DUPNP_STATIC -I/root/monero.build/external/easylogging++ -I/root/
monero.build/src -I/root/monero.build/contrib/epee/include -I/root/monero.build/external -I/root/monero.build/external/unbound/libunbo
und -I/root/monero.build/external/db_drivers/liblmdb -fno-strict-aliasing -maes -std=c11 -D_GNU_SOURCE   -Wall -Wextra -Wpointer-arith
 -Wundef -Wvla -Wwrite-strings -Wno-error=extra -Wno-error=deprecated-declarations -Wno-unused-parameter -Wno-unused-variable -Wno-err
or=unused-variable -Wno-error=undef -Wno-error=uninitialized -Wlogical-op -Wno-error=maybe-uninitialized -Wno-error=cpp -Waggregate-re
turn -Wnested-externs -Wold-style-definition -Wstrict-prototypes -march=x86-64   -fno-strict-aliasing -DNDEBUG -Ofast    -Werror -o CM
akeFiles/obj_cncrypto.dir/chacha8.c.o   -c /root/monero.build/src/crypto/chacha8.c
make: Fatal error: Command failed for target `src/crypto/CMakeFiles/obj_cncrypto.dir/chacha8.c.o'
Current working directory /root/monero.build/build/release
*** Error code 1
The following command caused the error:
make -f src/crypto/CMakeFiles/obj_cncrypto.dir/build.make src/crypto/CMakeFiles/obj_cncrypto.dir/build
make: Fatal error: Command failed for target `src/crypto/CMakeFiles/obj_cncrypto.dir/all'
<EXCLUDED>
```
Solution:
add next code in `src/common/int-util.h` before `#if defined(__ANDROID__)` line 39:
```
#if defined(__sun) && defined(__SVR4)
#include <endian.h>
#endif
```
- Iteration 4
Result:
```
[ 30%] Building CXX object src/crypto/CMakeFiles/obj_cncrypto.dir/crypto.cpp.o
In file included from /usr/include/boost/thread/detail/platform.hpp:17:0,
                 from /usr/include/boost/thread/mutex.hpp:12,
                 from /root/monero.build/src/crypto/crypto.cpp:37:
/usr/include/boost/config/requires_threads.hpp:47:5: error: #error "Compiler threading support is not turned on. Please set the correc
t command line options for threading: -pthread (Linux), -pthreads (Solaris) or -mthreads (Mingw32)"
 #   error "Compiler threading support is not turned on. Please set the correct command line options for threading: -pthread (Linux),
-pthreads (Solaris) or -mthreads (Mingw32)"
     ^
<EXCLUDED>
*** Error code 1
The following command caused the error:
cd /root/monero.build/build/release/src/crypto && /usr/bin/c++  -DAUTO_INITIALIZE_EASYLOGGINGPP -DBLOCKCHAIN_DB=DB_LMDB -DDEFAULT_DB_T
YPE=\"lmdb\" -DMINIUPNP_STATICLIB -DPER_BLOCK_CHECKPOINT -DSTATICLIB -DUPNP_STATIC -I/root/monero.build/external/easylogging++ -I/root
/monero.build/src -I/root/monero.build/contrib/epee/include -I/root/monero.build/external -I/root/monero.build/external/unbound/libunb
ound -I/root/monero.build/external/db_drivers/liblmdb -DZMQ_STATIC -fno-strict-aliasing -maes -std=c++11 -D_GNU_SOURCE   -Wall -Wextra
 -Wpointer-arith -Wundef -Wvla -Wwrite-strings -Wno-error=extra -Wno-error=deprecated-declarations -Wno-unused-parameter -Wno-unused-v
ariable -Wno-error=unused-variable -Wno-error=undef -Wno-error=uninitialized -Wlogical-op -Wno-error=maybe-uninitialized -Wno-error=cp
p -Wno-reorder -Wno-missing-field-initializers -march=x86-64   -fno-strict-aliasing -DNDEBUG -Ofast    -Werror -o CMakeFiles/obj_cncry
pto.dir/crypto.cpp.o -c /root/monero.build/src/crypto/crypto.cpp
make: Fatal error: Command failed for target `src/crypto/CMakeFiles/obj_cncrypto.dir/crypto.cpp.o'
<EXCLUDED>
```
Solution:
add next code in `monero/CMakeLists.txt` before `if (UNIX AND NOT APPLE)` line 323:
```
if (CMAKE_SYSTEM_NAME MATCHES "(SunOS|Solaris)")
  set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -pthreads")
endif ()
```
- Iteration 5
Result:
```
[ 34%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/random.c.o
/root/monero.build/src/crypto/random.c:99:1: error: destructor priorities are not supported
 FINALIZER(deinit_random) {
 ^
/root/monero.build/src/crypto/random.c:107:1: error: constructor priorities are not supported
 INITIALIZER(init_random) {
 ^
*** Error code 1
The following command caused the error:
cd /root/monero.build/build/release/src/crypto && /usr/bin/gcc -DAUTO_INITIALIZE_EASYLOGGINGPP -DBLOCKCHAIN_DB=DB_LMDB -DDEFAULT_DB_TYPE=\"lmdb\" -DMINIUPNP_STATICLIB -DPER_BLOCK_CHECKPOINT -DSTATICLIB -DUPNP_STATIC -I/root/monero.build/external/easylogging++ -I/root/monero.build/src -I/root/monero.build/contrib/epee/include -I/root/monero.build/external -I/root/monero.build/external/unbound/libunbound -I/root/monero.build/external/db_drivers/liblmdb -fno-strict-aliasing -maes -std=c11 -D_GNU_SOURCE   -Wall -Wextra -Wpointer-arith -Wundef -Wvla -Wwrite-strings -Wno-error=extra -Wno-error=deprecated-declarations -Wno-unused-parameter -Wno-unused-variable -Wno-error=unused-variable -Wno-error=undef -Wno-error=uninitialized -Wlogical-op -Wno-error=maybe-uninitialized -Wno-error=cpp -Waggregate-return -Wnested-externs -Wold-style-definition -Wstrict-prototypes -march=x86-64   -fno-strict-aliasing -DNDEBUG -Ofast    -Werror -o CMakeFiles/obj_cncrypto.dir/random.c.o   -c /root/monero.build/src/crypto/random.c
make: Fatal error: Command failed for target `src/crypto/CMakeFiles/obj_cncrypto.dir/random.c.o'
```
Solution (found on https://github.com/xianyi/OpenBLAS/issues/700):
remove `(101)` in `src/crypto/initializer.h` lines 35 and 36.
I understand that it's a dirty hack but I don't know how to write else..if there. Need a better solution.
- Iteration 6
Result:
```
[ 39%] Building CXX object src/common/CMakeFiles/obj_common.dir/util.cpp.o
/root/monero.build/src/common/util.cpp: In function ‘std::string tools::get_nix_version_display_string()’:
/root/monero.build/src/common/util.cpp:404:11: error: expected ‘;’ before ‘un’
   utsname un;
           ^
/root/monero.build/src/common/util.cpp:404:13: error: statement has no effect [-Werror=unused-value]
   utsname un;
             ^
/root/monero.build/src/common/util.cpp:406:13: error: ‘un’ was not declared in this scope
   if(uname(&un) < 0)
             ^
/root/monero.build/src/common/util.cpp:408:26: error: ‘un’ was not declared in this scope
   return std::string() + un.sysname + " " + un.version + " " + un.release;
                          ^
/root/monero.build/src/common/util.cpp:409:1: error: control reaches end of non-void function [-Werror=return-type]
 }
 ^
cc1plus: all warnings being treated as errors
*** Error code 1
The following command caused the error:
cd /root/monero.build/build/release/src/common && /usr/bin/c++  -DAUTO_INITIALIZE_EASYLOGGINGPP -DBLOCKCHAIN_DB=DB_LMDB -DDEFAULT_DB_TYPE=\"lmdb\" -DMINIUPNP_STATICLIB -DPER_BLOCK_CHECKPOINT -DSTATICLIB -DUPNP_STATIC -I/root/monero.build/external/easylogging++ -I/root/monero.build/src -I/root/monero.build/contrib/epee/include -I/root/monero.build/external -I/root/monero.build/external/unbound/libunbound -I/root/monero.build/external/db_drivers/liblmdb -DZMQ_STATIC -pthreads -fno-strict-aliasing -maes -std=c++11 -D_GNU_SOURCE   -Wall -Wextra -Wpointer-arith -Wundef -Wvla -Wwrite-strings -Wno-error=extra -Wno-error=deprecated-declarations -Wno-unused-parameter -Wno-unused-variable -Wno-error=unused-variable -Wno-error=undef -Wno-error=uninitialized -Wlogical-op -Wno-error=maybe-uninitialized -Wno-error=cpp -Wno-reorder -Wno-missing-field-initializers -march=x86-64   -fno-strict-aliasing -DNDEBUG -Ofast    -Werror -o CMakeFiles/obj_common.dir/util.cpp.o -c /root/monero.build/src/common/util.cpp
make: Fatal error: Command failed for target `src/common/CMakeFiles/obj_common.dir/util.cpp.o'
```
Solution:
change `   utsname un;` in `src/common/util.cpp` to `   struct utsname un;` line 404.
I don't remember how I came up with this. Dirty hack. Need a better solution.
- Iteration 7
Result:
```
[ 45%] Building CXX object src/cryptonote_core/CMakeFiles/obj_cryptonote_core.dir/blockchain.cpp.o
In file included from /usr/include/boost/asio/detail/socket_types.hpp:81:0,
                 from /usr/include/boost/asio/detail/impl/pipe_select_interrupter.ipp:31,
                 from /usr/include/boost/asio/detail/pipe_select_interrupter.hpp:82,
                 from /usr/include/boost/asio/detail/select_interrupter.hpp:27,
                 from /usr/include/boost/asio/detail/dev_poll_reactor.hpp:31,
                 from /usr/include/boost/asio/detail/reactor.hpp:25,
                 from /usr/include/boost/asio/detail/impl/task_io_service.ipp:24,
                 from /usr/include/boost/asio/detail/task_io_service.hpp:198,
                 from /usr/include/boost/asio/impl/io_service.hpp:71,
                 from /usr/include/boost/asio/io_service.hpp:767,
                 from /root/monero.build/src/cryptonote_core/blockchain.h:32,
                 from /root/monero.build/src/cryptonote_core/blockchain.cpp:39:
/usr/include/net/if.h:97:9: error: template argument required for ‘struct map’
  struct map *if_memmap;  /* rmap for interface specific memory */
         ^
*** Error code 1
The following command caused the error:
cd /root/monero.build/build/release/src/cryptonote_core && /usr/bin/c++  -DAUTO_INITIALIZE_EASYLOGGINGPP -DBLOCKCHAIN_DB=DB_LMDB -DDEFAULT_DB_TYPE=\"lmdb\" -DMINIUPNP_STATICLIB -DPER_BLOCK_CHECKPOINT -DSTATICLIB -DUPNP_STATIC -I/root/monero.build/external/easylogging++ -I/root/monero.build/src -I/root/monero.build/contrib/epee/include -I/root/monero.build/external -I/root/monero.build/external/unbound/libunbound -I/root/monero.build/external/db_drivers/liblmdb -DZMQ_STATIC -pthreads -fno-strict-aliasing -maes -std=c++11 -D_GNU_SOURCE   -Wall -Wextra -Wpointer-arith -Wundef -Wvla -Wwrite-strings -Wno-error=extra -Wno-error=deprecated-declarations -Wno-unused-parameter -Wno-unused-variable -Wno-error=unused-variable -Wno-error=undef -Wno-error=uninitialized -Wlogical-op -Wno-error=maybe-uninitialized -Wno-error=cpp -Wno-reorder -Wno-missing-field-initializers -march=x86-64   -fno-strict-aliasing -DNDEBUG -Ofast    -Werror -o CMakeFiles/obj_cryptonote_core.dir/blockchain.cpp.o -c /root/monero.build/src/cryptonote_core/blockchain.cpp
make: Fatal error: Command failed for target `src/cryptonote_core/CMakeFiles/obj_cryptonote_core.dir/blockchain.cpp.o'
```
Solution:
move `#include "blockchain.h"` in `src/cryptonote_core/blockchain.cpp` higher in the includes (for example to the line 36).
- Iteration 8
Result:
```
[ 46%] Building CXX object src/cryptonote_core/CMakeFiles/obj_cryptonote_core.dir/tx_pool.cpp.o
/usr/include/net/if.h:97:9: error: template argument required for ‘struct map’
  struct map *if_memmap;  /* rmap for interface specific memory */
         ^
```
Solution (same as in previous iteration):
move `#include "blockchain.h"` in `src/cryptonote_core/tx_pool.cpp` higher in the includes) for example to the line 36).
- Iteration 9
Result:
```
[ 48%] Linking CXX static library libblockchain_db.a
[ 48%] Built target blockchain_db
[ 48%] Generating blocks.o
ld: fatal: file binary: open failed: No such file or directory
*** Error code 1
The following command caused the error:
cd /root/monero.build/build/release/src/blocks && cd /root/monero.build/src/blocks && /usr/bin/ld -r -b binary -o /root/monero.build/build/release/src/blocks/blocks.o blocks.dat
make: Fatal error: Command failed for target `src/blocks/blocks.o'
```
Problem is in link editor:
```
# /usr/bin/ld --version
ld: Software Generation Utilities - Solaris Link Editors: 5.11-1.1755 (illumos)
# /usr/gnu/bin/ld --version
GNU ld (GNU Binutils) 2.25.1
Copyright (C) 2014 Free Software Foundation, Inc.
```
In Solaris version option '-b' have other purpose not the binary format as in GNU version. So I fixed this by overriding CMAKE_LINKER in `src/blocks/CMakeLists.txt` line 29:
```
if (CMAKE_SYSTEM_NAME MATCHES "(SunOS|Solaris)")
  set(CMAKE_LINKER "/usr/gnu/bin/ld")
endif ()
```
- Iteration 10
Result:
```
[ 55%] Building CXX object tests/core_tests/CMakeFiles/coretests.dir/block_reward.cpp.o
In file included from /usr/include/boost/asio/detail/socket_types.hpp:81:0,
                 from /usr/include/boost/asio/detail/impl/pipe_select_interrupter.ipp:31,
                 from /usr/include/boost/asio/detail/pipe_select_interrupter.hpp:82,
                 from /usr/include/boost/asio/detail/select_interrupter.hpp:27,
                 from /usr/include/boost/asio/detail/dev_poll_reactor.hpp:31,
                 from /usr/include/boost/asio/detail/reactor.hpp:25,
                 from /usr/include/boost/asio/detail/impl/task_io_service.ipp:24,
                 from /usr/include/boost/asio/detail/task_io_service.hpp:198,
                 from /usr/include/boost/asio/impl/io_service.hpp:71,
                 from /usr/include/boost/asio/io_service.hpp:767,
                 from /root/monero.build/contrib/epee/include/net/net_utils_base.h:32,
                 from /root/monero.build/src/p2p/net_node_common.h:34,
                 from /root/monero.build/src/cryptonote_core/cryptonote_core.h:39,
                 from /root/monero.build/tests/core_tests/chaingen.h:51,
                 from /root/monero.build/tests/core_tests/block_reward.cpp:31:
/usr/include/net/if.h:97:9: error: template argument required for ‘struct map’
  struct map *if_memmap;  /* rmap for interface specific memory */
         ^
```
Again as in iterations 7 and 8. I could not resolve it by moving up header include in various files so I just forgot about tests, removed 'build' dir and from now building with **make release-static**.
- Iteration 11
Result:
```
[ 75%] Building CXX object src/rpc/CMakeFiles/obj_daemon_rpc_server.dir/daemon_handler.cpp.o
In file included from /usr/include/boost/asio/detail/socket_types.hpp:81:0,
                 from /usr/include/boost/asio/detail/impl/pipe_select_interrupter.ipp:31,
                 from /usr/include/boost/asio/detail/pipe_select_interrupter.hpp:82,
                 from /usr/include/boost/asio/detail/select_interrupter.hpp:27,
                 from /usr/include/boost/asio/detail/dev_poll_reactor.hpp:31,
                 from /usr/include/boost/asio/detail/reactor.hpp:25,
                 from /usr/include/boost/asio/detail/impl/task_io_service.ipp:24,
                 from /usr/include/boost/asio/detail/task_io_service.hpp:198,
                 from /usr/include/boost/asio/impl/io_service.hpp:71,
                 from /usr/include/boost/asio/io_service.hpp:767,
                 from /root/monero.build/contrib/epee/include/net/net_utils_base.h:32,
                 from /root/monero.build/src/p2p/net_node_common.h:34,
                 from /root/monero.build/src/cryptonote_core/cryptonote_core.h:39,
                 from /root/monero.build/src/rpc/daemon_handler.h:34,
                 from /root/monero.build/src/rpc/daemon_handler.cpp:29:
/usr/include/net/if.h:97:9: error: template argument required for ‘struct map’
  struct map *if_memmap;  /* rmap for interface specific memory */
         ^
```
And again...
Solution:
move `#include "cryptonote_core/cryptonote_core.h"` higher in `src/rpc/daemon_handler.h` line 31.
- Iteration 12
Result:
```
[ 84%] Building CXX object src/wallet/CMakeFiles/obj_wallet.dir/wallet2.cpp.o
In file included from /usr/include/boost/asio/detail/socket_types.hpp:81:0,
                 from /usr/include/boost/asio/detail/impl/pipe_select_interrupter.ipp:31,
                 from /usr/include/boost/asio/detail/pipe_select_interrupter.hpp:82,
                 from /usr/include/boost/asio/detail/select_interrupter.hpp:27,
                 from /usr/include/boost/asio/detail/dev_poll_reactor.hpp:31,
                 from /usr/include/boost/asio/detail/reactor.hpp:25,
                 from /usr/include/boost/asio/detail/impl/task_io_service.ipp:24,
                 from /usr/include/boost/asio/detail/task_io_service.hpp:198,
                 from /usr/include/boost/asio/impl/io_service.hpp:71,
                 from /usr/include/boost/asio/io_service.hpp:767,
                 from /usr/include/boost/asio/basic_io_object.hpp:19,
                 from /usr/include/boost/asio/basic_socket.hpp:20,
                 from /usr/include/boost/asio/basic_datagram_socket.hpp:20,
                 from /usr/include/boost/asio.hpp:21,
                 from /root/monero.build/contrib/epee/include/net/net_helper.h:39,
                 from /root/monero.build/contrib/epee/include/net/http_client.h:40,
                 from /root/monero.build/src/wallet/wallet2.h:46,
                 from /root/monero.build/src/wallet/wallet2.cpp:41:
/usr/include/net/if.h:97:9: error: template argument required for ‘struct map’
  struct map *if_memmap;  /* rmap for interface specific memory */
         ^
```
Same problem...
Solution:
this time move `#include "net/http_client.h"` higher in `src/wallet/wallet2.h` line 35.
- Iteration 13
For now it is my last iteration in which I completely stuck.
Result:
```
[ 90%] Linking CXX executable ../../bin/monero-wallet-rpc
Undefined                       first referenced
 symbol                             in file
bind                                ../../external/unbound/libunbound.a(outside_network.c.o)  (symbol belongs to implicit dependency /lib/libsocket.so.1)
recv                                ../../external/unbound/libunbound.a(netevent.c.o)  (symbol belongs to implicit dependency /lib/libsocket.so.1)
send                                ../../external/unbound/libunbound.a(netevent.c.o)  (symbol belongs to implicit dependency /lib/libsocket.so.1)
__xnet_connect                      CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o  (symbol belongs to implicit dependency /lib/libsocket.so.1)
getservbyname                       ../../external/unbound/libunbound.a(str2wire.c.o)  (symbol belongs to implicit dependency /lib/libsocket.so.1)
if_indextoname                      CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o  (symbol belongs to implicit dependency /lib/libsocket.so.1)
__xnet_socket                       CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o  (symbol belongs to implicit dependency /lib/libsocket.so.1)
__xnet_getsockopt                   CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o  (symbol belongs to implicit dependency /lib/libsocket.so.1)
getsockname                         CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o  (symbol belongs to implicit dependency /lib/libsocket.so.1)
accept                              CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o  (symbol belongs to implicit dependency /lib/libsocket.so.1)
listen                              CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o  (symbol belongs to implicit dependency /lib/libsocket.so.1)
if_nametoindex                      CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o  (symbol belongs to implicit dependency /lib/libsocket.so.1)
sendto                              ../../external/unbound/libunbound.a(netevent.c.o)  (symbol belongs to implicit dependency /lib/libsocket.so.1)
socket                              ../../external/unbound/libunbound.a(outside_network.c.o)  (symbol belongs to implicit dependency /lib/libsocket.so.1)
getprotobyname                      ../../external/unbound/libunbound.a(str2wire.c.o)  (symbol belongs to implicit dependency /lib/libsocket.so.1)
getprotobynumber                    ../../external/unbound/libunbound.a(wire2str.c.o)  (symbol belongs to implicit dependency /lib/libsocket.so.1)
setsockopt                          CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o  (symbol belongs to implicit dependency /lib/libsocket.so.1)
getsockopt                          ../../external/unbound/libunbound.a(netevent.c.o)  (symbol belongs to implicit dependency /lib/libsocket.so.1)
connect                             ../../external/unbound/libunbound.a(outside_network.c.o)  (symbol belongs to implicit dependency /lib/libsocket.so.1)
__xnet_getaddrinfo                  CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o  (symbol belongs to implicit dependency /lib/libsocket.so.1)
getaddrinfo                         ../../external/unbound/libunbound.a(listen_dnsport.c.o)  (symbol belongs to implicit dependency /lib/libsocket.so.1)
getpeername                         CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o  (symbol belongs to implicit dependency /lib/libsocket.so.1)
recvfrom                            ../../external/unbound/libunbound.a(netevent.c.o)  (symbol belongs to implicit dependency /lib/libsocket.so.1)
freeaddrinfo                        CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o  (symbol belongs to implicit dependency /lib/libsocket.so.1)
inet_addr                           ../../contrib/epee/src/libepee.a(string_tools.cpp.o)  (symbol belongs to implicit dependency /lib/libnsl.so.1)
inet_pton                           CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o  (symbol belongs to implicit dependency /lib/libnsl.so.1)
inet_ntoa                           ../../contrib/epee/src/libepee.a(string_tools.cpp.o)  (symbol belongs to implicit dependency /lib/libnsl.so.1)
inet_ntop                           CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o  (symbol belongs to implicit dependency /lib/libnsl.so.1)
__xnet_bind                         CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o  (symbol belongs to implicit dependency /lib/libsocket.so.1)
gai_strerror                        ../../external/unbound/libunbound.a(listen_dnsport.c.o)  (symbol belongs to implicit dependency /lib/libsocket.so.1)
__xnet_recvmsg                      CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o  (symbol belongs to implicit dependency /lib/libsocket.so.1)
__xnet_sendmsg                      CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o  (symbol belongs to implicit dependency /lib/libsocket.so.1)
shutdown                            CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o  (symbol belongs to implicit dependency /lib/libsocket.so.1)
ld: fatal: symbol referencing errors. No output written to ../../bin/monero-wallet-rpc
collect2: error: ld returned 1 exit status
*** Error code 1
The following command caused the error:
cd /root/monero.build/build/release/src/wallet && /usr/bin/cmake -E cmake_link_script CMakeFiles/wallet_rpc_server.dir/link.txt --verbose=
make: Fatal error: Command failed for target `bin/monero-wallet-rpc'
Current working directory /root/monero.build/build/release
*** Error code 1
The following command caused the error:
make -f src/wallet/CMakeFiles/wallet_rpc_server.dir/build.make src/wallet/CMakeFiles/wallet_rpc_server.dir/build
make: Fatal error: Command failed for target `src/wallet/CMakeFiles/wallet_rpc_server.dir/all'
Current working directory /root/monero.build/build/release
*** Error code 1
The following command caused the error:
make -f CMakeFiles/Makefile2 all
make: Fatal error: Command failed for target `all'
Current working directory /root/monero.build/build/release
*** Error code 1
make: Fatal error: Command failed for target `release-static'
```
I suspect that problem in my excluded fake-rfc2553 in unbound module. But my brain is blowed up already and I can't invent nothing anymore.

So can anybody help me to move forward or fix my hacks? Perhaps I'm doing wrong something.

# Discussion History
## hyc | 2017-10-10T12:02:16+00:00
On Solaris you must link with `-lsocket`. You might also need `-lnsl`.

## acid-jack | 2017-10-10T12:07:32+00:00
Oh. Yes. Forgot to mention it.
I already tried `LDLIBS="-lsocket -lnsl -lresolv" make release-static` with same result.

## moneromooo-monero | 2017-10-10T12:34:06+00:00
Look in CMakeLists.txt in the root tree, from line 654, and add:
set (EXTRA_LIBRARIES socket nsl resolv)
instead of the set of tests. If that works, we need to detect SunOS there.

Thanks for the detailed report about the other failures.


## acid-jack | 2017-10-10T12:43:29+00:00
Yahoo!
Added in root CMakeLists.txt after DRAGONFLY section:
```
elseif (CMAKE_SYSTEM_NAME MATCHES "(SunOS|Solaris)")
  set (EXTRA_LIBRARIES socket nsl resolv)
```
Now dealing with next error.

## acid-jack | 2017-10-10T12:48:54+00:00
Iteration 14
Result:
```
[ 93%] Generating blocksdat.o
ld: fatal: file binary: open failed: No such file or directory
*** Error code 1
The following command caused the error:
cd /root/monero.build/build/release/src/daemon && cd /root/monero.build/src/daemon && cp ../blocks/checkpoints.dat blocks.dat && /usr/bin/ld -r -b bina
ry -o /root/monero.build/build/release/src/daemon/blocksdat.o blocks.dat && rm -f blocks.dat
make: Fatal error: Command failed for target `src/daemon/blocksdat.o'
```
Solution is the same as in Iteration 9:
override CMAKE_LINKER in `src/daemon/CMakeLists.txt`

## moneromooo-monero | 2017-10-10T12:57:11+00:00
Iteration 2 seems because cmake fails to detect getaddrinfo. Could you check whether this works as a replacement ?

```
diff --git a/external/unbound/configure_checks.cmake b/external/unbound/configure_checks.cmake
index 258f281..69fd269 100644
--- a/external/unbound/configure_checks.cmake
+++ b/external/unbound/configure_checks.cmake
@@ -108,6 +108,9 @@ check_function_exists(writev HAVE_WRITEV)
 check_function_exists(_beginthreadex HAVE__BEGINTHREADEX)
 
 set(getaddrinfo_headers)
+if (HAVE_SYS_SOCKET_H)
+  list(APPEND getaddrinfo_headers "sys/socket.h")
+endif ()
 if (HAVE_NETDB_H)
   list(APPEND getaddrinfo_headers "netdb.h")
 endif ()
```


## acid-jack | 2017-10-10T13:16:38+00:00
Iteration 15
Result:
```
[ 96%] Building CXX object src/blockchain_utilities/CMakeFiles/blockchain_export.dir/blockchain_export.cpp.o
In file included from /usr/include/boost/asio/detail/socket_types.hpp:81:0,
                 from /usr/include/boost/asio/detail/impl/pipe_select_interrupter.ipp:31,
                 from /usr/include/boost/asio/detail/pipe_select_interrupter.hpp:82,
                 from /usr/include/boost/asio/detail/select_interrupter.hpp:27,
                 from /usr/include/boost/asio/detail/dev_poll_reactor.hpp:31,
                 from /usr/include/boost/asio/detail/reactor.hpp:25,
                 from /usr/include/boost/asio/detail/impl/task_io_service.ipp:24,
                 from /usr/include/boost/asio/detail/task_io_service.hpp:198,
                 from /usr/include/boost/asio/impl/io_service.hpp:71,
                 from /usr/include/boost/asio/io_service.hpp:767,
                 from /root/monero.build/src/cryptonote_core/blockchain.h:32,
                 from /root/monero.build/src/blockchain_utilities/bootstrap_file.h:38,
                 from /root/monero.build/src/blockchain_utilities/blockchain_export.cpp:29:
/usr/include/net/if.h:97:9: error: template argument required for ‘struct map’
  struct map *if_memmap;  /* rmap for interface specific memory */
         ^
```
Solution:
put `#include "cryptonote_core/blockchain.h"` in `src/blockchain_utilities/bootstrap_file.h` above the `#include "cryptonote_basic/cryptonote_basic.h"`

## acid-jack | 2017-10-10T13:24:41+00:00
Tried to add `+  list(APPEND getaddrinfo_headers "sys/socket.h")`
Result is same error.

## acid-jack | 2017-10-10T14:23:52+00:00
Iteration 16
Result:
```
[ 97%] Building CXX object src/blockchain_utilities/CMakeFiles/blockchain_export.dir/bootstrap_file.cpp.o
In file included from /usr/include/boost/asio/detail/socket_types.hpp:81:0,
                 from /usr/include/boost/asio/detail/impl/pipe_select_interrupter.ipp:31,
                 from /usr/include/boost/asio/detail/pipe_select_interrupter.hpp:82,
                 from /usr/include/boost/asio/detail/select_interrupter.hpp:27,
                 from /usr/include/boost/asio/detail/dev_poll_reactor.hpp:31,
                 from /usr/include/boost/asio/detail/reactor.hpp:25,
                 from /usr/include/boost/asio/detail/impl/task_io_service.ipp:24,
                 from /usr/include/boost/asio/detail/task_io_service.hpp:198,
                 from /usr/include/boost/asio/impl/io_service.hpp:71,
                 from /usr/include/boost/asio/io_service.hpp:767,
                 from /root/monero.build/src/cryptonote_core/blockchain.h:32,
                 from /root/monero.build/src/blockchain_utilities/bootstrap_file.h:37,
                 from /root/monero.build/src/blockchain_utilities/bootstrap_file.cpp:33:
/usr/include/net/if.h:97:9: error: template argument required for ‘struct map’
  struct map *if_memmap;  /* rmap for interface specific memory */
         ^
```
Solution:
move `#include "bootstrap_file.h"` above `#include "bootstrap_serialization.h"` in `src/blockchain_utilities/bootstrap_file.cpp`

## acid-jack | 2017-10-10T14:26:08+00:00
Iteration 17
Result:
```
[ 97%] Building CXX object src/blockchain_utilities/CMakeFiles/blockchain_export.dir/blocksdat_file.cpp.o
In file included from /usr/include/boost/asio/detail/socket_types.hpp:81:0,
                 from /usr/include/boost/asio/detail/impl/pipe_select_interrupter.ipp:31,
                 from /usr/include/boost/asio/detail/pipe_select_interrupter.hpp:82,
                 from /usr/include/boost/asio/detail/select_interrupter.hpp:27,
                 from /usr/include/boost/asio/detail/dev_poll_reactor.hpp:31,
                 from /usr/include/boost/asio/detail/reactor.hpp:25,
                 from /usr/include/boost/asio/detail/impl/task_io_service.ipp:24,
                 from /usr/include/boost/asio/detail/task_io_service.hpp:198,
                 from /usr/include/boost/asio/impl/io_service.hpp:71,
                 from /usr/include/boost/asio/io_service.hpp:767,
                 from /root/monero.build/src/cryptonote_core/blockchain.h:32,
                 from /root/monero.build/src/blockchain_utilities/blocksdat_file.h:39,
                 from /root/monero.build/src/blockchain_utilities/blocksdat_file.cpp:29:
/usr/include/net/if.h:97:9: error: template argument required for ‘struct map’
  struct map *if_memmap;  /* rmap for interface specific memory */
         ^
```
Solution:
move `#include "cryptonote_core/blockchain.h"` above `#include "cryptonote_basic/cryptonote_basic.h"` in `src/blockchain_utilities/blocksdat_file.h`

## acid-jack | 2017-10-10T14:28:41+00:00
Iteration 18
Result:
```
[ 97%] Linking CXX executable ../../bin/monero-blockchain-export
[ 98%] Built target blockchain_export
[ 98%] Generating blocksdat.o
ld: fatal: file binary: open failed: No such file or directory
*** Error code 1
The following command caused the error:
cd /root/monero.build/build/release/src/blockchain_utilities && cd /root/monero.build/src/blockchain_utilities && cp ../blocks/checkpoints.dat blocks.dat && /usr/bin/ld -r -b binary -o /root/monero.build/build/release/src/blockchain_utilities/blocksdat.o blocks.dat && rm -f blocks.dat
make: Fatal error: Command failed for target `src/blockchain_utilities/blocksdat.o'
```
Solution is the same as in Iteration 9:
override CMAKE_LINKER in `src/blockchain_utilities/CMakeLists.txt`

## acid-jack | 2017-10-10T14:30:43+00:00
Bingo!
```
# ./monerod
2017-10-10 14:29:21.108                1        INFO    global  src/daemon/main.cpp:283 Monero 'Helium Hydra' (v0.11.0.0-86e9de58)
2017-10-10 14:29:21.109                1        INFO    global  src/daemon/protocol.h:55        Initializing cryptonote protocol...
2017-10-10 14:29:21.109                1        INFO    global  src/daemon/protocol.h:60        Cryptonote protocol initialized OK
2017-10-10 14:29:21.110                1        INFO    global  src/daemon/p2p.h:63     Initializing p2p server...
2017-10-10 14:29:25.944                1        INFO    global  src/daemon/p2p.h:68     P2p server initialized OK
2017-10-10 14:29:25.945                1        INFO    global  src/daemon/rpc.h:58     Initializing core rpc server...
2017-10-10 14:29:25.945                1        INFO    global  contrib/epee/include/net/http_server_impl_base.h:70     Binding on 127.0.0.1:18081
2017-10-10 14:29:25.945                1        INFO    global  src/daemon/rpc.h:63     Core rpc server initialized OK on port: 18081
2017-10-10 14:29:25.945                1        INFO    global  src/daemon/core.h:73    Initializing core...
2017-10-10 14:29:25.947                1        INFO    global  src/cryptonote_core/cryptonote_core.cpp:320     Loading blockchain from folder /root/.bitmonero/lmdb ...
2017-10-10 14:29:25.966                1        WARN    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:72   Error attempting to retrieve a hard fork version at height 0 from the db: MDB_NOTFOUND: No matching key/data pair found
2017-10-10 14:29:26.466                1        INFO    global  src/cryptonote_core/cryptonote_core.cpp:418     Loading checkpoints
[1507645766] libunbound[194:0] error: outgoing tcp: connect: No such file or directory for 78.140.142.137
[1507645766] libunbound[194:0] error: serviced_tcp_initiate: failed to send tcp query
2017-10-10 14:29:26.775                1        WARN    net.dns src/common/dns_utils.cpp:492    WARNING: no two valid MoneroPulse DNS checkpoint records were received
2017-10-10 14:29:26.775                1        INFO    global  src/daemon/core.h:78    Core initialized OK
2017-10-10 14:29:26.776                1        INFO    global  src/daemon/rpc.h:68     Starting core rpc server...
2017-10-10 14:29:26.776 [SRV_MAIN]      INFO    global  src/daemon/rpc.h:73     Core rpc server started ok
2017-10-10 14:29:26.778 [SRV_MAIN]      INFO    global  src/daemon/p2p.h:78     Starting p2p net loop...
2017-10-10 14:29:27.787 [P2P9]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1254
**********************************************************************
The daemon will start synchronizing with the network. This may take a long time to complete.

You can set the level of process detailization* through "set_log <level|categories>" command*,
where <level> is between 0 (no details) and 4 (very verbose), or custom category based levels (eg, *:WARNING)

Use the "help" command to see the list of available commands.
**********************************************************************

2017-10-10 14:29:27.840 [P2P9]  WARN    net.dns src/common/dns_utils.cpp:492    WARNING: no two valid MoneroPulse DNS checkpoint records were received
```

## moneromooo-monero | 2017-10-10T14:48:33+00:00
Nice :)

I think I know what causes the error in if.h. Can you apply the last patch in https://github.com/moneromooo-monero/bitmonero/tree/solaris and see if it fixes it, instead of moving the includes around ?


## acid-jack | 2017-10-10T16:43:10+00:00
I cloned solaris branch.
Had to repeat iterations 2, 9, 14 and override CMAKE_LINKER in src/blockchain_utilities.

But now I have a problem with lmdb:
```
2017-10-10 15:46:07.127  [P2P2]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1150    [xx.xxx.xxx.xx:18080 OUT]  Synced 82096/1417686
2017-10-10 15:46:07.162  [P2P2]  INFO    global  src/blockchain_db/lmdb/db_lmdb.cpp:578  [batch] DB resize needed
2017-10-10 15:46:07.378  [P2P2]  WARN    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:72   Failed to set new mapsize: No such device
Segmentation Fault
jack@xxxxxx:~/monero$ ./monerod
2017-10-10 15:57:16.655                    1        INFO    global  src/daemon/main.cpp:283 Monero 'Helium Hydra' (v0.11.0.0-86e9de58)
2017-10-10 15:57:16.655                 1        INFO    global  src/daemon/protocol.h:55        Initializing cryptonote protocol...
2017-10-10 15:57:16.655                 1        INFO    global  src/daemon/protocol.h:60        Cryptonote protocol initialized OK
2017-10-10 15:57:16.656                 1        INFO    global  src/daemon/p2p.h:63     Initializing p2p server...
2017-10-10 15:57:21.470                 1        INFO    global  src/daemon/p2p.h:68     P2p server initialized OK
2017-10-10 15:57:21.470                 1        INFO    global  src/daemon/rpc.h:58     Initializing core rpc server...
2017-10-10 15:57:21.471                 1        INFO    global  contrib/epee/include/net/http_server_impl_base.h:70     Binding on 127.0.0.1:18081
2017-10-10 15:57:21.471                 1        INFO    global  src/daemon/rpc.h:63     Core rpc server initialized OK on port: 18081
2017-10-10 15:57:21.471                 1        INFO    global  src/daemon/core.h:73    Initializing core...
2017-10-10 15:57:21.472                 1        INFO    global  src/cryptonote_core/cryptonote_core.cpp:320     Loading blockchain from folder /home/jack/.bitmonero/lmdb ...
2017-10-10 15:57:21.485                 1        WARN    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:72   Failed to open lmdb environment: Device busy
2017-10-10 15:57:21.502                 1        ERROR   cn      src/cryptonote_core/cryptonote_core.cpp:396     Error opening database: Failed to open lmdb environment: Device busy
2017-10-10 15:57:21.502                 1        INFO    global  src/daemon/rpc.h:90     Deinitializing rpc server...
2017-10-10 15:57:21.519                 1        INFO    global  src/daemon/p2p.h:90     Deinitializing p2p...
2017-10-10 15:57:25.523                 1        INFO    global  src/daemon/core.h:89    Deinitializing core...
2017-10-10 15:57:25.611                 1        ERROR   daemon  src/daemon/core.h:94    Failed to deinitialize core...
2017-10-10 15:57:25.629                 1        INFO    global  src/daemon/protocol.h:77        Stopping cryptonote protocol...
2017-10-10 15:57:25.629                 1        INFO    global  src/daemon/protocol.h:81        Cryptonote protocol stopped successfully
```

New build also have problem with lmdb:
```
2017-10-10 16:40:28.956                 1        WARN    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:73   Failed to open lmdb environment: Device busy
```

## moneromooo-monero | 2017-10-10T16:50:26+00:00
Are you running this on a local hard drive ? mmap can return ENODEV if the underlying FS/HW can't. But then it should have done so earlier. Maybe remapping fails. hyc should have a better idea what could go wrong here.

## acid-jack | 2017-10-10T16:55:27+00:00
Yes. It's a physical local disk.
I tried to remove `~/.bitmonero/lmdb/lock.mdb`
Now error is more interesting:
```
2017-10-10 16:53:45.098                 1        INFO    global  src/cryptonote_core/cryptonote_core.cpp:320     Loading blockchain from folder /home/jack/.bitmonero/lmdb ...
2017-10-10 16:53:45.191                 1        WARN    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:1162 LMDB memory map needs to be resized, doing that now.
2017-10-10 16:53:45.191                 1        WARN    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:73   Failed to set new mapsize: Value too large for defined data type
2017-10-10 16:53:45.216                 1        ERROR   cn      src/cryptonote_core/cryptonote_core.cpp:396     Error opening database: Failed to set new mapsize: Value too large for defined data type
```
data.mdb size is 1.1GB btw

## moneromooo-monero | 2017-10-10T17:26:40+00:00
I pushed the namespace reorg to https://github.com/monero-project/monero/pull/2629

## hyc | 2017-10-10T17:59:56+00:00
> Failed to open lmdb environment: Device busy

Sorry about this, it's a known issue with robust mutexes on Solaris. Was fixed upstream over a year ago and I never merged the patch here. You need https://github.com/LMDB/lmdb/commit/c367c1f69685a4d307acb8cea6945c1d67e1cc7e

I'll PR it here shortly.

## acid-jack | 2017-10-11T08:35:37+00:00
Thnaks for your efforts.
So I applied patch to mdb.c, made new build, removed ~/.bitmonero and received next error:
```
2017-10-11 08:28:42.556  [P2P4]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1150    [xxx.xxx.xxx.xx:18080 OUT]  Synced 82097/1418160
2017-10-11 08:28:42.557  [P2P4]  INFO    global  src/blockchain_db/lmdb/db_lmdb.cpp:579  [batch] DB resize needed
2017-10-11 08:28:42.684  [P2P4]  WARN    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:73   Failed to set new mapsize: No such device
Segmentation Fault (core dumped)
```

UPD: still can't make build without disabling fake-rfc2553
UPD: and still have to redefine CMAKE_LINKER for src/blocks and src/daemon and src/blockchain_utilities

## acid-jack | 2017-10-11T09:27:20+00:00
Tried to build all targets:
```
Scanning dependencies of target performance_tests
[ 71%] Building CXX object tests/performance_tests/CMakeFiles/performance_tests.dir/main.cpp.o
In file included from /home/jack/bitmonero/tests/performance_tests/main.cpp:32:0:
/home/jack/bitmonero/tests/performance_tests/performance_utils.h: In function ‘void set_process_affinity(int)’:
/home/jack/bitmonero/tests/performance_tests/performance_utils.h:53:3: error: ‘cpu_set_t’ was not declared in this scope
   cpu_set_t cpuset;
   ^
/home/jack/bitmonero/tests/performance_tests/performance_utils.h:54:13: error: ‘cpuset’ was not declared in this scope
   CPU_ZERO(&cpuset);
             ^
/home/jack/bitmonero/tests/performance_tests/performance_utils.h:54:19: error: ‘CPU_ZERO’ was not declared in this scope
   CPU_ZERO(&cpuset);
                   ^
/home/jack/bitmonero/tests/performance_tests/performance_utils.h:55:24: error: ‘CPU_SET’ was not declared in this scope
   CPU_SET(core, &cpuset);
                        ^
/home/jack/bitmonero/tests/performance_tests/performance_utils.h:56:12: error: ‘::pthread_setaffinity_np’ has not been declared
   if (0 != ::pthread_setaffinity_np(::pthread_self(), sizeof(cpuset), &cpuset))
            ^
*** Error code 1
make: Fatal error: Command failed for target `tests/performance_tests/CMakeFiles/performance_tests.dir/main.cpp.o'
```

## moneromooo-monero | 2017-10-11T09:57:41+00:00
Is GNU ld installed in /usr/gnu/bin by default ?

## acid-jack | 2017-10-11T10:00:48+00:00
No.
```
$ ld --version
ld: Software Generation Utilities - Solaris Link Editors: 5.11-1.1755 (illumos)
```

## hyc | 2017-10-11T10:05:45+00:00
> Failed to set new mapsize: No such device

Have never seen this before. This means the mmap() call failed, but the error code means that the underlying filesystem doesn't support mmap() at all. Which is weird because if the error code was legit it should have failed at startup/db open time. Not at resize. What filesystem are you using?

## acid-jack | 2017-10-11T10:10:52+00:00
zfs — native Solaris FS

BTW, there was one successful DB resize
```
2017-10-11 10:03:44.435  [P2P4]  INFO    global  src/blockchain_db/lmdb/db_lmdb.cpp:579  [batch] DB resize needed
2017-10-11 10:03:45.281  [P2P4]  INFO    global  src/blockchain_db/lmdb/db_lmdb.cpp:495  LMDB Mapsize increased.  Old: 1024MiB, New: 1536MiB
```
And on the second resize I'm receiving our error `Failed to set new mapsize: No such device`

## moneromooo-monero | 2017-10-11T10:11:04+00:00
Does it work if you omit -b in the ld command line (and use the default Soiaris linker) ?

## hyc | 2017-10-11T10:18:55+00:00
Looks to me like the resize is failing because of the requested size - hitting 2GB. 

## acid-jack | 2017-10-11T10:19:30+00:00
After removing '-b binary' option:
```
[ 71%] Generating blocks.o
ld: fatal: file blocks.dat: unknown file type
ld: fatal: file processing errors. No output written to /home/jack/bitmonero/build/release/src/blocks/blocks.o
```

blocks.dat have 0 size
Solaris linker don't like it.

## acid-jack | 2017-10-11T10:22:09+00:00
Now data.mdb size is 1230188544 bytes.

## hyc | 2017-10-11T10:28:42+00:00
Try using UFS instead and see if it behaves any differently.

## moneromooo-monero | 2017-10-11T10:31:56+00:00
Does the following patch work for getaddrinfo ?

```
diff --git a/external/unbound/configure_checks.cmake b/external/unbound/configure_checks.cmake
index 258f281..85de6a3 100644
--- a/external/unbound/configure_checks.cmake
+++ b/external/unbound/configure_checks.cmake
@@ -114,6 +114,9 @@ endif ()
 if (HAVE_WS2TCPIP_H)
   list(APPEND getaddrinfo_headers "ws2tcpip.h")
 endif ()
+if (CMAKE_SYSTEM_NAME MATCHES "(SunOS|Solaris)")
+  set(CMAKE_REQUIRED_LIBRARIES socket nsl)
+endif ()
 check_symbol_exists(getaddrinfo "${getaddrinfo_headers}" HAVE_GETADDRINFO)
 
 check_function_exists(getaddrinfo HAVE_GETADDRINFO)
```

## acid-jack | 2017-10-11T10:32:37+00:00
I can't create UFS. I have no free disks for experiments.

## acid-jack | 2017-10-11T10:40:20+00:00
```
+if (CMAKE_SYSTEM_NAME MATCHES "(SunOS|Solaris)")
+  set(CMAKE_REQUIRED_LIBRARIES socket nsl)
+endif ()
```
not helps, same redifinition error

## hyc | 2017-10-11T11:06:53+00:00
> LMDB Mapsize increased.  Old: 1024MiB, New: 1536MiB

So it successfully resized to 1.5GB.

> Now data.mdb size is 1230188544 bytes.

The actual file size is not expected to be identical to the map size. The map size is a maximum size, the actual size grows toward it.

> I can't create UFS. I have no free disks for experiments.

Since the resize to 1.5GB succeeded and the next resize attempt failed, I'm assuming your system has a problem with 2GB or larger mmap on ZFS. Probably there's some ZFS parameter you need to tune. Since I don't have any Solaris systems or documentation to check, you're on your own here.

## acid-jack | 2017-10-11T11:11:58+00:00
I don't understand which problem it could be:
```
$ dd if=/dev/zero of=zeroes bs=100M count=40
40+0 records in
40+0 records out
4194304000 bytes transferred in 6.403784 secs (654972775 bytes/sec)

$ dd if=/dev/zero bs=100M count=1>>zeroes
1+0 records in
1+0 records out
104857600 bytes transferred in 0.226117 secs (463731403 bytes/sec)
```

## acid-jack | 2017-10-11T11:55:52+00:00
I found `set(DATABASE memory)` in root CMakeLists.txt
Switched from 'lmdb' to 'memory' and received:
```
-- DATABASE set: memory
CMake Error at CMakeLists.txt:48 (message):
  Invalid database type: memory
```

## moneromooo-monero | 2017-10-11T12:22:21+00:00
lmdb is the only valid type.

## acid-jack | 2017-10-11T12:24:30+00:00
> lmdb is the only valid type.

And I investigated BerkeleyDB right now. So it useless?

## moneromooo-monero | 2017-10-11T12:29:00+00:00
It is obsolete now.

## moneromooo-monero | 2017-10-11T13:06:46+00:00
About the getaddrinfo one, it looks like cmake isn't detecting it, so you'd have to work out why it doesn't do so. It seems to be present and usable, since monerod builds and runs, so it's the test that seems wrong. It could be a missing header (unlikely, Solaris' man page lists the same headers), or a lib (seems to be socket, but we just tried that), or maybe the variables used are the wrong ones.

## acid-jack | 2017-10-11T13:17:53+00:00
Looks like without fake-rfc2553 it works good enought. But main problem is in lmdb now.

## moneromooo-monero | 2017-10-11T13:36:18+00:00
Yes, but ideally it'd be omitted because HAVE_GETADDRINFO is defined. I suppose checking for Solaris/SunOS is an acceptable fallback though.

## acid-jack | 2017-10-12T07:36:34+00:00
lmdb: I enabled --log-level 4 to get more details
Here they are:
```
2017-10-12 07:29:22.749                1        TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:2552 BlockchainLMDB::batch_start
2017-10-12 07:29:22.749                1        TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:554  BlockchainLMDB::check_and_resize_for_batch
2017-10-12 07:29:22.749                1        INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:555  [check_and_resize_for_batch] checking DB size
2017-10-12 07:29:22.749                1        TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:503  BlockchainLMDB::need_resize
2017-10-12 07:29:22.751                1        INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:519  DB map size:     1610612736
2017-10-12 07:29:22.751                1        INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:520  Space used:      1230184448
2017-10-12 07:29:22.751                1        INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:521  Space remaining: 380428288
2017-10-12 07:29:22.752                1        INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:522  Size threshold:  0
2017-10-12 07:29:22.752                1        INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:524  Percent used: 0.7638  Percent threshold: 0.8000
2017-10-12 07:29:22.752                1        INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:543  Threshold met (percent-based)
2017-10-12 07:29:22.752                1        INFO    global  src/blockchain_db/lmdb/db_lmdb.cpp:579  [batch] DB resize needed
2017-10-12 07:29:22.752                1        TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:435  BlockchainLMDB::do_resize
2017-10-12 07:29:22.756                1        WARN    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:73   Failed to set new mapsize: Value too large for defined data type
```
I could give the full log but it's size is 3 MB.

UPD: HA! I found almost the same [issue 402](https://github.com/monero-project/monero/issues/402).
UPD2: my uname -a — `SunOS <my hostname> 5.11 illumos-7c4ab494ff i86pc i386 i86pc Solaris`
Strange. Looks like my system is 32-bit...

## moneromooo-monero | 2017-10-12T08:22:10+00:00
Could you actually retry the library change, but with a clean build, because cmake tends to miscache: remove all CMakeCache.txt in the monero tree first. I've found another project which does essentially the same thing, so it looks like the right way to do it.

```
diff --git a/external/unbound/configure_checks.cmake b/external/unbound/configure_checks.cmake
index 258f281..2acf556 100644
--- a/external/unbound/configure_checks.cmake
+++ b/external/unbound/configure_checks.cmake
@@ -49,6 +49,11 @@ if (WIN32)
     iphlpapi
     ws2_32)
 endif ()
+if (CMAKE_SYSTEM_NAME MATCHES "(SunOS|Solaris)")
+  set(CMAKE_REQUIRED_LIBRARIES
+    socket
+    nsl)
+endif ()
 
 check_function_exists(_beginthreadex HAVE__BEGINTHREADEX)
 check_function_exists(arc4random HAVE_ARC4RANDOM)
```

## acid-jack | 2017-10-12T08:26:15+00:00
Remove all CMakeLists.txt? From all subdirs?

## moneromooo-monero | 2017-10-12T08:30:26+00:00
No. Just the files I mentioned. Keep the CMakeLists.txt, they're needed.

## acid-jack | 2017-10-12T08:32:48+00:00
```
cd build/release && cmake -D STATIC=ON -D ARCH="x86-64" -D BUILD_64=ON -D CMAKE_BUILD_TYPE=release ../.. && make
CMake Error: The source directory "/home/jack/bitmonero" does not appear to contain CMakeLists.txt.
Specify --help for usage, or press the help button on the CMake GUI.
*** Error code 1
make: Fatal error: Command failed for target `release-static'
```

## moneromooo-monero | 2017-10-12T08:34:56+00:00
That looks like you removed CMakeLists.txt ?

## acid-jack | 2017-10-12T08:35:37+00:00
Yes. I renamed root CMakeLists.txt

## moneromooo-monero | 2017-10-12T08:35:57+00:00
Then don't. As I said, keep those, they're needed.

## acid-jack | 2017-10-12T08:37:43+00:00
> remove all CMakeCache.txt in the monero tree first
So what did you mean? Which tree?

## moneromooo-monero | 2017-10-12T08:38:12+00:00
The monero tree. But just the ones named CMakeCache.txt, not CMakeLists.txt.

## acid-jack | 2017-10-12T08:42:07+00:00
In the root of https://github.com/monero-project/monero/ there is only the one CMakeLists.txt

## moneromooo-monero | 2017-10-12T08:42:48+00:00
OK, keep it.

## moneromooo-monero | 2017-10-12T08:50:49+00:00
And I mean look in the whole tree (they'll be in build), not just the root.

## acid-jack | 2017-10-12T08:53:49+00:00
I'm removing complete 'build' folder to make clean build usually.

## moneromooo-monero | 2017-10-12T08:55:07+00:00
OK, that should be (more than) enough.

## acid-jack | 2017-10-12T08:57:47+00:00
```
[  7%] Building C object external/unbound/CMakeFiles/unbound.dir/util/netevent.c.o
/home/jack/bitmonero/external/unbound/util/netevent.c: In function ‘comm_point_send_udp_msg_if’:
/home/jack/bitmonero/external/unbound/util/netevent.c:457:5: error: ‘struct msghdr’ has no member named ‘msg_control’
  msg.msg_control = control;
     ^
/home/jack/bitmonero/external/unbound/util/netevent.c:459:5: error: ‘struct msghdr’ has no member named ‘msg_controllen’
  msg.msg_controllen = sizeof(control);
     ^
/home/jack/bitmonero/external/unbound/util/netevent.c:461:5: error: ‘struct msghdr’ has no member named ‘msg_flags’
  msg.msg_flags = 0;
     ^
/home/jack/bitmonero/external/unbound/util/netevent.c:464:7: warning: assignment makes pointer from integer without a cast
  cmsg = CMSG_FIRSTHDR(&msg);
       ^
/home/jack/bitmonero/external/unbound/util/netevent.c:468:6: error: ‘struct msghdr’ has no member named ‘msg_controllen’
   msg.msg_controllen = CMSG_SPACE(sizeof(struct in_pktinfo));
      ^
/home/jack/bitmonero/external/unbound/util/netevent.c:472:11: warning: passing argument 1 of ‘memmove’ makes pointer from integer with
out a cast
   memmove(CMSG_DATA(cmsg), &r->pktinfo.v4info,
           ^
In file included from /usr/include/string.h:33:0,
                 from /home/jack/bitmonero/build/release/external/unbound/config.h:889,
                 from /home/jack/bitmonero/external/unbound/util/netevent.c:41:
/usr/include/iso/string_iso.h:71:14: note: expected ‘void *’ but argument is of type ‘int’
 extern void *memmove(void *, const void *, size_t);
              ^
/home/jack/bitmonero/external/unbound/util/netevent.c:475:13: warning: assignment makes pointer from integer without a cast
   cmsg_data = CMSG_DATA(cmsg);
             ^
/home/jack/bitmonero/external/unbound/util/netevent.c:492:6: error: ‘struct msghdr’ has no member named ‘msg_controllen’
   msg.msg_controllen = CMSG_SPACE(sizeof(struct in6_pktinfo));
      ^
/home/jack/bitmonero/external/unbound/util/netevent.c:496:11: warning: passing argument 1 of ‘memmove’ makes pointer from integer with
out a cast
   memmove(CMSG_DATA(cmsg), &r->pktinfo.v6info,
           ^
[...]
```
Full log is more longer.

## acid-jack | 2017-10-12T09:01:58+00:00
I'm trying now to build static binary with ARCH="i686" and BUILD_64=OFF.

## moneromooo-monero | 2017-10-12T09:02:21+00:00
That's interesting, it seems to be something that wasn't picked up before, but seems unrelated to getaddrinfo...

## moneromooo-monero | 2017-10-12T09:09:49+00:00
Do you have somehting like:

#if defined(OMITTED__D_XOPEN_SOURCE_600) && !defined(_XOPEN_SOURCE)
#define _XOPEN_SOURCE 600
#endif

in build/the-type-you-used/external/unbound/config.h ?

## acid-jack | 2017-10-12T09:16:12+00:00
Yes. From line 866.

## acid-jack | 2017-10-12T09:39:35+00:00
Looks like 32-bit build works ok now:
```
2017-10-12 09:35:11.392  [P2P9]  INFO    global  src/blockchain_db/lmdb/db_lmdb.cpp:579  [batch] DB resize needed
2017-10-12 09:35:11.392  [P2P9]  INFO    global  src/blockchain_db/lmdb/db_lmdb.cpp:495  LMDB Mapsize increased.  Old: 1536MiB, New: 2048MiB
2017-10-12 09:37:41.896  [P2P9]  INFO    global  src/blockchain_db/lmdb/db_lmdb.cpp:579  [batch] DB resize needed
2017-10-12 09:37:41.896  [P2P9]  INFO    global  src/blockchain_db/lmdb/db_lmdb.cpp:495  LMDB Mapsize increased.  Old: 2048MiB, New: 2784MiB
```
So problem was in `release-static` target. By default it compiles 64-bit binary and my system is something hybrid: 32-bit which can run 64-bit binaries.

## moneromooo-monero | 2017-10-12T13:36:32+00:00
Does that one fix the msg_control one ?

```
diff --git a/external/unbound/CMakeLists.txt b/external/unbound/CMakeLists.txt
index 3dae8b4..c17bbb9 100644
--- a/external/unbound/CMakeLists.txt
+++ b/external/unbound/CMakeLists.txt
@@ -44,7 +44,11 @@ endif ()
 
 set(RETSIGTYPE void)
 
+if(CMAKE_SYSTEM_NAME MATCHES "(SunOS|Solaris)")
+add_definitions(-D_XOPEN_SOURCE=600)
+else()
 add_definitions(-D_GNU_SOURCE)
+endif()
 
 option(USE_ECDSA "Use ECDSA algorithms" ON)
 option(USE_SHA2 "Enable SHA2 support" ON)
```

## acid-jack | 2017-10-12T14:50:14+00:00
Now I have next errors
```
/usr/include/sys/feature_tests.h:400:2: error: #error "Compiler or options invalid; UNIX 03 and POSIX.1-2001 applications       requir
e the use of c99"
 #error "Compiler or options invalid; UNIX 03 and POSIX.1-2001 applications \
  ^
[...]
/home/jack/bitmonero/external/unbound/compat/fake-rfc2553.h:54:8: error: redefinition of ‘struct sockaddr_storage’
 struct sockaddr_storage {
        ^
[...]
```

So we have two modified files: external/unbound/CMakeLists.txt and external/unbound/configure_checks.cmake

## moneromooo-monero | 2017-10-12T14:53:12+00:00
Slightly different:

```
diff --git a/external/unbound/CMakeLists.txt b/external/unbound/CMakeLists.txt
index 3dae8b4..b6855fd 100644
--- a/external/unbound/CMakeLists.txt
+++ b/external/unbound/CMakeLists.txt
@@ -44,7 +44,12 @@ endif ()
 
 set(RETSIGTYPE void)
 
+if(CMAKE_SYSTEM_NAME MATCHES "(SunOS|Solaris)")
+add_definitions(-D_XOPEN_SOURCE=600)
+else()
 add_definitions(-D_GNU_SOURCE)
+endif()
+add_definitions(-std=c99)
 
 option(USE_ECDSA "Use ECDSA algorithms" ON)
 option(USE_SHA2 "Enable SHA2 support" ON)
```

## acid-jack | 2017-10-12T14:56:16+00:00
I changed `add_definitions(-D_XOPEN_SOURCE=600)` to `add_definitions(-D_XOPEN_SOURCE=600 -D__EXTENSIONS__ -std=c99)`
struct msghdr error is gone but struct sockaddr_storage still present.

## moneromooo-monero | 2017-10-12T14:56:24+00:00
I just edited the patch: just one - for -std=c99 (in case you already copied it).

## moneromooo-monero | 2017-10-12T15:02:53+00:00
Right, so it's still not finding getaddrinfo apparently.


## acid-jack | 2017-10-12T16:08:06+00:00
Oh wait. I removed buid/ dir and could make a build!
```
diff --git a/external/unbound/CMakeLists.txt b/external/unbound/CMakeLists.txt
index 3dae8b42..d02b6686 100644
--- a/external/unbound/CMakeLists.txt
+++ b/external/unbound/CMakeLists.txt
@@ -44,7 +44,11 @@ endif ()

 set(RETSIGTYPE void)

-add_definitions(-D_GNU_SOURCE)
+if(CMAKE_SYSTEM_NAME MATCHES "(SunOS|Solaris)")
+add_definitions(-D_XOPEN_SOURCE=600 -D__EXTENSIONS__ -std=c99)
+else()
+ add_definitions(-D_GNU_SOURCE)
+endif()

 option(USE_ECDSA "Use ECDSA algorithms" ON)
 option(USE_SHA2 "Enable SHA2 support" ON)
diff --git a/external/unbound/configure_checks.cmake b/external/unbound/configure_checks.cmake
index 69fd2695..60f33cdf 100644
--- a/external/unbound/configure_checks.cmake
+++ b/external/unbound/configure_checks.cmake
@@ -49,6 +49,11 @@ if (WIN32)
     iphlpapi
     ws2_32)
 endif ()
+if (CMAKE_SYSTEM_NAME MATCHES "(SunOS|Solaris)")
+  set(CMAKE_REQUIRED_LIBRARIES
+    socket
+    nsl)
+endif ()

 check_function_exists(_beginthreadex HAVE__BEGINTHREADEX)
 check_function_exists(arc4random HAVE_ARC4RANDOM)
```

## acid-jack | 2017-10-12T16:13:36+00:00
So here are my modified files:
```
        modified:   Makefile
        modified:   external/unbound/CMakeLists.txt
        modified:   external/unbound/configure_checks.cmake
        modified:   src/blockchain_utilities/CMakeLists.txt
        modified:   src/blocks/CMakeLists.txt
        modified:   src/daemon/CMakeLists.txt
```
In Makefile I changed arch for release-static target. In unbound is our last patch. In src/*/CMakeLists.txt I redefined CMAKE_LINKER.
Not bad!

## hyc | 2017-10-12T17:01:17+00:00
Are you going to send a pull request with your changes?

## acid-jack | 2017-10-12T17:06:34+00:00
> Are you going to send a pull request with your changes?

I don't know how to do it :) All my changes described here in a free form.
I created account specially for this project.

BTW I still can't build tests for release-all target.

## hyc | 2017-10-12T17:07:59+00:00
In that case just do something like
  `git diff > diff.txt`

and attach the diff.txt file here.

## moneromooo-monero | 2017-10-12T17:14:45+00:00
I have it done here fwiw (apart from the linker thing, but since GNU ld isn't installed by default I think it's best left as a "run cmake -DCMAKE_LINKER=/wherever/you/put/it" in the README).

## acid-jack | 2017-10-12T17:17:30+00:00
I agree with moneromooo. Mix of linkers by default is not good idea.

And I have one more problem. After exiting from monerod with Ctrl+C there remains lock.mdb file which prevents next start of monerod. I have to delete it manually.

## moneromooo-monero | 2017-10-13T08:30:43+00:00
Can you check https://github.com/moneromooo-monero/bitmonero/tree/solaris works (ie, I didn't forget anything), modulo the linker change (with instructions in the README.md file) ? Also, what name/email formatting do you want for attribution ?

## acid-jack | 2017-10-13T09:11:34+00:00
At first I think it should be `cmake -DCMAKE_LINKER=/usr/gnu/bin/ld -D CMAKE_BUILD_TYPE=Release ../..` instead of `cmake -DCMAKE_LINKER=/usr/gnu/bin/ld -D CMAKE_BUILD_TYPE=Release ..`.
I mean `../..`

At second still can't build tests
```
[ 73%] Building CXX object tests/core_proxy/CMakeFiles/core_proxy.dir/core_proxy.cpp.o
/usr/include/net/if.h:97:9: error: template argument required for ‘struct map’
  struct map *if_memmap;  /* rmap for interface specific memory */
         ^
```
Now trying to build with BUILD_TESTS=OFF

## moneromooo-monero | 2017-10-13T09:18:02+00:00
Thanks. I guess I forgot to build tests. Will fix.

## acid-jack | 2017-10-13T09:28:12+00:00
I don't know how this works `cmake -DCMAKE_LINKER=/usr/gnu/bin/ld -D CMAKE_BUILD_TYPE=release ../..` but it not works :)
I could not build blocks.o because of `ld: fatal: file binary: open failed: No such file or directory`. So it was Solaris native linker not the GNU one.

## acid-jack | 2017-10-13T11:54:19+00:00
I could make a build with next command:
```
mkdir build/release; cd build/release && cmake -D BUILD_TESTS=OFF -D CMAKE_BUILD_TYPE=release -D CMAKE_LINKER=/usr/gnu/bin/ld ../.. && make
```

Not like in README:
```
        mkdir -p build/release
        cd build/release
        cmake -DCMAKE_LINKER=/path/to/ld -D CMAKE_BUILD_TYPE=Release ..
        cd ../..

Then you can run make as usual.
```

## moneromooo-monero | 2017-10-13T12:01:44+00:00
That's odd, it seems fine here. CMakeCache.txt gets the right linker path. Can you paste the errors you get ? And check what you have in CMakeCache.txt for CMAKE_LINKER.

## acid-jack | 2017-10-13T12:11:31+00:00
Let's start from beginning:
```
~/bitmonero$ cd build/release && cmake -DCMAKE_LINKER=/usr/gnu/bin/ld -D CMAKE_BUILD_TYPE=Release ..
CMake Error: The source directory "/home/jack/bitmonero/build" does not appear to contain CMakeLists.txt.
Specify --help for usage, or press the help button on the CMake GUI.
```

## moneromooo-monero | 2017-10-13T12:19:39+00:00
With ../..

I also fixed the tests in the solaris branch btw. Hopefully. Let me know if more fail.

## acid-jack | 2017-10-13T12:50:20+00:00
Hm, looks like it was my fault.
I completely removed 'build' dir and sucessfully built last version.

## moneromooo-monero | 2017-10-13T13:58:50+00:00
Great, thanks. Let me know how attribution should be given (name/nick, optional email).

## radfish | 2017-10-13T14:07:23+00:00
On Fri, Oct 13, 2017 at 05:11:36AM -0700, acid-jack wrote:
> ~/bitmonero$ cd build/release && cmake -DCMAKE_LINKER=/usr/gnu/bin/ld -D CMAKE_BUILD_TYPE=Release ..
> CMake Error: The source directory "/home/jack/bitmonero/build" does not appear to contain CMakeLists.txt.
> Specify --help for usage, or press the help button on the CMake GUI.

Last argument needs to point to source dir, so if you're inside build/release, you need `../..` at the end.


## acid-jack | 2017-10-13T14:10:19+00:00
> Great, thanks. Let me know how attribution should be given (name/nick, optional email).

Pavel Maryanov <acid[at]jack[dot]kiev[dot]ua>

## moneromooo-monero | 2017-10-13T14:21:14+00:00
PR'd as https://github.com/monero-project/monero/pull/2644, thanks for the help.

## acid-jack | 2017-10-13T14:22:52+00:00
It's great but what about lock.mdb? Should I create new issue?

## moneromooo-monero | 2017-10-13T14:24:13+00:00
Sure. That flie is meant to be around, and it should not prevent monerod from running.

## acid-jack | 2017-10-13T14:25:23+00:00
But if I stops monerod I can't start it later.

## moneromooo-monero | 2017-10-13T14:26:59+00:00
Well, that's why you'd open a new issue, right ?

## acid-jack | 2017-10-13T14:27:57+00:00
Yes. But I'm not sure is it problem of Solaris build or more general issue.
```
2017-10-13 14:28:02.701  [P2P6]  WARN    net.dns src/common/dns_utils.cpp:492    WARNING: no two valid MoneroPulse DNS checkpoint records were received
2017-10-13 14:28:03.020  [P2P3]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:305     [xxx.xx.xxx.xxx:18080 OUT] Sync data returned a new top block candidate: 478216 -> 1419829 [Your node is 941613 blocks (938 days) behind]
SYNCHRONIZATION started
^C2017-10-13 14:28:04.528        [SRV_MAIN]      INFO    global  src/daemon/p2p.h:80     p2p net loop stopped
2017-10-13 14:28:05.040  [SRV_MAIN]      INFO    global  src/daemon/rpc.h:78     Stopping core rpc server...
2017-10-13 14:28:05.040  [SRV_MAIN]      INFO    global  src/daemon/daemon.cpp:184       Node stopped.
2017-10-13 14:28:05.041  [SRV_MAIN]      INFO    global  src/daemon/rpc.h:90     Deinitializing rpc server...
2017-10-13 14:28:05.041  [SRV_MAIN]      INFO    global  src/daemon/p2p.h:90     Deinitializing p2p...
2017-10-13 14:28:09.053  [SRV_MAIN]      INFO    global  src/daemon/core.h:89    Deinitializing core...
2017-10-13 14:28:09.107  [SRV_MAIN]      INFO    global  src/daemon/protocol.h:77        Stopping cryptonote protocol...
2017-10-13 14:28:09.107  [SRV_MAIN]      INFO    global  src/daemon/protocol.h:81        Cryptonote protocol stopped successfully
jack@xxx:~/bitmonero/build/release/bin$ ./monerod
2017-10-13 14:28:12.190                    1        INFO    global  src/daemon/main.cpp:283 Monero 'Helium Hydra' (v0.11.0.0-c1343850)
2017-10-13 14:28:12.190                 1        INFO    global  src/daemon/protocol.h:55        Initializing cryptonote protocol...
2017-10-13 14:28:12.190                 1        INFO    global  src/daemon/protocol.h:60        Cryptonote protocol initialized OK
2017-10-13 14:28:12.191                 1        INFO    global  src/daemon/p2p.h:63     Initializing p2p server...
2017-10-13 14:28:16.528                 1        INFO    global  src/daemon/p2p.h:68     P2p server initialized OK
2017-10-13 14:28:16.532                 1        INFO    global  src/daemon/rpc.h:58     Initializing core rpc server...
2017-10-13 14:28:16.533                 1        INFO    global  contrib/epee/include/net/http_server_impl_base.h:70     Binding on 127.0.0.1:18081
2017-10-13 14:28:16.533                 1        INFO    global  src/daemon/rpc.h:63     Core rpc server initialized OK on port: 18081
2017-10-13 14:28:16.533                 1        INFO    global  src/daemon/core.h:73    Initializing core...
2017-10-13 14:28:16.534                 1        INFO    global  src/cryptonote_core/cryptonote_core.cpp:320     Loading blockchain from folder /home/jack/.bitmonero/lmdb ...
2017-10-13 14:28:16.536                 1        WARN    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:73   Failed to open lmdb environment: Device busy
2017-10-13 14:28:16.537                 1        ERROR   cn      src/cryptonote_core/cryptonote_core.cpp:396     Error opening database: Failed to open lmdb environment: Device busy
2017-10-13 14:28:16.538                 1        INFO    global  src/daemon/rpc.h:90     Deinitializing rpc server...
2017-10-13 14:28:16.538                 1        INFO    global  src/daemon/p2p.h:90     Deinitializing p2p...
2017-10-13 14:28:20.545                 1        INFO    global  src/daemon/core.h:89    Deinitializing core...
2017-10-13 14:28:20.547                 1        ERROR   daemon  src/daemon/core.h:94    Failed to deinitialize core...
2017-10-13 14:28:20.547                 1        INFO    global  src/daemon/protocol.h:77        Stopping cryptonote protocol...
2017-10-13 14:28:20.547                 1        INFO    global  src/daemon/protocol.h:81        Cryptonote protocol stopped successfully
```

## moneromooo-monero | 2017-10-13T14:32:18+00:00
You don't have to know beforehand. You can open a bug with that, note you're running on Solaris, details of arch, OS and filesystem. That is enough. Questions might be asked later, answer them if you can. That's enough.

## acid-jack | 2017-10-13T14:33:11+00:00
OK.
So now issue can be closed.
Big thx for your help.

## moneromooo-monero | 2017-10-13T14:44:04+00:00
I'll close it once the patches are merged.

## acid-jack | 2017-10-13T15:27:22+00:00
Wait. Small clarification.
Don't `cd ../..` after cmake command. make should be started directly in build/release. Otherwise I'm getting 'struct map' error.

## acid-jack | 2017-10-13T16:11:37+00:00
Damn. I don't understand. I again can't make a build.
```
$ git clone -b solaris https://github.com/moneromooo-monero/bitmonero.git
$ mkdir -p build/release; cd build/release && cmake -D CMAKE_LINKER=/usr/gnu/bin/ld -D CMAKE_BUILD_TYPE=release ../.. && cd ../.. && make -j 8

[ 48%] Building CXX object src/cryptonote_core/CMakeFiles/obj_cryptonote_core.dir/blockchain.cpp.o
/usr/include/net/if.h:97:9: error: template argument required for ‘struct map’
  struct map *if_memmap;  /* rmap for interface specific memory */
         ^
```

## moneromooo-monero | 2017-10-13T17:46:34+00:00
Are you using the two PRs ? I had committed the namespace one yesterday already. You need both.

## acid-jack | 2017-10-13T17:52:15+00:00
> Are you using the two PRs ? I had committed the namespace one yesterday already. You need both.

How to get them?
Which git commands?

## moneromooo-monero | 2017-10-13T18:18:55+00:00
git fetch origin pull/2659/head:2629
git fetch origin pull/2644/head:2644
git cherry-pick 2629 2644

## acid-jack | 2017-10-13T18:48:15+00:00
fatal: Couldn't find remote ref pull/2659/head
fatal: Couldn't find remote ref pull/2644/head

## acid-jack | 2017-10-17T17:43:55+00:00
Ufff. At least I understood this magic.
Repo was cloned from https://github.com/moneromooo-monero/bitmonero.git
And PRs was in https://github.com/monero-project/monero.git

That's why `git fetch` doesn't worked.
I changed repo url in .git/config and could fetch these two PRs.

## moneromooo-monero | 2017-11-14T19:43:41+00:00
+resolved

# Action History
- Created by: acid-jack | 2017-10-10T11:37:23+00:00
- Closed at: 2017-11-14T20:16:29+00:00
