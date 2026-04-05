---
title: 'Error when building xmrig on termux (cmake) '
source_url: https://github.com/xmrig/xmrig/issues/3006
author: mrugtangy
assignees: []
labels: []
created_at: '2022-04-06T08:07:33+00:00'
updated_at: '2025-06-28T10:41:52+00:00'
type: issue
status: closed
closed_at: '2025-06-28T10:41:52+00:00'
---

# Original Description
So, I'm trying to build xmrig on termux using cmake. But whenever I am executing the make command, It's throwing this error after reaching 6%


Consolidate compiler generated dependencies of target ethash [ 1%] Built target ethash Consolidate compiler generated dependencies of target ghostrider [ 1%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_echo.c.o clang-13: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument] [ 2%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_fugue.c.o clang-13: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument] [ 2%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_groestl.c.o clang-13: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument] [ 2%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_hamsi.c.o clang-13: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument] [ 3%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_jh.c.o clang-13: warning: optimization flag '-fno-tree-vrp' is not supported [-Wignored-optimization-argument] clang-13: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument] [ 3%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_keccak.c.o clang-13: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument] [ 4%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_luffa.c.o clang-13: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument] [ 4%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_shabal.c.o clang-13: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument] [ 4%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_shavite.c.o clang-13: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument] [ 5%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_simd.c.o clang-13: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument] [ 5%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_sha2.c.o clang-13: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument] [ 5%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_skein.c.o clang-13: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument] [ 6%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_whirlpool.c.o clang-13: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument] [ 6%] Building CXX object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/ghostrider.cpp.o clang-13: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument] In file included from /data/data/com.termux/files/home/xmrig/src/crypto/ghostrider/ghostrider.cpp:43: /data/data/com.termux/files/home/xmrig/src/crypto/ghostrider/../../crypto/cn/CryptoNight.h:41:58: warning: 'ms_abi' calling convention is not supported for this target [-Wignored-attributes] typedef void(*cn_mainloop_fun_ms_abi)(cryptonight_ctx**) ABI_ATTRIBUTE; ^ /data/data/com.termux/files/home/xmrig/src/crypto/ghostrider/../../crypto/cn/CryptoNight.h:36:41: note: expanded from macro 'ABI_ATTRIBUTE' # define ABI_ATTRIBUTE __attribute__((ms_abi)) ^ In file included from /data/data/com.termux/files/home/xmrig/src/crypto/ghostrider/ghostrider.cpp:59: In file included from /data/data/com.termux/files/usr/lib/clang/13.0.1/include/x86intrin.h:13: /data/data/com.termux/files/usr/lib/clang/13.0.1/include/ia32intrin.h:200:10: error: use of undeclared identifier '__builtin_ia32_readeflags_u32' return __builtin_ia32_readeflags_u32(); ^ /data/data/com.termux/files/usr/lib/clang/13.0.1/include/ia32intrin.h:206:3: error: use of undeclared identifier '__builtin_ia32_writeeflags_u32' __builtin_ia32_writeeflags_u32(__f); ^ /data/data/com.termux/files/usr/lib/clang/13.0.1/include/ia32intrin.h:288:10: error: use of undeclared identifier '__builtin_ia32_crc32qi' return __builtin_ia32_crc32qi(__C, __D); ^ /data/data/com.termux/files/usr/lib/clang/13.0.1/include/ia32intrin.h:309:10: error: use of undeclared identifier '__builtin_ia32_crc32hi'; did you mean '__builtin_arm_crc32h'? return __builtin_ia32_crc32hi(__C, __D); ^ /data/data/com.termux/files/usr/lib/clang/13.0.1/include/ia32intrin.h:309:10: note: '__builtin_arm_crc32h' declared here /data/data/com.termux/files/usr/lib/clang/13.0.1/include/ia32intrin.h:330:10: error: use of undeclared identifier '__builtin_ia32_crc32si' return __builtin_ia32_crc32si(__C, __D); ^ /data/data/com.termux/files/usr/lib/clang/13.0.1/include/ia32intrin.h:358:10: error: use of undeclared identifier '__builtin_ia32_rdpmc'; did you mean '__builtin_arm_dmb'? return __builtin_ia32_rdpmc(__A); ^ /data/data/com.termux/files/usr/lib/clang/13.0.1/include/ia32intrin.h:358:10: note: '__builtin_arm_dmb' declared here /data/data/com.termux/files/usr/lib/clang/13.0.1/include/ia32intrin.h:358:10: error: argument to '__builtin_arm_dmb' must be a constant integer return __builtin_ia32_rdpmc(__A); ^ ~~~ /data/data/com.termux/files/usr/lib/clang/13.0.1/include/ia32intrin.h:364:10: error: use of undeclared identifier '__builtin_ia32_rdtscp'; did you mean '__builtin_arm_rsrp'? return __builtin_ia32_rdtscp(__A); ^ /data/data/com.termux/files/usr/lib/clang/13.0.1/include/ia32intrin.h:364:10: note: '__builtin_arm_rsrp' declared here /data/data/com.termux/files/usr/lib/clang/13.0.1/include/ia32intrin.h:364:32: error: cannot initialize a parameter of type 'const char *' with an lvalue of type 'unsigned int *' return __builtin_ia32_rdtscp(__A); ^~~ /data/data/com.termux/files/usr/lib/clang/13.0.1/include/ia32intrin.h:373:3: error: use of undeclared identifier '__builtin_ia32_wbinvd' __builtin_ia32_wbinvd(); ^ In file included from /data/data/com.termux/files/home/xmrig/src/crypto/ghostrider/ghostrider.cpp:59: In file included from /data/data/com.termux/files/usr/lib/clang/13.0.1/include/x86intrin.h:15: In file included from /data/data/com.termux/files/usr/lib/clang/13.0.1/include/immintrin.h:13: In file included from /data/data/com.termux/files/usr/lib/clang/13.0.1/include/x86gprintrin.h:15: /data/data/com.termux/files/usr/lib/clang/13.0.1/include/hresetintrin.h:42:27: error: invalid input constraint 'a' in asm __asm__ ("hreset $0" :: "a"(__eax)); ^ In file included from /data/data/com.termux/files/home/xmrig/src/crypto/ghostrider/ghostrider.cpp:59: In file included from /data/data/com.termux/files/usr/lib/clang/13.0.1/include/x86intrin.h:15: In file included from /data/data/com.termux/files/usr/lib/clang/13.0.1/include/immintrin.h:17: /data/data/com.termux/files/usr/lib/clang/13.0.1/include/mmintrin.h:33:5: error: use of undeclared identifier '__builtin_ia32_emms'; did you mean '__builtin_isless'? __builtin_ia32_emms(); ^ /data/data/com.termux/files/usr/include/c++/v1/math.h:651:12: note: '__builtin_isless' declared here return isless(__lcpp_x, __lcpp_y); ^ /data/data/com.termux/files/usr/include/c++/v1/../../math.h:311:22: note: expanded from macro 'isless' #define isless(x, y) __builtin_isless((x), (y)) ^ In file included from /data/data/com.termux/files/home/xmrig/src/crypto/ghostrider/ghostrider.cpp:59: In file included from /data/data/com.termux/files/usr/lib/clang/13.0.1/include/x86intrin.h:15: In file included from /data/data/com.termux/files/usr/lib/clang/13.0.1/include/immintrin.h:17: /data/data/com.termux/files/usr/lib/clang/13.0.1/include/mmintrin.h:33:25: error: too few arguments to function call, expected 2, have 0 __builtin_ia32_emms(); ~~~~~~~~~~~~~~~~~~~~^ /data/data/com.termux/files/usr/lib/clang/13.0.1/include/mmintrin.h:50:19: error: use of undeclared identifier '__builtin_ia32_vec_init_v2si' return (__m64)__builtin_ia32_vec_init_v2si(__i, 0); ^ /data/data/com.termux/files/usr/lib/clang/13.0.1/include/mmintrin.h:67:12: error: use of undeclared identifier '__builtin_ia32_vec_ext_v2si' return __builtin_ia32_vec_ext_v2si((__v2si)__m, 0); ^ /data/data/com.termux/files/usr/lib/clang/13.0.1/include/mmintrin.h:129:19: error: use of undeclared identifier '__builtin_ia32_packsswb' return (__m64)__builtin_ia32_packsswb((__v4hi)__m1, (__v4hi)__m2); ^ /data/data/com.termux/files/usr/lib/clang/13.0.1/include/mmintrin.h:159:19: error: use of undeclared identifier '__builtin_ia32_packssdw' return (__m64)__builtin_ia32_packssdw((__v2si)__m1, (__v2si)__m2); ^ /data/data/com.termux/files/usr/lib/clang/13.0.1/include/mmintrin.h:189:19: error: use of undeclared identifier '__builtin_ia32_packuswb' return (__m64)__builtin_ia32_packuswb((__v4hi)__m1, (__v4hi)__m2); ^ /data/data/com.termux/files/usr/lib/clang/13.0.1/include/mmintrin.h:216:19: error: use of undeclared identifier '__builtin_ia32_punpckhbw' return (__m64)__builtin_ia32_punpckhbw((__v8qi)__m1, (__v8qi)__m2); ^ fatal error: too many errors emitted, stopping now [-ferror-limit=] 1 warning and 20 errors generated. make[2]: *** [src/crypto/ghostrider/CMakeFiles/ghostrider.dir/build.make:300: src/crypto/ghostrider/CMakeFiles/ghostrider.dir/ghostrider.cpp.o] Error 1 make[1]: *** [CMakeFiles/Makefile2:216: src/crypto/ghostrider/CMakeFiles/ghostrider.dir/all] Error 2 make: *** [Makefile:91: all] Error 2



