---
title: Cmake cannot find Boost on Fedora when building a static-release
source_url: https://github.com/monero-project/monero/issues/8393
author: layters
assignees: []
labels: []
created_at: '2022-06-19T01:03:36+00:00'
updated_at: '2022-06-19T13:07:21+00:00'
type: issue
status: closed
closed_at: '2022-06-19T13:07:21+00:00'
---

# Original Description
So this is the error generated from attempting to build monero statically:

```
$ make release-static && make release-static
mkdir -p build/"Linux/master"/release
cd build/"Linux/master"/release && cmake -D STATIC=ON -D ARCH="x86-64" -D BUILD_64=ON -D CMAKE_BUILD_TYPE=Release ../../../.. && make
-- CMake version 3.17.4
-- Found usable ccache: /usr/bin/ccache
-- Building without build tag
-- Checking submodules
-- Submodule 'external/miniupnp' is up-to-date
-- Submodule 'external/rapidjson' is up-to-date
-- Submodule 'external/trezor-common' is up-to-date
-- Submodule 'external/randomx' is up-to-date
-- Submodule 'external/supercop' is up-to-date
-- Could not find DEVELOPER_LOCAL_TOOLS in env (not required)
-- BOOST_IGNORE_SYSTEM_PATHS defaults to OFF
-- Building for a 64-bit system
-- Building internal libraries as static
-- Using LMDB as default DB type
-- Stack trace on exception enabled (using easylogging++)
-- Using OpenSSL include dir at /usr/include
CMake Warning (dev) at /usr/share/cmake/Modules/FindPackageHandleStandardArgs.cmake:272 (message):
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
-- Looking for libunbound
-- Found libunbound include (unbound.h) in /usr/include
-- Found libunbound library
-- Using 64-bit LMDB from source tree
-- Backtrace_LIBRARY: 
-- Setting CXX flag -maes
-- Setting C flag -maes
-- Using HIDAPI include dir at /usr/include/hidapi
-- Protobuf lib: /usr/lib64/libprotobuf.so, inc: /usr/include, protoc: /usr/bin/protoc
-- Trezor protobuf messages regenerated out: "."
-- LibUSB Compilation test: TRUE
-- Trezor compatible LibUSB found at: /usr/include/libusb-1.0
-- Building on x86_64 for x86-64
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
CMake Error at /usr/share/cmake/Modules/FindPackageHandleStandardArgs.cmake:164 (message):
  Could NOT find Boost (missing: system filesystem thread date_time chrono
  regex serialization program_options locale) (found suitable version
  "1.69.0", minimum required is "1.58")
Call Stack (most recent call first):
  /usr/share/cmake/Modules/FindPackageHandleStandardArgs.cmake:445 (_FPHSA_FAILURE_MESSAGE)
  /usr/share/cmake/Modules/FindBoost.cmake:2166 (find_package_handle_standard_args)
  CMakeLists.txt:1078 (find_package)


-- Configuring incomplete, errors occurred!
See also "/home/larteyoh/Downloads/monero/build/Linux/master/release/CMakeFiles/CMakeOutput.log".
See also "/home/larteyoh/Downloads/monero/build/Linux/master/release/CMakeFiles/CMakeError.log".
make: *** [Makefile:107: release-static] Error 1
```

Any way to fix this error?

# Discussion History
# Action History
- Created by: layters | 2022-06-19T01:03:36+00:00
- Closed at: 2022-06-19T13:07:21+00:00
