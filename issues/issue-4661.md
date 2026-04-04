---
title: v0.13.0.3.tar.gz fails to build
source_url: https://github.com/monero-project/monero/issues/4661
author: hegjon
assignees: []
labels: []
created_at: '2018-10-19T09:39:32+00:00'
updated_at: '2019-06-15T17:29:30+00:00'
type: issue
status: closed
closed_at: '2019-06-15T17:29:30+00:00'
---

# Original Description
Probably fails because the embedded miniupnpc library is not included in the release tarball.

It would be great if we could use the system library, so that we would be one step closer to include Monero in the official Fedora RPM repository.

```
~/rpmbuild/SOURCES/monero-0.13.0.3/build$ cmake -D CMAKE_BUILD_TYPE=Release .. 
-- CMake version 3.11.2
-- Building without build tag
-- Checking submodules
fatal: not a git repository (or any parent up to mount point /)
Stopping at filesystem boundary (GIT_DISCOVERY_ACROSS_FILESYSTEM not set).
fatal: not a git repository (or any parent up to mount point /)
Stopping at filesystem boundary (GIT_DISCOVERY_ACROSS_FILESYSTEM not set).
fatal: not a git repository (or any parent up to mount point /)
Stopping at filesystem boundary (GIT_DISCOVERY_ACROSS_FILESYSTEM not set).
fatal: not a git repository (or any parent up to mount point /)
Stopping at filesystem boundary (GIT_DISCOVERY_ACROSS_FILESYSTEM not set).
fatal: not a git repository (or any parent up to mount point /)
Stopping at filesystem boundary (GIT_DISCOVERY_ACROSS_FILESYSTEM not set).
fatal: not a git repository (or any parent up to mount point /)
Stopping at filesystem boundary (GIT_DISCOVERY_ACROSS_FILESYSTEM not set).
-- Could not find DEVELOPER_LOCAL_TOOLS in env (not required)
-- BOOST_IGNORE_SYSTEM_PATHS defaults to OFF
-- Could not find DEVELOPER_LIBUNBOUND_OLD in env (not required)
-- Building for a 64-bit system
-- Building internal libraries as static
-- Could not find DATABASE in env (not required unless you want to change database type from default: lmdb)
-- Using LMDB as default DB type
-- Stack trace on exception enabled (using easylogging++)
-- Using OpenSSL include dir at /usr/include
-- Found miniupnpc API version 16
-- Using in-tree miniupnpc
CMake Error at external/CMakeLists.txt:41 (add_subdirectory):
  add_subdirectory given source "miniupnp/miniupnpc" which is not an existing
  directory.


CMake Error at external/CMakeLists.txt:42 (set_property):
  set_property could not find TARGET libminiupnpc-static.  Perhaps it has not
  yet been created.


CMake Error at external/CMakeLists.txt:46 (set_property):
  set_property could not find TARGET libminiupnpc-static.  Perhaps it has not
  yet been created.


-- Looking for libunbound
-- Found libunbound include (unbound.h) in /usr/include
-- Found libunbound shared library
-- Using 64-bit LMDB from source tree
-- Using HIDAPI include dir at /usr/include/hidapi
-- Building on x86_64 for native
-- AES support enabled
-- Performing Test _fcf_protection=full_c
-- Performing Test _fcf_protection=full_c - Success
-- Performing Test _fcf_protection=full_cxx
-- Performing Test _fcf_protection=full_cxx - Success
-- Using C security hardening flags:  -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -fstack-protector -fstack-protector-strong -fcf-protection=full -fstack-clash-protection -mmitigate-rop
-- Using C++ security hardening flags:  -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -fstack-protector -fstack-protector-strong -fcf-protection=full -fstack-clash-protection -mmitigate-rop
-- Using linker security hardening flags:  -pie -Wl,-z,relro -Wl,-z,now -Wl,-z,noexecstack
-- Found Boost Version: 106600
-- Found readline library at: /usr
-- Found Git: /usr/bin/git
-- Configuring incomplete, errors occurred!
See also "/home/jonny/rpmbuild/SOURCES/monero-0.13.0.3/build/CMakeFiles/CMakeOutput.log".
See also "/home/jonny/rpmbuild/SOURCES/monero-0.13.0.3/build/CMakeFiles/CMakeError.log".
```

# Discussion History
## moneromooo-monero | 2018-10-19T09:40:59+00:00
IIRC the use of system miniupnpc was discontinued because they weren't releasing security patches.

## hegjon | 2018-10-19T09:45:32+00:00
Do you have more information? I would like to investigate if Fedora and RHEL have included the security patches for the system package

## moneromooo-monero | 2018-10-19T09:47:31+00:00
I do not, but anonimal might. I will ask.

## hegjon | 2018-10-30T22:55:28+00:00
Any reply from anonimal?

## moneromooo-monero | 2018-10-31T01:20:23+00:00
Not so far. He did say he was going to be away often though.

## hegjon | 2019-02-15T23:41:11+00:00
Can anyone give information about the security issues + patches for miniupnpc? I am sure that the library distributed by most Linux distroes contains them, so it would be nice if we could override what library to use

## moneromooo-monero | 2019-02-16T16:38:57+00:00
anonimal seems offline atm, I'll ask again when I see him around.
However, since the tree monero uses is https://github.com/monero-project/miniupnp, the patches which were applied by "us" can probably be picked out.

## moneromooo-monero | 2019-06-15T10:46:46+00:00
I pinged him with this url several times in the past, I'll assume he just doesn't want to reply here.
The bug is fixed, so closing.

+resolved


# Action History
- Created by: hegjon | 2018-10-19T09:39:32+00:00
- Closed at: 2019-06-15T17:29:30+00:00
