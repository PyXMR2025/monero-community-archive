---
title: ERROR when trying to "make"
source_url: https://github.com/xmrig/xmrig/issues/1612
author: OdinsRagnarok
assignees: []
labels: []
created_at: '2020-03-25T22:48:51+00:00'
updated_at: '2020-08-29T04:57:21+00:00'
type: issue
status: closed
closed_at: '2020-08-29T04:57:21+00:00'
---

# Original Description
Error when trying to "make". Installation on a RaspberryPi 3 b+. System already updated and all the required Libs/Apps where previously installed. 

~/xmrig/build $ make

[  3%] Built target argon2
[  4%] Linking CXX executable xmrig
/usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/opencl/OclWorker.cpp.o: en la función `xmrig::OclWorker::consumeJob()':
OclWorker.cpp:(.text+0x384): referencia a `__atomic_load_8' sin definir
/usr/bin/ld: OclWorker.cpp:(.text+0x3b4): referencia a `__atomic_load_8' sin definir
/usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/opencl/OclWorker.cpp.o: en la función `xmrig::OclWorker::start()':
OclWorker.cpp:(.text+0x5d4): referencia a `__atomic_load_8' sin definir
/usr/bin/ld: OclWorker.cpp:(.text+0x648): referencia a `__atomic_load_8' sin definir
/usr/bin/ld: OclWorker.cpp:(.text+0x65c): referencia a `__atomic_load_8' sin definir
/usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/opencl/OclWorker.cpp.o:OclWorker.cpp:(.text+0x6f8): más referencias a `__atomic_load_8' sin definir a continuación
/usr/bin/ld: CMakeFiles/xmrig.dir/src/crypto/common/Nonce.cpp.o: en la función `xmrig::Nonce::Nonce()':
Nonce.cpp:(.text+0x3c): referencia a `__atomic_store_8' sin definir
/usr/bin/ld: CMakeFiles/xmrig.dir/src/crypto/common/Nonce.cpp.o: en la función `xmrig::Nonce::stop()':
Nonce.cpp:(.text+0x1a0): referencia a `__atomic_store_8' sin definir
/usr/bin/ld: CMakeFiles/xmrig.dir/src/crypto/common/Nonce.cpp.o: en la función `xmrig::Nonce::touch()':
Nonce.cpp:(.text+0x1e0): referencia a `__atomic_fetch_add_8' sin definir
/usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/common/Worker.cpp.o: en la función `xmrig::Worker::storeStats()':
Worker.cpp:(.text+0x90): referencia a `__atomic_store_8' sin definir
/usr/bin/ld: Worker.cpp:(.text+0xbc): referencia a `__atomic_store_8' sin definir
/usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/common/Worker.cpp.o: en la función `xmrig::Worker::timestamp() const':
Worker.cpp:(.text._ZNK5xmrig6Worker9timestampEv[_ZNK5xmrig6Worker9timestampEv]+0x8): referencia a `__atomic_load_8' sin definir
/usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/common/Worker.cpp.o: en la función `xmrig::Worker::hashCount() const':
Worker.cpp:(.text._ZNK5xmrig6Worker9hashCountEv[_ZNK5xmrig6Worker9hashCountEv]+0x8): referencia a `__atomic_load_8' sin definir
/usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/common/Workers.cpp.o: en la función `xmrig::Workers<xmrig::CpuLaunchData>::stop()':
Workers.cpp:(.text._ZN5xmrig7WorkersINS_13CpuLaunchDataEE4stopEv[_ZN5xmrig7WorkersINS_13CpuLaunchDataEE4stopEv]+0x20): referencia a `__atomic_store_8' sin definir
/usr/bin/ld: Workers.cpp:(.text._ZN5xmrig7WorkersINS_13CpuLaunchDataEE4stopEv[_ZN5xmrig7WorkersINS_13CpuLaunchDataEE4stopEv]+0x9c): referencia a `__atomic_fetch_add_8' sin definir
/usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/common/Workers.cpp.o: en la función `xmrig::Workers<xmrig::CpuLaunchData>::tick(unsigned long long)':
Workers.cpp:(.text._ZN5xmrig7WorkersINS_13CpuLaunchDataEE4tickEy[_ZN5xmrig7WorkersINS_13CpuLaunchDataEE4tickEy]+0x38): referencia a `__atomic_load_8' sin definir
/usr/bin/ld: Workers.cpp:(.text._ZN5xmrig7WorkersINS_13CpuLaunchDataEE4tickEy[_ZN5xmrig7WorkersINS_13CpuLaunchDataEE4tickEy]+0x5c): referencia a `__atomic_load_8' sin definir
/usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/common/Workers.cpp.o: en la función `xmrig::Workers<xmrig::OclLaunchData>::stop()':
Workers.cpp:(.text._ZN5xmrig7WorkersINS_13OclLaunchDataEE4stopEv[_ZN5xmrig7WorkersINS_13OclLaunchDataEE4stopEv]+0x20): referencia a `__atomic_store_8' sin definir
/usr/bin/ld: Workers.cpp:(.text._ZN5xmrig7WorkersINS_13OclLaunchDataEE4stopEv[_ZN5xmrig7WorkersINS_13OclLaunchDataEE4stopEv]+0xdc): referencia a `__atomic_fetch_add_8' sin definir
/usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/common/Workers.cpp.o: en la función `xmrig::Workers<xmrig::OclLaunchData>::tick(unsigned long long)':
Workers.cpp:(.text._ZN5xmrig7WorkersINS_13OclLaunchDataEE4tickEy[_ZN5xmrig7WorkersINS_13OclLaunchDataEE4tickEy]+0x38): referencia a `__atomic_load_8' sin definir
/usr/bin/ld: Workers.cpp:(.text._ZN5xmrig7WorkersINS_13OclLaunchDataEE4tickEy[_ZN5xmrig7WorkersINS_13OclLaunchDataEE4tickEy]+0x5c): referencia a `__atomic_load_8' sin definir
/usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/common/Workers.cpp.o: en la función `xmrig::Workers<xmrig::CudaLaunchData>::stop()':
Workers.cpp:(.text._ZN5xmrig7WorkersINS_14CudaLaunchDataEE4stopEv[_ZN5xmrig7WorkersINS_14CudaLaunchDataEE4stopEv]+0x20): referencia a `__atomic_store_8' sin definir
/usr/bin/ld: Workers.cpp:(.text._ZN5xmrig7WorkersINS_14CudaLaunchDataEE4stopEv[_ZN5xmrig7WorkersINS_14CudaLaunchDataEE4stopEv]+0x9c): referencia a `__atomic_fetch_add_8' sin definir
/usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/common/Workers.cpp.o: en la función `xmrig::Workers<xmrig::CudaLaunchData>::tick(unsigned long long)':
Workers.cpp:(.text._ZN5xmrig7WorkersINS_14CudaLaunchDataEE4tickEy[_ZN5xmrig7WorkersINS_14CudaLaunchDataEE4tickEy]+0x38): referencia a `__atomic_load_8' sin definir
/usr/bin/ld: Workers.cpp:(.text._ZN5xmrig7WorkersINS_14CudaLaunchDataEE4tickEy[_ZN5xmrig7WorkersINS_14CudaLaunchDataEE4tickEy]+0x5c): referencia a `__atomic_load_8' sin definir
/usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/common/Workers.cpp.o: en la función `xmrig::Workers<xmrig::CpuLaunchData>::start(std::vector<xmrig::CpuLaunchData, std::allocator<xmrig::CpuLaunchData> > const&)':
Workers.cpp:(.text._ZN5xmrig7WorkersINS_13CpuLaunchDataEE5startERKSt6vectorIS1_SaIS1_EE[_ZN5xmrig7WorkersINS_13CpuLaunchDataEE5startERKSt6vectorIS1_SaIS1_EE]+0xd8): referencia a `__atomic_fetch_add_8' sin definir
/usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/common/Workers.cpp.o: en la función `xmrig::Workers<xmrig::OclLaunchData>::start(std::vector<xmrig::OclLaunchData, std::allocator<xmrig::OclLaunchData> > const&)':
Workers.cpp:(.text._ZN5xmrig7WorkersINS_13OclLaunchDataEE5startERKSt6vectorIS1_SaIS1_EE[_ZN5xmrig7WorkersINS_13OclLaunchDataEE5startERKSt6vectorIS1_SaIS1_EE]+0x200): referencia a `__atomic_fetch_add_8' sin definir
/usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/common/Workers.cpp.o: en la función `xmrig::Workers<xmrig::CudaLaunchData>::start(std::vector<xmrig::CudaLaunchData, std::allocator<xmrig::CudaLaunchData> > const&)':
Workers.cpp:(.text._ZN5xmrig7WorkersINS_14CudaLaunchDataEE5startERKSt6vectorIS1_SaIS1_EE[_ZN5xmrig7WorkersINS_14CudaLaunchDataEE5startERKSt6vectorIS1_SaIS1_EE]+0xd8): referencia a `__atomic_fetch_add_8' sin definir
/usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/cpu/CpuWorker.cpp.o: en la función `xmrig::CpuWorker<1u>::allocateRandomX_VM()':
CpuWorker.cpp:(.text._ZN5xmrig9CpuWorkerILj1EE18allocateRandomX_VMEv[_ZN5xmrig9CpuWorkerILj1EE18allocateRandomX_VMEv]+0x70): referencia a `__atomic_load_8' sin definir
/usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/cpu/CpuWorker.cpp.o: en la función `xmrig::CpuWorker<2u>::allocateRandomX_VM()':
CpuWorker.cpp:(.text._ZN5xmrig9CpuWorkerILj2EE18allocateRandomX_VMEv[_ZN5xmrig9CpuWorkerILj2EE18allocateRandomX_VMEv]+0x70): referencia a `__atomic_load_8' sin definir
/usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/cpu/CpuWorker.cpp.o: en la función `xmrig::CpuWorker<3u>::allocateRandomX_VM()':
CpuWorker.cpp:(.text._ZN5xmrig9CpuWorkerILj3EE18allocateRandomX_VMEv[_ZN5xmrig9CpuWorkerILj3EE18allocateRandomX_VMEv]+0x70): referencia a `__atomic_load_8' sin definir
/usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/cpu/CpuWorker.cpp.o: en la función `xmrig::CpuWorker<4u>::allocateRandomX_VM()':
CpuWorker.cpp:(.text._ZN5xmrig9CpuWorkerILj4EE18allocateRandomX_VMEv[_ZN5xmrig9CpuWorkerILj4EE18allocateRandomX_VMEv]+0x70): referencia a `__atomic_load_8' sin definir
/usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/cpu/CpuWorker.cpp.o: en la función `xmrig::CpuWorker<5u>::allocateRandomX_VM()':
CpuWorker.cpp:(.text._ZN5xmrig9CpuWorkerILj5EE18allocateRandomX_VMEv[_ZN5xmrig9CpuWorkerILj5EE18allocateRandomX_VMEv]+0x70): referencia a `__atomic_load_8' sin definir
/usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/cpu/CpuWorker.cpp.o:CpuWorker.cpp:(.text._ZN5xmrig9CpuWorkerILj1EE10consumeJobEv[_ZN5xmrig9CpuWorkerILj1EE10consumeJobEv]+0x14): más referencias a `__atomic_load_8' sin definir a continuación
collect2: error: ld returned 1 exit status
make[2]: *** [CMakeFiles/xmrig.dir/build.make:3044: xmrig] Error 1
make[1]: *** [CMakeFiles/Makefile2:73: CMakeFiles/xmrig.dir/all] Error 2
make: *** [Makefile:84: all] Error 2


# Discussion History
# Action History
- Created by: OdinsRagnarok | 2020-03-25T22:48:51+00:00
- Closed at: 2020-08-29T04:57:21+00:00
