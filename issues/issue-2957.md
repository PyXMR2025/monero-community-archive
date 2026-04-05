---
title: 'cc1plus: warning: unrecognized command line option ‘-Wno-class-memaccess’'
source_url: https://github.com/xmrig/xmrig/issues/2957
author: h053698
assignees: []
labels:
- bug
created_at: '2022-03-07T14:48:07+00:00'
updated_at: '2023-06-07T14:50:10+00:00'
type: issue
status: closed
closed_at: '2023-06-07T14:50:02+00:00'
---

# Original Description
gcc version: 8.4.0
operating system: ubuntu-18.04-x86_64

https://xmrig.com/docs/miner/build/ubuntu
I followed the Basic build tutorial above but got the error below.
Up to the ``cmake ..`` in item 4 was executed, but an error occurred in item 5.

https://github.com/xmrig/xmrig/issues/980
> I used GCC 8.4.0 version by referring to the issue, but it was not resolved.

error:
```bash
[  2%] Built target xmrig-asm
[  3%] Building CXX object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/ghostrider.cpp.o
/home/hash-mine/xmrig/src/crypto/ghostrider/ghostrider.cpp: In function ‘xmrig::ghostrider::HelperThread* xmrig::ghostrider::create_helper_thread(int64_t, int, const std::vector<long int>&)’:
/home/hash-mine/xmrig/src/crypto/ghostrider/ghostrider.cpp:490:26: error: ‘HWLOC_OBJ_L3CACHE’ was not declared in this scope
         findByType(root, HWLOC_OBJ_L3CACHE, [cpu_index, &is8MB](hwloc_obj_t obj) {
                          ^~~~~~~~~~~~~~~~~
/home/hash-mine/xmrig/src/crypto/ghostrider/ghostrider.cpp:490:26: note: suggested alternative: ‘HWLOC_OBJ_CACHE’
         findByType(root, HWLOC_OBJ_L3CACHE, [cpu_index, &is8MB](hwloc_obj_t obj) {
                          ^~~~~~~~~~~~~~~~~
                          HWLOC_OBJ_CACHE
/home/hash-mine/xmrig/src/crypto/ghostrider/ghostrider.cpp:514:48: error: ‘HWLOC_OBJ_L1CACHE’ was not declared in this scope
         for (auto obj_type : { HWLOC_OBJ_CORE, HWLOC_OBJ_L1CACHE, HWLOC_OBJ_L2CACHE, HWLOC_OBJ_L3CACHE }) {
                                                ^~~~~~~~~~~~~~~~~
/home/hash-mine/xmrig/src/crypto/ghostrider/ghostrider.cpp:514:48: note: suggested alternative: ‘HWLOC_OBJ_CACHE’
         for (auto obj_type : { HWLOC_OBJ_CORE, HWLOC_OBJ_L1CACHE, HWLOC_OBJ_L2CACHE, HWLOC_OBJ_L3CACHE }) {
                                                ^~~~~~~~~~~~~~~~~
                                                HWLOC_OBJ_CACHE
/home/hash-mine/xmrig/src/crypto/ghostrider/ghostrider.cpp:514:67: error: ‘HWLOC_OBJ_L2CACHE’ was not declared in this scope
         for (auto obj_type : { HWLOC_OBJ_CORE, HWLOC_OBJ_L1CACHE, HWLOC_OBJ_L2CACHE, HWLOC_OBJ_L3CACHE }) {
                                                                   ^~~~~~~~~~~~~~~~~
/home/hash-mine/xmrig/src/crypto/ghostrider/ghostrider.cpp:514:67: note: suggested alternative: ‘HWLOC_OBJ_CACHE’
         for (auto obj_type : { HWLOC_OBJ_CORE, HWLOC_OBJ_L1CACHE, HWLOC_OBJ_L2CACHE, HWLOC_OBJ_L3CACHE }) {
                                                                   ^~~~~~~~~~~~~~~~~
                                                                   HWLOC_OBJ_CACHE
/home/hash-mine/xmrig/src/crypto/ghostrider/ghostrider.cpp:514:104: error: unable to deduce ‘std::initializer_list<_Tp>&&’ from ‘{HWLOC_OBJ_CORE, <expression error>, <expression error>, HWLOC_OBJ_L3CACHE}’
         for (auto obj_type : { HWLOC_OBJ_CORE, HWLOC_OBJ_L1CACHE, HWLOC_OBJ_L2CACHE, HWLOC_OBJ_L3CACHE }) {
                                                                                                        ^
At global scope:
cc1plus: warning: unrecognized command line option ‘-Wno-class-memaccess’
src/crypto/ghostrider/CMakeFiles/ghostrider.dir/build.make:446: recipe for target 'src/crypto/ghostrider/CMakeFiles/ghostrider.dir/ghostrider.cpp.o' failed
make[2]: *** [src/crypto/ghostrider/CMakeFiles/ghostrider.dir/ghostrider.cpp.o] Error 1
CMakeFiles/Makefile2:476: recipe for target 'src/crypto/ghostrider/CMakeFiles/ghostrider.dir/all' failed
make[1]: *** [src/crypto/ghostrider/CMakeFiles/ghostrider.dir/all] Error 2
Makefile:83: recipe for target 'all' failed
make: *** [all] Error 2
```
How do I solve this problem?

# Discussion History
## Spudz76 | 2022-03-07T18:33:17+00:00
Your OS-provided hwloc library is too old (pre-v2)

Either disable ghostrider (`-DWITH_GHOSTRIDER=OFF`) or use the advanced build so it uses the bundled versions of hwloc/openssl/libuv instead of outdated OS-provided ones.  Or update OS to one that includes a recent hwloc.  Ubuntu Focal (20.04) for example has v2.1.0 which will work.

But really you should always use the advanced build everywhere, so that you have a known-same setup as everyone else regardless of OS.

## Spudz76 | 2022-03-07T18:34:30+00:00
Also the warning is not why it crashes, that comes up normally and is ignored.

## xmrig | 2023-06-07T14:50:02+00:00
#2927

# Action History
- Created by: h053698 | 2022-03-07T14:48:07+00:00
- Closed at: 2023-06-07T14:50:02+00:00
