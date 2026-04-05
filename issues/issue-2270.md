---
title: Error while compiling
source_url: https://github.com/xmrig/xmrig/issues/2270
author: gamethrower
assignees: []
labels: []
created_at: '2021-04-15T20:57:00+00:00'
updated_at: '2021-04-17T11:28:46+00:00'
type: issue
status: closed
closed_at: '2021-04-16T17:30:09+00:00'
---

# Original Description
```
[ 74%] Building CXX object CMakeFiles/xmrig.dir/src/hw/dmi/DmiReader_win.cpp.obj
C:/msys64/home/Fraunhofer/xmrig/src/hw/dmi/DmiReader_win.cpp:49:50: warning: multi-character character constant [-Wmultichar]
   49 |     const uint32_t size = GetSystemFirmwareTable('RSMB', 0, nullptr, 0);
      |                                                  ^~~~~~
C:/msys64/home/Fraunhofer/xmrig/src/hw/dmi/DmiReader_win.cpp:56:32: warning: multi-character character constant [-Wmultichar]
   56 |     if (GetSystemFirmwareTable('RSMB', 0, smb, size) != size) {
      |                                ^~~~~~
[ 74%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/json/Json_win.cpp.obj
[ 75%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Platform_win.cpp.obj
[ 75%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Process_win.cpp.obj
[ 75%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Platform_hwloc.cpp.obj
[ 76%] Building RC object CMakeFiles/xmrig.dir/res/app.rc.obj
[ 76%] Building CXX object CMakeFiles/xmrig.dir/src/App_win.cpp.obj
[ 76%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/VirtualMemory_win.cpp.obj
[ 77%] Building C object CMakeFiles/xmrig.dir/src/crypto/cn/c_blake256.c.obj
[ 77%] Building C object CMakeFiles/xmrig.dir/src/crypto/cn/c_groestl.c.obj
[ 78%] Building C object CMakeFiles/xmrig.dir/src/crypto/cn/c_jh.c.obj
[ 78%] Building C object CMakeFiles/xmrig.dir/src/crypto/cn/c_skein.c.obj
[ 78%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/cn/CnCtx.cpp.obj
[ 79%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/cn/CnHash.cpp.obj
[ 79%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/HugePagesInfo.cpp.obj
[ 79%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/MemoryPool.cpp.obj
[ 80%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/Nonce.cpp.obj
[ 80%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/VirtualMemory.cpp.obj
[ 81%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/NUMAMemoryPool.cpp.obj
[ 81%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/VirtualMemory_hwloc.cpp.obj
[ 81%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/aes_hash.cpp.obj
[ 82%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/allocator.cpp.obj
[ 82%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/blake2_generator.cpp.obj
[ 82%] Building C object CMakeFiles/xmrig.dir/src/crypto/randomx/blake2/blake2b.c.obj
[ 83%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/bytecode_machine.cpp.obj
[ 83%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/dataset.cpp.obj
[ 84%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/instructions_portable.cpp.obj
[ 84%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/randomx.cpp.obj
[ 84%] Building C object CMakeFiles/xmrig.dir/src/crypto/randomx/reciprocal.c.obj
[ 85%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/soft_aes.cpp.obj
[ 85%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/superscalar.cpp.obj
[ 86%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/virtual_machine.cpp.obj
[ 86%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/virtual_memory.cpp.obj
[ 86%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/vm_compiled_light.cpp.obj
[ 87%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/vm_compiled.cpp.obj
[ 87%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/vm_interpreted_light.cpp.obj
[ 87%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/vm_interpreted.cpp.obj
[ 88%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/Rx.cpp.obj
[ 88%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxAlgo.cpp.obj
[ 89%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxBasicStorage.cpp.obj
[ 89%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxCache.cpp.obj
[ 89%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxConfig.cpp.obj
[ 90%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxDataset.cpp.obj
[ 90%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxQueue.cpp.obj
[ 90%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxVm.cpp.obj
[ 91%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/jit_compiler_x86.cpp.obj
[ 91%] Building C object CMakeFiles/xmrig.dir/src/crypto/randomx/jit_compiler_x86_static.S.obj
[ 92%] Building C object CMakeFiles/xmrig.dir/src/crypto/randomx/blake2/blake2b_sse41.c.obj
[ 92%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxNUMAStorage.cpp.obj
[ 92%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxFix_win.cpp.obj
[ 93%] Building CXX object CMakeFiles/xmrig.dir/src/hw/msr/Msr_win.cpp.obj
[ 93%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxMsr.cpp.obj
[ 94%] Building CXX object CMakeFiles/xmrig.dir/src/hw/msr/Msr.cpp.obj
[ 94%] Building CXX object CMakeFiles/xmrig.dir/src/hw/msr/MsrItem.cpp.obj
[ 94%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/argon2/Impl.cpp.obj
[ 95%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/astrobwt/AstroBWT.cpp.obj
[ 95%] Building ASM object CMakeFiles/xmrig.dir/src/crypto/astrobwt/sha3_256_avx2.S.obj
[ 95%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/astrobwt/Salsa20.cpp.obj
[ 96%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/kawpow/KPCache.cpp.obj
[ 96%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/kawpow/KPHash.cpp.obj
[ 97%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Tls.cpp.obj
[ 97%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/tls/ServerTls.cpp.obj
[ 97%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/tls/TlsConfig.cpp.obj
[ 98%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/tls/TlsContext.cpp.obj
[ 98%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/tls/TlsGen.cpp.obj
[ 98%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/https/HttpsClient.cpp.obj
[ 98%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/https/HttpsServer.cpp.obj
[ 99%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/https/HttpsContext.cpp.obj
make[2]: *** No rule to make target '/libuv.la', needed by 'xmrig.exe'.  Stop.
make[2]: *** Waiting for unfinished jobs....
[100%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/cn/r/CryptonightR_gen.cpp.obj
[100%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/Assembly.cpp.obj
make[1]: *** [CMakeFiles/Makefile2:163: CMakeFiles/xmrig.dir/all] Error 2
make: *** [Makefile:91: all] Error 2

```
How do I fix this?

# Discussion History
## Spudz76 | 2021-04-15T23:22:05+00:00
MSVC2019?

You probably need to also clone `https://github.com/xmrig/xmrig-deps` and then provide `-DXMRIG_DEPS=` path to it.

CMake should have complained a whole lot without it.

## gamethrower | 2021-04-16T06:36:49+00:00
> MSVC2019?
> 
> You probably need to also clone `https://github.com/xmrig/xmrig-deps` and then provide `-DXMRIG_DEPS=` path to it.
> 
> CMake should have complained a whole lot without it.

It's msys2. I did download the deps and provided path to it. 

## gamethrower | 2021-04-16T17:30:09+00:00
Tried compiling with MSVC2019. Shit load of errors but it compiled successfully and seems to work. Closing the issue.

## Spudz76 | 2021-04-17T11:28:46+00:00
> Shit load of errors

**Warnings :)

# Action History
- Created by: gamethrower | 2021-04-15T20:57:00+00:00
- Closed at: 2021-04-16T17:30:09+00:00
