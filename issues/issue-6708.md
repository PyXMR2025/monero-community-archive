---
title: 'torsocks: obtaining initial peerlist often takes anywhere from 5 to 20 minutes'
source_url: https://github.com/monero-project/monero/issues/6708
author: tobtoht
assignees: []
labels: []
created_at: '2020-07-15T01:42:49+00:00'
updated_at: '2020-10-15T22:39:58+00:00'
type: issue
status: closed
closed_at: '2020-10-15T22:39:58+00:00'
---

# Original Description
If monerod is started with torsocks and it tries to obtain an initial peerlist by connecting to a seednode that happens to be offline it will incur a two minute timeout (see logs below). After failure, monerod attempts to connect to a different seed node. Quite a few seed nodes appear to be offline and it can often take anywhere from 5 to 20 minutes before monerod is able to reach a seed node that is online. This is an issue for simple/bootstrap mode in the GUI on Tails as the user expects to connect to a remote node right away, instead having to wait an arbitrary length of time without feedback.

```
2020-07-15 00:59:00.981	D Trying to connect to 161.67.132.39:18080, bind_ip = 0.0.0.0
2020-07-15 00:59:23.537	T Checking for idle peers...
2020-07-15 00:59:30.539	T BlockchainLMDB::for_all_txpool_txes
2020-07-15 00:59:30.539	T BlockchainLMDB::block_rtxn_start
2020-07-15 00:59:30.539	T mdb_txn_safe: destructor
2020-07-15 00:59:51.544	T Blockchain::get_current_blockchain_height
2020-07-15 00:59:51.544	T BlockchainLMDB::height
2020-07-15 00:59:51.544	T BlockchainLMDB::block_rtxn_start
2020-07-15 00:59:51.544	T mdb_txn_safe: destructor
2020-07-15 00:59:51.544	D Not checking block rate, offline or syncing
2020-07-15 00:59:53.545	T Checking for idle peers...
2020-07-15 01:00:00.546	T BlockchainLMDB::for_all_txpool_txes
2020-07-15 01:00:00.546	T BlockchainLMDB::block_rtxn_start
2020-07-15 01:00:00.546	T mdb_txn_safe: destructor
2020-07-15 01:00:15.549	T Blockchain::get_current_blockchain_height
2020-07-15 01:00:15.549	T BlockchainLMDB::height
2020-07-15 01:00:15.549	T BlockchainLMDB::block_rtxn_start
2020-07-15 01:00:15.549	T mdb_txn_safe: destructor
2020-07-15 01:00:15.549	T Checking for outgoing syncing peers...
2020-07-15 01:00:15.549	T 0 syncing, 0 synced
2020-07-15 01:00:23.552	T Checking for idle peers...
2020-07-15 01:00:30.553	T BlockchainLMDB::for_all_txpool_txes
2020-07-15 01:00:30.553	T BlockchainLMDB::block_rtxn_start
2020-07-15 01:00:30.554	T mdb_txn_safe: destructor
2020-07-15 01:00:51.557	T BlockchainLMDB::get_txpool_tx_count
2020-07-15 01:00:51.557	T BlockchainLMDB::block_rtxn_start
2020-07-15 01:00:51.557	T mdb_txn_safe: destructor
2020-07-15 01:00:51.557	T BlockchainLMDB::for_all_txpool_txes
2020-07-15 01:00:51.557	T BlockchainLMDB::block_rtxn_start
2020-07-15 01:00:51.557	T mdb_txn_safe: destructor
2020-07-15 01:00:53.558	T Checking for idle peers...
2020-07-15 01:01:00.559	T BlockchainLMDB::for_all_txpool_txes
2020-07-15 01:01:00.559	T BlockchainLMDB::block_rtxn_start
2020-07-15 01:01:00.559	T mdb_txn_safe: destructor
1594774867 ERROR torsocks[7966]: General SOCKS server failure (in socks5_recv_connect_reply() at socks5.c:527)
2020-07-15 01:01:07.145	T Some problems at connect, message: Connection refused
2020-07-15 01:01:07.145	T [sock -1] Socket destroyed without shutdown.
2020-07-15 01:01:07.145	T [sock -1] Socket destroyed
2020-07-15 01:01:07.145	T [<none> OUT] ~async_protocol_handler()
2020-07-15 01:01:07.145	D Destructing connection #2 to 0.0.0.0
2020-07-15 01:01:07.145	I 0Connect failed to 161.67.132.39:18080
2020-07-15 01:01:07.145	D Connecting to 163.172.182.165:18080(peer_type=1, last_seen: never)...
```
^ this is repeated until an online seed node is found

