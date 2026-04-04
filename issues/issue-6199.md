---
title: aarch64 SIGILL from aes_expand_key()
source_url: https://github.com/monero-project/monero/issues/6199
author: bjacquin
assignees: []
labels:
- invalid
created_at: '2019-11-30T14:55:19+00:00'
updated_at: '2019-12-04T18:57:33+00:00'
type: issue
status: closed
closed_at: '2019-12-04T18:57:33+00:00'
---

# Original Description
Hi,

When building monero on aarch64 (for Raspberry Pi 3b+) with boost 1.71, gcc 9.2.0 and glibc 2.29 and {C,CXX}FLAGS="-O2 -pipe -fomit-frame-pointer -mlittle-endian -mabi=lp64 -march=armv8-a+crypto", aes_expand_key() is leading to SIGILL:

```
Thread 5 "monerod" received signal SIGILL, Illegal instruction.
[Switching to Thread 0x77312ddee0 (LWP 1100)]
0x0000005555bb41e4 in aes_expand_key (
    key=key@entry=0x77310dcf80 "\206\206'H\313\266\064>\206\224\257\226\273\336\063^\302R\016K\225\213\021N\216\f\"\210\325k\311\272\317,\356\215\256q\361\243\035\027\220\065-\363\002\232\276y\232A\377\002R\205!\211c\035\321\352b\211\324\354\367UL\276\377\200\307\357\246\005\r\323\v\033\277S\304=#p\303\f\233\001h\353\227\275\361%.'L(\350g\343\324\033\060\"\312\016\365X\212h.\304\317\257\267\261\321Xa\021\337\062\237>\217\031i\213\244\006\367\244P\376\065\370Y\354\256\226\311^\305;\003\236\220\322\005\373\273\361e=,\377\025\360\345\"\237\025X\354\343L-\207\tC\276\376N\310G\304)\255\301\324\227\002\002\006", expandedKey=expandedKey@entry=0x77310dd310 "")
    at /usr/src/debug/net-p2p/monero-0.15.0.1/monero-0.15.0.1/src/crypto/slow-hash.c:1106
1106    __asm__(
(gdb) bt
#0  0x0000005555bb41e4 in aes_expand_key (
    key=key@entry=0x77310dcf80 "\206\206'H\313\266\064>\206\224\257\226\273\336\063^\302R\016K\225\213\021N\216\f\"\210\325k\311\272\317,\356\215\256q\361\243\035\027\220\065-\363\002\232\276y\232A\377\002R\205!\211c\035\321\352b\211\324\354\367UL\276\377\200\307\357\246\005\r\323\v\033\277S\304=#p\303\f\233\001h\353\227\275\361%.'L(\350g\343\324\033\060\"\312\016\365X\212h.\304\317\257\267\261\321Xa\021\337\062\237>\217\031i\213\244\006\367\244P\376\065\370Y\354\256\226\311^\305;\003\236\220\322\005\373\273\361e=,\377\025\360\345\"\237\025X\354\343L-\207\tC\276\376N\310G\304)\255\301\324\227\002\002\006", expandedKey=expandedKey@entry=0x77310dd310 "")
    at /usr/src/debug/net-p2p/monero-0.15.0.1/monero-0.15.0.1/src/crypto/slow-hash.c:1106
#1  0x0000005555bb4a2c in cn_slow_hash (data=<optimized out>, length=<optimized out>, hash=0x77312dce98 " \322-1w", hash@entry=0x77312dd558 "", variant=825085592, prehashed=prehashed@entry=0, height=height@entry=1974879)
    at /usr/src/debug/net-p2p/monero-0.15.0.1/monero-0.15.0.1/src/crypto/slow-hash.c:1290
#2  0x0000005555ba7bb8 in crypto::cn_slow_hash (height=1974879, variant=<optimized out>, hash=..., length=<optimized out>, data=<optimized out>) at /usr/src/debug/net-p2p/monero-0.15.0.1/monero-0.15.0.1/src/crypto/hash.h:74
#3  cryptonote::get_block_longhash (pbc=pbc@entry=0x5556157b40, b=..., res=..., height=height@entry=1974879, miners=miners@entry=0) at /usr/src/debug/net-p2p/monero-0.15.0.1/monero-0.15.0.1/src/cryptonote_core/cryptonote_tx_utils.cpp:707
#4  0x0000005555ba7d38 in cryptonote::get_block_longhash (pbc=pbc@entry=0x5556157b40, b=..., height=height@entry=1974879, miners=miners@entry=0)
    at /usr/src/debug/net-p2p/monero-0.15.0.1/monero-0.15.0.1/src/cryptonote_core/cryptonote_tx_utils.cpp:715
#5  0x0000005555b5b8b0 in cryptonote::Blockchain::block_longhash_worker (this=0x5556157b40, height=1974880, blocks=..., map=...) at /usr/src/debug/net-p2p/monero-0.15.0.1/monero-0.15.0.1/src/cryptonote_core/blockchain.cpp:4306
#6  0x0000005555be06dc in std::function<void ()>::operator()() const (this=0x77312dd620) at /usr/lib/gcc/aarch64-unknown-linux-gnu/9.2.0/include/g++-v9/bits/std_function.h:685
#7  tools::threadpool::run (this=0x5555fd86e0 <tools::threadpool::getInstance()::instance>, flush=false) at /usr/src/debug/net-p2p/monero-0.15.0.1/monero-0.15.0.1/src/common/threadpool.cpp:153
#8  0x0000007ff7727b5c in ?? () from /usr/lib64/libboost_thread.so.1.71.0
#9  0x0000007ff73a4d68 in start_thread () from /lib64/libpthread.so.0
#10 0x0000007ff72fb4bc in thread_start () from /lib64/libc.so.6
(gdb) fr 0
#0  0x0000005555bb41e4 in aes_expand_key (
    key=key@entry=0x77310dcf80 "\206\206'H\313\266\064>\206\224\257\226\273\336\063^\302R\016K\225\213\021N\216\f\"\210\325k\311\272\317,\356\215\256q\361\243\035\027\220\065-\363\002\232\276y\232A\377\002R\205!\211c\035\321\352b\211\324\354\367UL\276\377\200\307\357\246\005\r\323\v\033\277S\304=#p\303\f\233\001h\353\227\275\361%.'L(\350g\343\324\033\060\"\312\016\365X\212h.\304\317\257\267\261\321Xa\021\337\062\237>\217\031i\213\244\006\367\244P\376\065\370Y\354\256\226\311^\305;\003\236\220\322\005\373\273\361e=,\377\025\360\345\"\237\025X\354\343L-\207\tC\276\376N\310G\304)\255\301\324\227\002\002\006", expandedKey=expandedKey@entry=0x77310dd310 "")
    at /usr/src/debug/net-p2p/monero-0.15.0.1/monero-0.15.0.1/src/crypto/slow-hash.c:1106
1106    __asm__(
(gdb) info args
key = 0x77310dcf80 "\206\206'H\313\266\064>\206\224\257\226\273\336\063^\302R\016K\225\213\021N\216\f\"\210\325k\311\272\317,\356\215\256q\361\243\035\027\220\065-\363\002\232\276y\232A\377\002R\205!\211c\035\321\352b\211\324\354\367UL\276\377\200\307\357\246\005\r\323\v\033\277S\304=#p\303\f\233\001h\353\227\275\361%.'L(\350g\343\324\033\060\"\312\016\365X\212h.\304\317\257\267\261\321Xa\021\337\062\237>\217\031i\213\244\006\367\244P\376\065\370Y\354\256\226\311^\305;\003\236\220\322\005\373\273\361e=,\377\025\360\345\"\237\025X\354\343L-\207\tC\276\376N\310G\304)\255\301\324\227\002\002\006"
expandedKey = 0x77310dd310 ""
```

