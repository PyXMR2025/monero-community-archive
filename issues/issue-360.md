---
title: 'MUSL: static builds segfault'
source_url: https://github.com/Cuprate/cuprate/issues/360
author: Naia-love
assignees: []
labels:
- C-bug
created_at: '2024-12-26T02:36:51+00:00'
updated_at: '2024-12-26T13:07:24+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
<!--
Notes:
- All these fields are optional, add as much or as little info as you like
- Please search to see if an issue already exists for the bug you encountered
-->

## Environment
- OS: VoidLinux (musl)
- Cuprate: init branch (last commit is ed822eb as of testing this)

## Bug
When building for musl, rust will default to make the executable static.
Or at least try to here, (according to ldd it is not fully static, but it lack a .INTERP header, so buggy stuff).
running the static cuprated will result in a basicaly instant segfault.
While building with `RUSTFLAGS="-Ctarget-feature=-crt-static"` (which actively tell rust to not build the target as static) will make the executable work.

## Expected behavior
There are case where building fully static is not possible, this is to be researched here. If that the case here, make so cargo build use the appropriate feature to disable static build.
Imo the best case is being able to build a full static executable, as it would make distributing the executable even easier (it can run anywhere :D)
Also, at least according to the backrace, it appear to be linked to randomx (?), or I was able to build and run fully static benchmark ,codegen and test randomx executable.

## Steps to reproduce
1. build on musl
2. try to run the cuprated

## Log
```
./target/debug/cuprated                                   
[1]    29964 segmentation fault (core dumped)  ./target/debug/cuprated
```

backtrace on said core give
```
#0  0x0000000000061046 in ?? ()
#1  0x00007f9d467d67a7 in void std::vector<randomx::MacroOp, std::allocator<randomx::MacroOp> >::_M_realloc_insert<randomx::MacroOp>(__gnu_cxx::__normal_iterator<randomx::MacroOp*, std::vector<randomx::MacroOp, std::allocator<randomx::MacroOp> > >, randomx::MacroOp&&) ()
#2  0x00007f9d467d69f1 in randomx::SuperscalarInstructionInfo::SuperscalarInstructionInfo(char const*, randomx::SuperscalarInstructionType, randomx::MacroOp const&, int) ()
#3  0x00007f9d46484ed7 in _GLOBAL__sub_I_superscalar.cpp ()
#4  0x00007f9d468cfd61 in libc_start_init ()
    at ../src_musl/src/env/__libc_start_main.c:64
#5  0x00007f9d468cfd86 in libc_start_main_stage2 ()
    at ../src_musl/src/env/__libc_start_main.c:92
#6  0x00007f9d464853f8 in _start ()
```


# Discussion History
## Naia-love | 2024-12-26T12:27:05+00:00
messing around with https://github.com/Cuprate/randomx-rs 's build.rs, in particular just trying to static link stdc++ for the case linux, I was able to make cuprated fully static run. And confirmed I was able to run it on a glibc distro after moving what I built on it.
I just have to make proper check to only link stdc++ statically for the case musl (as its harcoded for my tests) and I could make a pr. 

## SyntheticBird45 | 2024-12-26T13:07:23+00:00
You are an angel

# Action History
- Created by: Naia-love | 2024-12-26T02:36:51+00:00
