---
title: Building XmRig Failed On Ubuntu 16.04
source_url: https://github.com/xmrig/xmrig/issues/641
author: emailyc
assignees: []
labels:
- libuv
created_at: '2018-05-21T04:34:46+00:00'
updated_at: '2018-05-30T09:14:48+00:00'
type: issue
status: closed
closed_at: '2018-05-30T09:14:48+00:00'
---

# Original Description
user@pc04:~/xmrig/build$ cmake ..
-- The C compiler identification is GNU 7.2.0
-- The CXX compiler identification is GNU 7.2.0
-- Check for working C compiler: /home/user/anaconda3/bin/cc
-- Check for working C compiler: /home/user/anaconda3/bin/cc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting C compile features - done
-- Check for working CXX compiler: /home/user/anaconda3/bin/c++
-- Check for working CXX compiler: /home/user/anaconda3/bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
CMake Error at /usr/share/cmake-3.5/Modules/FindPackageHandleStandardArgs.cmake:148 (message):
  Could NOT find UV (missing: UV_LIBRARY)
Call Stack (most recent call first):
  /usr/share/cmake-3.5/Modules/FindPackageHandleStandardArgs.cmake:388 (_FPHSA_FAILURE_MESSAGE)
  cmake/FindUV.cmake:25 (find_package_handle_standard_args)
  CMakeLists.txt:177 (find_package)


-- Configuring incomplete, errors occurred!
See also "/home/user/xmrig/build/CMakeFiles/CMakeOutput.log".


# Discussion History
## ghost | 2018-05-23T10:27:47+00:00
You must install libuv first 
```
Could NOT find UV (missing: UV_LIBRARY)
```
https://packages.ubuntu.com/search?suite=default&section=all&arch=any&keywords=libuv&searchon=names

## emailyc | 2018-05-24T02:31:22+00:00
Sorry for being a noob I'm new to Linux
I see a dozen version and have no idea which one to go for. Is it possible to get it via terminal ?


## ghost | 2018-05-24T15:41:02+00:00
What Ubuntu version are you using ( 18.04 , 16.04 , ... ) ?  I will compile it and give you the instruction ? 

## emailyc | 2018-05-24T15:42:02+00:00
16.04
yes please

## ghost | 2018-05-24T15:54:00+00:00
I just tested in my VPS , all OK
```
#apt-get install git build-essential cmake libuv1-dev libmicrohttpd-dev
```
Next time you should read the wiki first : https://github.com/xmrig/xmrig/wiki/Ubuntu-Build

# Action History
- Created by: emailyc | 2018-05-21T04:34:46+00:00
- Closed at: 2018-05-30T09:14:48+00:00
