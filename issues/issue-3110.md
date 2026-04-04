---
title: CMake Error
source_url: https://github.com/monero-project/monero/issues/3110
author: mia0x75
assignees: []
labels:
- invalid
created_at: '2018-01-13T11:54:27+00:00'
updated_at: '2024-04-02T10:07:53+00:00'
type: issue
status: closed
closed_at: '2018-06-10T09:32:53+00:00'
---

# Original Description
I met an error during compiling, what does it mean, how I can fix the error? Thanks.
```
CMake Error at src/CMakeLists.txt:90 (add_library):
  OBJECT library "obj_p2p" contains:

    CMakeFiles
    Makefile
    cmake_install.cmake
    CTestTestfile.cmake

  but may contain only headers and sources that compile.
Call Stack (most recent call first):
  src/p2p/CMakeLists.txt:38 (monero_add_library)


CMake Error at src/CMakeLists.txt:90 (add_library):
  OBJECT library "obj_cryptonote_protocol" contains:

    CMakeFiles
    Makefile
    cmake_install.cmake
    CTestTestfile.cmake

  but may contain only headers and sources that compile.
Call Stack (most recent call first):
  src/cryptonote_protocol/CMakeLists.txt:36 (monero_add_library)
```

# Discussion History
## moneromooo-monero | 2018-01-13T16:24:49+00:00
Make sure you're trying on a fresh tree (ie, make clean first). If it still happens with current master, let us know.

## moneromooo-monero | 2018-01-30T09:50:12+00:00
Ping. I'll close as invalid if there's no more activity after a reasonable amount of time.

## moneromooo-monero | 2018-06-10T09:28:27+00:00
+invalid

## fffeergrrrrtrrt | 2024-04-02T10:07:52+00:00
hello me have this problem



