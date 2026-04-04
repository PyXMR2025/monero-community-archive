---
title: monerod sync stuck sometimes.
source_url: https://github.com/monero-project/monero/issues/2795
author: miningpoolhub
assignees: []
labels: []
created_at: '2017-11-12T01:18:32+00:00'
updated_at: '2018-06-10T09:48:52+00:00'
type: issue
status: closed
closed_at: '2018-06-10T09:48:52+00:00'
---

# Original Description
I submitted same issue before and it was closed.
https://github.com/monero-project/monero/issues/2649

It stuck again. I'm running 0.11.1.0 Helium Hydra Point Release 1.
I did not run with --log-level 1, so there's no log data to show currently.

I just want to reopen this case. and check if I'm the only one experiencing the issue.
I'm currently running more than +10 monero server instances and only one stuck.
It runs fine when I just restart it.

# Discussion History
## moneromooo-monero | 2017-11-12T08:18:48+00:00
If you just say "it's stuck sometimes", it just doesn't help, and isn't going to get fixed.
So either you supply a level 1 log as I asked in that other bug, or this gets closed again <s>in 24 hours.</s> ok, that's a bit too soon, but seriously, just saying it ain't working without logs showing what it's doing is pointless.


## miningpoolhub | 2017-11-13T06:27:28+00:00
I'm currently running 16 monerod instances with `--log-level 1` from several servers.
Please don't close this issue, I'm trying to gather information to analyze.

## moneromooo-monero | 2017-11-13T08:58:25+00:00
OK, thank you. I'm fine waiting if I know you're trying to get some info :)


## moneromooo-monero | 2017-11-13T16:49:38+00:00
Just in case, when it gets stuck like that, get a full thread stack trace:
```
gdb /path/to.monerod `pidof monerod`
thread apply all bt
```

Replace /path/to/monerod with the actual path first.


## miningpoolhub | 2017-11-14T02:13:34+00:00
@moneromoo-monero OK. Thanks.

## assylias | 2017-11-15T12:32:52+00:00
@moneromooo-monero Hi there - I'm facing the same issue: the blockchain on one of my computers was about 40 days behind - when I run the daemon (v11.0.1.0) it syncs 5000 to 10000 blocks then stops syncing although it's not done yet. `monerod status` looks normal apart from the fact that the chain is behind and not syncing.

When I kill the daemon and restart it the syncing process starts normally.

Full stack trace (will post level 1 logs if/when the issue happens again):

