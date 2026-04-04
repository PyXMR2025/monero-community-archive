---
title: http_simple_client disconnect deadlock
source_url: https://github.com/monero-project/monero/issues/5397
author: ph4r05
assignees: []
labels: []
created_at: '2019-04-04T01:54:54+00:00'
updated_at: '2022-05-25T21:27:35+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
The `epee::net_utils::http::http_simple_client` with SSL enabled, used with RPC daemon cannot disconnect. It freezes on `m_http_client.disconnect()` call.

The trace from gdb when execution is interrupted:

```lldb
#0  0x00007ffff226d10f in epoll_wait (epfd=42, events=0x7fffffff9370, maxevents=128, timeout=-1) at ../sysdeps/unix/sysv/linux/epoll_wait.c:30
#1  0x0000555555d3522c in boost::asio::detail::epoll_reactor::run (this=0x5555567895c0, usec=-1, ops=...) at /usr/local/include/boost/asio/detail/impl/epoll_reactor.ipp:471
#2  0x0000555555d34d0a in boost::asio::detail::scheduler::do_run_one (this=0x555556516950, lock=..., this_thread=..., ec=...) at /usr/local/include/boost/asio/detail/impl/scheduler.ipp:385
#3  0x0000555555d348ae in boost::asio::detail::scheduler::run_one (this=0x555556516950, ec=...) at /usr/local/include/boost/asio/detail/impl/scheduler.ipp:175
#4  0x0000555555d26d33 in boost::asio::io_context::run_one (this=0x5555564572b0) at /usr/local/include/boost/asio/impl/io_context.ipp:77
#5  0x0000555555d2446b in epee::net_utils::blocked_mode_client::shutdown_ssl (this=0x5555564572b0) at /root/monero-tests/contrib/epee/include/net/net_helper.h:620
#6  0x0000555555ed6a86 in epee::net_utils::blocked_mode_client::disconnect (this=0x5555564572b0) at /root/monero-tests/contrib/epee/include/net/net_helper.h:264
#7  0x0000555555d1f0a8 in epee::net_utils::http::http_simple_client_template<epee::net_utils::blocked_mode_client>::disconnect (this=0x5555564572a8)
    at /root/monero-tests/contrib/epee/include/net/http_client.h:346
#8  0x0000555555d06175 in mock_daemon::~mock_daemon (this=0x555556456460) at /root/monero-tests/tests/trezor/daemon.cpp:105
```

I use it in `mock_deamon` in `trezor_tests`. Previously, the mock_daemon together with http_client was deinitialized, now it freezes. It may be the commit 7acfa9f3cc7b52c0f4776dde3c3f80674cc3306f

@vtnerd Do you have an idea why `m_io_service.run_one();` freezes now? I am a bit stuck on this.

I am using this branch: https://github.com/ph4r05/monero/tree/coverity_scan  

Can you pls reproduce this? If not I can make a simple PoC target with http client connecting to RPC over SSL. 

Thanks!

# Discussion History
## moneromooo-monero | 2019-04-04T10:01:33+00:00
Try removing:
    if (m_ssl_support == epee::net_utils::ssl_support_t::e_ssl_support_enabled)
      socket_.shutdown(ignored_ec);
in:
  template<class t_protocol_handler>
  bool connection<t_protocol_handler>::shutdown()



## ph4r05 | 2019-04-04T11:40:06+00:00
If I setup client with `e_ssl_support_disabled` it works fine.

However I am trying to reproduce it against my local RPC server and I am getting another error (OSX, fe3403c8f01e1b8207b4cb8f085c809c7a8e1a1d):

```
2019-04-04 11:18:40.350	[RPC1]	ERROR	net.ssl	contrib/epee/src/net_ssl.cpp:297	handshake failed, connection dropped: no shared cipher
2019-04-04 11:18:40.350	[RPC1]	ERROR	net	contrib/epee/include/net/abstract_tcp_server2.inl:458	SSL handshake failed
```

Linux behaves differently, the same commit manages to finish the handshake (maybe ossl issue).

## moneromooo-monero | 2019-04-04T12:09:47+00:00
Are both sides using monero code ?

