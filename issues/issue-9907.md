---
title: Arch Linux `Could NOT find Sodium` with `-DSTATIC=ON`
source_url: https://github.com/monero-project/monero/issues/9907
author: SyntheticBird45
assignees: []
labels: []
created_at: '2025-04-21T12:58:58+00:00'
updated_at: '2025-04-22T08:45:28+00:00'
type: issue
status: closed
closed_at: '2025-04-21T13:56:49+00:00'
---

# Original Description
On fresh arch installation, with the README's specified dependencies:

```
:: Synchronizing package databases...
 core is up to date
 extra is up to date
warning: base-devel-1-2 is up to date -- skipping
warning: cmake-4.0.1-1 is up to date -- skipping
warning: boost-1.87.0-3 is up to date -- skipping
warning: openssl-3.5.0-1 is up to date -- skipping
warning: zeromq-4.3.5-2 is up to date -- skipping
warning: unbound-1.22.0-3 is up to date -- skipping
warning: libsodium-1.0.20-1 is up to date -- skipping
warning: libunwind-1.8.1-3 is up to date -- skipping
warning: xz-5.8.1-1 is up to date -- skipping
warning: readline-8.2.013-1 is up to date -- skipping
warning: expat-2.7.1-1 is up to date -- skipping
warning: python-3.13.3-1 is up to date -- skipping
warning: doxygen-1.13.2-1 is up to date -- skipping
warning: graphviz-12.2.1-1 is up to date -- skipping
warning: qt5-tools-5.15.16+kde+r3-6 is up to date -- skipping
warning: hidapi-0.14.0-3 is up to date -- skipping
warning: libusb-1.0.28-1 is up to date -- skipping
warning: protobuf-30.1-1 is up to date -- skipping
warning: systemd-257.5-2 is up to date -- skipping
...
```

`pkg-config` is also installed:
```
warning: pkg-config-2.4.3-1 is up to date -- reinstalling
```

