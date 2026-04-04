---
title: RPi3B+ monerod errors
source_url: https://github.com/monero-project/monero/issues/4507
author: dawiepoolman
assignees: []
labels: []
created_at: '2018-10-06T14:40:52+00:00'
updated_at: '2018-10-13T16:17:10+00:00'
type: issue
status: closed
closed_at: '2018-10-10T16:51:57+00:00'
---

# Original Description
Hi guys

After having deleted and re-started downloading the blockchain a week ago I started seeing errors again:

![image](https://user-images.githubusercontent.com/2351212/46572367-d8810400-c984-11e8-8e6c-54f28e64d372.png)

I have been following [this](https://pinode.weebly.com/monero-node-for-pi-3-or-armv7-devices-no-lcd-display.html) guide for the setup.

I have used this refined command to launch monerod with more manageable block-sync-size:
```
./bin/monero-v0.12.3.0/monerod --rpc-bind-ip=192.168.1.10 --rpc-bind-port=4008 --confirm-external-bind --max-concurrency 1 --block-sync-size 20
```

It was running very stable up to this point. I have a 2Tb external hdd connected to the pi.  Is the mapping correc?

```
./bin/monero-v0.12.3.0/monerod --rpc-bind-ip=192.168.1.10 --rpc-bind-port=4008 --confirm-external-bind --max-concurrency 1 --block-sync-size 20 --log-level 1
```
produces:

![image](https://user-images.githubusercontent.com/2351212/46572459-1fbbc480-c986-11e8-9e9c-0b378f1c6f6f.png)

```
./bin/monero-v0.12.3.0/monerod --rpc-bind-ip=192.168.1.10 --rpc-bind-port=4008 --confirm-external-bind --db-salvage
```

Is the database corrupted again?

# Discussion History
## moneromooo-monero | 2018-10-06T14:48:00+00:00
You seem to be out of memory. Or something is trying to allocate a whole lot. Use more memory, add swap, etc. Do you have a stack trace for the crash ?

## dawiepoolman | 2018-10-06T16:10:33+00:00
Hi moneromoo
I am struggling to figure out how to produce/analyse the stack trace with gdb (I have no idea how this works tbh)

When I ran 
'''
gdb ./bin/monero-v0.12.3.0/monerod
run --rpc-bind-ip=192.168.1.10 --rpc-bind-port=4008 --confirm-external-bind --max-concurrency 1 --block-sync-size 20 --log-level 1
'''
I got this
![image](https://user-images.githubusercontent.com/2351212/46573213-18021d00-c992-11e8-8f65-82d21e02f97b.png)


I have tried increasing the swap file in the manual from 1000 to 5000 but when I ran 
'''sudo dphys-swapfile setup
'''
it appeared to have capped it to a max default of 2048MB
Would that be sufficient for --block-sync-size 20? I tried with --block-sync-size 1 as well but I get the same issue


## moneromooo-monero | 2018-10-06T16:15:38+00:00
That should be enough, and sync size should not really matter a whole lot here.

 But the db is probably corrupt indeed if you get a SIGSEGV there. You can type "bt" to get the stack trace at the crash point (you have just the tip here).


## dawiepoolman | 2018-10-06T16:29:42+00:00
Cool, I was close :P 
Here is the stack trace 

#0  0x0093ed64 in mdb_midl_xmerge ()
#1  0x00938ee6 in mdb_page_alloc.isra ()
#2  0x0093a430 in mdb_page_new ()
#3  0x0093a634 in mdb_node_add ()
#4  0x0093cb68 in mdb_cursor_put ()
#5  0x007c8640 in cryptonote::BlockchainLMDB::add_txpool_tx(cryptonote::transaction const&, cryptonote::txpool_tx_meta_t const&) ()
#6  0x008124e4 in cryptonote::tx_memory_pool::add_tx(cryptonote::transaction&, crypto::hash const&, unsigned int, cryptonote::tx_verification_context&, bool, bool, bool, unsigned char) ()
#7  0x008039aa in cryptonote::core::add_new_tx(cryptonote::transaction&, crypto::hash const&, crypto::hash const&, unsigned int, cryptonote::tx_verification_context&, bool, bool, bool) ()
#8  0x0080405c in cryptonote::core::handle_incoming_txs(std::__cxx11::list<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > const&, std::vector<cryptonote::tx_verification_context, std::allocator<cryptonote::tx_verification_context> >&, bool, bool, bool) ()
#9  0x007a4374 in cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::try_add_next_blocks(cryptonote::cryptonote_connection_context&) ()
#10 0x007a62de in cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::handle_response_get_objects(int, cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request&, cryptonote::cryptonote_connection_context&) ()
#11 0x006b727e in int epee::net_utils::buff_to_t_adapter<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request, cryptonote::cryptonote_connection_context, boost::_bi::bind_t<int, boost::_mfi::mf3<int, cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, int, cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request&, cryptonote::cryptonote_connection_context&>, boost::_bi::list4<boost::_bi::value<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*>, boost::arg<1>, boost::arg<2>, boost::arg<3> > > >(cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, boost::_bi::bind_t<int, boost::_mfi::mf3<int, cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, int, cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request&, cryptonote::cryptonote_connection_context&>, boost::_bi::list4<boost::_bi::value<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*>, boost::arg<1>, boost::arg<2>, boost::arg<3> > >, cryptonote::cryptonote_connection_context&) ()
#12 0x006b82f4 in int cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::handle_invoke_map<cryptonote::cryptonote_connection_context>(bool, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&, cryptonote::cryptonote_connection_context&, bool&) ()
#13 0x006b84aa in int nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::handle_invoke_map<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >(bool, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&, bool&) ()
#14 0x006b8732 in nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::notify(int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&) ()
#15 0x007b0890 in epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >::handle_recv(void const*, unsigned int) ()
#16 0x007bea76 in epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::handle_read(boost::system::error_code const&, unsigned int) ()
#17 0x007a7f2a in void boost::asio::detail::strand_service::dispatch<boost::asio::detail::binder2<boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned int>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::system::error_code, unsigned int> >(boost::asio::detail::strand_service::strand_impl*&, boost::asio::detail::binder2<boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned int>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::system::error_code, unsigned int>&) ()
#18 0x007a8110 in boost::asio::detail::completion_handler<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_context::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned int>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned int>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned int>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > > >::do_complete(void*, boost::asio::detail::scheduler_operation*, boost::system::error_code const&, unsigned int) ()
#19 0x007a833e in void boost::asio::detail::strand_service::dispatch<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_context::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned int>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned int>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::as---Type <return> to continue, or q <return> to quit---




## dawiepoolman | 2018-10-06T16:30:42+00:00
#19 0x007a833e in void boost::asio::detail::strand_service::dispatch<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_context::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned int>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned int>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::as---Type <return> to continue, or q <return> to quit---
ync_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned int>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > > >(boost::asio::detail::strand_service::strand_impl*&, boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_context::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned int>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned int>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned int>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > >&) ()
#20 0x007a847c in boost::asio::detail::reactive_socket_recv_op<boost::asio::mutable_buffers_1, boost::asio::detail::wrapped_handler<boost::asio::io_context::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned int>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running> >::do_complete(void*, boost::asio::detail::scheduler_operation*, boost::system::error_code const&, unsigned int) ()
#21 0x006e3276 in boost::asio::detail::epoll_reactor::descriptor_state::do_complete(void*, boost::asio::detail::scheduler_operation*, boost::system::error_code const&, unsigned int) ()
#22 0x00678e16 in boost::asio::detail::scheduler::run(boost::system::error_code&) ()
#23 0x0078c770 in epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread() ()
#24 0x00a86f8c in thread_proxy ()
#25 0x76ef8fc4 in start_thread (arg=0x667ff450) at pthread_create.c:335
#26 0x76e84bc8 in ?? () at ../sysdeps/unix/sysv/linux/arm/clone.S:76 from /lib/arm-linux-gnueabihf/libc.so.6
Backtrace stopped: previous frame identical to this frame (corrupt stack?)


## dawiepoolman | 2018-10-06T16:36:25+00:00
rm data.mdb and start again with 2048MB RAM instead of 1000MB?


## moneromooo-monero | 2018-10-06T17:59:51+00:00
I now think the memory's ok, the DB being shot probably causes it to request silly amounts based on bad data. Maybe hyc can help more here.

## dawiepoolman | 2018-10-07T06:16:49+00:00
so I deleted the mdb and restarted. after a few hours ...
![image](https://user-images.githubusercontent.com/2351212/46578864-e330ad00-ca07-11e8-9f28-0ac78d585abf.png)
should i run fsck?


## dawiepoolman | 2018-10-07T16:40:23+00:00
Hi guys, FYI, I cross posted this issue to the [r/pinode](https://old.reddit.com/r/pinode/comments/9m3522/pi_swapdrive_corrupt/) subreddit to ask for help there w.r.t. what could also be Pi setup related errors
u/shermand100 has been very helpful too

## dawiepoolman | 2018-10-07T19:58:23+00:00
Hi guys


I failed again:

2018-10-07 19:50:20.452 [P2P2]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171    [185.152.64.176:18080 OUT]  Synced 96116/1677909
2018-10-07 19:50:28.878 [P2P2]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171    [185.152.64.176:18080 OUT]  Synced 96121/1677909
2018-10-07 19:50:31.267 [P2P2]  ERROR   cn      src/cryptonote_basic/cryptonote_format_utils.cpp:987    Failed to parse block from blob
*** Error in `./bin/monero-v0.12.3.0/monerod': munmap_chunk(): invalid pointer: 0x4accc3c8 ***
Aborted
pi@xmrpi:~ $


## dawiepoolman | 2018-10-07T20:02:29+00:00
update
I ran:
./bin/monero-v0.12.3.0/monero-blockchain-import --pop-blocks 10

when I resumed monerod it went past the block.  
Why would it be so unstable?

## dawiepoolman | 2018-10-07T20:11:58+00:00
failed again

2018-10-07 20:09:01.940 [P2P4]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171    [148.251.89.12:18080 OUT]  Synced 96816/1677923
2018-10-07 20:09:02.633 [P2P4]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171    [148.251.89.12:18080 OUT]  Synced 96821/1677923
2018-10-07 20:09:08.860 [P2P4]  WARN    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:75   Failed to add output pubkey to db transaction: MDB_KEYEXIST: Key/data pair already exists
2018-10-07 20:09:11.931 [P2P4]  ERROR   blockchain      src/cryptonote_core/blockchain.cpp:3585 Error adding block with hash: <14f1cc8df986d22a2c9016dd8f5aecc9a7db3a429e724ab0eba392e91732f3e2> to blockchain, what = Failed to add output pubkey to db transaction: MDB_KEYEXIST: Key/data pair already exists
2018-10-07 20:09:11.952 [P2P4]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171    [148.251.89.12:18080 OUT]  Synced 96825/1677923
2018-10-07 20:10:08.620 [P2P1]  ERROR   blockchain      src/cryptonote_core/blockchain.cpp:3449 Block with id: <14f1cc8df986d22a2c9016dd8f5aecc9a7db3a429e724ab0eba392e91732f3e2> attempting to add transaction already in blockchain with id: <74366d0cb8736eb4368bb663938d705b40d58620038ee404bde971dc39e0ca6f>
2018-10-07 20:10:16.191 [P2P1]  ERROR   blockchain      src/cryptonote_core/blockchain.cpp:3449 Block with id: <14f1cc8df986d22a2c9016dd8f5aecc9a7db3a429e724ab0eba392e91732f3e2> attempting to add transaction already in blockchain with id: <74366d0cb8736eb4368bb663938d705b40d58620038ee404bde971dc39e0ca6f>
2018-10-07 20:10:26.976 [P2P6]  ERROR   blockchain      src/cryptonote_core/blockchain.cpp:3449 Block with id: <14f1cc8df986d22a2c9016dd8f5aecc9a7db3a429e724ab0eba392e91732f3e2> attempting to add transaction already in blockchain with id: <74366d0cb8736eb4368bb663938d705b40d58620038ee404bde971dc39e0ca6f>



## dawiepoolman | 2018-10-07T20:19:31+00:00
2018-10-07 20:17:07.080         76f12210        INFO    global  src/cryptonote_core/cryptonote_core.cpp:427     Loading blockchain from folder /home/pi/.bitmonero/lmdb ...
Bus error


## dawiepoolman | 2018-10-07T20:23:22+00:00
gdb ./bin/monero-v0.12.3.0/monerod
GNU gdb (Raspbian 7.12-6) 7.12.0.20161007-git
Copyright (C) 2016 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
and "show warranty" for details.
This GDB was configured as "arm-linux-gnueabihf".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
<http://www.gnu.org/software/gdb/documentation/>.
For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from ./bin/monero-v0.12.3.0/monerod...(no debugging symbols found)...done.
(gdb) run --rpc-bind-ip=192.168.1.10 --rpc-bind-port=4008 --confirm-external-bind --max-concurrency 1 --block-sync-size 5 --log-level 1
Starting program: /home/pi/bin/monero-v0.12.3.0/monerod --rpc-bind-ip=192.168.1.10 --rpc-bind-port=4008 --confirm-external-bind --max-concurrency 1 --block-sync-size 5 --log-level 1
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/arm-linux-gnueabihf/libthread_db.so.1".
2018-10-07 20:22:13.616         76ff6210        INFO    global  src/daemon/main.cpp:282 Monero 'Lithium Luna' (v0.12.3.0-release)
2018-10-07 20:22:13.616         76ff6210        INFO    daemon  src/daemon/main.cpp:284 Moving from main() into the daemonize now.
2018-10-07 20:22:13.617         76ff6210        INFO    global  src/daemon/protocol.h:53        Initializing cryptonote protocol...
2018-10-07 20:22:13.617         76ff6210        INFO    global  src/daemon/protocol.h:58        Cryptonote protocol initialized OK
[New Thread 0x76db3450 (LWP 604)]
2018-10-07 20:22:13.619         76ff6210        INFO    global  src/daemon/p2p.h:63     Initializing p2p server...
2018-10-07 20:22:13.620         76ff6210        INFO    net.throttle    contrib/epee/src/network_throttle-detail.cpp:162        Setting LIMIT: 2048 kbps
2018-10-07 20:22:13.620         76ff6210        INFO    net.p2p src/p2p/net_node.inl:1875       Set limit-up to 2048 kB/s
2018-10-07 20:22:13.620         76ff6210        INFO    net.throttle    contrib/epee/src/network_throttle-detail.cpp:162        Setting LIMIT: 8192 kbps
2018-10-07 20:22:13.620         76ff6210        INFO    net.throttle    contrib/epee/src/network_throttle-detail.cpp:162        Setting LIMIT: 8192 kbps
2018-10-07 20:22:13.620         76ff6210        INFO    net.p2p src/p2p/net_node.inl:1888       Set limit-down to 8192 kB/s
2018-10-07 20:22:13.620         76ff6210        INFO    net.throttle    contrib/epee/src/network_throttle-detail.cpp:162        Setting LIMIT: 2048 kbps
2018-10-07 20:22:13.620         76ff6210        INFO    net.p2p src/p2p/net_node.inl:1910       Set limit-up to 2048 kB/s
2018-10-07 20:22:13.621         76ff6210        INFO    net.throttle    contrib/epee/src/network_throttle-detail.cpp:162        Setting LIMIT: 8192 kbps
2018-10-07 20:22:13.621         76ff6210        INFO    net.throttle    contrib/epee/src/network_throttle-detail.cpp:162        Setting LIMIT: 8192 kbps
2018-10-07 20:22:13.621         76ff6210        INFO    net.p2p src/p2p/net_node.inl:1914       Set limit-down to 8192 kB/s
[New Thread 0x768b3450 (LWP 605)]
[New Thread 0x760b3450 (LWP 606)]
[New Thread 0x756ff450 (LWP 607)]
[New Thread 0x74cff450 (LWP 608)]
2018-10-07 20:22:13.790         768b3450        INFO    net.p2p src/p2p/net_node.inl:457        dns_threads[0] addr_str: seeds.moneroseeds.se  number of results: 0
[Thread 0x768b3450 (LWP 605) exited]
2018-10-07 20:22:13.814         756ff450        INFO    net.p2p src/p2p/net_node.inl:457        dns_threads[2] addr_str: seeds.moneroseeds.ch  number of results: 0
[Thread 0x756ff450 (LWP 607) exited]
2018-10-07 20:22:13.817         74cff450        INFO    net.p2p src/p2p/net_node.inl:457        dns_threads[3] addr_str: seeds.moneroseeds.li  number of results: 0
[Thread 0x74cff450 (LWP 608) exited]
2018-10-07 20:22:16.091         760b3450        INFO    net.p2p src/p2p/net_node.inl:457        dns_threads[1] addr_str: seeds.moneroseeds.ae.org  number of results: 0
2018-10-07 20:22:16.092         76ff6210        INFO    net.p2p src/p2p/net_node.inl:495        DNS seed node lookup either timed out or failed, falling back to defaults
[Thread 0x760b3450 (LWP 606) exited]
2018-10-07 20:22:16.099         76ff6210        INFO    net.p2p src/p2p/net_node.inl:357        Added seed node: 107.152.130.98:18080
2018-10-07 20:22:16.099         76ff6210        INFO    net.p2p src/p2p/net_node.inl:357        Added seed node: 161.67.132.39:18080
2018-10-07 20:22:16.100         76ff6210        INFO    net.p2p src/p2p/net_node.inl:357        Added seed node: 163.172.182.165:18080
2018-10-07 20:22:16.100         76ff6210        INFO    net.p2p src/p2p/net_node.inl:357        Added seed node: 195.154.123.123:18080
2018-10-07 20:22:16.100         76ff6210        INFO    net.p2p src/p2p/net_node.inl:357        Added seed node: 198.74.231.92:18080
2018-10-07 20:22:16.100         76ff6210        INFO    net.p2p src/p2p/net_node.inl:357        Added seed node: 212.83.172.165:18080
2018-10-07 20:22:16.100         76ff6210        INFO    net.p2p src/p2p/net_node.inl:357        Added seed node: 212.83.175.67:18080
2018-10-07 20:22:16.101         76ff6210        INFO    net.p2p src/p2p/net_node.inl:357        Added seed node: 5.9.100.248:18080
2018-10-07 20:22:16.147         76ff6210        INFO    net     contrib/epee/include/net/abstract_tcp_server2.inl:910   Set server type to: 2 from name: P2P, prefix_name = P2P
2018-10-07 20:22:16.147         76ff6210        INFO    net.p2p src/p2p/net_node.inl:546        Binding on 0.0.0.0:18080
2018-10-07 20:22:16.148         76ff6210        INFO    net.p2p src/p2p/net_node.inl:551        Net service bound to 0.0.0.0:18080
2018-10-07 20:22:17.756         76ff6210        INFO    net.p2p src/p2p/net_node.inl:2004       Added IGD port mapping.
2018-10-07 20:22:17.756         76ff6210        INFO    global  src/daemon/p2p.h:68     p2p server initialized OK
2018-10-07 20:22:17.758         76ff6210        INFO    global  src/daemon/rpc.h:63     Initializing core RPC server...
2018-10-07 20:22:17.758         76ff6210        INFO    net     contrib/epee/include/net/abstract_tcp_server2.inl:910   Set server type to: 1 from name: RPC, prefix_name = RPC
2018-10-07 20:22:17.758         76ff6210        INFO    global  contrib/epee/include/net/http_server_impl_base.h:76     Binding on 192.168.1.10:4008
2018-10-07 20:22:17.759         76ff6210        INFO    global  src/daemon/rpc.h:69     core RPC server initialized OK on port: 4008
2018-10-07 20:22:17.759         76ff6210        INFO    global  src/daemon/core.h:86    Initializing core...
2018-10-07 20:22:17.762         76ff6210        INFO    global  src/cryptonote_core/cryptonote_core.cpp:427     Loading blockchain from folder /home/pi/.bitmonero/lmdb ...
2018-10-07 20:22:17.763         76ff6210        INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:528  DB map size:     3074644480
2018-10-07 20:22:17.764         76ff6210        INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:529  Space used:      1632563200
2018-10-07 20:22:17.764         76ff6210        INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:530  Space remaining: 1442081280
2018-10-07 20:22:17.764         76ff6210        INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:531  Size threshold:  0
2018-10-07 20:22:17.764         76ff6210        INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:533  Percent used: 0.5310  Percent threshold: 0.8000

Thread 1 "monerod" received signal SIGBUS, Bus error.
0x009368b0 in mdb_rpage_get ()
(gdb)


## dawiepoolman | 2018-10-07T20:24:10+00:00
stuff it.  restarting from zero for the 4th and last time...

## dawiepoolman | 2018-10-07T20:25:58+00:00
(gdb) bt
#0  0x009368b0 in mdb_rpage_get ()
#1  0x00937f92 in mdb_page_get.isra ()
#2  0x009392ce in mdb_page_search_root ()
#3  0x0093952c in mdb_page_search ()
#4  0x00939970 in mdb_cursor_set ()
#5  0x009389e2 in mdb_cursor_get ()
#6  0x007d7eb8 in cryptonote::BlockchainLMDB::get_block_blob_from_height[abi:cxx11](unsigned long long const&) const ()
#7  0x007c0484 in cryptonote::BlockchainDB::get_block_from_height(unsigned long long const&) const ()
#8  0x0095976a in cryptonote::HardFork::rescan_from_block_height(unsigned long long) ()
#9  0x0095a758 in cryptonote::HardFork::init() ()
#10 0x007f89fe in cryptonote::Blockchain::init(cryptonote::BlockchainDB*, cryptonote::network_type, bool, cryptonote::test_options const*) ()
#11 0x00809f0e in cryptonote::core::init(boost::program_options::variables_map const&, char const*, cryptonote::test_options const*) ()
#12 0x00681d08 in daemonize::t_core::run() ()
#13 0x0066f760 in daemonize::t_daemon::run(bool) ()
#14 0x006cda74 in daemonize::t_executor::run_interactive(boost::program_options::variables_map const&) ()
#15 0x006d1b46 in bool daemonizer::daemonize<daemonize::t_executor>(int, char const**, daemonize::t_executor&&, boost::program_options::variables_map const&) ()
#16 0x00652e66 in main ()
(gdb)


## dawiepoolman | 2018-10-07T20:41:50+00:00
running for the 4th time from block 0 with:

./bin/monero-v0.12.3.0/monerod --rpc-bind-ip=192.168.1.10 --rpc-bind-port=4008 --confirm-external-bind --max-concurrency 1 --block-sync-size 20

## glv2 | 2018-10-07T21:39:56+00:00
If you see the problem again, you should try the ```dmesg``` command to check if the kernel detected hardware errors that could explain database corruptions.


## dawiepoolman | 2018-10-08T04:50:39+00:00
Next error

2018-10-08 00:15:24.542 [P2P8]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171    [107.10.255.62:18080 OUT]  Synced 92332/1678034
2018-10-08 00:16:10.535 [P2P8]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171    [107.10.255.62:18080 OUT]  Synced 92352/1678035
2018-10-08 00:16:11.194 [P2P8]  ERROR   blockchain      src/cryptonote_core/blockchain.cpp:3585 Error adding block with hash: <a26ca19719a37d4a9891833462dba509403cf202b7cd8f13fab6610b978f7895> to blockchain, what = Error adding spent key image to db transaction: Cannot allocate memory
2018-10-08 00:16:14.847 [P2P8]  ERROR   blockchain      src/cryptonote_core/blockchain.cpp:3585 Error adding block with hash: <a26ca19719a37d4a9891833462dba509403cf202b7cd8f13fab6610b978f7895> to blockchain, what = Attempting to add transaction that's already in the db (tx id 172038)
2018-10-08 00:16:15.059 [P2P8]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:310     [14.215.45.243:18080 OUT] Sync data returned a new top block candidate: 92352 -> 1678036 [Your node is 1585684 blocks (1565 days) behind]
SYNCHRONIZATION started
2018-10-08 00:16:49.660 [P2P8]  ERROR   blockchain      src/cryptonote_core/blockchain.cpp:3585 Error adding block with hash: <a26ca19719a37d4a9891833462dba509403cf202b7cd8f13fab6610b978f7895> to blockchain, what = Attempting to add transaction that's already in the db (tx id 172038)
2018-10-08 00:17:26.624 [P2P2]  WARN    net.dns src/common/dns_utils.cpp:508    WARNING: no two valid MoneroPulse DNS checkpoint records were received
2018-10-08 00:17:26.837 [P2P2]  ERROR   blockchain      src/cryptonote_core/blockchain.cpp:3585 Error adding block with hash: <a26ca19719a37d4a9891833462dba509403cf202b7cd8f13fab6610b978f7895> to blockchain, what = Attempting to add transaction that's already in the db (tx id 172038)
2018-10-08 00:17:53.068 [P2P2]  ERROR   blockchain      src/cryptonote_core/blockchain.cpp:3585 Error adding block with hash: <a26ca19719a37d4a9891833462dba509403cf202b7cd8f13fab6610b978f7895> to blockchain, what = Attempting to add transaction that's already in the db (tx id 172038)
2018-10-08 00:18:20.734 [P2P4]  ERROR   blockchain      src/cryptonote_core/blockchain.cpp:3585 Error adding block with hash: <a26ca19719a37d4a9891833462dba509403cf202b7cd8f13fab6610b978f7895> to blockchain, what = Attempting to add transaction that's already in the db (tx id 172038)
2018-10-08 00:18:32.383 [P2P3]  ERROR   blockchain      src/cryptonote_core/blockchain.cpp:3585 Error adding block with hash: <a26ca19719a37d4a9891833462dba509403cf202b7cd8f13fab6610b978f7895> to blockchain, what = Attempting to add transaction that's already in the db (tx id 172038)
2018-10-08 00:18:40.511 [P2P4]  ERROR   blockchain      src/cryptonote_core/blockchain.cpp:3585 Error adding block with hash: <a26ca19719a37d4a9891833462dba509403cf202b7cd8f13fab6610b978f7895> to blockchain, what = Attempting to add transaction that's already in the db (tx id 172038)
2018-10-08 00:18:56.613 [P2P0]  ERROR   blockchain      src/cryptonote_core/blockchain.cpp:3585 Error adding block with hash: <a26ca19719a37d4a9891833462dba509403cf202b7cd8f13fab6610b978f7895> to blockchain, what = Attempting to add transaction that's already in the db (tx id 172038)
2018-10-08 00:19:12.158 [P2P0]  ERROR   blockchain      src/cryptonote_core/blockchain.cpp:3585 Error adding block with hash: <a26ca19719a37d4a9891833462dba509403cf202b7cd8f13fab6610b978f7895> to blockchain, what = Attempting to add transaction that's already in the db (tx id 172038)
2018-10-08 00:19:12.957 [P2P5]  ERROR   blockchain      src/cryptonote_core/blockchain.cpp:3585 Error adding block with hash: <a26ca19719a37d4a9891833462dba509403cf202b7cd8f13fab6610b978f7895> to blockchain, what = Attempting to add transaction that's already in the db (tx id 172038)
2018-10-08 00:19:14.385 [P2P2]  ERROR   blockchain      src/cryptonote_core/blockchain.cpp:3585 Error adding block with hash: <a26ca19719a37d4a9891833462dba509403cf202b7cd8f13fab6610b978f7895> to blockchain, what = Attempting to add transaction that's already in the db (tx id 172038)
2018-10-08 00:19:26.217 [P2P6]  ERROR   blockchain      src/cryptonote_core/blockchain.cpp:3585 Error adding block with hash: <a26ca19719a37d4a9891833462dba509403cf202b7cd8f13fab6610b978f7895> to blockchain, what = Attempting to add transaction that's already in the db (tx id 172038)
2018-10-08 00:19:46.066 [P2P6]  ERROR   blockchain      src/cryptonote_core/blockchain.cpp:3585 Error adding block with hash: <a26ca19719a37d4a9891833462dba509403cf202b7cd8f13fab6610b978f7895> to blockchain, what = Attempting to add transaction that's already in the db (tx id 172038)
2018-10-08 00:19:47.358 [P2P5]  ERROR   blockchain      src/cryptonote_core/blockchain.cpp:3585 Error adding block with hash: <a26ca19719a37d4a9891833462dba509403cf202b7cd8f13fab6610b978f7895> to blockchain, what = Attempting to add transaction that's already in the db (tx id 172038)
2018-10-08 00:20:00.974 [P2P3]  ERROR   blockchain      src/cryptonote_core/blockchain.cpp:3585 Error adding block with hash: <a26ca19719a37d4a9891833462dba509403cf202b7cd8f13fab6610b978f7895> to blockchain, what = Attempting to add transaction that's already in the db (tx id 172038)
2018-10-08 00:20:05.109 [P2P1]  ERROR   blockchain      src/cryptonote_core/blockchain.cpp:3585 Error adding block with hash: <a26ca19719a37d4a9891833462dba509403cf202b7cd8f13fab6610b978f7895> to blockchain, what = Attempting to add transaction that's already in the db (tx id 172038)
2018-10-08 00:20:27.419 [P2P2]  ERROR   blockchain      src/cryptonote_core/blockchain.cpp:3585 Error adding block with hash: <a26ca19719a37d4a9891833462dba509403cf202b7cd8f13fab6610b978f7895> to blockchain, what = Attempting to add transaction that's already in the db (tx id 172038)
2018-10-08 00:20:32.886 [P2P1]  ERROR   blockchain      src/cryptonote_core/blockchain.cpp:3585 Error adding block with hash: <a26ca19719a37d4a9891833462dba509403cf202b7cd8f13fab6610b978f7895> to blockchain, what = Attempting to add transaction that's already in the db (tx id 172038)
2018-10-08 00:20:59.767 [P2P8]  ERROR   blockchain      src/cryptonote_core/blockchain.cpp:3585 Error adding block with hash: <a26ca19719a37d4a9891833462dba509403cf202b7cd8f13fab6610b978f7895> to blockchain, what = Attempting to add transaction that's already in the db (tx id 172038)
2018-10-08 00:21:19.007 [P2P1]  ERROR   blockchain      src/cryptonote_core/blockchain.cpp:3585 Error adding block with hash: <a26ca19719a37d4a9891833462dba509403cf202b7cd8f13fab6610b978f7895> to blockchain, what = Attempting to add transaction that's already in the db (tx id 172038)
2018-10-08 00:21:20.236 [P2P7]  ERROR   blockchain      src/cryptonote_core/blockchain.cpp:3585 Error adding block with hash: <a26ca19719a37d4a9891833462dba509403cf202b7cd8f13fab6610b978f7895> to blockchain, what = Attempting to add transaction that's already in the db (tx id 172038)
*** Error in `./bin/monero-v0.12.3.0/monerod': free(): invalid next size (normal): 0x3f48fd38 ***
Aborted
pi@xmrpi:~ $



## dawiepoolman | 2018-10-08T04:50:47+00:00
pi@xmrpi:~ $ dmesg
[    0.000000] Booting Linux on physical CPU 0x0
[    0.000000] Linux version 4.14.70-v7+ (dc4@dc4-XPS13-9333) (gcc version 4.9.3 (crosstool-NG crosstool-ng-1.22.0-88-g8460611)) #1144 SMP Tue Sep 18 17:34:46 BST 2018
[    0.000000] CPU: ARMv7 Processor [410fd034] revision 4 (ARMv7), cr=10c5383d
[    0.000000] CPU: div instructions available: patching division code
[    0.000000] CPU: PIPT / VIPT nonaliasing data cache, VIPT aliasing instruction cache
[    0.000000] OF: fdt: Machine model: Raspberry Pi 3 Model B Plus Rev 1.3
[    0.000000] Memory policy: Data cache writealloc
[    0.000000] cma: Reserved 8 MiB at 0x3ac00000
[    0.000000] On node 0 totalpages: 242688
[    0.000000] free_area_init_node: node 0, pgdat 80c84f80, node_mem_map ba39f000
[    0.000000]   Normal zone: 2133 pages used for memmap
[    0.000000]   Normal zone: 0 pages reserved
[    0.000000]   Normal zone: 242688 pages, LIFO batch:31
[    0.000000] percpu: Embedded 17 pages/cpu @ba348000 s38720 r8192 d22720 u69632
[    0.000000] pcpu-alloc: s38720 r8192 d22720 u69632 alloc=17*4096
[    0.000000] pcpu-alloc: [0] 0 [0] 1 [0] 2 [0] 3
[    0.000000] Built 1 zonelists, mobility grouping on.  Total pages: 240555
[    0.000000] Kernel command line: 8250.nr_uarts=0 bcm2708_fb.fbwidth=656 bcm2708_fb.fbheight=416 bcm2708_fb.fbswap=1 vc_mem.mem_base=0x3ec00000 vc_mem.mem_size=0x40000000  dwc_otg.lpm_enable=0 console=ttyS0,115200 console=tty1 root=PARTUUID=d82c22c1-b686-43fe-9749-68ea4720ac83 rootfstype=ext4 elevator=deadline fsck.repair=yes rootwait
[    0.000000] PID hash table entries: 4096 (order: 2, 16384 bytes)
[    0.000000] Dentry cache hash table entries: 131072 (order: 7, 524288 bytes)
[    0.000000] Inode-cache hash table entries: 65536 (order: 6, 262144 bytes)
[    0.000000] Memory: 940228K/970752K available (7168K kernel code, 575K rwdata, 2076K rodata, 1024K init, 706K bss, 22332K reserved, 8192K cma-reserved)
[    0.000000] Virtual kernel memory layout:
                   vector  : 0xffff0000 - 0xffff1000   (   4 kB)
                   fixmap  : 0xffc00000 - 0xfff00000   (3072 kB)
                   vmalloc : 0xbb800000 - 0xff800000   (1088 MB)
                   lowmem  : 0x80000000 - 0xbb400000   ( 948 MB)
                   modules : 0x7f000000 - 0x80000000   (  16 MB)
                     .text : 0x80008000 - 0x80800000   (8160 kB)
                     .init : 0x80b00000 - 0x80c00000   (1024 kB)
                     .data : 0x80c00000 - 0x80c8fe8c   ( 576 kB)
                      .bss : 0x80c96f10 - 0x80d478b0   ( 707 kB)
[    0.000000] SLUB: HWalign=64, Order=0-3, MinObjects=0, CPUs=4, Nodes=1
[    0.000000] ftrace: allocating 25276 entries in 75 pages
[    0.000000] Hierarchical RCU implementation.
[    0.000000] NR_IRQS: 16, nr_irqs: 16, preallocated irqs: 16
[    0.000000] arch_timer: cp15 timer(s) running at 19.20MHz (phys).
[    0.000000] clocksource: arch_sys_counter: mask: 0xffffffffffffff max_cycles: 0x46d987e47, max_idle_ns: 440795202767 ns
[    0.000007] sched_clock: 56 bits at 19MHz, resolution 52ns, wraps every 4398046511078ns
[    0.000022] Switching to timer-based delay loop, resolution 52ns
[    0.000274] Console: colour dummy device 80x30
[    0.000814] console [tty1] enabled
[    0.000850] Calibrating delay loop (skipped), value calculated using timer frequency.. 38.40 BogoMIPS (lpj=192000)
[    0.000890] pid_max: default: 32768 minimum: 301
[    0.001218] Mount-cache hash table entries: 2048 (order: 1, 8192 bytes)
[    0.001251] Mountpoint-cache hash table entries: 2048 (order: 1, 8192 bytes)
[    0.002207] Disabling memory control group subsystem
[    0.002301] CPU: Testing write buffer coherency: ok
[    0.002728] CPU0: thread -1, cpu 0, socket 0, mpidr 80000000
[    0.003145] Setting up static identity map for 0x100000 - 0x10003c
[    0.003284] Hierarchical SRCU implementation.
[    0.003982] smp: Bringing up secondary CPUs ...
[    0.004779] CPU1: thread -1, cpu 1, socket 0, mpidr 80000001
[    0.005624] CPU2: thread -1, cpu 2, socket 0, mpidr 80000002
[    0.006448] CPU3: thread -1, cpu 3, socket 0, mpidr 80000003
[    0.006552] smp: Brought up 1 node, 4 CPUs
[    0.006624] SMP: Total of 4 processors activated (153.60 BogoMIPS).
[    0.006645] CPU: All CPU(s) started in HYP mode.
[    0.006663] CPU: Virtualization extensions available.
[    0.007557] devtmpfs: initialized
[    0.017715] random: get_random_u32 called from bucket_table_alloc+0xfc/0x24c with crng_init=0
[    0.018387] VFP support v0.3: implementor 41 architecture 3 part 40 variant 3 rev 4
[    0.018630] clocksource: jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 19112604462750000 ns
[    0.018674] futex hash table entries: 1024 (order: 4, 65536 bytes)
[    0.019248] pinctrl core: initialized pinctrl subsystem
[    0.020044] NET: Registered protocol family 16
[    0.022650] DMA: preallocated 1024 KiB pool for atomic coherent allocations
[    0.027375] hw-breakpoint: found 5 (+1 reserved) breakpoint and 4 watchpoint registers.
[    0.027407] hw-breakpoint: maximum watchpoint size is 8 bytes.
[    0.027619] Serial: AMBA PL011 UART driver
[    0.029274] bcm2835-mbox 3f00b880.mailbox: mailbox enabled
[    0.029744] uart-pl011 3f201000.serial: could not find pctldev for node /soc/gpio@7e200000/uart0_pins, deferring probe
[    0.061002] bcm2835-dma 3f007000.dma: DMA legacy API manager at bb813000, dmachans=0x1
[    0.062437] SCSI subsystem initialized
[    0.062676] usbcore: registered new interface driver usbfs
[    0.062746] usbcore: registered new interface driver hub
[    0.062848] usbcore: registered new device driver usb
[    0.070085] raspberrypi-firmware soc:firmware: Attached to firmware from 2018-09-10 17:26
[    0.071388] clocksource: Switched to clocksource arch_sys_counter
[    0.148670] VFS: Disk quotas dquot_6.6.0
[    0.148782] VFS: Dquot-cache hash table entries: 1024 (order 0, 4096 bytes)
[    0.148985] FS-Cache: Loaded
[    0.149196] CacheFiles: Loaded
[    0.158046] NET: Registered protocol family 2
[    0.158783] TCP established hash table entries: 8192 (order: 3, 32768 bytes)
[    0.158912] TCP bind hash table entries: 8192 (order: 4, 65536 bytes)
[    0.159115] TCP: Hash tables configured (established 8192 bind 8192)
[    0.159259] UDP hash table entries: 512 (order: 2, 16384 bytes)
[    0.159321] UDP-Lite hash table entries: 512 (order: 2, 16384 bytes)
[    0.159564] NET: Registered protocol family 1
[    0.160037] RPC: Registered named UNIX socket transport module.
[    0.160061] RPC: Registered udp transport module.
[    0.160080] RPC: Registered tcp transport module.
[    0.160099] RPC: Registered tcp NFSv4.1 backchannel transport module.
[    0.161405] NOHZ: local_softirq_pending 80
[    0.161645] hw perfevents: enabled with armv7_cortex_a7 PMU driver, 7 counters available
[    0.164347] workingset: timestamp_bits=14 max_order=18 bucket_order=4
[    0.172250] FS-Cache: Netfs 'nfs' registered for caching
[    0.172866] NFS: Registering the id_resolver key type
[    0.172914] Key type id_resolver registered
[    0.172934] Key type id_legacy registered
[    0.172963] nfs4filelayout_init: NFSv4 File Layout Driver Registering...
[    0.174895] Block layer SCSI generic (bsg) driver version 0.4 loaded (major 251)
[    0.175051] io scheduler noop registered
[    0.175073] io scheduler deadline registered (default)
[    0.175361] io scheduler cfq registered
[    0.175383] io scheduler mq-deadline registered
[    0.175403] io scheduler kyber registered
[    0.177671] BCM2708FB: allocated DMA memory fad00000
[    0.177715] BCM2708FB: allocated DMA channel 0 @ bb813000
[    0.186248] Console: switching to colour frame buffer device 82x26
[    0.194607] bcm2835-rng 3f104000.rng: hwrng registered
[    0.197065] vc-mem: phys_addr:0x00000000 mem_base=0x3ec00000 mem_size:0x40000000(1024 MiB)
[    0.202217] vc-sm: Videocore shared memory driver
[    0.204804] gpiomem-bcm2835 3f200000.gpiomem: Initialised: Registers at 0x3f200000
[    0.218927] brd: module loaded
[    0.229745] loop: module loaded
[    0.232072] Loading iSCSI transport class v2.0-870.
[    0.235039] libphy: Fixed MDIO Bus: probed
[    0.237410] usbcore: registered new interface driver lan78xx
[    0.239741] usbcore: registered new interface driver smsc95xx
[    0.241933] dwc_otg: version 3.00a 10-AUG-2012 (platform bus)
[    0.271990] dwc_otg 3f980000.usb: base=0xf0980000
[    0.401386] NOHZ: local_softirq_pending 80
[    0.421386] NOHZ: local_softirq_pending 80
[    0.441385] NOHZ: local_softirq_pending 80
[    0.461386] NOHZ: local_softirq_pending 80
[    0.474396] Core Release: 2.80a
[    0.476410] Setting default values for core params
[    0.478445] Finished setting default values for core params
[    0.680698] Using Buffer DMA mode
[    0.682639] Periodic Transfer Interrupt Enhancement - disabled
[    0.684567] Multiprocessor Interrupt Enhancement - disabled
[    0.686497] OTG VER PARAM: 0, OTG VER FLAG: 0
[    0.688358] Dedicated Tx FIFOs mode
[    0.690446] WARN::dwc_otg_hcd_init:1046: FIQ DMA bounce buffers: virt = 0xbad14000 dma = 0xfad14000 len=9024
[    0.694318] FIQ FSM acceleration enabled for :
               Non-periodic Split Transactions
               Periodic Split Transactions
               High-Speed Isochronous Endpoints
               Interrupt/Control Split Transaction hack enabled
[    0.704010] dwc_otg: Microframe scheduler enabled
[    0.704066] WARN::hcd_init_fiq:459: FIQ on core 1 at 0x805e96c0
[    0.706082] WARN::hcd_init_fiq:460: FIQ ASM at 0x805e9a28 length 36
[    0.708076] WARN::hcd_init_fiq:486: MPHI regs_base at 0xf0006000
[    0.710178] dwc_otg 3f980000.usb: DWC OTG Controller
[    0.712368] dwc_otg 3f980000.usb: new USB bus registered, assigned bus number 1
[    0.714686] dwc_otg 3f980000.usb: irq 62, io mem 0x00000000
[    0.717003] Init: Port Power? op_state=1
[    0.719254] Init: Power Port (0)
[    0.721650] usb usb1: New USB device found, idVendor=1d6b, idProduct=0002
[    0.723959] usb usb1: New USB device strings: Mfr=3, Product=2, SerialNumber=1
[    0.726256] usb usb1: Product: DWC OTG Controller
[    0.728499] usb usb1: Manufacturer: Linux 4.14.70-v7+ dwc_otg_hcd
[    0.730772] usb usb1: SerialNumber: 3f980000.usb
[    0.733644] hub 1-0:1.0: USB hub found
[    0.735851] hub 1-0:1.0: 1 port detected
[    0.738429] dwc_otg: FIQ enabled
[    0.738434] dwc_otg: NAK holdoff enabled
[    0.738439] dwc_otg: FIQ split-transaction FSM enabled
[    0.738449] Module dwc_common_port init
[    0.738695] usbcore: registered new interface driver usb-storage
[    0.740978] mousedev: PS/2 mouse device common for all mice
[    0.743216] IR NEC protocol handler initialized
[    0.745385] IR RC5(x/sz) protocol handler initialized
[    0.747588] IR RC6 protocol handler initialized
[    0.749761] IR JVC protocol handler initialized
[    0.751853] IR Sony protocol handler initialized
[    0.753944] IR SANYO protocol handler initialized
[    0.756036] IR Sharp protocol handler initialized
[    0.758026] IR MCE Keyboard/mouse protocol handler initialized
[    0.760052] IR XMP protocol handler initialized
[    0.762728] bcm2835-wdt 3f100000.watchdog: Broadcom BCM2835 watchdog timer
[    0.765073] bcm2835-cpufreq: min=600000 max=1400000
[    0.767523] sdhci: Secure Digital Host Controller Interface driver
[    0.769650] sdhci: Copyright(c) Pierre Ossman
[    0.772108] mmc-bcm2835 3f300000.mmc: could not get clk, deferring probe
[    0.774585] sdhost-bcm2835 3f202000.mmc: could not get clk, deferring probe
[    0.776876] sdhci-pltfm: SDHCI platform and OF driver helper
[    0.780480] ledtrig-cpu: registered to indicate activity on CPUs
[    0.782898] hidraw: raw HID events driver (C) Jiri Kosina
[    0.785363] usbcore: registered new interface driver usbhid
[    0.787671] usbhid: USB HID core driver
[    0.790511] vchiq: vchiq_init_state: slot_zero = bad80000, is_master = 0
[    0.794248] [vc_sm_connected_init]: start
[    0.803017] [vc_sm_connected_init]: end - returning 0
[    0.805943] Initializing XFRM netlink socket
[    0.808325] NET: Registered protocol family 17
[    0.810779] Key type dns_resolver registered
[    0.813582] Registering SWP/SWPB emulation handler
[    0.816614] registered taskstats version 1
[    0.824955] uart-pl011 3f201000.serial: cts_event_workaround enabled
[    0.827519] 3f201000.serial: ttyAMA0 at MMIO 0x3f201000 (irq = 87, base_baud = 0) is a PL011 rev2
[    0.834276] mmc-bcm2835 3f300000.mmc: mmc_debug:0 mmc_debug2:0
[    0.836816] mmc-bcm2835 3f300000.mmc: DMA channel allocated
[    0.892013] sdhost: log_buf @ bad13000 (fad13000)
[    0.933043] mmc1: queuing unknown CIS tuple 0x80 (2 bytes)
[    0.937029] mmc1: queuing unknown CIS tuple 0x80 (3 bytes)
[    0.940892] mmc1: queuing unknown CIS tuple 0x80 (3 bytes)
[    0.945878] mmc1: queuing unknown CIS tuple 0x80 (7 bytes)
[    0.951513] Indeed it is in host mode hprt0 = 00021501
[    1.027731] random: fast init done
[    1.041434] mmc0: sdhost-bcm2835 loaded - DMA enabled (>1)
[    1.044528] of_cfs_init
[    1.046615] of_cfs_init: OK
[    1.049049] Waiting for root device PARTUUID=d82c22c1-b686-43fe-9749-68ea4720ac83...
[    1.071387] NOHZ: local_softirq_pending 80
[    1.098297] mmc1: new high speed SDIO card at address 0001
[    1.138400] mmc0: host does not support reading read-only switch, assuming write-enable
[    1.145568] mmc0: new high speed SDHC card at address 1388
[    1.148276] mmcblk0: mmc0:1388 USD00 29.5 GiB
[    1.151857]  mmcblk0: p1 p2
[    1.161436] usb 1-1: new high-speed USB device number 2 using dwc_otg
[    1.163773] Indeed it is in host mode hprt0 = 00001101
[    1.401653] usb 1-1: New USB device found, idVendor=0424, idProduct=2514
[    1.403937] usb 1-1: New USB device strings: Mfr=0, Product=0, SerialNumber=0
[    1.406832] hub 1-1:1.0: USB hub found
[    1.409294] hub 1-1:1.0: 4 ports detected
[    1.521406] NOHZ: local_softirq_pending 82
[    1.523812] NOHZ: local_softirq_pending 82
[    1.526125] NOHZ: local_softirq_pending 82
[    1.528343] NOHZ: local_softirq_pending 82
[    1.731422] usb 1-1.1: new high-speed USB device number 3 using dwc_otg
[    1.861609] usb 1-1.1: New USB device found, idVendor=0424, idProduct=2514
[    1.863889] usb 1-1.1: New USB device strings: Mfr=0, Product=0, SerialNumber=0
[    1.866557] hub 1-1.1:1.0: USB hub found
[    1.868797] hub 1-1.1:1.0: 3 ports detected
[    2.071470] Under-voltage detected! (0x00050005)
[    2.183703] dwc_otg_handle_wakeup_detected_intr lxstate = 2
[    2.571412] usb 1-1.1: reset high-speed USB device number 3 using dwc_otg
[    2.821613] usb 1-1.1: USB disconnect, device number 3
[    2.921413] usb 1-1.1: new high-speed USB device number 4 using dwc_otg
[    3.051619] usb 1-1.1: New USB device found, idVendor=0424, idProduct=2514
[    3.053742] usb 1-1.1: New USB device strings: Mfr=0, Product=0, SerialNumber=0
[    3.056293] hub 1-1.1:1.0: USB hub found
[    3.058365] hub 1-1.1:1.0: 3 ports detected
[    3.151420] usb 1-1.2: new high-speed USB device number 5 using dwc_otg
[    3.362279] usb 1-1.2: New USB device found, idVendor=1058, idProduct=25a2
[    3.364376] usb 1-1.2: New USB device strings: Mfr=1, Product=2, SerialNumber=3
[    3.366494] usb 1-1.2: Product: Elements 25A2
[    3.368652] usb 1-1.2: Manufacturer: Western Digital
[    3.370884] usb 1-1.2: SerialNumber: 57585631413538304A4C3558
[    3.373774] usb-storage 1-1.2:1.0: USB Mass Storage device detected
[    3.376594] scsi host0: usb-storage 1-1.2:1.0
[    3.931414] usb 1-1.1.1: new high-speed USB device number 6 using dwc_otg
[    4.061761] usb 1-1.1.1: New USB device found, idVendor=0424, idProduct=7800
[    4.064152] usb 1-1.1.1: New USB device strings: Mfr=0, Product=0, SerialNumber=0
[    4.336884] libphy: lan78xx-mdiobus: probed
[    4.391984] scsi 0:0:0:0: Direct-Access     WD       Elements 25A2    1021 PQ: 0 ANSI: 6
[    4.398672] sd 0:0:0:0: [sda] Spinning up disk...
[    5.431408] .
[    6.471408] .
[    7.511406] .
[    7.513791] ready
[    7.518228] sd 0:0:0:0: [sda] 3906963456 512-byte logical blocks: (2.00 TB/1.82 TiB)
[    7.522986] sd 0:0:0:0: [sda] Write Protect is off
[    7.525279] sd 0:0:0:0: [sda] Mode Sense: 47 00 10 08
[    7.525603] sd 0:0:0:0: [sda] No Caching mode page found
[    7.527835] sd 0:0:0:0: [sda] Assuming drive cache: write through
[    7.563766]  sda: sda1
[    7.567598] sd 0:0:0:0: [sda] Attached SCSI disk
[    7.805899] EXT4-fs (sda1): INFO: recovery required on readonly filesystem
[    7.808235] EXT4-fs (sda1): write access will be enabled during recovery
[    8.311464] Voltage normalised (0x00000000)
[    9.376310] random: crng init done
[   12.471465] Under-voltage detected! (0x00050005)
[   20.791468] Voltage normalised (0x00000000)
[   22.819313] EXT4-fs (sda1): recovery complete
[   22.829391] EXT4-fs (sda1): mounted filesystem with ordered data mode. Opts: (null)
[   22.833632] VFS: Mounted root (ext4 filesystem) readonly on device 8:1.
[   22.901122] devtmpfs: mounted
[   22.906358] Freeing unused kernel memory: 1024K
[   23.850413] systemd[1]: System time before build time, advancing clock.
[   24.197935] NET: Registered protocol family 10
[   24.201823] Segment Routing with IPv6
[   24.247749] ip_tables: (C) 2000-2006 Netfilter Core Team
[   24.340583] systemd[1]: systemd 232 running in system mode. (+PAM +AUDIT +SELINUX +IMA +APPARMOR +SMACK +SYSVINIT +UTMP +LIBCRYPTSETUP +GCRYPT +GNUTLS +ACL +XZ +LZ4 +SECCOMP +BLKID +ELFUTILS +KMOD +IDN)
[   24.349004] systemd[1]: Detected architecture arm.
[   24.398398] systemd[1]: Set hostname to <xmrpi>.
[   24.632108] systemd-fstab-generator[79]: Failed to create mount unit file /run/systemd/generator/-.mount, as it already exists. Duplicate entry in /etc/fstab?
[   24.700117] systemd[78]: /lib/systemd/system-generators/systemd-fstab-generator failed with error code 1.
[   25.222016] systemd[1]: Started Forward Password Requests to Wall Directory Watch.
[   25.231257] systemd[1]: Reached target Swap.
[   25.237663] systemd[1]: Listening on fsck to fsckd communication Socket.
[   25.244231] systemd[1]: Listening on Syslog Socket.
[   25.251256] systemd[1]: Set up automount Arbitrary Executable File Formats File System Automount Point.
[   25.261342] systemd[1]: Created slice System Slice.
[   34.057350] EXT4-fs (sda1): re-mounted. Opts: (null)
[   34.058712] EXT4-fs (sda1): re-mounted. Opts: (null)
[   34.156910] systemd-journald[100]: Received request to flush runtime journal from PID 1
[   35.060665] snd_bcm2835: module is from the staging directory, the quality is unknown, you have been warned.
[   35.066984] bcm2835_alsa bcm2835_alsa: card created with 8 channels
[   35.348754] sd 0:0:0:0: Attached scsi generic sg0 type 0
[   35.538117] brcmfmac: F1 signature read @0x18000000=0x15264345
[   35.545112] brcmfmac: brcmf_fw_map_chip_to_name: using brcm/brcmfmac43455-sdio.bin for chip 0x004345(17221) rev 0x000006
[   35.545971] usbcore: registered new interface driver brcmfmac
[   35.974418] brcmfmac: brcmf_c_preinit_dcmds: Firmware version = wl0: Feb 27 2018 03:15:32 version 7.45.154 (r684107 CY) FWID 01-4fbe0b04
[   35.975182] brcmfmac: brcmf_c_preinit_dcmds: CLM version = API: 12.2 Data: 9.10.105 Compiler: 1.29.4 ClmImport: 1.36.3 Creation: 2018-03-09 18:56:28
[   37.188682] uart-pl011 3f201000.serial: no DMA platform data
[   37.431590] Under-voltage detected! (0x00050005)
[   37.896748] IPv6: ADDRCONF(NETDEV_UP): wlan0: link is not ready
[   37.896794] brcmfmac: power management disabled
[   37.966128] Adding 2097148k swap on /var/swap.  Priority:-2 extents:5 across:2400252k FS
[   38.359809] IPv6: ADDRCONF(NETDEV_UP): eth0: link is not ready
[   41.258693] IPv6: ADDRCONF(NETDEV_CHANGE): wlan0: link becomes ready
[   43.844643] Bluetooth: Core ver 2.22
[   43.844723] NET: Registered protocol family 31
[   43.844729] Bluetooth: HCI device and connection manager initialized
[   43.844749] Bluetooth: HCI socket layer initialized
[   43.844762] Bluetooth: L2CAP socket layer initialized
[   43.844793] Bluetooth: SCO socket layer initialized
[   43.859761] Bluetooth: HCI UART driver ver 2.3
[   43.859775] Bluetooth: HCI UART protocol H4 registered
[   43.859781] Bluetooth: HCI UART protocol Three-wire (H5) registered
[   43.860001] Bluetooth: HCI UART protocol Broadcom registered
[   44.106714] Bluetooth: BNEP (Ethernet Emulation) ver 1.3
[   44.106734] Bluetooth: BNEP filters: protocol multicast
[   44.106764] Bluetooth: BNEP socket layer initialized
[   54.071475] Voltage normalised (0x00000000)
[  532.471230] rpi_firmware_get_throttled: 3 callbacks suppressed
[  532.471238] Under-voltage detected! (0x00050005)
[  538.711129] rpi_firmware_get_throttled: 3 callbacks suppressed
[  538.711135] Voltage normalised (0x00000000)
[  551.191140] Under-voltage detected! (0x00050005)
[  555.351127] Voltage normalised (0x00000000)
[  732.151059] Under-voltage detected! (0x00050005)
[  738.391010] Voltage normalised (0x00000000)
[  836.150977] Under-voltage detected! (0x00050005)
[  840.310944] Voltage normalised (0x00000000)
[  942.230905] Under-voltage detected! (0x00050005)
[  954.710861] Voltage normalised (0x00000000)
[  956.790898] Under-voltage detected! (0x00050005)
[  960.950848] Voltage normalised (0x00000000)
[ 1173.111419] rpi_firmware_get_throttled: 1 callbacks suppressed
[ 1173.111423] Voltage normalised (0x00000000)
[ 1175.191508] rpi_firmware_get_throttled: 2 callbacks suppressed
[ 1175.191515] Under-voltage detected! (0x00050005)
[ 1179.351470] Voltage normalised (0x00000000)
[ 1181.431496] Under-voltage detected! (0x00050005)
[ 1189.751502] Voltage normalised (0x00000000)
[ 1191.831543] Under-voltage detected! (0x00050005)
[ 1497.592757] rpi_firmware_get_throttled: 13 callbacks suppressed
[ 1497.592761] Voltage normalised (0x00000000)
[ 1499.672383] rpi_firmware_get_throttled: 13 callbacks suppressed
[ 1499.672391] Under-voltage detected! (0x00050005)
[ 1507.992309] Voltage normalised (0x00000000)
[ 1510.072380] Under-voltage detected! (0x00050005)
[ 1520.472329] Voltage normalised (0x00000000)
[ 1524.632388] Under-voltage detected! (0x00050005)
[ 1807.512556] rpi_firmware_get_throttled: 17 callbacks suppressed
[ 1807.512560] Voltage normalised (0x00000000)
[ 1811.672628] rpi_firmware_get_throttled: 17 callbacks suppressed
[ 1811.672636] Under-voltage detected! (0x00050005)
[ 1822.072571] Voltage normalised (0x00000000)
[ 1824.152578] Under-voltage detected! (0x00050005)
[ 1832.472521] Voltage normalised (0x00000000)
[ 1838.712625] Under-voltage detected! (0x00050005)
[ 2113.272715] rpi_firmware_get_throttled: 22 callbacks suppressed
[ 2113.272719] Voltage normalised (0x00000000)
[ 2117.432729] rpi_firmware_get_throttled: 22 callbacks suppressed
[ 2117.432736] Under-voltage detected! (0x00050005)
[ 2123.672749] Voltage normalised (0x00000000)
[ 2129.912809] Under-voltage detected! (0x00050005)
[ 2134.072718] Voltage normalised (0x00000000)
[ 2138.232812] Under-voltage detected! (0x00050005)
[ 2419.033072] rpi_firmware_get_throttled: 19 callbacks suppressed
[ 2419.033076] Voltage normalised (0x00000000)
[ 2421.113212] rpi_firmware_get_throttled: 19 callbacks suppressed
[ 2421.113236] Under-voltage detected! (0x00050005)
[ 2431.513076] Voltage normalised (0x00000000)
[ 2433.593132] Under-voltage detected! (0x00050005)
[ 2450.233102] Voltage normalised (0x00000000)
[ 2452.313199] Under-voltage detected! (0x00050005)
[ 2720.633326] rpi_firmware_get_throttled: 16 callbacks suppressed
[ 2720.633331] Voltage normalised (0x00000000)
[ 2724.793393] rpi_firmware_get_throttled: 16 callbacks suppressed
[ 2724.793401] Under-voltage detected! (0x00050005)
[ 2739.353341] Voltage normalised (0x00000000)
[ 2741.433321] Under-voltage detected! (0x00050005)
[ 2745.593312] Voltage normalised (0x00000000)
[ 2751.833430] Under-voltage detected! (0x00050005)
[ 3038.873532] rpi_firmware_get_throttled: 14 callbacks suppressed
[ 3038.873540] Under-voltage detected! (0x00050005)
[ 3051.353506] rpi_firmware_get_throttled: 15 callbacks suppressed
[ 3051.353511] Voltage normalised (0x00000000)
[ 3053.433501] Under-voltage detected! (0x00050005)
[ 3057.593503] Voltage normalised (0x00000000)
[ 3059.673568] Under-voltage detected! (0x00050005)
[ 3063.833478] Voltage normalised (0x00000000)
[ 3342.553659] rpi_firmware_get_throttled: 16 callbacks suppressed
[ 3342.553666] Under-voltage detected! (0x00050005)
[ 3350.873690] Under-voltage detected! (0x00050005)
[ 3357.113641] rpi_firmware_get_throttled: 17 callbacks suppressed
[ 3357.113645] Voltage normalised (0x00000000)
[ 3359.193713] Under-voltage detected! (0x00050005)
[ 3365.433630] Voltage normalised (0x00000000)
[ 3384.153700] Voltage normalised (0x00000000)
[ 3644.153771] rpi_firmware_get_throttled: 18 callbacks suppressed
[ 3644.153777] Under-voltage detected! (0x00050005)
[ 3691.993807] rpi_firmware_get_throttled: 17 callbacks suppressed
[ 3691.993812] Voltage normalised (0x00000000)
[ 3694.073881] Under-voltage detected! (0x00050005)
[ 3700.313804] Voltage normalised (0x00000000)
[ 3708.633814] Under-voltage detected! (0x00050005)
[ 3712.793778] Voltage normalised (0x00000000)
[ 3970.714044] rpi_firmware_get_throttled: 9 callbacks suppressed
[ 3970.714054] Under-voltage detected! (0x00050005)
[ 4035.193989] rpi_firmware_get_throttled: 9 callbacks suppressed
[ 4035.193996] Voltage normalised (0x00000000)
[ 4039.354014] Under-voltage detected! (0x00050005)
[ 4051.833897] Voltage normalised (0x00000000)
[ 4055.993941] Under-voltage detected! (0x00050005)
[ 4083.033934] Voltage normalised (0x00000000)
[ 4272.314256] rpi_firmware_get_throttled: 10 callbacks suppressed
[ 4272.314264] Under-voltage detected! (0x00050005)
[ 4282.714330] Under-voltage detected! (0x00050005)
[ 4297.274287] Under-voltage detected! (0x00050005)
[ 4343.034372] rpi_firmware_get_throttled: 13 callbacks suppressed
[ 4343.034378] Voltage normalised (0x00000000)
[ 4351.354364] Voltage normalised (0x00000000)
[ 4401.274457] Voltage normalised (0x00000000)
[ 4575.994745] rpi_firmware_get_throttled: 9 callbacks suppressed
[ 4575.994752] Under-voltage detected! (0x00050005)
[ 4592.634851] Under-voltage detected! (0x00050005)
[ 4652.954878] Under-voltage detected! (0x00050005)
[ 4657.114828] rpi_firmware_get_throttled: 8 callbacks suppressed
[ 4657.114833] Voltage normalised (0x00000000)
[ 4707.034902] Voltage normalised (0x00000000)
[ 4725.754976] Voltage normalised (0x00000000)
[ 4912.955226] rpi_firmware_get_throttled: 7 callbacks suppressed
[ 4912.955235] Under-voltage detected! (0x00050005)
[ 4927.515139] Under-voltage detected! (0x00050005)
[ 4973.275256] Under-voltage detected! (0x00050005)
[ 4977.435297] rpi_firmware_get_throttled: 7 callbacks suppressed
[ 4977.435305] Voltage normalised (0x00000000)
[ 4987.835235] Voltage normalised (0x00000000)
[ 5052.315254] Voltage normalised (0x00000000)
[ 5233.275478] rpi_firmware_get_throttled: 8 callbacks suppressed
[ 5233.275485] Under-voltage detected! (0x00050005)
[ 5254.075495] Under-voltage detected! (0x00050005)
[ 5316.475501] Under-voltage detected! (0x00050005)
[ 5326.875501] rpi_firmware_get_throttled: 8 callbacks suppressed
[ 5326.875506] Voltage normalised (0x00000000)
[ 5358.075526] Voltage normalised (0x00000000)
[ 5376.795553] Voltage normalised (0x00000000)
[ 5545.275745] rpi_firmware_get_throttled: 6 callbacks suppressed
[ 5545.275752] Under-voltage detected! (0x00050005)
[ 5578.555784] Under-voltage detected! (0x00050005)
[ 5651.355813] Under-voltage detected! (0x00050005)
[ 5655.515873] rpi_firmware_get_throttled: 6 callbacks suppressed
[ 5655.515879] Voltage normalised (0x00000000)
[ 5711.675797] Voltage normalised (0x00000000)
[ 5724.156423] Voltage normalised (0x00000000)
[ 5855.195913] rpi_firmware_get_throttled: 5 callbacks suppressed
[ 5855.195920] Under-voltage detected! (0x00050005)
[ 5907.195943] Under-voltage detected! (0x00050005)
[ 5915.515949] Under-voltage detected! (0x00050005)
[ 5973.755999] rpi_firmware_get_throttled: 7 callbacks suppressed
[ 5973.756005] Voltage normalised (0x00000000)
[ 5979.996007] Voltage normalised (0x00000000)
[ 5988.316050] Voltage normalised (0x00000000)
[ 6175.516153] rpi_firmware_get_throttled: 11 callbacks suppressed
[ 6175.516172] Under-voltage detected! (0x00050005)
[ 6198.396154] Under-voltage detected! (0x00050005)
[ 6225.436169] Under-voltage detected! (0x00050005)
[ 6277.436199] rpi_firmware_get_throttled: 11 callbacks suppressed
[ 6277.436205] Voltage normalised (0x00000000)
[ 6300.316212] Voltage normalised (0x00000000)
[ 6319.036232] Voltage normalised (0x00000000)
[ 6481.276348] rpi_firmware_get_throttled: 13 callbacks suppressed
[ 6481.276355] Under-voltage detected! (0x00050005)
[ 6518.716431] Under-voltage detected! (0x00050005)
[ 6533.276379] Under-voltage detected! (0x00050005)
[ 6616.476425] rpi_firmware_get_throttled: 13 callbacks suppressed
[ 6616.476432] Voltage normalised (0x00000000)
[ 6639.356439] Voltage normalised (0x00000000)
[ 6649.756419] Voltage normalised (0x00000000)
[ 6795.356578] rpi_firmware_get_throttled: 11 callbacks suppressed
[ 6795.356585] Under-voltage detected! (0x00050005)
[ 6801.596699] Under-voltage detected! (0x00050005)
[ 6818.236626] Under-voltage detected! (0x00050005)
[ 6945.116653] rpi_firmware_get_throttled: 15 callbacks suppressed
[ 6945.116660] Voltage normalised (0x00000000)
[ 6965.916668] Voltage normalised (0x00000000)
[ 6982.556685] Voltage normalised (0x00000000)
[ 7123.996791] rpi_firmware_get_throttled: 13 callbacks suppressed
[ 7123.996799] Under-voltage detected! (0x00050005)
[ 7182.236828] Under-voltage detected! (0x00050005)
[ 7209.276835] Under-voltage detected! (0x00050005)
[ 7267.516971] rpi_firmware_get_throttled: 10 callbacks suppressed
[ 7267.516977] Voltage normalised (0x00000000)
[ 7273.756966] Voltage normalised (0x00000000)
[ 7331.997191] Voltage normalised (0x00000000)
[ 7431.837354] rpi_firmware_get_throttled: 8 callbacks suppressed
[ 7431.837361] Under-voltage detected! (0x00050005)
[ 7442.237353] Under-voltage detected! (0x00050005)
[ 7506.717492] Under-voltage detected! (0x00050005)
[ 7583.678462] rpi_firmware_get_throttled: 6 callbacks suppressed
[ 7583.678468] Voltage normalised (0x00000000)
[ 7654.397768] Voltage normalised (0x00000000)
[ 7718.877810] Voltage normalised (0x00000000)
[ 7733.437855] rpi_firmware_get_throttled: 4 callbacks suppressed
[ 7733.437861] Under-voltage detected! (0x00050005)
[ 7750.077867] Under-voltage detected! (0x00050005)
[ 7802.077992] Under-voltage detected! (0x00050005)
[ 7960.158147] rpi_firmware_get_throttled: 6 callbacks suppressed
[ 7960.158153] Voltage normalised (0x00000000)
[ 7972.638182] Voltage normalised (0x00000000)
[ 8003.838220] Voltage normalised (0x00000000)
[ 8097.438344] rpi_firmware_get_throttled: 6 callbacks suppressed
[ 8097.438351] Under-voltage detected! (0x00050005)
[ 8124.478405] Under-voltage detected! (0x00050005)
[ 8147.358412] Under-voltage detected! (0x00050005)
[ 8274.238565] rpi_firmware_get_throttled: 8 callbacks suppressed
[ 8274.238572] Voltage normalised (0x00000000)
[ 8290.878570] Voltage normalised (0x00000000)
[ 8301.278573] Voltage normalised (0x00000000)
[ 8423.998745] rpi_firmware_get_throttled: 13 callbacks suppressed
[ 8423.998753] Under-voltage detected! (0x00050005)
[ 8444.798736] Under-voltage detected! (0x00050005)
[ 8513.438824] Under-voltage detected! (0x00050005)
[ 8575.838805] rpi_firmware_get_throttled: 9 callbacks suppressed
[ 8575.838808] Voltage normalised (0x00000000)
[ 8598.718892] Voltage normalised (0x00000000)
[ 8640.318915] Voltage normalised (0x00000000)
[ 8725.599059] rpi_firmware_get_throttled: 7 callbacks suppressed
[ 8725.599066] Under-voltage detected! (0x00050005)
[ 8742.239104] Under-voltage detected! (0x00050005)
[ 8802.559120] Under-voltage detected! (0x00050005)
[ 8966.879301] rpi_firmware_get_throttled: 7 callbacks suppressed
[ 8966.879307] Voltage normalised (0x00000000)
[ 8973.119240] Voltage normalised (0x00000000)
[ 8983.519254] Voltage normalised (0x00000000)
[ 9027.199308] rpi_firmware_get_throttled: 6 callbacks suppressed
[ 9027.199315] Under-voltage detected! (0x00050005)
[ 9060.479345] Under-voltage detected! (0x00050005)
[ 9068.799345] Under-voltage detected! (0x00050005)
[ 9272.639537] rpi_firmware_get_throttled: 14 callbacks suppressed
[ 9272.639556] Voltage normalised (0x00000000)
[ 9318.399606] Voltage normalised (0x00000000)
[ 9411.999670] rpi_firmware_get_throttled: 10 callbacks suppressed
[ 9411.999690] Under-voltage detected! (0x00050005)
[ 9422.399691] Voltage normalised (0x00000000)
[ 9466.079747] Under-voltage detected! (0x00050005)
[ 9476.479812] Under-voltage detected! (0x00050005)
[ 9580.479825] rpi_firmware_get_throttled: 7 callbacks suppressed
[ 9580.479831] Voltage normalised (0x00000000)
[ 9622.079867] Voltage normalised (0x00000000)
[ 9647.039894] Voltage normalised (0x00000000)
[ 9715.679970] rpi_firmware_get_throttled: 10 callbacks suppressed
[ 9715.679978] Under-voltage detected! (0x00050005)
[ 9734.400003] Under-voltage detected! (0x00050005)
[ 9767.680019] Under-voltage detected! (0x00050005)
[ 9904.960161] rpi_firmware_get_throttled: 8 callbacks suppressed
[ 9904.960166] Voltage normalised (0x00000000)
[ 9915.360135] Voltage normalised (0x00000000)
[ 9921.600159] Voltage normalised (0x00000000)
[10073.440295] rpi_firmware_get_throttled: 8 callbacks suppressed
[10073.440302] Under-voltage detected! (0x00050005)
[10092.160368] Under-voltage detected! (0x00050005)
[10100.480319] Under-voltage detected! (0x00050005)
[10231.520431] rpi_firmware_get_throttled: 10 callbacks suppressed
[10231.520437] Voltage normalised (0x00000000)
[10246.080449] Voltage normalised (0x00000000)
[10296.000494] Voltage normalised (0x00000000)
[10385.440588] rpi_firmware_get_throttled: 10 callbacks suppressed
[10385.440596] Under-voltage detected! (0x00050005)
[10395.840576] Under-voltage detected! (0x00050005)
[10435.360629] Under-voltage detected! (0x00050005)
[10535.200669] rpi_firmware_get_throttled: 8 callbacks suppressed
[10535.200687] Voltage normalised (0x00000000)
[10553.920728] Voltage normalised (0x00000000)
[10562.240689] Voltage normalised (0x00000000)
[10693.280824] rpi_firmware_get_throttled: 11 callbacks suppressed
[10693.280832] Under-voltage detected! (0x00050005)
[10718.240841] Under-voltage detected! (0x00050005)
[10730.720853] Under-voltage detected! (0x00050005)
[10845.120943] rpi_firmware_get_throttled: 10 callbacks suppressed
[10845.120949] Voltage normalised (0x00000000)
[10868.000980] Voltage normalised (0x00000000)
[10890.880983] Voltage normalised (0x00000000)
[11009.441087] rpi_firmware_get_throttled: 8 callbacks suppressed
[11009.441093] Under-voltage detected! (0x00050005)
[11032.321145] Under-voltage detected! (0x00050005)
[11092.641179] Under-voltage detected! (0x00050005)
[11163.361213] rpi_firmware_get_throttled: 8 callbacks suppressed
[11163.361219] Voltage normalised (0x00000000)
[11194.561241] Voltage normalised (0x00000000)
[11207.041252] Voltage normalised (0x00000000)
[11321.441545] rpi_firmware_get_throttled: 10 callbacks suppressed
[11321.441565] Under-voltage detected! (0x00050005)
[11363.041424] Under-voltage detected! (0x00050005)
[11379.681403] Under-voltage detected! (0x00050005)
[11498.241539] rpi_firmware_get_throttled: 10 callbacks suppressed
[11498.241545] Voltage normalised (0x00000000)
[11548.161573] Voltage normalised (0x00000000)
[11566.881577] Voltage normalised (0x00000000)
[11627.201716] rpi_firmware_get_throttled: 7 callbacks suppressed
[11627.201725] Under-voltage detected! (0x00050005)
[11635.521638] Under-voltage detected! (0x00050005)
[11670.881663] Under-voltage detected! (0x00050005)
[11849.761837] rpi_firmware_get_throttled: 10 callbacks suppressed
[11849.761843] Voltage normalised (0x00000000)
[11866.401838] Voltage normalised (0x00000000)
[11880.961861] Voltage normalised (0x00000000)
[11941.281977] rpi_firmware_get_throttled: 10 callbacks suppressed
[11941.281985] Under-voltage detected! (0x00050005)
[12007.841964] Under-voltage detected! (0x00050005)
[12018.241983] Under-voltage detected! (0x00050005)
[12190.882128] rpi_firmware_get_throttled: 10 callbacks suppressed
[12190.882134] Voltage normalised (0x00000000)
[12207.522158] Voltage normalised (0x00000000)
[12220.002171] Voltage normalised (0x00000000)
[12251.202203] rpi_firmware_get_throttled: 9 callbacks suppressed
[12251.202210] Under-voltage detected! (0x00050005)
[12263.682202] Under-voltage detected! (0x00050005)
[12296.962219] Under-voltage detected! (0x00050005)
[12519.522436] rpi_firmware_get_throttled: 10 callbacks suppressed
[12519.522442] Voltage normalised (0x00000000)
[12532.002450] Voltage normalised (0x00000000)
[12579.842583] rpi_firmware_get_throttled: 8 callbacks suppressed
[12579.842591] Under-voltage detected! (0x00050005)
[12590.242496] Voltage normalised (0x00000000)
[12608.962513] Under-voltage detected! (0x00050005)
[12658.882559] Under-voltage detected! (0x00050005)
[12827.362713] rpi_firmware_get_throttled: 7 callbacks suppressed
[12827.362720] Voltage normalised (0x00000000)
[12846.082740] Voltage normalised (0x00000000)
[12860.642751] Voltage normalised (0x00000000)
[12883.522764] rpi_firmware_get_throttled: 8 callbacks suppressed
[12883.522770] Under-voltage detected! (0x00050005)
[12900.162819] Under-voltage detected! (0x00050005)
[12914.722897] Under-voltage detected! (0x00050005)
[13137.282987] rpi_firmware_get_throttled: 15 callbacks suppressed
[13137.282993] Voltage normalised (0x00000000)
[13147.682999] Voltage normalised (0x00000000)
[13164.323012] Voltage normalised (0x00000000)
[13208.003051] rpi_firmware_get_throttled: 17 callbacks suppressed
[13208.003058] Under-voltage detected! (0x00050005)
[13222.563069] Under-voltage detected! (0x00050005)
[13251.683127] Under-voltage detected! (0x00050005)
[13443.043238] rpi_firmware_get_throttled: 11 callbacks suppressed
[13443.043243] Voltage normalised (0x00000000)
[13459.683223] Voltage normalised (0x00000000)
[13480.483232] Voltage normalised (0x00000000)
[13530.403365] rpi_firmware_get_throttled: 10 callbacks suppressed
[13530.403372] Under-voltage detected! (0x00050005)
[13567.843331] Under-voltage detected! (0x00050005)
[13584.483299] Under-voltage detected! (0x00050005)
[13759.203396] rpi_firmware_get_throttled: 10 callbacks suppressed
[13759.203400] Voltage normalised (0x00000000)
[13777.923391] Voltage normalised (0x00000000)
[13834.083546] rpi_firmware_get_throttled: 8 callbacks suppressed
[13834.083553] Under-voltage detected! (0x00050005)
[13852.803471] Voltage normalised (0x00000000)
[13873.603467] Under-voltage detected! (0x00050005)
[13884.003498] Under-voltage detected! (0x00050005)
[14075.363681] rpi_firmware_get_throttled: 11 callbacks suppressed
[14075.363701] Voltage normalised (0x00000000)
[14087.843576] Voltage normalised (0x00000000)
[14106.563646] Voltage normalised (0x00000000)
[14179.363677] rpi_firmware_get_throttled: 13 callbacks suppressed
[14179.363698] Under-voltage detected! (0x00050005)
[14200.163790] Under-voltage detected! (0x00050005)
[14218.883874] Under-voltage detected! (0x00050005)
[14397.763862] rpi_firmware_get_throttled: 14 callbacks suppressed
[14397.763868] Voltage normalised (0x00000000)
[14422.723885] Voltage normalised (0x00000000)
[14431.043884] Voltage normalised (0x00000000)
[14495.523940] rpi_firmware_get_throttled: 17 callbacks suppressed
[14495.523947] Under-voltage detected! (0x00050005)
[14514.243989] Under-voltage detected! (0x00050005)
[14543.364028] Under-voltage detected! (0x00050005)
[14707.684093] rpi_firmware_get_throttled: 19 callbacks suppressed
[14707.684098] Voltage normalised (0x00000000)
[14722.244117] Voltage normalised (0x00000000)
[14734.724130] Voltage normalised (0x00000000)
[14799.204156] rpi_firmware_get_throttled: 20 callbacks suppressed
[14799.204163] Under-voltage detected! (0x00050005)
[14815.844153] Under-voltage detected! (0x00050005)
[14828.324178] Under-voltage detected! (0x00050005)
[24787.373946] rpi_firmware_get_throttled: 5 callbacks suppressed
[24787.373953] Under-voltage detected! (0x00050005)
[24799.853955] rpi_firmware_get_throttled: 13 callbacks suppressed
[24799.853960] Voltage normalised (0x00000000)
[25041.134137] Under-voltage detected! (0x00050005)
[25047.374130] Voltage normalised (0x00000000)
[25059.854152] Under-voltage detected! (0x00050005)
[25066.094156] Voltage normalised (0x00000000)
[27231.376636] Under-voltage detected! (0x00050005)
[27241.776628] Voltage normalised (0x00000000)
[27264.656670] Under-voltage detected! (0x00050005)
[27268.816667] Voltage normalised (0x00000000)
[28930.738253] Under-voltage detected! (0x00050005)
[28934.898255] Voltage normalised (0x00000000)
[29305.138638] Under-voltage detected! (0x00050005)
[29309.298948] Voltage normalised (0x00000000)
[30652.979724] Under-voltage detected! (0x00050005)
[30659.219728] Voltage normalised (0x00000000)
[30665.460114] Under-voltage detected! (0x00050005)
[30673.779736] Voltage normalised (0x00000000)
[30675.859759] Under-voltage detected! (0x00050005)
[30696.659773] Voltage normalised (0x00000000)
pi@xmrpi:~ $


## dawiepoolman | 2018-10-08T04:51:25+00:00
Maybe the RPi is too weak to power the 2TB ext hdd?

## dawiepoolman | 2018-10-08T05:04:21+00:00
I have an output of 5V 3A Power supply

## dawiepoolman | 2018-10-08T05:05:45+00:00
Should I consider getting a SSD HD instead? They are probably more power efficient

## dawiepoolman | 2018-10-08T14:07:41+00:00
Ok, so I ordered a powered USB hub after checking out some Raspberry Pi forums.  Lets see if some more external power solves the reliability issue of the HDD.  
I will keep this issue updated on my progress so that other Pi node operators can learn from my potholes.

## dawiepoolman | 2018-10-10T04:35:29+00:00
So I think we cracked this one on reddit..
seemed like we should set
**max_usb_current=1** in boot config file to ensure enough current gets supplied to the HDD

Still syncing stable now..

## moneromooo-monero | 2018-10-10T09:56:39+00:00
Very good find :)

## dawiepoolman | 2018-10-10T10:02:07+00:00
Kudos to reddit user u/shermand100 for amazing perseverance and patience with an unusual symptoms and to @glv2 for the dmesg suggestion.  
It all culminated into a very good learning.
And to you @moneromooo-monero for always being involved and helping out too.  My learning curve has exploded since I started following your work.


## moneromooo-monero | 2018-10-10T15:36:31+00:00
Can you give a command that adds that setting to the boot file (ie, echo "max_usb_current=1" >> /etc/someconfig") which I can add to the README ? 

## hyc | 2018-10-10T16:05:47+00:00
I never even knew that was possible. Can't imagine it's good for the longevity of the Pi. Simple low-tech solution is just to get a USB Y-cable, and plug an external USB power supply in to give the drive enough juice.

## dawiepoolman | 2018-10-10T16:30:22+00:00
@moneromooo-monero 
I ran command:
> sudo nano /boot/config.txt

and then I added the setting to the config file:
> max_usb_current=1

@hyc we discussed the Y splitter cable and powered usb hub alternatives as well on [r/pinode](https://old.reddit.com/r/pinode/comments/9m3522/pi_swapdrive_corrupt/e7fp29n/)
TL;DR; the Y cable is not *ideal* and now not even the extra powered usb hub is really needed anymore it seems.

The pi is now running stable for a day already at temp=68.8'C which is below the max threshold of 80'C even without an extra cooling fan which I think is badass :P

## moneromooo-monero | 2018-10-10T16:47:53+00:00
Thanks, it's now in https://github.com/monero-project/monero/pull/4553

## hyc | 2018-10-13T16:12:06+00:00
Relying on the Pi to supply enough power by itself is a mistake. If there's extra CPU or network activity, it won't have enough juice for your HDD.

## dawiepoolman | 2018-10-13T16:17:10+00:00
Since my last post I received the powered usb hub.  I will plug that into the Pi for at least the period of catching up the initial sync.  It can only help carry the load indeed.

# Action History
- Created by: dawiepoolman | 2018-10-06T14:40:52+00:00
- Closed at: 2018-10-10T16:51:57+00:00