## ph4r05 | 2019-04-04T13:22:44+00:00
> Are both sides using monero code ?

Yes, I tried it also with mock_daemon - starts RPC in a separate thread, thus the same code.

https://github.com/ph4r05/monero/blob/73aa3842036a2c844d067024df9ecd5093342970/tests/trezor/http_client.cpp#L80

I cannot reproduce this on Linux. It still may be just an environment glitch.

## moneromooo-monero | 2019-04-04T13:28:26+00:00
It might be that your openssl version is somehow built without any of the ciphers monero whitelists.
See net_ssl.cpp for the list.

## ph4r05 | 2019-04-04T13:30:22+00:00
Anyway, I cannot reproduce the deadlock with simple isolated example. It may be something more complex after long course of interaction (like Wallet::API signature). So I close this until somebody can reproduce. 

## ph4r05 | 2019-04-04T14:29:27+00:00
Hmm I can reproduce it in trezor_tests if client uses `ssl_autodetect`:

```lldb
* thread #1, name = 'trezor_tests', stop reason = signal SIGSTOP
  * frame #0: 0x00007ffff226d10f libc.so.6`epoll_wait(epfd=36, events=0x00007fffffff93c0, maxevents=128, timeout=-1) at epoll_wait.c:30
    frame #1: 0x0000555555d3526c trezor_tests`boost::asio::detail::epoll_reactor::run(this=0x000055555652c700, usec=-1, ops=0x00007fffffff9b20) at epoll_reactor.ipp:471
    frame #2: 0x0000555555d34d4a trezor_tests`boost::asio::detail::scheduler::do_run_one(this=0x000055555644a600, lock=0x00007fffffff9b00, this_thread=0x00007fffffff9b10, ec=0x00007fffffff9b78) at scheduler.ipp:385
    frame #3: 0x0000555555d348ee trezor_tests`boost::asio::detail::scheduler::run_one(this=0x000055555644a600, ec=0x00007fffffff9b78) at scheduler.ipp:175
    frame #4: 0x0000555555d26d73 trezor_tests`boost::asio::io_context::run_one(this=0x00005555567884d0) at io_context.ipp:77
    frame #5: 0x0000555555d244ab trezor_tests`epee::net_utils::blocked_mode_client::shutdown_ssl(this=0x00005555567884d0) at net_helper.h:620
    frame #6: 0x0000555555ed6ac6 trezor_tests`epee::net_utils::blocked_mode_client::disconnect(this=0x00005555567884d0) at net_helper.h:264
    frame #7: 0x0000555555d1f0e8 trezor_tests`epee::net_utils::http::http_simple_client_template<epee::net_utils::blocked_mode_client>::disconnect(this=0x00005555567884c8) at http_client.h:346
    frame #8: 0x0000555555d06996 trezor_tests`mock_daemon::deinit(this=0x0000555556787680) at daemon.cpp:146
    frame #9: 0x0000555555d08126 trezor_tests`mock_daemon::stop_and_deinit(this=0x0000555556787680) at daemon.cpp:191
    frame #10: 0x0000555555ef9824 trezor_tests`main(argc=3, argv=0x00007fffffffe518) at trezor_tests.cpp:163
    frame #11: 0x00007ffff217609b libc.so.6`__libc_start_main(main=(trezor_tests`main at trezor_tests.cpp:93), argc=3, argv=0x00007fffffffe518, init=<unavailable>, fini=<unavailable>, rtld_fini=<unavailable>, stack_end=0x00007fffffffe508) at libc-start.c:308
    frame #12: 0x0000555555cf236a trezor_tests`_start + 42
