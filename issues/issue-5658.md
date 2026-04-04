---
title: Multiple Errors when attempting to build v0.14.1 for ARM v8 with Static binaries
  or Depends
source_url: https://github.com/monero-project/monero/issues/5658
author: JustHereToHelp
assignees: []
labels:
- invalid
created_at: '2019-06-17T02:32:54+00:00'
updated_at: '2019-06-17T06:56:12+00:00'
type: issue
status: closed
closed_at: '2019-06-17T05:33:45+00:00'
---

# Original Description
I am trying to build this new release to armv8 from a linux x86_64 system.  Have been trying since 14.1 was still just the master and have had no luck....

 ERROR when: 
 make depends target=aarch64-linux-gnu  

 make[3]: Entering directory '/home/user/monero/build/Linux/_HEAD_detached_at_v0.14.1.0_/release' [ 38%] Building CXX object contrib/epee/src/CMakeFiles/epee.dir/hex.cpp.o cc1plus: error: bad value (‘armv8-a’) for ‘-march=’ switch cc1plus: note: valid arguments to ‘-march=’ switch are: nocona core2 nehalem corei7 westmere sandybridge corei7-avx ivybridge core-avx-i haswell core-avx2 broadwell skylake skylake-avx512 bonnell atom silvermont slm knl x86-64 eden-x2 nano nano-1000 nano-2000 nano-3000 nano-x2 eden-x4 nano-x4 k8 k8-sse3 opteron opteron-sse3 athlon64 athlon64-sse3 athlon-fx amdfam10 barcelona bdver1 bdver2 bdver3 bdver4 znver1 btver1 btver2 contrib/epee/src/CMakeFiles/epee.dir/build.make:62: recipe for target 'contrib/epee/src/CMakeFiles/epee.dir/hex.cpp.o' failed make[3]: *** [contrib/epee/src/CMakeFiles/epee.dir/hex.cpp.o] Error 1 make[3]: Leaving directory '/home/user/monero/build/Linux/_HEAD_detached_at_v0.14.1.0_/release' CMakeFiles/Makefile2:455: recipe for target 'contrib/epee/src/CMakeFiles/epee.dir/all' failed make[2]: *** [contrib/epee/src/CMakeFiles/epee.dir/all] Error 2 make[2]: Leaving directory '/home/user/monero/build/Linux/_HEAD_detached_at_v0.14.1.0_/release' Makefile:140: recipe for target 'all' failed make[1]: *** [all] Error 2 make[1]: Leaving directory '/home/user/monero/build/Linux/_HEAD_detached_at_v0.14.1.0_/release' Makefile:130: recipe for target 'release-static-linux-armv8' failed make: *** [release-static-linux-armv8] Error 2  


ERROR when:  
~/monero$ git checkout v0.14.1.0
 HEAD is now at 29a505d1 Merge pull request #5638 
~/monero$ make release-static-linux-armv8  

 Preprocessing zeromq... patching file configure.ac patch unexpectedly ends in middle of line Hunk #1 succeeded at 261 with fuzz 2 (offset -4 lines). patching file configure.ac patch unexpectedly ends in middle of line Hunk #1 succeeded at 261 with fuzz 2 (offset 2 lines). autogen.sh: error: could not find libtool.  libtool is required to run autogen.sh. funcs.mk:242: recipe for target '/home/user/monero/contrib/depends/work/build/aarch64-linux-gnu/zeromq/4.1.5-195c1287412/.stamp_preprocessed' failed make[1]: *** [/home/user/monero/contrib/depends/work/build/aarch64-linux-gnu/zeromq/4.1.5-195c1287412/.stamp_preprocessed] Error 1 make[1]: Leaving directory '/home/user/monero/contrib/depends' Makefile:50: recipe for target 'depends' failed make: *** [depends] Error 2 

-this error said i needed libtool, when i installed libtool and re attempted, 

 make depends target=aarch64-linux-gnu 

cd contrib/depends && make HOST=aarch64-linux-gnu && cd ../.. && mkdir -p build/aarch64-linux-gnu/release make[1]: Entering directory '/home/user/monero/contrib/depends' Preprocessing zeromq... patching file configure.ac patch unexpectedly ends in middle of line Hunk #1 FAILED at 265. 1 out of 1 hunk FAILED -- saving rejects to file configure.ac.rej funcs.mk:242: recipe for target '/home/user/monero/contrib/depends/work/build/aarch64-linux-gnu/zeromq/4.1.5-195c1287412/.stamp_preprocessed' failed make[1]: *** [/home/user/monero/contrib/depends/work/build/aarch64-linux-gnu/zeromq/4.1.5-195c1287412/.stamp_preprocessed] Error 1 make[1]: Leaving directory '/home/user/monero/contrib/depends' Makefile:50: recipe for target 'depends' failed make: *** [depends] Error 2 

# Discussion History
## hyc | 2019-06-17T05:31:04+00:00
> cc1plus: error: bad value (‘armv8-a’) for ‘-march=’ switch

You're trying to compile for ARM using an x86 compiler. You need an ARM compiler if you want to build an ARM binary.

## hyc | 2019-06-17T05:31:37+00:00
+invalid


## JustHereToHelp | 2019-06-17T06:56:12+00:00
Is not the cross compiling and depends commands for doing exactly what i am trying?  Compiling for armv8 on another system?

# Action History
- Created by: JustHereToHelp | 2019-06-17T02:32:54+00:00
- Closed at: 2019-06-17T05:33:45+00:00