<del>`$ cmake -DCMAKE_C_COMPILER=clang -DCMAKE_CXX_COMPILER=clang++ -DCMAKE_BUILD_TYPE=Release`
or `cmake -DCMAKE_BUILD_TYPE=Release`
or `cmake -B build`</del>
`$ cmake -DSTATIC=ON -B build`
results in:
```
CMake Deprecation Warning at CMakeLists.txt:31 (cmake_minimum_required):
  Compatibility with CMake < 3.10 will be removed from a future version of
  CMake.

  Update the VERSION argument <min> value.  Or, use the <min>...<max> syntax
  to tell CMake that the project requires at least <min> but has been updated
  to work with policies introduced by <max> or earlier.


-- CMake version 4.0.1
-- ccache NOT found! Please install it for faster rebuilds.
CMake Deprecation Warning at /path/to/monero/build/CMakeFiles/CMakeTmp/test_project/CMakeLists.txt:1 (cmake_minimum_required):
  Compatibility with CMake < 3.10 will be removed from a future version of
  CMake.

  Update the VERSION argument <min> value.  Or, use the <min>...<max> syntax
  to tell CMake that the project requires at least <min> but has been updated
  to work with policies introduced by <max> or earlier.


CMake Deprecation Warning at /path/to/monero/build/CMakeFiles/CMakeTmp/test_project/CMakeLists.txt:1 (cmake_minimum_required):
  Compatibility with CMake < 3.10 will be removed from a future version of
  CMake.

  Update the VERSION argument <min> value.  Or, use the <min>...<max> syntax
  to tell CMake that the project requires at least <min> but has been updated
  to work with policies introduced by <max> or earlier.


-- Building without build tag
-- Checking submodules
-- Submodule 'external/miniupnp' is up-to-date
-- Submodule 'external/rapidjson' is up-to-date
-- Submodule 'external/randomx' is up-to-date
-- Submodule 'external/supercop' is up-to-date
-- Building for a 64-bit system
-- Building internal libraries as static
-- Using LMDB as default DB type
-- looking for liblzma
-- liblzma found
-- Stack trace on exception enabled (using libunwind)
-- Using OpenSSL include dir at /usr/include
CMake Warning (dev) at /usr/share/cmake/Modules/FindPackageHandleStandardArgs.cmake:430 (message):
  The package name passed to find_package_handle_standard_args() (MiniUPnPc)
  does not match the name of the calling package (Miniupnpc).  This can lead
  to problems in calling code that expects find_package() result variables
  (e.g., `_FOUND`) to follow a certain pattern.
Call Stack (most recent call first):
  cmake/FindMiniupnpc.cmake:39 (find_package_handle_standard_args)
  external/CMakeLists.txt:38 (find_package)
This warning is for project developers.  Use -Wno-dev to suppress it.

-- Could NOT find MiniUPnPc (missing: MINIUPNP_INCLUDE_DIR MINIUPNP_LIBRARY)
-- Using in-tree miniupnpc
CMake Deprecation Warning at external/miniupnp/miniupnpc/CMakeLists.txt:1 (cmake_minimum_required):
  Compatibility with CMake < 3.10 will be removed from a future version of
  CMake.

  Update the VERSION argument <min> value.  Or, use the <min>...<max> syntax
  to tell CMake that the project requires at least <min> but has been updated
  to work with policies introduced by <max> or earlier.


-- Looking for libunbound
-- Found libunbound include (unbound.h) in /usr/include
-- Found libunbound library
-- Using 64-bit LMDB from source tree
CMake Deprecation Warning at external/easylogging++/CMakeLists.txt:29 (cmake_minimum_required):
  Compatibility with CMake < 3.10 will be removed from a future version of
  CMake.

  Update the VERSION argument <min> value.  Or, use the <min>...<max> syntax
  to tell CMake that the project requires at least <min> but has been updated
  to work with policies introduced by <max> or earlier.


-- Backtrace_LIBRARY:
CMake Deprecation Warning at external/randomx/CMakeLists.txt:29 (cmake_minimum_required):
  Compatibility with CMake < 3.10 will be removed from a future version of
  CMake.

  Update the VERSION argument <min> value.  Or, use the <min>...<max> syntax
  to tell CMake that the project requires at least <min> but has been updated
  to work with policies introduced by <max> or earlier.


-- Performing Test _march=native_cxx
-- Performing Test _march=native_cxx - Success
-- Setting CXX flag -march=native
-- Performing Test _march=native_c
-- Performing Test _march=native_c - Success
-- Setting C flag -march=native
-- Using HIDAPI include dir at /usr/include/hidapi
-- Trezor: protobuf messages regenerated out.
-- LibUSB Compilation test: TRUE
-- Trezor: compatible LibUSB found at: /usr/include/libusb-1.0
-- Building on x86_64 for native
-- AES support enabled
-- Performing Test _Werror__fcf_protection=full_c
-- Performing Test _Werror__fcf_protection=full_c - Failed
-- Performing Test _Werror__fcf_protection=full_cxx
-- Performing Test _Werror__fcf_protection=full_cxx - Failed
-- Performing Test _Werror__Werror=switch_c
-- Performing Test _Werror__Werror=switch_c - Success
-- Performing Test _Werror__Werror=switch_cxx
-- Performing Test _Werror__Werror=switch_cxx - Success
-- Performing Test _Werror__Werror=return_type_c
-- Performing Test _Werror__Werror=return_type_c - Success
-- Performing Test _Werror__Werror=return_type_cxx
-- Performing Test _Werror__Werror=return_type_cxx - Success
-- Using C security hardening flags:  -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -fstack-protector -fstack-protector-strong -fstack-clash-protection -Werror=switch -Werror=return-type
-- Using C++ security hardening flags:  -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -fstack-protector -fstack-protector-strong -fstack-clash-protection -Werror=switch -Werror=return-type
-- Using linker security hardening flags:  -Wl,-pie -Wl,-z,relro -Wl,-z,now -Wl,-z,noexecstack
CMake Warning (dev) at CMakeLists.txt:1031 (find_package):
  Policy CMP0167 is not set: The FindBoost module is removed.  Run "cmake
  --help-policy CMP0167" for policy details.  Use the cmake_policy command to
  set the policy and suppress this warning.

This warning is for project developers.  Use -Wno-dev to suppress it.

-- Found Boost Version: 1.87.0
-- Boost components: filesystem;thread;date_time;chrono;serialization;program_options
CMake Warning (dev) at CMakeLists.txt:1056 (find_package):
  Policy CMP0167 is not set: The FindBoost module is removed.  Run "cmake
  --help-policy CMP0167" for policy details.  Use the cmake_policy command to
  set the policy and suppress this warning.

This warning is for project developers.  Use -Wno-dev to suppress it.

-- Found readline library at: /usr
CMake Error at /usr/share/cmake/Modules/FindPackageHandleStandardArgs.cmake:227 (message):
  Could NOT find Sodium (missing: sodium_LIBRARY_RELEASE
  sodium_LIBRARY_DEBUG)
Call Stack (most recent call first):
  /usr/share/cmake/Modules/FindPackageHandleStandardArgs.cmake:591 (_FPHSA_FAILURE_MESSAGE)
  cmake/FindSodium.cmake:227 (find_package_handle_standard_args)
  CMakeLists.txt:1132 (find_package)


-- Configuring incomplete, errors occurred!
```

