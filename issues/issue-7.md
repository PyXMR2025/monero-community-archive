---
title: Compiling on macOS
source_url: https://github.com/xmrig/xmrig/issues/7
author: Timmert
assignees: []
labels: []
created_at: '2017-05-24T13:22:51+00:00'
updated_at: '2017-05-27T09:14:39+00:00'
type: issue
status: closed
closed_at: '2017-05-27T09:14:39+00:00'
---

# Original Description
Although I know macOS support is not stated anywhere at this moment, I would like to use this on some spare Mac's as well. I'm currently mining inside a Windows VM with reasonable hashrate (240h/s) but native performance would be higher.

These are the results when compiling:
```
i7:xmrig Deve$ mkdir build
i7:xmrig Deve$ cd build
i7:build Deve$ cmake .. -DCMAKE_BUILD_TYPE=Release
-- The C compiler identification is AppleClang 8.1.0.8020042
-- Check for working C compiler: /usr/bin/cc
-- Check for working C compiler: /usr/bin/cc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Found CURL: /usr/lib/libcurl.dylib (found version "7.51.0") 
-- Configuring done
-- Generating done
-- Build files have been written to: /Volumes/Scratch/xmrig/build
i7:build Deve$ make
Scanning dependencies of target cpuid
[  2%] Building C object compat/libcpuid/CMakeFiles/cpuid.dir/cpuid_main.c.o
clang: error: unknown argument: '-ftree-loop-if-convert-stores'
clang: error: unknown argument: '-fbranch-target-load-optimize2'
clang: warning: optimization flag '-fvariable-expansion-in-unroller' is not supported [-Wignored-optimization-argument]
make[2]: *** [compat/libcpuid/CMakeFiles/cpuid.dir/cpuid_main.c.o] Error 1
make[1]: *** [compat/libcpuid/CMakeFiles/cpuid.dir/all] Error 2
make: *** [all] Error 2
```
If there is anything I can test/report please let me know!

# Discussion History
## xmrig | 2017-05-24T14:17:24+00:00
macOS not supported. I will try to add support, some parts of network code, huge pages, clang and maybe some other things else need adaptation.
Thank you.

## xmrig | 2017-05-27T07:39:12+00:00
I add mac support except CPU affinity. Please check.

## Timmert | 2017-05-27T09:14:39+00:00
Awesome! That seems to work now. Hashrate is a bit lower (270H/s vs 320H/s) but I'm running more background services in macOS so that's understandable, system is running stable as well. 

Compile info below, in case you could use it:

