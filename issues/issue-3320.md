---
title: Build errors on OSX (Sierra)
source_url: https://github.com/monero-project/monero/issues/3320
author: gsovereignty
assignees: []
labels: []
created_at: '2018-02-26T21:02:05+00:00'
updated_at: '2021-08-13T04:25:16+00:00'
type: issue
status: closed
closed_at: '2021-08-13T04:25:16+00:00'
---

# Original Description
Any ideas on what I can do about this error during the build process?

```
Undefined symbols for architecture x86_64:
  "boost::this_thread::hiden::sleep_until(timespec const&)", referenced from:
      epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::call_run_once_service_io() in wallet_rpc_server.cpp.o
      void boost::this_thread::sleep<boost::date_time::subsecond_duration<boost::posix_time::time_duration, 1000ll> >(boost::date_time::subsecond_duration<boost::posix_time::time_duration, 1000ll> const&) in wallet_rpc_server.cpp.o
      void boost::this_thread::sleep<boost::date_time::subsecond_duration<boost::posix_time::time_duration, 1000ll> >(boost::date_time::subsecond_duration<boost::posix_time::time_duration, 1000ll> const&) in libepee.a(connection_basic.cpp.o)
      cryptonote::miner::worker_thread() in libcryptonote_basic.a(miner.cpp.o)
  "boost::this_thread::hiden::sleep_for(timespec const&)", referenced from:
      epee::net_utils::http::http_simple_client_template<epee::net_utils::blocked_mode_client>::handle_target_data(std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> >&) in wallet_rpc_server.cpp.o
      epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::run_server(unsigned long, bool, boost::thread_attributes const&) in wallet_rpc_server.cpp.o
      epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::close() in wallet_rpc_server.cpp.o
      epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::add_ref() in wallet_rpc_server.cpp.o
      epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::release() in wallet_rpc_server.cpp.o
      epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::do_send_chunk(void const*, unsigned long) in wallet_rpc_server.cpp.o
      epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::handle_write(boost::system::error_code const&, unsigned long) in wallet_rpc_server.cpp.o
      ...
  "boost::re_detail::get_mem_block()", referenced from:
      boost::re_detail::perl_matcher<std::__1::__wrap_iter<char const*>, std::__1::allocator<boost::sub_match<std::__1::__wrap_iter<char const*> > >, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::match_imp() in wallet_rpc_server.cpp.o
      boost::re_detail::perl_matcher<std::__1::__wrap_iter<char const*>, std::__1::allocator<boost::sub_match<std::__1::__wrap_iter<char const*> > >, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::match_all_states() in wallet_rpc_server.cpp.o
      boost::re_detail::perl_matcher<std::__1::__wrap_iter<char const*>, std::__1::allocator<boost::sub_match<std::__1::__wrap_iter<char const*> > >, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::match_startmark() in wallet_rpc_server.cpp.o
      boost::re_detail::perl_matcher<std::__1::__wrap_iter<char const*>, std::__1::allocator<boost::sub_match<std::__1::__wrap_iter<char const*> > >, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::match_alt() in wallet_rpc_server.cpp.o
      boost::re_detail::perl_matcher<std::__1::__wrap_iter<char const*>, std::__1::allocator<boost::sub_match<std::__1::__wrap_iter<char const*> > >, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::match_rep() in wallet_rpc_server.cpp.o
      boost::re_detail::perl_matcher<std::__1::__wrap_iter<char const*>, std::__1::allocator<boost::sub_match<std::__1::__wrap_iter<char const*> > >, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::match_char_repeat() in wallet_rpc_server.cpp.o
      boost::re_detail::perl_matcher<std::__1::__wrap_iter<char const*>, std::__1::allocator<boost::sub_match<std::__1::__wrap_iter<char const*> > >, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::match_set_repeat() in wallet_rpc_server.cpp.o
      ...
  "boost::re_detail::put_mem_block(void*)", referenced from:
      boost::re_detail::perl_matcher<std::__1::__wrap_iter<char const*>, std::__1::allocator<boost::sub_match<std::__1::__wrap_iter<char const*> > >, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::match_imp() in wallet_rpc_server.cpp.o
      boost::re_detail::perl_matcher<std::__1::__wrap_iter<char const*>, std::__1::allocator<boost::sub_match<std::__1::__wrap_iter<char const*> > >, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::unwind_extra_block(bool) in wallet_rpc_server.cpp.o
      boost::re_detail::perl_matcher<std::__1::__wrap_iter<char const*>, std::__1::allocator<boost::sub_match<std::__1::__wrap_iter<char const*> > >, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::find_imp() in wallet_rpc_server.cpp.o
      boost::re_detail::perl_matcher<std::__1::__wrap_iter<char const*>, std::__1::allocator<boost::sub_match<std::__1::__wrap_iter<char const*> > >, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::find_imp() in libcommon.a(util.cpp.o)
      boost::re_detail::perl_matcher<std::__1::__wrap_iter<char const*>, std::__1::allocator<boost::sub_match<std::__1::__wrap_iter<char const*> > >, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::unwind_extra_block(bool) in libcommon.a(util.cpp.o)
      boost::re_detail::perl_matcher<std::__1::__wrap_iter<char const*>, std::__1::allocator<boost::sub_match<std::__1::__wrap_iter<char const*> > >, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::find_imp() in libwallet.a(wallet2.cpp.o)
      boost::re_detail::perl_matcher<std::__1::__wrap_iter<char const*>, std::__1::allocator<boost::sub_match<std::__1::__wrap_iter<char const*> > >, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::unwind_extra_block(bool) in libwallet.a(wallet2.cpp.o)
      ...
  "boost::re_detail::verify_options(unsigned int, boost::regex_constants::_match_flags)", referenced from:
      boost::re_detail::perl_matcher<std::__1::__wrap_iter<char const*>, std::__1::allocator<boost::sub_match<std::__1::__wrap_iter<char const*> > >, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::match_imp() in wallet_rpc_server.cpp.o
      boost::re_detail::perl_matcher<std::__1::__wrap_iter<char const*>, std::__1::allocator<boost::sub_match<std::__1::__wrap_iter<char const*> > >, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::find_imp() in wallet_rpc_server.cpp.o
      boost::re_detail::perl_matcher<std::__1::__wrap_iter<char const*>, std::__1::allocator<boost::sub_match<std::__1::__wrap_iter<char const*> > >, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::find_imp() in libcommon.a(util.cpp.o)
      boost::re_detail::perl_matcher<std::__1::__wrap_iter<char const*>, std::__1::allocator<boost::sub_match<std::__1::__wrap_iter<char const*> > >, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::find_imp() in libwallet.a(wallet2.cpp.o)
      boost::re_detail::perl_matcher<std::__1::__wrap_iter<char const*>, std::__1::allocator<boost::sub_match<std::__1::__wrap_iter<char const*> > >, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::match_imp() in libwallet.a(wallet2.cpp.o)
      boost::re_detail::perl_matcher<std::__1::__wrap_iter<char const*>, std::__1::allocator<boost::sub_match<std::__1::__wrap_iter<char const*> > >, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::match_imp() in libcheckpoints.a(checkpoints.cpp.o)
      boost::re_detail::perl_matcher<std::__1::__wrap_iter<char const*>, std::__1::allocator<boost::sub_match<std::__1::__wrap_iter<char const*> > >, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::find_imp() in libwallet.a(node_rpc_proxy.cpp.o)
      ...
  "boost::re_detail::raise_runtime_error(std::runtime_error const&)", referenced from:
      void boost::re_detail::raise_error<boost::regex_traits_wrapper<boost::regex_traits<char, boost::cpp_regex_traits<char> > > >(boost::regex_traits_wrapper<boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, boost::regex_constants::error_type) in wallet_rpc_server.cpp.o
      void boost::re_detail::raise_error<boost::regex_traits_wrapper<boost::regex_traits<char, boost::cpp_regex_traits<char> > > >(boost::regex_traits_wrapper<boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, boost::regex_constants::error_type) in libcommon.a(util.cpp.o)
      void boost::re_detail::raise_error<boost::regex_traits_wrapper<boost::regex_traits<char, boost::cpp_regex_traits<char> > > >(boost::regex_traits_wrapper<boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, boost::regex_constants::error_type) in libwallet.a(wallet2.cpp.o)
      void boost::re_detail::raise_error<boost::regex_traits_wrapper<boost::regex_traits<char, boost::cpp_regex_traits<char> > > >(boost::regex_traits_wrapper<boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, boost::regex_constants::error_type) in libcheckpoints.a(checkpoints.cpp.o)
      void boost::re_detail::raise_error<boost::regex_traits_wrapper<boost::regex_traits<char, boost::cpp_regex_traits<char> > > >(boost::regex_traits_wrapper<boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, boost::regex_constants::error_type) in libwallet.a(node_rpc_proxy.cpp.o)
      void boost::re_detail::raise_error<boost::regex_traits_wrapper<boost::regex_traits<char, boost::cpp_regex_traits<char> > > >(boost::regex_traits_wrapper<boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, boost::regex_constants::error_type) in libcryptonote_basic.a(miner.cpp.o)
  "boost::re_detail::get_default_error_string(boost::regex_constants::error_type)", referenced from:
      boost::re_detail::cpp_regex_traits_implementation<char>::error_string(boost::regex_constants::error_type) const in wallet_rpc_server.cpp.o
      boost::re_detail::cpp_regex_traits_implementation<char>::error_string(boost::regex_constants::error_type) const in libcommon.a(util.cpp.o)
      boost::re_detail::cpp_regex_traits_implementation<char>::error_string(boost::regex_constants::error_type) const in libwallet.a(wallet2.cpp.o)
      boost::re_detail::cpp_regex_traits_implementation<char>::error_string(boost::regex_constants::error_type) const in libcheckpoints.a(checkpoints.cpp.o)
      boost::re_detail::cpp_regex_traits_implementation<char>::error_string(boost::regex_constants::error_type) const in libwallet.a(node_rpc_proxy.cpp.o)
      boost::re_detail::cpp_regex_traits_implementation<char>::error_string(boost::regex_constants::error_type) const in libcryptonote_basic.a(miner.cpp.o)
  "boost::re_detail::cpp_regex_traits_implementation<char>::transform_primary(char const*, char const*) const", referenced from:
      std::__1::__wrap_iter<char const*> boost::re_detail::re_is_set_member<std::__1::__wrap_iter<char const*>, char, boost::regex_traits<char, boost::cpp_regex_traits<char> >, unsigned int>(std::__1::__wrap_iter<char const*>, std::__1::__wrap_iter<char const*>, boost::re_detail::re_set_long<unsigned int> const*, boost::re_detail::regex_data<char, boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, bool) in wallet_rpc_server.cpp.o
      std::__1::__wrap_iter<char const*> boost::re_detail::re_is_set_member<std::__1::__wrap_iter<char const*>, char, boost::regex_traits<char, boost::cpp_regex_traits<char> >, unsigned int>(std::__1::__wrap_iter<char const*>, std::__1::__wrap_iter<char const*>, boost::re_detail::re_set_long<unsigned int> const*, boost::re_detail::regex_data<char, boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, bool) in libcommon.a(util.cpp.o)
      std::__1::__wrap_iter<char const*> boost::re_detail::re_is_set_member<std::__1::__wrap_iter<char const*>, char, boost::regex_traits<char, boost::cpp_regex_traits<char> >, unsigned int>(std::__1::__wrap_iter<char const*>, std::__1::__wrap_iter<char const*>, boost::re_detail::re_set_long<unsigned int> const*, boost::re_detail::regex_data<char, boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, bool) in libwallet.a(wallet2.cpp.o)
      std::__1::__wrap_iter<char const*> boost::re_detail::re_is_set_member<std::__1::__wrap_iter<char const*>, char, boost::regex_traits<char, boost::cpp_regex_traits<char> >, unsigned int>(std::__1::__wrap_iter<char const*>, std::__1::__wrap_iter<char const*>, boost::re_detail::re_set_long<unsigned int> const*, boost::re_detail::regex_data<char, boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, bool) in libcheckpoints.a(checkpoints.cpp.o)
      std::__1::__wrap_iter<char const*> boost::re_detail::re_is_set_member<std::__1::__wrap_iter<char const*>, char, boost::regex_traits<char, boost::cpp_regex_traits<char> >, unsigned int>(std::__1::__wrap_iter<char const*>, std::__1::__wrap_iter<char const*>, boost::re_detail::re_set_long<unsigned int> const*, boost::re_detail::regex_data<char, boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, bool) in libwallet.a(node_rpc_proxy.cpp.o)
      std::__1::__wrap_iter<char const*> boost::re_detail::re_is_set_member<std::__1::__wrap_iter<char const*>, char, boost::regex_traits<char, boost::cpp_regex_traits<char> >, unsigned int>(std::__1::__wrap_iter<char const*>, std::__1::__wrap_iter<char const*>, boost::re_detail::re_set_long<unsigned int> const*, boost::re_detail::regex_data<char, boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, bool) in libcryptonote_basic.a(miner.cpp.o)
  "boost::re_detail::cpp_regex_traits_implementation<char>::transform(char const*, char const*) const", referenced from:
      std::__1::__wrap_iter<char const*> boost::re_detail::re_is_set_member<std::__1::__wrap_iter<char const*>, char, boost::regex_traits<char, boost::cpp_regex_traits<char> >, unsigned int>(std::__1::__wrap_iter<char const*>, std::__1::__wrap_iter<char const*>, boost::re_detail::re_set_long<unsigned int> const*, boost::re_detail::regex_data<char, boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, bool) in wallet_rpc_server.cpp.o
      std::__1::__wrap_iter<char const*> boost::re_detail::re_is_set_member<std::__1::__wrap_iter<char const*>, char, boost::regex_traits<char, boost::cpp_regex_traits<char> >, unsigned int>(std::__1::__wrap_iter<char const*>, std::__1::__wrap_iter<char const*>, boost::re_detail::re_set_long<unsigned int> const*, boost::re_detail::regex_data<char, boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, bool) in libcommon.a(util.cpp.o)
      std::__1::__wrap_iter<char const*> boost::re_detail::re_is_set_member<std::__1::__wrap_iter<char const*>, char, boost::regex_traits<char, boost::cpp_regex_traits<char> >, unsigned int>(std::__1::__wrap_iter<char const*>, std::__1::__wrap_iter<char const*>, boost::re_detail::re_set_long<unsigned int> const*, boost::re_detail::regex_data<char, boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, bool) in libwallet.a(wallet2.cpp.o)
      std::__1::__wrap_iter<char const*> boost::re_detail::re_is_set_member<std::__1::__wrap_iter<char const*>, char, boost::regex_traits<char, boost::cpp_regex_traits<char> >, unsigned int>(std::__1::__wrap_iter<char const*>, std::__1::__wrap_iter<char const*>, boost::re_detail::re_set_long<unsigned int> const*, boost::re_detail::regex_data<char, boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, bool) in libcheckpoints.a(checkpoints.cpp.o)
      std::__1::__wrap_iter<char const*> boost::re_detail::re_is_set_member<std::__1::__wrap_iter<char const*>, char, boost::regex_traits<char, boost::cpp_regex_traits<char> >, unsigned int>(std::__1::__wrap_iter<char const*>, std::__1::__wrap_iter<char const*>, boost::re_detail::re_set_long<unsigned int> const*, boost::re_detail::regex_data<char, boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, bool) in libwallet.a(node_rpc_proxy.cpp.o)
      std::__1::__wrap_iter<char const*> boost::re_detail::re_is_set_member<std::__1::__wrap_iter<char const*>, char, boost::regex_traits<char, boost::cpp_regex_traits<char> >, unsigned int>(std::__1::__wrap_iter<char const*>, std::__1::__wrap_iter<char const*>, boost::re_detail::re_set_long<unsigned int> const*, boost::re_detail::regex_data<char, boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, bool) in libcryptonote_basic.a(miner.cpp.o)
ld: symbol(s) not found for architecture x86_64
clang: error: linker command failed with exit code 1 (use -v to see invocation)
make[3]: *** [bin/monero-wallet-rpc] Error 1
make[2]: *** [src/wallet/CMakeFiles/wallet_rpc_server.dir/all] Error 2
make[1]: *** [all] Error 2
make: *** [release-static-mac-x86_64] Error 2
```

