---
title: CN-Heavy stopped working on AES-capable CPU with gcc-8
source_url: https://github.com/xmrig/xmrig/issues/2232
author: Spudz76
assignees: []
labels: []
created_at: '2021-04-03T06:47:42+00:00'
updated_at: '2021-04-06T06:52:52+00:00'
type: issue
status: closed
closed_at: '2021-04-06T06:52:52+00:00'
---

# Original Description
**Describe the bug**
CN-Heavy/XHV fails self-test on Xeon E5-2620 / `gcc version 8.3.0 (Debian 8.3.0-6) ` since some recent commit (testing commits now, to narrow it down)

Same seems to work fine on other various CPUs with various gcc versions (i7-4700MQ / `gcc version 9.3.0 (Ubuntu 9.3.0-17ubuntu1~20.04)` for one)

Same works fine on same exact machine if compiled with Clang-13.

**To Reproduce**
Check out `dev` branch, build it, try `./xmrig --algo=cn-heavy/xhv --stress`

**Expected behavior**
Should pass self-tests and work like it always did before.

**Required data**
```
root@somewhere:/usr/src/xmrig/build/gcc8# ./xmrig --algo=cn-heavy/xhv --stress
 * ABOUT        XMRig/6.11.0-dev gcc/8.3.0
 * LIBS         libuv/1.41.0 OpenSSL/1.1.1j hwloc/2.4.1
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          Intel(R) Xeon(R) CPU E5-2620 0 @ 2.00GHz (2) 64-bit AES
                L2:3.0 MB L3:30.0 MB 12C/24T NUMA:2
 * MEMORY       54.0/62.9 GB (86%)
                P1-DIMMA1: 4 GB DDR3 @ 1333 MHz M393B5170EH1-CH9  
                P1-DIMMA2: 4 GB DDR3 @ 1333 MHz M393B5170EH1-CH9  
                P1-DIMMB1: 4 GB DDR3 @ 1333 MHz M393B5170EH1-CH9  
                P1-DIMMB2: 4 GB DDR3 @ 1333 MHz M393B5170EH1-CH9  
                P1-DIMMC1: 4 GB DDR3 @ 1333 MHz M393B5170EH1-CH9  
                P1-DIMMC2: 4 GB DDR3 @ 1333 MHz M393B5170EH1-CH9  
                P1-DIMMD1: 4 GB DDR3 @ 1333 MHz M393B5170EH1-CH9  
                P1-DIMMD2: 4 GB DDR3 @ 1333 MHz M393B5170EH1-CH9  
                P2-DIMME1: 4 GB DDR3 @ 1333 MHz M393B5170EH1-CH9  
                P2-DIMME2: 4 GB DDR3 @ 1333 MHz M393B5170EH1-CH9  
                P2-DIMMF1: 4 GB DDR3 @ 1333 MHz M393B5170EH1-CH9  
                P2-DIMMF2: 4 GB DDR3 @ 1333 MHz M393B5170EH1-CH9  
                P2-DIMMG1: 4 GB DDR3 @ 1333 MHz M393B5170EH1-CH9  
                P2-DIMMG2: 4 GB DDR3 @ 1333 MHz M393B5170EH1-CH9  
                P2-DIMMH1: 4 GB DDR3 @ 1333 MHz M393B5170EH1-CH9  
                P2-DIMMH2: 4 GB DDR3 @ 1333 MHz M393B5170EH1-CH9  
 * MOTHERBOARD  Supermicro - X9DRD-7LN4F
 * DONATE       1%
 * ASSEMBLY     auto:intel
 * POOL #1      stratum+ssl://randomx.xmrig.com:443 algo cn-heavy/xhv
 * COMMANDS     hashrate, pause, resume, results, connection
[2021-04-02 23:23:45.857]  net      use pool randomx.xmrig.com:443 TLSv1.3 178.128.242.134
[2021-04-02 23:23:45.857]  net      fingerprint (SHA-256): "052f16d5ed26619bde92fc0ef3e39323c20c513b32166803247eeabfc45c3313"
[2021-04-02 23:23:45.857]  net      new job from randomx.xmrig.com:443 diff 286M algo cn-heavy/xhv height 0
[2021-04-02 23:23:45.862]  msr      register values for "intel" preset have been set successfully (5 ms)
[2021-04-02 23:23:45.862]  cpu      use profile  cn-heavy  (8 threads) scratchpad 4096 KB
[2021-04-02 23:23:45.907]  cpu      thread #1 self-test failed
[2021-04-02 23:23:45.907]  cpu      thread #3 self-test failed
[2021-04-02 23:23:45.908]  cpu      thread #0 self-test failed
[2021-04-02 23:23:45.909]  cpu      thread #2 self-test failed
[2021-04-02 23:23:45.915]  cpu      thread #4 self-test failed
[2021-04-02 23:23:45.915]  cpu      thread #5 self-test failed
[2021-04-02 23:23:45.915]  cpu      thread #6 self-test failed
[2021-04-02 23:23:45.922]  cpu      thread #7 self-test failed
[2021-04-02 23:23:45.922]  cpu      disabled (failed to start threads)
[2021-04-02 23:23:47.172]  signal   Ctrl+C received, exiting
[2021-04-02 23:23:47.173]  cpu      stopped (1 ms)
```
 - Config file not required for stress mode
 - OS: Linux / Debian Buster

