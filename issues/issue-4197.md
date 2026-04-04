---
title: Crash in cn_slow_hash()
source_url: https://github.com/monero-project/monero/issues/4197
author: Pei116
assignees: []
labels:
- invalid
created_at: '2018-07-30T19:16:14+00:00'
updated_at: '2018-08-18T12:43:20+00:00'
type: issue
status: closed
closed_at: '2018-08-15T11:17:00+00:00'
---

# Original Description
Trying to use monero wallet api in Android using JNI after pre-building the libraries.
It's always crashed with following error:
 `
*** *** *** *** *** *** *** *** *** *** *** *** *** *** *** ***
    Build fingerprint: 'samsung/hero2ltektt/hero2ltektt:8.0.0/R16NW/G935KKKU1EREA:user/release-keys'
    Revision: '8'
    ABI: 'arm64'
    pid: 28690, tid: 28709, name: roidJUnitRunner  >>> ... <<<
    signal 11 (SIGSEGV), code 2 (SEGV_ACCERR), fault addr 0x7f6aabb230
        x0   0000000000000000  x1   0000000000000000  x2   0000007f6acbb6e8  x3   0000000000000000
        x4   0000000000000000  x5   0000007f73cf5485  x6   6a616d5f64616568  x7   222c30353a22726f
        x8   0000007f6aabb230  x9   0000007f6aabb2f0  x10  0000000000000000  x11  14c79abb30e83214
        x12  627573222c303a22  x13  5f73736572646461  x14  0000000000000020  x15  0000007f73c092f0
        x16  0000007f6a3fec68  x17  0000007f69c8bc24  x18  0000007f73cf4e20  x19  0000007f73c59200
        x20  0000007f84b08100  x21  0000007f73c59200  x22  0000007f6acbdbcc  x23  0000007f6b04d97e
        x24  0000000000000014  x25  0000007f73c59298  x26  0000000000000000  x27  0000000000000003
        x28  0000000000000005  x29  0000007f6acbb690  x30  0000007f69513e1c
        sp   0000007f6aabb1f0  pc   0000007f69c8bc4c  pstate 0000000060000000
    backtrace:
        #00 pc 000000000142dc4c  /data/app/...-_E9DVGmcYSuB5P5kBSedRg==/lib/arm64/libmoneroj.so (cn_slow_hash+40)
        #01 pc 0000000000cb5e18  /data/app/...-_E9DVGmcYSuB5P5kBSedRg==/lib/arm64/libmoneroj.so (_ZN6crypto19generate_chacha_keyEPKvmRN5tools8scrubbedINSt6__ndk15arrayIhLm32EEEEE+68)
        #02 pc 0000000000cb5e18  /data/app/...-_E9DVGmcYSuB5P5kBSedRg==/lib/arm64/libmoneroj.so (_ZN6crypto19generate_chacha_keyEPKvmRN5tools8scrubbedINSt6__ndk15arrayIhLm32EEEEE+68)
        #03 pc 0000000000bae31c  /data/app/...-_E9DVGmcYSuB5P5kBSedRg==/lib/arm64/libmoneroj.so (_ZN5tools7wallet210store_keysERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEERKN4epee15wipeable_stringEb+5864)
        #04 pc 0000000000bb8ec8  /data/app/...-_E9DVGmcYSuB5P5kBSedRg==/lib/arm64/libmoneroj.so (_ZN5tools7wallet28generateERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEERKN4epee15wipeable_stringERKNS_8scrubbedIN6crypto9ec_scalarEEEbbb+2044)
        #05 pc 00000000009b43e4  /data/app/...-_E9DVGmcYSuB5P5kBSedRg==/lib/arm64/libmoneroj.so (_ZN6Monero10WalletImpl6createERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_S9_+1228)
        #06 pc 0000000000a63354  /data/app/...-_E9DVGmcYSuB5P5kBSedRg==/lib/arm64/libmoneroj.so (_ZN6Monero17WalletManagerImpl12createWalletERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_S9_NS_11NetworkTypeE+100)
        #07 pc 00000000009a6f08  /data/app/...-_E9DVGmcYSuB5P5kBSedRg==/lib/arm64/libmoneroj.so (Java_network_pyxis_moneroj_WalletManager_createWalletJ+480)
        #08 pc 0000000000013668  /data/app/...-_E9DVGmcYSuB5P5kBSedRg==/oat/arm64/base.odex (offset 0xf000)
`

