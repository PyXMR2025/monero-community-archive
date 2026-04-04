---
title: build NOTFOUND Z alpine, what's missing?
source_url: https://github.com/monero-project/monero/issues/9331
author: lavdnone2
assignees: []
labels: []
created_at: '2024-05-15T15:36:16+00:00'
updated_at: '2024-05-16T12:55:09+00:00'
type: issue
status: closed
closed_at: '2024-05-16T12:55:09+00:00'
---

# Original Description
alpine 3.16

mkdir build && cd build &&     CFLAGS="-march=native -mtune=native -Ofast" CXXFLAGS="-march=native -mtune=native -Ofast"     cmake .. -D BUILD_DOCUMENTATION=OFF -D BUILD_DEBUG_UTILITIES=OFF -D BUILD_TESTS=OFF -D BUILD_GUI_DEPS=OFF -D STACK_TRACE=OFF     -D USE_DEVICE_TREZOR=OFF -D STATIC=ON -D ARCH="native" -D CMAKE_BUILD_TYPE=release
 ---> Running in 9332612c2ede
-- CMake version 3.23.5
-- Found PythonInterp: /usr/bin/python3.10 (found version "3.10.14")
-- The C compiler identification is GNU 11.2.1
-- The CXX compiler identification is GNU 11.2.1
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
-- ccache NOT found! Please install it for faster rebuilds.
-- The ASM compiler identification is GNU
-- Found assembler: /usr/bin/cc
-- Looking for -Wl,--no-undefined linker flag
-- Looking for -Wl,--no-undefined linker flag - found
-- Looking for -Wl,-undefined,error linker flag
-- Looking for -Wl,-undefined,error linker flag - found
-- Building without build tag
-- Found Git: /usr/bin/git (found version "2.36.6")
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
-- Stack trace on exception disabled
-- Looking for pthread.h
-- Looking for pthread.h - found
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD - Success
-- Found Threads: TRUE
-- Performing Test _Werror__pthread_c
-- Performing Test _Werror__pthread_c - Success
-- Performing Test _Werror__pthread_cxx
-- Performing Test _Werror__pthread_cxx - Success
-- Found OpenSSL: /usr/local/openssl-1.1.1l/libcrypto.a (found version "1.1.1l")
-- Using OpenSSL include dir at /usr/local/openssl-1.1.1l/include
-- Could NOT find HIDAPI (missing: HIDAPI_LIBRARY HIDAPI_INCLUDE_DIR)
-- Looking for memset_s in c
-- Looking for memset_s in c - not found
-- Looking for explicit_bzero in c
-- Looking for explicit_bzero in c - found
-- Looking for strptime
-- Looking for strptime - found
CMake Warning (dev) at /usr/share/cmake/Modules/FindPackageHandleStandardArgs.cmake:438 (message):
  The package name passed to `find_package_handle_standard_args` (MiniUPnPc)
  does not match the name of the calling package (Miniupnpc).  This can lead
  to problems in calling code that expects `find_package` result variables
  (e.g., `_FOUND`) to follow a certain pattern.
Call Stack (most recent call first):
  cmake/FindMiniupnpc.cmake:39 (find_package_handle_standard_args)
  external/CMakeLists.txt:38 (find_package)
This warning is for project developers.  Use -Wno-dev to suppress it.

