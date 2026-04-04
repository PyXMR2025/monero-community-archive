---
title: Failed to build on centos7
source_url: https://github.com/monero-project/monero/issues/5089
author: oakatplatform
assignees: []
labels: []
created_at: '2019-01-23T04:16:56+00:00'
updated_at: '2019-01-23T04:43:18+00:00'
type: issue
status: closed
closed_at: '2019-01-23T04:43:18+00:00'
---

# Original Description
build error:

```
CMake Warning at CMakeLists.txt:457 (find_package):
  By not providing "FindHIDAPI.cmake" in CMAKE_MODULE_PATH this project has
  asked CMake to find a package configuration file provided by "HIDAPI", but
  CMake did not find one.

  Could not find a package configuration file provided by "HIDAPI" with any
  of the following names:

    HIDAPIConfig.cmake
    hidapi-config.cmake

  Add the installation prefix of "HIDAPI" to CMAKE_PREFIX_PATH or set
  "HIDAPI_DIR" to a directory containing one of the above files.  If "HIDAPI"
  provides a separate development package or SDK, be sure it has been
  installed.


-- Could NOT find MiniUPnPc (missing: MINIUPNP_INCLUDE_DIR MINIUPNP_LIBRARY) 
-- Using in-tree miniupnpc
-- Looking for libunbound
-- Using 64-bit LMDB from source tree
-- Could not find HIDAPI
-- Building on x86_64 for native
-- AES support enabled
-- Performing Test _fcf_protection=full_c
-- Performing Test _fcf_protection=full_c - Failed
-- Performing Test _fcf_protection=full_cxx
-- Performing Test _fcf_protection=full_cxx - Failed
-- Using C security hardening flags:  -Wformat -Wformat-security -fstack-protector -fstack-protector-strong
-- Using C++ security hardening flags:  -Wformat -Wformat-security -fstack-protector -fstack-protector-strong
-- Using linker security hardening flags:  -pie -Wl,-z,relro -Wl,-z,now -Wl,-z,noexecstack
-- Found Boost Version: 106300
-- Found readline library at: /usr
-- Found Git: /bin/git
CMake Error: The following variables are used in this project, but they are set to NOTFOUND.
Please set them or make sure they are set and tested correctly in the CMake files:
SODIUM_LIBRARY
    linked by target "cncrypto" in directory /root/qzhong/monero_master/src/crypto

-- Configuring incomplete, errors occurred!
See also "/root/qzhong/monero_master/build/static_on/CMakeFiles/CMakeOutput.log".
See also "/root/qzhong/monero_master/build/static_on/CMakeFiles/CMakeError.log".
```

# Discussion History
## oakatplatform | 2019-01-23T04:43:18+00:00
fixed by:
yum install libsodium-devel -y
yum install libsodium -y

# Action History
- Created by: oakatplatform | 2019-01-23T04:16:56+00:00
- Closed at: 2019-01-23T04:43:18+00:00
