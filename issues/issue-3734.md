---
title: Monero 0.12 stuck again
source_url: https://github.com/monero-project/monero/issues/3734
author: khelle
assignees: []
labels: []
created_at: '2018-04-30T11:25:20+00:00'
updated_at: '2018-05-16T10:40:57+00:00'
type: issue
status: closed
closed_at: '2018-05-16T10:40:57+00:00'
---

# Original Description
Hi, 
I had previously problem of blockchain sync beind stucked because of me not updating the node before the fork. I reported this and then fixed by doing blockchain rollback in issue #3657 . Doing that my node started to sync, worked for few days properly then again randomly stuck at 1562078. 

My logs are full of:

```
2018-04-30 11:18:58.270	[P2P7]	ERROR	verify	src/cryptonote_core/blockchain.cpp:1485	Block recognized as orphaned and rejected, id = <d26b91ac9c31e54bf90eaa23b290a09e4dc3d0236163b49d0e8cf5467d5a5480>, height 1562079, parent in alt 0, parent in main 0 (parent <5ae2602be524283870085adc8ad76ff176b7fae2fbc067fb48a4f10b38f2b116>, current top <af06c2be50b23c2e7e9414c3b1a3b6b636b6ce42dfb05d14048632b1a559f436>, chain height 1562078)
```

And:

```
2018-04-30 11:19:00.172	[P2P5]	INFO 	stacktrace	src/common/stack_trace.cpp:163	
2018-04-30 11:19:00.172	[P2P5]	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:82	Attempted to retrieve non-existent block height
2018-04-30 11:19:00.172	[P2P5]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-04-30 11:19:00.172	[P2P5]	INFO 	stacktrace	src/common/stack_trace.cpp:125	Unwound call stack:
2018-04-30 11:19:00.178	[P2P5]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [1] /home/xmr/node/bin/monerod:__wrap___cxa_throw+0x10a [0x55d7d8cbe1ba]
2018-04-30 11:19:00.178	[P2P5]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [2] /home/xmr/node/bin/monerod+0x51b0c9 [0x55d7d8be90c9]
2018-04-30 11:19:00.178	[P2P5]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [3] /home/xmr/node/bin/monerod:cryptonote::BlockchainLMDB::get_block_height(crypto::hash const&) const+0x437 [0x55d7d8bf7137]
2018-04-30 11:19:00.178	[P2P5]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [4] /home/xmr/node/bin/monerod:cryptonote::BlockchainLMDB::get_block_blob[abi:cxx11](crypto::hash const&) const+0x144 [0x55d7d8be9ea4]
2018-04-30 11:19:00.178	[P2P5]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [5] /home/xmr/node/bin/monerod:bool cryptonote::Blockchain::get_blocks<std::__cxx11::list<crypto::hash, std::allocator<crypto::hash> >, std::__cxx11::list<std::pair<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, cryptonote::block>, std::allocator<std::pair<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, cryptonote::block> > >, std::__cxx11::list<crypto::hash, std::allocator<crypto::hash> > >(std::__cxx11::list<crypto::hash, std::allocator<crypto::hash> > const&, std::__cxx11::list<std::pair<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, cryptonote::block>, std::allocator<std::pair<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, cryptonote::block> > >&, std::__cxx11::list<crypto::hash, std::allocator<crypto::hash> >&) const+0x1f1 [0x55d7d8c4c511]
2018-04-30 11:19:00.178	[P2P5]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [6] /home/xmr/node/bin/monerod:cryptonote::Blockchain::handle_get_objects(cryptonote::NOTIFY_REQUEST_GET_OBJECTS::request&, cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request&)+0x1de [0x55d7d8c3369e]
2018-04-30 11:19:00.178	[P2P5]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [7] /home/xmr/node/bin/monerod:cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::handle_request_get_objects(int, cryptonote::NOTIFY_REQUEST_GET_OBJECTS::request&, cryptonote::cryptonote_connection_context&)+0x18f [0x55d7d8baddbf]
2018-04-30 11:19:00.178	[P2P5]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [8] /home/xmr/node/bin/monerod:int epee::net_utils::buff_to_t_adapter<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, cryptonote::NOTIFY_REQUEST_GET_OBJECTS::request, cryptonote::cryptonote_connection_context, boost::_bi::bind_t<int, boost::_mfi::mf3<int, cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, int, cryptonote::NOTIFY_REQUEST_GET_OBJECTS::request&, cryptonote::cryptonote_connection_context&>, boost::_bi::list4<boost::_bi::value<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*>, boost::arg<1>, boost::arg<2>, boost::arg<3> > > >(cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, boost::_bi::bind_t<int, boost::_mfi::mf3<int, cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, int, cryptonote::NOTIFY_REQUEST_GET_OBJECTS::request&, cryptonote::cryptonote_connection_context&>, boost::_bi::list4<boost::_bi::value<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*>, boost::arg<1>, boost::arg<2>, boost::arg<3> > >, cryptonote::cryptonote_connection_context&)+0x24f [0x55d7d8a3a13f]
2018-04-30 11:19:00.178	[P2P5]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [9] /home/xmr/node/bin/monerod:int cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::handle_invoke_map<cryptonote::cryptonote_connection_context>(bool, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&, cryptonote::cryptonote_connection_context&, bool&)+0x2aa [0x55d7d8a4983a]
2018-04-30 11:19:00.178	[P2P5]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [10] /home/xmr/node/bin/monerod:int nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::handle_invoke_map<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >(bool, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&, bool&)+0xc2 [0x55d7d8a49ac2]
2018-04-30 11:19:00.178	[P2P5]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [11] /home/xmr/node/bin/monerod:nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::notify(int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&)+0x50 [0x55d7d8a49e90]
2018-04-30 11:19:00.178	[P2P5]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [12] /home/xmr/node/bin/monerod:epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >::handle_recv(void const*, unsigned long)+0x4ad [0x55d7d8bca0ad]
2018-04-30 11:19:00.178	[P2P5]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [13] /home/xmr/node/bin/monerod:epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::handle_read(boost::system::error_code const&, unsigned long)+0x1f8 [0x55d7d8be1ea8]
2018-04-30 11:19:00.178	[P2P5]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [14] /home/xmr/node/bin/monerod:void boost::asio::detail::strand_service::dispatch<boost::asio::detail::binder2<boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::system::error_code, unsigned long> >(boost::asio::detail::strand_service::strand_impl*&, boost::asio::detail::binder2<boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::system::error_code, unsigned long>&)+0x7a [0x55d7d8baadfa]
2018-04-30 11:19:00.178	[P2P5]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [15] /home/xmr/node/bin/monerod:boost::asio::detail::completion_handler<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > > >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long)+0x188 [0x55d7d8bab268]
2018-04-30 11:19:00.178	[P2P5]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [16] /home/xmr/node/bin/monerod:void boost::asio::detail::strand_service::dispatch<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > > >(boost::asio::detail::strand_service::strand_impl*&, boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > >&)+0x226 [0x55d7d8bab656]
2018-04-30 11:19:00.178	[P2P5]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [17] /home/xmr/node/bin/monerod:boost::asio::detail::reactive_socket_recv_op<boost::asio::mutable_buffers_1, boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running> >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long)+0x250 [0x55d7d8bab930]
2018-04-30 11:19:00.178	[P2P5]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [18] /home/xmr/node/bin/monerod:boost::asio::detail::epoll_reactor::descriptor_state::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long)+0x1f4 [0x55d7d89c92e4]
2018-04-30 11:19:00.178	[P2P5]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [19] /home/xmr/node/bin/monerod:epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread()+0x854 [0x55d7d8b8fb54]
2018-04-30 11:19:00.178	[P2P5]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [20] /home/xmr/node/bin/monerod+0x9870c5 [0x55d7d90550c5]
2018-04-30 11:19:00.178	[P2P5]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [21] /lib/x86_64-linux-gnu/libpthread.so.0+0x76ba [0x7f382ba516ba]
2018-04-30 11:19:00.178	[P2P5]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [22] /lib/x86_64-linux-gnu/libc.so.6:clone+0x6d [0x7f382b7873dd]
2018-04-30 11:19:00.178	[P2P5]	INFO 	stacktrace	src/common/stack_trace.cpp:163	
```

Seems to me a little like my node now has only pre-fork peers and is not able to move forward as they are another split.  What's the cause of this? How can I deal with that? Do I need another rollback?

# Discussion History
## moneromooo-monero | 2018-04-30T16:19:32+00:00
Post the output of:
status
sync_info
print_cn


## khelle | 2018-04-30T20:41:14+00:00
print_cn:

```
Remote Host                   Peer id             Support Flags       Recv/Sent (inactive,sec)      State                    Livetime(sec)       Down (kB/s) Down(now)     Up (kB/s) Up(now)      

INC 177.249.193.13:26036      8bea776fb282cffa    1                   27194(9)/14087098(9)          state_normal             128                 0           0             107       767          
OUT 79.143.181.221:18080      a10a38bf2e19497e    1                   266092(23)/122497(23)         state_normal             239                 1           2             0         0            
INC 220.73.27.229:36550       7a9d527e75067536    1                   27904(20)/898037(20)          state_normal             89                  0           2             9         64           
OUT 116.204.24.95:18080       f332d1d22295cf3f    1                   209724(3)/12547265(3)         state_normal             403                 0           0             30        37           
OUT 77.47.27.174:18080        a35a8fb168f2a446    1                   546008(24)/75550080(23)       state_normal             747                 0           1             98        198          
INC 185.5.28.231:51122        d2122ea058163ae1    1                   110639(10)/49168392(10)       state_normal             307                 0           0             156       2            
OUT 94.140.125.242:18080      386dd87105acf1b4    1                   382949(21)/22314660(21)       state_normal             933                 0           2             23        208          
INC 95.79.25.171:62092        10431c96cac1595b    1                   1918690(3)/2260473374(3)      state_normal             3068                0           0             719       993          
INC 193.251.162.94:57040      afa60164bfeebf99    1                   5464325(1)/484563464(1)       state_normal             3473                1           1             136       149          
OUT 74.75.46.39:18080         841579fc3428fec2    1                   1491218(6)/64503464(6)        state_normal             3822                0           2             16        48           
OUT 123.193.38.189:18080      c51953418bc9b4cf    1                   1435372(114)/345960547(94)    state_normal             4003                0           0             84        0            
OUT 70.74.217.186:18080       6d51f282acc32a31    1                   1909971(20)/146351537(20)     state_normal             4698                0           2             30        6            
INC 90.181.13.58:9161         16a26392247f4568    1                   7857592(21)/260305158(21)     state_normal             22179               0           2             11        37 
```

