---
title: 12.0 does not build on OSX 10.13.3
source_url: https://github.com/monero-project/monero/issues/3495
author: BigslimVdub
assignees: []
labels: []
created_at: '2018-03-25T04:18:14+00:00'
updated_at: '2018-05-30T03:04:24+00:00'
type: issue
status: closed
closed_at: '2018-05-30T03:04:24+00:00'
---

# Original Description
Tried master, release zip, and release tar.gz and all 3 give the following issue with GTest:

CMake Warning at /usr/local/Cellar/cmake/3.10.3/share/cmake/Modules/FindBoost.cmake:801 (message):
  New Boost version may have incorrect or missing dependencies and imported
  targets
Call Stack (most recent call first):
  /usr/local/Cellar/cmake/3.10.3/share/cmake/Modules/FindBoost.cmake:907 (_Boost_COMPONENT_DEPENDENCIES)
  /usr/local/Cellar/cmake/3.10.3/share/cmake/Modules/FindBoost.cmake:1542 (_Boost_MISSING_DEPENDENCIES)
  CMakeLists.txt:786 (find_package)


-- Found Boost Version: 106600
-- Looking for rl_copy_text
-- Looking for rl_copy_text - not found
-- Looking for rl_filename_completion_function
-- Looking for rl_filename_completion_function - found
-- Could not find GNU readline library so building without readline support
-- Found Git: /usr/local/bin/git
-- Could NOT find GTest (missing: GTEST_LIBRARY GTEST_INCLUDE_DIR GTEST_MAIN_LIBRARY) 
-- GTest not found on the system: will use GTest bundled with this source
Doxygen: graphviz not found - graphs disabled
-- Could NOT find Doxygen (missing: DOXYGEN_EXECUTABLE) 
-- Performing Test HAVE_C11
-- Performing Test HAVE_C11 - Success
-- Configuring incomplete, errors occurred!


I do not get errors building from brew (but that is only updated for 11.1.0 not 12.0)
I do not get errors building from brew

# Discussion History
## MarkusZoppelt | 2018-03-25T11:50:14+00:00
First, make sure to lone recursively to pull-in needed submodules:
`git clone --recursive https://github.com/monero-project/monero`
`git checkout v0.12.0.0`

You will need some more dependencies, run:

`brew install zeromq`
`brew install --HEAD andresv/gnuradio/cppzmq`

Then try `make` again

Please let me know if that helps.

## BigslimVdub | 2018-03-25T12:04:21+00:00
I already have zeromq installed and zpp file in the folder as listed in install wiki. 

I have installed aeon cli amd rebase cli and a few others with no issues after installing all dependencies. I’ve never seen this issue before. 

## CamilleScholtz | 2018-03-25T12:05:25+00:00
I'm having what looks like the same error on Linux (possibly? you should post your CMakeError.log @BigslimVdub) , installed `zeromq` and `ccpzmq`:

```CMake Warning at /usr/share/cmake/Modules/FindBoost.cmake:801 (message):
  New Boost version may have incorrect or missing dependencies and imported
  targets
Call Stack (most recent call first):
  /usr/share/cmake/Modules/FindBoost.cmake:907 (_Boost_COMPONENT_DEPENDENCIES)
  /usr/share/cmake/Modules/FindBoost.cmake:1542 (_Boost_MISSING_DEPENDENCIES)
  CMakeLists.txt:786 (find_package)


CMake Warning at /usr/share/cmake/Modules/FindBoost.cmake:801 (message):
  New Boost version may have incorrect or missing dependencies and imported
  targets
Call Stack (most recent call first):
  /usr/share/cmake/Modules/FindBoost.cmake:907 (_Boost_COMPONENT_DEPENDENCIES)
  /usr/share/cmake/Modules/FindBoost.cmake:1542 (_Boost_MISSING_DEPENDENCIES)
  CMakeLists.txt:786 (find_package)


CMake Warning at /usr/share/cmake/Modules/FindBoost.cmake:801 (message):
  New Boost version may have incorrect or missing dependencies and imported
  targets
Call Stack (most recent call first):
  /usr/share/cmake/Modules/FindBoost.cmake:907 (_Boost_COMPONENT_DEPENDENCIES)
  /usr/share/cmake/Modules/FindBoost.cmake:1542 (_Boost_MISSING_DEPENDENCIES)
  CMakeLists.txt:786 (find_package)


CMake Warning at /usr/share/cmake/Modules/FindBoost.cmake:801 (message):
  New Boost version may have incorrect or missing dependencies and imported
  targets
Call Stack (most recent call first):
  /usr/share/cmake/Modules/FindBoost.cmake:907 (_Boost_COMPONENT_DEPENDENCIES)
  /usr/share/cmake/Modules/FindBoost.cmake:1542 (_Boost_MISSING_DEPENDENCIES)
  CMakeLists.txt:786 (find_package)


-- Found Boost Version: 106600
-- Looking for rl_copy_text
-- Looking for rl_copy_text - found
-- Looking for rl_filename_completion_function
-- Looking for rl_filename_completion_function - found
-- Found readline library at: /usr
-- Found Git: /usr/bin/git
-- Found Doxygen: /usr/bin/doxygen (found version "1.8.14") found components:  doxygen dot
-- Performing Test HAVE_C11
-- Performing Test HAVE_C11 - Success
-- Configuring incomplete, errors occurred!
```

