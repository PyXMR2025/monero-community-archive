---
title: windows build
source_url: https://github.com/monero-project/monero/issues/270
author: Gingeropolous
assignees: []
labels: []
created_at: '2015-04-25T03:09:07+00:00'
updated_at: '2015-04-25T14:31:44+00:00'
type: issue
status: closed
closed_at: '2015-04-25T14:31:44+00:00'
---

# Original Description
tried to follow instructions as provided

$ make -j 2
mkdir -p build/release
cd build/release && cmake -D BUILD_TESTS=ON -D CMAKE_BUILD_TYPE=release ../.. &&                                            make
-- Building for: Visual Studio 12 2013
-- Could not find DEVELOPER_LOCAL_TOOLS in env (not required)
-- BOOST_IGNORE_SYSTEM_PATHS defaults to OFF
-- Could not find DEVELOPER_LIBUNBOUND_OLD in env (not required)
-- Building for a 32-bit system
-- Could not find DATABASE in env (not required unless you want to change databa                                           se type from default: lmdb)
-- Could not find miniupnp
-- Using miniupnpc from local source tree for static build
-- Looking for libunbound
CMake Error at C:/msys64/mingw64/share/cmake-3.2/Modules/FindPackageHandleStanda                                           rdArgs.cmake:138 (message):
  Could NOT find OpenSSL, try to set the path to OpenSSL root folder in the
  system variable OPENSSL_ROOT_DIR (missing: OPENSSL_LIBRARIES) (found
  version "1.0.2a")
Call Stack (most recent call first):
  C:/msys64/mingw64/share/cmake-3.2/Modules/FindPackageHandleStandardArgs.cmake:                                           374 (_FPHSA_FAILURE_MESSAGE)
  C:/msys64/mingw64/share/cmake-3.2/Modules/FindOpenSSL.cmake:324 (find_package_                                           handle_standard_args)
  external/unbound/CMakeLists.txt:33 (find_package)

-- Configuring incomplete, errors occurred!
See also "C:/msys64/home/ginger/bitmonero_latest/bitmonero/build/release/CMakeFil                                           es/CMakeOutput.log".
Makefile:30: recipe for target 'release-all' failed
make: **\* [release-all] Error 1


# Discussion History
## tewinget | 2015-04-25T04:47:16+00:00
I'll look into this later, but there shouldn't be any mention of visual
studio in the build process.  I fear you omitted the cmake step in the
instructions.
On Apr 24, 2015 11:09 PM, "Gingeropolous" notifications@github.com wrote:

> tried to follow instructions as provided
> 
> $ make -j 2
> mkdir -p build/release
> cd build/release && cmake -D BUILD_TESTS=ON -D CMAKE_BUILD_TYPE=release
> ../.. && make
> -- Building for: Visual Studio 12 2013
> -- Could not find DEVELOPER_LOCAL_TOOLS in env (not required)
> -- BOOST_IGNORE_SYSTEM_PATHS defaults to OFF
> -- Could not find DEVELOPER_LIBUNBOUND_OLD in env (not required)
> -- Building for a 32-bit system
> -- Could not find DATABASE in env (not required unless you want to change
> databa se type from default: lmdb)
> -- Could not find miniupnp
> -- Using miniupnpc from local source tree for static build
> -- Looking for libunbound
> CMake Error at
> C:/msys64/mingw64/share/cmake-3.2/Modules/FindPackageHandleStanda
> rdArgs.cmake:138 (message):
> Could NOT find OpenSSL, try to set the path to OpenSSL root folder in the
> system variable OPENSSL_ROOT_DIR (missing: OPENSSL_LIBRARIES) (found
> version "1.0.2a")
> Call Stack (most recent call first):
> C:/msys64/mingw64/share/cmake-3.2/Modules/FindPackageHandleStandardArgs.cmake:
> 374 (
> _FPHSA_FAILURE_MESSAGE)
> C:/msys64/mingw64/share/cmake-3.2/Modules/FindOpenSSL.cmake:324
> (find_package_ handle_standard_args)
> external/unbound/CMakeLists.txt:33 (find_package)
> 
> -- Configuring incomplete, errors occurred!
> See also
> "C:/msys64/home/ginger/bitmonero_latest/bitmonero/build/release/CMakeFil
> es/CMakeOutput.log".
> Makefile:30: recipe for target 'release-all' failed
> make: **\* [release-all] Error 1
> 
> —
> Reply to this email directly or view it on GitHub
> https://github.com/monero-project/bitmonero/issues/270.


