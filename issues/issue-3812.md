---
title: 'monerod stuck because of "Exception: cryptonote::BLOCK_DNE"'
source_url: https://github.com/monero-project/monero/issues/3812
author: Jnchk
assignees: []
labels: []
created_at: '2018-05-16T10:28:30+00:00'
updated_at: '2018-05-19T10:39:05+00:00'
type: issue
status: closed
closed_at: '2018-05-19T10:38:03+00:00'
---

# Original Description
It seems that it happens when we meet this "Sync data returned a new top block candidate: 1573899 -> 1567592 [Your node is 6307 blocks (8 days) ahead]".

Full logs:
```
2018-05-16 10:05:25.558     7fd0d1664740        INFO    global  src/daemon/main.cpp:280 Monero 'Lithium Luna' (v0.12.0.0-master-release)
2018-05-16 10:05:25.558     7fd0d1664740        INFO    global  src/daemon/protocol.h:53        Initializing cryptonote protocol...
2018-05-16 10:05:25.558     7fd0d1664740        INFO    global  src/daemon/protocol.h:58        Cryptonote protocol initialized OK
2018-05-16 10:05:25.561     7fd0d1664740        INFO    global  src/daemon/p2p.h:63     Initializing p2p server...
2018-05-16 10:05:30.121     7fd0d1664740        INFO    global  src/daemon/p2p.h:68     p2p server initialized OK
2018-05-16 10:05:30.122     7fd0d1664740        INFO    global  src/daemon/rpc.h:63     Initializing core RPC server...
2018-05-16 10:05:30.122     7fd0d1664740        INFO    global  contrib/epee/include/net/http_server_impl_base.h:76     Binding on 127.0.0.1:18081
2018-05-16 10:05:30.122     7fd0d1664740        INFO    global  src/daemon/rpc.h:69     core RPC server initialized OK on port: 18081
2018-05-16 10:05:30.122     7fd0d1664740        INFO    global  src/daemon/core.h:86    Initializing core...
2018-05-16 10:05:30.122     7fd0d1664740        INFO    global  src/cryptonote_core/cryptonote_core.cpp:427     Loading blockchain from folder /root/.bitmonero/lmdb ...
2018-05-16 10:05:30.159     7fd0d1664740        INFO    global  src/cryptonote_core/cryptonote_core.cpp:525     Loading checkpoints
2018-05-16 10:05:31.221     7fd0d1664740        WARN    net.dns src/common/dns_utils.cpp:508    WARNING: no two valid MoneroPulse DNS checkpoint records were received
2018-05-16 10:05:31.221     7fd0d1664740        INFO    global  src/daemon/core.h:92    Core initialized OK
2018-05-16 10:05:31.221     7fd0d1664740        INFO    global  src/daemon/rpc.h:74     Starting core RPC server...
2018-05-16 10:05:31.221 [SRV_MAIN]      INFO    global  src/daemon/rpc.h:79     core RPC server started ok
2018-05-16 10:05:31.227 [SRV_MAIN]      INFO    global  src/daemon/p2p.h:78     Starting p2p net loop...
2018-05-16 10:05:32.227 [P2P2]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1386    ^[[1;33m
**********************************************************************
The daemon will start synchronizing with the network. This may take a long time to complete.

You can set the level of process detailization through "set_log <level|categories>" command,
where <level> is between 0 (no details) and 4 (very verbose), or custom category based levels (eg, *:WARNING).

Use the "help" command to see the list of available commands.
Use "help <command>" to see a command's documentation.
**********************************************************************
^[[0m
2018-05-16 10:05:33.253 [P2P2]  WARN    net.dns src/common/dns_utils.cpp:508    WARNING: no two valid MoneroPulse DNS checkpoint records were received
2018-05-16 10:05:33.588 [P2P7]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1579    ^[[1;33m
**********************************************************************
You are now synchronized with the network. You may now start monero-wallet-cli.

Use the "help" command to see the list of available commands.
**********************************************************************^[[0m
2018-05-16 10:05:45.909 [P2P6]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:310     [93.105.187.121:18080 OUT] Sync data returned a new top block candidate: 1573899 -> 1567592 [Your node is 6307 blocks (8 days) ahead]
SYNCHRONIZATION started
2018-05-16 10:05:52.363 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:124  Exception: cryptonote::BLOCK_DNE
2018-05-16 10:05:52.363 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:125  Unwound call stack:
2018-05-16 10:05:52.368 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:163      [1] ./monerod:__wrap___cxa_throw+0x10a [0x7fd0d1c5e1ba]
2018-05-16 10:05:52.368 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:163      [2] ./monerod+0x51b0c9 [0x7fd0d1b890c9]
2018-05-16 10:05:52.368 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:163      [3] ./monerod:cryptonote::BlockchainLMDB::get_block_height(crypto::hash const&) const+0x437 [0x7fd0d1b97137]
2018-05-16 10:05:52.368 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:163      [4] ./monerod:cryptonote::BlockchainLMDB::get_block_blob[abi:cxx11](crypto::hash const&) const+0x144 [0x7fd0d1b89ea4]
2018-05-16 10:05:52.368 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:163      [5] ./monerod:bool cryptonote::Blockchain::get_blocks<std::__cxx11::list<crypto::hash, std::allocator<crypto::hash> >, std::__cxx11::list<std::pair<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, cryptonote::block>, std::allocator<std::pair<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, cryptonote::block> > >, std::__cxx11::list<crypto::hash, std::allocator<crypto::hash> > >(std::__cxx11::list<crypto::hash, std::allocator<crypto::hash> > const&, std::__cxx11::list<std::pair<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, cryptonote::block>, std::allocator<std::pair<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, cryptonote::block> > >&, std::__cxx11::list<crypto::hash, std::allocator<crypto::hash> >&) const+0x1f1 [0x7fd0d1bec511]
2018-05-16 10:05:52.368 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:163      [6] ./monerod:cryptonote::Blockchain::handle_get_objects(cryptonote::NOTIFY_REQUEST_GET_OBJECTS::request&, cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request&)+0x1de [0x7fd0d1bd369e]
2018-05-16 10:05:52.368 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:163      [7] ./monerod:cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::handle_request_get_objects(int, cryptonote::NOTIFY_REQUEST_GET_OBJECTS::request&, cryptonote::cryptonote_connection_context&)+0x18f [0x7fd0d1b4ddbf]
2018-05-16 10:05:52.368 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:163      [8] ./monerod:int epee::net_utils::buff_to_t_adapter<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, cryptonote::NOTIFY_REQUEST_GET_OBJECTS::request, cryptonote::cryptonote_connection_context, boost::_bi::bind_t<int, boost::_mfi::mf3<int, cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, int, cryptonote::NOTIFY_REQUEST_GET_OBJECTS::request&, cryptonote::cryptonote_connection_context&>, boost::_bi::list4<boost::_bi::value<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*>, boost::arg<1>, boost::arg<2>, boost::arg<3> > > >(cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, boost::_bi::bind_t<int, boost::_mfi::mf3<int, cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, int, cryptonote::NOTIFY_REQUEST_GET_OBJECTS::request&, cryptonote::cryptonote_connection_context&>, boost::_bi::list4<boost::_bi::value<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*>, boost::arg<1>, boost::arg<2>, boost::arg<3> > >, cryptonote::cryptonote_connection_context&)+0x24f [0x7fd0d19da13f]
2018-05-16 10:05:52.368 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:163      [9] ./monerod:int cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::handle_invoke_map<cryptonote::cryptonote_connection_context>(bool, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&, cryptonote::cryptonote_connection_context&, bool&)+0x2aa [0x7fd0d19e983a]
2018-05-16 10:05:52.368 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:163      [10] ./monerod:int nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::handle_invoke_map<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >(bool, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&, bool&)+0xc2 [0x7fd0d19e9ac2]
2018-05-16 10:05:52.368 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:163      [11] ./monerod:nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::notify(int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&)+0x50 [0x7fd0d19e9e90]
2018-05-16 10:05:52.368 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:163      [12] ./monerod:epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >::handle_recv(void const*, unsigned long)+0x4ad [0x7fd0d1b6a0ad]
2018-05-16 10:05:52.368 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:163      [13] ./monerod:epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::handle_read(boost::system::error_code const&, unsigned long)+0x1f8 [0x7fd0d1b81ea8]
2018-05-16 10:05:52.368 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:163      [14] ./monerod:void boost::asio::detail::strand_service::dispatch<boost::asio::detail::binder2<boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::system::error_code, unsigned long> >(boost::asio::detail::strand_service::strand_impl*&, boost::asio::detail::binder2<boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::system::error_code, unsigned long>&)+0x7a [0x7fd0d1b4adfa]
2018-05-16 10:05:52.368 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:163      [15] ./monerod:boost::asio::detail::completion_handler<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > > >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long)+0x188 [0x7fd0d1b4b268]
2018-05-16 10:05:52.368 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:163      [16] ./monerod:void boost::asio::detail::strand_service::dispatch<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > > >(boost::asio::detail::strand_service::strand_impl*&, boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > >&)+0x226 [0x7fd0d1b4b656]
2018-05-16 10:05:52.368 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:163      [17] ./monerod:boost::asio::detail::reactive_socket_recv_op<boost::asio::mutable_buffers_1, boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running> >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long)+0x250 [0x7fd0d1b4b930]
2018-05-16 10:05:52.368 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:163      [18] ./monerod:boost::asio::detail::epoll_reactor::descriptor_state::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long)+0x1f4 [0x7fd0d19692e4]
2018-05-16 10:05:52.368 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:163      [19] ./monerod:epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread()+0x854 [0x7fd0d1b2fb54]
2018-05-16 10:05:52.368 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:163      [20] ./monerod+0x9870c5 [0x7fd0d1ff50c5]
2018-05-16 10:05:52.368 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:163      [21] /lib/x86_64-linux-gnu/libpthread.so.0+0x76ba [0x7fd0d0d236ba]
2018-05-16 10:05:52.368 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:163      [22] /lib/x86_64-linux-gnu/libc.so.6:clone+0x6d [0x7fd0d0a5941d]
2018-05-16 10:05:52.368 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:163
```
Environment: ubuntu:16.04 in docker
Command: ./monerod --rpc-bind-port 18081 --log-file /var/log/monerod.log
Software version: 0.12.0.0 Lithium Luna downloaded from https://getmonero.org/downloads/#linux

