---
title: '[FR] Add support for RISC-V open ISA CPUs'
source_url: https://github.com/xmrig/xmrig/issues/1924
author: mark-stopka
assignees: []
labels:
- enhancement
- RISC-V
created_at: '2020-11-01T12:08:47+00:00'
updated_at: '2025-10-17T21:11:27+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Hi, RISC-V is gaining traction, and more and more powerfull open IP CPUs are becomming available on the market, I was wondering if you guys considered adding RISC-V support for RandomX into `xmrig`.

# Discussion History
## SChernykh | 2020-11-02T09:11:44+00:00
You are probably talking about https://www.sifive.com/blog/the-heart-of-risc-v-development-is-unmatched - yes, it will be able to run RandomX with decent hashrate, but it's a bit expensive at the moment. RISC-V is in the wish list, but there are no solid plans for it now. If you know of any RISC-V board with 4+ GB RAM and 64-bit CPU at no more than $100, let us know.

## mark-stopka | 2020-11-02T09:16:29+00:00
I may be willing to sponsor one for development purposes, are you US based so there would be no additional import dutties? 

## SChernykh | 2020-11-02T09:26:58+00:00
I'm in Europe. I'll be busy with Zen3-related changes in November and probably December anyway. Maybe RISC-V availability will be better in 2021.

## mark-stopka | 2020-11-02T09:34:23+00:00
Ok, I'll ping back in 2021, if you could leave the ticket open I would appreciate it, as I link it in my private Issue Tracker...

## Lonnegan | 2020-11-04T19:39:51+00:00
> I'll be busy with Zen3-related changes in November and probably December anyway. 

Okay... Will there be changes in Zen 3 which will affect xmrig? AFAIK will the cache sizes stay the same (hence in different structure; 1x 32 MB per die instead of 2x 16 MB per die), but no new instruction sets. Or do you have other information?



## SChernykh | 2020-11-04T23:33:51+00:00
Zen3 has vector AES instructions, I need to add support for them. MSR mod might not work as intended because it's CPU specific. Plus I need to check all previous Zen1/Zen2 optimizations to see if they work or not.

## Lonnegan | 2020-11-12T17:19:44+00:00
@SChernykh Did you have the chance to test the impact of VAES to one of the mining algo, already?

## SChernykh | 2020-11-12T17:23:17+00:00
Yes, I tested 2 different ways to use VAES and they both didn't give any speedup. AES in RandomX is limited by instruction latency and it stayed the same for VAES instructions.

## Lonnegan | 2020-11-12T18:24:42+00:00
> AES in RandomX is limited by instruction latency and it stayed the same for VAES instructions.

Plus the higher latency of the L3 cache in comparison to Zen 2. Seems like Zen 3 is not the same game changer in RandomX mining as it is in gaming then.

## xmrig | 2021-04-12T14:37:09+00:00
@mark-stopka Any news here? Thank you.

## mark-stopka | 2021-04-12T18:55:01+00:00
> @mark-stopka Any news here? Thank you.

I am not sure what news should I have, there is still only one board available, and I already offered to sponsor one for you guys if you'd like to implement RISC-V support, however, there should be new boards and chips available in next 6 months, so:

a) you'd like me to sponsor the current SiFive board which I am happy to do
b) wait for new boards and re-evaluate
c) you expect me to hire a 3rd party to implement such support, in which case I can look for someone, but having it done by the core team would probably be more cost-effective as you already know the codebase and the caveats of RandomX mining algo, I would have to recruit someone who never implemented RandomX before, nor contributed to your codebase as don't know anyone who has that experience

Let me know which one works for you, and we can move forward (or wait in case of option 2)

## SChernykh | 2021-04-12T21:44:51+00:00
I did a quick look again at https://www.sifive.com/boards/hifive-unmatched and https://www.sifive.com/cores/u74-mc and it seems that this board will be able to run 1 RandomX thread (2 MB L2 cache) at the full speed with JIT enabled (RV64GBC support covers all RandomX instructions), so it's good enough for development. Also this quote
```
The L1 Instruction Cache and the L2 Cache can be configured into high-speed deterministic SRAMs
```
got me really curious on how it can be used for RandomX. Price of the board is still quite high, but if you're happy to send it my way to Sweden (I can pay import tax), I'll add full support to xmrig.