-- Could NOT find MiniUPnPc (missing: MINIUPNP_INCLUDE_DIR MINIUPNP_LIBRARY)
-- Using in-tree miniupnpc
-- Looking for libunbound
-- Found libunbound include (unbound.h) in /usr/include
-- Found libunbound library
-- Using 64-bit LMDB from source tree
-- Looking for backtrace
-- Looking for backtrace - not found
-- Backtrace_LIBRARY: /usr/lib/libexecinfo.so
-- Found Backtrace: /usr/lib/libexecinfo.so
-- Performing Test _march=native_cxx
-- Performing Test _march=native_cxx - Success
-- Setting CXX flag -march=native
-- Performing Test _march=native_c
-- Performing Test _march=native_c - Success
-- Setting C flag -march=native
-- Performing Test HAVE_CXX_ATOMICS
-- Performing Test HAVE_CXX_ATOMICS - Success
-- Could not find HIDAPI
-- Trezor: support disabled by USE_DEVICE_TREZOR
-- Building on x86_64 for native
-- Performing Test CC_SUPPORTS_MARCH_NATIVE
-- Performing Test CC_SUPPORTS_MARCH_NATIVE - Success
-- AES support enabled
-- Performing Test _Werror__Wformat_c
-- Performing Test _Werror__Wformat_c - Success
-- Performing Test _Werror__Wformat_cxx
-- Performing Test _Werror__Wformat_cxx - Success
-- Performing Test _Werror__Wformat_security_c
-- Performing Test _Werror__Wformat_security_c - Success
-- Performing Test _Werror__Wformat_security_cxx
-- Performing Test _Werror__Wformat_security_cxx - Success
-- Performing Test _Werror__fstack_protector_c
-- Performing Test _Werror__fstack_protector_c - Success
-- Performing Test _Werror__fstack_protector_cxx
-- Performing Test _Werror__fstack_protector_cxx - Success
-- Performing Test _Werror__fstack_protector_strong_c
-- Performing Test _Werror__fstack_protector_strong_c - Success
-- Performing Test _Werror__fstack_protector_strong_cxx
-- Performing Test _Werror__fstack_protector_strong_cxx - Success
-- Performing Test _Werror__fcf_protection=full_c
-- Performing Test _Werror__fcf_protection=full_c - Success
-- Performing Test _Werror__fcf_protection=full_cxx
-- Performing Test _Werror__fcf_protection=full_cxx - Success
-- Performing Test _Werror__fstack_clash_protection_c
-- Performing Test _Werror__fstack_clash_protection_c - Success
-- Performing Test _Werror__fstack_clash_protection_cxx
-- Performing Test _Werror__fstack_clash_protection_cxx - Success
-- Looking for -pie linker flag
-- Looking for -pie linker flag - found
-- Looking for -Wl,-z,relro linker flag
-- Looking for -Wl,-z,relro linker flag - found
-- Looking for -Wl,-z,now linker flag
-- Looking for -Wl,-z,now linker flag - found
-- Looking for -Wl,-z,noexecstack linker flag
-- Looking for -Wl,-z,noexecstack linker flag - found
-- Looking for -Wl,-z,noexecheap linker flag
-- Looking for -Wl,-z,noexecheap linker flag - not found
-- Performing Test _Werror__Werror=switch_c
-- Performing Test _Werror__Werror=switch_c - Success
-- Performing Test _Werror__Werror=switch_cxx
-- Performing Test _Werror__Werror=switch_cxx - Success
-- Performing Test _Werror__Werror=return_type_c
-- Performing Test _Werror__Werror=return_type_c - Success
-- Performing Test _Werror__Werror=return_type_cxx
-- Performing Test _Werror__Werror=return_type_cxx - Success
-- Using C security hardening flags:  -Wformat -Wformat-security -fstack-protector -fstack-protector-strong -fcf-protection=full -fstack-clash-protection -Werror=switch -Werror=return-type
-- Using C++ security hardening flags:  -Wformat -Wformat-security -fstack-protector -fstack-protector-strong -fcf-protection=full -fstack-clash-protection -Werror=switch -Werror=return-type
-- Using linker security hardening flags:  -pie -Wl,-z,relro -Wl,-z,now -Wl,-z,noexecstack
-- Found Boost Version: 107700
-- Looking for rl_copy_text
-- Looking for rl_copy_text - not found
-- Looking for rl_filename_completion_function
-- Looking for rl_filename_completion_function - not found
-- Looking for rl_copy_text
-- Looking for rl_copy_text - not found
-- Looking for rl_filename_completion_function
-- Looking for rl_filename_completion_function - not found
-- Could not find GNU readline library so building without readline support
-- Found Sodium: /usr/local/lib/libsodium.a
-- Found Git: /usr/bin/git
-- You are currently on commit c8214782f
-- You are ahead of or behind a tagged release
-- Looking for a ASM-ATT compiler
-- Looking for a ASM-ATT compiler - /usr/bin/as
Wallet crypto is using amd64-64-24k backend
-- Trezor: support disabled
-- Not building tests
-- Not building debug utilities
-- Configuring done
CMake Error: The following variables are used in this project, but they are set to NOTFOUND.
Please set them or make sure they are set and tested correctly in the CMake files:
Z
    linked by target "epee" in directory /src/contrib/epee/src
    linked by target "common" in directory /src/src/common
    linked by target "cncrypto" in directory /src/src/crypto
    linked by target "ringct" in directory /src/src/ringct
    linked by target "ringct_basic" in directory /src/src/ringct
    linked by target "checkpoints" in directory /src/src/checkpoints
    linked by target "cryptonote_basic" in directory /src/src/cryptonote_basic
    linked by target "cryptonote_core" in directory /src/src/cryptonote_core
    linked by target "multisig" in directory /src/src/multisig
    linked by target "hardforks" in directory /src/src/hardforks
    linked by target "blockchain_db" in directory /src/src/blockchain_db
    linked by target "mnemonics" in directory /src/src/mnemonics
    linked by target "rpc_base" in directory /src/src/rpc
    linked by target "rpc" in directory /src/src/rpc
    linked by target "daemon_messages" in directory /src/src/rpc
    linked by target "daemon_rpc_server" in directory /src/src/rpc
    linked by target "seraphis_crypto" in directory /src/src/seraphis_crypto
    linked by target "serialization" in directory /src/src/serialization
    linked by target "wallet_rpc_server" in directory /src/src/wallet
    linked by target "wallet_rpc_server" in directory /src/src/wallet
    linked by target "wallet" in directory /src/src/wallet
    linked by target "wallet_api" in directory /src/src/wallet/api
    linked by target "p2p" in directory /src/src/p2p
    linked by target "cryptonote_protocol" in directory /src/src/cryptonote_protocol
    linked by target "simplewallet" in directory /src/src/simplewallet
    linked by target "simplewallet" in directory /src/src/simplewallet
    linked by target "gen_multisig" in directory /src/src/gen_multisig
    linked by target "gen_multisig" in directory /src/src/gen_multisig
    linked by target "gen_ssl_cert" in directory /src/src/gen_ssl_cert
    linked by target "gen_ssl_cert" in directory /src/src/gen_ssl_cert
    linked by target "daemonizer" in directory /src/src/daemonizer
    linked by target "daemon" in directory /src/src/daemon
    linked by target "daemon" in directory /src/src/daemon
    linked by target "blockchain_export" in directory /src/src/blockchain_utilities
    linked by target "blockchain_export" in directory /src/src/blockchain_utilities
    linked by target "blockchain_prune" in directory /src/src/blockchain_utilities
    linked by target "blockchain_prune" in directory /src/src/blockchain_utilities
    linked by target "blockchain_stats" in directory /src/src/blockchain_utilities
    linked by target "blockchain_stats" in directory /src/src/blockchain_utilities
    linked by target "blockchain_blackball" in directory /src/src/blockchain_utilities
    linked by target "blockchain_blackball" in directory /src/src/blockchain_utilities
    linked by target "blockchain_ancestry" in directory /src/src/blockchain_utilities
    linked by target "blockchain_ancestry" in directory /src/src/blockchain_utilities
    linked by target "blockchain_prune_known_spent_data" in directory /src/src/blockchain_utilities
    linked by target "blockchain_prune_known_spent_data" in directory /src/src/blockchain_utilities
    linked by target "blockchain_depth" in directory /src/src/blockchain_utilities
    linked by target "blockchain_depth" in directory /src/src/blockchain_utilities
    linked by target "blockchain_import" in directory /src/src/blockchain_utilities
    linked by target "blockchain_import" in directory /src/src/blockchain_utilities
    linked by target "blockchain_usage" in directory /src/src/blockchain_utilities
    linked by target "blockchain_usage" in directory /src/src/blockchain_utilities
    linked by target "device" in directory /src/src/device

# Discussion History
## lavdnone2 | 2024-05-16T12:55:09+00:00
guess somewhere on the way from 18.1 to 18.3 it picked up zlib-dev

# Action History
- Created by: lavdnone2 | 2024-05-15T15:36:16+00:00
- Closed at: 2024-05-16T12:55:09+00:00
