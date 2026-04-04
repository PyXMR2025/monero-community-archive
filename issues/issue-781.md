---
title: 'lto1: fatal error: bytecode stream generated with LTO version 2.2 instead
  of the expected 4.0 compilation terminated.'
source_url: https://github.com/monero-project/monero/issues/781
author: fluffypony
assignees: []
labels:
- invalid
created_at: '2016-04-02T04:17:24+00:00'
updated_at: '2017-10-03T10:36:23+00:00'
type: issue
status: closed
closed_at: '2017-10-03T10:36:23+00:00'
---

# Original Description
This occurred on the Linux64 buildbox today. We normally don't build tests for releases, this could simply be an effect of statically building tests?

```
Linking CXX executable unit_tests
CMakeFiles/unit_tests.dir/blockchain_db.cpp.o (symbol from plugin): warning: the use of `tmpnam' is dangerous, better use `mkstemp'
lto1: fatal error: bytecode stream generated with LTO version 2.2 instead of the expected 4.0
compilation terminated.
lto-wrapper: fatal error: /usr/bin/c++ returned 1 exit status
compilation terminated.
/usr/bin/ld: lto-wrapper failed
```

The actual command being run when this happens is:

```
/usr/bin/c++    -std=c++11 -D_GNU_SOURCE  -Wall -Wextra -Wpointer-arith -Wundef -Wvla -Wwrite-strings -Wno-error=extra -Wno-error=deprecated-declarations -Wno-error=sign-compare -Wno-error=strict-aliasing -Wno-error=type-limits -Wno-unused-parameter -Wno-error=unused-variable -Wno-error=undef -Wno-error=uninitialized -Werror -Wlogical-op -Wno-error=maybe-uninitialized -Wno-reorder -Wno-missing-field-initializers -march=x86-64 -maes -Ofast -DNDEBUG -Wno-unused-variable  -flto -ffat-lto-objects   -static-libgcc -static-libstdc++ CMakeFiles/unit_tests.dir/address_from_url.cpp.o CMakeFiles/unit_tests.dir/ban.cpp.o CMakeFiles/unit_tests.dir/base58.cpp.o CMakeFiles/unit_tests.dir/blockchain_db.cpp.o CMakeFiles/unit_tests.dir/block_reward.cpp.o CMakeFiles/unit_tests.dir/canonical_amounts.cpp.o CMakeFiles/unit_tests.dir/chacha8.cpp.o CMakeFiles/unit_tests.dir/checkpoints.cpp.o CMakeFiles/unit_tests.dir/decompose_amount_into_digits.cpp.o CMakeFiles/unit_tests.dir/dns_resolver.cpp.o CMakeFiles/unit_tests.dir/epee_boosted_tcp_server.cpp.o CMakeFiles/unit_tests.dir/epee_levin_protocol_handler_async.cpp.o CMakeFiles/unit_tests.dir/get_xtype_from_string.cpp.o CMakeFiles/unit_tests.dir/main.cpp.o CMakeFiles/unit_tests.dir/mnemonics.cpp.o CMakeFiles/unit_tests.dir/mul_div.cpp.o CMakeFiles/unit_tests.dir/parse_amount.cpp.o CMakeFiles/unit_tests.dir/serialization.cpp.o CMakeFiles/unit_tests.dir/slow_memmem.cpp.o CMakeFiles/unit_tests.dir/test_format_utils.cpp.o CMakeFiles/unit_tests.dir/test_peerlist.cpp.o CMakeFiles/unit_tests.dir/test_protocol_pack.cpp.o CMakeFiles/unit_tests.dir/hardfork.cpp.o CMakeFiles/unit_tests.dir/unbound.cpp.o  -o unit_tests -rdynamic ../../src/cryptonote_core/libcryptonote_core.a ../../src/blockchain_db/libblockchain_db.a ../../src/rpc/librpc.a ../../lib/libwallet.a ../../src/p2p/libp2p.a ../gtest/libgtest_main.a /usr/local/lib/libboost_chrono.a /usr/local/lib/libboost_regex.a /usr/local/lib/libboost_system.a /usr/local/lib/libboost_thread.a -Wl,-Bstatic -lunbound -lrt ../../src/cryptonote_protocol/libcryptonote_protocol.a ../../src/cryptonote_core/libcryptonote_core.a ../../src/blockchain_db/libblockchain_db.a ../../src/cryptonote_core/libcryptonote_core.a ../../src/blockchain_db/libblockchain_db.a ../../contrib/otshell_utils/libotshell_utils.a ../../src/blocks/libblocks.a -Wl,-Bdynamic /usr/local/lib/libboost_chrono.a ../../src/common/libcommon.a ../../external/unbound/libunbound.a -Wl,-Bstatic -lssl -lcrypto -Wl,-Bdynamic -ldl ../../src/crypto/libcrypto.a /usr/local/lib/libboost_date_time.a /usr/local/lib/libboost_program_options.a /usr/local/lib/libboost_filesystem.a ../../external/db_drivers/liblmdb/liblmdb.a /usr/local/lib/libboost_serialization.a /usr/local/lib/libboost_thread.a ../../src/mnemonics/libmnemonics.a /usr/local/lib/libboost_system.a ../gtest/libgtest.a -pthread -Wl,-Bstatic -lrt -Wl,-Bdynamic
```


# Discussion History
## tewinget | 2016-04-02T07:57:15+00:00
Based on this:
https://github.com/numenta/nupic/issues/1699#issuecomment-68493418

it seems that it may be that LTO is having issues linking something built
with one version of gcc to something built with a different version for
some reason.  My guess would be that your version of boost was built with a
different version of gcc than the one your system has.

Possible step for diagnosis: figure out which gcc the libboost in use was
built with `strings <path_to_a_libboost*.a_file> | grep 'GCC:'` and use
that version of gcc to build release-all.

On Sat, Apr 2, 2016 at 12:17 AM, Riccardo Spagni notifications@github.com
wrote:

> This occurred on the Linux64 buildbox today. We normally don't build tests
> for releases, this could simply be an effect of statically building tests?
> 
> Linking CXX executable unit_tests
> CMakeFiles/unit_tests.dir/blockchain_db.cpp.o (symbol from plugin): warning: the use of `tmpnam' is dangerous, better use`mkstemp'
> lto1: fatal error: bytecode stream generated with LTO version 2.2 instead of the expected 4.0
> compilation terminated.
> lto-wrapper: fatal error: /usr/bin/c++ returned 1 exit status
> compilation terminated.
> /usr/bin/ld: lto-wrapper failed
> 
> The actual command being run when this happens is:
> 
> /usr/bin/c++    -std=c++11 -D_GNU_SOURCE  -Wall -Wextra -Wpointer-arith -Wundef -Wvla -Wwrite-strings -Wno-error=extra -Wno-error=deprecated-declarations -Wno-error=sign-compare -Wno-error=strict-aliasing -Wno-error=type-limits -Wno-unused-parameter -Wno-error=unused-variable -Wno-error=undef -Wno-error=uninitialized -Werror -Wlogical-op -Wno-error=maybe-uninitialized -Wno-reorder -Wno-missing-field-initializers -march=x86-64 -maes -Ofast -DNDEBUG -Wno-unused-variable  -flto -ffat-lto-objects   -static-libgcc -static-libstdc++ CMakeFiles/unit_tests.dir/address_from_url.cpp.o CMakeFiles/unit_tests.dir/ban.cpp.o CMakeFiles/unit_tests.dir/base58.cpp.o CMakeFiles/unit_tests.dir/blockchain_db.cpp.o CMakeFiles/unit_tests.dir/block_reward.cpp.o CMakeFiles/unit_tests.dir/canonical_amounts.cpp.o CMakeFiles/unit_tests.dir/chacha8.cpp.o CMakeFiles/unit_tests.dir/checkpoints.cpp.o CMakeFiles/unit_tests.dir/decompose_amount_into_digits.cpp.o CMakeFiles/unit_tests.dir/dns_resolv
>  er.cpp.o
>   CMakeFiles/unit_tests.dir/epee_boosted_tcp_server.cpp.o CMakeFiles/unit_tests.dir/epee_levin_protocol_handler_async.cpp.o CMakeFiles/unit_tests.dir/get_xtype_from_string.cpp.o CMakeFiles/unit_tests.dir/main.cpp.o CMakeFiles/unit_tests.dir/mnemonics.cpp.o CMakeFiles/unit_tests.dir/mul_div.cpp.o CMakeFiles/unit_tests.dir/parse_amount.cpp.o CMakeFiles/unit_tests.dir/serialization.cpp.o CMakeFiles/unit_tests.dir/slow_memmem.cpp.o CMakeFiles/unit_tests.dir/test_format_utils.cpp.o CMakeFiles/unit_tests.dir/test_peerlist.cpp.o CMakeFiles/unit_tests.dir/test_protocol_pack.cpp.o CMakeFiles/unit_tests.dir/hardfork.cpp.o CMakeFiles/unit_tests.dir/unbound.cpp.o  -o unit_tests -rdynamic ../../src/cryptonote_core/libcryptonote_core.a ../../src/blockchain_db/libblockchain_db.a ../../src/rpc/librpc.a ../../lib/libwallet.a ../../src/p2p/libp2p.a ../gtest/libgtest_main.a /usr/local/lib/libboost_chrono.a /usr/local/lib/libboost_regex.a /usr/local/lib/libboost_system.a /usr/local/lib/libboost_
>  thread.a
>   -Wl,-Bstatic -lunbound -lrt ../../src/cryptonote_protocol/libcryptonote_protocol.a ../../src/cryptonote_core/libcryptonote_core.a ../../src/blockchain_db/libblockchain_db.a ../../src/cryptonote_core/libcryptonote_core.a ../../src/blockchain_db/libblockchain_db.a ../../contrib/otshell_utils/libotshell_utils.a ../../src/blocks/libblocks.a -Wl,-Bdynamic /usr/local/lib/libboost_chrono.a ../../src/common/libcommon.a ../../external/unbound/libunbound.a -Wl,-Bstatic -lssl -lcrypto -Wl,-Bdynamic -ldl ../../src/crypto/libcrypto.a /usr/local/lib/libboost_date_time.a /usr/local/lib/libboost_program_options.a /usr/local/lib/libboost_filesystem.a ../../external/db_drivers/liblmdb/liblmdb.a /usr/local/lib/libboost_serialization.a /usr/local/lib/libboost_thread.a ../../src/mnemonics/libmnemonics.a /usr/local/lib/libboost_system.a ../gtest/libgtest.a -pthread -Wl,-Bstatic -lrt -Wl,-Bdynamic
> 
> —
> You are receiving this because you are subscribed to this thread.
> Reply to this email directly or view it on GitHub
> https://github.com/monero-project/bitmonero/issues/781

## 

Thomas Winget
Computer Engineering
Purdue University '12


## ghost | 2017-09-03T13:40:23+00:00
Setup Swap
By default there is no swap setup on my VPS, it is required especially on a system with limited memory. I am setting up a 4GB swap, which is the most common swap size used for a VPS.

dd if=/dev/zero of=/mnt/myswap.swap bs=1M count=4000
mkswap /mnt/myswap.swap
swapon /mnt/myswap.swap

Now let’s add it into fstab so it will activate at boot.

nano /etc/fstab

Add the following line at the end of the file.

/mnt/myswap.swap none swap sw 0 0

## moneromooo-monero | 2017-10-03T10:25:42+00:00
I think I'll close this. It's likely a local thing (building with two different compilers), and LTO now defaults to off anyway.

+invalid

# Action History
- Created by: fluffypony | 2016-04-02T04:17:24+00:00
- Closed at: 2017-10-03T10:36:23+00:00
