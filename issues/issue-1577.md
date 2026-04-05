---
title: does not compile in CentOS 6
source_url: https://github.com/xmrig/xmrig/issues/1577
author: mrdogITC
assignees: []
labels:
- question
created_at: '2020-03-04T13:48:21+00:00'
updated_at: '2020-03-04T16:10:30+00:00'
type: issue
status: closed
closed_at: '2020-03-04T16:10:30+00:00'
---

# Original Description
**Describe the bug**
CentOS release 6.9 (Final)
gcc version 7.3.0 (GCC)
cmake version 2.8.12.2

I changed "-Ofast" to "-O2" and "-std = c ++ 11" to "-std = c ++ 0x" in the flags.cmake file.

I Execute:
cmake3 .. -DXMRIG_DEPS=scripts/deps
make -j$(nproc)

output:
Scanning dependencies of target xmrig-asm
[  1%] Building ASM object CMakeFiles/xmrig-asm.dir/src/crypto/cn/asm/cn_main_loop.S.o
[  1%] Building ASM object CMakeFiles/xmrig-asm.dir/src/crypto/cn/asm/CryptonightR_template.S.o
[  2%] Linking C static library libxmrig-asm.a
[  2%] Built target xmrig-asm
Scanning dependencies of target argon2-avx2
[  2%] Building C object src/3rdparty/argon2/CMakeFiles/argon2-avx2.dir/arch/x86_64/lib/argon2-avx2.c.o
[  3%] Linking C static library libargon2-avx2.a
[  3%] Built target argon2-avx2
Scanning dependencies of target argon2-avx512f
[  3%] Building C object src/3rdparty/argon2/CMakeFiles/argon2-avx512f.dir/arch/x86_64/lib/argon2-avx512f.c.o
[  4%] Linking C static library libargon2-avx512f.a
[  4%] Built target argon2-avx512f
Scanning dependencies of target argon2-xop
[  5%] Building C object src/3rdparty/argon2/CMakeFiles/argon2-xop.dir/arch/x86_64/lib/argon2-xop.c.o
[  5%] Linking C static library libargon2-xop.a
[  5%] Built target argon2-xop
Scanning dependencies of target argon2-ssse3
[  6%] Building C object src/3rdparty/argon2/CMakeFiles/argon2-ssse3.dir/arch/x86_64/lib/argon2-ssse3.c.o
[  6%] Linking C static library libargon2-ssse3.a
[  6%] Built target argon2-ssse3
Scanning dependencies of target argon2-sse2
[  6%] Building C object src/3rdparty/argon2/CMakeFiles/argon2-sse2.dir/arch/x86_64/lib/argon2-sse2.c.o
[  6%] Linking C static library libargon2-sse2.a
[  6%] Built target argon2-sse2
Scanning dependencies of target argon2
[  6%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/argon2.c.o
[  6%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/core.c.o
[  7%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/encoding.c.o
[  7%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/genkat.c.o
[  8%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/impl-select.c.o
[  8%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/blake2/blake2.c.o
[  9%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/arch/x86_64/lib/argon2-arch.c.o
[  9%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/arch/x86_64/lib/cpu-flags.c.o
[ 10%] Linking C static library libargon2.a
[ 10%] Built target argon2
Scanning dependencies of target xmrig
[ 11%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuLaunchData.cpp.o
In file included from /root/xmrig/src/backend/cpu/CpuLaunchData.h:33,
                 from /root/xmrig/src/backend/cpu/CpuLaunchData.cpp:27:
/root/xmrig/src/crypto/common/Nonce.h:29:18: error: atomic: No such file or directory
In file included from /root/xmrig/src/crypto/cn/CnAlgo.h:34,
                 from /root/xmrig/src/crypto/cn/CnHash.h:34,
                 from /root/xmrig/src/backend/cpu/CpuLaunchData.h:30,
                 from /root/xmrig/src/backend/cpu/CpuLaunchData.cpp:27:
/root/xmrig/src/crypto/common/Algorithm.h:118: error: ISO C++ forbids initialization of member ‘m_id’
/root/xmrig/src/crypto/common/Algorithm.h:118: error: making ‘m_id’ static
/root/xmrig/src/crypto/common/Algorithm.h:118: error: ISO C++ forbids in-class initialization of non-const static member ‘m_id’
In file included from /root/xmrig/src/crypto/cn/CnAlgo.h:34,
                 from /root/xmrig/src/crypto/cn/CnHash.h:34,
                 from /root/xmrig/src/backend/cpu/CpuLaunchData.h:30,
                 from /root/xmrig/src/backend/cpu/CpuLaunchData.cpp:27:
/root/xmrig/src/crypto/common/Algorithm.h: In constructor ‘xmrig::Algorithm::Algorithm(const char*)’:
/root/xmrig/src/crypto/common/Algorithm.h:90: error: ‘xmrig::Algorithm::Id xmrig::Algorithm::m_id’ is a static data member; it can only be initialized at its definition
/root/xmrig/src/crypto/common/Algorithm.h: In constructor ‘xmrig::Algorithm::Algorithm(xmrig::Algorithm::Id)’:
/root/xmrig/src/crypto/common/Algorithm.h:91: error: ‘xmrig::Algorithm::Id xmrig::Algorithm::m_id’ is a static data member; it can only be initialized at its definition
In file included from /root/xmrig/src/crypto/cn/CnAlgo.h:34,
                 from /root/xmrig/src/crypto/cn/CnHash.h:34,
                 from /root/xmrig/src/backend/cpu/CpuLaunchData.h:30,
                 from /root/xmrig/src/backend/cpu/CpuLaunchData.cpp:27:
/root/xmrig/src/crypto/common/Algorithm.h: At global scope:
/root/xmrig/src/crypto/common/Algorithm.h:122: error: expected nested-name-specifier before ‘Algorithms’
/root/xmrig/src/crypto/common/Algorithm.h:122: error: ‘Algorithms’ has not been declared
/root/xmrig/src/crypto/common/Algorithm.h:122: error: expected ‘;’ before ‘=’ token
/root/xmrig/src/crypto/common/Algorithm.h:122: error: expected unqualified-id before ‘=’ token
In file included from /root/xmrig/src/crypto/cn/CnHash.h:34,
                 from /root/xmrig/src/backend/cpu/CpuLaunchData.h:30,
                 from /root/xmrig/src/backend/cpu/CpuLaunchData.cpp:27:
/root/xmrig/src/crypto/cn/CnAlgo.h:45: error: ‘constexpr’ does not name a type
/root/xmrig/src/crypto/cn/CnAlgo.h:47: error: ISO C++ forbids declaration of ‘constexpr’ with no type
/root/xmrig/src/crypto/cn/CnAlgo.h:47: error: expected ‘;’ before ‘inline’
In file included from /root/xmrig/src/crypto/cn/CnHash.h:34,
                 from /root/xmrig/src/backend/cpu/CpuLaunchData.h:30,
                 from /root/xmrig/src/backend/cpu/CpuLaunchData.cpp:27:
/root/xmrig/src/crypto/cn/CnAlgo.h:48: error: expected ‘;’ before ‘constexpr’
/root/xmrig/src/crypto/cn/CnAlgo.h:48: error: ISO C++ forbids declaration of ‘constexpr’ with no type
/root/xmrig/src/crypto/cn/CnAlgo.h:48: error: expected ‘;’ before ‘inline’
/root/xmrig/src/crypto/cn/CnAlgo.h:49: error: expected ‘;’ before ‘constexpr’
/root/xmrig/src/crypto/cn/CnAlgo.h:49: error: ISO C++ forbids declaration of ‘constexpr’ with no type
/root/xmrig/src/crypto/cn/CnAlgo.h:49: error: expected ‘;’ before ‘inline’
/root/xmrig/src/crypto/cn/CnAlgo.h:50: error: expected ‘;’ before ‘constexpr’
/root/xmrig/src/crypto/cn/CnAlgo.h:50: error: ISO C++ forbids declaration of ‘constexpr’ with no type
/root/xmrig/src/crypto/cn/CnAlgo.h:50: error: expected ‘;’ before ‘inline’
/root/xmrig/src/crypto/cn/CnAlgo.h:51: error: expected ‘;’ before ‘constexpr’
/root/xmrig/src/crypto/cn/CnAlgo.h:51: error: ISO C++ forbids declaration of ‘constexpr’ with no type
/root/xmrig/src/crypto/cn/CnAlgo.h:51: error: expected ‘;’ before ‘inline’
/root/xmrig/src/crypto/cn/CnAlgo.h:52: error: expected ‘;’ before ‘constexpr’
/root/xmrig/src/crypto/cn/CnAlgo.h:52: error: ISO C++ forbids declaration of ‘constexpr’ with no type
/root/xmrig/src/crypto/cn/CnAlgo.h:52: error: expected ‘;’ before ‘inline’
/root/xmrig/src/crypto/cn/CnAlgo.h:54: error: expected ‘;’ before ‘inline’
/root/xmrig/src/crypto/cn/CnAlgo.h:192: error: ISO C++ forbids declaration of ‘constexpr’ with no type
/root/xmrig/src/crypto/cn/CnAlgo.h:192: error: expected ‘;’ before ‘const’
/root/xmrig/src/crypto/cn/CnAlgo.h:193: error: ISO C++ forbids declaration of ‘constexpr’ with no type
/root/xmrig/src/crypto/cn/CnAlgo.h:193: error: expected ‘;’ before ‘const’
/root/xmrig/src/crypto/cn/CnAlgo.h: In static member function ‘static size_t xmrig::CnAlgo<ALGO>::memory(xmrig::Algorithm::Id)’:
/root/xmrig/src/crypto/cn/CnAlgo.h:58: error: ‘CN_MEMORY’ was not declared in this scope
/root/xmrig/src/crypto/cn/CnAlgo.h: In static member function ‘static uint32_t xmrig::CnAlgo<ALGO>::iterations(xmrig::Algorithm::Id)’:
/root/xmrig/src/crypto/cn/CnAlgo.h:84: error: ‘CN_ITER’ was not declared in this scope
/root/xmrig/src/crypto/cn/CnAlgo.h: At global scope:
/root/xmrig/src/crypto/cn/CnAlgo.h:197: error: expected constructor, destructor, or type conversion before ‘inline’
/root/xmrig/src/crypto/cn/CnAlgo.h:198: error: expected constructor, destructor, or type conversion before ‘inline’
/root/xmrig/src/crypto/cn/CnAlgo.h:199: error: expected constructor, destructor, or type conversion before ‘inline’
/root/xmrig/src/crypto/cn/CnAlgo.h:200: error: expected constructor, destructor, or type conversion before ‘inline’
/root/xmrig/src/crypto/cn/CnAlgo.h:201: error: expected constructor, destructor, or type conversion before ‘inline’
/root/xmrig/src/crypto/cn/CnAlgo.h:202: error: expected constructor, destructor, or type conversion before ‘inline’
/root/xmrig/src/crypto/cn/CnAlgo.h:203: error: expected constructor, destructor, or type conversion before ‘inline’
/root/xmrig/src/crypto/cn/CnAlgo.h:204: error: expected constructor, destructor, or type conversion before ‘inline’
/root/xmrig/src/crypto/cn/CnAlgo.h:205: error: expected constructor, destructor, or type conversion before ‘inline’
/root/xmrig/src/crypto/cn/CnAlgo.h:206: error: expected constructor, destructor, or type conversion before ‘inline’
/root/xmrig/src/crypto/cn/CnAlgo.h:209: error: expected constructor, destructor, or type conversion before ‘inline’
/root/xmrig/src/crypto/cn/CnAlgo.h:210: error: expected constructor, destructor, or type conversion before ‘inline’
/root/xmrig/src/crypto/cn/CnAlgo.h:211: error: expected constructor, destructor, or type conversion before ‘inline’
/root/xmrig/src/crypto/cn/CnAlgo.h:212: error: expected constructor, destructor, or type conversion before ‘inline’
/root/xmrig/src/crypto/cn/CnAlgo.h:213: error: expected constructor, destructor, or type conversion before ‘inline’
/root/xmrig/src/crypto/cn/CnAlgo.h:214: error: expected constructor, destructor, or type conversion before ‘inline’
/root/xmrig/src/crypto/cn/CnAlgo.h:215: error: expected constructor, destructor, or type conversion before ‘inline’
/root/xmrig/src/crypto/cn/CnAlgo.h:216: error: expected constructor, destructor, or type conversion before ‘inline’
/root/xmrig/src/crypto/cn/CnAlgo.h:217: error: expected constructor, destructor, or type conversion before ‘inline’
/root/xmrig/src/crypto/cn/CnAlgo.h:218: error: expected constructor, destructor, or type conversion before ‘inline’
/root/xmrig/src/crypto/cn/CnAlgo.h:219: error: expected constructor, destructor, or type conversion before ‘inline’
/root/xmrig/src/crypto/cn/CnAlgo.h:220: error: expected constructor, destructor, or type conversion before ‘inline’
/root/xmrig/src/crypto/cn/CnAlgo.h:221: error: expected constructor, destructor, or type conversion before ‘inline’
/root/xmrig/src/crypto/cn/CnAlgo.h:222: error: expected constructor, destructor, or type conversion before ‘inline’
/root/xmrig/src/crypto/cn/CnAlgo.h:225: error: expected constructor, destructor, or type conversion before ‘inline’
/root/xmrig/src/crypto/cn/CnAlgo.h:226: error: expected constructor, destructor, or type conversion before ‘inline’
/root/xmrig/src/crypto/cn/CnAlgo.h:227: error: expected constructor, destructor, or type conversion before ‘inline’
/root/xmrig/src/crypto/cn/CnAlgo.h:228: error: expected constructor, destructor, or type conversion before ‘inline’
/root/xmrig/src/crypto/cn/CnAlgo.h:229: error: expected constructor, destructor, or type conversion before ‘inline’
/root/xmrig/src/crypto/cn/CnAlgo.h:230: error: expected constructor, destructor, or type conversion before ‘inline’
/root/xmrig/src/crypto/cn/CnAlgo.h:231: error: expected constructor, destructor, or type conversion before ‘inline’
/root/xmrig/src/crypto/cn/CnAlgo.h:234: error: expected constructor, destructor, or type conversion before ‘inline’
/root/xmrig/src/crypto/cn/CnAlgo.h:235: error: expected constructor, destructor, or type conversion before ‘inline’
In file included from /root/xmrig/src/crypto/cn/CnHash.h:35,
                 from /root/xmrig/src/backend/cpu/CpuLaunchData.h:30,
                 from /root/xmrig/src/backend/cpu/CpuLaunchData.cpp:27:
/root/xmrig/src/crypto/common/Assembly.h:68: error: ISO C++ forbids initialization of member ‘m_id’
/root/xmrig/src/crypto/common/Assembly.h:68: error: making ‘m_id’ static
/root/xmrig/src/crypto/common/Assembly.h:68: error: ISO C++ forbids in-class initialization of non-const static member ‘m_id’
/root/xmrig/src/crypto/common/Assembly.h: In constructor ‘xmrig::Assembly::Assembly(xmrig::Assembly::Id)’:
/root/xmrig/src/crypto/common/Assembly.h:49: error: ‘xmrig::Assembly::Id xmrig::Assembly::m_id’ is a static data member; it can only be initialized at its definition
/root/xmrig/src/crypto/common/Assembly.h: In constructor ‘xmrig::Assembly::Assembly(const char*)’:
/root/xmrig/src/crypto/common/Assembly.h:50: error: ‘xmrig::Assembly::Id xmrig::Assembly::m_id’ is a static data member; it can only be initialized at its definition
/root/xmrig/src/crypto/common/Assembly.h: In constructor ‘xmrig::Assembly::Assembly(const rapidjson::Value&)’:
/root/xmrig/src/crypto/common/Assembly.h:51: error: ‘xmrig::Assembly::Id xmrig::Assembly::m_id’ is a static data member; it can only be initialized at its definition
In file included from /root/xmrig/src/backend/cpu/CpuLaunchData.h:30,
                 from /root/xmrig/src/backend/cpu/CpuLaunchData.cpp:27:
/root/xmrig/src/crypto/cn/CnHash.h: At global scope:
/root/xmrig/src/crypto/cn/CnHash.h:44: error: expected nested-name-specifier before ‘cn_hash_fun’
/root/xmrig/src/crypto/cn/CnHash.h:44: error: ‘cn_hash_fun’ has not been declared
/root/xmrig/src/crypto/cn/CnHash.h:44: error: expected ‘;’ before ‘=’ token
/root/xmrig/src/crypto/cn/CnHash.h:44: error: expected unqualified-id before ‘=’ token
/root/xmrig/src/crypto/cn/CnHash.h:45: error: expected nested-name-specifier before ‘cn_mainloop_fun’
/root/xmrig/src/crypto/cn/CnHash.h:45: error: ‘cn_mainloop_fun’ has not been declared
/root/xmrig/src/crypto/cn/CnHash.h:45: error: expected ‘;’ before ‘=’ token
/root/xmrig/src/crypto/cn/CnHash.h:45: error: expected unqualified-id before ‘=’ token
/root/xmrig/src/crypto/cn/CnHash.h:68: error: ‘cn_hash_fun’ does not name a type
/root/xmrig/src/crypto/cn/CnHash.h:71: error: ‘cn_hash_fun’ does not name a type
In file included from /root/xmrig/src/backend/cpu/CpuLaunchData.h:33,
                 from /root/xmrig/src/backend/cpu/CpuLaunchData.cpp:27:
/root/xmrig/src/crypto/common/Nonce.h:61: error: ISO C++ forbids declaration of ‘atomic’ with no type
/root/xmrig/src/crypto/common/Nonce.h:61: error: invalid use of ‘::’
/root/xmrig/src/crypto/common/Nonce.h:61: error: expected ‘;’ before ‘<’ token
/root/xmrig/src/crypto/common/Nonce.h:62: error: ISO C++ forbids declaration of ‘atomic’ with no type
/root/xmrig/src/crypto/common/Nonce.h:62: error: invalid use of ‘::’
/root/xmrig/src/crypto/common/Nonce.h:62: error: expected ‘;’ before ‘<’ token
/root/xmrig/src/crypto/common/Nonce.h:55: error: ‘nullptr’ was not declared in this scope
In file included from /root/xmrig/src/backend/cpu/CpuLaunchData.h:33,
                 from /root/xmrig/src/backend/cpu/CpuLaunchData.cpp:27:
/root/xmrig/src/crypto/common/Nonce.h: In static member function ‘static bool xmrig::Nonce::isOutdated(xmrig::Nonce::Backend, uint64_t)’:
/root/xmrig/src/crypto/common/Nonce.h:48: error: ‘m_sequence’ was not declared in this scope
/root/xmrig/src/crypto/common/Nonce.h:48: error: ‘memory_order_relaxed’ is not a member of ‘std’
In file included from /root/xmrig/src/backend/cpu/CpuLaunchData.h:33,
                 from /root/xmrig/src/backend/cpu/CpuLaunchData.cpp:27:
/root/xmrig/src/crypto/common/Nonce.h: In static member function ‘static bool xmrig::Nonce::isPaused()’:
/root/xmrig/src/crypto/common/Nonce.h:49: error: ‘m_paused’ was not declared in this scope
/root/xmrig/src/crypto/common/Nonce.h:49: error: ‘memory_order_relaxed’ is not a member of ‘std’
/root/xmrig/src/crypto/common/Nonce.h: In static member function ‘static uint64_t xmrig::Nonce::sequence(xmrig::Nonce::Backend)’:
/root/xmrig/src/crypto/common/Nonce.h:50: error: ‘m_sequence’ was not declared in this scope
/root/xmrig/src/crypto/common/Nonce.h:50: error: ‘memory_order_relaxed’ is not a member of ‘std’
/root/xmrig/src/crypto/common/Nonce.h: In static member function ‘static void xmrig::Nonce::pause(bool)’:
/root/xmrig/src/crypto/common/Nonce.h:51: error: ‘m_paused’ was not declared in this scope
/root/xmrig/src/crypto/common/Nonce.h: In static member function ‘static void xmrig::Nonce::stop(xmrig::Nonce::Backend)’:
/root/xmrig/src/crypto/common/Nonce.h:52: error: ‘m_sequence’ was not declared in this scope
/root/xmrig/src/crypto/common/Nonce.h: In static member function ‘static void xmrig::Nonce::touch(xmrig::Nonce::Backend)’:
/root/xmrig/src/crypto/common/Nonce.h:53: error: ‘m_sequence’ was not declared in this scope
In file included from /root/xmrig/src/backend/cpu/CpuLaunchData.cpp:27:
/root/xmrig/src/backend/cpu/CpuLaunchData.h: At global scope:
/root/xmrig/src/backend/cpu/CpuLaunchData.h:52: error: ISO C++ forbids declaration of ‘constexpr’ with no type
/root/xmrig/src/backend/cpu/CpuLaunchData.h:52: error: ‘constexpr’ declared as an ‘inline’ field
/root/xmrig/src/backend/cpu/CpuLaunchData.h:52: error: expected ‘;’ before ‘static’
/root/xmrig/src/backend/cpu/CpuLaunchData.h:54: error: expected ‘;’ before ‘inline’
In file included from /root/xmrig/src/backend/common/Threads.h:33,
                 from /root/xmrig/src/backend/cpu/CpuConfig.h:29,
                 from /root/xmrig/src/backend/cpu/CpuLaunchData.cpp:30:
/root/xmrig/src/base/tools/String.h:51: error: expected ‘;’ before ‘noexcept’
In file included from /root/xmrig/src/backend/common/Threads.h:33,
                 from /root/xmrig/src/backend/cpu/CpuConfig.h:29,
                 from /root/xmrig/src/backend/cpu/CpuLaunchData.cpp:30:
/root/xmrig/src/base/tools/String.h:53: error: expected ‘;’ before ‘String’
/root/xmrig/src/base/tools/String.h:83: error: declaration of ‘operator=’ as non-function
/root/xmrig/src/base/tools/String.h:83: error: expected ‘;’ before ‘(’ token
/root/xmrig/src/base/tools/String.h:84: error: expected ‘;’ before ‘inline’
/root/xmrig/src/base/tools/String.h:84: error: expected ‘;’ before ‘noexcept’
/root/xmrig/src/base/tools/String.h:86: error: expected ‘;’ before ‘rapidjson’
/root/xmrig/src/base/tools/String.h:100: error: ‘nullptr’ was not declared in this scope
/root/xmrig/src/base/tools/String.h:100: error: ISO C++ forbids initialization of member ‘m_data’
/root/xmrig/src/base/tools/String.h:100: error: making ‘m_data’ static
/root/xmrig/src/base/tools/String.h:100: error: invalid in-class initialization of static data member of non-integral type ‘char*’
/root/xmrig/src/base/tools/String.h:101: error: ISO C++ forbids initialization of member ‘m_size’
/root/xmrig/src/base/tools/String.h:101: error: making ‘m_size’ static
/root/xmrig/src/base/tools/String.h:101: error: ISO C++ forbids in-class initialization of non-const static member ‘m_size’
In file included from /root/xmrig/src/backend/common/Threads.h:33,
                 from /root/xmrig/src/backend/cpu/CpuConfig.h:29,
                 from /root/xmrig/src/backend/cpu/CpuLaunchData.cpp:30:
/root/xmrig/src/base/tools/String.h: In constructor ‘xmrig::String::String(char*)’:
/root/xmrig/src/base/tools/String.h:50: error: class ‘xmrig::String’ does not have any field named ‘m_data’
/root/xmrig/src/base/tools/String.h:50: error: ‘size_t xmrig::String::m_size’ is a static data member; it can only be initialized at its definition
/root/xmrig/src/base/tools/String.h:50: error: ‘nullptr’ was not declared in this scope
In file included from /root/xmrig/src/backend/common/Threads.h:33,
                 from /root/xmrig/src/backend/cpu/CpuConfig.h:29,
                 from /root/xmrig/src/backend/cpu/CpuLaunchData.cpp:30:
/root/xmrig/src/base/tools/String.h: In destructor ‘xmrig::String::~String()’:
/root/xmrig/src/base/tools/String.h:57: error: ‘m_data’ was not declared in this scope
/root/xmrig/src/base/tools/String.h: In member function ‘bool xmrig::String::contains(const char*) const’:
/root/xmrig/src/base/tools/String.h:64: error: ‘m_data’ was not declared in this scope
/root/xmrig/src/base/tools/String.h:64: error: ‘nullptr’ was not declared in this scope
/root/xmrig/src/base/tools/String.h: In member function ‘bool xmrig::String::isNull() const’:
/root/xmrig/src/base/tools/String.h:68: error: ‘m_data’ was not declared in this scope
/root/xmrig/src/base/tools/String.h:68: error: ‘nullptr’ was not declared in this scope
/root/xmrig/src/base/tools/String.h: In member function ‘char* xmrig::String::data()’:
/root/xmrig/src/base/tools/String.h:69: error: ‘m_data’ was not declared in this scope
/root/xmrig/src/base/tools/String.h: In member function ‘const char* xmrig::String::data() const’:
/root/xmrig/src/base/tools/String.h:70: error: ‘m_data’ was not declared in this scope
/root/xmrig/src/base/tools/String.h: In member function ‘xmrig::String::operator const char*() const’:
/root/xmrig/src/base/tools/String.h:79: error: ‘m_data’ was not declared in this scope
In file included from /root/xmrig/src/backend/cpu/CpuThreads.h:32,
                 from /root/xmrig/src/backend/cpu/CpuConfig.h:31,
                 from /root/xmrig/src/backend/cpu/CpuLaunchData.cpp:30:
/root/xmrig/src/backend/cpu/CpuThread.h: At global scope:
/root/xmrig/src/backend/cpu/CpuThread.h:38: error: ‘constexpr’ does not name a type
/root/xmrig/src/backend/cpu/CpuThread.h:39: error: ‘constexpr’ does not name a type
In file included from /root/xmrig/src/backend/cpu/CpuThreads.h:32,
                 from /root/xmrig/src/backend/cpu/CpuConfig.h:31,
                 from /root/xmrig/src/backend/cpu/CpuLaunchData.cpp:30:
/root/xmrig/src/backend/cpu/CpuThread.h:54: error: ISO C++ forbids initialization of member ‘m_affinity’
/root/xmrig/src/backend/cpu/CpuThread.h:54: error: making ‘m_affinity’ static
/root/xmrig/src/backend/cpu/CpuThread.h:54: error: ISO C++ forbids in-class initialization of non-const static member ‘m_affinity’
/root/xmrig/src/backend/cpu/CpuThread.h:55: error: ISO C++ forbids initialization of member ‘m_intensity’
/root/xmrig/src/backend/cpu/CpuThread.h:55: error: making ‘m_intensity’ static
/root/xmrig/src/backend/cpu/CpuThread.h:55: error: ISO C++ forbids in-class initialization of non-const static member ‘m_intensity’
In file included from /root/xmrig/src/backend/cpu/CpuConfig.h:31,
                 from /root/xmrig/src/backend/cpu/CpuLaunchData.cpp:30:
/root/xmrig/src/backend/cpu/CpuThreads.h:66: error: ISO C++ forbids initialization of member ‘m_format’
/root/xmrig/src/backend/cpu/CpuThreads.h:66: error: making ‘m_format’ static
/root/xmrig/src/backend/cpu/CpuThreads.h:66: error: ISO C++ forbids in-class initialization of non-const static member ‘m_format’
/root/xmrig/src/backend/cpu/CpuThreads.h:67: error: ISO C++ forbids initialization of member ‘m_affinity’
/root/xmrig/src/backend/cpu/CpuThreads.h:67: error: making ‘m_affinity’ static
/root/xmrig/src/backend/cpu/CpuThreads.h:67: error: ISO C++ forbids in-class initialization of non-const static member ‘m_affinity’
/root/xmrig/src/backend/cpu/CpuThreads.h: In constructor ‘std::vector<_Tp, _Alloc>::vector(size_t, const _Tp&, const _Alloc&) [with _Tp = xmrig::CpuThread, _Alloc = std::allocator<xmrig::CpuThread>]’:
/root/xmrig/src/backend/cpu/CpuThreads.h:42: error: no matching function for call to ‘xmrig::CpuThread::CpuThread()’
/root/xmrig/src/backend/cpu/CpuThread.h:41: note: candidates are: xmrig::CpuThread::CpuThread(const rapidjson::Value&)
/root/xmrig/src/backend/cpu/CpuThread.h:36: note:                 xmrig::CpuThread::CpuThread(const xmrig::CpuThread&)
/root/xmrig/src/backend/cpu/CpuThreads.h: In member function ‘void xmrig::CpuThreads::add(int64_t, uint32_t)’:
/root/xmrig/src/backend/cpu/CpuThreads.h:51: error: no matching function for call to ‘xmrig::CpuThread::CpuThread(int64_t&, uint32_t&)’
/root/xmrig/src/backend/cpu/CpuThread.h:41: note: candidates are: xmrig::CpuThread::CpuThread(const rapidjson::Value&)
/root/xmrig/src/backend/cpu/CpuThread.h:36: note:                 xmrig::CpuThread::CpuThread(const xmrig::CpuThread&)
In file included from /root/xmrig/src/backend/cpu/CpuLaunchData.cpp:30:
/root/xmrig/src/backend/cpu/CpuConfig.h: At global scope:
/root/xmrig/src/backend/cpu/CpuConfig.h:72: error: ISO C++ forbids initialization of member ‘m_aes’
/root/xmrig/src/backend/cpu/CpuConfig.h:72: error: making ‘m_aes’ static
/root/xmrig/src/backend/cpu/CpuConfig.h:72: error: ISO C++ forbids in-class initialization of non-const static member ‘m_aes’
/root/xmrig/src/backend/cpu/CpuConfig.h:74: error: ISO C++ forbids initialization of member ‘m_enabled’
/root/xmrig/src/backend/cpu/CpuConfig.h:74: error: making ‘m_enabled’ static
/root/xmrig/src/backend/cpu/CpuConfig.h:74: error: ISO C++ forbids in-class initialization of non-const static member ‘m_enabled’
/root/xmrig/src/backend/cpu/CpuConfig.h:75: error: ISO C++ forbids initialization of member ‘m_hugePages’
/root/xmrig/src/backend/cpu/CpuConfig.h:75: error: making ‘m_hugePages’ static
/root/xmrig/src/backend/cpu/CpuConfig.h:75: error: ISO C++ forbids in-class initialization of non-const static member ‘m_hugePages’
/root/xmrig/src/backend/cpu/CpuConfig.h:76: error: ISO C++ forbids initialization of member ‘m_shouldSave’
/root/xmrig/src/backend/cpu/CpuConfig.h:76: error: making ‘m_shouldSave’ static
/root/xmrig/src/backend/cpu/CpuConfig.h:76: error: ISO C++ forbids in-class initialization of non-const static member ‘m_shouldSave’
/root/xmrig/src/backend/cpu/CpuConfig.h:77: error: ISO C++ forbids initialization of member ‘m_yield’
/root/xmrig/src/backend/cpu/CpuConfig.h:77: error: making ‘m_yield’ static
/root/xmrig/src/backend/cpu/CpuConfig.h:77: error: ISO C++ forbids in-class initialization of non-const static member ‘m_yield’
/root/xmrig/src/backend/cpu/CpuConfig.h:78: error: ISO C++ forbids initialization of member ‘m_memoryPool’
/root/xmrig/src/backend/cpu/CpuConfig.h:78: error: making ‘m_memoryPool’ static
/root/xmrig/src/backend/cpu/CpuConfig.h:78: error: ISO C++ forbids in-class initialization of non-const static member ‘m_memoryPool’
/root/xmrig/src/backend/cpu/CpuConfig.h:79: error: ISO C++ forbids initialization of member ‘m_priority’
/root/xmrig/src/backend/cpu/CpuConfig.h:79: error: making ‘m_priority’ static
/root/xmrig/src/backend/cpu/CpuConfig.h:79: error: ISO C++ forbids in-class initialization of non-const static member ‘m_priority’
/root/xmrig/src/backend/cpu/CpuConfig.h:82: error: ISO C++ forbids initialization of member ‘m_limit’
/root/xmrig/src/backend/cpu/CpuConfig.h:82: error: making ‘m_limit’ static
/root/xmrig/src/backend/cpu/CpuConfig.h:82: error: ISO C++ forbids in-class initialization of non-const static member ‘m_limit’
cc1plus: warning: unrecognized command line option "-Wno-class-memaccess"
make[2]: *** [CMakeFiles/xmrig.dir/src/backend/cpu/CpuLaunchData.cpp.o] Error 1
make[1]: *** [CMakeFiles/xmrig.dir/all] Error 2
make: *** [all] Error 2


# Discussion History
## xmrig | 2020-03-04T14:08:54+00:00
Just change `-std=c++0x` back to `-std=c++11`.
Thank you.

## mrdogITC | 2020-03-04T14:13:13+00:00
[root@vm123 build]# make
Scanning dependencies of target argon2-avx2
[  1%] Building C object src/3rdparty/argon2/CMakeFiles/argon2-avx2.dir/arch/x86_64/lib/argon2-avx2.c.o
Linking C static library libargon2-avx2.a
[  1%] Built target argon2-avx2
Scanning dependencies of target xmrig-asm
[  1%] Building ASM object CMakeFiles/xmrig-asm.dir/src/crypto/cn/asm/cn_main_loop.S.o
[  2%] Building ASM object CMakeFiles/xmrig-asm.dir/src/crypto/cn/asm/CryptonightR_template.S.o
Linking C static library libxmrig-asm.a
[  2%] Built target xmrig-asm
Scanning dependencies of target argon2-sse2
[  3%] Building C object src/3rdparty/argon2/CMakeFiles/argon2-sse2.dir/arch/x86_64/lib/argon2-sse2.c.o
Linking C static library libargon2-sse2.a
[  3%] Built target argon2-sse2
Scanning dependencies of target argon2-avx512f
[  3%] Building C object src/3rdparty/argon2/CMakeFiles/argon2-avx512f.dir/arch/x86_64/lib/argon2-avx512f.c.o
Linking C static library libargon2-avx512f.a
[  3%] Built target argon2-avx512f
Scanning dependencies of target argon2-ssse3
[  3%] Building C object src/3rdparty/argon2/CMakeFiles/argon2-ssse3.dir/arch/x86_64/lib/argon2-ssse3.c.o
Linking C static library libargon2-ssse3.a
[  3%] Built target argon2-ssse3
Scanning dependencies of target argon2-xop
[  4%] Building C object src/3rdparty/argon2/CMakeFiles/argon2-xop.dir/arch/x86_64/lib/argon2-xop.c.o
Linking C static library libargon2-xop.a
[  4%] Built target argon2-xop
Scanning dependencies of target argon2
[  4%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/argon2.c.o
[  4%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/core.c.o
[  5%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/encoding.c.o
[  5%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/genkat.c.o
[  6%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/impl-select.c.o
[  6%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/blake2/blake2.c.o
[  7%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/arch/x86_64/lib/argon2-arch.c.o
[  7%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/arch/x86_64/lib/cpu-flags.c.o
Linking C static library libargon2.a
[  7%] Built target argon2
Scanning dependencies of target xmrig
[  7%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuLaunchData.cpp.o
cc1plus: error: unrecognized command line option "-std=c++11"
cc1plus: warning: unrecognized command line option "-Wno-class-memaccess"
make[2]: *** [CMakeFiles/xmrig.dir/src/backend/cpu/CpuLaunchData.cpp.o] Error 1
make[1]: *** [CMakeFiles/xmrig.dir/all] Error 2
make: *** [all] Error 2


## xmrig | 2020-03-04T14:35:35+00:00
Try specify compiler by something like this `cmake .. -DCMAKE_C_COMPILER=gcc7 -DCMAKE_CXX_COMPILER=g++7`, not sure about exact compiler name.
Thank you.

## mrdogITC | 2020-03-04T15:16:49+00:00
$ which g++
$ which gcc
I found /usr/local/bin/gcc and /usr/local/bin/g++

I launch
$ cmake3 .. -DUV_LIBRARY=/usr/lib64/libuv.a -DXMRIG_DEPS=scripts/deps -DCMAKE_C_COMPILER=/usr/local/bin/gcc -DCMAKE_CXX_COMPILER=/usr/local/bin/g++
$ make -j$(nproc)

AND WORK UP TO 99%

[...]
[ 97%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Tls.cpp.o
[ 98%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpsClient.cpp.o
[ 98%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/Assembly.cpp.o
[ 99%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/cn/r/CryptonightR_gen.cpp.o
[ 99%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/cn/gpu/cn_gpu_avx.cpp.o
/tmp/ccchCdn9.s: Assembler messages:
/tmp/ccchCdn9.s:638: Error: suffix or operands invalid for `vpsrldq'
/tmp/ccchCdn9.s:639: Error: suffix or operands invalid for `vpslldq'
/tmp/ccchCdn9.s:640: Error: suffix or operands invalid for `vpor'
/tmp/ccchCdn9.s:1051: Error: suffix or operands invalid for `vpsrldq'
/tmp/ccchCdn9.s:1052: Error: suffix or operands invalid for `vpslldq'
/tmp/ccchCdn9.s:1751: Error: suffix or operands invalid for `vpor'
/tmp/ccchCdn9.s:1753: Error: suffix or operands invalid for `vpxor'
/tmp/ccchCdn9.s:1755: Error: suffix or operands invalid for `vpxor'
/tmp/ccchCdn9.s:1762: Error: suffix or operands invalid for `vpsrldq'
/tmp/ccchCdn9.s:1763: Error: suffix or operands invalid for `vpslldq'
/tmp/ccchCdn9.s:1764: Error: suffix or operands invalid for `vpor'
/tmp/ccchCdn9.s:1765: Error: suffix or operands invalid for `vpxor'
/tmp/ccchCdn9.s:1766: Error: suffix or operands invalid for `vpxor'
/tmp/ccchCdn9.s:1870: Error: suffix or operands invalid for `vpsrldq'
/tmp/ccchCdn9.s:1871: Error: suffix or operands invalid for `vpslldq'
/tmp/ccchCdn9.s:1872: Error: suffix or operands invalid for `vpor'
/tmp/ccchCdn9.s:1919: Error: suffix or operands invalid for `vpsrldq'
/tmp/ccchCdn9.s:1920: Error: suffix or operands invalid for `vpslldq'
/tmp/ccchCdn9.s:1921: Error: suffix or operands invalid for `vpor'
/tmp/ccchCdn9.s:1922: Error: suffix or operands invalid for `vpxor'
/tmp/ccchCdn9.s:1923: Error: suffix or operands invalid for `vpxor'
/tmp/ccchCdn9.s:2534: Error: suffix or operands invalid for `vpsrldq'
/tmp/ccchCdn9.s:2535: Error: suffix or operands invalid for `vpslldq'
/tmp/ccchCdn9.s:2536: Error: suffix or operands invalid for `vpor'
/tmp/ccchCdn9.s:2538: Error: suffix or operands invalid for `vpxor'
/tmp/ccchCdn9.s:2539: Error: suffix or operands invalid for `vpxor'
/tmp/ccchCdn9.s:2540: Error: suffix or operands invalid for `vpxor'
/tmp/ccchCdn9.s:2544: Error: no such instruction: `vperm2i128 $65,%ymm2,%ymm2,%ymm4'
/tmp/ccchCdn9.s:2547: Error: suffix or operands invalid for `vpxor'
make[2]: *** [CMakeFiles/xmrig.dir/src/crypto/cn/gpu/cn_gpu_avx.cpp.o] Error 1
make[1]: *** [CMakeFiles/xmrig.dir/all] Error 2
make: *** [all] Error 2

## mrdogITC | 2020-03-04T15:30:39+00:00
I use -DWITH_CN_GPU=OFF

[...]
[ 99%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpsClient.cpp.o
[ 99%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/Assembly.cpp.o
[100%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/cn/r/CryptonightR_gen.cpp.o
[100%] Linking CXX executable xmrig
/usr/lib/../lib64/libuv.a: could not read symbols: No such file or directory
collect2: error: ld returned 1 exit status
make[2]: *** [xmrig] Error 1
make[1]: *** [CMakeFiles/xmrig.dir/all] Error 2
make: *** [all] Error 2

What can I do now?

## mrdogITC | 2020-03-04T16:10:26+00:00
now I use:
git clone https://github.com/xmrig/xmrig.git
mkdir xmrig/build/
cd xmrig/scripts && ./build_deps.sh
cd /root/xmrig/build
cmake3 .. -DXMRIG_DEPS=scripts/deps -DWITH_CN_GPU=OFF -DCMAKE_C_COMPILER=/usr/local/bin/gcc -DCMAKE_CXX_COMPILER=/usr/local/bin/g++
make -j$(nproc)

and work!

Thanks!

# Action History
- Created by: mrdogITC | 2020-03-04T13:48:21+00:00
- Closed at: 2020-03-04T16:10:30+00:00
