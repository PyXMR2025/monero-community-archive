---
title: ERROR   daemon  src/daemon/main.cpp:290 Exception in main! Failed to initialize
  p2p server.
source_url: https://github.com/monero-project/monero/issues/2361
author: xmrminer2017
assignees: []
labels:
- invalid
created_at: '2017-08-27T16:35:29+00:00'
updated_at: '2017-10-13T09:57:56+00:00'
type: issue
status: closed
closed_at: '2017-08-28T15:00:15+00:00'
---

# Original Description
root@ubuntu-8gb-nyc1-01:~/monero/monero-v0.10.3.1# ./monerod
2017-08-27 16:34:02.876     7f4c2e97e780        INFO    global  contrib/epee/src/mlog.cpp:145   New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO
2017-08-27 16:34:02.876     7f4c2e97e780        INFO    global  src/daemon/main.cpp:282 Monero 'Wolfram Warptangent' (v0.10.3.1-release)
2017-08-27 16:34:02.876     7f4c2e97e780        INFO    global  src/daemon/protocol.h:55        Initializing cryptonote protocol...
2017-08-27 16:34:02.876     7f4c2e97e780        INFO    global  src/daemon/protocol.h:60        Cryptonote protocol initialized OK
2017-08-27 16:34:02.877     7f4c2e97e780        INFO    global  src/daemon/p2p.h:63     Initializing p2p server...
2017-08-27 16:34:03.142     7f4c2e97e780        INFO    global  src/daemon/core.h:89    Deinitializing core...
2017-08-27 16:34:03.146     7f4c2e97e780        ERROR   daemon  src/daemon/core.h:94    Failed to deinitialize core...
2017-08-27 16:34:03.146     7f4c2e97e780        INFO    global  src/daemon/protocol.h:77        Stopping cryptonote protocol...
2017-08-27 16:34:03.146     7f4c2e97e780        INFO    global  src/daemon/protocol.h:81        Cryptonote protocol stopped successfully
2017-08-27 16:34:03.146     7f4c2e97e780        ERROR   daemon  src/daemon/main.cpp:290 Exception in main! Failed to initialize p2p server.



Please nelp me

# Discussion History
## moneromooo-monero | 2017-08-27T18:12:09+00:00
Exit the monerod that's currently running first.