```

## ph4r05 | 2019-04-04T17:12:41+00:00
OK reopening. I managed to isolate the issue. It may be some race condition or I am just doing something wrong.

Commit 34d0e788b01e7f7d74c2866d670e03d36e198dac 

Reproduce:

```
make -j3 debug-test-trezor
lldb ./build/Linux/coverity_scan/debug/tests/trezor/http_client_tests 
(lldb) target create "./build/Linux/coverity_scan/debug/tests/trezor/http_client_tests"
Current executable set to './build/Linux/coverity_scan/debug/tests/trezor/http_client_tests' (x86_64).
run
Process 24664 launched: '/root/monero-tests/build/Linux/coverity_scan/debug/tests/trezor/http_client_tests' (x86_64)
Running main() from gtest_main.cc
[==========] Running 1 test from 1 test case.
[----------] Global test environment set-up.
[----------] 1 test from HTTP_Simple_Client
[ RUN      ] HTTP_Simple_Client.GetHeight
2019-04-04 16:54:19.745	    7fffef33ac40	INFO	net	contrib/epee/include/net/abstract_tcp_server2.inl:1034	Set server type to: 1 from name: RPC, prefix_name = RPC
2019-04-04 16:54:19.748	    7fffef33ac40	INFO	global	contrib/epee/include/net/http_server_impl_base.h:82	Binding on 127.0.0.1:61341
2019-04-04 16:54:19.748	    7fffef33ac40	INFO	global	contrib/epee/src/net_ssl.cpp:75	Generating SSL certificate
2019-04-04 16:54:20.557	    7fffef33ac40	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:962	start accept
2019-04-04 16:54:20.558	    7fffef33ac40	DEBUG	net.conn	contrib/epee/src/connection_basic.cpp:144	Spawned connection #0 to 0.0.0.0 currently we have sockets count:1
2019-04-04 16:54:20.558	    7fffef33ac40	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:107	test, connection constructor set m_connection_type=1
2019-04-04 16:54:20.567	    7fffef32f700	INFO	net.http	contrib/epee/include/net/http_server_impl_base.h:95	Run net_service loop( 2 threads)...
2019-04-04 16:54:20.572	    7fffef33ac40	INFO	global	contrib/epee/src/net_ssl.cpp:75	Generating SSL certificate
2019-04-04 16:54:20.574	[SRV_MAIN]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:1060	Run server thread name: RPC
2019-04-04 16:54:20.574	[SRV_MAIN]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:1060	Run server thread name: RPC
2019-04-04 16:54:20.575	[SRV_MAIN]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:1077	Reiniting OK.
error: ld-2.28.so 0xffffffff0005f117: adding range [0x14167-0x141ca) which has a base that is less than the function's low PC 0x148c0. Please file a bug and attach the file at the start of this error message
error: ld-2.28.so 0xffffffff0005f117: adding range [0x141e0-0x141e6) which has a base that is less than the function's low PC 0x148c0. Please file a bug and attach the file at the start of this error message
error: ld-2.28.so 0xffffffff0005f184: adding range [0x14167-0x141ca) which has a base that is less than the function's low PC 0x148c0. Please file a bug and attach the file at the start of this error message
error: ld-2.28.so 0xffffffff0005f184: adding range [0x141e0-0x141e6) which has a base that is less than the function's low PC 0x148c0. Please file a bug and attach the file at the start of this error message
2019-04-04 16:54:22.949	    7fffef33ac40	DEBUG	net.http	contrib/epee/include/net/http_client.h:381	Reconnecting...
2019-04-04 16:54:22.965	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:1151	handle_accept
2019-04-04 16:54:22.968	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:1164	New server for RPC connections, SSL autodetection
2019-04-04 16:54:22.968	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:880	set m_connection_type = RPC 
2019-04-04 16:54:22.968	[RPC0]	DEBUG	net.conn	contrib/epee/src/connection_basic.cpp:144	Spawned connection #1 to 0.0.0.0 currently we have sockets count:2
2019-04-04 16:54:22.968	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:107	test, connection constructor set m_connection_type=1
2019-04-04 16:54:22.970	[RPC1]	DEBUG	net.ssl	contrib/epee/src/net_ssl.cpp:196	SSL detection buffer, 144 bytes: 22 3 1 0 139 1 0 0 135
2019-04-04 16:54:22.970	[RPC1]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:443	That looks like SSL
2019-04-04 16:54:22.983	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:316	 connection type RPC 127.0.0.1:61341 <--> 127.0.0.1:57724 (via 127.0.0.1:57724)
2019-04-04 16:54:23.010	[RPC1]	DEBUG	net.ssl	contrib/epee/src/net_ssl.cpp:305	SSL handshake success
2019-04-04 16:54:23.016	    7fffef33ac40	DEBUG	net.ssl	contrib/epee/src/net_ssl.cpp:305	SSL handshake success


