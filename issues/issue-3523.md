---
title: release-v0.12 build issue on OSX 10.13.3 (High Sierra)
source_url: https://github.com/monero-project/monero/issues/3523
author: skaht
assignees: []
labels: []
created_at: '2018-03-30T03:17:22+00:00'
updated_at: '2018-04-15T22:31:31+00:00'
type: issue
status: closed
closed_at: '2018-04-15T22:31:31+00:00'
---

# Original Description
First time having issues with building Monero over the last 4 hard forks. Adding **zmq.hpp** to /usr/local/include did not fix issue when performing a **make release-static**.   The resulting monero/build/release/CMakeFiles/CMakeError.log file makes improper linking references to **-L/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.12.sdk/usr/lib** directory when the SDK goods are actually located at /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.13.sdk/usr/lib. Any suggestions?

# Discussion History
## skaht | 2018-03-30T04:22:46+00:00
% make release-static
mkdir -p build/release
cd build/release && cmake -D STATIC=ON -D ARCH="x86-64" -D BUILD_64=ON -D CMAKE_BUILD_TYPE=release ../.. && /Applications/Xcode.app/Contents/Developer/usr/bin/make
-- The C compiler identification is AppleClang 9.1.0.9020039
-- The CXX compiler identification is AppleClang 9.1.0.9020039
-- Check for working C compiler: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc
-- Check for working C compiler: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting C compile features - done
-- Check for working CXX compiler: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++
-- Check for working CXX compiler: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Building without build tag
-- Could not find DEVELOPER_LOCAL_TOOLS in env (not required)
-- BOOST_IGNORE_SYSTEM_PATHS defaults to OFF
-- Could not find DEVELOPER_LIBUNBOUND_OLD in env (not required)
-- Building for a 64-bit system
-- Building internal libraries as static
-- Could not find DATABASE in env (not required unless you want to change database type from default: lmdb)
-- Using LMDB as default DB type
-- Stack trace on exception disabled
-- Using OpenSSL found at /Users/Scott/usr2/local/opt/openssl
-- Found OpenSSL: /Users/Scott/usr2/local/opt/openssl/lib/libcrypto.a (found version "1.0.2n") 
-- Using OpenSSL include dir at /Users/Scott/usr2/local/opt/openssl/include
-- Found PkgConfig: /Users/Scott/usr2/local/bin/pkg-config (found version "0.29.2") 
-- Checking for module 'libpcsclite'
--   No package 'libpcsclite' found
-- Found PCSC: /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.13.sdk/System/Library/Frameworks/PCSC.framework  
-- Looking for memset_s in c
-- Looking for memset_s in c - found
-- Looking for explicit_bzero in c
-- Looking for explicit_bzero in c - not found
-- Looking for strptime
-- Looking for strptime - found
-- Could NOT find MiniUPnPc (missing:  MINIUPNP_INCLUDE_DIR MINIUPNP_LIBRARY) 
-- Using miniupnpc from local source tree for static build
-- Looking for libunbound
CMake Error at external/CMakeLists.txt:82 (add_subdirectory):
  The source directory

    /Users/Scott/Projects/Monero/monero-0.12.0.0/monero/external/unbound

  does not contain a CMakeLists.txt file.


