---
title: xmrig fails to Build on ubuntu 18.04
source_url: https://github.com/xmrig/xmrig/issues/3155
author: k7n2g
assignees: []
labels:
- bug
created_at: '2022-11-04T02:27:26+00:00'
updated_at: '2023-06-07T14:49:13+00:00'
type: issue
status: closed
closed_at: '2023-06-07T14:49:13+00:00'
---

# Original Description
Hello new xmrig build fails with Advanced build  and basic Build  gives this and github certificate failed to get,  i take it a dependency failed to download from GitHub  cmake ..  builds okay no problem,  Not sure what to do with this one tried downloading three times still fails.


[ 15%] Building CXX object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/ghostrider.cpp.o
/var/www/xmrig/src/crypto/ghostrider/ghostrider.cpp: In function ‘xmrig::ghostrider::HelperThread* xmrig::ghostrider::create_helper_thread(int64_t, int, const std::vector<long int>&)’:
/var/www/xmrig/src/crypto/ghostrider/ghostrider.cpp:490:26: error: ‘HWLOC_OBJ_L3CACHE’ was not declared in this scope
         findByType(root, HWLOC_OBJ_L3CACHE, [cpu_index, &is8MB](hwloc_obj_t obj) {
                          ^~~~~~~~~~~~~~~~~
/var/www/xmrig/src/crypto/ghostrider/ghostrider.cpp:490:26: note: suggested alternative: ‘HWLOC_OBJ_CACHE’
         findByType(root, HWLOC_OBJ_L3CACHE, [cpu_index, &is8MB](hwloc_obj_t obj) {
                          ^~~~~~~~~~~~~~~~~
                          HWLOC_OBJ_CACHE
/var/www/xmrig/src/crypto/ghostrider/ghostrider.cpp:514:48: error: ‘HWLOC_OBJ_L1CACHE’ was not declared in this scope
         for (auto obj_type : { HWLOC_OBJ_CORE, HWLOC_OBJ_L1CACHE, HWLOC_OBJ_L2CACHE, HWLOC_OBJ_L3CACHE }) {
                                                ^~~~~~~~~~~~~~~~~
/var/www/xmrig/src/crypto/ghostrider/ghostrider.cpp:514:48: note: suggested alternative: ‘HWLOC_OBJ_CACHE’
         for (auto obj_type : { HWLOC_OBJ_CORE, HWLOC_OBJ_L1CACHE, HWLOC_OBJ_L2CACHE, HWLOC_OBJ_L3CACHE }) {
                                                ^~~~~~~~~~~~~~~~~
                                                HWLOC_OBJ_CACHE
/var/www/xmrig/src/crypto/ghostrider/ghostrider.cpp:514:67: error: ‘HWLOC_OBJ_L2CACHE’ was not declared in this scope
         for (auto obj_type : { HWLOC_OBJ_CORE, HWLOC_OBJ_L1CACHE, HWLOC_OBJ_L2CACHE, HWLOC_OBJ_L3CACHE }) {
                                                                   ^~~~~~~~~~~~~~~~~
/var/www/xmrig/src/crypto/ghostrider/ghostrider.cpp:514:67: note: suggested alternative: ‘HWLOC_OBJ_CACHE’
         for (auto obj_type : { HWLOC_OBJ_CORE, HWLOC_OBJ_L1CACHE, HWLOC_OBJ_L2CACHE, HWLOC_OBJ_L3CACHE }) {
                                                                   ^~~~~~~~~~~~~~~~~
                                                                   HWLOC_OBJ_CACHE
/var/www/xmrig/src/crypto/ghostrider/ghostrider.cpp:514:104: error: unable to deduce ‘std::initializer_list<_Tp>&&’ from ‘{HWLOC_OBJ_CORE, <expression error>, <expression error>, HWLOC_OBJ_L3CACHE}’
         for (auto obj_type : { HWLOC_OBJ_CORE, HWLOC_OBJ_L1CACHE, HWLOC_OBJ_L2CACHE, HWLOC_OBJ_L3CACHE }) {
                                                                                                        ^
At global scope:
cc1plus: warning: unrecognized command line option ‘-Wno-class-memaccess’
src/crypto/ghostrider/CMakeFiles/ghostrider.dir/build.make:299: recipe for target 'src/crypto/ghostrider/CMakeFiles/ghostrider.dir/ghostrider.cpp.o' failed
make[2]: *** [src/crypto/ghostrider/CMakeFiles/ghostrider.dir/ghostrider.cpp.o] Error 1
make[2]: *** Waiting for unfinished jobs....
CMakeFiles/Makefile2:393: recipe for target 'src/crypto/ghostrider/CMakeFiles/ghostrider.dir/all' failed
make[1]: *** [src/crypto/ghostrider/CMakeFiles/ghostrider.dir/all] Error 2
Makefile:90: recipe for target 'all' failed
make: *** [all] Error 2
root@vmi574546:/var/www/xmrig/build#


# Discussion History
## Spudz76 | 2022-11-04T11:07:37+00:00
You have to use hwloc 2.x+, you must be building against the system provided `hwloc-dev` which is 1.x

So however you're doing the Advanced Buld and then telling CMake where those deps are must be wrong (remove `openssl-dev`, `libuv-dev`, `hwloc-dev`... then CMake will crash until you get the commands right).

Also you have to delete the build dir contents between giving new/different CMake args.  You may have to give the full qualified path to the deps rather than relative path.  The option would be like `-DXMRIG_DEPS=/var/www/xmrig/scripts/deps`.  And you shall have already run `cd scripts && ./build_deps.sh` or there will be no `scripts/deps` and it will silently find other (system) versions instead.

## k7n2g | 2022-11-04T12:08:03+00:00
Okay got it thanks for that much appreciated

## mckaygerhard | 2022-12-09T02:30:39+00:00
stupid feature .. just disable the ghostrider.. https://github.com/xmrig/xmrig/issues/2739#issuecomment-983368151

## Spudz76 | 2022-12-09T02:59:03+00:00
Or, you know, run something that was made in the last couple years not some antique junk.

## mckaygerhard | 2022-12-09T11:29:56+00:00
the antique junk just works and in some text for strange reason provide 200 Hks more rather something more modern.. that's why i used.. 

with the patch provided just works https://github.com/xmrig/xmrig/issues/3175#issuecomment-1343777285

## xmrig | 2023-06-07T14:49:13+00:00
#2927

# Action History
- Created by: k7n2g | 2022-11-04T02:27:26+00:00
- Closed at: 2023-06-07T14:49:13+00:00