**Additional context**
Suspect some of the GCC-related mods recently, pretty sure it worked well just before then.  Retesting some checkout points to ensure it's not some other problem with my compiler/toolchain/deps (it should work before I hit v6.10.x).  I use the `./scripts/build_deps.sh` and build with same compiler as would be used for main app build, to ensure perfect fit.

# Discussion History
## Spudz76 | 2021-04-03T07:04:37+00:00
File `src/crypto/cn/CryptoNight_x86.h` something in the workaround asm stub doesn't work.

Replaced with how it originally was, except more casting to let it know I'm super-serious about 64-bits.
`int64_t q = (int64_t)n / ((int64_t)d | (int64_t)0x5);`

## SChernykh | 2021-04-03T07:27:53+00:00
It works fine with gcc 10.2. It's probably a bug in older GCC versions.

## SChernykh | 2021-04-03T07:32:02+00:00
As far as I can see, it works with gcc 9.3, gcc 10.2 and fails with gcc 8.3. Can you test other versions?

## Spudz76 | 2021-04-03T23:56:29+00:00
Yes, building on a few other test cases now...  It does already seem to be very CPU Model dependent...

## Spudz76 | 2021-04-04T00:03:24+00:00
Exact same checkout and version of `gcc version 8.3.0 (Debian 8.3.0-6) ` but just different CPU (i3-2100) and it passes self-tests fine
```
root@elsewhere:/usr/src/xmrig/build/gcc8# ./xmrig --stress --algo cn-heavy/xhv
 * ABOUT        XMRig/6.11.0-dev gcc/8.3.0
 * LIBS         libuv/1.41.0 OpenSSL/1.1.1j hwloc/2.4.1
 * HUGE PAGES   supported
 * 1GB PAGES    unavailable
 * CPU          Intel(R) Core(TM) i3-2100 CPU @ 3.10GHz (1) 64-bit -AES
                L2:0.5 MB L3:3.0 MB 2C/4T NUMA:1
 * MEMORY       6.5/11.6 GB (56%)
                DIMM_A0: 2 GB DDR3 @ 1333 MHz M378B5773DH0-CH9  
                DIMM_A1: 4 GB DDR3 @ 1333 MHz BLS4G3D1609DS1S00.
                DIMM_B0: 2 GB DDR3 @ 1333 MHz M378B5773DH0-CH9  
                DIMM_B1: 4 GB DDR3 @ 1333 MHz BLS4G3D1609DS1S00.
 * MOTHERBOARD  Dell Inc. - 06D7TR
 * DONATE       1%
 * ASSEMBLY     auto:none
 * POOL #1      stratum+ssl://randomx.xmrig.com:443 algo cn-heavy/xhv
 * COMMANDS     hashrate, pause, resume, results, connection
[2021-04-03 17:00:39.646]  net      use pool randomx.xmrig.com:443 TLSv1.3 178.128.242.134
[2021-04-03 17:00:39.646]  net      fingerprint (SHA-256): "366c41365047d7d49f8bc669274ec20bdecab9c38748e01bedf2818bed747f82"
[2021-04-03 17:00:39.646]  net      new job from randomx.xmrig.com:443 diff 286M algo cn-heavy/xhv height 0
[2021-04-03 17:00:39.646]  cpu      use profile  cn-heavy  (1 thread) scratchpad 4096 KB
[2021-04-03 17:00:39.974]  cpu      READY threads 1/1 (1) huge pages 100% 2/2 memory 4096 KB (327 ms)
[2021-04-03 17:00:43.320]  signal   Ctrl+C received, exiting
[2021-04-03 17:00:43.410]  cpu      stopped (90 ms)
```

## Spudz76 | 2021-04-04T00:08:57+00:00
Both the working and not working CPU models are the same old 32nm Sandy Bridge core, maybe it affects only Xeon Sandy Bridge (as opposed to desktops) for some reason.  Strange, but also I did see the speedup on the ones where it works so it would be cool to fix.

Just noticed another difference, the i3 doesn't have AES.  Locating another desktop i5/i7 that does have AES and same core, but not Xeon.

* `gcc version 8.4.0 (Ubuntu 8.4.0-3ubuntu2)` on `Phenom II X6 1035T` works fine (not a very useful bisect, slightly newer compiler and AMD lol, but for completeness - also another non-AES)

