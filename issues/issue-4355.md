---
title: 'Failed to build static binaries on Ubuntu 14. '
source_url: https://github.com/monero-project/monero/issues/4355
author: ViperRu
assignees: []
labels: []
created_at: '2018-09-09T15:40:01+00:00'
updated_at: '2018-09-18T10:39:36+00:00'
type: issue
status: closed
closed_at: '2018-09-18T10:39:36+00:00'
---

# Original Description
```
> dpkg -l | grep libboost-chrono
ii  libboost-chrono1.58-dev:amd64               1.58.0+dfsg-4.1ubuntu3                               amd64        C++ representation of time duration, time point, and clocks
ii  libboost-chrono1.58.0:amd64                 1.58.0+dfsg-4.1ubuntu3                               amd64        C++ representation of time duration, time point, and clocks
```
make release-static
```
[ 86%] Building CXX object src/wallet/CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o
[ 87%] Linking CXX executable ../../bin/monero-wallet-rpc
/usr/bin/ld: /usr/lib/gcc/x86_64-linux-gnu/5/../../../x86_64-linux-gnu/libboost_chrono.a(chrono.o): relocation R_X86_64_32 against `.rodata.str1.1' can not be used when making a shared object; recompile with -fPIC
/usr/lib/gcc/x86_64-linux-gnu/5/../../../x86_64-linux-gnu/libboost_chrono.a: error adding symbols: Bad value
collect2: error: ld returned 1 exit status
make[3]: *** [bin/monero-wallet-rpc] Error 1
make[3]: Leaving directory `/home/monero/bitmonero/build/release'
make[2]: *** [src/wallet/CMakeFiles/wallet_rpc_server.dir/all] Error 2
make[2]: Leaving directory `/home/monero/bitmonero/build/release'
make[1]: *** [all] Error 2
make[1]: Leaving directory `/home/monero/bitmonero/build/release'
make: *** [release-static] Error 2
```

# Discussion History
## moneromooo-monero | 2018-09-09T16:01:01+00:00
You need to build boost with -fPIC. See boost docs for now to do so.

## ViperRu | 2018-09-09T17:22:37+00:00
The static binary version "Monero 'Helium Hydra' (v0.11.1.0-master-9a47944)" was built with current version package of boost. Have there been any changes (in work with boost) since then?

## moneromooo-monero | 2018-09-09T17:37:09+00:00
I don't know offhand.

## iDunk5400 | 2018-09-09T19:45:23+00:00
Hardened dependencies were not a requirement back then.
There are plenty of answers if you do a search.
https://github.com/monero-project/monero/issues?q=is%3Aissue+-fPIC

## gituser | 2018-09-16T11:55:12+00:00
check this issue - https://github.com/monero-project/monero/issues/3463 , specifically starting from this comment - https://github.com/monero-project/monero/issues/3463#issuecomment-379497956

and yes you need to build all required dependencies with `-fPIC`, the build system has been changed at some point.

## ViperRu | 2018-09-18T10:39:36+00:00
Thank you.

# Action History
- Created by: ViperRu | 2018-09-09T15:40:01+00:00
- Closed at: 2018-09-18T10:39:36+00:00