-- Using 64-bit LMDB from source tree
-- Looking for pthread.h
-- Looking for pthread.h - found
-- Looking for pthread_create
-- Looking for pthread_create - found
-- Found Threads: TRUE  
-- Building on x86_64 for x86-64
-- Performing Test _Wformat_c
-- Performing Test _Wformat_c - Success
-- Performing Test _Wformat_cxx
-- Performing Test _Wformat_cxx - Success
-- Performing Test _Wformat_security_c
-- Performing Test _Wformat_security_c - Success
-- Performing Test _Wformat_security_cxx
-- Performing Test _Wformat_security_cxx - Success
-- Performing Test _fstack_protector_c
-- Performing Test _fstack_protector_c - Success
-- Performing Test _fstack_protector_cxx
-- Performing Test _fstack_protector_cxx - Success
-- Performing Test _fstack_protector_strong_c
-- Performing Test _fstack_protector_strong_c - Success
-- Performing Test _fstack_protector_strong_cxx
-- Performing Test _fstack_protector_strong_cxx - Success
-- Looking for -pie linker flag
-- Looking for -pie linker flag - found
-- Looking for -Wl,-z,relro linker flag
-- Looking for -Wl,-z,relro linker flag - not found
-- Looking for -Wl,-z,now linker flag
-- Looking for -Wl,-z,now linker flag - not found
-- Looking for -Wl,-z,noexecstack linker flag
-- Looking for -Wl,-z,noexecstack linker flag - not found
-- Looking for -Wl,-z,noexecheap linker flag
-- Looking for -Wl,-z,noexecheap linker flag - not found
-- Using C security hardening flags:  -Wformat -Wformat-security -fstack-protector -fstack-protector-strong
-- Using C++ security hardening flags:  -Wformat -Wformat-security -fstack-protector -fstack-protector-strong
-- Using linker security hardening flags:  -pie
-- AES support enabled
-- Found Boost Version: 106300
-- Could NOT find Readline (missing:  Readline_INCLUDE_DIR) 
-- Looking for rl_copy_text
-- Looking for rl_copy_text - not found
-- Looking for rl_filename_completion_function
-- Looking for rl_filename_completion_function - found
-- Could not find GNU readline library so building without readline support
CMake Error at **CMakeLists.txt:848** (message):
  Could not find required header zmq.hpp


-- Configuring incomplete, errors occurred!
See also "/Users/Scott/Projects/Monero/monero-0.12.0.0/monero/build/release/CMakeFiles/CMakeOutput.log".
See also "/Users/Scott/Projects/Monero/monero-0.12.0.0/monero/build/release/CMakeFiles/CMakeError.log".
make: *** [release-static] Error 1


## skaht | 2018-03-30T05:12:01+00:00
The **CMakeLists.txt** file leaves some clues about setting environmental variables such as: 1. Readline_ROOT_DIR, 2. Readline_INCLUDE_DIR, 3. ZMQ_INCLUDE_PATH. 

Additionally, this leaves some clues:
% **brew info readline**
readline: stable 7.0.3 (bottled) [keg-only]
Library for command-line editing
https://tiswww.case.edu/php/chet/readline/rltop.html
/Users/Scott/usr2/local/homebrew/Cellar/readline/6.3.8 (46 files, 2MB)
  Poured from bottle on 2015-12-21 at 18:28:21
/Users/Scott/usr2/local/homebrew/Cellar/readline/7.0.1 (46 files, 2.1MB)
  Built from source on 2017-02-05 at 22:36:44
/Users/Scott/usr2/local/homebrew/Cellar/readline/7.0.3_1 (46 files, 1.4MB)
  Built from source on 2018-03-29 at 22:03:22
From: https://github.com/Homebrew/homebrew-core/blob/master/Formula/readline.rb
==> Caveats
This formula is keg-only, which means it was not symlinked into /Users/Scott/usr2/local,
because macOS provides the BSD libedit library, which shadows libreadline.
In order to prevent conflicts when programs look for libreadline we are
defaulting this GNU Readline installation to keg-only..

If you need to have this software first in your PATH run:
  echo 'setenv PATH /Users/Scott/usr2/local/opt/readline/bin:$PATH' >> ~/.cshrc

For compilers to find this software you may need to set:
    LDFLAGS:  -L/Users/Scott/usr2/local/opt/readline/lib
    CPPFLAGS: -I/Users/Scott/usr2/local/opt/readline/include

However, still unable to resolve the the build issues.

## italocoin-project | 2018-03-30T07:59:23+00:00
> -- Looking for libunbound
> CMake Error at external/CMakeLists.txt:82 (add_subdirectory):
> The source directory
> 
> /Users/Scott/Projects/Monero/monero-0.12.0.0/monero/external/unbound
> does not contain a CMakeLists.txt file.

You need to clone the repo with `--recursive`, unbound is on external repo, check that out

