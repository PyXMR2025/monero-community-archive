---
title: 'linux-x64-v0.13.0.4 daemon crash '
source_url: https://github.com/monero-project/monero/issues/4915
author: UnsGentoals
assignees: []
labels: []
created_at: '2018-11-29T16:04:59+00:00'
updated_at: '2018-11-29T17:41:18+00:00'
type: issue
status: closed
closed_at: '2018-11-29T17:41:18+00:00'
---

# Original Description
DISTRIB_ID=Ubuntu
DISTRIB_RELEASE=18.04
DISTRIB_CODENAME=bionic
DISTRIB_DESCRIPTION="Ubuntu 18.04.1 LTS"

kernel:4.15.0-39-generic #42-Ubuntu SMP Tue Oct 23 15:48:01 UTC 2018 x86_64 x86_64 x86_64 GNU/Linux

2018-11-29 15:51:53.857	    7fac6f0cd780	INFO 	logging	contrib/epee/src/mlog.cpp:277	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-11-29 15:51:53.857	    7fac6f0cd780	INFO 	global	src/daemon/main.cpp:287	Monero 'Beryllium Bullet' (v0.13.0.4-release)
2018-11-29 15:51:53.858	    7fac6f0cd780	INFO 	msgwriter	src/common/scoped_message_writer.h:102	Forking to background...
2018-11-29 15:51:53.858	    7fac6f0cd780	WARN 	daemon	src/daemon/executor.cpp:61	Monero 'Beryllium Bullet' (v0.13.0.4-release) Daemonised
2018-11-29 15:51:53.858	    7fac6f0cd780	INFO 	global	src/daemon/protocol.h:53	Initializing cryptonote protocol...
2018-11-29 15:51:53.858	    7fac6f0cd780	INFO 	global	src/daemon/protocol.h:58	Cryptonote protocol initialized OK
2018-11-29 15:51:53.859	    7fac6f0cd780	INFO 	global	src/daemon/p2p.h:63	Initializing p2p server...
2018-11-29 15:51:53.878	    7fac6f0cd780	INFO 	stacktrace	src/common/stack_trace.cpp:133	Exception: boost::exception_detail::clone_impl<boost::exception_detail::error_info_injector<boost::system::system_error> >
2018-11-29 15:51:53.878	    7fac6f0cd780	INFO 	stacktrace	src/common/stack_trace.cpp:134	Unwound call stack:
2018-11-29 15:51:53.883	    7fac6f0cd780	INFO 	stacktrace	src/common/stack_trace.cpp:172	    [1] /opt/monero-gui-linux-x64-v0.13.0.4/monerod:__wrap___cxa_throw+0x10a [0x55adb6cdd4ea]
2018-11-29 15:51:53.883	    7fac6f0cd780	INFO 	stacktrace	src/common/stack_trace.cpp:172	    [2] /opt/monero-gui-linux-x64-v0.13.0.4/monerod:void boost::throw_exception<boost::system::system_error>(boost::system::system_error const&)+0x1f0 [0x55adb69a64b0]
2018-11-29 15:51:53.883	    7fac6f0cd780	INFO 	stacktrace	src/common/stack_trace.cpp:172	    [3] /opt/monero-gui-linux-x64-v0.13.0.4/monerod:boost::asio::detail::do_throw_error(boost::system::error_code const&, char const*)+0x63 [0x55adb69c9d43]
2018-11-29 15:51:53.883	    7fac6f0cd780	INFO 	stacktrace	src/common/stack_trace.cpp:172	    [4] /opt/monero-gui-linux-x64-v0.13.0.4/monerod:epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::init_server(unsigned int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)+0x40b [0x55adb6bd70cb]
2018-11-29 15:51:53.883	    7fac6f0cd780	INFO 	stacktrace	src/common/stack_trace.cpp:172	    [5] /opt/monero-gui-linux-x64-v0.13.0.4/monerod:epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::init_server(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&)+0x69 [0x55adb6bda299]
2018-11-29 15:51:53.883	    7fac6f0cd780	INFO 	stacktrace	src/common/stack_trace.cpp:172	    [6] /opt/monero-gui-linux-x64-v0.13.0.4/monerod:nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::init(boost::program_options::variables_map const&)+0xb6d [0x55adb6bdb06d]
2018-11-29 15:51:53.883	    7fac6f0cd780	INFO 	stacktrace	src/common/stack_trace.cpp:172	    [7] /opt/monero-gui-linux-x64-v0.13.0.4/monerod:daemonize::t_p2p::t_p2p(boost::program_options::variables_map const&, daemonize::t_protocol&)+0x5bb [0x55adb69e9f4b]
2018-11-29 15:51:53.883	    7fac6f0cd780	INFO 	stacktrace	src/common/stack_trace.cpp:172	    [8] /opt/monero-gui-linux-x64-v0.13.0.4/monerod:daemonize::t_internals::t_internals(boost::program_options::variables_map const&)+0x4bf [0x55adb6a3c03f]
2018-11-29 15:51:53.883	    7fac6f0cd780	INFO 	stacktrace	src/common/stack_trace.cpp:172	    [9] /opt/monero-gui-linux-x64-v0.13.0.4/monerod:daemonize::t_daemon::t_daemon(boost::program_options::variables_map const&)+0x3c [0x55adb69bb2fc]
2018-11-29 15:51:53.883	    7fac6f0cd780	INFO 	stacktrace	src/common/stack_trace.cpp:172	    [10] /opt/monero-gui-linux-x64-v0.13.0.4/monerod:daemonize::t_executor::create_daemon(boost::program_options::variables_map const&)+0x15a [0x55adb6a75eca]
2018-11-29 15:51:53.883	    7fac6f0cd780	INFO 	stacktrace	src/common/stack_trace.cpp:172	    [11] /opt/monero-gui-linux-x64-v0.13.0.4/monerod:bool daemonizer::daemonize<daemonize::t_executor>(int, char const**, daemonize::t_executor&&, boost::program_options::variables_map const&)+0x11b [0x55adb6a7d5cb]
2018-11-29 15:51:53.883	    7fac6f0cd780	INFO 	stacktrace	src/common/stack_trace.cpp:172	    [12] /opt/monero-gui-linux-x64-v0.13.0.4/monerod:main+0x13a5 [0x55adb6991235]
2018-11-29 15:51:53.883	    7fac6f0cd780	INFO 	stacktrace	src/common/stack_trace.cpp:172	    [13] /lib/x86_64-linux-gnu/libc.so.6:__libc_start_main+0xe7 [0x7fac6e11ab97]
2018-11-29 15:51:53.883	    7fac6f0cd780	INFO 	stacktrace	src/common/stack_trace.cpp:172	    [14] /opt/monero-gui-linux-x64-v0.13.0.4/monerod:_start+0x29 [0x55adb699b3b9]
2018-11-29 15:51:53.883	    7fac6f0cd780	INFO 	stacktrace	src/common/stack_trace.cpp:172	
2018-11-29 15:51:53.883	    7fac6f0cd780	FATAL	net	contrib/epee/include/net/abstract_tcp_server2.inl:856	Error starting server: bind: Address already in use
2018-11-29 15:51:53.883	    7fac6f0cd780	INFO 	stacktrace	src/common/stack_trace.cpp:133	Exception: std::runtime_error
2018-11-29 15:51:53.883	    7fac6f0cd780	INFO 	stacktrace	src/common/stack_trace.cpp:134	Unwound call stack:
2018-11-29 15:51:53.886	    7fac6f0cd780	INFO 	stacktrace	src/common/stack_trace.cpp:172	    [1] /opt/monero-gui-linux-x64-v0.13.0.4/monerod:__wrap___cxa_throw+0x10a [0x55adb6cdd4ea]
2018-11-29 15:51:53.886	    7fac6f0cd780	INFO 	stacktrace	src/common/stack_trace.cpp:172	    [2] /opt/monero-gui-linux-x64-v0.13.0.4/monerod:daemonize::t_p2p::t_p2p(boost::program_options::variables_map const&, daemonize::t_protocol&)+0x766 [0x55adb69ea0f6]
2018-11-29 15:51:53.886	    7fac6f0cd780	INFO 	stacktrace	src/common/stack_trace.cpp:172	    [3] /opt/monero-gui-linux-x64-v0.13.0.4/monerod:daemonize::t_internals::t_internals(boost::program_options::variables_map const&)+0x4bf [0x55adb6a3c03f]
2018-11-29 15:51:53.886	    7fac6f0cd780	INFO 	stacktrace	src/common/stack_trace.cpp:172	    [4] /opt/monero-gui-linux-x64-v0.13.0.4/monerod:daemonize::t_daemon::t_daemon(boost::program_options::variables_map const&)+0x3c [0x55adb69bb2fc]
2018-11-29 15:51:53.886	    7fac6f0cd780	INFO 	stacktrace	src/common/stack_trace.cpp:172	    [5] /opt/monero-gui-linux-x64-v0.13.0.4/monerod:daemonize::t_executor::create_daemon(boost::program_options::variables_map const&)+0x15a [0x55adb6a75eca]
2018-11-29 15:51:53.886	    7fac6f0cd780	INFO 	stacktrace	src/common/stack_trace.cpp:172	    [6] /opt/monero-gui-linux-x64-v0.13.0.4/monerod:bool daemonizer::daemonize<daemonize::t_executor>(int, char const**, daemonize::t_executor&&, boost::program_options::variables_map const&)+0x11b [0x55adb6a7d5cb]
2018-11-29 15:51:53.886	    7fac6f0cd780	INFO 	stacktrace	src/common/stack_trace.cpp:172	    [7] /opt/monero-gui-linux-x64-v0.13.0.4/monerod:main+0x13a5 [0x55adb6991235]
2018-11-29 15:51:53.886	    7fac6f0cd780	INFO 	stacktrace	src/common/stack_trace.cpp:172	    [8] /lib/x86_64-linux-gnu/libc.so.6:__libc_start_main+0xe7 [0x7fac6e11ab97]
2018-11-29 15:51:53.886	    7fac6f0cd780	INFO 	stacktrace	src/common/stack_trace.cpp:172	    [9] /opt/monero-gui-linux-x64-v0.13.0.4/monerod:_start+0x29 [0x55adb699b3b9]
2018-11-29 15:51:53.886	    7fac6f0cd780	INFO 	stacktrace	src/common/stack_trace.cpp:172	
2018-11-29 15:51:53.886	    7fac6f0cd780	INFO 	global	src/daemon/core.h:103	Deinitializing core...
2018-11-29 15:51:53.886	    7fac6f0cd780	INFO 	stacktrace	src/common/stack_trace.cpp:133	Exception: cryptonote::DB_ERROR
2018-11-29 15:51:53.886	    7fac6f0cd780	INFO 	stacktrace	src/common/stack_trace.cpp:134	Unwound call stack:
2018-11-29 15:51:53.890	    7fac6f0cd780	INFO 	stacktrace	src/common/stack_trace.cpp:172	    [1] /opt/monero-gui-linux-x64-v0.13.0.4/monerod:__wrap___cxa_throw+0x10a [0x55adb6cdd4ea]
2018-11-29 15:51:53.890	    7fac6f0cd780	INFO 	stacktrace	src/common/stack_trace.cpp:172	    [2] /opt/monero-gui-linux-x64-v0.13.0.4/monerod:cryptonote::Blockchain::deinit()+0xd36 [0x55adb6c2f466]
2018-11-29 15:51:53.890	    7fac6f0cd780	INFO 	stacktrace	src/common/stack_trace.cpp:172	    [3] /opt/monero-gui-linux-x64-v0.13.0.4/monerod:cryptonote::core::deinit()+0x25 [0x55adb6c60bd5]
2018-11-29 15:51:53.890	    7fac6f0cd780	INFO 	stacktrace	src/common/stack_trace.cpp:172	    [4] /opt/monero-gui-linux-x64-v0.13.0.4/monerod:daemonize::t_core::~t_core()+0xe6 [0x55adb69d38f6]
2018-11-29 15:51:53.890	    7fac6f0cd780	INFO 	stacktrace	src/common/stack_trace.cpp:172	    [5] /opt/monero-gui-linux-x64-v0.13.0.4/monerod:daemonize::t_internals::t_internals(boost::program_options::variables_map const&)+0xa11 [0x55adb6a3c591]
2018-11-29 15:51:53.890	    7fac6f0cd780	INFO 	stacktrace	src/common/stack_trace.cpp:172	    [6] /opt/monero-gui-linux-x64-v0.13.0.4/monerod:daemonize::t_daemon::t_daemon(boost::program_options::variables_map const&)+0x3c [0x55adb69bb2fc]
2018-11-29 15:51:53.890	    7fac6f0cd780	INFO 	stacktrace	src/common/stack_trace.cpp:172	    [7] /opt/monero-gui-linux-x64-v0.13.0.4/monerod:daemonize::t_executor::create_daemon(boost::program_options::variables_map const&)+0x15a [0x55adb6a75eca]
2018-11-29 15:51:53.890	    7fac6f0cd780	INFO 	stacktrace	src/common/stack_trace.cpp:172	    [8] /opt/monero-gui-linux-x64-v0.13.0.4/monerod:bool daemonizer::daemonize<daemonize::t_executor>(int, char const**, daemonize::t_executor&&, boost::program_options::variables_map const&)+0x11b [0x55adb6a7d5cb]
2018-11-29 15:51:53.890	    7fac6f0cd780	INFO 	stacktrace	src/common/stack_trace.cpp:172	    [9] /opt/monero-gui-linux-x64-v0.13.0.4/monerod:main+0x13a5 [0x55adb6991235]
2018-11-29 15:51:53.890	    7fac6f0cd780	INFO 	stacktrace	src/common/stack_trace.cpp:172	    [10] /lib/x86_64-linux-gnu/libc.so.6:__libc_start_main+0xe7 [0x7fac6e11ab97]
2018-11-29 15:51:53.890	    7fac6f0cd780	INFO 	stacktrace	src/common/stack_trace.cpp:172	    [11] /opt/monero-gui-linux-x64-v0.13.0.4/monerod:_start+0x29 [0x55adb699b3b9]
2018-11-29 15:51:53.890	    7fac6f0cd780	INFO 	stacktrace	src/common/stack_trace.cpp:172	
2018-11-29 15:51:53.890	    7fac6f0cd780	ERROR	daemon	src/daemon/core.h:108	Failed to deinitialize core...
2018-11-29 15:51:53.890	    7fac6f0cd780	INFO 	global	src/daemon/protocol.h:75	Stopping cryptonote protocol...
2018-11-29 15:51:53.890	    7fac6f0cd780	INFO 	global	src/daemon/protocol.h:79	Cryptonote protocol stopped successfully
2018-11-29 15:51:53.891	    7fac6f0cd780	ERROR	daemon	src/daemon/main.cpp:295	Exception in main! Failed to initialize p2p server.
2018-11-29 15:51:55.864	    7f9ae3d65780	INFO 	logging	contrib/epee/src/mlog.cpp:277	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-11-29 15:52:17.252	    7f30de221780	INFO 	logging	contrib/epee/src/mlog.cpp:277	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-11-29 15:54:06.578	    7f9ae3d65780	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2018-11-29 15:54:27.058	    7f30de221780	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2018-11-29 15:54:38.300	    7f4589885780	INFO 	logging	contrib/epee/src/mlog.cpp:277	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-11-29 15:54:38.300	    7f4589885780	INFO 	global	src/daemon/main.cpp:287	Monero 'Beryllium Bullet' (v0.13.0.4-release)
2018-11-29 15:54:38.300	    7f4589885780	INFO 	msgwriter	src/common/scoped_message_writer.h:102	Forking to background...
2018-11-29 15:54:38.301	    7f4589885780	WARN 	daemon	src/daemon/executor.cpp:61	Monero 'Beryllium Bullet' (v0.13.0.4-release) Daemonised
2018-11-29 15:54:38.301	    7f4589885780	INFO 	global	src/daemon/protocol.h:53	Initializing cryptonote protocol...
2018-11-29 15:54:38.301	    7f4589885780	INFO 	global	src/daemon/protocol.h:58	Cryptonote protocol initialized OK
2018-11-29 15:54:38.301	    7f4589885780	INFO 	global	src/daemon/p2p.h:63	Initializing p2p server...
2018-11-29 15:54:38.320	    7f4589885780	INFO 	stacktrace	src/common/stack_trace.cpp:133	Exception: boost::exception_detail::clone_impl<boost::exception_detail::error_info_injector<boost::system::system_error> >
2018-11-29 15:54:38.320	    7f4589885780	INFO 	stacktrace	src/common/stack_trace.cpp:134	Unwound call stack:
2018-11-29 15:54:38.325	    7f4589885780	INFO 	stacktrace	src/common/stack_trace.cpp:172	    [1] /opt/monero-gui-linux-x64-v0.13.0.4/monerod:__wrap___cxa_throw+0x10a [0x555cae6d34ea]
2018-11-29 15:54:38.325	    7f4589885780	INFO 	stacktrace	src/common/stack_trace.cpp:172	    [2] /opt/monero-gui-linux-x64-v0.13.0.4/monerod:void boost::throw_exception<boost::system::system_error>(boost::system::system_error const&)+0x1f0 [0x555cae39c4b0]
2018-11-29 15:54:38.325	    7f4589885780	INFO 	stacktrace	src/common/stack_trace.cpp:172	    [3] /opt/monero-gui-linux-x64-v0.13.0.4/monerod:boost::asio::detail::do_throw_error(boost::system::error_code const&, char const*)+0x63 [0x555cae3bfd43]
2018-11-29 15:54:38.325	    7f4589885780	INFO 	stacktrace	src/common/stack_trace.cpp:172	    [4] /opt/monero-gui-linux-x64-v0.13.0.4/monerod:epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::init_server(unsigned int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)+0x40b [0x555cae5cd0cb]
2018-11-29 15:54:38.325	    7f4589885780	INFO 	stacktrace	src/common/stack_trace.cpp:172	    [5] /opt/monero-gui-linux-x64-v0.13.0.4/monerod:epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::init_server(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&)+0x69 [0x555cae5d0299]
2018-11-29 15:54:38.325	    7f4589885780	INFO 	stacktrace	src/common/stack_trace.cpp:172	    [6] /opt/monero-gui-linux-x64-v0.13.0.4/monerod:nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::init(boost::program_options::variables_map const&)+0xb6d [0x555cae5d106d]
2018-11-29 15:54:38.325	    7f4589885780	INFO 	stacktrace	src/common/stack_trace.cpp:172	    [7] /opt/monero-gui-linux-x64-v0.13.0.4/monerod:daemonize::t_p2p::t_p2p(boost::program_options::variables_map const&, daemonize::t_protocol&)+0x5bb [0x555cae3dff4b]
2018-11-29 15:54:38.325	    7f4589885780	INFO 	stacktrace	src/common/stack_trace.cpp:172	    [8] /opt/monero-gui-linux-x64-v0.13.0.4/monerod:daemonize::t_internals::t_internals(boost::program_options::variables_map const&)+0x4bf [0x555cae43203f]
2018-11-29 15:54:38.325	    7f4589885780	INFO 	stacktrace	src/common/stack_trace.cpp:172	    [9] /opt/monero-gui-linux-x64-v0.13.0.4/monerod:daemonize::t_daemon::t_daemon(boost::program_options::variables_map const&)+0x3c [0x555cae3b12fc]
2018-11-29 15:54:38.325	    7f4589885780	INFO 	stacktrace	src/common/stack_trace.cpp:172	    [10] /opt/monero-gui-linux-x64-v0.13.0.4/monerod:daemonize::t_executor::create_daemon(boost::program_options::variables_map const&)+0x15a [0x555cae46beca]
2018-11-29 15:54:38.325	    7f4589885780	INFO 	stacktrace	src/common/stack_trace.cpp:172	    [11] /opt/monero-gui-linux-x64-v0.13.0.4/monerod:bool daemonizer::daemonize<daemonize::t_executor>(int, char const**, daemonize::t_executor&&, boost::program_options::variables_map const&)+0x11b [0x555cae4735cb]
2018-11-29 15:54:38.325	    7f4589885780	INFO 	stacktrace	src/common/stack_trace.cpp:172	    [12] /opt/monero-gui-linux-x64-v0.13.0.4/monerod:main+0x13a5 [0x555cae387235]
2018-11-29 15:54:38.325	    7f4589885780	INFO 	stacktrace	src/common/stack_trace.cpp:172	    [13] /lib/x86_64-linux-gnu/libc.so.6:__libc_start_main+0xe7 [0x7f45888d2b97]
2018-11-29 15:54:38.325	    7f4589885780	INFO 	stacktrace	src/common/stack_trace.cpp:172	    [14] /opt/monero-gui-linux-x64-v0.13.0.4/monerod:_start+0x29 [0x555cae3913b9]
2018-11-29 15:54:38.325	    7f4589885780	INFO 	stacktrace	src/common/stack_trace.cpp:172	
2018-11-29 15:54:38.325	    7f4589885780	FATAL	net	contrib/epee/include/net/abstract_tcp_server2.inl:856	Error starting server: bind: Address already in use
2018-11-29 15:54:38.325	    7f4589885780	INFO 	stacktrace	src/common/stack_trace.cpp:133	Exception: std::runtime_error
2018-11-29 15:54:38.325	    7f4589885780	INFO 	stacktrace	src/common/stack_trace.cpp:134	Unwound call stack:
2018-11-29 15:54:38.328	    7f4589885780	INFO 	stacktrace	src/common/stack_trace.cpp:172	    [1] /opt/monero-gui-linux-x64-v0.13.0.4/monerod:__wrap___cxa_throw+0x10a [0x555cae6d34ea]
2018-11-29 15:54:38.328	    7f4589885780	INFO 	stacktrace	src/common/stack_trace.cpp:172	    [2] /opt/monero-gui-linux-x64-v0.13.0.4/monerod:daemonize::t_p2p::t_p2p(boost::program_options::variables_map const&, daemonize::t_protocol&)+0x766 [0x555cae3e00f6]
2018-11-29 15:54:38.328	    7f4589885780	INFO 	stacktrace	src/common/stack_trace.cpp:172	    [3] /opt/monero-gui-linux-x64-v0.13.0.4/monerod:daemonize::t_internals::t_internals(boost::program_options::variables_map const&)+0x4bf [0x555cae43203f]
2018-11-29 15:54:38.328	    7f4589885780	INFO 	stacktrace	src/common/stack_trace.cpp:172	    [4] /opt/monero-gui-linux-x64-v0.13.0.4/monerod:daemonize::t_daemon::t_daemon(boost::program_options::variables_map const&)+0x3c [0x555cae3b12fc]
2018-11-29 15:54:38.328	    7f4589885780	INFO 	stacktrace	src/common/stack_trace.cpp:172	    [5] /opt/monero-gui-linux-x64-v0.13.0.4/monerod:daemonize::t_executor::create_daemon(boost::program_options::variables_map const&)+0x15a [0x555cae46beca]
2018-11-29 15:54:38.328	    7f4589885780	INFO 	stacktrace	src/common/stack_trace.cpp:172	    [6] /opt/monero-gui-linux-x64-v0.13.0.4/monerod:bool daemonizer::daemonize<daemonize::t_executor>(int, char const**, daemonize::t_executor&&, boost::program_options::variables_map const&)+0x11b [0x555cae4735cb]
2018-11-29 15:54:38.328	    7f4589885780	INFO 	stacktrace	src/common/stack_trace.cpp:172	    [7] /opt/monero-gui-linux-x64-v0.13.0.4/monerod:main+0x13a5 [0x555cae387235]
2018-11-29 15:54:38.328	    7f4589885780	INFO 	stacktrace	src/common/stack_trace.cpp:172	    [8] /lib/x86_64-linux-gnu/libc.so.6:__libc_start_main+0xe7 [0x7f45888d2b97]
2018-11-29 15:54:38.328	    7f4589885780	INFO 	stacktrace	src/common/stack_trace.cpp:172	    [9] /opt/monero-gui-linux-x64-v0.13.0.4/monerod:_start+0x29 [0x555cae3913b9]
2018-11-29 15:54:38.328	    7f4589885780	INFO 	stacktrace	src/common/stack_trace.cpp:172	
2018-11-29 15:54:38.328	    7f4589885780	INFO 	global	src/daemon/core.h:103	Deinitializing core...
2018-11-29 15:54:38.328	    7f4589885780	INFO 	stacktrace	src/common/stack_trace.cpp:133	Exception: cryptonote::DB_ERROR
2018-11-29 15:54:38.328	    7f4589885780	INFO 	stacktrace	src/common/stack_trace.cpp:134	Unwound call stack:
2018-11-29 15:54:38.331	    7f4589885780	INFO 	stacktrace	src/common/stack_trace.cpp:172	    [1] /opt/monero-gui-linux-x64-v0.13.0.4/monerod:__wrap___cxa_throw+0x10a [0x555cae6d34ea]
2018-11-29 15:54:38.331	    7f4589885780	INFO 	stacktrace	src/common/stack_trace.cpp:172	    [2] /opt/monero-gui-linux-x64-v0.13.0.4/monerod:cryptonote::Blockchain::deinit()+0xd36 [0x555cae625466]
2018-11-29 15:54:38.331	    7f4589885780	INFO 	stacktrace	src/common/stack_trace.cpp:172	    [3] /opt/monero-gui-linux-x64-v0.13.0.4/monerod:cryptonote::core::deinit()+0x25 [0x555cae656bd5]
2018-11-29 15:54:38.331	    7f4589885780	INFO 	stacktrace	src/common/stack_trace.cpp:172	    [4] /opt/monero-gui-linux-x64-v0.13.0.4/monerod:daemonize::t_core::~t_core()+0xe6 [0x555cae3c98f6]
2018-11-29 15:54:38.331	    7f4589885780	INFO 	stacktrace	src/common/stack_trace.cpp:172	    [5] /opt/monero-gui-linux-x64-v0.13.0.4/monerod:daemonize::t_internals::t_internals(boost::program_options::variables_map const&)+0xa11 [0x555cae432591]
2018-11-29 15:54:38.331	    7f4589885780	INFO 	stacktrace	src/common/stack_trace.cpp:172	    [6] /opt/monero-gui-linux-x64-v0.13.0.4/monerod:daemonize::t_daemon::t_daemon(boost::program_options::variables_map const&)+0x3c [0x555cae3b12fc]
2018-11-29 15:54:38.331	    7f4589885780	INFO 	stacktrace	src/common/stack_trace.cpp:172	    [7] /opt/monero-gui-linux-x64-v0.13.0.4/monerod:daemonize::t_executor::create_daemon(boost::program_options::variables_map const&)+0x15a [0x555cae46beca]
2018-11-29 15:54:38.331	    7f4589885780	INFO 	stacktrace	src/common/stack_trace.cpp:172	    [8] /opt/monero-gui-linux-x64-v0.13.0.4/monerod:bool daemonizer::daemonize<daemonize::t_executor>(int, char const**, daemonize::t_executor&&, boost::program_options::variables_map const&)+0x11b [0x555cae4735cb]
2018-11-29 15:54:38.331	    7f4589885780	INFO 	stacktrace	src/common/stack_trace.cpp:172	    [9] /opt/monero-gui-linux-x64-v0.13.0.4/monerod:main+0x13a5 [0x555cae387235]
2018-11-29 15:54:38.331	    7f4589885780	INFO 	stacktrace	src/common/stack_trace.cpp:172	    [10] /lib/x86_64-linux-gnu/libc.so.6:__libc_start_main+0xe7 [0x7f45888d2b97]
2018-11-29 15:54:38.331	    7f4589885780	INFO 	stacktrace	src/common/stack_trace.cpp:172	    [11] /opt/monero-gui-linux-x64-v0.13.0.4/monerod:_start+0x29 [0x555cae3913b9]
2018-11-29 15:54:38.331	    7f4589885780	INFO 	stacktrace	src/common/stack_trace.cpp:172	
2018-11-29 15:54:38.332	    7f4589885780	ERROR	daemon	src/daemon/core.h:108	Failed to deinitialize core...
2018-11-29 15:54:38.332	    7f4589885780	INFO 	global	src/daemon/protocol.h:75	Stopping cryptonote protocol...
2018-11-29 15:54:38.332	    7f4589885780	INFO 	global	src/daemon/protocol.h:79	Cryptonote protocol stopped successfully
2018-11-29 15:54:38.332	    7f4589885780	ERROR	daemon	src/daemon/main.cpp:295	Exception in main! Failed to initialize p2p server.
2018-11-29 15:54:40.310	    7f20d5806780	INFO 	logging	contrib/epee/src/mlog.cpp:277	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-11-29 15:54:43.455	    7fd0d16ea780	INFO 	logging	contrib/epee/src/mlog.cpp:277	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-11-29 15:56:50.418	    7f20d5806780	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2018-11-29 15:56:54.518	    7fd0d16ea780	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081

# Discussion History
## UnsGentoals | 2018-11-29T17:41:18+00:00
I quit the GUI ,but daemon not quit , so the port is being used.
after reboot ,problem solved.

# Action History
- Created by: UnsGentoals | 2018-11-29T16:04:59+00:00
- Closed at: 2018-11-29T17:41:18+00:00
