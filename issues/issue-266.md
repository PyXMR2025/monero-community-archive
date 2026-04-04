---
title: Can't make
source_url: https://github.com/monero-project/monero/issues/266
author: Gingeropolous
assignees: []
labels: []
created_at: '2015-04-19T12:44:44+00:00'
updated_at: '2015-04-22T23:47:48+00:00'
type: issue
status: closed
closed_at: '2015-04-22T23:47:48+00:00'
---

# Original Description
This is on my machine that has faithfully been running tewinget's LMDB branch for over a month

http://pastebin.com/TFiJD7ki


# Discussion History
## Gingeropolous | 2015-04-22T02:44:11+00:00
Well, now its kicking out this:

-- Could not find DEVELOPER_LOCAL_TOOLS in env (not required)
-- BOOST_IGNORE_SYSTEM_PATHS defaults to OFF
-- Could not find DEVELOPER_LIBUNBOUND_OLD in env (not required)
-- Building for a 64-bit system
-- Could not find DATABASE in env (not required unless you want to change database type from default: lmdb)
-- Could not find miniupnp
-- Using miniupnpc from local source tree (/external/miniupnpc)
-- Looking for libunbound
-- Found libunbound include (unbound.h) in /usr/include
-- Found libunbound shared library
-- Using 64-bit LMDB from source tree
-- Could not find Berkeley DB >= 4.1 (missing:  BERKELEY_DB_INCLUDE_DIR BERKELEY_DB_LIBRARIES)
CMake Error at external/db_drivers/CMakeLists.txt:41 (add_subdirectory):
  add_subdirectory given source "libdb" which is not an existing directory.

-- BerkeleyDB not found, building from src tree
-- Enabling AES support
-- Found Git: /usr/bin/git
-- Could NOT find GTest (missing:  GTEST_LIBRARY GTEST_MAIN_LIBRARY)
Doxygen: graphviz not found - graphs disabled
-- Configuring incomplete, errors occurred!
See also "/home/e5405/bitmonero_latest/bitmonero/build/release/CMakeFiles/CMakeOutput.log".
See also "/home/e5405/bitmonero_latest/bitmonero/build/release/CMakeFiles/CMakeError.log".
make: **\* [release-all] Error 1
e5405@e5405-G31M-ES2L:~/bitmonero_latest/bitmonero$


## fluffypony | 2015-04-22T05:24:12+00:00
You need to install libgtest and libdb-dev / libdb++-dev


## Gingeropolous | 2015-04-22T10:49:58+00:00
hardware error?

http://pastebin.com/c2pPN6Wj


## Gingeropolous | 2015-04-22T23:47:48+00:00
Finally built. Ended up getting a fresh clone from master, and it built.  Yay. 


# Action History
- Created by: Gingeropolous | 2015-04-19T12:44:44+00:00
- Closed at: 2015-04-22T23:47:48+00:00
