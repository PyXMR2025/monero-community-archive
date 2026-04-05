---
title: Compiling fails on raspbian Raspberry Pi 4
source_url: https://github.com/xmrig/xmrig/issues/1102
author: jfikar
assignees: []
labels:
- arm
created_at: '2019-08-06T10:51:46+00:00'
updated_at: '2021-04-12T15:55:18+00:00'
type: issue
status: closed
closed_at: '2021-04-12T15:55:18+00:00'
---

# Original Description
I've tried to compile v2.99.4-beta on recent raspbian on Raspberry Pi 4. It fails during linking:

`Linking CXX executable xmrig
/usr/bin/ld: CMakeFiles/xmrig.dir/src/crypto/common/Nonce.cpp.o: in function xmrig::Nonce::Nonce():
Nonce.cpp:(.text+0x38): undefined reference to __atomic_store_8
/usr/bin/ld: Nonce.cpp:(.text+0x4c): undefined reference to __atomic_store_8
/usr/bin/ld: Nonce.cpp:(.text+0x60): undefined reference to __atomic_store_8
/usr/bin/ld: CMakeFiles/xmrig.dir/src/crypto/common/Nonce.cpp.o: in function xmrig::Nonce::reset(unsigned char):
Nonce.cpp:(.text+0x120): undefined reference to _atomic_fetch_add_8
/usr/bin/ld: Nonce.cpp:(.text+0x134): undefined reference to __atomic_fetch_add_8
/usr/bin/ld: Nonce.cpp:(.text+0x148): undefined reference to __atomic_fetch_add_8
/usr/bin/ld: CMakeFiles/xmrig.dir/src/crypto/common/Nonce.cpp.o: in function xmrig::Nonce::stop():
Nonce.cpp:(.text+0x194): undefined reference to __atomic_store_8
`

I figured out you need to specify the atomic library ` -latomic`. The easiest way is to add it to `EXTRA_LIBS` in `CMakeLists.txt`. I've added it here:

`       set(EXTRA_LIBS pthread rt dl atomic)`

But you may want it also for [FreeBSD](https://github.com/xmrig/xmrig/issues/1020). It could solve this [Alpine issue](https://github.com/xmrig/xmrig/issues/900) too.

# Discussion History
# Action History
- Created by: jfikar | 2019-08-06T10:51:46+00:00
- Closed at: 2021-04-12T15:55:18+00:00
