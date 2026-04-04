---
title: Not synching on Mac
source_url: https://github.com/monero-project/monero-gui/issues/4380
author: cmyk
assignees: []
labels: []
created_at: '2024-12-07T14:24:26+00:00'
updated_at: '2025-01-27T18:06:27+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I installed the Monero Wallet GUI (0.18.3.4) on my M1 MacBook 7 days ago. I started to sync the blockchain to an attached 4TB SSD. It is not going anywhere. Daemon blocks remaining is still above 3M!
At the same time I installed the Wallet on my Raspi 5 and it downloaded the blockchain in 2days.
What can I do to fix this on Mac?

# Discussion History
## cmyk | 2024-12-07T15:57:54+00:00
> #2187 check this for you issue. If it helps

It does not help. I didn’t build it. I downloaded the package. 

## selsta | 2024-12-07T17:33:48+00:00
Seems there is a scam bot attack on our github issues page in the past days...

Regarding your issue, syncing to the internal SSD should be a lot faster. Maybe you can try that and then copy the blockchain to the external drive. Also did you make sure to use the arm64 version?

## cmyk | 2024-12-07T19:07:36+00:00
Yes, I have the ARM version. The drive speed is not the issue.
It's literally stuck at this:
![Screenshot 2024-12-07 at 20 02 40](https://github.com/user-attachments/assets/eb2b714f-9e4e-4c0c-80e7-6c944d75b81e)



## cmyk | 2024-12-07T21:59:29+00:00
I tried again on the local drive after clearing 110GB. Now it's already half way through.
I don't understand. The external SSD writes at 750mb/s my internet connection is 50Mbps.

## selsta | 2024-12-07T23:42:42+00:00
It's not clear what is going on, using an external SSD should also work although it's slower.

## BaksiLi | 2024-12-12T02:17:11+00:00
I use an external SSD and it worked.

Maybe try to start monerod in CLI and connect it in the wallet as a remote node?
<img width="629" alt="Screenshot 2024-12-12 at 10 16 58" src="https://github.com/user-attachments/assets/94f0bf0b-b799-496c-aa87-b7c631cdd8f9" />


## geegee2221 | 2025-01-27T18:06:21+00:00
having this same issue with mac using a local node

## geegee2221 | 2025-01-27T18:06:26+00:00
-----------------------------------
Translated Report (Full Report Below)
-------------------------------------

Process:               monerod [7264]
Path:                  /Users/USER/Desktop/monero-wallet-gui.app/Contents/MacOS/monerod
Identifier:            monerod
Version:               ???
Code Type:             X86-64 (Native)
Parent Process:        launchd [1]
Responsible:           monero-wallet-gui [6741]
User ID:               501

Date/Time:             2025-01-27 13:00:01.6785 -0500
OS Version:            macOS 15.1.1 (24B91)
Report Version:        12
Bridge OS Version:     9.1 (22P1072)
Anonymous UUID:        7AE97A48-D19B-82BD-1279-1F754F21AE07

Sleep/Wake UUID:       D350432D-36AC-4450-9388-67D8495E4C45

Time Awake Since Boot: 4700 seconds
Time Since Wake:       643 seconds

System Integrity Protection: enabled

Crashed Thread:        0  Dispatch queue: com.apple.main-thread

Exception Type:        EXC_BAD_ACCESS (SIGBUS)
Exception Codes:        FS pagein error: 22 Invalid argument
Exception Codes:       0x000000000000000a, 0x00000036ffe6600a

Termination Reason:    Namespace SIGNAL, Code 10 Bus error: 10
Terminating Process:   exc handler [7264]

VM Region Info: 0x36ffe6600a is in 0x10f155000-0x3d3bf76000;  bytes after start: 231673499658  bytes before end: 26777550837
      REGION TYPE                    START - END         [ VSIZE] PRT/MAX SHRMOD  REGION DETAIL
      mapped file                 10f153000-10f155000    [    8K] rw-/rw- SM=PRV  Object_id=cd9ccb69
--->  mapped file                 10f155000-3d3bf76000   [240.7G] r--/rw- SM=PRV  Object_id=36dafcea
      GAP OF 0x5fc2c408a000 BYTES
      MALLOC_NANO              600000000000-600020000000 [512.0M] rw-/rwx SM=PRV  

Application Specific Information:
crashed on child side of fork pre-exec


Kernel Triage:
CL - (arg = 0x0) cluster_pagein past EOF
VM - (arg = 0x1900000016) Filesystem pagein returned an error in vnode_pagein
VM - (arg = 0x0) Page has error bit set


Thread 0 Crashed::  Dispatch queue: com.apple.main-thread
0   monerod                       	       0x10e01a4e1 mdb_page_search_root + 33
1   monerod                       	       0x10e019d9c mdb_page_search + 620
2   monerod                       	       0x10e013a74 mdb_cursor_first + 68
3   monerod                       	       0x10e012802 mdb_cursor_get + 242
4   monerod                       	       0x10e014697 mdb_page_alloc + 647
5   monerod                       	       0x10e01a164 mdb_page_touch + 100
6   monerod                       	       0x10e013e78 mdb_cursor_touch + 72
7   monerod                       	       0x10e01084c mdb_cursor_put + 668
8   monerod                       	       0x10e019419 mdb_dbi_open + 1337
9   monerod                       	       0x10dc5074a (anonymous namespace)::lmdb_db_open(MDB_txn*, char const*, int, unsigned int&, std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char>> const&) + 42
10  monerod                       	       0x10dc4d392 cryptonote::BlockchainLMDB::open(std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char>> const&, int) + 7586
11  monerod                       	       0x10dd3dd34 cryptonote::core::init(boost::program_options::variables_map const&, cryptonote::test_options const*, std::__1::function<epee::span<unsigned char const> const (cryptonote::network_type)> const&, bool) + 6900
12  monerod                       	       0x10d80ff48 daemonize::t_core::t_core(boost::program_options::variables_map const&) + 1304
13  monerod                       	       0x10d80d125 daemonize::t_internals::t_internals(boost::program_options::variables_map const&) + 101
14  monerod                       	       0x10d809d80 daemonize::t_daemon::t_daemon(boost::program_options::variables_map const&, unsigned short) + 48
15  monerod                       	       0x10d8a8856 daemonize::t_executor::create_daemon(boost::program_options::variables_map const&) + 774
16  monerod                       	       0x10d8aedfa bool daemonizer::daemonize<daemonize::t_executor>(int, char const**, daemonize::t_executor&&, boost::program_options::variables_map const&) + 458
17  monerod                       	       0x10d8ab602 main + 7698
18  dyld                          	    0x7ff8114e32cd start + 1805


Thread 0 crashed with X86 Thread State (64-bit):
  rax: 0x0000000000000000  rbx: 0x00000036ffe66000  rcx: 0x0000000000001000  rdx: 0x0000000000000004
  rdi: 0x00007ff7b27267a8  rsi: 0x0000000000000000  rbp: 0x00007ff7b2726510  rsp: 0x00007ff7b27264c0
   r8: 0x000000010e013a30   r9: 0x0000000000000000  r10: 0x0000000000000000  r11: 0x00007fae43020e2a
  r12: 0x00007ff7b27267a8  r13: 0x00007ff7b27267a8  r14: 0x0000000000000000  r15: 0x0000000000000004
  rip: 0x000000010e01a4e1  rfl: 0x0000000000010206  cr2: 0x00000036ffe6600a
  
Logical CPU:     2
Error Code:      0x00000004 (no mapping for user data read)
Trap Number:     14

Thread 0 instruction stream:
  8b 45 d0 80 48 7c 02 4c-89 65 c8 b8 0c 00 00 00  .E..H|.L.e......
  e9 bf fd ff ff 4c 89 65-c8 48 8b 4d c0 48 89 df  .....L.e.H.M.H..
  48 8b 5d d0 e9 e8 fd ff-ff 49 8b 47 28 48 89 70  H.]......I.G(H.p
  28 e9 ec fd ff ff 31 c0-e9 97 fd ff ff 66 90 55  (.....1......f.U
  48 89 e5 41 57 41 56 41-55 41 54 53 48 83 ec 28  H..AWAVAUATSH..(
  48 89 75 b8 49 89 fd 0f-b7 47 42 48 8b 5c c7 48  H.u.I....GBH.\.H
 [0f]b7 4b 0a f6 c1 01 0f-84 1f 02 00 00 41 89 d6  ..K..........A..	<==
  89 55 d4 41 f6 c6 0c 75-23 eb 34 0f 1f 40 00 41  .U.A...u#.4..@.A
  0f b7 45 42 49 8b 5c c5-48 0f b7 4b 0a f6 c1 01  ..EBI.\.H..K....
  0f 84 f6 01 00 00 41 f6-c6 0c 74 13 41 f6 c6 08  ......A...t.A...
  75 4d 31 c9 e9 c6 00 00-00 66 0f 1f 44 00 00 4c  uM1......f..D..L
  89 ef 48 8b 75 b8 48 8d-55 c0 e8 80 f9 ff ff 48  ..H.u.H.U......H

Binary Images:
       0x10d7d7000 -        0x10e953fff monerod (*) <bcce924b-c293-3748-b8e5-b03dc014f5a6> /Users/USER/Desktop/monero-wallet-gui.app/Contents/MacOS/monerod
    0x7ff8114dd000 -     0x7ff811569347 dyld (*) <4d52bd1e-6a0e-31db-b564-9e2029fdcd6f> /usr/lib/dyld
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
ReadOnly portion of Libraries: Total=487.5M resident=0K(0%) swapped_out_or_unallocated=487.5M(100%)
Writable regions: Total=931.8M written=0K(0%) resident=0K(0%) swapped_out=0K(0%) unallocated=931.8M(100%)

                                VIRTUAL   REGION 
REGION TYPE                        SIZE    COUNT (non-coalesced) 
===========                     =======  ======= 
Kernel Alloc Once                    8K        1 
MALLOC                           923.2M       18 
MALLOC guard page                   24K        6 
STACK GUARD                       56.0M        1 
Stack                             8192K        1 
__DATA                            6876K      335 
__DATA_CONST                      30.3M      353 
__DATA_DIRTY                       637K      111 
__FONT_DATA                        2352        1 
__LINKEDIT                       188.4M        2 
__OBJC_RO                         76.3M        1 
__OBJC_RW                         2355K        2 
__TEXT                           299.1M      362 
__TPRO_CONST                       272K        2 
mapped file                      240.7G        2 
shared memory                       32K        4 
===========                     =======  ======= 
TOTAL                            242.3G     1202 



-----------
Full Report
-----------

{"app_name":"monerod","timestamp":"2025-01-27 13:00:07.00 -0500","app_version":"","slice_uuid":"bcce924b-c293-3748-b8e5-b03dc014f5a6","build_version":"","platform":1,"share_with_app_devs":0,"is_first_party":1,"bug_type":"309","os_version":"macOS 15.1.1 (24B91)","roots_installed":0,"incident_id":"A4F21F7F-69A5-49F4-AAC0-B6595F5C5D55","name":"monerod"}
{
  "uptime" : 4700,
  "procRole" : "Unspecified",
  "version" : 2,
  "userID" : 501,
  "deployVersion" : 210,
  "modelCode" : "MacBookPro16,4",
  "coalitionID" : 881,
  "osVersion" : {
    "train" : "macOS 15.1.1",
    "build" : "24B91",
    "releaseType" : "User"
  },
  "captureTime" : "2025-01-27 13:00:01.6785 -0500",
  "codeSigningMonitor" : 0,
  "incident" : "A4F21F7F-69A5-49F4-AAC0-B6595F5C5D55",
  "pid" : 7264,
  "cpuType" : "X86-64",
  "roots_installed" : 0,
  "bug_type" : "309",
  "procLaunch" : "2025-01-27 13:00:01.6758 -0500",
  "procStartAbsTime" : 4777690916370,
  "procExitAbsTime" : 4777693392190,
  "procName" : "monerod",
  "procPath" : "\/Users\/USER\/Desktop\/monero-wallet-gui.app\/Contents\/MacOS\/monerod",
  "parentProc" : "launchd",
  "parentPid" : 1,
  "coalitionName" : "org.monero-project.monero-wallet-gui",
  "crashReporterKey" : "7AE97A48-D19B-82BD-1279-1F754F21AE07",
  "responsiblePid" : 6741,
  "responsibleProc" : "monero-wallet-gui",
  "codeSigningID" : "monerod",
  "codeSigningTeamID" : "R6LK4Q3MJT",
  "codeSigningFlags" : 570499089,
  "codeSigningValidationCategory" : 6,
  "codeSigningTrustLevel" : 4294967295,
  "bootSessionUUID" : "DFA4211C-85C8-4EF9-9146-F0728292257B",
  "wakeTime" : 643,
  "bridgeVersion" : {"build":"22P1072","train":"9.1"},
  "sleepWakeUUID" : "D350432D-36AC-4450-9388-67D8495E4C45",
  "sip" : "enabled",
  "vmRegionInfo" : "0x36ffe6600a is in 0x10f155000-0x3d3bf76000;  bytes after start: 231673499658  bytes before end: 26777550837\n      REGION TYPE                    START - END         [ VSIZE] PRT\/MAX SHRMOD  REGION DETAIL\n      mapped file                 10f153000-10f155000    [    8K] rw-\/rw- SM=PRV  Object_id=cd9ccb69\n--->  mapped file                 10f155000-3d3bf76000   [240.7G] r--\/rw- SM=PRV  Object_id=36dafcea\n      GAP OF 0x5fc2c408a000 BYTES\n      MALLOC_NANO              600000000000-600020000000 [512.0M] rw-\/rwx SM=PRV  ",
  "exception" : {"codes":"0x000000000000000a, 0x00000036ffe6600a","rawCodes":[10,236221521930],"type":"EXC_BAD_ACCESS","signal":"SIGBUS","subtype":" FS pagein error: 22 Invalid argument"},
  "termination" : {"flags":0,"code":10,"namespace":"SIGNAL","indicator":"Bus error: 10","byProc":"exc handler","byPid":7264},
  "ktriageinfo" : "CL - (arg = 0x0) cluster_pagein past EOF\nVM - (arg = 0x1900000016) Filesystem pagein returned an error in vnode_pagein\nVM - (arg = 0x0) Page has error bit set\n",
  "vmregioninfo" : "0x36ffe6600a is in 0x10f155000-0x3d3bf76000;  bytes after start: 231673499658  bytes before end: 26777550837\n      REGION TYPE                    START - END         [ VSIZE] PRT\/MAX SHRMOD  REGION DETAIL\n      mapped file                 10f153000-10f155000    [    8K] rw-\/rw- SM=PRV  Object_id=cd9ccb69\n--->  mapped file                 10f155000-3d3bf76000   [240.7G] r--\/rw- SM=PRV  Object_id=36dafcea\n      GAP OF 0x5fc2c408a000 BYTES\n      MALLOC_NANO              600000000000-600020000000 [512.0M] rw-\/rwx SM=PRV  ",
  "asi" : {"libsystem_c.dylib":["crashed on child side of fork pre-exec"]},
  "extMods" : {"caller":{"thread_create":0,"thread_set_state":0,"task_for_pid":0},"system":{"thread_create":0,"thread_set_state":0,"task_for_pid":0},"targeted":{"thread_create":0,"thread_set_state":0,"task_for_pid":0},"warnings":0},
  "faultingThread" : 0,
  "threads" : [{"triggered":true,"id":113583,"instructionState":{"instructionStream":{"bytes":[139,69,208,128,72,124,2,76,137,101,200,184,12,0,0,0,233,191,253,255,255,76,137,101,200,72,139,77,192,72,137,223,72,139,93,208,233,232,253,255,255,73,139,71,40,72,137,112,40,233,236,253,255,255,49,192,233,151,253,255,255,102,144,85,72,137,229,65,87,65,86,65,85,65,84,83,72,131,236,40,72,137,117,184,73,137,253,15,183,71,66,72,139,92,199,72,15,183,75,10,246,193,1,15,132,31,2,0,0,65,137,214,137,85,212,65,246,198,12,117,35,235,52,15,31,64,0,65,15,183,69,66,73,139,92,197,72,15,183,75,10,246,193,1,15,132,246,1,0,0,65,246,198,12,116,19,65,246,198,8,117,77,49,201,233,198,0,0,0,102,15,31,68,0,0,76,137,239,72,139,117,184,72,141,85,192,232,128,249,255,255,72],"offset":96}},"threadState":{"r13":{"value":140701827491752},"rax":{"value":0},"rflags":{"value":66054},"cpu":{"value":2},"r14":{"value":0},"rsi":{"value":0},"r8":{"value":4529928752,"symbolLocation":0,"symbol":"mdb_cursor_first"},"cr2":{"value":236221521930},"rdx":{"value":4},"r10":{"value":0},"r9":{"value":0},"r15":{"value":4},"rbx":{"value":236221521920},"trap":{"value":14,"description":"(no mapping for user data read)"},"err":{"value":4},"r11":{"value":140386425245226},"rip":{"value":4529956065,"matchesCrashFrame":1},"rbp":{"value":140701827491088},"rsp":{"value":140701827491008},"r12":{"value":140701827491752},"rcx":{"value":4096},"flavor":"x86_THREAD_STATE","rdi":{"value":140701827491752}},"queue":"com.apple.main-thread","frames":[{"imageOffset":8664289,"symbol":"mdb_page_search_root","symbolLocation":33,"imageIndex":0},{"imageOffset":8662428,"symbol":"mdb_page_search","symbolLocation":620,"imageIndex":0},{"imageOffset":8637044,"symbol":"mdb_cursor_first","symbolLocation":68,"imageIndex":0},{"imageOffset":8632322,"symbol":"mdb_cursor_get","symbolLocation":242,"imageIndex":0},{"imageOffset":8640151,"symbol":"mdb_page_alloc","symbolLocation":647,"imageIndex":0},{"imageOffset":8663396,"symbol":"mdb_page_touch","symbolLocation":100,"imageIndex":0},{"imageOffset":8638072,"symbol":"mdb_cursor_touch","symbolLocation":72,"imageIndex":0},{"imageOffset":8624204,"symbol":"mdb_cursor_put","symbolLocation":668,"imageIndex":0},{"imageOffset":8659993,"symbol":"mdb_dbi_open","symbolLocation":1337,"imageIndex":0},{"imageOffset":4691786,"symbol":"(anonymous namespace)::lmdb_db_open(MDB_txn*, char const*, int, unsigned int&, std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char>> const&)","symbolLocation":42,"imageIndex":0},{"imageOffset":4678546,"symbol":"cryptonote::BlockchainLMDB::open(std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char>> const&, int)","symbolLocation":7586,"imageIndex":0},{"imageOffset":5664052,"symbol":"cryptonote::core::init(boost::program_options::variables_map const&, cryptonote::test_options const*, std::__1::function<epee::span<unsigned char const> const (cryptonote::network_type)> const&, bool)","symbolLocation":6900,"imageIndex":0},{"imageOffset":233288,"symbol":"daemonize::t_core::t_core(boost::program_options::variables_map const&)","symbolLocation":1304,"imageIndex":0},{"imageOffset":221477,"symbol":"daemonize::t_internals::t_internals(boost::program_options::variables_map const&)","symbolLocation":101,"imageIndex":0},{"imageOffset":208256,"symbol":"daemonize::t_daemon::t_daemon(boost::program_options::variables_map const&, unsigned short)","symbolLocation":48,"imageIndex":0},{"imageOffset":858198,"symbol":"daemonize::t_executor::create_daemon(boost::program_options::variables_map const&)","symbolLocation":774,"imageIndex":0},{"imageOffset":884218,"symbol":"bool daemonizer::daemonize<daemonize::t_executor>(int, char const**, daemonize::t_executor&&, boost::program_options::variables_map const&)","symbolLocation":458,"imageIndex":0},{"imageOffset":869890,"symbol":"main","symbolLocation":7698,"imageIndex":0},{"imageOffset":25293,"symbol":"start","symbolLocation":1805,"imageIndex":1}]}],
  "usedImages" : [
  {
    "source" : "P",
    "arch" : "x86_64",
    "base" : 4521291776,
    "size" : 18337792,
    "uuid" : "bcce924b-c293-3748-b8e5-b03dc014f5a6",
    "path" : "\/Users\/USER\/Desktop\/monero-wallet-gui.app\/Contents\/MacOS\/monerod",
    "name" : "monerod"
  },
  {
    "source" : "P",
    "arch" : "x86_64",
    "base" : 140703418929152,
    "size" : 574280,
    "uuid" : "4d52bd1e-6a0e-31db-b564-9e2029fdcd6f",
    "path" : "\/usr\/lib\/dyld",
    "name" : "dyld"
  },
  {
    "size" : 0,
    "source" : "A",
    "base" : 0,
    "uuid" : "00000000-0000-0000-0000-000000000000"
  }
],
  "sharedCache" : {
  "base" : 140703418179584,
  "size" : 25769803776,
  "uuid" : "a2941340-823d-37e8-adb9-80f4b2cc5f55"
},
  "vmSummary" : "ReadOnly portion of Libraries: Total=487.5M resident=0K(0%) swapped_out_or_unallocated=487.5M(100%)\nWritable regions: Total=931.8M written=0K(0%) resident=0K(0%) swapped_out=0K(0%) unallocated=931.8M(100%)\n\n                                VIRTUAL   REGION \nREGION TYPE                        SIZE    COUNT (non-coalesced) \n===========                     =======  ======= \nKernel Alloc Once                    8K        1 \nMALLOC                           923.2M       18 \nMALLOC guard page                   24K        6 \nSTACK GUARD                       56.0M        1 \nStack                             8192K        1 \n__DATA                            6876K      335 \n__DATA_CONST                      30.3M      353 \n__DATA_DIRTY                       637K      111 \n__FONT_DATA                        2352        1 \n__LINKEDIT                       188.4M        2 \n__OBJC_RO                         76.3M        1 \n__OBJC_RW                         2355K        2 \n__TEXT                           299.1M      362 \n__TPRO_CONST                       272K        2 \nmapped file                      240.7G        2 \nshared memory                       32K        4 \n===========                     =======  ======= \nTOTAL                            242.3G     1202 \n",
  "legacyInfo" : {
  "threadTriggered" : {
    "queue" : "com.apple.main-thread"
  }
},
  "logWritingSignature" : "fb469fe4c6a31c2d126856df2b8bbf1d4e5e8ba3",
  "trialInfo" : {
  "rollouts" : [
    {
      "rolloutId" : "6297d96be2c9387df974efa4",
      "factorPackIds" : {

      },
      "deploymentId" : 240000032
    },
    {
      "rolloutId" : "5fb4245a1bbfe8005e33a1e1",
      "factorPackIds" : {

      },
      "deploymentId" : 240000021
    }
  ],
  "experiments" : [

  ]
}
}

Model: MacBookPro16,4, BootROM 2069.40.2.0.0 (iBridge: 22.16.11072.0.0,0), 8 processors, 8-Core Intel Core i9, 2.4 GHz, 64 GB, SMC 
Graphics: Intel UHD Graphics 630, Intel UHD Graphics 630, Built-In
Display: Color LCD, 3072 x 1920 Retina, Main, MirrorOff, Online
Graphics: AMD Radeon Pro 5600M, AMD Radeon Pro 5600M, PCIe, 8 GB
Memory Module: BANK 0/ChannelA-DIMM0, 32 GB, DDR4, 2667 MHz, Micron, MT40A4G8BAF-062E:B
Memory Module: BANK 2/ChannelB-DIMM0, 32 GB, DDR4, 2667 MHz, Micron, MT40A4G8BAF-062E:B
AirPort: spairport_wireless_card_type_wifi (0x14E4, 0x7BF), wl0: Jul 26 2024 22:36:01 version 9.30.514.0.32.5.94 FWID 01-68d7ff80
AirPort: 
Bluetooth: Version (null), 0 services, 0 devices, 0 incoming serial ports
Network Service: Wi-Fi, AirPort, en0
USB Device: USB31Bus
USB Device: Nano X
USB Device: T2Bus
USB Device: composite_device
USB Device: Touch Bar Backlight
USB Device: Touch Bar Display
USB Device: Apple Internal Keyboard / Trackpad
USB Device: Headset
USB Device: Ambient Light Sensor
USB Device: FaceTime HD Camera (Built-in)
USB Device: Apple T2 Controller
Thunderbolt Bus: MacBook Pro, Apple Inc., 63.5
Thunderbolt Bus: MacBook Pro, Apple Inc., 63.5


# Action History
- Created by: cmyk | 2024-12-07T14:24:26+00:00