```
Thread 18 (Thread 0x7f8b1a052700 (LWP 11131)):
#0  pthread_cond_timedwait@@GLIBC_2.3.2 () at ../sysdeps/unix/sysv/linux/x86_64/pthread_cond_timedwait.S:225
#1  0x0000000000989e9c in boost::this_thread::hiden::sleep_for(timespec const&) ()
#2  0x0000000000715fd2 in cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::request_missing_objects(cryptonote::cryptonote_connection_context&, bool, bool) ()
#3  0x000000000071d8c0 in cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::handle_response_chain_entry(int, cryptonote::NOTIFY_RESPONSE_CHAIN_ENTRY::request&, cryptonote::cryptonote_connection_context&) ()
#4  0x0000000000704ca7 in int epee::net_utils::buff_to_t_adapter<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, cryptonote::NOTIFY_RESPONSE_CHAIN_ENTRY::request, cryptonote::cryptonote_connection_context, boost::_bi::bind_t<int, boost::_mfi::mf3<int, cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, int, cryptonote::NOTIFY_RESPONSE_CHAIN_ENTRY::request&, cryptonote::cryptonote_connection_context&>, boost::_bi::list4<boost::_bi::value<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*>, boost::arg<1>, boost::arg<2>, boost::arg<3> > > >(cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, boost::_bi::bind_t<int, boost::_mfi::mf3<int, cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, int, cryptonote::NOTIFY_RESPONSE_CHAIN_ENTRY::request&, cryptonote::cryptonote_connection_context&>, boost::_bi::list4<boost::_bi::value<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*>, boost::arg<1>, boost::arg<2>, boost::arg<3> > >, cryptonote::cryptonote_connection_context&) ()
#5  0x000000000070c381 in int cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::handle_invoke_map<cryptonote::cryptonote_connection_context>(bool, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&, cryptonote::cryptonote_connection_context&, bool&) ()
#6  0x000000000070c7ce in int nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::handle_invoke_map<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >(bool, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&, bool&) ()
#7  0x000000000070cbdf in nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::notify(int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&) ()
#8  0x000000000070d0b0 in epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >::handle_recv(void const*, unsigned long) ()
#9  0x0000000000724cea in epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::handle_read(boost::system::error_code const&, unsigned long) ()
#10 0x00000000006cc391 in void boost::asio::detail::strand_service::dispatch<boost::asio::detail::binder2<boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::system::error_code, unsigned long> >(boost::asio::detail::strand_service::strand_impl*&, boost::asio::detail::binder2<boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::system::error_code, unsigned long>&) ()
#11 0x00000000006cc7c9 in boost::asio::detail::completion_handler<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > > >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) ()
#12 0x00000000006ccb8a in void boost::asio::detail::strand_service::dispatch<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > > >(boost::asio::detail::strand_service::strand_impl*&, boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost:---Type <return> to continue, or q <return> to quit---
:asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > >&) ()
#13 0x00000000006cce43 in boost::asio::detail::reactive_socket_recv_op<boost::asio::mutable_buffers_1, boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running> >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) ()
#14 0x0000000000649d1c in boost::asio::detail::epoll_reactor::descriptor_state::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) ()
#15 0x000000000066a7f7 in epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread() ()
#16 0x0000000000988fa5 in thread_proxy ()
#17 0x00007f8b25300494 in start_thread (arg=0x7f8b1a052700) at pthread_create.c:333
#18 0x00007f8b25042aff in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:97

Thread 17 (Thread 0x7f8b1b0fc700 (LWP 11130)):
#0  pthread_cond_timedwait@@GLIBC_2.3.2 () at ../sysdeps/unix/sysv/linux/x86_64/pthread_cond_timedwait.S:225
#1  0x0000000000989e9c in boost::this_thread::hiden::sleep_for(timespec const&) ()
#2  0x0000000000715fd2 in cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::request_missing_objects(cryptonote::cryptonote_connection_context&, bool, bool) ()
#3  0x000000000071d8c0 in cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::handle_response_chain_entry(int, cryptonote::NOTIFY_RESPONSE_CHAIN_ENTRY::request&, cryptonote::cryptonote_connection_context&) ()
#4  0x0000000000704ca7 in int epee::net_utils::buff_to_t_adapter<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, cryptonote::NOTIFY_RESPONSE_CHAIN_ENTRY::request, cryptonote::cryptonote_connection_context, boost::_bi::bind_t<int, boost::_mfi::mf3<int, cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, int, cryptonote::NOTIFY_RESPONSE_CHAIN_ENTRY::request&, cryptonote::cryptonote_connection_context&>, boost::_bi::list4<boost::_bi::value<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*>, boost::arg<1>, boost::arg<2>, boost::arg<3> > > >(cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, boost::_bi::bind_t<int, boost::_mfi::mf3<int, cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, int, cryptonote::NOTIFY_RESPONSE_CHAIN_ENTRY::request&, cryptonote::cryptonote_connection_context&>, boost::_bi::list4<boost::_bi::value<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*>, boost::arg<1>, boost::arg<2>, boost::arg<3> > >, cryptonote::cryptonote_connection_context&) ()
#5  0x000000000070c381 in int cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::handle_invoke_map<cryptonote::cryptonote_connection_context>(bool, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&, cryptonote::cryptonote_connection_context&, bool&) ()
#6  0x000000000070c7ce in int nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::handle_invoke_map<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >(bool, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&, bool&) ()
#7  0x000000000070cbdf in nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::notify(int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&) ()
#8  0x000000000070d0b0 in epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >::handle_recv(void const*, unsigned long) ()
#9  0x0000000000724cea in epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::handle_read(boost::system::error_code const&, unsigned long) ()
#10 0x00000000006cc391 in void boost::asio::detail::strand_service::dispatch<boost::asio::detail::binder2<boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::system::error_code, unsigned long> >(boost::asio::detail::strand_service::strand_impl*&, boost::asio::detail::binder2<boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::system::error_code, unsigned long>&) ()
#11 0x00000000006cc7c9 in boost::asio::detail::completion_handler<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > > >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) ()
#12 0x00000000006ccb8a in void boost::asio::detail::strand_service::dispatch<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > > >(boost::asio::detail::strand_service::strand_impl*&, boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > >&) ()
#13 0x00000000006cce43 in boost::asio::detail::reactive_socket_recv_op<boost::asio::mutable_buffers_1, boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running> >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) ()
#14 0x000000000066a7f7 in epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread() ()
#15 0x0000000000988fa5 in thread_proxy ()
#16 0x00007f8b25300494 in start_thread (arg=0x7f8b1b0fc700) at pthread_create.c:333
#17 0x00007f8b25042aff in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:97

Thread 16 (Thread 0x7f8b1b5fd700 (LWP 11129)):
#0  pthread_cond_timedwait@@GLIBC_2.3.2 () at ../sysdeps/unix/sysv/linux/x86_64/pthread_cond_timedwait.S:225
#1  0x0000000000989e9c in boost::this_thread::hiden::sleep_for(timespec const&) ()
#2  0x0000000000715fd2 in cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::request_missing_objects(cryptonote::cryptonote_connection_context&, bool, bool) ()
#3  0x0000000000719a2e in cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::try_add_next_blocks(cryptonote::cryptonote_connection_context&) ()
#4  0x000000000071cd2b in cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::handle_response_get_objects(int, cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request&, cryptonote::cryptonote_connection_context&) ()
#5  0x000000000070c1da in int epee::net_utils::buff_to_t_adapter<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request, cryptonote::cryptonote_connection_context, boost::_bi::bind_t<int, boost::_mfi::mf3<int, cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, int, cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request&, cryptonote::cryptonote_connection_context&>, boost::_bi::list4<boost::_bi::value<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*>, boost::arg<1>, boost::arg<2>, boost::arg<3> > > >(cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, boost::_bi::bind_t<int, boost::_mfi::mf3<int, cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, int, cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request&, cryptonote::cryptonote_connection_context&>, boost::_bi::list4<boost::_bi::value<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*>, boost::arg<1>, boost::arg<2>, boost::arg<3> > >, cryptonote::cryptonote_connection_context&) ()
#6  0x000000000070c4d3 in int cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::handle_invoke_map<cryptonote::cryptonote_connection_context>(bool, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&, cryptonote::cryptonote_connection_context&, bool&) ()
#7  0x000000000070c7ce in int nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::handle_invoke_map<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >(bool, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&, bool&) ()
#8  0x000000000070cbdf in nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::notify(int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&) ()
#9  0x000000000070d0b0 in epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >::handle_recv(void const*, unsigned long) ()
#10 0x0000000000724cea in epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::handle_read(boost::system::error_code const&, unsigned long) ()
#11 0x00000000006cc391 in void boost::asio::detail::strand_service::dispatch<boost::asio::detail::binder2<boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::system::error_code, unsigned long> >(boost::asio::detail::strand_service::strand_impl*&, boost::asio::detail::binder2<boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::system::error_code, unsigned long>&) ()
#12 0x00000000006cc7c9 in boost::asio::detail::completion_handler<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > > >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) ()
#13 0x00000000006ccb8a in void boost::asio::detail::strand_service::dispatch<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::crypton---Type <return> to continue, or q <return> to quit---
ote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > > >(boost::asio::detail::strand_service::strand_impl*&, boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > >&) ()
#14 0x00000000006cce43 in boost::asio::detail::reactive_socket_recv_op<boost::asio::mutable_buffers_1, boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running> >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) ()
#15 0x0000000000649d1c in boost::asio::detail::epoll_reactor::descriptor_state::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) ()
#16 0x000000000066a7f7 in epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread() ()
#17 0x0000000000988fa5 in thread_proxy ()
#18 0x00007f8b25300494 in start_thread (arg=0x7f8b1b5fd700) at pthread_create.c:333
#19 0x00007f8b25042aff in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:97

Thread 15 (Thread 0x7f8b1bafe700 (LWP 11128)):
#0  pthread_cond_timedwait@@GLIBC_2.3.2 () at ../sysdeps/unix/sysv/linux/x86_64/pthread_cond_timedwait.S:225
#1  0x0000000000989e9c in boost::this_thread::hiden::sleep_for(timespec const&) ()
#2  0x0000000000715fd2 in cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::request_missing_objects(cryptonote::cryptonote_connection_context&, bool, bool) ()
#3  0x0000000000719a2e in cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::try_add_next_blocks(cryptonote::cryptonote_connection_context&) ()
#4  0x000000000071cd2b in cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::handle_response_get_objects(int, cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request&, cryptonote::cryptonote_connection_context&) ()
#5  0x000000000070c1da in int epee::net_utils::buff_to_t_adapter<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request, cryptonote::cryptonote_connection_context, boost::_bi::bind_t<int, boost::_mfi::mf3<int, cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, int, cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request&, cryptonote::cryptonote_connection_context&>, boost::_bi::list4<boost::_bi::value<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*>, boost::arg<1>, boost::arg<2>, boost::arg<3> > > >(cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, boost::_bi::bind_t<int, boost::_mfi::mf3<int, cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, int, cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request&, cryptonote::cryptonote_connection_context&>, boost::_bi::list4<boost::_bi::value<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*>, boost::arg<1>, boost::arg<2>, boost::arg<3> > >, cryptonote::cryptonote_connection_context&) ()
#6  0x000000000070c4d3 in int cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::handle_invoke_map<cryptonote::cryptonote_connection_context>(bool, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&, cryptonote::cryptonote_connection_context&, bool&) ()
#7  0x000000000070c7ce in int nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::handle_invoke_map<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >(bool, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&, bool&) ()
#8  0x000000000070cbdf in nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::notify(int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&) ()
#9  0x000000000070d0b0 in epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >::handle_recv(void const*, unsigned long) ()
#10 0x0000000000724cea in epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::handle_read(boost::system::error_code const&, unsigned long) ()
#11 0x00000000006cc391 in void boost::asio::detail::strand_service::dispatch<boost::asio::detail::binder2<boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::system::error_code, unsigned long> >(boost::asio::detail::strand_service::strand_impl*&, boost::asio::detail::binder2<boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::system::error_code, unsigned long>&) ()
#12 0x00000000006cc7c9 in boost::asio::detail::completion_handler<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > > >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) ()
#13 0x00000000006ccb8a in void boost::asio::detail::strand_service::dispatch<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > > >(boost::asio::detail::strand_service::strand_impl*&, boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > >&) ()
#14 0x00000000006cce43 in boost::asio::detail::reactive_socket_recv_op<boost::asio::mutable_buffers_1, boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running> >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) ()
#15 0x0000000000649d1c in boost::asio::detail::epoll_reactor::descriptor_state::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) ()
#16 0x000000000066a7f7 in epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread() ()
#17 0x0000000000988fa5 in thread_proxy ()
#18 0x00007f8b25300494 in start_thread (arg=0x7f8b1bafe700) at pthread_create.c:333
#19 0x00007f8b25042aff in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:97

Thread 14 (Thread 0x7f8b1bfff700 (LWP 11127)):
#0  pthread_cond_timedwait@@GLIBC_2.3.2 () at ../sysdeps/unix/sysv/linux/x86_64/pthread_cond_timedwait.S:225
#1  0x0000000000989e9c in boost::this_thread::hiden::sleep_for(timespec const&) ()
#2  0x0000000000715fd2 in cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::request_missing_objects(cryptonote::cryptonote_connection_context&, bool, bool) ()
#3  0x0000000000719a2e in cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::try_add_next_blocks(cryptonote::cryptonote_connection_context&) ()
#4  0x000000000071cd2b in cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::handle_response_get_objects(int, cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request&, cryptonote::cryptonote_connection_context&) ()
#5  0x000000000070c1da in int epee::net_utils::buff_to_t_adapter<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request, cryptonote::cryptonote_connection_context, boost::_bi::bind_t<int, boost::_mfi::mf3<int, cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, int, cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request&, cryptonote::cryptonote_connection_context&>, boost::_bi::list4<boost::_bi::value<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*>, boost::arg<1>, boost::arg<2>, boost::arg<3> > > >(cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, boost::_bi::bind_t<int, boost::_mfi::mf3<int, cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, int, cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request&, cryptonote::cryptonote_connection_context&>, boost::_bi::list4<boost::_bi::value<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*>, boost::arg<1>, boost::arg<2>, boost::arg<3> > >, cryptonote::cryptonote_connection_context&) ()
#6  0x000000000070c4d3 in int cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::handle_invoke_map<cryptonote::cryptonote_connection_context>(bool, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&, cryptonote::cryptonote_connection_context&, bool&) ()
#7  0x000000000070c7ce in int nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::handle_invoke_map<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >(bool, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&, bool&) ()
#8  0x000000000070cbdf in nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::notify(int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&) ()
#9  0x000000000070d0b0 in epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >::handle_recv(void const*, unsigned long) ()
#10 0x0000000000724cea in epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::handle_read(boost::system::error_code const&, unsigned long) ()
#11 0x00000000006cc391 in void boost::asio::detail::strand_service::dispatch<boost::asio::detail::binder2<boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::system::error_code, unsigned long> >(boost::asio::detail::strand_service::strand_impl*&, boost::asio::detail::binder2<boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::system::error_code, unsigned long>&) ()
#12 0x00000000006cc7c9 in boost::asio::detail::completion_handler<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > > >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) ()
#13 0x00000000006ccb8a in void boost::asio::detail::strand_service::dispatch<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi---Type <return> to continue, or q <return> to quit---
::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > > >(boost::asio::detail::strand_service::strand_impl*&, boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > >&) ()
#14 0x00000000006cce43 in boost::asio::detail::reactive_socket_recv_op<boost::asio::mutable_buffers_1, boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running> >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) ()
#15 0x0000000000649d1c in boost::asio::detail::epoll_reactor::descriptor_state::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) ()
#16 0x000000000066a7f7 in epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread() ()
#17 0x0000000000988fa5 in thread_proxy ()
#18 0x00007f8b25300494 in start_thread (arg=0x7f8b1bfff700) at pthread_create.c:333
#19 0x00007f8b25042aff in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:97

Thread 13 (Thread 0x7f8b20735700 (LWP 11126)):
#0  pthread_cond_timedwait@@GLIBC_2.3.2 () at ../sysdeps/unix/sysv/linux/x86_64/pthread_cond_timedwait.S:225
#1  0x0000000000989e9c in boost::this_thread::hiden::sleep_for(timespec const&) ()
#2  0x0000000000715fd2 in cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::request_missing_objects(cryptonote::cryptonote_connection_context&, bool, bool) ()
#3  0x000000000071d8c0 in cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::handle_response_chain_entry(int, cryptonote::NOTIFY_RESPONSE_CHAIN_ENTRY::request&, cryptonote::cryptonote_connection_context&) ()
#4  0x0000000000704ca7 in int epee::net_utils::buff_to_t_adapter<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, cryptonote::NOTIFY_RESPONSE_CHAIN_ENTRY::request, cryptonote::cryptonote_connection_context, boost::_bi::bind_t<int, boost::_mfi::mf3<int, cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, int, cryptonote::NOTIFY_RESPONSE_CHAIN_ENTRY::request&, cryptonote::cryptonote_connection_context&>, boost::_bi::list4<boost::_bi::value<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*>, boost::arg<1>, boost::arg<2>, boost::arg<3> > > >(cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, boost::_bi::bind_t<int, boost::_mfi::mf3<int, cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, int, cryptonote::NOTIFY_RESPONSE_CHAIN_ENTRY::request&, cryptonote::cryptonote_connection_context&>, boost::_bi::list4<boost::_bi::value<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*>, boost::arg<1>, boost::arg<2>, boost::arg<3> > >, cryptonote::cryptonote_connection_context&) ()
#5  0x000000000070c381 in int cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::handle_invoke_map<cryptonote::cryptonote_connection_context>(bool, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&, cryptonote::cryptonote_connection_context&, bool&) ()
#6  0x000000000070c7ce in int nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::handle_invoke_map<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >(bool, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&, bool&) ()
#7  0x000000000070cbdf in nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::notify(int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&) ()
#8  0x000000000070d0b0 in epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >::handle_recv(void const*, unsigned long) ()
#9  0x0000000000724cea in epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::handle_read(boost::system::error_code const&, unsigned long) ()
#10 0x00000000006cc391 in void boost::asio::detail::strand_service::dispatch<boost::asio::detail::binder2<boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::system::error_code, unsigned long> >(boost::asio::detail::strand_service::strand_impl*&, boost::asio::detail::binder2<boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::system::error_code, unsigned long>&) ()
#11 0x00000000006cc7c9 in boost::asio::detail::completion_handler<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > > >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) ()
#12 0x00000000006ccb8a in void boost::asio::detail::strand_service::dispatch<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > > >(boost::asio::detail::strand_service::strand_impl*&, boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > >&) ()
#13 0x00000000006cce43 in boost::asio::detail::reactive_socket_recv_op<boost::asio::mutable_buffers_1, boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running> >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) ()
#14 0x0000000000649d1c in boost::asio::detail::epoll_reactor::descriptor_state::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) ()
#15 0x000000000066a7f7 in epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread() ()
#16 0x0000000000988fa5 in thread_proxy ()
#17 0x00007f8b25300494 in start_thread (arg=0x7f8b20735700) at pthread_create.c:333
#18 0x00007f8b25042aff in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:97

Thread 12 (Thread 0x7f8b20c36700 (LWP 11125)):
#0  pthread_cond_timedwait@@GLIBC_2.3.2 () at ../sysdeps/unix/sysv/linux/x86_64/pthread_cond_timedwait.S:225
#1  0x0000000000989e9c in boost::this_thread::hiden::sleep_for(timespec const&) ()
#2  0x0000000000715fd2 in cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::request_missing_objects(cryptonote::cryptonote_connection_context&, bool, bool) ()
#3  0x000000000071d8c0 in cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::handle_response_chain_entry(int, cryptonote::NOTIFY_RESPONSE_CHAIN_ENTRY::request&, cryptonote::cryptonote_connection_context&) ()
#4  0x0000000000704ca7 in int epee::net_utils::buff_to_t_adapter<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, cryptonote::NOTIFY_RESPONSE_CHAIN_ENTRY::request, cryptonote::cryptonote_connection_context, boost::_bi::bind_t<int, boost::_mfi::mf3<int, cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, int, cryptonote::NOTIFY_RESPONSE_CHAIN_ENTRY::request&, cryptonote::cryptonote_connection_context&>, boost::_bi::list4<boost::_bi::value<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*>, boost::arg<1>, boost::arg<2>, boost::arg<3> > > >(cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, boost::_bi::bind_t<int, boost::_mfi::mf3<int, cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, int, cryptonote::NOTIFY_RESPONSE_CHAIN_ENTRY::request&, cryptonote::cryptonote_connection_context&>, boost::_bi::list4<boost::_bi::value<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*>, boost::arg<1>, boost::arg<2>, boost::arg<3> > >, cryptonote::cryptonote_connection_context&) ()
#5  0x000000000070c381 in int cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::handle_invoke_map<cryptonote::cryptonote_connection_context>(bool, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&, cryptonote::cryptonote_connection_context&, bool&) ()
#6  0x000000000070c7ce in int nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::handle_invoke_map<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >(bool, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&, bool&) ()
#7  0x000000000070cbdf in nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::notify(int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&) ()
#8  0x000000000070d0b0 in epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >::handle_recv(void const*, unsigned long) ()
#9  0x0000000000724cea in epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::handle_read(boost::system::error_code const&, unsigned long) ()
#10 0x00000000006cc391 in void boost::asio::detail::strand_service::dispatch<boost::asio::detail::binder2<boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::system::error_code, unsigned long> >(boost::asio::detail::strand_service::strand_impl*&, boost::asio::detail::binder2<boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::system::error_code, unsigned long>&) ()
#11 0x00000000006cc7c9 in boost::asio::detail::completion_handler<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > > >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) ()
#12 0x00000000006ccb8a in void boost::asio::detail::strand_service::dispatch<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boos---Type <return> to continue, or q <return> to quit---
t::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > > >(boost::asio::detail::strand_service::strand_impl*&, boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > >&) ()
#13 0x00000000006cce43 in boost::asio::detail::reactive_socket_recv_op<boost::asio::mutable_buffers_1, boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running> >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) ()
#14 0x0000000000649d1c in boost::asio::detail::epoll_reactor::descriptor_state::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) ()
#15 0x000000000066a7f7 in epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread() ()
#16 0x0000000000988fa5 in thread_proxy ()
#17 0x00007f8b25300494 in start_thread (arg=0x7f8b20c36700) at pthread_create.c:333
#18 0x00007f8b25042aff in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:97

Thread 11 (Thread 0x7f8b21137700 (LWP 11124)):
#0  pthread_cond_timedwait@@GLIBC_2.3.2 () at ../sysdeps/unix/sysv/linux/x86_64/pthread_cond_timedwait.S:225
#1  0x0000000000989e9c in boost::this_thread::hiden::sleep_for(timespec const&) ()
#2  0x0000000000715fd2 in cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::request_missing_objects(cryptonote::cryptonote_connection_context&, bool, bool) ()
#3  0x0000000000719a2e in cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::try_add_next_blocks(cryptonote::cryptonote_connection_context&) ()
#4  0x000000000071cd2b in cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::handle_response_get_objects(int, cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request&, cryptonote::cryptonote_connection_context&) ()
#5  0x000000000070c1da in int epee::net_utils::buff_to_t_adapter<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request, cryptonote::cryptonote_connection_context, boost::_bi::bind_t<int, boost::_mfi::mf3<int, cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, int, cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request&, cryptonote::cryptonote_connection_context&>, boost::_bi::list4<boost::_bi::value<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*>, boost::arg<1>, boost::arg<2>, boost::arg<3> > > >(cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, boost::_bi::bind_t<int, boost::_mfi::mf3<int, cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, int, cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request&, cryptonote::cryptonote_connection_context&>, boost::_bi::list4<boost::_bi::value<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*>, boost::arg<1>, boost::arg<2>, boost::arg<3> > >, cryptonote::cryptonote_connection_context&) ()
#6  0x000000000070c4d3 in int cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::handle_invoke_map<cryptonote::cryptonote_connection_context>(bool, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&, cryptonote::cryptonote_connection_context&, bool&) ()
#7  0x000000000070c7ce in int nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::handle_invoke_map<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >(bool, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&, bool&) ()
#8  0x000000000070cbdf in nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::notify(int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&) ()
#9  0x000000000070d0b0 in epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >::handle_recv(void const*, unsigned long) ()
#10 0x0000000000724cea in epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::handle_read(boost::system::error_code const&, unsigned long) ()
#11 0x00000000006cc391 in void boost::asio::detail::strand_service::dispatch<boost::asio::detail::binder2<boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::system::error_code, unsigned long> >(boost::asio::detail::strand_service::strand_impl*&, boost::asio::detail::binder2<boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::system::error_code, unsigned long>&) ()
#12 0x00000000006cc7c9 in boost::asio::detail::completion_handler<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > > >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) ()
#13 0x00000000006ccb8a in void boost::asio::detail::strand_service::dispatch<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > > >(boost::asio::detail::strand_service::strand_impl*&, boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > >&) ()
#14 0x00000000006cce43 in boost::asio::detail::reactive_socket_recv_op<boost::asio::mutable_buffers_1, boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running> >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) ()
#15 0x0000000000649d1c in boost::asio::detail::epoll_reactor::descriptor_state::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) ()
#16 0x000000000066a7f7 in epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread() ()
#17 0x0000000000988fa5 in thread_proxy ()
#18 0x00007f8b25300494 in start_thread (arg=0x7f8b21137700) at pthread_create.c:333
#19 0x00007f8b25042aff in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:97

Thread 10 (Thread 0x7f8b21638700 (LWP 11123)):
#0  pthread_cond_timedwait@@GLIBC_2.3.2 () at ../sysdeps/unix/sysv/linux/x86_64/pthread_cond_timedwait.S:225
#1  0x0000000000989e9c in boost::this_thread::hiden::sleep_for(timespec const&) ()
#2  0x0000000000715fd2 in cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::request_missing_objects(cryptonote::cryptonote_connection_context&, bool, bool) ()
#3  0x0000000000719a2e in cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::try_add_next_blocks(cryptonote::cryptonote_connection_context&) ()
#4  0x000000000071cd2b in cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::handle_response_get_objects(int, cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request&, cryptonote::cryptonote_connection_context&) ()
#5  0x000000000070c1da in int epee::net_utils::buff_to_t_adapter<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request, cryptonote::cryptonote_connection_context, boost::_bi::bind_t<int, boost::_mfi::mf3<int, cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, int, cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request&, cryptonote::cryptonote_connection_context&>, boost::_bi::list4<boost::_bi::value<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*>, boost::arg<1>, boost::arg<2>, boost::arg<3> > > >(cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, boost::_bi::bind_t<int, boost::_mfi::mf3<int, cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, int, cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request&, cryptonote::cryptonote_connection_context&>, boost::_bi::list4<boost::_bi::value<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*>, boost::arg<1>, boost::arg<2>, boost::arg<3> > >, cryptonote::cryptonote_connection_context&) ()
#6  0x000000000070c4d3 in int cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::handle_invoke_map<cryptonote::cryptonote_connection_context>(bool, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&, cryptonote::cryptonote_connection_context&, bool&) ()
#7  0x000000000070c7ce in int nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::handle_invoke_map<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >(bool, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&, bool&) ()
#8  0x000000000070cbdf in nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::notify(int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&) ()
#9  0x000000000070d0b0 in epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >::handle_recv(void const*, unsigned long) ()
#10 0x0000000000724cea in epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::handle_read(boost::system::error_code const&, unsigned long) ()
#11 0x00000000006cc391 in void boost::asio::detail::strand_service::dispatch<boost::asio::detail::binder2<boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::system::error_code, unsigned long> >(boost::asio::detail::strand_service::strand_impl*&, boost::asio::detail::binder2<boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::system::error_code, unsigned long>&) ()
#12 0x00000000006cc7c9 in boost::asio::detail::completion_handler<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_con---Type <return> to continue, or q <return> to quit---
text> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > > >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) ()
#13 0x00000000006ccb8a in void boost::asio::detail::strand_service::dispatch<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > > >(boost::asio::detail::strand_service::strand_impl*&, boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > >&) ()
#14 0x00000000006cce43 in boost::asio::detail::reactive_socket_recv_op<boost::asio::mutable_buffers_1, boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running> >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) ()
#15 0x0000000000649d1c in boost::asio::detail::epoll_reactor::descriptor_state::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) ()
#16 0x000000000066a7f7 in epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread() ()
#17 0x0000000000988fa5 in thread_proxy ()
#18 0x00007f8b25300494 in start_thread (arg=0x7f8b21638700) at pthread_create.c:333
#19 0x00007f8b25042aff in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:97

Thread 9 (Thread 0x7f8b21b39700 (LWP 11122)):
#0  pthread_cond_timedwait@@GLIBC_2.3.2 () at ../sysdeps/unix/sysv/linux/x86_64/pthread_cond_timedwait.S:225
#1  0x0000000000989e9c in boost::this_thread::hiden::sleep_for(timespec const&) ()
#2  0x0000000000715fd2 in cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::request_missing_objects(cryptonote::cryptonote_connection_context&, bool, bool) ()
#3  0x0000000000719a2e in cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::try_add_next_blocks(cryptonote::cryptonote_connection_context&) ()
#4  0x000000000071cd2b in cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::handle_response_get_objects(int, cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request&, cryptonote::cryptonote_connection_context&) ()
#5  0x000000000070c1da in int epee::net_utils::buff_to_t_adapter<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request, cryptonote::cryptonote_connection_context, boost::_bi::bind_t<int, boost::_mfi::mf3<int, cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, int, cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request&, cryptonote::cryptonote_connection_context&>, boost::_bi::list4<boost::_bi::value<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*>, boost::arg<1>, boost::arg<2>, boost::arg<3> > > >(cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, boost::_bi::bind_t<int, boost::_mfi::mf3<int, cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, int, cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request&, cryptonote::cryptonote_connection_context&>, boost::_bi::list4<boost::_bi::value<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*>, boost::arg<1>, boost::arg<2>, boost::arg<3> > >, cryptonote::cryptonote_connection_context&) ()
#6  0x000000000070c4d3 in int cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::handle_invoke_map<cryptonote::cryptonote_connection_context>(bool, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&, cryptonote::cryptonote_connection_context&, bool&) ()
#7  0x000000000070c7ce in int nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::handle_invoke_map<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >(bool, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&, bool&) ()
#8  0x000000000070cbdf in nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::notify(int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&) ()
#9  0x000000000070d0b0 in epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >::handle_recv(void const*, unsigned long) ()
#10 0x0000000000724cea in epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::handle_read(boost::system::error_code const&, unsigned long) ()
#11 0x00000000006cc391 in void boost::asio::detail::strand_service::dispatch<boost::asio::detail::binder2<boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::system::error_code, unsigned long> >(boost::asio::detail::strand_service::strand_impl*&, boost::asio::detail::binder2<boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::system::error_code, unsigned long>&) ()
#12 0x00000000006cc7c9 in boost::asio::detail::completion_handler<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > > >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) ()
#13 0x00000000006ccb8a in void boost::asio::detail::strand_service::dispatch<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > > >(boost::asio::detail::strand_service::strand_impl*&, boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > >&) ()
#14 0x00000000006cce43 in boost::asio::detail::reactive_socket_recv_op<boost::asio::mutable_buffers_1, boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running> >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) ()
#15 0x0000000000649d1c in boost::asio::detail::epoll_reactor::descriptor_state::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) ()
#16 0x000000000066a7f7 in epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread() ()
#17 0x0000000000988fa5 in thread_proxy ()
#18 0x00007f8b25300494 in start_thread (arg=0x7f8b21b39700) at pthread_create.c:333
#19 0x00007f8b25042aff in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:97

Thread 8 (Thread 0x7f8b23855700 (LWP 11121)):
#0  pthread_cond_timedwait@@GLIBC_2.3.2 () at ../sysdeps/unix/sysv/linux/x86_64/pthread_cond_timedwait.S:225
#1  0x0000000000989e9c in boost::this_thread::hiden::sleep_for(timespec const&) ()
#2  0x0000000000654a6a in boost::detail::thread_data<nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::run()::{lambda()#1}>::run() ()
#3  0x0000000000988fa5 in thread_proxy ()
#4  0x00007f8b25300494 in start_thread (arg=0x7f8b23855700) at pthread_create.c:333
#5  0x00007f8b25042aff in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:97

Thread 7 (Thread 0x7f8b1a853700 (LWP 11120)):
#0  pthread_cond_wait@@GLIBC_2.3.2 () at ../sysdeps/unix/sysv/linux/x86_64/pthread_cond_wait.S:185
#1  0x0000000000669502 in epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::worker_thread() ()
#2  0x0000000000988fa5 in thread_proxy ()
#3  0x00007f8b25300494 in start_thread (arg=0x7f8b1a853700) at pthread_create.c:333
#4  0x00007f8b25042aff in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:97

Thread 6 (Thread 0x7f8b23054700 (LWP 11119)):
#0  0x00007f8b250430f3 in epoll_wait () at ../sysdeps/unix/syscall-template.S:84
#1  0x00000000006690ab in epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::worker_thread() ()
#2  0x0000000000988fa5 in thread_proxy ()
#3  0x00007f8b25300494 in start_thread (arg=0x7f8b23054700) at pthread_create.c:333
#4  0x00007f8b25042aff in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:97

Thread 5 (Thread 0x7f8b22551700 (LWP 11118)):
#0  pthread_cond_wait@@GLIBC_2.3.2 () at ../sysdeps/unix/sysv/linux/x86_64/pthread_cond_wait.S:185
#1  0x00000000008220ea in boost::asio::io_service::run() ()
#2  0x0000000000988fa5 in thread_proxy ()
---Type <return> to continue, or q <return> to quit---
#3  0x00007f8b25300494 in start_thread (arg=0x7f8b22551700) at pthread_create.c:333
#4  0x00007f8b25042aff in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:97

Thread 4 (Thread 0x7f8b24557700 (LWP 11110)):
#0  pthread_cond_wait@@GLIBC_2.3.2 () at ../sysdeps/unix/sysv/linux/x86_64/pthread_cond_wait.S:185
#1  0x000000000088c223 in tools::thread_group::data::run() ()
#2  0x0000000000988fa5 in thread_proxy ()
#3  0x00007f8b25300494 in start_thread (arg=0x7f8b24557700) at pthread_create.c:333
#4  0x00007f8b25042aff in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:97

Thread 3 (Thread 0x7f8b24a58700 (LWP 11109)):
#0  pthread_cond_wait@@GLIBC_2.3.2 () at ../sysdeps/unix/sysv/linux/x86_64/pthread_cond_wait.S:185
#1  0x000000000088c223 in tools::thread_group::data::run() ()
#2  0x0000000000988fa5 in thread_proxy ()
#3  0x00007f8b25300494 in start_thread (arg=0x7f8b24a58700) at pthread_create.c:333
#4  0x00007f8b25042aff in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:97

Thread 2 (Thread 0x7f8b24f59700 (LWP 11108)):
#0  pthread_cond_wait@@GLIBC_2.3.2 () at ../sysdeps/unix/sysv/linux/x86_64/pthread_cond_wait.S:185
#1  0x000000000088c223 in tools::thread_group::data::run() ()
#2  0x0000000000988fa5 in thread_proxy ()
#3  0x00007f8b25300494 in start_thread (arg=0x7f8b24f59700) at pthread_create.c:333
#4  0x00007f8b25042aff in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:97

Thread 1 (Thread 0x7f8b25c1bec0 (LWP 11107)):
#0  pthread_cond_wait@@GLIBC_2.3.2 () at ../sysdeps/unix/sysv/linux/x86_64/pthread_cond_wait.S:185
#1  0x000000000098ab03 in boost::thread::join_noexcept() ()
#2  0x000000000072da4b in epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::run_server(unsigned long, bool, boost::thread_attributes const&) ()
#3  0x000000000072f067 in nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::run() ()
#4  0x000000000063cee4 in daemonize::t_daemon::run(bool) ()
#5  0x0000000000741ce6 in bool daemonizer::daemonize<daemonize::t_executor>(int, char const**, daemonize::t_executor&&, boost::program_options::variables_map const&) ()
#6  0x0000000000611bc7 in main ()
```

