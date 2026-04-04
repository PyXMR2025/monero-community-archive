---
title: undefined reference to `boost::re_detail::cpp_regex_traits_implementation
source_url: https://github.com/monero-project/monero/issues/5449
author: mbassan
assignees: []
labels:
- invalid
created_at: '2019-04-15T22:24:30+00:00'
updated_at: '2019-06-15T17:24:54+00:00'
type: issue
status: closed
closed_at: '2019-06-15T17:24:54+00:00'
---

# Original Description
Os: Ubuntu 16.04
Branch: release-v0.13
Dependencies have all been installed.

I am trying to `make` monero but I am receiving the following error. Any guidance would be much appreciated. I have tried setting BOOST_ROOT and BOOST_LIBDIR to no avail:

```
CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o: In function `__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > boost::re_detail::re_is_set_member<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, char, boost::regex_traits<char, boost::cpp_regex_traits<char> >, unsigned int>(__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, __gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, boost::re_detail::re_set_long<unsigned int> const*, boost::re_detail::regex_data<char, boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, bool)':
wallet_rpc_server.cpp:(.text._ZN5boost9re_detail16re_is_set_memberIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEEcNS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEjEET_SH_SH_PKNS0_11re_set_longIT2_EERKNS0_10regex_dataIT0_T1_EEb[_ZN5boost9re_detail16re_is_set_memberIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEEcNS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEjEET_SH_SH_PKNS0_11re_set_longIT2_EERKNS0_10regex_dataIT0_T1_EEb]+0x1db): undefined reference to `boost::re_detail::cpp_regex_traits_implementation<char>::transform_primary[abi:cxx11](char const*, char const*) const'
wallet_rpc_server.cpp:(.text._ZN5boost9re_detail16re_is_set_memberIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEEcNS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEjEET_SH_SH_PKNS0_11re_set_longIT2_EERKNS0_10regex_dataIT0_T1_EEb[_ZN5boost9re_detail16re_is_set_memberIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEEcNS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEjEET_SH_SH_PKNS0_11re_set_longIT2_EERKNS0_10regex_dataIT0_T1_EEb]+0x5b3): undefined reference to `boost::re_detail::cpp_regex_traits_implementation<char>::transform[abi:cxx11](char const*, char const*) const'
collect2: error: ld returned 1 exit status
src/wallet/CMakeFiles/wallet_rpc_server.dir/build.make:127: recipe for target 'bin/monero-wallet-rpc' failed
make[2]: *** [bin/monero-wallet-rpc] Error 1
CMakeFiles/Makefile2:2252: recipe for target 'src/wallet/CMakeFiles/wallet_rpc_server.dir/all' failed
make[1]: *** [src/wallet/CMakeFiles/wallet_rpc_server.dir/all] Error 2
Makefile:140: recipe for target 'all' failed
make: *** [all] Error 2
```

# Discussion History
## moneromooo-monero | 2019-04-15T22:33:12+00:00
You likely have two boost installed. Is that the case ?

## mbassan | 2019-04-16T15:25:22+00:00
Thank you for the quick response. I am not aware of having two boost installed, but I did manually install a higher version of cmake, so maybe that new version came with boost.

As far as I know I have only installed the default `libboost-dev-all` library.

I can see now, however that I do have two directories with boost files.

What should I do if there are two versions of boost?

## moneromooo-monero | 2019-04-16T16:20:34+00:00
Post the output of:

<pre>
grep -i boost `find build -name CMakeCache.txt`
</pre>