> CMake Error at CMakeLists.txt:848 (message):
> Could not find required header zmq.hpp
> 
> -- Configuring incomplete, errors occurred!

I don;t know about mac i guess `brew install zeromq`
Ubuntu/debian install `libzmq-dev`  and for red hat `libzmq-devel`

## trevorbernard | 2018-03-30T19:03:29+00:00
It looks like you're missing cppzmq. https://github.com/zeromq/cppzmq

## skaht | 2018-04-03T20:01:22+00:00
@trevorbenard - Not missing https://github.com/zeromq/cppzmq.  However, *Monero* is behaving such that cppzmq headers must be installed at **/usr/local/include** which is locked down on my computer. https://github.com/zeromq/cppzmq/issues/193 shows how to install cppzmq package into an unprivileged directory.  However, defining an environmental variable called **ZMQ_INCLUDE_PATH** or defining **ZMQ_INCLUDE_PATH** as part of **make ZMQ_INCLUDE_PATH=/Users/Scott/Projects/Monero/monero-0.12.0.0/cppzmq/usr/local/include release-static** seems to have no impact on fixing Monero build errors. Any other suggestions?

## italocoin-project | 2018-04-04T05:06:13+00:00
Install zmqcpp an libzmq from source and add the prefix to /usr/local

## skaht | 2018-04-06T01:59:48+00:00
My bad. On the git clone, I'm guilty of dropping the **--recursive**.  

% git clone **--recursive** https://github.com/monero-project/monero

% git branch -a
\* master
  remotes/origin/HEAD -> origin/master
  remotes/origin/master
  remotes/origin/release-v0.11.0.0
  remotes/origin/release-v0.12

% git checkout release-v0.12
Branch release-v0.12 set up to track remote branch release-v0.12 from origin.
Switched to a new branch 'release-v0.12'
 
% git branch -v
  master        8361d60a Merge pull request #3434
\* release-v0.12 7090121b Merge pull request #3512

Summary of relevant **Homebrew** packages installed at this end:
/Users/Scott/usr2/local/homebrew/Cellar/**gcc/7.3.0_1** (1,487 files, 285.9MB) *
/Users/Scott/usr2/local/homebrew/Cellar/**cmake/3.11.0** (2,363 files, 32.9MB) *
/Users/Scott/usr2/local/homebrew/Cellar/**pkg-config/0.29.2** (11 files, 627.3KB) *
/Users/Scott/usr2/local/homebrew/Cellar/**boost/1.66.0** (13,101 files, 435.2MB) *
/Users/Scott/usr2/local/homebrew/Cellar/**openssl/1.0.2o_1** (1,783 files, 12.3MB) - Apple TLS overrides GNU, no homebrew symlinks in /Users/Scott/usr2/local/include
/Users/Scott/usr2/local/homebrew/Cellar/**unbound/1.7.0** (54 files, 4.7MB) *
/Users/Scott/usr2/local/homebrew/Cellar/**libsodium/1.0.16** (71 files, 945.2KB) *
/Users/Scott/usr2/local/homebrew/Cellar/**zeromq/4.2.5** (77 files, 2.7MB) *
/Users/Scott/usr2/local/homebrew/Cellar/**zmqpp/4.2.0** (237 files, 2.7MB) *
/Users/Scott/usr2/local/homebrew/Cellar/**readline/7.0.3_1** (46 files, 1.4MB) - Apple BSD overrides GNU, no homebrew symlinks in /Users/Scott/usr2/local/include

However, there is now a linking issue when executing a **make release-static**.
Code is compiling until [95%] is reached. 

[ 95%] Linking CXX executable ../../bin/monerod
clang: warning: argument unused during compilation: '-pie' [-Wunused-command-line-argument]
ld: warning: directory not found for option '-L/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/**MacOSX10.12.sdk**/usr/lib'
Undefined symbols for architecture x86_64:

% ls -l /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs
total 0
drwxr-xr-x  4 root  wheel  128 Mar 29 19:22 ./
drwxr-xr-x  5 root  wheel  160 Mar 19 23:28 ../
drwxr-xr-x  5 root  wheel  160 Mar 29 19:22 MacOSX.sdk/
lrwxr-xr-x  1 root  wheel   10 Sep 21  2017 MacOSX10.13.sdk@ -> MacOSX.sdk

