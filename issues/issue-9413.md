---
title: Error compiling on nixos
source_url: https://github.com/monero-project/monero/issues/9413
author: Redhawk18
assignees: []
labels:
- more info needed
created_at: '2024-07-31T03:16:25+00:00'
updated_at: '2024-09-15T21:39:45+00:00'
type: issue
status: closed
closed_at: '2024-09-15T21:39:45+00:00'
---

# Original Description
```bash
-- Using linker security hardening flags:  -pie -Wl,-z,relro -Wl,-z,now -Wl,-z,noexecstack
CMake Error at /usr/share/cmake-3.29/Modules/FindPackageHandleStandardArgs.cmake:230 (message):
  Could NOT find Boost (missing: system filesystem thread date_time chrono
  regex serialization program_options) (found suitable version "1.81.0",
  minimum required is "1.58")
Call Stack (most recent call first):
  /usr/share/cmake-3.29/Modules/FindPackageHandleStandardArgs.cmake:600 (_FPHSA_FAILURE_MESSAGE)
  /usr/share/cmake-3.29/Modules/FindBoost.cmake:2393 (find_package_handle_standard_args)
  CMakeLists.txt:1091 (find_package)


-- Configuring incomplete, errors occurred!
make: *** [Makefile:103: release-all] Error 1
📦[redhawk@ubuntu monero]$ sudo apt install libboost-chrono-dev libboost-date-time-dev libboost-filesystem-dev libboost-locale-dev libboost-program-options-dev libboost-regex-dev libboost-serialization-dev libboost-system-dev libboost-thread-dev
libboost-chrono-dev is already the newest version (1.83.0.2ubuntu1).
libboost-date-time-dev is already the newest version (1.83.0.2ubuntu1).
libboost-filesystem-dev is already the newest version (1.83.0.2ubuntu1).
libboost-locale-dev is already the newest version (1.83.0.2ubuntu1).
libboost-program-options-dev is already the newest version (1.83.0.2ubuntu1).
libboost-regex-dev is already the newest version (1.83.0.2ubuntu1).
libboost-serialization-dev is already the newest version (1.83.0.2ubuntu1).
libboost-system-dev is already the newest version (1.83.0.2ubuntu1).
libboost-thread-dev is already the newest version (1.83.0.2ubuntu1).
Summary:
  Upgrading: 0, Installing: 0, Removing: 0, Not Upgrading: 16
```

I seem to have all the correct packages outlined in the docs, I just don't know why it's not working now.

# Discussion History
## selsta | 2024-07-31T16:20:08+00:00
Can you share more information? Which OS are you using? ARM / x86? Exact steps you use to build?

## Redhawk18 | 2024-07-31T16:23:57+00:00
> Can you share more information? Which OS are you using? ARM / x86? Exact steps you use to build?

I'm on nixos but I opened a distrobox ubuntu container to try to compile everything and I followed the build instructions on the readme

## selsta | 2024-07-31T16:27:30+00:00
Which Ubuntu version is used? Is this indistinguishable from a regular Ubuntu install?

## 0xFFFC0000 | 2024-07-31T16:28:20+00:00
Might be related, check this out too:

https://github.com/monero-project/monero/issues/9140#issuecomment-1925430930

## Redhawk18 | 2024-07-31T16:29:54+00:00
I'll try on nixos again and if I can get it working I'll pr my flake for so no other nixos user will have problems compiling.

## Redhawk18 | 2024-07-31T17:48:32+00:00
> Can you share more information? Which OS are you using? ARM / x86? Exact steps you use to build?