* `gcc version 8.4.0 (Ubuntu 8.4.0-3ubuntu2)` on `i7-4700MQ` crashes (has AES, and fails - also totally different old deps oops)
```
root@thisotherplace:/usr/src/xmrig/build/gcc8$ ./xmrig --stress --algo cn-heavy/xhv
 * ABOUT        XMRig/6.11.0-dev gcc/8.4.0
 * LIBS         libuv/1.34.2 OpenSSL/1.1.1f hwloc/2.1.0
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          Intel(R) Core(TM) i7-4700MQ CPU @ 2.40GHz (1) 64-bit AES
                L2:1.0 MB L3:6.0 MB 4C/8T NUMA:1
 * MEMORY       14.4/15.5 GB (93%)
                DIMM_A0: 4 GB DDR3 @ 1600 MHz M471B5173QH0-YK0  
                DIMM_A1: 4 GB DDR3 @ 1600 MHz M471B5173QH0-YK0  
                DIMM_B0: 4 GB DDR3 @ 1600 MHz M471B5173QH0-YK0  
                DIMM_B1: 4 GB DDR3 @ 1600 MHz M471B5173QH0-YK0  
 * MOTHERBOARD  LENOVO - 20BHA0N9US
 * DONATE       1%
 * ASSEMBLY     auto:intel
 * POOL #1      stratum+ssl://randomx.xmrig.com:443 algo cn-heavy/xhv
 * COMMANDS     hashrate, pause, resume, results, connection
[2021-04-03 18:51:36.991]  net      use pool randomx.xmrig.com:443 TLSv1.3 178.128.242.134
[2021-04-03 18:51:36.991]  net      fingerprint (SHA-256): "366c41365047d7d49f8bc669274ec20bdecab9c38748e01bedf2818bed747f82"
[2021-04-03 18:51:36.991]  net      new job from randomx.xmrig.com:443 diff 286M algo cn-heavy/xhv height 0
[2021-04-03 18:51:36.995]  msr      register values for "intel" preset have been set successfully (4 ms)
[2021-04-03 18:51:36.996]  cpu      use profile  cn-heavy  (2 threads) scratchpad 4096 KB
[2021-04-03 18:51:37.149]  cpu      thread #1 self-test failed
[2021-04-03 18:51:37.152]  cpu      thread #0 self-test failed
[2021-04-03 18:51:37.152]  cpu      disabled (failed to start threads)
[2021-04-03 18:51:39.746]  signal   Ctrl+C received, exiting
[2021-04-03 18:51:39.746]  cpu      stopped (0 ms)
```

## Spudz76 | 2021-04-04T01:05:55+00:00
So then in summary, it seems to be a problem on AES-capable CPUs only, with only gcc-8 (which is the default GCC version on Debian Buster and Ubuntu Focal).  And probably only Intel.

## SChernykh | 2021-04-04T07:03:41+00:00
Ubuntu Focal has gcc 9.3 as default. I'll check what happens with gcc 8.3.

## SChernykh | 2021-04-04T08:17:31+00:00
The problem with gcc-8 is in `add rsi, rdx` instruction which should've been `add rsi, rcx` because `rdx` register is not used in the loop at all. It does use `rdx` instead of `rcx` everywhere if I revert to the old code, so it's a compiler bug.

gcc-7.5, gcc-9.3 and gcc-10.2 all work fine.

```
.L1262:
	mov	QWORD PTR 8[rsp], rsi
	and	ecx, 4194288
	movq	xmm0, QWORD PTR 8[rsp]
	mov	QWORD PTR 8[rsp], rdi
	add	rcx, r10
	movdqa	xmm2, XMMWORD PTR [rcx]
	movhps	xmm0, QWORD PTR 8[rsp]
	aesenc	xmm2, xmm0
	pxor	xmm1, xmm2
	movq	rax, xmm2
	movaps	XMMWORD PTR [rcx], xmm1
	movq	rcx, xmm2
	and	ecx, 4194288
	add	rcx, r10
	mov	r11, QWORD PTR [rcx]
	mov	r12, QWORD PTR 8[rcx]
	mul	r11
	lea	rax, [rax+rdi]
	add	rsi, rdx
	mov	rdi, r12
	mov	QWORD PTR 8[rsp], rsi
	xor	rsi, r11
	movq	xmm1, QWORD PTR 8[rsp]
	xor	rdi, rax
	mov	QWORD PTR 8[rsp], rax
	mov	r11, rsi
	and	r11d, 4194288
	add	r11, r10
	movhps	xmm1, QWORD PTR 8[rsp]
	movups	XMMWORD PTR [rcx], xmm1
	movsx	rcx, DWORD PTR 8[r11]
	mov	r12, QWORD PTR [r11]
	mov	rax, r12
	movdqa	xmm1, xmm2
	cqo
	mov r13, rcx
	or r13, 5
	idiv	r13
	xor	r12, rax
	xor	rcx, rax
	mov	QWORD PTR [r11], r12
	not	rcx
	sub	r8, 1
	jne	.L1262
```

# Action History
- Created by: Spudz76 | 2021-04-03T06:47:42+00:00
- Closed at: 2021-04-06T06:52:52+00:00
