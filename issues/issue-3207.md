---
title: Segfault on Mac M1 with arm64 version v6.19.0
source_url: https://github.com/xmrig/xmrig/issues/3207
author: footcow
assignees: []
labels:
- bug
- arm
- randomx
created_at: '2023-02-02T07:57:56+00:00'
updated_at: '2023-10-20T00:36:36+00:00'
type: issue
status: closed
closed_at: '2023-02-02T14:41:45+00:00'
---

# Original Description
Use this config.json file and just launch `./xmrig` then after few second get a segfault, going back to version 6.18.1 with exact same config.json file.

**config.json**
```
{
    "api": {
        "id": null,
        "worker-id": null
    },
    "http": {
        "enabled": false,
        "host": "127.0.0.1",
        "port": 0,
        "access-token": null,
        "restricted": true
    },
    "autosave": true,
    "background": false,
    "colors": true,
    "title": true,
    "randomx": {
        "init": -1,
        "init-avx2": -1,
        "mode": "auto",
        "1gb-pages": false,
        "rdmsr": true,
        "wrmsr": false,
        "cache_qos": false,
        "numa": true,
        "scratchpad_prefetch_mode": 1
    },
    "cpu": {
        "enabled": true,
        "huge-pages": true,
        "huge-pages-jit": false,
        "hw-aes": null,
        "priority": null,
        "memory-pool": false,
        "yield": true,
        "argon2-impl": null,
        "astrobwt-max-size": 550,
        "astrobwt-avx2": false,
        "argon2": [0, 1, 2, 3, 4, 5, 6, 7],
        "astrobwt": [0, 1, 2, 3, 4, 5, 6, 7],
        "cn": [0, 1, 2, 3, 4, 5, 6, 7],
        "cn-heavy": [0, 1, 2, 3, 4, 5, 6, 7],
        "cn-lite": [0, 1, 2, 3, 4, 5, 6, 7],
        "cn-pico": [0, 1, 2, 3, 4, 5, 6, 7],
        "cn/upx2": [0, 1, 2, 3, 4, 5, 6, 7],
        "rx": [0, 1, 2, 3, 4, 5, 6, 7],
        "rx/wow": [0, 1, 2, 3, 4, 5, 6, 7],
        "cn/0": false,
        "cn-lite/0": false,
        "rx/arq": "rx/wow",
        "rx/keva": "rx/wow"
    },
    "opencl": {
        "enabled": false,
        "cache": true,
        "loader": null,
        "cn/0": false,
        "cn-lite/0": false
    },
    "cuda": {
        "enabled": false,
        "loader": null,
        "cn/0": false,
        "cn-lite/0": false
    },
    "log-file": null,
    "donate-level": 1,
    "donate-over-proxy": 1,
    "pools": [
        {
            "algo": "rx/0",
            "coin": null,
            "url": "rx.unmineable.com:3333",
            "user": "BNB:0x6xxxx.MacM1",
            "pass": "x",
            "rig-id": null,
            "nicehash": false,
            "keepalive": false,
            "enabled": true,
            "tls": false,
            "tls-fingerprint": null,
            "daemon": false,
            "socks5": null,
            "self-select": null,
            "submit-to-origin": false
        }
    ],
    "retries": 5,
    "retry-pause": 5,
    "print-time": 60,
    "syslog": false,
    "tls": {
        "enabled": false,
        "protocols": null,
        "cert": null,
        "cert_key": null,
        "ciphers": null,
        "ciphersuites": null,
        "dhparam": null
    },
    "dns": {
        "ipv6": false,
        "ttl": 30
    },
    "user-agent": null,
    "verbose": 0,
    "watch": true,
    "pause-on-battery": false,
    "pause-on-active": false
}
```

