---
title: 'Compiling on OpenBSD fails in external/unbound '
source_url: https://github.com/monero-project/monero/issues/3746
author: ghost
assignees: []
labels:
- invalid
created_at: '2018-05-02T08:31:25+00:00'
updated_at: '2018-05-04T10:48:52+00:00'
type: issue
status: closed
closed_at: '2018-05-04T10:48:52+00:00'
---

# Original Description
Running OpenBSD 6.3, trying to compile release-v0.12. 

Following the steps outlined here:
https://github.com/monero-project/monero#openbsd--62-1

Compile bombs when it doesn't find a CMakeLists.txt in external/unbound/  ...The entire directory is empty actually - am I missing something here?

Output:

```
testing$ env DEVELOPER_LOCAL_TOOLS=1 BOOST_ROOT=/usr/local make release-static
mkdir -p build/release
cd build/release && cmake -D STATIC=ON -D ARCH="x86-64" -D BUILD_64=ON -D CMAKE_BUILD_TYPE=release ../.. && make
-- The C compiler identification is Clang 5.0.1
-- The CXX compiler identification is Clang 5.0.1
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
-- Found: env DEVELOPER_LOCAL_TOOLS = 1
-- BOOST_IGNORE_SYSTEM_PATHS defaults to ON
-- Could not find DEVELOPER_LIBUNBOUND_OLD in env (not required)
-- Building for a 64-bit system
-- Building internal libraries as static
-- Could not find DATABASE in env (not required unless you want to change database type from default: lmdb)
-- Using LMDB as default DB type
-- looking for liblzma
-- liblzma found
-- Could not find libunwind (missing: LIBUNWIND_INCLUDE_DIR) 
-- Stack trace on exception disabled
-- Looking for pthread.h
-- Looking for pthread.h - found
-- Looking for pthread_create
-- Looking for pthread_create - not found
-- Check if compiler accepts -pthread
-- Check if compiler accepts -pthread - yes
-- Found Threads: TRUE  
-- Found OpenSSL: /usr/lib/libcrypto.a (found version "2.0.0") 
-- Using OpenSSL include dir at /usr/include
-- Found PkgConfig: /usr/bin/pkg-config (found version "0.27.1") 
-- Checking for module 'libpcsclite'
--   
-- Could NOT find PCSC (missing: PCSC_LIBRARY PCSC_INCLUDE_DIR) 
-- Looking for memset_s in c
-- Looking for memset_s in c - not found
-- Looking for explicit_bzero in c
-- Looking for explicit_bzero in c - found
-- Looking for strptime
-- Looking for strptime - found
-- Found MiniUPnPc: /usr/local/include/miniupnpc  
-- Found miniupnpc API version 10
-- Using miniupnpc from local source tree for static build
-- Looking for libunbound
CMake Error at external/CMakeLists.txt:82 (add_subdirectory):
  The source directory

    /home/meow/monero-0.12.0.0/external/unbound

  does not contain a CMakeLists.txt file.


-- Using 64-bit LMDB from source tree
-- Building on amd64 for x86-64
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
-- Looking for -Wl,-z,noexecheap linker flag - found
-- Using C security hardening flags:  -Wformat -Wformat-security -fstack-protector -fstack-protector-strong
-- Using C++ security hardening flags:  -Wformat -Wformat-security -fstack-protector -fstack-protector-strong
-- Using linker security hardening flags:  -pie -Wl,-z,relro -Wl,-z,now -Wl,-z,noexecstack -Wl,-z,noexecheap
-- AES support enabled
-- Found Boost Version: 106400
-- Looking for rl_copy_text
-- Looking for rl_copy_text - not found
-- Looking for rl_filename_completion_function
-- Looking for rl_filename_completion_function - not found
-- Looking for rl_copy_text
-- Looking for rl_copy_text - found
-- Looking for rl_filename_completion_function
-- Looking for rl_filename_completion_function - found
-- Found readline library at: /usr
-- Found Git: /usr/local/bin/git
-- Found Doxygen: /usr/local/bin/doxygen (found version "1.8.14") found components:  doxygen dot 
-- Performing Test HAVE_C11
-- Performing Test HAVE_C11 - Success
-- Configuring incomplete, errors occurred!
See also "/home/meow/monero-0.12.0.0/build/release/CMakeFiles/CMakeOutput.log".
See also "/home/meow/monero-0.12.0.0/build/release/CMakeFiles/CMakeError.log".
*** Error 1 in /home/meow/monero-0.12.0.0 (Makefile:69 'release-static')
```


