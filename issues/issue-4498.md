---
title: Compiling GUI deps fails
source_url: https://github.com/monero-project/monero/issues/4498
author: glv2
assignees: []
labels: []
created_at: '2018-10-04T13:18:57+00:00'
updated_at: '2018-10-06T18:24:50+00:00'
type: issue
status: closed
closed_at: '2018-10-06T18:24:50+00:00'
---

# Original Description
Trying to compile v0.13.0.2-RC2 (commit 735a33e8d88f230533203cdfd314847f47a30743) with ```BUILD_GUI_DEPS=ON``` fails:

```
make clean
mkdir -p build/Linux/release
cd build/Linux/release
cmake -D BUILD_GUI_DEPS=ON -D BUILD_TESTS=ON -D CMAKE_BUILD_TYPE=release ../../..
make

...all goes well until...

Scanning dependencies of target obj_wallet_api
[ 46%] Building CXX object src/wallet/api/CMakeFiles/obj_wallet_api.dir/wallet.cpp.o
/.../monero/src/wallet/api/wallet.cpp: Dans le constructeur « Monero::WalletImpl::WalletImpl(Monero::NetworkType, uint64_t) »:
/.../monero/src/wallet/api/wallet.cpp:380:21: error: « make_unique » n'est pas un membre de « std »
     m_wallet = std::make_unique<tools::wallet2>(static_cast<cryptonote::network_type>(nettype), kdf_rounds, true);

...some other errors of the same kind...
```

Apparently compiling fails because of the use of ```make_unique```.
According to https://en.cppreference.com/w/cpp/memory/unique_ptr/make_unique, ```make_unique``` is available only since C++14, and as Monero is currently compiled using C++11, I suppose ```make_unique``` can't be used.

# Discussion History
## moneromooo-monero | 2018-10-04T13:42:58+00:00
Does https://github.com/monero-project/monero/pull/4499 help ?

## iDunk5400 | 2018-10-04T14:08:04+00:00
`libwallet_merged.a` built properly with #4499 on Ubuntu 16.04.

## glv2 | 2018-10-04T14:14:40+00:00
Yes, with #4499 everything compiles fine.


## moneromooo-monero | 2018-10-06T18:21:37+00:00
+resolved

# Action History
- Created by: glv2 | 2018-10-04T13:18:57+00:00
- Closed at: 2018-10-06T18:24:50+00:00