Possible solutions:
* Remove permanently offline seed nodes
* Find a way to lower the timeout
* Try to connect to multiple seednodes at once


# Discussion History
## tobtoht | 2020-07-15T02:49:22+00:00
Offline / unconnectable seed nodes (at this time, tested with --add-exclusive-node):
- 107.152.130.98:18080
- 163.172.182.165:18080
- 161.67.132.39:18080
- 198.74.231.92:18080

Connection refused (Tor block? see logs below):
- 195.154.123.123:18080
- 209.250.243.248:18080
- 5.9.100.248:18080

Online:
- 212.83.175.67:18080
- 212.83.172.165:18080
- 192.110.160.146:18080
- 88.198.163.90:18080
- 104.238.221.81:18080
- 66.85.74.134:18080
- 95.217.25.101:18080

```
2020-07-15 02:46:15.005	D Trying to connect to 5.9.100.248:18080, bind_ip = 0.0.0.0
1594781175 ERROR torsocks[10790]: Connection refused to Tor SOCKS (in socks5_recv_connect_reply() at socks5.c:543)
2020-07-15 02:46:15.100	T Some problems at connect, message: Connection refused
2020-07-15 02:46:15.101	T [sock -1] Socket destroyed without shutdown.
2020-07-15 02:46:15.101	T [sock -1] Socket destroyed
2020-07-15 02:46:15.101	T [<none> OUT] ~async_protocol_handler()
2020-07-15 02:46:15.101	D Destructing connection #17 to 0.0.0.0
2020-07-15 02:46:15.101	I 0[priority]Connect failed to 5.9.100.248:18080
2020-07-15 02:46:16.101	D Connecting to 5.9.100.248:18080(peer_type=1, last_seen: never)...
2020-07-15 02:46:16.101	D Spawned connection #18 to 0.0.0.0 currently we have sockets count:2
2020-07-15 02:46:16.101	D test, connection constructor set m_connection_type=2
2020-07-15 02:46:16.101	D connections_ size now 1
2020-07-15 02:46:16.102	D Trying to connect to 5.9.100.248:18080, bind_ip = 0.0.0.0
1594781176 ERROR torsocks[10790]: Connection refused to Tor SOCKS (in socks5_recv_connect_reply() at socks5.c:543)
2020-07-15 02:46:16.204	T Some problems at connect, message: Connection refused
2020-07-15 02:46:16.204	T [sock -1] Socket destroyed without shutdown.
2020-07-15 02:46:16.204	T [sock -1] Socket destroyed
2020-07-15 02:46:16.205	T [<none> OUT] ~async_protocol_handler()
2020-07-15 02:46:16.205	D Destructing connection #18 to 0.0.0.0
2020-07-15 02:46:16.205	I 0[priority]Connect failed to 5.9.100.248:18080
2020-07-15 02:46:17.205	D Connecting to 5.9.100.248:18080(peer_type=1, last_seen: never)...
2020-07-15 02:46:17.205	D Spawned connection #19 to 0.0.0.0 currently we have sockets count:2
2020-07-15 02:46:17.205	D test, connection constructor set m_connection_type=2
2020-07-15 02:46:17.205	D connections_ size now 1
2020-07-15 02:46:17.206	D Trying to connect to 5.9.100.248:18080, bind_ip = 0.0.0.0
1594781177 ERROR torsocks[10790]: Connection refused to Tor SOCKS (in socks5_recv_connect_reply() at socks5.c:543)
```


## erciccione | 2020-07-15T07:34:59+00:00
> Remove permanently offline seed nodes