# Discussion History
## baryluk | 2018-05-16T15:31:37+00:00
After getting very close to synchronization I started getting exactly same exceptions too. My node managed to synchronize, but I still see these exception every few hours. And when they happen they happen in a batch of multiple exceptions each just few milliseconds apart, and then nothing for few hours.

```text
$ grep src/common/stack_trace.cpp:124  ~/.bitmonero/bitmonero.log
2018-05-15 20:54:49.129	    7f46523c9700	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: boost::thread_interrupted
2018-05-15 23:15:26.238	    7fe63ffff700	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: boost::thread_interrupted
2018-05-15 23:28:00.830	    7f91d5da8700	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: boost::thread_interrupted
2018-05-15 23:58:36.897	    7f1b2093b700	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: boost::thread_interrupted
2018-05-16 01:21:10.513	    7f7e1bfff700	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: boost::thread_interrupted
2018-05-16 03:15:57.560	[P2P8]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 03:15:57.605	[P2P8]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 03:15:57.609	[P2P8]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 03:15:57.614	[P2P8]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 03:15:57.619	[P2P8]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 03:15:57.623	[P2P8]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 03:15:57.628	[P2P8]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 03:15:57.633	[P2P8]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 03:15:57.638	[P2P8]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 03:15:57.643	[P2P8]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 03:15:57.648	[P2P8]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 03:15:57.653	[P2P8]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 03:15:57.658	[P2P8]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 03:15:57.663	[P2P8]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 03:15:57.669	[P2P8]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 03:15:57.674	[P2P8]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 03:15:57.679	[P2P8]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 03:15:57.684	[P2P8]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 03:15:57.689	[P2P8]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 03:15:57.694	[P2P8]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 04:47:05.866	[P2P2]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 04:47:05.871	[P2P2]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 04:47:05.877	[P2P2]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 04:47:05.882	[P2P2]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 04:47:05.887	[P2P2]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 04:47:05.892	[P2P2]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 04:47:05.897	[P2P2]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 04:47:05.902	[P2P2]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 04:47:05.907	[P2P2]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 04:47:05.913	[P2P2]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 04:47:05.918	[P2P2]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 04:47:05.923	[P2P2]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 04:47:05.928	[P2P2]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 04:47:05.933	[P2P2]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 04:47:05.938	[P2P2]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 04:47:05.943	[P2P2]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 04:47:05.949	[P2P2]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 04:47:05.954	[P2P2]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 04:47:05.959	[P2P2]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 04:47:05.964	[P2P2]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 05:33:50.705	[P2P9]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 05:33:50.710	[P2P9]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 05:33:50.716	[P2P9]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 05:33:50.721	[P2P9]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 05:33:50.726	[P2P9]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 05:33:50.731	[P2P9]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 05:33:50.736	[P2P9]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 05:33:50.741	[P2P9]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 05:33:50.746	[P2P9]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 05:33:50.751	[P2P9]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 05:33:50.757	[P2P9]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 05:33:50.762	[P2P9]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 05:33:50.767	[P2P9]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 05:33:50.772	[P2P9]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 05:33:50.777	[P2P9]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 05:33:50.782	[P2P9]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 05:33:50.787	[P2P9]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 05:33:50.792	[P2P9]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 05:33:50.797	[P2P9]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 05:33:50.802	[P2P9]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 06:44:04.002	[P2P1]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 06:44:04.021	[P2P1]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 06:44:04.026	[P2P1]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 06:44:04.037	[P2P1]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 06:44:04.042	[P2P1]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 06:44:04.047	[P2P1]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 06:44:04.052	[P2P1]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 06:44:04.057	[P2P1]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 06:44:04.062	[P2P1]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 06:44:04.067	[P2P1]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 06:44:04.073	[P2P1]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 06:44:04.078	[P2P1]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 06:44:04.083	[P2P1]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 06:44:04.088	[P2P1]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 06:44:04.093	[P2P1]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 06:44:04.098	[P2P1]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 06:44:04.103	[P2P1]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 06:44:04.108	[P2P1]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 06:44:04.113	[P2P1]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 06:44:04.118	[P2P1]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 09:02:19.142	[P2P2]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 09:02:19.162	[P2P2]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 09:02:19.167	[P2P2]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 09:02:19.172	[P2P2]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 09:02:19.178	[P2P2]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 09:02:19.183	[P2P2]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 09:02:19.188	[P2P2]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 09:02:19.193	[P2P2]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 09:02:19.198	[P2P2]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 09:02:19.203	[P2P2]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 09:02:19.209	[P2P2]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 09:02:19.214	[P2P2]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 09:02:19.219	[P2P2]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 09:02:19.224	[P2P2]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 09:02:19.229	[P2P2]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 09:02:19.235	[P2P2]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 09:02:19.240	[P2P2]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 09:02:19.245	[P2P2]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 09:02:19.250	[P2P2]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 09:02:19.256	[P2P2]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 09:04:32.364	[P2P9]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 09:04:32.370	[P2P9]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 09:04:32.375	[P2P9]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 09:04:32.380	[P2P9]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 09:04:32.385	[P2P9]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 09:04:32.390	[P2P9]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 09:04:32.396	[P2P9]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 09:04:32.401	[P2P9]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 09:04:32.406	[P2P9]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 09:04:32.411	[P2P9]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 09:04:32.416	[P2P9]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 09:04:32.421	[P2P9]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 09:04:32.426	[P2P9]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 09:04:32.431	[P2P9]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 09:04:32.436	[P2P9]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 09:04:32.441	[P2P9]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 09:04:32.446	[P2P9]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 09:04:32.451	[P2P9]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 09:04:32.456	[P2P9]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 09:04:32.462	[P2P9]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 13:27:45.857	[P2P7]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 13:27:45.888	[P2P7]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 13:27:45.894	[P2P7]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 13:27:45.899	[P2P7]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 13:27:45.905	[P2P7]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 13:27:45.911	[P2P7]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 13:27:45.917	[P2P7]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 13:27:45.922	[P2P7]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 13:27:45.928	[P2P7]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 13:27:45.934	[P2P7]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 13:27:45.939	[P2P7]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 13:27:45.945	[P2P7]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 13:27:45.950	[P2P7]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 13:27:45.956	[P2P7]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 13:27:45.962	[P2P7]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 13:27:45.968	[P2P7]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 13:27:45.974	[P2P7]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 13:27:45.980	[P2P7]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 13:27:45.986	[P2P7]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 13:27:45.991	[P2P7]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 13:59:40.355	[P2P4]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 13:59:40.368	[P2P4]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 13:59:40.374	[P2P4]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 13:59:40.379	[P2P4]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 13:59:40.384	[P2P4]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 13:59:40.389	[P2P4]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 13:59:40.394	[P2P4]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 13:59:40.399	[P2P4]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 13:59:40.404	[P2P4]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 13:59:40.409	[P2P4]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 13:59:40.414	[P2P4]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 13:59:40.419	[P2P4]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 13:59:40.424	[P2P4]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 13:59:40.429	[P2P4]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 13:59:40.434	[P2P4]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 13:59:40.439	[P2P4]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 13:59:40.444	[P2P4]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 13:59:40.450	[P2P4]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 13:59:40.455	[P2P4]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 13:59:40.460	[P2P4]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 14:07:35.630	[P2P5]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 14:07:35.637	[P2P5]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 14:07:35.643	[P2P5]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 14:07:35.648	[P2P5]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 14:07:35.653	[P2P5]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 14:07:35.658	[P2P5]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 14:07:35.663	[P2P5]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 14:07:35.669	[P2P5]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 14:07:35.674	[P2P5]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 14:07:35.679	[P2P5]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 14:07:35.684	[P2P5]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 14:07:35.689	[P2P5]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 14:07:35.695	[P2P5]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 14:07:35.700	[P2P5]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 14:07:35.705	[P2P5]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 14:07:35.710	[P2P5]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 14:07:35.715	[P2P5]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 14:07:35.720	[P2P5]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 14:07:35.725	[P2P5]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 14:07:35.730	[P2P5]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 15:07:10.599	[P2P3]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 15:07:10.618	[P2P3]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 15:07:10.624	[P2P3]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 15:07:10.629	[P2P3]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 15:07:10.634	[P2P3]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 15:07:10.639	[P2P3]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 15:07:10.644	[P2P3]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 15:07:10.649	[P2P3]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 15:07:10.654	[P2P3]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 15:07:10.659	[P2P3]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 15:07:10.665	[P2P3]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 15:07:10.670	[P2P3]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 15:07:10.675	[P2P3]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 15:07:10.680	[P2P3]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 15:07:10.685	[P2P3]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 15:07:10.690	[P2P3]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 15:07:10.695	[P2P3]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 15:07:10.700	[P2P3]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 15:07:10.705	[P2P3]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-16 15:07:10.710	[P2P3]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
```

