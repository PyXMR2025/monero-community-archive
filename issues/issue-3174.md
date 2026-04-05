---
title: build error due is_trivially_copyable after ixed unaligned memory read in DMI
source_url: https://github.com/xmrig/xmrig/issues/3174
author: mckaygerhard
assignees: []
labels: []
created_at: '2022-12-09T02:39:52+00:00'
updated_at: '2025-06-18T22:51:14+00:00'
type: issue
status: closed
closed_at: '2025-06-18T22:51:14+00:00'
---

# Original Description
**Describe the bug**

error when compiling

```
In file included from /opt/xmrig/src/base/net/stratum/Job.cpp:33:0:
/opt/xmrig/src/base/tools/Alignment.h: In function ‘T xmrig::readUnaligned(const T*)’:
/opt/xmrig/src/base/tools/Alignment.h:33:19: error: ‘is_trivially_copyable’ is not a member of ‘std’
     static_assert(std::is_trivially_copyable<T>::value, "T must be trivially copyable");
                   ^
/opt/xmrig/src/base/tools/Alignment.h:33:47: error: expected primary-expression before ‘>’ token
     static_assert(std::is_trivially_copyable<T>::value, "T must be trivially copyable");
                                               ^
/opt/xmrig/src/base/tools/Alignment.h:33:48: error: ‘::value’ has not been declared
     static_assert(std::is_trivially_copyable<T>::value, "T must be trivially copyable");
                                                ^
/opt/xmrig/src/base/tools/Alignment.h: In function ‘void xmrig::writeUnaligned(T*, T)’:
/opt/xmrig/src/base/tools/Alignment.h:44:19: error: ‘is_trivially_copyable’ is not a member of ‘std’
     static_assert(std::is_trivially_copyable<T>::value, "T must be trivially copyable");
                   ^
/opt/xmrig/src/base/tools/Alignment.h:44:47: error: expected primary-expression before ‘>’ token
     static_assert(std::is_trivially_copyable<T>::value, "T must be trivially copyable");
                                               ^
/opt/xmrig/src/base/tools/Alignment.h:44:48: error: ‘::value’ has not been declared
     static_assert(std::is_trivially_copyable<T>::value, "T must be trivially copyable");
                                                ^
[ 21%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Pool.cpp.o
```

**To Reproduce**

mkdir /opt/xmrig/build && cd /opt/xmrig/build
cmake .. -DWITH_GHOSTRIDER=OFF
make

**Expected behavior**

just a compilaton

**Required data**
 - OS: of course not windows crap

**Additional context**




# Discussion History
## Spudz76 | 2022-12-09T02:53:33+00:00
Your GCC must be antique, below v5, and that won't work because this project and most of the deps are C++11 standard (and moving to C++17)

https://stackoverflow.com/questions/25123458/is-trivially-copyable-is-not-a-member-of-std

## mckaygerhard | 2022-12-09T03:07:22+00:00
the release just can be patched .. 

```
#if __GNUG__ && __GNUC__ < 5
#define IS_TRIVIALLY_COPYABLE(T) __has_trivial_copy(T)
#else
#define IS_TRIVIALLY_COPYABLE(T) std::is_trivially_copyable<T>::value
#endif
```

and just works..  this is a debian wheezy working baremetal also:


```
 * ABOUT        XMRig/6.18.1 gcc/4.8.1
 * LIBS         libuv/1.34.2 OpenSSL/1.0.0 hwloc/1.11.12
 * HUGE PAGES   supported
 * 1GB PAGES    unavailable
 * CPU          Intel(R) Xeon(R) CPU E31220 @ 3.10GHz (1) 64-bit AES
                L2:1.0 MB L3:8.0 MB 4C/4T NUMA:1
 * MEMORY       12.9/16.2 GB (78%)
                DIMM  1 : 4 GB DDR3 @ 1633 MHz DIMM  1 
                DIMM  2 : 4 GB DDR3 @ 1633 MHz DIMM  2 
                DIMM  3 : 4 GB DDR3 @ 1633 MHz DIMM  3 
                DIMM  4 : 4 GB DDR3 @ 1633 MHz DIMM  4 
 * DONATE       0%
 * ASSEMBLY     auto:intel
 * POOL #1      pool.supportxmr.com:3333 algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled
[2022-12-08 22:54:03.596]  net      use pool pool.supportxmr.com:3333
```

## SChernykh | 2022-12-09T08:17:37+00:00
XMRig requires fully C++11 compatible compiler. GCC 4.8.1 theoretically should support C++11, but you also need cmake 3.1 or newer to generate the correct command line for gcc. Instead of tinkering with ancient junk, just update your cmake and gcc/g++

## SChernykh | 2022-12-09T08:27:12+00:00
But no, GCC 4.8.1 will not compile XMRig's code even with `-std=c++11` in command line because it doesn't fully support it - `is_trivially_copyable` is missing. GCC 5 or newer is required, and we have to draw a line somewhere of what compilers we support.

## mckaygerhard | 2022-12-09T11:27:54+00:00
what a crap, i already compiled in debian jessie and LFS 3.6 the xmrig miner.. using older gcc, raising requirements is just ways to put obstacles in the way

just patched the code with the already provided code in second comment

## SChernykh | 2022-12-09T11:32:04+00:00
Yes, your servers are an old crap.

## mckaygerhard | 2022-12-09T13:07:40+00:00
> Yes, your servers are an old crap.

but works more faster.. give me 200 Hz more rather using lasted.. i changed due that.. later after sumarize allt he machines gain a 3Khz more using older software


