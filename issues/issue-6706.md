---
title: Daemon often fails to shut down gracefully on Tails
source_url: https://github.com/monero-project/monero/issues/6706
author: tobtoht
assignees: []
labels: []
created_at: '2020-07-14T11:57:20+00:00'
updated_at: '2022-02-19T11:24:59+00:00'
type: issue
status: closed
closed_at: '2022-02-19T11:24:59+00:00'
---

# Original Description
> 2020-07-14 11:47:02.155	T BlockchainLMDB::get_block_timestamp
> 2020-07-14 11:47:02.155	T BlockchainLMDB::get_block_cumulative_difficulty  height: 2120673
> 2020-07-14 11:47:02.155	T BlockchainLMDB::get_block_timestamp
> 2020-07-14 11:47:02.155	T BlockchainLMDB::get_block_cumulative_difficulty  height: 2120674
> 2020-07-14 11:47:02.155	D Invalidating block template cache
> 2020-07-14 11:47:02.155	T Blockchain::cleanup_handle_incoming_blocks
> 2020-07-14 11:47:02.155	T BlockchainLMDB::batch_stop
> 2020-07-14 11:47:02.155	T batch transaction: committing...
> 2020-07-14 11:47:02.166	T mdb_txn_safe: destructor
> 2020-07-14 11:47:02.167	T batch transaction: end
> 2020-07-14 11:47:02.168	T BlockchainLMDB::prune_worker
> 2020-07-14 11:47:02.168	T mdb_txn_safe: abort()
> 2020-07-14 11:47:02.168	D Pruning not enabled, nothing to do
> 2020-07-14 11:47:02.168	T mdb_txn_safe: destructor
> 2020-07-14 11:47:02.169	T BlockchainLMDB::prune_worker
> 2020-07-14 11:47:02.169	T mdb_txn_safe: abort()
> 2020-07-14 11:47:02.169	D Pruning not enabled, nothing to do
> 2020-07-14 11:47:02.169	T mdb_txn_safe: destructor
> 2020-07-14 11:47:02.169	T BlockchainLMDB::for_all_txpool_txes
> 2020-07-14 11:47:02.169	T BlockchainLMDB::block_rtxn_start
> 2020-07-14 11:47:02.169	T mdb_txn_safe: destructor
> 2020-07-14 11:47:02.169	D miner::resume: 1 -> 0
> 2020-07-14 11:47:02.169	T Setting 00:04:49.443000 expiry
> 2020-07-14 11:47:02.169	E Setting timer on a shut down object

It then hangs here forever.

Typing exit once more produces the following output, but the program does not exit:

> exit
> 2020-07-14 12:17:34.748	D Read command: exit
> 2020-07-14 12:17:34.748	D [node] sending stop signal
> 2020-07-14 12:17:34.748	D [node] Stop signal sent
> 2020-07-14 12:17:34.748	T Miner has received stop signal
> 2020-07-14 12:17:34.748	T Not mining - nothing to stop
> Stop signal sent

Ran with v0.16.0.1, and: 
`DNS_PUBLIC=tcp torsocks ./monerod --p2p-bind-ip 127.0.0.1 --no-igd --rpc-bind-ip 127.0.0.1 --rpc-bind-port 17600 --log-level 4 --data-dir /home/amnesia/Persistent/.bitmonero`

# Discussion History
## zhang111111112 | 2020-07-14T14:54:52+00:00
Duplicate of https://github.com/monero-project/monero/issues/5098

You can use "killall -9 monerod" to end the process.

