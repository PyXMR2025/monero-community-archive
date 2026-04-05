---
title: Compile xmrig static in linux
source_url: https://github.com/xmrig/xmrig/issues/3274
author: SirKnightV
assignees: []
labels: []
created_at: '2023-05-24T05:41:40+00:00'
updated_at: '2023-05-24T08:12:10+00:00'
type: issue
status: closed
closed_at: '2023-05-24T06:29:25+00:00'
---

# Original Description
Hello, i'm some new with Compiling C and C++ files with cmake, i dont have use it before, i have trying compile xmrig source code with the next python3 code
```
import os
        os.system("sudo apt-get install libuv1-dev libssl-dev libhwloc-dev")
        os.system("sudo apt-get install git build-essential cmake libuv1-dev libssl-dev libhwloc-dev")
        os.system("sudo apt-get install git build-essential cmake automake libtool autoconf")
        os.system("sudo apt-get install build-essential cmake libuv1-dev libssl-dev libhwloc-dev libmicrohttpd-dev libcurl4-openssl-dev libjansson-dev")
        os.system("mkdir build")
        os.system("cd build && cmake .. && make -j$(nproc) ")
```
i have edited CMakeLists.txt with the next lines
```
cmake_minimum_required(VERSION 2.8.12)
project(xmrig)

option(WITH_HWLOC           "Enable hwloc support" ON)
option(WITH_CN_LITE         "Enable CryptoNight-Lite algorithms family" ON)
option(WITH_CN_HEAVY        "Enable CryptoNight-Heavy algorithms family" ON)
option(WITH_CN_PICO         "Enable CryptoNight-Pico algorithm" ON)
option(WITH_CN_FEMTO        "Enable CryptoNight-UPX2 algorithm" ON)
option(WITH_RANDOMX         "Enable RandomX algorithms family" ON)
option(WITH_ARGON2          "Enable Argon2 algorithms family" ON)
option(WITH_KAWPOW          "Enable KawPow algorithms family" ON)
option(WITH_GHOSTRIDER      "Enable GhostRider algorithm" ON)
option(WITH_HTTP            "Enable HTTP protocol support (client/server)" ON)
option(WITH_DEBUG_LOG       "Enable debug log output" OFF)
option(WITH_TLS             "Enable OpenSSL support" ON)
option(WITH_ASM             "Enable ASM PoW implementations" ON)
option(WITH_MSR             "Enable MSR mod & 1st-gen Ryzen fix" ON)
option(WITH_ENV_VARS        "Enable environment variables support in config file" ON)
option(WITH_EMBEDDED_CONFIG "Enable internal embedded JSON config" OFF)
option(WITH_OPENCL          "Enable OpenCL backend" ON)
set(WITH_OPENCL_VERSION 200 CACHE STRING "Target OpenCL version")
set_property(CACHE WITH_OPENCL_VERSION PROPERTY STRINGS 120 200 210 220)
option(WITH_CUDA            "Enable CUDA backend" ON)
option(WITH_NVML            "Enable NVML (NVIDIA Management Library) support (only if CUDA backend enabled)" ON)
option(WITH_ADL             "Enable ADL (AMD Display Library) or sysfs support (only if OpenCL backend enabled)" ON)
option(WITH_STRICT_CACHE    "Enable strict checks for OpenCL cache" ON)
option(WITH_INTERLEAVE_DEBUG_LOG "Enable debug log for threads interleave" OFF)
option(WITH_PROFILING       "Enable profiling for developers" OFF)
option(WITH_SSE4_1          "Enable SSE 4.1 for Blake2" ON)
option(WITH_AVX2            "Enable AVX2 for Blake2" ON)
option(WITH_VAES            "Enable VAES instructions for Cryptonight" ON)
option(WITH_BENCHMARK       "Enable builtin RandomX benchmark and stress test" ON)
option(WITH_SECURE_JIT      "Enable secure access to JIT memory" OFF)
option(WITH_DMI             "Enable DMI/SMBIOS reader" ON)

option(BUILD_STATIC         "Build static binary" ON)
option(ARM_TARGET           "Force use specific ARM target 8 or 7" 0)
option(HWLOC_DEBUG          "Enable hwloc debug helpers and log" OFF)


set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} "${CMAKE_SOURCE_DIR}/cmake")


include (CheckIncludeFile)
include (cmake/cpu.cmake)
include (cmake/os.cmake)
include (src/base/base.cmake)
include (src/backend/backend.cmake)


set(HEADERS
    "${HEADERS_BASE}"
    "${HEADERS_BASE_HTTP}"
    "${HEADERS_BACKEND}"
    src/App.h
    src/core/config/Config_default.h
    src/core/config/Config_platform.h
    src/core/config/Config.h
    src/core/config/ConfigTransform.h
    src/core/config/usage.h
    src/core/Controller.h
    src/core/Miner.h
    src/core/Taskbar.h
    src/net/interfaces/IJobResultListener.h
    src/net/JobResult.h
    src/net/JobResults.h
    src/net/Network.h
    src/net/strategies/DonateStrategy.h
    src/Summary.h
    src/version.h
   )

set(HEADERS_CRYPTO
    src/backend/common/interfaces/IMemoryPool.h
    src/crypto/cn/asm/CryptonightR_template.h
    src/crypto/cn/c_blake256.h
    src/crypto/cn/c_groestl.h
    src/crypto/cn/c_jh.h
    src/crypto/cn/c_skein.h
    src/crypto/cn/CnAlgo.h
    src/crypto/cn/CnCtx.h
    src/crypto/cn/CnHash.h
    src/crypto/cn/CryptoNight_monero.h
    src/crypto/cn/CryptoNight_test.h
    src/crypto/cn/CryptoNight.h
    src/crypto/cn/groestl_tables.h
    src/crypto/cn/hash.h
    src/crypto/cn/skein_port.h
    src/crypto/cn/soft_aes.h
    src/crypto/common/HugePagesInfo.h
    src/crypto/common/MemoryPool.h
    src/crypto/common/Nonce.h
    src/crypto/common/portable/mm_malloc.h
    src/crypto/common/VirtualMemory.h
   )

if (XMRIG_ARM)
    set(HEADERS_CRYPTO "${HEADERS_CRYPTO}" src/crypto/cn/CryptoNight_arm.h)
else()
    set(HEADERS_CRYPTO "${HEADERS_CRYPTO}" src/crypto/cn/CryptoNight_x86.h)
endif()

set(SOURCES
    "${SOURCES_BASE}"
    "${SOURCES_BASE_HTTP}"
    "${SOURCES_BACKEND}"
    src/App.cpp
    src/core/config/Config.cpp
    src/core/config/ConfigTransform.cpp
    src/core/Controller.cpp
    src/core/Miner.cpp
    src/core/Taskbar.cpp
    src/net/JobResults.cpp
    src/net/Network.cpp
    src/net/strategies/DonateStrategy.cpp
    src/Summary.cpp
    src/xmrig.cpp
   )

set(SOURCES_CRYPTO
    src/crypto/cn/c_blake256.c
    src/crypto/cn/c_groestl.c
    src/crypto/cn/c_jh.c
    src/crypto/cn/c_skein.c
    src/crypto/cn/CnCtx.cpp
    src/crypto/cn/CnHash.cpp
    src/crypto/common/HugePagesInfo.cpp
    src/crypto/common/MemoryPool.cpp
    src/crypto/common/Nonce.cpp
    src/crypto/common/VirtualMemory.cpp
   )

if (CMAKE_C_COMPILER_ID MATCHES GNU)
    set_source_files_properties(src/crypto/cn/CnHash.cpp PROPERTIES COMPILE_FLAGS "-Ofast -fno-tree-vectorize")
endif()

if (WITH_VAES)
    add_definitions(-DXMRIG_VAES)
    set(HEADERS_CRYPTO "${HEADERS_CRYPTO}" src/crypto/cn/CryptoNight_x86_vaes.h)
    set(SOURCES_CRYPTO "${SOURCES_CRYPTO}" src/crypto/cn/CryptoNight_x86_vaes.cpp)
    if (CMAKE_C_COMPILER_ID MATCHES GNU OR CMAKE_C_COMPILER_ID MATCHES Clang)
        set_source_files_properties(src/crypto/cn/CryptoNight_x86_vaes.cpp PROPERTIES COMPILE_FLAGS "-Ofast -fno-tree-vectorize -mavx2 -mvaes")
    endif()
endif()

if (WITH_HWLOC)
    list(APPEND HEADERS_CRYPTO
        src/crypto/common/NUMAMemoryPool.h
        )

    list(APPEND SOURCES_CRYPTO
        src/crypto/common/NUMAMemoryPool.cpp
        src/crypto/common/VirtualMemory_hwloc.cpp
        )
endif()

if (XMRIG_OS_WIN)
    list(APPEND SOURCES_OS
        res/app.rc
        src/App_win.cpp
        src/crypto/common/VirtualMemory_win.cpp
        )

    set(EXTRA_LIBS ws2_32 psapi iphlpapi userenv)
elseif (XMRIG_OS_APPLE)
    list(APPEND SOURCES_OS
        src/App_unix.cpp
        src/crypto/common/VirtualMemory_unix.cpp
        )

    find_library(IOKIT_LIBRARY IOKit)
    find_library(CORESERVICES_LIBRARY CoreServices)
    set(EXTRA_LIBS ${IOKIT_LIBRARY} ${CORESERVICES_LIBRARY})
else()
    list(APPEND SOURCES_OS
        src/App_unix.cpp
        src/crypto/common/VirtualMemory_unix.cpp
        )

    if (XMRIG_OS_ANDROID)
        set(EXTRA_LIBS pthread rt dl log)
    elseif (XMRIG_OS_LINUX)
        list(APPEND SOURCES_OS
            src/crypto/common/LinuxMemory.h
            src/crypto/common/LinuxMemory.cpp
            )

        set(EXTRA_LIBS pthread rt dl)
    elseif (XMRIG_OS_FREEBSD)
        set(EXTRA_LIBS kvm pthread)
    endif()
endif()

add_definitions(-DXMRIG_MINER_PROJECT -DXMRIG_JSON_SINGLE_LINE_ARRAY)
add_definitions(-D__STDC_FORMAT_MACROS -DUNICODE -D_FILE_OFFSET_BITS=64)

find_package(UV REQUIRED)

include(cmake/flags.cmake)
include(cmake/randomx.cmake)
include(cmake/argon2.cmake)
include(cmake/kawpow.cmake)
include(cmake/ghostrider.cmake)
include(cmake/OpenSSL.cmake)
include(cmake/asm.cmake)

if (WITH_CN_LITE)
    add_definitions(/DXMRIG_ALGO_CN_LITE)
endif()

if (WITH_CN_HEAVY)
    add_definitions(/DXMRIG_ALGO_CN_HEAVY)
endif()

if (WITH_CN_PICO)
    add_definitions(/DXMRIG_ALGO_CN_PICO)
endif()

if (WITH_CN_FEMTO)
    add_definitions(/DXMRIG_ALGO_CN_FEMTO)
endif()

if (WITH_EMBEDDED_CONFIG)
    add_definitions(/DXMRIG_FEATURE_EMBEDDED_CONFIG)
endif()

include(src/hw/api/api.cmake)
include(src/hw/dmi/dmi.cmake)

include_directories(src)
include_directories(src/3rdparty)
include_directories(${UV_INCLUDE_DIR})

if (WITH_DEBUG_LOG)
    add_definitions(/DAPP_DEBUG)
endif()
add_subdirectory(libs)
set(CMAKE_EXE_LINKER_FLAGS "-static-libgcc -static-libstdc++")
add_executable(${CMAKE_PROJECT_NAME} ${HEADERS} ${SOURCES} ${SOURCES_OS} ${HEADERS_CRYPTO} ${SOURCES_CRYPTO} ${SOURCES_SYSLOG} ${TLS_SOURCES} ${XMRIG_ASM_SOURCES})
target_link_libraries(${CMAKE_PROJECT_NAME}
    ${XMRIG_ASM_LIBRARY}
    ${OPENSSL_LIBRARIES}
    ${UV_LIBRARIES}
    ${EXTRA_LIBS}
    ${CPUID_LIB}
    ${ARGON2_LIBRARY}
    ${ETHASH_LIBRARY}
    ${GHOSTRIDER_LIBRARY}
    c m hwloc uv
)
if (WIN32)
    add_custom_command(TARGET ${CMAKE_PROJECT_NAME} POST_BUILD COMMAND ${CMAKE_COMMAND} -E copy_if_different "${CMAKE_SOURCE_DIR}/bin/WinRing0/WinRing0x64.sys" $<TARGET_FILE_DIR:${CMAKE_PROJECT_NAME}>)
    add_custom_command(TARGET ${CMAKE_PROJECT_NAME} POST_BUILD COMMAND ${CMAKE_COMMAND} -E copy_if_different "${CMAKE_SOURCE_DIR}/scripts/benchmark_1M.cmd" $<TARGET_FILE_DIR:${CMAKE_PROJECT_NAME}>)
    add_custom_command(TARGET ${CMAKE_PROJECT_NAME} POST_BUILD COMMAND ${CMAKE_COMMAND} -E copy_if_different "${CMAKE_SOURCE_DIR}/scripts/benchmark_10M.cmd" $<TARGET_FILE_DIR:${CMAKE_PROJECT_NAME}>)
    add_custom_command(TARGET ${CMAKE_PROJECT_NAME} POST_BUILD COMMAND ${CMAKE_COMMAND} -E copy_if_different "${CMAKE_SOURCE_DIR}/scripts/pool_mine_example.cmd" $<TARGET_FILE_DIR:${CMAKE_PROJECT_NAME}>)
    add_custom_command(TARGET ${CMAKE_PROJECT_NAME} POST_BUILD COMMAND ${CMAKE_COMMAND} -E copy_if_different "${CMAKE_SOURCE_DIR}/scripts/solo_mine_example.cmd" $<TARGET_FILE_DIR:${CMAKE_PROJECT_NAME}>)
    add_custom_command(TARGET ${CMAKE_PROJECT_NAME} POST_BUILD COMMAND ${CMAKE_COMMAND} -E copy_if_different "${CMAKE_SOURCE_DIR}/scripts/rtm_ghostrider_example.cmd" $<TARGET_FILE_DIR:${CMAKE_PROJECT_NAME}>)
endif()

if (CMAKE_CXX_COMPILER_ID MATCHES Clang AND CMAKE_BUILD_TYPE STREQUAL Release AND NOT CMAKE_GENERATOR STREQUAL Xcode)
    add_custom_command(TARGET ${PROJECT_NAME} POST_BUILD COMMAND ${CMAKE_STRIP} ${CMAKE_PROJECT_NAME})
endif()
```
I Have Tried copy the libraries finding them with the next command
`sudo find / -name "libc.so.6" -o -name "libm.so.6" -o -name "libhwloc.so.15" -o -name "libuv.so.1"`
Later i have coppy all libraries into new folder with name libs inside xmrig folder, and inside libs folder i have made the next CMakeLists.txt...
```
cmake_minimum_required(VERSION 3.0)
project(Librerias)

# Librería libc
add_library(c STATIC IMPORTED)
set_target_properties(c PROPERTIES IMPORTED_LOCATION libc.so.6)

# Librería libm
add_library(m STATIC IMPORTED)
set_target_properties(m PROPERTIES IMPORTED_LOCATION libm.so.6)

# Librería libhwloc
add_library(hwloc STATIC IMPORTED)
set_target_properties(hwloc PROPERTIES IMPORTED_LOCATION libhwloc.so.15)

# Librería libuv
add_library(uv STATIC IMPORTED)
set_target_properties(uv PROPERTIES IMPORTED_LOCATION libuv.so.1)

```
My Goal is compile the xmrig static with the libs that requires for run in other OS without depend if library is installed or not (for this reason i want compile it static), can anyone please guide for compile it statically with all libs that need for run in any other linux OS ?
Thanks for Read :)