## moneromooo-monero | 2017-11-15T13:19:22+00:00
When this happens again, please post the output of those commands:
sync_info
print_cn

And that trace makes me think you should run with log levels: 1,net.cn:DEBUG

## hyc | 2017-11-16T02:10:55+00:00
Something conspicuously absent from this trace is tools::threadpool threads. Did they all die? We're going to need to see more verbose logs...

## assylias | 2017-11-16T10:02:57+00:00
@hyc Unfortunately the sync finished on the third attempt (when I put the log level 1 on) so I can't reproduce it any more. If there's a way to bring the blockchain back to a lower height, I can try to resync from the height where I was before the issue to see if it happens again.

## moneromooo-monero | 2017-11-16T10:30:07+00:00
monero-blockchain-import --pop-blocks N

vary N as needed

## miningpoolhub | 2017-11-17T06:45:53+00:00
Here's gdb output

```
Thread 30 (Thread 0x7f42e6ac6700 (LWP 31973)):
#0  pthread_cond_wait@@GLIBC_2.3.2 () at ../sysdeps/unix/sysv/linux/x86_64/pthread_cond_wait.S:185
#1  0x00000000005b4b42 in epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread() ()
#2  0x00007f50716d65d5 in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0
#3  0x00007f50706246ba in start_thread (arg=0x7f42e6ac6700) at pthread_create.c:333
#4  0x00007f507035a3dd in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109

Thread 29 (Thread 0x7f5064557700 (LWP 31972)):
#0  pthread_cond_wait@@GLIBC_2.3.2 () at ../sysdeps/unix/sysv/linux/x86_64/pthread_cond_wait.S:185
#1  0x00000000005b4b42 in epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread() ()
#2  0x00007f50716d65d5 in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0
#3  0x00007f50706246ba in start_thread (arg=0x7f5064557700) at pthread_create.c:333
#4  0x00007f507035a3dd in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109

Thread 28 (Thread 0x7f5064a58700 (LWP 31971)):
#0  pthread_cond_wait@@GLIBC_2.3.2 () at ../sysdeps/unix/sysv/linux/x86_64/pthread_cond_wait.S:185
#1  0x00000000005b4b42 in epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread() ()
#2  0x00007f50716d65d5 in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0
#3  0x00007f50706246ba in start_thread (arg=0x7f5064a58700) at pthread_create.c:333
#4  0x00007f507035a3dd in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109

Thread 27 (Thread 0x7f5064f59700 (LWP 31970)):
#0  pthread_cond_wait@@GLIBC_2.3.2 () at ../sysdeps/unix/sysv/linux/x86_64/pthread_cond_wait.S:185
#1  0x00000000005b4b42 in epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread() ()
#2  0x00007f50716d65d5 in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0
#3  0x00007f50706246ba in start_thread (arg=0x7f5064f59700) at pthread_create.c:333
#4  0x00007f507035a3dd in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109

Thread 26 (Thread 0x7f506545a700 (LWP 31969)):
#0  pthread_cond_wait@@GLIBC_2.3.2 () at ../sysdeps/unix/sysv/linux/x86_64/pthread_cond_wait.S:185
#1  0x00000000005b4b42 in epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread() ()
#2  0x00007f50716d65d5 in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0
#3  0x00007f50706246ba in start_thread (arg=0x7f506545a700) at pthread_create.c:333
#4  0x00007f507035a3dd in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109

Thread 25 (Thread 0x7f506595b700 (LWP 31968)):
#0  pthread_cond_wait@@GLIBC_2.3.2 () at ../sysdeps/unix/sysv/linux/x86_64/pthread_cond_wait.S:185
#1  0x00000000005b4b42 in epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread() ()
#2  0x00007f50716d65d5 in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0
#3  0x00007f50706246ba in start_thread (arg=0x7f506595b700) at pthread_create.c:333
#4  0x00007f507035a3dd in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109

Thread 24 (Thread 0x7f5065e5c700 (LWP 31967)):
#0  pthread_cond_wait@@GLIBC_2.3.2 () at ../sysdeps/unix/sysv/linux/x86_64/pthread_cond_wait.S:185
#1  0x00000000005b4b42 in epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread() ()
#2  0x00007f50716d65d5 in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0
#3  0x00007f50706246ba in start_thread (arg=0x7f5065e5c700) at pthread_create.c:333
#4  0x00007f507035a3dd in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109

Thread 23 (Thread 0x7f506635d700 (LWP 31966)):
#0  pthread_cond_wait@@GLIBC_2.3.2 () at ../sysdeps/unix/sysv/linux/x86_64/pthread_cond_wait.S:185
#1  0x00000000005b4b42 in epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread() ()
#2  0x00007f50716d65d5 in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0
#3  0x00007f50706246ba in start_thread (arg=0x7f506635d700) at pthread_create.c:333
#4  0x00007f507035a3dd in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109

Thread 22 (Thread 0x7f506685e700 (LWP 31965)):
#0  pthread_cond_wait@@GLIBC_2.3.2 () at ../sysdeps/unix/sysv/linux/x86_64/pthread_cond_wait.S:185
#1  0x00000000005b4b42 in epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread() ()
#2  0x00007f50716d65d5 in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0
#3  0x00007f50706246ba in start_thread (arg=0x7f506685e700) at pthread_create.c:333
#4  0x00007f507035a3dd in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109

Thread 21 (Thread 0x7f5066d5f700 (LWP 31964)):
#0  0x00007f507035a9d3 in epoll_wait () at ../sysdeps/unix/syscall-template.S:84
#1  0x00000000005b46eb in epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread() ()
#2  0x00007f50716d65d5 in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0
#3  0x00007f50706246ba in start_thread (arg=0x7f5066d5f700) at pthread_create.c:333
#4  0x00007f507035a3dd in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109

Thread 20 (Thread 0x7f5068f64700 (LWP 31963)):
#0  pthread_cond_timedwait@@GLIBC_2.3.2 () at ../sysdeps/unix/sysv/linux/x86_64/pthread_cond_timedwait.S:225
#1  0x00007f50716d67e2 in boost::this_thread::hiden::sleep_for(timespec const&) () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0
#2  0x00000000005a01ea in boost::detail::thread_data<nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::run()::{lambda()#1}>::run() ()
#3  0x00007f50716d65d5 in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0
#4  0x00007f50706246ba in start_thread (arg=0x7f5068f64700) at pthread_create.c:333
#5  0x00007f507035a3dd in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109

Thread 19 (Thread 0x7f5068763700 (LWP 31962)):
#0  0x00007f507035a9d3 in epoll_wait () at ../sysdeps/unix/syscall-template.S:84
#1  0x00000000005b346b in epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::worker_thread() ()
#2  0x00007f50716d65d5 in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0
#3  0x00007f50706246ba in start_thread (arg=0x7f5068763700) at pthread_create.c:333
#4  0x00007f507035a3dd in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109

Thread 18 (Thread 0x7f5067f62700 (LWP 31961)):
#0  pthread_cond_wait@@GLIBC_2.3.2 () at ../sysdeps/unix/sysv/linux/x86_64/pthread_cond_wait.S:185
#1  0x00000000005b38c2 in epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::worker_thread() ()
#2  0x00007f50716d65d5 in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0
#3  0x00007f50706246ba in start_thread (arg=0x7f5067f62700) at pthread_create.c:333
#4  0x00007f507035a3dd in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109

Thread 17 (Thread 0x7f5067761700 (LWP 31933)):
#0  pthread_cond_wait@@GLIBC_2.3.2 () at ../sysdeps/unix/sysv/linux/x86_64/pthread_cond_wait.S:185
#1  0x0000000000774aba in boost::asio::io_service::run() ()
#2  0x00007f50716d65d5 in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0
#3  0x00007f50706246ba in start_thread (arg=0x7f5067761700) at pthread_create.c:333
#4  0x00007f507035a3dd in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109

Thread 16 (Thread 0x7f5069465700 (LWP 31831)):
#0  pthread_cond_wait@@GLIBC_2.3.2 () at ../sysdeps/unix/sysv/linux/x86_64/pthread_cond_wait.S:185
#1  0x00000000007de253 in tools::thread_group::data::run() ()
#2  0x00007f50716d65d5 in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0
#3  0x00007f50706246ba in start_thread (arg=0x7f5069465700) at pthread_create.c:333
#4  0x00007f507035a3dd in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109

Thread 15 (Thread 0x7f5069966700 (LWP 31830)):
#0  pthread_cond_wait@@GLIBC_2.3.2 () at ../sysdeps/unix/sysv/linux/x86_64/pthread_cond_wait.S:185
#1  0x00000000007de253 in tools::thread_group::data::run() ()
#2  0x00007f50716d65d5 in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0
#3  0x00007f50706246ba in start_thread (arg=0x7f5069966700) at pthread_create.c:333
#4  0x00007f507035a3dd in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109

Thread 14 (Thread 0x7f5069e67700 (LWP 31829)):
#0  pthread_cond_wait@@GLIBC_2.3.2 () at ../sysdeps/unix/sysv/linux/x86_64/pthread_cond_wait.S:185
#1  0x00000000007de253 in tools::thread_group::data::run() ()
#2  0x00007f50716d65d5 in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0
#3  0x00007f50706246ba in start_thread (arg=0x7f5069e67700) at pthread_create.c:333
#4  0x00007f507035a3dd in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109

Thread 13 (Thread 0x7f506a368700 (LWP 31828)):
#0  pthread_cond_wait@@GLIBC_2.3.2 () at ../sysdeps/unix/sysv/linux/x86_64/pthread_cond_wait.S:185
#1  0x00000000007de253 in tools::thread_group::data::run() ()
#2  0x00007f50716d65d5 in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0
#3  0x00007f50706246ba in start_thread (arg=0x7f506a368700) at pthread_create.c:333
#4  0x00007f507035a3dd in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109

Thread 12 (Thread 0x7f506a869700 (LWP 31827)):
#0  pthread_cond_wait@@GLIBC_2.3.2 () at ../sysdeps/unix/sysv/linux/x86_64/pthread_cond_wait.S:185
#1  0x00000000007de253 in tools::thread_group::data::run() ()
#2  0x00007f50716d65d5 in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0
#3  0x00007f50706246ba in start_thread (arg=0x7f506a869700) at pthread_create.c:333
#4  0x00007f507035a3dd in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109

Thread 11 (Thread 0x7f506ad6a700 (LWP 31826)):
#0  pthread_cond_wait@@GLIBC_2.3.2 () at ../sysdeps/unix/sysv/linux/x86_64/pthread_cond_wait.S:185
#1  0x00000000007de253 in tools::thread_group::data::run() ()
#2  0x00007f50716d65d5 in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0
#3  0x00007f50706246ba in start_thread (arg=0x7f506ad6a700) at pthread_create.c:333
#4  0x00007f507035a3dd in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109

Thread 10 (Thread 0x7f506b26b700 (LWP 31825)):
#0  pthread_cond_wait@@GLIBC_2.3.2 () at ../sysdeps/unix/sysv/linux/x86_64/pthread_cond_wait.S:185
#1  0x00000000007de253 in tools::thread_group::data::run() ()
#2  0x00007f50716d65d5 in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0
#3  0x00007f50706246ba in start_thread (arg=0x7f506b26b700) at pthread_create.c:333
#4  0x00007f507035a3dd in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109

Thread 9 (Thread 0x7f506b76c700 (LWP 31824)):
#0  pthread_cond_wait@@GLIBC_2.3.2 () at ../sysdeps/unix/sysv/linux/x86_64/pthread_cond_wait.S:185
#1  0x00000000007de253 in tools::thread_group::data::run() ()
#2  0x00007f50716d65d5 in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0
#3  0x00007f50706246ba in start_thread (arg=0x7f506b76c700) at pthread_create.c:333
#4  0x00007f507035a3dd in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109

Thread 8 (Thread 0x7f506bc6d700 (LWP 31823)):
#0  pthread_cond_wait@@GLIBC_2.3.2 () at ../sysdeps/unix/sysv/linux/x86_64/pthread_cond_wait.S:185
#1  0x00000000007de253 in tools::thread_group::data::run() ()
#2  0x00007f50716d65d5 in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0
#3  0x00007f50706246ba in start_thread (arg=0x7f506bc6d700) at pthread_create.c:333
#4  0x00007f507035a3dd in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109

Thread 7 (Thread 0x7f506c16e700 (LWP 31822)):
#0  pthread_cond_wait@@GLIBC_2.3.2 () at ../sysdeps/unix/sysv/linux/x86_64/pthread_cond_wait.S:185
#1  0x00000000007de253 in tools::thread_group::data::run() ()
#2  0x00007f50716d65d5 in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0
#3  0x00007f50706246ba in start_thread (arg=0x7f506c16e700) at pthread_create.c:333
#4  0x00007f507035a3dd in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109

Thread 6 (Thread 0x7f506c66f700 (LWP 31821)):
#0  pthread_cond_wait@@GLIBC_2.3.2 () at ../sysdeps/unix/sysv/linux/x86_64/pthread_cond_wait.S:185
#1  0x00000000007de253 in tools::thread_group::data::run() ()
#2  0x00007f50716d65d5 in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0
#3  0x00007f50706246ba in start_thread (arg=0x7f506c66f700) at pthread_create.c:333
#4  0x00007f507035a3dd in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109

Thread 5 (Thread 0x7f506cb70700 (LWP 31820)):
#0  pthread_cond_wait@@GLIBC_2.3.2 () at ../sysdeps/unix/sysv/linux/x86_64/pthread_cond_wait.S:185
#1  0x00000000007de253 in tools::thread_group::data::run() ()
#2  0x00007f50716d65d5 in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0
#3  0x00007f50706246ba in start_thread (arg=0x7f506cb70700) at pthread_create.c:333
#4  0x00007f507035a3dd in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109

Thread 4 (Thread 0x7f506d071700 (LWP 31819)):
#0  pthread_cond_wait@@GLIBC_2.3.2 () at ../sysdeps/unix/sysv/linux/x86_64/pthread_cond_wait.S:185
#1  0x00000000007de253 in tools::thread_group::data::run() ()
#2  0x00007f50716d65d5 in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0
#3  0x00007f50706246ba in start_thread (arg=0x7f506d071700) at pthread_create.c:333
#4  0x00007f507035a3dd in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109

Thread 3 (Thread 0x7f506d572700 (LWP 31818)):
#0  pthread_cond_wait@@GLIBC_2.3.2 () at ../sysdeps/unix/sysv/linux/x86_64/pthread_cond_wait.S:185
#1  0x00000000007de253 in tools::thread_group::data::run() ()
#2  0x00007f50716d65d5 in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0
#3  0x00007f50706246ba in start_thread (arg=0x7f506d572700) at pthread_create.c:333
#4  0x00007f507035a3dd in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109

Thread 2 (Thread 0x7f506da73700 (LWP 31817)):
#0  pthread_cond_wait@@GLIBC_2.3.2 () at ../sysdeps/unix/sysv/linux/x86_64/pthread_cond_wait.S:185
#1  0x00000000007de253 in tools::thread_group::data::run() ()
#2  0x00007f50716d65d5 in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0
#3  0x00007f50706246ba in start_thread (arg=0x7f506da73700) at pthread_create.c:333
#4  0x00007f507035a3dd in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109

Thread 1 (Thread 0x7f5072f12740 (LWP 31813)):
#0  pthread_cond_wait@@GLIBC_2.3.2 () at ../sysdeps/unix/sysv/linux/x86_64/pthread_cond_wait.S:185
#1  0x00007f50716d8043 in boost::thread::join_noexcept() () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0
#2  0x000000000067db28 in epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::run_server(unsigned long, bool, boost::thread_attributes const&) ()
#3  0x000000000067f157 in nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::run() ()
#4  0x0000000000588784 in daemonize::t_daemon::run(bool) ()
#5  0x0000000000691ff2 in bool daemonizer::daemonize<daemonize::t_executor>(int, char const**, daemonize::t_executor&&, boost::program_options::variables_map const&) ()
#6  0x000000000055d36e in main ()
```

