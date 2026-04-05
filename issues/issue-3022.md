---
title: The CXX compiler identification is unknown
source_url: https://github.com/xmrig/xmrig/issues/3022
author: Xargana
assignees: []
labels: []
created_at: '2022-04-16T08:12:20+00:00'
updated_at: '2022-04-16T14:05:38+00:00'
type: issue
status: closed
closed_at: '2022-04-16T14:05:38+00:00'
---

# Original Description
when  i run the command "cmake .." it gives an error saying, The CXX compiler identification is unknown


-- The CXX compiler identification is unknown
   Called from: [3]	/usr/share/cmake-3.16/Modules/CMakeDetermineCompilerId.cmake
                [2]	/usr/share/cmake-3.16/Modules/CMakeDetermineCXXCompiler.cmake
                [1]	/home/merta/Masaüstü/mine/xmrig/CMakeLists.txt
CMake Error at CMakeLists.txt:2 (project):
  No CMAKE_CXX_COMPILER could be found.

  Tell CMake where to find the compiler by setting either the environment
  variable "CXX" or the CMake cache entry CMAKE_CXX_COMPILER to the full path
  to the compiler, or to the compiler name if it is in the PATH.

i dont know that much of coding. please help




# Discussion History
## Spudz76 | 2022-04-16T08:25:45+00:00
`apt install build-essential` and such?

## Xargana | 2022-04-16T10:01:43+00:00
and now its missing HWLOC_LIBRARY HWLOC_INCLUDE_DIR is there a library i need to install?


## Xargana | 2022-04-16T14:05:38+00:00
i found how to do it. thanks for help

# Action History
- Created by: Xargana | 2022-04-16T08:12:20+00:00
- Closed at: 2022-04-16T14:05:38+00:00
