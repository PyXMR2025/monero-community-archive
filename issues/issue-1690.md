---
title: Possible undefined behavior on initialization
source_url: https://github.com/monero-project/monero/issues/1690
author: ghost
assignees: []
labels:
- invalid
created_at: '2017-02-06T07:54:12+00:00'
updated_at: '2017-10-15T18:36:20+00:00'
type: issue
status: closed
closed_at: '2017-10-15T18:36:20+00:00'
---

# Original Description
As discussed with @vtnerd in #1595 (now closed), we're seeing this segfault during initialisation.

Note the `conditional jump or move depends on uninitialised value(s)` in `cryptonote_core.cpp`

```
nodey@odroidc2:~$ valgrind --max-stackframe=2097824 ~/monero/build/release/bin/monerod --no-igd
==1298== Memcheck, a memory error detector
==1298== Copyright (C) 2002-2015, and GNU GPL'd, by Julian Seward et al.
==1298== Using Valgrind-3.11.0 and LibVEX; rerun with -h for copyright info
==1298== Command: /home/nodey/monero/build/release/bin/monerod --no-igd
==1298== 
2017-01-30 03:13:01.597	         6e74830	INFO 	global	src/daemon/main.cpp:265	Monero 'Wolfram Warptangent' (v0.10.1.0-4629ead)
2017-01-30 03:13:01.747	         6e74830	INFO 	global	src/daemon/protocol.h:53	Initializing cryptonote protocol...
2017-01-30 03:13:01.752	         6e74830	INFO 	global	src/daemon/protocol.h:58	Cryptonote protocol initialized OK
==1298== Syscall param epoll_ctl(event) points to uninitialised byte(s)
==1298==    at 0x4951508: epoll_ctl (syscall-template.S:84)
==1298==    by 0x4E5EA3: boost::asio::io_service::service* boost::asio::detail::service_registry::create<boost::asio::detail::epoll_reactor>(boost::asio::io_service&) (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x661107: boost::asio::detail::service_registry::do_use_service(boost::asio::io_service::service::key const&, boost::asio::io_service::service* (*)(boost::asio::io_service&)) [clone .constprop.2011] (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x508057: boost::asio::io_service::service* boost::asio::detail::service_registry::create<boost::asio::socket_acceptor_service<boost::asio::ip::tcp> >(boost::asio::io_service&) (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x661107: boost::asio::detail::service_registry::do_use_service(boost::asio::io_service::service::key const&, boost::asio::io_service::service* (*)(boost::asio::io_service&)) [clone .constprop.2011] (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x5013EB: daemonize::t_daemon::t_daemon(boost::program_options::variables_map const&) (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x5EECDF: daemonize::t_executor::run_interactive(boost::program_options::variables_map const&) (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x4B84C3: main (in /home/nodey/monero/build/release/bin/monerod)
==1298==  Address 0xffefff464 is on thread 1's stack
==1298==  in frame #1, created by boost::asio::io_service::service* boost::asio::detail::service_registry::create<boost::asio::detail::epoll_reactor>(boost::asio::io_service&) (???:)
==1298== 
==1298== Syscall param epoll_ctl(event) points to uninitialised byte(s)
==1298==    at 0x4951508: epoll_ctl (syscall-template.S:84)
==1298==    by 0x4E5EE7: boost::asio::io_service::service* boost::asio::detail::service_registry::create<boost::asio::detail::epoll_reactor>(boost::asio::io_service&) (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x661107: boost::asio::detail::service_registry::do_use_service(boost::asio::io_service::service::key const&, boost::asio::io_service::service* (*)(boost::asio::io_service&)) [clone .constprop.2011] (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x508057: boost::asio::io_service::service* boost::asio::detail::service_registry::create<boost::asio::socket_acceptor_service<boost::asio::ip::tcp> >(boost::asio::io_service&) (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x661107: boost::asio::detail::service_registry::do_use_service(boost::asio::io_service::service::key const&, boost::asio::io_service::service* (*)(boost::asio::io_service&)) [clone .constprop.2011] (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x5013EB: daemonize::t_daemon::t_daemon(boost::program_options::variables_map const&) (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x5EECDF: daemonize::t_executor::run_interactive(boost::program_options::variables_map const&) (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x4B84C3: main (in /home/nodey/monero/build/release/bin/monerod)
==1298==  Address 0xffefff464 is on thread 1's stack
==1298==  in frame #1, created by boost::asio::io_service::service* boost::asio::detail::service_registry::create<boost::asio::detail::epoll_reactor>(boost::asio::io_service&) (???:)
==1298== 
2017-01-30 03:13:01.841	         6e74830	INFO 	global	src/daemon/p2p.h:63	Initializing p2p server...
==1298== Syscall param epoll_ctl(event) points to uninitialised byte(s)
==1298==    at 0x4951508: epoll_ctl (syscall-template.S:84)
==1298==    by 0x4EA5B7: boost::asio::basic_socket<boost::asio::ip::tcp, boost::asio::stream_socket_service<boost::asio::ip::tcp> >::open(boost::asio::ip::tcp const&) (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x4F5183: epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::init_server(unsigned int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x645A6B: nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::init(boost::program_options::variables_map const&) [clone .constprop.316] (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x5016D3: daemonize::t_daemon::t_daemon(boost::program_options::variables_map const&) (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x5EECDF: daemonize::t_executor::run_interactive(boost::program_options::variables_map const&) (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x4B84C3: main (in /home/nodey/monero/build/release/bin/monerod)
==1298==  Address 0xffeffe0c4 is on thread 1's stack
==1298==  in frame #1, created by boost::asio::basic_socket<boost::asio::ip::tcp, boost::asio::stream_socket_service<boost::asio::ip::tcp> >::open(boost::asio::ip::tcp const&) (???:)
==1298== 
==1298== Syscall param epoll_ctl(event) points to uninitialised byte(s)
==1298==    at 0x4951508: epoll_ctl (syscall-template.S:84)
==1298==    by 0x66DF4F: boost::asio::detail::epoll_reactor::start_op(int, int, boost::asio::detail::epoll_reactor::descriptor_state*&, boost::asio::detail::reactor_op*, bool, bool) [clone .constprop.2061] (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x4CE7B3: boost::asio::detail::reactive_socket_service_base::start_op(boost::asio::detail::reactive_socket_service_base::base_implementation_type&, int, boost::asio::detail::reactor_op*, bool, bool, bool) (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x4F5457: epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::init_server(unsigned int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x645A6B: nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::init(boost::program_options::variables_map const&) [clone .constprop.316] (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x5016D3: daemonize::t_daemon::t_daemon(boost::program_options::variables_map const&) (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x5EECDF: daemonize::t_executor::run_interactive(boost::program_options::variables_map const&) (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x4B84C3: main (in /home/nodey/monero/build/release/bin/monerod)
==1298==  Address 0xffeffe064 is on thread 1's stack
==1298==  in frame #1, created by boost::asio::detail::epoll_reactor::start_op(int, int, boost::asio::detail::epoll_reactor::descriptor_state*&, boost::asio::detail::reactor_op*, bool, bool) [clone .constprop.2061] (???:)
==1298== 
2017-01-30 03:13:05.699	         6e74830	INFO 	global	src/daemon/p2p.h:68	P2p server initialized OK
2017-01-30 03:13:05.709	         6e74830	INFO 	global	src/daemon/rpc.h:58	Initializing core rpc server...
==1298== Syscall param epoll_ctl(event) points to uninitialised byte(s)
==1298==    at 0x4951508: epoll_ctl (syscall-template.S:84)
==1298==    by 0x4EA5B7: boost::asio::basic_socket<boost::asio::ip::tcp, boost::asio::stream_socket_service<boost::asio::ip::tcp> >::open(boost::asio::ip::tcp const&) (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x55E03B: cryptonote::core_rpc_server::init(boost::program_options::variables_map const&) (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x50182F: daemonize::t_daemon::t_daemon(boost::program_options::variables_map const&) (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x5EECDF: daemonize::t_executor::run_interactive(boost::program_options::variables_map const&) (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x4B84C3: main (in /home/nodey/monero/build/release/bin/monerod)
==1298==  Address 0xffefff2b4 is on thread 1's stack
==1298==  in frame #1, created by boost::asio::basic_socket<boost::asio::ip::tcp, boost::asio::stream_socket_service<boost::asio::ip::tcp> >::open(boost::asio::ip::tcp const&) (???:)
==1298== 
==1298== Syscall param epoll_ctl(event) points to uninitialised byte(s)
==1298==    at 0x4951508: epoll_ctl (syscall-template.S:84)
==1298==    by 0x66DF4F: boost::asio::detail::epoll_reactor::start_op(int, int, boost::asio::detail::epoll_reactor::descriptor_state*&, boost::asio::detail::reactor_op*, bool, bool) [clone .constprop.2061] (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x4CE7B3: boost::asio::detail::reactive_socket_service_base::start_op(boost::asio::detail::reactive_socket_service_base::base_implementation_type&, int, boost::asio::detail::reactor_op*, bool, bool, bool) (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x64BDFF: void boost::asio::detail::reactive_socket_service<boost::asio::ip::tcp>::async_accept<boost::asio::basic_socket<boost::asio::ip::tcp, boost::asio::stream_socket_service<boost::asio::ip::tcp> >, boost::_bi::bind_t<void, boost::_mfi::mf1<void, epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&>, boost::_bi::list2<boost::_bi::value<epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >*>, boost::arg<1> (*)()> > >(boost::asio::detail::reactive_socket_service<boost::asio::ip::tcp>::implementation_type&, boost::asio::basic_socket<boost::asio::ip::tcp, boost::asio::stream_socket_service<boost::asio::ip::tcp> >&, boost::asio::ip::basic_endpoint<boost::asio::ip::tcp>*, boost::_bi::bind_t<void, boost::_mfi::mf1<void, epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&>, boost::_bi::list2<boost::_bi::value<epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >*>, boost::arg<1> (*)()> >&) [clone .constprop.885] (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x55E317: cryptonote::core_rpc_server::init(boost::program_options::variables_map const&) (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x50182F: daemonize::t_daemon::t_daemon(boost::program_options::variables_map const&) (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x5EECDF: daemonize::t_executor::run_interactive(boost::program_options::variables_map const&) (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x4B84C3: main (in /home/nodey/monero/build/release/bin/monerod)
==1298==  Address 0xffefff1d4 is on thread 1's stack
==1298==  in frame #1, created by boost::asio::detail::epoll_reactor::start_op(int, int, boost::asio::detail::epoll_reactor::descriptor_state*&, boost::asio::detail::reactor_op*, bool, bool) [clone .constprop.2061] (???:)
==1298== 
2017-01-30 03:13:05.766	         6e74830	INFO 	global	src/daemon/rpc.h:63	Core rpc server initialized OK on port: 18081
2017-01-30 03:13:05.776	         6e74830	INFO 	global	src/daemon/core.h:74	Initializing core...
2017-01-30 03:13:06.072	         6e74830	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:318	Loading blockchain from folder /home/nodey/.bitmonero/lmdb ...
==1298== Warning: set address range perms: large range [0x3939c000, 0x43939c000) (defined)
==1298== Conditional jump or move depends on uninitialised value(s)
==1298==    at 0x6071E0: cryptonote::core::update_checkpoints() [clone .part.127] [clone .constprop.953] (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x58E62F: cryptonote::core::init(boost::program_options::variables_map const&, cryptonote::test_options const*) (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x4FDADF: daemonize::t_daemon::run(bool) (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x5EECEB: daemonize::t_executor::run_interactive(boost::program_options::variables_map const&) (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x4B84C3: main (in /home/nodey/monero/build/release/bin/monerod)
==1298== 
2017-01-30 03:13:15.995	         6e74830	INFO 	global	src/daemon/core.h:79	Core initialized OK
2017-01-30 03:13:15.998	         6e74830	INFO 	global	src/daemon/rpc.h:68	Starting core rpc server...
==1298== Thread 3:
==1298== Syscall param epoll_pwait(sigmask) points to unaddressable byte(s)
==1298==    at 0x49512A4: epoll_pwait (epoll_pwait.c:42)
==1298==    by 0x66DB47: boost::asio::detail::epoll_reactor::run(bool, boost::asio::detail::op_queue<boost::asio::detail::task_io_service_operation>&) [clone .constprop.2067] (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x63BF7F: boost::asio::detail::task_io_service::run(boost::system::error_code&) [clone .constprop.1343] (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x4F0FFF: epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::worker_thread() (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x4CF7CF7: ??? (in /usr/lib/aarch64-linux-gnu/libboost_thread.so.1.58.0)
==1298==    by 0x4865FC3: start_thread (pthread_create.c:335)
==1298==    by 0x495110F: thread_start (clone.S:89)
==1298==  Address 0x0 is not stack'd, malloc'd or (recently) free'd
==1298== 
2017-01-30 03:13:16.081	[SRV_MAIN]	INFO 	global	src/daemon/rpc.h:73	Core rpc server started ok
2017-01-30 03:13:16.195	[SRV_MAIN]	INFO 	global	src/daemon/p2p.h:78	Starting p2p net loop...
==1298== Thread 8:
==1298== Syscall param epoll_pwait(sigmask) points to unaddressable byte(s)
==1298==    at 0x49512A4: epoll_pwait (epoll_pwait.c:42)
==1298==    by 0x66DB47: boost::asio::detail::epoll_reactor::run(bool, boost::asio::detail::op_queue<boost::asio::detail::task_io_service_operation>&) [clone .constprop.2067] (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x63BF7F: boost::asio::detail::task_io_service::run(boost::system::error_code&) [clone .constprop.1343] (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x4F168F: epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread() (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x4CF7CF7: ??? (in /usr/lib/aarch64-linux-gnu/libboost_thread.so.1.58.0)
==1298==    by 0x4865FC3: start_thread (pthread_create.c:335)
==1298==    by 0x495110F: thread_start (clone.S:89)
==1298==  Address 0x0 is not stack'd, malloc'd or (recently) free'd
==1298== 
==1298== Syscall param epoll_ctl(event) points to uninitialised byte(s)
==1298==    at 0x4951508: epoll_ctl (syscall-template.S:84)
==1298==    by 0x515E57: boost::asio::detail::reactive_socket_accept_op_base<boost::asio::basic_socket<boost::asio::ip::tcp, boost::asio::stream_socket_service<boost::asio::ip::tcp> >, boost::asio::ip::tcp>::do_perform(boost::asio::detail::reactor_op*) (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x4CA0DF: boost::asio::detail::epoll_reactor::descriptor_state::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x63C13F: boost::asio::detail::task_io_service::run(boost::system::error_code&) [clone .constprop.1343] (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x4F168F: epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread() (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x4CF7CF7: ??? (in /usr/lib/aarch64-linux-gnu/libboost_thread.so.1.58.0)
==1298==    by 0x4865FC3: start_thread (pthread_create.c:335)
==1298==    by 0x495110F: thread_start (clone.S:89)
==1298==  Address 0xcf7c554 is on thread 8's stack
==1298==  in frame #1, created by boost::asio::detail::reactive_socket_accept_op_base<boost::asio::basic_socket<boost::asio::ip::tcp, boost::asio::stream_socket_service<boost::asio::ip::tcp> >, boost::asio::ip::tcp>::do_perform(boost::asio::detail::reactor_op*) (???:)
==1298== 
==1298== Syscall param epoll_ctl(event) points to uninitialised byte(s)
==1298==    at 0x4951508: epoll_ctl (syscall-template.S:84)
==1298==    by 0x66DF4F: boost::asio::detail::epoll_reactor::start_op(int, int, boost::asio::detail::epoll_reactor::descriptor_state*&, boost::asio::detail::reactor_op*, bool, bool) [clone .constprop.2061] (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x4CE7B3: boost::asio::detail::reactive_socket_service_base::start_op(boost::asio::detail::reactive_socket_service_base::base_implementation_type&, int, boost::asio::detail::reactor_op*, bool, bool, bool) (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x4F4B7F: epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::handle_accept(boost::system::error_code const&) (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x50AF63: boost::asio::detail::reactive_socket_accept_op<boost::asio::basic_socket<boost::asio::ip::tcp, boost::asio::stream_socket_service<boost::asio::ip::tcp> >, boost::asio::ip::tcp, boost::_bi::bind_t<void, boost::_mfi::mf1<void, epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&>, boost::_bi::list2<boost::_bi::value<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >*>, boost::arg<1> (*)()> > >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x4CA1E3: boost::asio::detail::epoll_reactor::descriptor_state::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x63C13F: boost::asio::detail::task_io_service::run(boost::system::error_code&) [clone .constprop.1343] (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x4F168F: epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread() (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x4CF7CF7: ??? (in /usr/lib/aarch64-linux-gnu/libboost_thread.so.1.58.0)
==1298==    by 0x4865FC3: start_thread (pthread_create.c:335)
==1298==    by 0x495110F: thread_start (clone.S:89)
==1298==  Address 0xcf7c344 is on thread 8's stack
==1298==  in frame #1, created by boost::asio::detail::epoll_reactor::start_op(int, int, boost::asio::detail::epoll_reactor::descriptor_state*&, boost::asio::detail::reactor_op*, bool, bool) [clone .constprop.2061] (???:)
==1298== 
2017-01-30 03:13:16.490	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1029	
**********************************************************************
You are now synchronized with the network. You may now start monero-wallet-cli.

Use the "help" command to see the list of available commands.
**********************************************************************
==1298== Thread 16:
==1298== Syscall param epoll_ctl(event) points to uninitialised byte(s)
==1298==    at 0x4951508: epoll_ctl (syscall-template.S:84)
==1298==    by 0x4EA5B7: boost::asio::basic_socket<boost::asio::ip::tcp, boost::asio::stream_socket_service<boost::asio::ip::tcp> >::open(boost::asio::ip::tcp const&) (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x523FBF: nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::handle_handshake(int, nodetool::COMMAND_HANDSHAKE_T<cryptonote::CORE_SYNC_DATA>::request&, nodetool::COMMAND_HANDSHAKE_T<cryptonote::CORE_SYNC_DATA>::response&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&) (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x64C82F: int nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::handle_invoke_map<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >(bool, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&, bool&) [clone .constprop.829] (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x511BB7: epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >::handle_recv(void const*, unsigned long) (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x4F00EB: epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::handle_read(boost::system::error_code const&, unsigned long) (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x50CE0F: boost::asio::detail::completion_handler<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > > >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x50DBEB: boost::asio::detail::reactive_socket_recv_op<boost::asio::mutable_buffers_1, boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running> >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x63C13F: boost::asio::detail::task_io_service::run(boost::system::error_code&) [clone .constprop.1343] (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x4F168F: epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread() (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x4CF7CF7: ??? (in /usr/lib/aarch64-linux-gnu/libboost_thread.so.1.58.0)
==1298==    by 0x4865FC3: start_thread (pthread_create.c:335)
==1298==  Address 0xf77ad04 is on thread 16's stack
==1298==  in frame #1, created by boost::asio::basic_socket<boost::asio::ip::tcp, boost::asio::stream_socket_service<boost::asio::ip::tcp> >::open(boost::asio::ip::tcp const&) (???:)
==1298== 
==1298== Syscall param epoll_ctl(event) points to uninitialised byte(s)
==1298==    at 0x4951508: epoll_ctl (syscall-template.S:84)
==1298==    by 0x66DF4F: boost::asio::detail::epoll_reactor::start_op(int, int, boost::asio::detail::epoll_reactor::descriptor_state*&, boost::asio::detail::reactor_op*, bool, bool) [clone .constprop.2061] (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x660E4B: boost::asio::detail::reactive_socket_service_base::start_connect_op(boost::asio::detail::reactive_socket_service_base::base_implementation_type&, boost::asio::detail::reactor_op*, bool, sockaddr const*, unsigned long) [clone .constprop.2035] (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x5243B3: nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::handle_handshake(int, nodetool::COMMAND_HANDSHAKE_T<cryptonote::CORE_SYNC_DATA>::request&, nodetool::COMMAND_HANDSHAKE_T<cryptonote::CORE_SYNC_DATA>::response&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&) (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x64C82F: int nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::handle_invoke_map<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >(bool, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&, bool&) [clone .constprop.829] (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x511BB7: epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >::handle_recv(void const*, unsigned long) (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x4F00EB: epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::handle_read(boost::system::error_code const&, unsigned long) (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x50CE0F: boost::asio::detail::completion_handler<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > > >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x50DBEB: boost::asio::detail::reactive_socket_recv_op<boost::asio::mutable_buffers_1, boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running> >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x63C13F: boost::asio::detail::task_io_service::run(boost::system::error_code&) [clone .constprop.1343] (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x4F168F: epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread() (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x4CF7CF7: ??? (in /usr/lib/aarch64-linux-gnu/libboost_thread.so.1.58.0)
==1298==  Address 0xf77aca4 is on thread 16's stack
==1298==  in frame #1, created by boost::asio::detail::epoll_reactor::start_op(int, int, boost::asio::detail::epoll_reactor::descriptor_state*&, boost::asio::detail::reactor_op*, bool, bool) [clone .constprop.2061] (???:)
==1298== 
2017-01-30 03:13:17.265	[P2P9]	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:1027	
**********************************************************************
The daemon will start synchronizing with the network. It may take up to several hours.

You can set the level of process detailization* through "set_log <level|categories>" command*,
where <level> is between 0 (no details) and 4 (very verbose), or custom category based levels (eg, *:WARNING)

Use the "help" command to see the list of available commands.
**********************************************************************

==1298== Thread 8:
==1298== Syscall param epoll_ctl(event) points to uninitialised byte(s)
==1298==    at 0x4951508: epoll_ctl (syscall-template.S:84)
==1298==    by 0x4EA5B7: boost::asio::basic_socket<boost::asio::ip::tcp, boost::asio::stream_socket_service<boost::asio::ip::tcp> >::open(boost::asio::ip::tcp const&) (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x60B897: epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::connect(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, unsigned int, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&) [clone .constprop.1082] (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x60CE87: nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::try_to_connect_and_handshake_with_new_peer(nodetool::net_address const&, bool, unsigned long, bool) [clone .constprop.1078] (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x60EDAF: nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::make_new_connection_from_peerlist(bool) [clone .constprop.1074] (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x60F11B: nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::make_expected_connections_count(bool, unsigned long) [clone .part.4611] [clone .constprop.1073] (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x4E76B7: nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::connections_maker() (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x4E4D37: nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::idle_worker() (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x4EAAB3: epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::global_timer_handler(boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext_base>) (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x50B293: boost::asio::detail::wait_handler<boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext_base> >, boost::_bi::list2<boost::_bi::value<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >*>, boost::_bi::value<boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext_base> > > > >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x63C13F: boost::asio::detail::task_io_service::run(boost::system::error_code&) [clone .constprop.1343] (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x4F168F: epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread() (in /home/nodey/monero/build/release/bin/monerod)
==1298==  Address 0xcf7ba84 is on thread 8's stack
==1298==  in frame #1, created by boost::asio::basic_socket<boost::asio::ip::tcp, boost::asio::stream_socket_service<boost::asio::ip::tcp> >::open(boost::asio::ip::tcp const&) (???:)
==1298== 
==1298== Syscall param epoll_ctl(event) points to uninitialised byte(s)
==1298==    at 0x4951508: epoll_ctl (syscall-template.S:84)
==1298==    by 0x66DF4F: boost::asio::detail::epoll_reactor::start_op(int, int, boost::asio::detail::epoll_reactor::descriptor_state*&, boost::asio::detail::reactor_op*, bool, bool) [clone .constprop.2061] (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x660E4B: boost::asio::detail::reactive_socket_service_base::start_connect_op(boost::asio::detail::reactive_socket_service_base::base_implementation_type&, boost::asio::detail::reactor_op*, bool, sockaddr const*, unsigned long) [clone .constprop.2035] (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x60BAAB: epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::connect(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, unsigned int, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&) [clone .constprop.1082] (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x60CE87: nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::try_to_connect_and_handshake_with_new_peer(nodetool::net_address const&, bool, unsigned long, bool) [clone .constprop.1078] (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x60EDAF: nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::make_new_connection_from_peerlist(bool) [clone .constprop.1074] (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x60F11B: nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::make_expected_connections_count(bool, unsigned long) [clone .part.4611] [clone .constprop.1073] (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x4E76B7: nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::connections_maker() (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x4E4D37: nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::idle_worker() (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x4EAAB3: epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::global_timer_handler(boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext_base>) (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x50B293: boost::asio::detail::wait_handler<boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext_base> >, boost::_bi::list2<boost::_bi::value<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >*>, boost::_bi::value<boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext_base> > > > >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x63C13F: boost::asio::detail::task_io_service::run(boost::system::error_code&) [clone .constprop.1343] (in /home/nodey/monero/build/release/bin/monerod)
==1298==  Address 0xcf7ba24 is on thread 8's stack
==1298==  in frame #1, created by boost::asio::detail::epoll_reactor::start_op(int, int, boost::asio::detail::epoll_reactor::descriptor_state*&, boost::asio::detail::reactor_op*, bool, bool) [clone .constprop.2061] (???:)
==1298== 
2017-01-30 03:13:41.864	[P2P9]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:288	[212.20.7.188:52757 INC] Sync data returned a new top block candidate: 1234822 -> 1009962 [Your node is 224860 blocks (312 days) ahead] 
SYNCHRONIZATION started
2017-01-30 03:13:53.481	[P2P9]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:288	[91.107.12.146:64449 INC] Sync data returned a new top block candidate: 1234822 -> 1009962 [Your node is 224860 blocks (312 days) ahead] 
SYNCHRONISATION started
```