Process 24664 stopped
* thread #1, name = 'http_client_tes', stop reason = signal SIGSTOP
    frame #0: 0x00007ffff267310f libc.so.6`epoll_wait(epfd=17, events=0x00007fffffff6d70, maxevents=128, timeout=-1) at epoll_wait.c:30
(lldb) bt
* thread #1, name = 'http_client_tes', stop reason = signal SIGSTOP
  * frame #0: 0x00007ffff267310f libc.so.6`epoll_wait(epfd=17, events=0x00007fffffff6d70, maxevents=128, timeout=-1) at epoll_wait.c:30
    frame #1: 0x0000555555a3c84c http_client_tests`boost::asio::detail::epoll_reactor::run(this=0x0000555555f9fad0, usec=-1, ops=0x00007fffffff74d0) at epoll_reactor.ipp:471
    frame #2: 0x0000555555a3c32a http_client_tests`boost::asio::detail::scheduler::do_run_one(this=0x0000555555ed49e0, lock=0x00007fffffff74b0, this_thread=0x00007fffffff74c0, ec=0x00007fffffff7528) at scheduler.ipp:385
    frame #3: 0x0000555555a3bece http_client_tests`boost::asio::detail::scheduler::run_one(this=0x0000555555ed49e0, ec=0x00007fffffff7528) at scheduler.ipp:175
    frame #4: 0x0000555555a2e353 http_client_tests`boost::asio::io_context::run_one(this=0x00007fffffffc7a8) at io_context.ipp:77
    frame #5: 0x0000555555bf2262 http_client_tests`epee::net_utils::blocked_mode_client::recv(this=0x00007fffffffc7a8, buff="h\xa5???, timeout=(__r = 60000)) at net_helper.h:437
    frame #6: 0x0000555555be93b3 http_client_tests`epee::net_utils::http::http_simple_client_template<epee::net_utils::blocked_mode_client>::handle_reciev(this=0x00007fffffffc7a0, timeout=(__r = 60000)) at http_client.h:470
    frame #7: 0x0000555555be7fb3 http_client_tests`epee::net_utils::http::http_simple_client_template<epee::net_utils::blocked_mode_client>::invoke(this=0x00007fffffffc7a0, uri=(ptr_ = "/json_rpc", len_ = 9), method=(ptr_ = "GET", len_ = 3), body="??UUU"..., timeout=(__r = 60000), ppresponse_info=0x00007fffffffb040, additional_params=size=1) at http_client.h:417
    frame #8: 0x0000555555c1b02f http_client_tests`bool epee::net_utils::invoke_http_json<epee::json_rpc::request<epee::misc_utils::struct_init<cryptonote::COMMAND_RPC_GET_VERSION::request_t> >, epee::json_rpc::response<epee::misc_utils::struct_init<cryptonote::COMMAND_RPC_GET_VERSION::response_t>, epee::json_rpc::error>, epee::net_utils::http::http_simple_client_template<epee::net_utils::blocked_mode_client> >(uri=(ptr_ = "/json_rpc", len_ = 9), out_struct=0x00007fffffffb5f8, result_struct=0x00007fffffffb440, transport=0x00007fffffffc7a0, timeout=(__r = 60000), method=(ptr_ = "GET", len_ = 3)) at http_abstract_invoke.h:51
    frame #9: 0x0000555555c1a5f3 http_client_tests`bool epee::net_utils::invoke_http_json_rpc<epee::misc_utils::struct_init<cryptonote::COMMAND_RPC_GET_VERSION::request_t>, epee::misc_utils::struct_init<cryptonote::COMMAND_RPC_GET_VERSION::response_t>, epee::net_utils::http::http_simple_client_template<epee::net_utils::blocked_mode_client> >(uri=(ptr_ = "/json_rpc", len_ = 9), method_name="", out_struct=0x00007fffffffba40, result_struct=0x00007fffffffc010, transport=0x00007fffffffc7a0, timeout=(__r = 60000), http_method=(ptr_ = "GET", len_ = 3), req_id="\xb8\xbf???) at http_abstract_invoke.h:112
    frame #10: 0x0000555555c013e2 http_client_tests`get_version(m_http_client=0x00007fffffffc7a0) at http_client.cpp:63
    frame #11: 0x0000555555c00f10 http_client_tests`HTTP_Simple_Client_GetHeight_Test::TestBody(this=0x0000555555ea96c0) at http_client.cpp:111
