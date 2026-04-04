---
title: Boost Reference not difined
source_url: https://github.com/monero-project/monero/issues/8446
author: dedetuga
assignees: []
labels: []
created_at: '2022-07-20T22:27:17+00:00'
updated_at: '2022-07-23T08:14:15+00:00'
type: issue
status: closed
closed_at: '2022-07-23T08:14:15+00:00'
---

# Original Description
Hi,
I'm trying to compile monero from git repo, I instaled all the dependecies and I'm geting this error:


`db_lmdb.cpp:(.text.unlikely+0x7de0): referência não definida para "boost::detail::set_tss_data(void const*, void (*)(void (*)(void*), void*), void (*)(void*), void*, bool)"
collect2: error: ld returned 1 exit status
make[3]: *** [src/wallet/CMakeFiles/wallet_rpc_server.dir/build.make:142: bin/monero-wallet-rpc] Erro 1
make[3]: a sair da pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
make[2]: *** [CMakeFiles/Makefile2:3484: src/wallet/CMakeFiles/wallet_rpc_server.dir/all] Erro 2
make[2]: a sair da pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
make[1]: *** [Makefile:141: all] Erro 2
make[1]: a sair da pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
make: *** [Makefile:103: release-all] Erro 2
`

I'm using Ubuntu 20.04.3 LTS

How can i solve this?

thanks  

# Discussion History
## selsta | 2022-07-20T23:03:49+00:00
Can you do `apt update` and `apt upgrade` and then do a clean build? Did you do any source code changes?

## dedetuga | 2022-07-21T09:07:54+00:00
Thanks for reply, nothing change


there is a full output:



