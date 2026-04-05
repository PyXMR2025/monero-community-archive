---
title: Unable to build
source_url: https://github.com/xmrig/xmrig/issues/3636
author: i0nel
assignees: []
labels:
- arm
created_at: '2025-02-13T12:06:38+00:00'
updated_at: '2025-06-16T15:16:12+00:00'
type: issue
status: closed
closed_at: '2025-06-16T15:16:12+00:00'
---

# Original Description
I am unable to build source code. Getting the following error messages:







```
/usr/bin/ld: ./libcrypto.a(libcrypto-lib-threads_pthread.o): in function `CRYPTO_atomic_or':
threads_pthread.c:(.text+0x178): undefined reference to `__atomic_is_lock_free'
/usr/bin/ld: threads_pthread.c:(.text+0x1fc): undefined reference to `__atomic_fetch_or_8'
/usr/bin/ld: ./libcrypto.a(libcrypto-lib-threads_pthread.o): in function `CRYPTO_atomic_load':
threads_pthread.c:(.text+0x238): undefined reference to `__atomic_is_lock_free'
/usr/bin/ld: threads_pthread.c:(.text+0x288): undefined reference to `__atomic_load_8'
collect2: error: ld returned 1 exit status
make[1]: *** [Makefile:12983: fuzz/asn1-test] Error 1
make[1]: *** Waiting for unfinished jobs....
make[1]: Leaving directory '/home/user/xmrig/scripts/build/openssl-3.0.15'
make: *** [Makefile:2532: build_sw] Error 2
```








Any insight is appreciated. Thanks




OS:
PRETTY_NAME="Raspbian GNU/Linux 12 (bookworm)"


# Discussion History
## SChernykh | 2025-02-13T12:57:16+00:00
What is your GCC version? And how exactly do you build XMRig (all commands)?

## i0nel | 2025-02-13T15:59:43+00:00
gcc verison:
gcc (Raspbian 12.2.0-14+rpi1) 12.2.0


I followed the instructions here:
https://xmrig.com/docs/miner/build/ubuntu

OR

1. sudo apt install git build-essential cmake automake libtool autoconf
2. git clone https://github.com/xmrig/xmrig.git
3. mkdir xmrig/build && cd xmrig/scripts
4. ./build_deps.sh && cd ../build
5. **Unable to continue because of 2 errors**
6. cmake .. -DXMRIG_DEPS=scripts/deps
7. make -j$(nproc)

## SChernykh | 2025-02-16T09:03:33+00:00
Quick google search says that you need to add `atomic` to the list of libraries to link. You can add `atomic` to the list here: https://github.com/xmrig/xmrig/blob/master/CMakeLists.txt#L189
or better here to be sure: https://github.com/xmrig/xmrig/blob/master/CMakeLists.txt#L240

# Action History
- Created by: i0nel | 2025-02-13T12:06:38+00:00
- Closed at: 2025-06-16T15:16:12+00:00