## moneromooo-monero | 2020-07-14T23:20:15+00:00
Run gdb on it (gdb /path/to/monerod \`pidof monerod\`) then: thread apply all bt


## tobtoht | 2020-07-14T23:47:11+00:00
```
(gdb) thread apply all bt

Thread 11 (Thread 0x71bfdd2f6700 (LWP 5518)):
#0  0x000071d7c1e5800c in pthread_cond_wait@@GLIBC_2.3.2 () from /lib/x86_64-linux-gnu/libpthread.so.0
#1  0x0000635800b0ca1d in tools::threadpool::run(bool) ()
#2  0x0000635800e7ed1d in thread_proxy ()
#3  0x000071d7c1e51fa3 in start_thread () from /lib/x86_64-linux-gnu/libpthread.so.0
#4  0x000071d7c1d824cf in clone () from /lib/x86_64-linux-gnu/libc.so.6

Thread 10 (Thread 0x71bfdffff700 (LWP 5509)):
#0  0x000071d7c1d7a037 in select () from /lib/x86_64-linux-gnu/libc.so.6
#1  0x000071d7c2018623 in ?? () from /usr/lib/x86_64-linux-gnu/torsocks/libtorsocks.so
#2  0x000071d7c2018838 in ?? () from /usr/lib/x86_64-linux-gnu/torsocks/libtorsocks.so
#3  0x000071d7c20192b0 in ?? () from /usr/lib/x86_64-linux-gnu/torsocks/libtorsocks.so
#4  0x000071d7c20129e1 in tsocks_connect () from /usr/lib/x86_64-linux-gnu/torsocks/libtorsocks.so
#5  0x00006358009910e5 in boost::asio::detail::reactive_socket_service_base::start_connect_op(boost::asio::detail::reactive_socket_service_base::base_implementation_type&, boost::asio::detail::reactor_op*, bool, sockaddr const*, unsigned long) ()
#6  0x00006358009cf7d6 in epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::try_connect(boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > >, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, boost::asio::basic_stream_socket<boost::asio::ip::tcp, boost::asio::stream_socket_service<boost::asio::ip::tcp> >&, boost::asio::ip::basic_endpoint<boost::asio::ip::tcp> const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, unsigned int, epee::net_utils::ssl_support_t) ()
#7  0x0000635800a0fef0 in epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::connect(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, unsigned int, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, epee::net_utils::ssl_support_t) ()
#8  0x0000635800a1180a in nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::public_connect(nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::network_zone&, epee::net_utils::network_address const&, epee::net_utils::ssl_support_t) ()
#9  0x0000635800a1e62c in nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::try_to_connect_and_handshake_with_new_peer(epee::net_utils::network_address const&, bool, unsigned long, nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::PeerType, unsigned long) ()
#10 0x0000635800a21a08 in nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::make_new_connection_from_peerlist(nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::network_zone&, bool) ()
#11 0x0000635800a22e64 in nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::make_expected_connections_count(nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::network_zone&, nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::PeerType, unsigned long) ()
#12 0x0000635800a24343 in nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::connections_maker() ()
#13 0x0000635800990043 in nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::idle_worker() ()
#14 0x00006358009b8839 in bool epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::global_timer_handler<boost::_bi::bind_t<bool, boost::_mfi::mf0<bool, nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> > >, boost::_bi::list1<boost::_bi::value<nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >*> > > >(boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext<boost::_bi::bind_t<bool, boost::_mfi::mf0<bool, nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> > >, boost::_bi::list1<boost::_bi::value<nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >*> > > > >) ()
#15 0x000063580099160b in boost::asio::detail::wait_handler<boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext<boost::_bi::bind_t<bool, boost::_mfi::mf0<bool, nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> > >, boost::_bi::list1<boost::_bi::value<nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >*> > > > > >, boost::_bi::list2<boost::_bi::value<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >*>, boost::_bi::value<boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext<boost::_bi::bind_t<bool, boost::_mfi::mf0<bool, nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> > >, boost::_bi::list1<boost::_bi::value<nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >*> > > > > > > > >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) ()
#16 0x00006358006f41b0 in boost::asio::detail::task_io_service::do_run_one(boost::asio::detail::scoped_lock<boost::asio::detail::posix_mutex>&, boost::asio::detail::task_io_service_thread_info&, boost::system::error_code const&) ()
#17 0x00006358009b709d in epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread() ()
#18 0x0000635800e7ed1d in thread_proxy ()
#19 0x000071d7c1e51fa3 in start_thread () from /lib/x86_64-linux-gnu/libpthread.so.0
--Type <RET> for more, q to quit, c to continue without paging--
#20 0x000071d7c1d824cf in clone () from /lib/x86_64-linux-gnu/libc.so.6

Thread 9 (Thread 0x71bff97f6700 (LWP 5506)):
#0  0x000071d7c1d77819 in poll () from /lib/x86_64-linux-gnu/libc.so.6
#1  0x0000635800bd8480 in zmq::signaler_t::wait(int) ()
#2  0x0000635800bca42f in zmq::mailbox_t::recv(zmq::command_t*, int) ()
#3  0x0000635800bdc7a2 in zmq::socket_base_t::process_commands(int, bool) ()
#4  0x0000635800bdc527 in zmq::socket_base_t::recv(zmq::msg_t*, int) ()
#5  0x0000635800bbae17 in s_recvmsg(zmq::socket_base_t*, zmq_msg_t*, int) ()
#6  0x0000635800bbb653 in zmq_msg_recv ()
#7  0x0000635800d8ec05 in net::zmq::receive[abi:cxx11](void*, int) ()
#8  0x0000635800b571a6 in cryptonote::rpc::ZmqServer::serve() ()
#9  0x0000635800e7ed1d in thread_proxy ()
#10 0x000071d7c1e51fa3 in start_thread () from /lib/x86_64-linux-gnu/libpthread.so.0
#11 0x000071d7c1d824cf in clone () from /lib/x86_64-linux-gnu/libc.so.6

Thread 8 (Thread 0x71bff9ff7700 (LWP 5505)):
#0  0x000071d7c1d827ef in epoll_wait () from /lib/x86_64-linux-gnu/libc.so.6
#1  0x0000635800bc8c06 in zmq::epoll_t::loop() ()
#2  0x0000635800bc8ec6 in zmq::epoll_t::worker_routine(void*) ()
#3  0x0000635800be6c61 in thread_routine ()
#4  0x000071d7c1e51fa3 in start_thread () from /lib/x86_64-linux-gnu/libpthread.so.0
#5  0x000071d7c1d824cf in clone () from /lib/x86_64-linux-gnu/libc.so.6

Thread 7 (Thread 0x71bffa7f8700 (LWP 5504)):
#0  0x000071d7c1d827ef in epoll_wait () from /lib/x86_64-linux-gnu/libc.so.6
#1  0x0000635800bc8c06 in zmq::epoll_t::loop() ()
#2  0x0000635800bc8ec6 in zmq::epoll_t::worker_routine(void*) ()
#3  0x0000635800be6c61 in thread_routine ()
#4  0x000071d7c1e51fa3 in start_thread () from /lib/x86_64-linux-gnu/libpthread.so.0
#5  0x000071d7c1d824cf in clone () from /lib/x86_64-linux-gnu/libc.so.6

Thread 6 (Thread 0x71bffaff9700 (LWP 5503)):
#0  0x000071d7c1e5800c in pthread_cond_wait@@GLIBC_2.3.2 () from /lib/x86_64-linux-gnu/libpthread.so.0
#1  0x00006358006d71a6 in boost::condition_variable::wait(boost::unique_lock<boost::mutex>&) ()
#2  0x00006358006da973 in bool epee::async_console_handler::run<epee::async_console_handler::run<boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::command_handler, boost::optional<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > const&>, boost::_bi::list2<boost::_bi::value<epee::console_handlers_binder*>, boost::arg<1> > > >(boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::command_handler, boost::optional<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > const&>, boost::_bi::list2<boost::_bi::value<epee::console_handlers_binder*>, boost::arg<1> > >, std::function<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > ()>, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::function<void ()>)::{lambda(boost::optional<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > const&)#1}>(std::function<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > ()>, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, epee::async_console_handler::run<boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::command_handler, boost::optional<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > const&>, boost::_bi::list2<boost::_bi::value<epee::console_handlers_binder*>, boost::arg<1> > > >(boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::command_handler, boost::optional<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > const&>, boost::_bi::list2<boost::_bi::value<epee::console_handlers_binder*>, boost::arg<1> > >, std::function<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > ()>, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::function<void ()>)::{lambda(boost::optional<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > const&)#1} const&, std::function<void ()>) ()
#3  0x00006358006db7a1 in epee::console_handlers_binder::run_handling(std::function<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > ()>, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::function<void ()>) ()
#4  0x00006358006d7aff in boost::detail::thread_data<boost::_bi::bind_t<bool, boost::_mfi::mf3<bool, epee::console_handlers_binder, std::function<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > ()>, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::function<void ()> >, boost::_bi::list4<boost::_bi::value<epee::console_handlers_binder*>, boost::_bi::value<std::function<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > ()> >, boost::_bi::value<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, boost::_bi::value<std::function<void ()> > > > >::run() ()
--Type <RET> for more, q to quit, c to continue without paging--
#5  0x0000635800e7ed1d in thread_proxy ()
#6  0x000071d7c1e51fa3 in start_thread () from /lib/x86_64-linux-gnu/libpthread.so.0
#7  0x000071d7c1d824cf in clone () from /lib/x86_64-linux-gnu/libc.so.6

Thread 5 (Thread 0x71bffb7fa700 (LWP 5502)):
#0  0x000071d7c1d7a037 in select () from /lib/x86_64-linux-gnu/libc.so.6
#1  0x00006358006d75b1 in epee::async_stdin_reader::reader_thread_func() ()
#2  0x0000635800e7ed1d in thread_proxy ()
#3  0x000071d7c1e51fa3 in start_thread () from /lib/x86_64-linux-gnu/libpthread.so.0
#4  0x000071d7c1d824cf in clone () from /lib/x86_64-linux-gnu/libc.so.6

Thread 4 (Thread 0x71bffc04e700 (LWP 5501)):
#0  0x000071d7c1e5800c in pthread_cond_wait@@GLIBC_2.3.2 () from /lib/x86_64-linux-gnu/libpthread.so.0
#1  0x00006358006f4117 in boost::asio::detail::task_io_service::do_run_one(boost::asio::detail::scoped_lock<boost::asio::detail::posix_mutex>&, boost::asio::detail::task_io_service_thread_info&, boost::system::error_code const&) ()
#2  0x0000635800704b05 in epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::worker_thread() ()
#3  0x0000635800e7ed1d in thread_proxy ()
#4  0x000071d7c1e51fa3 in start_thread () from /lib/x86_64-linux-gnu/libpthread.so.0
#5  0x000071d7c1d824cf in clone () from /lib/x86_64-linux-gnu/libc.so.6

Thread 3 (Thread 0x71bffc84f700 (LWP 5500)):
#0  0x000071d7c1d827ef in epoll_wait () from /lib/x86_64-linux-gnu/libc.so.6
#1  0x00006358006f369d in boost::asio::detail::epoll_reactor::run(bool, boost::asio::detail::op_queue<boost::asio::detail::task_io_service_operation>&) ()
#2  0x00006358006f3fb9 in boost::asio::detail::task_io_service::do_run_one(boost::asio::detail::scoped_lock<boost::asio::detail::posix_mutex>&, boost::asio::detail::task_io_service_thread_info&, boost::system::error_code const&) ()
#3  0x0000635800704b05 in epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::worker_thread() ()
#4  0x0000635800e7ed1d in thread_proxy ()
#5  0x000071d7c1e51fa3 in start_thread () from /lib/x86_64-linux-gnu/libpthread.so.0
#6  0x000071d7c1d824cf in clone () from /lib/x86_64-linux-gnu/libc.so.6

Thread 2 (Thread 0x71bffd851700 (LWP 5498)):
#0  0x000071d7c1e5800c in pthread_cond_wait@@GLIBC_2.3.2 () from /lib/x86_64-linux-gnu/libpthread.so.0
#1  0x0000635800a75058 in boost::asio::io_service::run() ()
#2  0x0000635800e7ed1d in thread_proxy ()
#3  0x000071d7c1e51fa3 in start_thread () from /lib/x86_64-linux-gnu/libpthread.so.0
#4  0x000071d7c1d824cf in clone () from /lib/x86_64-linux-gnu/libc.so.6

Thread 1 (Thread 0x71d7c1c83240 (LWP 5494)):
#0  0x000071d7c1e5800c in pthread_cond_wait@@GLIBC_2.3.2 () from /lib/x86_64-linux-gnu/libpthread.so.0
#1  0x00006358006d71a6 in boost::condition_variable::wait(boost::unique_lock<boost::mutex>&) ()
#2  0x0000635800e7f204 in boost::thread::join_noexcept() ()
#3  0x0000635800a1449b in epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::run_server(unsigned long, bool, boost::thread_attributes const&) ()
#4  0x0000635800a163ae in nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::run() ()
#5  0x00006358006f65a3 in daemonize::t_p2p::run() ()
#6  0x00006358006e528e in daemonize::t_daemon::run(bool) ()
#7  0x0000635800778691 in daemonize::t_executor::run_interactive(boost::program_options::variables_map const&) ()
#8  0x000063580077cafe in bool daemonizer::daemonize<daemonize::t_executor>(int, char const**, daemonize::t_executor&&, boost::program_options::variables_map const&) ()
#9  0x00006358006b15d6 in main ()
```

## moneromooo-monero | 2020-07-15T09:26:49+00:00
Stuck in connection as in the other bug. torsocks sucks (or boost). We set a connection timeout of 5 seconds IIRC, and either boost or torsocks is ignoring us here.

# Action History
- Created by: tobtoht | 2020-07-14T11:57:20+00:00
- Closed at: 2022-02-19T11:24:59+00:00
