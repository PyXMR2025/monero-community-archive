---
title: 'NetworkState.cpp:87: error: ''topDiff'' was not declared in this scope(Maybe
  Not Bug)'
source_url: https://github.com/xmrig/xmrig/issues/728
author: YongTianY
assignees: []
labels: []
created_at: '2018-08-01T07:03:38+00:00'
updated_at: '2018-11-05T13:56:36+00:00'
type: issue
status: closed
closed_at: '2018-11-05T13:56:36+00:00'
---

# Original Description
flags.cmake
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)
set(CMAKE_CXX_STANDARD 11)

if ("${CMAKE_BUILD_TYPE}" STREQUAL "")
    set(CMAKE_BUILD_TYPE Release)
endif()

if (CMAKE_BUILD_TYPE STREQUAL "Release")
    add_definitions(/DNDEBUG)
endif()

if (CMAKE_CXX_COMPILER_ID MATCHES GNU)

    set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -Wall -Wno-strict-aliasing")
    set(CMAKE_C_FLAGS_RELEASE "${CMAKE_C_FLAGS_RELEASE} ")

    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -fno-exceptions -fno-rtti")
    set(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE}  -s")

    if (XMRIG_ARMv8)
        set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -march=armv8-a+crypto")
        set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -march=armv8-a+crypto -flax-vector-conversions")
    elseif (XMRIG_ARMv7)
        set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -mfpu=neon")
        set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -mfpu=neon -flax-vector-conversions")
    else()
        set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} ")
        set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS}")
    endif()

    if (WIN32)
        set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} -static")
    else()
        set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} -static-libgcc -static-libstdc++")
    endif()

    add_definitions(/D_GNU_SOURCE)

    if (${CMAKE_VERSION} VERSION_LESS "3.1.0")
        set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")
    endif()

    #set(CMAKE_C_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE} -gdwarf-2")

elseif (CMAKE_CXX_COMPILER_ID MATCHES MSVC)

    set(CMAKE_C_FLAGS_RELEASE "${CMAKE_C_FLAGS_RELEASE} /Ox /Ot /Oi /MT /GL")
    set(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE} /Ox /Ot /Oi /MT /GL")
    add_definitions(/D_CRT_SECURE_NO_WARNINGS)
    add_definitions(/D_CRT_NONSTDC_NO_WARNINGS)
    add_definitions(/DNOMINMAX)

elseif (CMAKE_CXX_COMPILER_ID MATCHES Clang)

    set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -Wall")
    set(CMAKE_C_FLAGS_RELEASE "${CMAKE_C_FLAGS_RELEASE} -Ofast -funroll-loops -fmerge-all-constants")

    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -fno-exceptions -fno-rtti -Wno-missing-braces")
    set(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE} -Ofast -funroll-loops -fmerge-all-constants")

    if (XMRIG_ARMv8)
        set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -march=armv8-a+crypto")
        set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -march=armv8-a+crypto")
    elseif (XMRIG_ARMv7)
        set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -mfpu=neon -march=${CMAKE_SYSTEM_PROCESSOR}")
        set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -mfpu=neon -march=${CMAKE_SYSTEM_PROCESSOR}")
    else()
        set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -maes")
        set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -maes")
    endif()

endif()

remove -maes in cflags.cmake

cmake .. -DCMAKE_C_COMPILER=arm-linux-gcc -DCMAKE_CXX_COMPILER=arm-linux-g++ -DUV_LIBRARY=/home/leaf/libuv-v1.9.1/out/lib/libvu.a -DWITH_HTTPD=OFF -DCMAKE_SYSTEM_PROCESSOR=armv7 -DUV_INCLUDE_DIR=/home/leaf/libuv-v1.9.1/out/include

In file included from /home/leaf/xmrig-2.6.4/src/api/NetworkState.cpp:31:
/home/leaf/xmrig-2.6.4/src/api/NetworkState.h:48: error: function definition does not declare parameters
/home/leaf/xmrig-2.6.4/src/api/NetworkState.cpp: In member function 'void NetworkState::add(const SubmitResult&, const char*)':
/home/leaf/xmrig-2.6.4/src/api/NetworkState.cpp:87: error: 'topDiff' was not declared in this scope
make[2]: *** [CMakeFiles/xmrig.dir/src/api/NetworkState.cpp.o] Error 1
make[1]: *** [CMakeFiles/xmrig.dir/all] Error 2


# Discussion History
# Action History
- Created by: YongTianY | 2018-08-01T07:03:38+00:00
- Closed at: 2018-11-05T13:56:36+00:00
