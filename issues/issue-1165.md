---
title: macOS static build ?!
source_url: https://github.com/xmrig/xmrig/issues/1165
author: furiousteam
assignees: []
labels: []
created_at: '2019-09-09T00:12:16+00:00'
updated_at: '2024-02-24T05:05:35+00:00'
type: issue
status: closed
closed_at: '2019-12-22T19:23:46+00:00'
---

# Original Description
I'm trying to make a static build for macOS using the following command:

cmake .. -DOPENSSL_ROOT_DIR=/usr/local/Cellar/openssl/1.0.2s -DBUILD_STATIC=ON -DUV_INCLUDE_DIR=/usr/local/Cellar/libuv/1.31.0/lib/

also tried this:

cmake .. DOPENSSL_ROOT_DIR=/usr/local/Cellar/openssl/1.0.2s -DOPENSSL_LIBRARIES=/usr/local/Cellar/openssl/1.0.2s/lib -DBUILD_STATIC=ON -DUV_INCLUDE_DIR=/usr/local/Cellar/libuv/1.31.0 -DUV_LIBRARY=/usr/local/Cellar/libuv/1.31.0/lib/libuv.a

But i get the following error after 100% at compile:

ld: library not found for -lcrt0.o
clang: error: linker command failed with exit code 1 (use -v to see invocation)
make[2]: *** [xmrig] Error 1
make[1]: *** [CMakeFiles/xmrig.dir/all] Error 2
make: *** [all] Error 2

CMakeError.log:
[CMakeError.log](https://github.com/xmrig/xmrig/files/3588225/CMakeError.log)

Thank you.

# Discussion History
## djfinch | 2019-11-21T09:43:23+00:00
OSX version? Xcode version?
It's linker issue. I was not able to build miner with Xcode's Clang but used Homebrew's one and build passing. Currently on Elcap with X8 & llvm7, unable to install llvm9. Also, do not use absolute paths for libs --> use symlinks created by Homebrew instead...

`cmake .. -DUV_LIBRARY=/usr/local/lib/libuv.a -DOPENSSL_SSL_LIBRARY=/usr/local/opt/openssl/lib/libssl.a -DOPENSSL_CRYPTO_LIBRARY=/usr/local/opt/openssl/lib/libcrypto.a -DCMAKE_C_COMPILER=/usr/local/Cellar/llvm/7.0.0/bin/clang -DCMAKE_CXX_COMPILER=/usr/local/Cellar/llvm/7.0.0/bin/clang++`

## xmrig | 2019-11-21T09:57:48+00:00
Also please check new build docs https://xmrig.com/docs/miner/macos-build custom static build required only for hwloc.
Thank you.

## ZeppLu | 2024-02-24T05:05:33+00:00
I tried to link statically to brew's `libhwloc.a`, and finally come up with this configuration:

```
LDFLAGS="-framework OpenCL $(xml2-config --libs)" cmake .. -DOPENSSL_ROOT_DIR=$(brew --prefix openssl) -DHWLOC_INCLUDE_DIR=$(brew --prefix hwloc)/include -DHWLOC_LIBRARY=$(brew --prefix hwloc)/lib/libhwloc.a
```

# Action History
- Created by: furiousteam | 2019-09-09T00:12:16+00:00
- Closed at: 2019-12-22T19:23:46+00:00
