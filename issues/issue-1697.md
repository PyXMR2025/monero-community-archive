---
title: Error when compiling on Ubuntu 16.04
source_url: https://github.com/monero-project/monero/issues/1697
author: BTGMiningUSA
assignees: []
labels: []
created_at: '2017-02-08T10:49:22+00:00'
updated_at: '2017-02-09T08:48:18+00:00'
type: issue
status: closed
closed_at: '2017-02-08T17:40:59+00:00'
---

# Original Description
Hi,
tried to install as per your instructions and getting many errors.
clean install, ubuntu 16.04. Did updates, installed dependencies.
Tried make clean then make release, same errors

[ 93%] Linking CXX executable ../../bin/monero-blockchain-import
/root/monero/src/crypto/slow-hash.c: In function ‘cn_slow_hash’:
/root/monero/src/crypto/oaes_lib.c:948:2: warning: ‘aes_ctx’ may be used uninitialized in this function [-Wmaybe-uninitialized]
free( _ctx );
^
/root/monero/src/crypto/slow-hash.c:533:15: note: ‘aes_ctx’ was declared here
oaes_ctx aes_ctx;
^
/tmp/ccbwxXET.ltrans15.ltrans.o: In function boost::re_detail::perl_matcher<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > >, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::unwind_extra_block(bool)': <artificial>:(.text+0x1e1c): undefined reference toboost::re_detail::put_mem_block(void)'
/tmp/ccbwxXET.ltrans15.ltrans.o: In function boost::re_detail::perl_matcher<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > >, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::match_prefix()': <artificial>:(.text+0x215c): undefined reference toboost::match_results<__gnu_cxx::__normal_iterator<char const, std::__cxx11::basic_string<char, std::char_traits, std::allocator > >, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits, std::allocator > > > > >::maybe_assign(boost::match_results<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits, std::allocator > >, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits, std::allocator > > > > > const&)'
/tmp/ccbwxXET.ltrans15.ltrans.o: In function boost::re_detail::perl_matcher<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > >, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::match_match()': <artificial>:(.text+0x4d71): undefined reference toboost::match_results<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits, std::allocator > >, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits, std::allocator > > > > >::maybe_assign(boost::match_results<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits, std::allocator > >, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits, std::allocator > > > > > const&)'
/tmp/ccbwxXET.ltrans15.ltrans.o: In function tools::is_local_address(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&)': <artificial>:(.text+0x6a9d): undefined reference toboost::basic_regex<char, boost::regex_traits<char, boost::cpp_regex_traits > >::do_assign(char const*, char const*, unsigned int)'
:(.text+0x74d5): undefined reference to boost::basic_regex<char, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::do_assign(char const*, char const*, unsigned int)' /tmp/ccbwxXET.ltrans20.ltrans.o: In function__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits, std::allocator > > boost::re_detail::re_is_set_member<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits, std::allocator > >, char, boost::regex_traits<char, boost::cpp_regex_traits >, unsigned int>(__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits, std::allocator > >, __gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits, std::allocator > >, boost::re_detail::re_set_long const*, boost::re_detail::regex_data<char, boost::regex_traits<char, boost::cpp_regex_traits > > const&, bool)':
:(.text+0x59a2): undefined reference to boost::re_detail::cpp_regex_traits_implementation<char>::transform_primary(char const*, char const*) const' <artificial>:(.text+0x5bbd): undefined reference toboost::re_detail::cpp_regex_traits_implementation::transform(char const*, char const*) const'
/tmp/ccbwxXET.ltrans20.ltrans.o: In function void boost::re_detail::raise_error<boost::regex_traits_wrapper<boost::regex_traits<char, boost::cpp_regex_traits<char> > > >(boost::regex_traits_wrapper<boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, boost::regex_constants::error_type)': <artificial>:(.text+0x5f1a): undefined reference toboost::re_detail::raise_runtime_error(std::runtime_error const&)'
:(.text+0x5f38): undefined reference to boost::re_detail::get_default_error_string(boost::regex_constants::error_type)' /tmp/ccbwxXET.ltrans20.ltrans.o: In functionboost::re_detail::perl_matcher<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits, std::allocator > >, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits, std::allocator > > > >, boost::regex_traits<char, boost::cpp_regex_traits > >::extend_stack()':
:(.text+0x5fa8): undefined reference to boost::re_detail::get_mem_block()' /tmp/ccbwxXET.ltrans29.ltrans.o: In functionbool boost::regex_search<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits, std::allocator > >, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits, std::allocator > > > >, char, boost::regex_traits<char, boost::cpp_regex_traits > >(__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits, std::allocator > >, __gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits, std::allocator > >, boost::match_results<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits, std::allocator > >, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits, std::allocator > > > > >&, boost::basic_regex<char, boost::regex_traits<char, boost::cpp_regex_traits > > const&, boost::regex_constants::_match_flags, __gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits, std::allocator > >) [clone .constprop.17]':
:(.text+0x872): undefined reference to boost::re_detail::perl_matcher<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > >, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::construct_init(boost::basic_regex<char, boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, boost::regex_constants::_match_flags)' <artificial>:(.text+0x877): undefined reference toboost::re_detail::get_mem_block()'
:(.text+0x9d8): undefined reference to boost::re_detail::verify_options(unsigned int, boost::regex_constants::_match_flags)' <artificial>:(.text+0xa25): undefined reference toboost::re_detail::put_mem_block(void*)'
:(.text+0xd80): undefined reference to `boost::re_detail::put_mem_block(void*)'
collect2: error: ld returned 1 exit status
src/blockchain_utilities/CMakeFiles/blockchain_import.dir/build.make:170: recipe for target 'bin/monero-blockchain-import' failed
make[3]: *** [bin/monero-blockchain-import] Error 1
make[3]: Leaving directory '/root/monero/build/release'
CMakeFiles/Makefile2:1730: recipe for target 'src/blockchain_utilities/CMakeFiles/blockchain_import.dir/all' failed
make[2]: *** [src/blockchain_utilities/CMakeFiles/blockchain_import.dir/all] Error 2
make[2]: Leaving directory '/root/monero/build/release'
Makefile:138: recipe for target 'all' failed
make[1]: *** [all] Error 2
make[1]: Leaving directory '/root/monero/build/release'
Makefile:51: recipe for target 'release' failed
make: *** [release] Error 2
root@xmrglobalpool:~/monero#

# Discussion History
## ghost | 2017-02-08T11:57:03+00:00
#1674 has just been merged which should fix this. Please try updating your local repo and recompiling. 

If it works, please report back and then close this issue. 

## BTGMiningUSA | 2017-02-08T17:40:59+00:00
redid, followed #1674 and all is good, thank you

## ghost | 2017-02-09T08:48:18+00:00
Thanks @daveinli!

# Action History
- Created by: BTGMiningUSA | 2017-02-08T10:49:22+00:00
- Closed at: 2017-02-08T17:40:59+00:00