# Discussion History
## hyc | 2018-07-30T19:44:18+00:00
cn_slow_hash() requires a fairly large stack. Make sure your calling thread has at least 5MB stack.

## Pei116 | 2018-07-30T19:45:41+00:00
Thanks for your quick answer. But how do i ensure that?

## moneromooo-monero | 2018-07-30T20:44:21+00:00
For example, to set the GNU linker to setup a large stack:

set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} -Wl,--stack,10485760")

Otherwise, use your threading library to set stack size, eg pthread_attr_setstacksize.

## Pei116 | 2018-07-31T02:34:58+00:00
I tried to add this line in CMakesList.txt of the monero repo but there's no luck yet.
`set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} -Wl,--stack,10485760")`

## naughtyfox | 2018-08-06T12:08:48+00:00
I encountered this issue either. The problem is not every `arm8` cpu supports `aes` instruction set. By default monero compiles with flag `-march=${ARCH}+crypto`. Try to compile it with just `-march=${ARCH}` (it will be slower, but it probably will work on your cpu), it helped me.

If you want to check if your cpu supports `aes` instruction set run the following command on your device:
```sh
$ cat /proc/cpuinfo | grep aes
```
and if you get nothing - probably current cpu has no `aes` instruction set.

## moneromooo-monero | 2018-08-15T11:11:38+00:00
Not a monero bug.

+invalid


## Pei116 | 2018-08-15T17:47:12+00:00
@naughtyfox You saved my life! It's now working fine after I removed `crypto` flag from the build command.
Btw I was wondering if it affects any functionality of monero library.

## naughtyfox | 2018-08-16T11:34:23+00:00
It doesn't. AES instructions are used to speed up slow hash

## Pei116 | 2018-08-17T17:35:26+00:00
It's started crashing in x86 also with the same exception. It's been breaking my heart.

## MoroccanMalinois | 2018-08-17T18:07:42+00:00
@Pei116 

If you can't set the stack size like suggested by hyc and mooo, you can try 
https://github.com/monero-project/monero/blob/master/src/crypto/CMakeLists.txt#L99

## Pei116 | 2018-08-17T23:42:31+00:00
@MoroccanMalinois Where do I need to put it in? I tried to add it to the end of the [monero CMakeLists](https://github.com/monero-project/monero/blob/master/CMakeLists.txt) but there's the same crash.

## MoroccanMalinois | 2018-08-18T12:43:20+00:00
OK @Pei116, here goes the full explanation :)

Look at https://github.com/monero-project/monero/blob/master/src/crypto/slow-hash.c#L1127

By default, the program use the stack :

> uint8_t long_state[MEMORY]; 

`MEMORY` is a define holding the size of the scratchpad, i.e. 2MB. On android, the default stack size is 1MB (when it's not the main thread), hence the crash.

So the first natural thing to do is to increase the stack size (like suggested by hyc and mooo). Except sometimes you simply cannot control that parameter, like monero-wallet-gui (It's done in Qt internals and clang does not support `-Wl,--stack`).

So if we can't use the `stack`, we have to use the `heap`.
That's what the define `FORCE_USE_HEAP` does. By activating it, the program will use `malloc` for allocating the memory of the variable `long_state`.

Now to answer your question, you have multiple ways to activate this flag: you can either:

- add the define flag to the cmake command, e.g. `cmake -DFORCE_USE_HEAP=1 ....`
- make sure that `ANDROID` and `BUILD_GUI_DEPS` are defined
- modify `src/crypto/CMakeLists.txt` to include `add_definitions(-DFORCE_USE_HEAP=1)` on the conditions that suits you
- modify `src/crypto/slow-hash.c` to always use `malloc` (most uggly solution, but might be usefull to make sure that this is indeed the problem, before start debugging cmake :sweat_smile:  )

# Action History
- Created by: Pei116 | 2018-07-30T19:16:14+00:00
- Closed at: 2018-08-15T11:17:00+00:00
