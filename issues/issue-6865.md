---
title: Build failed v0.17.0.1 (release-static)
source_url: https://github.com/monero-project/monero/issues/6865
author: glenfidich75
assignees: []
labels: []
created_at: '2020-10-07T07:24:35+00:00'
updated_at: '2020-10-15T07:52:19+00:00'
type: issue
status: closed
closed_at: '2020-10-15T07:52:19+00:00'
---

# Original Description
I succeed to build monero-v0.17.0.1 'release' mode but failed 'release-static' mode

`sudo make release-static'

Error Message:
Scanning dependencies of target wallet_rpc_server
make[3]: Leaving directory '/home/hjyee/monero/build/Linux/v0.17.0.1/release'
make[3]: Entering directory '/home/hjyee/monero/build/Linux/v0.17.0.1/release'
[ 90%] Building CXX object src/wallet/CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o
[ 92%] Linking CXX executable ../../bin/monero-wallet-rpc
/opt/rh/devtoolset-8/root/usr/libexec/gcc/x86_64-redhat-linux/8/ld: /usr/local/lib/libboost_chrono.a(chrono.o): relocation R_X86_64_32 against symbol `_ZZN5boost6system15system_categoryEvE24system_category_instance' can not be used when making a PIE object; recompile with -fPIC
/opt/rh/devtoolset-8/root/usr/libexec/gcc/x86_64-redhat-linux/8/ld: /usr/local/lib/libboost_program_options.a(cmdline.o): relocation R_X86_64_32 against hidden symbol `_ZZN5boost9function1ISt6vectorINS_15program_options12basic_optionIcEESaIS4_EERS1_ISsSaISsEEE9assign_toINS_3_bi6bind_tIS6_NS_4_mfi3mf1IS6_NS2_6detail7cmdlineES9_EENSC_5list2INSC_5valueIPSH_EENS_3argILi1EEEEEEEEEvT_E13stored_vtable' can not be used when making a PIE object
/opt/rh/devtoolset-8/root/usr/libexec/gcc/x86_64-redhat-linux/8/ld: /usr/local/lib/libboost_program_options.a(options_description.o): relocation R_X86_64_32S against symbol `_ZNSs4_Rep20_S_empty_rep_storageE' can not be used when making a PIE object; recompile with -fPIC
/opt/rh/devtoolset-8/root/usr/libexec/gcc/x86_64-redhat-linux/8/ld: /usr/local/lib/libboost_program_options.a(parsers.o): relocation R_X86_64_32 against symbol `__pthread_key_create@@GLIBC_2.2.5' can not be used when making a PIE object; recompile with -fPIC
/opt/rh/devtoolset-8/root/usr/libexec/gcc/x86_64-redhat-linux/8/ld: /usr/local/lib/libboost_program_options.a(variables_map.o): relocation R_X86_64_32 against `.bss' can not be used when making a PIE object; recompile with -fPIC
/opt/rh/devtoolset-8/root/usr/libexec/gcc/x86_64-redhat-linux/8/ld: /usr/local/lib/libboost_program_options.a(value_semantic.o): relocation R_X86_64_32 against hidden symbol `_ZN5boost15program_options3argE' can not be used when making a PIE object
/opt/rh/devtoolset-8/root/usr/libexec/gcc/x86_64-redhat-linux/8/ld: /usr/local/lib/libboost_program_options.a(positional_options.o): relocation R_X86_64_32S against symbol `_ZNSs4_Rep20_S_empty_rep_storageE' can not be used when making a PIE object; recompile with -fPIC
/opt/rh/devtoolset-8/root/usr/libexec/gcc/x86_64-redhat-linux/8/ld: /usr/local/lib/libboost_program_options.a(convert.o): relocation R_X86_64_32S against hidden symbol `_ZNKSt23__codecvt_abstract_baseIwc11__mbstate_tE2inERS0_PKcS4_RS4_PwS6_RS6_' can not be used when making a PIE object
/opt/rh/devtoolset-8/root/usr/libexec/gcc/x86_64-redhat-linux/8/ld: /usr/local/lib/libboost_program_options.a(config_file.o): relocation R_X86_64_32S against symbol `_ZNSs4_Rep20_S_empty_rep_storageE' can not be used when making a PIE object; recompile with -fPIC
/opt/rh/devtoolset-8/root/usr/libexec/gcc/x86_64-redhat-linux/8/ld: /usr/local/lib/libboost_program_options.a(utf8_codecvt_facet.o): relocation R_X86_64_32S against hidden symbol `_ZTVN5boost15program_options6detail18utf8_codecvt_facetE' can not be used when making a PIE object
/opt/rh/devtoolset-8/root/usr/libexec/gcc/x86_64-redhat-linux/8/ld: /usr/local/lib/libboost_filesystem.a(operations.o): relocation R_X86_64_32S against symbol `_ZZN5boost6system15system_categoryEvE24system_category_instance' can not be used when making a PIE object; recompile with -fPIC
/opt/rh/devtoolset-8/root/usr/libexec/gcc/x86_64-redhat-linux/8/ld: /usr/local/lib/libboost_filesystem.a(path.o): relocation R_X86_64_32S against symbol `_ZNSs4_Rep20_S_empty_rep_storageE' can not be used when making a PIE object; recompile with -fPIC
/opt/rh/devtoolset-8/root/usr/libexec/gcc/x86_64-redhat-linux/8/ld: /usr/local/lib/libboost_filesystem.a(exception.o): relocation R_X86_64_32 against `.rodata.str1.1' can not be used when making a PIE object; recompile with -fPIC
/opt/rh/devtoolset-8/root/usr/libexec/gcc/x86_64-redhat-linux/8/ld: /usr/local/lib/libboost_filesystem.a(directory.o): relocation R_X86_64_32S against symbol `_ZZN5boost6system15system_categoryEvE24system_category_instance' can not be used when making a PIE object; recompile with -fPIC
/opt/rh/devtoolset-8/root/usr/libexec/gcc/x86_64-redhat-linux/8/ld: /usr/local/lib/libboost_thread.a(thread.o): relocation R_X86_64_32 against `.text' can not be used when making a PIE object; recompile with -fPIC
/opt/rh/devtoolset-8/root/usr/libexec/gcc/x86_64-redhat-linux/8/ld: /usr/local/lib/libboost_thread.a(once.o): relocation R_X86_64_32 against `.bss' can not be used when making a PIE object; recompile with -fPIC
/opt/rh/devtoolset-8/root/usr/libexec/gcc/x86_64-redhat-linux/8/ld: /usr/local/lib/libboost_serialization.a(basic_archive.o): relocation R_X86_64_32 against `.rodata.str1.1' can not be used when making a PIE object; recompile with -fPIC
/opt/rh/devtoolset-8/root/usr/libexec/gcc/x86_64-redhat-linux/8/ld: /usr/local/lib/libboost_serialization.a(basic_iarchive.o): relocation R_X86_64_32S against symbol `_ZTVN5boost7archive6detail14basic_iarchiveE' can not be used when making a PIE object; recompile with -fPIC
/opt/rh/devtoolset-8/root/usr/libexec/gcc/x86_64-redhat-linux/8/ld: /usr/local/lib/libboost_serialization.a(basic_iserializer.o): relocation R_X86_64_32S against symbol `_ZTVN5boost7archive6detail17basic_iserializerE' can not be used when making a PIE object; recompile with -fPIC
/opt/rh/devtoolset-8/root/usr/libexec/gcc/x86_64-redhat-linux/8/ld: /usr/local/lib/libboost_serialization.a(binary_iarchive.o): relocation R_X86_64_32S against hidden symbol `_ZTVN5boost7archive12codecvt_nullIcEE' can not be used when making a PIE object
/opt/rh/devtoolset-8/root/usr/libexec/gcc/x86_64-redhat-linux/8/ld: /usr/local/lib/libboost_serialization.a(extended_type_info.o): relocation R_X86_64_32S against symbol `_ZTVN5boost13serialization18extended_type_infoE' can not be used when making a PIE object; recompile with -fPIC
/opt/rh/devtoolset-8/root/usr/libexec/gcc/x86_64-redhat-linux/8/ld: /usr/local/lib/libboost_serialization.a(extended_type_info_typeid.o): relocation R_X86_64_32S against symbol `_ZTVN5boost13serialization13typeid_system27extended_type_info_typeid_0E' can not be used when making a PIE object; recompile with -fPIC
/opt/rh/devtoolset-8/root/usr/libexec/gcc/x86_64-redhat-linux/8/ld: /usr/local/lib/libboost_serialization.a(archive_exception.o): relocation R_X86_64_32S against symbol `_ZTVN5boost7archive17archive_exceptionE' can not be used when making a PIE object; recompile with -fPIC
/opt/rh/devtoolset-8/root/usr/libexec/gcc/x86_64-redhat-linux/8/ld: /usr/local/lib/libboost_regex.a(instances.o): relocation R_X86_64_32S against `.rodata' can not be used when making a PIE object; recompile with -fPIC
/opt/rh/devtoolset-8/root/usr/libexec/gcc/x86_64-redhat-linux/8/ld: /usr/local/lib/libboost_regex.a(regex.o): relocation R_X86_64_32S against hidden symbol `_ZTVN5boost11regex_errorE' can not be used when making a PIE object
/opt/rh/devtoolset-8/root/usr/libexec/gcc/x86_64-redhat-linux/8/ld: /usr/local/lib/libboost_regex.a(regex_traits_defaults.o): relocation R_X86_64_32 against `.rodata' can not be used when making a PIE object; recompile with -fPIC
/opt/rh/devtoolset-8/root/usr/libexec/gcc/x86_64-redhat-linux/8/ld: /usr/local/lib/libboost_regex.a(cpp_regex_traits.o): relocation R_X86_64_32 against hidden symbol `_ZZN5boost16cpp_regex_traitsIcE14get_mutex_instEvE7s_mutex' can not be used when making a PIE object
/opt/rh/devtoolset-8/root/usr/libexec/gcc/x86_64-redhat-linux/8/ld: /usr/local/lib/libboost_thread.a(future.o): relocation R_X86_64_32 against `.rodata.str1.1' can not be used when making a PIE object; recompile with -fPIC
/opt/rh/devtoolset-8/root/usr/libexec/gcc/x86_64-redhat-linux/8/ld: /usr/local/lib/libboost_filesystem.a(unique_path.o): relocation R_X86_64_32 against symbol `_ZZN5boost6system15system_categoryEvE24system_category_instance' can not be used when making a PIE object; recompile with -fPIC
/opt/rh/devtoolset-8/root/usr/libexec/gcc/x86_64-redhat-linux/8/ld: final link failed: Nonrepresentable section on output
collect2: error: ld returned 1 exit status
make[3]: *** [src/wallet/CMakeFiles/wallet_rpc_server.dir/build.make:157: bin/monero-wallet-rpc] Error 1
make[3]: Leaving directory '/home/hjyee/monero/build/Linux/v0.17.0.1/release'
make[2]: *** [CMakeFiles/Makefile2:2855: src/wallet/CMakeFiles/wallet_rpc_server.dir/all] Error 2
make[2]: Leaving directory '/home/hjyee/monero/build/Linux/v0.17.0.1/release'
make[1]: *** [Makefile:160: all] Error 2
make[1]: Leaving directory '/home/hjyee/monero/build/Linux/v0.17.0.1/release'
make: *** [Makefile:107: release-static] Error 2


Please help me

# Discussion History
## moneromooo-monero | 2020-10-07T16:36:46+00:00
This message tells you what to do:
> R_X86_64_32 against hidden symbol _ZZN5boost16cpp_regex_traitsIcE14get_mutex_instEvE7s_mutex' can not be used when making a PIE object /opt/rh/devtoolset-8/root/usr/libexec/gcc/x86_64-redhat-linux/8/ld: /usr/local/lib/libboost_thread.a(future.o): relocation R_X86_64_32 against .rodata.str1.1' can not be used when making a PIE object; recompile with -fPIC

Build boost with -fPIC. PIC (Position independent code) is traditionally used only for shared libraries, but building a position independent executable (PIE) also needs it, and PIE is needed for ASLR, a security defense layer, which monero enables.

## glenfidich75 | 2020-10-15T07:52:15+00:00
Thanks

# Action History
- Created by: glenfidich75 | 2020-10-07T07:24:35+00:00
- Closed at: 2020-10-15T07:52:19+00:00
