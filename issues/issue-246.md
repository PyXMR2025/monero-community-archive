---
title: cmake miniupnpc filename case mismatch
source_url: https://github.com/monero-project/monero/issues/246
author: meshpoint
assignees: []
labels: []
created_at: '2015-03-26T07:41:37+00:00'
updated_at: '2015-03-26T11:52:09+00:00'
type: issue
status: closed
closed_at: '2015-03-26T11:52:09+00:00'
---

# Original Description
CMake 3.2.1 cannot find shared miniupnpc when building on a case-sensitive filesystem.

> CMake Warning at external/CMakeLists.txt:38 (find_package):
>  By not providing "FindMiniUpnpc.cmake" in CMAKE_MODULE_PATH this project
>  has asked CMake to find a package configuration file provided by
>  "MiniUpnpc", but CMake did not find one.

```
find_package(MiniUpnpc QUIET)
   cmake/FindMiniupnpc.cmake
```


# Discussion History
## fluffypony | 2015-03-26T07:48:51+00:00
Nice catch - would you like to submit a fix via PR so you get credit for it? You can either rename the .cmake file or change the line in external/CMakeLists.txt, there's no knock-on effect for either and there's no preference for one route over another.


## meshpoint | 2015-03-26T11:35:05+00:00
Other projects seem to spell it FindMiniupnpc.cmake


# Action History
- Created by: meshpoint | 2015-03-26T07:41:37+00:00
- Closed at: 2015-03-26T11:52:09+00:00
