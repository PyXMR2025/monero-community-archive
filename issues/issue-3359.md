---
title: Build fails on ARMv8 device (Rock64).
source_url: https://github.com/monero-project/monero/issues/3359
author: grubles
assignees: []
labels: []
created_at: '2018-03-06T02:30:55+00:00'
updated_at: '2018-03-14T15:40:52+00:00'
type: issue
status: closed
closed_at: '2018-03-14T15:40:52+00:00'
---

# Original Description
Ubuntu 16.04.4
```
[ 58%] Linking CXX executable ../../bin/monero-wallet-rpc
../../lib/libwallet.a(wallet2.cpp.o): In function `tools::wallet2::encrypt(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, tools::scrubbed<crypto::ec_scalar> const&, bool) const':
wallet2.cpp:(.text+0x9848): undefined reference to `cn_slow_hash_pre'
../../lib/libwallet.a(wallet2.cpp.o): In function `crypto::generate_chacha_key(void const*, unsigned long, tools::scrubbed<std::array<unsigned char, 32ul> >&, bool)':
wallet2.cpp:(.text._ZN6crypto19generate_chacha_keyEPKvmRN5tools8scrubbedISt5arrayIhLm32EEEEb[_ZN6crypto19generate_chacha_keyEPKvmRN5tools8scrubbedISt5arrayIhLm32EEEEb]+0x30): undefined reference to `cn_slow_hash_pre'
../cryptonote_basic/libcryptonote_basic.a(cryptonote_format_utils.cpp.o): In function `cryptonote::generate_chacha_key_from_secret_keys(cryptonote::account_keys const&, tools::scrubbed<std::array<unsigned char, 32ul> >&)':
cryptonote_format_utils.cpp:(.text+0xba8): undefined reference to `cn_slow_hash_pre'
collect2: error: ld returned 1 exit status
src/wallet/CMakeFiles/wallet_rpc_server.dir/build.make:137: recipe for target 'bin/monero-wallet-rpc' failed
make[3]: *** [bin/monero-wallet-rpc] Error 1
make[3]: Leaving directory '/home/rock64/builds/monero/build/release'
CMakeFiles/Makefile2:2129: recipe for target 'src/wallet/CMakeFiles/wallet_rpc_server.dir/all' failed
make[2]: *** [src/wallet/CMakeFiles/wallet_rpc_server.dir/all] Error 2
make[2]: Leaving directory '/home/rock64/builds/monero/build/release'
Makefile:138: recipe for target 'all' failed
make[1]: *** [all] Error 2
make[1]: Leaving directory '/home/rock64/builds/monero/build/release'
Makefile:64: recipe for target 'release-all' failed
make: *** [release-all] Error 2
 ```

# Discussion History
## moneromooo-monero | 2018-03-06T20:38:15+00:00
Only one of the 4 cn_slow_hash versions got changed for ledger. The other three need to be changed to match.

## moneromooo-monero | 2018-03-06T20:46:50+00:00
Does https://github.com/moneromooo-monero/bitmonero/tree/slow fix it ?

## radfish | 2018-03-07T14:43:18+00:00
Still failing on Rock64 at 04a0cc89cf30f5c5c9a5c88c5e3c1b10a2c0f7e4 plus #3347 
```
[ 78%] Linking CXX executable ../../bin/monero-blockchain-import
../cryptonote_basic/libcryptonote_basic.a(cryptonote_format_utils.cpp.o): In function `cryptonote::generate_chacha_key_from_secret_keys(cryptonote::account_keys const&, tools::scrubbed<std::array<unsigned char, 32ul> >&)':
cryptonote_format_utils.cpp:(.text+0xc34): undefined reference to `cn_slow_hash_pre'
cryptonote_format_utils.cpp:(.text+0xc4c): undefined reference to `cn_slow_hash_pre'
collect2: error: ld returned 1 exit status
````

## moneromooo-monero | 2018-03-07T15:01:22+00:00
stoffu had the same fix in 3350. Also 3370 fixes the uint64 typo. 3350 + 3370 should fix it.

## radfish | 2018-03-09T04:13:37+00:00
confirming: 3350 + 3370 does build on rock64. thanks.

## moneromooo-monero | 2018-03-14T15:27:05+00:00
+resolved

# Action History
- Created by: grubles | 2018-03-06T02:30:55+00:00
- Closed at: 2018-03-14T15:40:52+00:00
