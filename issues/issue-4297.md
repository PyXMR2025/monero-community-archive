---
title: Trouble generating cold wallet on PiZero - Illegal instruction
source_url: https://github.com/monero-project/monero/issues/4297
author: KnoAll
assignees: []
labels: []
created_at: '2018-08-23T16:28:20+00:00'
updated_at: '2018-09-18T17:29:17+00:00'
type: issue
status: closed
closed_at: '2018-09-18T17:29:17+00:00'
---

# Original Description
I am trying to create a cold wallet on a PiZero. This is an ARMv6 processor, and I'm getting 'Illegal instruction' when running monero-wallet-cli. In my searching this appears to be an ARMv6 vs ARMv7 issue with the precompiled code. The Pi does not have any networking capabilities, so I'm following the instructions for how to compile on another Pi of the same ARMv6 that does have networking.
The instructions (including the part for building on Raspian Jessie) have gone smoothly so far, but at the 'make release' step i'm getting an error. 
Makefile:53: recipe for target 'cmake-release' failed
make: *** [cmake-release] Error 1

in the log file i see (among others)
CheckSymbolExists.c:(.text+0x38): undefined reference to `pthread_create'
collect2: error: ld returned 1 exit status
CMakeFiles/cmTC_a5c2a.dir/build.make:97: recipe for target 'cmTC_a5c2a' failed
make[2]: *** [cmTC_a5c2a] Error 1



# Discussion History
## moneromooo-monero | 2018-08-24T10:03:56+00:00
You want to link against libpthread. Does this work ?

```
diff --git a/CMakeLists.txt b/CMakeLists.txt
index 3b93988..c9fcca7 100644
--- a/CMakeLists.txt
+++ b/CMakeLists.txt
@@ -810,6 +810,8 @@ elseif(NOT MSVC)
   set(EXTRA_LIBRARIES ${RT})
 endif()
 
+set(EXTRA_LIBRARIES ${EXTRA_LIBRARIES} pthread)
+
 list(APPEND EXTRA_LIBRARIES ${CMAKE_DL_LIBS})
 
 option(USE_READLINE "Build with GNU readline support." ON)

```

## KnoAll | 2018-08-24T14:36:44+00:00
I get an error when running this diff --git a/CMakeLists.txt b/CMakeLists.txt

diff: unrecognized option '--git'


## moneromooo-monero | 2018-08-25T09:37:55+00:00
You use it by saving the patch in a file, then:

patch -p1 < filename-you-saved-it-in



## KnoAll | 2018-08-30T03:22:57+00:00
Forgive me, I am not an advanced user and this does not make sense to me. I don't recall seeing anything about a patch or how to work with it.

## dEBRUYNE-1 | 2018-08-30T11:27:18+00:00
@KnoAll - You have to create a new text file in your git working directory with moneromooo's patch. Practically speaking this works as follows:

1. Create a new text file in your git working directory.

2. Add moneromooo's patch from this comment -> https://github.com/monero-project/monero/issues/4297#issuecomment-415714324

3. Save the file as patch.txt

4. In the terminal, type patch -p1 < patch.txt

5. The patch should now be applied and you can recompile thereafter.

## KnoAll | 2018-08-30T14:42:18+00:00
Thank you @dEBRUYNE-1 that was very helpful. That did work and got me past the errors I was seeing previously.  Unfortunately now I am getting errors farther down the line.

`~/monero# make release
mkdir -p build/release
cd build/release && cmake -D CMAKE_BUILD_TYPE=Release ../..
-- Building without build tag
-- Could not find DEVELOPER_LOCAL_TOOLS in env (not required)
-- BOOST_IGNORE_SYSTEM_PATHS defaults to OFF
-- Could not find DEVELOPER_LIBUNBOUND_OLD in env (not required)
-- Building for a 32-bit system
-- Building internal libraries as static
-- Could not find DATABASE in env (not required unless you want to change database type from default: lmdb)
-- Using LMDB as default DB type
-- Stack trace on exception enabled (using easylogging++)
-- Using OpenSSL include dir at /usr/include
-- Found miniupnpc API version 10
-- Using in-tree miniupnpc
CMake Error at external/CMakeLists.txt:42 (add_subdirectory):
  add_subdirectory given source "miniupnp/miniupnpc" which is not an existing
  directory.


CMake Error at external/CMakeLists.txt:44 (set_property):
  set_property could not find TARGET libminiupnpc-static.  Perhaps it has not
  yet been created.


