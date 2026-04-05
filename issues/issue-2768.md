---
title: Crash on make -j$(nproc)
source_url: https://github.com/xmrig/xmrig/issues/2768
author: MoizEzzy
assignees: []
labels:
- bug
created_at: '2021-12-01T16:09:30+00:00'
updated_at: '2023-06-07T14:50:47+00:00'
type: issue
status: closed
closed_at: '2021-12-15T15:34:49+00:00'
---

# Original Description
[ 12%] Building CXX object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/ghostrider.cpp.o
Linking C static library libargon2.a
[ 12%] Built target argon2
/root/xmrig/src/crypto/ghostrider/ghostrider.cpp: In function ‘xmrig::ghostrider::HelperThread* xmrig::ghostrider::create_helper_thread(int64_t, const std::vector<long int>&)’:
/root/xmrig/src/crypto/ghostrider/ghostrider.cpp:488:26: error: ‘HWLOC_OBJ_L3CACHE’ was not declared in this scope
         findByType(root, HWLOC_OBJ_L3CACHE, [cpu_index, &is8MB](hwloc_obj_t obj) {
                          ^
/root/xmrig/src/crypto/ghostrider/ghostrider.cpp:512:48: error: ‘HWLOC_OBJ_L1CACHE’ was not declared in this scope
         for (auto obj_type : { HWLOC_OBJ_CORE, HWLOC_OBJ_L1CACHE, HWLOC_OBJ_L2CACHE, HWLOC_OBJ_L3CACHE }) {
                                                ^
/root/xmrig/src/crypto/ghostrider/ghostrider.cpp:512:67: error: ‘HWLOC_OBJ_L2CACHE’ was not declared in this scope
         for (auto obj_type : { HWLOC_OBJ_CORE, HWLOC_OBJ_L1CACHE, HWLOC_OBJ_L2CACHE, HWLOC_OBJ_L3CACHE }) {
                                                                   ^
/root/xmrig/src/crypto/ghostrider/ghostrider.cpp:512:104: error: unable to deduce ‘std::initializer_list<_Tp>&&’ from ‘{HWLOC_OBJ_CORE, <expression error>, <expression error>, HWLOC_OBJ_L3CACHE}’
         for (auto obj_type : { HWLOC_OBJ_CORE, HWLOC_OBJ_L1CACHE, HWLOC_OBJ_L2CACHE, HWLOC_OBJ_L3CACHE }) {
                                                                                                        ^
At global scope:
cc1plus: warning: unrecognized command line option "-Wno-class-memaccess" [enabled by default]
make[2]: *** [src/crypto/ghostrider/CMakeFiles/ghostrider.dir/ghostrider.cpp.o] Error 1
make[2]: *** Waiting for unfinished jobs....
make[1]: *** [src/crypto/ghostrider/CMakeFiles/ghostrider.dir/all] Error 2
make: *** [all] Error 2


# Discussion History
## Spudz76 | 2021-12-01T18:55:41+00:00
You need to either run a current OS or build the bundled deps so you have a workable version of hwloc.

## MoizEzzy | 2021-12-02T14:59:32+00:00
I followed the basic build in this doc https://xmrig.com/docs/miner/build/centos7 I wonder why it is still not working I didn't face such in other nodes though

## Spudz76 | 2021-12-02T15:14:36+00:00
If the other nodes didn't have GhostRider algo yet then this bug didn't exist.  Now it requires 2.4.x and CentOS 7 as usual is going antiquing with 1.11.8

Follow the advanced build on that same page.  Your other CentOS7 rigs will also require it if you pull the latest code (or you could disable GhostRider).

Running the bundled deps is preferred because then if you need further support we know we're all on the "same page".  Especially on an OS that refuses to have versions of things from the last 5 years.

## MoizEzzy | 2021-12-03T12:34:21+00:00
Yep, the advanced build worked, Thanks

# Action History
- Created by: MoizEzzy | 2021-12-01T16:09:30+00:00
- Closed at: 2021-12-15T15:34:49+00:00