sync_info
```
Height: 1562078, target: 1562794 (99.9542%)
Downloading at 10 kB/s
15 peers
109.169.3.47:18080        337381faa7b5dcf3  1562794  5 kB/s, 0 blocks / 0 MB queued
125.238.232.131:18080     a4a46de314382e1f  1546200  2 kB/s, 0 blocks / 0 MB queued
177.249.193.13:26036      8bea776fb282cffa  1383880  0 kB/s, 0 blocks / 0 MB queued
220.73.27.229:36550       7a9d527e75067536  1553237  0 kB/s, 0 blocks / 0 MB queued
116.204.24.95:18080       f332d1d22295cf3f  1551936  0 kB/s, 0 blocks / 0 MB queued
77.47.27.174:18080        a35a8fb168f2a446  119056  1 kB/s, 0 blocks / 0 MB queued
185.5.28.231:51122        d2122ea058163ae1  1560807  2 kB/s, 0 blocks / 0 MB queued
94.140.125.242:18080      386dd87105acf1b4  1557789  0 kB/s, 0 blocks / 0 MB queued
95.79.25.171:62092        10431c96cac1595b  1357908  0 kB/s, 0 blocks / 0 MB queued
193.251.162.94:57040      afa60164bfeebf99  1041376  0 kB/s, 0 blocks / 0 MB queued
74.75.46.39:18080         841579fc3428fec2  322992  0 kB/s, 0 blocks / 0 MB queued
123.193.38.189:18080      c51953418bc9b4cf  1448356  0 kB/s, 0 blocks / 0 MB queued
46.166.187.49:56625       0000000000000000  0  0 kB/s, 0 blocks / 0 MB queued
70.74.217.186:18080       6d51f282acc32a31  1561540  0 kB/s, 0 blocks / 0 MB queued
90.181.13.58:9161         16a26392247f4568  507936  0 kB/s, 0 blocks / 0 MB queued
110 spans, 134.367 MB
                          20 (1546020 - 1546039, 329 kB)  14 kB/s (0)
                          20 (1546040 - 1546059, 335 kB)  9 kB/s (0)
                          20 (1546060 - 1546079, 243 kB)  8 kB/s (0)
                          20 (1546080 - 1546099, 378 kB)  18 kB/s (0)
                          20 (1546100 - 1546119, 349 kB)  14 kB/s (0)
                          20 (1546120 - 1546139, 1251 kB)  11 kB/s (0)
                          20 (1546140 - 1546159, 985 kB)  9 kB/s (0)
                          20 (1546160 - 1546179, 464 kB)  11 kB/s (0)
                          20 (1546180 - 1546199, 475 kB)  12 kB/s (0)
                          20 (1546200 - 1546219, 381 kB)  19 kB/s (0)
                          20 (1546220 - 1546239, 442 kB)  5 kB/s (0)
                          20 (1546240 - 1546259, 470 kB)  8 kB/s (0)
                          20 (1546260 - 1546279, 559 kB)  14 kB/s (0)
                          20 (1546280 - 1546299, 339 kB)  11 kB/s (0)
                          20 (1546300 - 1546319, 299 kB)  18 kB/s (0)
                          20 (1546320 - 1546339, 1061 kB)  14 kB/s (0)
                          20 (1546340 - 1546359, 213 kB)  12 kB/s (0)
                          20 (1546360 - 1546379, 213 kB)  9 kB/s (0)
                          20 (1546380 - 1546399, 162 kB)  12 kB/s (0)
                          20 (1546400 - 1546419, 218 kB)  15 kB/s (0)
                          20 (1546420 - 1546439, 226 kB)  27 kB/s (0)
                          20 (1546440 - 1546459, 479 kB)  23 kB/s (0)
                          20 (1546460 - 1546479, 125 kB)  7 kB/s (0)
                          20 (1546480 - 1546499, 185 kB)  7 kB/s (0)
                          20 (1546500 - 1546519, 238 kB)  8 kB/s (0)
                          20 (1546520 - 1546539, 205 kB)  8 kB/s (0)
                          20 (1546540 - 1546559, 108 kB)  5 kB/s (0)
                          20 (1546560 - 1546579, 145 kB)  11 kB/s (0)
                          20 (1546580 - 1546599, 110 kB)  6 kB/s (0)
                          20 (1546600 - 1546619, 55 kB)  7 kB/s (0)
                          20 (1546620 - 1546639, 181 kB)  1 kB/s (0)
                          20 (1546640 - 1546659, 98 kB)  11 kB/s (0)
                          20 (1546660 - 1546679, 70 kB)  9 kB/s (0)
                          20 (1546680 - 1546699, 159 kB)  6 kB/s (0)
                          20 (1546700 - 1546719, 175 kB)  15 kB/s (0)
                          20 (1546720 - 1546739, 191 kB)  2 kB/s (0)
                          20 (1546740 - 1546759, 254 kB)  2 kB/s (0)
                          20 (1546760 - 1546779, 120 kB)  1 kB/s (0)
                          20 (1546780 - 1546799, 107 kB)  1 kB/s (0)
                          1 (1560620 - 1560620, 307 kB)  448 kB/s (0.04)
                          20 (1562079 - 1562098, 2076 kB)  1604 kB/s (0.14)
                          20 (1562099 - 1562118, 2991 kB)  5651 kB/s (0.42)
                          20 (1562119 - 1562138, 3579 kB)  8970 kB/s (0.42)
                          20 (1562139 - 1562158, 4565 kB)  10125 kB/s (0.42)
                          20 (1562159 - 1562178, 3080 kB)  8689 kB/s (0.42)
                          20 (1562179 - 1562198, 3888 kB)  9496 kB/s (0.42)
                          20 (1562199 - 1562218, 1796 kB)  2368 kB/s (0.42)
                          20 (1562219 - 1562238, 2789 kB)  388 kB/s (0.42)
                          20 (1562239 - 1562258, 3462 kB)  9270 kB/s (0.42)
                          20 (1562259 - 1562278, 5664 kB)  11086 kB/s (0.42)
                          20 (1562279 - 1562298, 3092 kB)  8083 kB/s (0.42)
                          20 (1562299 - 1562318, 3086 kB)  7764 kB/s (0.42)
                          20 (1562319 - 1562338, 2635 kB)  1925 kB/s (0.42)
                          20 (1562339 - 1562358, 2753 kB)  527 kB/s (0.42)
                          20 (1562359 - 1562378, 6107 kB)  10408 kB/s (0.42)
                          20 (1562379 - 1562398, 4179 kB)  9842 kB/s (0.42)
                          20 (1562399 - 1562418, 3728 kB)  6536 kB/s (0.42)
                          20 (1562419 - 1562438, 3151 kB)  6305 kB/s (0.42)
                          20 (1562439 - 1562458, 2997 kB)  474 kB/s (0.42)
                          20 (1562459 - 1562478, 3276 kB)  10343 kB/s (0.42)
                          20 (1562479 - 1562498, 2163 kB)  6175 kB/s (0.42)
                          20 (1562499 - 1562518, 4397 kB)  9620 kB/s (0.42)
                          1 (1562519 - 1562519, 301 kB)  1915 kB/s (0.42)
                          3 (1562520 - 1562522, 542 kB)  2176 kB/s (0.18)
                          1 (1562523 - 1562523, 277 kB)  20 kB/s (0)
                          9 (1562524 - 1562532, 1975 kB)  6094 kB/s (0.52)
                          2 (1562533 - 1562534, 372 kB)  89 kB/s (0.01)
                          2 (1562535 - 1562536, 506 kB)  1262 kB/s (0.11)
                          20 (1562537 - 1562556, 3207 kB)  914 kB/s (0.05)
                          3 (1562557 - 1562559, 372 kB)  193 kB/s (0.05)
                          4 (1562560 - 1562563, 908 kB)  142 kB/s (0.01)
                          2 (1562564 - 1562565, 390 kB)  2338 kB/s (0.2)
                          20 (1562566 - 1562585, 2277 kB)  76 kB/s (0.01)
                          19 (1562586 - 1562604, 2490 kB)  81 kB/s (0.01)
                          11 (1562605 - 1562615, 2499 kB)  11827 kB/s (1)
                          5 (1562616 - 1562620, 1542 kB)  770 kB/s (0.07)
                          19 (1562621 - 1562639, 2902 kB)  64 kB/s (0)
                          1 (1562640 - 1562640, 300 kB)  33 kB/s (0)
                          1 (1562641 - 1562641, 310 kB)  2217 kB/s (0.19)
                          6 (1562642 - 1562647, 1086 kB)  185 kB/s (0.02)
                          20 (1562648 - 1562667, 3389 kB)  78 kB/s (0)
                          20 (1562668 - 1562687, 2776 kB)  29 kB/s (0)
                          20 (1562688 - 1562707, 3282 kB)  45 kB/s (0)
                          9 (1562708 - 1562716, 1404 kB)  56 kB/s (0)
                          18 (1562717 - 1562734, 2824 kB)  42 kB/s (0)
                          5 (1562735 - 1562739, 1320 kB)  223 kB/s (0.02)
                          3 (1562740 - 1562742, 681 kB)  35 kB/s (0)
                          1 (1562743 - 1562743, 218 kB)  35 kB/s (0)
                          8 (1562744 - 1562751, 2037 kB)  92 kB/s (0.01)
                          1 (1562752 - 1562752, 230 kB)  97 kB/s (0.01)
                          5 (1562753 - 1562757, 679 kB)  753 kB/s (0.06)
                          1 (1562758 - 1562758, 13 kB)  15 kB/s (0)
                          1 (1562759 - 1562759, 144 kB)  266 kB/s (0.02)
                          1 (1562760 - 1562760, 207 kB)  1561 kB/s (0.13)
                          3 (1562761 - 1562763, 646 kB)  3285 kB/s (0.28)
                          1 (1562764 - 1562764, 108 kB)  108 kB/s (0.01)
                          1 (1562765 - 1562765, 299 kB)  223 kB/s (0.02)
                          1 (1562766 - 1562766, 95 kB)  219 kB/s (0.02)
                          1 (1562767 - 1562767, 27 kB)  353 kB/s (0.03)
                          1 (1562768 - 1562768, 67 kB)  173 kB/s (0.01)
                          10 (1562769 - 1562778, 1111 kB)  2513 kB/s (0.21)
                          5 (1562779 - 1562783, 528 kB)  1249 kB/s (0.11)
                          1 (1562784 - 1562784, 39 kB)  151 kB/s (0.01)
                          2 (1562785 - 1562786, 602 kB)  2430 kB/s (0.21)
                          1 (1562787 - 1562787, 217 kB)  1419 kB/s (0.12)
                          1 (1562788 - 1562788, 163 kB)  376 kB/s (0.03)
                          2 (1562789 - 1562790, 155 kB)  331 kB/s (0.03)
                          1 (1562791 - 1562791, 40 kB)  103 kB/s (0.01)
                          1 (1562792 - 1562792, 299 kB)  1146 kB/s (0.1)
                          1 (1562793 - 1562793, 295 kB)  1315 kB/s (0.11)
```

status:

```
Height: 1562078/1562078 (100.0%) on mainnet, not mining, net hash 512.88 MH/s, v7, up to date, 6(out)+8(in) connections, uptime 0d 9h 55m 50s
```

## moneromooo-monero | 2018-04-30T21:48:26+00:00
This is likely fixed by https://github.com/monero-project/monero/pull/3723

## khelle | 2018-05-01T10:45:50+00:00
So how do I fix this issue now? Build binaries from the master directly?

## moneromooo-monero | 2018-05-01T10:53:00+00:00
Build from release-0.12

## gorthorb | 2018-05-05T03:42:59+00:00
I'm seeing (what seems like) exactly the same thing on a node that was working fine until a few days ago.  I've built from release-v0.12 (af6febaa8) plus c188615 cherry-picked to fix the build.

Here's a representative snapshot:

- I restart the node:

```
2018-05-05 03:02:37.900 [P2P2]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:310     [128.199.252.162:18080 OUT] Sync data returned a new top block candidate: 1565707 -> 1565828 [Your node is 121 blocks (0 days) behind]
```

- It connects to peers that are advertising recent blocks:

```
2018-05-05 03:05:22.380 [P2P1]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:310     [82.211.130.137:18080 OUT] Sync data returned a new top block candidate: 1565707 -> 1565829 [Your node is 122 blocks (0 days) behind]
SYNCHRONIZATION started
2018-05-05 03:05:25.582 [P2P1]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:310     [67.175.0.251:62939 INC] Sync data returned a new top block candidate: 1565707 -> 1565829 [Your node is 122 blocks (0 days) behind]
SYNCHRONIZATION started
```

- sync_info / status / print_cn:

```
sync_info
Height: 1565707, target: 1565829 (99.9922%)
Downloading at 2 kB/s
9 peers
67.175.0.251:62939        0000000000000000  1565829  0 kB/s, 0 blocks / 0 MB queued
91.200.28.85:18080        3a3a42f482321b24  1548079  2 kB/s, 0 blocks / 0 MB queued
72.94.61.216:18080        1e7b2bb0d3acf8aa  1388952  0 kB/s, 0 blocks / 0 MB queued
47.52.29.96:51386         1f2eb8c8a97746b1  1565707  0 kB/s, 0 blocks / 0 MB queued
217.121.47.2:18080        1153400e5a2a4b7d  1565707  0 kB/s, 0 blocks / 0 MB queued
24.207.102.89:52316       fd58182a91890f2c  1565056  0 kB/s, 0 blocks / 0 MB queued
217.182.101.234:18080     2b26ae493de642ae  1565707  0 kB/s, 0 blocks / 0 MB queued
37.200.46.80:18080        1383f9f54784bf1e  1354904  0 kB/s, 0 blocks / 0 MB queued
178.150.5.221:18080       4fb020a0e461c351  1409400  0 kB/s, 0 blocks / 0 MB queued
0 spans, 0 MB

status
Height: 1565707/1565829 (99.9%) on mainnet, not mining, net hash 494.70 MH/s, v7, up to date, 7(out)+2(in) connections, uptime 0d 0h 3m 59s

print_cn
Remote Host                   Peer id             Support Flags       Recv/Sent (inactive,sec)      State                    Livetime(sec)       Down (kB/s) Down(now)     Up (kB/s) Up(now)

OUT 47.254.34.54:18080        0000000000000000    0                   0(4)/259(4)                   state_before_handshake   4                   0           0             0         0
OUT 138.197.182.111:18080     d16f35c2662b8436    1                   20440644(13)/22745(13)        state_normal             28                  712         932           0         1
OUT 91.200.28.85:18080        3a3a42f482321b24    1                   55860(5)/12174650(4)          state_normal             89                  0           0             133       278
OUT 72.94.61.216:18080        1e7b2bb0d3acf8aa    1                   28560(44)/13976330(25)        state_normal             160                 0           0             85        0
INC 47.52.29.96:51386         1f2eb8c8a97746b1    1                   75518(24)/62246(25)           state_normal             165                 0           2             0         0
OUT 217.121.47.2:18080        1153400e5a2a4b7d    1                   112980(24)/75686(25)          state_normal             218                 0           2             0         0
INC 24.207.102.89:52316       fd58182a91890f2c    1                   5982(73)/9065224(25)          state_normal             99                  0           0             89        0
OUT 217.182.101.234:18080     2b26ae493de642ae    1                   113148(24)/86636(25)          state_normal             219                 0           2             0         0
OUT 178.150.5.221:18080       4fb020a0e461c351    1                   78925(16)/10118073(16)        state_normal             238                 0           2             41        275
```

- A minute later, it seems to have completely forgotten about 1565829, and now thinks it's up-to-date!

```
sync_info
Height: 1565707, target: 1565707 (100%)
Downloading at 48 kB/s
11 peers
24.253.254.189:18080      851336bf80b874f8  1565707  1 kB/s, 0 blocks / 0 MB queued
31.185.253.62:40112       16ff0173b5f6f5e9  1562224  34 kB/s, 0 blocks / 0 MB queued
85.165.70.216:18080       89e9c906a12e87c5  1380260  0 kB/s, 0 blocks / 0 MB queued
172.112.3.240:18080       6a15f61ac38bc992  982204  1 kB/s, 0 blocks / 0 MB queued
176.63.48.72:18080        ec43cf215f12621b  1565707  1 kB/s, 0 blocks / 0 MB queued
91.200.28.85:18080        3a3a42f482321b24  1548079  0 kB/s, 0 blocks / 0 MB queued
72.94.61.216:18080        1e7b2bb0d3acf8aa  1389752  2 kB/s, 0 blocks / 0 MB queued
47.52.29.96:51386         1f2eb8c8a97746b1  1565707  1 kB/s, 0 blocks / 0 MB queued
217.121.47.2:18080        1153400e5a2a4b7d  1565707  4 kB/s, 0 blocks / 0 MB queued
24.207.102.89:52316       fd58182a91890f2c  1565056  0 kB/s, 0 blocks / 0 MB queued
217.182.101.234:18080     2b26ae493de642ae  1565707  4 kB/s, 0 blocks / 0 MB queued
0 spans, 0 MB
```

- More confusion about what "up to date" means:

```
2018-05-05 03:23:48.435 [P2P0]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:310     [47.156.168.68:58810 INC] Sync data returned a new top block candidate: 1565707 -> 1565832 [Your node is 125 blocks (0 days) behind]
SYNCHRONIZATION started
2018-05-05 03:24:00.350 [P2P9]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:310     [75.172.36.88:52603 INC] Sync data returned a new top block candidate: 1565707 -> 1566328 [Your node is 621 blocks (0 days) behind]
SYNCHRONIZATION started
2018-05-05 03:24:35.433 [P2P0]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:310     [139.219.65.149:1224 INC] Sync data returned a new top block candidate: 1565707 -> 1565832 [Your node is 125 blocks (0 days) behind]
SYNCHRONIZATION started
```

(According to monerohash, 1565832 is the actual latest block at the moment.)

- Regardless, it downloads and downloads, but never advances the top block:

```
sync_info
Height: 1565707, target: 1565838 (99.9916%)
Downloading at 632 kB/s
20 peers
100.16.95.24:18080        818fc2daaf674311  1553800  0 kB/s, 0 blocks / 0 MB queued
97.113.25.37:18080        f4d6ca89c1f6a559  1550386  0 kB/s, 0 blocks / 0 MB queued
77.154.8.125:52244        3796c76facc7c157  1565490  4 kB/s, 0 blocks / 0 MB queued
98.202.151.50:34356       4674b832ac16251f  1565694  4 kB/s, 0 blocks / 0 MB queued
84.55.109.219:53445       2989866c689d8171  1565707  4 kB/s, 0 blocks / 0 MB queued
97.87.103.224:57108       5eb5e0e7fbbd6117  1565838  597 kB/s, 10 blocks / 3.11792 MB queued
134.3.59.240:55054        2b6a189858db3dae  1547734  0 kB/s, 0 blocks / 0 MB queued
74.109.186.21:55513       b3cee3e91dfa1f3b  1302248  2 kB/s, 0 blocks / 0 MB queued
222.1.141.148:50037       5d72b2ed1571e742  1565707  4 kB/s, 0 blocks / 0 MB queued
46.119.230.172:58126      7b2057fbb2200f5d  1553811  0 kB/s, 0 blocks / 0 MB queued
99.16.133.15:53970        436d69ae0e23e466  1559581  0 kB/s, 0 blocks / 0 MB queued
78.137.4.249:18080        a01118f84c07dadf  1565707  4 kB/s, 0 blocks / 0 MB queued
79.169.134.90:40820       75fa3b55a11e1473  1547003  0 kB/s, 0 blocks / 0 MB queued
35.234.98.37:48556        d34cfdad5bb36dee  1546111  2 kB/s, 0 blocks / 0 MB queued
122.116.59.198:42254      6f5bb2059b7e1028  1565707  1 kB/s, 0 blocks / 0 MB queued
91.139.231.245:52580      a3b4b5a615409a1e  1565707  2 kB/s, 0 blocks / 0 MB queued
46.101.101.90:18080       e05a676c8776c77f  1552324  2 kB/s, 0 blocks / 0 MB queued
91.200.28.85:18080        3a3a42f482321b24  1548079  2 kB/s, 0 blocks / 0 MB queued
105.186.195.58:18080      44410c2583cf6bca  1552009  2 kB/s, 0 blocks / 0 MB queued
72.94.61.216:18080        1e7b2bb0d3acf8aa  1395392  2 kB/s, 0 blocks / 0 MB queued
2 spans, 3.11792 MB
97.87.103.224:57108       10 (1565818 - 1565827, 3117 kB)  654 kB/s (1)
97.87.103.224:57108       10 (1565828 - 1565837)  -

sync_info
Height: 1565707, target: 1565707 (100%)
Downloading at 13 kB/s
17 peers
96.255.124.71:50506       0201bc3068ce2010  1564464  5 kB/s, 0 blocks / 0 MB queued
212.32.255.69:46134       853c708a00290a0f  1565449  1 kB/s, 0 blocks / 0 MB queued
121.75.15.62:18080        f7bc47ed135838b0  732591  0 kB/s, 0 blocks / 0 MB queued
78.46.64.150:46032        4a0197cb3b58d63f  1564768  0 kB/s, 0 blocks / 0 MB queued
100.16.95.24:18080        818fc2daaf674311  1553800  0 kB/s, 0 blocks / 0 MB queued
46.101.156.123:52676      14211e2007f36718  1562063  0 kB/s, 0 blocks / 0 MB queued
98.202.151.50:34356       4674b832ac16251f  1565694  3 kB/s, 0 blocks / 0 MB queued
84.55.109.219:53445       2989866c689d8171  1565707  1 kB/s, 0 blocks / 0 MB queued
74.109.186.21:55513       b3cee3e91dfa1f3b  1302568  0 kB/s, 0 blocks / 0 MB queued
222.1.141.148:50037       5d72b2ed1571e742  1565707  1 kB/s, 0 blocks / 0 MB queued
79.169.134.90:40820       75fa3b55a11e1473  1547003  0 kB/s, 0 blocks / 0 MB queued
35.234.98.37:48556        d34cfdad5bb36dee  1546231  0 kB/s, 0 blocks / 0 MB queued
122.116.59.198:42254      6f5bb2059b7e1028  1565707  1 kB/s, 0 blocks / 0 MB queued
91.139.231.245:52580      a3b4b5a615409a1e  1565707  1 kB/s, 0 blocks / 0 MB queued
91.200.28.85:18080        3a3a42f482321b24  1548079  0 kB/s, 0 blocks / 0 MB queued
105.186.195.58:18080      44410c2583cf6bca  1552009  0 kB/s, 0 blocks / 0 MB queued
72.94.61.216:18080        1e7b2bb0d3acf8aa  1395692  0 kB/s, 0 blocks / 0 MB queued
0 spans, 0 MB
```