## Spudz76 | 2022-12-09T15:59:19+00:00
WooOOooOooo 200 hashes you're gonna be so much richer than anyone else

## mckaygerhard | 2022-12-10T14:12:07+00:00
> WooOOooOooo 200 hashes you're gonna be so much richer than anyone else

pretty ignorant.. of course not in one machine.. the case here is that any gain is well welcome

## Spudz76 | 2022-12-10T14:18:47+00:00
cool, it's still not supported.  You could probably get your hashes back by turning off mitigations or uninstalling intel-microcode since that's the only real difference between old junk and a supported revision as far as CPU performance.

## mckaygerhard | 2022-12-12T16:22:07+00:00
> cool, it's still not supported. You could probably get your hashes back by turning off mitigations or uninstalling intel-microcode since that's the only real difference between old junk and a supported revision as far as CPU performance.

already done.. still more performance in older BETTER .. 

## omalisson | 2024-01-17T10:49:52+00:00
> the release just can be patched ..
> 
> ```
> #if __GNUG__ && __GNUC__ < 5
> #define IS_TRIVIALLY_COPYABLE(T) __has_trivial_copy(T)
> #else
> #define IS_TRIVIALLY_COPYABLE(T) std::is_trivially_copyable<T>::value
> #endif
> ```
> 
> and just works.. this is a debian wheezy working baremetal also:
> 
> ```
>  * ABOUT        XMRig/6.18.1 gcc/4.8.1
>  * LIBS         libuv/1.34.2 OpenSSL/1.0.0 hwloc/1.11.12
>  * HUGE PAGES   supported
>  * 1GB PAGES    unavailable
>  * CPU          Intel(R) Xeon(R) CPU E31220 @ 3.10GHz (1) 64-bit AES
>                 L2:1.0 MB L3:8.0 MB 4C/4T NUMA:1
>  * MEMORY       12.9/16.2 GB (78%)
>                 DIMM  1 : 4 GB DDR3 @ 1633 MHz DIMM  1 
>                 DIMM  2 : 4 GB DDR3 @ 1633 MHz DIMM  2 
>                 DIMM  3 : 4 GB DDR3 @ 1633 MHz DIMM  3 
>                 DIMM  4 : 4 GB DDR3 @ 1633 MHz DIMM  4 
>  * DONATE       0%
>  * ASSEMBLY     auto:intel
>  * POOL #1      pool.supportxmr.com:3333 algo auto
>  * COMMANDS     hashrate, pause, resume, results, connection
>  * OPENCL       disabled
>  * CUDA         disabled
> [2022-12-08 22:54:03.596]  net      use pool pool.supportxmr.com:3333
> ```

Good morning!

I have the same problem you faced and I can't solve it with your hack tip.

I'm not a "Dev" nor do I master languages like C, C++ and many others, but with a little knowledge I have I'm trying to adjust the "Alignment.h" file by applying the "if" test but it's showing an error as described below:

[  2%] Built target xmrig-asm
[  9%] Built target ghostrider
[ 11%] Built target argon2-sse2
[ 11%] Built target argon2-avx512f
[ 13%] Built target argon2-avx2
[ 13%] Built target argon2-xop
[ 14%] Built target argon2-ssse3
[ 14%] Built target ethash
[ 16%] Built target argon2
Scanning dependencies of target xmrig
[ 18%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Job.cpp.o
[ 18%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/strategies/FailoverStrategy.cpp.o
In file included from /root/xmrig/src/base/net/stratum/Job.cpp:33:0:
/root/xmrig/src/base/tools/Alignment.h:30:1: error: expected unqualified-id before ‘if’
 if __GNUG__ && __GNUC__ < 5
 ^
/root/xmrig/src/base/tools/Alignment.h:49:1: error: expected unqualified-id before ‘if’
 if __GNUG__ && __GNUC__ < 5
 ^
/root/xmrig/src/base/net/stratum/Job.cpp: In member function ‘bool xmrig::Job::setBlob(const char*)’:
/root/xmrig/src/base/net/stratum/Job.cpp:83:30: error: ‘readUnaligned’ was not declared in this scope
     if (readUnaligned(nonce()) != 0 && !m_nicehash) {
                              ^
At global scope:
cc1plus: warning: unrecognized command line option "-Wno-class-memaccess" [enabled by default]
make[2]: ** [CMakeFiles/xmrig.dir/src/base/net/stratum/Job.cpp.o] Erro 1
make[2]: *** Esperando que os outros processos terminem....
make[1]: ** [CMakeFiles/xmrig.dir/all] Erro 2
make: ** [all] Erro 2

I would really appreciate it if my friend can help me with this adjustment on how to do it!

## mckaygerhard | 2024-01-17T16:02:37+00:00
> In file included from /root/xmrig/src/base/net/stratum/Job.cpp:33:0:
> /root/xmrig/src/base/tools/Alignment.h:30:1: error: expected unqualified-id before ‘if’
> if **GNUG** && **GNUC** < 5

you @omalisson  have a typo here.. that's why is not working


## omalisson | 2024-01-29T12:43:03+00:00
> > In file included from /root/xmrig/src/base/net/stratum/Job.cpp:33:0:
> > /root/xmrig/src/base/tools/Alignment.h:30:1: error: expected unqualified-id before ‘if’
> > if **GNUG** && **GNUC** < 5
> 
> you @omalisson have a typo here.. that's why is not working

Thanks for your response!
At the moment I have suspended the miner's laboratory, but as soon as I return I will correct this error.

# Action History
- Created by: mckaygerhard | 2022-12-09T02:39:52+00:00
- Closed at: 2025-06-18T22:51:14+00:00