I tried building on nixos again and got this new error this time
```bash
monero on  master [!+?] via △ v3.29.6 via ❄  impure (devenv-shell-env) 
❯ make
mkdir -p build/"Linux/master"/release
cd build/"Linux/master"/release && cmake -D BUILD_TESTS=ON -D CMAKE_BUILD_TYPE=Release ../../../.. && make
-- CMake version 3.29.6
-- Found PythonInterp: /nix/store/l014xp1qxdl6gim3zc0jv3mpxhbp346s-python3-3.12.4/bin/python (found version "3.12.4")
-- The C compiler identification is GNU 13.3.0
-- The CXX compiler identification is GNU 13.3.0
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /nix/store/62zpnw69ylcfhcpy1di8152zlzmbls91-gcc-wrapper-13.3.0/bin/gcc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: /nix/store/62zpnw69ylcfhcpy1di8152zlzmbls91-gcc-wrapper-13.3.0/bin/g++ - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Found usable ccache: /nix/store/wk0wqsmqbz9m4i6y1pad0sv63cmb5bc5-ccache-4.10.2/bin/ccache
-- The ASM compiler identification is GNU
-- Found assembler: /nix/store/62zpnw69ylcfhcpy1di8152zlzmbls91-gcc-wrapper-13.3.0/bin/gcc
-- Looking for -Wl,--no-undefined linker flag
-- Looking for -Wl,--no-undefined linker flag - found
-- Looking for -Wl,-undefined,error linker flag
-- Looking for -Wl,-undefined,error linker flag - found
-- Building without build tag
-- Found Git: /home/redhawk/.nix-profile/bin/git (found version "2.45.2")
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
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD - Success
-- Found Threads: TRUE
-- Performing Test _Werror__pthread_c
-- Performing Test _Werror__pthread_c - Success
-- Performing Test _Werror__pthread_cxx
-- Performing Test _Werror__pthread_cxx - Success
-- Found OpenSSL: /nix/store/1zd8iqbcl36rliw0bbf9wn4ca31rqz5c-openssl-3.0.14/lib/libcrypto.so (found version "3.0.14")
-- Using OpenSSL include dir at /nix/store/bvrly5zpaqxydbfnx3dm4i7k8cbkrp32-openssl-3.0.14-dev/include
-- Found HIDAPI: /nix/store/2f6smhfnpbm1zc64pa179q0wdjjfxpn6-hidapi-0.14.0/lib/libhidapi-libusb.so
-- Looking for memset_s in c
-- Looking for memset_s in c - not found
-- Looking for explicit_bzero in c
-- Looking for explicit_bzero in c - found
-- Looking for strptime
-- Looking for strptime - found
CMake Warning (dev) at /nix/store/aqckch626lg0vxh41dabyzrq0jx7gdk5-cmake-3.29.6/share/cmake-3.29/Modules/FindPackageHandleStandardArgs.cmake:438 (message):
  The package name passed to `find_package_handle_standard_args` (MiniUPnPc)
  does not match the name of the calling package (Miniupnpc).  This can lead
  to problems in calling code that expects `find_package` result variables
  (e.g., `_FOUND`) to follow a certain pattern.
Call Stack (most recent call first):
  cmake/FindMiniupnpc.cmake:39 (find_package_handle_standard_args)
  external/CMakeLists.txt:38 (find_package)
This warning is for project developers.  Use -Wno-dev to suppress it.

-- Found MiniUPnPc: /nix/store/5d1225n0bvlxi6mzhf5hmm8llw2jsnkc-miniupnpc-2.2.8/include/miniupnpc
-- Found miniupnpc API version 18
-- Using in-tree miniupnpc
-- Looking for libunbound
-- Found libunbound include (unbound.h) in /nix/store/hmimvpif140zx0xssbhgwk5i3nkx6yn9-unbound-1.20.0/include
-- Found libunbound library
-- Using 64-bit LMDB from source tree
-- Looking for backtrace
-- Looking for backtrace - found
-- backtrace facility detected in default set of libraries
-- Backtrace_LIBRARY: 
-- Found Backtrace: /nix/store/1vp54ln0frvhzgasr2a377mfbwvqdm6i-glibc-2.39-52-dev/include
-- Performing Test _march=native_cxx
-- Performing Test _march=native_cxx - Success
-- Setting CXX flag -march=native
-- Performing Test _march=native_c
-- Performing Test _march=native_c - Success
-- Setting C flag -march=native
-- Performing Test HAVE_CXX_ATOMICS
-- Performing Test HAVE_CXX_ATOMICS - Success
-- Using HIDAPI include dir at /nix/store/2f6smhfnpbm1zc64pa179q0wdjjfxpn6-hidapi-0.14.0/include/hidapi
-- Found Protobuf: /nix/store/zlrliq0akg5wn38rffmdkwrpbnhyllqj-protobuf-25.3/lib/libprotobuf.so (found version "4.25.3")
-- Checking for module 'protobuf'
--   Found protobuf, version 25.3.0
-- Trezor: Protobuf lib: /nix/store/zlrliq0akg5wn38rffmdkwrpbnhyllqj-protobuf-25.3/lib/libprotobuf.so, inc: /nix/store/zlrliq0akg5wn38rffmdkwrpbnhyllqj-protobuf-25.3/include, protoc: /nix/store/zlrliq0akg5wn38rffmdkwrpbnhyllqj-protobuf-25.3/bin/protoc
-- Trezor: protobuf messages regenerated out: "."
-- Found PkgConfig: /nix/store/65lhpq7pbc6nnngfp030ddglb71xixg9-pkg-config-wrapper-0.29.2/bin/pkg-config (found version "0.29.2")
-- Checking for module 'libusb-1.0'
--   Found libusb-1.0, version 1.0.27
-- Looking for libusb_get_device_list in /nix/store/gkhma9q8dm7vgjzqhjg1p34pflmpz6jz-libusb-1.0.27/lib/libusb-1.0.so
-- Looking for libusb_get_device_list in /nix/store/gkhma9q8dm7vgjzqhjg1p34pflmpz6jz-libusb-1.0.27/lib/libusb-1.0.so - found
-- Looking for libusb_get_port_numbers in /nix/store/gkhma9q8dm7vgjzqhjg1p34pflmpz6jz-libusb-1.0.27/lib/libusb-1.0.so
-- Looking for libusb_get_port_numbers in /nix/store/gkhma9q8dm7vgjzqhjg1p34pflmpz6jz-libusb-1.0.27/lib/libusb-1.0.so - found
-- LibUSB Compilation test: TRUE
-- Trezor: compatible LibUSB found at: /nix/store/a12ffvgqpl4j9q8mnfj9sdj37vjpva7p-libusb-1.0.27-dev/include/libusb-1.0
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
-- Using C security hardening flags:  -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -fstack-protector -fstack-protector-strong -fcf-protection=full -fstack-clash-protection -Werror=switch -Werror=return-type
-- Using C++ security hardening flags:  -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -fstack-protector -fstack-protector-strong -fcf-protection=full -fstack-clash-protection -Werror=switch -Werror=return-type
-- Using linker security hardening flags:  -pie -Wl,-z,relro -Wl,-z,now -Wl,-z,noexecstack
-- Found Boost Version: 108100
-- Could NOT find Readline (missing: Readline_INCLUDE_DIR) 
-- Looking for rl_copy_text
-- Looking for rl_copy_text - found
-- Looking for rl_filename_completion_function
-- Looking for rl_filename_completion_function - found
-- Could not find GNU readline library so building without readline support
-- Found Sodium: /nix/store/qjsms7x27xqykdgsvlnrs47d23zd39s9-libsodium-1.0.20/lib/libsodium.so
-- Found Git: /home/redhawk/.nix-profile/bin/git
-- You are currently on commit caa62bc9e
-- You are ahead of or behind a tagged release
-- Looking for a ASM-ATT compiler
-- Looking for a ASM-ATT compiler - /nix/store/v39mysip3yjpvddmsyj6pfvdhwgmak4m-clang-wrapper-18.1.8/bin/as
Wallet crypto is using amd64-64-24k backend
-- Trezor: support enabled
-- Building tests
-- Found GTest: /nix/store/1gjj14lgvqxjnclrk1aj98sc437s2bsc-gtest-1.14.0-dev/lib/cmake/GTest/GTestConfig.cmake (found version "1.14.0")
-- Copying test data directory...
Wallet crypto bench is using cn;amd64-64-24k;amd64-51-30k
-- Not building debug utilities
-- Found Doxygen: /nix/store/nvlg97w10pf3vz4ad12l92x8zb5rchnh-doxygen-1.10.0/bin/doxygen (found version "1.10.0") found components: doxygen dot
-- Configuring done (10.1s)
CMake Error: The following variables are used in this project, but they are set to NOTFOUND.
Please set them or make sure they are set and tested correctly in the CMake files:
Z
    linked by target "epee" in directory /home/redhawk/code/monero/contrib/epee/src
    linked by target "common" in directory /home/redhawk/code/monero/src/common
    linked by target "cncrypto" in directory /home/redhawk/code/monero/src/crypto
    linked by target "ringct" in directory /home/redhawk/code/monero/src/ringct
    linked by target "ringct_basic" in directory /home/redhawk/code/monero/src/ringct
    linked by target "checkpoints" in directory /home/redhawk/code/monero/src/checkpoints
    linked by target "cryptonote_basic" in directory /home/redhawk/code/monero/src/cryptonote_basic
    linked by target "cryptonote_core" in directory /home/redhawk/code/monero/src/cryptonote_core
    linked by target "multisig" in directory /home/redhawk/code/monero/src/multisig
    linked by target "hardforks" in directory /home/redhawk/code/monero/src/hardforks
    linked by target "blockchain_db" in directory /home/redhawk/code/monero/src/blockchain_db
    linked by target "mnemonics" in directory /home/redhawk/code/monero/src/mnemonics
    linked by target "rpc_base" in directory /home/redhawk/code/monero/src/rpc
    linked by target "rpc" in directory /home/redhawk/code/monero/src/rpc
    linked by target "daemon_messages" in directory /home/redhawk/code/monero/src/rpc
    linked by target "daemon_rpc_server" in directory /home/redhawk/code/monero/src/rpc
    linked by target "seraphis_crypto" in directory /home/redhawk/code/monero/src/seraphis_crypto
    linked by target "serialization" in directory /home/redhawk/code/monero/src/serialization
    linked by target "wallet_rpc_server" in directory /home/redhawk/code/monero/src/wallet
    linked by target "wallet_rpc_server" in directory /home/redhawk/code/monero/src/wallet
    linked by target "wallet" in directory /home/redhawk/code/monero/src/wallet
    linked by target "wallet_api" in directory /home/redhawk/code/monero/src/wallet/api
    linked by target "p2p" in directory /home/redhawk/code/monero/src/p2p
    linked by target "cryptonote_protocol" in directory /home/redhawk/code/monero/src/cryptonote_protocol
    linked by target "simplewallet" in directory /home/redhawk/code/monero/src/simplewallet
    linked by target "simplewallet" in directory /home/redhawk/code/monero/src/simplewallet
    linked by target "gen_multisig" in directory /home/redhawk/code/monero/src/gen_multisig
    linked by target "gen_multisig" in directory /home/redhawk/code/monero/src/gen_multisig
    linked by target "gen_ssl_cert" in directory /home/redhawk/code/monero/src/gen_ssl_cert
    linked by target "gen_ssl_cert" in directory /home/redhawk/code/monero/src/gen_ssl_cert
    linked by target "daemonizer" in directory /home/redhawk/code/monero/src/daemonizer
    linked by target "daemon" in directory /home/redhawk/code/monero/src/daemon
    linked by target "daemon" in directory /home/redhawk/code/monero/src/daemon
    linked by target "blockchain_export" in directory /home/redhawk/code/monero/src/blockchain_utilities
    linked by target "blockchain_export" in directory /home/redhawk/code/monero/src/blockchain_utilities
    linked by target "blockchain_prune" in directory /home/redhawk/code/monero/src/blockchain_utilities
    linked by target "blockchain_prune" in directory /home/redhawk/code/monero/src/blockchain_utilities
    linked by target "blockchain_stats" in directory /home/redhawk/code/monero/src/blockchain_utilities
    linked by target "blockchain_stats" in directory /home/redhawk/code/monero/src/blockchain_utilities
    linked by target "blockchain_blackball" in directory /home/redhawk/code/monero/src/blockchain_utilities
    linked by target "blockchain_blackball" in directory /home/redhawk/code/monero/src/blockchain_utilities
    linked by target "blockchain_ancestry" in directory /home/redhawk/code/monero/src/blockchain_utilities
    linked by target "blockchain_ancestry" in directory /home/redhawk/code/monero/src/blockchain_utilities
    linked by target "blockchain_prune_known_spent_data" in directory /home/redhawk/code/monero/src/blockchain_utilities
    linked by target "blockchain_prune_known_spent_data" in directory /home/redhawk/code/monero/src/blockchain_utilities
    linked by target "blockchain_depth" in directory /home/redhawk/code/monero/src/blockchain_utilities
    linked by target "blockchain_depth" in directory /home/redhawk/code/monero/src/blockchain_utilities
    linked by target "blockchain_import" in directory /home/redhawk/code/monero/src/blockchain_utilities
    linked by target "blockchain_import" in directory /home/redhawk/code/monero/src/blockchain_utilities
    linked by target "blockchain_usage" in directory /home/redhawk/code/monero/src/blockchain_utilities
    linked by target "blockchain_usage" in directory /home/redhawk/code/monero/src/blockchain_utilities
    linked by target "device" in directory /home/redhawk/code/monero/src/device
    linked by target "device_trezor" in directory /home/redhawk/code/monero/src/device_trezor
    linked by target "core_tests" in directory /home/redhawk/code/monero/tests/core_tests
    linked by target "utf8_fuzz_tests" in directory /home/redhawk/code/monero/tests/fuzz
    linked by target "block_fuzz_tests" in directory /home/redhawk/code/monero/tests/fuzz
    linked by target "load-from-json_fuzz_tests" in directory /home/redhawk/code/monero/tests/fuzz
    linked by target "signature_fuzz_tests" in directory /home/redhawk/code/monero/tests/fuzz
    linked by target "cold-outputs_fuzz_tests" in directory /home/redhawk/code/monero/tests/fuzz
    linked by target "cold-transaction_fuzz_tests" in directory /home/redhawk/code/monero/tests/fuzz
    linked by target "load-from-binary_fuzz_tests" in directory /home/redhawk/code/monero/tests/fuzz
    linked by target "base58_fuzz_tests" in directory /home/redhawk/code/monero/tests/fuzz
    linked by target "parse-url_fuzz_tests" in directory /home/redhawk/code/monero/tests/fuzz
    linked by target "tx-extra_fuzz_tests" in directory /home/redhawk/code/monero/tests/fuzz
    linked by target "http-client_fuzz_tests" in directory /home/redhawk/code/monero/tests/fuzz
    linked by target "transaction_fuzz_tests" in directory /home/redhawk/code/monero/tests/fuzz
    linked by target "levin_fuzz_tests" in directory /home/redhawk/code/monero/tests/fuzz
    linked by target "bulletproof_fuzz_tests" in directory /home/redhawk/code/monero/tests/fuzz
    linked by target "cnv4-jit-tests" in directory /home/redhawk/code/monero/tests/crypto
    linked by target "cncrypto-tests" in directory /home/redhawk/code/monero/tests/crypto
    linked by target "make_test_signature" in directory /home/redhawk/code/monero/tests/functional_tests
    linked by target "functional_tests" in directory /home/redhawk/code/monero/tests/functional_tests
    linked by target "performance_tests" in directory /home/redhawk/code/monero/tests/performance_tests
    linked by target "test_notifier" in directory /home/redhawk/code/monero/tests/unit_tests
    linked by target "unit_tests" in directory /home/redhawk/code/monero/tests/unit_tests
    linked by target "difficulty-tests" in directory /home/redhawk/code/monero/tests/difficulty
    linked by target "block_weight" in directory /home/redhawk/code/monero/tests/block_weight
    linked by target "hash-tests" in directory /home/redhawk/code/monero/tests/hash
    linked by target "net_load_tests_srv" in directory /home/redhawk/code/monero/tests/net_load_tests
    linked by target "net_load_tests_clt" in directory /home/redhawk/code/monero/tests/net_load_tests

-- Generating done (0.3s)
CMake Generate step failed.  Build files cannot be regenerated correctly.
make: *** [Makefile:103: release-all] Error 1

```

