---
title: Building only shared wallet library for Android
source_url: https://github.com/monero-project/monero/issues/2051
author: ivan-ushakov
assignees: []
labels:
- invalid
created_at: '2017-05-26T19:13:04+00:00'
updated_at: '2018-07-30T17:59:05+00:00'
type: issue
status: closed
closed_at: '2017-10-03T11:24:23+00:00'
---

# Original Description
Is it possible to build shared wallet library for Android without any other binaries? I tried to follow guide for Android but it is for static build.

# Discussion History
## ivan-ushakov | 2017-05-28T07:10:14+00:00
I found how to build shared library but I can't use wallet API because of following crash:

    /? D/MoneroTest: creating wallet
    /? A/libc: Fatal signal 11 (SIGSEGV), code 1, fault addr 0x7f8b7fc2d0 in tid 6753 (Thread-4)
               
               [ 05-28 09:51:38.012   378:  378 W/         ]
               debuggerd: handling request: pid=6727 uid=10136 gid=10136 tid=6753
    /? D/upgrade: ACTION_PACKAGE_REMOVED
    /? A/DEBUG: *** *** *** *** *** *** *** *** *** *** *** *** *** *** *** ***
    /? A/DEBUG: Build fingerprint: 'google/bullhead/bullhead:7.1.2/N2G47O/3852959:user/release-keys'
    /? A/DEBUG: Revision: 'rev_1.0'
    /? A/DEBUG: ABI: 'arm64'
    /? A/DEBUG: pid: 6727, tid: 6753, name: Thread-4  >>> com.test.monerotest <<<
    /? A/DEBUG: signal 11 (SIGSEGV), code 1 (SEGV_MAPERR), fault addr 0x7f8b7fc2d0
    /? A/DEBUG:     x0   0000007f8b9fcd21  x1   000000000000000c  x2   0000007f8b9fc688  x3   0000000000000010
    /? A/DEBUG:     x4   00000000000000c6  x5   0000007f8b9fc1c8  x6   0000007f9af5ecec  x7   0000000000000000
    /? A/DEBUG:     x8   0000007f8b9fc588  x9   0000007f8b7fc318  x10  0000000000000000  x11  0000000000000018
    /? A/DEBUG:     x12  0000000000000120  x13  3a2265756c61765f  x14  7561666564222c30  x15  0000000000000000
    /? A/DEBUG:     x16  0000007f8b590448  x17  0000007f8b255e20  x18  0000000000000010  x19  0000007f8ba7b400
    /? A/DEBUG:     x20  0000007fa8ca3c78  x21  0000007f8ba7b400  x22  0000007f8b9fe62c  x23  0000007fa3ce2f54
    /? A/DEBUG:     x24  0000000000000010  x25  8d7816f78c282855  x26  0000007f8ba7b498  x27  8d7816f78c282855
    /? A/DEBUG:     x28  0000007f8b9fe350  x29  0000007f8b9fc660  x30  0000007f8aad4094
    /? A/DEBUG:     sp   0000007f8b7fc1f0  pc   0000007f8b255e50  pstate 0000000080000000
    /? I/ActivityManager: Start proc 6765:com.vkontakte.android/u0a89 for broadcast com.vkontakte.android/ru.mail.libverify.utils.PackageStateReceiver
    /? A/DEBUG: backtrace:
    /? A/DEBUG:     #00 pc 0000000000eaae50  /data/app/com.test.monerotest-2/lib/arm64/libwallet.so (cn_slow_hash+48)
    /? A/DEBUG:     #01 pc 0000000000729090  /data/app/com.test.monerotest-2/lib/arm64/libwallet.so (_ZN6crypto20generate_chacha8_keyEPKvmRNS_11chacha8_keyE+40)
    /? A/DEBUG:     #02 pc 0000000000729090  /data/app/com.test.monerotest-2/lib/arm64/libwallet.so (_ZN6crypto20generate_chacha8_keyEPKvmRNS_11chacha8_keyE+40)
    /? A/DEBUG:     #03 pc 0000000000725c54  /data/app/com.test.monerotest-2/lib/arm64/libwallet.so (_ZN6crypto20generate_chacha8_keyENSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEERNS_11chacha8_keyE+344)
    /? A/DEBUG:     #04 pc 00000000006bcbc4  /data/app/com.test.monerotest-2/lib/arm64/libwallet.so (_ZN5tools7wallet210store_keysERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_b+3536)
    /? A/DEBUG:     #05 pc 00000000006c19b8  /data/app/com.test.monerotest-2/lib/arm64/libwallet.so (_ZN5tools7wallet28generateERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_RKN6crypto10secret_keyEbb+1176)
    /? A/DEBUG:     #06 pc 00000000009f8cc8  /data/app/com.test.monerotest-2/lib/arm64/libwallet.so (_ZN6Monero10WalletImpl6createERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_S9_+1128)
    /? A/DEBUG:     #07 pc 0000000000a13be8  /data/app/com.test.monerotest-2/lib/arm64/libwallet.so (_ZN6Monero17WalletManagerImpl12createWalletERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_S9_b+108)
    /? A/DEBUG:     #08 pc 0000000000014394  /data/app/com.test.monerotest-2/lib/arm64/libnative-lib.so (Java_com_test_monerotest_MainActivity_createWallet+236)
    /? A/DEBUG:     #09 pc 00000000000dbd90  /system/lib64/libart.so (art_quick_generic_jni_trampoline+144)
    /? A/DEBUG:     #10 pc 00000000000d27b4  /system/lib64/libart.so (art_quick_invoke_stub+580)
    /? A/DEBUG:     #11 pc 00000000000df480  /system/lib64/libart.so (_ZN3art9ArtMethod6InvokeEPNS_6ThreadEPjjPNS_6JValueEPKc+208)
    /? A/DEBUG:     #12 pc 000000000029084c  /system/lib64/libart.so (_ZN3art11interpreter34ArtInterpreterToCompiledCodeBridgeEPNS_6ThreadEPNS_9ArtMethodEPKNS_7DexFile8CodeItemEPNS_11ShadowFrameEPNS_6JValueE+312)
    /? A/DEBUG:     #13 pc 0000000000289838  /system/lib64/libart.so (_ZN3art11interpreter6DoCallILb0ELb0EEEbPNS_9ArtMethodEPNS_6ThreadERNS_11ShadowFrameEPKNS_11InstructionEtPNS_6JValueE+596)
    /? A/DEBUG:     #14 pc 000000000055af9c  /system/lib64/libart.so (MterpInvokeDirect+392)
    /? A/DEBUG:     #15 pc 00000000000c5294  /system/lib64/libart.so (ExecuteMterpImpl+14484)

