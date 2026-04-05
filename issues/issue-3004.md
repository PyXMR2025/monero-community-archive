---
title: Android xmrig miner,running DERO-HE ,crash !!!!
source_url: https://github.com/xmrig/xmrig/issues/3004
author: Digger-coder
assignees: []
labels: []
created_at: '2022-04-06T04:02:42+00:00'
updated_at: '2025-06-28T10:42:01+00:00'
type: issue
status: closed
closed_at: '2025-06-28T10:42:01+00:00'
---

# Original Description
 28298-28310/com.xmrig.miner A/libc: Fatal signal 11 (SIGSEGV), code 1, fault addr 0x4c in tid 28310 (HeapTaskDaemon)
 A/DEBUG: *** *** *** *** *** *** *** *** *** *** *** *** *** *** *** ***
 A/DEBUG: Build fingerprint: 'Oppo/OppoS6/OppoS6:7.0/N90M/15291888:user/release-keys'
 A/DEBUG: Revision: '0'
 A/DEBUG: ABI: 'arm'
 A/DEBUG: pid: 28298, tid: 28310, name: HeapTaskDaemon  >>> com.xmrig.miner <<<
 A/DEBUG: signal 11 (SIGSEGV), code 1 (SEGV_MAPERR), fault addr 0x4c
 A/DEBUG:     r0 00000000  r1 03d17621  r2 f5f082fc  r3 00000080
 A/DEBUG:     r4 f3c6a204  r5 f3c2aba0  r6 ec73a000  r7 f3b7d484
 A/DEBUG:     r8 f3c2abe8  r9 12caafd8  sl ec73a000  fp 00000000
 A/DEBUG:     ip f5efe948  sp f2c41318  lr f5eddf1f  pc f39adc80  cpsr 80070030
 A/DEBUG: backtrace:
 A/DEBUG:     #00 pc 002a4c80  /system/lib/libart.so (_ZN3art11MonitorList16SweepMonitorListEPNS_15IsMarkedVisitorE+171)
 A/DEBUG:     #01 pc 0031f7b9  /system/lib/libart.so (_ZN3art7Runtime16SweepSystemWeaksEPNS_15IsMarkedVisitorE+20)
 A/DEBUG:     #02 pc 00177edd  /system/lib/libart.so (_ZN3art2gc9collector9MarkSweep16SweepSystemWeaksEPNS_6ThreadE+136)
 A/DEBUG:     #03 pc 00176f23  /system/lib/libart.so (_ZN3art2gc9collector9MarkSweep12ReclaimPhaseEv+114)
 A/DEBUG:     #04 pc 00176c7f  /system/lib/libart.so (_ZN3art2gc9collector9MarkSweep9RunPhasesEv+306)
 A/DEBUG:     #05 pc 00171851  /system/lib/libart.so (_ZN3art2gc9collector16GarbageCollector3RunENS0_7GcCauseEb+244)
 A/DEBUG:     #06 pc 001951f9  /system/lib/libart.so (_ZN3art2gc4Heap22CollectGarbageInternalENS0_9collector6GcTypeENS0_7GcCauseEb+2360)
 A/DEBUG:     #07 pc 0019aae5  /system/lib/libart.so (_ZN3art2gc4Heap12ConcurrentGCEPNS_6ThreadEb+68)
 A/DEBUG:     #08 pc 0019f683  /system/lib/libart.so (_ZN3art2gc4Heap16ConcurrentGCTask3RunEPNS_6ThreadE+18)
 A/DEBUG:     #09 pc 001b7b5b  /system/lib/libart.so (_ZN3art2gc13TaskProcessor11RunAllTasksEPNS_6ThreadE+30)
 A/DEBUG:     #10 pc 005e044f  /system/framework/arm/boot-core-libart.oat (offset 0x480000) (dalvik.system.VMRuntime.runHeapTasks+74)
 A/DEBUG:     #11 pc 005e41fb  /system/framework/arm/boot-core-libart.oat (offset 0x480000) (java.lang.Daemons$HeapTaskDaemon.run+150)
 A/DEBUG:     #12 pc 005f848d  /system/framework/arm/boot.oat (offset 0x56f000) (java.lang.Thread.run+48)
 A/DEBUG:     #13 pc 000a9fc1  /system/lib/libart.so (art_quick_invoke_stub_internal+64)
 A/DEBUG:     #14 pc 0040d5fd  /system/lib/libart.so (art_quick_invoke_stub+232)
 A/DEBUG:     #15 pc 000b1289  /system/lib/libart.so (_ZN3art9ArtMethod6InvokeEPNS_6ThreadEPjjPNS_6JValueEPKc+136)
 A/DEBUG:     #16 pc 0031a2bb  /system/lib/libart.so (_ZN3artL18InvokeWithArgArrayERKNS_33ScopedObjectAccessAlreadyRunnableEPNS_9ArtMethodEPNS_8ArgArrayEPNS_6JValueEPKc+58)
 A/DEBUG:     #17 pc 0031b069  /system/lib/libart.so (_ZN3art35InvokeVirtualOrInterfaceWithJValuesERKNS_33ScopedObjectAccessAlreadyRunnableEP8_jobjectP10_jmethodIDP6jvalue+256)
 A/DEBUG:     #18 pc 003349ad  /system/lib/libart.so (_ZN3art6Thread14CreateCallbackEPv+848)
 A/DEBUG:     #19 pc 00047273  /system/lib/libc.so (_ZL15__pthread_startPv+22)
 A/DEBUG:     #20 pc 00019e4d  /system/lib/libc.so (__start_thread+6)

# Discussion History
# Action History
- Created by: Digger-coder | 2022-04-06T04:02:42+00:00
- Closed at: 2025-06-28T10:42:01+00:00
