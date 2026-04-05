---
title: Problem when trying to build with Intel compiler
source_url: https://github.com/xmrig/xmrig/issues/3477
author: void-512
assignees: []
labels: []
created_at: '2024-05-10T01:12:36+00:00'
updated_at: '2024-05-13T12:26:58+00:00'
type: issue
status: closed
closed_at: '2024-05-13T12:26:57+00:00'
---

# Original Description
**Describe the bug**
[log.txt](https://github.com/xmrig/xmrig/files/15269163/log.txt)

**To Reproduce**

Added the following code in ./cmake/flags.cmake:

```
elseif (CMAKE_CXX_COMPILER_ID MATCHES Intel)

    set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -Ofast -mkl -march=native -mfma -Xclang -target-feature -Xclang +vaes")
    set(CMAKE_C_FLAGS_RELEASE "${CMAKE_C_FLAGS_RELEASE} -Ofast -mkl -march=native -mfma -Xclang -target-feature -Xclang +vaes")

    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Ofast -mkl -march=native -mfma -Xclang -target-feature -Xclang +vaes")
    set(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE} -Ofast -mkl -march=native -mfma -Xclang -target-feature -Xclang +vaes")
```

and use the following compile command:
`cmake .. -DCMAKE_C_COMPILER=icx -DCMAKE_CXX_COMPILER=icpx`

**Expected behavior**
Should compile successfully

**Required data**
 - XMRig 6.21.3
 - OS: Ubuntu2404


# Discussion History
## SChernykh | 2024-05-10T06:09:33+00:00
Intel compiler is not supported. Since you already started modifying CMake files, you should also add `HAVE_ROTR` check to `flags.cmake`
```
        check_symbol_exists("_rotr" "x86intrin.h" HAVE_ROTR)
        if (HAVE_ROTR)
            add_definitions(-DHAVE_ROTR)
        endif()
```

## void-512 | 2024-05-13T12:26:57+00:00
Thank you, compiled successfully with HAVE_ROTR above

# Action History
- Created by: void-512 | 2024-05-10T01:12:36+00:00
- Closed at: 2024-05-13T12:26:57+00:00