CMake Error at external/CMakeLists.txt:48 (set_property):
  set_property could not find TARGET libminiupnpc-static.  Perhaps it has not
  yet been created.


-- Looking for libunbound
-- Found libunbound include (unbound.h) in /usr/include
-- Found libunbound shared library
-- Using 32-bit LMDB from source tree
-- Using PCSC include dir at /usr/include/PCSC
-- Building on armv6l for native
-- Using C security hardening flags:  -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -fstack-protector -fstack-protector-strong
-- Using C++ security hardening flags:  -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -fstack-protector -fstack-protector-strong
-- Using linker security hardening flags:  -pie -Wl,-z,relro -Wl,-z,now -Wl,-z,noexecstack
-- AES support not available on ARMv6
-- Setting FPU Flags for ARM Processors
-- Selecting VFP for ARMv6
CMake Warning at /usr/share/cmake-3.6/Modules/FindBoost.cmake:743 (message):
  Imported targets not available for Boost version 106400
Call Stack (most recent call first):
  /usr/share/cmake-3.6/Modules/FindBoost.cmake:842 (_Boost_COMPONENT_DEPENDENCIES)
  /usr/share/cmake-3.6/Modules/FindBoost.cmake:1411 (_Boost_MISSING_DEPENDENCIES)
  CMakeLists.txt:781 (find_package)


CMake Warning at /usr/share/cmake-3.6/Modules/FindBoost.cmake:743 (message):
  Imported targets not available for Boost version 106400
Call Stack (most recent call first):
  /usr/share/cmake-3.6/Modules/FindBoost.cmake:842 (_Boost_COMPONENT_DEPENDENCIES)
  /usr/share/cmake-3.6/Modules/FindBoost.cmake:1411 (_Boost_MISSING_DEPENDENCIES)
  CMakeLists.txt:781 (find_package)


CMake Warning at /usr/share/cmake-3.6/Modules/FindBoost.cmake:743 (message):
  Imported targets not available for Boost version 106400
Call Stack (most recent call first):
  /usr/share/cmake-3.6/Modules/FindBoost.cmake:842 (_Boost_COMPONENT_DEPENDENCIES)
  /usr/share/cmake-3.6/Modules/FindBoost.cmake:1411 (_Boost_MISSING_DEPENDENCIES)
  CMakeLists.txt:781 (find_package)


CMake Warning at /usr/share/cmake-3.6/Modules/FindBoost.cmake:743 (message):
  Imported targets not available for Boost version 106400
Call Stack (most recent call first):
  /usr/share/cmake-3.6/Modules/FindBoost.cmake:842 (_Boost_COMPONENT_DEPENDENCIES)
  /usr/share/cmake-3.6/Modules/FindBoost.cmake:1411 (_Boost_MISSING_DEPENDENCIES)
  CMakeLists.txt:781 (find_package)


CMake Warning at /usr/share/cmake-3.6/Modules/FindBoost.cmake:743 (message):
  Imported targets not available for Boost version 106400
Call Stack (most recent call first):
  /usr/share/cmake-3.6/Modules/FindBoost.cmake:842 (_Boost_COMPONENT_DEPENDENCIES)
  /usr/share/cmake-3.6/Modules/FindBoost.cmake:1411 (_Boost_MISSING_DEPENDENCIES)
  CMakeLists.txt:781 (find_package)


CMake Warning at /usr/share/cmake-3.6/Modules/FindBoost.cmake:743 (message):
  Imported targets not available for Boost version 106400
Call Stack (most recent call first):
  /usr/share/cmake-3.6/Modules/FindBoost.cmake:842 (_Boost_COMPONENT_DEPENDENCIES)
  /usr/share/cmake-3.6/Modules/FindBoost.cmake:1411 (_Boost_MISSING_DEPENDENCIES)
  CMakeLists.txt:781 (find_package)


CMake Warning at /usr/share/cmake-3.6/Modules/FindBoost.cmake:743 (message):
  Imported targets not available for Boost version 106400
Call Stack (most recent call first):
  /usr/share/cmake-3.6/Modules/FindBoost.cmake:842 (_Boost_COMPONENT_DEPENDENCIES)
  /usr/share/cmake-3.6/Modules/FindBoost.cmake:1411 (_Boost_MISSING_DEPENDENCIES)
  CMakeLists.txt:781 (find_package)