**Trace segfault log**
```
-------------------------------------
Translated Report (Full Report Below)
-------------------------------------

Process:               xmrig [59367]
Path:                  /Users/USER/Downloads/*/xmrig
Identifier:            xmrig
Version:               ???
Code Type:             ARM-64 (Native)
Parent Process:        zsh [1483]
User ID:               501

Date/Time:             2023-02-02 08:36:15.1793 +0100
OS Version:            macOS 13.1 (22C65)
Report Version:        12
Anonymous UUID:        BE81BE42-2DAE-A625-77FF-485EEEBE001E

Sleep/Wake UUID:       1AAC1675-0457-4E65-BCB2-B8509C47BC88

Time Awake Since Boot: 3000000 seconds
Time Since Wake:       400 seconds

System Integrity Protection: enabled

Crashed Thread:        12

Exception Type:        EXC_BAD_ACCESS (SIGSEGV)
Exception Codes:       KERN_INVALID_ADDRESS at 0x0000000000000000
Exception Codes:       0x0000000000000001, 0x0000000000000000

Termination Reason:    Namespace SIGNAL, Code 11 Segmentation fault: 11
Terminating Process:   exc handler [59367]

VM Region Info: 0 is not in any region.  Bytes before following region: 4362878976
      REGION TYPE                    START - END         [ VSIZE] PRT/MAX SHRMOD  REGION DETAIL
      UNUSED SPACE AT START
--->  
      __TEXT                      1040c4000-104594000    [ 4928K] r-x/r-x SM=COW  ...loads/*/xmrig

Thread 0::  Dispatch queue: com.apple.main-thread
0   libsystem_kernel.dylib        	       0x19294fe18 kevent + 8
1   xmrig                         	       0x1043e5cd4 0x1040c4000 + 3284180
2   xmrig                         	       0x1043d69b4 0x1040c4000 + 3221940
3   xmrig                         	       0x10417a06c 0x1040c4000 + 745580
4   xmrig                         	       0x10418593c 0x1040c4000 + 792892
5   dyld                          	       0x19265fe50 start + 2544

Thread 1:
0   libsystem_kernel.dylib        	       0x19294d564 __psynch_cvwait + 8
1   libsystem_pthread.dylib       	       0x192989638 _pthread_cond_wait + 1232
2   libc++.1.dylib                	       0x1928d6ac4 std::__1::condition_variable::wait(std::__1::unique_lock<std::__1::mutex>&) + 28
3   xmrig                         	       0x1041eb168 0x1040c4000 + 1208680
4   xmrig                         	       0x1041ec094 0x1040c4000 + 1212564
5   libsystem_pthread.dylib       	       0x19298906c _pthread_start + 148
6   libsystem_pthread.dylib       	       0x192983e2c thread_start + 8

Thread 2:
0   libsystem_kernel.dylib        	       0x19294d564 __psynch_cvwait + 8
1   libsystem_pthread.dylib       	       0x192989638 _pthread_cond_wait + 1232
2   xmrig                         	       0x1043e161c 0x1040c4000 + 3266076
3   xmrig                         	       0x1043d3684 0x1040c4000 + 3208836
4   libsystem_pthread.dylib       	       0x19298906c _pthread_start + 148
5   libsystem_pthread.dylib       	       0x192983e2c thread_start + 8

Thread 3:
0   libsystem_kernel.dylib        	       0x19294d564 __psynch_cvwait + 8
1   libsystem_pthread.dylib       	       0x192989638 _pthread_cond_wait + 1232
2   xmrig                         	       0x1043e161c 0x1040c4000 + 3266076
3   xmrig                         	       0x1043d3684 0x1040c4000 + 3208836
4   libsystem_pthread.dylib       	       0x19298906c _pthread_start + 148
5   libsystem_pthread.dylib       	       0x192983e2c thread_start + 8

Thread 4:
0   libsystem_kernel.dylib        	       0x19294d564 __psynch_cvwait + 8
1   libsystem_pthread.dylib       	       0x192989638 _pthread_cond_wait + 1232
2   xmrig                         	       0x1043e161c 0x1040c4000 + 3266076
3   xmrig                         	       0x1043d3684 0x1040c4000 + 3208836
4   libsystem_pthread.dylib       	       0x19298906c _pthread_start + 148
5   libsystem_pthread.dylib       	       0x192983e2c thread_start + 8

Thread 5:
0   libsystem_kernel.dylib        	       0x19294d564 __psynch_cvwait + 8
1   libsystem_pthread.dylib       	       0x192989638 _pthread_cond_wait + 1232
2   xmrig                         	       0x1043e161c 0x1040c4000 + 3266076
3   xmrig                         	       0x1043d3684 0x1040c4000 + 3208836
4   libsystem_pthread.dylib       	       0x19298906c _pthread_start + 148
5   libsystem_pthread.dylib       	       0x192983e2c thread_start + 8

Thread 6:
0   xmrig                         	       0x1041d5ffc void fillAes1Rx4<0>(void*, unsigned long, void*) + 104
1   xmrig                         	       0x10414e664 xmrig::CpuWorker<1ul>::start() + 572
2   xmrig                         	       0x104144c34 xmrig::Workers<xmrig::CpuLaunchData>::onReady(void*) + 84
3   libsystem_pthread.dylib       	       0x19298906c _pthread_start + 148
4   libsystem_pthread.dylib       	       0x192983e2c thread_start + 8

Thread 7:
0   xmrig                         	       0x1041d5ffc void fillAes1Rx4<0>(void*, unsigned long, void*) + 104
1   xmrig                         	       0x10414e664 xmrig::CpuWorker<1ul>::start() + 572
2   xmrig                         	       0x104144c34 xmrig::Workers<xmrig::CpuLaunchData>::onReady(void*) + 84
3   libsystem_pthread.dylib       	       0x19298906c _pthread_start + 148
4   libsystem_pthread.dylib       	       0x192983e2c thread_start + 8

Thread 8:
0   xmrig                         	       0x1041d5ffc void fillAes1Rx4<0>(void*, unsigned long, void*) + 104
1   xmrig                         	       0x10414e664 xmrig::CpuWorker<1ul>::start() + 572
2   xmrig                         	       0x104144c34 xmrig::Workers<xmrig::CpuLaunchData>::onReady(void*) + 84
3   libsystem_pthread.dylib       	       0x19298906c _pthread_start + 148
4   libsystem_pthread.dylib       	       0x192983e2c thread_start + 8

Thread 9:
0   xmrig                         	       0x1041d5ffc void fillAes1Rx4<0>(void*, unsigned long, void*) + 104
1   xmrig                         	       0x10414e664 xmrig::CpuWorker<1ul>::start() + 572
2   xmrig                         	       0x104144c34 xmrig::Workers<xmrig::CpuLaunchData>::onReady(void*) + 84
3   libsystem_pthread.dylib       	       0x19298906c _pthread_start + 148
4   libsystem_pthread.dylib       	       0x192983e2c thread_start + 8

Thread 10:
0   xmrig                         	       0x1041d5ffc void fillAes1Rx4<0>(void*, unsigned long, void*) + 104
1   xmrig                         	       0x10414e664 xmrig::CpuWorker<1ul>::start() + 572
2   xmrig                         	       0x104144c34 xmrig::Workers<xmrig::CpuLaunchData>::onReady(void*) + 84
3   libsystem_pthread.dylib       	       0x19298906c _pthread_start + 148
4   libsystem_pthread.dylib       	       0x192983e2c thread_start + 8

Thread 11:
0   xmrig                         	       0x1041d5ffc void fillAes1Rx4<0>(void*, unsigned long, void*) + 104
1   xmrig                         	       0x10414e664 xmrig::CpuWorker<1ul>::start() + 572
2   xmrig                         	       0x104144c34 xmrig::Workers<xmrig::CpuLaunchData>::onReady(void*) + 84
3   libsystem_pthread.dylib       	       0x19298906c _pthread_start + 148
4   libsystem_pthread.dylib       	       0x192983e2c thread_start + 8

Thread 12 Crashed:
0   ???                           	       0x104778240 ???

Thread 13:
0   xmrig                         	       0x1041d5ffc void fillAes1Rx4<0>(void*, unsigned long, void*) + 104
1   xmrig                         	       0x10414e664 xmrig::CpuWorker<1ul>::start() + 572
2   xmrig                         	       0x104144c34 xmrig::Workers<xmrig::CpuLaunchData>::onReady(void*) + 84
3   libsystem_pthread.dylib       	       0x19298906c _pthread_start + 148
4   libsystem_pthread.dylib       	       0x192983e2c thread_start + 8


Thread 12 crashed with ARM Thread State (64-bit):
    x0: 0x0000000000000000   x1: 0x00000002801041c0   x2: 0x0000000140008000   x3: 0x0000000000000800
    x4: 0x574884c0aaed8544   x5: 0xff1d6511b994ef32   x6: 0x0ee8cda11e8970fe   x7: 0x06e642e9f555a42c
    x8: 0x0000000000000000   x9: 0x529d81c02fa48660  x10: 0x529d81c02fa48660  x11: 0x0000000000000000
   x12: 0x95cb002475bf75e2  x13: 0xd8bf363adaa0a6a3  x14: 0x0b9d2b833891aff8  x15: 0x4285d88244746661
   x16: 0x0000000140050640  x17: 0x00000001401e01c0  x18: 0x0000000000000000  x19: 0x0000000017278a9b
   x20: 0x0000000000000000  x21: 0x0000000000000000  x22: 0xb4180e1c44a771bd  x23: 0x935b3bd18dddbf06
   x24: 0xf928c40a02493854  x25: 0x8d91848b8d51a3f7  x26: 0xc5057ddb11f292cf  x27: 0xb9deff907dad51b5
   x28: 0xbdcbc399d1ac3507   fp: 0x99fab19e98fa3c16   lr: 0xff6341c34e177305
    sp: 0x000000016e1b6d60   pc: 0x0000000104778240 cpsr: 0x60001000
   far: 0x0000000000000000  esr: 0x92000006 (Data Abort) byte read Translation fault

Binary Images:
       0x192949000 -        0x192981ff3 libsystem_kernel.dylib (*) <aebf397e-e2ef-3a49-be58-23d4558511f6> /usr/lib/system/libsystem_kernel.dylib
       0x1040c4000 -        0x104593fff xmrig (*) <a9505f1b-8e76-379e-a738-0e974dbe5652> /Users/USER/Downloads/*/xmrig
       0x19265a000 -        0x1926e4b63 dyld (*) <487cfdeb-9b07-39bf-bfb9-970b61aea2d1> /usr/lib/dyld
       0x192982000 -        0x19298effb libsystem_pthread.dylib (*) <132084c6-c347-3489-9ac2-fcaad21cdb73> /usr/lib/system/libsystem_pthread.dylib
       0x1928ca000 -        0x192930ff3 libc++.1.dylib (*) <a4bed887-64ce-3f2e-80df-87d583b262d9> /usr/lib/libc++.1.dylib
               0x0 - 0xffffffffffffffff ??? (*) <00000000-0000-0000-0000-000000000000> ???

External Modification Summary:
  Calls made by other processes targeting this process:
    task_for_pid: 0
    thread_create: 0
    thread_set_state: 0
  Calls made by this process:
    task_for_pid: 0
    thread_create: 0
    thread_set_state: 0
  Calls made by all processes on this machine:
    task_for_pid: 0
    thread_create: 0
    thread_set_state: 0

VM Region Summary:
ReadOnly portion of Libraries: Total=870.5M resident=0K(0%) swapped_out_or_unallocated=870.5M(100%)
Writable regions: Total=3.6G written=0K(0%) resident=0K(0%) swapped_out=0K(0%) unallocated=3.6G(100%)

                                VIRTUAL   REGION 
REGION TYPE                        SIZE    COUNT (non-coalesced) 
===========                     =======  ======= 
Activity Tracing                   256K        1 
Kernel Alloc Once                   32K        1 
MALLOC                             2.5G       48 
MALLOC guard page                   96K        5 
MALLOC_MEDIUM (reserved)         720.0M        6         reserved VM address space (unallocated)
MALLOC_NANO (reserved)           384.0M        1         reserved VM address space (unallocated)
STACK GUARD                       56.2M       14 
Stack                             44.8M       14 
VM_ALLOCATE                        128K        2 
__AUTH                             307K       58 
__AUTH_CONST                      3543K      142 
__DATA                            2123K      137 
__DATA_CONST                      4341K      144 
__DATA_DIRTY                       361K       58 
__LINKEDIT                       767.3M        2 
__OBJC_CONST                       289K       36 
__OBJC_RO                         65.4M        1 
__OBJC_RW                         1986K        1 
__TEXT                           103.2M      151 
dyld private memory                256K        1 
mapped file                         64K        1 
shared memory                       32K        2 
===========                     =======  ======= 
TOTAL                              4.6G      826 
TOTAL, minus reserved VM space     3.5G      826 



-----------
Full Report
-----------

{"app_name":"xmrig","timestamp":"2023-02-02 08:36:15.00 +0100","app_version":"","slice_uuid":"a9505f1b-8e76-379e-a738-0e974dbe5652","build_version":"","platform":1,"share_with_app_devs":1,"is_first_party":1,"bug_type":"309","os_version":"macOS 13.1 (22C65)","roots_installed":0,"incident_id":"02A2E427-A011-469C-8A8F-65E47AFF9A07","name":"xmrig"}
{
  "uptime" : 3000000,
  "procRole" : "Unspecified",
  "version" : 2,
  "userID" : 501,
  "deployVersion" : 210,
  "modelCode" : "MacBookPro17,1",
  "coalitionID" : 823,
  "osVersion" : {
    "train" : "macOS 13.1",
    "build" : "22C65",
    "releaseType" : "User"
  },
  "captureTime" : "2023-02-02 08:36:15.1793 +0100",
  "incident" : "02A2E427-A011-469C-8A8F-65E47AFF9A07",
  "pid" : 59367,
  "translated" : false,
  "cpuType" : "ARM-64",
  "roots_installed" : 0,
  "bug_type" : "309",
  "procLaunch" : "2023-02-02 08:36:09.7249 +0100",
  "procStartAbsTime" : 74057837528378,
  "procExitAbsTime" : 74057968107409,
  "procName" : "xmrig",
  "procPath" : "\/Users\/USER\/Downloads\/*\/xmrig",
  "parentProc" : "zsh",
  "parentPid" : 1483,
  "coalitionName" : "com.googlecode.iterm2",
  "crashReporterKey" : "BE81BE42-2DAE-A625-77FF-485EEEBE001E",
  "responsiblePid" : 1290,
  "wakeTime" : 400,
  "sleepWakeUUID" : "1AAC1675-0457-4E65-BCB2-B8509C47BC88",
  "sip" : "enabled",
  "vmRegionInfo" : "0 is not in any region.  Bytes before following region: 4362878976\n      REGION TYPE                    START - END         [ VSIZE] PRT\/MAX SHRMOD  REGION DETAIL\n      UNUSED SPACE AT START\n--->  \n      __TEXT                      1040c4000-104594000    [ 4928K] r-x\/r-x SM=COW  ...loads\/*\/xmrig",
  "exception" : {"codes":"0x0000000000000001, 0x0000000000000000","rawCodes":[1,0],"type":"EXC_BAD_ACCESS","signal":"SIGSEGV","subtype":"KERN_INVALID_ADDRESS at 0x0000000000000000"},
  "termination" : {"flags":0,"code":11,"namespace":"SIGNAL","indicator":"Segmentation fault: 11","byProc":"exc handler","byPid":59367},
  "vmregioninfo" : "0 is not in any region.  Bytes before following region: 4362878976\n      REGION TYPE                    START - END         [ VSIZE] PRT\/MAX SHRMOD  REGION DETAIL\n      UNUSED SPACE AT START\n--->  \n      __TEXT                      1040c4000-104594000    [ 4928K] r-x\/r-x SM=COW  ...loads\/*\/xmrig",
  "extMods" : {"caller":{"thread_create":0,"thread_set_state":0,"task_for_pid":0},"system":{"thread_create":0,"thread_set_state":0,"task_for_pid":0},"targeted":{"thread_create":0,"thread_set_state":0,"task_for_pid":0},"warnings":0},
  "faultingThread" : 12,
  "threads" : [{"id":24692811,"queue":"com.apple.main-thread","frames":[{"imageOffset":28184,"symbol":"kevent","symbolLocation":8,"imageIndex":0},{"imageOffset":3284180,"imageIndex":1},{"imageOffset":3221940,"imageIndex":1},{"imageOffset":745580,"imageIndex":1},{"imageOffset":792892,"imageIndex":1},{"imageOffset":24144,"symbol":"start","symbolLocation":2544,"imageIndex":2}]},{"id":24692812,"frames":[{"imageOffset":17764,"symbol":"__psynch_cvwait","symbolLocation":8,"imageIndex":0},{"imageOffset":30264,"symbol":"_pthread_cond_wait","symbolLocation":1232,"imageIndex":3},{"imageOffset":51908,"symbol":"std::__1::condition_variable::wait(std::__1::unique_lock<std::__1::mutex>&)","symbolLocation":28,"imageIndex":4},{"imageOffset":1208680,"imageIndex":1},{"imageOffset":1212564,"imageIndex":1},{"imageOffset":28780,"symbol":"_pthread_start","symbolLocation":148,"imageIndex":3},{"imageOffset":7724,"symbol":"thread_start","symbolLocation":8,"imageIndex":3}]},{"id":24692813,"frames":[{"imageOffset":17764,"symbol":"__psynch_cvwait","symbolLocation":8,"imageIndex":0},{"imageOffset":30264,"symbol":"_pthread_cond_wait","symbolLocation":1232,"imageIndex":3},{"imageOffset":3266076,"imageIndex":1},{"imageOffset":3208836,"imageIndex":1},{"imageOffset":28780,"symbol":"_pthread_start","symbolLocation":148,"imageIndex":3},{"imageOffset":7724,"symbol":"thread_start","symbolLocation":8,"imageIndex":3}]},{"id":24692814,"frames":[{"imageOffset":17764,"symbol":"__psynch_cvwait","symbolLocation":8,"imageIndex":0},{"imageOffset":30264,"symbol":"_pthread_cond_wait","symbolLocation":1232,"imageIndex":3},{"imageOffset":3266076,"imageIndex":1},{"imageOffset":3208836,"imageIndex":1},{"imageOffset":28780,"symbol":"_pthread_start","symbolLocation":148,"imageIndex":3},{"imageOffset":7724,"symbol":"thread_start","symbolLocation":8,"imageIndex":3}]},{"id":24692815,"frames":[{"imageOffset":17764,"symbol":"__psynch_cvwait","symbolLocation":8,"imageIndex":0},{"imageOffset":30264,"symbol":"_pthread_cond_wait","symbolLocation":1232,"imageIndex":3},{"imageOffset":3266076,"imageIndex":1},{"imageOffset":3208836,"imageIndex":1},{"imageOffset":28780,"symbol":"_pthread_start","symbolLocation":148,"imageIndex":3},{"imageOffset":7724,"symbol":"thread_start","symbolLocation":8,"imageIndex":3}]},{"id":24692816,"frames":[{"imageOffset":17764,"symbol":"__psynch_cvwait","symbolLocation":8,"imageIndex":0},{"imageOffset":30264,"symbol":"_pthread_cond_wait","symbolLocation":1232,"imageIndex":3},{"imageOffset":3266076,"imageIndex":1},{"imageOffset":3208836,"imageIndex":1},{"imageOffset":28780,"symbol":"_pthread_start","symbolLocation":148,"imageIndex":3},{"imageOffset":7724,"symbol":"thread_start","symbolLocation":8,"imageIndex":3}]},{"id":24692850,"frames":[{"imageOffset":1122300,"symbol":"void fillAes1Rx4<0>(void*, unsigned long, void*)","symbolLocation":104,"imageIndex":1},{"imageOffset":566884,"symbol":"xmrig::CpuWorker<1ul>::start()","symbolLocation":572,"imageIndex":1},{"imageOffset":527412,"symbol":"xmrig::Workers<xmrig::CpuLaunchData>::onReady(void*)","symbolLocation":84,"imageIndex":1},{"imageOffset":28780,"symbol":"_pthread_start","symbolLocation":148,"imageIndex":3},{"imageOffset":7724,"symbol":"thread_start","symbolLocation":8,"imageIndex":3}]},{"id":24692851,"frames":[{"imageOffset":1122300,"symbol":"void fillAes1Rx4<0>(void*, unsigned long, void*)","symbolLocation":104,"imageIndex":1},{"imageOffset":566884,"symbol":"xmrig::CpuWorker<1ul>::start()","symbolLocation":572,"imageIndex":1},{"imageOffset":527412,"symbol":"xmrig::Workers<xmrig::CpuLaunchData>::onReady(void*)","symbolLocation":84,"imageIndex":1},{"imageOffset":28780,"symbol":"_pthread_start","symbolLocation":148,"imageIndex":3},{"imageOffset":7724,"symbol":"thread_start","symbolLocation":8,"imageIndex":3}]},{"id":24692852,"frames":[{"imageOffset":1122300,"symbol":"void fillAes1Rx4<0>(void*, unsigned long, void*)","symbolLocation":104,"imageIndex":1},{"imageOffset":566884,"symbol":"xmrig::CpuWorker<1ul>::start()","symbolLocation":572,"imageIndex":1},{"imageOffset":527412,"symbol":"xmrig::Workers<xmrig::CpuLaunchData>::onReady(void*)","symbolLocation":84,"imageIndex":1},{"imageOffset":28780,"symbol":"_pthread_start","symbolLocation":148,"imageIndex":3},{"imageOffset":7724,"symbol":"thread_start","symbolLocation":8,"imageIndex":3}]},{"id":24692853,"frames":[{"imageOffset":1122300,"symbol":"void fillAes1Rx4<0>(void*, unsigned long, void*)","symbolLocation":104,"imageIndex":1},{"imageOffset":566884,"symbol":"xmrig::CpuWorker<1ul>::start()","symbolLocation":572,"imageIndex":1},{"imageOffset":527412,"symbol":"xmrig::Workers<xmrig::CpuLaunchData>::onReady(void*)","symbolLocation":84,"imageIndex":1},{"imageOffset":28780,"symbol":"_pthread_start","symbolLocation":148,"imageIndex":3},{"imageOffset":7724,"symbol":"thread_start","symbolLocation":8,"imageIndex":3}]},{"id":24692854,"frames":[{"imageOffset":1122300,"symbol":"void fillAes1Rx4<0>(void*, unsigned long, void*)","symbolLocation":104,"imageIndex":1},{"imageOffset":566884,"symbol":"xmrig::CpuWorker<1ul>::start()","symbolLocation":572,"imageIndex":1},{"imageOffset":527412,"symbol":"xmrig::Workers<xmrig::CpuLaunchData>::onReady(void*)","symbolLocation":84,"imageIndex":1},{"imageOffset":28780,"symbol":"_pthread_start","symbolLocation":148,"imageIndex":3},{"imageOffset":7724,"symbol":"thread_start","symbolLocation":8,"imageIndex":3}]},{"id":24692855,"frames":[{"imageOffset":1122300,"symbol":"void fillAes1Rx4<0>(void*, unsigned long, void*)","symbolLocation":104,"imageIndex":1},{"imageOffset":566884,"symbol":"xmrig::CpuWorker<1ul>::start()","symbolLocation":572,"imageIndex":1},{"imageOffset":527412,"symbol":"xmrig::Workers<xmrig::CpuLaunchData>::onReady(void*)","symbolLocation":84,"imageIndex":1},{"imageOffset":28780,"symbol":"_pthread_start","symbolLocation":148,"imageIndex":3},{"imageOffset":7724,"symbol":"thread_start","symbolLocation":8,"imageIndex":3}]},{"triggered":true,"id":24692856,"threadState":{"x":[{"value":0},{"value":10738483648},{"value":5368741888},{"value":2048},{"value":6289422842659177796},{"value":18382960380798627634},{"value":1074334603013615870},{"value":497158381481862188},{"value":0},{"value":5953056944886679136},{"value":5953056944886679136},{"value":0},{"value":10793721088517830114},{"value":15618261659148134051},{"value":836872948350562296},{"value":4793475432411588193},{"value":5369038400},{"value":5370675648},{"value":0},{"value":388467355},{"value":0},{"value":0},{"value":12977137840841781693},{"value":10618146317670399750},{"value":17953815461779552340},{"value":10201080365877142519},{"value":14196891780207776463},{"value":13393423337895317941},{"value":13676239758855779591}],"flavor":"ARM_THREAD_STATE64","lr":{"value":18402624809450566405},"cpsr":{"value":1610616832},"fp":{"value":11095375926710123542},"sp":{"value":6142258528},"esr":{"value":2449473542,"description":"(Data Abort) byte read Translation fault"},"pc":{"value":4369908288,"matchesCrashFrame":1},"far":{"value":0}},"frames":[{"imageOffset":4369908288,"imageIndex":5}]},{"id":24692857,"frames":[{"imageOffset":1122300,"symbol":"void fillAes1Rx4<0>(void*, unsigned long, void*)","symbolLocation":104,"imageIndex":1},{"imageOffset":566884,"symbol":"xmrig::CpuWorker<1ul>::start()","symbolLocation":572,"imageIndex":1},{"imageOffset":527412,"symbol":"xmrig::Workers<xmrig::CpuLaunchData>::onReady(void*)","symbolLocation":84,"imageIndex":1},{"imageOffset":28780,"symbol":"_pthread_start","symbolLocation":148,"imageIndex":3},{"imageOffset":7724,"symbol":"thread_start","symbolLocation":8,"imageIndex":3}]}],
  "usedImages" : [
  {
    "source" : "P",
    "arch" : "arm64e",
    "base" : 6754177024,
    "size" : 233460,
    "uuid" : "aebf397e-e2ef-3a49-be58-23d4558511f6",
    "path" : "\/usr\/lib\/system\/libsystem_kernel.dylib",
    "name" : "libsystem_kernel.dylib"
  },
  {
    "source" : "P",
    "arch" : "arm64",
    "base" : 4362878976,
    "size" : 5046272,
    "uuid" : "a9505f1b-8e76-379e-a738-0e974dbe5652",
    "path" : "\/Users\/USER\/Downloads\/*\/xmrig",
    "name" : "xmrig"
  },
  {
    "source" : "P",
    "arch" : "arm64e",
    "base" : 6751100928,
    "size" : 568164,
    "uuid" : "487cfdeb-9b07-39bf-bfb9-970b61aea2d1",
    "path" : "\/usr\/lib\/dyld",
    "name" : "dyld"
  },
  {
    "source" : "P",
    "arch" : "arm64e",
    "base" : 6754410496,
    "size" : 53244,
    "uuid" : "132084c6-c347-3489-9ac2-fcaad21cdb73",
    "path" : "\/usr\/lib\/system\/libsystem_pthread.dylib",
    "name" : "libsystem_pthread.dylib"
  },
  {
    "source" : "P",
    "arch" : "arm64e",
    "base" : 6753656832,
    "size" : 421876,
    "uuid" : "a4bed887-64ce-3f2e-80df-87d583b262d9",
    "path" : "\/usr\/lib\/libc++.1.dylib",
    "name" : "libc++.1.dylib"
  },
  {
    "size" : 0,
    "source" : "A",
    "base" : 0,
    "uuid" : "00000000-0000-0000-0000-000000000000"
  }
],
  "sharedCache" : {
  "base" : 6750453760,
  "size" : 3434283008,
  "uuid" : "00a1fbb6-43e1-3c11-8483-faf0db659249"
},
  "vmSummary" : "ReadOnly portion of Libraries: Total=870.5M resident=0K(0%) swapped_out_or_unallocated=870.5M(100%)\nWritable regions: Total=3.6G written=0K(0%) resident=0K(0%) swapped_out=0K(0%) unallocated=3.6G(100%)\n\n                                VIRTUAL   REGION \nREGION TYPE                        SIZE    COUNT (non-coalesced) \n===========                     =======  ======= \nActivity Tracing                   256K        1 \nKernel Alloc Once                   32K        1 \nMALLOC                             2.5G       48 \nMALLOC guard page                   96K        5 \nMALLOC_MEDIUM (reserved)         720.0M        6         reserved VM address space (unallocated)\nMALLOC_NANO (reserved)           384.0M        1         reserved VM address space (unallocated)\nSTACK GUARD                       56.2M       14 \nStack                             44.8M       14 \nVM_ALLOCATE                        128K        2 \n__AUTH                             307K       58 \n__AUTH_CONST                      3543K      142 \n__DATA                            2123K      137 \n__DATA_CONST                      4341K      144 \n__DATA_DIRTY                       361K       58 \n__LINKEDIT                       767.3M        2 \n__OBJC_CONST                       289K       36 \n__OBJC_RO                         65.4M        1 \n__OBJC_RW                         1986K        1 \n__TEXT                           103.2M      151 \ndyld private memory                256K        1 \nmapped file                         64K        1 \nshared memory                       32K        2 \n===========                     =======  ======= \nTOTAL                              4.6G      826 \nTOTAL, minus reserved VM space     3.5G      826 \n",
  "legacyInfo" : {
  "threadTriggered" : {

  }
},
  "trialInfo" : {
  "rollouts" : [
    {
      "rolloutId" : "610d52e1fc54bc3389840408",
      "factorPackIds" : {
        "SIRI_UNDERSTANDING_ASR_ASSISTANT" : "63c7a8807b814a4e084bc5d3",
        "SIRI_UNDERSTANDING_MORPHUN" : "62ec7220c682040ba94e6a20"
      },
      "deploymentId" : 240000602
    },
    {
      "rolloutId" : "60f8ddccefea4203d95cbeef",
      "factorPackIds" : {

      },
      "deploymentId" : 240000021
    }
  ],
  "experiments" : [

  ]
}
}
```



# Discussion History
## xmrig | 2023-02-02T14:33:32+00:00
[xmrig-6.19.0-macos-arm64.tar.gz](https://github.com/xmrig/xmrig/releases/download/v6.19.0/xmrig-6.19.0-macos-arm64.tar.gz) replaced, please redownload.
Unfortunately the only known way to use the miner on ARM macOS Ventura is to build it on macOS Big Sur. Source of this bug/incompatibility not yet discovered.
Thank you.

## footcow | 2023-02-02T14:41:45+00:00
Works well with this new release. Thanks

## SChernykh | 2023-10-19T16:18:22+00:00
Fixed in #3346

# Action History
- Created by: footcow | 2023-02-02T07:57:56+00:00
- Closed at: 2023-02-02T14:41:45+00:00