bitmonero.log
monero ran with --log-level 1
```
2017-11-17 04:25:08.365 [P2P6]  WARN    net.dns src/common/dns_utils.cpp:487    WARNING: no two valid MoneroPulse DNS checkpoint records were received
2017-11-17 06:20:58.792 [P2P1]  WARN    net.dns src/common/dns_utils.cpp:487    WARNING: no two valid MoneroPulse DNS checkpoint records were received
```
sync_info cal
```
{
  "id": "0",
  "jsonrpc": "2.0",
  "result": {
    "height": 1444683,
    "peers": [{
      "info": {
        "address": "175.118.209.218:18080",
        "avg_download": 0,
        "avg_upload": 0,
        "connection_id": "\rk\tï¿½Kyï¿½]ï¿½-cï¿½ï¿½\t",
                  "current_download": 3,
                  "current_upload": 0,
                  "height": 0,
                  "host": "175.118.209.218",
                  "incoming": false,
                  "ip": "175.118.209.218",
                  "live_time": 29151,
                  "local_ip": false,
                  "localhost": false,
                  "peer_id": "0",
                  "port": "18080",
                  "recv_count": 32153,
                  "recv_idle_time": 29151,
                  "send_count": 364,
                  "send_idle_time": 29151,
                  "state": "state_before_handshake",
                  "support_flags": 0
                }
              }],
              "status": "OK",
              "target_height": 0
  }
```

