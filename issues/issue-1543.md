---
title: Mac OS X build
source_url: https://github.com/xmrig/xmrig/issues/1543
author: Neuroelectric86
assignees: []
labels: []
created_at: '2020-02-09T17:06:36+00:00'
updated_at: '2020-08-29T04:05:22+00:00'
type: issue
status: closed
closed_at: '2020-08-29T04:05:22+00:00'
---

# Original Description
I'm running Mac OS X El Capitan on a 2009 Macbook, I was gonna partion my HD to run Windows but I think I can get Xmrig to work. My issues seem to be average with Windows users, my first issue is; CMake Error at /usr/local/Cellar/cmake/3.16.3/share/cmake/Modules/FindPackageHandleStandardArgs.cmake:146 (message):
  Could NOT find UV (missing: UV_INCLUDE_DIR)
Call Stack (most recent call first):
  /usr/local/Cellar/cmake/3.16.3/share/cmake/Modules/FindPackageHandleStandardArgs.cmake:393 (_FPHSA_FAILURE_MESSAGE)
  cmake/FindUV.cmake:25 (find_package_handle_standard_args)
  CMakeLists.txt:175 (find_package)....


**To Reproduce**
After downloading the master and all deps from Homebrew:
mkdir xmrig
cd xmrig
mkdir build
cd build
cmake .. -DOPENSSL_ROOT_DIR=/usr/local/opt/openssl

I expected the executable would be created so I can create the conf.json to make configurations. 

mkdir xmrig
cd xmrig
mkdir build
cd build
cmake .. -DOPENSSL_ROOT_DIR=/usr/local/opt/openssl
Ryans-MacBook:build Neuroelectric$ cmake .. -DOPENSSL_ROOT_DIR=/usr/local/opt/openssl
-- The C compiler identification is AppleClang 8.0.0.8000042
-- The CXX compiler identification is AppleClang 8.0.0.8000042
-- Check for working C compiler: /Library/Developer/CommandLineTools/usr/bin/cc
-- Check for working C compiler: /Library/Developer/CommandLineTools/usr/bin/cc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting C compile features - done
-- Check for working CXX compiler: /Library/Developer/CommandLineTools/usr/bin/c++
-- Check for working CXX compiler: /Library/Developer/CommandLineTools/usr/bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Looking for syslog.h
-- Looking for syslog.h - found
-- Found HWLOC: /usr/local/lib/libhwloc.dylib  
CMake Error at /usr/local/Cellar/cmake/3.16.3/share/cmake/Modules/FindPackageHandleStandardArgs.cmake:146 (message):
  Could NOT find UV (missing: UV_INCLUDE_DIR)
Call Stack (most recent call first):
  /usr/local/Cellar/cmake/3.16.3/share/cmake/Modules/FindPackageHandleStandardArgs.cmake:393 (_FPHSA_FAILURE_MESSAGE)
  cmake/FindUV.cmake:25 (find_package_handle_standard_args)
  CMakeLists.txt:175 (find_package)


-- Configuring incomplete, errors occurred!
See also "/Users/Neuroelectric/xmrig/xmrig/build/CMakeFiles/CMakeOutput.log".
Ryans-MacBook:build Neuroelectric$ make
make: *** No targets specified and no makefile found.  Stop.
Ryans-MacBook:build Neuroelectric$ 

 OS X 10.11.6
 Nvidia Geforce 9400M 256 MB



# Discussion History
## xmrig | 2020-02-12T16:27:49+00:00
https://xmrig.com/docs/miner/macos-build
Very likely you missed `brew install libuv`, anyway this error means development files for libuv not found.
Thank you.

## Neuroelectric86 | 2020-02-17T17:49:03+00:00
I got it to work, thanks.

# Action History
- Created by: Neuroelectric86 | 2020-02-09T17:06:36+00:00
- Closed at: 2020-08-29T04:05:22+00:00
