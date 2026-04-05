---
title: 'error: ‘HWLOC_OBJ_L3CACHE’ was not declared in this scope'
source_url: https://github.com/xmrig/xmrig/issues/2739
author: minzak
assignees: []
labels:
- bug
created_at: '2021-11-28T18:39:42+00:00'
updated_at: '2023-03-08T01:31:53+00:00'
type: issue
status: closed
closed_at: '2022-07-14T09:56:30+00:00'
---

# Original Description
Typical Debian, and always all be fine except today.

```
gcc -v
Using built-in specs.
COLLECT_GCC=gcc
COLLECT_LTO_WRAPPER=/usr/lib/gcc/x86_64-linux-gnu/8/lto-wrapper
OFFLOAD_TARGET_NAMES=nvptx-none
OFFLOAD_TARGET_DEFAULT=1
Target: x86_64-linux-gnu
Configured with: ../src/configure -v --with-pkgversion='Debian 8.3.0-6' --with-bugurl=file:///usr/share/doc/gcc-8/README.Bugs --enable-languages=c,ada,c++,go,brig,d,fortran,objc,obj-c++ --prefix=/usr --with-gcc-major-version-only --program-suffix=-8 --program-prefix=x86_64-linux-gnu- --enable-shared --enable-linker-build-id --libexecdir=/usr/lib --without-included-gettext --enable-threads=posix --libdir=/usr/lib --enable-nls --enable-bootstrap --enable-clocale=gnu --enable-libstdcxx-debug --enable-libstdcxx-time=yes --with-default-libstdcxx-abi=new --enable-gnu-unique-object --disable-vtable-verify --enable-libmpx --enable-plugin --enable-default-pie --with-system-zlib --with-target-system-zlib --enable-objc-gc=auto --enable-multiarch --disable-werror --with-arch-32=i686 --with-abi=m64 --with-multilib-list=m32,m64,mx32 --enable-multilib --with-tune=generic --enable-offload-targets=nvptx-none --without-cuda-driver --enable-checking=release --build=x86_64-linux-gnu --host=x86_64-linux-gnu --target=x86_64-linux-gnu
Thread model: posix
gcc version 8.3.0 (Debian 8.3.0-6) 

```