`mkdir -p build/"Linux/release-v0.18"/release
cd build/"Linux/release-v0.18"/release && cmake -D BUILD_TESTS=ON -D CMAKE_BUILD_TYPE=Release ../../../.. && make
-- CMake version 3.16.3
-- Found usable ccache: /usr/bin/ccache
-- Building without build tag
-- Checking submodules
-- Submodule 'external/miniupnp' is up-to-date
-- Submodule 'external/rapidjson' is up-to-date
-- Submodule 'external/trezor-common' is up-to-date
-- Submodule 'external/randomx' is up-to-date
-- Submodule 'external/supercop' is up-to-date
-- Could not find DEVELOPER_LOCAL_TOOLS in env (not required)
-- BOOST_IGNORE_SYSTEM_PATHS defaults to OFF
-- Building for a 64-bit system
-- Building internal libraries as static
-- Using LMDB as default DB type
-- Stack trace on exception enabled (using easylogging++)
-- Using OpenSSL include dir at /usr/include
-- Could NOT find MiniUPnPc (missing: MINIUPNP_INCLUDE_DIR MINIUPNP_LIBRARY) 
-- Using in-tree miniupnpc
-- Looking for libunbound
-- Found libunbound include (unbound.h) in /usr/include
-- Found libunbound library
-- Using 64-bit LMDB from source tree
-- Backtrace_LIBRARY: 
-- Performing Test _march=native_cxx
-- Performing Test _march=native_cxx - Success
-- Setting CXX flag -march=native
-- Performing Test _march=native_c
-- Performing Test _march=native_c - Success
-- Setting C flag -march=native
-- Using HIDAPI include dir at /usr/include/hidapi
-- Protobuf lib: /usr/local/lib/libprotobuf.so, inc: /usr/local/include, protoc: /usr/local/bin/protoc
-- Trezor protobuf messages regenerated out: "."
-- LibUSB Compilation test: TRUE
-- Trezor compatible LibUSB found at: /usr/include/libusb-1.0
-- Building on x86_64 for native
-- AES support enabled
-- Performing Test _Werror__fcf_protection=full_c
-- Performing Test _Werror__fcf_protection=full_c - Success
-- Performing Test _Werror__fcf_protection=full_cxx
-- Performing Test _Werror__fcf_protection=full_cxx - Success
-- Performing Test _Werror__Werror=switch_c
-- Performing Test _Werror__Werror=switch_c - Success
-- Performing Test _Werror__Werror=switch_cxx
-- Performing Test _Werror__Werror=switch_cxx - Success
-- Performing Test _Werror__Werror=return_type_c
-- Performing Test _Werror__Werror=return_type_c - Success
-- Performing Test _Werror__Werror=return_type_cxx
-- Performing Test _Werror__Werror=return_type_cxx - Success
-- Using C security hardening flags:  -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -fstack-protector -fstack-protector-strong -fcf-protection=full -fstack-clash-protection -Werror=switch -Werror=return-type
-- Using C++ security hardening flags:  -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -fstack-protector -fstack-protector-strong -fcf-protection=full -fstack-clash-protection -Werror=switch -Werror=return-type
-- Using linker security hardening flags:  -pie -Wl,-z,relro -Wl,-z,now -Wl,-z,noexecstack -Wl,-z,noexecheap
-- Found Boost Version: 107100
-- Found readline library at: /usr
-- Found Git: /usr/bin/git
-- You are currently on commit b6a029f22
-- You are building a tagged release
Wallet crypto is using amd64-64-24k backend
-- Trezor support enabled
-- Building tests
Wallet crypto bench is using cn;amd64-64-24k;amd64-51-30k
-- Not building debug utilities
-- Configuring done
-- Generating done
-- Build files have been written to: /home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release
make[1]: a entrar na pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
make[2]: a entrar na pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
make[3]: a entrar na pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
make[3]: a sair da pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
[  2%] Built target generate_translations_header
make[3]: a entrar na pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
make[3]: a sair da pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
[  5%] Built target libminiupnpc-static
make[3]: a entrar na pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
make[3]: a sair da pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
[  5%] Built target upnpc-static
make[3]: a entrar na pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
make[3]: a sair da pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
[  5%] Built target testupnpreplyparse
make[3]: a entrar na pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
make[3]: a sair da pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
[  8%] Built target libminiupnpc-shared
make[3]: a entrar na pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
make[3]: a sair da pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
[  9%] Built target upnpc-shared
make[3]: a entrar na pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
make[3]: a sair da pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
[  9%] Built target listdevices
make[3]: a entrar na pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
make[3]: a sair da pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
[  9%] Built target testaddr_is_reserved
make[3]: a entrar na pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
make[3]: a sair da pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
[ 10%] Built target testminixml
make[3]: a entrar na pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
make[3]: a sair da pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
[ 12%] Built target testminiwget
make[3]: a entrar na pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
make[3]: a sair da pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
[ 12%] Built target minixmlvalid
make[3]: a entrar na pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
make[3]: a sair da pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
[ 15%] Built target testigddescparse
make[3]: a entrar na pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
make[3]: a sair da pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
[ 15%] Built target lmdb
make[3]: a entrar na pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
make[3]: a sair da pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
[ 16%] Built target easylogging
make[3]: a entrar na pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
make[3]: a sair da pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
[ 16%] Built target qrcodegen
make[3]: a entrar na pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
make[3]: a sair da pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
[ 16%] Built target obj_epee_readline
make[3]: a entrar na pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
make[3]: a sair da pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
[ 16%] Built target epee_readline
make[3]: a entrar na pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
make[3]: a sair da pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
[ 20%] Built target obj_epee
make[3]: a entrar na pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
make[3]: a sair da pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
[ 20%] Built target epee
make[3]: a entrar na pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
make[3]: a sair da pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
[ 20%] Built target genversion
make[3]: a entrar na pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
make[3]: a sair da pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
[ 20%] Built target obj_version
make[3]: a entrar na pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
make[3]: a sair da pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
[ 20%] Built target version
make[3]: a entrar na pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
make[3]: a sair da pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
[ 24%] Built target obj_cncrypto
make[3]: a entrar na pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
make[3]: a sair da pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
[ 29%] Built target randomx
make[3]: a entrar na pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
make[3]: a sair da pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
[ 30%] Built target cncrypto
make[3]: a entrar na pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
make[3]: a sair da pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
[ 34%] Built target obj_common
make[3]: a entrar na pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
make[3]: a sair da pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
[ 34%] Built target common
make[3]: a entrar na pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
make[3]: a sair da pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
[ 39%] Built target monero-crypto-amd64-64-24k
make[3]: a entrar na pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
make[3]: a sair da pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
[ 39%] Built target wallet-crypto
make[3]: a entrar na pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
make[3]: a sair da pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
[ 39%] Built target obj_device
make[3]: a entrar na pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
make[3]: a sair da pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
[ 40%] Built target obj_ringct_basic
make[3]: a entrar na pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
make[3]: a sair da pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
[ 40%] Built target ringct_basic
make[3]: a entrar na pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
make[3]: a sair da pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
[ 40%] Built target obj_cryptonote_format_utils_basic
make[3]: a entrar na pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
make[3]: a sair da pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
[ 40%] Built target cryptonote_format_utils_basic
make[3]: a entrar na pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
make[3]: a sair da pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
[ 41%] Built target obj_blocks
make[3]: a entrar na pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
make[3]: a sair da pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
[ 41%] Built target blocks
make[3]: a entrar na pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
make[3]: a sair da pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
[ 41%] Built target device
make[3]: a entrar na pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
make[3]: a sair da pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
[ 41%] Built target obj_ringct
make[3]: a entrar na pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
make[3]: a sair da pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
[ 41%] Built target obj_checkpoints
make[3]: a entrar na pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
make[3]: a sair da pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
[ 41%] Built target checkpoints
make[3]: a entrar na pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
make[3]: a sair da pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
[ 42%] Built target obj_cryptonote_basic
make[3]: a entrar na pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
make[3]: a sair da pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
[ 42%] Built target cryptonote_basic
make[3]: a entrar na pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
make[3]: a sair da pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
[ 42%] Built target ringct
make[3]: a entrar na pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
make[3]: a sair da pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
[ 43%] Built target obj_cryptonote_core
make[3]: a entrar na pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
make[3]: a sair da pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
[ 43%] Built target obj_hardforks
make[3]: a entrar na pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
make[3]: a sair da pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
[ 43%] Built target hardforks
make[3]: a entrar na pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
make[3]: a sair da pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
[ 44%] Built target obj_blockchain_db
make[3]: a entrar na pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
make[3]: a sair da pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
[ 45%] Built target blockchain_db
make[3]: a entrar na pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
make[3]: a sair da pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
[ 46%] Built target cryptonote_core
make[3]: a entrar na pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
make[3]: a sair da pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
[ 47%] Built target obj_lmdb_lib
make[3]: a entrar na pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
make[3]: a sair da pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
[ 48%] Built target lmdb_lib
make[3]: a entrar na pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
make[3]: a sair da pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
[ 49%] Built target obj_multisig
make[3]: a entrar na pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
make[3]: a sair da pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
[ 50%] Built target multisig
make[3]: a entrar na pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
make[3]: a sair da pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
[ 52%] Built target obj_net
make[3]: a entrar na pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
make[3]: a sair da pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
[ 52%] Built target net
make[3]: a entrar na pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
make[3]: a sair da pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
[ 52%] Built target obj_mnemonics
make[3]: a entrar na pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
make[3]: a sair da pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
[ 53%] Built target mnemonics
make[3]: a entrar na pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
make[3]: a sair da pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
[ 53%] Built target obj_rpc_pub
make[3]: a entrar na pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
make[3]: a sair da pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
[ 53%] Built target obj_serialization
make[3]: a entrar na pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
make[3]: a sair da pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
[ 53%] Built target obj_p2p
make[3]: a entrar na pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
make[3]: a sair da pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
[ 53%] Built target p2p
make[3]: a entrar na pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
make[3]: a sair da pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
[ 54%] Built target obj_cryptonote_protocol
make[3]: a entrar na pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
make[3]: a sair da pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
[ 54%] Built target cryptonote_protocol
make[3]: a entrar na pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
make[3]: a sair da pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
[ 54%] Built target serialization
make[3]: a entrar na pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
make[3]: a sair da pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
[ 55%] Built target rpc_pub
make[3]: a entrar na pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
make[3]: a sair da pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
[ 56%] Built target obj_rpc_base
make[3]: a entrar na pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
make[3]: a sair da pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
[ 56%] Built target rpc_base
make[3]: a entrar na pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
make[3]: a sair da pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
[ 57%] Built target obj_rpc
make[3]: a entrar na pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
make[3]: a sair da pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
[ 57%] Built target obj_daemon_rpc_server
make[3]: a entrar na pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
make[3]: a sair da pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
[ 57%] Built target rpc
make[3]: a entrar na pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
make[3]: a sair da pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
[ 57%] Built target obj_daemon_messages
make[3]: a entrar na pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
make[3]: a sair da pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
[ 57%] Built target daemon_messages
make[3]: a entrar na pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
make[3]: a sair da pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
[ 57%] Built target daemon_rpc_server
make[3]: a entrar na pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
make[3]: a sair da pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
[ 59%] Built target obj_device_trezor
make[3]: a entrar na pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
make[3]: a sair da pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
[ 59%] Built target device_trezor
make[3]: a entrar na pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
make[3]: a sair da pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
[ 60%] Built target obj_wallet
make[3]: a entrar na pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
make[3]: a sair da pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
[ 60%] Built target wallet
make[3]: a entrar na pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
make[3]: a sair da pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
[ 61%] Built target obj_daemonizer
make[3]: a entrar na pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
make[3]: a sair da pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
[ 62%] Built target daemonizer
make[3]: a entrar na pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
make[3]: a sair da pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
make[3]: a entrar na pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
[ 63%] Linking CXX executable ../../bin/monero-wallet-rpc
/usr/bin/ld: aviso: -z noexecheap ignorada
/usr/bin/ld: CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o: na função "tools::wallet_rpc_server::on_get_accounts(epee::misc_utils::struct_init<tools::wallet_rpc::COMMAND_RPC_GET_ACCOUNTS::request_t> const&, epee::misc_utils::struct_init<tools::wallet_rpc::COMMAND_RPC_GET_ACCOUNTS::response_t>&, epee::json_rpc::error&, epee::net_utils::connection_context_base const*)":
wallet_rpc_server.cpp:(.text+0x225cc): referência não definida para "boost::re_detail_107100::perl_matcher<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > >, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::construct_init(boost::basic_regex<char, boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, boost::regex_constants::_match_flags)"
/usr/bin/ld: CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o: na função "boost::re_detail_107100::perl_matcher<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > >, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::unwind_extra_block(bool)":
wallet_rpc_server.cpp:(.text._ZN5boost16re_detail_10710012perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISC_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE18unwind_extra_blockEb[_ZN5boost16re_detail_10710012perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISC_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE18unwind_extra_blockEb]+0x30): referência não definida para "boost::re_detail_107100::put_mem_block(void*)"
/usr/bin/ld: CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o: na função "void boost::serialization::throw_exception<boost::archive::portable_binary_iarchive_exception>(boost::archive::portable_binary_iarchive_exception const&)":
wallet_rpc_server.cpp:(.text.unlikely._ZN5boost13serialization15throw_exceptionINS_7archive34portable_binary_iarchive_exceptionEEEvRKT_[_ZN5boost13serialization15throw_exceptionINS_7archive34portable_binary_iarchive_exceptionEEEvRKT_]+0x38): referência não definida para "boost::archive::archive_exception::archive_exception(boost::archive::archive_exception const&)"
/usr/bin/ld: CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o: na função "void boost::serialization::throw_exception<boost::archive::archive_exception>(boost::archive::archive_exception const&)":
wallet_rpc_server.cpp:(.text.unlikely._ZN5boost13serialization15throw_exceptionINS_7archive17archive_exceptionEEEvRKT_[_ZN5boost13serialization15throw_exceptionINS_7archive17archive_exceptionEEEvRKT_]+0x1f): referência não definida para "boost::archive::archive_exception::archive_exception(boost::archive::archive_exception const&)"
/usr/bin/ld: CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o: na função "epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::timed_wait_server_stop(unsigned long)":
wallet_rpc_server.cpp:(.text._ZN4epee9net_utils18boosted_tcp_serverINS0_4http19http_custom_handlerINS0_23connection_context_baseEEEE22timed_wait_server_stopEm[_ZN4epee9net_utils18boosted_tcp_serverINS0_4http19http_custom_handlerINS0_23connection_context_baseEEEE22timed_wait_server_stopEm]+0xff): referência não definida para "boost::thread::do_try_join_until_noexcept(boost::detail::mono_platform_timepoint const&, bool&)"
/usr/bin/ld: CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o: na função "void boost::re_detail_107100::raise_error<boost::regex_traits_wrapper<boost::regex_traits<char, boost::cpp_regex_traits<char> > > >(boost::regex_traits_wrapper<boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, boost::regex_constants::error_type)":
wallet_rpc_server.cpp:(.text._ZN5boost16re_detail_10710011raise_errorINS_20regex_traits_wrapperINS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEEEEEvRKT_NS_15regex_constants10error_typeE[_ZN5boost16re_detail_10710011raise_errorINS_20regex_traits_wrapperINS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEEEEEvRKT_NS_15regex_constants10error_typeE]+0xa1): referência não definida para "boost::re_detail_107100::get_default_error_string(boost::regex_constants::error_type)"
/usr/bin/ld: wallet_rpc_server.cpp:(.text._ZN5boost16re_detail_10710011raise_errorINS_20regex_traits_wrapperINS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEEEEEvRKT_NS_15regex_constants10error_typeE[_ZN5boost16re_detail_10710011raise_errorINS_20regex_traits_wrapperINS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEEEEEvRKT_NS_15regex_constants10error_typeE]+0xdb): referência não definida para "boost::re_detail_107100::raise_runtime_error(std::runtime_error const&)"
/usr/bin/ld: CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o: na função "__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > boost::re_detail_107100::re_is_set_member<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, char, boost::regex_traits<char, boost::cpp_regex_traits<char> >, unsigned int>(__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, __gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, boost::re_detail_107100::re_set_long<unsigned int> const*, boost::re_detail_107100::regex_data<char, boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, bool)":
wallet_rpc_server.cpp:(.text._ZN5boost16re_detail_10710016re_is_set_memberIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEEcNS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEjEET_SH_SH_PKNS0_11re_set_longIT2_EERKNS0_10regex_dataIT0_T1_EEb[_ZN5boost16re_detail_10710016re_is_set_memberIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEEcNS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEjEET_SH_SH_PKNS0_11re_set_longIT2_EERKNS0_10regex_dataIT0_T1_EEb]+0x447): referência não definida para "boost::re_detail_107100::cpp_regex_traits_implementation<char>::transform_primary[abi:cxx11](char const*, char const*) const"
/usr/bin/ld: wallet_rpc_server.cpp:(.text._ZN5boost16re_detail_10710016re_is_set_memberIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEEcNS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEjEET_SH_SH_PKNS0_11re_set_longIT2_EERKNS0_10regex_dataIT0_T1_EEb[_ZN5boost16re_detail_10710016re_is_set_memberIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEEcNS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEjEET_SH_SH_PKNS0_11re_set_longIT2_EERKNS0_10regex_dataIT0_T1_EEb]+0x544): referência não definida para "boost::re_detail_107100::cpp_regex_traits_implementation<char>::transform[abi:cxx11](char const*, char const*) const"
/usr/bin/ld: CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o: na função "boost::re_detail_107100::perl_matcher<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > >, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::extend_stack()":
wallet_rpc_server.cpp:(.text._ZN5boost16re_detail_10710012perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISC_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE12extend_stackEv[_ZN5boost16re_detail_10710012perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISC_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE12extend_stackEv]+0x1b): referência não definida para "boost::re_detail_107100::get_mem_block()"
/usr/bin/ld: CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o: na função "boost::re_detail_107100::perl_matcher<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > >, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::match_imp()":
wallet_rpc_server.cpp:(.text._ZN5boost16re_detail_10710012perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISC_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE9match_impEv[_ZN5boost16re_detail_10710012perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISC_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE9match_impEv]+0xc): referência não definida para "boost::re_detail_107100::get_mem_block()"
/usr/bin/ld: wallet_rpc_server.cpp:(.text._ZN5boost16re_detail_10710012perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISC_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE9match_impEv[_ZN5boost16re_detail_10710012perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISC_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE9match_impEv]+0xfa): referência não definida para "boost::re_detail_107100::verify_options(unsigned int, boost::regex_constants::_match_flags)"
/usr/bin/ld: wallet_rpc_server.cpp:(.text._ZN5boost16re_detail_10710012perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISC_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE9match_impEv[_ZN5boost16re_detail_10710012perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISC_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE9match_impEv]+0x115): referência não definida para "boost::re_detail_107100::put_mem_block(void*)"
/usr/bin/ld: wallet_rpc_server.cpp:(.text._ZN5boost16re_detail_10710012perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISC_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE9match_impEv[_ZN5boost16re_detail_10710012perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISC_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE9match_impEv]+0x1d8): referência não definida para "boost::re_detail_107100::put_mem_block(void*)"
/usr/bin/ld: CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o: na função "epee::serialization::convert_to_integral<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, unsigned long, false>::convert(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, unsigned long&)":
wallet_rpc_server.cpp:(.text._ZN4epee13serialization19convert_to_integralINSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEmLb0EE7convertERKS7_Rm[_ZN4epee13serialization19convert_to_integralINSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEmLb0EE7convertERKS7_Rm]+0x2d6): referência não definida para "boost::re_detail_107100::perl_matcher<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > >, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::construct_init(boost::basic_regex<char, boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, boost::regex_constants::_match_flags)"
/usr/bin/ld: CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o: na função "boost::re_detail_107100::perl_matcher<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > >, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::find_imp()":
wallet_rpc_server.cpp:(.text._ZN5boost16re_detail_10710012perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISC_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE8find_impEv[_ZN5boost16re_detail_10710012perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISC_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE8find_impEv]+0xf): referência não definida para "boost::re_detail_107100::get_mem_block()"
/usr/bin/ld: wallet_rpc_server.cpp:(.text._ZN5boost16re_detail_10710012perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISC_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE8find_impEv[_ZN5boost16re_detail_10710012perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISC_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE8find_impEv]+0x13c): referência não definida para "boost::re_detail_107100::verify_options(unsigned int, boost::regex_constants::_match_flags)"
/usr/bin/ld: wallet_rpc_server.cpp:(.text._ZN5boost16re_detail_10710012perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISC_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE8find_impEv[_ZN5boost16re_detail_10710012perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISC_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE8find_impEv]+0x184): referência não definida para "boost::re_detail_107100::put_mem_block(void*)"
/usr/bin/ld: wallet_rpc_server.cpp:(.text._ZN5boost16re_detail_10710012perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISC_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE8find_impEv[_ZN5boost16re_detail_10710012perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISC_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE8find_impEv]+0x2ab): referência não definida para "boost::re_detail_107100::put_mem_block(void*)"
/usr/bin/ld: CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o: na função "bool boost::regex_search<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > >, char, boost::regex_traits<char, boost::cpp_regex_traits<char> > >(__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, __gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, boost::match_results<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > > >&, boost::basic_regex<char, boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, boost::regex_constants::_match_flags, __gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >)":
wallet_rpc_server.cpp:(.text._ZN5boost12regex_searchIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISB_EEEcNS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEEEbT_SJ_RNS_13match_resultsISJ_T0_EERKNS_11basic_regexIT1_T2_EENS_15regex_constants12_match_flagsESJ_[_ZN5boost12regex_searchIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISB_EEEcNS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEEEbT_SJ_RNS_13match_resultsISJ_T0_EERKNS_11basic_regexIT1_T2_EENS_15regex_constants12_match_flagsESJ_]+0x136): referência não definida para "boost::re_detail_107100::perl_matcher<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > >, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::construct_init(boost::basic_regex<char, boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, boost::regex_constants::_match_flags)"
/usr/bin/ld: ../../lib/libwallet.a(wallet2.cpp.o): na função "tools::wallet2::load(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, epee::wipeable_string const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&) [clone .cold]":
wallet2.cpp:(.text.unlikely+0x1fedf): referência não definida para "boost::filesystem::detail::copy_file(boost::filesystem::path const&, boost::filesystem::path const&, boost::filesystem::detail::copy_option, boost::system::error_code*)"
/usr/bin/ld: wallet2.cpp:(.text.unlikely+0x20adc): referência não definida para "boost::filesystem::detail::copy_file(boost::filesystem::path const&, boost::filesystem::path const&, boost::filesystem::detail::copy_option, boost::system::error_code*)"
/usr/bin/ld: ../../lib/libwallet.a(wallet2.cpp.o): na função "boost::archive::detail::common_iarchive<boost::archive::binary_iarchive>::vload(boost::archive::class_name_type&)":
wallet2.cpp:(.text._ZN5boost7archive6detail15common_iarchiveINS0_15binary_iarchiveEE5vloadERNS0_15class_name_typeE[_ZN5boost7archive6detail15common_iarchiveINS0_15binary_iarchiveEE5vloadERNS0_15class_name_typeE]+0x5): referência não definida para "boost::archive::basic_binary_iarchive<boost::archive::binary_iarchive>::load_override(boost::archive::class_name_type&)"
/usr/bin/ld: ../../lib/libwallet.a(wallet2.cpp.o): na função "bool boost::regex_match<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > >, char, boost::regex_traits<char, boost::cpp_regex_traits<char> > >(__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, __gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, boost::match_results<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > > >&, boost::basic_regex<char, boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, boost::regex_constants::_match_flags)":
wallet2.cpp:(.text._ZN5boost11regex_matchIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISB_EEEcNS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEEEbT_SJ_RNS_13match_resultsISJ_T0_EERKNS_11basic_regexIT1_T2_EENS_15regex_constants12_match_flagsE[_ZN5boost11regex_matchIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISB_EEEcNS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEEEbT_SJ_RNS_13match_resultsISJ_T0_EERKNS_11basic_regexIT1_T2_EENS_15regex_constants12_match_flagsE]+0xfe): referência não definida para "boost::re_detail_107100::perl_matcher<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > >, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::construct_init(boost::basic_regex<char, boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, boost::regex_constants::_match_flags)"
/usr/bin/ld: ../device_trezor/libdevice_trezor.a(device_trezor_base.cpp.o): na função "hw::trezor::device_trezor_base::set_derivation_path(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&)":
device_trezor_base.cpp:(.text+0x383c): referência não definida para "boost::re_detail_107100::perl_matcher<char const*, std::allocator<boost::sub_match<char const*> >, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::construct_init(boost::basic_regex<char, boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, boost::regex_constants::_match_flags)"
/usr/bin/ld: ../device_trezor/libdevice_trezor.a(device_trezor_base.cpp.o): na função "boost::re_detail_107100::perl_matcher<char const*, std::allocator<boost::sub_match<char const*> >, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::unwind_extra_block(bool)":
device_trezor_base.cpp:(.text._ZN5boost16re_detail_10710012perl_matcherIPKcSaINS_9sub_matchIS3_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE18unwind_extra_blockEb[_ZN5boost16re_detail_10710012perl_matcherIPKcSaINS_9sub_matchIS3_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE18unwind_extra_blockEb]+0x30): referência não definida para "boost::re_detail_107100::put_mem_block(void*)"
/usr/bin/ld: ../device_trezor/libdevice_trezor.a(device_trezor_base.cpp.o): na função "char const* boost::re_detail_107100::re_is_set_member<char const*, char, boost::regex_traits<char, boost::cpp_regex_traits<char> >, unsigned int>(char const*, char const*, boost::re_detail_107100::re_set_long<unsigned int> const*, boost::re_detail_107100::regex_data<char, boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, bool)":
device_trezor_base.cpp:(.text._ZN5boost16re_detail_10710016re_is_set_memberIPKccNS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEjEET_S8_S8_PKNS0_11re_set_longIT2_EERKNS0_10regex_dataIT0_T1_EEb[_ZN5boost16re_detail_10710016re_is_set_memberIPKccNS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEjEET_S8_S8_PKNS0_11re_set_longIT2_EERKNS0_10regex_dataIT0_T1_EEb]+0x1c0): referência não definida para "boost::re_detail_107100::cpp_regex_traits_implementation<char>::transform_primary[abi:cxx11](char const*, char const*) const"
/usr/bin/ld: device_trezor_base.cpp:(.text._ZN5boost16re_detail_10710016re_is_set_memberIPKccNS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEjEET_S8_S8_PKNS0_11re_set_longIT2_EERKNS0_10regex_dataIT0_T1_EEb[_ZN5boost16re_detail_10710016re_is_set_memberIPKccNS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEjEET_S8_S8_PKNS0_11re_set_longIT2_EERKNS0_10regex_dataIT0_T1_EEb]+0x4b7): referência não definida para "boost::re_detail_107100::cpp_regex_traits_implementation<char>::transform[abi:cxx11](char const*, char const*) const"
/usr/bin/ld: ../device_trezor/libdevice_trezor.a(device_trezor_base.cpp.o): na função "boost::re_detail_107100::perl_matcher<char const*, std::allocator<boost::sub_match<char const*> >, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::extend_stack()":
device_trezor_base.cpp:(.text._ZN5boost16re_detail_10710012perl_matcherIPKcSaINS_9sub_matchIS3_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE12extend_stackEv[_ZN5boost16re_detail_10710012perl_matcherIPKcSaINS_9sub_matchIS3_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE12extend_stackEv]+0x1b): referência não definida para "boost::re_detail_107100::get_mem_block()"
/usr/bin/ld: ../device_trezor/libdevice_trezor.a(device_trezor_base.cpp.o): na função "boost::re_detail_107100::perl_matcher<char const*, std::allocator<boost::sub_match<char const*> >, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::match_imp()":
device_trezor_base.cpp:(.text._ZN5boost16re_detail_10710012perl_matcherIPKcSaINS_9sub_matchIS3_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE9match_impEv[_ZN5boost16re_detail_10710012perl_matcherIPKcSaINS_9sub_matchIS3_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE9match_impEv]+0x2d): referência não definida para "boost::re_detail_107100::get_mem_block()"
/usr/bin/ld: device_trezor_base.cpp:(.text._ZN5boost16re_detail_10710012perl_matcherIPKcSaINS_9sub_matchIS3_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE9match_impEv[_ZN5boost16re_detail_10710012perl_matcherIPKcSaINS_9sub_matchIS3_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE9match_impEv]+0x4e2): referência não definida para "boost::re_detail_107100::verify_options(unsigned int, boost::regex_constants::_match_flags)"
/usr/bin/ld: device_trezor_base.cpp:(.text._ZN5boost16re_detail_10710012perl_matcherIPKcSaINS_9sub_matchIS3_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE9match_impEv[_ZN5boost16re_detail_10710012perl_matcherIPKcSaINS_9sub_matchIS3_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE9match_impEv]+0x5ba): referência não definida para "boost::re_detail_107100::put_mem_block(void*)"
/usr/bin/ld: device_trezor_base.cpp:(.text._ZN5boost16re_detail_10710012perl_matcherIPKcSaINS_9sub_matchIS3_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE9match_impEv[_ZN5boost16re_detail_10710012perl_matcherIPKcSaINS_9sub_matchIS3_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE9match_impEv]+0xb32): referência não definida para "boost::re_detail_107100::put_mem_block(void*)"
/usr/bin/ld: ../blockchain_db/libblockchain_db.a(db_lmdb.cpp.o): na função "cryptonote::BlockchainLMDB::close()":
db_lmdb.cpp:(.text+0xa6c9): referência não definida para "boost::detail::set_tss_data(void const*, void (*)(void (*)(void*), void*), void (*)(void*), void*, bool)"
/usr/bin/ld: ../blockchain_db/libblockchain_db.a(db_lmdb.cpp.o): na função "cryptonote::BlockchainLMDB::~BlockchainLMDB()":
db_lmdb.cpp:(.text+0xaac6): referência não definida para "boost::detail::set_tss_data(void const*, void (*)(void (*)(void*), void*), void (*)(void*), void*, bool)"
/usr/bin/ld: ../blockchain_db/libblockchain_db.a(db_lmdb.cpp.o): na função "cryptonote::BlockchainLMDB::block_rtxn_start(MDB_txn**, cryptonote::mdb_txn_cursors**) const":
db_lmdb.cpp:(.text+0xe61b): referência não definida para "boost::detail::set_tss_data(void const*, void (*)(void (*)(void*), void*), void (*)(void*), void*, bool)"
/usr/bin/ld: ../blockchain_db/libblockchain_db.a(db_lmdb.cpp.o): na função "cryptonote::BlockchainLMDB::BlockchainLMDB(bool) [clone .cold]":
db_lmdb.cpp:(.text.unlikely+0x7de0): referência não definida para "boost::detail::set_tss_data(void const*, void (*)(void (*)(void*), void*), void (*)(void*), void*, bool)"
collect2: error: ld returned 1 exit status
make[3]: *** [src/wallet/CMakeFiles/wallet_rpc_server.dir/build.make:142: bin/monero-wallet-rpc] Erro 1
make[3]: a sair da pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
make[2]: *** [CMakeFiles/Makefile2:3484: src/wallet/CMakeFiles/wallet_rpc_server.dir/all] Erro 2
make[2]: a sair da pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
make[1]: *** [Makefile:141: all] Erro 2
make[1]: a sair da pasta "/home/filipe/Transferências/cryptonote/Monero/monero/build/Linux/release-v0.18/release"
make: *** [Makefile:103: release-all] Erro 2
`

## selsta | 2022-07-21T13:36:00+00:00
What make command did you enter?

## dedetuga | 2022-07-21T17:44:45+00:00
I enter the cmd make

## selsta | 2022-07-21T17:47:29+00:00
just `make` or `make release-static`?

## dedetuga | 2022-07-21T18:46:24+00:00
I tryed make and make release

## selsta | 2022-07-22T10:58:43+00:00
Did you ever successfully build monero in the past?

## dedetuga | 2022-07-23T08:14:15+00:00
I builded from source/Install:

- gcc-10
- Boost
- Opessl

After all I runned: `sudo ldconfig /usr/local/lib64/`



# Action History
- Created by: dedetuga | 2022-07-20T22:27:17+00:00
- Closed at: 2022-07-23T08:14:15+00:00
