---
title: Compile failled In function `std::thread::_State_impl<std::thread::_Invoker<std::tuple<void
  (*)(void*)
source_url: https://github.com/xmrig/xmrig/issues/1644
author: moi162001
assignees: []
labels: []
created_at: '2020-04-13T00:29:51+00:00'
updated_at: '2022-11-24T09:10:19+00:00'
type: issue
status: closed
closed_at: '2020-08-29T04:43:08+00:00'
---

# Original Description
same results dev branch or master

ubuntu 18.04 update and upgrade ok
nvidia driver 440.33.01 cuda 10.2
Model name:          Intel(R) Xeon(R) CPU E31230 @ 3.20GHz

cmake 
- The C compiler identification is GNU 5.5.0
-- The CXX compiler identification is GNU 7.3.0
-- Check for working C compiler: /usr/bin/cc
-- Check for working C compiler: /usr/bin/cc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting C compile features - done
-- Check for working CXX compiler: /usr/bin/c++
-- Check for working CXX compiler: /usr/bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Looking for syslog.h
-- Looking for syslog.h - found
-- Found HWLOC: /usr/lib/x86_64-linux-gnu/libhwloc.so  
-- Found UV: /usr/lib/x86_64-linux-gnu/libuv.a  
-- Looking for __builtin___clear_cache
-- Looking for __builtin___clear_cache - found
-- WITH_MSR=ON
-- argon2: detecting feature 'sse2'...
-- Performing Test FEATURE_sse2_NOFLAG
-- Performing Test FEATURE_sse2_NOFLAG - Success
-- argon2: feature 'sse2' detected!
-- argon2: detecting feature 'ssse3'...
-- Performing Test FEATURE_ssse3_NOFLAG
-- Performing Test FEATURE_ssse3_NOFLAG - Failed
-- Performing Test FEATURE_ssse3_FLAG
-- Performing Test FEATURE_ssse3_FLAG - Success
-- argon2: feature 'ssse3' detected!
-- argon2: detecting feature 'xop'...
-- Performing Test FEATURE_xop_NOFLAG
-- Performing Test FEATURE_xop_NOFLAG - Failed
-- Performing Test FEATURE_xop_FLAG
-- Performing Test FEATURE_xop_FLAG - Success
-- argon2: feature 'xop' detected!
-- argon2: detecting feature 'avx2'...
-- Performing Test FEATURE_avx2_NOFLAG
-- Performing Test FEATURE_avx2_NOFLAG - Failed
-- Performing Test FEATURE_avx2_FLAG
-- Performing Test FEATURE_avx2_FLAG - Success
-- argon2: feature 'avx2' detected!
-- argon2: detecting feature 'avx512f'...
-- Performing Test FEATURE_avx512f_NOFLAG
-- Performing Test FEATURE_avx512f_NOFLAG - Failed
-- Performing Test FEATURE_avx512f_FLAG
-- Performing Test FEATURE_avx512f_FLAG - Success
-- argon2: feature 'avx512f' detected!
-- The ASM compiler identification is GNU
-- Found assembler: /usr/bin/cc
-- Found OpenSSL: /usr/local/lib/libcrypto.so (found version "1.1.1") 
-- Configuring done
-- Generating done
-- Build files have been written to: /home/m1/NVOC/mining/miners/xmrig/build
m1@m1-desktop:~/NVOC/mining/miners/xmrig/build$ make
Scanning dependencies of target argon2-sse2
[  1%] Building C object src/3rdparty/argon2/CMakeFiles/argon2-sse2.dir/arch/x86_64/lib/argon2-sse2.c.o
[  1%] Linking C static library libargon2-sse2.a
[  1%] Built target argon2-sse2
Scanning dependencies of target argon2-avx512f
[  2%] Building C object src/3rdparty/argon2/CMakeFiles/argon2-avx512f.dir/arch/x86_64/lib/argon2-avx512f.c.o
[  2%] Linking C static library libargon2-avx512f.a
[  2%] Built target argon2-avx512f
Scanning dependencies of target argon2-avx2
[  3%] Building C object src/3rdparty/argon2/CMakeFiles/argon2-avx2.dir/arch/x86_64/lib/argon2-avx2.c.o
[  3%] Linking C static library libargon2-avx2.a
[  3%] Built target argon2-avx2
Scanning dependencies of target argon2-xop
[  3%] Building C object src/3rdparty/argon2/CMakeFiles/argon2-xop.dir/arch/x86_64/lib/argon2-xop.c.o
[  4%] Linking C static library libargon2-xop.a
[  4%] Built target argon2-xop
Scanning dependencies of target argon2-ssse3
[  4%] Building C object src/3rdparty/argon2/CMakeFiles/argon2-ssse3.dir/arch/x86_64/lib/argon2-ssse3.c.o
[  5%] Linking C static library libargon2-ssse3.a
[  5%] Built target argon2-ssse3
Scanning dependencies of target argon2
[  5%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/argon2.c.o
[  5%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/core.c.o
[  6%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/encoding.c.o
[  6%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/genkat.c.o
[  7%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/impl-select.c.o
[  7%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/blake2/blake2.c.o
[  8%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/arch/x86_64/lib/argon2-arch.c.o
[  8%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/arch/x86_64/lib/cpu-flags.c.o
[  8%] Linking C static library libargon2.a
[  8%] Built target argon2
Scanning dependencies of target xmrig-asm
[  9%] Building ASM object CMakeFiles/xmrig-asm.dir/src/crypto/cn/asm/cn_main_loop.S.o
[  9%] Building ASM object CMakeFiles/xmrig-asm.dir/src/crypto/cn/asm/CryptonightR_template.S.o
[ 10%] Linking C static library libxmrig-asm.a
[ 10%] Built target xmrig-asm
Scanning dependencies of target xmrig
got to 100 %

and
[100%] Linking CXX executable xmrig
CMakeFiles/xmrig.dir/src/backend/common/Workers.cpp.o: In function `std::thread::_State_impl<std::thread::_Invoker<std::tuple<void (*)(void*), xmrig::Thread<xmrig::CpuLaunchData>*> > >::~_State_impl()':
Workers.cpp:(.text._ZNSt6thread11_State_implINS_8_InvokerISt5tupleIJPFvPvEPN5xmrig6ThreadINS6_13CpuLaunchDataEEEEEEEED2Ev[_ZNSt6thread11_State_implINS_8_InvokerISt5tupleIJPFvPvEPN5xmrig6ThreadINS6_13CpuLaunchDataEEEEEEEED5Ev]+0xb): undefined reference to `std::thread::_State::~_State()'
CMakeFiles/xmrig.dir/src/backend/common/Workers.cpp.o: In function `std::thread::_State_impl<std::thread::_Invoker<std::tuple<void (*)(void*), xmrig::Thread<xmrig::CpuLaunchData>*> > >::~_State_impl()':
Workers.cpp:(.text._ZNSt6thread11_State_implINS_8_InvokerISt5tupleIJPFvPvEPN5xmrig6ThreadINS6_13CpuLaunchDataEEEEEEEED0Ev[_ZNSt6thread11_State_implINS_8_InvokerISt5tupleIJPFvPvEPN5xmrig6ThreadINS6_13CpuLaunchDataEEEEEEEED5Ev]+0xf): undefined reference to `std::thread::_State::~_State()'
CMakeFiles/xmrig.dir/src/backend/common/Workers.cpp.o: In function `std::thread::_State_impl<std::thread::_Invoker<std::tuple<void (*)(void*), xmrig::Thread<xmrig::CudaLaunchData>*> > >::~_State_impl()':
Workers.cpp:(.text._ZNSt6thread11_State_implINS_8_InvokerISt5tupleIJPFvPvEPN5xmrig6ThreadINS6_14CudaLaunchDataEEEEEEEED2Ev[_ZNSt6thread11_State_implINS_8_InvokerISt5tupleIJPFvPvEPN5xmrig6ThreadINS6_14CudaLaunchDataEEEEEEEED5Ev]+0xb): undefined reference to `std::thread::_State::~_State()'
CMakeFiles/xmrig.dir/src/backend/common/Workers.cpp.o: In function `std::thread::_State_impl<std::thread::_Invoker<std::tuple<void (*)(void*), xmrig::Thread<xmrig::CudaLaunchData>*> > >::~_State_impl()':
Workers.cpp:(.text._ZNSt6thread11_State_implINS_8_InvokerISt5tupleIJPFvPvEPN5xmrig6ThreadINS6_14CudaLaunchDataEEEEEEEED0Ev[_ZNSt6thread11_State_implINS_8_InvokerISt5tupleIJPFvPvEPN5xmrig6ThreadINS6_14CudaLaunchDataEEEEEEEED5Ev]+0xf): undefined reference to `std::thread::_State::~_State()'
CMakeFiles/xmrig.dir/src/backend/common/Workers.cpp.o: In function `std::thread::_State_impl<std::thread::_Invoker<std::tuple<void (*)(void*), xmrig::Thread<xmrig::OclLaunchData>*> > >::~_State_impl()':
Workers.cpp:(.text._ZNSt6thread11_State_implINS_8_InvokerISt5tupleIJPFvPvEPN5xmrig6ThreadINS6_13OclLaunchDataEEEEEEEED2Ev[_ZNSt6thread11_State_implINS_8_InvokerISt5tupleIJPFvPvEPN5xmrig6ThreadINS6_13OclLaunchDataEEEEEEEED5Ev]+0xb): undefined reference to `std::thread::_State::~_State()'
CMakeFiles/xmrig.dir/src/backend/common/Workers.cpp.o:Workers.cpp:(.text._ZNSt6thread11_State_implINS_8_InvokerISt5tupleIJPFvPvEPN5xmrig6ThreadINS6_13OclLaunchDataEEEEEEEED0Ev[_ZNSt6thread11_State_implINS_8_InvokerISt5tupleIJPFvPvEPN5xmrig6ThreadINS6_13OclLaunchDataEEEEEEEED5Ev]+0xf): more undefined references to `std::thread::_State::~_State()' follow
CMakeFiles/xmrig.dir/src/backend/common/Workers.cpp.o: In function `xmrig::Workers<xmrig::CpuLaunchData>::start(std::vector<xmrig::CpuLaunchData, std::allocator<xmrig::CpuLaunchData> > const&)':
Workers.cpp:(.text._ZN5xmrig7WorkersINS_13CpuLaunchDataEE5startERKSt6vectorIS1_SaIS1_EE[_ZN5xmrig7WorkersINS_13CpuLaunchDataEE5startERKSt6vectorIS1_SaIS1_EE]+0x18f): undefined reference to `std::thread::_M_start_thread(std::unique_ptr<std::thread::_State, std::default_delete<std::thread::_State> >, void (*)())'
CMakeFiles/xmrig.dir/src/backend/common/Workers.cpp.o: In function `xmrig::Workers<xmrig::OclLaunchData>::start(std::vector<xmrig::OclLaunchData, std::allocator<xmrig::OclLaunchData> > const&)':
Workers.cpp:(.text._ZN5xmrig7WorkersINS_13OclLaunchDataEE5startERKSt6vectorIS1_SaIS1_EE[_ZN5xmrig7WorkersINS_13OclLaunchDataEE5startERKSt6vectorIS1_SaIS1_EE]+0x317): undefined reference to `std::thread::_M_start_thread(std::unique_ptr<std::thread::_State, std::default_delete<std::thread::_State> >, void (*)())'
CMakeFiles/xmrig.dir/src/backend/common/Workers.cpp.o: In function `xmrig::Workers<xmrig::CudaLaunchData>::start(std::vector<xmrig::CudaLaunchData, std::allocator<xmrig::CudaLaunchData> > const&)':
Workers.cpp:(.text._ZN5xmrig7WorkersINS_14CudaLaunchDataEE5startERKSt6vectorIS1_SaIS1_EE[_ZN5xmrig7WorkersINS_14CudaLaunchDataEE5startERKSt6vectorIS1_SaIS1_EE]+0x187): undefined reference to `std::thread::_M_start_thread(std::unique_ptr<std::thread::_State, std::default_delete<std::thread::_State> >, void (*)())'
CMakeFiles/xmrig.dir/src/crypto/rx/RxDataset.cpp.o: In function `xmrig::RxDataset::init(xmrig::Buffer const&, unsigned int, int)':
RxDataset.cpp:(.text+0x6e4): undefined reference to `std::thread::_M_start_thread(std::unique_ptr<std::thread::_State, std::default_delete<std::thread::_State> >, void (*)())'
CMakeFiles/xmrig.dir/src/crypto/rx/RxDataset.cpp.o: In function `std::thread::_State_impl<std::thread::_Invoker<std::tuple<void (*)(randomx_dataset*, randomx_cache*, unsigned long, unsigned long, int), randomx_dataset*, randomx_cache*, unsigned int, unsigned int, int> > >::~_State_impl()':
RxDataset.cpp:(.text._ZNSt6thread11_State_implINS_8_InvokerISt5tupleIJPFvP15randomx_datasetP13randomx_cachemmiES4_S6_jjiEEEEED2Ev[_ZNSt6thread11_State_implINS_8_InvokerISt5tupleIJPFvP15randomx_datasetP13randomx_cachemmiES4_S6_jjiEEEEED5Ev]+0xb): undefined reference to `std::thread::_State::~_State()'
CMakeFiles/xmrig.dir/src/crypto/rx/RxDataset.cpp.o: In function `std::thread::_State_impl<std::thread::_Invoker<std::tuple<void (*)(randomx_dataset*, randomx_cache*, unsigned long, unsigned long, int), randomx_dataset*, randomx_cache*, unsigned int, unsigned int, int> > >::~_State_impl()':
RxDataset.cpp:(.text._ZNSt6thread11_State_implINS_8_InvokerISt5tupleIJPFvP15randomx_datasetP13randomx_cachemmiES4_S6_jjiEEEEED0Ev[_ZNSt6thread11_State_implINS_8_InvokerISt5tupleIJPFvP15randomx_datasetP13randomx_cachemmiES4_S6_jjiEEEEED5Ev]+0xf): undefined reference to `std::thread::_State::~_State()'
CMakeFiles/xmrig.dir/src/crypto/rx/RxDataset.cpp.o: In function `void std::vector<std::thread, std::allocator<std::thread> >::_M_realloc_insert<void (&)(randomx_dataset*, randomx_cache*, unsigned long, unsigned long, int), randomx_dataset*&, randomx_cache*, unsigned int const&, unsigned int, int&>(__gnu_cxx::__normal_iterator<std::thread*, std::vector<std::thread, std::allocator<std::thread> > >, void (&)(randomx_dataset*, randomx_cache*, unsigned long, unsigned long, int), randomx_dataset*&, randomx_cache*&&, unsigned int const&, unsigned int&&, int&)':
RxDataset.cpp:(.text._ZNSt6vectorISt6threadSaIS0_EE17_M_realloc_insertIJRFvP15randomx_datasetP13randomx_cachemmiERS5_S7_RKjjRiEEEvN9__gnu_cxx17__normal_iteratorIPS0_S2_EEDpOT_[_ZNSt6vectorISt6threadSaIS0_EE17_M_realloc_insertIJRFvP15randomx_datasetP13randomx_cachemmiERS5_S7_RKjjRiEEEvN9__gnu_cxx17__normal_iteratorIPS0_S2_EEDpOT_]+0x124): undefined reference to `std::thread::_M_start_thread(std::unique_ptr<std::thread::_State, std::default_delete<std::thread::_State> >, void (*)())'
CMakeFiles/xmrig.dir/src/crypto/rx/RxQueue.cpp.o: In function `xmrig::RxQueue::RxQueue(xmrig::IRxListener*)':
RxQueue.cpp:(.text+0x11b): undefined reference to `std::thread::_M_start_thread(std::unique_ptr<std::thread::_State, std::default_delete<std::thread::_State> >, void (*)())'
CMakeFiles/xmrig.dir/src/crypto/rx/RxQueue.cpp.o: In function `std::thread::_State_impl<std::thread::_Invoker<std::tuple<void (xmrig::RxQueue::*)(), xmrig::RxQueue*> > >::~_State_impl()':
RxQueue.cpp:(.text._ZNSt6thread11_State_implINS_8_InvokerISt5tupleIJMN5xmrig7RxQueueEFvvEPS4_EEEEED2Ev[_ZNSt6thread11_State_implINS_8_InvokerISt5tupleIJMN5xmrig7RxQueueEFvvEPS4_EEEEED5Ev]+0xb): undefined reference to `std::thread::_State::~_State()'
CMakeFiles/xmrig.dir/src/crypto/rx/RxQueue.cpp.o: In function `std::thread::_State_impl<std::thread::_Invoker<std::tuple<void (xmrig::RxQueue::*)(), xmrig::RxQueue*> > >::~_State_impl()':
RxQueue.cpp:(.text._ZNSt6thread11_State_implINS_8_InvokerISt5tupleIJMN5xmrig7RxQueueEFvvEPS4_EEEEED0Ev[_ZNSt6thread11_State_implINS_8_InvokerISt5tupleIJMN5xmrig7RxQueueEFvvEPS4_EEEEED5Ev]+0xf): undefined reference to `std::thread::_State::~_State()'
CMakeFiles/xmrig.dir/src/crypto/rx/RxNUMAStorage.cpp.o: In function `xmrig::RxNUMAStorage::init(xmrig::RxSeed const&, unsigned int, bool, bool, xmrig::RxConfig::Mode, int)':
RxNUMAStorage.cpp:(.text+0x78f): undefined reference to `std::thread::_M_start_thread(std::unique_ptr<std::thread::_State, std::default_delete<std::thread::_State> >, void (*)())'
RxNUMAStorage.cpp:(.text+0xc30): undefined reference to `std::thread::_M_start_thread(std::unique_ptr<std::thread::_State, std::default_delete<std::thread::_State> >, void (*)())'
RxNUMAStorage.cpp:(.text+0xd4b): undefined reference to `std::thread::_M_start_thread(std::unique_ptr<std::thread::_State, std::default_delete<std::thread::_State> >, void (*)())'
CMakeFiles/xmrig.dir/src/crypto/rx/RxNUMAStorage.cpp.o: In function `std::thread::_State_impl<std::thread::_Invoker<std::tuple<void (*)(xmrig::RxNUMAStoragePrivate*, unsigned int, bool, bool), xmrig::RxNUMAStoragePrivate*, unsigned int, bool, bool> > >::~_State_impl()':
RxNUMAStorage.cpp:(.text._ZNSt6thread11_State_implINS_8_InvokerISt5tupleIJPFvPN5xmrig20RxNUMAStoragePrivateEjbbES5_jbbEEEEED2Ev[_ZNSt6thread11_State_implINS_8_InvokerISt5tupleIJPFvPN5xmrig20RxNUMAStoragePrivateEjbbES5_jbbEEEEED5Ev]+0xb): undefined reference to `std::thread::_State::~_State()'
CMakeFiles/xmrig.dir/src/crypto/rx/RxNUMAStorage.cpp.o: In function `std::thread::_State_impl<std::thread::_Invoker<std::tuple<void (*)(xmrig::RxNUMAStoragePrivate*, unsigned int, bool, bool), xmrig::RxNUMAStoragePrivate*, unsigned int, bool, bool> > >::~_State_impl()':
RxNUMAStorage.cpp:(.text._ZNSt6thread11_State_implINS_8_InvokerISt5tupleIJPFvPN5xmrig20RxNUMAStoragePrivateEjbbES5_jbbEEEEED0Ev[_ZNSt6thread11_State_implINS_8_InvokerISt5tupleIJPFvPN5xmrig20RxNUMAStoragePrivateEjbbES5_jbbEEEEED5Ev]+0xf): undefined reference to `std::thread::_State::~_State()'
CMakeFiles/xmrig.dir/src/crypto/rx/RxNUMAStorage.cpp.o: In function `std::thread::_State_impl<std::thread::_Invoker<std::tuple<void (*)(xmrig::RxDataset*, unsigned int, void const*), xmrig::RxDataset*, unsigned int, void*> > >::~_State_impl()':
RxNUMAStorage.cpp:(.text._ZNSt6thread11_State_implINS_8_InvokerISt5tupleIJPFvPN5xmrig9RxDatasetEjPKvES5_jPvEEEEED2Ev[_ZNSt6thread11_State_implINS_8_InvokerISt5tupleIJPFvPN5xmrig9RxDatasetEjPKvES5_jPvEEEEED5Ev]+0xb): undefined reference to `std::thread::_State::~_State()'
CMakeFiles/xmrig.dir/src/crypto/rx/RxNUMAStorage.cpp.o: In function `std::thread::_State_impl<std::thread::_Invoker<std::tuple<void (*)(xmrig::RxDataset*, unsigned int, void const*), xmrig::RxDataset*, unsigned int, void*> > >::~_State_impl()':
RxNUMAStorage.cpp:(.text._ZNSt6thread11_State_implINS_8_InvokerISt5tupleIJPFvPN5xmrig9RxDatasetEjPKvES5_jPvEEEEED0Ev[_ZNSt6thread11_State_implINS_8_InvokerISt5tupleIJPFvPN5xmrig9RxDatasetEjPKvES5_jPvEEEEED5Ev]+0xf): undefined reference to `std::thread::_State::~_State()'
CMakeFiles/xmrig.dir/src/crypto/rx/RxNUMAStorage.cpp.o: In function `std::thread::_State_impl<std::thread::_Invoker<std::tuple<void (*)(xmrig::RxNUMAStoragePrivate*, unsigned int, bool), xmrig::RxNUMAStoragePrivate*, unsigned int, bool> > >::~_State_impl()':
RxNUMAStorage.cpp:(.text._ZNSt6thread11_State_implINS_8_InvokerISt5tupleIJPFvPN5xmrig20RxNUMAStoragePrivateEjbES5_jbEEEEED2Ev[_ZNSt6thread11_State_implINS_8_InvokerISt5tupleIJPFvPN5xmrig20RxNUMAStoragePrivateEjbES5_jbEEEEED5Ev]+0xb): undefined reference to `std::thread::_State::~_State()'
CMakeFiles/xmrig.dir/src/crypto/rx/RxNUMAStorage.cpp.o:RxNUMAStorage.cpp:(.text._ZNSt6thread11_State_implINS_8_InvokerISt5tupleIJPFvPN5xmrig20RxNUMAStoragePrivateEjbES5_jbEEEEED0Ev[_ZNSt6thread11_State_implINS_8_InvokerISt5tupleIJPFvPN5xmrig20RxNUMAStoragePrivateEjbES5_jbEEEEED5Ev]+0xf): more undefined references to `std::thread::_State::~_State()' follow
CMakeFiles/xmrig.dir/src/crypto/rx/RxNUMAStorage.cpp.o: In function `void std::vector<std::thread, std::allocator<std::thread> >::_M_realloc_insert<void (&)(xmrig::RxNUMAStoragePrivate*, unsigned int, bool, bool), xmrig::RxNUMAStoragePrivate*, unsigned int&, bool&, bool&>(__gnu_cxx::__normal_iterator<std::thread*, std::vector<std::thread, std::allocator<std::thread> > >, void (&)(xmrig::RxNUMAStoragePrivate*, unsigned int, bool, bool), xmrig::RxNUMAStoragePrivate*&&, unsigned int&, bool&, bool&)':
RxNUMAStorage.cpp:(.text._ZNSt6vectorISt6threadSaIS0_EE17_M_realloc_insertIJRFvPN5xmrig20RxNUMAStoragePrivateEjbbES6_RjRbSA_EEEvN9__gnu_cxx17__normal_iteratorIPS0_S2_EEDpOT_[_ZNSt6vectorISt6threadSaIS0_EE17_M_realloc_insertIJRFvPN5xmrig20RxNUMAStoragePrivateEjbbES6_RjRbSA_EEEvN9__gnu_cxx17__normal_iteratorIPS0_S2_EEDpOT_]+0xfe): undefined reference to `std::thread::_M_start_thread(std::unique_ptr<std::thread::_State, std::default_delete<std::thread::_State> >, void (*)())'
CMakeFiles/xmrig.dir/src/crypto/rx/RxNUMAStorage.cpp.o: In function `void std::vector<std::thread, std::allocator<std::thread> >::_M_realloc_insert<void (&)(xmrig::RxDataset*, unsigned int, void const*), xmrig::RxDataset* const&, unsigned int const&, void*>(__gnu_cxx::__normal_iterator<std::thread*, std::vector<std::thread, std::allocator<std::thread> > >, void (&)(xmrig::RxDataset*, unsigned int, void const*), xmrig::RxDataset* const&, unsigned int const&, void*&&)':
RxNUMAStorage.cpp:(.text._ZNSt6vectorISt6threadSaIS0_EE17_M_realloc_insertIJRFvPN5xmrig9RxDatasetEjPKvERKS6_RKjPvEEEvN9__gnu_cxx17__normal_iteratorIPS0_S2_EEDpOT_[_ZNSt6vectorISt6threadSaIS0_EE17_M_realloc_insertIJRFvPN5xmrig9RxDatasetEjPKvERKS6_RKjPvEEEvN9__gnu_cxx17__normal_iteratorIPS0_S2_EEDpOT_]+0xe3): undefined reference to `std::thread::_M_start_thread(std::unique_ptr<std::thread::_State, std::default_delete<std::thread::_State> >, void (*)())'
collect2: error: ld returned 1 exit status
CMakeFiles/xmrig.dir/build.make:5427: recipe for target 'xmrig' failed
make[2]: *** [xmrig] Error 1
CMakeFiles/Makefile2:73: recipe for target 'CMakeFiles/xmrig.dir/all' failed
make[1]: *** [CMakeFiles/xmrig.dir/all] Error 2
Makefile:83: recipe for target 'all' failed
make: *** [all] Error 2


# Discussion History
## xmrig | 2020-08-29T04:43:08+00:00
```
The C compiler identification is GNU 5.5.0
The CXX compiler identification is GNU 7.3.0
```

Both compilers should be same version.
Thank you.

## mengjianwei12345 | 2022-11-24T09:10:19+00:00
hello what are this instructions are below?
_ZNSt6thread11_State_implINS_8_InvokerISt5tupleIJPFvPvEPN5xmrig6ThreadINS6_13CpuLaunchDataEEEEEEEED0Ev

# Action History
- Created by: moi162001 | 2020-04-13T00:29:51+00:00
- Closed at: 2020-08-29T04:43:08+00:00
