---
title: smart mining
source_url: https://github.com/monero-project/monero/issues/230
author: Gingeropolous
assignees: []
labels: []
created_at: '2015-02-20T03:05:46+00:00'
updated_at: '2015-11-24T14:48:18+00:00'
type: issue
status: closed
closed_at: '2015-11-24T14:48:18+00:00'
---

# Original Description
tried building orangejuice's smart mining. Need sigar library. impossible for noob to get sigar library. 

cd build/release && cmake -D BUILD_TESTS=ON -D CMAKE_BUILD_TYPE=release ../.. && make
-- Could not find DEVELOPER_LOCAL_TOOLS in env (not required)
-- BOOST_IGNORE_SYSTEM_PATHS defaults to OFF
-- Using miniupnpc from local source tree (/external/miniupnpc)
-- Looking for libunbound
-- Found libunbound include (unbound.h) in /usr/include
-- Found libunbound shared library
CMake Error at CMakeLists.txt:45 (message):
  **Sigar library wasn't found**
Call Stack (most recent call first):
  external/CMakeLists.txt:112 (die)

-- Configuring incomplete, errors occurred!
See also "/home/marty/bitmonero_smartmining/bitmonero/build/release/CMakeFiles/CMakeOutput.log".
See also "/home/marty/bitmonero_smartmining/bitmonero/build/release/CMakeFiles/CMakeError.log".
make: **\* [all-release] Error 1


# Discussion History
## fluffypony | 2015-11-24T14:48:18+00:00
Lots to be done before this can compile or be vaguely usable, closing this issue for the moment.


# Action History
- Created by: Gingeropolous | 2015-02-20T03:05:46+00:00
- Closed at: 2015-11-24T14:48:18+00:00
