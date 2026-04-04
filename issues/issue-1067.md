---
title: Error on build
source_url: https://github.com/monero-project/monero-gui/issues/1067
author: SpliffyMap
assignees: []
labels: []
created_at: '2018-01-09T14:57:22+00:00'
updated_at: '2018-01-11T19:52:55+00:00'
type: issue
status: closed
closed_at: '2018-01-11T19:52:55+00:00'
---

# Original Description
Getting these errors on build with Ubuntu.

![selection_025](https://user-images.githubusercontent.com/35120072/34726682-7198b838-f55d-11e7-8833-e2307fd3dfc8.png)
![selection_024](https://user-images.githubusercontent.com/35120072/34726683-71ba06f0-f55d-11e7-9c5c-19c450272c7e.png)

 

# Discussion History
## danrmiller | 2018-01-09T15:01:28+00:00
This will be fixed by https://github.com/monero-project/monero/pull/3061

## SpliffyMap | 2018-01-09T15:35:23+00:00
That pull request fixed transtation file error. But how about /usr/bin/ld: cannot find -lwallet_merged @danrmiller  ? 
Am I doing something wrong?
  

## danrmiller | 2018-01-09T15:47:50+00:00
You're not doing anything wrong. That error is the result of the earlier one, because it can't finish building the library it later needs to link against.

So with that patch you still get the cannot find -lwallet_merged error?

## SpliffyMap | 2018-01-09T16:16:29+00:00
It failed again, but now with other errors

> Scanning dependencies of target wallet
[ 82%] Linking CXX static library ../../lib/libwallet.a
[ 82%] Built target wallet
Scanning dependencies of target obj_rpc_base
[ 84%] Building CXX object src/rpc/CMakeFiles/obj_rpc_base.dir/rpc_args.cpp.o
[ 84%] Built target obj_rpc_base
Scanning dependencies of target rpc_base
[ 85%] Linking CXX static library librpc_base.a
[ 85%] Built target rpc_base
Scanning dependencies of target wallet_rpc_server
[ 87%] Building CXX object src/wallet/CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o
[ 88%] Linking CXX executable ../../bin/monero-wallet-rpc
CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o: In function `__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > boost::re_detail::re_is_set_member<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, char, boost::regex_traits<char, boost::cpp_regex_traits<char> >, unsigned int>(__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, __gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, boost::re_detail::re_set_long<unsigned int> const*, boost::re_detail::regex_data<char, boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, bool)':
wallet_rpc_server.cpp:(.text._ZN5boost9re_detail16re_is_set_memberIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEEcNS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEjEET_SH_SH_PKNS0_11re_set_longIT2_EERKNS0_10regex_dataIT0_T1_EEb[_ZN5boost9re_detail16re_is_set_memberIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEEcNS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEjEET_SH_SH_PKNS0_11re_set_longIT2_EERKNS0_10regex_dataIT0_T1_EEb]+0x17a): undefined reference to `boost::re_detail::cpp_regex_traits_implementation<char>::transform_primary[abi:cxx11](char const*, char const*) const'
wallet_rpc_server.cpp:(.text._ZN5boost9re_detail16re_is_set_memberIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEEcNS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEjEET_SH_SH_PKNS0_11re_set_longIT2_EERKNS0_10regex_dataIT0_T1_EEb[_ZN5boost9re_detail16re_is_set_memberIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEEcNS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEjEET_SH_SH_PKNS0_11re_set_longIT2_EERKNS0_10regex_dataIT0_T1_EEb]+0x36a): undefined reference to `boost::re_detail::cpp_regex_traits_implementation<char>::transform[abi:cxx11](char const*, char const*) const'
collect2: **error**: ld returned 1 exit status
src/wallet/CMakeFiles/wallet_rpc_server.dir/build.make:130: recipe for target 'bin/monero-wallet-rpc'failed
make[2]: *** [bin/monero-wallet-rpc] Error 1
CMakeFiles/Makefile2:2199: recipe for target 'src/wallet/CMakeFiles/wallet_rpc_server.dir/all' failed
make[1]: *** [src/wallet/CMakeFiles/wallet_rpc_server.dir/all] Error 2
Makefile:138: recipe for target 'all' failed
**make: *** [all] Error 2**
[  3%] Built target blocks
[  6%] Built target lmdb
[  7%] Built target easylogging
[ 26%] Built target obj_cncrypto
[ 28%] Built target cncrypto
[ 38%] Built target epee
-- You are currently on commit ba61734
-- The most recent tag was at 793bc97
-- You are ahead of or behind a tagged release
[ 38%] Built target genversion
[ 38%] Built target obj_version
[ 38%] Built target version
[ 39%] Built target generate_translations_header
[ 50%] Built target obj_common
[ 50%] Built target common
[ 57%] Built target obj_cryptonote_basic
[ 58%] Built target obj_checkpoints
[ 60%] Built target checkpoints
[ 61%] Built target cryptonote_basic
[ 66%] Built target obj_ringct
[ 68%] Built target ringct
[ 73%] Built target obj_cryptonote_core
[ 73%] Built target obj_multisig
[ 74%] Built target multisig
[ 76%] Built target obj_blockchain_db
[ 76%] Built target blockchain_db
[ 76%] Built target cryptonote_core
[ 77%] Built target obj_mnemonics
[ 77%] Built target mnemonics
[ 80%] Built target obj_wallet
[ 82%] Built target wallet
[ 84%] Built target obj_rpc_base
[ 85%] Built target rpc_base
[ 87%] Linking CXX executable ../../bin/monero-wallet-rpc
CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o: In function `__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > boost::re_detail::re_is_set_member<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, char, boost::regex_traits<char, boost::cpp_regex_traits<char> >, unsigned int>(__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, __gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, boost::re_detail::re_set_long<unsigned int> const*, boost::re_detail::regex_data<char, boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, bool)':
wallet_rpc_server.cpp:(.text._ZN5boost9re_detail16re_is_set_memberIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEEcNS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEjEET_SH_SH_PKNS0_11re_set_longIT2_EERKNS0_10regex_dataIT0_T1_EEb[_ZN5boost9re_detail16re_is_set_memberIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEEcNS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEjEET_SH_SH_PKNS0_11re_set_longIT2_EERKNS0_10regex_dataIT0_T1_EEb]+0x17a): undefined reference to `boost::re_detail::cpp_regex_traits_implementation<char>::transform_primary[abi:cxx11](char const*, char const*) const'
wallet_rpc_server.cpp:(.text._ZN5boost9re_detail16re_is_set_memberIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEEcNS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEjEET_SH_SH_PKNS0_11re_set_longIT2_EERKNS0_10regex_dataIT0_T1_EEb[_ZN5boost9re_detail16re_is_set_memberIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEEcNS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEjEET_SH_SH_PKNS0_11re_set_longIT2_EERKNS0_10regex_dataIT0_T1_EEb]+0x36a): undefined reference to `boost::re_detail::cpp_regex_traits_implementation<char>::transform[abi:cxx11](char const*, char const*) const'
**collect2: error: ld returned 1 exit status
src/wallet/CMakeFiles/wallet_rpc_server.dir/build.make:130: recipe for target 'bin/monero-wallet-rpc'failed**
make[2]: *** [bin/monero-wallet-rpc] Error 1
CMakeFiles/Makefile2:2199: recipe for target 'src/wallet/CMakeFiles/wallet_rpc_server.dir/all' failed
make[1]: *** [src/wallet/CMakeFiles/wallet_rpc_server.dir/all] Error 2
Makefile:138: recipe for target 'all' failed
make: *** [all] Error 2
~/CRYPTO/monero-gui/monero/build/release ~/CRYPTO/monero-gui ~/CRYPTO/monero-gui
~/CRYPTO/monero-gui/monero/build/release/src/daemon ~/CRYPTO/monero-gui/monero/build/release ~/CRYPTO/monero-gui ~/CRYPTO/monero-gui
[  2%] Built target blocks
Scanning dependencies of target libminiupnpc-static
[  3%] Building C object external/miniupnpc/CMakeFiles/libminiupnpc-static.dir/igd_desc_parse.c.o
[  3%] Building C object external/miniupnpc/CMakeFiles/libminiupnpc-static.dir/miniupnpc.c.o
[  5%] Building C object external/miniupnpc/CMakeFiles/libminiupnpc-static.dir/minixml.c.o
[  5%] Building C object external/miniupnpc/CMakeFiles/libminiupnpc-static.dir/minisoap.c.o

## SpliffyMap | 2018-01-09T16:19:16+00:00
@danrmiller 
![selection_026](https://user-images.githubusercontent.com/35120072/34730945-83c2d9a6-f569-11e7-8661-afa6a0683957.png)
![selection_027](https://user-images.githubusercontent.com/35120072/34730944-83a09a12-f569-11e7-8d0d-34068023722d.png)


## SpliffyMap | 2018-01-09T17:41:08+00:00
I found what is wrong. Yesterday I changed GCC-5 to GCC-6, now it's alright with 5
![selection_028](https://user-images.githubusercontent.com/35120072/34734615-07e63218-f575-11e7-81da-c0887427bcb2.png)

  

# Action History
- Created by: SpliffyMap | 2018-01-09T14:57:22+00:00
- Closed at: 2018-01-11T19:52:55+00:00
