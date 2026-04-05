---
title: FreeBSD, cant build, hwloc + ghostrider
source_url: https://github.com/xmrig/xmrig/issues/2829
author: dawidmosk
assignees: []
labels:
- bug
created_at: '2021-12-22T12:12:58+00:00'
updated_at: '2023-06-07T14:50:38+00:00'
type: issue
status: closed
closed_at: '2021-12-29T23:38:02+00:00'
---

# Original Description
`[  8%] Built target xmrig-asm
[  8%] Building CXX object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/ghostrider.cpp.o
Consolidate compiler generated dependencies of target argon2
[ 11%] Built target argon2
/root/rtm/xmrig/src/crypto/ghostrider/ghostrider.cpp:486:26: error: use of undeclared identifier 'HWLOC_OBJ_L3CACHE'; did you mean 'HWLOC_OBJ_CACHE'?
        findByType(root, HWLOC_OBJ_L3CACHE, [cpu_index, &is8MB](hwloc_obj_t obj) {
                         ^~~~~~~~~~~~~~~~~
                         HWLOC_OBJ_CACHE
/root/rtm/xmrig/scripts/deps/include/hwloc.h:204:3: note: 'HWLOC_OBJ_CACHE' declared here
  HWLOC_OBJ_CACHE,      /**< \brief Cache.
  ^
/root/rtm/xmrig/src/crypto/ghostrider/ghostrider.cpp:510:48: error: use of undeclared identifier 'HWLOC_OBJ_L1CACHE'; did you mean 'HWLOC_OBJ_CACHE'?
        for (auto obj_type : { HWLOC_OBJ_CORE, HWLOC_OBJ_L1CACHE, HWLOC_OBJ_L2CACHE, HWLOC_OBJ_L3CACHE }) {
                                               ^~~~~~~~~~~~~~~~~
                                               HWLOC_OBJ_CACHE
/root/rtm/xmrig/scripts/deps/include/hwloc.h:204:3: note: 'HWLOC_OBJ_CACHE' declared here
  HWLOC_OBJ_CACHE,      /**< \brief Cache.
  ^
/root/rtm/xmrig/src/crypto/ghostrider/ghostrider.cpp:510:67: error: use of undeclared identifier 'HWLOC_OBJ_L2CACHE'; did you mean 'HWLOC_OBJ_CACHE'?
        for (auto obj_type : { HWLOC_OBJ_CORE, HWLOC_OBJ_L1CACHE, HWLOC_OBJ_L2CACHE, HWLOC_OBJ_L3CACHE }) {
                                                                  ^~~~~~~~~~~~~~~~~
                                                                  HWLOC_OBJ_CACHE
/root/rtm/xmrig/scripts/deps/include/hwloc.h:204:3: note: 'HWLOC_OBJ_CACHE' declared here
  HWLOC_OBJ_CACHE,      /**< \brief Cache.
  ^
/root/rtm/xmrig/src/crypto/ghostrider/ghostrider.cpp:510:86: error: use of undeclared identifier 'HWLOC_OBJ_L3CACHE'; did you mean 'HWLOC_OBJ_CACHE'?
        for (auto obj_type : { HWLOC_OBJ_CORE, HWLOC_OBJ_L1CACHE, HWLOC_OBJ_L2CACHE, HWLOC_OBJ_L3CACHE }) {
                                                                                     ^~~~~~~~~~~~~~~~~
                                                                                     HWLOC_OBJ_CACHE
/root/rtm/xmrig/scripts/deps/include/hwloc.h:204:3: note: 'HWLOC_OBJ_CACHE' declared here
  HWLOC_OBJ_CACHE,      /**< \brief Cache.
  ^
/root/rtm/xmrig/src/crypto/ghostrider/ghostrider.cpp:573:30: warning: lambda capture 'n' is not required to be captured for this use [-Wunused-lambda-capture]
        helper->launch_task([n, av, data, size, &ctx_memory, ctx, &cn_indices, &core_indices, &tmp, output, tune]() {
                             ^~
1 warning and 4 errors generated.
--- src/crypto/ghostrider/CMakeFiles/ghostrider.dir/ghostrider.cpp.o ---
*** [src/crypto/ghostrider/CMakeFiles/ghostrider.dir/ghostrider.cpp.o] Error code 1

make[2]: stopped in /root/rtm/xmrig/build
1 error

make[2]: stopped in /root/rtm/xmrig/build
--- src/crypto/ghostrider/CMakeFiles/ghostrider.dir/all ---
*** [src/crypto/ghostrider/CMakeFiles/ghostrider.dir/all] Error code 2

make[1]: stopped in /root/rtm/xmrig/build
1 error
`

hwloc1 or hwloc2 not working.


# Discussion History
## dawidmosk | 2021-12-29T23:38:02+00:00
Fixed now, thank You.

# Action History
- Created by: dawidmosk | 2021-12-22T12:12:58+00:00
- Closed at: 2021-12-29T23:38:02+00:00
