---
title: 'alpine error - libudev.so.1: undefined reference to `gettid'''
source_url: https://github.com/xmrig/xmrig/issues/2440
author: mckaygerhard
assignees: []
labels: []
created_at: '2021-06-13T03:21:26+00:00'
updated_at: '2021-06-13T07:14:38+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
**Describe the bug**

at linking part.. compilation fails with `alpine error - libudev.so.1: undefined reference to `gettid' ` so why is xmirg related to libudev ? shitstemd related?

**To Reproduce**

```
apk add git make cmake libstdc++ gcc g++ libuv-dev openssl-dev
cat > /etc/apk/repositories << EOF
http://dl-4.alpinelinux.org/alpine/v$(cat /etc/alpine-release | cut -d'.' -f1,2)/main
http://dl-4.alpinelinux.org/alpine/v$(cat /etc/alpine-release | cut -d'.' -f1,2)/community
http://dl-4.alpinelinux.org/alpine/edge/main
http://dl-4.alpinelinux.org/alpine/edge/community
http://dl-4.alpinelinux.org/alpine/edge/testing
EOF
apk update
apk add hwloc-dev
cat > /etc/apk/repositories << EOF
http://dl-4.alpinelinux.org/alpine/v$(cat /etc/alpine-release | cut -d'.' -f1,2)/main
http://dl-4.alpinelinux.org/alpine/v$(cat /etc/alpine-release | cut -d'.' -f1,2)/community
EOF
apk update
cd /opt && mkdir xmrig
git clone https://github.com/xmrig/xmrig
mkdir /opt/xmrig/build && cd /opt/xmrig/build
cmake ..
make -j$(nproc)
```

**Expected behavior**

..a Sussess compilation

**Required data**

 - Miner log as text or screenshot : N/A
 - Config file or command line (without wallets) : N/A
 - OS: Linux of course !!! puff
 - For GPU related issues: i do not use "drivers" is linux! all modules are loaded and working!

**Additional context**

IT seems some dependencies are not figured.. why is happened? i cannot handle the order of linking! can some one help with?

i later add `apk add eudev-dev`  and compiles! you should update docs.. all the alpine related comamnds are wrong and incorrect puff (as always.. puff)


# Discussion History
## ghost | 2021-06-13T07:09:28+00:00
Try advanced build from xmrig documentation 
https://xmrig.com/docs/miner/build/alpine

## xmrig | 2021-06-13T07:14:37+00:00
udev dependency comes from hwloc, I think it should be installed automatically with hwloc-dev. Advanced build use hwloc without unnecessary dependencies https://github.com/xmrig/xmrig/blob/master/scripts/build.hwloc.sh#L15
Thank you.

# Action History
- Created by: mckaygerhard | 2021-06-13T03:21:26+00:00
