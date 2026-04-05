---
title: '[arm] Crash on android'
source_url: https://github.com/xmrig/xmrig/issues/619
author: kuangzhongwen
assignees: []
labels:
- arm
created_at: '2018-05-08T14:59:46+00:00'
updated_at: '2018-05-09T02:50:20+00:00'
type: issue
status: closed
closed_at: '2018-05-09T02:12:04+00:00'
---

# Original Description
#ifndef XMRIG_ARM
#   define VARIANT1_INIT(part) \
    uint64_t tweak1_2_##part = 0; \
    if (VARIANT > 0) { \
        tweak1_2_##part = (*reinterpret_cast<const uint64_t*>(input + 35 + part * size) ^ \
                          *(reinterpret_cast<const uint64_t*>(ctx[part]->state) + 24)); \
    }
#else
#   define VARIANT1_INIT(part) \
    uint64_t tweak1_2_##part = 0; \
    if (VARIANT > 0) { \
        volatile const uint64_t a = *reinterpret_cast<const uint64_t*>(input + 35 + part * size); \
        volatile const uint64_t b = *(reinterpret_cast<const uint64_t*>(ctx[part]->state) + 24); \
        tweak1_2_##part = a ^ b; \
    }
#endif


The "self_test" function crashed in this piece, my cell phone was Android 7, I used NDK compilation, compiled and passed, but this crash problem occurred during the runtime, and looked at the JNI crash log:
05-08 22:33:22.919 26600 26600 F DEBUG   : signal 7 (SIGBUS), code 1 (BUS_ADRALN), fault addr 0xc9170aa3
05-08 22:33:22.919 26600 26600 F DEBUG   :     r0 c6db2000  r1 c6cfe780  r2 f2052714  r3 f2052714
05-08 22:33:22.919 26600 26600 F DEBUG   :     r4 c9170aa3  r5 e711b008  r6 c937c9c4  r7 0000004c
05-08 22:33:22.919 26600 26600 F DEBUG   :     r8 df990504  r9 c937ccb0  sl c9121c45  fp 0000000d
05-08 22:33:22.919 26600 26600 F DEBUG   :     ip 00000000  sp c6cfe840  lr c911170d  pc c911c67c  cpsr 60010030
05-08 22:33:22.920   419   419 E ServiceManager: try to find service failed, not allowed access from isolated processes.
05-08 22:33:22.921 26600 26600 F DEBUG   : 
05-08 22:33:22.921 26600 26600 F DEBUG   : backtrace:
05-08 22:33:22.921 26600 26600 F DEBUG   :     #00 pc 0002e67c  /data/app/io.waterhole.miner-1/lib/arm/libmonero-miner.so (_Z23cryptonight_single_hashILN5xmrig4AlgoE0ELb1ELi1EEvPKhjPhPP15cryptonight_ctx+75)
05-08 22:33:22.921 26600 26600 F DEBUG   :     #01 pc 00031f25  /data/app/io.waterhole.miner-1/lib/arm/libmonero-miner.so (_ZN11MultiWorkerILj1EE8selfTestEv+92)
05-08 22:33:22.921 26600 26600 F DEBUG   :     #02 pc 00033cd9  /data/app/io.waterhole.miner-1/lib/arm/libmonero-miner.so (_ZN7Workers7onReadyEPv+148)
05-08 22:33:22.921 26600 26600 F DEBUG   :     #03 pc 00047983  /system/lib/libc.so (_ZL15__pthread_startPv+22)
05-08 22:33:22.922 26600 26600 F DEBUG   :     #04 pc 00019efd  /system/lib/libc.so (__start_thread+6)




It seems that the memory alignment problem, I hope you can help me. Thx!


# Discussion History
## xmrig | 2018-05-08T21:52:25+00:00
It known issue #446 still no fix it.
@NanoBytesInc maybe you already found solution?
Thank you.

## kuangzhongwen | 2018-05-09T02:10:56+00:00
@xmrig https://github.com/NanoBytesInc/miners，he @NanoBytesInc ran the old version on Android. The code seems to have changed little. Is there anything special?

## kuangzhongwen | 2018-05-09T02:41:21+00:00
@NanoBytesInc But my machine is 64-bit, I can use the old xmrig you compiled to run, but the new version of xmrig I compiled has crashed.

root      590   1     2252552 17024          0 0000000000 S zygote64


The new versions of this code(crash):
#ifndef XMRIG_ARM
#define VARIANT1_INIT(part) \
    uint64_t tweak1_2_##part = 0; \
    if (VARIANT > 0) { \
        tweak1_2_##part = (*reinterpret_cast<const uint64_t*>(input + 35 + part * size) ^ \
                          *(reinterpret_cast<const uint64_t*>(ctx[part]->state) + 24)); \
    }
#else
#define VARIANT1_INIT(part) \
    uint64_t tweak1_2_##part = 0; \
    if (VARIANT > 0) { \
        volatile const uint64_t a = *reinterpret_cast<const uint64_t*>(input + 35 + part * size); \
        volatile const uint64_t b = *(reinterpret_cast<const uint64_t*>(ctx[part]->state) + 24); \
        LOGD("%s", "arm VARIANT1_INIT end"); \
    }
#endif


The old versions of this code(ok):
#define VARIANT1_INIT(part) \
    uint64_t tweak1_2_##part = 0; \
    if (VARIANT > 0) { \
        tweak1_2_##part = (*reinterpret_cast<const uint64_t*>(input + 35 + part * size) ^ \
                          *(reinterpret_cast<const uint64_t*>(ctx->state##part) + 24)); \
    }

# Action History
- Created by: kuangzhongwen | 2018-05-08T14:59:46+00:00
- Closed at: 2018-05-09T02:12:04+00:00