I used following code.

    WalletManager *manager = WalletManagerFactory::getWalletManager();
    if (manager != NULL) {
        __android_log_print(ANDROID_LOG_DEBUG, APPNAME, "creating wallet");
        manager->createWallet(convert(env, path), convert(env, password), convert(env, language));
    }

## hyc | 2017-05-28T13:16:54+00:00
This is probably a stack overrun. cn_slow_hash uses more than 2MB of stack and the default process and thread stack size is too small. This isn't a problem in the monero apps because they explicitly set a thread stack size of 5MB.

## ivan-ushakov | 2017-05-28T13:30:00+00:00
Yes, I already found this. It is a bit cryptic, but finally I can create wallet now. Next problem I faced is when I created wallet with wallet manager and check status I see critical error. I try to get error message but app fails on executing that getter.

## ehanoc | 2017-05-29T09:41:22+00:00
Any news on this? I had similar issue trying to integrate monero in Android projects. Help! 

## moneromooo-monero | 2017-05-31T22:03:45+00:00
Did you initialize the wallet correctly ? It needs init called on it (which maybe the wallet manager does, I'm not sure)

## ivan-ushakov | 2017-06-01T07:41:53+00:00
When I need to init wallet? After creating?

## moneromooo-monero | 2017-06-01T18:46:24+00:00
Yes. After creating, and before using. Call the init function. But check, maybe wallet manager already does this for you.

## moneromooo-monero | 2017-08-09T10:08:50+00:00
Did that work ?

## moneromooo-monero | 2017-10-03T11:15:51+00:00
The original bug was a stack overflow, not a monero bug. The subsequent one is unclear, no info given. Please reopen if there is more info.

+invalid


## Pei116 | 2018-07-30T17:59:05+00:00
@ivan-ushakov How were you able to fix the crash problem with cn_slow_hash()?

# Action History
- Created by: ivan-ushakov | 2017-05-26T19:13:04+00:00
- Closed at: 2017-10-03T11:24:23+00:00