## dEBRUYNE-1 | 2018-05-16T16:14:35+00:00
See #3284 

## moneromooo-monero | 2018-05-16T18:02:42+00:00
These two things are unrelated. The sync problems are fixed in current release-0.12. The spammy DNE logs are also silenced where appropriate.




## baryluk | 2018-05-16T22:17:10+00:00
Ok. I guess I posted this in the wrong bug, as I didn't seen the other one, it was recently closed. But I do use 0.12, so I shouldn't be getting these messages probably.

## moneromooo-monero | 2018-05-16T22:28:35+00:00
You're likely using v0.12.0.0 rather than release-0.12, right ?

## Jnchk | 2018-05-17T02:53:57+00:00
@moneromooo-monero  yes, i'm using v0.12.0.0.
But where can i get release-0.12, should I build the release-0.12 manually?

## moneromooo-monero | 2018-05-17T07:29:11+00:00
You do this:

git clone https://github.com/monero-project/monero/
cd monero
git checkout release-0.12
make

If you already have a monero tree, you can skip the first step.
You need to build it, yes. There are no binaries with these fixes yet.

## stoffu | 2018-05-17T07:54:11+00:00
If first time cloning, you'd need `git clone --recursive https://github.com/monero-project/monero/`.
Otherwise, make sure any submodules are up to date by `git submodule init && git submodule update`