# Discussion History
## bjacquin | 2019-11-30T15:07:12+00:00
Note that enabling -DNO_AES fixes the issue

## hyc | 2019-11-30T15:24:11+00:00
Yes, because raspberry Pis suck and all lack AES support. No issue to fix here.
It's wrong to use -march=armv8-a+crypto on these processors, you should just use -march=armv8-a.

## bjacquin | 2019-11-30T15:28:35+00:00
> Yes, because raspberry Pis suck and all lack AES support. No issue to fix here.
> It's wrong to use -march=armv8-a+crypto on these processors, you should just use -march=armv8-a.

You are likely correct, however armv8-a+crypto is set by CMakeLists.txt itself when NO_AES is not defined. It seems `CHECK_CXX_ACCEPTS_FLAG("-march=${ARCH}+crypto" ARCH_PLUS_CRYPTO)` does not identify the lack of AES support.

## hyc | 2019-11-30T15:32:35+00:00
Right, the compiler understands the flag. It doesn't know that the system you're going to run the binary on doesn't support it. If you feel like submitting a patch to do runtime detection of AES support for ARM, it would probably be welcomed. (Note that AES/crypto instructions may be supported on both ARMv8-a and ARMv7-l.)

## moneromooo-monero | 2019-12-04T18:48:55+00:00
+invalid

# Action History
- Created by: bjacquin | 2019-11-30T14:55:19+00:00
- Closed at: 2019-12-04T18:57:33+00:00