CMake Warning at /usr/share/cmake-3.6/Modules/FindBoost.cmake:743 (message):
  Imported targets not available for Boost version 106400
Call Stack (most recent call first):
  /usr/share/cmake-3.6/Modules/FindBoost.cmake:842 (_Boost_COMPONENT_DEPENDENCIES)
  /usr/share/cmake-3.6/Modules/FindBoost.cmake:1411 (_Boost_MISSING_DEPENDENCIES)
  CMakeLists.txt:781 (find_package)


CMake Warning at /usr/share/cmake-3.6/Modules/FindBoost.cmake:743 (message):
  Imported targets not available for Boost version 106400
Call Stack (most recent call first):
  /usr/share/cmake-3.6/Modules/FindBoost.cmake:842 (_Boost_COMPONENT_DEPENDENCIES)
  /usr/share/cmake-3.6/Modules/FindBoost.cmake:1411 (_Boost_MISSING_DEPENDENCIES)
  CMakeLists.txt:781 (find_package)


-- Found Boost Version: 106400
-- Found readline library at: /usr
-- Found Git: /usr/bin/git
-- Configuring incomplete, errors occurred!
See also "/root/monero/build/release/CMakeFiles/CMakeOutput.log".
See also "/root/monero/build/release/CMakeFiles/CMakeError.log".
Makefile:53: recipe for target 'cmake-release' failed
make: *** [cmake-release] Error 1
root@:~/monero#
`

## moneromooo-monero | 2018-08-30T14:45:55+00:00
git submodule init && git submodule update, from the readme.

## KnoAll | 2018-08-30T16:21:52+00:00
Aah, thank you. It is making! Thanks again, and apologies again for the n00b questions.

## KnoAll | 2018-08-31T14:24:13+00:00
This was running along happily but then seems to have died...


`[ 78%] Linking CXX static library libdaemon_messages.a
make[3]: Leaving directory '/root/monero/build/release'
[ 78%] Built target daemon_messages
make[3]: Entering directory '/root/monero/build/release'
Scanning dependencies of target daemon_rpc_server
make[3]: Leaving directory '/root/monero/build/release'
make[3]: Entering directory '/root/monero/build/release'
[ 78%] Linking CXX static library libdaemon_rpc_server.a
make[3]: Leaving directory '/root/monero/build/release'
[ 78%] Built target daemon_rpc_server
make[3]: Entering directory '/root/monero/build/release'
Scanning dependencies of target obj_wallet
make[3]: Leaving directory '/root/monero/build/release'
make[3]: Entering directory '/root/monero/build/release'
[ 79%] Building CXX object src/wallet/CMakeFiles/obj_wallet.dir/wallet2.cpp.o
c++: internal compiler error: Killed (program cc1plus)
Please submit a full bug report,
with preprocessed source if appropriate.
See <file:///usr/share/doc/gcc-4.9/README.Bugs> for instructions.
src/wallet/CMakeFiles/obj_wallet.dir/build.make:62: recipe for target 'src/wallet/CMakeFiles/obj_wallet.dir/wallet2.cpp.o' failed
make[3]: *** [src/wallet/CMakeFiles/obj_wallet.dir/wallet2.cpp.o] Error 4
make[3]: Leaving directory '/root/monero/build/release'
CMakeFiles/Makefile2:2294: recipe for target 'src/wallet/CMakeFiles/obj_wallet.dir/all' failed
make[2]: *** [src/wallet/CMakeFiles/obj_wallet.dir/all] Error 2
make[2]: Leaving directory '/root/monero/build/release'
Makefile:138: recipe for target 'all' failed
make[1]: *** [all] Error 2
make[1]: Leaving directory '/root/monero/build/release'
Makefile:57: recipe for target 'release' failed
make: *** [release] Error 2
`


## moneromooo-monero | 2018-08-31T14:35:46+00:00
You're out of memory. Use more memory. Kill firefox. Add swap. Don't use -j if you did.

## moneromooo-monero | 2018-09-14T11:26:08+00:00
Did the patch work ?

## KnoAll | 2018-09-18T17:29:16+00:00
@moneromooo-monero Unfortunately I was never able to get this working. I changed my approach and simply used your offline generator html package as all i was trying to do was create an offline wallet. 
Thanks for your help, and thanks for the html package too!


# Action History
- Created by: KnoAll | 2018-08-23T16:28:20+00:00
- Closed at: 2018-09-18T17:29:17+00:00
