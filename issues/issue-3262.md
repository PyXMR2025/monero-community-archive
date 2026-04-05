---
title: I have this error
source_url: https://github.com/xmrig/xmrig/issues/3262
author: valoudd
assignees: []
labels: []
created_at: '2023-04-24T16:58:00+00:00'
updated_at: '2025-06-18T22:37:05+00:00'
type: issue
status: closed
closed_at: '2025-06-18T22:37:05+00:00'
---

# Original Description
CMake Error at /usr/share/cmake-3.25/Modules/FindPackageHandleStandardArgs.cmake:230 (message):
  Could NOT find HWLOC (missing: HWLOC_LIBRARY HWLOC_INCLUDE_DIR)                                                                  
Call Stack (most recent call first):                                                                                               
  /usr/share/cmake-3.25/Modules/FindPackageHandleStandardArgs.cmake:600 (_FPHSA_FAILURE_MESSAGE)                                   
  cmake/FindHWLOC.cmake:25 (find_package_handle_standard_args)                                                                     
  src/backend/cpu/cpu.cmake:30 (find_package)                                                                                      
  src/backend/backend.cmake:1 (include)                                                                                            
  CMakeLists.txt:48 (include)               

# Discussion History
# Action History
- Created by: valoudd | 2023-04-24T16:58:00+00:00
- Closed at: 2025-06-18T22:37:05+00:00