# Discussion History
## moneromooo-monero | 2017-02-06T21:53:30+00:00
This is not a segfault. Please try to use the correct terms, or it makes people waste time debugging (not here, since you also give the valgrind logs, but in general it's infuriating).

The using uninitialized data thing seems like a bona fide bug, yes.

Do you see this also without the easylogging patches ?

## vtnerd | 2017-02-07T02:19:50+00:00
I have been seeing a segfault on v0.10.0 and v0.10.1 on my Gentoo VM. I will gather more information from a trunk build, but part of the trouble is that it only occurs on the first or second launch from a cold boot.

## vtnerd | 2017-02-08T02:55:24+00:00
@NanoAkron  can you apply [this patch](https://github.com/monero-project/monero/pull/1696), and see if the valgrind error still persists?

## ghost | 2017-02-08T15:15:07+00:00
@vtnerd Will test at home tonight

## ghost | 2017-02-09T06:25:05+00:00
Oddly I can't test your PR at the moment because I'm now getting that regex issue from current master, despite PR #1674. I recently changed from GCC 5.4.1 to 6.2.0, but I can't quite see why that would do anything. Testing.

## ghost | 2017-02-10T09:17:11+00:00
@vtnerd Valgrind with your latest PR below. Note it still contains `==24636== Conditional jump or move depends on uninitialised value(s)`

```
nodey@odroidc2:~$ valgrind --max-stackframe=2097824 ~/monero/build/release/bin/monerod --no-igd
==24636== Memcheck, a memory error detector
==24636== Copyright (C) 2002-2015, and GNU GPL'd, by Julian Seward et al.
==24636== Using Valgrind-3.11.0 and LibVEX; rerun with -h for copyright info
==24636== Command: /home/nodey/monero/build/release/bin/monerod --no-igd
==24636== 
2017-02-10 09:15:05.759	         6e7b3b0	INFO 	global	src/daemon/main.cpp:265	Monero 'Wolfram Warptangent' (v0.10.1.0-99ee3fd)
2017-02-10 09:15:05.914	         6e7b3b0	INFO 	global	src/daemon/protocol.h:55	Initializing cryptonote protocol...
2017-02-10 09:15:05.919	         6e7b3b0	INFO 	global	src/daemon/protocol.h:60	Cryptonote protocol initialized OK
==24636== Syscall param epoll_ctl(event) points to uninitialised byte(s)
==24636==    at 0x4951508: epoll_ctl (syscall-template.S:84)
==24636==    by 0x52B163: boost::asio::io_service::service* boost::asio::detail::service_registry::create<boost::asio::detail::epoll_reactor>(boost::asio::io_service&) (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x62D0EF: boost::asio::detail::service_registry::do_use_service(boost::asio::io_service::service::key const&, boost::asio::io_service::service* (*)(boost::asio::io_service&)) [clone .constprop.2012] (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x50950F: boost::asio::io_service::service* boost::asio::detail::service_registry::create<boost::asio::socket_acceptor_service<boost::asio::ip::tcp> >(boost::asio::io_service&) (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x62D0EF: boost::asio::detail::service_registry::do_use_service(boost::asio::io_service::service::key const&, boost::asio::io_service::service* (*)(boost::asio::io_service&)) [clone .constprop.2012] (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x505C1B: daemonize::t_daemon::t_daemon(boost::program_options::variables_map const&) (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x5AEEEF: daemonize::t_executor::run_interactive(boost::program_options::variables_map const&) (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x4B71BF: main (in /home/nodey/monero/build/release/bin/monerod)
==24636==  Address 0xffefff454 is on thread 1's stack
==24636==  in frame #1, created by boost::asio::io_service::service* boost::asio::detail::service_registry::create<boost::asio::detail::epoll_reactor>(boost::asio::io_service&) (???:)
==24636== 
==24636== Syscall param epoll_ctl(event) points to uninitialised byte(s)
==24636==    at 0x4951508: epoll_ctl (syscall-template.S:84)
==24636==    by 0x52B1A7: boost::asio::io_service::service* boost::asio::detail::service_registry::create<boost::asio::detail::epoll_reactor>(boost::asio::io_service&) (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x62D0EF: boost::asio::detail::service_registry::do_use_service(boost::asio::io_service::service::key const&, boost::asio::io_service::service* (*)(boost::asio::io_service&)) [clone .constprop.2012] (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x50950F: boost::asio::io_service::service* boost::asio::detail::service_registry::create<boost::asio::socket_acceptor_service<boost::asio::ip::tcp> >(boost::asio::io_service&) (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x62D0EF: boost::asio::detail::service_registry::do_use_service(boost::asio::io_service::service::key const&, boost::asio::io_service::service* (*)(boost::asio::io_service&)) [clone .constprop.2012] (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x505C1B: daemonize::t_daemon::t_daemon(boost::program_options::variables_map const&) (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x5AEEEF: daemonize::t_executor::run_interactive(boost::program_options::variables_map const&) (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x4B71BF: main (in /home/nodey/monero/build/release/bin/monerod)
==24636==  Address 0xffefff454 is on thread 1's stack
==24636==  in frame #1, created by boost::asio::io_service::service* boost::asio::detail::service_registry::create<boost::asio::detail::epoll_reactor>(boost::asio::io_service&) (???:)
==24636== 
2017-02-10 09:15:06.009	         6e7b3b0	INFO 	global	src/daemon/p2p.h:63	Initializing p2p server...
==24636== Syscall param epoll_ctl(event) points to uninitialised byte(s)
==24636==    at 0x4951508: epoll_ctl (syscall-template.S:84)
==24636==    by 0x5304F7: boost::asio::basic_socket<boost::asio::ip::tcp, boost::asio::stream_socket_service<boost::asio::ip::tcp> >::open(boost::asio::ip::tcp const&) (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x53910B: epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::init_server(unsigned int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x65478F: nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::init(boost::program_options::variables_map const&) [clone .constprop.320] (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x505F03: daemonize::t_daemon::t_daemon(boost::program_options::variables_map const&) (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x5AEEEF: daemonize::t_executor::run_interactive(boost::program_options::variables_map const&) (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x4B71BF: main (in /home/nodey/monero/build/release/bin/monerod)
==24636==  Address 0xffeffe024 is on thread 1's stack
==24636==  in frame #1, created by boost::asio::basic_socket<boost::asio::ip::tcp, boost::asio::stream_socket_service<boost::asio::ip::tcp> >::open(boost::asio::ip::tcp const&) (???:)
==24636== 
==24636== Syscall param epoll_ctl(event) points to uninitialised byte(s)
==24636==    at 0x4951508: epoll_ctl (syscall-template.S:84)
==24636==    by 0x66798F: boost::asio::detail::epoll_reactor::start_op(int, int, boost::asio::detail::epoll_reactor::descriptor_state*&, boost::asio::detail::reactor_op*, bool, bool) [clone .constprop.2054] (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x4CEBB3: boost::asio::detail::reactive_socket_service_base::start_op(boost::asio::detail::reactive_socket_service_base::base_implementation_type&, int, boost::asio::detail::reactor_op*, bool, bool, bool) (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x5393CF: epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::init_server(unsigned int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x65478F: nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::init(boost::program_options::variables_map const&) [clone .constprop.320] (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x505F03: daemonize::t_daemon::t_daemon(boost::program_options::variables_map const&) (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x5AEEEF: daemonize::t_executor::run_interactive(boost::program_options::variables_map const&) (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x4B71BF: main (in /home/nodey/monero/build/release/bin/monerod)
==24636==  Address 0xffeffdfc4 is on thread 1's stack
==24636==  in frame #1, created by boost::asio::detail::epoll_reactor::start_op(int, int, boost::asio::detail::epoll_reactor::descriptor_state*&, boost::asio::detail::reactor_op*, bool, bool) [clone .constprop.2054] (???:)
==24636== 
2017-02-10 09:15:10.350	         6e7b3b0	INFO 	global	src/daemon/p2p.h:68	P2p server initialized OK
2017-02-10 09:15:10.360	         6e7b3b0	INFO 	global	src/daemon/rpc.h:58	Initializing core rpc server...
==24636== Syscall param epoll_ctl(event) points to uninitialised byte(s)
==24636==    at 0x4951508: epoll_ctl (syscall-template.S:84)
==24636==    by 0x5304F7: boost::asio::basic_socket<boost::asio::ip::tcp, boost::asio::stream_socket_service<boost::asio::ip::tcp> >::open(boost::asio::ip::tcp const&) (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x57D953: cryptonote::core_rpc_server::init(boost::program_options::variables_map const&) (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x50605F: daemonize::t_daemon::t_daemon(boost::program_options::variables_map const&) (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x5AEEEF: daemonize::t_executor::run_interactive(boost::program_options::variables_map const&) (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x4B71BF: main (in /home/nodey/monero/build/release/bin/monerod)
==24636==  Address 0xffefff2a4 is on thread 1's stack
==24636==  in frame #1, created by boost::asio::basic_socket<boost::asio::ip::tcp, boost::asio::stream_socket_service<boost::asio::ip::tcp> >::open(boost::asio::ip::tcp const&) (???:)
==24636== 
==24636== Syscall param epoll_ctl(event) points to uninitialised byte(s)
==24636==    at 0x4951508: epoll_ctl (syscall-template.S:84)
==24636==    by 0x66798F: boost::asio::detail::epoll_reactor::start_op(int, int, boost::asio::detail::epoll_reactor::descriptor_state*&, boost::asio::detail::reactor_op*, bool, bool) [clone .constprop.2054] (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x4CEBB3: boost::asio::detail::reactive_socket_service_base::start_op(boost::asio::detail::reactive_socket_service_base::base_implementation_type&, int, boost::asio::detail::reactor_op*, bool, bool, bool) (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x663ECF: void boost::asio::detail::reactive_socket_service<boost::asio::ip::tcp>::async_accept<boost::asio::basic_socket<boost::asio::ip::tcp, boost::asio::stream_socket_service<boost::asio::ip::tcp> >, boost::_bi::bind_t<void, boost::_mfi::mf1<void, epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&>, boost::_bi::list2<boost::_bi::value<epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >*>, boost::arg<1> (*)()> > >(boost::asio::detail::reactive_socket_service<boost::asio::ip::tcp>::implementation_type&, boost::asio::basic_socket<boost::asio::ip::tcp, boost::asio::stream_socket_service<boost::asio::ip::tcp> >&, boost::asio::ip::basic_endpoint<boost::asio::ip::tcp>*, boost::_bi::bind_t<void, boost::_mfi::mf1<void, epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&>, boost::_bi::list2<boost::_bi::value<epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >*>, boost::arg<1> (*)()> >&) [clone .constprop.891] (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x57DC2F: cryptonote::core_rpc_server::init(boost::program_options::variables_map const&) (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x50605F: daemonize::t_daemon::t_daemon(boost::program_options::variables_map const&) (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x5AEEEF: daemonize::t_executor::run_interactive(boost::program_options::variables_map const&) (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x4B71BF: main (in /home/nodey/monero/build/release/bin/monerod)
==24636==  Address 0xffefff1c4 is on thread 1's stack
==24636==  in frame #1, created by boost::asio::detail::epoll_reactor::start_op(int, int, boost::asio::detail::epoll_reactor::descriptor_state*&, boost::asio::detail::reactor_op*, bool, bool) [clone .constprop.2054] (???:)
==24636== 
2017-02-10 09:15:10.419	         6e7b3b0	INFO 	global	src/daemon/rpc.h:63	Core rpc server initialized OK on port: 18081
2017-02-10 09:15:10.434	         6e7b3b0	INFO 	global	src/daemon/core.h:74	Initializing core...
2017-02-10 09:15:10.568	         6e7b3b0	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:327	Loading blockchain from folder /home/nodey/.bitmonero/lmdb ...
==24636== Warning: set address range perms: large range [0x3939c000, 0x47939c000) (defined)
==24636== Conditional jump or move depends on uninitialised value(s)
==24636==    at 0x65DDB8: cryptonote::core::update_checkpoints() [clone .part.129] [clone .constprop.959] (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x56927B: cryptonote::core::init(boost::program_options::variables_map const&, cryptonote::test_options const*) (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x5023B7: daemonize::t_daemon::run(bool) (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x5AEEFB: daemonize::t_executor::run_interactive(boost::program_options::variables_map const&) (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x4B71BF: main (in /home/nodey/monero/build/release/bin/monerod)
==24636== 
2017-02-10 09:15:26.221	         6e7b3b0	INFO 	global	src/daemon/core.h:79	Core initialized OK
2017-02-10 09:15:26.224	         6e7b3b0	INFO 	global	src/daemon/rpc.h:68	Starting core rpc server...
==24636== Thread 3:
==24636== Syscall param epoll_pwait(sigmask) points to unaddressable byte(s)
==24636==    at 0x49512A4: epoll_pwait (epoll_pwait.c:42)
==24636==    by 0x667587: boost::asio::detail::epoll_reactor::run(bool, boost::asio::detail::op_queue<boost::asio::detail::task_io_service_operation>&) [clone .constprop.2060] (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x6220AF: boost::asio::detail::task_io_service::run(boost::system::error_code&) [clone .constprop.1363] (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x535B77: epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::worker_thread() (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x4D0ACF7: ??? (in /usr/lib/aarch64-linux-gnu/libboost_thread.so.1.58.0)
==24636==    by 0x4865FC3: start_thread (pthread_create.c:335)
==24636==    by 0x495110F: thread_start (clone.S:89)
==24636==  Address 0x0 is not stack'd, malloc'd or (recently) free'd
==24636== 
2017-02-10 09:15:26.308	[SRV_MAIN]	INFO 	global	src/daemon/rpc.h:73	Core rpc server started ok
2017-02-10 09:15:26.421	[SRV_MAIN]	INFO 	global	src/daemon/p2p.h:78	Starting p2p net loop...
==24636== Thread 8:
==24636== Syscall param epoll_pwait(sigmask) points to unaddressable byte(s)
==24636==    at 0x49512A4: epoll_pwait (epoll_pwait.c:42)
==24636==    by 0x667587: boost::asio::detail::epoll_reactor::run(bool, boost::asio::detail::op_queue<boost::asio::detail::task_io_service_operation>&) [clone .constprop.2060] (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x6220AF: boost::asio::detail::task_io_service::run(boost::system::error_code&) [clone .constprop.1363] (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x536207: epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread() (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x4D0ACF7: ??? (in /usr/lib/aarch64-linux-gnu/libboost_thread.so.1.58.0)
==24636==    by 0x4865FC3: start_thread (pthread_create.c:335)
==24636==    by 0x495110F: thread_start (clone.S:89)
==24636==  Address 0x0 is not stack'd, malloc'd or (recently) free'd
==24636== 
==24636== Syscall param epoll_ctl(event) points to uninitialised byte(s)
==24636==    at 0x4951508: epoll_ctl (syscall-template.S:84)
==24636==    by 0x516FDF: boost::asio::detail::reactive_socket_accept_op_base<boost::asio::basic_socket<boost::asio::ip::tcp, boost::asio::stream_socket_service<boost::asio::ip::tcp> >, boost::asio::ip::tcp>::do_perform(boost::asio::detail::reactor_op*) (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x4CA2D7: boost::asio::detail::epoll_reactor::descriptor_state::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x62226F: boost::asio::detail::task_io_service::run(boost::system::error_code&) [clone .constprop.1363] (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x536207: epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread() (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x4D0ACF7: ??? (in /usr/lib/aarch64-linux-gnu/libboost_thread.so.1.58.0)
==24636==    by 0x4865FC3: start_thread (pthread_create.c:335)
==24636==    by 0x495110F: thread_start (clone.S:89)
==24636==  Address 0xcf82554 is on thread 8's stack
==24636==  in frame #1, created by boost::asio::detail::reactive_socket_accept_op_base<boost::asio::basic_socket<boost::asio::ip::tcp, boost::asio::stream_socket_service<boost::asio::ip::tcp> >, boost::asio::ip::tcp>::do_perform(boost::asio::detail::reactor_op*) (???:)
==24636== 
==24636== Syscall param epoll_ctl(event) points to uninitialised byte(s)
==24636==    at 0x4951508: epoll_ctl (syscall-template.S:84)
==24636==    by 0x66798F: boost::asio::detail::epoll_reactor::start_op(int, int, boost::asio::detail::epoll_reactor::descriptor_state*&, boost::asio::detail::reactor_op*, bool, bool) [clone .constprop.2054] (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x4CEBB3: boost::asio::detail::reactive_socket_service_base::start_op(boost::asio::detail::reactive_socket_service_base::base_implementation_type&, int, boost::asio::detail::reactor_op*, bool, bool, bool) (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x538B07: epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::handle_accept(boost::system::error_code const&) (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x50A8D3: boost::asio::detail::reactive_socket_accept_op<boost::asio::basic_socket<boost::asio::ip::tcp, boost::asio::stream_socket_service<boost::asio::ip::tcp> >, boost::asio::ip::tcp, boost::_bi::bind_t<void, boost::_mfi::mf1<void, epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&>, boost::_bi::list2<boost::_bi::value<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >*>, boost::arg<1> (*)()> > >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x4CA3DB: boost::asio::detail::epoll_reactor::descriptor_state::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x62226F: boost::asio::detail::task_io_service::run(boost::system::error_code&) [clone .constprop.1363] (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x536207: epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread() (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x4D0ACF7: ??? (in /usr/lib/aarch64-linux-gnu/libboost_thread.so.1.58.0)
==24636==    by 0x4865FC3: start_thread (pthread_create.c:335)
==24636==    by 0x495110F: thread_start (clone.S:89)
==24636==  Address 0xcf82344 is on thread 8's stack
==24636==  in frame #1, created by boost::asio::detail::epoll_reactor::start_op(int, int, boost::asio::detail::epoll_reactor::descriptor_state*&, boost::asio::detail::reactor_op*, bool, bool) [clone .constprop.2054] (???:)
==24636== 
2017-02-10 09:15:26.743	[P2P1]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:288	[185.42.221.58:57874 INC] Sync data returned a new top block candidate: 1242141 -> 1242910 [Your node is 769 blocks (1 days) behind] 
SYNCHRONIZATION started
==24636== Thread 9:
==24636== Syscall param epoll_ctl(event) points to uninitialised byte(s)
==24636==    at 0x4951508: epoll_ctl (syscall-template.S:84)
==24636==    by 0x5304F7: boost::asio::basic_socket<boost::asio::ip::tcp, boost::asio::stream_socket_service<boost::asio::ip::tcp> >::open(boost::asio::ip::tcp const&) (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x4F4B07: nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::handle_handshake(int, nodetool::COMMAND_HANDSHAKE_T<cryptonote::CORE_SYNC_DATA>::request&, nodetool::COMMAND_HANDSHAKE_T<cryptonote::CORE_SYNC_DATA>::response&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&) (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x6747EF: int nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::handle_invoke_map<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >(bool, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&, bool&) [clone .constprop.835] (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x512EAF: epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >::handle_recv(void const*, unsigned long) (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x5347D3: epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::handle_read(boost::system::error_code const&, unsigned long) (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x50CC27: boost::asio::detail::completion_handler<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > > >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x50D3A3: boost::asio::detail::reactive_socket_recv_op<boost::asio::mutable_buffers_1, boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running> >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x62226F: boost::asio::detail::task_io_service::run(boost::system::error_code&) [clone .constprop.1363] (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x536207: epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread() (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x4D0ACF7: ??? (in /usr/lib/aarch64-linux-gnu/libboost_thread.so.1.58.0)
==24636==    by 0x4865FC3: start_thread (pthread_create.c:335)
==24636==  Address 0xd480d04 is on thread 9's stack
==24636==  in frame #1, created by boost::asio::basic_socket<boost::asio::ip::tcp, boost::asio::stream_socket_service<boost::asio::ip::tcp> >::open(boost::asio::ip::tcp const&) (???:)
==24636== 
==24636== Syscall param epoll_ctl(event) points to uninitialised byte(s)
==24636==    at 0x4951508: epoll_ctl (syscall-template.S:84)
==24636==    by 0x66798F: boost::asio::detail::epoll_reactor::start_op(int, int, boost::asio::detail::epoll_reactor::descriptor_state*&, boost::asio::detail::reactor_op*, bool, bool) [clone .constprop.2054] (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x62CF5B: boost::asio::detail::reactive_socket_service_base::start_connect_op(boost::asio::detail::reactive_socket_service_base::base_implementation_type&, boost::asio::detail::reactor_op*, bool, sockaddr const*, unsigned long) [clone .constprop.2036] (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x4F4EFB: nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::handle_handshake(int, nodetool::COMMAND_HANDSHAKE_T<cryptonote::CORE_SYNC_DATA>::request&, nodetool::COMMAND_HANDSHAKE_T<cryptonote::CORE_SYNC_DATA>::response&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&) (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x6747EF: int nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::handle_invoke_map<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >(bool, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&, bool&) [clone .constprop.835] (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x512EAF: epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >::handle_recv(void const*, unsigned long) (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x5347D3: epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::handle_read(boost::system::error_code const&, unsigned long) (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x50CC27: boost::asio::detail::completion_handler<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > > >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x50D3A3: boost::asio::detail::reactive_socket_recv_op<boost::asio::mutable_buffers_1, boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running> >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x62226F: boost::asio::detail::task_io_service::run(boost::system::error_code&) [clone .constprop.1363] (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x536207: epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread() (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x4D0ACF7: ??? (in /usr/lib/aarch64-linux-gnu/libboost_thread.so.1.58.0)
==24636==  Address 0xd480ca4 is on thread 9's stack
==24636==  in frame #1, created by boost::asio::detail::epoll_reactor::start_op(int, int, boost::asio::detail::epoll_reactor::descriptor_state*&, boost::asio::detail::reactor_op*, bool, bool) [clone .constprop.2054] (???:)
==24636== 
2017-02-10 09:15:27.542	[P2P8]	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:1037	
**********************************************************************
The daemon will start synchronizing with the network. It may take up to several hours.

You can set the level of process detailization* through "set_log <level|categories>" command*,
where <level> is between 0 (no details) and 4 (very verbose), or custom category based levels (eg, *:WARNING)

Use the "help" command to see the list of available commands.
**********************************************************************

==24636== Thread 14:
==24636== Syscall param epoll_ctl(event) points to uninitialised byte(s)
==24636==    at 0x4951508: epoll_ctl (syscall-template.S:84)
==24636==    by 0x5304F7: boost::asio::basic_socket<boost::asio::ip::tcp, boost::asio::stream_socket_service<boost::asio::ip::tcp> >::open(boost::asio::ip::tcp const&) (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x660DB7: epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::connect(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, unsigned int, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&) [clone .constprop.1083] (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x662397: nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::try_to_connect_and_handshake_with_new_peer(nodetool::net_address const&, bool, unsigned long, bool) [clone .constprop.1079] (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x664747: nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::make_new_connection_from_peerlist(bool) [clone .constprop.1075] (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x664AB3: nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::make_expected_connections_count(bool, unsigned long) [clone .part.4588] [clone .constprop.1074] (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x52D6F7: nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::connections_maker() (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x4F8847: nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::idle_worker() (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x530C33: epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::global_timer_handler(boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext_base>) (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x50AC03: boost::asio::detail::wait_handler<boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext_base> >, boost::_bi::list2<boost::_bi::value<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >*>, boost::_bi::value<boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext_base> > > > >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x62226F: boost::asio::detail::task_io_service::run(boost::system::error_code&) [clone .constprop.1363] (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x536207: epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread() (in /home/nodey/monero/build/release/bin/monerod)
==24636==  Address 0xed81a94 is on thread 14's stack
==24636==  in frame #1, created by boost::asio::basic_socket<boost::asio::ip::tcp, boost::asio::stream_socket_service<boost::asio::ip::tcp> >::open(boost::asio::ip::tcp const&) (???:)
==24636== 
==24636== Syscall param epoll_ctl(event) points to uninitialised byte(s)
==24636==    at 0x4951508: epoll_ctl (syscall-template.S:84)
==24636==    by 0x66798F: boost::asio::detail::epoll_reactor::start_op(int, int, boost::asio::detail::epoll_reactor::descriptor_state*&, boost::asio::detail::reactor_op*, bool, bool) [clone .constprop.2054] (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x62CF5B: boost::asio::detail::reactive_socket_service_base::start_connect_op(boost::asio::detail::reactive_socket_service_base::base_implementation_type&, boost::asio::detail::reactor_op*, bool, sockaddr const*, unsigned long) [clone .constprop.2036] (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x660FCB: epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::connect(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, unsigned int, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&) [clone .constprop.1083] (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x662397: nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::try_to_connect_and_handshake_with_new_peer(nodetool::net_address const&, bool, unsigned long, bool) [clone .constprop.1079] (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x664747: nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::make_new_connection_from_peerlist(bool) [clone .constprop.1075] (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x664AB3: nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::make_expected_connections_count(bool, unsigned long) [clone .part.4588] [clone .constprop.1074] (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x52D6F7: nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::connections_maker() (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x4F8847: nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::idle_worker() (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x530C33: epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::global_timer_handler(boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext_base>) (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x50AC03: boost::asio::detail::wait_handler<boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext_base> >, boost::_bi::list2<boost::_bi::value<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >*>, boost::_bi::value<boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext_base> > > > >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x62226F: boost::asio::detail::task_io_service::run(boost::system::error_code&) [clone .constprop.1363] (in /home/nodey/monero/build/release/bin/monerod)
==24636==  Address 0xed81a34 is on thread 14's stack
==24636==  in frame #1, created by boost::asio::detail::epoll_reactor::start_op(int, int, boost::asio::detail::epoll_reactor::descriptor_state*&, boost::asio::detail::reactor_op*, bool, bool) [clone .constprop.2054] (???:)
==24636== 
2017-02-10 09:15:28.785	[P2P4]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1029	
**********************************************************************
You are now synchronized with the network. You may now start monero-wallet-cli.

Use the "help" command to see the list of available commands.
**********************************************************************
==24636== Thread 9:
==24636== Syscall param epoll_ctl(event) points to uninitialised byte(s)
==24636==    at 0x4951508: epoll_ctl (syscall-template.S:84)
==24636==    by 0x667273: boost::asio::detail::task_io_service::post_deferred_completions(boost::asio::detail::op_queue<boost::asio::detail::task_io_service_operation>&) [clone .constprop.2069] (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x51B97F: epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >::anvoke_handler<bool epee::net_utils::async_invoke_remote_command2<nodetool::COMMAND_HANDSHAKE_T<cryptonote::CORE_SYNC_DATA>::response, nodetool::COMMAND_HANDSHAKE_T<cryptonote::CORE_SYNC_DATA>::request, nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::do_handshake_with_peer(unsigned long&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&, bool)::{lambda(int, nodetool::COMMAND_HANDSHAKE_T<cryptonote::CORE_SYNC_DATA>::response const&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&)#1}, epee::levin::async_protocol_handler_config<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >(boost::uuids::uuid, int, nodetool::COMMAND_HANDSHAKE_T<cryptonote::CORE_SYNC_DATA>::request const&, epee::levin::async_protocol_handler_config<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >&, nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::do_handshake_with_peer(unsigned long&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&, bool)::{lambda(int, nodetool::COMMAND_HANDSHAKE_T<cryptonote::CORE_SYNC_DATA>::response const&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&)#1}, unsigned long)::{lambda(int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&)#1}>::cancel_timer() (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x51328B: epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >::handle_recv(void const*, unsigned long) (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x5347D3: epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::handle_read(boost::system::error_code const&, unsigned long) (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x50CC27: boost::asio::detail::completion_handler<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > > >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x50D3A3: boost::asio::detail::reactive_socket_recv_op<boost::asio::mutable_buffers_1, boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running> >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x4CA3DB: boost::asio::detail::epoll_reactor::descriptor_state::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x62226F: boost::asio::detail::task_io_service::run(boost::system::error_code&) [clone .constprop.1363] (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x536207: epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread() (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x4D0ACF7: ??? (in /usr/lib/aarch64-linux-gnu/libboost_thread.so.1.58.0)
==24636==    by 0x4865FC3: start_thread (pthread_create.c:335)
==24636==  Address 0xd481e94 is on thread 9's stack
==24636==  in frame #1, created by boost::asio::detail::task_io_service::post_deferred_completions(boost::asio::detail::op_queue<boost::asio::detail::task_io_service_operation>&) [clone .constprop.2069] (???:)
==24636== 
==24636== Thread 11:
==24636== Syscall param epoll_ctl(event) points to uninitialised byte(s)
==24636==    at 0x4951508: epoll_ctl (syscall-template.S:84)
==24636==    by 0x4CEA1F: boost::asio::detail::task_io_service::post_immediate_completion(boost::asio::detail::task_io_service_operation*, bool) (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x6679AF: boost::asio::detail::epoll_reactor::start_op(int, int, boost::asio::detail::epoll_reactor::descriptor_state*&, boost::asio::detail::reactor_op*, bool, bool) [clone .constprop.2054] (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x4CEBB3: boost::asio::detail::reactive_socket_service_base::start_op(boost::asio::detail::reactive_socket_service_base::base_implementation_type&, int, boost::asio::detail::reactor_op*, bool, bool, bool) (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x6590D3: boost::asio::async_result<boost::asio::handler_type<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, void (boost::system::error_code, unsigned long)>::type>::type boost::asio::stream_socket_service<boost::asio::ip::tcp>::async_receive<boost::asio::mutable_buffers_1, boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running> >(boost::asio::detail::reactive_socket_service<boost::asio::ip::tcp>::implementation_type&, boost::asio::mutable_buffers_1 const&, int, boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>&&) [clone .constprop.1108] (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x6601C7: epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::start(bool, bool) [clone .constprop.1099] (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x538AB7: epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::handle_accept(boost::system::error_code const&) (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x50A8D3: boost::asio::detail::reactive_socket_accept_op<boost::asio::basic_socket<boost::asio::ip::tcp, boost::asio::stream_socket_service<boost::asio::ip::tcp> >, boost::asio::ip::tcp, boost::_bi::bind_t<void, boost::_mfi::mf1<void, epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&>, boost::_bi::list2<boost::_bi::value<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >*>, boost::arg<1> (*)()> > >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x4CA3DB: boost::asio::detail::epoll_reactor::descriptor_state::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x62226F: boost::asio::detail::task_io_service::run(boost::system::error_code&) [clone .constprop.1363] (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x536207: epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread() (in /home/nodey/monero/build/release/bin/monerod)
==24636==    by 0x4D0ACF7: ??? (in /usr/lib/aarch64-linux-gnu/libboost_thread.so.1.58.0)
==24636==  Address 0xde81fa4 is on thread 11's stack
==24636==  in frame #1, created by boost::asio::detail::task_io_service::post_immediate_completion(boost::asio::detail::task_io_service_operation*, bool) (???:)
==24636== 
2017-02-10 09:15:43.859	[P2P9]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:288	[38.135.33.74:54088 INC] Sync data returned a new top block candidate: 1242141 -> 1242910 [Your node is 769 blocks (1 days) behind] 
SYNCHRONIZATION started
```

## moneromooo-monero | 2017-02-24T00:37:05+00:00
Can you try with a debug build, so we can see which line causes that uninitialized use.

## ghost | 2017-02-24T06:10:31+00:00
Ok will try

## ghost | 2017-02-24T06:10:42+00:00
D'oh, wrong button

## moneromooo-monero | 2017-08-08T11:30:52+00:00
Is this still happening ? I recently ran monerod with valgrind and didn't see any reports near init time.

## moneromooo-monero | 2017-10-03T11:17:21+00:00
I'll close this soon if no further info/confirmation is given.

## moneromooo-monero | 2017-10-15T18:29:00+00:00
Still no reports from valgrind between "Cryptonote protocol initialized OK" and "Initializing p2p server...", and no answer, closing.

+invalid

# Action History
- Created by: ghost | 2017-02-06T07:54:12+00:00
- Closed at: 2017-10-15T18:36:20+00:00
