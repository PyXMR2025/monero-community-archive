---
title: Build failure on ARMv7
source_url: https://github.com/xmrig/xmrig/issues/3673
author: benthetechguy
assignees: []
labels:
- bug
- arm
created_at: '2025-06-18T02:12:41+00:00'
updated_at: '2025-06-23T00:45:02+00:00'
type: issue
status: closed
closed_at: '2025-06-23T00:45:01+00:00'
---

# Original Description
**Describe the bug**
The new XMRig release 6.23.0 fails to build on ARMv7 Linux.
Looks like some llhttp functions want a vector of 8 uint16 but the code is supplying a vector of 16 uint8.

**To Reproduce**
1. Get XMRig 6.23.0 source
2. `mkdir build && cd build`
3. `cmake ..`
4. `make`

**Expected behavior**
XMRig builds successfully

**Required data**
 - OS: Debian sid
 - One of the occurrences of the error:
   ```cpp
   /home/ben/xmrig-6.23.0/src/3rdparty/llhttp/llhttp.c: In function ‘llhttp__internal__run’:
   /home/ben/xmrig-6.23.0/src/3rdparty/llhttp/llhttp.c:2645:9: note: use ‘-flax-vector-conversions’ to permit conversions between vectors with differing element types or numbers of subparts
    2645 |         );
         |         ^
   /home/ben/xmrig-6.23.0/src/3rdparty/llhttp/llhttp.c:2643:11: error: incompatible type for argument 1 of ‘vandq_u16’
    2643 |           vcgeq_u8(input, vdupq_n_u8(' ')),
         |           ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
         |           |
         |           uint8x16_t
   In file included from /home/ben/xmrig-6.23.0/src/3rdparty/llhttp/llhttp.c:14:
   /usr/lib/gcc/arm-linux-gnueabihf/14/include/arm_neon.h:15231:23: note: expected ‘uint16x8_t’ but argument is of type ‘uint8x16_t’
   15231 | vandq_u16 (uint16x8_t __a, uint16x8_t __b)
         |
   ```