```

Scanning dependencies of target argon2
[ 14%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/genkat.c.o
[ 14%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/blake2/blake2.c.o
[ 15%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/impl-select.c.o
[ 15%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/core.c.o
[ 15%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/argon2.c.o
[ 15%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/encoding.c.o
[ 15%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/arch/x86_64/lib/argon2-arch.c.o
/usr/local/src/xmrig/src/crypto/ghostrider/ghostrider.cpp: In function ‘xmrig::ghostrider::HelperThread* xmrig::ghostrider::create_helper_thread(int64_t, const std::vector<long int>&)’:
/usr/local/src/xmrig/src/crypto/ghostrider/ghostrider.cpp:488:26: error: ‘HWLOC_OBJ_L3CACHE’ was not declared in this scope
         findByType(root, HWLOC_OBJ_L3CACHE, [cpu_index, &is8MB](hwloc_obj_t obj) {
                          ^~~~~~~~~~~~~~~~~
/usr/local/src/xmrig/src/crypto/ghostrider/ghostrider.cpp:488:26: note: suggested alternative: ‘HWLOC_OBJ_CACHE’
         findByType(root, HWLOC_OBJ_L3CACHE, [cpu_index, &is8MB](hwloc_obj_t obj) {
                          ^~~~~~~~~~~~~~~~~
                          HWLOC_OBJ_CACHE
/usr/local/src/xmrig/src/crypto/ghostrider/ghostrider.cpp:512:48: error: ‘HWLOC_OBJ_L1CACHE’ was not declared in this scope
         for (auto obj_type : { HWLOC_OBJ_CORE, HWLOC_OBJ_L1CACHE, HWLOC_OBJ_L2CACHE, HWLOC_OBJ_L3CACHE }) {
                                                ^~~~~~~~~~~~~~~~~
[ 15%] Linking C static library libargon2.a
/usr/local/src/xmrig/src/crypto/ghostrider/ghostrider.cpp:512:48: note: suggested alternative: ‘HWLOC_OBJ_CACHE’
         for (auto obj_type : { HWLOC_OBJ_CORE, HWLOC_OBJ_L1CACHE, HWLOC_OBJ_L2CACHE, HWLOC_OBJ_L3CACHE }) {
                                                ^~~~~~~~~~~~~~~~~
                                                HWLOC_OBJ_CACHE
/usr/local/src/xmrig/src/crypto/ghostrider/ghostrider.cpp:512:67: error: ‘HWLOC_OBJ_L2CACHE’ was not declared in this scope
         for (auto obj_type : { HWLOC_OBJ_CORE, HWLOC_OBJ_L1CACHE, HWLOC_OBJ_L2CACHE, HWLOC_OBJ_L3CACHE }) {
                                                                   ^~~~~~~~~~~~~~~~~
/usr/local/src/xmrig/src/crypto/ghostrider/ghostrider.cpp:512:67: note: suggested alternative: ‘HWLOC_OBJ_CACHE’
         for (auto obj_type : { HWLOC_OBJ_CORE, HWLOC_OBJ_L1CACHE, HWLOC_OBJ_L2CACHE, HWLOC_OBJ_L3CACHE }) {
                                                                   ^~~~~~~~~~~~~~~~~
                                                                   HWLOC_OBJ_CACHE
/usr/local/src/xmrig/src/crypto/ghostrider/ghostrider.cpp:512:104: error: unable to deduce ‘std::initializer_list<_Tp>&&’ from ‘{HWLOC_OBJ_CORE, <expression error>, <expression error>, HWLOC_OBJ_L3CACHE}’
         for (auto obj_type : { HWLOC_OBJ_CORE, HWLOC_OBJ_L1CACHE, HWLOC_OBJ_L2CACHE, HWLOC_OBJ_L3CACHE }) {
                                                                                                        ^
[ 15%] Built target argon2
make[2]: *** [src/crypto/ghostrider/CMakeFiles/ghostrider.dir/build.make:271: src/crypto/ghostrider/CMakeFiles/ghostrider.dir/ghostrider.cpp.o] Error 1
make[2]: *** Waiting for unfinished jobs....
make[1]: *** [CMakeFiles/Makefile2:482: src/crypto/ghostrider/CMakeFiles/ghostrider.dir/all] Error 2
make: *** [Makefile:84: all] Error 2

```
What additional I may do for debugging this? 