Modifying https://github.com/monero-project/monero/blob/master/cmake/FindSodium.cmake#L228 `Sodium` value to either `sodium` or `libsodium` make `cmake` passes validation with the following warning:

```
CMake Warning (dev) at /usr/share/cmake/Modules/FindPackageHandleStandardArgs.cmake:430 (message):
  The package name passed to find_package_handle_standard_args() (sodium)
  does not match the name of the calling package (Sodium).  This can lead to
  problems in calling code that expects find_package() result variables
  (e.g., `_FOUND`) to follow a certain pattern.
Call Stack (most recent call first):
  cmake/FindSodium.cmake:227 (find_package_handle_standard_args)
  CMakeLists.txt:1132 (find_package)
```

Compilation then end up with:
```
/usr/bin/ld: ../cryptonote_core/libcryptonote_core.a(blockchain.cpp.o): undefined reference to symbol 'crypto_verify_32'
/usr/bin/ld: /usr/lib/libsodium.so.26: error adding symbols: DSO missing from command line
clang++: error: linker command failed with exit code 1 (use -v to see invocation)
make[2]: *** [src/blockchain_utilities/CMakeFiles/blockchain_import.dir/build.make:174: bin/monero-blockchain-import] Error 1
make[1]: *** [CMakeFiles/Makefile2:4347: src/blockchain_utilities/CMakeFiles/blockchain_import.dir/all] Error 2
make[1]: *** Waiting for unfinished jobs....
```

# Discussion History
## SyntheticBird45 | 2025-04-21T13:43:35+00:00
Caused by `cmake` not cleaning prior attempts. This error is caused by `-DSTATIC=ON`

## SyntheticBird45 | 2025-04-21T13:56:49+00:00
Resolved, people wanting to statically build `monero` on Arch Linux must use `libsodium-static` AUR package.

## jeffro256 | 2025-04-22T04:07:30+00:00
Perhaps the CMake message could be clarified to provide useful information iff dynamic lib found AND NOT static lib found. 

## SyntheticBird45 | 2025-04-22T08:45:27+00:00
> Perhaps the CMake message could be clarified to provide useful information iff dynamic lib found AND NOT static lib found.

Would be awesome.

# Action History
- Created by: SyntheticBird45 | 2025-04-21T12:58:58+00:00
- Closed at: 2025-04-21T13:56:49+00:00
