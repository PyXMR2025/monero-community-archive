---
title: Add build instructions for Alpine Linux
source_url: https://github.com/xmrig/xmrig/issues/1810
author: wzykubek
assignees: []
labels: []
created_at: '2020-08-13T14:36:10+00:00'
updated_at: '2020-08-28T16:22:21+00:00'
type: issue
status: closed
closed_at: '2020-08-28T16:22:21+00:00'
---

# Original Description
# Alpine Linux
Disclaimer: You need to enable testing repository to download some dependencies.
+ Install build dependencies.
```
# apk add git cmake libuv-dev libstdc++ openssl-dev gcc g++ hwloc-dev make
```
+ Clone repo.
```
$ git clone https://github.com/xmrig/xmrig 
$ mkdir xmrig/build && cd xmrig/build
```
## Dynamic linked
+ Build XMRig.
```
$ cmake ..
$ make -j$(nproc)
```
## Static linked
+ Install additional build dependencies.
```
# apk add bzip2 automake libtool autoconf linux-headers
```
+ Build dependencies.
```
$ cd ../scripts && ./build_deps.sh
```
+ Build XMRig.
```
$ cd ../build && cmake .. -DXMRIG_DEPS=scripts/deps
$ make -j$(nproc)
```


# Discussion History
## xmrig | 2020-08-19T08:27:59+00:00
Would be nice if you add commands to enable testing repository too or maybe a better way is use `scripts/build.hwloc.sh` I'm not sure.

For static build there is also a useful cmake option `-DBUILD_STATIC=ON` to create a fully static executable, thanks to musl it should work without side effects.
Thank you.

## xmrig | 2020-08-28T16:22:21+00:00
https://xmrig.com/docs/miner/build/alpine

# Action History
- Created by: wzykubek | 2020-08-13T14:36:10+00:00
- Closed at: 2020-08-28T16:22:21+00:00