After some digging I found ticket #2575 and ston1th's work-around on 0.11. So I added  a CMakeLists.txt to external/unbound/ with the code below which seems to get things compiling(yay libreSSL!)...

```
### external/unbound/CMakeLists.txt ###

# determine if we have libressl
check_symbol_exists(LIBRESSL_VERSION_TEXT "openssl/opensslv.h" HAVE_LIBRESSL)
# check if we have found HAVE_DECL_REALLOCARRAY already, so we can safely undefine and redefine it with value 1
if (HAVE_LIBRESSL AND HAVE_DECL_REALLOCARRAY)
  unset(HAVE_DECL_REALLOCARRAY CACHE)
  add_definitions(-DHAVE_DECL_REALLOCARRAY=1)
endif ()
```


It gets further along and then breaks when it can't find the header file for unbound.... 
Error:
```
Scanning dependencies of target obj_common
[ 39%] Building CXX object src/common/CMakeFiles/obj_common.dir/base58.cpp.o
[ 39%] Building CXX object src/common/CMakeFiles/obj_common.dir/command_line.cpp.o
[ 40%] Building CXX object src/common/CMakeFiles/obj_common.dir/dns_utils.cpp.o
/home/meow/monero-0.12.0.0/src/common/dns_utils.cpp:31:10: fatal error: 'unbound.h' file not found
#include "unbound.h"
         ^~~~~~~~~~~
1 error generated.
*** Error 1 in build/release (src/common/CMakeFiles/obj_common.dir/build.make:111 'src/common/CMakeFiles/obj_common.dir/dns_utils.cpp.o': cd...)
*** Error 1 in build/release (CMakeFiles/Makefile2:750 'src/common/CMakeFiles/obj_common.dir/all')
*** Error 1 in build/release (Makefile:141 'all')
*** Error 1 in /home/meow/monero-0.12.0.0 (Makefile:69 'release-static')
```

So I went and dug up the unbound header file from OpenBSD's src for 6.3 and dropped it into src/common/ 

This gets me to an 82% build but then it bombs again at the linker.

```
[ 82%] Linking CXX executable ../../bin/monero-wallet-rpc
/usr/bin/ld: cannot find -lunbound
c++: error: linker command failed with exit code 1 (use -v to see invocation)
*** Error 1 in build/release (src/wallet/CMakeFiles/wallet_rpc_server.dir/build.make:129 'bin/monero-wallet-rpc')
*** Error 1 in build/release (CMakeFiles/Makefile2:2279 'src/wallet/CMakeFiles/wallet_rpc_server.dir/all')
*** Error 1 in build/release (Makefile:141 'all')
*** Error 1 in /home/w0rlds/monero-0.12.0.0 (Makefile:69 'release-static')
```

At this point I don't know where to go...

If it isn't already clear I'm largely shooting in the dark - my C knowledge is fairly limited, I'm just a sysadmin who loves monero. If I've gone down the wrong path
here with manually adding these files let me know.  I've been digging through past issues and I see Dyrcona has submitted patches for Monero specifically related to
OpenBSD's unbound issues, he mentions them in this ticket: https://github.com/monero-project/monero/pull/2249#issuecomment-320477937

Any help or suggestions are much appreciated...

# Discussion History
## moneromooo-monero | 2018-05-02T09:43:25+00:00
git submodule init
git submodule update

(remove what you added there first)


## ghost | 2018-05-04T01:26:00+00:00
feel free to delete this. sorry to bother you guys.

## moneromooo-monero | 2018-05-04T10:44:18+00:00
+invalid

# Action History
- Created by: ghost | 2018-05-02T08:31:25+00:00
- Closed at: 2018-05-04T10:48:52+00:00