```
Dev:Scratch Dev$ git clone https://github.com/xmrig/xmrig.git
Cloning into 'xmrig'...
remote: Counting objects: 658, done.
remote: Compressing objects: 100% (21/21), done.
remote: Total 658 (delta 12), reused 17 (delta 8), pack-reused 629
Receiving objects: 100% (658/658), 312.32 KiB | 0 bytes/s, done.
Resolving deltas: 100% (380/380), done.
Dev:Scratch Dev$ cd xmrig
Dev:xmrig Dev$ mkdir build
Dev:xmrig Dev$ cd build
Dev:build Dev$ cmake .. -DCMAKE_BUILD_TYPE=Release
-- The C compiler identification is AppleClang 8.1.0.8020042
-- Check for working C compiler: /usr/bin/cc
-- Check for working C compiler: /usr/bin/cc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Found CURL: /usr/lib/libcurl.dylib (found version "7.51.0") 
-- Configuring done
-- Generating done
-- Build files have been written to: /Volumes/Scratch/xmrig/build
Dev:build Dev$ make
Scanning dependencies of target cpuid
[  2%] Building C object compat/libcpuid/CMakeFiles/cpuid.dir/cpuid_main.c.o
clang: warning: opDevization flag '-fvariable-expansion-in-unroller' is not supported [-Wignored-opDevization-argument]
[  4%] Building C object compat/libcpuid/CMakeFiles/cpuid.dir/asm-bits.c.o
clang: warning: opDevization flag '-fvariable-expansion-in-unroller' is not supported [-Wignored-opDevization-argument]
[  6%] Building C object compat/libcpuid/CMakeFiles/cpuid.dir/recog_amd.c.o
clang: warning: opDevization flag '-fvariable-expansion-in-unroller' is not supported [-Wignored-opDevization-argument]
/Volumes/Scratch/xmrig/compat/libcpuid/recog_amd.c:437:20: warning: implicit
      conversion from enumeration type 'enum _common_codes_t' to different
      enumeration type 'amd_code_t' (aka 'enum _amd_code_t') [-Wenum-conversion]
        amd_code_t code = NC;
                   ~~~~   ^~
1 warning generated.
[  9%] Building C object compat/libcpuid/CMakeFiles/cpuid.dir/recog_intel.c.o
clang: warning: opDevization flag '-fvariable-expansion-in-unroller' is not supported [-Wignored-opDevization-argument]
[ 11%] Building C object compat/libcpuid/CMakeFiles/cpuid.dir/libcpuid_util.c.o
clang: warning: opDevization flag '-fvariable-expansion-in-unroller' is not supported [-Wignored-opDevization-argument]
Linking C static library libcpuid.a
[ 11%] Built target cpuid
Scanning dependencies of target jansson
[ 13%] Building C object compat/jansson/CMakeFiles/jansson.dir/dump.c.o
clang: warning: opDevization flag '-fvariable-expansion-in-unroller' is not supported [-Wignored-opDevization-argument]
[ 16%] Building C object compat/jansson/CMakeFiles/jansson.dir/error.c.o
clang: warning: opDevization flag '-fvariable-expansion-in-unroller' is not supported [-Wignored-opDevization-argument]
[ 18%] Building C object compat/jansson/CMakeFiles/jansson.dir/hashtable.c.o
clang: warning: opDevization flag '-fvariable-expansion-in-unroller' is not supported [-Wignored-opDevization-argument]
[ 20%] Building C object compat/jansson/CMakeFiles/jansson.dir/hashtable_seed.c.o
clang: warning: opDevization flag '-fvariable-expansion-in-unroller' is not supported [-Wignored-opDevization-argument]
[ 23%] Building C object compat/jansson/CMakeFiles/jansson.dir/load.c.o
clang: warning: opDevization flag '-fvariable-expansion-in-unroller' is not supported [-Wignored-opDevization-argument]
[ 25%] Building C object compat/jansson/CMakeFiles/jansson.dir/memory.c.o
clang: warning: opDevization flag '-fvariable-expansion-in-unroller' is not supported [-Wignored-opDevization-argument]
[ 27%] Building C object compat/jansson/CMakeFiles/jansson.dir/pack_unpack.c.o
clang: warning: opDevization flag '-fvariable-expansion-in-unroller' is not supported [-Wignored-opDevization-argument]
[ 30%] Building C object compat/jansson/CMakeFiles/jansson.dir/strbuffer.c.o
clang: warning: opDevization flag '-fvariable-expansion-in-unroller' is not supported [-Wignored-opDevization-argument]
[ 32%] Building C object compat/jansson/CMakeFiles/jansson.dir/strconv.c.o
clang: warning: opDevization flag '-fvariable-expansion-in-unroller' is not supported [-Wignored-opDevization-argument]
[ 34%] Building C object compat/jansson/CMakeFiles/jansson.dir/utf.c.o
clang: warning: opDevization flag '-fvariable-expansion-in-unroller' is not supported [-Wignored-opDevization-argument]
[ 37%] Building C object compat/jansson/CMakeFiles/jansson.dir/value.c.o
clang: warning: opDevization flag '-fvariable-expansion-in-unroller' is not supported [-Wignored-opDevization-argument]
Linking C static library libjansson.a
[ 37%] Built target jansson
Scanning dependencies of target xmrig
[ 39%] Building C object CMakeFiles/xmrig.dir/xmrig.c.o
clang: warning: opDevization flag '-fvariable-expansion-in-unroller' is not supported [-Wignored-opDevization-argument]
/Volumes/Scratch/xmrig/xmrig.c:101:27: warning: address of array
      'stratum_ctx->work.job_id' will always evaluate to 'true'
      [-Wpointer-bool-conversion]
    if (stratum_ctx->work.job_id && (!stratum_ctx->g_work_Deve || strcmp...
        ~~~~~~~~~~~~~~~~~~^~~~~~ ~~
1 warning generated.
[ 41%] Building C object CMakeFiles/xmrig.dir/algo/cryptonight/cryptonight.c.o
clang: warning: opDevization flag '-fvariable-expansion-in-unroller' is not supported [-Wignored-opDevization-argument]
[ 44%] Building C object CMakeFiles/xmrig.dir/algo/cryptonight/cryptonight_av1_aesni.c.o
clang: warning: opDevization flag '-fvariable-expansion-in-unroller' is not supported [-Wignored-opDevization-argument]
[ 46%] Building C object CMakeFiles/xmrig.dir/algo/cryptonight/cryptonight_av2_aesni_double.c.o
clang: warning: opDevization flag '-fvariable-expansion-in-unroller' is not supported [-Wignored-opDevization-argument]
[ 48%] Building C object CMakeFiles/xmrig.dir/algo/cryptonight/cryptonight_av3_softaes.c.o
clang: warning: opDevization flag '-fvariable-expansion-in-unroller' is not supported [-Wignored-opDevization-argument]
[ 51%] Building C object CMakeFiles/xmrig.dir/algo/cryptonight/cryptonight_av4_softaes_double.c.o
clang: warning: opDevization flag '-fvariable-expansion-in-unroller' is not supported [-Wignored-opDevization-argument]
[ 53%] Building C object CMakeFiles/xmrig.dir/util.c.o
clang: warning: opDevization flag '-fvariable-expansion-in-unroller' is not supported [-Wignored-opDevization-argument]
[ 55%] Building C object CMakeFiles/xmrig.dir/options.c.o
clang: warning: opDevization flag '-fvariable-expansion-in-unroller' is not supported [-Wignored-opDevization-argument]
[ 58%] Building C object CMakeFiles/xmrig.dir/stratum.c.o
clang: warning: opDevization flag '-fvariable-expansion-in-unroller' is not supported [-Wignored-opDevization-argument]
/Volumes/Scratch/xmrig/stratum.c:213:16: warning: using the result of an
      assignment as a condition without parentheses [-Wparentheses]
    if (method = json_string_value(json_object_get(val, "method"))) {
        ~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/Volumes/Scratch/xmrig/stratum.c:213:16: note: place parentheses around the
      assignment to silence this warning
    if (method = json_string_value(json_object_get(val, "method"))) {
               ^
        (                                                         )
/Volumes/Scratch/xmrig/stratum.c:213:16: note: use '==' to turn this assignment
      into an equality comparison
    if (method = json_string_value(json_object_get(val, "method"))) {
               ^
               ==
1 warning generated.
[ 60%] Building C object CMakeFiles/xmrig.dir/stats.c.o
clang: warning: opDevization flag '-fvariable-expansion-in-unroller' is not supported [-Wignored-opDevization-argument]
[ 62%] Building C object CMakeFiles/xmrig.dir/memory.c.o
clang: warning: opDevization flag '-fvariable-expansion-in-unroller' is not supported [-Wignored-opDevization-argument]
[ 65%] Building C object CMakeFiles/xmrig.dir/crypto/c_keccak.c.o
clang: warning: opDevization flag '-fvariable-expansion-in-unroller' is not supported [-Wignored-opDevization-argument]
[ 67%] Building C object CMakeFiles/xmrig.dir/crypto/c_groestl.c.o
clang: warning: opDevization flag '-fvariable-expansion-in-unroller' is not supported [-Wignored-opDevization-argument]
[ 69%] Building C object CMakeFiles/xmrig.dir/crypto/c_blake256.c.o
clang: warning: opDevization flag '-fvariable-expansion-in-unroller' is not supported [-Wignored-opDevization-argument]
[ 72%] Building C object CMakeFiles/xmrig.dir/crypto/c_jh.c.o
clang: warning: opDevization flag '-fvariable-expansion-in-unroller' is not supported [-Wignored-opDevization-argument]
[ 74%] Building C object CMakeFiles/xmrig.dir/crypto/c_skein.c.o
clang: warning: opDevization flag '-fvariable-expansion-in-unroller' is not supported [-Wignored-opDevization-argument]
[ 76%] Building C object CMakeFiles/xmrig.dir/crypto/soft_aes.c.o
clang: warning: opDevization flag '-fvariable-expansion-in-unroller' is not supported [-Wignored-opDevization-argument]
[ 79%] Building C object CMakeFiles/xmrig.dir/utils/applog.c.o
clang: warning: opDevization flag '-fvariable-expansion-in-unroller' is not supported [-Wignored-opDevization-argument]
[ 81%] Building C object CMakeFiles/xmrig.dir/utils/summary.c.o
clang: warning: opDevization flag '-fvariable-expansion-in-unroller' is not supported [-Wignored-opDevization-argument]
[ 83%] Building C object CMakeFiles/xmrig.dir/mac/cpu_mac.c.o
clang: warning: opDevization flag '-fvariable-expansion-in-unroller' is not supported [-Wignored-opDevization-argument]
[ 86%] Building C object CMakeFiles/xmrig.dir/mac/memory_mac.c.o
clang: warning: opDevization flag '-fvariable-expansion-in-unroller' is not supported [-Wignored-opDevization-argument]
[ 88%] Building C object CMakeFiles/xmrig.dir/mac/xmrig_mac.c.o
clang: warning: opDevization flag '-fvariable-expansion-in-unroller' is not supported [-Wignored-opDevization-argument]
[ 90%] Building C object CMakeFiles/xmrig.dir/cpu.c.o
clang: warning: opDevization flag '-fvariable-expansion-in-unroller' is not supported [-Wignored-opDevization-argument]
[ 93%] Building C object CMakeFiles/xmrig.dir/algo/cryptonight-lite/cryptonight_lite_av1_aesni.c.o
clang: warning: opDevization flag '-fvariable-expansion-in-unroller' is not supported [-Wignored-opDevization-argument]
[ 95%] Building C object CMakeFiles/xmrig.dir/algo/cryptonight-lite/cryptonight_lite_av2_aesni_double.c.o
clang: warning: opDevization flag '-fvariable-expansion-in-unroller' is not supported [-Wignored-opDevization-argument]
[ 97%] Building C object CMakeFiles/xmrig.dir/algo/cryptonight-lite/cryptonight_lite_av3_softaes.c.o
clang: warning: opDevization flag '-fvariable-expansion-in-unroller' is not supported [-Wignored-opDevization-argument]
[100%] Building C object CMakeFiles/xmrig.dir/algo/cryptonight-lite/cryptonight_lite_av4_softaes_double.c.o
clang: warning: opDevization flag '-fvariable-expansion-in-unroller' is not supported [-Wignored-opDevization-argument]
Linking C executable xmrig
ld: warning: -L path '/usr/lib/libcurl.dylib' is not a directory
[100%] Built target xmrig
```

Great work! I will close this issue but let me know if I can test other stuff for you.

# Action History
- Created by: Timmert | 2017-05-24T13:22:51+00:00
- Closed at: 2017-05-27T09:14:39+00:00