```

Interestingly, when the `get_version` function body is unrolled in the place of the call the bug does not manifest itself.



## moneromooo-monero | 2019-04-12T18:14:43+00:00
Does https://github.com/monero-project/monero/pull/5432 help ?

## ph4r05 | 2019-04-12T18:22:05+00:00
This looks quite promising! I will give it a try soon.

## ph4r05 | 2019-04-15T15:02:04+00:00
Hmm I've got deadlock in reading now :/ 
I will double-check if I can reproduce it well also on Trezor tests where the problem manifested originally

```lldb
* thread #1, name = 'http_client_tes', stop reason = signal SIGSTOP
  * frame #0: 0x00007ffff268410f libc.so.6`epoll_wait(epfd=17, events=0x00007fffffff6820, maxevents=128, timeout=-1) at epoll_wait.c:30
    frame #1: 0x0000555555a3c98c http_client_tests`boost::asio::detail::epoll_reactor::run(this=0x0000555555fa9a00, usec=-1, ops=0x00007fffffff6f80) at epoll_reactor.ipp:471
    frame #2: 0x0000555555a3c46a http_client_tests`boost::asio::detail::scheduler::do_run_one(this=0x0000555555ed79e0, lock=0x00007fffffff6f60, this_thread=0x00007fffffff6f70, ec=0x00007fffffff6fd8) at scheduler.ipp:385
    frame #3: 0x0000555555a3c00e http_client_tests`boost::asio::detail::scheduler::run_one(this=0x0000555555ed79e0, ec=0x00007fffffff6fd8) at scheduler.ipp:175
    frame #4: 0x0000555555a2e493 http_client_tests`boost::asio::io_context::run_one(this=0x00007fffffffc260) at io_context.ipp:77
    frame #5: 0x0000555555befc62 http_client_tests`epee::net_utils::blocked_mode_client::recv(this=0x00007fffffffc260, buff="(\xa0���, timeout=(__r = 60000)) at net_helper.h:439
    frame #6: 0x0000555555be6f13 http_client_tests`epee::net_utils::http::http_simple_client_template<epee::net_utils::blocked_mode_client>::handle_reciev(this=0x00007fffffffc258, timeout=(__r = 60000)) at http_client.h:469
    frame #7: 0x0000555555be5ae3 http_client_tests`epee::net_utils::http::http_simple_client_template<epee::net_utils::blocked_mode_client>::invoke(this=0x00007fffffffc258, uri=(ptr_ = "/json_rpc", len_ = 9), method=(ptr_ = "GET", len_ = 3), body="���UUU"..., timeout=(__r = 60000), ppresponse_info=0x00007fffffffab00, additional_params=size=1) at http_client.h:406
    frame #8: 0x0000555555c1895f http_client_tests`bool epee::net_utils::invoke_http_json<epee::json_rpc::request<epee::misc_utils::struct_init<cryptonote::COMMAND_RPC_GET_VERSION::request_t> >, epee::json_rpc::response<epee::misc_utils::struct_init<cryptonote::COMMAND_RPC_GET_VERSION::response_t>, epee::json_rpc::error>, epee::net_utils::http::http_simple_client_template<epee::net_utils::blocked_mode_client> >(uri=(ptr_ = "/json_rpc", len_ = 9), out_struct=0x00007fffffffb0b8, result_struct=0x00007fffffffaf00, transport=0x00007fffffffc258, timeout=(__r = 60000), method=(ptr_ = "GET", len_ = 3)) at http_abstract_invoke.h:51
    frame #9: 0x0000555555c17f23 http_client_tests`bool epee::net_utils::invoke_http_json_rpc<epee::misc_utils::struct_init<cryptonote::COMMAND_RPC_GET_VERSION::request_t>, epee::misc_utils::struct_init<cryptonote::COMMAND_RPC_GET_VERSION::response_t>, epee::net_utils::http::http_simple_client_template<epee::net_utils::blocked_mode_client> >(uri=(ptr_ = "/json_rpc", len_ = 9), method_name="", out_struct=0x00007fffffffb500, result_struct=0x00007fffffffbad0, transport=0x00007fffffffc258, timeout=(__r = 60000), http_method=(ptr_ = "GET", len_ = 3), req_id="x\xba���) at http_abstract_invoke.h:112
    frame #10: 0x0000555555bfed72 http_client_tests`get_version(m_http_client=0x00007fffffffc258) at http_client.cpp:63
    frame #11: 0x0000555555bfe8a6 http_client_tests`HTTP_Simple_Client_GetHeight_Test::TestBody(this=0x0000555555eac6c0) at http_client.cpp:111
    frame #12: 0x0000555555d0745e http_client_tests`void testing::internal::HandleSehExceptionsInMethodIfSupported<testing::Test, void>(testing::Test*, void (testing::Test::*)(), char const*) + 126
    frame #13: 0x0000555555cf51bb http_client_tests`void testing::internal::HandleExceptionsInMethodIfSupported<testing::Test, void>(testing::Test*, void (testing::Test::*)(), char const*) + 123
    frame #14: 0x0000555555cdc646 http_client_tests`testing::Test::Run() + 198
    frame #15: 0x0000555555cdd376 http_client_tests`testing::TestInfo::Run() + 230
    frame #16: 0x0000555555cdda3f http_client_tests`testing::TestCase::Run() + 239
    frame #17: 0x0000555555ce50ee http_client_tests`testing::internal::UnitTestImpl::RunAllTests() + 734
    frame #18: 0x0000555555d0a0fe http_client_tests`bool testing::internal::HandleSehExceptionsInMethodIfSupported<testing::internal::UnitTestImpl, bool>(testing::internal::UnitTestImpl*, bool (testing::internal::UnitTestImpl::*)(), char const*) + 126
    frame #19: 0x0000555555cf741b http_client_tests`bool testing::internal::HandleExceptionsInMethodIfSupported<testing::internal::UnitTestImpl, bool>(testing::internal::UnitTestImpl*, bool (testing::internal::UnitTestImpl::*)(), char const*) + 123
    frame #20: 0x0000555555ce4dc3 http_client_tests`testing::UnitTest::Run() + 211
    frame #21: 0x0000555555d0e081 http_client_tests`RUN_ALL_TESTS() + 17
    frame #22: 0x0000555555d0e069 http_client_tests`main + 57
    frame #23: 0x00007ffff258d09b libc.so.6`__libc_start_main(main=(http_client_tests`main), argc=1, argv=0x00007fffffffdfc8, init=<unavailable>, fini=<unavailable>, rtld_fini=<unavailable>, stack_end=0x00007fffffffdfb8) at libc-start.c:308
    frame #24: 0x00005555559f9a4a http_client_tests`_start + 42
