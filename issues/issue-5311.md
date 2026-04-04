---
title: Mac debug build error
source_url: https://github.com/monero-project/monero/issues/5311
author: woodser
assignees: []
labels: []
created_at: '2019-03-18T14:41:05+00:00'
updated_at: '2019-03-20T14:05:31+00:00'
type: issue
status: closed
closed_at: '2019-03-20T14:05:31+00:00'
---

# Original Description
I get this build error with `make debug` on OSX 10.14:

```
[ 71%] Linking CXX shared library libdevice_trezor.dylib
Undefined symbols for architecture x86_64:
  "boost::archive::detail::basic_serializer_map::erase(boost::archive::detail::basic_serializer const*)", referenced from:
      boost::archive::detail::archive_serializer_map<boost::archive::portable_binary_iarchive>::erase(boost::archive::detail::basic_serializer const*) in device_trezor.cpp.o
      boost::archive::detail::archive_serializer_map<boost::archive::portable_binary_oarchive>::erase(boost::archive::detail::basic_serializer const*) in device_trezor.cpp.o
  "boost::archive::detail::basic_serializer_map::insert(boost::archive::detail::basic_serializer const*)", referenced from:
      boost::archive::detail::archive_serializer_map<boost::archive::portable_binary_iarchive>::insert(boost::archive::detail::basic_serializer const*) in device_trezor.cpp.o
      boost::archive::detail::archive_serializer_map<boost::archive::portable_binary_oarchive>::insert(boost::archive::detail::basic_serializer const*) in device_trezor.cpp.o
  "boost::archive::detail::basic_serializer_map::find(boost::serialization::extended_type_info const&) const", referenced from:
      boost::archive::detail::archive_serializer_map<boost::archive::portable_binary_iarchive>::find(boost::serialization::extended_type_info const&) in device_trezor.cpp.o
      boost::archive::detail::archive_serializer_map<boost::archive::portable_binary_oarchive>::find(boost::serialization::extended_type_info const&) in device_trezor.cpp.o
ld: symbol(s) not found for architecture x86_64
clang: error: linker command failed with exit code 1 (use -v to see invocation)
make[3]: *** [src/device_trezor/libdevice_trezor.dylib] Error 1
make[2]: *** [src/device_trezor/CMakeFiles/device_trezor.dir/all] Error 2
make[1]: *** [all] Error 2
make: *** [debug] Error 2
```

# Discussion History
## ph4r05 | 2019-03-18T20:40:28+00:00
Is it still relevant? As I went through IRC I've got a feeling that you built it eventually.

## woodser | 2019-03-18T21:03:48+00:00
I didn’t need to build it for what we were doing, but it does not build for Mac.

## ph4r05 | 2019-03-18T21:36:45+00:00
I am building it on OSX 10.14.3, `make debug` and cannot reproduce. Which Boost version do you have?

## woodser | 2019-03-19T14:01:26+00:00
Just updated from Boost version 1.68.0.0 to 1.68.0.1 and the build error remains.

I notice when starting make I get 9 of these warnings:

```
CMake Warning at /usr/local/Cellar/cmake/3.7.1/share/cmake/Modules/FindBoost.cmake:744 (message):
  Imported targets not available for Boost version 106800
Call Stack (most recent call first):
  /usr/local/Cellar/cmake/3.7.1/share/cmake/Modules/FindBoost.cmake:848 (_Boost_COMPONENT_DEPENDENCIES)
  /usr/local/Cellar/cmake/3.7.1/share/cmake/Modules/FindBoost.cmake:1435 (_Boost_MISSING_DEPENDENCIES)
  CMakeLists.txt:886 (find_package)
```

## ph4r05 | 2019-03-19T14:03:08+00:00
Could you also try cmake 3.9 pls? I use 3.12

## woodser | 2019-03-19T14:22:40+00:00
Upgrading cmake from 3.7.1 to 3.14.0 removed the warnings but still fails with the same error.

