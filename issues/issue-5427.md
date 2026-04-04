---
title: Compilation error when cross compiling to ARMv7 with -DBACKCOMPAT enabled
source_url: https://github.com/monero-project/monero/issues/5427
author: throwaway2957
assignees: []
labels: []
created_at: '2019-04-12T03:14:16+00:00'
updated_at: '2022-02-19T04:57:04+00:00'
type: issue
status: closed
closed_at: '2022-02-19T04:57:03+00:00'
---

# Original Description
I'm trying to compile from master (5dbcceb6640) using the following command:

` make -j6 depends target=arm-linux-gnueabihf`

the build fails with this error:
```
[ 88%] Linking CXX executable ../../bin/monero-blockchain-import
../../external/unbound/libunbound.a(configlexer.c.o): In function `config_start_include_glob':
configlexer.c:(.text+0x4fe): undefined reference to `__wrap_glob'
../../external/unbound/libunbound.a(config_file.c.o): In function `config_read':
config_file.c:(.text+0x264): undefined reference to `__wrap_glob'
../../external/unbound/libunbound.a(val_anchor.c.o): In function `anchors_apply_cfg':
val_anchor.c:(.text+0x1530): undefined reference to `__wrap_glob'
collect2: error: ld returned 1 exit status
src/blockchain_utilities/CMakeFiles/blockchain_import.dir/build.make:182: recipe for target 'bin/monero-blockchain-import' failed
make[3]: *** [bin/monero-blockchain-import] Error 1
make[3]: Leaving directory '/home/thowaway/monero/build/arm-linux-gnueabihf/release'
CMakeFiles/Makefile2:3418: recipe for target 'src/blockchain_utilities/CMakeFiles/blockchain_import.dir/all' failed
make[2]: *** [src/blockchain_utilities/CMakeFiles/blockchain_import.dir/all] Error 2
../../external/unbound/libunbound.a(configlexer.c.o): In function `config_start_include_glob':
configlexer.c:(.text+0x4fe): undefined reference to `__wrap_glob'
../../external/unbound/libunbound.a(config_file.c.o): In function `config_read':
config_file.c:(.text+0x264): undefined reference to `__wrap_glob'
../../external/unbound/libunbound.a(val_anchor.c.o): In function `anchors_apply_cfg':
val_anchor.c:(.text+0x1530): undefined reference to `__wrap_glob'
collect2: error: ld returned 1 exit status
src/blockchain_utilities/CMakeFiles/blockchain_export.dir/build.make:181: recipe for target 'bin/monero-blockchain-export' failed
make[3]: *** [bin/monero-blockchain-export] Error 1
make[3]: Leaving directory '/home/thowaway/monero/build/arm-linux-gnueabihf/release'
CMakeFiles/Makefile2:3366: recipe for target 'src/blockchain_utilities/CMakeFiles/blockchain_export.dir/all' failed
make[2]: *** [src/blockchain_utilities/CMakeFiles/blockchain_export.dir/all] Error 2
In file included from /usr/arm-linux-gnueabihf/include/c++/7/vector:69:0,
                 from /usr/arm-linux-gnueabihf/include/c++/7/bits/random.h:34,
                 from /usr/arm-linux-gnueabihf/include/c++/7/random:49,
                 from /home/thowaway/monero/src/wallet/wallet2.cpp:32:
/usr/arm-linux-gnueabihf/include/c++/7/bits/vector.tcc: In member function ‘bool epee::json_rpc::response<t_param, t_error>::load(t_storage&, typename t_storage::hsection) [with t_storage = epee::serialization::portable_storage; t_param = epee::misc_utils::struct_init<cryptonote::COMMAND_RPC_GET_BLOCK_HEADERS_RANGE::response_t>; t_error = epee::json_rpc::error]’:
/usr/arm-linux-gnueabihf/include/c++/7/bits/vector.tcc:143:19: note: parameter passing for argument of type ‘__gnu_cxx::__normal_iterator<cryptonote::block_header_response*, std::vector<cryptonote::block_header_response> >’ changed in GCC 7.1
  _M_realloc_insert(begin() + (__position - cbegin()), __x);
  ~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
make[3]: Leaving directory '/home/thowaway/monero/build/arm-linux-gnueabihf/release'
[ 88%] Built target obj_wallet
make[2]: Leaving directory '/home/thowaway/monero/build/arm-linux-gnueabihf/release'
Makefile:140: recipe for target 'all' failed
make[1]: *** [all] Error 2
make[1]: Leaving directory '/home/thowaway/monero/build/arm-linux-gnueabihf/release'
Makefile:50: recipe for target 'depends' failed
make: *** [depends] Error 2

```

It seems to be an issue with the `-Wl,--wrap=glob` flag.

PS: I had to edit `monero/CMakeLists.txt` directly because `make` wouldn't pick-up the `-DBACKCOMPAT` flag.
I just commented the if statement so the flags could be set no matter what. Here's that change:

```sh
  #if(BACKCOMPAT)
      add_linker_flag_if_supported(-Wl,--wrap=__divmoddi4 LD_BACKCOMPAT_FLAGS)
      add_linker_flag_if_supported(-Wl,--wrap=glob LD_BACKCOMPAT_FLAGS)
      message(STATUS "Using Lib C back compat flags: ${LD_BACKCOMPAT_FLAGS}")
  #endif()
```  

The flags were set as intended, but then compilation failed at 88%

# Discussion History
## sedited | 2019-06-13T00:13:01+00:00
Sorry for picking this up months later. `-DBACKCOMPAT=ON` has to be passed to cmake, before you run make, so you probably have to edit the makefile to make the cmake command include the backcompat flag. Either way it should build if the flags are set. Can you tell me on which operating system you were attempting this?

## moneromooo-monero | 2019-06-15T10:41:26+00:00
A path in the log says: /home/thowaway/monero/build/arm-linux-gnueabihf/release

So it's probably linux on arm.

## selsta | 2022-02-19T04:57:03+00:00
We cross compile every commit to ARMv7 on CI. It seems to work fine these days. Please comment if you still run into issues.

# Action History
- Created by: throwaway2957 | 2019-04-12T03:14:16+00:00
- Closed at: 2022-02-19T04:57:03+00:00
