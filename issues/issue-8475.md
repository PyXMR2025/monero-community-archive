---
title: mingw compilation broken
source_url: https://github.com/monero-project/monero/issues/8475
author: Basement-Science
assignees: []
labels: []
created_at: '2022-07-31T21:08:27+00:00'
updated_at: '2022-08-04T11:18:50+00:00'
type: issue
status: closed
closed_at: '2022-07-31T21:32:28+00:00'
---

# Original Description
I have been successfully building monero with minGW several times before. However now in v0.18.0.0 it still compiles without errors, but monerod.exe immediately throws an error on launch saying that execution cannot continue because `libunbound-8.dll` cannot be found.

Monero has never generated any dlls before and the binaries from [getmonero.org](getmonero.org) dont need any either, so something must be wrong with compilation. All my packages are up to date as well. I've also double-checked the instructions in the Readme.

If it helps, here is the start of console output:
```Starting to compile monero...
mkdir -p build/"MINGW64_NT-10.0-22000/release-v0.18"/release
cd build/"MINGW64_NT-10.0-22000/release-v0.18"/release && cmake -G "MSYS Makefiles" -D STATIC=ON -D ARCH="x86-64" -D BUILD_64=ON -D CMAKE_BUILD_TYPE=Release -D BUILD_TAG="win-x64" -D CMAKE_TOOLCHAIN_FILE=../../../../cmake/64-bit-toolchain.cmake -D MSYS2_FOLDER=C:/msys64/ ../../../.. && make
-- CMake version 3.23.3
-- Found ccache C:/msys64/usr/bin/ccache.exe, but is UNUSABLE! Return code: FALSE
-- Building build tag win-x64
-- Checking submodules
-- Submodule 'external/miniupnp' is up-to-date
-- Submodule 'external/rapidjson' is up-to-date
-- Submodule 'external/trezor-common' is up-to-date
-- Submodule 'external/randomx' is up-to-date
-- Submodule 'external/supercop' is up-to-date
-- Could not find DEVELOPER_LOCAL_TOOLS in env (not required)
-- BOOST_IGNORE_SYSTEM_PATHS defaults to OFF
-- Building for a 64-bit system
-- Building internal libraries as static
-- MSYS location: C:/msys64
-- Using LMDB as default DB type
-- looking for liblzma
-- liblzma found
-- Could not find libunwind (missing: LIBUNWIND_INCLUDE_DIR)
-- Stack trace on exception disabled
-- Using OpenSSL include dir at C:/msys64/mingw64/include
CMake Warning (dev) at C:/msys64/mingw64/share/cmake/Modules/FindPackageHandleStandardArgs.cmake:438 (message):
  The package name passed to `find_package_handle_standard_args` (MiniUPnPc)
  does not match the name of the calling package (Miniupnpc).  This can lead
  to problems in calling code that expects `find_package` result variables
  (e.g., `_FOUND`) to follow a certain pattern.
Call Stack (most recent call first):
  cmake/FindMiniupnpc.cmake:39 (find_package_handle_standard_args)
  external/CMakeLists.txt:38 (find_package)
This warning is for project developers.  Use -Wno-dev to suppress it.

-- Could NOT find MiniUPnPc (missing: MINIUPNP_INCLUDE_DIR MINIUPNP_LIBRARY)
-- Using in-tree miniupnpc
-- Looking for libunbound
-- Found libunbound include (unbound.h) in C:/msys64/mingw64/include
-- Found libunbound library
-- Using 64-bit LMDB from source tree
-- Backtrace_LIBRARY:
-- Could NOT find Backtrace (missing: Backtrace_LIBRARY Backtrace_INCLUDE_DIR)
-- Setting CXX flag -maes
-- Setting C flag -maes
-- Using HIDAPI include dir at C:/msys64/mingw64/include/hidapi
-- Could NOT find Protobuf (missing: Protobuf_LIBRARIES Protobuf_INCLUDE_DIR)
-- Could NOT find Protobuf (missing: Protobuf_LIBRARIES Protobuf_INCLUDE_DIR)
-- Could not find Protobuf
-- Building on AMD64 for x86-64
-- AES support enabled
-- Performing Test _Werror__fcf_protection=full_c
-- Performing Test _Werror__fcf_protection=full_c - Success
-- Performing Test _Werror__fcf_protection=full_cxx
-- Performing Test _Werror__fcf_protection=full_cxx - Success
-- Performing Test _Werror__Werror=switch_c
-- Performing Test _Werror__Werror=switch_c - Success
-- Performing Test _Werror__Werror=switch_cxx
-- Performing Test _Werror__Werror=switch_cxx - Success
-- Performing Test _Werror__Werror=return_type_c
-- Performing Test _Werror__Werror=return_type_c - Success
-- Performing Test _Werror__Werror=return_type_cxx
-- Performing Test _Werror__Werror=return_type_cxx - Success
-- Using C security hardening flags:  -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -fstack-protector -fstack-protector-strong -fcf-protection=full -Werror=switch -Werror=return-type
-- Using C++ security hardening flags:  -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -fstack-protector -fstack-protector-strong -fcf-protection=full -Werror=switch -Werror=return-type
-- Using linker security hardening flags:  -pie -Wl,--dynamicbase -Wl,--nxcompat -Wl,--high-entropy-va
-- Found Boost Version: 107900
-- Could NOT find Readline (missing: Readline_INCLUDE_DIR)
-- Could not find GNU readline library so building without readline support
-- Found Git: C:/msys64/usr/bin/git.exe
-- You are currently on commit 0942d32fd
-- You are ahead of or behind a tagged release
Monero crypto autodetect failed to find any libraries for target platform
Defaulting to internal crypto library for wallet
-- Trezor support disabled
-- Not building tests
-- Not building debug utilities
Doxygen: graphviz not found - graphs disabled
-- Could NOT find Doxygen (missing: DOXYGEN_EXECUTABLE)
-- Configuring done
-- Generating done
```