## jtgrassie | 2018-05-17T11:22:16+00:00
@stoffu 
> `git submodule init && git submodule update`

Or even `git submodule update --init`



## Jnchk | 2018-05-18T06:26:49+00:00
Thank you for your advice. But I got an error when I was building the source code.
Here are the logs:
```
[ 93%] Building CXX object tests/unit_tests/CMakeFiles/unit_tests.dir/sha256.cpp.o
[ 94%] Building CXX object tests/unit_tests/CMakeFiles/unit_tests.dir/slow_memmem.cpp.o
[ 94%] Building CXX object tests/unit_tests/CMakeFiles/unit_tests.dir/subaddress.cpp.o
[ 94%] Building CXX object tests/unit_tests/CMakeFiles/unit_tests.dir/test_tx_utils.cpp.o
[ 95%] Building CXX object tests/unit_tests/CMakeFiles/unit_tests.dir/test_peerlist.cpp.o
[ 95%] Building CXX object tests/unit_tests/CMakeFiles/unit_tests.dir/test_protocol_pack.cpp.o
[ 95%] Building CXX object tests/unit_tests/CMakeFiles/unit_tests.dir/hardfork.cpp.o
[ 96%] Building CXX object tests/unit_tests/CMakeFiles/unit_tests.dir/unbound.cpp.o
[ 96%] Building CXX object tests/unit_tests/CMakeFiles/unit_tests.dir/uri.cpp.o
[ 96%] Building CXX object tests/unit_tests/CMakeFiles/unit_tests.dir/varint.cpp.o
[ 97%] Building CXX object tests/unit_tests/CMakeFiles/unit_tests.dir/ringct.cpp.o
[ 97%] Building CXX object tests/unit_tests/CMakeFiles/unit_tests.dir/output_selection.cpp.o
[ 97%] Building CXX object tests/unit_tests/CMakeFiles/unit_tests.dir/vercmp.cpp.o
[ 98%] Linking CXX executable unit_tests
/usr/bin/ld: /usr/lib/gcc/x86_64-linux-gnu/5/../../../../lib/libgtest.a(gtest-all.cc.o): relocation R_X86_64_32 against `.rodata' can not be used when making a shared object; recompile with -fPIC
/usr/lib/gcc/x86_64-linux-gnu/5/../../../../lib/libgtest.a: error adding symbols: Bad value
collect2: error: ld returned 1 exit status
tests/unit_tests/CMakeFiles/unit_tests.dir/build.make:1205: recipe for target 'tests/unit_tests/unit_tests' failed
make[3]: *** [tests/unit_tests/unit_tests] Error 1
make[3]: Leaving directory '/root/monero-recursive/build/release'
CMakeFiles/Makefile2:4425: recipe for target 'tests/unit_tests/CMakeFiles/unit_tests.dir/all' failed
make[2]: *** [tests/unit_tests/CMakeFiles/unit_tests.dir/all] Error 2
make[2]: Leaving directory '/root/monero-recursive/build/release'
Makefile:138: recipe for target 'all' failed
make[1]: *** [all] Error 2
make[1]: Leaving directory '/root/monero-recursive/build/release'
Makefile:64: recipe for target 'release-all' failed
make: *** [release-all] Error 2
root@bc2cb1d5ea2d:~/monero-recursive# 
```
Build commands are below
```
git clone --recursive https://github.com/monero-project/monero.git monero-recursive
git checkout -b 12 origin/release-v0.12
make
```
`libgtest*.a` are generated by the commands in README.
```
ls /usr/lib/gcc/x86_64-linux-gnu/5/../../../../lib/libgt*
/usr/lib/gcc/x86_64-linux-gnu/5/../../../../lib/libgtest.a
/usr/lib/gcc/x86_64-linux-gnu/5/../../../../lib/libgtest_main.a
```
Do i need some update of libgtest?

## stoffu | 2018-05-18T06:41:19+00:00
As the error message says:

> recompile with -fPIC

The error is caused by your system's `libgtest` not being compiled with -fPIC. The gtest source is bundled in the Monero repository, so you can simply uninstall your system's gtest and build the bundled one.


## Jnchk | 2018-05-18T08:57:21+00:00
I followed this answer https://stackoverflow.com/a/38297422/8157756, and add `set(CMAKE_POSITION_INDEPENDENT_CODE ON)` to `cmake/internal_utils.cmake` under `/usr/src/gtest` and then execute
```
root@bc2cb1d5ea2d:/usr/src/gtest# pwd
/usr/src/gtest
root@bc2cb1d5ea2d:/usr/src/gtest# ls cmake/internal_utils.cmake 
cmake/internal_utils.cmake
root@bc2cb1d5ea2d:/usr/src/gtest# cmake .
root@bc2cb1d5ea2d:/usr/src/gtest# make
```
then I can compile monero bins successfully. But it still depends on libzmq3-dev libunbound-dev. And when i build monero with `make release-static`, I will get this error
```
[ 88%] Building CXX object src/wallet/CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o
[ 89%] Linking CXX executable ../../bin/monero-wallet-rpc
/usr/bin/ld: /usr/lib/gcc/x86_64-linux-gnu/5/../../../x86_64-linux-gnu/libboost_chrono.a(chrono.o): relocation R_X86_64_32 against `.rodata.str1.1' can not be used when making a shared object; recompile with -fPIC
/usr/lib/gcc/x86_64-linux-gnu/5/../../../x86_64-linux-gnu/libboost_chrono.a: error adding symbols: Bad value
collect2: error: ld returned 1 exit status
src/wallet/CMakeFiles/wallet_rpc_server.dir/build.make:133: recipe for target 'bin/monero-wallet-rpc' failed
make[3]: *** [bin/monero-wallet-rpc] Error 1
make[3]: Leaving directory '/root/monero-recursive/build/release'
CMakeFiles/Makefile2:2367: recipe for target 'src/wallet/CMakeFiles/wallet_rpc_server.dir/all' failed
make[2]: *** [src/wallet/CMakeFiles/wallet_rpc_server.dir/all] Error 2
make[2]: Leaving directory '/root/monero-recursive/build/release'
Makefile:138: recipe for target 'all' failed
make[1]: *** [all] Error 2
make[1]: Leaving directory '/root/monero-recursive/build/release'
Makefile:68: recipe for target 'release-static' failed
make: *** [release-static] Error 2
```
Does it mean that I need to rebuild libboost? Anyway, I think i've got a workable monerod :).
Thank you guys. Thank you very much.

## Jnchk | 2018-05-19T10:39:05+00:00
The new compiled monerod just works fine. Close the Issue.

# Action History
- Created by: Jnchk | 2018-05-16T10:28:30+00:00
- Closed at: 2018-05-19T10:38:03+00:00
