---
title: 'c++: error: unrecognized command line option ‘-maes’'
source_url: https://github.com/monero-project/monero/issues/954
author: ghost
assignees: []
labels:
- arm
created_at: '2016-08-10T11:58:24+00:00'
updated_at: '2018-03-03T22:35:32+00:00'
type: issue
status: closed
closed_at: '2016-08-16T21:45:43+00:00'
---

# Original Description
Hi, have just tried to compile from source on the Odroid C2 (ARM64) running a clean install of Ubuntu 16.04 Xenial server edition from Armbian (http://www.armbian.com/odroid-c2/) and am getting the seemingly fatal error above. 

Followed the instructions here:
https://moneroexamples.github.io/compile-monero-09-on-ubuntu-16-04/

And installed the extra packages identified by ferretinjapan here:
https://www.reddit.com/r/Monero/comments/4wkgmh/gui_release_keeps_getting_closer/

Screen dump:

nodey@odroidc2:~$ git clone https://github.com/monero-project/bitmonero.git
Cloning into 'bitmonero'...
remote: Counting objects: 16008, done.
remote: Total 16008 (delta 0), reused 0 (delta 0), pack-reused 16008
Receiving objects: 100% (16008/16008), 62.32 MiB | 3.93 MiB/s, done.
Resolving deltas: 100% (11480/11480), done.
Checking connectivity... done.
nodey@odroidc2:~$ cd bitmonero/
nodey@odroidc2:~/bitmonero$ make release
mkdir -p build/release
cd build/release && cmake -D CMAKE_BUILD_TYPE=Release ../..
-- The C compiler identification is GNU 5.4.0
-- The CXX compiler identification is GNU 5.4.0
-- Check for working C compiler: /usr/bin/cc
-- Check for working C compiler: /usr/bin/cc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting C compile features - done
-- Check for working CXX compiler: /usr/bin/c++
-- Check for working CXX compiler: /usr/bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Building natively on aarch64
-- Could not find DEVELOPER_LOCAL_TOOLS in env (not required)
-- BOOST_IGNORE_SYSTEM_PATHS defaults to OFF
-- Could not find DEVELOPER_LIBUNBOUND_OLD in env (not required)
-- Building for a 64-bit system
-- Could not find DATABASE in env (not required unless you want to change database type from default: lmdb)
-- Using LMDB as default DB type
-- Could not find libunwind (missing:  LIBUNWIND_INCLUDE_DIR LIBUNWIND_LIBRARIES) 
-- Stack trace on exception disabled
-- Looking for pthread.h
-- Looking for pthread.h - found
-- Looking for pthread_create
-- Looking for pthread_create - not found
-- Check if compiler accepts -pthread
-- Check if compiler accepts -pthread - yes
-- Found Threads: TRUE  
-- Could not find miniupnp
-- Using miniupnpc from local source tree (/external/miniupnpc)
-- Looking for libunbound
-- Found libunbound include (unbound.h) in /usr/include
-- Found libunbound shared library
-- Using 64-bit LMDB from source tree
-- AES support enabled
-- Found Git: /usr/bin/git
CMake Warning (dev) at cmake/MergeStaticLibs.cmake:43 (get_target_property):
  Policy CMP0026 is not set: Disallow use of the LOCATION target property.
  Run "cmake --help-policy CMP0026" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  The LOCATION property should not be read from target "wallet".  Use the
  target name directly with add_custom_command, or use the generator
  expression $<TARGET_FILE>, as appropriate.

Call Stack (most recent call first):
  src/wallet/CMakeLists.txt:79 (merge_static_libs)
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at cmake/MergeStaticLibs.cmake:43 (get_target_property):
  Policy CMP0026 is not set: Disallow use of the LOCATION target property.
  Run "cmake --help-policy CMP0026" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  The LOCATION property should not be read from target "cryptonote_core".
  Use the target name directly with add_custom_command, or use the generator
  expression $<TARGET_FILE>, as appropriate.

Call Stack (most recent call first):
  src/wallet/CMakeLists.txt:79 (merge_static_libs)
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at cmake/MergeStaticLibs.cmake:43 (get_target_property):
  Policy CMP0026 is not set: Disallow use of the LOCATION target property.
  Run "cmake --help-policy CMP0026" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  The LOCATION property should not be read from target "mnemonics".  Use the
  target name directly with add_custom_command, or use the generator
  expression $<TARGET_FILE>, as appropriate.

Call Stack (most recent call first):
  src/wallet/CMakeLists.txt:79 (merge_static_libs)
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at cmake/MergeStaticLibs.cmake:43 (get_target_property):
  Policy CMP0026 is not set: Disallow use of the LOCATION target property.
  Run "cmake --help-policy CMP0026" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  The LOCATION property should not be read from target "common".  Use the
  target name directly with add_custom_command, or use the generator
  expression $<TARGET_FILE>, as appropriate.

Call Stack (most recent call first):
  src/wallet/CMakeLists.txt:79 (merge_static_libs)
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at cmake/MergeStaticLibs.cmake:43 (get_target_property):
  Policy CMP0026 is not set: Disallow use of the LOCATION target property.
  Run "cmake --help-policy CMP0026" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  The LOCATION property should not be read from target "crypto".  Use the
  target name directly with add_custom_command, or use the generator
  expression $<TARGET_FILE>, as appropriate.

Call Stack (most recent call first):
  src/wallet/CMakeLists.txt:79 (merge_static_libs)
This warning is for project developers.  Use -Wno-dev to suppress it.

-- will be merging /home/nodey/bitmonero/build/release/lib/libwallet.a;/home/nodey/bitmonero/build/release/src/cryptonote_core/libcryptonote_core.a;/home/nodey/bitmonero/build/release/src/mnemonics/libmnemonics.a;/home/nodey/bitmonero/build/release/src/common/libcommon.a;/home/nodey/bitmonero/build/release/src/crypto/libcrypto.a
CMake Warning (dev) at cmake/MergeStaticLibs.cmake:85 (get_target_property):
  Policy CMP0026 is not set: Disallow use of the LOCATION target property.
  Run "cmake --help-policy CMP0026" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  The LOCATION property should not be read from target "wallet_merged".  Use
  the target name directly with add_custom_command, or use the generator
  expression $<TARGET_FILE>, as appropriate.

Call Stack (most recent call first):
  src/wallet/CMakeLists.txt:79 (merge_static_libs)
This warning is for project developers.  Use -Wno-dev to suppress it.

-- outfile location is /home/nodey/bitmonero/build/release/lib/libwallet_merged.a
-- Found Doxygen: /usr/bin/doxygen (found version "1.8.11") 
-- Configuring done
-- Generating done
-- Build files have been written to: /home/nodey/bitmonero/build/release
cd build/release && make
make[1]: Entering directory '/home/nodey/bitmonero/build/release'
make[2]: Entering directory '/home/nodey/bitmonero/build/release'
make[3]: Entering directory '/home/nodey/bitmonero/build/release'
Scanning dependencies of target version
make[3]: Leaving directory '/home/nodey/bitmonero/build/release'
make[3]: Entering directory '/home/nodey/bitmonero/build/release'
[  1%] Generating version/version.h
-- You are currently on commit 0fbe9cf
-- The most recent tag was at e7c8a32
-- You are ahead of or behind a tagged release
make[3]: Leaving directory '/home/nodey/bitmonero/build/release'
[  1%] Built target version
make[3]: Entering directory '/home/nodey/bitmonero/build/release'
Scanning dependencies of target upnpc-static
make[3]: Leaving directory '/home/nodey/bitmonero/build/release'
make[3]: Entering directory '/home/nodey/bitmonero/build/release'
[  1%] Building C object external/miniupnpc/CMakeFiles/upnpc-static.dir/igd_desc_parse.c.o
[  2%] Building C object external/miniupnpc/CMakeFiles/upnpc-static.dir/miniupnpc.c.o
[  3%] Building C object external/miniupnpc/CMakeFiles/upnpc-static.dir/minixml.c.o
[  4%] Building C object external/miniupnpc/CMakeFiles/upnpc-static.dir/minisoap.c.o
[  4%] Building C object external/miniupnpc/CMakeFiles/upnpc-static.dir/minissdpc.c.o
[  5%] Building C object external/miniupnpc/CMakeFiles/upnpc-static.dir/miniwget.c.o
[  6%] Building C object external/miniupnpc/CMakeFiles/upnpc-static.dir/upnpc.c.o
[  7%] Building C object external/miniupnpc/CMakeFiles/upnpc-static.dir/upnpcommands.c.o
[  8%] Building C object external/miniupnpc/CMakeFiles/upnpc-static.dir/upnpdev.c.o
[  8%] Building C object external/miniupnpc/CMakeFiles/upnpc-static.dir/upnpreplyparse.c.o
[  9%] Building C object external/miniupnpc/CMakeFiles/upnpc-static.dir/upnperrors.c.o
[ 10%] Building C object external/miniupnpc/CMakeFiles/upnpc-static.dir/connecthostport.c.o
[ 11%] Building C object external/miniupnpc/CMakeFiles/upnpc-static.dir/portlistingparse.c.o
[ 12%] Building C object external/miniupnpc/CMakeFiles/upnpc-static.dir/receivedata.c.o
[ 12%] Linking C static library libminiupnpc.a
make[3]: Leaving directory '/home/nodey/bitmonero/build/release'
[ 12%] Built target upnpc-static
make[3]: Entering directory '/home/nodey/bitmonero/build/release'
Scanning dependencies of target lmdb
make[3]: Leaving directory '/home/nodey/bitmonero/build/release'
make[3]: Entering directory '/home/nodey/bitmonero/build/release'
[ 13%] Building C object external/db_drivers/liblmdb/CMakeFiles/lmdb.dir/mdb.c.o
[ 14%] Building C object external/db_drivers/liblmdb/CMakeFiles/lmdb.dir/midl.c.o
[ 15%] Linking C static library liblmdb.a
make[3]: Leaving directory '/home/nodey/bitmonero/build/release'
[ 15%] Built target lmdb
make[3]: Entering directory '/home/nodey/bitmonero/build/release'
Scanning dependencies of target otshell_utils
make[3]: Leaving directory '/home/nodey/bitmonero/build/release'
make[3]: Entering directory '/home/nodey/bitmonero/build/release'
[ 16%] Building CXX object contrib/otshell_utils/CMakeFiles/otshell_utils.dir/windows_stream.cpp.o
c++: error: unrecognized command line option ‘-maes’
contrib/otshell_utils/CMakeFiles/otshell_utils.dir/build.make:62: recipe for target 'contrib/otshell_utils/CMakeFiles/otshell_utils.dir/windows_stream.cpp.o' failed
make[3]: **\* [contrib/otshell_utils/CMakeFiles/otshell_utils.dir/windows_stream.cpp.o] Error 1
make[3]: Leaving directory '/home/nodey/bitmonero/build/release'
CMakeFiles/Makefile2:321: recipe for target 'contrib/otshell_utils/CMakeFiles/otshell_utils.dir/all' failed
make[2]: **\* [contrib/otshell_utils/CMakeFiles/otshell_utils.dir/all] Error 2
make[2]: Leaving directory '/home/nodey/bitmonero/build/release'
Makefile:138: recipe for target 'all' failed
make[1]: **\* [all] Error 2
make[1]: Leaving directory '/home/nodey/bitmonero/build/release'
Makefile:51: recipe for target 'release' failed
make: **\* [release] Error 2


# Discussion History
## hyc | 2016-08-11T20:12:18+00:00
Yeah, we need to remove the -maes flag when compiling on ARM, that flag is x86-specific.


## hyc | 2016-08-11T20:59:51+00:00
In c6501607 we removed the flag for ARM6 and ARM7. It should just be removed for all ARM, since AES support on ARM8 doesn't use that flag anyway.


## ghost | 2016-08-11T22:53:20+00:00
Thanks @hyc - I hope to be able to get a node up and running soon. The Odroid C2 is the next version up from the ARM board used for the 'Bitnode B1' and I was thinking of making it my low power, live-in-the-corner node/miner.

I've just been reading and have found that this board uses an Amlogic S905 - a quad core ARMv8 Cortex-A53 CPU which claims to have a hardware "Crypto engine for AES-128/192/256, SHA-1/SHA-2 engine"

Hmm...

Do you know what I should change in the makefile to enable AES support on this chip?

Thanks!


## hyc | 2016-08-11T23:18:07+00:00
Nobody has written the necessary ARM-specific code to leverage its accelerated AES instructions yet. It's been on my todo list for awhile but I got sidetracked over the summer.


## hyc | 2016-08-11T23:29:54+00:00
I've got a geekbox running as my dedicated node these days. (8 core Cortex A-53, 2GB RAM). Have a Pine A64 ready to run too but not much point until I get the AES code written.


## ghost | 2016-08-12T01:20:22+00:00
So I got it to compile by manually tinkering with CMakelists.txt to create an ARM8 option by checking $ARCH for "aarch64" and then using the following CMAKE_C_FLAGS and CMAKE_CXX_FLAGS:

-march=armv8-a+crypto -mtune=cortex-a53 -mfix-cortex-a53-835769 -mfix-cortex-a53-843419

Now I'm sure there's a better way of checking for the A53 architecture and including the extra bugfix flags in a future version of CMakelists.txt, for example by querying /proc/cpuinfo for the first core and checking the reported CPU part number: 0xd03 signals Cortex-A53.

Interestingly the compiler wouldn't accept mfpu=crypto-neon-fp-armv8 or any mcpu options...


## ghost | 2016-08-13T19:09:11+00:00
Hi again @hyc - I've just submitted my first ever pull request on GitHub to update CMakeLists.txt with my new version

Would you mind checking it out for me, and then maybe this issue can be closed?


## ghost | 2016-08-16T21:45:42+00:00
I've now finished a version of CMakeLists.txt that detects and accounts for ARMv8 processors and submitted a pull.


## gldneagl | 2018-03-03T22:35:32+00:00
Where may I find this updated code "that detects and accounts for ARMv8 processors?

# Action History
- Created by: ghost | 2016-08-10T11:58:24+00:00
- Closed at: 2016-08-16T21:45:43+00:00
