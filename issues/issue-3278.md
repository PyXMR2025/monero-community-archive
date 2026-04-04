---
title: Makefile warnings with Boost 1.66
source_url: https://github.com/monero-project/monero/issues/3278
author: ghost
assignees: []
labels:
- invalid
created_at: '2018-02-16T20:37:50+00:00'
updated_at: '2018-06-18T15:01:22+00:00'
type: issue
status: closed
closed_at: '2018-06-18T15:01:22+00:00'
---

# Original Description
```
CMake Warning at /usr/share/cmake-3.5/Modules/FindBoost.cmake:725 (message):
  Imported targets not available for Boost version 106600
Call Stack (most recent call first):
  /usr/share/cmake-3.5/Modules/FindBoost.cmake:763 (_Boost_COMPONENT_DEPENDENCIES)
  /usr/share/cmake-3.5/Modules/FindBoost.cmake:1332 (_Boost_MISSING_DEPENDENCIES)
  CMakeLists.txt:777 (find_package)


CMake Warning at /usr/share/cmake-3.5/Modules/FindBoost.cmake:725 (message):
  Imported targets not available for Boost version 106600
Call Stack (most recent call first):
  /usr/share/cmake-3.5/Modules/FindBoost.cmake:763 (_Boost_COMPONENT_DEPENDENCIES)
  /usr/share/cmake-3.5/Modules/FindBoost.cmake:1332 (_Boost_MISSING_DEPENDENCIES)
  CMakeLists.txt:777 (find_package)


CMake Warning at /usr/share/cmake-3.5/Modules/FindBoost.cmake:725 (message):
  Imported targets not available for Boost version 106600
Call Stack (most recent call first):
  /usr/share/cmake-3.5/Modules/FindBoost.cmake:763 (_Boost_COMPONENT_DEPENDENCIES)
  /usr/share/cmake-3.5/Modules/FindBoost.cmake:1332 (_Boost_MISSING_DEPENDENCIES)
  CMakeLists.txt:777 (find_package)


CMake Warning at /usr/share/cmake-3.5/Modules/FindBoost.cmake:725 (message):
  Imported targets not available for Boost version 106600
Call Stack (most recent call first):
  /usr/share/cmake-3.5/Modules/FindBoost.cmake:763 (_Boost_COMPONENT_DEPENDENCIES)
  /usr/share/cmake-3.5/Modules/FindBoost.cmake:1332 (_Boost_MISSING_DEPENDENCIES)
  CMakeLists.txt:777 (find_package)


CMake Warning at /usr/share/cmake-3.5/Modules/FindBoost.cmake:725 (message):
  Imported targets not available for Boost version 106600
Call Stack (most recent call first):
  /usr/share/cmake-3.5/Modules/FindBoost.cmake:763 (_Boost_COMPONENT_DEPENDENCIES)
  /usr/share/cmake-3.5/Modules/FindBoost.cmake:1332 (_Boost_MISSING_DEPENDENCIES)
  CMakeLists.txt:777 (find_package)


CMake Warning at /usr/share/cmake-3.5/Modules/FindBoost.cmake:725 (message):
  Imported targets not available for Boost version 106600
Call Stack (most recent call first):
  /usr/share/cmake-3.5/Modules/FindBoost.cmake:763 (_Boost_COMPONENT_DEPENDENCIES)
  /usr/share/cmake-3.5/Modules/FindBoost.cmake:1332 (_Boost_MISSING_DEPENDENCIES)
  CMakeLists.txt:777 (find_package)


CMake Warning at /usr/share/cmake-3.5/Modules/FindBoost.cmake:725 (message):
  Imported targets not available for Boost version 106600
Call Stack (most recent call first):
  /usr/share/cmake-3.5/Modules/FindBoost.cmake:763 (_Boost_COMPONENT_DEPENDENCIES)
  /usr/share/cmake-3.5/Modules/FindBoost.cmake:1332 (_Boost_MISSING_DEPENDENCIES)
  CMakeLists.txt:777 (find_package)


CMake Warning at /usr/share/cmake-3.5/Modules/FindBoost.cmake:725 (message):
  Imported targets not available for Boost version 106600
Call Stack (most recent call first):
  /usr/share/cmake-3.5/Modules/FindBoost.cmake:763 (_Boost_COMPONENT_DEPENDENCIES)
  /usr/share/cmake-3.5/Modules/FindBoost.cmake:1332 (_Boost_MISSING_DEPENDENCIES)
  CMakeLists.txt:777 (find_package)


-- Found Boost Version: 106600
```

# Discussion History
## hyc | 2018-02-16T20:46:10+00:00
CMake 3.5's FindBoost module doesn't know about any versions newer than 1.61. Downgrade boost or upgrade cmake.

## iDunk5400 | 2018-02-16T21:29:26+00:00
Same thing with cmake 3.10.2. The build proceeds normaly. Ignore.

## ghost | 2018-02-17T19:00:04+00:00
The build does proceed normally, might leave this open in case others get worried

## moneromooo-monero | 2018-06-18T14:49:54+00:00
Nothing we can reasonably do.
+invalid


# Action History
- Created by: ghost | 2018-02-16T20:37:50+00:00
- Closed at: 2018-06-18T15:01:22+00:00
