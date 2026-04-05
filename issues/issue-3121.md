---
title: xmrig windows build not working
source_url: https://github.com/xmrig/xmrig/issues/3121
author: srinivas10247
assignees: []
labels: []
created_at: '2022-09-17T04:17:25+00:00'
updated_at: '2025-06-18T22:52:54+00:00'
type: issue
status: closed
closed_at: '2025-06-18T22:52:54+00:00'
---

# Original Description
i have followed build guide 

https://xmrig.com/docs/miner/build/windows

i used "cmake .. -G "Visual Studio 17 2022" -DUV_INCLUDE_DIR=C:\xmrig-deps\msvc2019\x64\include -DUV_LIBRARY=C:\xmrig-deps\msvc2019\x64\lib\libuv.lib -A x64 -DXMRIG_DEPS=c:\xmrig-deps\msvc2019\x64"

and then xmrig.sln generated.

i tried "cmake --build . --config Release"

but it dosen't get any file that i can run on windows.

i also tried to build from visual studio

i opened .sln in visual studio then
changed build to release 
build => build ALL_BUILD

i got following response 

Build started...
1>------ Build started: Project: ZERO_CHECK, Configuration: Release x64 ------
1>Checking Build System
2>------ Build started: Project: xmrig-asm, Configuration: Release x64 ------
3>------ Build started: Project: hwloc, Configuration: Release x64 ------
4>------ Build started: Project: ghostrider, Configuration: Release x64 ------
5>------ Build started: Project: ethash, Configuration: Release x64 ------
6>------ Build started: Project: argon2-xop, Configuration: Release x64 ------
7>------ Build started: Project: argon2-ssse3, Configuration: Release x64 ------
8>------ Build started: Project: argon2-sse2, Configuration: Release x64 ------
9>------ Build started: Project: argon2-avx512f, Configuration: Release x64 ------
10>------ Build started: Project: argon2-avx2, Configuration: Release x64 ------
2>Building Custom Rule C:/Users/SRINIVAS/Downloads/xmrig/CMakeLists.txt
2>Assembling C:\Users\SRINIVAS\Downloads\xmrig\src\crypto\cn\asm\cn_main_loop.asm...
2>Assembling C:\Users\SRINIVAS\Downloads\xmrig\src\crypto\cn\asm\CryptonightR_template.asm...
4>Building Custom Rule C:/Users/SRINIVAS/Downloads/xmrig/src/crypto/ghostrider/CMakeLists.txt
3>Building Custom Rule C:/Users/SRINIVAS/Downloads/xmrig/src/3rdparty/hwloc/CMakeLists.txt
10>Building Custom Rule C:/Users/SRINIVAS/Downloads/xmrig/src/3rdparty/argon2/CMakeLists.txt
2>xmrig-asm.vcxproj -> C:\Users\SRINIVAS\Downloads\xmrig\xmrigbuild\Release\xmrig-asm.lib
4>sph_blake.c
7>Building Custom Rule C:/Users/SRINIVAS/Downloads/xmrig/src/3rdparty/argon2/CMakeLists.txt
5>Building Custom Rule C:/Users/SRINIVAS/Downloads/xmrig/src/3rdparty/libethash/CMakeLists.txt
6>Building Custom Rule C:/Users/SRINIVAS/Downloads/xmrig/src/3rdparty/argon2/CMakeLists.txt
8>Building Custom Rule C:/Users/SRINIVAS/Downloads/xmrig/src/3rdparty/argon2/CMakeLists.txt
10>argon2-avx2.c
3>base64.c
6>argon2-xop.c
5>ethash_internal.c
7>cl : command line  warning D9002: ignoring unknown option '/arch:SSSE3'
7>argon2-ssse3.c
4>sph_bmw.c
8>argon2-sse2.c
5>C:\Users\SRINIVAS\Downloads\xmrig\src\3rdparty\libethash\ethash_internal.c(157,11): warning C4244: 'return': conversion from 'uint64_t' to 'uint32_t', possible loss of data
5>C:\Users\SRINIVAS\Downloads\xmrig\src\3rdparty\libethash\ethash_internal.c(156,35): warning C4244: 'initializing': conversion from 'uint64_t' to 'const uint32_t', possible loss of data
5>C:\Users\SRINIVAS\Downloads\xmrig\src\3rdparty\libethash\ethash_internal.c(205,4): warning C4133: 'function': incompatible types - from 'const node *' to 'const char *'
5>keccakf800.c
9>Building Custom Rule C:/Users/SRINIVAS/Downloads/xmrig/src/3rdparty/argon2/CMakeLists.txt
4>sph_cubehash.c
4>sph_echo.c
6>argon2-xop.vcxproj -> C:\Users\SRINIVAS\Downloads\xmrig\xmrigbuild\src\3rdparty\argon2\Release\argon2-xop.lib
7>argon2-ssse3.vcxproj -> C:\Users\SRINIVAS\Downloads\xmrig\xmrigbuild\src\3rdparty\argon2\Release\argon2-ssse3.lib
10>argon2-avx2.vcxproj -> C:\Users\SRINIVAS\Downloads\xmrig\xmrigbuild\src\3rdparty\argon2\Release\argon2-avx2.lib
5>ethash.vcxproj -> C:\Users\SRINIVAS\Downloads\xmrig\xmrigbuild\src\3rdparty\libethash\Release\ethash.lib
4>sph_fugue.c
4>C:\Users\SRINIVAS\Downloads\xmrig\src\crypto\ghostrider\sph_fugue.c(748,2): warning C4267: '=': conversion from 'size_t' to 'unsigned int', possible loss of data
4>C:\Users\SRINIVAS\Downloads\xmrig\src\crypto\ghostrider\sph_fugue.c(809,2): warning C4267: '=': conversion from 'size_t' to 'unsigned int', possible loss of data
4>C:\Users\SRINIVAS\Downloads\xmrig\src\crypto\ghostrider\sph_fugue.c(869,2): warning C4267: '=': conversion from 'size_t' to 'unsigned int', possible loss of data
4>sph_groestl.c
3>bind.c
8>argon2-sse2.vcxproj -> C:\Users\SRINIVAS\Downloads\xmrig\xmrigbuild\src\3rdparty\argon2\Release\argon2-sse2.lib
7>Done building project "argon2-ssse3.vcxproj".
5>Done building project "ethash.vcxproj".
9>cl : command line  warning D9002: ignoring unknown option '/arch:AVX512F'
9>argon2-avx512f.c
4>sph_hamsi.c
4>sph_jh.c
9>argon2-avx512f.vcxproj -> C:\Users\SRINIVAS\Downloads\xmrig\xmrigbuild\src\3rdparty\argon2\Release\argon2-avx512f.lib
3>bitmap.c
9>Done building project "argon2-avx512f.vcxproj".
11>------ Build started: Project: argon2, Configuration: Release x64 ------
4>sph_keccak.c
4>sph_luffa.c
4>sph_shabal.c
4>sph_shavite.c
4>C:\Users\SRINIVAS\Downloads\xmrig\src\crypto\ghostrider\sph_shavite.c(1526,37): warning C4267: '+=': conversion from 'size_t' to 'sph_u32', possible loss of data
4>C:\Users\SRINIVAS\Downloads\xmrig\src\crypto\ghostrider\sph_shavite.c(1546,25): warning C4267: '=': conversion from 'size_t' to 'unsigned char', possible loss of data
4>C:\Users\SRINIVAS\Downloads\xmrig\src\crypto\ghostrider\sph_shavite.c(1547,25): warning C4267: '=': conversion from 'size_t' to 'unsigned char', possible loss of data
4>C:\Users\SRINIVAS\Downloads\xmrig\src\crypto\ghostrider\sph_shavite.c(1611,37): warning C4267: '+=': conversion from 'size_t' to 'sph_u32', possible loss of data
4>C:\Users\SRINIVAS\Downloads\xmrig\src\crypto\ghostrider\sph_shavite.c(1635,26): warning C4267: '=': conversion from 'size_t' to 'unsigned char', possible loss of data
4>C:\Users\SRINIVAS\Downloads\xmrig\src\crypto\ghostrider\sph_shavite.c(1636,26): warning C4267: '=': conversion from 'size_t' to 'unsigned char', possible loss of data
4>sph_simd.c
11>Building Custom Rule C:/Users/SRINIVAS/Downloads/xmrig/src/3rdparty/argon2/CMakeLists.txt
4>C:\Users\SRINIVAS\Downloads\xmrig\src\crypto\ghostrider\sph_simd.c(1638,20): warning C4267: '+=': conversion from 'size_t' to 'u32', possible loss of data
4>C:\Users\SRINIVAS\Downloads\xmrig\src\crypto\ghostrider\sph_simd.c(1649,20): warning C4267: '+=': conversion from 'size_t' to 'u32', possible loss of data
4>sph_sha2.c
4>sph_skein.c
3>components.c
11>argon2.c
4>sph_whirlpool.c
11>core.c
4>ghostrider.cpp
3>diff.c
11>encoding.c
11>genkat.c
11>impl-select.c
11>blake2.c
3>distances.c
4>C:\Users\SRINIVAS\Downloads\xmrig\src\crypto\ghostrider\ghostrider.cpp(48,10): fatal  error C1083: Cannot open include file: 'uv.h': No such file or directory
11>argon2-arch.c
4>Done building project "ghostrider.vcxproj" -- FAILED.
11>argon2.vcxproj -> C:\Users\SRINIVAS\Downloads\xmrig\xmrigbuild\src\3rdparty\argon2\Release\argon2.lib
3>misc.c
3>pci-common.c
3>shmem.c
3>topology.c
3>topology-noos.c
3>topology-synthetic.c
3>topology-windows.c
3>C:\Users\SRINIVAS\Downloads\xmrig\src\3rdparty\hwloc\src\topology-windows.c(1013,5): warning C4996: 'GetVersionExA': was declared deprecated
3>topology-x86.c
3>topology-xml.c
3>topology-xml-nolibxml.c
3>traversal.c
3>memattrs.c
3>cpukinds.c
3>Generating Code...
3>hwloc.vcxproj -> C:\Users\SRINIVAS\Downloads\xmrig\xmrigbuild\src\3rdparty\hwloc\Release\hwloc.lib
3>Done building project "hwloc.vcxproj".
12>------ Build started: Project: xmrig, Configuration: Release x64 ------
12>Building Custom Rule C:/Users/SRINIVAS/Downloads/xmrig/CMakeLists.txt
12>Assembling C:\Users\SRINIVAS\Downloads\xmrig\src\crypto\randomx\jit_compiler_x86_static.asm...
12>CpuLaunchData.cpp
12>HashAesKernel.cpp
12>format.cc
12>Algorithm.cpp
12>Coin.cpp
12>keccak.cpp
12>sha3.cpp
12>C:\Users\SRINIVAS\Downloads\xmrig\src\base\crypto\sha3.cpp(146,42): warning C4267: '=': conversion from 'size_t' to 'unsigned int', possible loss of data
12>Async.cpp
12>C:\Users\SRINIVAS\Downloads\xmrig\src\base/tools/Handle.h(23,10): fatal  error C1083: Cannot open include file: 'uv.h': No such file or directory
12>Console.cpp
12>C:\Users\SRINIVAS\Downloads\xmrig\src\base/tools/Handle.h(23,10): fatal  error C1083: Cannot open include file: 'uv.h': No such file or directory
12>Env.cpp
12>C:\Users\SRINIVAS\Downloads\xmrig\src\base\io\Env.cpp(25,10): fatal  error C1083: Cannot open include file: 'uv.h': No such file or directory
12>Json.cpp
12>JsonChain.cpp
12>JsonRequest.cpp
12>ConsoleLog.cpp
12>C:\Users\SRINIVAS\Downloads\xmrig\src\base/tools/Handle.h(23,10): fatal  error C1083: Cannot open include file: 'uv.h': No such file or directory
12>FileLog.cpp
12>FileLogWriter.cpp
12>C:\Users\SRINIVAS\Downloads\xmrig\src\base\io\log\FileLogWriter.cpp(25,10): fatal  error C1083: Cannot open include file: 'uv.h': No such file or directory
12>Log.cpp
12>C:\Users\SRINIVAS\Downloads\xmrig\src\base\io\log\Log.cpp(32,10): fatal  error C1083: Cannot open include file: 'uv.h': No such file or directory
12>Tags.cpp
12>Signals.cpp
12>C:\Users\SRINIVAS\Downloads\xmrig\src\base/tools/Handle.h(23,10): fatal  error C1083: Cannot open include file: 'uv.h': No such file or directory
12>Watcher.cpp
12>C:\Users\SRINIVAS\Downloads\xmrig\src\base\io\Watcher.cpp(26,10): fatal  error C1083: Cannot open include file: 'uv.h': No such file or directory
12>Compiling...
12>Base.cpp
12>BaseConfig.cpp
12>C:\Users\SRINIVAS\Downloads\xmrig\src\base\kernel\config\BaseConfig.cpp(35,10): fatal  error C1083: Cannot open include file: 'uv.h': No such file or directory
12>BaseTransform.cpp
12>Title.cpp
12>Entry.cpp
12>C:\Users\SRINIVAS\Downloads\xmrig\src\base\kernel\Entry.cpp(27,10): fatal  error C1083: Cannot open include file: 'uv.h': No such file or directory
12>Platform.cpp
12>C:\Users\SRINIVAS\Downloads\xmrig\src\base\kernel\Platform.cpp(24,10): fatal  error C1083: Cannot open include file: 'uv.h': No such file or directory
12>Process.cpp
12>C:\Users\SRINIVAS\Downloads\xmrig\src\base\kernel\Process.cpp(21,10): fatal  error C1083: Cannot open include file: 'uv.h': No such file or directory
12>Dns.cpp
12>DnsConfig.cpp
12>DnsRecord.cpp
12>C:\Users\SRINIVAS\Downloads\xmrig\src\base\net\dns\DnsRecord.cpp(20,10): fatal  error C1083: Cannot open include file: 'uv.h': No such file or directory
12>DnsRecords.cpp
12>C:\Users\SRINIVAS\Downloads\xmrig\src\base\net\dns\DnsRecords.cpp(19,10): fatal  error C1083: Cannot open include file: 'uv.h': No such file or directory
12>DnsUvBackend.cpp
12>C:\Users\SRINIVAS\Downloads\xmrig\src\base\net\dns\DnsUvBackend.cpp(20,10): fatal  error C1083: Cannot open include file: 'uv.h': No such file or directory
12>BaseClient.cpp
12>Client.cpp
12>C:\Users\SRINIVAS\Downloads\xmrig\src\base/net/stratum/Client.h(26,10): fatal  error C1083: Cannot open include file: 'uv.h': No such file or directory
12>Job.cpp
12>NetworkState.cpp
12>C:\Users\SRINIVAS\Downloads\xmrig\src\base\net\stratum\NetworkState.cpp(33,10): fatal  error C1083: Cannot open include file: 'uv.h': No such file or directory
12>Pool.cpp
12>C:\Users\SRINIVAS\Downloads\xmrig\src\base/net/stratum/Client.h(26,10): fatal  error C1083: Cannot open include file: 'uv.h': No such file or directory
12>Pools.cpp
12>ProxyUrl.cpp
12>Socks5.cpp
12>C:\Users\SRINIVAS\Downloads\xmrig\src\base/net/stratum/Client.h(26,10): fatal  error C1083: Cannot open include file: 'uv.h': No such file or directory
12>Compiling...
12>FailoverStrategy.cpp
12>SinglePoolStrategy.cpp
12>Url.cpp
12>LineReader.cpp
12>NetBuffer.cpp
12>C:\Users\SRINIVAS\Downloads\xmrig\src\base\net\tools\NetBuffer.cpp(26,10): fatal  error C1083: Cannot open include file: 'uv.h': No such file or directory
12>Arguments.cpp
12>C:\Users\SRINIVAS\Downloads\xmrig\src\base\tools\Arguments.cpp(21,10): fatal  error C1083: Cannot open include file: 'uv.h': No such file or directory
12>Chrono.cpp
12>BlockTemplate.cpp
12>Signatures.cpp
12>C:\Users\SRINIVAS\Downloads\xmrig\src\crypto/randomx/blake2/blake2.h(82,25): warning C4804: '/': unsafe use of type 'bool' in operation
12>C:\Users\SRINIVAS\Downloads\xmrig\src\crypto/randomx/blake2/blake2.h(84,3): warning C4804: '/': unsafe use of type 'bool' in operation
12>C:\Users\SRINIVAS\Downloads\xmrig\src\base\tools\cryptonote\Signatures.cpp(58,78): warning C4267: 'argument': conversion from 'size_t' to 'int', possible loss of data
12>WalletAddress.cpp
12>C:\Users\SRINIVAS\Downloads\xmrig\src\base\tools\cryptonote\WalletAddress.cpp(48,60): warning C4267: '=': conversion from 'size_t' to 'int8_t', possible loss of data
12>C:\Users\SRINIVAS\Downloads\xmrig\src\base\tools\cryptonote\WalletAddress.cpp(59,38): warning C4267: '=': conversion from 'size_t' to 'int', possible loss of data
12>Cvt.cpp
12>String.cpp
12>Timer.cpp
12>C:\Users\SRINIVAS\Downloads\xmrig\src\base/tools/Handle.h(23,10): fatal  error C1083: Cannot open include file: 'uv.h': No such file or directory
12>AutoClient.cpp
12>C:\Users\SRINIVAS\Downloads\xmrig\src\base/net/stratum/Client.h(26,10): fatal  error C1083: Cannot open include file: 'uv.h': No such file or directory
12>EthStratumClient.cpp
12>C:\Users\SRINIVAS\Downloads\xmrig\src\base/net/stratum/Client.h(26,10): fatal  error C1083: Cannot open include file: 'uv.h': No such file or directory
12>BenchClient.cpp
12>C:\Users\SRINIVAS\Downloads\xmrig\src\base/net/stratum/Client.h(26,10): fatal  error C1083: Cannot open include file: 'uv.h': No such file or directory
12>BenchConfig.cpp
12>Httpd.cpp
12>C:\Users\SRINIVAS\Downloads\xmrig\src\base/net/tools/TcpServer.h(29,10): fatal  error C1083: Cannot open include file: 'uv.h': No such file or directory
12>ApiRequest.cpp
12>HttpApiRequest.cpp
12>Compiling...
12>Fetch.cpp
12>HttpApiResponse.cpp
12>HttpClient.cpp
12>C:\Users\SRINIVAS\Downloads\xmrig\src\base\net\http\HttpClient.cpp(32,10): fatal  error C1083: Cannot open include file: 'uv.h': No such file or directory
12>HttpContext.cpp
12>C:\Users\SRINIVAS\Downloads\xmrig\src\base\net\http\HttpContext.cpp(29,10): fatal  error C1083: Cannot open include file: 'uv.h': No such file or directory
12>HttpData.cpp
12>C:\Users\SRINIVAS\Downloads\xmrig\src\base\net\http\HttpData.cpp(28,10): fatal  error C1083: Cannot open include file: 'uv.h': No such file or directory
12>HttpListener.cpp
12>HttpResponse.cpp
12>C:\Users\SRINIVAS\Downloads\xmrig\src\base\net\http\HttpResponse.cpp(30,10): fatal  error C1083: Cannot open include file: 'uv.h': No such file or directory
12>DaemonClient.cpp
12>C:\Users\SRINIVAS\Downloads\xmrig\src\base\net\stratum\DaemonClient.cpp(27,10): fatal  error C1083: Cannot open include file: 'uv.h': No such file or directory
12>SelfSelectClient.cpp
12>C:\Users\SRINIVAS\Downloads\xmrig\src\base/net/stratum/Client.h(26,10): fatal  error C1083: Cannot open include file: 'uv.h': No such file or directory
12>TcpServer.cpp
12>C:\Users\SRINIVAS\Downloads\xmrig\src\base/net/tools/TcpServer.h(29,10): fatal  error C1083: Cannot open include file: 'uv.h': No such file or directory
12>Hashrate.cpp
12>C:\Users\SRINIVAS\Downloads\xmrig\src\base/tools/Handle.h(23,10): fatal  error C1083: Cannot open include file: 'uv.h': No such file or directory
12>Threads.cpp
12>Worker.cpp
12>Workers.cpp
12>Benchmark.cpp
12>BenchState.cpp
12>C:\Users\SRINIVAS\Downloads\xmrig\src\backend\common\benchmark\BenchState.cpp(81,36): warning C4101: 'ex': unreferenced local variable
12>HashrateInterpolator.cpp
12>GpuWorker.cpp
12>Cpu.cpp
12>CpuBackend.cpp
12>Compiling...
12>CpuConfig.cpp
12>CpuThread.cpp
12>CpuThreads.cpp
12>CpuWorker.cpp
12>C:\Users\SRINIVAS\Downloads\xmrig\src\backend\cpu\CpuWorker.cpp(481,1): warning C4267: '=': conversion from 'size_t' to 'int', possible loss of data
12>C:\Users\SRINIVAS\Downloads\xmrig\src\backend\cpu\CpuWorker.cpp(474): message : while compiling class template member function 'void xmrig::CpuWorker<1>::allocateCnCtx(void)'
12>C:\Users\SRINIVAS\Downloads\xmrig\src\backend\cpu\CpuWorker.cpp(158): message : see reference to function template instantiation 'void xmrig::CpuWorker<1>::allocateCnCtx(void)' being compiled
12>C:\Users\SRINIVAS\Downloads\xmrig\src\backend/cpu/CpuWorker.h(113): message : see reference to class template instantiation 'xmrig::CpuWorker<1>' being compiled
12>HwlocCpuInfo.cpp
12>BasicCpuInfo.cpp
12>OclSource.cpp
12>ocl_generic_cn_generator.cpp
12>ocl_vega_cn_generator.cpp
12>Cn0Kernel.cpp
12>Cn1Kernel.cpp
12>Cn2Kernel.cpp
12>CnBranchKernel.cpp
12>OclBackend.cpp
12>C:\Users\SRINIVAS\Downloads\xmrig\src\backend\opencl\OclBackend.cpp(212,53): warning C4244: 'initializing': conversion from 'uint64_t' to 'uint32_t', possible loss of data
12>C:\Users\SRINIVAS\Downloads\xmrig\src\backend\opencl\OclBackend.cpp(212,38): warning C4244: 'initializing': conversion from 'uint64_t' to 'const uint32_t', possible loss of data
12>OclCache.cpp
12>OclConfig.cpp
12>OclLaunchData.cpp
12>OclThread.cpp
12>C:\Users\SRINIVAS\Downloads\xmrig\src\backend\opencl\OclThread.cpp(130,48): warning C4267: 'argument': conversion from 'size_t' to 'rapidjson::SizeType', possible loss of data
12>OclThreads.cpp
12>OclWorker.cpp
12>C:\Users\SRINIVAS\Downloads\xmrig\src\backend\opencl\OclWorker.cpp(185,16): warning C4267: 'argument': conversion from 'size_t' to 'uint32_t', possible loss of data
12>C:\Users\SRINIVAS\Downloads\xmrig\src\backend\opencl\OclWorker.cpp(206,57): warning C4267: 'argument': conversion from 'size_t' to 'uint32_t', possible loss of data
12>Compiling...
12>OclBaseRunner.cpp
12>OclCnRunner.cpp
12>C:\Users\SRINIVAS\Downloads\xmrig\src\crypto/cn/CnAlgo.h(122,1): warning C4267: 'return': conversion from 'size_t' to 'uint32_t', possible loss of data
12>C:\Users\SRINIVAS\Downloads\xmrig\src\crypto/cn/CnAlgo.h(99): message : while compiling class template member function 'uint32_t xmrig::CnAlgo<xmrig::Algorithm::INVALID>::mask(xmrig::Algorithm::Id)'
12>C:\Users\SRINIVAS\Downloads\xmrig\src\backend\opencl\runners\OclCnRunner.cpp(45): message : see reference to function template instantiation 'uint32_t xmrig::CnAlgo<xmrig::Algorithm::INVALID>::mask(xmrig::Algorithm::Id)' being compiled
12>C:\Users\SRINIVAS\Downloads\xmrig\src\backend\opencl\runners\OclCnRunner.cpp(44): message : see reference to class template instantiation 'xmrig::CnAlgo<xmrig::Algorithm::INVALID>' being compiled
12>OclCnR.cpp
12>C:\Users\SRINIVAS\Downloads\xmrig\src\backend\opencl\runners\tools\OclCnR.cpp(39,10): fatal  error C1083: Cannot open include file: 'uv.h': No such file or directory
12>OclSharedData.cpp
12>OclSharedState.cpp
12>OclContext.cpp
12>OclDevice.cpp
12>OclError.cpp
12>OclKernel.cpp
12>OclLib.cpp
12>C:\Users\SRINIVAS\Downloads\xmrig\src\backend\opencl\wrappers\OclLib.cpp(21,10): fatal  error C1083: Cannot open include file: 'uv.h': No such file or directory
12>OclPlatform.cpp
12>D:\vs 2022\VC\Tools\MSVC\14.33.31629\include\xmemory(682,1): warning C4267: 'argument': conversion from 'size_t' to 'uint32_t', possible loss of data
12>D:\vs 2022\VC\Tools\MSVC\14.33.31629\include\vector(840): message : see reference to function template instantiation 'void std::_Default_allocator_traits<_Alloc>::construct<_Ty,size_t&,_cl_device_id*&,_cl_platform_id*>(_Alloc &,_Objty *const ,size_t &,_cl_device_id *&,_cl_platform_id *&&)' being compiled
12>        with
12>        [
12>            _Alloc=std::allocator<xmrig::OclDevice>,
12>            _Ty=xmrig::OclDevice,
12>            _Objty=xmrig::OclDevice
12>        ]
12>D:\vs 2022\VC\Tools\MSVC\14.33.31629\include\vector(840): message : see reference to function template instantiation 'void std::_Default_allocator_traits<_Alloc>::construct<_Ty,size_t&,_cl_device_id*&,_cl_platform_id*>(_Alloc &,_Objty *const ,size_t &,_cl_device_id *&,_cl_platform_id *&&)' being compiled
12>        with
12>        [
12>            _Alloc=std::allocator<xmrig::OclDevice>,
12>            _Ty=xmrig::OclDevice,
12>            _Objty=xmrig::OclDevice
12>        ]
12>D:\vs 2022\VC\Tools\MSVC\14.33.31629\include\vector(822): message : see reference to function template instantiation '_Ty &std::vector<_Ty,std::allocator<_Ty>>::_Emplace_back_with_unused_capacity<size_t&,_cl_device_id*&,_cl_platform_id*>(size_t &,_cl_device_id *&,_cl_platform_id *&&)' being compiled
12>        with
12>        [
12>            _Ty=xmrig::OclDevice
12>        ]
12>D:\vs 2022\VC\Tools\MSVC\14.33.31629\include\vector(822): message : see reference to function template instantiation '_Ty &std::vector<_Ty,std::allocator<_Ty>>::_Emplace_back_with_unused_capacity<size_t&,_cl_device_id*&,_cl_platform_id*>(size_t &,_cl_device_id *&,_cl_platform_id *&&)' being compiled
12>        with
12>        [
12>            _Ty=xmrig::OclDevice
12>        ]
12>D:\vs 2022\VC\Tools\MSVC\14.33.31629\include\vector(904): message : see reference to function template instantiation '_Ty &std::vector<_Ty,std::allocator<_Ty>>::_Emplace_one_at_back<size_t&,_cl_device_id*&,_cl_platform_id*>(size_t &,_cl_device_id *&,_cl_platform_id *&&)' being compiled
12>        with
12>        [
12>            _Ty=xmrig::OclDevice
12>        ]
12>D:\vs 2022\VC\Tools\MSVC\14.33.31629\include\vector(904): message : see reference to function template instantiation '_Ty &std::vector<_Ty,std::allocator<_Ty>>::_Emplace_one_at_back<size_t&,_cl_device_id*&,_cl_platform_id*>(size_t &,_cl_device_id *&,_cl_platform_id *&&)' being compiled
12>        with
12>        [
12>            _Ty=xmrig::OclDevice
12>        ]
12>C:\Users\SRINIVAS\Downloads\xmrig\src\backend\opencl\wrappers\OclPlatform.cpp(105): message : see reference to function template instantiation 'void std::vector<xmrig::OclDevice,std::allocator<xmrig::OclDevice>>::emplace_back<size_t&,_Ty&,cl_platform_id>(size_t &,_Ty &,cl_platform_id &&)' being compiled
12>        with
12>        [
12>            _Ty=cl_device_id
12>        ]
12>OclCache_win.cpp
12>ocl_generic_rx_generator.cpp
12>Blake2bHashRegistersKernel.cpp
12>Blake2bInitialHashKernel.cpp
12>C:\Users\SRINIVAS\Downloads\xmrig\src\backend\opencl\kernels\rx\Blake2bInitialHashKernel.cpp(49,28): warning C4267: 'initializing': conversion from 'size_t' to 'uint32_t', possible loss of data
12>C:\Users\SRINIVAS\Downloads\xmrig\src\backend\opencl\kernels\rx\Blake2bInitialHashKernel.cpp(49,28): warning C4267: 'initializing': conversion from 'size_t' to 'const uint32_t', possible loss of data
12>ExecuteVmKernel.cpp
12>FillAesKernel.cpp
12>FindSharesKernel.cpp
12>InitVmKernel.cpp
12>RxJitKernel.cpp
12>Compiling...
12>RxRunKernel.cpp
12>OclRxBaseRunner.cpp
12>OclRxJitRunner.cpp
12>OclRxVmRunner.cpp
12>ocl_generic_kawpow_generator.cpp
12>KawPow_CalculateDAGKernel.cpp
12>OclKawPowRunner.cpp
12>C:\Users\SRINIVAS\Downloads\xmrig\src\backend\opencl\runners\OclKawPowRunner.cpp(103,48): warning C4267: '=': conversion from 'size_t' to 'uint32_t', possible loss of data
12>C:\Users\SRINIVAS\Downloads\xmrig\src\backend\opencl\runners\OclKawPowRunner.cpp(117,74): warning C4267: 'argument': conversion from 'size_t' to 'uint32_t', possible loss of data
12>C:\Users\SRINIVAS\Downloads\xmrig\src\backend\opencl\runners\OclKawPowRunner.cpp(150,45): warning C4244: 'initializing': conversion from 'uint64_t' to 'uint32_t', possible loss of data
12>C:\Users\SRINIVAS\Downloads\xmrig\src\backend\opencl\runners\OclKawPowRunner.cpp(150,34): warning C4244: 'initializing': conversion from 'uint64_t' to 'const uint32_t', possible loss of data
12>C:\Users\SRINIVAS\Downloads\xmrig\src\backend\opencl\runners\OclKawPowRunner.cpp(151,105): warning C4267: 'argument': conversion from 'size_t' to 'uint32_t', possible loss of data
12>OclKawPow.cpp
12>C:\Users\SRINIVAS\Downloads\xmrig\src\backend\opencl\runners\tools\OclKawPow.cpp(42,10): fatal  error C1083: Cannot open include file: 'uv.h': No such file or directory
12>AdlLib.cpp
12>C:\Users\SRINIVAS\Downloads\xmrig\src\backend\opencl\wrappers\AdlLib.cpp(21,10): fatal  error C1083: Cannot open include file: 'uv.h': No such file or directory
12>CudaBackend.cpp
12>C:\Users\SRINIVAS\Downloads\xmrig\src\backend\cuda\CudaBackend.cpp(224,53): warning C4244: 'initializing': conversion from 'uint64_t' to 'uint32_t', possible loss of data
12>C:\Users\SRINIVAS\Downloads\xmrig\src\backend\cuda\CudaBackend.cpp(224,38): warning C4244: 'initializing': conversion from 'uint64_t' to 'const uint32_t', possible loss of data
12>CudaConfig.cpp
12>CudaLaunchData.cpp
12>CudaThread.cpp
12>CudaThreads.cpp
12>CudaWorker.cpp
12>C:\Users\SRINIVAS\Downloads\xmrig\src\backend\cuda\CudaWorker.cpp(153,16): warning C4267: 'argument': conversion from 'size_t' to 'uint32_t', possible loss of data
12>C:\Users\SRINIVAS\Downloads\xmrig\src\backend\cuda\CudaWorker.cpp(174,55): warning C4267: 'argument': conversion from 'size_t' to 'uint32_t', possible loss of data
12>CudaBaseRunner.cpp
12>CudaCnRunner.cpp
12>CudaDevice.cpp
12>CudaLib.cpp
12>C:\Users\SRINIVAS\Downloads\xmrig\src\backend\cuda\wrappers\CudaLib.cpp(20,10): fatal  error C1083: Cannot open include file: 'uv.h': No such file or directory
12>NvmlLib.cpp
12>C:\Users\SRINIVAS\Downloads\xmrig\src\backend\cuda\wrappers\NvmlLib.cpp(20,10): fatal  error C1083: Cannot open include file: 'uv.h': No such file or directory
12>Compiling...
12>CudaRxRunner.cpp
12>C:\Users\SRINIVAS\Downloads\xmrig\src\backend\cuda\runners\CudaRxRunner.cpp(64,117): warning C4267: 'argument': conversion from 'size_t' to 'uint32_t', possible loss of data
12>CudaKawPowRunner.cpp
12>C:\Users\SRINIVAS\Downloads\xmrig\src\backend\cuda\runners\CudaKawPowRunner.cpp(52,35): warning C4244: 'initializing': conversion from 'uint64_t' to 'uint32_t', possible loss of data
12>C:\Users\SRINIVAS\Downloads\xmrig\src\backend\cuda\runners\CudaKawPowRunner.cpp(52,26): warning C4244: 'initializing': conversion from 'uint64_t' to 'const uint32_t', possible loss of data
12>C:\Users\SRINIVAS\Downloads\xmrig\src\backend\cuda\runners\CudaKawPowRunner.cpp(62,127): warning C4244: 'argument': conversion from 'const uint64_t' to 'uint32_t', possible loss of data
12>App.cpp
12>C:\Users\SRINIVAS\Downloads\xmrig\src\App.cpp(28,10): fatal  error C1083: Cannot open include file: 'uv.h': No such file or directory
12>Config.cpp
12>C:\Users\SRINIVAS\Downloads\xmrig\src\core\config\Config.cpp(22,10): fatal  error C1083: Cannot open include file: 'uv.h': No such file or directory
12>ConfigTransform.cpp
12>Controller.cpp
12>Miner.cpp
12>C:\Users\SRINIVAS\Downloads\xmrig\src\crypto/randomx/blake2/blake2.h(82,25): warning C4804: '/': unsafe use of type 'bool' in operation
12>C:\Users\SRINIVAS\Downloads\xmrig\src\crypto/randomx/blake2/blake2.h(84,3): warning C4804: '/': unsafe use of type 'bool' in operation
12>Taskbar.cpp
12>JobResults.cpp
12>C:\Users\SRINIVAS\Downloads\xmrig\src\net\JobResults.cpp(62,10): fatal  error C1083: Cannot open include file: 'uv.h': No such file or directory
12>Network.cpp
12>C:\Users\SRINIVAS\Downloads\xmrig\src\base/net/stratum/Client.h(26,10): fatal  error C1083: Cannot open include file: 'uv.h': No such file or directory
12>DonateStrategy.cpp
12>C:\Users\SRINIVAS\Downloads\xmrig\src\base/net/stratum/Client.h(26,10): fatal  error C1083: Cannot open include file: 'uv.h': No such file or directory
12>Summary.cpp
12>C:\Users\SRINIVAS\Downloads\xmrig\src\Summary.cpp(21,10): fatal  error C1083: Cannot open include file: 'uv.h': No such file or directory
12>xmrig.cpp
12>HwApi.cpp
12>DmiBoard.cpp
12>DmiMemory.cpp
12>DmiReader.cpp
12>C:\Users\SRINIVAS\Downloads\xmrig\src\hw\dmi\DmiReader.cpp(60,46): warning C4267: 'argument': conversion from 'size_t' to 'rapidjson::SizeType', possible loss of data
12>DmiTools.cpp
12>DmiReader_win.cpp
12>C:\Users\SRINIVAS\Downloads\xmrig\src\hw\dmi\DmiReader_win.cpp(40,13): warning C4200: nonstandard extension used: zero-sized array in struct/union
12>C:\Users\SRINIVAS\Downloads\xmrig\src\hw\dmi\DmiReader_win.cpp(40,13): message : This member will be ignored by a defaulted constructor or copy/move assignment operator
12>Json_win.cpp
12>Compiling...
12>Platform_win.cpp
12>C:\Users\SRINIVAS\Downloads\xmrig\src\base\kernel\Platform_win.cpp(23,10): fatal  error C1083: Cannot open include file: 'uv.h': No such file or directory
12>Process_win.cpp
12>C:\Users\SRINIVAS\Downloads\xmrig\src\base\kernel\Process_win.cpp(20,10): fatal  error C1083: Cannot open include file: 'uv.h': No such file or directory
12>Platform_hwloc.cpp
12>App_win.cpp
12>VirtualMemory_win.cpp
12>CnCtx.cpp
12>CnHash.cpp
12>HugePagesInfo.cpp
12>MemoryPool.cpp
12>Nonce.cpp
12>VirtualMemory.cpp
12>CryptoNight_x86_vaes.cpp
12>NUMAMemoryPool.cpp
12>VirtualMemory_hwloc.cpp
12>aes_hash.cpp
12>C:\Users\SRINIVAS\Downloads\xmrig\src\crypto/randomx/blake2/blake2.h(82,25): warning C4804: '/': unsafe use of type 'bool' in operation
12>C:\Users\SRINIVAS\Downloads\xmrig\src\crypto/randomx/blake2/blake2.h(84,3): warning C4804: '/': unsafe use of type 'bool' in operation
12>allocator.cpp
12>blake2_generator.cpp
12>C:\Users\SRINIVAS\Downloads\xmrig\src\crypto/randomx/blake2/blake2.h(82,25): warning C4804: '/': unsafe use of type 'bool' in operation
12>C:\Users\SRINIVAS\Downloads\xmrig\src\crypto/randomx/blake2/blake2.h(84,3): warning C4804: '/': unsafe use of type 'bool' in operation
12>bytecode_machine.cpp
12>dataset.cpp
12>C:\Users\SRINIVAS\Downloads\xmrig\src\crypto/randomx/jit_compiler_x86.hpp(143,15): warning C4267: '+=': conversion from 'size_t' to 'uint32_t', possible loss of data
12>instructions_portable.cpp
12>C:\Users\SRINIVAS\Downloads\xmrig\src\crypto\randomx\instructions_portable.cpp(63,6): warning C4067: unexpected tokens following preprocessor directive - expected a newline
12>C:\Users\SRINIVAS\Downloads\xmrig\src\crypto\randomx\instructions_portable.cpp(70,6): warning C4067: unexpected tokens following preprocessor directive - expected a newline
12>Compiling...
12>randomx.cpp
12>C:\Users\SRINIVAS\Downloads\xmrig\src\crypto/randomx/jit_compiler_x86.hpp(143,15): warning C4267: '+=': conversion from 'size_t' to 'uint32_t', possible loss of data
12>C:\Users\SRINIVAS\Downloads\xmrig\src\crypto/randomx/blake2/blake2.h(82,25): warning C4804: '/': unsafe use of type 'bool' in operation
12>C:\Users\SRINIVAS\Downloads\xmrig\src\crypto/randomx/blake2/blake2.h(84,3): warning C4804: '/': unsafe use of type 'bool' in operation
12>C:\Users\SRINIVAS\Downloads\xmrig\src\crypto\randomx\randomx.cpp(181,41): warning C4244: '=': conversion from '__int64' to 'uint32_t', possible loss of data
12>C:\Users\SRINIVAS\Downloads\xmrig\src\crypto\randomx\randomx.cpp(187,41): warning C4244: '=': conversion from '__int64' to 'uint32_t', possible loss of data
12>C:\Users\SRINIVAS\Downloads\xmrig\src\crypto\randomx\randomx.cpp(396,26): warning C4101: 'ex': unreferenced local variable
12>C:\Users\SRINIVAS\Downloads\xmrig\src\crypto\randomx\randomx.cpp(493,50): warning C4291: 'void *randomx::CompiledLightVm<1>::operator new(size_t,void *)': no matching operator delete found; memory will not be freed if initialization throws an exception
12>C:\Users\SRINIVAS\Downloads\xmrig\src\crypto/randomx/vm_compiled_light.hpp(40): message : see declaration of 'randomx::CompiledLightVm<1>::operator new'
12>C:\Users\SRINIVAS\Downloads\xmrig\src\crypto\randomx\randomx.cpp(498,45): warning C4291: 'void *randomx::CompiledVm<1>::operator new(size_t,void *)': no matching operator delete found; memory will not be freed if initialization throws an exception
12>C:\Users\SRINIVAS\Downloads\xmrig\src\crypto/randomx/vm_compiled.hpp(45): message : see declaration of 'randomx::CompiledVm<1>::operator new'
12>C:\Users\SRINIVAS\Downloads\xmrig\src\crypto\randomx\randomx.cpp(513,50): warning C4291: 'void *randomx::CompiledLightVm<0>::operator new(size_t,void *)': no matching operator delete found; memory will not be freed if initialization throws an exception
12>C:\Users\SRINIVAS\Downloads\xmrig\src\crypto/randomx/vm_compiled_light.hpp(40): message : see declaration of 'randomx::CompiledLightVm<0>::operator new'
12>C:\Users\SRINIVAS\Downloads\xmrig\src\crypto\randomx\randomx.cpp(518,45): warning C4291: 'void *randomx::CompiledVm<0>::operator new(size_t,void *)': no matching operator delete found; memory will not be freed if initialization throws an exception
12>C:\Users\SRINIVAS\Downloads\xmrig\src\crypto/randomx/vm_compiled.hpp(45): message : see declaration of 'randomx::CompiledVm<0>::operator new'
12>C:\Users\SRINIVAS\Downloads\xmrig\src\crypto\randomx\randomx.cpp(537,26): warning C4101: 'ex': unreferenced local variable
12>soft_aes.cpp
12>superscalar.cpp
12>C:\Users\SRINIVAS\Downloads\xmrig\src\crypto\randomx\superscalar.cpp(154,1): warning C4267: 'return': conversion from 'size_t' to 'int', possible loss of data
12>virtual_machine.cpp
12>C:\Users\SRINIVAS\Downloads\xmrig\src\crypto/randomx/blake2/blake2.h(82,25): warning C4804: '/': unsafe use of type 'bool' in operation
12>C:\Users\SRINIVAS\Downloads\xmrig\src\crypto/randomx/blake2/blake2.h(84,3): warning C4804: '/': unsafe use of type 'bool' in operation
12>C:\Users\SRINIVAS\Downloads\xmrig\src\crypto\randomx\virtual_machine.cpp(84,29): warning C4244: '=': conversion from 'uint64_t' to 'randomx::addr_t', possible loss of data
12>virtual_memory.cpp
12>vm_compiled_light.cpp
12>C:\Users\SRINIVAS\Downloads\xmrig\src\crypto/randomx/jit_compiler_x86.hpp(143,15): warning C4267: '+=': conversion from 'size_t' to 'uint32_t', possible loss of data
12>C:\Users\SRINIVAS\Downloads\xmrig\src\crypto\randomx\vm_compiled_light.cpp(58,50): warning C4244: 'argument': conversion from 'uint64_t' to 'uint32_t', possible loss of data
12>C:\Users\SRINIVAS\Downloads\xmrig\src\crypto\randomx\vm_compiled_light.cpp(50): message : while compiling class template member function 'void randomx::CompiledLightVm<1>::run(void *)'
12>C:\Users\SRINIVAS\Downloads\xmrig\src\crypto\randomx\vm_compiled_light.cpp(64): message : see reference to class template instantiation 'randomx::CompiledLightVm<1>' being compiled
12>vm_compiled.cpp
12>C:\Users\SRINIVAS\Downloads\xmrig\src\crypto/randomx/jit_compiler_x86.hpp(143,15): warning C4267: '+=': conversion from 'size_t' to 'uint32_t', possible loss of data
12>C:\Users\SRINIVAS\Downloads\xmrig\src\crypto/randomx/blake2/blake2.h(82,25): warning C4804: '/': unsafe use of type 'bool' in operation
12>C:\Users\SRINIVAS\Downloads\xmrig\src\crypto/randomx/blake2/blake2.h(84,3): warning C4804: '/': unsafe use of type 'bool' in operation
12>vm_interpreted_light.cpp
12>C:\Users\SRINIVAS\Downloads\xmrig\src\crypto\randomx\vm_interpreted_light.cpp(42,23): warning C4244: 'initializing': conversion from 'uint64_t' to 'uint32_t', possible loss of data
12>C:\Users\SRINIVAS\Downloads\xmrig\src\crypto\randomx\vm_interpreted_light.cpp(41): message : while compiling class template member function 'void randomx::InterpretedLightVm<1>::datasetRead(uint64_t,randomx::int_reg_t (&)[8])'
12>C:\Users\SRINIVAS\Downloads\xmrig\src\crypto\randomx\vm_interpreted_light.cpp(52): message : see reference to class template instantiation 'randomx::InterpretedLightVm<1>' being compiled
12>vm_interpreted.cpp
12>Rx.cpp
12>RxAlgo.cpp
12>RxBasicStorage.cpp
12>RxCache.cpp
12>RxConfig.cpp
12>C:\Users\SRINIVAS\Downloads\xmrig\src\crypto\rx\RxConfig.cpp(147,52): warning C4267: 'argument': conversion from 'size_t' to 'rapidjson::SizeType', possible loss of data
12>C:\Users\SRINIVAS\Downloads\xmrig\src\crypto\rx\RxConfig.cpp(213,34): warning C4267: 'return': conversion from 'size_t' to 'uint32_t', possible loss of data
12>RxDataset.cpp
12>C:\Users\SRINIVAS\Downloads\xmrig\src\crypto\rx\RxDataset.cpp(32,10): fatal  error C1083: Cannot open include file: 'uv.h': No such file or directory
12>RxQueue.cpp
12>RxVm.cpp
12>jit_compiler_x86.cpp
12>C:\Users\SRINIVAS\Downloads\xmrig\src\crypto/randomx/jit_compiler_x86.hpp(143,15): warning C4267: '+=': conversion from 'size_t' to 'uint32_t', possible loss of data
12>C:\Users\SRINIVAS\Downloads\xmrig\src\crypto/randomx/blake2/blake2.h(82,25): warning C4804: '/': unsafe use of type 'bool' in operation
12>C:\Users\SRINIVAS\Downloads\xmrig\src\crypto/randomx/blake2/blake2.h(84,3): warning C4804: '/': unsafe use of type 'bool' in operation
12>C:\Users\SRINIVAS\Downloads\xmrig\src\crypto\randomx\jit_compiler_x86.cpp(293,31): warning C4244: '=': conversion from '__int64' to 'uint32_t', possible loss of data
12>C:\Users\SRINIVAS\Downloads\xmrig\src\crypto\randomx\jit_compiler_x86.cpp(405,55): warning C4244: '=': conversion from '__int64' to 'uint32_t', possible loss of data
12>C:\Users\SRINIVAS\Downloads\xmrig\src\crypto\randomx\jit_compiler_x86.cpp(458,14): warning C4244: '+=': conversion from '__int64' to 'uint32_t', possible loss of data
12>C:\Users\SRINIVAS\Downloads\xmrig\src\crypto\randomx\jit_compiler_x86.cpp(477,33): warning C4244: 'argument': conversion from '__int64' to 'uint32_t', possible loss of data
12>C:\Users\SRINIVAS\Downloads\xmrig\src\crypto\randomx\jit_compiler_x86.cpp(868,31): warning C4244: 'argument': conversion from 'const uint64_t' to 'const uint32_t', possible loss of data
12>C:\Users\SRINIVAS\Downloads\xmrig\src\crypto\randomx\jit_compiler_x86.cpp(873,22): warning C4244: 'argument': conversion from 'uint64_t' to 'uint32_t', possible loss of data
12>C:\Users\SRINIVAS\Downloads\xmrig\src\crypto\randomx\jit_compiler_x86.cpp(920,32): warning C4244: 'argument': conversion from 'const uint64_t' to 'const uint32_t', possible loss of data
12>C:\Users\SRINIVAS\Downloads\xmrig\src\crypto\randomx\jit_compiler_x86.cpp(929,36): warning C4244: '=': conversion from 'uint64_t' to 'uint32_t', possible loss of data
12>C:\Users\SRINIVAS\Downloads\xmrig\src\crypto\randomx\jit_compiler_x86.cpp(944,32): warning C4244: 'argument': conversion from 'const uint64_t' to 'const uint32_t', possible loss of data
12>C:\Users\SRINIVAS\Downloads\xmrig\src\crypto\randomx\jit_compiler_x86.cpp(968,17): warning C4244: 'argument': conversion from 'uint64_t' to 'uint8_t', possible loss of data
12>C:\Users\SRINIVAS\Downloads\xmrig\src\crypto\randomx\jit_compiler_x86.cpp(982,32): warning C4244: 'argument': conversion from 'const uint64_t' to 'const uint32_t', possible loss of data
12>C:\Users\SRINIVAS\Downloads\xmrig\src\crypto\randomx\jit_compiler_x86.cpp(991,36): warning C4244: '=': conversion from 'uint64_t' to 'uint32_t', possible loss of data
12>C:\Users\SRINIVAS\Downloads\xmrig\src\crypto\randomx\jit_compiler_x86.cpp(1049,37): warning C4244: '=': conversion from 'uint64_t' to 'uint32_t', possible loss of data
12>C:\Users\SRINIVAS\Downloads\xmrig\src\crypto\randomx\jit_compiler_x86.cpp(1070,31): warning C4244: 'argument': conversion from 'const uint64_t' to 'const uint32_t', possible loss of data
12>C:\Users\SRINIVAS\Downloads\xmrig\src\crypto\randomx\jit_compiler_x86.cpp(1071,22): warning C4244: 'argument': conversion from 'uint64_t' to 'uint32_t', possible loss of data
12>C:\Users\SRINIVAS\Downloads\xmrig\src\crypto\randomx\jit_compiler_x86.cpp(1074,37): warning C4244: '=': conversion from 'uint64_t' to 'uint32_t', possible loss of data
12>C:\Users\SRINIVAS\Downloads\xmrig\src\crypto\randomx\jit_compiler_x86.cpp(1095,37): warning C4244: '=': conversion from 'uint64_t' to 'uint32_t', possible loss of data
12>C:\Users\SRINIVAS\Downloads\xmrig\src\crypto\randomx\jit_compiler_x86.cpp(1116,37): warning C4244: '=': conversion from 'uint64_t' to 'uint32_t', possible loss of data
12>C:\Users\SRINIVAS\Downloads\xmrig\src\crypto\randomx\jit_compiler_x86.cpp(376,35): warning C4244: '=': conversion from '__int64' to 'uint32_t', possible loss of data
12>C:\Users\SRINIVAS\Downloads\xmrig\src\crypto\randomx\jit_compiler_x86.cpp(395): message : see reference to function template instantiation 'void randomx::JitCompilerX86::generateSuperscalarHash<16>(randomx::SuperscalarProgram (&)[16])' being compiled
12>RxNUMAStorage.cpp
12>RxFix_win.cpp
12>Compiling...
12>Msr_win.cpp
12>C:\Users\SRINIVAS\Downloads\xmrig\src\hw\msr\Msr_win.cpp(108,59): warning C4267: 'argument': conversion from 'size_t' to 'DWORD', possible loss of data
12>C:\Users\SRINIVAS\Downloads\xmrig\src\hw\msr\Msr_win.cpp(142,20): warning C4267: 'argument': conversion from 'size_t' to 'DWORD', possible loss of data
12>RxMsr.cpp
12>Msr.cpp
12>MsrItem.cpp
12>Impl.cpp
12>KPCache.cpp
12>C:\Users\SRINIVAS\Downloads\xmrig\src\crypto\kawpow\KPCache.cpp(77,47): warning C4244: '=': conversion from 'uint64_t' to 'uint32_t', possible loss of data
12>C:\Users\SRINIVAS\Downloads\xmrig\src\crypto\kawpow\KPCache.cpp(91,50): warning C4244: 'initializing': conversion from 'uint64_t' to 'uint32_t', possible loss of data
12>C:\Users\SRINIVAS\Downloads\xmrig\src\crypto\kawpow\KPCache.cpp(91,30): warning C4244: 'initializing': conversion from 'uint64_t' to 'const uint32_t', possible loss of data
12>C:\Users\SRINIVAS\Downloads\xmrig\src\crypto\kawpow\KPCache.cpp(92,56): warning C4244: 'initializing': conversion from 'uint64_t' to 'uint32_t', possible loss of data
12>C:\Users\SRINIVAS\Downloads\xmrig\src\crypto\kawpow\KPCache.cpp(92,30): warning C4244: 'initializing': conversion from 'uint64_t' to 'const uint32_t', possible loss of data
12>KPHash.cpp
12>C:\Users\SRINIVAS\Downloads\xmrig\src\crypto\kawpow\KPHash.cpp(274,47): warning C4244: '=': conversion from 'uint64_t' to 'uint32_t', possible loss of data
12>Tls.cpp
12>C:\Users\SRINIVAS\Downloads\xmrig\src\base/net/stratum/Client.h(26,10): fatal  error C1083: Cannot open include file: 'uv.h': No such file or directory
12>ServerTls.cpp
12>C:\Users\SRINIVAS\Downloads\xmrig\src\base\net\tls\ServerTls.cpp(65,32): warning C4267: 'argument': conversion from 'size_t' to 'int', possible loss of data
12>C:\Users\SRINIVAS\Downloads\xmrig\src\base\net\tls\ServerTls.cpp(84,33): warning C4267: 'argument': conversion from 'size_t' to 'int', possible loss of data
12>TlsConfig.cpp
12>TlsContext.cpp
12>C:\Users\SRINIVAS\Downloads\xmrig\src\base\net\tls\TlsContext.cpp(81,15): warning C4996: 'DH_new': Since OpenSSL 3.0
12>C:\Users\SRINIVAS\Downloads\xmrig\src\base\net\tls\TlsContext.cpp(89,42): warning C4996: 'DH_set0_pqg': Since OpenSSL 3.0
12>C:\Users\SRINIVAS\Downloads\xmrig\src\base\net\tls\TlsContext.cpp(90,9): warning C4996: 'DH_free': Since OpenSSL 3.0
12>C:\Users\SRINIVAS\Downloads\xmrig\src\base\net\tls\TlsContext.cpp(204,14): warning C4996: 'PEM_read_bio_DHparams': Since OpenSSL 3.0
12>C:\Users\SRINIVAS\Downloads\xmrig\src\base\net\tls\TlsContext.cpp(221,5): warning C4996: 'DH_free': Since OpenSSL 3.0
12>TlsGen.cpp
12>C:\Users\SRINIVAS\Downloads\xmrig\src\base\net\tls\TlsGen.cpp(42,21): warning C4996: 'RSA_new': Since OpenSSL 3.0
12>C:\Users\SRINIVAS\Downloads\xmrig\src\base\net\tls\TlsGen.cpp(45,65): warning C4996: 'RSA_generate_key_ex': Since OpenSSL 3.0
12>C:\Users\SRINIVAS\Downloads\xmrig\src\base\net\tls\TlsGen.cpp(48,9): warning C4996: 'RSA_free': Since OpenSSL 3.0
12>HttpsClient.cpp
12>C:\Users\SRINIVAS\Downloads\xmrig\src\base\net\https\HttpsClient.cpp(23,10): fatal  error C1083: Cannot open include file: 'uv.h': No such file or directory
12>HttpsContext.cpp
12>C:\Users\SRINIVAS\Downloads\xmrig\src\base\net\https\HttpsContext.cpp(25,10): fatal  error C1083: Cannot open include file: 'uv.h': No such file or directory
12>HttpsServer.cpp
12>C:\Users\SRINIVAS\Downloads\xmrig\src\base\net\https\HttpsServer.cpp(19,10): fatal  error C1083: Cannot open include file: 'uv.h': No such file or directory
12>Assembly.cpp
12>CryptonightR_gen.cpp
12>Done building project "xmrig.vcxproj" -- FAILED.
13>------ Build started: Project: ALL_BUILD, Configuration: Release x64 ------
13>Building Custom Rule C:/Users/SRINIVAS/Downloads/xmrig/CMakeLists.txt
========== Build: 11 succeeded, 2 failed, 0 up-to-date, 0 skipped ==========




what is the issue ?




# Discussion History
## SChernykh | 2022-09-17T09:29:24+00:00
Remove this part `-DUV_INCLUDE_DIR=C:\xmrig-deps\msvc2019\x64\include -DUV_LIBRARY=C:\xmrig-deps\msvc2019\x64\lib\libuv.lib`, you don't need it. The error you get is `uv.h not found`, double check that you have it in `c:\xmrig-deps\msvc2019\x64\include`

## sohosynergy | 2022-10-01T11:16:08+00:00
> 
> what is the issue ?

You need to change the \ for each directory entry to /  for example:
-DUV_INCLUDE_DIR=C:/xmrig-deps/msvc2019/x64/include -DUV_LIBRARY=C:/xmrig-deps/msvc2019/x64/lib/libuv.lib -A x64 -DXMRIG_DEPS=c:/xmrig-deps/msvc2019/x64"

Reason: CMAKE uses the linux method for directory switching which is always a /   whereas windows uses \  so cmake won't find the 


# Action History
- Created by: srinivas10247 | 2022-09-17T04:17:25+00:00
- Closed at: 2025-06-18T22:52:54+00:00
