---
title: Build from source failing in Ubuntu 18.04
source_url: https://github.com/monero-project/monero/issues/6432
author: Sviluppo718
assignees: []
labels: []
created_at: '2020-04-06T03:39:00+00:00'
updated_at: '2020-05-16T15:56:51+00:00'
type: issue
status: closed
closed_at: '2020-05-16T15:56:51+00:00'
---

# Original Description
My configuration/system seems to be very up-to-date and all the required dependencies seem to be met.

I'm getting the output and errors as follows:
```
[ 51%] Building CXX object tests/fuzz/CMakeFiles/http-client_fuzz_tests.dir/fuzzer.cpp.o
[ 51%] Linking CXX executable parse-url_fuzz_tests
CMakeFiles/parse-url_fuzz_tests.dir/parse_url.cpp.o: In function `__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > boost::re_detail_106700::re_is_set_member<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, char, boost::regex_traits<char, boost::cpp_regex_traits<char> >, unsigned int>(__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, __gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, boost::re_detail_106700::re_set_long<unsigned int> const*, boost::re_detail_106700::regex_data<char, boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, bool)':
parse_url.cpp:(.text._ZN5boost16re_detail_10670016re_is_set_memberIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEEcNS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEjEET_SH_SH_PKNS0_11re_set_longIT2_EERKNS0_10regex_dataIT0_T1_EEb[_ZN5boost16re_detail_10670016re_is_set_memberIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEEcNS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEjEET_SH_SH_PKNS0_11re_set_longIT2_EERKNS0_10regex_dataIT0_T1_EEb]+0x1bb): undefined reference to `boost::re_detail_106700::cpp_regex_traits_implementation<char>::transform_primary[abi:cxx11](char const*, char const*) const'
parse_url.cpp:(.text._ZN5boost16re_detail_10670016re_is_set_memberIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEEcNS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEjEET_SH_SH_PKNS0_11re_set_longIT2_EERKNS0_10regex_dataIT0_T1_EEb[_ZN5boost16re_detail_10670016re_is_set_memberIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEEcNS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEjEET_SH_SH_PKNS0_11re_set_longIT2_EERKNS0_10regex_dataIT0_T1_EEb]+0x5b1): undefined reference to `boost::re_detail_106700::cpp_regex_traits_implementation<char>::transform[abi:cxx11](char const*, char const*) const'
collect2: error: ld returned 1 exit status
tests/fuzz/CMakeFiles/parse-url_fuzz_tests.dir/build.make:132: recipe for target 'tests/fuzz/parse-url_fuzz_tests' failed
make[3]: *** [tests/fuzz/parse-url_fuzz_tests] Error 1
make[3]: Leaving directory '[snip]/monero/build/Linux/release-v0.15/release'
CMakeFiles/Makefile2:5085: recipe for target 'tests/fuzz/CMakeFiles/parse-url_fuzz_tests.dir/all' failed
make[2]: *** [tests/fuzz/CMakeFiles/parse-url_fuzz_tests.dir/all] Error 2
make[2]: *** Waiting for unfinished jobs....
[ 52%] Linking CXX executable http-client_fuzz_tests
CMakeFiles/http-client_fuzz_tests.dir/http-client.cpp.o: In function `__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > boost::re_detail_106700::re_is_set_member<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, char, boost::regex_traits<char, boost::cpp_regex_traits<char> >, unsigned int>(__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, __gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, boost::re_detail_106700::re_set_long<unsigned int> const*, boost::re_detail_106700::regex_data<char, boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, bool)':
http-client.cpp:(.text._ZN5boost16re_detail_10670016re_is_set_memberIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEEcNS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEjEET_SH_SH_PKNS0_11re_set_longIT2_EERKNS0_10regex_dataIT0_T1_EEb[_ZN5boost16re_detail_10670016re_is_set_memberIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEEcNS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEjEET_SH_SH_PKNS0_11re_set_longIT2_EERKNS0_10regex_dataIT0_T1_EEb]+0x424): undefined reference to `boost::re_detail_106700::cpp_regex_traits_implementation<char>::transform_primary[abi:cxx11](char const*, char const*) const'
http-client.cpp:(.text._ZN5boost16re_detail_10670016re_is_set_memberIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEEcNS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEjEET_SH_SH_PKNS0_11re_set_longIT2_EERKNS0_10regex_dataIT0_T1_EEb[_ZN5boost16re_detail_10670016re_is_set_memberIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEEcNS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEjEET_SH_SH_PKNS0_11re_set_longIT2_EERKNS0_10regex_dataIT0_T1_EEb]+0x551): undefined reference to `boost::re_detail_106700::cpp_regex_traits_implementation<char>::transform[abi:cxx11](char const*, char const*) const'
collect2: error: ld returned 1 exit status
tests/fuzz/CMakeFiles/http-client_fuzz_tests.dir/build.make:133: recipe for target 'tests/fuzz/http-client_fuzz_tests' failed
make[3]: *** [tests/fuzz/http-client_fuzz_tests] Error 1
make[3]: Leaving directory '[snip]//monero/build/Linux/release-v0.15/release'
CMakeFiles/Makefile2:4864: recipe for target 'tests/fuzz/CMakeFiles/http-client_fuzz_tests.dir/all' failed
make[2]: *** [tests/fuzz/CMakeFiles/http-client_fuzz_tests.dir/all] Error 2
make[2]: Leaving directory '[snip]//monero/build/Linux/release-v0.15/release'
Makefile:140: recipe for target 'all' failed
make[1]: *** [all] Error 2
make[1]: Leaving directory '[snip]//monero/build/Linux/release-v0.15/release'
Makefile:95: recipe for target 'release' failed
make: *** [release] Error 2
```

Any suggestions on how what might need altering or adjustment?  I've tried a few variations of the instructions the most recent being:

$ git clone --recursive https://github.com/monero-project/monero
$ cd monero
$ git submodule update
$ git checkout release-v0.15
$ make -j3

also: 
$ make -j3 release

(flailing here :P)

# Discussion History
## sumogr | 2020-04-06T07:18:54+00:00
you have two boost versions conflicting
you had one already configured in the past the way you wanted and you reinstalled another version with libboost-all-dev if you dont need both my suggestion would be uninstall cleanly both and reinstall libbost-all-dev with apt

## moneromooo-monero | 2020-05-16T15:56:51+00:00
Very probably user error and no followup, closing.

# Action History
- Created by: Sviluppo718 | 2020-04-06T03:39:00+00:00
- Closed at: 2020-05-16T15:56:51+00:00
