---
title: Slackware 14.2 64-bit Compile error xmrig version 3.1.2
source_url: https://github.com/xmrig/xmrig/issues/1173
author: marcel1974
assignees: []
labels:
- duplicate
created_at: '2019-09-16T04:54:18+00:00'
updated_at: '2019-09-16T10:50:48+00:00'
type: issue
status: closed
closed_at: '2019-09-16T10:38:57+00:00'
---

# Original Description
xmrig 2.14 compiles ok and xmrig version 4 beta compile with no errors
xmrig 3.0.0 to xmrig 3.1.2 output this error.
What is this about?

[  1%] Built target argon2-xop
[  4%] Built target xmrig-asm
[  5%] Built target argon2-avx512f
[  6%] Built target argon2-sse2
[  8%] Built target argon2-ssse3
[ 10%] Built target argon2-avx2
[ 16%] Built target argon2
[ 17%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/cn/CnHash.cpp.o
CMakeFiles/xmrig.dir/build.make:1838: recipe for target 'CMakeFiles/xmrig.dir/src/crypto/cn/CnHash.cpp.o' failed
CMakeFiles/Makefile2:73: recipe for target 'CMakeFiles/xmrig.dir/all' failed
Makefile:83: recipe for target 'all' failed


And Some More


[  1%] Built target argon2-xop
[  4%] Built target xmrig-asm
[  5%] Built target argon2-avx512f
[  6%] Built target argon2-sse2
[  8%] Built target argon2-ssse3
[ 10%] Built target argon2-avx2
[ 16%] Built target argon2
[ 17%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/cn/CnHash.cpp.o
In file included from /xmrig-cpu/xmrig-3.1.2/src/crypto/cn/CnHash.h:34:0,
                 from /xmrig-cpu/xmrig-3.1.2/src/crypto/cn/CnHash.cpp:30:
/xmrig-cpu/xmrig-3.1.2/src/crypto/cn/CnAlgo.h: In instantiation of 'constexpr const size_t xmrig::CnAlgo<(xmrig::Algorithm::Id)6>::m_memory []':
/xmrig-cpu/xmrig-3.1.2/src/crypto/cn/CnAlgo.h:47:61:   required from 'constexpr xmrig::CnAlgo<ALGO>::CnAlgo() [with xmrig::Algorithm::Id ALGO = (xmrig::Algori
thm::Id)6]'
/xmrig-cpu/xmrig-3.1.2/src/crypto/cn/CnHash.cpp:163:62:   required from here
/xmrig-cpu/xmrig-3.1.2/src/crypto/cn/CnAlgo.h:103:35: error: initializer fails to determine size of 'xmrig::CnAlgo<(xmrig::Algorithm::Id)6>::m_memory'
     constexpr const static size_t m_memory[] = {
                                   ^
/xmrig-cpu/xmrig-3.1.2/src/crypto/cn/CnAlgo.h:103:35: error: array must be initialized with a brace-enclosed initializer
/xmrig-cpu/xmrig-3.1.2/src/crypto/cn/CnAlgo.h: In instantiation of 'constexpr xmrig::CnAlgo<ALGO>::CnAlgo() [with xmrig::Algorithm::Id ALGO = (xmrig::Algorith
m::Id)6]':
/xmrig-cpu/xmrig-3.1.2/src/crypto/cn/CnHash.cpp:163:62:   required from here
/xmrig-cpu/xmrig-3.1.2/src/crypto/cn/CnAlgo.h:48:29: error: invalid application of 'sizeof' to incomplete type 'const size_t [] {aka const long unsigned int [
]}'
         static_assert(sizeof(m_memory)     / sizeof(m_memory)[0]     == Algorithm::MAX, "memory table size mismatch");
                             ^
/xmrig-cpu/xmrig-3.1.2/src/crypto/cn/CnAlgo.h: In instantiation of 'constexpr const uint32_t xmrig::CnAlgo<(xmrig::Algorithm::Id)6>::m_iterations []':
/xmrig-cpu/xmrig-3.1.2/src/crypto/cn/CnAlgo.h:49:29:   required from 'constexpr xmrig::CnAlgo<ALGO>::CnAlgo() [with xmrig::Algorithm::Id ALGO = (xmrig::Algori
thm::Id)6]'
/xmrig-cpu/xmrig-3.1.2/src/crypto/cn/CnHash.cpp:163:62:   required from here
/xmrig-cpu/xmrig-3.1.2/src/crypto/cn/CnAlgo.h:142:37: error: initializer fails to determine size of 'xmrig::CnAlgo<(xmrig::Algorithm::Id)6>::m_iterations'
     constexpr const static uint32_t m_iterations[] = {
                                     ^
/xmrig-cpu/xmrig-3.1.2/src/crypto/cn/CnAlgo.h:142:37: error: array must be initialized with a brace-enclosed initializer
/xmrig-cpu/xmrig-3.1.2/src/crypto/cn/CnAlgo.h: In instantiation of 'constexpr xmrig::CnAlgo<ALGO>::CnAlgo() [with xmrig::Algorithm::Id ALGO = (xmrig::Algorith
m::Id)6]':
/xmrig-cpu/xmrig-3.1.2/src/crypto/cn/CnHash.cpp:163:62:   required from here
/xmrig-cpu/xmrig-3.1.2/src/crypto/cn/CnAlgo.h:49:29: error: invalid application of 'sizeof' to incomplete type 'const uint32_t [] {aka const unsigned int []}'
         static_assert(sizeof(m_iterations) / sizeof(m_iterations)[0] == Algorithm::MAX, "iterations table size mismatch");
                             ^
/xmrig-cpu/xmrig-3.1.2/src/crypto/cn/CnAlgo.h: In instantiation of 'constexpr const xmrig::Algorithm::Id xmrig::CnAlgo<(xmrig::Algorithm::Id)6>::m_base []':
/xmrig-cpu/xmrig-3.1.2/src/crypto/cn/CnAlgo.h:50:29:   required from 'constexpr xmrig::CnAlgo<ALGO>::CnAlgo() [with xmrig::Algorithm::Id ALGO = (xmrig::Algori
thm::Id)6]'
/xmrig-cpu/xmrig-3.1.2/src/crypto/cn/CnHash.cpp:163:62:   required from here
/xmrig-cpu/xmrig-3.1.2/src/crypto/cn/CnAlgo.h:181:42: error: initializer fails to determine size of 'xmrig::CnAlgo<(xmrig::Algorithm::Id)6>::m_base'
     constexpr const static Algorithm::Id m_base[] = {


# Discussion History
## xmrig | 2019-09-16T10:37:19+00:00
This bug was already reported and fixed in v4, but fix will not backported to v3, you can use v4 without OpenCL backend (`-DWITH_OPENCL=OFF`) or try use another compiler. v4 for CPU almost identical to v3, except 2 things:
1. Algorithm `cn/wow` removed, and other underlying changes with algorithm handle it it main reason why I'd no like to backport the fix.
2. RandomX dataset initialization is more synchronous, it little slower but much less error prone.
Thank you.

## xmrig | 2019-09-16T10:38:57+00:00
#1140

## marcel1974 | 2019-09-16T10:50:48+00:00
Hi, thank you I had no idea it was opencl or wow related.

# Action History
- Created by: marcel1974 | 2019-09-16T04:54:18+00:00
- Closed at: 2019-09-16T10:38:57+00:00
