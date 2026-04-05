---
title: Xmrig 2.9.3 won't compile Mac osx
source_url: https://github.com/xmrig/xmrig/issues/914
author: gorgovski
assignees: []
labels: []
created_at: '2019-01-18T15:30:55+00:00'
updated_at: '2019-08-02T13:05:20+00:00'
type: issue
status: closed
closed_at: '2019-08-02T13:05:20+00:00'
---

# Original Description
When I try to compile xmrig, always the same error would come. Couldn't find openssl drivers... any help?

iMac-van-Maxim:build maximgaorgievski$ make
[ 10%] Built target cpuid
[ 13%] Built target xmrig-asm
[ 15%] Building CXX object CMakeFiles/xmrig.dir/src/common/config/CommonConfig.cpp.o
/Users/maximgaorgievski/Desktop/xmrig-2.9.3/src/common/config/CommonConfig.cpp:38:13: fatal error: 
      'openssl/opensslv.h' file not found
#   include <openssl/opensslv.h>
            ^~~~~~~~~~~~~~~~~~~~
1 error generated.
make[2]: *** [CMakeFiles/xmrig.dir/src/common/config/CommonConfig.cpp.o] Error 1
make[1]: *** [CMakeFiles/xmrig.dir/all] Error 2
make: *** [all] Error 2


# Discussion History
## xmrig | 2019-01-18T15:42:15+00:00
https://github.com/xmrig/xmrig/wiki/OS-X-Build

You have 2 options:
1. Install openssl via homebrew and specify path to openssl when run cmake: `cmake .. -DOPENSSL_ROOT_DIR=/usr/local/opt/openssl`.
2. Build miner without TLS support: `cmake .. -DWITH_TLS=OFF`

## gorgovski | 2019-01-18T15:54:51+00:00
> https://github.com/xmrig/xmrig/wiki/OS-X-Build
> 
> You have 2 options:
> 
> 1. Install openssl via homebrew and specify path to openssl when run cmake: `cmake .. -DOPENSSL_ROOT_DIR=/usr/local/opt/openssl`.
> 2. Build miner without TLS support: `cmake .. -DWITH_TLS=OFF`

thank you, I will try to install openssl trough homebrew. 

## DeadManWalkingTO | 2019-03-17T15:56:38+00:00
I think this issue can be closed.
Thank you!

# Action History
- Created by: gorgovski | 2019-01-18T15:30:55+00:00
- Closed at: 2019-08-02T13:05:20+00:00