# Discussion History
## hyc | 2022-07-31T21:32:28+00:00
previous releases used libunbound in the Monero source tree, but that was removed for v0.18. So you either need to make sure that a static version of libunbound is installed on your build machine, or bundle the libunbound.dll with the monerod.exe.

## Basement-Science | 2022-07-31T22:41:00+00:00
Soo.. in other words the instructions are no longer valid, the build wont output the same independent exe as the official download and I dont know how to best compile the lib etc. That also doesnt explain why the official (cross-compiled*) binary apparently does contain the DLL even though it is apparently no longer in the source tree. *which btw also doesnt work on all distros: #8409

Plus there's no real standard way to "install" a library in Windows that doesnt break all conventions to my knowledge. Throwing a DLL next to the exe is therefore the only proper option. And obviously downloading a random DLL from a random website, for a security-critical program especially, is not really a great idea either..

So I dont really get why you're closing this. In my view this either needs to get fixed, or at least declared to be broken in the README.

## selsta | 2022-07-31T23:05:03+00:00
The problem is that the unbound package does not contain a static library: https://packages.msys2.org/package/mingw-w64-x86_64-unbound so the resulting binary also isn't fully static.

For cross compiling we build our own static unbound library, you would have to do the same to solve this issue.

> So I dont really get why you're closing this.

Compilation isn't broken and when you start the binary out of the msys2 console it should also start correctly. The Windows README instructions explain for developers / users how to build monero from source, not how to build the exact same binary as we offer on getmonero.org. For that we have the gitian build system: https://github.com/monero-project/monero/tree/master/contrib/gitian

> In my view this either needs to get fixed

This should be fixed on msys2/mingw package maintainers side, you might want to reach out to them and ask them to remove this line so that they install a static library: https://github.com/msys2/MINGW-packages/blob/master/mingw-w64-unbound/PKGBUILD#L40

## Basement-Science | 2022-08-01T02:08:28+00:00
> Compilation isn't broken and when you start the binary out of the msys2 console it should also start correctly. The Windows README instructions explain for developers / users how to build monero from source, not how to build the exact same binary as we offer on getmonero.org. For that we have the gitian build system: https://github.com/monero-project/monero/tree/master/contrib/gitian

Well in my mind, if the instructions dont result in a complete, functional program, the instructions are wrong at least. 

> This should be fixed on msys2/mingw package maintainers side, you might want to reach out to them and ask them to remove this line so that they install a static library: https://github.com/msys2/MINGW-packages/blob/master/mingw-w64-unbound/PKGBUILD#L40

I dont really understand how their packaging system works, I imagine they have reasons to packaged it as they did. One of you guys can surely make this work properly.

## selsta | 2022-08-01T20:33:40+00:00
Opened this now: https://github.com/msys2/MINGW-packages/pull/12396

Once they merge this building static binaries should work as expected again.

## selsta | 2022-08-02T16:04:49+00:00
@Basement-Science msys2 merged my change and once they update the package the issue should be resolved. You can follow the queue here: https://packages.msys2.org/queue

## Basement-Science | 2022-08-04T11:04:01+00:00
Thank you. I tried it out now, and after updating packages **and deleting the old `bin` folder**, it works now. 

## selsta | 2022-08-04T11:18:50+00:00
Thanks for confirming!

# Action History
- Created by: Basement-Science | 2022-07-31T21:08:27+00:00
- Closed at: 2022-07-31T21:32:28+00:00