# Discussion History
## moneromooo-monero | 2018-02-27T08:50:30+00:00
might need to link against boost_regex.

## BigslimVdub | 2018-03-25T03:56:11+00:00
fyi I just compiled 11.1.0 just fine with brew, but @sammy007 has not updated yet for 12.0. Also can not get 12.0 to build with High sierra on Cmake.
CMake Warning at /usr/local/Cellar/cmake/3.10.3/share/cmake/Modules/FindBoost.cmake:801 (message):
  New Boost version may have incorrect or missing dependencies and imported
  targets. using boost 1.66.



## hyc | 2018-03-25T07:36:58+00:00
@BigslimVdub that's just a warning and can be ignored. Or you can update your FindBoost module to recognize Boost 1.66 but it doesn't matter either way.

## jonathancross | 2019-04-16T18:04:19+00:00
Has anyone managed to resolve this?  I'm getting the same errors in Mac OS Mojave `10.14.4`.
If not, how are Mac releases being built?

## BigslimVdub | 2019-04-16T18:28:06+00:00
I have compiled the latest 13.0 and 14.0 on high Sierra so it does build. I do not believe Brew has been updated for Mojave and I do not want to upgrade since so many people have had issues building many projects with Mojave. 

## jonathancross | 2019-04-27T11:09:47+00:00
@BigslimVdub Homebrew is working fine for me on Mojave.  Can you please provide some details on your configuration / any tweeks you made?
For example:
`brew list --versions`

## selsta | 2021-08-13T04:25:16+00:00
No reports about issues building on macOS for a while. Closing

# Action History
- Created by: gsovereignty | 2018-02-26T21:02:05+00:00
- Closed at: 2021-08-13T04:25:16+00:00
