---
title: make -j$(nproc) is not working on ubuntu 18.04
source_url: https://github.com/xmrig/xmrig/issues/2812
author: MoizEzzy
assignees: []
labels:
- bug
created_at: '2021-12-15T15:36:41+00:00'
updated_at: '2023-06-07T14:49:31+00:00'
type: issue
status: closed
closed_at: '2023-06-07T14:49:30+00:00'
---

# Original Description
[ 15%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/arch/x86_64/lib/argon2-arch.c.o
/root/xmrig/src/crypto/ghostrider/ghostrider.cpp: In function ‘xmrig::ghostrider::HelperThread* xmrig::ghostrider::create_helper_thread(int64_t, const std::vector<long int>&)’:
/root/xmrig/src/crypto/ghostrider/ghostrider.cpp:486:26: error: ‘HWLOC_OBJ_L3CACHE’ was not declared in this scope
         findByType(root, HWLOC_OBJ_L3CACHE, [cpu_index, &is8MB](hwloc_obj_t obj) {
                          ^~~~~~~~~~~~~~~~~
/root/xmrig/src/crypto/ghostrider/ghostrider.cpp:486:26: note: suggested alternative: ‘HWLOC_OBJ_CACHE’
         findByType(root, HWLOC_OBJ_L3CACHE, [cpu_index, &is8MB](hwloc_obj_t obj) {
                          ^~~~~~~~~~~~~~~~~
                          HWLOC_OBJ_CACHE
/root/xmrig/src/crypto/ghostrider/ghostrider.cpp:510:48: error: ‘HWLOC_OBJ_L1CACHE’ was not declared in this scope
         for (auto obj_type : { HWLOC_OBJ_CORE, HWLOC_OBJ_L1CACHE, HWLOC_OBJ_L2CACHE, HWLOC_OBJ_L3CACHE }) {
                                                ^~~~~~~~~~~~~~~~~
/root/xmrig/src/crypto/ghostrider/ghostrider.cpp:510:48: note: suggested alternative: ‘HWLOC_OBJ_CACHE’
         for (auto obj_type : { HWLOC_OBJ_CORE, HWLOC_OBJ_L1CACHE, HWLOC_OBJ_L2CACHE, HWLOC_OBJ_L3CACHE }) {
                                                ^~~~~~~~~~~~~~~~~
                                                HWLOC_OBJ_CACHE
/root/xmrig/src/crypto/ghostrider/ghostrider.cpp:510:67: error: ‘HWLOC_OBJ_L2CACHE’ was not declared in this scope
         for (auto obj_type : { HWLOC_OBJ_CORE, HWLOC_OBJ_L1CACHE, HWLOC_OBJ_L2CACHE, HWLOC_OBJ_L3CACHE }) {
                                                                   ^~~~~~~~~~~~~~~~~
/root/xmrig/src/crypto/ghostrider/ghostrider.cpp:510:67: note: suggested alternative: ‘HWLOC_OBJ_CACHE’
         for (auto obj_type : { HWLOC_OBJ_CORE, HWLOC_OBJ_L1CACHE, HWLOC_OBJ_L2CACHE, HWLOC_OBJ_L3CACHE }) {
                                                                   ^~~~~~~~~~~~~~~~~
                                                                   HWLOC_OBJ_CACHE
/root/xmrig/src/crypto/ghostrider/ghostrider.cpp:510:104: error: unable to deduce ‘std::initializer_list<_Tp>&&’ from ‘{HWLOC_OBJ_CORE, <expression error>, <expression error>, HWLOC_OBJ_L3CACHE}’
         for (auto obj_type : { HWLOC_OBJ_CORE, HWLOC_OBJ_L1CACHE, HWLOC_OBJ_L2CACHE, HWLOC_OBJ_L3CACHE }) {
                                                                                                        ^
At global scope:
cc1plus: warning: unrecognized command line option ‘-Wno-class-memaccess’
src/crypto/ghostrider/CMakeFiles/ghostrider.dir/build.make:446: recipe for target 'src/crypto/ghostrider/CMakeFiles/ghostrider.dir/ghostrider.cpp.o' failed
make[2]: *** [src/crypto/ghostrider/CMakeFiles/ghostrider.dir/ghostrider.cpp.o] Error 1
make[2]: *** Waiting for unfinished jobs....
[ 15%] Linking C static library libargon2.a
[ 15%] Built target argon2
CMakeFiles/Makefile2:476: recipe for target 'src/crypto/ghostrider/CMakeFiles/ghostrider.dir/all' failed
make[1]: *** [src/crypto/ghostrider/CMakeFiles/ghostrider.dir/all] Error 2
Makefile:83: recipe for target 'all' failed
make: *** [all] Error 2



I followed the below ubuntu build.
https://xmrig.com/docs/miner/build/ubuntu


# Discussion History
## Spudz76 | 2021-12-15T15:58:55+00:00
Use advanced, build_deps.sh

Your system hwloc is too old.

Or, use `-DWITH_GHOSTRIDER=OFF` since that's the only place the newer hwloc is "required".

## echoLOGNAME | 2021-12-18T17:30:46+00:00
Hello!  I'm using Ubuntu 16.04.7 and am having a similar error when I get to the "make -j$(nproc)" command in the ubuntu install guide (I used the advanced build) relating the ghostrider directory.  May I ask how I incorporate "-DWITH_GHOSTRIDER=OFF" to fix this?  It's not an option of the make command, so if I could please get some clarification on how I can resolve this issue, I would greatly appreciate it!

This is the full output for reference:

`[  2%] Built target ethash
[  4%] Built target argon2
[  4%] Building CXX object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/ghostrider.cpp.o
In file included from /home/echo/xmrig/src/crypto/ghostrider/ghostrider.cpp:57:0:
/home/echo/xmrig/src/crypto/ghostrider/../../crypto/cn/sse2neon.h: In function ‘uint64x2_t _sse2neon_vmull_p64(uint64x1_t, uint64x1_t)’:
/home/echo/xmrig/src/crypto/ghostrider/../../crypto/cn/sse2neon.h:7029:55: error: ‘vreinterpret_p64_u64’ was not declared in this scope
     poly64_t a = vget_lane_p64(vreinterpret_p64_u64(_a), 0);
                                                       ^
/home/echo/xmrig/src/crypto/ghostrider/../../crypto/cn/sse2neon.h:7029:59: error: ‘vget_lane_p64’ was not declared in this scope
     poly64_t a = vget_lane_p64(vreinterpret_p64_u64(_a), 0);
                                                           ^
/home/echo/xmrig/src/crypto/ghostrider/../../crypto/cn/sse2neon.h:7031:50: error: ‘vreinterpretq_u64_p128’ was not declared in this scope
     return vreinterpretq_u64_p128(vmull_p64(a, b));
                                                  ^
At global scope:
cc1plus: warning: unrecognized command line option ‘-Wno-class-memaccess’
src/crypto/ghostrider/CMakeFiles/ghostrider.dir/build.make:446: recipe for target 'src/crypto/ghostrider/CMakeFiles/ghostrider.dir/ghostrider.cpp.o' failed
make[2]: *** [src/crypto/ghostrider/CMakeFiles/ghostrider.dir/ghostrider.cpp.o] Error 1
CMakeFiles/Makefile2:234: recipe for target 'src/crypto/ghostrider/CMakeFiles/ghostrider.dir/all' failed
make[1]: *** [src/crypto/ghostrider/CMakeFiles/ghostrider.dir/all] Error 2
Makefile:83: recipe for target 'all' failed
make: *** [all] Error 2
`

## Spudz76 | 2021-12-18T22:40:25+00:00
`-D` additions go on the cmake command.

Some options require a fresh build dir (or at least delete CMakeCache.txt).

build_deps as outlined works too.

## echoLOGNAME | 2021-12-19T05:39:03+00:00
Thank you so much!

## MoizEzzy | 2021-12-19T08:19:25+00:00
> Use advanced, build_deps.sh
> 
> Your system hwloc is too old.
> 
> Or, use `-DWITH_GHOSTRIDER=OFF` since that's the only place the newer hwloc is "required".

Yep, advanced build worked for me too, however make sure to update the system ubuntu or centos i faced many issues and updating system fixed it, it is not mentioned in thu build page though

## xmrig | 2023-06-07T14:49:30+00:00
#2927

# Action History
- Created by: MoizEzzy | 2021-12-15T15:36:41+00:00
- Closed at: 2023-06-07T14:49:30+00:00