# Discussion History
## SChernykh | 2023-05-24T05:47:42+00:00
See "Advanced build" in https://xmrig.com/docs/miner/build/ubuntu

## SirKnightV | 2023-05-24T05:49:31+00:00
> See "Advanced build" in https://xmrig.com/docs/miner/build/ubuntu

Going to check it , and will let you know if worked :) thanks

## SirKnightV | 2023-05-24T05:57:21+00:00
> See "Advanced build" in https://xmrig.com/docs/miner/build/ubuntu

i have tried advanced build, the steps i have followed in sudo mode got the next
Step 1:
`cd xmrig/scripts`
Step 2:
`sudo chmod +x *`
Step 3:
`bash build_deps.sh`
And my Output Got the next
```
bash build_deps.sh 

build_deps.sh: line 2: $'\r': command not found

: No such file or directoryild.uv.sh

: No such file or directoryild.hwloc.sh

: invalid option

```
and when i do `ls` my output is the next
```
/xmrig/scripts# ls

benchmark_10M.cmd  build.hwloc.sh     build.uv.sh          pool_mine_example.cmd

benchmark_1M.cmd   build.libressl.sh  enable_1gb_pages.sh  randomx_boost.sh

build_deps.sh      build.openssl3.sh  generate_cl.js       rtm_ghostrider_example.cmd

build.hwloc1.sh    build.openssl.sh   js                   solo_mine_example.cmd
```
:/