Edit: I just realized there's no AES support though, so it won't give high hashrate in any case.

## mark-stopka | 2021-04-12T21:50:17+00:00
@SChernykh, cool, can you ping me at mstopka@opensuse.org?

## gavan-x | 2021-08-08T09:43:45+00:00
@mark-stopka @SChernykh I was one of the few that received a BeagleV board here in Tokyo. Using the [July 27th fedora release](https://github.com/starfive-tech/Fedora_on_StarFive) 

Following the Fedora build steps, dependencies installed correctly, 

`make` error.

```
[riscv@fedora-starfive build]$ make -j2
Scanning dependencies of target ethash
Scanning dependencies of target xmrig-asm
[  0%] Building C object src/3rdparty/libethash/CMakeFiles/ethash.dir/ethash_internal.c.o
[  1%] Building ASM object CMakeFiles/xmrig-asm.dir/src/crypto/cn/asm/cn_main_loop.S.o
cc: error: unrecognized command-line option ‘-maes’
make[2]: *** [src/3rdparty/libethash/CMakeFiles/ethash.dir/build.make:82: src/3rdparty/libethash/CMakeFiles/ethash.dir/ethash_internal.c.o] Error 1
make[1]: *** [CMakeFiles/Makefile2:375: src/3rdparty/libethash/CMakeFiles/ethash.dir/all] Error 2
make[1]: *** Waiting for unfinished jobs....
[  1%] Building ASM object CMakeFiles/xmrig-asm.dir/src/crypto/cn/asm/CryptonightR_template.S.o
/home/riscv/xmrig-6.12.2-mo2/src/crypto/cn/asm/cn_main_loop.S: Assembler messages:
/home/riscv/xmrig-6.12.2-mo2/src/crypto/cn/asm/cn_main_loop.S:6: Error: unknown pseudo-op: `.intel_syntax'
/home/riscv/xmrig-6.12.2-mo2/src/crypto/cn/asm/cn_main_loop.S:22: Warning: alignment too large: 63 assumed

as: out of memory allocating 9223372036854841442 bytes after a total of 135168 bytes
make[2]: *** [CMakeFiles/xmrig-asm.dir/build.make:82: CMakeFiles/xmrig-asm.dir/src/crypto/cn/asm/cn_main_loop.S.o] Error 1
make[2]: *** Waiting for unfinished jobs....
/home/riscv/xmrig-6.12.2-mo2/src/crypto/cn/asm/CryptonightR_template.S: Assembler messages:
/home/riscv/xmrig-6.12.2-mo2/src/crypto/cn/asm/CryptonightR_template.S:6: Error: unknown pseudo-op: `.intel_syntax'
/home/riscv/xmrig-6.12.2-mo2/src/crypto/cn/asm/CryptonightR_template.inc:13: Warning: alignment too large: 63 assumed

as: out of memory allocating 9223372036854841442 bytes after a total of 270336 bytes
make[2]: *** [CMakeFiles/xmrig-asm.dir/build.make:87: CMakeFiles/xmrig-asm.dir/src/crypto/cn/asm/CryptonightR_template.S.o] Error 1
make[1]: *** [CMakeFiles/Makefile2:182: CMakeFiles/xmrig-asm.dir/all] Error 2
make: *** [Makefile:103: all] Error 2
```




## benthetechguy | 2021-12-17T03:04:24+00:00
I'm also interested in RISC-V xmrig, I have a Nezha D1 I'm willing to test any code on.

## divinity76 | 2024-03-17T09:16:35+00:00
@gavan1 and what happens if you compile with
```
-DWITH_CN_LITE=OFF -DWITH_CN_HEAVY=OFF -DWITH_CN_PICO=OFF -DWITH_CN_FEMTO=OFF
```
? (disables cryptonight algorithm)

## kami4ka | 2024-04-18T20:16:05+00:00
@divinity76 nothing, the code won't compile due to the lack of code for RISC-V, so it tries to build x86 instead

## KiritakeKumi | 2024-06-27T09:07:56+00:00
Currently, there is a host milkv pioneer on the market that uses the high-performance RISC-V chip SG2042. This chip looks very similar to the Antminer X5 dedicated XMR mining machine. Has anyone done research on this device?

## SChernykh | 2024-06-27T09:15:04+00:00
Antminer X5 uses SG2042R which is a version of SG2042 with some additional instructions and hardware AES. I guess they added new instructions for the most commonly used sequences in RandomX generated code.

## KiritakeKumi | 2024-06-27T09:24:57+00:00
So can we set an option in the compilation to support RISC-V without any acceleration to avoid compilation failures due to x86/arm related instruction sets, later add RISC-V Cryptography Extension (K) to achieve full acceleration support.

## SChernykh | 2024-06-27T09:45:01+00:00
It's not supported by XMRig yet. Once I have an easily accessible RISC-V system, I will make sure it compiles.

## KiritakeKumi | 2024-07-01T10:26:56+00:00
RISC-V International provides some RISC-V devices that can be accessed remotely. If you don’t have any devices, you can choose here https://riscv.org/risc-v-labs/.

## aragubas | 2024-07-27T12:16:27+00:00
I have a StarFive VisionFive 2 with 8GB of RAM and Dual Ethernet model, any updates on this?

## aragubas | 2024-07-27T15:00:48+00:00
Trying to build on the StarFive VisionFive 2 yields the following errors:

```
[  2%] Building C object src/3rdparty/argon2/CMakeFiles/argon2-avx2.dir/arch/x86_64/lib/argon2-avx2.c.o
[  2%] Building C object src/3rdparty/libethash/CMakeFiles/ethash.dir/ethash_internal.c.o
[  2%] Building ASM object CMakeFiles/xmrig-asm.dir/src/crypto/cn/asm/cn_main_loop.S.o
[  2%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_blake.c.o
cc: error: unrecognized command-line option ‘-maes’
cc: error: unrecognized command-line option ‘-maes’
make[2]: *** [src/3rdparty/argon2/CMakeFiles/argon2-avx2.dir/build.make:76: src/3rdparty/argon2/CMakeFiles/argon2-avx2.dir/arch/x86_64/lib/argon2-avx2.c.o] Error 1
make[2]: *** [src/3rdparty/libethash/CMakeFiles/ethash.dir/build.make:76: src/3rdparty/libethash/CMakeFiles/ethash.dir/ethash_internal.c.o] Error 1
make[1]: *** [CMakeFiles/Makefile2:368: src/3rdparty/libethash/CMakeFiles/ethash.dir/all] Error 2
make[1]: *** Waiting for unfinished jobs....
make[1]: *** [CMakeFiles/Makefile2:286: src/3rdparty/argon2/CMakeFiles/argon2-avx2.dir/all] Error 2
cc: error: unrecognized command-line option ‘-maes’
make[2]: *** [src/crypto/ghostrider/CMakeFiles/ghostrider.dir/build.make:76: src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_blake.c.o] Error 1
make[2]: *** Waiting for unfinished jobs....
/home/dietpi/Downloads/xmrig/src/crypto/cn/asm/cn_main_loop.S: Assembler messages:
/home/dietpi/Downloads/xmrig/src/crypto/cn/asm/cn_main_loop.S:6: Error: unknown pseudo-op: `.intel_syntax'
/home/dietpi/Downloads/xmrig/src/crypto/cn/asm/cn_main_loop.S:25: Warning: alignment too large: 63 assumed

as: out of memory allocating 9223372036854841462 bytes after a total of 270336 bytes
make[2]: *** [CMakeFiles/xmrig-asm.dir/build.make:75: CMakeFiles/xmrig-asm.dir/src/crypto/cn/asm/cn_main_loop.S.o] Error 1
make[2]: *** Waiting for unfinished jobs....
[  3%] Building ASM object CMakeFiles/xmrig-asm.dir/src/crypto/cn/asm/CryptonightR_template.S.o
[  3%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_bmw.c.o
cc: error: unrecognized command-line option ‘-maes’
make[2]: *** [src/crypto/ghostrider/CMakeFiles/ghostrider.dir/build.make:90: src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_bmw.c.o] Error 1
make[1]: *** [CMakeFiles/Makefile2:394: src/crypto/ghostrider/CMakeFiles/ghostrider.dir/all] Error 2
/home/dietpi/Downloads/xmrig/src/crypto/cn/asm/CryptonightR_template.S: Assembler messages:
/home/dietpi/Downloads/xmrig/src/crypto/cn/asm/CryptonightR_template.S:6: Error: unknown pseudo-op: `.intel_syntax'
/home/dietpi/Downloads/xmrig/src/crypto/cn/asm/CryptonightR_template.inc:13: Warning: alignment too large: 63 assumed

as: out of memory allocating 9223372036854841462 bytes after a total of 405504 bytes
make[2]: *** [CMakeFiles/xmrig-asm.dir/build.make:88: CMakeFiles/xmrig-asm.dir/src/crypto/cn/asm/CryptonightR_template.S.o] Error 1
make[1]: *** [CMakeFiles/Makefile2:148: CMakeFiles/xmrig-asm.dir/all] Error 2
make: *** [Makefile:91: all] Error 2
```

## benthetechguy | 2024-07-27T15:08:29+00:00
That error just means it's trying to compile with x86-specific options, because xmrig is built to treat everything it can't detect ARM on as x86.


## aragubas | 2024-07-27T15:10:16+00:00
> That error just means it's trying to compile with x86-specific options, because xmrig is built to treat everything it can't detect ARM on as x86.

Is there a way for me to specify that I'm building on RISC-V?

## benthetechguy | 2024-07-27T16:02:08+00:00
No, there's no code for RISC-V yet. There's code in xmrig that uses x86 specific features, and the only reason ARM works is because of translation layers like sse2neon. Before you can compile for RISC-V, we need to implement something like that.


## SChernykh | 2024-07-27T16:02:32+00:00
Not yet, but I think it can be fixed with a few changes in CMake files. I'll try to set up a risc-v Qemu VM to see what needs to be done.

## HubertusWine | 2024-09-09T19:20:53+00:00
I would be willing to provide a Risc-V Server for development if this helps.

## divinity76 | 2024-09-10T12:59:14+00:00
@HubertusWine 
> I would be willing to provide a Risc-V Server for development if this helps.

see https://github.com/xmrig/xmrig/issues/1924#issuecomment-818263351 

## HubertusWine | 2024-09-10T13:09:28+00:00
@SChernykh I can't provide hardware, but as mentioned:

> I would be willing to provide a Risc-V Server for development if this helps.

CPU: TH1520
RAM: 16 GB

You could have root access. I use alpine on them, but I could install any riscv compiled image (Ubuntu, Kosmos, Debian, Fedora, Android,...).

## divinity76 | 2024-09-10T13:22:51+00:00
TH1520 have `RVV 0.7.1` (RISC-V Vector Extension) instructions, Similar to ARM-Neon / x86 SSE, I wonder if those are relevant for RandomX 🤔 

## SChernykh | 2024-09-10T15:31:50+00:00
@HubertusWine I plan to try running XMRig in RISC-V QEMU virtual machine and as soon as I'll get it working I will ask you to test it. But there's no ETA on this yet because I don't know how much code I will need to fix.

## HubertusWine | 2024-09-10T15:33:42+00:00
@SChernykh  Thanks. If it helps, I was able to run this without problems: https://github.com/hadi-guang/RandomX-RISCV

## SChernykh | 2024-09-10T15:52:40+00:00
https://github.com/tevador/RandomX/ already supports RISC-V, and https://github.com/SChernykh/p2pool/ uses it so it also supports RISC-V.

XMRig just has many many changes which will make integration of that code not straight-forward.

## IngwiePhoenix | 2025-10-17T21:11:27+00:00
What exactly would be needed for said integration?

I often find myself experimenting with RISC-V and am in the process of aquiring a Milk-V Pioneer - which has a pretty good compute grunt. So I might be able to help out - but I am entirely new to the project and it's structure...though I do bring experience in C and Go.

# Action History
- Created by: mark-stopka | 2020-11-01T12:08:47+00:00
