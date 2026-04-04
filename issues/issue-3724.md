---
title: set_property could not find TARGET libminiupnpc-static.
source_url: https://github.com/monero-project/monero/issues/3724
author: 5-digits
assignees: []
labels: []
created_at: '2018-04-29T01:52:22+00:00'
updated_at: '2018-10-25T10:17:02+00:00'
type: issue
status: closed
closed_at: '2018-10-25T10:17:02+00:00'
---

# Original Description
I get this error when compiling the Monero project, i'm using the ubuntu 16

```
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
-- Found readline library at: /usr
-- Found Git: /usr/bin/git
-- Configuring incomplete, errors occurred!
See also "/home/MR/monero/build/release/CMakeFiles/CMakeOutput.log".
See also "/home/MR/monero/build/release/CMakeFiles/CMakeError.log".
Makefile:64: recipe for target 'release-all' failed
make: *** [release-all] Error 1

```

# Discussion History
## radfish | 2018-04-29T03:33:16+00:00
    git submodule init
    git submodule update


## Hoshpak | 2018-05-24T12:36:21+00:00
Obviously, this only works if the directory you are working in is a git repository. Shouldn't miniupnpc be included in the release tarballs if it is needed to compile monero and using versions installed in the system no longer works?

## anonimal | 2018-05-24T18:15:57+00:00
>Shouldn't miniupnpc be included in the release tarballs if it is needed to compile monero and using versions installed in the system no longer works?

That's a github problem: they don't package that way.

## Hoshpak | 2018-05-25T10:57:36+00:00
It seems other projects found a way to work around that and produce release tarballs that include submodules. Tarballs that contain everything are important for people buildings stable releases (e.g. package maintainers) and don't want or can apply manual workarounds or pull dependencies from somewhere into the build directory.

If I may ask, why was that changed anyway, what's wrong with using system provided libraries? Does monero alter miniupnpc in any way that makes it incompatible with upstream copies?

## moneromooo-monero | 2018-10-25T10:07:28+00:00
+resolved

# Action History
- Created by: 5-digits | 2018-04-29T01:52:22+00:00
- Closed at: 2018-10-25T10:17:02+00:00
