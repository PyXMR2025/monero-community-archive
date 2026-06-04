---
title: Windows GUI binary crashing
source_url: https://github.com/seraphis-migration/monero/issues/376
author: j-berman
assignees: []
labels: []
created_at: '2026-05-12T20:38:07+00:00'
updated_at: '2026-06-02T07:05:08+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
@redsh4de reports the windows GUI binary crashes upon connecting to a node, but not the self-compiled version.

Maybe related to #367

# Discussion History
## redsh4de | 2026-06-01T21:40:10+00:00
WinDbg `!analyze -v` output from a procdump capture of the v2.0 release binary
```
*******************************************************************************
*                                                                             *
*                        Exception Analysis                                   *
*                                                                             *
*******************************************************************************


KEY_VALUES_STRING: 1

    Key  : AV.Type
    Value: Read

    Key  : Analysis.CPU.mSec
    Value: 1453

    Key  : Analysis.Elapsed.mSec
    Value: 17370

    Key  : Analysis.IO.Other.Mb
    Value: 15

    Key  : Analysis.IO.Read.Mb
    Value: 386

    Key  : Analysis.IO.Write.Mb
    Value: 142

    Key  : Analysis.Init.CPU.mSec
    Value: 8656

    Key  : Analysis.Init.Elapsed.mSec
    Value: 220486

    Key  : Analysis.Memory.CommitPeak.Mb
    Value: 205

    Key  : Analysis.Version.DbgEng
    Value: 10.0.29547.1002

    Key  : Analysis.Version.Description
    Value: 10.2602.27.2 amd64fre

    Key  : Analysis.Version.Ext
    Value: 1.2602.27.2

    Key  : Failure.Bucket
    Value: INVALID_POINTER_READ_c0000005_monero-wallet-gui.exe!Unknown

    Key  : Failure.Exception.Code
    Value: 0xc0000005

    Key  : Failure.Exception.IP.Address
    Value: 0x7ff719493489

    Key  : Failure.Exception.IP.Module
    Value: monero_wallet_gui

    Key  : Failure.Exception.IP.Offset
    Value: 0xbc3489

    Key  : Failure.Hash
    Value: {248e52a1-581a-b921-2423-ff898c192306}

    Key  : Failure.ProblemClass.Primary
    Value: INVALID_POINTER_READ

    Key  : Faulting.IP.Type
    Value: Paged

    Key  : Timeline.OS.Boot.DeltaSec
    Value: 8979

    Key  : Timeline.Process.Start.DeltaSec
    Value: 26

    Key  : WER.OS.Branch
    Value: vb_release

    Key  : WER.OS.Version
    Value: 10.0.19041.1


FILE_IN_CAB:  crashdump.dmp

COMMENT:  
*** procdump  -ma -e -w monero-wallet-gui.exe C:\Users\user\crashdump.dmp
*** Unhandled exception: C0000005.ACCESS_VIOLATION

NTGLOBALFLAG:  0

APPLICATION_VERIFIER_FLAGS:  0

CONTEXT:  (.ecxr)
rax=00007ff71bbabb50 rbx=0000000000000030 rcx=0000000000000030
rdx=0000000000000000 rsi=000002657a14be78 rdi=00000265093ccd60
rip=00007ff719493489 rsp=000000a664ffe6a0 rbp=000002657a14bf90
 r8=00000000000006cc  r9=0000000000000040 r10=00000000000006c0
r11=c0000009000000e0 r12=00007ff71d980540 r13=000002656eae8170
r14=000000a664ffece0 r15=00000265094cc200
iopl=0         nv up ei pl nz na pe nc
cs=0033  ss=002b  ds=002b  es=002b  fs=0053  gs=002b             efl=00010204
monero_wallet_gui+0xbc3489:
00007ff7`19493489 488b4908        mov     rcx,qword ptr [rcx+8] ds:00000000`00000038=????????????????
Resetting default scope

EXCEPTION_RECORD:  (.exr -1)
ExceptionAddress: 00007ff719493489 (monero_wallet_gui+0x0000000000bc3489)
   ExceptionCode: c0000005 (Access violation)
  ExceptionFlags: 00000000
NumberParameters: 2
   Parameter[0]: 0000000000000000
   Parameter[1]: 0000000000000038
Attempt to read from address 0000000000000038

PROCESS_NAME:  monero-wallet-gui.exe

READ_ADDRESS:  0000000000000038 

ERROR_CODE: (NTSTATUS) 0xc0000005 - The instruction at 0x%p referenced memory at 0x%p. The memory could not be %s.

EXCEPTION_CODE_STR:  c0000005

EXCEPTION_PARAMETER1:  0000000000000000

EXCEPTION_PARAMETER2:  0000000000000038

STACK_TEXT:  
000000a6`64ffe6a0 00007ff7`1895ee79     : 00000265`091035d0 00000265`7a14be78 00000000`00000000 000000a6`64ffece0 : monero_wallet_gui+0xbc3489
000000a6`64ffe6e0 00007ff7`189659e8     : 00000000`00000000 0aa66903`6d884390 00000000`00000000 00000265`6e829110 : monero_wallet_gui+0x8ee79
000000a6`64ffe7c0 00007ff7`1aa32f83     : 00000000`00000116 00000000`00000116 00000265`09403a60 00000265`00000000 : monero_wallet_gui+0x959e8
000000a6`64ffec60 00007ff7`1aa35d57     : 00000265`76d748d0 000000a6`000001c3 00000265`091035d0 00000000`00004e20 : monero_wallet_gui+0x2162f83
000000a6`64ffefb0 00007ff7`1b438197     : 00000265`093c2be0 00007ff7`1b499a9c 00000000`00000016 000000a6`64fff4c0 : monero_wallet_gui+0x2165d57
000000a6`64fff340 00007ff7`18b1ad2d     : 000000a6`64fff588 000000a6`64fff5a8 000000a6`64fff4c0 000000a6`64fff4d0 : monero_wallet_gui!ZNK5boost7archive6detail11iserializerINS0_24portable_binary_iarchiveESt6vectorIySaIyEEE16load_object_dataERNS1_14basic_iarchiveEPvj+0x2a2477
000000a6`64fff3b0 00007ff7`189a49eb     : 000000a6`64fff820 000000a6`64fff860 000000a6`64fff8c8 00000000`00000000 : monero_wallet_gui+0x24ad2d
000000a6`64fff680 00007ff7`189a8476     : 000000a6`64fff800 00007ff9`6b409c9c 00000265`0912caa0 000000a6`64fffad0 : monero_wallet_gui+0xd49eb
000000a6`64fff6e0 00007ff7`189bad7c     : 00000265`0912c910 00000265`65000000 00000265`650002b8 00000000`00000050 : monero_wallet_gui+0xd8476
000000a6`64fff720 00007ff7`188f1e51     : 00000265`78392200 00000265`65000000 00000265`650002ac 00000265`651c0000 : monero_wallet_gui+0xead7c
000000a6`64fffa40 00007ff7`188fd42c     : 00000265`65000000 00000265`0946edb0 00000265`09347b10 00000000`00000000 : monero_wallet_gui+0x21e51
000000a6`64fffbb0 00007ff7`1b40a5d6     : 00000000`00000000 000000a6`64fffd40 000000a6`64fffd40 00000000`00000001 : monero_wallet_gui+0x2d42c
000000a6`64fffc60 00007ff7`1a287508     : 00000000`00000010 00000265`7869cd30 00000265`77c5fd20 00000265`77c5fd20 : monero_wallet_gui!ZNK5boost7archive6detail11iserializerINS0_24portable_binary_iarchiveESt6vectorIySaIyEEE16load_object_dataERNS1_14basic_iarchiveEPvj+0x2748b6
000000a6`64fffd00 00007ff7`1a0773dd     : 00000265`785ed150 00000000`00000000 00000000`00000000 00000000`00000000 : monero_wallet_gui+0x19b7508
000000a6`64fffdb0 00007ff9`6c4d7374     : 00000000`00000000 00000000`00000000 00000000`00000000 00000000`00000000 : monero_wallet_gui+0x17a73dd
000000a6`64fffe00 00007ff9`6cddcc91     : 00000000`00000000 00000000`00000000 00000000`00000000 00000000`00000000 : kernel32!BaseThreadInitThunk+0x14
000000a6`64fffe30 00000000`00000000     : 00000000`00000000 00000000`00000000 00000000`00000000 00000000`00000000 : ntdll!RtlUserThreadStart+0x21


STACK_COMMAND: ~9s; .ecxr ; kb

IP_IN_PAGED_CODE: 
monero_wallet_gui+bc3489
00007ff7`19493489 488b4908        mov     rcx,qword ptr [rcx+8]

SYMBOL_NAME:  monero_wallet_gui+bc3489

MODULE_NAME: monero_wallet_gui

IMAGE_NAME:  monero-wallet-gui.exe

FAILURE_BUCKET_ID:  INVALID_POINTER_READ_c0000005_monero-wallet-gui.exe!Unknown

OS_VERSION:  10.0.19041.1

BUILDLAB_STR:  vb_release

OSPLATFORM_TYPE:  x64

OSNAME:  Windows 10

FAILURE_ID_HASH:  {248e52a1-581a-b921-2423-ff898c192306}

Followup:     MachineOwner
---------
```

# Action History
- Created by: j-berman | 2026-05-12T20:38:07+00:00