```

## ph4r05 | 2019-04-15T15:09:00+00:00
Trezor tests cannot shutdown ssl :/ 

```lldb
* thread #1, name = 'trezor_tests', stop reason = signal SIGSTOP
  * frame #0: 0x00007ffff228910f libc.so.6`epoll_wait(epfd=36, events=0x00007fffffff7360, maxevents=128, timeout=-1) at epoll_wait.c:30
    frame #1: 0x0000555555d3c39c trezor_tests`boost::asio::detail::epoll_reactor::run(this=0x00005555566871c0, usec=-1, ops=0x00007fffffff7ac0) at epoll_reactor.ipp:471
    frame #2: 0x0000555555d3be7a trezor_tests`boost::asio::detail::scheduler::do_run_one(this=0x00005555565ebdc0, lock=0x00007fffffff7aa0, this_thread=0x00007fffffff7ab0, ec=0x00007fffffff7b18) at scheduler.ipp:385
    frame #3: 0x0000555555d3ba1e trezor_tests`boost::asio::detail::scheduler::run_one(this=0x00005555565ebdc0, ec=0x00007fffffff7b18) at scheduler.ipp:175
    frame #4: 0x0000555555d2dea3 trezor_tests`boost::asio::io_context::run_one(this=0x000055555679ebb0) at io_context.ipp:77
    frame #5: 0x0000555555d2b5db trezor_tests`epee::net_utils::blocked_mode_client::shutdown_ssl(this=0x000055555679ebb0) at net_helper.h:634
    frame #6: 0x0000555555edd072 trezor_tests`epee::net_utils::blocked_mode_client::disconnect(this=0x000055555679ebb0) at net_helper.h:264
    frame #7: 0x0000555555d26148 trezor_tests`epee::net_utils::http::http_simple_client_template<epee::net_utils::blocked_mode_client>::disconnect(this=0x000055555679eba8) at http_client.h:335
    frame #8: 0x0000555555d0da86 trezor_tests`mock_daemon::deinit(this=0x000055555679ddf0) at daemon.cpp:146
    frame #9: 0x0000555555d0f186 trezor_tests`mock_daemon::stop_and_deinit(this=0x000055555679ddf0) at daemon.cpp:191
    frame #10: 0x0000555555efe465 trezor_tests`main(argc=3, argv=0x00007fffffffdfa8) at trezor_tests.cpp:164
    frame #11: 0x00007ffff219209b libc.so.6`__libc_start_main(main=(trezor_tests`main at trezor_tests.cpp:93), argc=3, argv=0x00007fffffffdfa8, init=<unavailable>, fini=<unavailable>, rtld_fini=<unavailable>, stack_end=0x00007fffffffdf98) at libc-start.c:308
    frame #12: 0x0000555555cf945a trezor_tests`_start + 42
