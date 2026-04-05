---
title: 'visual c++ 2015 : MASM : error A2070: invalid instruction operands'
source_url: https://github.com/xmrig/xmrig/issues/768
author: adevelopcr
assignees: []
labels:
- bug
created_at: '2018-10-01T20:03:47+00:00'
updated_at: '2018-10-08T18:53:34+00:00'
type: issue
status: closed
closed_at: '2018-10-08T18:53:34+00:00'
---

# Original Description
I got several of this error during build for x64 release and thus the linker failed at the the end of compilation to link against xmrig-asm.lib

these are some of the errors : 

    1>------ Build started: Project: xmrig-asm, Configuration: Release x64 ------
    1>  Assembling E:\fx\xmrig-project\xmrig-2.8.0\src\crypto\asm\cnv2_main_loop.asm...
    1>MASM : error A2070: invalid instruction operands
    1>MASM : error A2070: invalid instruction operands
    1>MASM : error A2070: invalid instruction operands
    1>MASM : error A2070: invalid instruction operands
    1>MASM : error A2070: invalid instruction operands
    1>MASM : error A2070: invalid instruction operands
    1>MASM : error A2070: invalid instruction operands
    1>MASM : error A2070: invalid instruction operands
    1>MASM : error A2070: invalid instruction operands
    1>MASM : error A2070: invalid instruction operands
    1>MASM : error A2070: invalid instruction operands
    1>MASM : error A2070: invalid instruction operands
    1>MASM : error A2070: invalid instruction operands
    1>MASM : error A2070: invalid instruction operands
    1>MASM : error A2070: invalid instruction operands
    1>MASM : error A2070: invalid instruction operands
    1>MASM : error A2070: invalid instruction operands
    1>MASM : error A2070: invalid instruction operands
    1>MASM : error A2070: invalid instruction operands
    1>MASM : error A2070: invalid instruction operands
    1>MASM : error A2070: invalid instruction operands
    1>MASM : error A2070: invalid instruction operands
    1>MASM : error A2070: invalid instruction operands
    1>MASM : error A2070: invalid instruction operands
    1>MASM : error A2070: invalid instruction operands
    1>MASM : error A2070: invalid instruction operands
    1>MASM : error A2070: invalid instruction operands
    1>MASM : error A2070: invalid instruction operands
    1>MASM : error A2070: invalid instruction operands
    1>MASM : error A2070: invalid instruction operands
    1>MASM : error A2070: invalid instruction operands
    1>MASM : error A2070: invalid instruction operands
    1>MASM : error A2070: invalid instruction operands
    1>MASM : error A2070: invalid instruction operands
    1>MASM : error A2150: word register cannot be first operand
    1>MASM : error A2070: invalid instruction operands
    1>MASM : error A2070: invalid instruction operands
    1>MASM : error A2150: word register cannot be first operand
    1>MASM : error A2150: word register cannot be first operand
    1>MASM : error A2150: word register cannot be first operand
    1>6) : fatal error A1012: error count exceeds 100; stopping assembly

    2>LINK : fatal error LNK1181: cannot open input file 'Release\xmrig-asm.lib'

# Discussion History
## adevelopcr | 2018-10-01T20:32:27+00:00
I built it successfully with mingw-w64 but it doesn't build with visual studio 2015
what happened ! have anything changed in 2.8 release or should I do anything special ?

## adevelopcr | 2018-10-01T20:47:52+00:00
I checked the old releases and it didn't have the asm folder or the asm files and didn't use the assembler
so is the new version incompatible with visual studio 2015 ?

## adevelopcr | 2018-10-01T20:55:03+00:00
@xmrig 

## xmrig | 2018-10-01T20:58:15+00:00
I will check it tomorrow, likely need add some workarounds for MSVC 2015. asm code successfully compiled with MSVC 2017.

## adevelopcr | 2018-10-02T13:48:28+00:00
Can I build with option WITH_ASM=OFF

## adevelopcr | 2018-10-02T14:06:48+00:00
yes it built but I think I'll lose some performance , am I right ?

## xmrig | 2018-10-02T14:53:53+00:00
Fixed in [dev](https://github.com/xmrig/xmrig/commits/dev) branch.
Your are right, without ASM you lose performance for `cn/2` with single and double modes. More about `asm` option https://github.com/xmrig/xmrig/issues/753#issuecomment-424243330.
Thank you.

# Action History
- Created by: adevelopcr | 2018-10-01T20:03:47+00:00
- Closed at: 2018-10-08T18:53:34+00:00
