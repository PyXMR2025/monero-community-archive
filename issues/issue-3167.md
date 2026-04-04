---
title: Help on compiling for Win64
source_url: https://github.com/monero-project/monero/issues/3167
author: onemoreitguy
assignees: []
labels:
- invalid
created_at: '2018-01-21T13:44:08+00:00'
updated_at: '2018-11-03T11:48:01+00:00'
type: issue
status: closed
closed_at: '2018-01-22T10:24:30+00:00'
---

# Original Description
Hello guys,
I've followed the instructions to build on a Windows 7 (and also 10) but I get compile errors over and over.
first: I got the openssl
  Could NOT find OpenSSL, try to set the path to OpenSSL root folder in the  system variable OPENSSL_ROOT_DIR (missing: OPENSSL_CRYPTO_LIBRARY  OPENSSL_INCLUDE_DIR)
I manage to overcome by installing OpenSSL and setting manually the variable location paths on CMakeCache.txt
But the errors of libraries not found keep going over and over as more as I 

I assume that I'm doing something wrong from the beginning. Any can provide some clues?

# Discussion History
## moneromooo-monero | 2018-01-21T13:54:43+00:00
Install the others too ?

## onemoreitguy | 2018-01-21T14:18:59+00:00
1. Initial dependency compile dependency failures (OPENSSL) 
>> Install MSYS2 with the defaults (root of the C: drive) will not generate initial dependency failures
2. failure: C:/msys64/mingw64/share/cmake-3.10/Modules/FindBoost.cmake:907 (_Boost_COMPONENT_DEPENDENCIES)
>> it will continue compile if install GIT (?!): pacman -S git 
3. Compilation failure: [ 51%] Building CXX object contrib/epee/src/CMakeFiles/epee_readline.dir/readline_buffer.cpp.obj
C:/msys64/home/test/monero-master/contrib/epee/src/readline_buffer.cpp:4:10: fatal error: sys/select.h: No such file or directory
>> (stuck now)

## moneromooo-monero | 2018-01-21T15:49:42+00:00
Fixed in https://github.com/monero-project/monero/pull/3155

## onemoreitguy | 2018-01-21T15:55:40+00:00
I was about to write that.
I guess I didn't dig enough on the info.

Thanks and continue the good work ;)


## moneromooo-monero | 2018-01-22T10:18:16+00:00
+invalid

## vans163 | 2018-11-03T11:47:45+00:00
This issue is present if you compile from /d/ or if msys is on /d/ drive or a combo of both. Basically only works if both are on your /c/.

# Action History
- Created by: onemoreitguy | 2018-01-21T13:44:08+00:00
- Closed at: 2018-01-22T10:24:30+00:00
