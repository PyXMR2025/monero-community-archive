---
title: Monero GUI wallet 0.17.3.0 for mac crashes on startup
source_url: https://github.com/monero-project/monero-gui/issues/3806
author: yossarian82it
assignees: []
labels: []
created_at: '2021-12-15T10:55:50+00:00'
updated_at: '2021-12-15T10:57:46+00:00'
type: issue
status: closed
closed_at: '2021-12-15T10:57:45+00:00'
---

# Original Description
Hello,
I just downloaded the latest version of Gui wallet for mac and I replaced the old version with the newest one, as I do for every version.
Unfortunately when as soon as I open the new wallet, it crashes and it gives me this error:

-------------------------------------
Translated Report (Full Report Below)
-------------------------------------

Process:               monero-wallet-gui [5657]
Path:                  /Applications/monero-wallet-gui.app/Contents/MacOS/monero-wallet-gui
Identifier:            org.monero-project.monero-wallet-gui
Version:               0.17.3.0 ()
Code Type:             X86-64 (Translated)
Parent Process:        launchd [1]
User ID:               501

Date/Time:             2021-12-15 11:51:07.5008 +0100
OS Version:            macOS 12.1 (21C52)
Report Version:        12
Anonymous UUID:        5999AE66-78BD-26A6-E27E-9A6D0D36B60D


Time Awake Since Boot: 3100 seconds

System Integrity Protection: enabled

Crashed Thread:        0  Dispatch queue: com.apple.main-thread

Exception Type:        EXC_BAD_INSTRUCTION (SIGILL)
Exception Codes:       0x0000000000000001, 0x0000000000000000
Exception Note:        EXC_CORPSE_NOTIFY

Termination Reason:    Namespace SIGNAL, Code 4 Illegal instruction: 4
Terminating Process:   exc handler [5657]

Kernel Triage:
VM - pmap_enter failed with resource shortage
VM - pmap_enter failed with resource shortage
VM - pmap_enter failed with resource shortage
VM - pmap_enter failed with resource shortage
VM - pmap_enter failed with resource shortage


Thread 0 Crashed::  Dispatch queue: com.apple.main-thread
0   monero-wallet-gui             	       0x100e16097 0x100d1f000 + 1011863
1   dyld                          	       0x202177b49 invocation function for block in dyld4::Loader::findAndRunAllInitializers(dyld4::RuntimeState&) const + 182
2   dyld                          	       0x20219e0ff invocation function for block in dyld3::MachOAnalyzer::forEachInitializer(Diagnostics&, dyld3::MachOAnalyzer::VMAddrConverter const&, void (unsigned int) block_pointer, void const*) const + 129
3   dyld                          	       0x202195893 invocation function for block in dyld3::MachOFile::forEachSection(void (dyld3::MachOFile::SectionInfo const&, bool, bool&) block_pointer) const + 566
4   dyld                          	       0x202164d91 dyld3::MachOFile::forEachLoadCommand(Diagnostics&, void (load_command const*, bool&) block_pointer) const + 129
5   dyld                          	       0x20219561b dyld3::MachOFile::forEachSection(void (dyld3::MachOFile::SectionInfo const&, bool, bool&) block_pointer) const + 179
6   dyld                          	       0x20219db30 dyld3::MachOAnalyzer::forEachInitializerPointerSection(Diagnostics&, void (unsigned int, unsigned int, unsigned char const*, bool&) block_pointer) const + 118
7   dyld                          	       0x20219dda2 dyld3::MachOAnalyzer::forEachInitializer(Diagnostics&, dyld3::MachOAnalyzer::VMAddrConverter const&, void (unsigned int) block_pointer, void const*) const + 386
8   dyld                          	       0x202177a7c dyld4::Loader::findAndRunAllInitializers(dyld4::RuntimeState&) const + 144
9   dyld                          	       0x202177c08 dyld4::Loader::runInitializersBottomUp(dyld4::RuntimeState&, dyld3::Array<dyld4::Loader const*>&) const + 178
10  dyld                          	       0x202177cac dyld4::Loader::runInitializersBottomUpPlusUpwardLinks(dyld4::RuntimeState&) const + 108
11  dyld                          	       0x20218b32e dyld4::APIs::runAllInitializersForMain() + 222
12  dyld                          	       0x202169358 dyld4::prepare(dyld4::APIs&, dyld3::MachOAnalyzer const*) + 3438
13  dyld                          	       0x2021684b4 start + 388