I'm including other cmake output before building starts in case it reveals anything useful:

```
mkdir -p build/"Darwin/inconsistent_patch"/debug
cd build/"Darwin/inconsistent_patch"/debug && cmake -D CMAKE_BUILD_TYPE=Debug ../../../..
-- CMake version 3.14.0
-- Building without build tag
-- Checking submodules
-- Submodule 'external/miniupnp' is up-to-date
-- Submodule 'external/unbound' is up-to-date
-- Submodule 'external/rapidjson' is up-to-date
-- Submodule 'external/trezor-common' is up-to-date
-- Could not find DEVELOPER_LOCAL_TOOLS in env (not required)
-- BOOST_IGNORE_SYSTEM_PATHS defaults to OFF
-- Could not find DEVELOPER_LIBUNBOUND_OLD in env (not required)
-- Building for a 64-bit system
-- Building internal libraries with position independent code
-- Could not find DATABASE in env (not required unless you want to change database type from default: lmdb)
-- Using LMDB as default DB type
-- Stack trace on exception disabled
-- Using OpenSSL found at /usr/local/opt/openssl
-- Using OpenSSL include dir at /usr/local/opt/openssl/include
-- Found miniupnpc API version 17
-- Using in-tree miniupnpc
-- Looking for libunbound
-- Found libunbound include (unbound.h) in /usr/local/include
-- Found libunbound shared library
-- Using 64-bit LMDB from source tree
-- Using HIDAPI include dir at /usr/local/include/hidapi
-- Could NOT find Protobuf (missing: Protobuf_LIBRARIES Protobuf_INCLUDE_DIR) 
-- Could NOT find Protobuf (missing: Protobuf_LIBRARIES Protobuf_INCLUDE_DIR) 
-- Could not find Protobuf
-- Building on x86_64 for native
-- AES support enabled
-- Performing Test _fcf_protection=full_c
-- Performing Test _fcf_protection=full_c - Failed
-- Performing Test _fcf_protection=full_cxx
-- Performing Test _fcf_protection=full_cxx - Failed
-- Using C security hardening flags:  -Wformat -Wformat-security -fstack-protector -fstack-protector-strong
-- Using C++ security hardening flags:  -Wformat -Wformat-security -fstack-protector -fstack-protector-strong
-- Using linker security hardening flags:  -pie
-- Found Boost Version: 106800
-- Found readline library at: /usr/local/opt/readline
-- Found Git: /usr/bin/git
-- Trezor support disabled
-- Could NOT find GTest (missing: GTEST_MAIN_LIBRARY) 
-- GTest not found on the system: will use GTest bundled with this source
-- Found Doxygen: /usr/local/bin/doxygen (found version "1.8.15") found components:  doxygen dot 
-- Configuring done
CMake Warning (dev):
  Policy CMP0042 is not set: MACOSX_RPATH is enabled by default.  Run "cmake
  --help-policy CMP0042" for policy details.  Use the cmake_policy command to
  set the policy and suppress this warning.

  MACOSX_RPATH is not specified for the following targets:

   easylogging

This warning is for project developers.  Use -Wno-dev to suppress it.
```

## ph4r05 | 2019-03-19T15:44:37+00:00
Ah, I found it... 
I am working on a path.

Btw pls if there is an issue with the Trezor code, just mention me in the issue, I will check it out. Thanks!

## ph4r05 | 2019-03-19T16:15:27+00:00
@woodser pls try #5316. I could reproduce the bug and this fixes it. Thanks a lot!

## woodser | 2019-03-19T16:58:59+00:00
@ph4r05 Your PR does indeed fix the build error.  Thank you!

## ph4r05 | 2019-03-20T14:03:25+00:00
@woodser great this works for you! So, do you think you can close the issue now?

## woodser | 2019-03-20T14:05:31+00:00
Yes.  Thanks again.

# Action History
- Created by: woodser | 2019-03-18T14:41:05+00:00
- Closed at: 2019-03-20T14:05:31+00:00