## SChernykh | 2023-05-24T06:01:20+00:00
> build_deps.sh: line 2: $'\r': command not found

You somehow corrupted the build script, or copied it from repository that was cloned on a Windows machine. Do everything on a Linux machine, starting from cloning the repository.

## SirKnightV | 2023-05-24T06:11:56+00:00
> > build_deps.sh: line 2: $'\r': command not found
> 
> You somehow corrupted the build script, or copied it from repository that was cloned on a Windows machine. Do everything on a Linux machine, starting from cloning the repository.

Hello again, i have git cloned again in ubuntu the repository and tried again the build_deps script and worked now :), will try compile statically with advanced options and let you know what happend, thanks :)

## SirKnightV | 2023-05-24T06:28:59+00:00
> > build_deps.sh: line 2: $'\r': command not found
> 
> You somehow corrupted the build script, or copied it from repository that was cloned on a Windows machine. Do everything on a Linux machine, starting from cloning the repository.

well now worked :)
i have made a python script for automate process this worked for me manually but i automated it with python if anyone need it, thanks same for help me :)
```
import os
        os.system("rm -rf build && rm -rf xmrig")
        os.system("sudo apt-get install libuv1-dev libssl-dev libhwloc-dev")
        os.system("sudo apt-get install git build-essential cmake libuv1-dev libssl-dev libhwloc-dev")
        os.system("sudo apt-get install git build-essential cmake automake libtool autoconf")
        os.system("sudo apt-get install build-essential cmake libuv1-dev libssl-dev libhwloc-dev libmicrohttpd-dev libcurl4-openssl-dev libjansson-dev")
        os.system("mkdir build")
        os.system("rm -rf scripts")
        os.system("git clone https://github.com/xmrig/xmrig.git && cd xmrig && mv scripts .. && cd .. && rm -rf xmrig")
        os.system("cd scripts && sudo chmod +x * && sudo bash build_deps.sh")
        os.system("cd build && cmake .. -DXMRIG_DEPS=scripts/deps && make -j$(nproc)")
```

# Action History
- Created by: SirKnightV | 2023-05-24T05:41:40+00:00
- Closed at: 2023-05-24T06:29:25+00:00