Thread 1:: com.apple.rosetta.exceptionserver
0   runtime                       	    0x7ff7ffc038e4 0x7ff7ffbff000 + 18660
1   runtime                       	    0x7ff7ffc10928 0x7ff7ffbff000 + 71976
2   runtime                       	    0x7ff7ffc120a4 0x7ff7ffbff000 + 77988

Thread 2:
0   runtime                       	    0x7ff7ffc21814 0x7ff7ffbff000 + 141332

Thread 3:
0   runtime                       	    0x7ff7ffc21814 0x7ff7ffbff000 + 141332


Thread 0 crashed with X86 Thread State (64-bit):
  rax: 0x8da74d2d3237005b  rbx: 0x0000000306f36860  rcx: 0x0000000306f39b60  rdx: 0x0000000306f39af0
  rdi: 0x0000000000000001  rsi: 0x0000000306f39ae0  rbp: 0x0000000306f36850  rsp: 0x0000000306f36830
   r8: 0x00007ff84a3a94f0   r9: 0x0000000000000000  r10: 0x00007ff84a3788e0  r11: 0x0000000000000000
  r12: 0x0000000306f36d40  r13: 0x0000000100d1f878  r14: 0x0000000100e16080  r15: 0x000000010ad69060
  rip: 0x0000000100e16097  rfl: 0x0000000000000202
 tmp0: 0x0000000100e16097 tmp1: 0x0511f8c5c057f8c5 tmp2: 0x0005c74800f7a6bd


Binary Images:
       0x100d1f000 -        0x101d1cfff org.monero-project.monero-wallet-gui (0.17.3.0) <aca24bdb-516f-37c2-92a7-89556d26288a> /Applications/monero-wallet-gui.app/Contents/MacOS/monero-wallet-gui
       0x202163000 -        0x2021cefff dyld (*) <cef5a27a-d50b-3020-af03-1734b19bc8c5> /usr/lib/dyld
    0x7ff7ffbff000 -     0x7ff7ffc2efff runtime (*) <21c1e0c9-a36e-3e4b-a12b-1bf54ce4403e> /usr/libexec/rosetta/runtime

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
ReadOnly portion of Libraries: Total=968.5M resident=0K(0%) swapped_out_or_unallocated=968.5M(100%)
Writable regions: Total=704.5M written=0K(0%) resident=0K(0%) swapped_out=0K(0%) unallocated=704.5M(100%)

                                VIRTUAL   REGION 
REGION TYPE                        SIZE    COUNT (non-coalesced) 
===========                     =======  ======= 
Activity Tracing                   256K        1 
Kernel Alloc Once                    8K        1 
MALLOC                           163.1M       16 
MALLOC guard page                   96K        5 
MALLOC_NANO (reserved)           384.0M        1         reserved VM address space (unallocated)
Rosetta Arena                     4096K        2 
Rosetta Generic                    876K      216 
Rosetta IndirectBranch              64K        1 
Rosetta JIT                      128.0M        1 
Rosetta Return Stack                60K        6 
Rosetta Thread Context              60K        6 
STACK GUARD                          8K        2 
Stack                             9240K        3 
Stack Guard                       56.0M        1 
VM_ALLOCATE                       11.0M       20 
VM_ALLOCATE (reserved)              60K        8         reserved VM address space (unallocated)
__DATA                            18.0M      277 
__DATA_CONST                      10.9M      149 
__DATA_DIRTY                       485K       85 
__FONT_DATA                          4K        1 
__LINKEDIT                       710.5M       35 
__OBJC_RO                         81.8M        1 
__OBJC_RW                         3136K        2 
__TEXT                           258.0M      285 
__UNICODE                          588K        1 
dyld private memory               1088K        3 
mapped file                        5.1G      378 
shared memory                       64K        4 
unshared pmap                     2528K        2 
===========                     =======  ======= 
TOTAL                              6.9G     1513 
TOTAL, minus reserved VM space     6.5G     1513 



-----------
Full Report
-----------

