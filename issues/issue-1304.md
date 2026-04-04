---
title: Add -fPIC to ARM compile flags
source_url: https://github.com/monero-project/monero/issues/1304
author: ghost
assignees: []
labels: []
created_at: '2016-11-07T16:51:44+00:00'
updated_at: '2016-11-10T22:12:39+00:00'
type: issue
status: closed
closed_at: '2016-11-10T22:12:39+00:00'
---

# Original Description
Noticed this in the compilation log from #1263 on ARMv8

```[ 89%] Linking CXX executable ../../bin/monero-wallet-cli
/usr/bin/ld: /usr/lib/gcc/aarch64-linux-gnu/6/../../../aarch64-linux-gnu/libcrypto.a(armcap.o): relocation R_AARCH64_ADR_PREL_PG_HI21 against external symbol `__stack_chk_guard@@GLIBC_2.17' can not be used when making a shared object; recompile with -fPIC
/usr/bin/ld: /usr/lib/gcc/aarch64-linux-gnu/6/../../../aarch64-linux-gnu/libcrypto.a(armcap.o)(.text.startup+0x4): unresolvable R_AARCH64_ADR_PREL_PG_HI21 relocation against symbol `__stack_chk_guard@@GLIBC_2.17'
/usr/bin/ld: final link failed: Bad value
collect2: error: ld returned 1 exit status
```

Probably good advice from the compiler. Will try to add at some point but please feel free to beat me to it.

# Discussion History
## ghost | 2016-11-07T21:47:23+00:00
Delete lines 411 and 412 from CMakeLists.txt
Check PIC_FLAG actually gets set for ARMv8 (why wouldn't it...)


## ghost | 2016-11-08T21:29:17+00:00
Relevant links:
http://stackoverflow.com/questions/3146744/difference-in-position-independent-code-x86-vs-x86-64
https://www.technovelty.org/c/position-independent-code-and-x86-64-libraries.html

Looks like 64-bit code needs to be compiled with -fPIC in case it gets placed into memory >2GB in size.

This isn't an issue on the current generation of small ARMv8 systems but may arise for the next gen.

We also need to use -fPIC rather than -fpic because the GOT can only be 28k in size on the aarch64 and this allows for future-proofing with some increase in overhead/lookups


# Action History
- Created by: ghost | 2016-11-07T16:51:44+00:00
- Closed at: 2016-11-10T22:12:39+00:00