get_info
```
{
  "id": "0",
  "jsonrpc": "2.0",
  "result": {
    "alt_blocks_count": 5,
    "block_size_limit": 600000,
    "cumulative_difficulty": 4800982594835623,
    "difficulty": 30426415723,
    "grey_peerlist_size": 5000,
    "height": 1444683,
    "incoming_connections_count": 0,
    "outgoing_connections_count": 1,
    "start_time": 1510554044,
    "status": "OK",
    "target": 120,
    "target_height": 0,
    "testnet": false,
    "top_block_hash": "fdd3f6f271cc287274944339334c6bf11eb4c5c71188d969dd97a06ecbf8db6d",
    "tx_count": 1910687,
    "tx_pool_size": 11,
    "white_peerlist_size": 1000
  }
```


get_connections
```
{
  "id": "0",
  "jsonrpc": "2.0",
  "result": {
    "connections": [{
      "address": "175.118.209.218:18080",
      "avg_download": 0,
      "avg_upload": 0,
      "connection_id": "\rk\tï¿½Kyï¿½]ï¿½-cï¿½ï¿½\t",
      "current_download": 3,
      "current_upload": 0,
      "height": 0,
      "host": "175.118.209.218",
      "incoming": false,
      "ip": "175.118.209.218",
      "live_time": 29451,
      "local_ip": false,
      "localhost": false,
      "peer_id": "0",
      "port": "18080",
      "recv_count": 32153,
      "recv_idle_time": 29451,
      "send_count": 364,
      "send_idle_time": 29451,
      "state": "state_before_handshake",
      "support_flags": 0
    }],
    "status": "OK"
  }
```