This should be done anyway. Some nodes have been offline since forever and should be removed from the list. We discussed this in a dev meeting not long ago (https://github.com/monero-project/meta/issues/449).

> Connection refused (Tor block? see logs below):
209.250.243.248:18080

This one is mine. The daemon went offline or got stuck few days ago, but i cannot access that VPS at the moment. It will be back online as soon as possible, probably before the end of this month.

## tobtoht | 2020-07-15T17:27:09+00:00
```
2020-07-15 15:56:44.127	D Trying to connect to 198.74.231.92:18080, bind_ip = 0.0.0.0
1594828604 DEBUG torsocks[243392]: [socket] Creating socket with domain 2, type 1 and protocol 6 (in tsocks_socket() at socket.c:32)
1594828604 DEBUG torsocks[243392]: Connect caught on fd 22 (in tsocks_connect() at connect.c:118)
1594828604 DEBUG torsocks[243392]: [connect] Socket family AF_INET and type 1 (in tsocks_validate_socket() at connect.c:76)
1594828604 DEBUG torsocks[243392]: [onion] Finding onion entry for IP 198.74.231.92 (in onion_entry_find_by_addr() at onion.c:267)
1594828604 DEBUG torsocks[243392]: Connecting to the Tor network on fd 22 (in tsocks_connect_to_tor() at torsocks.c:473)
1594828604 DEBUG torsocks[243392]: Setting up a connection to the Tor network on fd 22 (in setup_tor_connection() at torsocks.c:368)
1594828604 DEBUG torsocks[243392]: Socks5 sending method ver: 5, nmethods 0x01, methods 0x00 (in socks5_send_method() at socks5.c:228)
1594828604 DEBUG torsocks[243392]: Socks5 received method ver: 5, method 0x00 (in socks5_recv_method() at socks5.c:262)
1594828604 DEBUG torsocks[243392]: Socks5 sending connect request to fd 22 (in socks5_send_connect_request() at socks5.c:459)

... 2 minutes later

1594828729 DEBUG torsocks[243392]: Socks5 received connect reply - ver: 5, rep: 0x01, atype: 0x01 (in socks5_recv_connect_reply() at socks5.c:518)
1594828729 ERROR torsocks[243392]: General SOCKS server failure (in socks5_recv_connect_reply() at socks5.c:527)
2020-07-15 15:58:49.260	T Some problems at connect, message: Connection refused
1594828729 DEBUG torsocks[243392]: [close] Close caught for fd 22 (in tsocks_close() at close.c:33)
2020-07-15 15:58:49.260	T [sock -1] Socket destroyed without shutdown.
2020-07-15 15:58:49.260	T [sock -1] Socket destroyed
```

Looking at torsocks source it is apparent that it simply waits for the Tor daemon to respond with the status of the connect request, which it receives after about ~2 minutes.

I'm not sure why using torsocks causes try_connect() in contrib/epee/include/net/abstract_tcp_server2.inl to fail at enforcing the 5 second timeout.

What's more peculiar is that the call stack is essentially the same as #6706, yet there it never recovers:

```
Thread 12 (Thread 0x7fcf8effd700 (LWP 257011)):
#0  0x00007fcfe7b704fb in select () from /usr/lib/libc.so.6
#1  0x00007fcfe86e8606 in wait_on_fd (fd=fd@entry=22) at socks5.c:40
#2  0x00007fcfe86e8835 in recv_data_impl (fd=22, buf=0x7fcf8effb8e0, len=<optimized out>) at socks5.c:70
#3  0x00007fcfe86e938d in socks5_recv_connect_reply (conn=conn@entry=0x7fcf8001e1a0) at socks5.c:515
#4  0x00007fcfe86e1f32 in tsocks_connect_to_tor (conn=conn@entry=0x7fcf8001e1a0) at torsocks.c:500
#5  0x00007fcfe86e29cd in tsocks_connect (sockfd=<optimized out>, addr=0x7fcf8effbe30, addrlen=<optimized out>) at connect.c:206
#6  0x0000556ae3fea759 in boost::asio::detail::reactive_socket_service_base::start_connect_op(boost::asio::detail::reactive_socket_service_base::base_implementation_type&, boost::asio::detail::reactor_op*, bool, sockaddr const*, unsigned long) ()
#7  0x0000556ae4056666 in void boost::asio::basic_socket<boost::asio::ip::tcp, boost::asio::executor>::initiate_async_connect::operator()<boost::_bi::bind_t<void, epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::try_connect(boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > >, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, boost::asio::basic_stream_socket<boost::asio::ip::tcp, boost::asio::executor>&, boost::asio::ip::basic_endpoint<boost::asio::ip::tcp> const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, unsigned int, epee::net_utils::ssl_support_t)::{lambda(boost::system::error_code, boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::try_connect(boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > >, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, boost::asio::basic_stream_socket<boost::asio::ip::tcp, boost::asio::executor>&, boost::asio::ip::basic_endpoint<boost::asio::ip::tcp> const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, unsigned int, epee::net_utils::ssl_support_t)::local_async_context>)#1}, boost::_bi::list2<boost::arg<1>, boost::_bi::value<boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::try_connect(boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > >, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, boost::asio::basic_stream_socket<boost::asio::ip::tcp, boost::asio::executor>&, boost::asio::ip::basic_endpoint<boost::asio::ip::tcp> const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, unsigned int, epee::net_utils::ssl_support_t)::local_async_context> > > > >(boost::_bi::bind_t<void, epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::try_connect(boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > >, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, boost::asio::basic_stream_socket<boost::asio::ip::tcp, boost::asio::executor>&, boost::asio::ip::basic_endpoint<boost::asio::ip::tcp> const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, unsigned int, epee::net_utils::ssl_support_t)::{lambda(boost::system::error_code, boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::try_connect(boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > >, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, boost::asio::basic_stream_socket<boost::asio::ip::tcp, boost::asio::executor>&, boost::asio::ip::basic_endpoint<boost::asio::ip::tcp> const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, unsigned int, epee::net_utils::ssl_support_t)::local_async_context>)#1}, boost::_bi::list2<boost::arg<1>, boost::_bi::value<boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::try_connect(boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > >, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, boost::asio::basic_stream_socket<boost::asio::ip::tcp, boost::asio::executor>&, boost::asio::ip::basic_endpoint<boost::asio::ip::tcp> const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, unsigned int, epee::net_utils::ssl_support_t)::local_async_context> > > >&&, boost::asio::ip::basic_endpoint<boost::asio::ip::tcp> const&, boost::system::error_code const&) const ()
#8  0x0000556ae4056a21 in ?? ()
#9  0x0000556ae4067a47 in epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::connect(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, unsigned int, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, epee::net_utils::ssl_support_t) ()
#10 0x0000556ae40695c1 in nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::public_connect(nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::network_zone&, epee::net_utils::network_address const&, epee::net_utils::ssl_support_t) ()
#11 0x0000556ae408045b in nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::try_to_connect_and_handshake_with_new_peer(epee::net_utils::network_address const&, bool, unsigned long, nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::PeerType, unsigned long) ()
#12 0x0000556ae4087554 in nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::connections_maker() ()
#13 0x0000556ae3fe538c in nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::idle_worker() ()
#14 0x0000556ae4025812 in bool epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::global_timer_handler<boost::_bi::bind_t<bool, boost::_mfi::mf0<bool, nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> > >, boost::_bi::list1<boost::_bi::value<nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >*> > > >(boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext<boost::_bi::bind_t<bool, boost::_mfi::mf0<bool, nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> > >, boost::_bi::list1<boost::_bi::value<nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >*> > > > >) ()
#15 0x0000556ae4053e7c in boost::asio::detail::wait_handler<boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext<boost::_bi::bind_t<bool, boost::_mfi::mf0<bool, nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> > >, boost::_bi::list1<boost::_bi::value<nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >*> > > > > >, boost::_bi::list2<boost::_bi::value<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >*>, boost::_bi::value<boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext<boost::_bi::bind_t<bool, boost::_mfi::mf0<bool, nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> > >, boost::_bi::list1<boost::_bi::value<nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >*> > > > > > > >, boost::asio::detail::io_object_executor<boost::asio::executor> >::do_complete(void*, boost::asio::detail::scheduler_operation*, boost::system::error_code const&, unsigned long) ()
#16 0x0000556ae3fcca87 in ?? ()
#17 0x0000556ae4005efb in epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread() ()
#18 0x00007fcfe8320857 in ?? () from /usr/lib/libboost_thread.so.1.72.0
#19 0x00007fcfe7c4b422 in start_thread () from /usr/lib/libpthread.so.0
#20 0x00007fcfe7b78bf3 in clone () from /usr/lib/libc.so.6
```

## erciccione | 2020-07-23T08:09:40+00:00
FYI my node (209.250.243.248:18080) is up again and some dead nodes are being removed (https://github.com/monero-project/monero/pull/6571). That should partially improve the situation.

## normoes | 2020-07-27T19:57:24+00:00
Do you know about this?

https://community.xmr.to/xmr-seed-nodes/

## moneromooo-monero | 2020-10-15T22:39:58+00:00
The seed list was cleaned up, and more added.

# Action History
- Created by: tobtoht | 2020-07-15T01:42:49+00:00
- Closed at: 2020-10-15T22:39:58+00:00
