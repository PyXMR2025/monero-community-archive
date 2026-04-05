---
title: Better Source Code Documentation
source_url: https://github.com/xmrig/xmrig/issues/2210
author: KungFuJesus
assignees: []
labels:
- question
created_at: '2021-03-25T22:08:27+00:00'
updated_at: '2021-04-12T13:48:21+00:00'
type: issue
status: closed
closed_at: '2021-04-12T13:48:21+00:00'
---

# Original Description
**Describe the bug**
The current source structure is difficult to navigate and profile.  I've built the miner with the "profiler on" for armv8, by swapping out the x86 only rdtsc instruction with the aarch64 only instruction with a compiler macro:
```
@@ -50,9 +50,15 @@ static FORCE_INLINE uint64_t ReadTSC()
 #ifdef _MSC_VER
     return __rdtsc();
 #else
+    #ifdef __AMD64__
     uint32_t hi, lo;
     __asm__ __volatile__("rdtsc" : "=a"(lo), "=d"(hi));
     return (((uint64_t)hi) << 32) | lo;
+    #else
+    int64_t virtual_timer_value;
+    asm volatile("mrs %0, cntvct_el0" : "=r"(virtual_timer_value));
+    return virtual_timer_value;
+    #endif
 #endif
```
The breakdown it gives is very poor (the ns measured may not even be accurate, there maybe a multiplier needed, but to a relative scale it's probably correct):

```
[2021-03-25 17:57:30.872]  profile  Thread 28147061251 | RandomX_hash                   | 100.000% |  58200475 ns
[2021-03-25 17:57:30.873]  profile  Thread 28147061251 | RandomX_run                    |  96.411% |   6991284 ns
[2021-03-25 17:57:30.873]  profile  Thread 28147061251 | RandomX_JIT_execute            |  95.602% |   6932614 ns
[2021-03-25 17:57:30.873]  profile  Thread 28147061251 | RandomX_AES                    |   3.729% |   2170281 ns
[2021-03-25 17:57:30.873]  profile  Thread 28147061251 | RandomX_Blake2b                |   0.129% |      8292 ns
[2021-03-25 17:57:30.874]  profile  Thread 28147061251 | RandomX_generate_program       |   0.026% |      1875 ns
[2021-03-25 17:57:30.874]  profile  --------------|--------------------------------|----------|-------------
[2021-03-25 17:57:30.874]  profile  Thread 28147062090 | RandomX_hash                   | 100.000% |  56498177 ns
[2021-03-25 17:57:30.875]  profile  Thread 28147062090 | RandomX_run                    |  96.513% |   6803191 ns
[2021-03-25 17:57:30.875]  profile  Thread 28147062090 | RandomX_JIT_execute            |  95.822% |   6754438 ns
[2021-03-25 17:57:30.875]  profile  Thread 28147062090 | RandomX_AES                    |   3.521% |   1989271 ns
[2021-03-25 17:57:30.876]  profile  Thread 28147062090 | RandomX_Blake2b                |   0.102% |      6375 ns
[2021-03-25 17:57:30.876]  profile  Thread 28147062090 | RandomX_generate_program       |   0.025% |      1750 ns
[2021-03-25 17:57:30.876]  profile  --------------|--------------------------------|----------|-------------
[2021-03-25 17:57:30.876]  profile  Thread 28147062930 | RandomX_hash                   | 100.000% |  28239651 ns
[2021-03-25 17:57:30.876]  profile  Thread 28147062930 | RandomX_run                    |  91.173% |   3211294 ns
[2021-03-25 17:57:30.876]  profile  Thread 28147062930 | RandomX_JIT_execute            |  90.158% |   3175542 ns
[2021-03-25 17:57:30.877]  profile  Thread 28147062930 | RandomX_AES                    |   8.526% |   2407752 ns
[2021-03-25 17:57:30.877]  profile  Thread 28147062930 | RandomX_Blake2b                |   0.404% |     12626 ns
[2021-03-25 17:57:30.877]  profile  Thread 28147062930 | RandomX_generate_program       |   0.048% |      1667 ns
[2021-03-25 17:57:30.877]  profile  --------------|--------------------------------|----------|-------------
[2021-03-25 17:57:30.877]  profile  Thread 28147063769 | RandomX_hash                   | 100.000% |  30386805 ns
[2021-03-25 17:57:30.878]  profile  Thread 28147063769 | RandomX_run                    |  91.243% |   3456390 ns
[2021-03-25 17:57:30.878]  profile  Thread 28147063769 | RandomX_JIT_execute            |  90.451% |   3426388 ns
[2021-03-25 17:57:30.878]  profile  Thread 28147063769 | RandomX_AES                    |   8.720% |   2649764 ns
[2021-03-25 17:57:30.878]  profile  Thread 28147063769 | RandomX_Blake2b                |   0.153% |      5125 ns
[2021-03-25 17:57:30.878]  profile  Thread 28147063769 | RandomX_generate_program       |   0.045% |      1667 ns
[2021-03-25 17:57:30.879]  profile  --------------|--------------------------------|----------|-------------
[2021-03-25 17:57:30.879]  profile  Thread 28147064608 | RandomX_hash                   | 100.000% |  23022168 ns
[2021-03-25 17:57:30.879]  profile  Thread 28147064608 | RandomX_run                    |  90.795% |   2610846 ns
[2021-03-25 17:57:30.879]  profile  Thread 28147064608 | RandomX_JIT_execute            |  89.967% |   2587053 ns
[2021-03-25 17:57:30.879]  profile  Thread 28147064608 | RandomX_AES                    |   9.109% |   2097027 ns
[2021-03-25 17:57:30.880]  profile  Thread 28147064608 | RandomX_Blake2b                |   0.157% |      4000 ns
[2021-03-25 17:57:30.880]  profile  Thread 28147064608 | RandomX_generate_program       |   0.055% |      1542 ns
[2021-03-25 17:57:30.880]  profile  --------------|--------------------------------|----------|-------------
[2021-03-25 17:57:30.880]  profile  Thread 28147317331 | RandomX_hash                   | 100.000% |  23033669 ns
[2021-03-25 17:57:30.880]  profile  Thread 28147317331 | RandomX_run                    |  90.481% |   2604470 ns
[2021-03-25 17:57:30.880]  profile  Thread 28147317331 | RandomX_JIT_execute            |  89.625% |   2579802 ns
[2021-03-25 17:57:30.881]  profile  Thread 28147317331 | RandomX_AES                    |   9.302% |   2142654 ns
[2021-03-25 17:57:30.881]  profile  Thread 28147317331 | RandomX_Blake2b                |   0.162% |      4125 ns
[2021-03-25 17:57:30.881]  profile  Thread 28147317331 | RandomX_generate_program       |   0.054% |      1542 ns
[2021-03-25 17:57:30.881]  profile  --------------|--------------------------------|----------|-------------
[2021-03-25 17:57:30.881]  profile  RandomX_AES                    2242791.5 ns
[2021-03-25 17:57:30.881]  profile  RandomX_Blake2b                   6757.3 ns
[2021-03-25 17:57:30.882]  profile  RandomX_JIT_execute            4242639.6 ns
[2021-03-25 17:57:30.882]  profile  RandomX_generate_program          1673.7 ns
[2021-03-25 17:57:30.882]  profile  RandomX_hash                   36563490.8 ns
[2021-03-25 17:57:30.882]  profile  RandomX_run                    4279579.1 ns
```
The problem is this a very coarse profile and gives a pretty awful indicator for where the performance sore spots are.  Linux's perf profiler absolutely hates JIT'd code, so you really can't tell what's going on there apart from a few basic functions (a blake hash, some AES crypto accelerated functions, etc).  Is there any readme that could be compiled that gives a sort of tour of the code?  I suspect the _static.S file is most of the fast optimized code for aarch64 (I see a lot of explicit vectorization there) but a big section filled with zeros for what I assume is JIT generated code.

I found a few functions that might be suboptimal in the "JIT" but I think it's for some interpreted mode in the JIT.  For instance, the code that swaps 2 64 bit values in a "q" vector register is calling vdup with a lane select.  I believe it's fewer instructions and faster to do vext and swizzle them in one go.  Dropping a printf statement in there, it does appear that function actually ever gets called.

I don't know the specifics of the RandomX hash, but I did arrive pretty quickly at the conclusion with scrypt that vectorized EOR + bit shift rotations are a lot slower than the special variant of scalar EOR on aarch64 that lets you specify a shift or rotation for the second operand (superscalar nature of Cortex-A73 also made it possible to do vector operations in tandem, but not without some special TBLs. And sharing a scratchpad meant that this rearrangement of rows in the Salsa8 round of hashing would need to exist in the scalar variant as well, causing a lot of unnecessary moves).  I was trying to find that pattern anywhere in the code (XOR with rotated integer), but there's no clear picture of where the bytecode is authored in this.  

Namely, I just want to try to improve the hashrate on my Odroid-N2 (and M1 users will probably prosper as well).  Any guidance would be appreciated.

Also your option to use SSE4.1 for the blake hash bits is not working, due to a harded 0 value in the code.  The gains are negligible but the CMake option implies that it should be on.  Perhaps you did it intentionally to save the user from the SSE to AVX penalty, but given that the blake SSE4 code is in intrinsics, GCC and most compilers are smart enough to use the VEX coded instructions.  


# Discussion History
## SChernykh | 2021-03-25T23:15:29+00:00
There's no documentation except code comments. Profiler is an internal thing and is currently used for RandomX. It only works properly on x86 with fixed clock speed CPU. The functions you found are used in interpreter and are not relevant, everything worth optimizing is in `jit_compiler_a64_static.S` and `jit_compiler_a64.cpp`. Blake2 SSE4.1 is used only for x86 CPUs.

## KungFuJesus | 2021-03-25T23:46:27+00:00
Right, I was simply pointing out the SSE4 issue for those on x86, for which I'm sure is 98% of users. It'd be trivial to SIMD vectorize the blake2 stuff for aarch64 (and I probably will), but it's less than a percent of the run time.

I was hoping maybe it'd be possible for the JIT's function pipeline to be documented as far as when code is compiled, how the register allocation works, when and how it scoreboard's a microarchitecture's superscalar capabilities (there's evidence this was done for ivybridge in one of the source files).

As an example, if I wanted to emit a keyhole optimization for an EOR with rotations pattern (as is commonly seen with crypto hashes), how would I go about doing that?

## SChernykh | 2021-03-26T07:36:28+00:00
> I was simply pointing out the SSE4 issue for those on x86

It works on x86: https://github.com/xmrig/xmrig/blob/master/src/crypto/rx/RxVm.cpp#L54

RandomX documentation:
https://github.com/tevador/RandomX/blob/master/doc/design.md
https://github.com/tevador/RandomX/blob/master/doc/specs.md

There's no XOR with rotation that I know of.

## KungFuJesus | 2021-03-26T13:16:08+00:00
Strange, I definitely have the capability (Sandybridge) but those methods weren't called until I defined that extern variable as 1 instead of 0 where it's declared 

Maybe I'll see what's going on in a debugger.

## KungFuJesus | 2021-03-29T02:33:02+00:00
So I may have just implemented this tiny keyhole optimization in the JIT (at least I think I emitted the correct modifications in the imm argument to make this work).  There's limited places this can be done, namely: 

- It only makes sense when the XOR, OR, or AND operation this register's value is done with is _only_ used as an argument to an XOR and the register's value is otherwise replaced. 
- One could possibly follow the value through swaps, but as a simple first pass (and for correctness), I think I'll just keep it how I have it.  
- I think the barrel shifters could also be used for the move/swap operation as well but I'm not entirely sure, yet.

Does the benchmark mode verify correctness?  I'd like to see that this is functioning properly before trying to submit work to the pool.  Also my implementation is pretty unpolished at the moment.

## SChernykh | 2021-03-29T07:00:18+00:00
> Does the benchmark mode verify correctness?

If you mean `--bench` argument then yes, it has hardcoded hashes to compare against, but you have to calculate at least 100K hashes which will take some time on an ARM CPU.

Also, of course, you need to check that your changes actually make the overall hashrate bigger.

## KungFuJesus | 2021-03-29T15:34:12+00:00
> If you mean `--bench` argument then yes, it has hardcoded hashes to compare against, but you have to calculate at least 100K hashes which will take some time on an ARM CPU.

Looks like it's actually 1 million hashes.  Do I have to fix the seed or anything?  It printed out a hash in red, which I presume means it's wrong, but I can't tell for sure.

Also side note: I realize this is random code but I suspect it will optimize at least a little.  Has anyone considered compiling this bytecode to LLVM-IR and tried to JIT the programs out with that?  



## SChernykh | 2021-03-29T18:17:20+00:00
`--bench=100K` switches to 100,000 hashes and it should be green hash in the end. LLVM is too slow for this - hash calculation time is 1-2 ms and there are 8 programs to be compiled in each hash.

# Action History
- Created by: KungFuJesus | 2021-03-25T22:08:27+00:00
- Closed at: 2021-04-12T13:48:21+00:00