# Discussion History
## Spudz76 | 2021-11-28T19:27:41+00:00
If using the `libhwloc-dev` from Debian it might be too old, try with the bundled versions of deps (as in Advanced section of [Ubuntu Build Docs](https://xmrig.com/docs/miner/build/ubuntu))

That gcc should be fine, I think I have it on some systems / but I never use the distro deps only the bundled.

## nebulous2 | 2021-11-28T23:02:07+00:00
Hello - I am experiencing the same exact error:

```
gcc -v
Using built-in specs.
COLLECT_GCC=gcc
COLLECT_LTO_WRAPPER=/usr/lib/gcc/x86_64-linux-gnu/7/lto-wrapper
OFFLOAD_TARGET_NAMES=nvptx-none
OFFLOAD_TARGET_DEFAULT=1
Target: x86_64-linux-gnu
Configured with: ../src/configure -v --with-pkgversion='Ubuntu 7.5.0-3ubuntu1~18.04' --with-bugurl=file:///usr/share/doc/gcc-7/README.Bugs --enable-languages=c,ada,c++,go,brig,d,fortran,objc,obj-c++ --prefix=/usr --with-gcc-major-version-only --program-suffix=-7 --program-prefix=x86_64-linux-gnu- --enable-shared --enable-linker-build-id --libexecdir=/usr/lib --without-included-gettext --enable-threads=posix --libdir=/usr/lib --enable-nls --enable-bootstrap --enable-clocale=gnu --enable-libstdcxx-debug --enable-libstdcxx-time=yes --with-default-libstdcxx-abi=new --enable-gnu-unique-object --disable-vtable-verify --enable-libmpx --enable-plugin --enable-default-pie --with-system-zlib --with-target-system-zlib --enable-objc-gc=auto --enable-multiarch --disable-werror --with-arch-32=i686 --with-abi=m64 --with-multilib-list=m32,m64,mx32 --enable-multilib --with-tune=generic --enable-offload-targets=nvptx-none --without-cuda-driver --enable-checking=release --build=x86_64-linux-gnu --host=x86_64-linux-gnu --target=x86_64-linux-gnu
Thread model: posix
gcc version 7.5.0 (Ubuntu 7.5.0-3ubuntu1~18.04) 
```
```
make -j$(nproc)
Consolidate compiler generated dependencies of target argon2-avx2
Consolidate compiler generated dependencies of target ghostrider
Consolidate compiler generated dependencies of target argon2-avx512f
Consolidate compiler generated dependencies of target ethash
Scanning dependencies of target xmrig-asm
Consolidate compiler generated dependencies of target argon2-sse2
Consolidate compiler generated dependencies of target argon2-xop
Consolidate compiler generated dependencies of target argon2-ssse3
[  0%] Built target argon2-sse2
[  3%] Built target xmrig-asm
[  3%] Built target argon2-avx2
[  4%] Built target argon2-xop
[  5%] Built target ethash
[  6%] Built target argon2-avx512f
[  7%] Built target argon2-ssse3
[  8%] Building CXX object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/ghostrider.cpp.o
Consolidate compiler generated dependencies of target argon2
[ 10%] Built target argon2
/home/ben/xmrig/src/crypto/ghostrider/ghostrider.cpp: In function ‘xmrig::ghostrider::HelperThread* xmrig::ghostrider::create_helper_thread(int64_t, const std::vector<long int>&)’:
/home/ben/xmrig/src/crypto/ghostrider/ghostrider.cpp:488:26: error: ‘HWLOC_OBJ_L3CACHE’ was not declared in this scope
         findByType(root, HWLOC_OBJ_L3CACHE, [cpu_index, &is8MB](hwloc_obj_t obj) {
                          ^~~~~~~~~~~~~~~~~
/home/ben/xmrig/src/crypto/ghostrider/ghostrider.cpp:488:26: note: suggested alternative: ‘HWLOC_OBJ_CACHE’
         findByType(root, HWLOC_OBJ_L3CACHE, [cpu_index, &is8MB](hwloc_obj_t obj) {
                          ^~~~~~~~~~~~~~~~~
                          HWLOC_OBJ_CACHE
/home/ben/xmrig/src/crypto/ghostrider/ghostrider.cpp:512:48: error: ‘HWLOC_OBJ_L1CACHE’ was not declared in this scope
         for (auto obj_type : { HWLOC_OBJ_CORE, HWLOC_OBJ_L1CACHE, HWLOC_OBJ_L2CACHE, HWLOC_OBJ_L3CACHE }) {
                                                ^~~~~~~~~~~~~~~~~
/home/ben/xmrig/src/crypto/ghostrider/ghostrider.cpp:512:48: note: suggested alternative: ‘HWLOC_OBJ_CACHE’
         for (auto obj_type : { HWLOC_OBJ_CORE, HWLOC_OBJ_L1CACHE, HWLOC_OBJ_L2CACHE, HWLOC_OBJ_L3CACHE }) {
                                                ^~~~~~~~~~~~~~~~~
                                                HWLOC_OBJ_CACHE
/home/ben/xmrig/src/crypto/ghostrider/ghostrider.cpp:512:67: error: ‘HWLOC_OBJ_L2CACHE’ was not declared in this scope
         for (auto obj_type : { HWLOC_OBJ_CORE, HWLOC_OBJ_L1CACHE, HWLOC_OBJ_L2CACHE, HWLOC_OBJ_L3CACHE }) {
                                                                   ^~~~~~~~~~~~~~~~~
/home/ben/xmrig/src/crypto/ghostrider/ghostrider.cpp:512:67: note: suggested alternative: ‘HWLOC_OBJ_CACHE’
         for (auto obj_type : { HWLOC_OBJ_CORE, HWLOC_OBJ_L1CACHE, HWLOC_OBJ_L2CACHE, HWLOC_OBJ_L3CACHE }) {
                                                                   ^~~~~~~~~~~~~~~~~
                                                                   HWLOC_OBJ_CACHE
/home/ben/xmrig/src/crypto/ghostrider/ghostrider.cpp:512:104: error: unable to deduce ‘std::initializer_list<_Tp>&&’ from ‘{HWLOC_OBJ_CORE, <expression error>, <expression error>, HWLOC_OBJ_L3CACHE}’
         for (auto obj_type : { HWLOC_OBJ_CORE, HWLOC_OBJ_L1CACHE, HWLOC_OBJ_L2CACHE, HWLOC_OBJ_L3CACHE }) {
                                                                                                        ^
At global scope:
cc1plus: warning: unrecognized command line option ‘-Wno-class-memaccess’
src/crypto/ghostrider/CMakeFiles/ghostrider.dir/build.make:299: recipe for target 'src/crypto/ghostrider/CMakeFiles/ghostrider.dir/ghostrider.cpp.o' failed
make[2]: *** [src/crypto/ghostrider/CMakeFiles/ghostrider.dir/ghostrider.cpp.o] Error 1
CMakeFiles/Makefile2:393: recipe for target 'src/crypto/ghostrider/CMakeFiles/ghostrider.dir/all' failed
make[1]: *** [src/crypto/ghostrider/CMakeFiles/ghostrider.dir/all] Error 2
Makefile:90: recipe for target 'all' failed
make: *** [all] Error 2
```

## phil2sat | 2021-11-29T06:18:54+00:00
Please upgrade your systems, like mentioned.
Here we are talking about efficiency, so its code has to be higly optimized for actual Hardware to be able to gain profit. If you say hey i dont need it. Please give your money to someone who is able to use it a better way.

My recommendation if ubuntu, then at least 20.04,GCC 10.2 if under ZEN3

For Zen3 at least GCC 10.3 and  better Arch or Gentoo with GCC 11.2 tuned for your march. 

## Spudz76 | 2021-11-29T15:20:29+00:00
Or, just build the bundled deps, and it works fine.

## titi288 | 2021-12-01T07:34:47+00:00
Building the bundled deps, doesnt work. Same error.
Solution / workaround  is to disable ghostrider:

$ grep GHOST CMakeCache.txt
WITH_GHOSTRIDER:BOOL=OFF

## nebulous2 | 2021-12-01T19:28:43+00:00
Thanks - build with buldled deps worked fine.

## lauarvik | 2021-12-08T08:02:00+00:00
Probably you have v1.x of hwloc. Try to install 2.x version instead.
We need exactly "Portable Hardware Locality (hwloc): Version 2.0" for basic build
https://www.open-mpi.org/software/hwloc/v2.0/
I was helped this on FreeBSD system

## Spudz76 | 2021-12-08T15:57:55+00:00
@titi288 Not only do you need to build the deps, but you have to tell CMake to use them, too.

`cmake .. -DXMRIG_DEPS=scripts/deps`

## Robert-Riedl | 2021-12-08T16:10:48+00:00
building from deps alone and cmake .. -DXMRIG_DEPS=scripts/deps didnt help me.
I had to disable ghostrider in CMakeLists.txt:
remove from "targe_link_libraries"
comment/remove "include(cmake/ghostrider.cmake)"
and change ON to OFF here "option(WITH_GHOSTRIDER      "Enable GhostRider algorithm" OFF)"

@titi288 thanks for pointing me in the right direction

## Spudz76 | 2021-12-08T16:25:55+00:00
Setting `XMRIG_DEPS` definitely works, you're doing it wrong.  Possibly nuke the build folder especially `CmakeCache.txt` before switching deps or it will still use distro (old, broken) ones if you ran it the first time without `XMRIG_DEPS`...

## phil2sat | 2021-12-08T22:37:07+00:00
git clone https://github.com/open-mpi/hwloc.git
cd hwloc
./autogen.sh

./configure --prefix=$PREFIX
make -j$(nproc)
make install -j$(nproc)

does also

## Jobine23 | 2021-12-19T04:58:16+00:00
I had a similar issue, I ended up using "Advanced build" from https://xmrig.com/docs/miner/build/ubuntu instead

## mckaygerhard | 2022-02-06T12:13:08+00:00
i have same issue, too complicated now to build the miner, or we must tuned the ghostrider or we must build a external library (cos bundled will also depends on updates in miner)

again more "upgrades based on modern hardwares" sorry guys but the miner used better the cpu with older version of OS event most modern and populated ones

## Spudz76 | 2022-02-06T22:19:30+00:00
Or you could *upgrade your old OS* so it has the 2.x hwloc and not some antiques.

## mckaygerhard | 2022-02-07T02:34:06+00:00
if course not.. cos that means change a lot of already configured things by vendor support.. that is antiques BUT STILL WELL suported

## Spudz76 | 2022-02-07T02:39:06+00:00
It's not well supported if you want to use GhostRider.  Most software doesn't need to know information about the L3 cache thus it works fine without this 2.0+ feature.  GhostRider has to be able to get this information and v1.x do not have it at all.

## mckaygerhard | 2022-02-07T02:49:05+00:00
umm inderstood.. so the right way its to autodetect the version of hwloc and disable all the goshtrider featrure if not present.. 

and by the way.. to be able to backport.. was is the minimum version need? i try to search to the hwloc project page.. but it seems is on the large changelog.. just 2.0.0 and that's all ?

## Spudz76 | 2022-02-07T19:32:16+00:00
[v2.0.4 seems to have `HWLOC_OBJ_L3CACHE`](https://www.open-mpi.org/projects/hwloc/doc/v2.0.4/a00148.php#gacd37bb612667dc437d66bfb175a8dc55) and I can't find any v2.0.0 so I think v2.0.4 was the first v2.x release.

So yes any v2.x has it.  All v1.x don't.  But v2.6.x is the current stable version.

EDIT: looking into whether CMake can probe the version during configuration phase.  Currently it has no idea other than "any" hwloc library exists.

## Spudz76 | 2022-02-07T20:11:35+00:00
#2927 will force `WITH_GHOSTRIDER=OFF` if you have antique hwloc.

## EnkhAmar | 2022-07-12T17:46:46+00:00
> I had a similar issue, I ended up using "Advanced build" from https://xmrig.com/docs/miner/build/ubuntu instead

Thank you! This worked for me.

## oneidprod | 2022-07-17T03:07:57+00:00
> > I had a similar issue, I ended up using "Advanced build" from https://xmrig.com/docs/miner/build/ubuntu instead
> 
> Thank you! This worked for me.

Same here, but had to delete xmrig folder and start over as trying to use the advanced build instructions with having already tried the basic build instructions didn't work, got the same error.  Just make sure to delete xmrig folder and start fresh with the advanced build instructions and should work unless it is the older os issue.

## Spudz76 | 2022-07-17T15:55:48+00:00
You could just delete the contents of the build folder, or at a minimum the `CMakeCache.txt` file there, to get a "clean" cmake session.  Otherwise the cache is loaded and the old answers will be used even if you provide some new answers.

## mckaygerhard | 2023-03-08T01:31:53+00:00
i ended making my own builds.. https://build.opensuse.org/package/show/home:vegnuli:deploy-vnx2/xmrig i patch to disable corectly and still build under debian jessie and devuan 1, that performs more for mining as i already pointed.. 

# Action History
- Created by: minzak | 2021-11-28T18:39:42+00:00
- Closed at: 2022-07-14T09:56:30+00:00
