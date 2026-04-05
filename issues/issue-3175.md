---
title: 'build error due missing binary operator before token "(" '
source_url: https://github.com/xmrig/xmrig/issues/3175
author: mckaygerhard
assignees: []
labels: []
created_at: '2022-12-09T02:50:46+00:00'
updated_at: '2025-06-18T22:50:11+00:00'
type: issue
status: closed
closed_at: '2025-06-18T22:50:11+00:00'
---

# Original Description
**Describe the bug**
build error on working ancient gcc :

```
[ 94%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/astrobwt/sort_indices2.cpp.o
[ 94%] /opt/xmrig/src/crypto/astrobwt/sort_indices2.cpp:40:24: error: missing binary operator before token "("
 #if __has_cpp_attribute(unlikely)
                        ^
Building C object CMakeFiles/xmrig.dir/src/crypto/astrobwt/xmm6int/salsa20_xmm6int-avx2.c.o
CMakeFiles/xmrig.dir/build.make:5528: recipe for target 'CMakeFiles/xmrig.dir/src/crypto/astrobwt/sort_indices2.cpp.o' failed
make[2]: *** [CMakeFiles/xmrig.dir/src/crypto/astrobwt/sort_indices2.cpp.o] Error 1

```

**To Reproduce**
compiling in gcc 4.8 and 4.7

**Expected behavior**
 compilation

**Required data**
 
 - OS: of course not the crap of guyindows

**Additional context**

related to #3057  


# Discussion History
## Spudz76 | 2022-12-09T02:57:11+00:00
Yeah gcc below 5 (really, 7) is not really going to work.  It's not crazy to require a compiler from 2017 in almost 2023...

## mckaygerhard | 2022-12-09T02:58:12+00:00
it works.. 

just patch 

```
#ifndef __has_cpp_attribute
#define __has_cpp_attribute(x) 0
#endif

#ifndef __has_attribute
#define __has_attribute(x) 0
#endif
```



## mckaygerhard | 2022-12-09T02:59:57+00:00
after patch results in good mining respect newer versions of OS.. 

```
 * ABOUT        XMRig/6.17.1-dev gcc/4.9.2
 * LIBS         libuv/1.34.2 OpenSSL/1.0.2l hwloc/1.11.12
 * HUGE PAGES   supported
 * 1GB PAGES    unavailable
 * CPU          Intel(R) Xeon(R) CPU E31220 @ 3.10GHz (1) 64-bit AES
                L2:1.0 MB L3:8.0 MB 4C/4T NUMA:1
 * MEMORY       6.9/7.8 GB (88%)
                DIMM  1 : 2 GB DDR3 @ 1333 MHz DIMM  1 
                DIMM  2 : 2 GB DDR3 @ 1333 MHz DIMM  2 
                DIMM  3 : 2 GB DDR3 @ 1333 MHz DIMM  3 
                DIMM  4 : 2 GB DDR3 @ 1333 MHz DIMM  4 
 * DONATE       0%
 * ASSEMBLY     auto:intel
 * POOL #1      pool.supportxmr.com:3333 algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled
[2022-12-08 22:54:03.596]  net      use pool pool.supportxmr.com:3333  104.243.43.115
```

# Action History
- Created by: mckaygerhard | 2022-12-09T02:50:46+00:00
- Closed at: 2025-06-18T22:50:11+00:00
