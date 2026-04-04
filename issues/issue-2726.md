---
title: Build failed on Ubuntu 16.04.3 LTS, on tag release-v0.11.0.0
source_url: https://github.com/monero-project/monero/issues/2726
author: c0nst4nt
assignees: []
labels: []
created_at: '2017-10-24T18:36:28+00:00'
updated_at: '2017-10-24T20:36:00+00:00'
type: issue
status: closed
closed_at: '2017-10-24T20:36:00+00:00'
---

# Original Description
Have problems with make on v0.11. I can't understand what I'm doing wrong. All dependencies installed, but not sure about versions.

`/opt/monero# make
Scanning dependencies of target version
[  1%] Generating version/version.h
-- You are currently on commit fda88c8
-- The most recent tag was at 793bc97
-- You are ahead of or behind a tagged release
[  1%] Built target version
Scanning dependencies of target lmdb
[  2%] Building C object external/db_drivers/liblmdb/CMakeFiles/lmdb.dir/mdb.c.o
[  3%] Building C object external/db_drivers/liblmdb/CMakeFiles/lmdb.dir/midl.c.o
[  3%] Linking C shared library liblmdb.so
[  3%] Built target lmdb
Scanning dependencies of target easylogging
[  4%] Building CXX object external/easylogging++/CMakeFiles/easylogging.dir/easylogging++.cc.o
[  5%] Linking CXX shared library libeasylogging.so
[  5%] Built target easylogging
Scanning dependencies of target obj_cncrypto
[  6%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/aesb.c.o
[  7%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/blake256.c.o
[  7%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/chacha8.c.o
[  8%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/crypto-ops-data.c.o
[  9%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/crypto-ops.c.o
[ 10%] Building CXX object src/crypto/CMakeFiles/obj_cncrypto.dir/crypto.cpp.o
[ 11%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/groestl.c.o
[ 12%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/hash-extra-blake.c.o
[ 13%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/hash-extra-groestl.c.o
[ 13%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/hash-extra-jh.c.o
[ 14%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/hash-extra-skein.c.o
[ 15%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/hash.c.o
[ 16%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/jh.c.o
[ 17%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/keccak.c.o
[ 18%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/oaes_lib.c.o
[ 19%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/random.c.o
[ 19%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/skein.c.o
[ 20%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/slow-hash.c.o
[ 21%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/tree-hash.c.o
[ 21%] Built target obj_cncrypto
Scanning dependencies of target cncrypto
[ 22%] Linking CXX shared library libcncrypto.so
[ 22%] Built target cncrypto
Scanning dependencies of target epee
[ 23%] Building CXX object contrib/epee/src/CMakeFiles/epee.dir/hex.cpp.o
[ 23%] Building CXX object contrib/epee/src/CMakeFiles/epee.dir/http_auth.cpp.o
[ 24%] Building CXX object contrib/epee/src/CMakeFiles/epee.dir/mlog.cpp.o
[ 25%] Building CXX object contrib/epee/src/CMakeFiles/epee.dir/string_tools.cpp.o
[ 26%] Building CXX object contrib/epee/src/CMakeFiles/epee.dir/readline_buffer.cpp.o
[ 27%] Linking CXX static library libepee.a
[ 27%] Built target epee
Scanning dependencies of target obj_common
[ 28%] Building CXX object src/common/CMakeFiles/obj_common.dir/base58.cpp.o
[ 29%] Building CXX object src/common/CMakeFiles/obj_common.dir/command_line.cpp.o
[ 30%] Building CXX object src/common/CMakeFiles/obj_common.dir/dns_utils.cpp.o
[ 30%] Building CXX object src/common/CMakeFiles/obj_common.dir/download.cpp.o
[ 31%] Building CXX object src/common/CMakeFiles/obj_common.dir/util.cpp.o
[ 32%] Building CXX object src/common/CMakeFiles/obj_common.dir/i18n.cpp.o
[ 33%] Building CXX object src/common/CMakeFiles/obj_common.dir/password.cpp.o
[ 34%] Building CXX object src/common/CMakeFiles/obj_common.dir/perf_timer.cpp.o
[ 35%] Building CXX object src/common/CMakeFiles/obj_common.dir/task_region.cpp.o
[ 36%] Building CXX object src/common/CMakeFiles/obj_common.dir/thread_group.cpp.o
[ 36%] Building CXX object src/common/CMakeFiles/obj_common.dir/updates.cpp.o
[ 37%] Building CXX object src/common/CMakeFiles/obj_common.dir/stack_trace.cpp.o
[ 37%] Built target obj_common
Scanning dependencies of target common
[ 38%] Linking CXX shared library libcommon.so
[ 38%] Built target common
Scanning dependencies of target obj_ringct
[ 39%] Building CXX object src/ringct/CMakeFiles/obj_ringct.dir/rctOps.cpp.o
[ 40%] Building CXX object src/ringct/CMakeFiles/obj_ringct.dir/rctSigs.cpp.o
[ 41%] Building CXX object src/ringct/CMakeFiles/obj_ringct.dir/rctTypes.cpp.o
[ 42%] Building C object src/ringct/CMakeFiles/obj_ringct.dir/rctCryptoOps.c.o
[ 42%] Built target obj_ringct
Scanning dependencies of target obj_cryptonote_basic
[ 43%] Building CXX object src/cryptonote_basic/CMakeFiles/obj_cryptonote_basic.dir/account.cpp.o
[ 44%] Building CXX object src/cryptonote_basic/CMakeFiles/obj_cryptonote_basic.dir/checkpoints.cpp.o
[ 45%] Building CXX object src/cryptonote_basic/CMakeFiles/obj_cryptonote_basic.dir/cryptonote_basic_impl.cpp.o
[ 46%] Building CXX object src/cryptonote_basic/CMakeFiles/obj_cryptonote_basic.dir/cryptonote_format_utils.cpp.o
[ 46%] Building CXX object src/cryptonote_basic/CMakeFiles/obj_cryptonote_basic.dir/difficulty.cpp.o
[ 47%] Building CXX object src/cryptonote_basic/CMakeFiles/obj_cryptonote_basic.dir/hardfork.cpp.o
[ 48%] Building CXX object src/cryptonote_basic/CMakeFiles/obj_cryptonote_basic.dir/miner.cpp.o
[ 48%] Built target obj_cryptonote_basic
Scanning dependencies of target cryptonote_basic
[ 49%] Linking CXX shared library libcryptonote_basic.so
[ 49%] Built target cryptonote_basic
Scanning dependencies of target ringct
[ 50%] Linking CXX shared library libringct.so
[ 50%] Built target ringct
Scanning dependencies of target obj_cryptonote_core
[ 51%] Building CXX object src/cryptonote_core/CMakeFiles/obj_cryptonote_core.dir/blockchain.cpp.o
[ 52%] Building CXX object src/cryptonote_core/CMakeFiles/obj_cryptonote_core.dir/cryptonote_core.cpp.o
[ 53%] Building CXX object src/cryptonote_core/CMakeFiles/obj_cryptonote_core.dir/tx_pool.cpp.o
[ 54%] Building CXX object src/cryptonote_core/CMakeFiles/obj_cryptonote_core.dir/cryptonote_tx_utils.cpp.o
[ 54%] Built target obj_cryptonote_core
[ 55%] Generating testnet_blocks.o
[ 56%] Generating blocks.o
Scanning dependencies of target blocks
[ 57%] Building C object src/blocks/CMakeFiles/blocks.dir/blockexports.c.o
[ 57%] Linking C static library libblocks.a
[ 57%] Built target blocks
Scanning dependencies of target obj_blockchain_db
[ 58%] Building CXX object src/blockchain_db/CMakeFiles/obj_blockchain_db.dir/blockchain_db.cpp.o
[ 59%] Building CXX object src/blockchain_db/CMakeFiles/obj_blockchain_db.dir/lmdb/db_lmdb.cpp.o
[ 59%] Built target obj_blockchain_db
Scanning dependencies of target blockchain_db
[ 59%] Linking CXX shared library libblockchain_db.so
[ 59%] Built target blockchain_db
Scanning dependencies of target cryptonote_core
[ 60%] Linking CXX shared library libcryptonote_core.so
[ 60%] Built target cryptonote_core
Scanning dependencies of target obj_mnemonics
[ 61%] Building CXX object src/mnemonics/CMakeFiles/obj_mnemonics.dir/electrum-words.cpp.o
[ 61%] Built target obj_mnemonics
Scanning dependencies of target mnemonics
[ 62%] Linking CXX shared library libmnemonics.so
[ 62%] Built target mnemonics
Scanning dependencies of target obj_rpc
[ 63%] Building CXX object src/rpc/CMakeFiles/obj_rpc.dir/core_rpc_server.cpp.o
c++: internal compiler error: Убито (program cc1plus)
Please submit a full bug report,
with preprocessed source if appropriate.
See <file:///usr/share/doc/gcc-5/README.Bugs> for instructions.
src/rpc/CMakeFiles/obj_rpc.dir/build.make:62: ошибка выполнения рецепта для цели «src/rpc/CMakeFiles/obj_rpc.dir/core_rpc_server.cpp.o»
make[2]: *** [src/rpc/CMakeFiles/obj_rpc.dir/core_rpc_server.cpp.o] Ошибка 4
CMakeFiles/Makefile2:1147: ошибка выполнения рецепта для цели «src/rpc/CMakeFiles/obj_rpc.dir/all»
make[1]: *** [src/rpc/CMakeFiles/obj_rpc.dir/all] Ошибка 2
Makefile:138: ошибка выполнения рецепта для цели «all»
make: *** [all] Ошибка 2
`

