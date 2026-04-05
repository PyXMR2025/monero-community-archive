---
title: Build issue related to OpenSsl.
source_url: https://github.com/xmrig/xmrig/issues/1350
author: mingbuaa
assignees: []
labels:
- question
created_at: '2019-12-01T06:53:46+00:00'
updated_at: '2019-12-22T19:41:54+00:00'
type: issue
status: closed
closed_at: '2019-12-22T19:41:54+00:00'
---

# Original Description
So I tried to build the project using vs 2017 and got the following error.

-- Could NOT find OpenSSL, try to set the path to OpenSSL root folder in the system variable OPENSSL_ROOT_DIR (missing: OPENSSL_CRYPTO_LIBRARY) (found version "1.1.1c")

The command I was using was 
cmake .. -G "Visual Studio 15 2017 Win64" 
-DXMRIG_DEPS=C:\Users\Ming\Documents\GitHub\xmrig-master\xmrig-deps\msvc2017\x64 -DUV_INCLUDE_DIR=C:\Users\Ming\Documents\GitHub\xmrig-master\xmrig-deps-3.5\msvc2017\x64\include 
-DUV_LIBRARY=C:\Users\Ming\Documents\GitHub\xmrig-master\xmrig-deps-3.5\msvc2017\x64\lib -DOPENSSL_CRYPTO_LIBRARY=C:\Users\Ming\Documents\GitHub\xmrig-master\xmrig-deps-3.5\msvc2017\x64\lib 
-DOPENSSL_INCLUDE_DIR=C:\Users\Ming\Documents\GitHub\xmrig-master\xmrig-deps-3.5\msvc2017\x64\include

Can anyone give me a pointer?

# Discussion History
## xmrig | 2019-12-02T01:12:05+00:00
Remove all files which cmake created and use only `-DXMRIG_DEPS=C:\Users\Ming\Documents\GitHub\xmrig-master\xmrig-deps\msvc2017\x64`

## mingbuaa | 2019-12-02T01:23:35+00:00
Thank you. That is what I did in the first place. I got the following error:

CMake Error at C:/Program Files/CMake/share/cmake-3.9/Modules/FindPackageHandleStandardArgs.cmake:137 (message):
  Could NOT find UV (missing: UV_LIBRARY UV_INCLUDE_DIR)
Call Stack (most recent call first):
  C:/Program Files/CMake/share/cmake-3.9/Modules/FindPackageHandleStandardArgs.cmake:377 (_FPHSA_FAILURE_MESSAGE)
  cmake/FindUV.cmake:25 (find_package_handle_standard_args)
  CMakeLists.txt:174 (find_package)

Then I set the uv include and lib and got the following:
-- Could NOT find OpenSSL, try to set the path to OpenSSL root folder in the system variable OPENSSL_ROOT_DIR (missing: OPENSSL_CRYPTO_LIBRARY OPENSSL_INCLUDE_DIR)
CMake Error at cmake/OpenSSL.cmake:23 (message):
  OpenSSL NOT found: use `-DWITH_TLS=OFF` to build without TLS support
Call Stack (most recent call first):
  CMakeLists.txt:179 (include)

I set  them in options as following:
C:\Users\Ming\Documents\GitHub\xmrig-master\build>cmake .. -G "Visual Studio 15 2017 Win64" -DXMRIG_DEPS=C:\Users\Ming\Documents\GitHub\xmrig-master\xmrig-deps\msvc2017\x64 -DUV_INCLUDE_DIR=C:\Users\Ming\Documents\GitHub\xmrig-master\xmrig-deps-3.5\msvc2017\x64\include -DUV_LIBRARY=C:\Users\Ming\Documents\GitHub\xmrig-master\xmrig-deps-3.5\msvc2017\x64\lib -DOPENSSL_CRYPTO_LIBRARY=C:\Users\Ming\Documents\GitHub\xmrig-master\xmrig-deps-3.5\msvc2017\x64\lib -DOPENSSL_INCLUDE_DIR=C:\Users\Ming\Documents\GitHub\xmrig-master\xmrig-deps-3.5\msvc2017\x64\include

Got the error:
-- Could NOT find OpenSSL, try to set the path to OpenSSL root folder in the system variable OPENSSL_ROOT_DIR (missing: OPENSSL_CRYPTO_LIBRARY) (found version "1.1.1c")

What is weird is that it said found version 1.1.1c but no library. I change to path to include openssl folder, still no go.

Anyway, thanks for taking time to look into it. I did it trying to solve the issue with my 4GB gpus. I want to use my old rig to mine xmr. They are in my garage and I need to keep it warm anyway but I simply can’t make it work.

rx allocated 2336 MB (2080+256) huge pages 11% 128/1168 +JIT (5 ms)

This is when the program started and I got only 400h/s.
Thanks,
Ming



From: xmrig [mailto:notifications@github.com]
Sent: Sunday, December 01, 2019 5:12 PM
To: xmrig/xmrig
Cc: mingbuaa; State change
Subject: Re: [xmrig/xmrig] Build issue related to OpenSsl. (#1350)


Remove all files which cmake created and use only -DXMRIG_DEPS=C:\Users\Ming\Documents\GitHub\xmrig-master\xmrig-deps\msvc2017\x64

—
You are receiving this because you modified the open/close state.
Reply to this email directly, view it on GitHub<https://github.com/xmrig/xmrig/issues/1350?email_source=notifications&email_token=AAYVJMOV7KJJVFVTZWGTYSTQWROGNA5CNFSM4JTKHAK2YY3PNVWWK3TUL52HS4DFVREXG43VMVBW63LNMVXHJKTDN5WW2ZLOORPWSZGOEFR4G6Q#issuecomment-560186234>, or unsubscribe<https://github.com/notifications/unsubscribe-auth/AAYVJMIYG2OTSNHBW7RIB7LQWROGNANCNFSM4JTKHAKQ>.


# Action History
- Created by: mingbuaa | 2019-12-01T06:53:46+00:00
- Closed at: 2019-12-22T19:41:54+00:00