getlastblockheader
```

{
  "id": "0",
  "jsonrpc": "2.0",
  "result": {
    "block_header": {
      "block_size": 13616,
      "depth": 0,
      "difficulty": 30419921438,
      "hash": "fdd3f6f271cc287274944339334c6bf11eb4c5c71188d969dd97a06ecbf8db6d",
      "height": 1444682,
      "major_version": 6,
      "minor_version": 6,
      "nonce": 6333,
      "num_txes": 1,
      "orphan_status": false,
      "prev_hash": "342014e8aa522a1e9a64b4bfc918aad73d0301cf59767cb7c30178801aba4b93",
      "reward": 5896167955878,
      "timestamp": 1510895377
    },
    "status": "OK"
  }
```


## miningpoolhub | 2017-11-17T06:52:42+00:00
monero-blockchain-import --pop-blocks 10
```
2017-11-17 06:48:33.164     7f6b883c3740        INFO    bcutil  src/blockchain_utilities/blockchain_import.cpp:646      Starting...
2017-11-17 06:48:33.164     7f6b883c3740        INFO    bcutil  src/blockchain_utilities/blockchain_import.cpp:681      database: lmdb
2017-11-17 06:48:33.164     7f6b883c3740        INFO    bcutil  src/blockchain_utilities/blockchain_import.cpp:682      database flags: 0
2017-11-17 06:48:33.164     7f6b883c3740        INFO    bcutil  src/blockchain_utilities/blockchain_import.cpp:683      verify:  true
2017-11-17 06:48:33.164     7f6b883c3740        INFO    bcutil  src/blockchain_utilities/blockchain_import.cpp:687      batch:   true  batch size: 5000
2017-11-17 06:48:33.164     7f6b883c3740        INFO    bcutil  src/blockchain_utilities/blockchain_import.cpp:693      resume:  true
2017-11-17 06:48:33.164     7f6b883c3740        INFO    bcutil  src/blockchain_utilities/blockchain_import.cpp:694      testnet: false
2017-11-17 06:48:33.164     7f6b883c3740        INFO    bcutil  src/blockchain_utilities/blockchain_import.cpp:696      bootstrap file path: /home/xxx/.bitmonero/export/blockchain.raw
2017-11-17 06:48:33.164     7f6b883c3740        INFO    bcutil  src/blockchain_utilities/blockchain_import.cpp:697      database path:       /home/xxx/.bitmonero
2017-11-17 06:48:33.165     7f6b883c3740        INFO    global  src/cryptonote_core/cryptonote_core.cpp:323     Loading blockchain from folder /home/xxx/.bitmonero/lmdb ...
2017-11-17 06:48:34.343     7f6b883c3740        INFO    global  src/cryptonote_core/cryptonote_core.cpp:421     Loading checkpoints
2017-11-17 06:48:34.343     7f6b883c3740        WARN    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:2674 WARNING: batch transaction mode already enabled, but asked to enable batch mode
2017-11-17 06:48:34.343     7f6b883c3740        INFO    bcutil  src/blockchain_utilities/blockchain_import.cpp:716      height: 1444683
2017-11-17 06:48:34.352     7f6b883c3740        INFO    bcutil  src/blockchain_utilities/blockchain_import.cpp:718      height: 1444673

```

I don't know what this command is for.


## moneromooo-monero | 2017-11-17T13:01:51+00:00
Do you have the string "Exception:" in your bitmonero.log ? If so, can you paste them ?

## miningpoolhub | 2017-11-18T06:01:47+00:00
Yeah there's some exception logs few hours before the sync stop

```
2017-11-17 01:13:05.130 [P2P5]  WARN    net.p2p src/p2p/net_node.inl:834        [46.180.15.206:18080 OUT] COMMAND_TIMED_SYNC invoke failed. (-4, LEVIN_ERROR_CONNECTION_TIMEDOUT)
2017-11-17 01:13:05.157 [P2P8]  WARN    net.p2p src/p2p/net_node.inl:1195       Failed to connect to any of seed peers, trying fallback seeds
2017-11-17 01:13:05.157 [P2P8]  WARN    net.p2p src/p2p/net_node.inl:1206       Failed to connect to any of seed peers, continuing without seeds
2017-11-17 01:16:30.863 [P2P2]  WARN    net.p2p src/p2p/net_node.inl:1629       [71.56.200.134:18080 OUT] COMMAND_REQUEST_SUPPORT_FLAGS invoke failed. (-3, LEVIN_ERROR_CONNECTION_DESTROYED)
2017-11-17 01:16:31.047 [P2P5]  ERROR   net     contrib/epee/include/net/levin_protocol_handler_async.h:289     [71.56.200.134:18080 OUT] [levin_protocol] -->> start_outer_call failed
2017-11-17 01:20:46.197 [P2P9]  WARN    net.dns src/common/dns_utils.cpp:487    WARNING: no two valid MoneroPulse DNS checkpoint records were received
2017-11-17 01:26:12.495 [P2P2]  WARN    net.p2p src/p2p/net_node.inl:1629       [216.155.136.170:18090 OUT] COMMAND_REQUEST_SUPPORT_FLAGS invoke failed. (-3, LEVIN_ERROR_CONNECTION_DESTROYED)
2017-11-17 01:27:08.536 [P2P7]  ERROR   verify  src/cryptonote_core/cryptonote_core.cpp:653     Transaction verification failed: <630d0a2f39803e71b297076b9afbf315571581dd9e0bf5d8ec16488316c53ef7>
2017-11-17 01:27:30.377 [P2P2]  WARN    net.p2p src/p2p/net_node.inl:1629       [62.210.104.31:18081 OUT] COMMAND_REQUEST_SUPPORT_FLAGS invoke failed. (-3, LEVIN_ERROR_CONNECTION_DESTROYED)
2017-11-17 01:28:31.571 [P2P4]  WARN    net.p2p src/p2p/net_node.inl:1629       [73.213.46.244:18080 OUT] COMMAND_REQUEST_SUPPORT_FLAGS invoke failed. (-3, LEVIN_ERROR_CONNECTION_DESTROYED)
2017-11-17 01:31:54.832 [P2P9]  ERROR   verify  src/cryptonote_core/cryptonote_core.cpp:653     Transaction verification failed: <1c3a3ba17092117c311d164e11fa1084947c596e1b8ffcc26a9739f195e64525>
2017-11-17 01:34:57.799 [P2P2]  WARN    net.p2p src/p2p/net_node.inl:1629       [192.99.30.103:18080 OUT] COMMAND_REQUEST_SUPPORT_FLAGS invoke failed. (-3, LEVIN_ERROR_CONNECTION_DESTROYED)
2017-11-17 01:39:12.478 [P2P4]  WARN    net.p2p src/p2p/net_node.inl:1629       [52.57.101.207:18080 OUT] COMMAND_REQUEST_SUPPORT_FLAGS invoke failed. (-3, LEVIN_ERROR_CONNECTION_DESTROYED)
2017-11-17 01:39:12.577 [P2P6]  ERROR   net     contrib/epee/include/net/levin_protocol_handler_async.h:289     [52.57.101.207:18080 OUT] [levin_protocol] -->> start_outer_call failed
2017-11-17 01:42:41.993 [P2P4]  ERROR   verify  src/cryptonote_core/cryptonote_core.cpp:653     Transaction verification failed: <fa69cbe355535afe1beb11c4497f1eb902031ed733fb4e62140171dd67d9895b>
2017-11-17 01:47:51.649 [P2P2]  WARN    net.p2p src/p2p/net_node.inl:1629       [139.162.74.83:18080 OUT] COMMAND_REQUEST_SUPPORT_FLAGS invoke failed. (-3, LEVIN_ERROR_CONNECTION_DESTROYED)
2017-11-17 01:48:12.063 [P2P6]  ERROR   verify  src/cryptonote_core/cryptonote_core.cpp:653     Transaction verification failed: <0c5ad74ab281599120e5b28ab690d6a9ad5295025c62de3337bbd8e2cbd6488f>
2017-11-17 01:48:12.063 [P2P5]  ERROR   verify  src/cryptonote_core/cryptonote_core.cpp:653     Transaction verification failed: <0c5ad74ab281599120e5b28ab690d6a9ad5295025c62de3337bbd8e2cbd6488f>
2017-11-17 01:48:12.652 [P2P6]  WARN    net.p2p src/p2p/net_node.inl:834        [78.47.74.29:18080 OUT] COMMAND_TIMED_SYNC invoke failed. (-3, LEVIN_ERROR_CONNECTION_DESTROYED)
2017-11-17 01:48:12.663 [P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:120  Exception: boost::exception_detail::clone_impl<boost::exception_detail::error_info_injector<std::out_of_range> >
2017-11-17 01:48:12.663 [P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:121  Unwound call stack:
2017-11-17 01:48:12.680 [P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:159      [1] monerod:__cxa_throw+0x106 [0x7e3446]
2017-11-17 01:48:12.680 [P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:159      [2] monerod:void boost::throw_exception<std::out_of_range>(std::out_of_range const&)+0x16e [0x59762e]
2017-11-17 01:48:12.681 [P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:159      [3] monerod:epee::levin::async_protocol_handler_config<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >::del_out_connections(unsigned long)+0x529 [0x5d9959]
2017-11-17 01:48:12.681 [P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:159      [4] monerod:nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::try_to_connect_and_handshake_with_new_peer(epee::net_utils::network_address const&, bool, unsigned long, nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::PeerType, unsigned long)+0x485 [0x6837f5]
2017-11-17 01:48:12.681 [P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:159      [5] monerod:nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::make_new_connection_from_peerlist(bool)+0xa09 [0x6857f9]
2017-11-17 01:48:12.681 [P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:159      [6] monerod:nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::make_expected_connections_count(nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::PeerType, unsigned long)+0x1e4 [0x686064]
2017-11-17 01:48:12.681 [P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:159      [7] monerod:nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::connections_maker()+0x182 [0x6868f2]
2017-11-17 01:48:12.681 [P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:159      [8] monerod:nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::idle_worker()+0x7c [0x58e69c]
2017-11-17 01:48:12.681 [P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:159      [9] monerod:epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::global_timer_handler(boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext_base>)+0x25 [0x5ba005]
2017-11-17 01:48:12.681 [P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:159      [10] monerod:boost::asio::detail::wait_handler<boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext_base> >, boost::_bi::list2<boost::_bi::value<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >*>, boost::_bi::value<boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext_base> > > > >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long)+0xfc [0x59244c]
2017-11-17 01:48:12.681 [P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:159      [11] monerod:epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread()+0x807 [0x5b4be7]
2017-11-17 01:48:12.681 [P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:159      [12] /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0+0x115d5 [0x7f50716d65d5]
2017-11-17 01:48:12.681 [P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:159      [13] /lib/x86_64-linux-gnu/libpthread.so.0+0x76ba [0x7f50706246ba]
2017-11-17 01:48:12.681 [P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:159      [14] /lib/x86_64-linux-gnu/libc.so.6:clone+0x6d [0x7f507035a3dd]
2017-11-17 01:48:12.681 [P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:159
2017-11-17 01:48:12.684 [P2P6]  ERROR   net     contrib/epee/include/net/abstract_tcp_server2.inl:776   Exception at server worker thread, what=Unable to find key in unordered_map.
2017-11-17 02:07:57.038 [P2P0]  ERROR   verify  src/cryptonote_core/cryptonote_core.cpp:653     Transaction verification failed: <2b9673bf808099f7c3d905a2ed5b0197d924518cc75d50dcbc848e74c35056f3>
2017-11-17 02:17:14.734 [P2P1]  ERROR   verify  src/cryptonote_core/cryptonote_core.cpp:653     Transaction verification failed: <8fb89a8063d194bb68f878b53a42fc5f94618f65d82040a9497151114ab39359>
2017-11-17 02:23:14.967 [P2P0]  WARN    net.dns src/common/dns_utils.cpp:487    WARNING: no two valid MoneroPulse DNS checkpoint records were received
2017-11-17 02:50:01.295 [P2P7]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154    ^[[1;33m[43.255.106.193:18080 OUT]  Synced 1444611/1444611^[[0m
2017-11-17 02:50:01.295 [P2P7]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1521    ^[[1;32mSYNCHRONIZED OK^[[0m
2017-11-17 03:24:27.326 [P2P5]  WARN    net.dns src/common/dns_utils.cpp:487    WARNING: no two valid MoneroPulse DNS checkpoint records were received
2017-11-17 04:25:08.365 [P2P6]  WARN    net.dns src/common/dns_utils.cpp:487    WARNING: no two valid MoneroPulse DNS checkpoint records were received
2017-11-17 06:20:58.792 [P2P1]  WARN    net.dns src/common/dns_utils.cpp:487    WARNING: no two valid MoneroPulse DNS checkpoint records were received
```

