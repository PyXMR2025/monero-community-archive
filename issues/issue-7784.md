---
title: 'Trezor: exception in wallet crashes monero-wallet-cli'
source_url: https://github.com/monero-project/monero/issues/7784
author: ph4r05
assignees: []
labels: []
created_at: '2021-07-11T18:21:53+00:00'
updated_at: '2021-08-12T02:30:38+00:00'
type: issue
status: closed
closed_at: '2021-08-12T02:30:37+00:00'
---

# Original Description
When monero-wallet-cli is using Trezor connected via Bridge (HTTP communication protocol) and the wallet fails with an exception, wallet crashes with the following dump use-after-free on Linux (dump below).

How to reproduce:
- Restore wallet from Trezor HW device
- Enter passphrase (PC or Trezor, does not matter)
- Confirm view-only credentials export on Trezor
- After wallet asks `Is this okay?  (Y/Yes/N/No):`, type "N"
- wallet crashes

Alternatively: create atexit handler triggering http get, call http get (to init regex after atexit), let test crash on atexit handler. 

From the dump it is obvious that wallet crashes during `atexit()` from: 
https://github.com/monero-project/monero/blob/de3456e1275836725291ba71036b7ef0e2cda91f/src/device/device.cpp#L63

As devices are destroyed, living connection to Trezor via Bridge is being closed. For that to happen, Bridge transport needs to send HTTP request. This request fails.

Failing to properly close Trezor device causes Trezor cannot be normally used after the crash as session is kept by the crashed wallet. Bridge has to be restarted, which causes problems for beginners (Trezor reconnect may help).