## fluffypony | 2015-04-25T07:09:07+00:00
Definitely omitted the CMake step:)


## Gingeropolous | 2015-04-25T13:56:56+00:00
nah uh! I followed step-by-step. 

$ cmake -G "MSYS Makefiles" -D CMAKE_BUILD_TYPE=Release -D CMAKE_TOOLCHAIN_FILE=                                                                                                                ../cmake/64-bit-toolchain.cmake -D MSYS2_FOLDER=c:/msys64 ..
-- Could not find DEVELOPER_LOCAL_TOOLS in env (not required)
-- BOOST_IGNORE_SYSTEM_PATHS defaults to OFF
-- Could not find DEVELOPER_LIBUNBOUND_OLD in env (not required)
-- Building for a 64-bit system
-- Could not find DATABASE in env (not required unless you want to change databa                                                                                                                se type from default: lmdb)
-- Could not find miniupnp
-- Using miniupnpc from local source tree for static build
-- Looking for libunbound
-- Using 64-bit LMDB from source tree
-- Enabling AES support
-- Found Git: C:/Program Files (x86)/Git/cmd/git.exe
Doxygen: graphviz not found - graphs disabled
-- Could NOT find Doxygen (missing:  DOXYGEN_EXECUTABLE)
-- Configuring done
-- Generating done
CMake Warning:
  Manually-specified variables were not used by the project:

```
CMAKE_TOOLCHAIN_FILE
```

-- Build files have been written to: C:/msys64/home/ginger/bitmonero_latest/bitmo                                                                                                                nero/build

but I'll see if any of the paths are wonky. 


## fluffypony | 2015-04-25T13:59:25+00:00
That doesn't look like the expected output from within a mingw-w64 shell; it would never find git in Program Files. Are you in Command Prompt or a mingw-w64 shell?


## fluffypony | 2015-04-25T14:00:13+00:00
Also when you run make is it from within the build subdirectory or the root of the source?


## fluffypony | 2015-04-25T14:00:55+00:00
Lastly, try running "make release-static-win64" from the source root


## Gingeropolous | 2015-04-25T14:01:12+00:00
mingw-w64 shell. I'm trying now by running make in the /build directory. :)

yeah, before I was running the root of the source like Im used to in linux.

there's subtle nuances that should be in the instructions... i'll try and come up with something more explicit


## Gingeropolous | 2015-04-25T14:03:00+00:00
i have installed git for windows.... so that may explain why it found git in program files. 


## fluffypony | 2015-04-25T14:07:37+00:00
It'll ignore git for Windows, because it's not git for mingw-w64:)

Your problem was running `make` from the source root. The README has you `cd` into the build folder, but then it says "run `make`" without telling you to change folders again. Most people are only building for one OS, so they won't be familiar with build instructions for Linux / OS X. For those people it's easier to state what _should_ be done without mentioning what _shouldn't_, as people tend to blindly run commands even if it says "never, EVER run `rm -rf /`" because that appears in a list of instructions so logic.

Those that are building for multiple platforms are expected to work through the differences in build instructions / environments, and we'll gladly help them work through the differences (as we are on this thread).


## Gingeropolous | 2015-04-25T14:31:44+00:00
yes this makes sense. I see now where I went wrong. I overlooked the instructions to open minGW, and opened up msys instead, because you can open either via the start menu, and unfortunately it seems whenever I've tried to follow these instructions its at hours of the night when my brain seems to follow some variant of the 6x6 rule, and msys is in different colors in the instructions, so thats what happens.

The instructions are explicit, and I am at fault. I will lash myself accordingly. 

As always, thank you for your patience.

Next I will test whether I can build on my toaster. 

It built. it is running. Take that entropy. 


# Action History
- Created by: Gingeropolous | 2015-04-25T03:09:07+00:00
- Closed at: 2015-04-25T14:31:44+00:00