## mbassan | 2019-04-16T19:26:11+00:00
```
//Ignore boost system paths for local boost installation
BOOST_ROOT:PATH=/usr/local/include/boost
Boost_ATOMIC_LIBRARY_DEBUG:FILEPATH=/usr/lib/x86_64-linux-gnu/libboost_atomic.so
Boost_ATOMIC_LIBRARY_RELEASE:FILEPATH=/usr/lib/x86_64-linux-gnu/libboost_atomic.so
Boost_CHRONO_LIBRARY_DEBUG:FILEPATH=/usr/lib/x86_64-linux-gnu/libboost_chrono.so
Boost_CHRONO_LIBRARY_RELEASE:FILEPATH=/usr/lib/x86_64-linux-gnu/libboost_chrono.so
Boost_DATE_TIME_LIBRARY_DEBUG:FILEPATH=/usr/lib/x86_64-linux-gnu/libboost_date_time.so
Boost_DATE_TIME_LIBRARY_RELEASE:FILEPATH=/usr/lib/x86_64-linux-gnu/libboost_date_time.so
Boost_FILESYSTEM_LIBRARY_DEBUG:FILEPATH=/usr/lib/x86_64-linux-gnu/libboost_filesystem.so
Boost_FILESYSTEM_LIBRARY_RELEASE:FILEPATH=/usr/lib/x86_64-linux-gnu/libboost_filesystem.so
Boost_LOCALE_LIBRARY_DEBUG:FILEPATH=/usr/lib/x86_64-linux-gnu/libboost_locale.so
Boost_LOCALE_LIBRARY_RELEASE:FILEPATH=/usr/lib/x86_64-linux-gnu/libboost_locale.so
Boost_PROGRAM_OPTIONS_LIBRARY_DEBUG:FILEPATH=/usr/lib/x86_64-linux-gnu/libboost_program_options.so
Boost_PROGRAM_OPTIONS_LIBRARY_RELEASE:FILEPATH=/usr/lib/x86_64-linux-gnu/libboost_program_options.so
Boost_REGEX_LIBRARY_DEBUG:FILEPATH=/usr/lib/x86_64-linux-gnu/libboost_regex.so
Boost_REGEX_LIBRARY_RELEASE:FILEPATH=/usr/lib/x86_64-linux-gnu/libboost_regex.so
Boost_SERIALIZATION_LIBRARY_DEBUG:FILEPATH=/usr/lib/x86_64-linux-gnu/libboost_serialization.so
Boost_SERIALIZATION_LIBRARY_RELEASE:FILEPATH=/usr/lib/x86_64-linux-gnu/libboost_serialization.so
Boost_SYSTEM_LIBRARY_DEBUG:FILEPATH=/usr/lib/x86_64-linux-gnu/libboost_system.so
Boost_SYSTEM_LIBRARY_RELEASE:FILEPATH=/usr/lib/x86_64-linux-gnu/libboost_system.so
Boost_THREAD_LIBRARY_DEBUG:FILEPATH=/usr/lib/x86_64-linux-gnu/libboost_thread.so
Boost_THREAD_LIBRARY_RELEASE:FILEPATH=/usr/lib/x86_64-linux-gnu/libboost_thread.so
blockchain_db_LIB_DEPENDS:STATIC=general;common;general;cncrypto;general;ringct;general;lmdb;general;/usr/lib/x86_64-linux-gnu/libboost_filesystem.so;general;/usr/lib/x86_64-linux-gnu/libboost_thread.so;general;/usr/lib/x86_64-linux-gnu/librt.so;general;dl;
checkpoints_LIB_DEPENDS:STATIC=general;common;general;cncrypto;general;/usr/lib/x86_64-linux-gnu/libboost_date_time.so;general;/usr/lib/x86_64-linux-gnu/libboost_program_options.so;general;/usr/lib/x86_64-linux-gnu/libboost_serialization.so;general;/usr/lib/x86_64-linux-gnu/libboost_filesystem.so;general;/usr/lib/x86_64-linux-gnu/libboost_system.so;general;/usr/lib/x86_64-linux-gnu/libboost_thread.so;general;/usr/lib/x86_64-linux-gnu/librt.so;general;dl;
cncrypto_LIB_DEPENDS:STATIC=general;epee;general;/usr/lib/x86_64-linux-gnu/libboost_system.so;general;/usr/lib/x86_64-linux-gnu/libsodium.so;general;/usr/lib/x86_64-linux-gnu/librt.so;general;dl;
common_LIB_DEPENDS:STATIC=general;cncrypto;general;/usr/lib/x86_64-linux-gnu/libunbound.so;general;/usr/lib/x86_64-linux-gnu/libboost_date_time.so;general;/usr/lib/x86_64-linux-gnu/libboost_filesystem.so;general;/usr/lib/x86_64-linux-gnu/libboost_system.so;general;/usr/lib/x86_64-linux-gnu/libboost_thread.so;general;/usr/lib/x86_64-linux-gnu/libboost_regex.so;general;/usr/lib/x86_64-linux-gnu/libboost_chrono.so;general;/usr/lib/x86_64-linux-gnu/libssl.so;general;/usr/lib/x86_64-linux-gnu/libcrypto.so;general;/usr/lib/x86_64-linux-gnu/librt.so;general;dl;
cryptonote_basic_LIB_DEPENDS:STATIC=general;common;general;cncrypto;general;checkpoints;general;device;general;/usr/lib/x86_64-linux-gnu/libboost_date_time.so;general;/usr/lib/x86_64-linux-gnu/libboost_program_options.so;general;/usr/lib/x86_64-linux-gnu/libboost_serialization.so;general;/usr/lib/x86_64-linux-gnu/libboost_filesystem.so;general;/usr/lib/x86_64-linux-gnu/libboost_system.so;general;/usr/lib/x86_64-linux-gnu/libboost_thread.so;general;/usr/lib/x86_64-linux-gnu/librt.so;general;dl;
cryptonote_core_LIB_DEPENDS:STATIC=general;version;general;common;general;cncrypto;general;blockchain_db;general;multisig;general;ringct;general;device;general;/usr/lib/x86_64-linux-gnu/libboost_date_time.so;general;/usr/lib/x86_64-linux-gnu/libboost_program_options.so;general;/usr/lib/x86_64-linux-gnu/libboost_serialization.so;general;/usr/lib/x86_64-linux-gnu/libboost_filesystem.so;general;/usr/lib/x86_64-linux-gnu/libboost_system.so;general;/usr/lib/x86_64-linux-gnu/libboost_thread.so;general;blocks;general;/usr/lib/x86_64-linux-gnu/librt.so;general;dl;
daemon_rpc_server_LIB_DEPENDS:STATIC=general;rpc;general;cryptonote_core;general;cryptonote_protocol;general;daemon_messages;general;serialization;general;/usr/lib/x86_64-linux-gnu/libboost_chrono.so;general;/usr/lib/x86_64-linux-gnu/libboost_regex.so;general;/usr/lib/x86_64-linux-gnu/libboost_system.so;general;/usr/lib/x86_64-linux-gnu/libboost_thread.so;general;/usr/lib/x86_64-linux-gnu/libzmq.so;general;/usr/lib/x86_64-linux-gnu/libpgm.so;general;/usr/lib/x86_64-linux-gnu/libsodium.so;general;/usr/lib/x86_64-linux-gnu/librt.so;general;dl;
daemonizer_LIB_DEPENDS:STATIC=general;common;general;/usr/lib/x86_64-linux-gnu/libboost_chrono.so;general;/usr/lib/x86_64-linux-gnu/libboost_filesystem.so;general;/usr/lib/x86_64-linux-gnu/libboost_program_options.so;general;/usr/lib/x86_64-linux-gnu/librt.so;general;dl;
epee_LIB_DEPENDS:STATIC=general;easylogging;general;/usr/lib/x86_64-linux-gnu/libboost_chrono.so;general;/usr/lib/x86_64-linux-gnu/libboost_filesystem.so;general;/usr/lib/x86_64-linux-gnu/libboost_thread.so;general;/usr/lib/x86_64-linux-gnu/libssl.so;general;/usr/lib/x86_64-linux-gnu/libcrypto.so;general;/usr/lib/x86_64-linux-gnu/librt.so;general;dl;
mnemonics_LIB_DEPENDS:STATIC=general;epee;general;easylogging;general;/usr/lib/x86_64-linux-gnu/libboost_system.so;general;/usr/lib/x86_64-linux-gnu/librt.so;general;dl;
p2p_LIB_DEPENDS:STATIC=general;version;general;cryptonote_core;general;libminiupnpc-static;general;/usr/lib/x86_64-linux-gnu/libboost_chrono.so;general;/usr/lib/x86_64-linux-gnu/libboost_program_options.so;general;/usr/lib/x86_64-linux-gnu/libboost_filesystem.so;general;/usr/lib/x86_64-linux-gnu/libboost_system.so;general;/usr/lib/x86_64-linux-gnu/libboost_thread.so;general;/usr/lib/x86_64-linux-gnu/libboost_serialization.so;general;/usr/lib/x86_64-linux-gnu/librt.so;general;dl;
rpc_LIB_DEPENDS:STATIC=general;rpc_base;general;common;general;cryptonote_core;general;cryptonote_protocol;general;/usr/lib/x86_64-linux-gnu/libboost_regex.so;general;/usr/lib/x86_64-linux-gnu/libboost_thread.so;general;/usr/lib/x86_64-linux-gnu/librt.so;general;dl;
rpc_base_LIB_DEPENDS:STATIC=general;common;general;epee;general;/usr/lib/x86_64-linux-gnu/libboost_regex.so;general;/usr/lib/x86_64-linux-gnu/libboost_thread.so;general;/usr/lib/x86_64-linux-gnu/libboost_program_options.so;general;/usr/lib/x86_64-linux-gnu/librt.so;general;dl;
serialization_LIB_DEPENDS:STATIC=general;cryptonote_core;general;cryptonote_protocol;general;/usr/lib/x86_64-linux-gnu/libboost_chrono.so;general;/usr/lib/x86_64-linux-gnu/libboost_regex.so;general;/usr/lib/x86_64-linux-gnu/libboost_system.so;general;/usr/lib/x86_64-linux-gnu/libboost_thread.so;general;/usr/lib/x86_64-linux-gnu/librt.so;general;dl;
wallet_LIB_DEPENDS:STATIC=general;multisig;general;common;general;cryptonote_core;general;mnemonics;general;lmdb;general;/usr/lib/x86_64-linux-gnu/libboost_chrono.so;general;/usr/lib/x86_64-linux-gnu/libboost_serialization.so;general;/usr/lib/x86_64-linux-gnu/libboost_filesystem.so;general;/usr/lib/x86_64-linux-gnu/libboost_system.so;general;/usr/lib/x86_64-linux-gnu/libboost_thread.so;general;/usr/lib/x86_64-linux-gnu/libboost_regex.so;general;/usr/lib/x86_64-linux-gnu/librt.so;general;dl;
wallet_api_LIB_DEPENDS:STATIC=general;wallet;general;common;general;cryptonote_core;general;mnemonics;general;lmdb;general;/usr/lib/x86_64-linux-gnu/libboost_chrono.so;general;/usr/lib/x86_64-linux-gnu/libboost_serialization.so;general;/usr/lib/x86_64-linux-gnu/libboost_filesystem.so;general;/usr/lib/x86_64-linux-gnu/libboost_system.so;general;/usr/lib/x86_64-linux-gnu/libboost_thread.so;general;/usr/lib/x86_64-linux-gnu/libboost_regex.so;general;/usr/lib/x86_64-linux-gnu/librt.so;general;dl;
_BOOST_ROOT_LAST:INTERNAL=/usr/local/include/boost
_Boost_NAMESPACE_LAST:INTERNAL=boost
```

## moneromooo-monero | 2019-04-16T19:34:17+00:00
This is pointing to two different places, /usr/lib and /usr/local. This is your problem.

## mbassan | 2019-04-16T19:52:39+00:00
How do I correct this? I tried changing the values in CMakeCache.txt, but this was just a wild guess at what would correct the problem. 

I am obviously not very skilled at building from source...

## moneromooo-monero | 2019-04-16T20:00:05+00:00
I have these set:
<pre>
export BOOSTROOT=$boost_install
export BOOST_ROOT=$boost_install
export BOOST_LIB=$boost_install/lib
export BOOST_IGNORE_SYSTEM_PATHS=1
export BOOST_LIBRARYDIR=$boost_install/lib
</pre>

However, this was a result of much looking around in boost docs and search engines, so if it doesn't work for you, you get to more of the looking around :)

## moneromooo-monero | 2019-06-15T10:40:26+00:00
User config error.

+invalid

# Action History
- Created by: mbassan | 2019-04-15T22:24:30+00:00
- Closed at: 2019-06-15T17:24:54+00:00
