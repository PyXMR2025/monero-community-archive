---
title: Compile failure using Intel OneAPI
source_url: https://github.com/xmrig/xmrig/issues/2785
author: dkokron
assignees: []
labels: []
created_at: '2021-12-03T17:56:30+00:00'
updated_at: '2021-12-03T17:56:30+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
The Intel OneAPI compiler errors out.

**To Reproduce**
Install Base and HPC toolkits from Intel.
https://www.intel.com/content/www/us/en/developer/tools/oneapi/toolkits.html#gs.hsqmii

git clone https://github.com/xmrig/xmrig.git
mkdir xmrig/build.intel && cd xmrig/build.intel
cmake -DCMAKE_C_COMPILER=icc -DCMAKE_CXX_COMPILER=icpc ..
make VERBOSE=1

[ 15%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/cn/CnHash.cpp.o
/opt/intel/oneapi/compiler/2021.4.0/linux/bin/intel64/icpc  -DASTROBWT_AVX2 -DCL_TARGET_OPENCL_VERSION=200 -DCL_USE_DEPRECATED_OPENCL_1_2_APIS -DHAVE_SYSLOG_H -DNDEBUG -DRAPIDJSON_SSE2 -DUNICODE -DXMRIG_64_BIT -DXMRIG_ALGO_ARGON2 -DXMRIG_ALGO_ASTROBWT -DXMRIG_ALGO_CN_FEMTO -DXMRIG_ALGO_CN_HEAVY -DXMRIG_ALGO_CN_LITE -DXMRIG_ALGO_CN_PICO -DXMRIG_ALGO_GHOSTRIDER -DXMRIG_ALGO_KAWPOW -DXMRIG_ALGO_RANDOMX -DXMRIG_FEATURE_ADL -DXMRIG_FEATURE_API -DXMRIG_FEATURE_ASM -DXMRIG_FEATURE_BENCHMARK -DXMRIG_FEATURE_CUDA -DXMRIG_FEATURE_DMI -DXMRIG_FEATURE_ENV -DXMRIG_FEATURE_HTTP -DXMRIG_FEATURE_HWLOC -DXMRIG_FEATURE_MSR -DXMRIG_FEATURE_NVML -DXMRIG_FEATURE_OPENCL -DXMRIG_FEATURE_SSE4_1 -DXMRIG_FEATURE_TLS -DXMRIG_FIX_RYZEN -DXMRIG_JSON_SINGLE_LINE_ARRAY -DXMRIG_MINER_PROJECT -DXMRIG_OS_LINUX -DXMRIG_OS_UNIX -DXMRIG_STRICT_OPENCL_CACHE -DXMRIG_VAES -D_FILE_OFFSET_BITS=64 -D__STDC_FORMAT_MACROS -I/home/XXX/Projects/XMRIG/xmrig/src -I/home/XXX/Projects/XMRIG/xmrig/src/3rdparty  -O3 -DNDEBUG   -std=c++11 -o CMakeFiles/xmrig.dir/src/crypto/cn/CnHash.cpp.o -c /home/XXX/Projects/XMRIG/xmrig/src/crypto/cn/CnHash.cpp

In file included from /home/XXX/Projects/XMRIG/xmrig/src/crypto/cn/CnHash.cpp(29):
/home/XXX/Projects/XMRIG/xmrig/src/crypto/cn/CryptoNight_x86.h(582): **error:** argument of type "unsigned long long *" is incompatible with parameter of type "unsigned long *"
      _addcarry_u64(_subborrow_u64(0, x2, n0, (unsigned long long int*)&x2), r, 0, (unsigned long long int*)&r);
                                              ^

In file included from /home/XXX/Projects/XMRIG/xmrig/src/crypto/cn/CnHash.cpp(29):
/home/dkokron/Projects/XMRIG/xmrig/src/crypto/cn/CryptoNight_x86.h(582): **error**: argument of type "unsigned long long *" is incompatible with parameter of type "unsigned long *"
      _addcarry_u64(_subborrow_u64(0, x2, n0, (unsigned long long int*)&x2), r, 0, (unsigned long long int*)&r);
                                                                                   ^

 - OS: Ubuntu-20.04.3


# Discussion History
# Action History
- Created by: dkokron | 2021-12-03T17:56:30+00:00
