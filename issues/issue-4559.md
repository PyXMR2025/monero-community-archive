---
title: 'Build failed on ARMv7: c++: error: missing argument to ‘-march=’'
source_url: https://github.com/monero-project/monero/issues/4559
author: Lafudoci
assignees: []
labels: []
created_at: '2018-10-11T14:52:22+00:00'
updated_at: '2018-10-15T12:49:04+00:00'
type: issue
status: closed
closed_at: '2018-10-15T12:49:04+00:00'
---

# Original Description
Build failed on ASUS tinkerboard (an ARMv7 clone board of raspberry pi, worked well before update to v0.13)
Error after `make release`.
```
Scanning dependencies of target epee
make[3]: Leaving directory '/home/linaro/monero/build/Linux/master/release'
make[3]: Entering directory '/home/linaro/monero/build/Linux/master/release'
[ 15%] Building CXX object contrib/epee/src/CMakeFiles/epee.dir/hex.cpp.o
c++: error: missing argument to ‘-march=’
contrib/epee/src/CMakeFiles/epee.dir/build.make:62: recipe for target 'contrib/epee/src/CMakeFiles/epee.dir/hex.cpp.o' failed
make[3]: *** [contrib/epee/src/CMakeFiles/epee.dir/hex.cpp.o] Error 1
make[3]: Leaving directory '/home/linaro/monero/build/Linux/master/release'
CMakeFiles/Makefile2:397: recipe for target 'contrib/epee/src/CMakeFiles/epee.dir/all' failed
make[2]: *** [contrib/epee/src/CMakeFiles/epee.dir/all] Error 2
make[2]: Leaving directory '/home/linaro/monero/build/Linux/master/release'
Makefile:138: recipe for target 'all' failed
make[1]: *** [all] Error 2
make[1]: Leaving directory '/home/linaro/monero/build/Linux/master/release'
Makefile:78: recipe for target 'release' failed
make: *** [release] Error 2
```

# Discussion History
## xiphon | 2018-10-11T15:25:29+00:00
Please provide the complete log

## Lafudoci | 2018-10-11T15:30:31+00:00
@xiphon OK, here it is.
https://paste.fedoraproject.org/paste/01orcBgX-biyA~ZoYz3MpA

## xiphon | 2018-10-11T21:46:53+00:00
1. Run `make clean` and apply the first patch, check the compilation.
2. Run `make clean`, revert the first patch and apply the second one, check the compilation.

```diff
diff --git a/CMakeLists.txt b/CMakeLists.txt
index 1bffd29b..50f32217 100644
--- a/CMakeLists.txt
+++ b/CMakeLists.txt
@@ -523,7 +522,7 @@ else()
     endif()
   endif()
   message(STATUS "Building on ${CMAKE_SYSTEM_PROCESSOR} for ${ARCH}")
-  if(ARCH STREQUAL "default")
+  if(NOT ARCH OR ARCH STREQUAL "default")
     set(ARCH_FLAG "")
   elseif(PPC64LE)
     set(ARCH_FLAG "-mcpu=power8")
```

```diff
diff --git a/CMakeLists.txt b/CMakeLists.txt
index 1bffd29b..50f32217 100644
--- a/CMakeLists.txt
+++ b/CMakeLists.txt
@@ -534,6 +533,8 @@ else()
   elseif(IOS AND ARCH STREQUAL "arm64")
     message(STATUS "IOS: Changing arch from arm64 to armv8")
     set(ARCH_FLAG "-march=armv8")
+  elseif(ARM7)
+    set(ARCH_FLAG "-march=armv7")
   else()
     set(ARCH_FLAG "-march=${ARCH}")
     if(ARCH STREQUAL "native")
```

## ghost | 2018-10-11T22:49:16+00:00
This patch shouldn't really work, because you'll never hit ARCH STREQUAL "arm64" with an ARM7 processor...

I suspect the cmakefile needs finessing further up top when the architectures are first tested.

## sedited | 2018-10-11T22:57:12+00:00
I think the problem is that in the current way it is setup, there is a different branch in the cmake logic taken between native and cross arm compilation. It's kind of annoying that these differences are needed at all. Would be nice to have a default native path and a cross compilation path. 

## xiphon | 2018-10-11T23:04:37+00:00
> This patch shouldn't really work, because you'll never hit ARCH STREQUAL "arm64" with an ARM7 processor...

The comment doesn't seem valid to me. Please take a closer look at what the patch does. 

Anyway, still waiting for a report from @Lafudoci (or another ARMv7 user)

## xiphon | 2018-10-11T23:31:03+00:00
@TheCharlatan 
Think the issue is related to:
1. We don't have a default/native ARCH fallback if none of the ARCH-definition rules were met
2. We don't set `-march=armv7` flag

## Lafudoci | 2018-10-12T01:56:35+00:00
@xiphon, Thanks for your help, first patch built well. The second patch build is running, but it has passed the previous fail point. I'll report once it finish.

## Lafudoci | 2018-10-12T03:02:14+00:00
@xiphon Second patch built successfully as well. Thank you.

## keffnet | 2018-10-12T07:31:44+00:00
The patch does not work for me. Before applying same errors as Lafudoci . After ,

[ 27%] Building CXX object contrib/epee/src/CMakeFiles/epee.dir/hex.cpp.o
/root/monero/contrib/epee/src/hex.cpp:1:0: error: target CPU does not support ARM mode
 // Copyright (c) 2017-2018, The Monero Project

contrib/epee/src/CMakeFiles/epee.dir/build.make:62: recipe for target 'contrib/epee/src/CMakeFiles/epee.dir/hex.cpp.o' failed

---

 
model name      : ARMv7 Processor rev 4 (v7l)
Linux a 4.14.34-v7+ #1110 SMP Mon Apr 16 15:18:51 BST 2018 armv7l GNU/Linux



## keffnet | 2018-10-12T07:35:40+00:00
> 
> 
> The patch does not work for me. Before applying same errors as Lafudoci . After ,
> 
> [ 27%] Building CXX object contrib/epee/src/CMakeFiles/epee.dir/hex.cpp.o
> /root/monero/contrib/epee/src/hex.cpp:1:0: error: target CPU does not support ARM mode
> // Copyright (c) 2017-2018, The Monero Project
> 
> contrib/epee/src/CMakeFiles/epee.dir/build.make:62: recipe for target 'contrib/epee/src/CMakeFiles/epee.dir/hex.cpp.o' failed
> 
> model name : ARMv7 Processor rev 4 (v7l)
> Linux a 4.14.34-v7+ #1110 SMP Mon Apr 16 15:18:51 BST 2018 armv7l GNU/Linux

--march=armv7-a  works.

There must be some better way of doing this or does every arch need to be added? :D How was it before this release?

## xiphon | 2018-10-12T12:53:57+00:00
@shyrwall

1. Run `make clean`
2. Apply the patch from #4565
3. Report back the results. 

Would be nice to see the logs if a build fails.

## keffnet | 2018-10-12T16:31:20+00:00
Sorry for the late reply. Looks good so far. Takes like 10h to compile.. 💃 

## keffnet | 2018-10-14T02:24:35+00:00
Compiled fine. Thanks. New release seems to use 2GB of ram while compiling. Hard on a RPi with 1GB of ram :D Swapping to a SD-card isn't the best ;) 

## moneromooo-monero | 2018-10-15T12:30:18+00:00
+resolved

# Action History
- Created by: Lafudoci | 2018-10-11T14:52:22+00:00
- Closed at: 2018-10-15T12:49:04+00:00