`(Tue Apr-4 6:04:34am)-(CPU 25.4%:0:Net 50)-(qqqq:~/Downloads)-(1.9G:78)
> cd monero-master/
(Tue Apr-4 6:04:36am)-(CPU 25.4%:0:Net 49)-(qqqq:~/Downloads/monero-master)-(268K:16)
> ls
./      cmake/              contrib/    Doxyfile   Makefile   tests/
../     CMakeLists_IOS.txt  Dockerfile  external/  README.md  translations/
build/  CMakeLists.txt      docs/       LICENSE    src/       utils/
(Tue Apr-4 6:04:37am)-(CPU 25.4%:0:Net 49)-(qqqq:~/Downloads/monero-master)-(268K:16)
> make
ls: cannot access '.git/config': No such file or directory
fatal: not a git repository (or any of the parent directories): .git
mkdir -p build/release
cd build/release && cmake -D BUILD_TESTS=ON -D CMAKE_BUILD_TYPE=Release ../.. && make
-- CMake version 3.29.0
-- Found usable ccache: /usr/bin/ccache
-- Building without build tag
-- Checking submodules
fatal: not a git repository (or any of the parent directories): .git
fatal: not a git repository (or any of the parent directories): .git
-- Submodule 'external/miniupnp' is up-to-date
fatal: not a git repository (or any of the parent directories): .git
fatal: not a git repository (or any of the parent directories): .git
-- Submodule 'external/rapidjson' is up-to-date
fatal: not a git repository (or any of the parent directories): .git
fatal: not a git repository (or any of the parent directories): .git
-- Submodule 'external/trezor-common' is up-to-date
fatal: not a git repository (or any of the parent directories): .git
fatal: not a git repository (or any of the parent directories): .git
-- Submodule 'external/randomx' is up-to-date
fatal: not a git repository (or any of the parent directories): .git
fatal: not a git repository (or any of the parent directories): .git
-- Submodule 'external/supercop' is up-to-date
-- Could not find DEVELOPER_LOCAL_TOOLS in env (not required)
-- BOOST_IGNORE_SYSTEM_PATHS defaults to OFF
-- Building for a 64-bit system
-- Building internal libraries as static
-- Using LMDB as default DB type
-- Stack trace on exception enabled (using easylogging++)
-- Using OpenSSL include dir at /usr/include
CMake Warning (dev) at /usr/share/cmake/Modules/FindPackageHandleStandardArgs.cmake:438 (message):
  The package name passed to `find_package_handle_standard_args` (MiniUPnPc)
  does not match the name of the calling package (Miniupnpc).  This can lead
  to problems in calling code that expects `find_package` result variables
  (e.g., `_FOUND`) to follow a certain pattern.
Call Stack (most recent call first):
  cmake/FindMiniupnpc.cmake:39 (find_package_handle_standard_args)
  external/CMakeLists.txt:38 (find_package)
This warning is for project developers.  Use -Wno-dev to suppress it.

-- Could NOT find MiniUPnPc (missing: MINIUPNP_INCLUDE_DIR MINIUPNP_LIBRARY) 
-- Using in-tree miniupnpc
CMake Error at external/CMakeLists.txt:42 (add_subdirectory):
  add_subdirectory given source "miniupnp/miniupnpc" which is not an existing
  directory.


CMake Error at external/CMakeLists.txt:43 (set_property):
  set_property could not find TARGET libminiupnpc-static.  Perhaps it has not
  yet been created.


CMake Error at external/CMakeLists.txt:44 (set_property):
  set_property could not find TARGET libminiupnpc-static.  Perhaps it has not
  yet been created.


CMake Error at external/CMakeLists.txt:48 (set_property):
  set_property could not find TARGET libminiupnpc-static.  Perhaps it has not
  yet been created.


-- Looking for libunbound
-- Found libunbound include (unbound.h) in /usr/include
-- Found libunbound library
-- Using 64-bit LMDB from source tree
-- Looking for backtrace
-- Looking for backtrace - found
-- backtrace facility detected in default set of libraries
-- Backtrace_LIBRARY: 
-- Found Backtrace: /usr/include
CMake Error at external/CMakeLists.txt:72 (add_subdirectory):
  The source directory

    /home/qqqq/Downloads/monero-master/external/randomx

  does not contain a CMakeLists.txt file.


-- Using HIDAPI include dir at /usr/include/hidapi
-- Found Protobuf: /usr/lib/libprotobuf.so (found version "4.25.3")
-- Found ZLIB: /usr/lib/libz.so (found version "1.3.1")
CMake Warning at cmake/CheckTrezor.cmake:63 (message):
  Trezor: Unsupported Protobuf version 25.3.0.  Please, use Protobuf v21.


  ==========================================================================

  [WARNING] Trezor support cannot be compiled! Skipping Trezor compilation.

  For more information, please check src/device_trezor/README.md

Call Stack (most recent call first):
  cmake/CheckTrezor.cmake:87 (trezor_fatal_msg)
  CMakeLists.txt:704 (include)


-- Building on x86_64 for native
-- Performing Test CC_SUPPORTS_MARCH_NATIVE
-- Performing Test CC_SUPPORTS_MARCH_NATIVE - Success
-- AES support enabled
-- Performing Test _Werror__Wformat_c
-- Performing Test _Werror__Wformat_c - Success
-- Performing Test _Werror__Wformat_cxx
-- Performing Test _Werror__Wformat_cxx - Success
-- Performing Test _Werror__Wformat_security_c
-- Performing Test _Werror__Wformat_security_c - Failed
-- Performing Test _Werror__Wformat_security_cxx
-- Performing Test _Werror__Wformat_security_cxx - Failed
-- Performing Test _Werror__fstack_protector_c
-- Performing Test _Werror__fstack_protector_c - Success
-- Performing Test _Werror__fstack_protector_cxx
-- Performing Test _Werror__fstack_protector_cxx - Success
-- Performing Test _Werror__fstack_protector_strong_c
-- Performing Test _Werror__fstack_protector_strong_c - Success
-- Performing Test _Werror__fstack_protector_strong_cxx
-- Performing Test _Werror__fstack_protector_strong_cxx - Success
-- Performing Test _Werror__fcf_protection=full_c
-- Performing Test _Werror__fcf_protection=full_c - Success
-- Performing Test _Werror__fcf_protection=full_cxx
-- Performing Test _Werror__fcf_protection=full_cxx - Success
-- Performing Test _Werror__fstack_clash_protection_c
-- Performing Test _Werror__fstack_clash_protection_c - Success
-- Performing Test _Werror__fstack_clash_protection_cxx
-- Performing Test _Werror__fstack_clash_protection_cxx - Success
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
-- Performing Test _Werror__Werror=switch_c
-- Performing Test _Werror__Werror=switch_c - Success
-- Performing Test _Werror__Werror=switch_cxx
-- Performing Test _Werror__Werror=switch_cxx - Success
-- Performing Test _Werror__Werror=return_type_c
-- Performing Test _Werror__Werror=return_type_c - Success
-- Performing Test _Werror__Werror=return_type_cxx
-- Performing Test _Werror__Werror=return_type_cxx - Success
-- Using C security hardening flags:  -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -fstack-protector -fstack-protector-strong -fcf-protection=full -fstack-clash-protection -Werror=switch -Werror=return-type
-- Using C++ security hardening flags:  -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -fstack-protector -fstack-protector-strong -fcf-protection=full -fstack-clash-protection -Werror=switch -Werror=return-type
-- Using linker security hardening flags:  -pie -Wl,-z,relro -Wl,-z,now -Wl,-z,noexecstack
-- Found Boost Version: 108300
-- Looking for rl_copy_text
-- Looking for rl_copy_text - found
-- Looking for rl_filename_completion_function
-- Looking for rl_filename_completion_function - found
-- Found readline library at: /usr
-- Found Sodium: /usr/lib/libsodium.so
CMake Error at CMakeLists.txt:1228 (include):
  include could not find requested file:

    external/supercop/functions.cmake


-- Found Git: /usr/bin/git
fatal: not a git repository (or any of the parent directories): .git
CMake Warning at cmake/GitVersion.cmake:43 (message):
  Cannot determine current commit.  Make sure that you are building either
  from a Git working tree or from a source archive.
Call Stack (most recent call first):
  cmake/Version.cmake:42 (get_version_tag_from_git)
  src/CMakeLists.txt:83 (include)


CMake Error at src/crypto/wallet/CMakeLists.txt:39 (monero_crypto_autodetect):
  Unknown CMake command "monero_crypto_autodetect".


-- Configuring incomplete, errors occurred!
make: *** [Makefile:103: release-all] Error 1
(ERROR)-(Exit Code 2)-(Missing keyword, command, or permission problem)
(Tue Apr-4 6:04:49am)-(CPU 25.4%:0:Net 49)-(qqqq:~/Downloads/monero-master)-(268K:16)
> sudo make
[sudo] password for qqqq: 
ls: cannot access '.git/config': No such file or directory
fatal: not a git repository (or any of the parent directories): .git
mkdir -p build/release
cd build/release && cmake -D BUILD_TESTS=ON -D CMAKE_BUILD_TYPE=Release ../.. && make
-- CMake version 3.29.0
-- Found usable ccache: /usr/bin/ccache
-- Building without build tag
-- Checking submodules
fatal: not a git repository (or any of the parent directories): .git
fatal: not a git repository (or any of the parent directories): .git
-- Submodule 'external/miniupnp' is up-to-date
fatal: not a git repository (or any of the parent directories): .git
fatal: not a git repository (or any of the parent directories): .git
-- Submodule 'external/rapidjson' is up-to-date
fatal: not a git repository (or any of the parent directories): .git
fatal: not a git repository (or any of the parent directories): .git
-- Submodule 'external/trezor-common' is up-to-date
fatal: not a git repository (or any of the parent directories): .git
fatal: not a git repository (or any of the parent directories): .git
-- Submodule 'external/randomx' is up-to-date
fatal: not a git repository (or any of the parent directories): .git
fatal: not a git repository (or any of the parent directories): .git
-- Submodule 'external/supercop' is up-to-date
-- Could not find DEVELOPER_LOCAL_TOOLS in env (not required)
-- BOOST_IGNORE_SYSTEM_PATHS defaults to OFF
-- Building for a 64-bit system
-- Building internal libraries as static
-- Using LMDB as default DB type
-- Stack trace on exception enabled (using easylogging++)
-- Using OpenSSL include dir at /usr/include
CMake Warning (dev) at /usr/share/cmake/Modules/FindPackageHandleStandardArgs.cmake:438 (message):
  The package name passed to `find_package_handle_standard_args` (MiniUPnPc)
  does not match the name of the calling package (Miniupnpc).  This can lead
  to problems in calling code that expects `find_package` result variables
  (e.g., `_FOUND`) to follow a certain pattern.
Call Stack (most recent call first):
  cmake/FindMiniupnpc.cmake:39 (find_package_handle_standard_args)
  external/CMakeLists.txt:38 (find_package)
This warning is for project developers.  Use -Wno-dev to suppress it.

-- Could NOT find MiniUPnPc (missing: MINIUPNP_INCLUDE_DIR MINIUPNP_LIBRARY) 
-- Using in-tree miniupnpc
CMake Error at external/CMakeLists.txt:42 (add_subdirectory):
  add_subdirectory given source "miniupnp/miniupnpc" which is not an existing
  directory.


CMake Error at external/CMakeLists.txt:43 (set_property):
  set_property could not find TARGET libminiupnpc-static.  Perhaps it has not
  yet been created.


CMake Error at external/CMakeLists.txt:44 (set_property):
  set_property could not find TARGET libminiupnpc-static.  Perhaps it has not
  yet been created.


CMake Error at external/CMakeLists.txt:48 (set_property):
  set_property could not find TARGET libminiupnpc-static.  Perhaps it has not
  yet been created.


-- Looking for libunbound
-- Found libunbound include (unbound.h) in /usr/include
-- Found libunbound library
-- Using 64-bit LMDB from source tree
-- Backtrace_LIBRARY: 
CMake Error at external/CMakeLists.txt:72 (add_subdirectory):
  The source directory

    /home/qqqq/Downloads/monero-master/external/randomx

  does not contain a CMakeLists.txt file.


-- Using HIDAPI include dir at /usr/include/hidapi
CMake Warning at cmake/CheckTrezor.cmake:63 (message):
  Trezor: Unsupported Protobuf version 25.3.0.  Please, use Protobuf v21.


  ==========================================================================

  [WARNING] Trezor support cannot be compiled! Skipping Trezor compilation.

  For more information, please check src/device_trezor/README.md

Call Stack (most recent call first):
  cmake/CheckTrezor.cmake:87 (trezor_fatal_msg)
  CMakeLists.txt:704 (include)


-- Building on x86_64 for native
-- AES support enabled
-- Performing Test _Werror__fcf_protection=full_c
-- Performing Test _Werror__fcf_protection=full_c - Success
-- Performing Test _Werror__fcf_protection=full_cxx
-- Performing Test _Werror__fcf_protection=full_cxx - Success
-- Performing Test _Werror__Werror=switch_c
-- Performing Test _Werror__Werror=switch_c - Success
-- Performing Test _Werror__Werror=switch_cxx
-- Performing Test _Werror__Werror=switch_cxx - Success
-- Performing Test _Werror__Werror=return_type_c
-- Performing Test _Werror__Werror=return_type_c - Success
-- Performing Test _Werror__Werror=return_type_cxx
-- Performing Test _Werror__Werror=return_type_cxx - Success
-- Using C security hardening flags:  -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -fstack-protector -fstack-protector-strong -fcf-protection=full -fstack-clash-protection -Werror=switch -Werror=return-type
-- Using C++ security hardening flags:  -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -fstack-protector -fstack-protector-strong -fcf-protection=full -fstack-clash-protection -Werror=switch -Werror=return-type
-- Using linker security hardening flags:  -pie -Wl,-z,relro -Wl,-z,now -Wl,-z,noexecstack
-- Found Boost Version: 108300
-- Found readline library at: /usr
CMake Error at CMakeLists.txt:1228 (include):
  include could not find requested file:

    external/supercop/functions.cmake


-- Found Git: /usr/bin/git
fatal: not a git repository (or any of the parent directories): .git
CMake Warning at cmake/GitVersion.cmake:43 (message):
  Cannot determine current commit.  Make sure that you are building either
  from a Git working tree or from a source archive.
Call Stack (most recent call first):
  cmake/Version.cmake:42 (get_version_tag_from_git)
  src/CMakeLists.txt:83 (include)


CMake Error at src/crypto/wallet/CMakeLists.txt:39 (monero_crypto_autodetect):
  Unknown CMake command "monero_crypto_autodetect".


-- Configuring incomplete, errors occurred!
make: *** [Makefile:103: release-all] Error 1
`

# Action History
- Created by: mia0x75 | 2018-01-13T11:54:27+00:00
- Closed at: 2018-06-10T09:32:53+00:00