I hope that helps.

## moneromooo-monero | 2018-05-05T09:00:03+00:00
Looks like it's OK.It finds a potentially better chain, syncs, notices it's actually a bad one, dumps it. Most of the nodes seem to have the same tip, so your chain would only progress once a block is found. Or am I missing a case ?

## gorthorb | 2018-05-05T09:25:19+00:00
Thanks for your reply.  I appreciate your help!

Maybe I'm missing something -- but it seems to me like it's dumping the _good one_, and no matter how many peers connect and try to convince it to join the real chain, it refuses?

It's stuck at 1565707 (now all the way up to 1565715, 5 hours later) even though it hears from lots of nodes about newer chains.

But you're right... it's hearing from those peers one at a time.  Maybe my node is disconnecting them (or vice-versa) before they can form a bigger consensus than these nodes who are all stuck on this dumb 1565715 chain?

Like right now, sync_info is showing that it's talking to _one_ peer with the full chain (1565986 is indeed the current latest block, according to moneroexplorer):

```
Height: 1565714, target: 1565986 (99.9826%)
Downloading at 1144 kB/s
29 peers
145.239.103.146:59946     0000000000000000  0  0 kB/s, 0 blocks / 0 MB queued
195.154.177.56:18080      c30d6aca25332aa1  1553380  2 kB/s, 0 blocks / 0 MB queued
14.201.165.153:56128      79614294097dc91d  1017199  0 kB/s, 0 blocks / 0 MB queued
216.9.177.52:18080        0fdfeee0f05c8ce3  1565713  5 kB/s, 0 blocks / 0 MB queued
62.49.92.9:57085          e0637bf527b6dfae  1555168  0 kB/s, 0 blocks / 0 MB queued
37.117.49.115:56586       1f0c7a7aed11c79c  1565970  0 kB/s, 0 blocks / 0 MB queued
217.72.95.107:54086       f44c6e8c8e309ebb  1565155  0 kB/s, 0 blocks / 0 MB queued
67.213.237.164:53038      5d0b67f636317d73  1565932  0 kB/s, 0 blocks / 0 MB queued
128.199.179.100:18080     7712a907363e4475  1565986  910 kB/s, 0 blocks / 0 MB queued
162.219.178.234:61081     0e250971501707b7  1565970  0 kB/s, 0 blocks / 0 MB queued
5.9.122.17:37918          6032fc4560e2beab  1514266  0 kB/s, 0 blocks / 0 MB queued
109.248.75.203:8811       1356018e3e312eca  1546033  0 kB/s, 0 blocks / 0 MB queued
51.137.107.33:51187       cfb6046918b12cf4  409761  0 kB/s, 0 blocks / 0 MB queued
163.172.171.163:10568     d547cfe03dbbe454  1565969  0 kB/s, 0 blocks / 0 MB queued
80.203.138.103:18080      0000000000000000  0  0 kB/s, 0 blocks / 0 MB queued
73.51.217.1:50122         dee23debb207d568  1549438  0 kB/s, 0 blocks / 0 MB queued
80.203.138.103:54321      46262a9404b06f2a  1565969  0 kB/s, 0 blocks / 0 MB queued
97.93.159.37:58138        994b66259d468c0b  1565715  161 kB/s, 0 blocks / 0 MB queued
203.87.112.172:58089      2307ad4a3829a117  1546024  0 kB/s, 0 blocks / 0 MB queued
188.68.49.154:54568       09178a0882f55503  1549051  0 kB/s, 0 blocks / 0 MB queued
51.171.205.40:44278       58a9895105e3a6d9  1434352  0 kB/s, 0 blocks / 0 MB queued
108.172.144.241:34551     bc75d63e94e5719d  62000  0 kB/s, 0 blocks / 0 MB queued
176.9.17.19:41648         d14c138c74537566  1546719  0 kB/s, 0 blocks / 0 MB queued
78.134.29.69:51660        1cc9683ce2c50516  1565704  0 kB/s, 0 blocks / 0 MB queued
163.172.20.17:43042       514fc0b79e214263  1565969  0 kB/s, 0 blocks / 0 MB queued
59.152.242.84:49891       3a662ee419902515  1565713  66 kB/s, 0 blocks / 0 MB queued
42.200.227.121:64774      ba75e9f07f297277  1548587  0 kB/s, 0 blocks / 0 MB queued
78.148.32.60:18080        aec328c2c13ba5cd  1380016  0 kB/s, 0 blocks / 0 MB queued
60.227.240.63:18080       98abb9f7b3c9d01e  1562993  0 kB/s, 0 blocks / 0 MB queued
1 spans, 0 MB
128.199.179.100:18080     10 (1565921 - 1565930)  -
```

...but then a minute later, something will cause it to stop talking to that node (I guess?) and now it thinks the last block is 1565970:

```
sync_info
Height: 1565715, target: 1565970 (99.9837%)
Downloading at 241 kB/s
30 peers
195.181.243.204:18080     6a0f3a127e6bfffe  1565707  2 kB/s, 0 blocks / 0 MB queued
82.75.208.34:18080        af6b1bb85992e907  1565241  2 kB/s, 0 blocks / 0 MB queued
72.68.224.102:18080       49c72406388653ce  1565715  2 kB/s, 0 blocks / 0 MB queued
195.154.177.56:18080      c30d6aca25332aa1  1553380  2 kB/s, 0 blocks / 0 MB queued
14.201.165.153:56128      79614294097dc91d  1017199  0 kB/s, 0 blocks / 0 MB queued
216.9.177.52:18080        0fdfeee0f05c8ce3  1565713  2 kB/s, 0 blocks / 0 MB queued
62.49.92.9:57085          e0637bf527b6dfae  1555168  0 kB/s, 0 blocks / 0 MB queued
37.117.49.115:56586       1f0c7a7aed11c79c  1565970  0 kB/s, 0 blocks / 0 MB queued
217.72.95.107:54086       f44c6e8c8e309ebb  1565155  0 kB/s, 0 blocks / 0 MB queued
67.213.237.164:53038      5d0b67f636317d73  1565932  0 kB/s, 0 blocks / 0 MB queued
162.219.178.234:61081     0e250971501707b7  1565970  0 kB/s, 0 blocks / 0 MB queued
5.9.122.17:37918          6032fc4560e2beab  1514266  0 kB/s, 0 blocks / 0 MB queued
109.248.75.203:8811       1356018e3e312eca  1546033  0 kB/s, 0 blocks / 0 MB queued
51.137.107.33:51187       cfb6046918b12cf4  409761  0 kB/s, 0 blocks / 0 MB queued
163.172.171.163:10568     d547cfe03dbbe454  1565969  0 kB/s, 0 blocks / 0 MB queued
73.51.217.1:50122         dee23debb207d568  1549438  0 kB/s, 0 blocks / 0 MB queued
80.203.138.103:54321      46262a9404b06f2a  1565969  0 kB/s, 0 blocks / 0 MB queued
97.93.159.37:58138        994b66259d468c0b  1565715  161 kB/s, 0 blocks / 0 MB queued
203.87.112.172:58089      2307ad4a3829a117  1546024  0 kB/s, 0 blocks / 0 MB queued
188.68.49.154:54568       09178a0882f55503  1549051  0 kB/s, 0 blocks / 0 MB queued
51.171.205.40:44278       58a9895105e3a6d9  1434352  0 kB/s, 0 blocks / 0 MB queued
108.172.144.241:34551     bc75d63e94e5719d  62000  0 kB/s, 0 blocks / 0 MB queued
176.9.17.19:41648         d14c138c74537566  1546719  0 kB/s, 0 blocks / 0 MB queued
78.134.29.69:51660        1cc9683ce2c50516  1565704  0 kB/s, 0 blocks / 0 MB queued
163.172.20.17:43042       514fc0b79e214263  1565969  0 kB/s, 0 blocks / 0 MB queued
59.152.242.84:49891       3a662ee419902515  1565713  66 kB/s, 0 blocks / 0 MB queued
42.200.227.121:64774      ba75e9f07f297277  1548587  0 kB/s, 0 blocks / 0 MB queued
213.168.13.151:18080      7ca381f7bc7cb7d2  1565715  2 kB/s, 0 blocks / 0 MB queued
78.148.32.60:18080        aec328c2c13ba5cd  1380016  0 kB/s, 0 blocks / 0 MB queued
60.227.240.63:18080       98abb9f7b3c9d01e  1562993  2 kB/s, 0 blocks / 0 MB queued
0 spans, 0 MB
```

...and then a few minutes later, the "last block" has reverted back to 1565715.

Also, even when it's downloading at 1 MB/sec, it advances to the next block extremely rarely (as you can see, 8 blocks in 5 hours)

