---
title: Question about xmrig source code, is it bug in source?
source_url: https://github.com/xmrig/xmrig/issues/3460
author: xcryptodigger
assignees: []
labels:
- bug
created_at: '2024-04-13T12:13:57+00:00'
updated_at: '2024-04-14T17:49:00+00:00'
type: issue
status: closed
closed_at: '2024-04-14T17:35:06+00:00'
---

# Original Description
Can You please help me understand one thing in xmrig sources.
I am debugging sources (purpose is performance improvement) and one thing puzzles very much and probably can be a bug?

Please look at xmrig/src/crypto/randomx/randomx.cpp these lines of code:

```
typedef void(randomx::JitCompilerX86::* InstructionGeneratorX86_2)(const randomx::Instruction&);

#define JIT_HANDLE(x, prev) do { \
		const InstructionGeneratorX86_2 p = &randomx::JitCompilerX86::h_##x; \
		printf("sizeof(p) %d sizeof(engine)/256 %d\n",sizeof(p),sizeof(randomx::JitCompilerX86::engine)/256); \
		memcpy(randomx::JitCompilerX86::engine + k, &p, sizeof(p)); \
	} while (0)

```

You may notice I added  one line of code with printf().
This is because something strange happens with function handlers assignments.
engine is array of type InstructionGeneratorX86 but handler is assigned to InstructionGeneratorX86_2.
Issue is they are different size (and probably mean different things).

Output is:
```
* ABOUT        XMRig/6.21.0 MSVC/2019 (built for Windows x86-64, 64 bit)
 * LIBS         libuv/1.44.2 OpenSSL/1.1.1s hwloc/2.9.0
 * HUGE PAGES   permission granted
 * 1GB PAGES    unavailable
 * CPU          Intel(R) Core(TM) i7-7700HQ CPU @ 2.80GHz (1) 64-bit AES
                L2:1.0 MB L3:6.0 MB 4C/8T NUMA:1
 * MEMORY       9.7/15.9 GB (61%)
                DIMM_A0: 16 GB DDR4 @ 2400 MHz MSI24D4S7D8MB-16
                DIMM_B0: <empty>
 * MOTHERBOARD  Micro-Star International Co., Ltd. - MS-1799
 * DONATE       0%
 * ASSEMBLY     auto:intel
 * POOL #1      benchmark algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled
[2024-04-13 14:38:56.328]  bench    start benchmark hashes 250K algo rx/0
[2024-04-13 14:38:56.329]  cpu      use argon2 implementation AVX2
[2024-04-13 14:38:56.330]  msr      to access MSR registers Administrator privileges required.
[2024-04-13 14:38:56.330]  msr      FAILED TO APPLY MSR MOD, HASHRATE WILL BE LOW
[2024-04-13 14:38:56.330]  randomx  init dataset algo rx/0 (8 threads) seed 0000000000000000...
sizeof(p) 24 sizeof(engine)/256 8
sizeof(p) 24 sizeof(engine)/256 8
sizeof(p) 24 sizeof(engine)/256 8
sizeof(p) 24 sizeof(engine)/256 8
```

So single entry has size 8 bytes but const InstructionGeneratorX86_2 p has size 24 bytes.
I see that bigger struct is copied into smaller struct.
Is it ever correct?
I feel this is issue which may cause xmrig segfaults sometimes because some memory is spoiled after array..

Please, write me if my assumption is correct or not.








# Discussion History
## SChernykh | 2024-04-13T18:27:49+00:00
sizeof(p) is 8, and your code prints `sizeof(p) 8 sizeof(engine)/256 8` when I compile it in MSVC. What compiler version did you use? Maybe you used some special compiler settings?

## SChernykh | 2024-04-13T18:33:24+00:00
In any case, this PR should make this a compile-time problem instead: https://github.com/xmrig/xmrig/pull/3461
If it compiles, you can be sure pointer sizes match.

## xcryptodigger | 2024-04-14T05:15:22+00:00
> sizeof(p) is 8, and your code prints `sizeof(p) 8 sizeof(engine)/256 8` when I compile it in MSVC. What compiler version did you use? Maybe you used some special compiler settings?

It is not only on MSVC.
When built on Ubuntu, g++ then it prints
**sizeof(p) 16 sizeof(engine)/256 8**
So it is also not correct and again memcpy spoils memory after engine array.

I noticed that because when my own JIT compiler implementation grows with code then sometimes it works and sometimes does not work just because unpredictable behave. And seem reason is those handler pointers.


## SChernykh | 2024-04-14T07:02:18+00:00
Did you try to compile with #3461? Like I said, I can't reproduce your results.

Edit: it is, indeed, 16 bytes in g++. I'll look into it.

## SChernykh | 2024-04-14T07:15:38+00:00
#3462 should fix it.

## xcryptodigger | 2024-04-14T17:35:06+00:00
Thank You!
Seems now fixed.
PS: Someone can explain why compilers can reserve too much bytes per simple pointer? I have no idea why..

## SChernykh | 2024-04-14T17:48:59+00:00
I found this article on the topic: https://devblogs.microsoft.com/oldnewthing/20040209-00/?p=40713

# Action History
- Created by: xcryptodigger | 2024-04-13T12:13:57+00:00
- Closed at: 2024-04-14T17:35:06+00:00
