---
title: Building monero under Ubuntu 16.04.4 fails with CMake errors
source_url: https://github.com/monero-project/monero/issues/3825
author: mxjoe
assignees: []
labels:
- invalid
created_at: '2018-05-17T20:15:26+00:00'
updated_at: '2018-05-17T20:24:54+00:00'
type: issue
status: closed
closed_at: '2018-05-17T20:24:54+00:00'
---

# Original Description
Hi,

I tried to build monero from source under my Ubuntu 16.04.4 server with following commands:

```
cd /usr/local/src
sudo git clone https://github.com/monero-project/monero.git
cd monero
sudo git checkout release-v0.12
curl https://raw.githubusercontent.com/mxjoe/nodejs-pool/master/deployment/monero_daemon.patch | sudo git apply -v
sudo make -j$(nproc)
```

The make fails every time with this output when running `sudo make -j$(nproc)`:

```
mkdir -p build/release
cd build/release && cmake -D BUILD_TESTS=ON -D CMAKE_BUILD_TYPE=release ../.. && make
-- Building without build tag
-- Could not find DEVELOPER_LOCAL_TOOLS in env (not required)
-- BOOST_IGNORE_SYSTEM_PATHS defaults to OFF
-- Could not find DEVELOPER_LIBUNBOUND_OLD in env (not required)
-- Building for a 64-bit system
-- Building internal libraries as static
-- Could not find DATABASE in env (not required unless you want to change database type from default: lmdb)
-- Using LMDB as default DB type
-- Stack trace on exception enabled (using easylogging++)
-- Using OpenSSL include dir at /usr/include
-- Checking for module 'libpcsclite'
--   No package 'libpcsclite' found
-- Could NOT find PCSC (missing:  PCSC_LIBRARY PCSC_INCLUDE_DIR) 
-- Found miniupnpc API version 10
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
-- Found libunbound include (unbound.h) in /usr/include
-- Found libunbound shared library
-- Using 64-bit LMDB from source tree
-- Building on x86_64 for native
-- Using C security hardening flags:  -Wformat -Wformat-security -fstack-protector -fstack-protector-strong
-- Using C++ security hardening flags:  -Wformat -Wformat-security -fstack-protector -fstack-protector-strong
-- Using linker security hardening flags:  -pie -Wl,-z,relro -Wl,-z,now -Wl,-z,noexecstack
-- AES support enabled
-- Found Boost Version: 105800
-- Could NOT find Readline (missing:  Readline_INCLUDE_DIR Readline_LIBRARY) 
-- Could not find GNU readline library so building without readline support
-- Found Git: /usr/bin/git
Doxygen: graphviz not found - graphs disabled
-- Could NOT find Doxygen (missing:  DOXYGEN_EXECUTABLE) 
-- Configuring incomplete, errors occurred!
See also "/usr/local/src/monero/build/release/CMakeFiles/CMakeOutput.log".
See also "/usr/local/src/monero/build/release/CMakeFiles/CMakeError.log".
Makefile:64: recipe for target 'release-all' failed
make: *** [release-all] Error 1
```

The CMake log files are attached to this post. Am I doing something wrong or is this indeed a bug?
[CMakeError.log](https://github.com/monero-project/monero/files/2014603/CMakeError.log)
[Uploading CMakeOutput.log…]()

It might be the patching which does brake it but I am not sure.

# Discussion History
## moneromooo-monero | 2018-05-17T20:16:57+00:00
See README.md about submodules.

+invalid

## dEBRUYNE-1 | 2018-05-17T20:23:08+00:00
To add, this step:

`sudo git clone https://github.com/monero-project/monero.git`

Needs to be:

`sudo git clone --recursive https://github.com/monero-project/monero.git`


# Action History
- Created by: mxjoe | 2018-05-17T20:15:26+00:00
- Closed at: 2018-05-17T20:24:54+00:00