# Discussion History
## moneromooo-monero | 2017-10-24T18:40:45+00:00
What does Убито mean ?

## c0nst4nt | 2017-10-24T19:00:45+00:00
@moneromooo-monero on my russian locale it means "killed"

## radfish | 2017-10-24T19:07:39+00:00
Looks like insufficient RAM. You need about 1.5-2GB RAM per thread. Try
adding more swap. And pass 'make -j1' to be sure it's not parallizing.

On Tue, Oct 24, 2017 at 11:36:37AM -0700, Constantin wrote:
> Have problems with make on v0.11. I can't understand what I'm doing wrong. All dependencies installed, but not sure about versions.
> 
> `/opt/monero# make
> Scanning dependencies of target version
> [  1%] Generating version/version.h
> -- You are currently on commit fda88c8
> -- The most recent tag was at 793bc97
> -- You are ahead of or behind a tagged release
> [  1%] Built target version
> Scanning dependencies of target lmdb
> [  2%] Building C object external/db_drivers/liblmdb/CMakeFiles/lmdb.dir/mdb.c.o
> [  3%] Building C object external/db_drivers/liblmdb/CMakeFiles/lmdb.dir/midl.c.o
> [  3%] Linking C shared library liblmdb.so
> [  3%] Built target lmdb
> Scanning dependencies of target easylogging
> [  4%] Building CXX object external/easylogging++/CMakeFiles/easylogging.dir/easylogging++.cc.o
> [  5%] Linking CXX shared library libeasylogging.so
> [  5%] Built target easylogging
> Scanning dependencies of target obj_cncrypto
> [  6%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/aesb.c.o
> [  7%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/blake256.c.o
> [  7%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/chacha8.c.o
> [  8%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/crypto-ops-data.c.o
> [  9%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/crypto-ops.c.o
> [ 10%] Building CXX object src/crypto/CMakeFiles/obj_cncrypto.dir/crypto.cpp.o
> [ 11%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/groestl.c.o
> [ 12%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/hash-extra-blake.c.o
> [ 13%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/hash-extra-groestl.c.o
> [ 13%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/hash-extra-jh.c.o
> [ 14%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/hash-extra-skein.c.o
> [ 15%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/hash.c.o
> [ 16%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/jh.c.o
> [ 17%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/keccak.c.o
> [ 18%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/oaes_lib.c.o
> [ 19%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/random.c.o
> [ 19%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/skein.c.o
> [ 20%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/slow-hash.c.o
> [ 21%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/tree-hash.c.o
> [ 21%] Built target obj_cncrypto
> Scanning dependencies of target cncrypto
> [ 22%] Linking CXX shared library libcncrypto.so
> [ 22%] Built target cncrypto
> Scanning dependencies of target epee
> [ 23%] Building CXX object contrib/epee/src/CMakeFiles/epee.dir/hex.cpp.o
> [ 23%] Building CXX object contrib/epee/src/CMakeFiles/epee.dir/http_auth.cpp.o
> [ 24%] Building CXX object contrib/epee/src/CMakeFiles/epee.dir/mlog.cpp.o
> [ 25%] Building CXX object contrib/epee/src/CMakeFiles/epee.dir/string_tools.cpp.o
> [ 26%] Building CXX object contrib/epee/src/CMakeFiles/epee.dir/readline_buffer.cpp.o
> [ 27%] Linking CXX static library libepee.a
> [ 27%] Built target epee
> Scanning dependencies of target obj_common
> [ 28%] Building CXX object src/common/CMakeFiles/obj_common.dir/base58.cpp.o
> [ 29%] Building CXX object src/common/CMakeFiles/obj_common.dir/command_line.cpp.o
> [ 30%] Building CXX object src/common/CMakeFiles/obj_common.dir/dns_utils.cpp.o
> [ 30%] Building CXX object src/common/CMakeFiles/obj_common.dir/download.cpp.o
> [ 31%] Building CXX object src/common/CMakeFiles/obj_common.dir/util.cpp.o
> [ 32%] Building CXX object src/common/CMakeFiles/obj_common.dir/i18n.cpp.o
> [ 33%] Building CXX object src/common/CMakeFiles/obj_common.dir/password.cpp.o
> [ 34%] Building CXX object src/common/CMakeFiles/obj_common.dir/perf_timer.cpp.o
> [ 35%] Building CXX object src/common/CMakeFiles/obj_common.dir/task_region.cpp.o
> [ 36%] Building CXX object src/common/CMakeFiles/obj_common.dir/thread_group.cpp.o
> [ 36%] Building CXX object src/common/CMakeFiles/obj_common.dir/updates.cpp.o
> [ 37%] Building CXX object src/common/CMakeFiles/obj_common.dir/stack_trace.cpp.o
> [ 37%] Built target obj_common
> Scanning dependencies of target common
> [ 38%] Linking CXX shared library libcommon.so
> [ 38%] Built target common
> Scanning dependencies of target obj_ringct
> [ 39%] Building CXX object src/ringct/CMakeFiles/obj_ringct.dir/rctOps.cpp.o
> [ 40%] Building CXX object src/ringct/CMakeFiles/obj_ringct.dir/rctSigs.cpp.o
> [ 41%] Building CXX object src/ringct/CMakeFiles/obj_ringct.dir/rctTypes.cpp.o
> [ 42%] Building C object src/ringct/CMakeFiles/obj_ringct.dir/rctCryptoOps.c.o
> [ 42%] Built target obj_ringct
> Scanning dependencies of target obj_cryptonote_basic
> [ 43%] Building CXX object src/cryptonote_basic/CMakeFiles/obj_cryptonote_basic.dir/account.cpp.o
> [ 44%] Building CXX object src/cryptonote_basic/CMakeFiles/obj_cryptonote_basic.dir/checkpoints.cpp.o
> [ 45%] Building CXX object src/cryptonote_basic/CMakeFiles/obj_cryptonote_basic.dir/cryptonote_basic_impl.cpp.o
> [ 46%] Building CXX object src/cryptonote_basic/CMakeFiles/obj_cryptonote_basic.dir/cryptonote_format_utils.cpp.o
> [ 46%] Building CXX object src/cryptonote_basic/CMakeFiles/obj_cryptonote_basic.dir/difficulty.cpp.o
> [ 47%] Building CXX object src/cryptonote_basic/CMakeFiles/obj_cryptonote_basic.dir/hardfork.cpp.o
> [ 48%] Building CXX object src/cryptonote_basic/CMakeFiles/obj_cryptonote_basic.dir/miner.cpp.o
> [ 48%] Built target obj_cryptonote_basic
> Scanning dependencies of target cryptonote_basic
> [ 49%] Linking CXX shared library libcryptonote_basic.so
> [ 49%] Built target cryptonote_basic
> Scanning dependencies of target ringct
> [ 50%] Linking CXX shared library libringct.so
> [ 50%] Built target ringct
> Scanning dependencies of target obj_cryptonote_core
> [ 51%] Building CXX object src/cryptonote_core/CMakeFiles/obj_cryptonote_core.dir/blockchain.cpp.o
> [ 52%] Building CXX object src/cryptonote_core/CMakeFiles/obj_cryptonote_core.dir/cryptonote_core.cpp.o
> [ 53%] Building CXX object src/cryptonote_core/CMakeFiles/obj_cryptonote_core.dir/tx_pool.cpp.o
> [ 54%] Building CXX object src/cryptonote_core/CMakeFiles/obj_cryptonote_core.dir/cryptonote_tx_utils.cpp.o
> [ 54%] Built target obj_cryptonote_core
> [ 55%] Generating testnet_blocks.o
> [ 56%] Generating blocks.o
> Scanning dependencies of target blocks
> [ 57%] Building C object src/blocks/CMakeFiles/blocks.dir/blockexports.c.o
> [ 57%] Linking C static library libblocks.a
> [ 57%] Built target blocks
> Scanning dependencies of target obj_blockchain_db
> [ 58%] Building CXX object src/blockchain_db/CMakeFiles/obj_blockchain_db.dir/blockchain_db.cpp.o
> [ 59%] Building CXX object src/blockchain_db/CMakeFiles/obj_blockchain_db.dir/lmdb/db_lmdb.cpp.o
> [ 59%] Built target obj_blockchain_db
> Scanning dependencies of target blockchain_db
> [ 59%] Linking CXX shared library libblockchain_db.so
> [ 59%] Built target blockchain_db
> Scanning dependencies of target cryptonote_core
> [ 60%] Linking CXX shared library libcryptonote_core.so
> [ 60%] Built target cryptonote_core
> Scanning dependencies of target obj_mnemonics
> [ 61%] Building CXX object src/mnemonics/CMakeFiles/obj_mnemonics.dir/electrum-words.cpp.o
> [ 61%] Built target obj_mnemonics
> Scanning dependencies of target mnemonics
> [ 62%] Linking CXX shared library libmnemonics.so
> [ 62%] Built target mnemonics
> Scanning dependencies of target obj_rpc
> [ 63%] Building CXX object src/rpc/CMakeFiles/obj_rpc.dir/core_rpc_server.cpp.o
> c++: internal compiler error: Убито (program cc1plus)
> Please submit a full bug report,
> with preprocessed source if appropriate.
> See <file:///usr/share/doc/gcc-5/README.Bugs> for instructions.
> src/rpc/CMakeFiles/obj_rpc.dir/build.make:62: ошибка выполнения рецепта для цели «src/rpc/CMakeFiles/obj_rpc.dir/core_rpc_server.cpp.o»
> make[2]: *** [src/rpc/CMakeFiles/obj_rpc.dir/core_rpc_server.cpp.o] Ошибка 4
> CMakeFiles/Makefile2:1147: ошибка выполнения рецепта для цели «src/rpc/CMakeFiles/obj_rpc.dir/all»
> make[1]: *** [src/rpc/CMakeFiles/obj_rpc.dir/all] Ошибка 2
> Makefile:138: ошибка выполнения рецепта для цели «all»
> make: *** [all] Ошибка 2
> `
> 
> -- 
> You are receiving this because you are subscribed to this thread.
> Reply to this email directly or view it on GitHub:
> https://github.com/monero-project/monero/issues/2726


## c0nst4nt | 2017-10-24T20:36:00+00:00
@radfish interesting, looks like you're right. Tried to build on vps with only 1GM Ram, on local machine with more memory it works normally. Thanks)

# Action History
- Created by: c0nst4nt | 2017-10-24T18:36:28+00:00
- Closed at: 2017-10-24T20:36:00+00:00