My hypothesis is that there is a race between `atexit` and static regex destructor as [this post indicates](https://community.ibm.com/community/user/ibmz-and-linuxone/blogs/fang-lu2/2020/03/24/be-careful-when-using-the-atexit-routine-with-static-objects?lang=en). [This SO](https://stackoverflow.com/questions/16010083/order-between-destruction-of-global-object-and-atexit-in-c) is also related. 

It seems that regex is lazily initialized when firstly used here: https://github.com/monero-project/monero/blob/de3456e1275836725291ba71036b7ef0e2cda91f/contrib/epee/include/net/http_client.h#L757

As `atexit` is called before this regex initialization, the regex is probably destructed sooner than `atexit` function is called (my hypothesis). Claim from the crash `previously allocated by thread T0 here:` seems to support this idea.

## Proposed solution
Add account deinit to wallet destructor https://github.com/monero-project/monero/blob/de3456e1275836725291ba71036b7ef0e2cda91f/src/wallet/wallet2.cpp#L1214-L1216

```cpp
wallet2::~wallet2()
{
    m_account.deinit();
}
```

This causes existing devices to properly disconnect. I've tested this on Trezor and it fixes this issue. 

## Dump & info
```
Generated new wallet on hw device: 4BBKEeg8iH3JtyQKfdh5KRYNe2WK4aDMBeMwPvkjrm45BQ8bVHurmLyadDx3EiM6AjNH7JJx5TMNrjC4JLZEhszc5f3G8Yg
No restore height is specified. Assumed you are creating a new account, restore will be done from current estimated blockchain height. Use --restore-height or --restore-date if you want to restore an already setup account from a specific height.
Is this okay?  (Y/Yes/N/No): n
=================================================================
==3156==ERROR: AddressSanitizer: heap-use-after-free on address 0x614000003468 at pc 0x55e6ddb86530 bp 0x7fff139fe4d0 sp 0x7fff139fe4c0
READ of size 4 at 0x614000003468 thread T0
    #0 0x55e6ddb8652f in bool boost::regex_search<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > >, char, boost::regex_traits<char, boost::cpp_regex_traits<char> > >(__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, __gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, boost::match_results<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > > >&, boost::basic_regex<char, boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, boost::regex_constants::_match_flags, __gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >) (/home/ph4r05/Desktop/monero-wallet-cli-linux4+0x18ae52f)
    #1 0x55e6ddb86d9c in bool boost::regex_search<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > >, char, boost::regex_traits<char, boost::cpp_regex_traits<char> > >(__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, __gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, boost::match_results<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > > >&, boost::basic_regex<char, boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, boost::regex_constants::_match_flags) /usr/include/boost/regex/v4/regex_search.hpp:42
    #2 0x55e6ddb871e2 in bool boost::regex_search<std::char_traits<char>, std::allocator<char>, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > >, char, boost::regex_traits<char, boost::cpp_regex_traits<char> > >(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, boost::match_results<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >::const_iterator, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > > >&, boost::basic_regex<char, boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, boost::regex_constants::_match_flags) /usr/include/boost/regex/v4/regex_search.hpp:81
    #3 0x55e6ddb871e2 in epee::net_utils::http::http_simple_client_template<epee::net_utils::blocked_mode_client>::set_reply_content_encoder() /root/monero2/contrib/epee/include/net/http_client.h:759
    #4 0x55e6ddb8ac7f in epee::net_utils::http::http_simple_client_template<epee::net_utils::blocked_mode_client>::analize_cached_header_and_invoke_state() /root/monero2/contrib/epee/include/net/http_client.h:786
    #5 0x55e6ddb8eb50 in epee::net_utils::http::http_simple_client_template<epee::net_utils::blocked_mode_client>::handle_header(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&, bool&) /root/monero2/contrib/epee/include/net/http_client.h:423
    #6 0x55e6ddb8fb45 in epee::net_utils::http::http_simple_client_template<epee::net_utils::blocked_mode_client>::handle_reciev(std::chrono::duration<long, std::ratio<1l, 1000l> >) /root/monero2/contrib/epee/include/net/http_client.h:368
    #7 0x55e6ddb94720 in epee::net_utils::http::http_simple_client_template<epee::net_utils::blocked_mode_client>::invoke(boost::basic_string_ref<char, std::char_traits<char> >, boost::basic_string_ref<char, std::char_traits<char> >, boost::basic_string_ref<char, std::char_traits<char> >, std::chrono::duration<long, std::ratio<1l, 1000l> >, epee::net_utils::http::http_response_info const**, std::__cxx11::list<std::pair<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::allocator<std::pair<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > > const&) /root/monero2/contrib/epee/include/net/http_client.h:282
    #8 0x55e6ddb204b3 in bool hw::trezor::invoke_bridge_http<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, rapidjson::GenericDocument<rapidjson::UTF8<char>, rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator>, rapidjson::CrtAllocator>, epee::net_utils::http::http_simple_client_template<epee::net_utils::blocked_mode_client> >(boost::basic_string_ref<char, std::char_traits<char> >, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, rapidjson::GenericDocument<rapidjson::UTF8<char>, rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator>, rapidjson::CrtAllocator>&, epee::net_utils::http::http_simple_client_template<epee::net_utils::blocked_mode_client>&, boost::basic_string_ref<char, std::char_traits<char> >, std::chrono::duration<long, std::ratio<1l, 1000l> >) /root/monero2/src/device_trezor/trezor/transport.hpp:96
    #9 0x55e6ddaaf55a in hw::trezor::BridgeTransport::close() /root/monero2/src/device_trezor/trezor/transport.cpp:436
    #10 0x55e6ddb9abad in hw::trezor::device_trezor_base::disconnect() /root/monero2/src/device_trezor/device_trezor_base.cpp:161
    #11 0x55e6dd8fda07 in hw::trezor::device_trezor::disconnect() /root/monero2/src/device_trezor/device_trezor.cpp:103
    #12 0x55e6dd8fdafb in hw::trezor::device_trezor::~device_trezor() /root/monero2/src/device_trezor/device_trezor.cpp:69
    #13 0x55e6dd8fe120 in hw::trezor::device_trezor::~device_trezor() /root/monero2/src/device_trezor/device_trezor.cpp:74
    #14 0x55e6ddf144de in std::default_delete<hw::device>::operator()(hw::device*) const /usr/include/c++/9/bits/unique_ptr.h:81
    #15 0x55e6ddf144de in std::unique_ptr<hw::device, std::default_delete<hw::device> >::~unique_ptr() /usr/include/c++/9/bits/unique_ptr.h:292
    #16 0x55e6ddf144de in std::pair<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const, std::unique_ptr<hw::device, std::default_delete<hw::device> > >::~pair() /usr/include/c++/9/bits/stl_pair.h:208
    #17 0x55e6ddf144de in void __gnu_cxx::new_allocator<std::_Rb_tree_node<std::pair<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const, std::unique_ptr<hw::device, std::default_delete<hw::device> > > > >::destroy<std::pair<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const, std::unique_ptr<hw::device, std::default_delete<hw::device> > > >(std::pair<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const, std::unique_ptr<hw::device, std::default_delete<hw::device> > >*) /usr/include/c++/9/ext/new_allocator.h:153
    #18 0x55e6ddf144de in void std::allocator_traits<std::allocator<std::_Rb_tree_node<std::pair<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const, std::unique_ptr<hw::device, std::default_delete<hw::device> > > > > >::destroy<std::pair<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const, std::unique_ptr<hw::device, std::default_delete<hw::device> > > >(std::allocator<std::_Rb_tree_node<std::pair<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const, std::unique_ptr<hw::device, std::default_delete<hw::device> > > > >&, std::pair<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const, std::unique_ptr<hw::device, std::default_delete<hw::device> > >*) /usr/include/c++/9/bits/alloc_traits.h:497
    #19 0x55e6ddf144de in std::_Rb_tree<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::pair<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const, std::unique_ptr<hw::device, std::default_delete<hw::device> > >, std::_Select1st<std::pair<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const, std::unique_ptr<hw::device, std::default_delete<hw::device> > > >, std::less<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::allocator<std::pair<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const, std::unique_ptr<hw::device, std::default_delete<hw::device> > > > >::_M_destroy_node(std::_Rb_tree_node<std::pair<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const, std::unique_ptr<hw::device, std::default_delete<hw::device> > > >*) /usr/include/c++/9/bits/stl_tree.h:642
    #20 0x55e6ddf144de in std::_Rb_tree<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::pair<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const, std::unique_ptr<hw::device, std::default_delete<hw::device> > >, std::_Select1st<std::pair<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const, std::unique_ptr<hw::device, std::default_delete<hw::device> > > >, std::less<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::allocator<std::pair<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const, std::unique_ptr<hw::device, std::default_delete<hw::device> > > > >::_M_drop_node(std::_Rb_tree_node<std::pair<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const, std::unique_ptr<hw::device, std::default_delete<hw::device> > > >*) /usr/include/c++/9/bits/stl_tree.h:650
    #21 0x55e6ddf144de in std::_Rb_tree<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::pair<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const, std::unique_ptr<hw::device, std::default_delete<hw::device> > >, std::_Select1st<std::pair<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const, std::unique_ptr<hw::device, std::default_delete<hw::device> > > >, std::less<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::allocator<std::pair<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const, std::unique_ptr<hw::device, std::default_delete<hw::device> > > > >::_M_erase(std::_Rb_tree_node<std::pair<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const, std::unique_ptr<hw::device, std::default_delete<hw::device> > > >*) /usr/include/c++/9/bits/stl_tree.h:1915
    #22 0x55e6ddf11d4b in std::_Rb_tree<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::pair<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const, std::unique_ptr<hw::device, std::default_delete<hw::device> > >, std::_Select1st<std::pair<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const, std::unique_ptr<hw::device, std::default_delete<hw::device> > > >, std::less<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::allocator<std::pair<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const, std::unique_ptr<hw::device, std::default_delete<hw::device> > > > >::~_Rb_tree() /usr/include/c++/9/bits/stl_tree.h:995
    #23 0x55e6ddf11d4b in std::map<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::unique_ptr<hw::device, std::default_delete<hw::device> >, std::less<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::allocator<std::pair<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const, std::unique_ptr<hw::device, std::default_delete<hw::device> > > > >::~map() /usr/include/c++/9/bits/stl_map.h:300
    #24 0x55e6ddf11d4b in hw::device_registry::~device_registry() /root/monero2/src/device/device.hpp:258
    #25 0x55e6ddf11d4b in get_device_registry /root/monero2/src/device/device.cpp:48
    #26 0x55e6ddf11def in clear_device_registry /root/monero2/src/device/device.cpp:55
    #27 0x7f72ddfb6a26  (/lib/x86_64-linux-gnu/libc.so.6+0x49a26)
    #28 0x7f72ddfb6bdf in exit (/lib/x86_64-linux-gnu/libc.so.6+0x49bdf)
    #29 0x7f72ddf940b9 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x270b9)
    #30 0x55e6dc79d1ed in _start (/home/ph4r05/Desktop/monero-wallet-cli-linux4+0x4c51ed)

0x614000003468 is located 40 bytes inside of 408-byte region [0x614000003440,0x6140000035d8)
freed by thread T0 here:
    #0 0x7f72de415025 in operator delete(void*, unsigned long) (/lib/x86_64-linux-gnu/libasan.so.5+0x111025)
    #1 0x55e6dc9e78b9 in boost::detail::sp_counted_base::release() /usr/include/boost/smart_ptr/detail/sp_counted_base_std_atomic.hpp:112
    #2 0x55e6ddacfce3 in boost::detail::shared_count::~shared_count() /usr/include/boost/smart_ptr/detail/shared_count.hpp:427
    #3 0x55e6ddacfce3 in boost::shared_ptr<boost::re_detail_107100::basic_regex_implementation<char, boost::regex_traits<char, boost::cpp_regex_traits<char> > > >::~shared_ptr() /usr/include/boost/smart_ptr/shared_ptr.hpp:341
    #4 0x55e6ddacfce3 in boost::basic_regex<char, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::~basic_regex() /usr/include/boost/regex/v4/basic_regex.hpp:353
    #5 0x7f72ddfb6a26  (/lib/x86_64-linux-gnu/libc.so.6+0x49a26)

previously allocated by thread T0 here:
    #0 0x7f72de413947 in operator new(unsigned long) (/lib/x86_64-linux-gnu/libasan.so.5+0x10f947)
    #1 0x55e6de7e843c in boost::basic_regex<char, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::do_assign(char const*, char const*, unsigned int) (/home/ph4r05/Desktop/monero-wallet-cli-linux4+0x251043c)
    #2 0x55e6ddb8ac7f in epee::net_utils::http::http_simple_client_template<epee::net_utils::blocked_mode_client>::analize_cached_header_and_invoke_state() /root/monero2/contrib/epee/include/net/http_client.h:786
    #3 0x55e6ddb8eb50 in epee::net_utils::http::http_simple_client_template<epee::net_utils::blocked_mode_client>::handle_header(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&, bool&) /root/monero2/contrib/epee/include/net/http_client.h:423
    #4 0x55e6ddb8fb45 in epee::net_utils::http::http_simple_client_template<epee::net_utils::blocked_mode_client>::handle_reciev(std::chrono::duration<long, std::ratio<1l, 1000l> >) /root/monero2/contrib/epee/include/net/http_client.h:368
    #5 0x55e6ddb94720 in epee::net_utils::http::http_simple_client_template<epee::net_utils::blocked_mode_client>::invoke(boost::basic_string_ref<char, std::char_traits<char> >, boost::basic_string_ref<char, std::char_traits<char> >, boost::basic_string_ref<char, std::char_traits<char> >, std::chrono::duration<long, std::ratio<1l, 1000l> >, epee::net_utils::http::http_response_info const**, std::__cxx11::list<std::pair<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::allocator<std::pair<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > > const&) /root/monero2/contrib/epee/include/net/http_client.h:282
    #6 0x55e6ddb204b3 in bool hw::trezor::invoke_bridge_http<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, rapidjson::GenericDocument<rapidjson::UTF8<char>, rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator>, rapidjson::CrtAllocator>, epee::net_utils::http::http_simple_client_template<epee::net_utils::blocked_mode_client> >(boost::basic_string_ref<char, std::char_traits<char> >, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, rapidjson::GenericDocument<rapidjson::UTF8<char>, rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator>, rapidjson::CrtAllocator>&, epee::net_utils::http::http_simple_client_template<epee::net_utils::blocked_mode_client>&, boost::basic_string_ref<char, std::char_traits<char> >, std::chrono::duration<long, std::ratio<1l, 1000l> >) /root/monero2/src/device_trezor/trezor/transport.hpp:96
    #7 0x55e6ddab3ddc in hw::trezor::BridgeTransport::enumerate(std::vector<std::shared_ptr<hw::trezor::Transport>, std::allocator<std::shared_ptr<hw::trezor::Transport> > >&) /root/monero2/src/device_trezor/trezor/transport.cpp:370
    #8 0x55e6ddabb20a in hw::trezor::enumerate(std::vector<std::shared_ptr<hw::trezor::Transport>, std::allocator<std::shared_ptr<hw::trezor::Transport> > >&) /root/monero2/src/device_trezor/trezor/transport.cpp:1172
    #9 0x55e6ddba3805 in hw::trezor::device_trezor_base::connect() /root/monero2/src/device_trezor/device_trezor_base.cpp:119
    #10 0x55e6dde170b3 in cryptonote::account_base::create_from_device(hw::device&) /root/monero2/src/cryptonote_basic/account.cpp:218
    #11 0x55e6dce78602 in tools::wallet2::restore(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, epee::wipeable_string const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, bool) /root/monero2/src/wallet/wallet2.cpp:4923

    #12 0x55e6dc85d8bf in cryptonote::simple_wallet::new_wallet(boost::program_options::variables_map const&) /root/monero2/src/simplewallet/simplewallet.cpp:5091
    #13 0x55e6dc978ffe in cryptonote::simple_wallet::init(boost::program_options::variables_map const&) /root/monero2/src/simplewallet/simplewallet.cpp:4586
    #14 0x55e6dc983366 in main /root/monero2/src/simplewallet/simplewallet.cpp:10646
    #15 0x7f72ddf940b2 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x270b2)

SUMMARY: AddressSanitizer: heap-use-after-free (/home/ph4r05/Desktop/monero-wallet-cli-linux4+0x18ae52f) in bool boost::regex_search<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > >, char, boost::regex_traits<char, boost::cpp_regex_traits<char> > >(__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, __gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, boost::match_results<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::alloca
Shadow bytes around the buggy address:
  0x0c287fff8630: fd fd fd fd fd fd fd fd fd fd fa fa fa fa fa fa
  0x0c287fff8640: fa fa fa fa fa fa fa fa 00 00 00 00 00 00 00 00
  0x0c287fff8650: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c287fff8660: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c287fff8670: 00 00 00 00 00 00 00 00 00 fa fa fa fa fa fa fa
=>0x0c287fff8680: fa fa fa fa fa fa fa fa fd fd fd fd fd[fd]fd fd
  0x0c287fff8690: fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd
  0x0c287fff86a0: fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd
  0x0c287fff86b0: fd fd fd fd fd fd fd fd fd fd fd fa fa fa fa fa
  0x0c287fff86c0: fa fa fa fa fa fa fa fa fd fd fd fd fd fd fd fd
  0x0c287fff86d0: fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd
Shadow byte legend (one shadow byte represents 8 application bytes):
  Addressable:           00
  Partially addressable: 01 02 03 04 05 06 07 
  Heap left redzone:       fa
  Freed heap region:       fd
  Stack left redzone:      f1
  Stack mid redzone:       f2
  Stack right redzone:     f3
  Stack after return:      f5
  Stack use after scope:   f8
  Global redzone:          f9
  Global init order:       f6
  Poisoned by user:        f7
  Container overflow:      fc
  Array cookie:            ac
  Intra object redzone:    bb
  ASan internal:           fe
  Left alloca redzone:     ca
  Right alloca redzone:    cb
  Shadow gap:              cc
==3156==ABORTING
``` 

Env:
- CMake version 3.16.3
- Found Boost Version: 107100
- gcc:

```
COLLECT_GCC=gcc
COLLECT_LTO_WRAPPER=/usr/lib/gcc/x86_64-linux-gnu/9/lto-wrapper
OFFLOAD_TARGET_NAMES=nvptx-none:hsa
OFFLOAD_TARGET_DEFAULT=1
Target: x86_64-linux-gnu
Configured with: ../src/configure -v --with-pkgversion='Ubuntu 9.3.0-10ubuntu2' --with-bugurl=file:///usr/share/doc/gcc-9/README.Bugs --enable-languages=c,ada,c++,go,brig,d,fortran,objc,obj-c++,gm2 --prefix=/usr --with-gcc-major-version-only --program-suffix=-9 --program-prefix=x86_64-linux-gnu- --enable-shared --enable-linker-build-id --libexecdir=/usr/lib --without-included-gettext --enable-threads=posix --libdir=/usr/lib --enable-nls --enable-clocale=gnu --enable-libstdcxx-debug --enable-libstdcxx-time=yes --with-default-libstdcxx-abi=new --enable-gnu-unique-object --disable-vtable-verify --enable-plugin --enable-default-pie --with-system-zlib --with-target-system-zlib=auto --enable-objc-gc=auto --enable-multiarch --disable-werror --with-arch-32=i686 --with-abi=m64 --with-multilib-list=m32,m64,mx32 --enable-multilib --with-tune=generic --enable-offload-targets=nvptx-none,hsa --without-cuda-driver --enable-checking=release --build=x86_64-linux-gnu --host=x86_64-linux-gnu --target=x86_64-linux-gnu
Thread model: posix
gcc version 9.3.0 (Ubuntu 9.3.0-10ubuntu2) 
```

# Discussion History
## moneromooo-monero | 2021-07-14T08:27:54+00:00
Looks like m_account.deinit is already called in wallet2::deinit. Since wallet2::deinit also cleans up other things, it looks like that call is missing from the caller. Calling it from the dtor might be ok, if a check for m_is_initialized is added.

## ph4r05 | 2021-07-14T08:48:54+00:00
@moneromooo-monero thanks for feedback, I've modified PR #7786 to reflect this. 

One more thing though - should we return bool from `wallet2::deinit()` based on `m_is_initialized`? For now, we always return true and return value is not used anywhere. 

## moneromooo-monero | 2021-07-14T10:18:38+00:00
If you want to do anything with that return value, sure.

## ph4r05 | 2021-07-14T10:21:08+00:00
> If you want to do anything with that return value, sure.

I am not using it, so the code can stay as it is I guess.

# Action History
- Created by: ph4r05 | 2021-07-11T18:21:53+00:00
- Closed at: 2021-08-12T02:30:37+00:00
