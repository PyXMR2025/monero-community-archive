---
title: make fails @fedora 28
source_url: https://github.com/monero-project/monero/issues/4083
author: lejeczek
assignees: []
labels:
- invalid
created_at: '2018-06-29T15:20:45+00:00'
updated_at: '2018-07-12T23:09:00+00:00'
type: issue
status: closed
closed_at: '2018-07-12T23:09:00+00:00'
---

# Original Description
$ make 
mkdir -p build/release
cd build/release && cmake -D BUILD_TESTS=ON -D CMAKE_BUILD_TYPE=release ../.. && make
-- The C compiler identification is GNU 8.1.1
-- The CXX compiler identification is GNU 8.1.1
-- Check for working C compiler: /bin/cc
-- Check for working C compiler: /bin/cc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting C compile features - done
-- Check for working CXX compiler: /bin/c++
-- Check for working CXX compiler: /bin/c++ -- works
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
-- Found OpenSSL: /usr/lib64/libcrypto.so (found version "1.1.0h") 
-- Using OpenSSL include dir at /usr/include
-- Found PkgConfig: /bin/pkg-config (found version "1.4.2") 
-- Checking for module 'libpcsclite'
--   Found libpcsclite, version 1.8.23
-- Found PCSC: /usr/lib64/libpcsclite.so  
-- Looking for memset_s in c
-- Looking for memset_s in c - not found
-- Looking for explicit_bzero in c
-- Looking for explicit_bzero in c - found
-- Looking for strptime
-- Looking for strptime - found
-- Found MiniUPnPc: /usr/include/miniupnpc  
-- Found miniupnpc API version 16
-- Using in-tree miniupnpc
CMake Error at external/CMakeLists.txt:42 (add_subdirectory):
  add_subdirectory given source "miniupnp/miniupnpc" which is not an existing
  directory.


CMake Error at external/CMakeLists.txt:44 (set_property):
  set_property could not find TARGET libminiupnpc-static.  Perhaps it has not
  yet been created.


CMake Error at external/CMakeLists.txt:48 (set_property):
  set_property could not find TARGET libminiupnpc-static.  Perhaps it has not
  yet been created.


-- Looking for libunbound
CMake Error at external/CMakeLists.txt:61 (add_subdirectory):
  The source directory

  ../vol.f2fs/var/lib/lxc/chrome/rootfs/home/gornik/bin/gits/monero/external/unbound

  does not contain a CMakeLists.txt file.


-- Using 64-bit LMDB from source tree
-- Using PCSC include dir at /usr/include/PCSC
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
-- Found Git: /bin/git
-- Found GTest: /usr/lib64/libgtest.so  
Doxygen: graphviz not found - graphs disabled
-- Could NOT find Doxygen (missing: DOXYGEN_EXECUTABLE) 
-- Performing Test HAVE_C11
-- Performing Test HAVE_C11 - Success
-- Configuring incomplete, errors occurred!

Looking into CMakeOutput.log I cannot(not that I'm a programmer) see any errors.
Is not odd the fact that miniupnpc is in the OS and cmake finds it but still uses in-tree one?

regards, L.

# Discussion History
## moneromooo-monero | 2018-06-29T15:48:58+00:00
Did you follow the cloning instructions in the README ?


## kintarowonders | 2018-07-01T00:31:58+00:00
Looks like libminiupnpc has deprecated things this uses, try downgrading.

## moneromooo-monero | 2018-07-01T08:13:02+00:00
I see no evidence of this in the log. Just follow the instructions from the README.

## lejeczek | 2018-07-02T15:59:09+00:00
No much of a help, which part am I not following, more specifically?

## moneromooo-monero | 2018-07-02T17:02:42+00:00
The part about cloning. But if I just tell you the commands, that'll help just this time, so I point to the place you can find out for yourself.

## lejeczek | 2018-07-03T09:31:01+00:00
Okey, when I did "pull" hoping that would update I think I still had (old?) readme which did not mention "clone". I've done fresh clone and make succeeds now.

But now... having boost packages from OS's repo - why monero insists on ignoring them. Is there a "switch" which would tell build process to use local(maybe all if os-available) dependencies?

Now after successful build and I distributed binaries out I get:

/monerod: error while loading shared libraries: libboost_chrono.so.1.66.0: cannot open shared object file: No such file or directory

And Fedoras boost is 1.64.

Many! thanks.


## moneromooo-monero | 2018-07-03T10:15:35+00:00
OK, that's not it. "pull" is OK if you've got a repo already. The important bit I hoped you'd see is submodules (init + update).

For using your own boost, you need to set BOOST_ROOT. And when running, probably LD_LIBRARY_PATH.

## moneromooo-monero | 2018-07-12T23:06:00+00:00
This was user error.

+invalid


# Action History
- Created by: lejeczek | 2018-06-29T15:20:45+00:00
- Closed at: 2018-07-12T23:09:00+00:00