My (very layman's) interpretation is that my node doesn't seem to want to hear about the good version of the blockchain that most other people are on.  Like it's stuck on some god-forsaken branch with these other broken nodes, who are somehow managing to form a little clique.  Proper peers do connect and try to make it see the light, but they don't stick around.  A "status" immediately afterward shows that it just won't listen:

```
2018-05-05 09:14:46.636 [P2P7]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:310     [107.193.98.78:59320 INC] Sync data returned a new top block candidate: 1565715 -> 1565991 [Your node is 276 blocks (0 days) behind]
SYNCHRONIZATION started
2018-05-05 09:14:51.540 [P2P9]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:310     [90.188.254.184:18080 OUT] Sync data returned a new top block candidate: 1565715 -> 1565991 [Your node is 276 blocks (0 days) behind]
SYNCHRONIZATION started
2018-05-05 09:15:12.257 [P2P2]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:310     [112.185.110.240:18080 OUT] Sync data returned a new top block candidate: 1565715 -> 1565991 [Your node is 276 blocks (0 days) behind]
SYNCHRONIZATION started
2018-05-05 09:15:36.939 [P2P7]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:310     [188.190.156.232:53223 INC] Sync data returned a new top block candidate: 1565715 -> 1565991 [Your node is 276 blocks (0 days) behind]
SYNCHRONIZATION started
2018-05-05 09:17:00.219 [P2P6]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:310     [138.201.124.177:59448 INC] Sync data returned a new top block candidate: 1565715 -> 1565992 [Your node is 277 blocks (0 days) behind]
SYNCHRONIZATION started
2018-05-05 09:18:39.807 [P2P0]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:310     [193.70.41.139:18080 OUT] Sync data returned a new top block candidate: 1565715 -> 1565993 [Your node is 278 blocks (0 days) behind]
SYNCHRONIZATION started

status
Height: 1565715/1565970 (99.9%) on mainnet, not mining, net hash 494.99 MH/s, v7, up to date, 8(out)+26(in) connections, uptime 0d 2h 17m 5s

2018-05-05 09:19:19.182 [P2P9]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:310     [114.77.116.114:18080 OUT] Sync data returned a new top block candidate: 1565715 -> 1565994 [Your node is 279 blocks (0 days) behind]
SYNCHRONIZATION started

status
Height: 1565715/1565715 (100.0%) on mainnet, not mining, net hash 494.99 MH/s, v7, up to date, 7(out)+5(in) connections, uptime 0d 2h 18m 50s
```

I actually have another node running on a different server, which seems to be OK.  I forced them to connect to each other with --add-priority-node, and you know what happens?  This one that's stuck ends up banning the good one!

Or am I misinterpreting all this?

## moneromooo-monero | 2018-05-05T09:50:10+00:00
Ah, I was assuming that other height was a bad node since it seemed to be the only one claiming it. In that case, it looks like you're right.
In monerod: set_log 1
Then wait for a full set of connecting to such a bad node, and dropping it, then paste the resulting log portion.

## gorthorb | 2018-05-05T11:33:11+00:00
Here we go:

```
2018-05-05 11:24:31.133 [P2P9]  INFO    net.p2p src/p2p/net_node.inl:1761       [95.143.220.103:18080 88179ff3-4011-4e48-d557-f1383eef7633 OUT] NEW CONNECTION
2018-05-05 11:24:31.545 [P2P8]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:310     [95.143.220.103:18080 OUT] Sync data returned a new top block candidate: 1565715 -> 1566060 [Your node is 345 blocks (0 days) behind]
2018-05-05 11:24:31.546 [P2P8]  INFO    net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:313     Remote blockchain height: 1566060, id: <8aa1b9e258193c1d17a3da077971341d51e78edc2663e2f47b2483a6
2018-05-05 11:24:31.844 [P2P4]  INFO    net.p2p.msg     src/cryptonote_protocol/cryptonote_protocol_handler.inl:1605    [95.143.220.103:18080 OUT] Received NOTIFY_RESPONSE_CHAIN_ENTRY: m_block_ids.size()=386, m_start_height=1565674, m_total_height=1566060 src/cryptonote_protocol/cryptonote_protocol_handler.inl:1510    [95.143.220.103:18080 OUT] -->>NOTIFY_REQUEST_GET_OBJECTS: blocks.size()=10, txs.size()=0requested blocks count=10 / 10 from 1565713, first hash <18df45c5743bc8b4eb235df0478e4b2bd72dd619d5851e640918af3abfafbdf1>     [190.72.113.106:58993 INC] Received NOTIFY_REQUEST_GET_OBJECTS (20 blocks, 0 txes)
2018-05-05 11:24:35.542 [P2P5]  INFO    net.p2p.msg     src/cryptonote_protocol/cryptonote_protocol_handler.inl:839     [95.143.220.103:18080 OUT] Received NOTIFY_RESPONSE_GET_OBJECTS (10 blocks, 0 txes)
2018-05-05 11:24:35.616 [P2P5]  ERROR   verify  src/cryptonote_core/blockchain.cpp:1485 Block recognized as orphaned and rejected, id = <18df45c5743bc8b4eb235df0478e4b2bd72dd619d5851e640918af3abfafbdf1>, height 1565713, parent in alt 0, parent in main 0 (parent <b92100b8a012f81b51fdd3cdaa274d0f70f9aba9c12912316ea10dfa39f5e2f4>, current top <1ce9c7f554d0c9f4c709bb3c733803db6b9865a0b9237c2e60654751758de5c3>, chain height 1565715)
2018-05-05 11:24:35.617 [P2P5]  INFO    net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1127    [95.143.220.103:18080 OUT] Block received at sync phase was marked as orphaned, dropping connection
2018-05-05 11:24:35.617 [P2P5]  INFO    net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1734    Target height decreasing from 1566060 to 1565715
2018-05-05 11:24:35.618 [P2P5]  INFO    net.p2p src/p2p/net_node.inl:1776       [95.143.220.103:18080 88179ff3-4011-4e48-d557-f1383eef7633 OUT] CLOSE CONNECTION
```

I see the same story for all of the peers that connect -- that same ID being rejected, and the connection dropped.

## moneromooo-monero | 2018-05-05T12:35:14+00:00
Please paste the output of:
print_block b92100b8a012f81b51fdd3cdaa274d0f70f9aba9c12912316ea10dfa39f5e2f4

## moneromooo-monero | 2018-05-05T12:35:52+00:00
And:
print_bc 1565708 1565715
If it errors out, decrease the second number by one till it works.

## gorthorb | 2018-05-05T13:05:36+00:00
Ask and ye shall receive:

```
print_block b92100b8a012f81b51fdd3cdaa274d0f70f9aba9c12912316ea10dfa39f5e2f4
2018-05-05 12:40:59.723     7fd58e96a700        INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:82   Attempted to retrieve non-existent block height
Error: Unsuccessful --

print_block 18df45c5743bc8b4eb235df0478e4b2bd72dd619d5851e640918af3abfafbdf1
2018-05-05 12:49:29.939     7fd58e96a700        INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:82   Attempted to retrieve non-existent block height
Error: Unsuccessful --
```

Non-existent block _height?_  That's weird.

I seem to be able to give ``print_block`` a height rather than a hash, and _that_ does work (though of course doesn't show us the orphan block we're looking for):

```
print_block 1565713
timestamp: 1525508979
previous hash: 3e52d4418bd8b947bdf1b0019291d30393caa4b69ddf9a563c9054e844b4a0e6
nonce: 4229803
is orphan: 0
height: 1565713
depth: 2
hash: dfe1177bc646bff69d1ec0305f50f32e60986925ee393f93c3ce74f32579172e
difficulty: 58974132822
reward: 4896172189551
{
  "major_version": 7,
  "minor_version": 7,
  "timestamp": 1525508979,
  "prev_id": "3e52d4418bd8b947bdf1b0019291d30393caa4b69ddf9a563c9054e844b4a0e6",
  "nonce": 4229803,
  "miner_tx": {
    "version": 2,
    "unlock_time": 1565773,
    "vin": [ {
        "gen": {
          "height": 1565713
        }
      }
    ],
    "vout": [ {
        "amount": 4896172189551,
        "target": {
          "key": "31624a4ec5c7f029946a766567abd4d2dbcef0531f287c5951e5b32c7a45e649"
        }
      }
    ],
    "extra": [ 1, 8, 190, 255, 164, 234, 61, 124, 226, 143, 10, 29, 237, 160, 159, 215, 39, 170, 225, 111, 229, 105, 83, 138, 221, 161, 135, 51, 165, 179, 154, 31, 53, 2, 8, 156, 2, 0, 23, 74, 0, 0, 0
    ],
    "rct_signatures": {
      "type": 0
    }
  },
  "tx_hashes": [ "3bf9e40dfc9eca57c75fd3d0a1fc9dbc8bae25fbaffd36abdb79b7366ac18734", "ecd773fe1e6f242392ed6519e57341eec172586cff38991e57bc618723c730f1", "04746ba9817214be7577235993e3d1626a8ddff85f4407137df894c700ae3abb", "16b05888794a6df63c6e68d4d9abf15320f93411bc87780668d93e8088d4b745", "6658b51774f62620d70bc294584c3b1b54ace121d005805e7dd5dc9a4448e982", "62edd26f0194754aa4d776893328ca9d91d4635e903223d833e61d7e941ca64a", "16e75225d9c008c04030544f5ef009f1039f0101d92279f98be77a16e58ec09a", "b9013088d743510996fe690a0e7eaa65bffe66f5f24ef18af4edd940902e5191", "3581e3da15b248041d3b6a309582b4d5dd67fd987158a298ef21bc7f2785ec97", "ecc49bbffd8a8ddf047a8f0593c87c7963acd9245d5b63a1edfffb44e33ed967", "1345eee310ce2ca6a781dcee5ba5a65093dcd94836d08e9fa0ef1f910218d0b6", "be48ec56babf49063be221a204be4a84fc9d35b054fc5a19ff7b29d0b1b0f423", "ef8056c7ad7114b8b67392f866efecfef41a4f744b0589da551b61b7262402b1", "9b247c89e576d7486b6d87c89a2017f9e91a3a344872ad330b7f1c8d6cf9b129", "bc4b3a2e2a74380b7bff364280719cfd49612df76a4a800ec41bd3b8e8ad2296", "90ecb52cbc8ece92d7b3d13ec77b29926897d273ef40721ff5a0891c48c05abc", "5540b1b7b4e4ebfcefc8fb78481d10dc98af74d812fca5dc00639aced624f9fd", "33949281090b3cf2457b57fe77aa5bff27838e58fbce55a52616973014e7c0ac", "7f688df27e6032d215fe3523c405be6015e783457d475d4f2f89a231f07e8288"
  ]
}
```

(Though it's worth noting that this is, of course, a completely different block 1565713 than is found on the "authentic" blockchain, which has hash 18df45c5743bc8b4eb235df0478e4b2bd72dd619d5851e640918af3abfafbdf1.)

```
print_bc 1565708 1565715
Error: Unsuccessful --
print_height
1565715
```

But then I came back from reading code a minute later and tried again... now it works?

```
print_bc 1565708 1565715
height: 1565708, timestamp: 1525492133, difficulty: 59143517061, size: 313532, transactions: 22
major version: 7, minor version: 7
block id: f55452373002de26f931c250f7288b97de52fc0cdde8ab9fd0083a4ef0835a4e, previous block id: b9da753dd2955433ff8dec9cbab8d552a2fdde0fb74fe3b60e4f938486e309a9
difficulty: 59143517061, nonce 3278710783, reward 4.939752263883

height: 1565709, timestamp: 1525493147, difficulty: 58993236539, size: 309454, transactions: 20
major version: 7, minor version: 7
block id: 52074a653142e628843cbfd218afe4438f70b4a4c626db2f7bc998eede7ab23a, previous block id: f55452373002de26f931c250f7288b97de52fc0cdde8ab9fd0083a4ef0835a4e
difficulty: 58993236539, nonce 332472, reward 4.895301945330

height: 1565710, timestamp: 1525493167, difficulty: 58882612311, size: 304060, transactions: 23
major version: 7, minor version: 7
block id: bb3dd2d148285eb62276db71c8db3d38058d1f45efb163ffc54770bd1c408260, previous block id: 52074a653142e628843cbfd218afe4438f70b4a4c626db2f7bc998eede7ab23a
difficulty: 58882612311, nonce 1621111211, reward 4.893090185842

height: 1565711, timestamp: 1525495299, difficulty: 58853675871, size: 313688, transactions: 18
major version: 7, minor version: 7
block id: dd70bdbf313f242c0251b327ca1d1e6450dae3dbb666f90a0212b70f87659146, previous block id: bb3dd2d148285eb62276db71c8db3d38058d1f45efb163ffc54770bd1c408260
difficulty: 58853675871, nonce 3993779565, reward 4.897175339930

height: 1565712, timestamp: 1525505106, difficulty: 58843584304, size: 307531, transactions: 21
major version: 7, minor version: 7
block id: 3e52d4418bd8b947bdf1b0019291d30393caa4b69ddf9a563c9054e844b4a0e6, previous block id: dd70bdbf313f242c0251b327ca1d1e6450dae3dbb666f90a0212b70f87659146
difficulty: 58843584304, nonce 3817, reward 4.942555427552

height: 1565713, timestamp: 1525508979, difficulty: 58974132822, size: 307593, transactions: 19
major version: 7, minor version: 7
block id: dfe1177bc646bff69d1ec0305f50f32e60986925ee393f93c3ce74f32579172e, previous block id: 3e52d4418bd8b947bdf1b0019291d30393caa4b69ddf9a563c9054e844b4a0e6
difficulty: 58974132822, nonce 4229803, reward 4.896172189551

height: 1565714, timestamp: 1525509004, difficulty: 58819783649, size: 304061, transactions: 23
major version: 7, minor version: 7
block id: 1ce9c7f554d0c9f4c709bb3c733803db6b9865a0b9237c2e60654751758de5c3, previous block id: dfe1177bc646bff69d1ec0305f50f32e60986925ee393f93c3ce74f32579172e
difficulty: 58819783649, nonce 6353794, reward 4.893027649150

height: 1565715, timestamp: 1525524046, difficulty: 59399134840, size: 316868, transactions: 24
major version: 7, minor version: 7
block id: fd69fe969b72991e2d971982c3ed28884a06cae081705f453f401814d9e00e4f, previous block id: 1ce9c7f554d0c9f4c709bb3c733803db6b9865a0b9237c2e60654751758de5c3
difficulty: 59399134840, nonce 739928, reward 5.135728015834
```

(in case you're wondering: no, ``print_block b92100b8a012f81b51fdd3cdaa274d0f70f9aba9c12912316ea10dfa39f5e2f4`` still fails)

By even by that point, it's already diverged from the authentic blockchain; those hashes are all wrong.

Height 1565690 is where they diverge.  Good blockchain:

```
height: 1565690, timestamp: 1525470081, difficulty: 58653367587, size: 151536, transactions: 10
major version: 7, minor version: 7
block id: 9fbcd6c0aee81b18f72bb05d98ea43983e60c967fd26214ab60a713121f400a4, previous block id: 4d964df126f5ca131356c105f529fe0c4b60521c4cfbeb64dec0a3d6c83fe239
difficulty: 58653367587, nonce 2432720206, reward 4.713224682521
```

my stuck node:

```
height: 1565690, timestamp: 1525470502, difficulty: 58653367587, size: 304637, transactions: 17
major version: 7, minor version: 7
block id: 41c65e7cc3f3497b163e51f8c7582b4d013ea9bf5b6010df2b9d505a50207102, previous block id: 4d964df126f5ca131356c105f529fe0c4b60521c4cfbeb64dec0a3d6c83fe239
difficulty: 58653367587, nonce 589661, reward 4.828513088528
```

## gituser | 2018-05-05T13:15:42+00:00
I have the same issue.

Node is stuck at `1565715`. Running `monerod v0.12.0.0-release`

```
./monerod status
Height: 1565715/1566120 (99.9%) on mainnet, not mining, net hash 494.99 MH/s, v7, up to date, 28(out)+0(in) connections, uptime 7d 12h 24m 50s
```

```
./monerod print_cn
Remote Host                   Peer id             Support Flags       Recv/Sent (inactive,sec)      State                    Livetime(sec)       Down (kB/s) Down(now)     Up (kB/s) Up(now)      

OUT 80.241.216.213:18080      f18826006315a89d    1                   48800(29)/128685(29)          state_normal             82                  0           2             1         0            
OUT 94.23.48.141:18080        70131cad0a1d9c6f    1                   26500(70)/758004(29)          state_normal             148                 0           0             5         0            
OUT 31.28.25.99:18080         d3f7819027af0b36    1                   287914(28)/166190(29)         state_normal             149                 1           28            1         0            
OUT 176.9.137.218:18080       259e1304ccab57f4    1                   152893(28)/166190(28)         state_normal             149                 1           2             1         2            
OUT 207.237.29.64:18080       63b3e463f7c0a7df    1                   82483(27)/4965762(27)         state_normal             206                 0           2             23        171          
OUT 211.87.232.191:18080      fe66275cfb9afc52    1                   232033(14)/297085(14)         state_normal             245                 0           0             1         2            
OUT 198.204.226.26:18080      b51c3d466eeab418    1                   154766(28)/297085(29)         state_normal             280                 0           2             1         0            
OUT 200.2.142.2:18080         9e9745fcdc892011    0                   25262(344)/666954(29)         state_normal             348                 0           2             1         0            
OUT 176.155.233.253:18080     0a29d0cf98f32623    1                   406073(16)/492187(16)         state_normal             384                 1           12            1         2            
OUT 69.42.17.238:18080        fca768e3a1c3e06a    1                   395983(28)/492187(29)         state_normal             385                 1           2             1         0            
OUT 88.220.144.210:18080      b7e8a184a09bde52    1                   154669(13)/8995258(13)        state_normal             634                 0           0             13        34           
OUT 138.68.74.193:18080       92305706a61c2505    1                   715504(11)/862319(11)         state_normal             681                 1           0             1         2            
OUT 83.243.66.120:18080       ab689ba3faec8389    1                   2080420(1)/13133045(1)        state_normal             728                 2           0             17        34           
OUT 183.162.127.232:18080     63eacd5d2aa5f337    1                   242833(22)/11116460(27)       state_normal             859                 0           2             12        58           
OUT 73.207.217.103:18080      16d3b15275a88b79    1                   1019883(0)/82244585(0)        state_normal             1611                0           1             49        58           
OUT 72.68.227.248:18080       62efb34bac2d96f6    1                   609037(6)/22393595(10)        state_normal             2467                0           2             8         37           
OUT 91.121.192.112:18080      009796a3e8d1c2e2    1                   612990(57)/162928749(29)      state_normal             2860                0           0             55        0            
OUT 200.73.210.161:18080      1859904c4c84ad1f    1                   734093(19)/181770178(19)      state_normal             2937                0           1             60        41           
OUT 69.144.154.51:18080       d5e5ed0310de12f9    1                   879747(15)/296790337(15)      state_normal             3736                0           2             77        316          
OUT 195.14.201.75:18080       4d47b691c60c0778    1                   83300(29)/524200(29)          state_normal             370                 0           2             1         3            
OUT 77.199.192.154:18080      bb97f68e5aebcb8a    1                   1307521(2)/51111287(2)        state_normal             5539                0           0             9         2            
OUT 84.178.118.191:18080      8ad30d74bdbbcc92    1                   6630272(28)/13085147(29)      state_normal             6044                1           3             2         0            
OUT 73.115.73.65:18080        fbd715066e3e0219    1                   4336603(3)/2213036299(15)     state_normal             18465               0           0             117       391          
OUT 74.109.186.21:18080       b3cee3e91dfa1f3b    1                   7579854(24)/2462246750(24)    state_normal             37597               0           2             63        469          
OUT 151.227.83.7:18080        4b28700e142d48f5    1                   10333776(1)/265361422(1)      state_normal             46002               0           0             5         6    
```

```
$ ./monerod sync_info
Height: 1565715, target: 1566120 (99.9741%)
Downloading at 21 kB/s
22 peers
195.242.93.192:18080      96b8f4cf8fa38a2d  1565792  3 kB/s, 0 blocks / 0 MB queued
105.186.195.58:18080      939c2d97e81ea400  1566120  4 kB/s, 0 blocks / 0 MB queued
94.23.48.141:18080        70131cad0a1d9c6f  1546018  2 kB/s, 0 blocks / 0 MB queued
31.28.25.99:18080         d3f7819027af0b36  1565715  1 kB/s, 0 blocks / 0 MB queued
176.9.137.218:18080       259e1304ccab57f4  1565715  2 kB/s, 0 blocks / 0 MB queued
207.237.29.64:18080       63b3e463f7c0a7df  1565284  2 kB/s, 0 blocks / 0 MB queued
211.87.232.191:18080      fe66275cfb9afc52  1565715  0 kB/s, 0 blocks / 0 MB queued
200.2.142.2:18080         9e9745fcdc892011  75601  2 kB/s, 0 blocks / 0 MB queued
88.220.144.210:18080      b7e8a184a09bde52  448092  0 kB/s, 0 blocks / 0 MB queued
83.243.66.120:18080       ab689ba3faec8389  1555025  0 kB/s, 0 blocks / 0 MB queued
183.162.127.232:18080     63eacd5d2aa5f337  276592  0 kB/s, 0 blocks / 0 MB queued
73.207.217.103:18080      16d3b15275a88b79  530840  0 kB/s, 0 blocks / 0 MB queued
72.68.227.248:18080       62efb34bac2d96f6  895856  2 kB/s, 0 blocks / 0 MB queued
91.121.192.112:18080      009796a3e8d1c2e2  1546020  0 kB/s, 0 blocks / 0 MB queued
200.73.210.161:18080      1859904c4c84ad1f  1560110  0 kB/s, 0 blocks / 0 MB queued
69.144.154.51:18080       d5e5ed0310de12f9  1513872  0 kB/s, 0 blocks / 0 MB queued
195.14.201.75:18080       4d47b691c60c0778  1565609  0 kB/s, 0 blocks / 0 MB queued
77.199.192.154:18080      bb97f68e5aebcb8a  1551036  0 kB/s, 0 blocks / 0 MB queued
84.178.118.191:18080      8ad30d74bdbbcc92  1566005  3 kB/s, 5 blocks / 0.635414 MB queued
73.115.73.65:18080        fbd715066e3e0219  1468368  0 kB/s, 0 blocks / 0 MB queued
74.109.186.21:18080       b3cee3e91dfa1f3b  1426148  0 kB/s, 0 blocks / 0 MB queued
151.227.83.7:18080        4b28700e142d48f5  174924  0 kB/s, 0 blocks / 0 MB queued
388 spans, 77.3572 MB
                          5 (1546005 - 1546009, 291 kB)  936 kB/s (0.01)
                          5 (1546010 - 1546014, 53 kB)  500 kB/s (0.01)
                          5 (1546015 - 1546019, 134 kB)  18 kB/s (0.01)
                          5 (1546020 - 1546024, 112 kB)  10 kB/s (0.01)
                          5 (1546025 - 1546029, 41 kB)  4 kB/s (0.01)
                          5 (1546030 - 1546034, 40 kB)  8 kB/s (0.01)
                          5 (1546035 - 1546039, 135 kB)  54 kB/s (0.01)
                          5 (1546040 - 1546044, 91 kB)  19 kB/s (0.01)
                          5 (1546045 - 1546049, 142 kB)  16 kB/s (0.01)
                          5 (1546050 - 1546054, 53 kB)  8 kB/s (0.01)
                          5 (1546055 - 1546059, 47 kB)  8 kB/s (0.01)
                          5 (1546060 - 1546064, 42 kB)  8 kB/s (0.01)
                          5 (1546065 - 1546069, 108 kB)  11 kB/s (0.01)
                          5 (1546070 - 1546074, 53 kB)  8 kB/s (0.01)
                          5 (1546075 - 1546079, 40 kB)  111 kB/s (0.01)
                          5 (1546080 - 1546084, 14 kB)  143 kB/s (0.01)
                          5 (1546085 - 1546089, 13 kB)  155 kB/s (0.01)
                          5 (1546090 - 1546094, 147 kB)  421 kB/s (0.01)
                          5 (1546095 - 1546099, 202 kB)  374 kB/s (0.01)
                          5 (1546100 - 1546104, 67 kB)  215 kB/s (0.01)
                          5 (1546105 - 1546109, 79 kB)  496 kB/s (0.01)
                          5 (1546110 - 1546114, 158 kB)  117 kB/s (0.01)
                          5 (1546115 - 1546119, 43 kB)  32 kB/s (0.01)
                          5 (1546120 - 1546124, 124 kB)  150 kB/s (0.01)
                          5 (1546125 - 1546129, 133 kB)  412 kB/s (0.01)
                          5 (1546130 - 1546134, 80 kB)  626 kB/s (0.01)
                          5 (1546135 - 1546139, 912 kB)  837 kB/s (0.01)
                          5 (1546140 - 1546144, 281 kB)  212 kB/s (0.01)
                          5 (1546145 - 1546149, 94 kB)  384 kB/s (0.01)
                          5 (1546150 - 1546154, 40 kB)  10 kB/s (0.01)
                          5 (1546155 - 1546159, 568 kB)  674 kB/s (0.01)
                          5 (1546160 - 1546164, 322 kB)  1631 kB/s (0.01)
                          5 (1546165 - 1546169, 54 kB)  175 kB/s (0.01)
                          5 (1546170 - 1546174, 13 kB)  20 kB/s (0.01)
                          5 (1546175 - 1546179, 74 kB)  43 kB/s (0.01)
                          1 (1561819 - 1561819, 182 kB)  257 kB/s (0.01)
                          1 (1562062 - 1562062, 13 kB)  109 kB/s (0)
                          1 (1562521 - 1562521, 268 kB)  299 kB/s (0.01)
                          1 (1563538 - 1563538, 308 kB)  1496 kB/s (0.05)
                          1 (1565132 - 1565132, 313 kB)  9 kB/s (0)
                          1 (1565690 - 1565690, 151 kB)  791 kB/s (0.02)
                          1 (1565691 - 1565691, 13 kB)  309 kB/s (0.01)
                          1 (1565692 - 1565692, 53 kB)  31632 kB/s (0.98)
                          1 (1565693 - 1565693, 277 kB)  97 kB/s (0)
                          1 (1565694 - 1565694, 54 kB)  206 kB/s (0)
                          1 (1565695 - 1565695, 40 kB)  63 kB/s (0)
                          1 (1565696 - 1565696, 0 kB)  1 kB/s (0)
                          1 (1565697 - 1565697, 103 kB)  241 kB/s (0)
                          1 (1565698 - 1565698, 101 kB)  111 kB/s (0)
                          1 (1565699 - 1565699, 108 kB)  507 kB/s (0.01)
                          1 (1565700 - 1565700, 27 kB)  193 kB/s (0.01)
                          1 (1565701 - 1565701, 27 kB)  215 kB/s (0.01)
                          1 (1565702 - 1565702, 79 kB)  1759 kB/s (0.05)
                          2 (1565703 - 1565704, 79 kB)  355 kB/s (0.01)
                          1 (1565705 - 1565705, 79 kB)  916 kB/s (0.03)
                          1 (1565706 - 1565706, 298 kB)  5915 kB/s (0.18)
84.178.118.191:18080      5 (1565707 - 1565711, 635 kB)  3153 kB/s (0.1)
                          1 (1565708 - 1565708, 299 kB)  982 kB/s (0.03)
                          4 (1565709 - 1565712, 335 kB)  294 kB/s (0.01)
                          5 (1565713 - 1565717, 336 kB)  366 kB/s (0.01)
                          1 (1565714 - 1565714, 304 kB)  973 kB/s (0.03)
                          1 (1565715 - 1565715, 317 kB)  244 kB/s (0.01)
                          1 (1565716 - 1565716, 0 kB)  1 kB/s (0)
                          1 (1565717 - 1565717, 112 kB)  1120 kB/s (0.03)
                          2 (1565718 - 1565719, 254 kB)  548 kB/s (0.02)
                          1 (1565720 - 1565720, 13 kB)  45 kB/s (0.02)
                          1 (1565721 - 1565721, 310 kB)  1384 kB/s (0.02)
                          1 (1565722 - 1565722, 301 kB)  812 kB/s (0.02)
                          1 (1565723 - 1565723, 314 kB)  2926 kB/s (0.09)
                          1 (1565724 - 1565724, 304 kB)  288 kB/s (0.01)
                          1 (1565725 - 1565725, 296 kB)  511 kB/s (0.02)
                          1 (1565726 - 1565726, 304 kB)  5867 kB/s (0.18)
                          1 (1565727 - 1565727, 297 kB)  310 kB/s (0.01)
                          1 (1565728 - 1565728, 299 kB)  4011 kB/s (0.12)
                          1 (1565729 - 1565729, 295 kB)  5341 kB/s (0.13)
                          1 (1565730 - 1565730, 306 kB)  2883 kB/s (0.13)
                          1 (1565731 - 1565731, 302 kB)  303 kB/s (0.01)
                          1 (1565732 - 1565732, 303 kB)  435 kB/s (0.01)
                          1 (1565733 - 1565733, 280 kB)  6016 kB/s (0.19)
                          1 (1565734 - 1565734, 287 kB)  2495 kB/s (0.08)
                          2 (1565735 - 1565736, 485 kB)  4070 kB/s (0.13)
                          1 (1565737 - 1565737, 244 kB)  859 kB/s (0.03)
                          1 (1565738 - 1565738, 309 kB)  490 kB/s (0.02)
                          1 (1565739 - 1565739, 242 kB)  2563 kB/s (0.08)
                          1 (1565740 - 1565740, 235 kB)  593 kB/s (0.02)
                          1 (1565741 - 1565741, 261 kB)  112 kB/s (0)
                          1 (1565742 - 1565742, 87 kB)  135 kB/s (0)
                          1 (1565743 - 1565743, 42 kB)  161 kB/s (0.01)
                          2 (1565744 - 1565745, 209 kB)  814 kB/s (0.03)
                          1 (1565746 - 1565746, 284 kB)  1181 kB/s (0.01)
                          1 (1565747 - 1565747, 281 kB)  2444 kB/s (0.01)
                          1 (1565748 - 1565748, 0 kB)  1 kB/s (0.01)
                          1 (1565749 - 1565749, 13 kB)  210 kB/s (0.01)
                          1 (1565750 - 1565750, 0 kB)  1 kB/s (0.01)
                          1 (1565751 - 1565751, 192 kB)  4058 kB/s (0.13)
                          3 (1565752 - 1565754, 835 kB)  368 kB/s (0.01)
                          1 (1565755 - 1565755, 198 kB)  236 kB/s (0)
                          1 (1565756 - 1565756, 141 kB)  70 kB/s (0)
                          1 (1565757 - 1565757, 13 kB)  37 kB/s (0)
                          1 (1565758 - 1565758, 217 kB)  114 kB/s (0)
                          1 (1565759 - 1565759, 41 kB)  517 kB/s (0.02)
                          1 (1565760 - 1565760, 68 kB)  856 kB/s (0.02)
                          1 (1565761 - 1565761, 0 kB)  1 kB/s (0)
                          1 (1565762 - 1565762, 302 kB)  397 kB/s (0.01)
                          1 (1565763 - 1565763, 106 kB)  924 kB/s (0.03)
                          1 (1565764 - 1565764, 295 kB)  181 kB/s (0.03)
                          1 (1565765 - 1565765, 214 kB)  1605 kB/s (0.03)
                          1 (1565766 - 1565766, 289 kB)  364 kB/s (0.01)
                          2 (1565767 - 1565768, 417 kB)  6 kB/s (0)
                          1 (1565769 - 1565769, 295 kB)  763 kB/s (0.02)
                          1 (1565770 - 1565770, 188 kB)  491 kB/s (0.02)
                          3 (1565771 - 1565773, 490 kB)  208 kB/s (0)
                          1 (1565774 - 1565774, 67 kB)  83 kB/s (0)
                          1 (1565775 - 1565775, 16 kB)  8 kB/s (0)
                          1 (1565776 - 1565776, 13 kB)  184 kB/s (0.03)
                          1 (1565777 - 1565777, 205 kB)  2009 kB/s (0.03)
                          5 (1565778 - 1565782, 422 kB)  3259 kB/s (0.11)
                          4 (1565783 - 1565786, 396 kB)  4170 kB/s (0.11)
                          1 (1565787 - 1565787, 0 kB)  0 kB/s (0.01)
                          1 (1565788 - 1565788, 300 kB)  629 kB/s (0.01)
                          1 (1565789 - 1565789, 271 kB)  460 kB/s (0.01)
                          1 (1565790 - 1565790, 0 kB)  0 kB/s (0)
                          1 (1565791 - 1565791, 93 kB)  185 kB/s (0.01)
                          2 (1565792 - 1565793, 298 kB)  79 kB/s (0)
                          1 (1565794 - 1565794, 27 kB)  38 kB/s (0)
                          1 (1565795 - 1565795, 91 kB)  57 kB/s (0)
                          1 (1565796 - 1565796, 26 kB)  333 kB/s (0.01)
                          1 (1565797 - 1565797, 13 kB)  134 kB/s (0)
                          2 (1565798 - 1565799, 336 kB)  1170 kB/s (0.02)
                          1 (1565800 - 1565800, 43 kB)  344 kB/s (0.02)
                          2 (1565801 - 1565802, 301 kB)  2717 kB/s (0.05)
                          1 (1565803 - 1565803, 47 kB)  565 kB/s (0.05)
                          1 (1565804 - 1565804, 13 kB)  312 kB/s (0.04)
                          1 (1565805 - 1565805, 107 kB)  2358 kB/s (0.04)
                          1 (1565806 - 1565806, 240 kB)  228 kB/s (0.01)
                          1 (1565807 - 1565807, 0 kB)  0 kB/s (0)
                          1 (1565808 - 1565808, 42 kB)  38 kB/s (0)
                          1 (1565809 - 1565809, 67 kB)  268 kB/s (0.01)
                          1 (1565810 - 1565810, 153 kB)  220 kB/s (0.01)
                          1 (1565811 - 1565811, 27 kB)  77 kB/s (0)
                          2 (1565812 - 1565813, 655 kB)  4790 kB/s (0.15)
                          1 (1565814 - 1565814, 306 kB)  3335 kB/s (0.1)
                          1 (1565815 - 1565815, 306 kB)  3748 kB/s (0.14)
                          1 (1565816 - 1565816, 309 kB)  5481 kB/s (0.14)
                          2 (1565817 - 1565818, 630 kB)  871 kB/s (0.03)
                          5 (1565819 - 1565823, 1560 kB)  607 kB/s (0.01)
                          2 (1565824 - 1565825, 577 kB)  484 kB/s (0.01)
                          1 (1565826 - 1565826, 302 kB)  231 kB/s (0.01)
                          1 (1565827 - 1565827, 341 kB)  3788 kB/s (0.12)
                          1 (1565828 - 1565828, 274 kB)  3056 kB/s (0.09)
                          1 (1565829 - 1565829, 300 kB)  218 kB/s (0.01)
                          2 (1565830 - 1565831, 614 kB)  1843 kB/s (0.06)
                          1 (1565832 - 1565832, 334 kB)  3692 kB/s (0.11)
                          1 (1565833 - 1565833, 294 kB)  5416 kB/s (0.17)
                          1 (1565834 - 1565834, 301 kB)  320 kB/s (0.01)
                          1 (1565835 - 1565835, 297 kB)  2516 kB/s (0.08)
                          1 (1565836 - 1565836, 299 kB)  3492 kB/s (0.14)
                          1 (1565837 - 1565837, 299 kB)  5379 kB/s (0.14)
                          1 (1565838 - 1565838, 304 kB)  239 kB/s (0.01)
                          1 (1565839 - 1565839, 296 kB)  282 kB/s (0.01)
                          1 (1565840 - 1565840, 307 kB)  337 kB/s (0.01)
                          1 (1565841 - 1565841, 267 kB)  160 kB/s (0.01)
                          1 (1565842 - 1565842, 293 kB)  402 kB/s (0.01)
                          1 (1565843 - 1565843, 202 kB)  2167 kB/s (0.07)
                          1 (1565844 - 1565844, 248 kB)  2418 kB/s (0.07)
                          1 (1565845 - 1565845, 205 kB)  2030 kB/s (0.07)
                          3 (1565846 - 1565848, 784 kB)  149 kB/s (0)
                          1 (1565849 - 1565849, 41 kB)  492 kB/s (0.02)
                          1 (1565850 - 1565850, 296 kB)  2414 kB/s (0.04)
                          1 (1565851 - 1565851, 26 kB)  314 kB/s (0.04)
                          1 (1565852 - 1565852, 0 kB)  0 kB/s (0)
                          1 (1565853 - 1565853, 69 kB)  786 kB/s (0.03)
                          1 (1565854 - 1565854, 141 kB)  1275 kB/s (0.03)
                          1 (1565855 - 1565855, 13 kB)  46 kB/s (0)
                          1 (1565856 - 1565856, 40 kB)  126 kB/s (0)
                          1 (1565857 - 1565857, 13 kB)  45 kB/s (0)
                          1 (1565858 - 1565858, 0 kB)  1 kB/s (0)
                          1 (1565859 - 1565859, 54 kB)  97 kB/s (0)
                          3 (1565860 - 1565862, 629 kB)  2635 kB/s (0.08)
                          1 (1565863 - 1565863, 307 kB)  355 kB/s (0.01)
                          1 (1565864 - 1565864, 304 kB)  602 kB/s (0.02)
                          2 (1565865 - 1565866, 608 kB)  931 kB/s (0.02)
                          1 (1565867 - 1565867, 304 kB)  891 kB/s (0.03)
                          1 (1565868 - 1565868, 304 kB)  1303 kB/s (0.04)
                          1 (1565869 - 1565869, 308 kB)  85 kB/s (0)
                          1 (1565870 - 1565870, 304 kB)  2503 kB/s (0.08)
                          5 (1565871 - 1565875, 1533 kB)  7488 kB/s (0.12)
                          1 (1565876 - 1565876, 304 kB)  2557 kB/s (0.12)
                          1 (1565877 - 1565877, 304 kB)  2550 kB/s (0.12)
                          1 (1565878 - 1565878, 306 kB)  277 kB/s (0.01)
                          1 (1565879 - 1565879, 300 kB)  249 kB/s (0.01)
                          1 (1565880 - 1565880, 302 kB)  1069 kB/s (0.03)
                          1 (1565881 - 1565881, 0 kB)  1 kB/s (0)
                          1 (1565882 - 1565882, 309 kB)  532 kB/s (0.02)
                          1 (1565883 - 1565883, 178 kB)  354 kB/s (0.01)
                          3 (1565884 - 1565886, 329 kB)  236 kB/s (0.01)
                          1 (1565887 - 1565887, 0 kB)  0 kB/s (0)
                          1 (1565888 - 1565888, 217 kB)  165 kB/s (0.01)
                          1 (1565889 - 1565889, 305 kB)  249 kB/s (0.01)
                          1 (1565890 - 1565890, 298 kB)  893 kB/s (0.05)
                          1 (1565891 - 1565891, 302 kB)  2506 kB/s (0.05)
                          1 (1565892 - 1565892, 281 kB)  202 kB/s (0.01)
                          1 (1565893 - 1565893, 199 kB)  3012 kB/s (0.1)
                          1 (1565894 - 1565894, 258 kB)  3700 kB/s (0.1)
                          1 (1565895 - 1565895, 146 kB)  131 kB/s (0)
                          1 (1565896 - 1565896, 28 kB)  239 kB/s (0.01)
                          1 (1565897 - 1565897, 306 kB)  2494 kB/s (0.08)
                          1 (1565898 - 1565898, 66 kB)  348 kB/s (0.01)
                          2 (1565899 - 1565900, 436 kB)  3670 kB/s (0.11)
                          1 (1565901 - 1565901, 27 kB)  197 kB/s (0.01)
                          2 (1565902 - 1565903, 607 kB)  1165 kB/s (0.04)
                          1 (1565904 - 1565904, 264 kB)  1970 kB/s (0.06)
                          1 (1565905 - 1565905, 188 kB)  795 kB/s (0.02)
                          1 (1565906 - 1565906, 54 kB)  632 kB/s (0.02)
                          1 (1565907 - 1565907, 81 kB)  1849 kB/s (0.06)
                          1 (1565908 - 1565908, 69 kB)  1564 kB/s (0.02)
                          1 (1565909 - 1565909, 0 kB)  1 kB/s (0.02)
                          1 (1565910 - 1565910, 0 kB)  2 kB/s (0)
                          2 (1565911 - 1565912, 81 kB)  2022 kB/s (0.06)
                          1 (1565913 - 1565913, 13 kB)  19 kB/s (0)
                          2 (1565914 - 1565915, 482 kB)  4079 kB/s (0.13)
                          1 (1565916 - 1565916, 0 kB)  0 kB/s (0)
                          1 (1565917 - 1565917, 297 kB)  6235 kB/s (0.15)
                          1 (1565918 - 1565918, 170 kB)  3654 kB/s (0.15)
                          3 (1565919 - 1565921, 61 kB)  172 kB/s (0.01)
                          1 (1565922 - 1565922, 27 kB)  45 kB/s (0)
                          1 (1565923 - 1565923, 122 kB)  1408 kB/s (0.04)
                          1 (1565924 - 1565924, 40 kB)  947 kB/s (0.03)
                          1 (1565925 - 1565925, 26 kB)  283 kB/s (0.01)
                          1 (1565926 - 1565926, 54 kB)  655 kB/s (0.02)
                          1 (1565927 - 1565927, 76 kB)  45 kB/s (0)
                          1 (1565928 - 1565928, 41 kB)  99 kB/s (0)
                          1 (1565929 - 1565929, 222 kB)  4419 kB/s (0.14)
                          1 (1565930 - 1565930, 249 kB)  5554 kB/s (0.17)
                          1 (1565931 - 1565931, 27 kB)  270 kB/s (0.01)
                          1 (1565932 - 1565932, 314 kB)  981 kB/s (0.03)
                          2 (1565933 - 1565934, 594 kB)  588 kB/s (0.01)
                          1 (1565935 - 1565935, 185 kB)  270 kB/s (0.01)
                          1 (1565936 - 1565936, 0 kB)  1 kB/s (0)
                          1 (1565937 - 1565937, 13 kB)  242 kB/s (0)
                          1 (1565938 - 1565938, 37 kB)  118 kB/s (0)
                          2 (1565939 - 1565940, 228 kB)  1852 kB/s (0.06)
                          1 (1565941 - 1565941, 0 kB)  0 kB/s (0)
                          1 (1565942 - 1565942, 300 kB)  344 kB/s (0.01)
                          1 (1565943 - 1565943, 160 kB)  161 kB/s (0)
                          2 (1565944 - 1565945, 176 kB)  267 kB/s (0.01)
                          1 (1565946 - 1565946, 0 kB)  0 kB/s (0)
                          1 (1565947 - 1565947, 94 kB)  237 kB/s (0.01)
                          1 (1565948 - 1565948, 43 kB)  123 kB/s (0)
                          1 (1565949 - 1565949, 0 kB)  1 kB/s (0)
                          1 (1565950 - 1565950, 162 kB)  2600 kB/s (0.08)
                          2 (1565951 - 1565952, 173 kB)  1296 kB/s (0.04)
                          1 (1565953 - 1565953, 53 kB)  853 kB/s (0.03)
                          1 (1565954 - 1565954, 300 kB)  3503 kB/s (0.11)
                          1 (1565955 - 1565955, 174 kB)  2868 kB/s (0.09)
                          2 (1565956 - 1565957, 237 kB)  308 kB/s (0.01)
                          1 (1565958 - 1565958, 304 kB)  4339 kB/s (0.13)
                          1 (1565959 - 1565959, 231 kB)  4943 kB/s (0.15)
                          2 (1565960 - 1565961, 528 kB)  9141 kB/s (0.28)
                          3 (1565962 - 1565964, 731 kB)  240 kB/s (0.01)
                          1 (1565965 - 1565965, 0 kB)  0 kB/s (0)
                          1 (1565966 - 1565966, 170 kB)  2462 kB/s (0.04)
                          1 (1565967 - 1565967, 13 kB)  155 kB/s (0.04)
                          1 (1565968 - 1565968, 40 kB)  51 kB/s (0)
                          1 (1565969 - 1565969, 305 kB)  2601 kB/s (0.08)
                          1 (1565970 - 1565970, 312 kB)  32337 kB/s (1)
                          1 (1565971 - 1565971, 305 kB)  518 kB/s (0.01)
                          1 (1565972 - 1565972, 304 kB)  30 kB/s (0.01)
                          1 (1565973 - 1565973, 303 kB)  24 kB/s (0)
                          1 (1565974 - 1565974, 301 kB)  1527 kB/s (0.05)
                          1 (1565975 - 1565975, 241 kB)  1633 kB/s (0.05)
                          1 (1565976 - 1565976, 133 kB)  692 kB/s (0.02)
                          1 (1565977 - 1565977, 299 kB)  2745 kB/s (0.08)
                          1 (1565978 - 1565978, 13 kB)  14 kB/s (0)
                          1 (1565979 - 1565979, 115 kB)  175 kB/s (0.01)
                          1 (1565980 - 1565980, 27 kB)  329 kB/s (0.01)
                          2 (1565981 - 1565982, 41 kB)  28 kB/s (0)
                          1 (1565983 - 1565983, 40 kB)  119 kB/s (0)
                          1 (1565984 - 1565984, 28 kB)  660 kB/s (0.02)
                          1 (1565985 - 1565985, 39 kB)  79 kB/s (0)
                          1 (1565986 - 1565986, 308 kB)  114 kB/s (0)
                          1 (1565987 - 1565987, 306 kB)  2182 kB/s (0.07)
                          1 (1565988 - 1565988, 148 kB)  670 kB/s (0.02)
                          1 (1565989 - 1565989, 166 kB)  745 kB/s (0.02)
                          1 (1565990 - 1565990, 27 kB)  38 kB/s (0)
                          1 (1565991 - 1565991, 26 kB)  38 kB/s (0)
                          1 (1565992 - 1565992, 27 kB)  69 kB/s (0)
                          1 (1565993 - 1565993, 100 kB)  1465 kB/s (0.05)
                          1 (1565994 - 1565994, 41 kB)  232 kB/s (0.01)
                          2 (1565995 - 1565996, 309 kB)  450 kB/s (0.01)
                          2 (1565997 - 1565998, 123 kB)  296 kB/s (0.01)
                          5 (1565999 - 1566003, 229 kB)  94 kB/s (0)
                          1 (1566004 - 1566004, 27 kB)  64 kB/s (0)
                          1 (1566005 - 1566005, 13 kB)  262 kB/s (0.01)
                          1 (1566006 - 1566006, 67 kB)  785 kB/s (0.02)
                          1 (1566007 - 1566007, 304 kB)  2928 kB/s (0.09)
                          1 (1566008 - 1566008, 299 kB)  332 kB/s (0.01)
                          1 (1566009 - 1566009, 121 kB)  117 kB/s (0)
                          2 (1566010 - 1566011, 71 kB)  311 kB/s (0.01)
                          1 (1566012 - 1566012, 111 kB)  1350 kB/s (0.04)
                          1 (1566013 - 1566013, 28 kB)  351 kB/s (0.01)
                          1 (1566014 - 1566014, 317 kB)  1594 kB/s (0.05)
                          1 (1566015 - 1566015, 318 kB)  1725 kB/s (0.05)
                          1 (1566016 - 1566016, 303 kB)  1746 kB/s (0.05)
                          1 (1566017 - 1566017, 310 kB)  187 kB/s (0.01)
                          1 (1566018 - 1566018, 306 kB)  831 kB/s (0.03)
                          1 (1566019 - 1566019, 317 kB)  512 kB/s (0.02)
                          1 (1566020 - 1566020, 300 kB)  969 kB/s (0.03)
                          1 (1566021 - 1566021, 304 kB)  892 kB/s (0.03)
                          2 (1566022 - 1566023, 617 kB)  4146 kB/s (0.13)
                          1 (1566024 - 1566024, 302 kB)  869 kB/s (0.03)
                          1 (1566025 - 1566025, 297 kB)  2394 kB/s (0.07)
                          1 (1566026 - 1566026, 81 kB)  201 kB/s (0.01)
                          1 (1566027 - 1566027, 40 kB)  695 kB/s (0.02)
                          1 (1566028 - 1566028, 304 kB)  549 kB/s (0.02)
                          2 (1566029 - 1566030, 327 kB)  323 kB/s (0.01)
                          1 (1566031 - 1566031, 0 kB)  0 kB/s (0)
                          1 (1566032 - 1566032, 108 kB)  31 kB/s (0)
                          3 (1566033 - 1566035, 664 kB)  850 kB/s (0.03)
                          1 (1566036 - 1566036, 295 kB)  6834 kB/s (0.21)
                          1 (1566037 - 1566037, 298 kB)  6758 kB/s (0.21)
                          2 (1566038 - 1566039, 596 kB)  4848 kB/s (0.15)
                          1 (1566040 - 1566040, 266 kB)  393 kB/s (0.01)
                          1 (1566041 - 1566041, 318 kB)  256 kB/s (0.01)
                          1 (1566042 - 1566042, 295 kB)  581 kB/s (0.02)
                          1 (1566043 - 1566043, 164 kB)  632 kB/s (0.02)
                          1 (1566044 - 1566044, 301 kB)  513 kB/s (0.02)
                          1 (1566045 - 1566045, 42 kB)  320 kB/s (0.01)
                          1 (1566046 - 1566046, 136 kB)  705 kB/s (0.02)
                          1 (1566047 - 1566047, 231 kB)  7 kB/s (0)
                          1 (1566048 - 1566048, 125 kB)  662 kB/s (0.02)
                          1 (1566049 - 1566049, 0 kB)  0 kB/s (0)
                          1 (1566050 - 1566050, 65 kB)  728 kB/s (0.02)
                          1 (1566051 - 1566051, 109 kB)  1222 kB/s (0.04)
                          1 (1566052 - 1566052, 305 kB)  2494 kB/s (0.08)
                          1 (1566053 - 1566053, 80 kB)  876 kB/s (0.03)
                          1 (1566054 - 1566054, 39 kB)  8 kB/s (0)
                          1 (1566055 - 1566055, 150 kB)  237 kB/s (0.01)
                          1 (1566056 - 1566056, 116 kB)  105 kB/s (0)
                          2 (1566057 - 1566058, 133 kB)  107 kB/s (0)
                          1 (1566059 - 1566059, 53 kB)  140 kB/s (0)
                          1 (1566060 - 1566060, 40 kB)  100 kB/s (0)
                          2 (1566061 - 1566062, 232 kB)  293 kB/s (0.01)
                          1 (1566063 - 1566063, 68 kB)  73 kB/s (0)
                          1 (1566064 - 1566064, 0 kB)  0 kB/s (0)
                          1 (1566065 - 1566065, 67 kB)  113 kB/s (0)
                          1 (1566066 - 1566066, 54 kB)  664 kB/s (0.02)
                          1 (1566067 - 1566067, 299 kB)  763 kB/s (0.02)
                          1 (1566068 - 1566068, 196 kB)  2461 kB/s (0.08)
                          1 (1566069 - 1566069, 39 kB)  505 kB/s (0.02)
                          2 (1566070 - 1566071, 319 kB)  1098 kB/s (0.03)
                          1 (1566072 - 1566072, 14 kB)  169 kB/s (0.01)
                          1 (1566073 - 1566073, 187 kB)  660 kB/s (0.02)
                          1 (1566074 - 1566074, 50 kB)  312 kB/s (0.01)
                          1 (1566075 - 1566075, 35 kB)  33 kB/s (0)
                          1 (1566076 - 1566076, 255 kB)  304 kB/s (0.01)
                          1 (1566077 - 1566077, 27 kB)  277 kB/s (0.01)
                          1 (1566078 - 1566078, 316 kB)  304 kB/s (0.01)
                          1 (1566079 - 1566079, 80 kB)  104 kB/s (0)
                          1 (1566080 - 1566080, 54 kB)  80 kB/s (0)
                          1 (1566081 - 1566081, 0 kB)  1 kB/s (0)
                          1 (1566082 - 1566082, 80 kB)  1624 kB/s (0.05)
                          2 (1566083 - 1566084, 332 kB)  1586 kB/s (0.05)
                          1 (1566085 - 1566085, 297 kB)  552 kB/s (0.02)
                          1 (1566086 - 1566086, 310 kB)  1684 kB/s (0.05)
                          1 (1566087 - 1566087, 0 kB)  1 kB/s (0)
                          1 (1566088 - 1566088, 94 kB)  1021 kB/s (0.03)
                          1 (1566089 - 1566089, 219 kB)  2024 kB/s (0.06)
                          1 (1566090 - 1566090, 80 kB)  284 kB/s (0.01)
                          4 (1566091 - 1566094, 270 kB)  219 kB/s (0.01)
                          1 (1566095 - 1566095, 67 kB)  178 kB/s (0.01)
                          1 (1566096 - 1566096, 201 kB)  4058 kB/s (0.13)
                          3 (1566097 - 1566099, 162 kB)  284 kB/s (0.01)
                          1 (1566100 - 1566100, 152 kB)  43 kB/s (0)
                          1 (1566101 - 1566101, 233 kB)  45 kB/s (0)
                          1 (1566102 - 1566102, 299 kB)  195 kB/s (0)
                          1 (1566103 - 1566103, 294 kB)  425 kB/s (0.01)
                          1 (1566104 - 1566104, 306 kB)  239 kB/s (0.01)
                          1 (1566105 - 1566105, 209 kB)  2238 kB/s (0.07)
                          1 (1566106 - 1566106, 277 kB)  2462 kB/s (0.08)
                          1 (1566107 - 1566107, 278 kB)  816 kB/s (0.03)
                          1 (1566108 - 1566108, 217 kB)  565 kB/s (0.02)
                          1 (1566109 - 1566109, 41 kB)  130 kB/s (0)
                          5 (1566110 - 1566114, 533 kB)  4139 kB/s (0.07)
                          1 (1566115 - 1566115, 16 kB)  196 kB/s (0.07)
                          2 (1566116 - 1566117, 163 kB)  324 kB/s (0.01)
                          1 (1566118 - 1566118, 0 kB)  0 kB/s (0)
                          1 (1566119 - 1566119, 20 kB)  69 kB/s (0)
```

```
./monerod print_bc 1565708 1565714
height: 1565708, timestamp: 1525492133, difficulty: 59143517061, size: 313532, transactions: 22
major version: 7, minor version: 7
block id: f55452373002de26f931c250f7288b97de52fc0cdde8ab9fd0083a4ef0835a4e, previous block id: b9da753dd2955433ff8dec9cbab8d552a2fdde0fb74fe3b60e4f938486e309a9
difficulty: 59143517061, nonce 3278710783, reward 4.939752263883

height: 1565709, timestamp: 1525493147, difficulty: 58993236539, size: 309454, transactions: 20
major version: 7, minor version: 7
block id: 52074a653142e628843cbfd218afe4438f70b4a4c626db2f7bc998eede7ab23a, previous block id: f55452373002de26f931c250f7288b97de52fc0cdde8ab9fd0083a4ef0835a4e
difficulty: 58993236539, nonce 332472, reward 4.895301945330

height: 1565710, timestamp: 1525493167, difficulty: 58882612311, size: 304060, transactions: 23
major version: 7, minor version: 7
block id: bb3dd2d148285eb62276db71c8db3d38058d1f45efb163ffc54770bd1c408260, previous block id: 52074a653142e628843cbfd218afe4438f70b4a4c626db2f7bc998eede7ab23a
difficulty: 58882612311, nonce 1621111211, reward 4.893090185842

height: 1565711, timestamp: 1525495299, difficulty: 58853675871, size: 313688, transactions: 18
major version: 7, minor version: 7
block id: dd70bdbf313f242c0251b327ca1d1e6450dae3dbb666f90a0212b70f87659146, previous block id: bb3dd2d148285eb62276db71c8db3d38058d1f45efb163ffc54770bd1c408260
difficulty: 58853675871, nonce 3993779565, reward 4.897175339930

height: 1565712, timestamp: 1525505106, difficulty: 58843584304, size: 307531, transactions: 21
major version: 7, minor version: 7
block id: 3e52d4418bd8b947bdf1b0019291d30393caa4b69ddf9a563c9054e844b4a0e6, previous block id: dd70bdbf313f242c0251b327ca1d1e6450dae3dbb666f90a0212b70f87659146
difficulty: 58843584304, nonce 3817, reward 4.942555427552

height: 1565713, timestamp: 1525508979, difficulty: 58974132822, size: 307593, transactions: 19
major version: 7, minor version: 7
block id: dfe1177bc646bff69d1ec0305f50f32e60986925ee393f93c3ce74f32579172e, previous block id: 3e52d4418bd8b947bdf1b0019291d30393caa4b69ddf9a563c9054e844b4a0e6
difficulty: 58974132822, nonce 4229803, reward 4.896172189551

height: 1565714, timestamp: 1525509004, difficulty: 58819783649, size: 304061, transactions: 23
major version: 7, minor version: 7
block id: 1ce9c7f554d0c9f4c709bb3c733803db6b9865a0b9237c2e60654751758de5c3, previous block id: dfe1177bc646bff69d1ec0305f50f32e60986925ee393f93c3ce74f32579172e
difficulty: 58819783649, nonce 6353794, reward 4.893027649150
```
```
./monerod print_bc 1565708 1565715
2018-05-05 13:16:45.842	    7f4a9b4c9740	ERROR	net.http	contrib/epee/include/storages/http_abstract_invoke.h:118	RPC call of "getblockheadersrange" returned error: -2, message: Invalid start/end heights.
Error: Unsuccessful -- json_rpc_request:
```

Does building from branch `release-0.12` fixes the issue?

## gituser | 2018-05-05T13:27:59+00:00
Yes, same issue as @gorthorb, `1565713` got wrong txhash - `dfe1177bc646bff69d1ec0305f50f32e60986925ee393f93c3ce74f32579172e` 

```
$ ./monerod print_block 1565713
timestamp: 1525508979
previous hash: 3e52d4418bd8b947bdf1b0019291d30393caa4b69ddf9a563c9054e844b4a0e6
nonce: 4229803
is orphan: 0
height: 1565713
depth: 1
hash: dfe1177bc646bff69d1ec0305f50f32e60986925ee393f93c3ce74f32579172e
difficulty: 58974132822
reward: 4896172189551
{
  "major_version": 7, 
  "minor_version": 7, 
  "timestamp": 1525508979, 
  "prev_id": "3e52d4418bd8b947bdf1b0019291d30393caa4b69ddf9a563c9054e844b4a0e6", 
  "nonce": 4229803, 
  "miner_tx": {
    "version": 2, 
    "unlock_time": 1565773, 
    "vin": [ {
        "gen": {
          "height": 1565713
        }
      }
    ], 
    "vout": [ {
        "amount": 4896172189551, 
        "target": {
          "key": "31624a4ec5c7f029946a766567abd4d2dbcef0531f287c5951e5b32c7a45e649"
        }
      }
    ], 
    "extra": [ 1, 8, 190, 255, 164, 234, 61, 124, 226, 143, 10, 29, 237, 160, 159, 215, 39, 170, 225, 111, 229, 105, 83, 138, 221, 161, 135, 51, 165, 179, 154, 31, 53, 2, 8, 156, 2, 0, 23, 74, 0, 0, 0
    ], 
    "rct_signatures": {
      "type": 0
    }
  }, 
  "tx_hashes": [ "3bf9e40dfc9eca57c75fd3d0a1fc9dbc8bae25fbaffd36abdb79b7366ac18734", "ecd773fe1e6f242392ed6519e57341eec172586cff38991e57bc618723c730f1", "04746ba9817214be7577235993e3d1626a8ddff85f4407137df894c700ae3abb", "16b05888794a6df63c6e68d4d9abf15320f93411bc87780668d93e8088d4b745", "6658b51774f62620d70bc294584c3b1b54ace121d005805e7dd5dc9a4448e982", "62edd26f0194754aa4d776893328ca9d91d4635e903223d833e61d7e941ca64a", "16e75225d9c008c04030544f5ef009f1039f0101d92279f98be77a16e58ec09a", "b9013088d743510996fe690a0e7eaa65bffe66f5f24ef18af4edd940902e5191", "3581e3da15b248041d3b6a309582b4d5dd67fd987158a298ef21bc7f2785ec97", "ecc49bbffd8a8ddf047a8f0593c87c7963acd9245d5b63a1edfffb44e33ed967", "1345eee310ce2ca6a781dcee5ba5a65093dcd94836d08e9fa0ef1f910218d0b6", "be48ec56babf49063be221a204be4a84fc9d35b054fc5a19ff7b29d0b1b0f423", "ef8056c7ad7114b8b67392f866efecfef41a4f744b0589da551b61b7262402b1", "9b247c89e576d7486b6d87c89a2017f9e91a3a344872ad330b7f1c8d6cf9b129", "bc4b3a2e2a74380b7bff364280719cfd49612df76a4a800ec41bd3b8e8ad2296", "90ecb52cbc8ece92d7b3d13ec77b29926897d273ef40721ff5a0891c48c05abc", "5540b1b7b4e4ebfcefc8fb78481d10dc98af74d812fca5dc00639aced624f9fd", "33949281090b3cf2457b57fe77aa5bff27838e58fbce55a52616973014e7c0ac", "7f688df27e6032d215fe3523c405be6015e783457d475d4f2f89a231f07e8288"
  ]
}
```

## gituser | 2018-05-05T13:42:02+00:00
After updating to the branch https://github.com/monero-project/monero/tree/release-v0.12 `release-0.12` monerod updated to the latest block!

```
 ./monerod status
Height: 1566142/1566142 (100.0%) on mainnet, not mining, net hash 456.95 MH/s, v7, up to date, 12(out)+0(in) connections, uptime 0d 0h 5m 57s
```

## gorthorb | 2018-05-06T00:43:57+00:00
I restarted with log level 1, and found these things happening at startup that seem relevant.

We start with lots of these:

```
2018-05-06 00:29:00.893     7f054d454780        INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:2087 transaction with hash b8307f068f6254c50a8c38de847475c6a6d217c2d6b325c66b71171120c92a00 not found in db
```

Then we connect to a node and start processing a long list of "alternative" blocks starting with:

```
2018-05-06 00:29:05.649 [P2P8]  INFO    global  src/cryptonote_core/blockchain.cpp:1475 ----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 1565690
id:     <9fbcd6c0aee81b18f72bb05d98ea43983e60c967fd26214ab60a713121f400a4>
PoW:    <283843c82cef22c32bb7e1ad0984f3f01107af63d702b85c7cefbe0b00000000>
difficulty:     58653367587
```

(these "alternative" blocks are, of course, the correct fork that I want to be on!)

This continues up to here:

```
2018-05-06 00:29:08.282 [P2P1]  INFO    global  src/cryptonote_core/blockchain.cpp:1475 ----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 1565717
id:     <237d516c30240da561aa0421ef8554a2b53722acccd1bc1ea96f9963a8189407>
PoW:    <77696a5302fb41febd0f18800dbe1092f0c9093662e6e59d5140370300000000>
difficulty:     59510014143
2018-05-06 00:29:08.316 [P2P1]  INFO    global  src/cryptonote_core/blockchain.cpp:1464 ###### REORGANIZE on height: 1565690 of 1565717 with cum_difficulty 14334122999529414 alternative blockchain size: 29 with cum_difficulty 14334182620838037
```

Then we apparently-successfully add these blocks, albeit with lots of transaction-not-found errors:

```
2018-05-06 00:29:15.465 [P2P1]  INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:2087 transaction with hash ca290bcdf1e5ee3add8996b7d2554ef8db76c7a8b092543f68400671afc1b74e not found in db
2018-05-06 00:29:15.471 [P2P1]  INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:2087 transaction with hash b64f738f2861f8624669f10fd77ac23b864a574538ad1cd5196de3abfbe11f4d not found in db
2018-05-06 00:29:15.536 [P2P1]  INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:2087 transaction with hash 952dafdb6e28d11953d55ca7ddae99df19eff9540e4e96799b9822c0596835ae not found in db
2018-05-06 00:29:15.558 [P2P1]  INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:2087 transaction with hash 7b5471b3850ea127d34033b11da487c6953b854b11ec9df6f8bacfb5fd983f23 not found in db
2018-05-06 00:29:15.567 [P2P1]  INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:2087 transaction with hash 14aa810597e4ce4aec73b48bb60303ed55fc7e337c936376c8c055651387fa08 not found in db
2018-05-06 00:29:15.578 [P2P1]  INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:2087 transaction with hash d0d71e0f5c137c4246d713710551b2680ea4d150f491ff11b969c7f8a00324cb not found in db
2018-05-06 00:29:15.584 [P2P1]  INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:2087 transaction with hash 3efdceb2bd2b729fb793b86ac518e1a34086935fb0175cd6e0c46b37ffcf52f1 not found in db
2018-05-06 00:29:15.590 [P2P1]  INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:2087 transaction with hash 275f040b3f2ccaf0e59ef687cac36913e54abafac59911397e5b040ec698967f not found in db
2018-05-06 00:29:15.601 [P2P1]  INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:2087 transaction with hash 4f3c0ccdd032787e403e5cc8512d603a6b1727d3df466d6652d61d44f95fa49a not found in db
2018-05-06 00:29:15.608 [P2P1]  INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:2087 transaction with hash dd64f2d49f835e745e84453f87f82f0e0b728dbf0af4cdbbe0ad75c81dd786ca not found in db
2018-05-06 00:29:15.617 [P2P1]  INFO    blockchain      src/cryptonote_core/blockchain.cpp:3549 +++++ BLOCK SUCCESSFULLY ADDED
id:     <9fbcd6c0aee81b18f72bb05d98ea43983e60c967fd26214ab60a713121f400a4>
PoW:    <283843c82cef22c32bb7e1ad0984f3f01107af63d702b85c7cefbe0b00000000>
HEIGHT 1565690, difficulty:     58653367587
block reward: 4.713224682521(4.670716132521 + 0.042508550000), coinbase_blob_size: 95, cumulative size: 151536, 179(1/27)ms
2018-05-06 00:29:15.647 [P2P1]  INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:2087 transaction with hash addaf66ddb226cd10ac9f895a6e4ffcd11eceebdfdd61bdf0b1a1dd2897c2d0a not found in db
2018-05-06 00:29:15.658 [P2P1]  INFO    blockchain      src/cryptonote_core/blockchain.cpp:3549 +++++ BLOCK SUCCESSFULLY ADDED
id:     <8e8f738e270be25c220371f07141139b17941208b350091c7550b460e7b68fb4>
PoW:    <17f20023019aec000b518f560dce5ebccb63da2f5475ac883545750a00000000>
HEIGHT 1565691, difficulty:     58766584555
block reward: 4.681169703837(4.670707223837 + 0.010462480000), coinbase_blob_size: 104, cumulative size: 13891, 38(0/28)ms
...
...
...
2018-05-06 00:29:18.362 [P2P1]  INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:2087 transaction with hash 5b73f547afeebab68c7398334a05bc49cdfa595ec00d696b5a09af90d1144735 not found in db
2018-05-06 00:29:18.373 [P2P1]  INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:2087 transaction with hash 1e47f5e02304735562c4d3893af8412e6b7f6bd94d49fef39a04cd78773bbbb5 not found in db
2018-05-06 00:29:18.384 [P2P1]  INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:2087 transaction with hash 953f6f93953dcd5be5f05a00638ffabf116b2771e0da8d3f50fc744ad6f294d5 not found in db
2018-05-06 00:29:18.394 [P2P1]  INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:2087 transaction with hash 129bd9c5c724f379f5189fba7c5e1b2f13e3a4cba51d6ce311a3509c8e06617e not found in db
2018-05-06 00:29:18.405 [P2P1]  INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:2087 transaction with hash fa0f314a78d58c0da1521293a94f354def0f77a27a0c43a856454fc9d381458d not found in db
2018-05-06 00:29:18.417 [P2P1]  INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:2087 transaction with hash 7c3706fd17f2fc7312780741a0013a6d707310f1136ec1c39c042a85cbc41b4a not found in db
2018-05-06 00:29:18.451 [P2P1]  INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:2087 transaction with hash 3f99ccdd60a5368272c1b42aa47f135dd13bf43627c18f5257e7016811be1794 not found in db
2018-05-06 00:29:18.471 [P2P1]  INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:2087 transaction with hash 5b82d22e8c3c4a8f1105ac95f3f18e8acdb08e6bbdfbab4edd64310e8fa5621c not found in db
2018-05-06 00:29:18.481 [P2P1]  INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:2087 transaction with hash ef99316af9290a0a2110947370117038e945a41c172cb878b194a429894fe990 not found in db
2018-05-06 00:29:18.492 [P2P1]  INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:2087 transaction with hash f0a0c1529a401f4bc66706d5b00a8d3c737b58124148f22a59c8b4ccaa51a7f9 not found in db
2018-05-06 00:29:18.499 [P2P1]  INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:2087 transaction with hash 502ac3a39dc4481e087722dc5816673f9b0e41c0d2936c4755c395784519af74 not found in db
2018-05-06 00:29:18.506 [P2P1]  INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:2087 transaction with hash 41f89a3b39fb7599f4c9125536b2c1492b466e52e55a69b0a91cadae85aea47a not found in db
2018-05-06 00:29:18.513 [P2P1]  INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:2087 transaction with hash b3d25b41c0af370861c5d7d92c8b923525772d75b1b385ff3ecf44e89c298ac4 not found in db
2018-05-06 00:29:18.519 [P2P1]  INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:2087 transaction with hash 6179a4a60b816cd055a1fb182c2eafc85ec606163cc8c42b583c569c6a8878e0 not found in db
2018-05-06 00:29:18.526 [P2P1]  INFO    blockchain      src/cryptonote_core/blockchain.cpp:3549 +++++ BLOCK SUCCESSFULLY ADDED
id:     <6b112935419a1b9378987acc7d9d813bae456ce7dd7611898b9b9cd0f7893730>
PoW:    <da214a12b8d792a37dbd8c55ab505ae2b2bb77953cb9e1c596d82b0100000000>
HEIGHT 1565709, difficulty:     58993236539
block reward: 4.745092040431(4.670546870431 + 0.074545170000), coinbase_blob_size: 104, cumulative size: 205962, 193(0/29)ms
```

Which culminates with:

```
2018-05-06 00:29:18.557 [P2P1]  INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:2087 transaction with hash 6ba209648b4c4c5a230af15082e3abc75451d432f907a0560f438bf463c5561e not found in db
2018-05-06 00:29:18.564 [P2P1]  INFO    ringct  src/ringct/rctSigs.cpp:882      MG signature verification failed
2018-05-06 00:29:18.565 [P2P1]  ERROR   verify  src/cryptonote_core/blockchain.cpp:2901 Failed to check ringct signatures!
2018-05-06 00:29:18.566 [P2P1]  ERROR   verify  src/cryptonote_core/blockchain.cpp:3450 Block with id: <64e978e1893ba6b54f787b5857866e2d6edd5adb2306fd24ac3df4e4b7fe51bb> has at least one transaction (id: <6ba209648b4c4c5a230af15082e3abc75451d432f907a0560f438bf463c5561e>) with wrong inputs.
2018-05-06 00:29:18.567 [P2P1]  INFO    blockchain      src/cryptonote_core/blockchain.cpp:2209 BLOCK ADDED AS INVALID: <64e978e1893ba6b54f787b5857866e2d6edd5adb2306fd24ac3df4e4b7fe51bb>
, prev_id=<6b112935419a1b9378987acc7d9d813bae456ce7dd7611898b9b9cd0f7893730>, m_invalid_blocks count=1
2018-05-06 00:29:18.568 [P2P1]  ERROR   verify  src/cryptonote_core/blockchain.cpp:3454 Block with id <64e978e1893ba6b54f787b5857866e2d6edd5adb2306fd24ac3df4e4b7fe51bb> added as invalid because of wrong inputs in transactions
2018-05-06 00:29:18.574 [P2P1]  INFO    ringct  src/ringct/rctSigs.cpp:882      MG signature verification failed
2018-05-06 00:29:18.575 [P2P1]  ERROR   verify  src/cryptonote_core/blockchain.cpp:2901 Failed to check ringct signatures!
2018-05-06 00:29:18.576 [P2P1]  INFO    txpool  src/cryptonote_core/tx_pool.cpp:307     Transaction added to pool: txid <6ba209648b4c4c5a230af15082e3abc75451d432f907a0560f438bf463c5561e> bytes: 19499 fee/byte: 2.05139e+06
2018-05-06 00:29:18.577 [P2P1]  ERROR   blockchain      src/cryptonote_core/blockchain.cpp:886  Failed to switch to alternative blockchain
```

That block ID about which it's complaining is:

```
2018-05-06 00:29:08.059 [P2P1]  INFO    global  src/cryptonote_core/blockchain.cpp:1475 ----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 1565710
id:     <64e978e1893ba6b54f787b5857866e2d6edd5adb2306fd24ac3df4e4b7fe51bb>
PoW:    <b57c2378e51a3d229f7d1171c0e334ca37fee45ec77b1aba8529dc0300000000>
difficulty:     58882612311
```

## moneromooo-monero | 2018-05-06T10:19:32+00:00
I'll have a log patch for you to apply so I can get more info.

## moneromooo-monero | 2018-05-06T11:21:40+00:00
http://paste.debian.net/hidden/fe7422ae/

Write this to a file, then:

git am /path/to/that/file

Then make, and run, and post the logs after that tx is tried.

## gorthorb | 2018-05-06T14:01:26+00:00
Log with patch applied:

http://paste.debian.net/hidden/7a5dff48/

## moneromooo-monero | 2018-05-06T20:02:55+00:00
Thanks, all seems good so far, I'll add more logs and post again.

## russoj88 | 2018-05-06T20:16:42+00:00
I'm having the same issue on Ubuntu 16.04, but not on FreeBSD 11.1.  I compiled v0.12.  Syncing both nodes from scratch (fresh OS install in bhyve), 0 stops on FreeBSD, but about 5 on Ubuntu.  That being said, I can't say for sure that the OS is the issue.

This is the last thing in the logs consistently:
```
2018-05-06 19:49:05.783 [P2P8]  INFO    global  src/cryptonote_core/blockchain.cpp:1475 ----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 1565715
id:     <fd69fe969b72991e2d971982c3ed28884a06cae081705f453f401814d9e00e4f>                                                                                                                                         
PoW:    <4fd414727331da2a3ddb40f7f37e8923f0a2996eb5bfb987ccff540300000000>                                                                                                                                         
difficulty:     59399134840                                                                                                                                                                                        
2018-05-06 19:49:05.802 [P2P8]  INFO    global  src/cryptonote_core/blockchain.cpp:1475 ----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 1565716
id:     <1420925be80816e4767d310b94f432ef23f74152b68149831ea94fccb6491638>                                                                                                                                         
PoW:    <5b44aa202e07bbafebe5e6e883452d17bd92bcf770a98b8abc60631100000000>                                                                                                                                         
difficulty:     59517898470                                                                                                                                                                                        
2018-05-06 19:49:05.824 [P2P8]  INFO    global  src/cryptonote_core/blockchain.cpp:1475 ----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 1565717
id:     <17a9b9fac7052d31018f9f7b57213c87291ad16242c53c2e6a75d0910c0f5526>                                                                                                                                         
PoW:    <3dbab8f728ba15198f66febaad57f7fd513e2ea1238a75d25d6f111200000000>                                                                                                                                         
difficulty:     59510014143                                                                                                                                                                                        
2018-05-06 19:49:05.844 [P2P8]  INFO    global  src/cryptonote_core/blockchain.cpp:1475 ----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 1565718
id:     <a0facc01cc6760d5aa6d10f155bba7b59cb96aeea334dbccbf68e922a27859ed>                                                                                                                                         
PoW:    <2e7fdb7db676d93f52d602d44fc105bb72132d96dfd4f10a1cbf1c0800000000>                                                                                                                                         
difficulty:     59621308623                                                                                                                                                                                        
2018-05-06 19:49:05.871 [P2P8]  INFO    global  src/cryptonote_core/blockchain.cpp:1475 ----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 1565719
id:     <ca94181d359043a93f15bf682eba8d1ce944409ae3c85c34c23b930cdf7f30b1>                                                                                                                                         
PoW:    <d8d22bcea53fee793a412ae6b6fbf9f560f54553b0797e1b46033a0200000000>                                                                                                                                         
difficulty:     59617270489                                                                                                                                                                                        
2018-05-06 20:03:07.183 [P2P8]  INFO    global  src/cryptonote_core/blockchain.cpp:1475 ----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 1566908
id:     <b39731769b12a15aa4f72f04d0f12e77b7e6650bf97964b2f7e7c74ce711b021>                                                                                                                                         
PoW:    <59705eaf25526da2c6cd5b144b2c0bb18c8d28a8c63f829160143b0300000000>                                                                                                                                         
difficulty:     55545136357                                                                                                                                                                                        
2018-05-06 20:03:07.203 [P2P8]  INFO    global  src/cryptonote_core/blockchain.cpp:1475 ----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 1566909
id:     <d6bc8950b59c66d1b43fbf7eaea31ee50ba74c44cca90034e05bf5026f648d10>                                                                                                                                         
PoW:    <a5eba2d33ed976cb0e04b6a369b4370eb7da11abdbbe32c92198740d00000000>                                                                                                                                         
difficulty:     55523834982                                                                                                                                                                                        
2018-05-06 20:03:07.223 [P2P8]  INFO    global  src/cryptonote_core/blockchain.cpp:1475 ----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 1566910
id:     <4bd985bbf24c89c065fd76133030d864fb53c8d1e6f0973180819b4026ba0291>                                                                                                                                         
PoW:    <5779d3a69c81b447e6c2ec6f2c7ae32dea7cd68774bf2f37c96c6b0600000000>                                                                                                                                         
difficulty:     55472444411
```

## moneromooo-monero | 2018-05-06T22:06:10+00:00
More logs here: http://paste.debian.net/hidden/a3c39ca0/

## gorthorb | 2018-05-06T23:12:47+00:00
New log: http://paste.debian.net/hidden/f6f0bc27/

(I included the BLOCK_DNE exception at the end just in case -- although I think that's probably what's meant to be fixed by #3726, which I don't yet have applied)

## gorthorb | 2018-05-06T23:15:22+00:00
> That being said, I can't say for sure that the OS is the issue.

I don't think it is, as I have two nodes on identical platforms: one has this issue and one doesn't.

I think it's more likely that one node just got unlucky and ended up stuck on this wrong fork, and now can't get back.  Judging by the number of peers that my bad node has, I think this is probably not that uncommon.

(Although it seems particularly unlucky if you've resynced from scratch and hit it a _second_ time!)

## moneromooo-monero | 2018-05-07T11:52:01+00:00
Can you run this on those two nodes, when monerod is not running:
mdb_dump -s txpool_meta ~/.bitmonero/lmdb | grep -c 6ba209648b4c4c5a230af15082e3abc75451d432f907a0560f438bf463c5561e

## gorthorb | 2018-05-07T13:00:55+00:00
Good node: ``0``

Broken node: ``1``

## moneromooo-monero | 2018-05-07T18:26:16+00:00
Try with https://github.com/monero-project/monero/pull/3775

## gorthorb | 2018-05-08T15:01:02+00:00
Cherry-picked and rebuilt.  Exactly the same as before, I'm afraid:

```
2018-05-08 15:00:16.049 [P2P4]  INFO    global  src/cryptonote_core/blockchain.cpp:1464 ###### REORGANIZE on height: 1565690 of 1565721 with cum_difficulty 14334361370969229
 alternative blockchain size: 33 with cum_difficulty 14334420844565009
2018-05-08 15:00:27.548 [P2P4]  ERROR   blockchain      src/cryptonote_core/blockchain.cpp:886  Failed to switch to alternative blockchain
2018-05-08 15:00:30.347 [P2P4]  WARN    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:2780 WARNING: batch transaction mode already enabled, but asked to enable batch mode
2018-05-08 15:00:39.434 [P2P4]  WARN    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:2780 WARNING: batch transaction mode already enabled, but asked to enable batch mode
2018-05-08 15:00:39.488 [P2P4]  ERROR   blockchain      src/cryptonote_core/blockchain.cpp:2208 at insertion invalid by tx returned status existed
2018-05-08 15:00:39.489 [P2P4]  ERROR   blockchain      src/cryptonote_core/blockchain.cpp:897  The block was inserted as invalid while connecting new alternative chain, block_id: <35b6e48186b90cfeade0c8b95eaf32e961edbad538f9428fd080af86bdce35d0>
```

## moneromooo-monero | 2018-05-08T15:32:39+00:00
Alright, then try http://paste.debian.net/hidden/9e3a5d97/ without #3775, and with --log-level 1.

## moneromooo-monero | 2018-05-08T19:51:57+00:00
I think it's fixed by http://paste.debian.net/hidden/f8496e47/ (on top of 3775).

## gituser | 2018-05-09T02:15:47+00:00
just to clarify:

will there be a release with a bugfix to prevent future problems like this?

## gorthorb | 2018-05-09T02:32:44+00:00
That fixed it!  Good work! :D

## khelle | 2018-05-09T08:20:11+00:00
To sum up - which branch do I clone/build now for monero to finally work? I tried branch 0.12 as @moneromooo-monero suggested at the beginning, it then went from 1562078 to 1565730 and then stuck again (around the same block as for everyone else). If I understand correctly I need #3775 PR and http://paste.debian.net/hidden/f8496e47 . but from which branch? Do I need to use still 0.12 and cherry-pick this one commit or do I use master on which this commit is already merged and use only patch?

## moneromooo-monero | 2018-05-09T08:38:01+00:00
release-0.12 is the best to use atm. 3775 is now merged, and the patch above is now PRed as 3788.

## gituser | 2018-05-09T08:57:39+00:00
would be nice if after a week or so you'd release a 0.12.1 bugfix release so others would update to not experience such stuck situations.

## moneromooo-monero | 2018-05-16T10:25:36+00:00
It'll get released whenever pony gets time.
+resolved


# Action History
- Created by: khelle | 2018-04-30T11:25:20+00:00
- Closed at: 2018-05-16T10:40:57+00:00