## xmrminer2017 | 2017-08-27T18:15:02+00:00
I was running  ./monerod --detach
How i can exit this mode :( ?

## MaxXor | 2017-08-27T18:43:17+00:00
@xmrminer2017 I'm sending a SIGTERM to the running monero daemon via `kill <pid>`. It will shutdown normally without corrupting the local blockchain. Not sure if there is any other easy way.

## xmrminer2017 | 2017-08-27T19:14:07+00:00
@MaxXor please let me know how i can kill it

## hyc | 2017-08-27T19:23:33+00:00
Just use `monerod exit`

## moneromooo-monero | 2017-08-28T14:57:56+00:00
Reopen in case this was not problem, but it seems very likely it is.

+invalid

## chamalis | 2017-10-12T18:09:59+00:00
I am having this issue when I try **to run monerod over torsocks**, otherwise (without TOR) works fine.

Version: Monero 'Helium Hydra' (v0.11.0.0-86e9de58), built from compiling the master branch, and I can confirm that:

* `monerod` is not running (`ps aux | grep -i monero` won't find anything - and `monerod exit` doesn't work)
* `--enforce-dns-checkpointing` didn't help 
* Tor accepts connections at 9050, configured firefox and works fine.

```
$ DNS_PUBLIC=tcp TORSOCKS_ALLOW_INBOUND=1 torsocks ./build/release/bin/monerod --log-file tmonerod.log --enforce-dns-checkpointing --p2p-bind-ip 127.0.0.1:9050 --no-igd
2017-10-12 18:03:04.044	    7ff234672740	INFO 	global	src/daemon/main.cpp:283	Monero 'Helium Hydra' (v0.11.0.0-86e9de58)
2017-10-12 18:03:04.044	    7ff234672740	INFO 	global	src/daemon/protocol.h:55	Initializing cryptonote protocol...
2017-10-12 18:03:04.044	    7ff234672740	INFO 	global	src/daemon/protocol.h:60	Cryptonote protocol initialized OK
2017-10-12 18:03:04.045	    7ff234672740	INFO 	global	src/daemon/p2p.h:63	Initializing p2p server...
2017-10-12 18:03:04.045	    7ff22b700700	WARN 	net.dns	src/common/dns_utils.cpp:207	Using public DNS server: 8.8.4.4 (TCP)
1507831404 ERROR torsocks[13114]: Unable to resolve. Status reply: 1 (in socks5_recv_resolve_reply() at socks5.c:683)
2017-10-12 18:03:24.053	    7ff234672740	INFO 	global	src/daemon/core.h:89	Deinitializing core...
2017-10-12 18:03:24.054	    7ff234672740	ERROR	daemon	src/daemon/core.h:94	Failed to deinitialize core...
2017-10-12 18:03:24.054	    7ff234672740	INFO 	global	src/daemon/protocol.h:77	Stopping cryptonote protocol...
2017-10-12 18:03:24.054	    7ff234672740	INFO 	global	src/daemon/protocol.h:81	Cryptonote protocol stopped successfully
2017-10-12 18:03:24.054	    7ff234672740	ERROR	daemon	src/daemon/main.cpp:291	Exception in main! Failed to initialize p2p server.
```

Daemon's log file:

```
$ cat tmonerod.log 
2017-10-12 17:54:37.114	    7fde55486740	INFO 	logging	contrib/epee/src/mlog.cpp:180	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-10-12 17:54:37.115	    7fde55486740	INFO 	global	src/daemon/main.cpp:283	Monero 'Helium Hydra' (v0.11.0.0-86e9de58)
2017-10-12 17:54:37.115	    7fde55486740	INFO 	global	src/daemon/protocol.h:55	Initializing cryptonote protocol...
2017-10-12 17:54:37.115	    7fde55486740	INFO 	global	src/daemon/protocol.h:60	Cryptonote protocol initialized OK
2017-10-12 17:54:37.115	    7fde55486740	INFO 	global	src/daemon/p2p.h:63	Initializing p2p server...
2017-10-12 17:54:37.116	    7fde4c514700	WARN 	net.dns	src/common/dns_utils.cpp:207	Using public DNS server: 8.8.4.4 (TCP)
2017-10-12 17:54:43.858	    7fde55486740	INFO 	stacktrace	src/common/stack_trace.cpp:120	Exception: boost::exception_detail::clone_impl<boost::exception_detail::error_info_injector<boost::system::system_error> >
2017-10-12 17:54:43.858	    7fde55486740	INFO 	stacktrace	src/common/stack_trace.cpp:121	Unwound call stack:
2017-10-12 17:54:43.860	    7fde55486740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [1] ./build/release/bin/monerod:__cxa_throw+0xfa [0x55a4c3dd612a]
2017-10-12 17:54:43.860	    7fde55486740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [2] ./build/release/bin/monerod:void boost::throw_exception<boost::system::system_error>(boost::system::system_error const&)+0x12d [0x55a4c3ba46cd]
2017-10-12 17:54:43.860	    7fde55486740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [3] ./build/release/bin/monerod:boost::asio::detail::do_throw_error(boost::system::error_code const&, char const*)+0x4e [0x55a4c3ba476e]
2017-10-12 17:54:43.860	    7fde55486740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [4] ./build/release/bin/monerod:epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::init_server(unsigned int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)+0xd85 [0x55a4c3c43255]
2017-10-12 17:54:43.860	    7fde55486740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [5] ./build/release/bin/monerod:epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::init_server(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&)+0xef [0x55a4c3c45daf]
2017-10-12 17:54:43.860	    7fde55486740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [6] ./build/release/bin/monerod:nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::init(boost::program_options::variables_map const&)+0x179a [0x55a4c3c4770a]
2017-10-12 17:54:43.860	    7fde55486740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [7] ./build/release/bin/monerod:daemonize::t_p2p::t_p2p(boost::program_options::variables_map const&, daemonize::t_protocol&)+0x48c [0x55a4c3c484ec]
2017-10-12 17:54:43.860	    7fde55486740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [8] ./build/release/bin/monerod:daemonize::t_daemon::t_daemon(boost::program_options::variables_map const&)+0x552 [0x55a4c3b8f312]
2017-10-12 17:54:43.860	    7fde55486740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [9] ./build/release/bin/monerod:daemonize::t_executor::run_interactive(boost::program_options::variables_map const&)+0x11 [0x55a4c3c52c01]
2017-10-12 17:54:43.860	    7fde55486740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [10] ./build/release/bin/monerod:bool daemonizer::daemonize<daemonize::t_executor>(int, char const**, daemonize::t_executor&&, boost::program_options::variables_map const&)+0x15e [0x55a4c3c54f5e]
2017-10-12 17:54:43.860	    7fde55486740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [11] ./build/release/bin/monerod:main+0x17c9 [0x55a4c3b649d9]
2017-10-12 17:54:43.860	    7fde55486740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [12] /lib/x86_64-linux-gnu/libc.so.6:__libc_start_main+0xf1 [0x7fde51dde2e1]
2017-10-12 17:54:43.860	    7fde55486740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [13] ./build/release/bin/monerod:_start+0x2a [0x55a4c3b6ce1a]
2017-10-12 17:54:43.860	    7fde55486740	INFO 	stacktrace	src/common/stack_trace.cpp:159	
2017-10-12 17:54:43.860	    7fde55486740	INFO 	stacktrace	src/common/stack_trace.cpp:120	Exception: std::runtime_error
2017-10-12 17:54:43.860	    7fde55486740	INFO 	stacktrace	src/common/stack_trace.cpp:121	Unwound call stack:
2017-10-12 17:54:43.861	    7fde55486740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [1] ./build/release/bin/monerod:__cxa_throw+0xfa [0x55a4c3dd612a]
2017-10-12 17:54:43.861	    7fde55486740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [2] ./build/release/bin/monerod:daemonize::t_p2p::t_p2p(boost::program_options::variables_map const&, daemonize::t_protocol&)+0x5a4 [0x55a4c3c48604]
2017-10-12 17:54:43.861	    7fde55486740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [3] ./build/release/bin/monerod:daemonize::t_daemon::t_daemon(boost::program_options::variables_map const&)+0x552 [0x55a4c3b8f312]
2017-10-12 17:54:43.861	    7fde55486740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [4] ./build/release/bin/monerod:daemonize::t_executor::run_interactive(boost::program_options::variables_map const&)+0x11 [0x55a4c3c52c01]
2017-10-12 17:54:43.861	    7fde55486740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [5] ./build/release/bin/monerod:bool daemonizer::daemonize<daemonize::t_executor>(int, char const**, daemonize::t_executor&&, boost::program_options::variables_map const&)+0x15e [0x55a4c3c54f5e]
2017-10-12 17:54:43.861	    7fde55486740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [6] ./build/release/bin/monerod:main+0x17c9 [0x55a4c3b649d9]
2017-10-12 17:54:43.861	    7fde55486740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [7] /lib/x86_64-linux-gnu/libc.so.6:__libc_start_main+0xf1 [0x7fde51dde2e1]
2017-10-12 17:54:43.861	    7fde55486740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [8] ./build/release/bin/monerod:_start+0x2a [0x55a4c3b6ce1a]
2017-10-12 17:54:43.861	    7fde55486740	INFO 	stacktrace	src/common/stack_trace.cpp:159	
2017-10-12 17:54:43.861	    7fde55486740	INFO 	global	src/daemon/core.h:89	Deinitializing core...
2017-10-12 17:54:43.861	    7fde55486740	INFO 	stacktrace	src/common/stack_trace.cpp:120	Exception: cryptonote::DB_ERROR*
2017-10-12 17:54:43.861	    7fde55486740	INFO 	stacktrace	src/common/stack_trace.cpp:121	Unwound call stack:
2017-10-12 17:54:43.862	    7fde55486740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [1] ./build/release/bin/monerod:__cxa_throw+0xfa [0x55a4c3dd612a]
2017-10-12 17:54:43.862	    7fde55486740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [2] ./build/release/bin/monerod:cryptonote::Blockchain::deinit()+0x9b8 [0x55a4c3d40c08]
2017-10-12 17:54:43.862	    7fde55486740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [3] ./build/release/bin/monerod:cryptonote::core::deinit()+0x25 [0x55a4c3d6eab5]
2017-10-12 17:54:43.862	    7fde55486740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [4] ./build/release/bin/monerod:daemonize::t_core::~t_core()+0xd2 [0x55a4c3bad602]
2017-10-12 17:54:43.862	    7fde55486740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [5] ./build/release/bin/monerod:daemonize::t_daemon::t_daemon(boost::program_options::variables_map const&)+0x935 [0x55a4c3b8f6f5]
2017-10-12 17:54:43.862	    7fde55486740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [6] ./build/release/bin/monerod:daemonize::t_executor::run_interactive(boost::program_options::variables_map const&)+0x11 [0x55a4c3c52c01]
2017-10-12 17:54:43.862	    7fde55486740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [7] ./build/release/bin/monerod:bool daemonizer::daemonize<daemonize::t_executor>(int, char const**, daemonize::t_executor&&, boost::program_options::variables_map const&)+0x15e [0x55a4c3c54f5e]
2017-10-12 17:54:43.862	    7fde55486740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [8] ./build/release/bin/monerod:main+0x17c9 [0x55a4c3b649d9]
2017-10-12 17:54:43.862	    7fde55486740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [9] /lib/x86_64-linux-gnu/libc.so.6:__libc_start_main+0xf1 [0x7fde51dde2e1]
2017-10-12 17:54:43.862	    7fde55486740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [10] ./build/release/bin/monerod:_start+0x2a [0x55a4c3b6ce1a]
2017-10-12 17:54:43.862	    7fde55486740	INFO 	stacktrace	src/common/stack_trace.cpp:159	
2017-10-12 17:54:43.862	    7fde55486740	ERROR	daemon	src/daemon/core.h:94	Failed to deinitialize core...
2017-10-12 17:54:43.862	    7fde55486740	INFO 	global	src/daemon/protocol.h:77	Stopping cryptonote protocol...
2017-10-12 17:54:43.862	    7fde55486740	INFO 	global	src/daemon/protocol.h:81	Cryptonote protocol stopped successfully
2017-10-12 17:54:43.862	    7fde55486740	ERROR	daemon	src/daemon/main.cpp:291	Exception in main! Failed to initialize p2p server.
2017-10-12 18:00:38.361	    7fa77691c740	INFO 	logging	contrib/epee/src/mlog.cpp:180	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-10-12 18:00:38.362	    7fa77691c740	INFO 	global	src/daemon/main.cpp:283	Monero 'Helium Hydra' (v0.11.0.0-86e9de58)
2017-10-12 18:00:38.362	    7fa77691c740	INFO 	global	src/daemon/protocol.h:55	Initializing cryptonote protocol...
2017-10-12 18:00:38.362	    7fa77691c740	INFO 	global	src/daemon/protocol.h:60	Cryptonote protocol initialized OK
2017-10-12 18:00:38.362	    7fa77691c740	INFO 	global	src/daemon/p2p.h:63	Initializing p2p server...
2017-10-12 18:00:38.363	    7fa76d9aa700	WARN 	net.dns	src/common/dns_utils.cpp:207	Using public DNS server: 8.8.4.4 (TCP)
2017-10-12 18:00:58.366	    7fa77691c740	INFO 	stacktrace	src/common/stack_trace.cpp:120	Exception: boost::exception_detail::clone_impl<boost::exception_detail::error_info_injector<boost::system::system_error> >
2017-10-12 18:00:58.366	    7fa77691c740	INFO 	stacktrace	src/common/stack_trace.cpp:121	Unwound call stack:
2017-10-12 18:00:58.368	    7fa77691c740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [1] ./build/release/bin/monerod:__cxa_throw+0xfa [0x55dfbe8cd12a]
2017-10-12 18:00:58.368	    7fa77691c740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [2] ./build/release/bin/monerod:void boost::throw_exception<boost::system::system_error>(boost::system::system_error const&)+0x12d [0x55dfbe69b6cd]
2017-10-12 18:00:58.368	    7fa77691c740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [3] ./build/release/bin/monerod:boost::asio::detail::do_throw_error(boost::system::error_code const&, char const*)+0x4e [0x55dfbe69b76e]
2017-10-12 18:00:58.368	    7fa77691c740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [4] ./build/release/bin/monerod:epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::init_server(unsigned int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)+0xd85 [0x55dfbe73a255]
2017-10-12 18:00:58.368	    7fa77691c740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [5] ./build/release/bin/monerod:epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::init_server(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&)+0xef [0x55dfbe73cdaf]
2017-10-12 18:00:58.368	    7fa77691c740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [6] ./build/release/bin/monerod:nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::init(boost::program_options::variables_map const&)+0x179a [0x55dfbe73e70a]
2017-10-12 18:00:58.368	    7fa77691c740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [7] ./build/release/bin/monerod:daemonize::t_p2p::t_p2p(boost::program_options::variables_map const&, daemonize::t_protocol&)+0x48c [0x55dfbe73f4ec]
2017-10-12 18:00:58.368	    7fa77691c740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [8] ./build/release/bin/monerod:daemonize::t_daemon::t_daemon(boost::program_options::variables_map const&)+0x552 [0x55dfbe686312]
2017-10-12 18:00:58.368	    7fa77691c740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [9] ./build/release/bin/monerod:daemonize::t_executor::run_interactive(boost::program_options::variables_map const&)+0x11 [0x55dfbe749c01]
2017-10-12 18:00:58.368	    7fa77691c740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [10] ./build/release/bin/monerod:bool daemonizer::daemonize<daemonize::t_executor>(int, char const**, daemonize::t_executor&&, boost::program_options::variables_map const&)+0x15e [0x55dfbe74bf5e]
2017-10-12 18:00:58.368	    7fa77691c740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [11] ./build/release/bin/monerod:main+0x17c9 [0x55dfbe65b9d9]
2017-10-12 18:00:58.368	    7fa77691c740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [12] /lib/x86_64-linux-gnu/libc.so.6:__libc_start_main+0xf1 [0x7fa7732742e1]
2017-10-12 18:00:58.368	    7fa77691c740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [13] ./build/release/bin/monerod:_start+0x2a [0x55dfbe663e1a]
2017-10-12 18:00:58.368	    7fa77691c740	INFO 	stacktrace	src/common/stack_trace.cpp:159	
2017-10-12 18:00:58.368	    7fa77691c740	INFO 	stacktrace	src/common/stack_trace.cpp:120	Exception: std::runtime_error
2017-10-12 18:00:58.368	    7fa77691c740	INFO 	stacktrace	src/common/stack_trace.cpp:121	Unwound call stack:
2017-10-12 18:00:58.369	    7fa77691c740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [1] ./build/release/bin/monerod:__cxa_throw+0xfa [0x55dfbe8cd12a]
2017-10-12 18:00:58.369	    7fa77691c740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [2] ./build/release/bin/monerod:daemonize::t_p2p::t_p2p(boost::program_options::variables_map const&, daemonize::t_protocol&)+0x5a4 [0x55dfbe73f604]
2017-10-12 18:00:58.369	    7fa77691c740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [3] ./build/release/bin/monerod:daemonize::t_daemon::t_daemon(boost::program_options::variables_map const&)+0x552 [0x55dfbe686312]
2017-10-12 18:00:58.369	    7fa77691c740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [4] ./build/release/bin/monerod:daemonize::t_executor::run_interactive(boost::program_options::variables_map const&)+0x11 [0x55dfbe749c01]
2017-10-12 18:00:58.369	    7fa77691c740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [5] ./build/release/bin/monerod:bool daemonizer::daemonize<daemonize::t_executor>(int, char const**, daemonize::t_executor&&, boost::program_options::variables_map const&)+0x15e [0x55dfbe74bf5e]
2017-10-12 18:00:58.369	    7fa77691c740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [6] ./build/release/bin/monerod:main+0x17c9 [0x55dfbe65b9d9]
2017-10-12 18:00:58.369	    7fa77691c740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [7] /lib/x86_64-linux-gnu/libc.so.6:__libc_start_main+0xf1 [0x7fa7732742e1]
2017-10-12 18:00:58.369	    7fa77691c740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [8] ./build/release/bin/monerod:_start+0x2a [0x55dfbe663e1a]
2017-10-12 18:00:58.369	    7fa77691c740	INFO 	stacktrace	src/common/stack_trace.cpp:159	
2017-10-12 18:00:58.369	    7fa77691c740	INFO 	global	src/daemon/core.h:89	Deinitializing core...
2017-10-12 18:00:58.369	    7fa77691c740	INFO 	stacktrace	src/common/stack_trace.cpp:120	Exception: cryptonote::DB_ERROR*
2017-10-12 18:00:58.369	    7fa77691c740	INFO 	stacktrace	src/common/stack_trace.cpp:121	Unwound call stack:
2017-10-12 18:00:58.370	    7fa77691c740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [1] ./build/release/bin/monerod:__cxa_throw+0xfa [0x55dfbe8cd12a]
2017-10-12 18:00:58.370	    7fa77691c740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [2] ./build/release/bin/monerod:cryptonote::Blockchain::deinit()+0x9b8 [0x55dfbe837c08]
2017-10-12 18:00:58.370	    7fa77691c740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [3] ./build/release/bin/monerod:cryptonote::core::deinit()+0x25 [0x55dfbe865ab5]
2017-10-12 18:00:58.370	    7fa77691c740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [4] ./build/release/bin/monerod:daemonize::t_core::~t_core()+0xd2 [0x55dfbe6a4602]
2017-10-12 18:00:58.370	    7fa77691c740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [5] ./build/release/bin/monerod:daemonize::t_daemon::t_daemon(boost::program_options::variables_map const&)+0x935 [0x55dfbe6866f5]
2017-10-12 18:00:58.370	    7fa77691c740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [6] ./build/release/bin/monerod:daemonize::t_executor::run_interactive(boost::program_options::variables_map const&)+0x11 [0x55dfbe749c01]
2017-10-12 18:00:58.370	    7fa77691c740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [7] ./build/release/bin/monerod:bool daemonizer::daemonize<daemonize::t_executor>(int, char const**, daemonize::t_executor&&, boost::program_options::variables_map const&)+0x15e [0x55dfbe74bf5e]
2017-10-12 18:00:58.370	    7fa77691c740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [8] ./build/release/bin/monerod:main+0x17c9 [0x55dfbe65b9d9]
2017-10-12 18:00:58.370	    7fa77691c740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [9] /lib/x86_64-linux-gnu/libc.so.6:__libc_start_main+0xf1 [0x7fa7732742e1]
2017-10-12 18:00:58.370	    7fa77691c740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [10] ./build/release/bin/monerod:_start+0x2a [0x55dfbe663e1a]
2017-10-12 18:00:58.370	    7fa77691c740	INFO 	stacktrace	src/common/stack_trace.cpp:159	
2017-10-12 18:00:58.370	    7fa77691c740	ERROR	daemon	src/daemon/core.h:94	Failed to deinitialize core...
2017-10-12 18:00:58.370	    7fa77691c740	INFO 	global	src/daemon/protocol.h:77	Stopping cryptonote protocol...
2017-10-12 18:00:58.370	    7fa77691c740	INFO 	global	src/daemon/protocol.h:81	Cryptonote protocol stopped successfully
2017-10-12 18:00:58.371	    7fa77691c740	ERROR	daemon	src/daemon/main.cpp:291	Exception in main! Failed to initialize p2p server.
2017-10-12 18:03:04.044	    7ff234672740	INFO 	logging	contrib/epee/src/mlog.cpp:180	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-10-12 18:03:04.044	    7ff234672740	INFO 	global	src/daemon/main.cpp:283	Monero 'Helium Hydra' (v0.11.0.0-86e9de58)
2017-10-12 18:03:04.044	    7ff234672740	INFO 	global	src/daemon/protocol.h:55	Initializing cryptonote protocol...
2017-10-12 18:03:04.044	    7ff234672740	INFO 	global	src/daemon/protocol.h:60	Cryptonote protocol initialized OK
2017-10-12 18:03:04.045	    7ff234672740	INFO 	global	src/daemon/p2p.h:63	Initializing p2p server...
2017-10-12 18:03:04.045	    7ff22b700700	WARN 	net.dns	src/common/dns_utils.cpp:207	Using public DNS server: 8.8.4.4 (TCP)
2017-10-12 18:03:24.049	    7ff234672740	INFO 	stacktrace	src/common/stack_trace.cpp:120	Exception: boost::exception_detail::clone_impl<boost::exception_detail::error_info_injector<boost::system::system_error> >
2017-10-12 18:03:24.050	    7ff234672740	INFO 	stacktrace	src/common/stack_trace.cpp:121	Unwound call stack:
2017-10-12 18:03:24.051	    7ff234672740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [1] ./build/release/bin/monerod:__cxa_throw+0xfa [0x560a3f9a812a]
2017-10-12 18:03:24.051	    7ff234672740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [2] ./build/release/bin/monerod:void boost::throw_exception<boost::system::system_error>(boost::system::system_error const&)+0x12d [0x560a3f7766cd]
2017-10-12 18:03:24.051	    7ff234672740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [3] ./build/release/bin/monerod:boost::asio::detail::do_throw_error(boost::system::error_code const&, char const*)+0x4e [0x560a3f77676e]
2017-10-12 18:03:24.051	    7ff234672740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [4] ./build/release/bin/monerod:epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::init_server(unsigned int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)+0xd85 [0x560a3f815255]
2017-10-12 18:03:24.051	    7ff234672740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [5] ./build/release/bin/monerod:epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::init_server(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&)+0xef [0x560a3f817daf]
2017-10-12 18:03:24.052	    7ff234672740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [6] ./build/release/bin/monerod:nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::init(boost::program_options::variables_map const&)+0x179a [0x560a3f81970a]
2017-10-12 18:03:24.052	    7ff234672740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [7] ./build/release/bin/monerod:daemonize::t_p2p::t_p2p(boost::program_options::variables_map const&, daemonize::t_protocol&)+0x48c [0x560a3f81a4ec]
2017-10-12 18:03:24.052	    7ff234672740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [8] ./build/release/bin/monerod:daemonize::t_daemon::t_daemon(boost::program_options::variables_map const&)+0x552 [0x560a3f761312]
2017-10-12 18:03:24.052	    7ff234672740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [9] ./build/release/bin/monerod:daemonize::t_executor::run_interactive(boost::program_options::variables_map const&)+0x11 [0x560a3f824c01]
2017-10-12 18:03:24.052	    7ff234672740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [10] ./build/release/bin/monerod:bool daemonizer::daemonize<daemonize::t_executor>(int, char const**, daemonize::t_executor&&, boost::program_options::variables_map const&)+0x15e [0x560a3f826f5e]
2017-10-12 18:03:24.052	    7ff234672740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [11] ./build/release/bin/monerod:main+0x17c9 [0x560a3f7369d9]
2017-10-12 18:03:24.052	    7ff234672740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [12] /lib/x86_64-linux-gnu/libc.so.6:__libc_start_main+0xf1 [0x7ff230fca2e1]
2017-10-12 18:03:24.052	    7ff234672740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [13] ./build/release/bin/monerod:_start+0x2a [0x560a3f73ee1a]
2017-10-12 18:03:24.052	    7ff234672740	INFO 	stacktrace	src/common/stack_trace.cpp:159	
2017-10-12 18:03:24.052	    7ff234672740	INFO 	stacktrace	src/common/stack_trace.cpp:120	Exception: std::runtime_error
2017-10-12 18:03:24.052	    7ff234672740	INFO 	stacktrace	src/common/stack_trace.cpp:121	Unwound call stack:
2017-10-12 18:03:24.053	    7ff234672740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [1] ./build/release/bin/monerod:__cxa_throw+0xfa [0x560a3f9a812a]
2017-10-12 18:03:24.053	    7ff234672740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [2] ./build/release/bin/monerod:daemonize::t_p2p::t_p2p(boost::program_options::variables_map const&, daemonize::t_protocol&)+0x5a4 [0x560a3f81a604]
2017-10-12 18:03:24.053	    7ff234672740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [3] ./build/release/bin/monerod:daemonize::t_daemon::t_daemon(boost::program_options::variables_map const&)+0x552 [0x560a3f761312]
2017-10-12 18:03:24.053	    7ff234672740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [4] ./build/release/bin/monerod:daemonize::t_executor::run_interactive(boost::program_options::variables_map const&)+0x11 [0x560a3f824c01]
2017-10-12 18:03:24.053	    7ff234672740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [5] ./build/release/bin/monerod:bool daemonizer::daemonize<daemonize::t_executor>(int, char const**, daemonize::t_executor&&, boost::program_options::variables_map const&)+0x15e [0x560a3f826f5e]
2017-10-12 18:03:24.053	    7ff234672740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [6] ./build/release/bin/monerod:main+0x17c9 [0x560a3f7369d9]
2017-10-12 18:03:24.053	    7ff234672740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [7] /lib/x86_64-linux-gnu/libc.so.6:__libc_start_main+0xf1 [0x7ff230fca2e1]
2017-10-12 18:03:24.053	    7ff234672740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [8] ./build/release/bin/monerod:_start+0x2a [0x560a3f73ee1a]
2017-10-12 18:03:24.053	    7ff234672740	INFO 	stacktrace	src/common/stack_trace.cpp:159	
2017-10-12 18:03:24.053	    7ff234672740	INFO 	global	src/daemon/core.h:89	Deinitializing core...
2017-10-12 18:03:24.053	    7ff234672740	INFO 	stacktrace	src/common/stack_trace.cpp:120	Exception: cryptonote::DB_ERROR*
2017-10-12 18:03:24.053	    7ff234672740	INFO 	stacktrace	src/common/stack_trace.cpp:121	Unwound call stack:
2017-10-12 18:03:24.054	    7ff234672740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [1] ./build/release/bin/monerod:__cxa_throw+0xfa [0x560a3f9a812a]
2017-10-12 18:03:24.054	    7ff234672740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [2] ./build/release/bin/monerod:cryptonote::Blockchain::deinit()+0x9b8 [0x560a3f912c08]
2017-10-12 18:03:24.054	    7ff234672740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [3] ./build/release/bin/monerod:cryptonote::core::deinit()+0x25 [0x560a3f940ab5]
2017-10-12 18:03:24.054	    7ff234672740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [4] ./build/release/bin/monerod:daemonize::t_core::~t_core()+0xd2 [0x560a3f77f602]
2017-10-12 18:03:24.054	    7ff234672740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [5] ./build/release/bin/monerod:daemonize::t_daemon::t_daemon(boost::program_options::variables_map const&)+0x935 [0x560a3f7616f5]
2017-10-12 18:03:24.054	    7ff234672740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [6] ./build/release/bin/monerod:daemonize::t_executor::run_interactive(boost::program_options::variables_map const&)+0x11 [0x560a3f824c01]
2017-10-12 18:03:24.054	    7ff234672740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [7] ./build/release/bin/monerod:bool daemonizer::daemonize<daemonize::t_executor>(int, char const**, daemonize::t_executor&&, boost::program_options::variables_map const&)+0x15e [0x560a3f826f5e]
2017-10-12 18:03:24.054	    7ff234672740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [8] ./build/release/bin/monerod:main+0x17c9 [0x560a3f7369d9]
2017-10-12 18:03:24.054	    7ff234672740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [9] /lib/x86_64-linux-gnu/libc.so.6:__libc_start_main+0xf1 [0x7ff230fca2e1]
2017-10-12 18:03:24.054	    7ff234672740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [10] ./build/release/bin/monerod:_start+0x2a [0x560a3f73ee1a]
2017-10-12 18:03:24.054	    7ff234672740	INFO 	stacktrace	src/common/stack_trace.cpp:159	
2017-10-12 18:03:24.054	    7ff234672740	ERROR	daemon	src/daemon/core.h:94	Failed to deinitialize core...
2017-10-12 18:03:24.054	    7ff234672740	INFO 	global	src/daemon/protocol.h:77	Stopping cryptonote protocol...
2017-10-12 18:03:24.054	    7ff234672740	INFO 	global	src/daemon/protocol.h:81	Cryptonote protocol stopped successfully
2017-10-12 18:03:24.054	    7ff234672740	ERROR	daemon	src/daemon/main.cpp:291	Exception in main! Failed to initialize p2p server.
```


## chamalis | 2017-10-13T09:57:55+00:00
Should we reopen this?

# Action History
- Created by: xmrminer2017 | 2017-08-27T16:35:29+00:00
- Closed at: 2017-08-28T15:00:15+00:00