## moneromooo-monero | 2017-11-18T11:43:25+00:00
That's exactly the one I was suspecting. It's supposed to be fixed by f2939bdce8c86b0f96921f731184c361106390c8, do you have this one ?

## moneromooo-monero | 2017-11-18T11:45:27+00:00
It's not in 0.11.1.0, which you said you were using. I thought this bug was pretty rare, so I did not include it as I was not sure 100% sure it would not cause side effects. So you can apply it on top of 0.11.1.0 and run that.

## miningpoolhub | 2017-11-20T04:09:34+00:00
Okay. I updated one of my instance. Will monitor it for few days.

## miningpoolhub | 2017-11-21T01:37:53+00:00
It stuck again from new build.
Here's the log.

```
2017-11-20 16:09:12.772 [P2P2]  INFO    stacktrace      src/common/stack_trace.cpp:120  Exception: boost::exception_detail::clone_impl<boost::exception_detail::error_info_injector<std::out_of_range> >
2017-11-20 16:09:12.772 [P2P2]  INFO    stacktrace      src/common/stack_trace.cpp:121  Unwound call stack:
2017-11-20 16:09:12.778 [P2P2]  INFO    stacktrace      src/common/stack_trace.cpp:159      [1] monerod:__cxa_throw+0x106 [0x7e3446]
2017-11-20 16:09:12.778 [P2P2]  INFO    stacktrace      src/common/stack_trace.cpp:159      [2] monerod:void boost::throw_exception<std::out_of_range>(std::out_of_range const&)+0x16e [0x59762e]
2017-11-20 16:09:12.778 [P2P2]  INFO    stacktrace      src/common/stack_trace.cpp:159      [3] monerod:epee::levin::async_protocol_handler_config<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >::del_out_connections(unsigned long)+0x529 [0x5d9959]
2017-11-20 16:09:12.778 [P2P2]  INFO    stacktrace      src/common/stack_trace.cpp:159      [4] monerod:nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::try_to_connect_and_handshake_with_new_peer(epee::net_utils::network_address const&, bool, unsigned long, nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::PeerType, unsigned long)+0x485 [0x6837f5]
2017-11-20 16:09:12.778 [P2P2]  INFO    stacktrace      src/common/stack_trace.cpp:159      [5] monerod:nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::make_new_connection_from_peerlist(bool)+0xa09 [0x6857f9]
2017-11-20 16:09:12.778 [P2P2]  INFO    stacktrace      src/common/stack_trace.cpp:159      [6] monerod:nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::make_expected_connections_count(nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::PeerType, unsigned long)+0x1e4 [0x686064]
2017-11-20 16:09:12.778 [P2P2]  INFO    stacktrace      src/common/stack_trace.cpp:159      [7] monerod:nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::connections_maker()+0x182 [0x6868f2]
2017-11-20 16:09:12.778 [P2P2]  INFO    stacktrace      src/common/stack_trace.cpp:159      [8] monerod:nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::idle_worker()+0x7c [0x58e69c]
2017-11-20 16:09:12.778 [P2P2]  INFO    stacktrace      src/common/stack_trace.cpp:159      [9] monerod:epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::global_timer_handler(boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext_base>)+0x25 [0x5ba005]
2017-11-20 16:09:12.778 [P2P2]  INFO    stacktrace      src/common/stack_trace.cpp:159      [10] monerod:boost::asio::detail::wait_handler<boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext_base> >, boost::_bi::list2<boost::_bi::value<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >*>, boost::_bi::value<boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext_base> > > > >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long)+0xfc [0x59244c]
2017-11-20 16:09:12.778 [P2P2]  INFO    stacktrace      src/common/stack_trace.cpp:159      [11] monerod:epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread()+0x807 [0x5b4be7]
2017-11-20 16:09:12.778 [P2P2]  INFO    stacktrace      src/common/stack_trace.cpp:159      [12] /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0+0x115d5 [0x7f0e8bd055d5]
2017-11-20 16:09:12.778 [P2P2]  INFO    stacktrace      src/common/stack_trace.cpp:159      [13] /lib/x86_64-linux-gnu/libpthread.so.0+0x76ba [0x7f0e8ac536ba]
2017-11-20 16:09:12.778 [P2P2]  INFO    stacktrace      src/common/stack_trace.cpp:159      [14] /lib/x86_64-linux-gnu/libc.so.6:clone+0x6d [0x7f0e8a9893dd]
2017-11-20 16:09:12.778 [P2P2]  INFO    stacktrace      src/common/stack_trace.cpp:159
2017-11-20 16:09:12.781 [P2P2]  ERROR   net     contrib/epee/include/net/abstract_tcp_server2.inl:776   Exception at server worker thread, what=Unable to find key in unordered_map.
2017-11-20 16:17:03.887 [P2P0]  WARN    net.dns src/common/dns_utils.cpp:487    WARNING: no two valid MoneroPulse DNS checkpoint records were received
2017-11-20 16:21:00.352 [P2P9]  ERROR   verify  src/cryptonote_core/cryptonote_core.cpp:653     Transaction verification failed: <6c7814c0843a72ec6e00104fd51db657af795e3a8c8a6a06fa7ca47885a1f539>
2017-11-20 16:21:05.261 [P2P7]  ERROR   verify  src/cryptonote_core/cryptonote_core.cpp:653     Transaction verification failed: <8265d7a417738b9d934621f5fec8402655dbace8212ae8eae0e39b8276c252fd>
2017-11-20 16:25:13.445 [P2P8]  ERROR   verify  src/cryptonote_core/cryptonote_core.cpp:653     Transaction verification failed: <1f5edac6e2e3666dadfbce3f34ea474d71011315a5ed383c9d121f6071154d2c>
2017-11-20 17:17:21.753 [P2P9]  WARN    net.dns src/common/dns_utils.cpp:487    WARNING: no two valid MoneroPulse DNS checkpoint records were received
2017-11-20 18:17:41.665 [P2P0]  WARN    net.dns src/common/dns_utils.cpp:487    WARNING: no two valid MoneroPulse DNS checkpoint records were received
2017-11-20 19:17:58.184 [P2P1]  WARN    net.dns src/common/dns_utils.cpp:487    WARNING: no two valid MoneroPulse DNS checkpoint records were received
2017-11-20 20:19:08.770 [P2P8]  WARN    net.dns src/common/dns_utils.cpp:487    WARNING: no two valid MoneroPulse DNS checkpoint records were received
2017-11-20 21:24:34.956 [P2P6]  WARN    net.dns src/common/dns_utils.cpp:487    WARNING: no two valid MoneroPulse DNS checkpoint records were received
2017-11-20 21:33:22.351 [P2P5]  ERROR   verify  src/cryptonote_core/blockchain.cpp:2971 One of outputs for one of inputs has wrong tx.unlock_time = 1447344
2017-11-20 21:33:22.357 [P2P5]  ERROR   verify  src/cryptonote_core/blockchain.cpp:239  Failed to handle_output for output no = 5, with absolute offset 3395381
2017-11-20 21:33:22.357 [P2P5]  ERROR   verify  src/cryptonote_core/blockchain.cpp:2991 Failed to get output keys for tx with amount = 0.000000000000 and count indexes 6
2017-11-20 21:33:22.357 [P2P5]  ERROR   verify  src/cryptonote_core/blockchain.cpp:2597 Failed to check ring signature for tx <14c8d8dd1236f0848c765f4325cd4833f905a44cfdc5bea339b5d2fd08421f1a>  vin key with k_image: <b5bf5c597dda357f813a0298099c34d08d6f00062fc667e0eef98b516c69f431>  sig_index: 0
2017-11-20 21:33:22.357 [P2P5]  ERROR   verify  src/cryptonote_core/blockchain.cpp:2600   *pmax_used_block_height: 0
2017-11-20 21:33:22.358 [P2P5]  ERROR   verify  src/cryptonote_core/cryptonote_core.cpp:653     Transaction verification failed: <14c8d8dd1236f0848c765f4325cd4833f905a44cfdc5bea339b5d2fd08421f1a>
2017-11-20 23:01:01.349 [SRV_MAIN]      INFO    global  src/daemon/p2p.h:80     p2p net loop stopped
2017-11-20 23:01:01.350 [SRV_MAIN]      INFO    global  src/daemon/rpc.h:78     Stopping core rpc server...
2017-11-20 23:01:01.353 [SRV_MAIN]      INFO    global  src/daemon/daemon.cpp:145       Node stopped.
2017-11-20 23:01:01.354 [SRV_MAIN]      INFO    global  src/daemon/rpc.h:90     Deinitializing rpc server...
2017-11-20 23:01:01.354 [SRV_MAIN]      INFO    global  src/daemon/p2p.h:90     Deinitializing p2p...
2017-11-20 23:01:01.956 [SRV_MAIN]      INFO    global  src/daemon/core.h:89    Deinitializing core...
2017-11-20 23:01:01.984 [SRV_MAIN]      INFO    global  src/daemon/protocol.h:77        Stopping cryptonote protocol...
2017-11-20 23:01:01.984 [SRV_MAIN]      INFO    global  src/daemon/protocol.h:81        Cryptonote protocol stopped successfully
```

