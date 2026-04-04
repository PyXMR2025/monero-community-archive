---
title: 'inlining failed in call to always_inline ‘_mm_aeskeygenassist_si128’:'
source_url: https://github.com/monero-project/monero/issues/5459
author: Raptor3um
assignees: []
labels: []
created_at: '2019-04-18T10:48:22+00:00'
updated_at: '2019-04-18T14:15:12+00:00'
type: issue
status: closed
closed_at: '2019-04-18T14:15:12+00:00'
---

# Original Description
Trying to compile latest from master I receive:

OS: Ubuntu 18.04
cmake: 3.10.2

So far have been unable to resolve it. A kick in the right direction would be appreciated.

```
In file included from crypto/cryptonote/slow-hash.c:369:0:
crypto/cryptonote/slow-hash.c: In function ‘aes_256_assist2’:
/usr/lib/gcc/x86_64-linux-gnu/7/include/wmmintrin.h:87:1: error: inlining failed in call to always_inline ‘_mm_aeskeygenassist_si128’: target specific option mismatch
 _mm_aeskeygenassist_si128 (__m128i __X, const int __C)
 ^~~~~~~~~~~~~~~~~~~~~~~~~
crypto/cryptonote/slow-hash.c:550:8: note: called from here
     t4 = _mm_aeskeygenassist_si128(*t1, 0x00);
     ~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
```


# Discussion History
## moneromooo-monero | 2019-04-18T10:53:12+00:00
What architecture ? What compiler ?

## Raptor3um | 2019-04-18T11:03:39+00:00
gcc is 7.3.0
OS is x64

Thanks!

## moneromooo-monero | 2019-04-18T11:19:03+00:00
Can you be more specific about the architecture ?

## moneromooo-monero | 2019-04-18T11:21:22+00:00
Also, does cmake say anything about AES near the beginning of the build ? You might have to make clean first.

## Raptor3um | 2019-04-18T12:46:31+00:00
I tried make clean first and it did not help, cmake does not mention AES at all.

Architecture:        x86_64
CPU op-mode(s):      32-bit, 64-bit
Byte Order:          Little Endian
CPU(s):              2
On-line CPU(s) list: 0,1
Thread(s) per core:  1
Core(s) per socket:  1
Socket(s):           2
NUMA node(s):        1
Vendor ID:           GenuineIntel
CPU family:          6
Model:               58
Model name:          Intel(R) Xeon(R) CPU E3-1245 V2 @ 3.40GHz
Stepping:            9
CPU MHz:             3392.292
BogoMIPS:            6784.58
Hypervisor vendor:   KVM
Virtualization type: full
L1d cache:           32K
L1i cache:           32K
L2 cache:            256K
L3 cache:            8192K
NUMA node0 CPU(s):   0,1
Flags:               fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ss syscall nx rdtscp lm constant_tsc arch_perfmon rep_good nopl xtopology cpuid pni pclmulqdq ssse3 cx16 pcid sse4_1 sse4_2 x2apic popcnt tsc_deadline_timer aes xsave avx f16c rdrand hypervisor lahf_lm pti ssbd ibrs ibpb stibp fsgsbase tsc_adjust smep erms xsaveopt arat




## moneromooo-monero | 2019-04-18T13:02:45+00:00
That's odd you don't get AES info, the only way I can see that happening is if you're on ARM, which you clearly aren't. Does cmake say anything about "Crypto extensions" ? Better even, make clean again, make again, and post the cmake output on fpaste.org or paste.debian.net.

## Raptor3um | 2019-04-18T14:15:12+00:00
This worked after I completely removed the repo, cloned again and built, really weird but seems ok now.

Thanks again @moneromooo-monero 



# Action History
- Created by: Raptor3um | 2019-04-18T10:48:22+00:00
- Closed at: 2019-04-18T14:15:12+00:00
