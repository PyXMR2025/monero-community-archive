---
title: Fuzz tests fail to compile.
source_url: https://github.com/monero-project/monero/issues/5023
author: dachen0
assignees: []
labels:
- invalid
created_at: '2018-12-27T22:46:31+00:00'
updated_at: '2019-01-01T15:09:01+00:00'
type: issue
status: closed
closed_at: '2019-01-01T15:09:01+00:00'
---

# Original Description
I was trying to compile Monero from master and then this happened...
CMakeFiles/http-client_fuzz_tests.dir/http-client.cpp.o: In function `__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > boost::re_detail_106501::re_is_set_member<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, char, boost::regex_traits<char, boost::cpp_regex_traits<char> >, unsigned int>(__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, __gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, boost::re_detail_106501::re_set_long<unsigned int> const*, boost::re_detail_106501::regex_data<char, boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, bool)':
http-client.cpp:(.text._ZN5boost16re_detail_10650116re_is_set_memberIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEEcNS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEjEET_SH_SH_PKNS0_11re_set_longIT2_EERKNS0_10regex_dataIT0_T1_EEb[_ZN5boost16re_detail_10650116re_is_set_memberIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEEcNS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEjEET_SH_SH_PKNS0_11re_set_longIT2_EERKNS0_10regex_dataIT0_T1_EEb]+0x159): undefined reference to `boost::re_detail_106501::cpp_regex_traits_implementation<char>::transform_primary(char const*, char const*) const'
http-client.cpp:(.text._ZN5boost16re_detail_10650116re_is_set_memberIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEEcNS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEjEET_SH_SH_PKNS0_11re_set_longIT2_EERKNS0_10regex_dataIT0_T1_EEb[_ZN5boost16re_detail_10650116re_is_set_memberIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEEcNS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEjEET_SH_SH_PKNS0_11re_set_longIT2_EERKNS0_10regex_dataIT0_T1_EEb]+0x332): undefined reference to `boost::re_detail_106501::cpp_regex_traits_implementation<char>::transform(char const*, char const*) const'
collect2: error: ld returned 1 exit status
tests/fuzz/CMakeFiles/http-client_fuzz_tests.dir/build.make:133: recipe for target 'tests/fuzz/http-client_fuzz_tests' failed
make[3]: *** [tests/fuzz/http-client_fuzz_tests] Error 1


# Discussion History
## moneromooo-monero | 2018-12-27T22:50:42+00:00
Do you have several boost versions installed ?

## dachen0 | 2018-12-28T00:56:17+00:00
Yes.

## dachen0 | 2018-12-28T01:00:45+00:00
Actually, no I don't think so.

## moneromooo-monero | 2018-12-28T10:35:01+00:00
Check only one boost install is getting used (check cmake output, CMakeCache.txt, and compiler + linker commands).

## dachen0 | 2018-12-29T02:03:50+00:00
I did a fresh install and that part compiled.

## moneromooo-monero | 2019-01-01T14:56:06+00:00
+invalid

# Action History
- Created by: dachen0 | 2018-12-27T22:46:31+00:00
- Closed at: 2019-01-01T15:09:01+00:00