# Discussion History
## Spudz76 | 2022-04-07T02:44:38+00:00
If you aren't using that algorithm you could add `-DWITH_GHOSTRIDER=OFF` to the cmake command line and avoid compiling it completely.

## mrugtangy | 2022-04-16T11:48:54+00:00
Now, it's giving me this error

[ 41%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuWorker.cpp.o
clang-14: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
In file included from /data/data/com.termux/files/home/xmrig/src/backend/cpu/CpuWorker.cpp:32:
/data/data/com.termux/files/home/xmrig/src/crypto/cn/CryptoNight.h:41:58: warning: 'ms_abi' calling convention is not supported for this target [-Wignored-attributes]
typedef void(*cn_mainloop_fun_ms_abi)(cryptonight_ctx**) ABI_ATTRIBUTE;
                                                         ^
/data/data/com.termux/files/home/xmrig/src/crypto/cn/CryptoNight.h:36:41: note: expanded from macro 'ABI_ATTRIBUTE'
#   define ABI_ATTRIBUTE __attribute__((ms_abi))
                                        ^
1 warning generated.
[ 42%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/platform/BasicCpuInfo.cpp.o
clang-14: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
In file included from /data/data/com.termux/files/home/xmrig/src/backend/cpu/platform/BasicCpuInfo.cpp:29:
/data/data/com.termux/files/usr/lib/clang/14.0.0/include/cpuid.h:14:2: error: this header is for x86 only
#error this header is for x86 only
^
/data/data/com.termux/files/usr/lib/clang/14.0.0/include/cpuid.h:287:5: error: invalid output constraint '=a' in asm
    __cpuid(__leaf, __eax, __ebx, __ecx, __edx);
    ^
/data/data/com.termux/files/usr/lib/clang/14.0.0/include/cpuid.h:252:11: note: expanded from macro '__cpuid'
        : "=a"(__eax), "=r" (__ebx), "=c"(__ecx), "=d"(__edx) \
          ^
/data/data/com.termux/files/usr/lib/clang/14.0.0/include/cpuid.h:302:5: error: invalid output constraint '=a' in asm
    __cpuid(__leaf, *__eax, *__ebx, *__ecx, *__edx);
    ^
/data/data/com.termux/files/usr/lib/clang/14.0.0/include/cpuid.h:252:11: note: expanded from macro '__cpuid'
        : "=a"(__eax), "=r" (__ebx), "=c"(__ecx), "=d"(__edx) \
          ^
/data/data/com.termux/files/usr/lib/clang/14.0.0/include/cpuid.h:316:5: error: invalid output constraint '=a' in asm
    __cpuid_count(__leaf, __subleaf, *__eax, *__ebx, *__ecx, *__edx);
    ^
/data/data/com.termux/files/usr/lib/clang/14.0.0/include/cpuid.h:259:11: note: expanded from macro '__cpuid_count'
        : "=a"(__eax), "=r" (__ebx), "=c"(__ecx), "=d"(__edx) \
          ^
/data/data/com.termux/files/home/xmrig/src/backend/cpu/platform/BasicCpuInfo.cpp:80:5: error: invalid output constraint '=a' in asm
    __cpuid_count(level, 0, output[0], output[1], output[2], output[3]);
    ^
/data/data/com.termux/files/usr/lib/clang/14.0.0/include/cpuid.h:259:11: note: expanded from macro '__cpuid_count'
        : "=a"(__eax), "=r" (__ebx), "=c"(__ecx), "=d"(__edx) \
          ^
/data/data/com.termux/files/home/xmrig/src/backend/cpu/platform/BasicCpuInfo.cpp:138:36: error: invalid output constraint '=a' in asm
    __asm__ __volatile__("xgetbv": "=a"(eax_reg), "=d"(edx_reg) : "c"(0) : "cc");
                                   ^
6 errors generated.
make[2]: *** [CMakeFiles/xmrig.dir/build.make:1350: CMakeFiles/xmrig.dir/src/backend/cpu/platform/BasicCpuInfo.cpp.o] Error 1
make[1]: *** [CMakeFiles/Makefile2:119: CMakeFiles/xmrig.dir/all] Error 2
make: *** [Makefile:91: all] Error 2

## Spudz76 | 2022-04-16T15:15:10+00:00
If it is 64-bit ARM try `-DARM_TARGET=8`

If it is 32-bit ARM try `-DARM_TARGET=7`

Sometimes I guess it doesn't detect properly.  It's trying to use x86 code which shouldn't happen if it figured out it was ARM.

## mrugtangy | 2022-04-17T06:32:01+00:00
Error when trying with -DARM_TARGET=7


In file included from /data/data/com.termux/files/home/xmrig/src/crypto/cn/CnHash.cpp:27:
In file included from /data/data/com.termux/files/home/xmrig/src/crypto/cn/CryptoNight_arm.h:35:
In file included from /data/data/com.termux/files/home/xmrig/src/crypto/cn/soft_aes.h:31:
/data/data/com.termux/files/home/xmrig/src/crypto/cn/sse2neon.h:122:2: error: "Unsupported target. Must be either ARMv7-A+NEON or ARMv8-A."
#error "Unsupported target. Must be either ARMv7-A+NEON or ARMv8-A."
^
/data/data/com.termux/files/home/xmrig/src/crypto/cn/sse2neon.h:7303:9: warning: array designators are a C99 extension [-Wc99-designator]
        [0] = {SSE2NEON_sbox[vreinterpretq_nth_u8_m128i(a, 0)],
        ^~~
1 warning and 1 error generated.
make[2]: *** [CMakeFiles/xmrig.dir/build.make:2694: CMakeFiles/xmrig.dir/src/crypto/cn/CnHash.cpp.o] Error 1
make[1]: *** [CMakeFiles/Makefile2:119: CMakeFiles/xmrig.dir/all] Error 2
make: *** [Makefile:91: all] Error 2

## mrugtangy | 2022-04-17T07:01:25+00:00
Error when trying with DARM_TARGET=8

/data/data/com.termux/files/home/xmrig/src/backend/cpu/platform/BasicCpuInfo_arm.cpp:78:49: error: use of undeclared identifier 'HWCAP_AES'
    m_flags.set(FLAG_AES, getauxval(AT_HWCAP) & HWCAP_AES);
                                                ^
1 error generated.
make[2]: *** [CMakeFiles/xmrig.dir/build.make:1350: CMakeFiles/xmrig.dir/src/backend/cpu/platform/BasicCpuInfo_arm.cpp.o] Error 1
make[1]: *** [CMakeFiles/Makefile2:119: CMakeFiles/xmrig.dir/all] Error 2
make: *** [Makefile:91: all] Error 2

## Spudz76 | 2022-04-17T07:30:40+00:00
Something is weird about the compiler/toolchain.  What does `lscpu` and `uname -a` and `gcc -v` say?

## mrugtangy | 2022-04-18T10:51:57+00:00
~/xmrig/build $ lscpu
Architecture:           armv8l
  Byte Order:           Little Endian
CPU(s):                 8
  On-line CPU(s) list:  0-3
  Off-line CPU(s) list: 4-7
Vendor ID:              ARM
  Model name:           Cortex-A53
    Model:              4
    Thread(s) per core: 1
    Core(s) per socket: 4
    Socket(s):          1
    Stepping:           r0p4
    CPU(s) scaling MHz: 79%
    CPU max MHz:        1586.0000
    CPU min MHz:        0.0000
    Flags:              half thumb fastmult vfp edsp neon vfpv3 tls vfpv4 id
                        iva idivt lpae evtstrm aes pmull sha1 sha2 crc32
~/xmrig/build $ uname -a
Linux localhost 3.18.91-15641782-QB44315427 #1 SMP PREEMPT Mon Oct 4 18:13:34 KST 2021 armv8l Android
~/xmrig/build $ gcc -v
clang version 14.0.0
Target: armv7a-unknown-linux-android24
Thread model: posix
InstalledDir: /data/data/com.termux/files/usr/bin


## Spudz76 | 2022-04-18T11:08:39+00:00
Your toolchain is 32-bit (`armv7a`) and must match the rest of things (64-bit `armv8l`)

## mrugtangy | 2022-04-18T14:57:29+00:00
But I tried with both methods and it didn't work

## Spudz76 | 2022-04-18T16:14:58+00:00
My bad; I read some more and `armv8l` is a 64-bit CPU in 32-bit mode (I had thought all armv8 was always 64).  Unless you can change kernels (probably a full image flash) to an `aarch64` one then it probably won't work.

I have checked the CMake logic and it doesn't know `armv8l` which is why it had to be forced.  The sse2neon adaptation layer may also not be figuring out the CPU properly.  I am making a patch that may help.

What does `gcc -print-targets` say?

## mrugtangy | 2022-04-19T18:49:35+00:00
Registered Targets:
    aarch64    - AArch64 (little endian)
    aarch64_32 - AArch64 (little endian ILP32)
    aarch64_be - AArch64 (big endian)
    amdgcn     - AMD GCN GPUs
    arc        - ARC
    arm        - ARM
    arm64      - ARM64 (little endian)
    arm64_32   - ARM64 (little endian ILP32)
    armeb      - ARM (big endian)
    avr        - Atmel AVR Microcontroller
    bpf        - BPF (host endian)
    bpfeb      - BPF (big endian)
    bpfel      - BPF (little endian)
    csky       - C-SKY
    hexagon    - Hexagon
    lanai      - Lanai
    m68k       - Motorola 68000 family
    mips       - MIPS (32-bit big endian)
    mips64     - MIPS (64-bit big endian)
    mips64el   - MIPS (64-bit little endian)
    mipsel     - MIPS (32-bit little endian)
    msp430     - MSP430 [experimental]
    nvptx      - NVIDIA PTX 32-bit
    nvptx64    - NVIDIA PTX 64-bit
    ppc32      - PowerPC 32
    ppc32le    - PowerPC 32 LE
    ppc64      - PowerPC 64
    ppc64le    - PowerPC 64 LE
    r600       - AMD GPUs HD2XXX-HD6XXX
    riscv32    - 32-bit RISC-V
    riscv64    - 64-bit RISC-V
    sparc      - Sparc
    sparcel    - Sparc LE
    sparcv9    - Sparc V9
    systemz    - SystemZ
    thumb      - Thumb
    thumbeb    - Thumb (big endian)
    ve         - VE
    wasm32     - WebAssembly 32-bit
    wasm64     - WebAssembly 64-bit
    x86        - 32-bit X86: Pentium-Pro and above
    x86-64     - 64-bit X86: EM64T and AMD64
    xcore      - XCore

## Spudz76 | 2022-04-19T22:07:31+00:00
What sort of device is it, so I can try setting up an emulator for further testing.

## mrugtangy | 2022-04-27T08:56:50+00:00
It's termux, running on a Samsung Galaxy A2 Core phone

## max-ishere | 2022-07-10T16:22:53+00:00
Seems to also be an issue on Galaxy J7 Pro (J730).

# Action History
- Created by: mrugtangy | 2022-04-06T08:07:33+00:00
- Closed at: 2025-06-28T10:41:52+00:00