## moneromooo-monero | 2017-11-21T13:16:24+00:00
And you've double checked this is running f2939bdce8c86b0f96921f731184c361106390c8 right ?

## miningpoolhub | 2017-11-21T22:19:50+00:00
Sure.
I wonder why I'm the only one experiencing this issue.
Not all nodes stuck in my case. One of them stuck frequently.

## moneromooo-monero | 2017-11-22T09:15:52+00:00
Use the patch below, then run the "bad" node again with `--log-level 3,*throttle*:ERROR`, then paste the last 1000 lines to fpaste.org. This will generate a lot of stuff. Please keep the log, just in case the last 1000 lines aren't enough and I ask for more. Also, please make sure you're building with stack traces enabled (either libunwind or CLANG internal).

```
commit 7a047191ebee8453b8e00534fbb4c6ee6aa61983
Author: moneromooo-monero <moneromooo-monero@users.noreply.github.com>
Date:   Wed Nov 22 09:12:19 2017 +0000

    epee: some logs on connection handling

diff --git a/contrib/epee/include/net/levin_protocol_handler_async.h b/contrib/epee/include/net/levin_protocol_handler_async.h
index 7ad6d19..174ffe1 100644
--- a/contrib/epee/include/net/levin_protocol_handler_async.h
+++ b/contrib/epee/include/net/levin_protocol_handler_async.h
@@ -718,6 +718,7 @@ template<class t_connection_context>
 void async_protocol_handler_config<t_connection_context>::del_connection(async_protocol_handler<t_connection_context>* pconn)
 {
   CRITICAL_REGION_BEGIN(m_connects_lock);
+  try { LOG_PRINT_L0("Deleting connection " << pconn->get_connection_id()); throw "del"; } catch (...) {}
   m_connects.erase(pconn->get_connection_id());
   CRITICAL_REGION_END();
   m_pcommands_handler->on_connection_close(pconn->m_connection_context);
@@ -731,7 +732,10 @@ void async_protocol_handler_config<t_connection_context>::del_out_connections(si
        for (auto& c: m_connects)
        {
                if (!c.second->m_connection_context.m_is_income)
+               {
+LOG_PRINT_L0("del_out_connections: selecting " << c.first);
                        out_connections.push_back(c.first);
+               }
        }
        
        if (out_connections.size() == 0)
@@ -744,6 +748,7 @@ void async_protocol_handler_config<t_connection_context>::del_out_connections(si
        while (count > 0 && out_connections.size() > 0)
        {
                boost::uuids::uuid connection_id = *out_connections.begin();
+LOG_PRINT_L0("del_out_connections: going to delete " << connection_id << ", cur " << (m_connects.find(connection_id) != m_connects.end()));
                async_protocol_handler<t_connection_context> *connection = find_connection(connection_id);
                // we temporarily ref the connection so it doesn't drop from the m_connects table
                // when we close it
```

## miningpoolhub | 2017-11-28T18:53:29+00:00
@moneromooo-monero 
Thank you for detailed instruction.
I'm currently running some script to automatically restart stuck monero wallet because I'm using it for pool production service. I'll test it on other machine later.

## lasergoat | 2017-12-07T19:33:31+00:00
I have a similar issue in the gui client... not sure if this is the right place to mention this...


![monero-sync-issue](https://user-images.githubusercontent.com/15964/33734781-07a7fb42-db53-11e7-824b-02638fca11c5.gif)

It just keeps showing a small number like 20, 40 or 60 blocks and then switching to 53,000 or so.

Is this normal?

## moneromooo-monero | 2017-12-07T19:36:55+00:00
See https://github.com/monero-project/monero-core for this.

## DavidBruchmann | 2017-12-09T08:03:00+00:00
Without any proves I just want to post my impression about it:

when synchronizing seems stopping the priority of network connection changes from in to out - means the program is sending much more than receiving. I stopped the demon then and started again, then it's synchronizing again on my own PC. I assume there is a process that is sending data for others to synchronize, but that should be blocked till the own database is synchronized.
Sorry, if I'm mistaking completely.

## DavidBruchmann | 2017-12-09T08:06:20+00:00
@miningpoolhub why don't you just copy the synchronized databases from one device to another?
I synchronized a week now and finally finished, but a copy would enable you to start instantly.

## moneromooo-monero | 2017-12-09T11:50:01+00:00
Upload should not have impact on failing to sync.

## DavidBruchmann | 2017-12-09T16:56:02+00:00
yeah as newbie I never can tell much about it. But when I synchronized it happened at the same time.

## razorman8669 | 2017-12-11T18:23:26+00:00
@miningpoolhub I too am experiencing the issue:
the 0.11.1.0 daemon stays synchronized fine for a few days, and then, without any errors/exceptions, just stops staying up to date with the network.  after restarting the daemon, it catches back up and is fine for another few days, but then gets stuck again.

@moneromooo-monero I'm using the latest release version here: https://github.com/monero-project/monero/releases/tag/v0.11.1.0 (did not compile from source) for Ubuntu 16.04

I am going to restart with `--log-level 1,*p2p*:DEBUG,net.cn:DEBUG` and post my logs (if any) soon as it reproduces (might be around 2-3 days).

@miningpoolhub are you building from source using the 0.11.1.0 tag version?  or are you using the prebuilt binaries?  what OS are you using?  can you give more info about your environment please...

## razorman8669 | 2017-12-11T21:36:34+00:00
also, fwiw, it seems this guy had the same issue as well @miningpoolhub https://github.com/monero-project/monero/issues/2536

## miningpoolhub | 2017-12-19T04:28:55+00:00
@razorman8669 I built from source code. Seems exactly same thing is happening like you.
It happens even on electroneum wallet too (electroneum is monero forked coin)
FYI, I didn't experience this issue before the helium hydra release.

## moneromooo-monero | 2017-12-19T11:05:21+00:00
https://github.com/monero-project/monero/pull/2936 fixes the original problem differently. Run half your daemons with that one, and half without, and compare.

## moneromooo-monero | 2018-01-18T23:37:05+00:00
Any luck ? If no reply after some reasonable amount of time, I'll deem this fixed.

## razorman8669 | 2018-01-23T21:15:27+00:00
@moneromooo-monero I have had the `Atex` fix described in #2936 applied to 2 of my daemons for the last week and have not seen the described issue reappear, however, It can take much longer for the problem to surface so I am still unsure it's fully working yet.  ***on another note*** have you taken a look at this comment: https://github.com/monero-project/monero/pull/2936#issuecomment-356695949  I think there are issues with that PR which are unaddressed.

## moneromooo-monero | 2018-01-27T11:49:01+00:00
OK, I'll keep this open then, add a comment when you stop testing.
I've not seen the other comments, I guess they were added after it got merged, thanks.

## moneromooo-monero | 2018-03-07T15:02:54+00:00
https://github.com/monero-project/monero/pull/3308 also fixes a sync failure.

## pille | 2018-04-06T10:04:00+00:00
i had this buggy behavior on linux with 0.11 and that was fixed with 0.12. now after running one week, sync_info reports only alive peers.

## mmortal03 | 2018-04-06T18:27:51+00:00
Is this only an issue with 0.11, or is it still present in 0.12? I'm noticing similar behavior on 0.12, running monerod under Windows Subsystem for Linux for the first time. What I'm noticing is that running monerod under WSL does work (I got the firewall and port forwarding working), but it seems to slowly lag on my machine (not a fast machine, mind you), getting progressively behind the current block count over a number of hours, to the point where, if I don't restart the daemon, it will finally lock up where typing commands into it is unresponsive. I was thinking that this could just be that my machine isn't fast enough to handle the virtualization overhead of WSL, but then I came across this bug report, which sounds very similar. If I restart the daemon, it starts syncing properly again, before starting to lag yet again.

## miningpoolhub | 2018-05-05T03:31:33+00:00
Sync stuck today at 1565706 again.
I think this is not fixed still.

Someone reporting this issue on reddit.
https://www.reddit.com/r/Monero/comments/8h4rc1/whats_happening_at_block_1565706_or_1565707_for/
https://moneroexplorer.com/ stuck at 1565706 still.

## moneromooo-monero | 2018-05-09T10:13:02+00:00
There are a couple fixes in #3775 and #3788.

## moneromooo-monero | 2018-06-10T09:26:44+00:00
AFAIK, all such bugs are now fixed in 0.12.2.0.

+resolved

# Action History
- Created by: miningpoolhub | 2017-11-12T01:18:32+00:00
- Closed at: 2018-06-10T09:48:52+00:00
