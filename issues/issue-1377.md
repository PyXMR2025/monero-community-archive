---
title: 'Segfault :: ../sysdeps/unix/sysv/linux/x86_64/clone.S: No such file or directory'
source_url: https://github.com/monero-project/monero/issues/1377
author: M5M400
assignees: []
labels: []
created_at: '2016-11-25T09:30:55+00:00'
updated_at: '2016-12-15T16:01:43+00:00'
type: issue
status: closed
closed_at: '2016-12-15T16:01:43+00:00'
---

# Original Description
Running dbf2ab5 on node.supportxmr.com

Getting random segfaults after running smoothly for 1-48h. Seems like a boost problem.

Ubuntu 16.04.1 LTS x86_64, boost 1.58.0.1ubuntu1

```
Thread 14 "monerod" received signal SIGSEGV, Segmentation fault.
[Switching to Thread 0x7fffe27fc700 (LWP 1814)]
0x0000000000710328 in nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::for_each_connection(std::function<bool (cryptonote::cryptonote_connection_context&, unsigned long, unsigned int)>) [clone .lto_priv.2964] ()
```

```
#0  0x0000000000710328 in nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::for_each_connection(std::function<bool (cryptonote::cryptonote_connection_context&, unsigned long, unsigned int)>) [clone .lto_priv.2964] ()
#1  0x000000000071374f in cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::relay_block(cryptonote::NOTIFY_NEW_BLOCK::request&, cryptonote::cryptonote_connection_context&) ()
#2  0x0000000000550ba3 in cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::handle_notify_new_block(int, cryptonote::NOTIFY_NEW_BLOCK::request&, cryptonote::cryptonote_connection_context&) ()
#3  0x0000000000746b65 in int nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::handle_invoke_map<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >(bool, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&, bool&) [clone .constprop.455] ()
#4  0x0000000000710b70 in nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::notify(int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&) ()
#5  0x000000000051025c in epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >::handle_recv(void const*, unsigned long) ()
#6  0x00000000005257df in epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::handle_read(boost::system::error_code const&, unsigned long) ()
#7  0x000000000056d126 in boost::asio::detail::completion_handler<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > > >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) ()
#8  0x000000000051c945 in boost::asio::detail::reactive_socket_recv_op<boost::asio::mutable_buffers_1, boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running> >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) ()
#9  0x00000000004aafd9 in boost::asio::detail::epoll_reactor::descriptor_state::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) ()
#10 0x00000000006bc934 in boost::asio::detail::task_io_service::run(boost::system::error_code&) [clone .constprop.1159] ()
#11 0x00000000004d605f in epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread() ()
#12 0x00007ffff5f065d5 in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0
#13 0x00007ffff7bc170a in start_thread (arg=0x7fffe27fc700) at pthread_create.c:333
#14 0x00007ffff78f782d in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109
```

```
#0  0x0000000000710328 in nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::for_each_connection(std::function<bool (cryptonote::cryptonote_connection_context&, unsigned long, unsigned int)>) [clone .lto_priv.2964] ()
(gdb) list
1       ../sysdeps/unix/sysv/linux/x86_64/clone.S: No such file or directory.
```

# Discussion History
## ghost | 2016-11-25T15:16:46+00:00
P2P issue? Which of the pulls merged in the second to last batch fiddled around with TCP/P2P stuff?

## ghost | 2016-12-03T22:25:55+00:00
I can confirm that acf908c "thread_group: fix build with asserts enabled", #1312 is rock steady - just before the first fluffy blocks pull

Been up for 9 days with no crashes, 64+34 connections

## M5M400 | 2016-12-05T10:49:48+00:00
built 45bb393 now on node.supportxmr.com to see if #1389 fixed the issue. will report back

## M5M400 | 2016-12-07T10:24:28+00:00
No crashes in the last 48h. Seems to be OK now!

## M5M400 | 2016-12-09T13:26:18+00:00
4 days, no crash.

## luigi1111 | 2016-12-15T16:01:43+00:00
Fixed by #1389 (reopen if untrue).

# Action History
- Created by: M5M400 | 2016-11-25T09:30:55+00:00
- Closed at: 2016-12-15T16:01:43+00:00
