---
title: Compile on Centos 6
source_url: https://github.com/monero-project/monero/issues/2085
author: knutov
assignees: []
labels:
- invalid
created_at: '2017-06-13T19:52:44+00:00'
updated_at: '2017-10-15T13:36:21+00:00'
type: issue
status: closed
closed_at: '2017-10-15T13:36:21+00:00'
---

# Original Description
How to compile on Centos 6?

# Discussion History
## moneromooo-monero | 2017-06-13T22:44:48+00:00
make, or make release-static

Install all the things it needs and complains about.

If errors which aren't due to missing dependencies, post here.

## knutov | 2017-06-13T22:48:12+00:00
After 

yum install expat-devel openssl-devel unbound-devel libunwind-devel xz-devel xz-libs ldns-devel gtest-devel doxygen graphviz graphviz-devel boost-devel boost-static pth-devel glibc-static glibc-devel

I still can not compile this. `make` ends with 

```
CMake Error at CMakeLists.txt:48 (message):
  Could not find Boost libraries, please make sure you have installed
  Boost or libboost-all-dev (1.58) or the equivalent
```

./monero-master/build/release/CMakeFiles/CMakeError.log
ends with 
```
Run Build Command:/usr/bin/gmake "cmTryCompileExec993420673/fast"
gmake[1]: Entering directory `/vz/monero/monero-master/build/release/CMakeFiles/CMakeTmp'
/usr/bin/gmake -f CMakeFiles/cmTryCompileExec993420673.dir/build.make CMakeFiles/cmTryCompileExec993420673.dir/build
gmake[2]: Entering directory `/vz/monero/monero-master/build/release/CMakeFiles/CMakeTmp'
/usr/bin/cmake -E cmake_progress_report /vz/monero/monero-master/build/release/CMakeFiles/CMakeTmp/CMakeFiles 1
Building C object CMakeFiles/cmTryCompileExec993420673.dir/CheckFunctionExists.c.o
/usr/bin/cc   -DCHECK_FUNCTION_EXISTS=pthread_create   -o CMakeFiles/cmTryCompileExec993420673.dir/CheckFunctionExists.c.o   -c /usr/share/cmake/Modules/CheckFunctionExists.c
Linking C executable cmTryCompileExec993420673
/usr/bin/cmake -E cmake_link_script CMakeFiles/cmTryCompileExec993420673.dir/link.txt --verbose=1
/usr/bin/cc   -DCHECK_FUNCTION_EXISTS=pthread_create    CMakeFiles/cmTryCompileExec993420673.dir/CheckFunctionExists.c.o  -o cmTryCompileExec993420673 -rdynamic -lpthreads
/usr/bin/ld: cannot find -lpthreads
collect2: ld returned 1 exit status
gmake[2]: *** [cmTryCompileExec993420673] Error 1
gmake[2]: Leaving directory `/vz/monero/monero-master/build/release/CMakeFiles/CMakeTmp'
gmake[1]: Leaving directory `/vz/monero/monero-master/build/release/CMakeFiles/CMakeTmp'
gmake[1]: *** [cmTryCompileExec993420673/fast] Error 2
```

What should I install else?

## hyc | 2017-06-14T18:17:45+00:00
Seems like a makefile error somewhere. The correct library name on Linux is "-lpthread" not "-lpthreads". Also, we shouldn't even be referencing this library at all, we should be using the compiler switch "-pthread" which tells the compiler to build thread-aware code and link to the appropriate platform-specific thread library (which isn't always named libpthread anyway).

## moneromooo-monero | 2017-06-14T21:23:25+00:00
As for boost, install ALL of boost.

## ghost | 2017-06-17T23:47:01+00:00
Instructions for building boost are contained in readme.md

## moneromooo-monero | 2017-10-15T13:25:14+00:00
The bit using -lpthreads seems to be cmake probing to see what it should use, so doesn't seem like an error. Since it seems this bug is just about needing to install boost, it's invalid.

+invalid

# Action History
- Created by: knutov | 2017-06-13T19:52:44+00:00
- Closed at: 2017-10-15T13:36:21+00:00