```


## moneromooo-monero | 2019-04-15T16:13:55+00:00
Do you have a custom io service ? If so, it is stopped before that ?

## ph4r05 | 2019-04-22T15:12:09+00:00
I am using `epee::net_utils::http::http_simple_client`, so I think there is no custom IO service.

## moneromooo-monero | 2019-09-02T11:22:16+00:00
Did you work it out in the end ?

## moneromooo-monero | 2020-05-16T16:28:20+00:00
ping

## selsta | 2022-04-08T16:33:17+00:00
@ph4r05 I tried to test https://github.com/monero-project/monero/commit/34d0e788b01e7f7d74c2866d670e03d36e198dac but wasn't able to find the `http_client_tests` binary, I have to spend more time on it to debug the CMake code.

I'm interested to know if this issue is fixed, and if not if #7760 fixes it, as it has some fixes regarding SSL shutdown.

## ph4r05 | 2022-04-12T20:24:07+00:00
@selsta ah sorry, I missed the message. The binary is in Trezor tests folder, not the best location, I admit 😅

Trezor tests need to be built.

## selsta | 2022-04-18T22:18:31+00:00
@ph4r05

```
OPTION(USE_DEVICE_TREZOR "Trezor support compilation" ON)
OPTION(USE_DEVICE_TREZOR_LIBUSB "Trezor LibUSB compilation" ON)
OPTION(USE_DEVICE_TREZOR_UDP_RELEASE "Trezor UdpTransport in release mode" OFF)
OPTION(USE_DEVICE_TREZOR_DEBUG "Trezor Debugging enabled" OFF)
OPTION(TREZOR_DEBUG "Main trezor debugging switch" OFF)
```

That's the only options I found. Did I miss something? Where to I find trezor tests.


`git grep -i "trezor_tests"` also did not find anything interesting.


## ph4r05 | 2022-05-25T11:47:21+00:00
ah, sorry @selsta, I keep forgetting on this one. 

I use the following Makefile goals to build Trezor tests

```
debug-test-trezor:
        mkdir -p $(builddir)/debug
        cd $(builddir)/debug && cmake -D BUILD_TESTS=ON -D TREZOR_DEBUG=ON -D CMAKE_BUILD_TYPE=Debug $(topdir) &&  $(MAKE) && $(MAKE) ARGS="-E libwallet_api_tests"