macOS High Sierra uses a linker from **MacOSX10.13.sdk**, not **MacOSX10.12.sdk**.  **UNCLEAR HOW TO OVERRIDE THIS LINKING PATH ISSUE.**  The following brew queries provides insights about how Homebrew is being used at this end. Notice reference only to MacOSX10.13.sdk.

% brew --env
HOMEBREW_CC: clang
HOMEBREW_CXX: clang++
SDKROOT: /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.13.sdk
MAKEFLAGS: -j8
CMAKE_PREFIX_PATH: /Users/Scott/usr2/local
CMAKE_INCLUDE_PATH: /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.13.sdk/usr/include/libxml2:/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.13.sdk/usr/include/apache2:/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.13.sdk/System/Library/Frameworks/OpenGL.framework/Versions/Current/Headers
CMAKE_LIBRARY_PATH: /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.13.sdk/System/Library/Frameworks/OpenGL.framework/Versions/Current/Libraries
CMAKE_FRAMEWORK_PATH: /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.13.sdk/System/Library/Frameworks
PKG_CONFIG_LIBDIR: /usr/lib/pkgconfig:/Users/Scott/usr2/local/homebrew/Library/Homebrew/os/mac/pkgconfig/10.13
HOMEBREW_SDKROOT: /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.13.sdk
ACLOCAL_PATH: /Users/Scott/usr2/local/share/aclocal
PATH: /Users/Scott/usr2/local/homebrew/Library/Homebrew/shims/super:/usr/bin:/bin:/usr/sbin:/sbin

% brew --config
HOMEBREW_VERSION: 1.5.14
ORIGIN: https://github.com/Homebrew/brew.git
HEAD: 7fd6210127f088b6ee8708a1d7f4ec2df3fc5bb4
Last commit: 4 days ago
Core tap ORIGIN: https://github.com/Homebrew/homebrew-core
Core tap HEAD: 9f8b6cb8008782f188708603f93a3946d9853fc7
Core tap last commit: 7 hours ago
**HOMEBREW_PREFIX**: /Users/Scott/usr2/local
**HOMEBREW_REPOSITORY**: /Users/Scott/usr2/local/homebrew
**HOMEBREW_CELLAR**: /Users/Scott/usr2/local/homebrew/Cellar
**HOMEBREW_CACHE**: /Users/Scott/usr2/local/cache
**HOMEBREW_LIBRARY_PATH**: /Users/Scott/usr2/local/homebrew/Library
CPU: octa-core 64-bit haswell
Homebrew Ruby: 2.3.3 => /System/Library/Frameworks/Ruby.framework/Versions/2.3/usr/bin/ruby
Clang: 9.1 build 902
Git: 2.11.1 => /Users/Scott/usr2/local/bin/git
Curl: 7.54.0 => /usr/bin/curl
Java: N/A
macOS: 10.13.3-x86_64
CLT: N/A
Xcode: 9.3
XQuartz: N/A

The **HOMEBREW_\*** environmental variables bolded above are also documented at https://github.com/Homebrew/brew/blob/master/docs/External-Commands.md#shell-scripts. These variables make it very simple to redefine paths for where brew packages are installed on OSX. Been using this trick very successfully for over 3 years building numerous packages.


## skaht | 2018-04-06T02:36:05+00:00
Got code to compile!! Did only two things since the issue above. Defined the **BOOST_ROOT** environmental variable to be /Users/Scott/usr2/local/homebrew/Cellar/boost/1.66.0 and removed /Users/Scott/usr2/local/include/zmq_addon.hpp that came directly from https://github.com/zeromq/cppzmq source code. 

Still need to test freshly compiled code.  

## skaht | 2018-04-15T22:31:31+00:00
The statically compiled daemon and client compiled 10 days ago appear to work. 

# Action History
- Created by: skaht | 2018-03-30T03:17:22+00:00
- Closed at: 2018-04-15T22:31:31+00:00