CMakeError.log:

```
Determining if the pthread_create exist failed with the following output:
Change Dir: /usr/src/pkg/wrk/monero/src/monero-0.12.0.0/CMakeFiles/CMakeTmp

Run Build Command:"/usr/bin/make" "cmTC_18e08/fast"
/usr/bin/make -f CMakeFiles/cmTC_18e08.dir/build.make CMakeFiles/cmTC_18e08.dir/build
make[1]: Entering directory '/usr/src/pkg/wrk/monero/src/monero-0.12.0.0/CMakeFiles/CMakeTmp'
Building C object CMakeFiles/cmTC_18e08.dir/CheckSymbolExists.c.o
/usr/bin/cc   -O2 -march=native    -o CMakeFiles/cmTC_18e08.dir/CheckSymbolExists.c.o   -c /usr/src/pkg/wrk/monero/src/monero-0.12.0.0/CMakeFiles/CMakeTmp/CheckSymbolExists.c
Linking C executable cmTC_18e08
/usr/bin/cmake -E cmake_link_script CMakeFiles/cmTC_18e08.dir/link.txt --verbose=1
/usr/bin/cc -O2 -march=native     -rdynamic CMakeFiles/cmTC_18e08.dir/CheckSymbolExists.c.o  -o cmTC_18e08 
CMakeFiles/cmTC_18e08.dir/CheckSymbolExists.c.o: In function `main':
CheckSymbolExists.c:(.text.startup+0x6): undefined reference to `pthread_create'
collect2: error: ld returned 1 exit status
make[1]: *** [CMakeFiles/cmTC_18e08.dir/build.make:98: cmTC_18e08] Error 1
make[1]: Leaving directory '/usr/src/pkg/wrk/monero/src/monero-0.12.0.0/CMakeFiles/CMakeTmp'
make: *** [Makefile:126: cmTC_18e08/fast] Error 2

File /usr/src/pkg/wrk/monero/src/monero-0.12.0.0/CMakeFiles/CMakeTmp/CheckSymbolExists.c:
/* */
#include <pthread.h>

int main(int argc, char** argv)
{
  (void)argv;
#ifndef pthread_create
  return ((int*)(&pthread_create))[argc];
#else
  (void)argc;
  return 0;
#endif
}

Determining if the function memset_s exists in the c failed with the following output:
Change Dir: /usr/src/pkg/wrk/monero/src/monero-0.12.0.0/CMakeFiles/CMakeTmp

Run Build Command:"/usr/bin/make" "cmTC_1a7e0/fast"
/usr/bin/make -f CMakeFiles/cmTC_1a7e0.dir/build.make CMakeFiles/cmTC_1a7e0.dir/build
make[1]: Entering directory '/usr/src/pkg/wrk/monero/src/monero-0.12.0.0/CMakeFiles/CMakeTmp'
Building C object CMakeFiles/cmTC_1a7e0.dir/CheckFunctionExists.c.o
/usr/bin/cc   -O2 -march=native -DCHECK_FUNCTION_EXISTS=memset_s   -o CMakeFiles/cmTC_1a7e0.dir/CheckFunctionExists.c.o   -c /usr/share/cmake/Modules/CheckFunctionExists.c
Linking C executable cmTC_1a7e0
/usr/bin/cmake -E cmake_link_script CMakeFiles/cmTC_1a7e0.dir/link.txt --verbose=1
/usr/bin/cc -O2 -march=native -DCHECK_FUNCTION_EXISTS=memset_s    -rdynamic CMakeFiles/cmTC_1a7e0.dir/CheckFunctionExists.c.o  -o cmTC_1a7e0  -L/usr/src/pkg/wrk/monero/src/monero-0.12.0.0/CMakeFiles/CMakeTmp/string.h -Wl,-rpath,/usr/src/pkg/wrk/monero/src/monero-0.12.0.0/CMakeFiles/CMakeTmp/string.h -lc 
CMakeFiles/cmTC_1a7e0.dir/CheckFunctionExists.c.o: In function `main':
CheckFunctionExists.c:(.text.startup+0xc): undefined reference to `memset_s'
collect2: error: ld returned 1 exit status
make[1]: *** [CMakeFiles/cmTC_1a7e0.dir/build.make:98: cmTC_1a7e0] Error 1
make[1]: Leaving directory '/usr/src/pkg/wrk/monero/src/monero-0.12.0.0/CMakeFiles/CMakeTmp'
make: *** [Makefile:126: cmTC_1a7e0/fast] Error 2


Determining if the function explicit_bzero exists in the c failed with the following output:
Change Dir: /usr/src/pkg/wrk/monero/src/monero-0.12.0.0/CMakeFiles/CMakeTmp

Run Build Command:"/usr/bin/make" "cmTC_cfdfa/fast"
/usr/bin/make -f CMakeFiles/cmTC_cfdfa.dir/build.make CMakeFiles/cmTC_cfdfa.dir/build
make[1]: Entering directory '/usr/src/pkg/wrk/monero/src/monero-0.12.0.0/CMakeFiles/CMakeTmp'
Building C object CMakeFiles/cmTC_cfdfa.dir/CheckFunctionExists.c.o
/usr/bin/cc   -O2 -march=native -DCHECK_FUNCTION_EXISTS=explicit_bzero   -o CMakeFiles/cmTC_cfdfa.dir/CheckFunctionExists.c.o   -c /usr/share/cmake/Modules/CheckFunctionExists.c
Linking C executable cmTC_cfdfa
/usr/bin/cmake -E cmake_link_script CMakeFiles/cmTC_cfdfa.dir/link.txt --verbose=1
/usr/bin/cc -O2 -march=native -DCHECK_FUNCTION_EXISTS=explicit_bzero    -rdynamic CMakeFiles/cmTC_cfdfa.dir/CheckFunctionExists.c.o  -o cmTC_cfdfa  -L/usr/src/pkg/wrk/monero/src/monero-0.12.0.0/CMakeFiles/CMakeTmp/strings.h -Wl,-rpath,/usr/src/pkg/wrk/monero/src/monero-0.12.0.0/CMakeFiles/CMakeTmp/strings.h -lc 
CMakeFiles/cmTC_cfdfa.dir/CheckFunctionExists.c.o: In function `main':
CheckFunctionExists.c:(.text.startup+0xc): undefined reference to `explicit_bzero'
collect2: error: ld returned 1 exit status
make[1]: *** [CMakeFiles/cmTC_cfdfa.dir/build.make:98: cmTC_cfdfa] Error 1
make[1]: Leaving directory '/usr/src/pkg/wrk/monero/src/monero-0.12.0.0/CMakeFiles/CMakeTmp'
make: *** [Makefile:126: cmTC_cfdfa/fast] Error 2


Determining if the -Wl,-z,noexecheap linker flag is suppored failed with the following output:
Change Dir: /usr/src/pkg/wrk/monero/src/monero-0.12.0.0/CMakeFiles/CMakeTmp

Run Build Command:"/usr/bin/make" "cmTC_d5788/fast"
/usr/bin/make -f CMakeFiles/cmTC_d5788.dir/build.make CMakeFiles/cmTC_d5788.dir/build
make[1]: Entering directory '/usr/src/pkg/wrk/monero/src/monero-0.12.0.0/CMakeFiles/CMakeTmp'
Building C object CMakeFiles/cmTC_d5788.dir/CheckLinkerFlag.c.o
/usr/bin/cc   -Wl,-z,noexecheap    -Wl,-z,noexecheap -o CMakeFiles/cmTC_d5788.dir/CheckLinkerFlag.c.o   -c /usr/src/pkg/wrk/monero/src/monero-0.12.0.0/cmake/CheckLinkerFlag.c
Linking C executable cmTC_d5788
/usr/bin/cmake -E cmake_link_script CMakeFiles/cmTC_d5788.dir/link.txt --verbose=1
/usr/bin/cc -Wl,-z,noexecheap     -rdynamic CMakeFiles/cmTC_d5788.dir/CheckLinkerFlag.c.o  -o cmTC_d5788 
/usr/bin/ld: warning: -z noexecheap ignored.
make[1]: Leaving directory '/usr/src/pkg/wrk/monero/src/monero-0.12.0.0/CMakeFiles/CMakeTmp'
``

## erkmos | 2018-03-27T04:19:57+00:00
Had the same issue and an easy work-around seems to be to use Boost 1.65 instead. cmake seemingly has some hack that needs to be updated for every boost version (even 3.10.3 doesn't seem to work with boost 1.66.0). Didn't dig deeper, but this works for me with cmake 3.5.1 from xenial repos

## CamilleScholtz | 2018-03-27T07:14:53+00:00
I tried cmake 3.10.3 and 3.11 (still in beta), both don't work. The thing is, I haven't had any problems compiling other programs with boost 1.66.

## blockchainbuzz | 2018-03-27T19:38:06+00:00
I think you have is missing dependencies, such as 'readline', 'doxygen', and 'gtest'. It is requested when you compile it with cmake not with brew.  I slowly fix the compiling error. one by one by installing missing dependencies. It might be related with my ticket. #3506 


## CamilleScholtz | 2018-03-27T19:40:16+00:00
https://github.com/monero-project/monero#compiling-monero-from-source

I have all the non-optional dependencies installed, besides libunbound which should be vendored.

## danrmiller | 2018-03-27T19:44:18+00:00
I can build on osx 10.13 with boost 1.66. 
https://build.getmonero.org/builders/monero-static-osx-10.13/builds/3
This is from 'master', I'll setup a job to build from the release tag shortly.
It is supposed to build fine without the optional dependencies readline and doxygen that @blockchainbuzz mentions, and if gtest is not found it uses the "vendored" code included in the monero tree.

## danrmiller | 2018-03-27T19:48:29+00:00
I know this was already asked in this thread, but can you please confirm that you cloned recursively?

## erkmos | 2018-03-28T03:53:51+00:00
Should add that I had the issue when building with the Dockerfile supplied by the v0.12.0.0 release, not with homebrew. Just changing to boost 1.65 fixed the issue for me.

## BigslimVdub | 2018-03-30T01:53:31+00:00
Honestly I just downloaded the binaries and running that now.  monero-mac-x64-v0.12.0.0.tar.bz2 and it seems to be working fine. Unfortunately GUI isn't built yet so I will have to use CLI for now. 


## moneromooo-monero | 2018-04-12T13:13:24+00:00
Those cmake warnings about boost are OK, they're not fatal. There must have been another error.

## moneromooo-monero | 2018-05-16T11:01:31+00:00
Please post the rest of the cmake output, as the error is likely there.

## BigslimVdub | 2018-05-29T04:23:58+00:00
I was able to clone today and build on 10.13.4 but apparently after updating submodule it only built 0.12.0 not 0.12.1. 

Everything works now sans it only building 12.0

## dEBRUYNE-1 | 2018-05-29T10:49:47+00:00
@BigslimVdub - Did you checkout the v0.12.1.0 tag? 

## BigslimVdub | 2018-05-29T11:08:37+00:00
I did not add the tag before building. This was related to 12.0 so if you want to close that’s fine. When I get time I can try 12.1 

## moneromooo-monero | 2018-05-29T15:23:29+00:00
Doesn't matter, we can keep it open till you confirm.

## BigslimVdub | 2018-05-30T03:04:24+00:00
successful build on 10.13.4 using : 

```
git checkout tags/v0.12.1.0
```

Can you add that line to the compile instructions? I am closing this due to it building now. 

# Action History
- Created by: BigslimVdub | 2018-03-25T04:18:14+00:00
- Closed at: 2018-05-30T03:04:24+00:00