## Redhawk18 | 2024-07-31T17:57:31+00:00
A weird thing is I added gnu's readline library because cmake complained and it still doesn't find it.

## 0xFFFC0000 | 2024-09-15T16:54:37+00:00
This says it needs zlib library when building master [1]. 


I have PR to fix this. But for now you can add zlib in your Nix package description. ( I did roughly the same with GUIX ). 


Another issue you mentioned is gnu readline library, is because the Cmake file for finding it does not interact correctly with sandboxed build ( like nix / guix ). This fixes it [2]. Or you can fix it the way GUIX fixed it [3]. 

1. https://github.com/monero-project/monero/blob/a1dc85c5373a30f14aaf7dcfdd95f5a7375d3623/CMakeLists.txt#L1131

2. https://github.com/monero-project/monero/pull/9445

3. https://git.savannah.gnu.org/cgit/guix.git/tree/gnu/packages/finance.scm#n1219

## 0xFFFC0000 | 2024-09-15T20:37:35+00:00
@Redhawk18 Feel free close the issue if you were able to build successfully. 

## Redhawk18 | 2024-09-15T21:39:45+00:00
Thanks this is my flake for anyone in the future since I've moved on
```nix
{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    devenv.url = "github:cachix/devenv";
  };

  outputs =
    inputs@{ flake-parts, nixpkgs, ... }:
    flake-parts.lib.mkFlake { inherit inputs; } {
      imports = [ inputs.devenv.flakeModule ];
      systems = nixpkgs.lib.systems.flakeExposed;

      perSystem =
        { lib
        , pkgs
        , ...
        }:
        {
          # Per-system attributes can be defined here. The self' and inputs'
          # module parameters provide easy access to attributes of the same
          # system.
          devenv.shells.default = {
            # https://devenv.sh/reference/options/
            dotenv.disableHint = true;

            languages.cplusplus.enable = true;

            env = {
              nativeBuildInputs = with pkgs; [
                ccache
                cmake
                doxygen
                gcc
                graphviz
                gtest
                pkg-config
              ];

              buildInputs = with pkgs; [
                boost
                expat
                hidapi
                libsodium
                libunwind
                libusb
                #                libpgm
                miniupnpc
                openssl
                protobuf
                readline
                systemd
                unbound
                util-linux
                xz
                zeromq
                zlib
                python3
                python312Packages.requests
                python312Packages.psutil
                python312Packages.monotonic
                python312Packages.pyzmq
                python312Packages.deepdiff
              ];
            };
          };
        };
    };
}
```

# Action History
- Created by: Redhawk18 | 2024-07-31T03:16:25+00:00
- Closed at: 2024-09-15T21:39:45+00:00