```


## selsta | 2022-05-25T21:26:49+00:00
@ph4r05 Thanks, that worked. Do I need some extra setup to get past `SSL certificate is not in the allowed list, connection dropped`?
```
selsta@mbp ~/d/m/b/D/h/d/t/trezor (http_simple_client_deadlock)> ./http_client_tests
Running main() from gtest_main.cc
[==========] Running 1 test from 1 test case.
[----------] Global test environment set-up.
[----------] 1 test from HTTP_Simple_Client
[ RUN      ] HTTP_Simple_Client.GetHeight
2022-05-25 21:18:46.598	I Set server type to: 1 from name: RPC, prefix_name = RPC
2022-05-25 21:18:46.599	I Binding on 127.0.0.1 (IPv4):61341
2022-05-25 21:18:46.634	D start accept (IPv4)
2022-05-25 21:18:46.634	D Spawned connection #0 to 0.0.0.0 currently we have sockets count:1
2022-05-25 21:18:46.634	D test, connection constructor set m_connection_type=1
2022-05-25 21:18:46.634	I [PARSE URI] regex not matched for uri: ^(([^:]*?)://)?(\[(.*)\](:(\d+))?)(.*)?
2022-05-25 21:18:46.635	I Run net_service loop( 2 threads)...
2022-05-25 21:18:46.635	D Run server thread name: RPC
2022-05-25 21:18:46.635	D Run server thread name: RPC
2022-05-25 21:18:46.635	D Reiniting OK.
2022-05-25 21:18:46.636	I [PARSE URI] regex not matched for uri: ^(([^:]*?)://)?(\[(.*)\](:(\d+))?)(.*)?
2022-05-25 21:18:46.671	I Generating SSL certificate
2022-05-25 21:18:48.205	D Reconnecting...
2022-05-25 21:18:48.205	D handle_accept
2022-05-25 21:18:48.205	D New server for RPC connections, SSL autodetection
2022-05-25 21:18:48.205	D set m_connection_type = RPC 
2022-05-25 21:18:48.206	D Spawned connection #1 to 0.0.0.0 currently we have sockets count:2
2022-05-25 21:18:48.206	D test, connection constructor set m_connection_type=1
2022-05-25 21:18:48.206	D  connection type RPC 127.0.0.1:61341 <--> 127.0.0.1:62502 (via 127.0.0.1:62502)
2022-05-25 21:18:48.206	D SSL detection buffer, 517 bytes: 22 3 1 2 0 1 0 1 252
2022-05-25 21:18:48.206	D That looks like SSL
2022-05-25 21:18:48.340	E SSL certificate is not in the allowed list, connection dropped
2022-05-25 21:18:48.347	E SSL handshake failed, connection dropped: tlsv1 alert unknown ca (SSL routines)
2022-05-25 21:18:48.347	E SSL handshake failed
2022-05-25 21:18:48.347	D Destructing connection #0 to 0.0.0.0
2022-05-25 21:18:48.375	E SSL handshake failed, connection dropped: unregistered scheme (STORE routines)
2022-05-25 21:18:48.375	W Failed to establish SSL connection
2022-05-25 21:18:48.375	D Failed to connect to 127.0.0.1:61341
2022-05-25 21:18:48.375	I Failed to invoke http request to  /json_rpc
2022-05-25 21:18:48.375	E Version: RPC error - Get version
2022-05-25 21:18:48.375	I 
2022-05-25 21:18:48.375	D Problems at ssl shutdown: shutdown while in init (SSL routines)
2022-05-25 21:18:48.376	D Problems at shutdown: Socket is not connected
2022-05-25 21:18:48.400	D Problems at cancel: Bad file descriptor
2022-05-25 21:18:48.400	D Problems at shutdown: Bad file descriptor
2022-05-25 21:18:48.400	D Destructing connection #1 to 0.0.0.0
unknown file: Failure
C++ exception with description "RPC error - Get version" thrown in the test body.
[  FAILED  ] HTTP_Simple_Client.GetHeight (1807 ms)
[----------] 1 test from HTTP_Simple_Client (1807 ms total)

[----------] Global test environment tear-down
[==========] 1 test from 1 test case ran. (1807 ms total)
[  PASSED  ] 0 tests.
[  FAILED  ] 1 test, listed below:
[  FAILED  ] HTTP_Simple_Client.GetHeight

 1 FAILED TEST
```

# Action History
- Created by: ph4r05 | 2019-04-04T01:54:54+00:00