**Additional context**
Full build log:
```cpp
ben@deb2:~/xmrig-6.23.0/build$ cmake ..
-- The C compiler identification is GNU 14.2.0
-- The CXX compiler identification is GNU 14.2.0
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /usr/bin/cc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: /usr/bin/c++ - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Performing Test VAES_SUPPORTED
-- Performing Test VAES_SUPPORTED - Failed
-- Use ARM_TARGET=7 (armv7l)
-- Looking for syslog.h
-- Looking for syslog.h - found
-- Found HWLOC: /usr/lib/arm-linux-gnueabihf/libhwloc.so
-- Found UV: /usr/lib/arm-linux-gnueabihf/libuv.a
-- Looking for __builtin___clear_cache
-- Looking for __builtin___clear_cache - found
-- Looking for posix_memalign
-- Looking for posix_memalign - found
-- WITH_MSR=OFF
-- Found OpenSSL: /usr/lib/arm-linux-gnueabihf/libcrypto.so (found version "3.5.0")
-- Configuring done (9.6s)
-- Generating done (0.4s)
-- Build files have been written to: /home/ben/xmrig-6.23.0/build
ben@deb2:~/xmrig-6.23.0/build$ make -j4
[  0%] Building C object src/3rdparty/libethash/CMakeFiles/ethash.dir/ethash_internal.c.o
[  0%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/argon2.c.o
[  0%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/core.c.o
[  0%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_blake.c.o
[  0%] Building C object src/3rdparty/libethash/CMakeFiles/ethash.dir/keccakf800.c.o
[  1%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/encoding.c.o
[  1%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/genkat.c.o
[  2%] Linking C static library libethash.a
[  2%] Built target ethash
[  2%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/impl-select.c.o
[  3%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_bmw.c.o
[  4%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/blake2/blake2.c.o
[  4%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_cubehash.c.o
[  4%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/arch/generic/lib/argon2-arch.c.o
[  4%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_echo.c.o
[  5%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_fugue.c.o
[  5%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_groestl.c.o
[  5%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_hamsi.c.o
[  6%] Linking C static library libargon2.a
[  6%] Built target argon2
[  7%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_jh.c.o
[  7%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_keccak.c.o
[  8%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_luffa.c.o
[  8%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_shabal.c.o
[  8%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_shavite.c.o
[  9%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_simd.c.o
[  9%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_sha2.c.o
[ 10%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_skein.c.o
[ 10%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_whirlpool.c.o
[ 10%] Building CXX object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/ghostrider.cpp.o
[ 11%] Linking CXX static library libghostrider.a
[ 11%] Built target ghostrider
[ 11%] Building CXX object CMakeFiles/xmrig.dir/src/3rdparty/fmt/format.cc.o
[ 11%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuLaunchData.cpp.o
[ 11%] Building CXX object CMakeFiles/xmrig.dir/src/base/crypto/Algorithm.cpp.o
[ 12%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/rx/HashAesKernel.cpp.o
[ 13%] Building CXX object CMakeFiles/xmrig.dir/src/base/crypto/Coin.cpp.o
[ 13%] Building CXX object CMakeFiles/xmrig.dir/src/base/crypto/keccak.cpp.o
[ 13%] Building CXX object CMakeFiles/xmrig.dir/src/base/crypto/sha3.cpp.o
[ 14%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Async.cpp.o
[ 14%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Console.cpp.o
[ 15%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Env.cpp.o
[ 15%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/json/Json.cpp.o
[ 15%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/json/JsonChain.cpp.o
[ 16%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/json/JsonRequest.cpp.o
[ 16%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/backends/ConsoleLog.cpp.o
[ 17%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/backends/FileLog.cpp.o
In file included from /usr/include/c++/14/string:51,
                 from /usr/include/c++/14/bits/locale_classes.h:40,
                 from /usr/include/c++/14/locale:41,
                 from /home/ben/xmrig-6.23.0/src/3rdparty/fmt/format-inl.h:21,
                 from /home/ben/xmrig-6.23.0/src/3rdparty/fmt/format.cc:8:
In static member function ‘static _Up* std::__copy_move<_IsMove, true, std::random_access_iterator_tag>::__copy_m(_Tp*, _Tp*, _Up*) [with _Tp = const char; _Up = char; bool _IsMove = false]’,
    inlined from ‘_OI std::__copy_move_a2(_II, _II, _OI) [with bool _IsMove = false; _II = const char*; _OI = char*]’ at /usr/include/c++/14/bits/stl_algobase.h:521:30,
    inlined from ‘_OI std::__copy_move_a1(_II, _II, _OI) [with bool _IsMove = false; _II = const char*; _OI = char*]’ at /usr/include/c++/14/bits/stl_algobase.h:548:42,
    inlined from ‘_OI std::__copy_move_a(_II, _II, _OI) [with bool _IsMove = false; _II = const char*; _OI = char*]’ at /usr/include/c++/14/bits/stl_algobase.h:555:31,
    inlined from ‘_OI std::copy(_II, _II, _OI) [with _II = const char*; _OI = char*]’ at /usr/include/c++/14/bits/stl_algobase.h:651:7,
    inlined from ‘OutputIt fmt::v7::detail::copy_str(InputIt, InputIt, OutputIt) [with OutChar = char; InputIt = const char*; OutputIt = char*; typename std::enable_if<(! std::integral_constant<bool, (std::is_same<typename std::iterator_traits<_II>::value_type, char>::value && std::is_same<OutChar, char8_type>::value)>::value), int>::type <anonymous> = 0]’ at /home/ben/xmrig-6.23.0/src/3rdparty/fmt/format.h:574:19,
    inlined from ‘OutputIt fmt::v7::detail::write_float(OutputIt, const big_decimal_fp&, float_specs, Char) [with OutputIt = char*; Char = char]’ at /home/ben/xmrig-6.23.0/src/3rdparty/fmt/format.h:1755:25:
/usr/include/c++/14/bits/stl_algobase.h:452:30: warning: ‘void* __builtin_memmove(void*, const void*, unsigned int)’ pointer overflow between offset 1 and size 2147483647 [-Warray-bounds=]
  452 |             __builtin_memmove(__result, __first, sizeof(_Tp) * _Num);
      |             ~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
[ 17%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/FileLogWriter.cpp.o
[ 17%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/Log.cpp.o
[ 18%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/Tags.cpp.o
[ 18%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Signals.cpp.o
[ 18%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Watcher.cpp.o
[ 19%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Base.cpp.o
[ 19%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/config/BaseConfig.cpp.o
[ 20%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/config/BaseTransform.cpp.o
[ 20%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/config/Title.cpp.o
[ 20%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Entry.cpp.o
[ 21%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Platform.cpp.o
[ 21%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Process.cpp.o
[ 22%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/dns/Dns.cpp.o
[ 22%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/dns/DnsConfig.cpp.o
[ 22%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/dns/DnsRecord.cpp.o
[ 23%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/dns/DnsRecords.cpp.o
[ 23%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/dns/DnsUvBackend.cpp.o
[ 24%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/Http.cpp.o
[ 24%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/BaseClient.cpp.o
[ 24%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Client.cpp.o
[ 25%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Job.cpp.o
[ 25%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/NetworkState.cpp.o
[ 25%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Pool.cpp.o
[ 26%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Pools.cpp.o
[ 26%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/ProxyUrl.cpp.o
[ 27%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Socks5.cpp.o
[ 27%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/strategies/FailoverStrategy.cpp.o
[ 27%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/strategies/SinglePoolStrategy.cpp.o
[ 28%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Url.cpp.o
[ 28%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/tools/LineReader.cpp.o
[ 29%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/tools/NetBuffer.cpp.o
[ 29%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/Arguments.cpp.o
[ 29%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/Chrono.cpp.o
[ 30%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/cryptonote/BlockTemplate.cpp.o
[ 30%] Building C object CMakeFiles/xmrig.dir/src/base/tools/cryptonote/crypto-ops-data.c.o
[ 31%] Building C object CMakeFiles/xmrig.dir/src/base/tools/cryptonote/crypto-ops.c.o
[ 31%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/cryptonote/Signatures.cpp.o
[ 31%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/cryptonote/WalletAddress.cpp.o
[ 32%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/Cvt.cpp.o
[ 32%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/String.cpp.o
[ 32%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/Timer.cpp.o
[ 33%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/AutoClient.cpp.o
[ 33%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/EthStratumClient.cpp.o
[ 34%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/benchmark/BenchClient.cpp.o
[ 34%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/benchmark/BenchConfig.cpp.o
[ 34%] Building C object CMakeFiles/xmrig.dir/src/3rdparty/llhttp/llhttp.c.o
[ 35%] Building C object CMakeFiles/xmrig.dir/src/3rdparty/llhttp/api.c.o
/home/ben/xmrig-6.23.0/src/3rdparty/llhttp/llhttp.c: In function ‘llhttp__internal__run’:
/home/ben/xmrig-6.23.0/src/3rdparty/llhttp/llhttp.c:2645:9: note: use ‘-flax-vector-conversions’ to permit conversions between vectors with differing element types or numbers of subparts
 2645 |         );
      |         ^
/home/ben/xmrig-6.23.0/src/3rdparty/llhttp/llhttp.c:2643:11: error: incompatible type for argument 1 of ‘vandq_u16’
 2643 |           vcgeq_u8(input, vdupq_n_u8(' ')),
      |           ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
      |           |
      |           uint8x16_t
In file included from /home/ben/xmrig-6.23.0/src/3rdparty/llhttp/llhttp.c:14:
/usr/lib/gcc/arm-linux-gnueabihf/14/include/arm_neon.h:15231:23: note: expected ‘uint16x8_t’ but argument is of type ‘uint8x16_t’
15231 | vandq_u16 (uint16x8_t __a, uint16x8_t __b)
      |            ~~~~~~~~~~~^~~
/home/ben/xmrig-6.23.0/src/3rdparty/llhttp/llhttp.c:2644:11: error: incompatible type for argument 2 of ‘vandq_u16’
 2644 |           vcleq_u8(input, vdupq_n_u8('~'))
      |           ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
      |           |
      |           uint8x16_t
/usr/lib/gcc/arm-linux-gnueabihf/14/include/arm_neon.h:15231:39: note: expected ‘uint16x8_t’ but argument is of type ‘uint8x16_t’
15231 | vandq_u16 (uint16x8_t __a, uint16x8_t __b)
      |                            ~~~~~~~~~~~^~~
/home/ben/xmrig-6.23.0/src/3rdparty/llhttp/llhttp.c:2646:26: error: incompatible type for argument 1 of ‘vorrq_u16’
 2646 |         mask = vorrq_u16(mask, single);
      |                          ^~~~
      |                          |
      |                          uint8x16_t
/usr/lib/gcc/arm-linux-gnueabihf/14/include/arm_neon.h:15343:23: note: expected ‘uint16x8_t’ but argument is of type ‘uint8x16_t’
15343 | vorrq_u16 (uint16x8_t __a, uint16x8_t __b)
      |            ~~~~~~~~~~~^~~
/home/ben/xmrig-6.23.0/src/3rdparty/llhttp/llhttp.c:2646:32: error: incompatible type for argument 2 of ‘vorrq_u16’
 2646 |         mask = vorrq_u16(mask, single);
      |                                ^~~~~~
      |                                |
      |                                uint8x16_t
/usr/lib/gcc/arm-linux-gnueabihf/14/include/arm_neon.h:15343:39: note: expected ‘uint16x8_t’ but argument is of type ‘uint8x16_t’
15343 | vorrq_u16 (uint16x8_t __a, uint16x8_t __b)
      |                            ~~~~~~~~~~~^~~
/home/ben/xmrig-6.23.0/src/3rdparty/llhttp/llhttp.c:2648:11: error: incompatible type for argument 1 of ‘vandq_u16’
 2648 |           vcgeq_u8(input, vdupq_n_u8(0x80)),
      |           ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
      |           |
      |           uint8x16_t
/usr/lib/gcc/arm-linux-gnueabihf/14/include/arm_neon.h:15231:23: note: expected ‘uint16x8_t’ but argument is of type ‘uint8x16_t’
15231 | vandq_u16 (uint16x8_t __a, uint16x8_t __b)
      |            ~~~~~~~~~~~^~~
/home/ben/xmrig-6.23.0/src/3rdparty/llhttp/llhttp.c:2649:11: error: incompatible type for argument 2 of ‘vandq_u16’
 2649 |           vcleq_u8(input, vdupq_n_u8(0xff))
      |           ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
      |           |
      |           uint8x16_t
/usr/lib/gcc/arm-linux-gnueabihf/14/include/arm_neon.h:15231:39: note: expected ‘uint16x8_t’ but argument is of type ‘uint8x16_t’
15231 | vandq_u16 (uint16x8_t __a, uint16x8_t __b)
      |                            ~~~~~~~~~~~^~~
/home/ben/xmrig-6.23.0/src/3rdparty/llhttp/llhttp.c:2651:26: error: incompatible type for argument 1 of ‘vorrq_u16’
 2651 |         mask = vorrq_u16(mask, single);
      |                          ^~~~
      |                          |
      |                          uint8x16_t
/usr/lib/gcc/arm-linux-gnueabihf/14/include/arm_neon.h:15343:23: note: expected ‘uint16x8_t’ but argument is of type ‘uint8x16_t’
15343 | vorrq_u16 (uint16x8_t __a, uint16x8_t __b)
      |            ~~~~~~~~~~~^~~
/home/ben/xmrig-6.23.0/src/3rdparty/llhttp/llhttp.c:2651:32: error: incompatible type for argument 2 of ‘vorrq_u16’
 2651 |         mask = vorrq_u16(mask, single);
      |                                ^~~~~~
      |                                |
      |                                uint8x16_t
/usr/lib/gcc/arm-linux-gnueabihf/14/include/arm_neon.h:15343:39: note: expected ‘uint16x8_t’ but argument is of type ‘uint8x16_t’
15343 | vorrq_u16 (uint16x8_t __a, uint16x8_t __b)
      |                            ~~~~~~~~~~~^~~
/home/ben/xmrig-6.23.0/src/3rdparty/llhttp/llhttp.c:2652:30: error: incompatible type for argument 1 of ‘vshrn_n_u16’
 2652 |         narrow = vshrn_n_u16(mask, 4);
      |                              ^~~~
      |                              |
      |                              uint8x16_t
/usr/lib/gcc/arm-linux-gnueabihf/14/include/arm_neon.h:4699:25: note: expected ‘uint16x8_t’ but argument is of type ‘uint8x16_t’
 4699 | vshrn_n_u16 (uint16x8_t __a, const int __b)
      |              ~~~~~~~~~~~^~~
[ 35%] Building C object CMakeFiles/xmrig.dir/src/3rdparty/llhttp/http.c.o
make[2]: *** [CMakeFiles/xmrig.dir/build.make:919: CMakeFiles/xmrig.dir/src/3rdparty/llhttp/llhttp.c.o] Error 1
make[2]: *** Waiting for unfinished jobs....
make[1]: *** [CMakeFiles/Makefile2:157: CMakeFiles/xmrig.dir/all] Error 2
make: *** [Makefile:91: all] Error 2
```

# Discussion History
## xmrig | 2025-06-18T08:04:57+00:00
Try add `-flax-vector-conversions` to the line https://github.com/xmrig/xmrig/blob/master/cmake/flags.cmake#L29|
```
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -march=armv7-a -mfpu=neon -flax-vector-conversions")
```

But please note even if the 32-bit version compiles, it is still not really supported now.
Thank you.

# Action History
- Created by: benthetechguy | 2025-06-18T02:12:41+00:00
- Closed at: 2025-06-23T00:45:01+00:00