{"app_name":"monero-wallet-gui","timestamp":"2021-12-15 11:51:09.00 +0100","app_version":"0.17.3.0","slice_uuid":"aca24bdb-516f-37c2-92a7-89556d26288a","build_version":"","platform":1,"bundleID":"org.monero-project.monero-wallet-gui","share_with_app_devs":0,"is_first_party":0,"bug_type":"309","os_version":"macOS 12.1 (21C52)","incident_id":"FE273283-507C-44D1-A92F-1CD2F4A21A84","name":"monero-wallet-gui"}
{
  "uptime" : 3100,
  "procLaunch" : "2021-12-15 11:51:06.5856 +0100",
  "procRole" : "Background",
  "version" : 2,
  "userID" : 501,
  "deployVersion" : 210,
  "modelCode" : "iMac21,1",
  "procStartAbsTime" : 75278700512,
  "coalitionID" : 4284,
  "osVersion" : {
    "train" : "macOS 12.1",
    "build" : "21C52",
    "releaseType" : "User"
  },
  "captureTime" : "2021-12-15 11:51:07.5008 +0100",
  "incident" : "FE273283-507C-44D1-A92F-1CD2F4A21A84",
  "bug_type" : "309",
  "pid" : 5657,
  "procExitAbsTime" : 75300479975,
  "translated" : true,
  "cpuType" : "X86-64",
  "procName" : "monero-wallet-gui",
  "procPath" : "\/Applications\/monero-wallet-gui.app\/Contents\/MacOS\/monero-wallet-gui",
  "bundleInfo" : {"CFBundleShortVersionString":"0.17.3.0","CFBundleVersion":"","CFBundleIdentifier":"org.monero-project.monero-wallet-gui"},
  "storeInfo" : {"deviceIdentifierForVendor":"F3FDC83F-ECA0-5B22-BBD6-047088B0B701","thirdParty":true},
  "parentProc" : "launchd",
  "parentPid" : 1,
  "coalitionName" : "org.monero-project.monero-wallet-gui",
  "crashReporterKey" : "5999AE66-78BD-26A6-E27E-9A6D0D36B60D",
  "sip" : "enabled",
  "isCorpse" : 1,
  "exception" : {"codes":"0x0000000000000001, 0x0000000000000000","rawCodes":[1,0],"type":"EXC_BAD_INSTRUCTION","signal":"SIGILL"},
  "termination" : {"flags":0,"code":4,"namespace":"SIGNAL","indicator":"Illegal instruction: 4","byProc":"exc handler","byPid":5657},
  "ktriageinfo" : "VM - pmap_enter failed with resource shortage\nVM - pmap_enter failed with resource shortage\nVM - pmap_enter failed with resource shortage\nVM - pmap_enter failed with resource shortage\nVM - pmap_enter failed with resource shortage\n",
  "extMods" : {"caller":{"thread_create":0,"thread_set_state":0,"task_for_pid":0},"system":{"thread_create":0,"thread_set_state":0,"task_for_pid":0},"targeted":{"thread_create":0,"thread_set_state":0,"task_for_pid":0},"warnings":0},
  "faultingThread" : 0,
  "threads" : [{"triggered":true,"id":128007,"threadState":{"r13":{"value":4308727928},"rflags":{"value":514},"rax":{"value":10207211936969850971},"rosetta":{"tmp2":{"value":1626486951356093},"tmp1":{"value":365346573012957381},"tmp0":{"value":4309737623}},"r14":{"value":4309737600},"rsi":{"value":13001530080},"r8":{"value":140704373970160,"symbolLocation":16,"symbol":"dyld4::gDyld"},"rdx":{"value":13001530096},"r10":{"value":140704373770464,"symbolLocation":24,"symbol":"atexit_mutex"},"r9":{"value":0},"r15":{"value":4476801120},"rbx":{"value":13001517152},"r11":{"value":0},"rip":{"value":4309737623},"rbp":{"value":13001517136},"rsp":{"value":13001517104},"r12":{"value":13001518400},"rcx":{"value":13001530208},"flavor":"x86_THREAD_STATE","rdi":{"value":1}},"queue":"com.apple.main-thread","frames":[{"imageOffset":1011863,"imageIndex":0},{"imageOffset":84809,"symbol":"invocation function for block in dyld4::Loader::findAndRunAllInitializers(dyld4::RuntimeState&) const","symbolLocation":182,"imageIndex":1},{"imageOffset":241919,"symbol":"invocation function for block in dyld3::MachOAnalyzer::forEachInitializer(Diagnostics&, dyld3::MachOAnalyzer::VMAddrConverter const&, void (unsigned int) block_pointer, void const*) const","symbolLocation":129,"imageIndex":1},{"imageOffset":206995,"symbol":"invocation function for block in dyld3::MachOFile::forEachSection(void (dyld3::MachOFile::SectionInfo const&, bool, bool&) block_pointer) const","symbolLocation":566,"imageIndex":1},{"imageOffset":7569,"symbol":"dyld3::MachOFile::forEachLoadCommand(Diagnostics&, void (load_command const*, bool&) block_pointer) const","symbolLocation":129,"imageIndex":1},{"imageOffset":206363,"symbol":"dyld3::MachOFile::forEachSection(void (dyld3::MachOFile::SectionInfo const&, bool, bool&) block_pointer) const","symbolLocation":179,"imageIndex":1},{"imageOffset":240432,"symbol":"dyld3::MachOAnalyzer::forEachInitializerPointerSection(Diagnostics&, void (unsigned int, unsigned int, unsigned char const*, bool&) block_pointer) const","symbolLocation":118,"imageIndex":1},{"imageOffset":241058,"symbol":"dyld3::MachOAnalyzer::forEachInitializer(Diagnostics&, dyld3::MachOAnalyzer::VMAddrConverter const&, void (unsigned int) block_pointer, void const*) const","symbolLocation":386,"imageIndex":1},{"imageOffset":84604,"symbol":"dyld4::Loader::findAndRunAllInitializers(dyld4::RuntimeState&) const","symbolLocation":144,"imageIndex":1},{"imageOffset":85000,"symbol":"dyld4::Loader::runInitializersBottomUp(dyld4::RuntimeState&, dyld3::Array<dyld4::Loader const*>&) const","symbolLocation":178,"imageIndex":1},{"imageOffset":85164,"symbol":"dyld4::Loader::runInitializersBottomUpPlusUpwardLinks(dyld4::RuntimeState&) const","symbolLocation":108,"imageIndex":1},{"imageOffset":164654,"symbol":"dyld4::APIs::runAllInitializersForMain()","symbolLocation":222,"imageIndex":1},{"imageOffset":25432,"symbol":"dyld4::prepare(dyld4::APIs&, dyld3::MachOAnalyzer const*)","symbolLocation":3438,"imageIndex":1},{"imageOffset":21684,"symbol":"start","symbolLocation":388,"imageIndex":1}]},{"id":128012,"name":"com.apple.rosetta.exceptionserver","frames":[{"imageOffset":18660,"imageIndex":2},{"imageOffset":71976,"imageIndex":2},{"imageOffset":77988,"imageIndex":2}]},{"id":128046,"frames":[{"imageOffset":141332,"imageIndex":2}]},{"id":128047,"frames":[{"imageOffset":141332,"imageIndex":2}]}],
  "usedImages" : [
  {
    "source" : "P",
    "arch" : "x86_64",
    "base" : 4308725760,
    "CFBundleShortVersionString" : "0.17.3.0",
    "CFBundleIdentifier" : "org.monero-project.monero-wallet-gui",
    "size" : 16769024,
    "uuid" : "aca24bdb-516f-37c2-92a7-89556d26288a",
    "path" : "\/Applications\/monero-wallet-gui.app\/Contents\/MacOS\/monero-wallet-gui",
    "name" : "monero-wallet-gui",
    "CFBundleVersion" : ""
  },
  {
    "source" : "P",
    "arch" : "x86_64",
    "base" : 8624943104,
    "size" : 442368,
    "uuid" : "cef5a27a-d50b-3020-af03-1734b19bc8c5",
    "path" : "\/usr\/lib\/dyld",
    "name" : "dyld"
  },
  {
    "source" : "P",
    "arch" : "arm64",
    "base" : 140703124418560,
    "size" : 196608,
    "uuid" : "21c1e0c9-a36e-3e4b-a12b-1bf54ce4403e",
    "path" : "\/usr\/libexec\/rosetta\/runtime",
    "name" : "runtime"
  }
],
  "sharedCache" : {
  "base" : 140703271911424,
  "size" : 15218081792,
  "uuid" : "e72a2011-6acf-3f25-bfe7-730570330401"
},
  "vmSummary" : "ReadOnly portion of Libraries: Total=968.5M resident=0K(0%) swapped_out_or_unallocated=968.5M(100%)\nWritable regions: Total=704.5M written=0K(0%) resident=0K(0%) swapped_out=0K(0%) unallocated=704.5M(100%)\n\n                                VIRTUAL   REGION \nREGION TYPE                        SIZE    COUNT (non-coalesced) \n===========                     =======  ======= \nActivity Tracing                   256K        1 \nKernel Alloc Once                    8K        1 \nMALLOC                           163.1M       16 \nMALLOC guard page                   96K        5 \nMALLOC_NANO (reserved)           384.0M        1         reserved VM address space (unallocated)\nRosetta Arena                     4096K        2 \nRosetta Generic                    876K      216 \nRosetta IndirectBranch              64K        1 \nRosetta JIT                      128.0M        1 \nRosetta Return Stack                60K        6 \nRosetta Thread Context              60K        6 \nSTACK GUARD                          8K        2 \nStack                             9240K        3 \nStack Guard                       56.0M        1 \nVM_ALLOCATE                       11.0M       20 \nVM_ALLOCATE (reserved)              60K        8         reserved VM address space (unallocated)\n__DATA                            18.0M      277 \n__DATA_CONST                      10.9M      149 \n__DATA_DIRTY                       485K       85 \n__FONT_DATA                          4K        1 \n__LINKEDIT                       710.5M       35 \n__OBJC_RO                         81.8M        1 \n__OBJC_RW                         3136K        2 \n__TEXT                           258.0M      285 \n__UNICODE                          588K        1 \ndyld private memory               1088K        3 \nmapped file                        5.1G      378 \nshared memory                       64K        4 \nunshared pmap                     2528K        2 \n===========                     =======  ======= \nTOTAL                              6.9G     1513 \nTOTAL, minus reserved VM space     6.5G     1513 \n",
  "legacyInfo" : {
  "threadTriggered" : {
    "queue" : "com.apple.main-thread"
  }
},
  "trialInfo" : {
  "rollouts" : [
    {
      "rolloutId" : "607844aa04477260f58a8077",
      "factorPackIds" : {
        "SIRI_MORPHUN_ASSETS" : "6103050cbfe6dc472e1c982a"
      },
      "deploymentId" : 240000066
    },
    {
      "rolloutId" : "60da5e84ab0ca017dace9abf",
      "factorPackIds" : {

      },
      "deploymentId" : 240000008
    },
    {
      "rolloutId" : "602ad4dac86151000cf27e46",
      "factorPackIds" : {
        "SIRI_DICTATION_ASSETS" : "61a80a438feb033580c2778b"
      },
      "deploymentId" : 240000290
    },
    {
      "rolloutId" : "5ffde50ce2aacd000d47a95f",
      "factorPackIds" : {

      },
      "deploymentId" : 240000086
    },
    {
      "rolloutId" : "5fc94383418129005b4e9ae0",
      "factorPackIds" : {

      },
      "deploymentId" : 240000185
    },
    {
      "rolloutId" : "601d9415f79519000ccd4b69",
      "factorPackIds" : {
        "SIRI_TEXT_TO_SPEECH" : "6194416f2171a2330e561f05"
      },
      "deploymentId" : 240000339
    }
  ],
  "experiments" : [

  ]
}
}



# Discussion History
## selsta | 2021-12-15T10:57:45+00:00
Thanks for the report, please see my comment here: https://github.com/monero-project/monero-gui/issues/3782#issuecomment-988287979

The next version will have this issue resolved. In the meantime please continue to use v0.17.2.3 or manually compile v0.17.3.0 from source. Both work.

Closing as a duplicate.

# Action History
- Created by: yossarian82it | 2021-12-15T10:55:50+00:00
- Closed at: 2021-12-15T10:57:45+00:00
