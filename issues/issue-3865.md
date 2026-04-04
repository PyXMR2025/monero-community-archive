---
title: It takes a long time to send a tx, just send it.It's not waiting for confirmation.
source_url: https://github.com/monero-project/monero/issues/3865
author: wwaayyaa
assignees: []
labels: []
created_at: '2018-05-26T08:55:56+00:00'
updated_at: '2018-05-28T14:02:30+00:00'
type: issue
status: closed
closed_at: '2018-05-28T12:54:49+00:00'
---

# Original Description
[version 0.12.0.0]

when i send a tx, cli or rpc always take long time.I don't even know about the transaction.

use of cli:
```
[wallet 442zNf]: transfer ..address.. ..amount..
                 // maybe waiting 2~5 minutes
Wallet password:
No payment id is included with this transaction. Is this okay?  (Y/Yes/N/No): y
		// always waiting 30~60 minute, very terrible
Transaction 1/1:
Spending from address index 0
Sending 10.091929848267.  The transaction fee is 0.010173520000
Is this okay?  (Y/Yes/N/No): y

		//and then there's no problem

```


use of rpc : 

```
[2018-05-26 08:30:26] production.INFO: requestWallet -> {"method":"transfer","params":{"destinations":[{"amount":1086941032289,"address":"44tLjmXrQNrWJ5NBsEj2R77ZBEgDa3fEe9GLpSf2FRmhexPvfYDUAB7EXX1Hdb3aMQ9FLqdJ56yaAhiXoRsceGJCRS3Jxkn"}],"payment_id":"05b451c37d536a34bdd2a0f63bbfef1e1598980c13d61fbbcf6aaba9bcd11dc2","mixin":0,"priority":0,"get_tx_key":true},"endpoint":"http://xxx.xxx.xxx.xxx:88888/json_rpc"}
[2018-05-26 08:33:26] production.ERROR: transfer error:cURL error 28: Operation timed out after 180001 milliseconds with 0 bytes received (see http://curl.haxx.se/libcurl/c/libcurl-errors.html)
Waiting for data... 
```

now , I don't know the state of the transaction at this time. Show_transfers can not be seen in cli.

Who can give me some suggestions to help me increase the speed of sending transactions?





# Discussion History
## wwaayyaa | 2018-05-26T09:42:29+00:00
I found out that there is 0.12.1 version. Will it be better after upgrading?

## dEBRUYNE-1 | 2018-05-26T09:47:47+00:00
>I found out that there is 0.12.1 version. Will it be better after upgrading?

Presumably. 

## lyntrd99 | 2018-05-26T10:45:31+00:00
I also had this issue with 0.12.0
Now with 0.12.1 (compiled from source) the confirmation request is immediate. I have noticed a marked improvement.

## wwaayyaa | 2018-05-26T13:43:35+00:00
clone github.......
checkout v0.12.1.0
make

Sad, I am already 0.12.1.0 version now, but I still have to wait for a long time.



## wwaayyaa | 2018-05-26T14:07:55+00:00
![image](https://user-images.githubusercontent.com/6279538/40576971-e07ab42e-6130-11e8-8666-6b544b34cd02.png)
Look, I'm waiting for two of my wallet . It has been 20 minutes. ```sweep``` or ```transfer``` is the same.

## moneromooo-monero | 2018-05-26T14:08:11+00:00
If you're running 0.12.1.0 and still have this problem:
- make sure you're REALLY running 0.12.1.0
- if you are, then wait for this to happen, then run (use the correct path for your system): gdb /path/to/monerod \`pidof monerod\`
- then, in gdb: thread apply all bt
- post the multi-page result here
- also paste the result of the "version" command in monerod


## wwaayyaa | 2018-05-26T14:17:28+00:00
```
(gdb) thread apply all bt

Thread 26 (Thread 0x7f5b419f8700 (LWP 22952)):
#0  0x00007f5b55b14593 in ?? () from /lib/x86_64-linux-gnu/libc.so.6
#1  0x0000000000000000 in ?? ()

Thread 25 (Thread 0x7f5b411f7700 (LWP 22951)):
#0  0x00007f5b55b14593 in ?? () from /lib/x86_64-linux-gnu/libc.so.6
#1  0x0000000000000000 in ?? ()

Thread 24 (Thread 0x7f5b409f6700 (LWP 22950)):
#0  0x00007f5b55b14593 in ?? () from /lib/x86_64-linux-gnu/libc.so.6
#1  0x0000000000000000 in ?? ()

Thread 23 (Thread 0x7f5b515fd700 (LWP 22949)):
#0  0x00007f5b55b14593 in ?? () from /lib/x86_64-linux-gnu/libc.so.6
#1  0x0000000000000000 in ?? ()

Thread 22 (Thread 0x7f5b426fa700 (LWP 22804)):
#0  __lll_lock_wait () at ../sysdeps/unix/sysv/linux/x86_64/lowlevellock.S:135
#1  0x00007f5b55deae42 in __GI___pthread_mutex_lock (mutex=0x55648a06a278)
#2  0x00005564888de6d4 in cryptonote::tx_memory_pool::get_transaction(crypto::hash const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&) const ()
#3  0x000055648882ae86 in cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::handle_notify_new_fluffy_block(int, cryptonote::NOTIFY_NEW_FLUFFY_BLOCK::request&, cryptonote::cryptonote_connection_context&) ()
#4  0x00005564886c2d09 in int epee::net_utils::buff_to_t_adapter<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, cryptonote::NOTIFY_NEW_FLUFFY_BLOCK::request, cryptonote::cryptonote_connection_context, boost::_bi::bind_t<int, boost::_mfi::mf3<int, cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, int, cryptonote::NOTIFY_NEW_FLUFFY_BLOCK::request&, cryptonote::cryptonote_connection_context&>, boost::_bi::list4<boost::_bi::value<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*>, boost::arg<1>, boost::arg<2>, boost::arg<3> > > >(cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, boost::_bi::bind_t<int, boost::_mfi::mf3<int, cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, int, cryptonote::NOTIFY_NEW_FLUFFY_BLOCK::request&, cryptonote::cryptonote_connection_context&>, boost::_bi::list4<boost::_bi::value<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*>, boost::arg<1>, boost::arg<2>, boost::arg<3> > >, cryptonote::cryptonote_connection_context&) ()
#5  0x00005564886c3cfb in int cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::handle_invoke_map<cryptonote::cryptonote_connection_context>(bool, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&, cryptonote::cryptonote_connection_context&, bool&) ()
#6  0x00005564886c3e32 in int nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::handle_invoke_map<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >(bool, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&, bool&) ()
#7  0x00005564886c4200 in nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::notify(int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&) ()
#8  0x000055648884514d in epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >::handle_recv(void const*, unsigned long) ()
#9  0x000055648885d088 in epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::handle_read(boost::system::error_code const&, unsigned long) ()
#10 0x0000556488825d9a in void boost::asio::detail::strand_service::dispatch<boost::asio::detail::binder2<boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::system::error_code, unsigned long> >(boost::asio::detail::strand_service::strand_impl*&, boost::asio::detail::binder2<boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::system::error_code, unsigned long>&) ()
#11 0x0000556488826208 in boost::asio::detail::completion_handler<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > > >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) ()
#12 0x00005564888265f6 in void boost::asio::detail::strand_service::dispatch<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > > >(boost::asio::detail::strand_service::strand_impl*&, boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin[0/189]_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boos
t::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::crypto
note_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodeto
ol::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > >&) ()
#13 0x00005564888268d3 in boost::asio::detail::reactive_socket_recv_op<boost::asio::mutable_buffers_1, boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost:
:_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsign
ed long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context
> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running> >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operatio
n*, boost::system::error_code const&, unsigned long) ()
#14 0x0000556488643424 in boost::asio::detail::epoll_reactor::descriptor_state::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_cod
e const&, unsigned long) ()
#15 0x000055648880a6b4 in epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread() ()
#16 0x00007f5b565a75d5 in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0
#17 0x00007f5b55de86ba in start_thread (arg=0x7f5b426fa700) at pthread_create.c:333
#18 0x00007f5b55b1e3dd in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:74
#19 0x0000000000000000 in ?? ()

Thread 21 (Thread 0x7f5b42bfb700 (LWP 22803)):
#0  __lll_lock_wait () at ../sysdeps/unix/sysv/linux/x86_64/lowlevellock.S:135
#1  0x00007f5b55deae42 in __GI___pthread_mutex_lock (mutex=0x55648a06a278) at ../nptl/pthread_mutex_lock.c:115
#2  0x00005564888de6d4 in cryptonote::tx_memory_pool::get_transaction(crypto::hash const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&) const ()
#3  0x000055648882ae86 in cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::handle_notify_new_fluffy_block(int, cryptonote::NOTIFY_NEW_FLUFFY_BLOCK::request&, cryptonote::cryptonote_connection_
context&) ()
#4  0x00005564886c2d09 in int epee::net_utils::buff_to_t_adapter<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, cryptonote::NOTIFY_NEW_FLUFFY_BLOCK::request, cryptonote::cryptonote_connectio
n_context, boost::_bi::bind_t<int, boost::_mfi::mf3<int, cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, int, cryptonote::NOTIFY_NEW_FLUFFY_BLOCK::request&, cryptonote::cryptonote_connection_
context&>, boost::_bi::list4<boost::_bi::value<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*>, boost::arg<1>, boost::arg<2>, boost::arg<3> > > >(cryptonote::t_cryptonote_protocol_handler<cr
yptonote::core>*, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, boost::_bi::bind_t<int, boost::_mfi::mf3<int, cryptonote::t_cryptonote_protocol_handler<crypt
onote::core>, int, cryptonote::NOTIFY_NEW_FLUFFY_BLOCK::request&, cryptonote::cryptonote_connection_context&>, boost::_bi::list4<boost::_bi::value<cryptonote::t_cryptonote_protocol_handler<cryptonote::cor
e>*>, boost::arg<1>, boost::arg<2>, boost::arg<3> > >, cryptonote::cryptonote_connection_context&) ()
#5  0x00005564886c3cfb in int cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::handle_invoke_map<cryptonote::cryptonote_connection_context>(bool, int, std::__cxx11::basic_string<char, std::cha
r_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&, cryptonote::cryptonote_connection_context&, bool&) ()
#6  0x00005564886c3e32 in int nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::handle_invoke_map<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_co
ntext> >(bool, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&, nodetool::p2p_
connection_context_t<cryptonote::cryptonote_connection_context>&, bool&) ()
#7  0x00005564886c4200 in nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::notify(int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > c
onst&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&) ()
#8  0x000055648884514d in epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >::handle_recv(void const*, unsigned long) ()
#9  0x000055648885d088 in epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::handle_read(boost::system::erro
r_code const&, unsigned long) ()
#10 0x0000556488825d9a in void boost::asio::detail::strand_service::dispatch<boost::asio::detail::binder2<boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_pro
tocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epe
e::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::systext_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > >&) ()
#13 0x00005564888268d3 in boost::asio::detail::reactive_socket_recv_op<boost::asio::mutable_buffers_1, boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running> >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) ()
#14 0x0000556488643424 in boost::asio::detail::epoll_reactor::descriptor_state::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) ()
#15 0x000055648880a6b4 in epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread() ()
#16 0x00007f5b565a75d5 in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0
#17 0x00007f5b55de86ba in start_thread (arg=0x7f5b426fa700) at pthread_create.c:333
#18 0x00007f5b55b1e3dd in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:74
#19 0x0000000000000000 in ?? ()

Thread 21 (Thread 0x7f5b42bfb700 (LWP 22803)):
#0  __lll_lock_wait () at ../sysdeps/unix/sysv/linux/x86_64/lowlevellock.S:135
#1  0x00007f5b55deae42 in __GI___pthread_mutex_lock (mutex=0x55648a06a278) at ../nptl/pthread_mutex_lock.c:115
#2  0x00005564888de6d4 in cryptonote::tx_memory_pool::get_transaction(crypto::hash const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&) const ()
#3  0x000055648882ae86 in cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::handle_notify_new_fluffy_block(int, cryptonote::NOTIFY_NEW_FLUFFY_BLOCK::request&, cryptonote::cryptonote_connection_context&) ()
#4  0x00005564886c2d09 in int epee::net_utils::buff_to_t_adapter<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, cryptonote::NOTIFY_NEW_FLUFFY_BLOCK::request, cryptonote::cryptonote_connection_context, boost::_bi::bind_t<int, boost::_mfi::mf3<int, cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, int, cryptonote::NOTIFY_NEW_FLUFFY_BLOCK::request&, cryptonote::cryptonote_connection_context&>, boost::_bi::list4<boost::_bi::value<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*>, boost::arg<1>, boost::arg<2>, boost::arg<3> > > >(cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, boost::_bi::bind_t<int, boost::_mfi::mf3<int, cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, int, cryptonote::NOTIFY_NEW_FLUFFY_BLOCK::request&, cryptonote::cryptonote_connection_context&>, boost::_bi::list4<boost::_bi::value<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*>, boost::arg<1>, boost::arg<2>, boost::arg<3> > >, cryptonote::cryptonote_connection_context&) ()
#5  0x00005564886c3cfb in int cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::handle_invoke_map<cryptonote::cryptonote_connection_context>(bool, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&, cryptonote::cryptonote_connection_context&, bool&) ()
#6  0x00005564886c3e32 in int nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::handle_invoke_map<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >(bool, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&, bool&) ()
#7  0x00005564886c4200 in nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::notify(int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&) ()
#8  0x000055648884514d in epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >::handle_recv(void const*, unsigned long) ()
#9  0x000055648885d088 in epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::handle_read(boost::system::error_code const&, unsigned long) ()
#10 0x0000556488825d9a in void boost::asio::detail::strand_service::dispatch<boost::asio::detail::binder2<boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::system::error_code, unsigned long> >(boost::asio::detail::strand_service::strand_impl*&, boost::asio::detail::binder2<boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::system::error_code, unsigned long>&) ()
#11 0x0000556488826208 in boost::asio::detail::completion_handler<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > > >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) ()
#12 0x00005564888265f6 in void boost::asio::detail::strand_service::dispatch<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > > >(boost::asio::detail::strand_service::strand_impl*&, boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > >&) ()
#13 0x00005564888268d3 in boost::asio::detail::reactive_socket_recv_op<boost::asio::mutable_buffers_1, boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running> >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) ()
#14 0x0000556488643424 in boost::asio::detail::epoll_reactor::descriptor_state::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) ()
#15 0x000055648880a6b4 in epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread() ()
#16 0x00007f5b565a75d5 in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0
#17 0x00007f5b55de86ba in start_thread (arg=0x7f5b42bfb700) at pthread_create.c:333
#18 0x00007f5b55b1e3dd in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:74
#19 0x0000000000000000 in ?? ()

Thread 20 (Thread 0x7f5b430fc700 (LWP 22802)):
#0  __lll_lock_wait () at ../sysdeps/unix/sysv/linux/x86_64/lowlevellock.S:135
#1  0x00007f5b55deae42 in __GI___pthread_mutex_lock (mutex=0x55648a06a278) at ../nptl/pthread_mutex_lock.c:115
#2  0x00005564888de6d4 in cryptonote::tx_memory_pool::get_transaction(crypto::hash const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&) const ()
#3  0x000055648882ae86 in cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::handle_notify_new_fluffy_block(int, cryptonote::NOTIFY_NEW_FLUFFY_BLOCK::request&, cryptonote::cryptonote_connection_context&) ()
#4  0x00005564886c2d09 in int epee::net_utils::buff_to_t_adapter<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, cryptonote::NOTIFY_NEW_FLUFFY_BLOCK::request, cryptonote::cryptonote_connection_context, boost::_bi::bind_t<int, boost::_mfi::mf3<int, cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, int, cryptonote::NOTIFY_NEW_FLUFFY_BLOCK::request&, cryptonote::cryptonote_connection_context&>, boost::_bi::list4<boost::_bi::value<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*>, boost::arg<1>, boost::arg<2>, boost::arg<3> > > >(cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, boost::_bi::bind_t<int, boost::_mfi::mf3<int, cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, int, cryptonote::NOTIFY_NEW_FLUFFY_BLOCK::request&, cryptonote::cryptonote_connection_context&>, boost::_bi::list4<boost::_bi::value<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*>, boost::arg<1>, boost::arg<2>, boost::arg<3> > >, cryptonote::cryptonote_connection_context&) ()
#5  0x00005564886c3cfb in int cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::handle_invoke_map<cryptonote::cryptonote_connection_context>(bool, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&, cryptonote::cryptonote_connection_context&, bool&) ()
#6  0x00005564886c3e32 in int nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::handle_invoke_map<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >(bool, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&, bool&) ()
#7  0x00005564886c4200 in nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::notify(int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&) ()
#8  0x000055648884514d in epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >::handle_recv(void const*, unsigned long) ()
#9  0x000055648885d088 in epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::handle_read(boost::system::error_code const&, unsigned long) ()
#10 0x0000556488825d9a in void boost::asio::detail::strand_service::dispatch<boost::asio::detail::binder2<boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::system::error_code, unsigned long> >(boost::asio::detail::strand_service::strand_impl*&, boost::asio::detail::binder2<boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::system::error_code, unsigned long>&) ()
#11 0x0000556488826208 in boost::asio::detail::completion_handler<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > > >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) ()
#12 0x00005564888265f6 in void boost::asio::detail::strand_service::dispatch<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > > >(boost::asio::detail::strand_service::strand_impl*&, boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > >&) ()
#13 0x00005564888268d3 in boost::asio::detail::reactive_socket_recv_op<boost::asio::mutable_buffers_1, boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running> >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) ()
#14 0x0000556488643424 in boost::asio::detail::epoll_reactor::descriptor_state::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) ()
#15 0x000055648880a6b4 in epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread() ()
#16 0x00007f5b565a75d5 in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0
#17 0x00007f5b55de86ba in start_thread (arg=0x7f5b430fc700) at pthread_create.c:333
#18 0x00007f5b55b1e3dd in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:74
#19 0x0000000000000000 in ?? ()

Thread 19 (Thread 0x7f5b435fd700 (LWP 22801)):
#0  __lll_lock_wait () at ../sysdeps/unix/sysv/linux/x86_64/lowlevellock.S:135
#1  0x00007f5b55deae42 in __GI___pthread_mutex_lock (mutex=0x55648a06a278) at ../nptl/pthread_mutex_lock.c:115
#2  0x00005564888de6d4 in cryptonote::tx_memory_pool::get_transaction(crypto::hash const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&) const ()
#3  0x000055648882ae86 in cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::handle_notify_new_fluffy_block(int, cryptonote::NOTIFY_NEW_FLUFFY_BLOCK::request&, cryptonote::cryptonote_connection_context&) ()
#4  0x00005564886c2d09 in int epee::net_utils::buff_to_t_adapter<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, cryptonote::NOTIFY_NEW_FLUFFY_BLOCK::request, cryptonote::cryptonote_connection_context, boost::_bi::bind_t<int, boost::_mfi::mf3<int, cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, int, cryptonote::NOTIFY_NEW_FLUFFY_BLOCK::request&, cryptonote::cryptonote_connection_context&>, boost::_bi::list4<boost::_bi::value<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*>, boost::arg<1>, boost::arg<2>, boost::arg<3> > > >(cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, boost::_bi::bind_t<int, boost::_mfi::mf3<int, cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, int, cryptonote::NOTIFY_NEW_FLUFFY_BLOCK::request&, cryptonote::cryptonote_connection_context&>, boost::_bi::list4<boost::_bi::value<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*>, boost::arg<1>, boost::arg<2>, boost::arg<3> > >, cryptonote::cryptonote_connection_context&) ()
#5  0x00005564886c3cfb in int cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::handle_invoke_map<cryptonote::cryptonote_connection_context>(bool, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&, cryptonote::cryptonote_connection_context&, bool&) ()
#6  0x00005564886c3e32 in int nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::handle_invoke_map<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >(bool, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&, bool&) ()
#7  0x00005564886c4200 in nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::notify(int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&) ()
#8  0x000055648884514d in epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >::handle_recv(void const*, unsigned long) ()
#9  0x000055648885d088 in epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::handle_read(boost::system::error_code const&, unsigned long) ()
#10 0x0000556488825d9a in void boost::asio::detail::strand_service::dispatch<boost::asio::detail::binder2<boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::system::error_code, unsigned long> >(boost::asio::detail::strand_service::strand_impl*&, boost::asio::detail::binder2<boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::system::error_code, unsigned long>&) ()
#11 0x0000556488826208 in boost::asio::detail::completion_handler<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > > >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) ()
#12 0x00005564888265f6 in void boost::asio::detail::strand_service::dispatch<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > > >(boost::asio::detail::strand_service::strand_impl*&, boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > >&) ()
#13 0x00005564888268d3 in boost::asio::detail::reactive_socket_recv_op<boost::asio::mutable_buffers_1, boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running> >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) ()
#14 0x0000556488643424 in boost::asio::detail::epoll_reactor::descriptor_state::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) ()
#15 0x000055648880a6b4 in epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread() ()
#16 0x00007f5b565a75d5 in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0
#17 0x00007f5b55de86ba in start_thread (arg=0x7f5b435fd700) at pthread_create.c:333
#18 0x00007f5b55b1e3dd in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:74
#19 0x0000000000000000 in ?? ()
``` 
Is that all? Thank you。  @moneromooo-monero 

## wwaayyaa | 2018-05-26T14:39:10+00:00
./monerod --p2p-bind-ip=0.0.0.0 --p2p-bind-port=18080 --rpc-bind-ip=0.0.0.0 --rpc-bind-port=18081 --non-interactive --confirm-external-bind  --data-dir /work/monero-data/monero --config-file /work/monero-data/config.conf --log-level 0
2018-05-26 13:03:15.086     7f5b5878d780        INFO    global  src/daemon/main.cpp:279 Monero 'Lithium Luna' (v0.12.1.0-master-release)


## moneromooo-monero | 2018-05-26T16:04:06+00:00
18 threads are missing. Of the ones shown here, none are stuck in RPC. Some are waiting to process a new block, so it's likely one of them at least is stuck in RPC.


## wwaayyaa | 2018-05-26T16:21:27+00:00
try agin

## cli
[wallet 442zNf]: sweep_all 442zNfHF32k2YgmAv4ZUVpd47T7cF7jxk6K8WqvEuQkn73mnhuLm5X5HkJVWrxSyfwYTrSWznJ1N7RJAb5PMAMR8GKd2za5
Wallet password:
No payment id is included with this transaction. Is this okay?  (Y/Yes/N/No): y
// now waiting

## gdb  
```
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
pthread_cond_wait@@GLIBC_2.3.2 () at ../sysdeps/unix/sysv/linux/x86_64/pthread_cond_wait.S:185
185     ../sysdeps/unix/sysv/linux/x86_64/pthread_cond_wait.S: No such file or directory.
(gdb) thread apply all bt

Thread 26 (Thread 0x7fa65f7fe700 (LWP 23983)):
#0  0x00007fbc0a3d85d3 in select () at ../sysdeps/unix/syscall-template.S:84
#1  0x00007fbc0b9f928c in ?? () from /usr/lib/x86_64-linux-gnu/libunbound.so.2
#2  0x00007fbc0b9cbcc7 in ?? () from /usr/lib/x86_64-linux-gnu/libunbound.so.2
#3  0x00007fbc0b9e25cd in ub_resolve () from /usr/lib/x86_64-linux-gnu/libunbound.so.2
#4  0x000055ae9e8938ad in tools::DNSResolver::get_record(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, int, std::__cxx11::basic_string<char, std::char_traits<char
>, std::allocator<char> > (*)(char const*, unsigned long), bool&, bool&) ()
#5  0x000055ae9e893b1e in tools::DNSResolver::get_txt_record(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, bool&, bool&) ()
#6  0x000055ae9e895697 in boost::detail::thread_data<tools::dns_utils::load_txt_records_from_dns(std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator
<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > >&, std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::__cx
x11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > const&)::{lambda()#1}>::run() ()
#7  0x00007fbc0ae6b5d5 in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0
#8  0x00007fbc0a6ac6ba in start_thread (arg=0x7fa65f7fe700) at pthread_create.c:333
#9  0x00007fbc0a3e241d in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109
Thread 25 (Thread 0x7fa694b0c700 (LWP 23981)):
#0  0x00007fbc0a3d85d3 in select () at ../sysdeps/unix/syscall-template.S:84
#1  0x00007fbc0b9f928c in ?? () from /usr/lib/x86_64-linux-gnu/libunbound.so.2
#2  0x00007fbc0b9cbcc7 in ?? () from /usr/lib/x86_64-linux-gnu/libunbound.so.2
#3  0x00007fbc0b9e25cd in ub_resolve () from /usr/lib/x86_64-linux-gnu/libunbound.so.2
#4  0x000055ae9e8938ad in tools::DNSResolver::get_record(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > (*)(char const*, unsigned long), bool&, bool&) ()
#5  0x000055ae9e893b1e in tools::DNSResolver::get_txt_record(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, bool&, bool&) ()
#6  0x000055ae9e895697 in boost::detail::thread_data<tools::dns_utils::load_txt_records_from_dns(std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > >&, std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > const&)::{lambda()#1}>::run() ()
#7  0x00007fbc0ae6b5d5 in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0
#8  0x00007fbc0a6ac6ba in start_thread (arg=0x7fa694b0c700) at pthread_create.c:333
#9  0x00007fbc0a3e241d in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109

Thread 24 (Thread 0x7fa69530d700 (LWP 23980)):
#0  0x00007fbc0a3d85d3 in select () at ../sysdeps/unix/syscall-template.S:84
#1  0x00007fbc0b9f928c in ?? () from /usr/lib/x86_64-linux-gnu/libunbound.so.2
#2  0x00007fbc0b9cbcc7 in ?? () from /usr/lib/x86_64-linux-gnu/libunbound.so.2
#3  0x00007fbc0b9e25cd in ub_resolve () from /usr/lib/x86_64-linux-gnu/libunbound.so.2
#4  0x000055ae9e8938ad in tools::DNSResolver::get_record(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > (*)(char const*, unsigned long), bool&, bool&) ()
#5  0x000055ae9e893b1e in tools::DNSResolver::get_txt_record(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, bool&, bool&) ()
#6  0x000055ae9e895697 in boost::detail::thread_data<tools::dns_utils::load_txt_records_from_dns(std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > >&, std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > const&)::{lambda()#1}>::run() ()
#7  0x00007fbc0ae6b5d5 in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0
#8  0x00007fbc0a6ac6ba in start_thread (arg=0x7fa69530d700) at pthread_create.c:333
#9  0x00007fbc0a3e241d in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109

Thread 23 (Thread 0x7fa69580e700 (LWP 23966)):
#0  0x00007fbc0a3e2a13 in epoll_wait () at ../sysdeps/unix/syscall-template.S:84
#1  0x000055ae9e77f19d in epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread() ()
#2  0x00007fbc0ae6b5d5 in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0
#3  0x00007fbc0a6ac6ba in start_thread (arg=0x7fa69580e700) at pthread_create.c:333
#4  0x00007fbc0a3e241d in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109

Thread 22 (Thread 0x7fa695d0f700 (LWP 23965)):
#0  pthread_cond_wait@@GLIBC_2.3.2 () at ../sysdeps/unix/sysv/linux/x86_64/pthread_cond_wait.S:185
#1  0x000055ae9e77f609 in epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread() ()
#2  0x00007fbc0ae6b5d5 in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0
#3  0x00007fbc0a6ac6ba in start_thread (arg=0x7fa695d0f700) at pthread_create.c:333
#4  0x00007fbc0a3e241d in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109

Thread 21 (Thread 0x7fa696210700 (LWP 23964)):
#0  pthread_cond_wait@@GLIBC_2.3.2 () at ../sysdeps/unix/sysv/linux/x86_64/pthread_cond_wait.S:185
#1  0x000055ae9e77f609 in epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread() ()
#2  0x00007fbc0ae6b5d5 in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0
#3  0x00007fbc0a6ac6ba in start_thread (arg=0x7fa696210700) at pthread_create.c:333
#4  0x00007fbc0a3e241d in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109

Thread 20 (Thread 0x7fa696711700 (LWP 23963)):
#0  pthread_cond_wait@@GLIBC_2.3.2 () at ../sysdeps/unix/sysv/linux/x86_64/pthread_cond_wait.S:185
#1  0x000055ae9e77f609 in epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread() ()
#2  0x00007fbc0ae6b5d5 in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0
#3  0x00007fbc0a6ac6ba in start_thread (arg=0x7fa696711700) at pthread_create.c:333
#4  0x00007fbc0a3e241d in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109

Thread 19 (Thread 0x7fbbf46f6700 (LWP 23962)):
#0  pthread_cond_wait@@GLIBC_2.3.2 () at ../sysdeps/unix/sysv/linux/x86_64/pthread_cond_wait.S:185
#1  0x000055ae9e77f609 in epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread() ()
#2  0x00007fbc0ae6b5d5 in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0
#3  0x00007fbc0a6ac6ba in start_thread (arg=0x7fbbf46f6700) at pthread_create.c:333
#4  0x00007fbc0a3e241d in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109

Thread 18 (Thread 0x7fbbf4bf7700 (LWP 23961)):
#0  pthread_cond_wait@@GLIBC_2.3.2 () at ../sysdeps/unix/sysv/linux/x86_64/pthread_cond_wait.S:185
#1  0x000055ae9e77f609 in epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread() ()
#2  0x00007fbc0ae6b5d5 in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0
#3  0x00007fbc0a6ac6ba in start_thread (arg=0x7fbbf4bf7700) at pthread_create.c:333
#4  0x00007fbc0a3e241d in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109

Thread 17 (Thread 0x7fbbf50f8700 (LWP 23960)):
#0  pthread_cond_wait@@GLIBC_2.3.2 () at ../sysdeps/unix/sysv/linux/x86_64/pthread_cond_wait.S:185
#1  0x000055ae9e7bd56f in nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::do_handshake_with_peer(unsigned long&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&, bool) ()
#2  0x000055ae9e7cc5ae in nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::try_to_connect_and_handshake_with_new_peer(epee::net_utils::network_address const&, bool, unsigned long, nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::PeerType, unsigned long) ()
#3  0x000055ae9e7ce481 in nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::make_new_connection_from_peerlist(bool) ()
#4  0x000055ae9e7cec54 in nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::make_expected_connections_count(nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::PeerType, unsigned long) ()
#5  0x000055ae9e7cf641 in nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::connections_maker() ()
#6  0x000055ae9e767210 in nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::idle_worker() ()
#7  0x000055ae9e781897 in epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::global_timer_handler(boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext_base>) ()
#8  0x000055ae9e767a99 in boost::asio::detail::wait_handler<boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext_base> >, boost::_bi::list2<boost::_bi::value<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >*>, boost::_bi::value<boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext_base> > > > >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) ()
#9  0x000055ae9e77f6b4 in epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread() ()
#10 0x00007fbc0ae6b5d5 in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0
#11 0x00007fbc0a6ac6ba in start_thread (arg=0x7fbbf50f8700) at pthread_create.c:333
#12 0x00007fbc0a3e241d in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109

Thread 16 (Thread 0x7fbbf55f9700 (LWP 23959)):
#0  pthread_cond_wait@@GLIBC_2.3.2 () at ../sysdeps/unix/sysv/linux/x86_64/pthread_cond_wait.S:185
#1  0x000055ae9e77f609 in epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread() ()
#2  0x00007fbc0ae6b5d5 in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0
#3  0x00007fbc0a6ac6ba in start_thread (arg=0x7fbbf55f9700) at pthread_create.c:333
#4  0x00007fbc0a3e241d in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109

Thread 15 (Thread 0x7fbbf5afa700 (LWP 23958)):
#0  pthread_cond_wait@@GLIBC_2.3.2 () at ../sysdeps/unix/sysv/linux/x86_64/pthread_cond_wait.S:185
#1  0x00007fbc0ae6d043 in boost::thread::join_noexcept() () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0
#2  0x000055ae9e8963a7 in tools::dns_utils::load_txt_records_from_dns(std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > >&, std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > const&) ()
#3  0x000055ae9e8ae2c8 in tools::check_updates(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&) ()
#4  0x000055ae9e845dd8 in cryptonote::core::check_updates() ()
#5  0x000055ae9e84174c in cryptonote::core::on_idle() ()
#6  0x000055ae9e766ff9 in cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::on_idle() ()
#7  0x000055ae9e781897 in epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::global_timer_handler(boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext_base>) ()
#8  0x000055ae9e767a99 in boost::asio::detail::wait_handler<boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext_base> >, boost::_bi::list2<boost::_bi::value<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >*>, boost::_bi::value<boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext_base> > > > >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) ()
#9  0x000055ae9e77f6b4 in epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread() ()
#10 0x00007fbc0ae6b5d5 in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0
#11 0x00007fbc0a6ac6ba in start_thread (arg=0x7fbbf5afa700) at pthread_create.c:333
#12 0x00007fbc0a3e241d in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109

Thread 14 (Thread 0x7fbbf5ffb700 (LWP 23957)):
#0  pthread_cond_wait@@GLIBC_2.3.2 () at ../sysdeps/unix/sysv/linux/x86_64/pthread_cond_wait.S:185
#1  0x000055ae9e77f609 in epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread() ()
#2  0x00007fbc0ae6b5d5 in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0
#3  0x00007fbc0a6ac6ba in start_thread (arg=0x7fbbf5ffb700) at pthread_create.c:333
#4  0x00007fbc0a3e241d in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109

Thread 13 (Thread 0x7fbbf67fc700 (LWP 23956)):
#0  pthread_cond_timedwait@@GLIBC_2.3.2 () at ../sysdeps/unix/sysv/linux/x86_64/pthread_cond_timedwait.S:225
#1  0x00007fbc0ae6b7e2 in boost::this_thread::hiden::sleep_for(timespec const&) () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0
#2  0x000055ae9e770a4b in nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::run()::{lambda()#1}::operator()() const ()
#3  0x00007fbc0ae6b5d5 in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0
#4  0x00007fbc0a6ac6ba in start_thread (arg=0x7fbbf67fc700) at pthread_create.c:333
#5  0x00007fbc0a3e241d in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109

Thread 12 (Thread 0x7fbbf6ffd700 (LWP 23955)):
#0  0x00007fbc0a3d674d in poll () at ../sysdeps/unix/syscall-template.S:84
#1  0x00007fbc0be6312a in ?? () from /usr/lib/x86_64-linux-gnu/libzmq.so.5
#2  0x00007fbc0be4e176 in ?? () from /usr/lib/x86_64-linux-gnu/libzmq.so.5
#3  0x00007fbc0be643f1 in ?? () from /usr/lib/x86_64-linux-gnu/libzmq.so.5
#4  0x00007fbc0be64bd0 in ?? () from /usr/lib/x86_64-linux-gnu/libzmq.so.5
#5  0x00007fbc0be7aa09 in ?? () from /usr/lib/x86_64-linux-gnu/libzmq.so.5
#6  0x000055ae9e8c3c9f in cryptonote::rpc::ZmqServer::serve() ()
#7  0x00007fbc0ae6b5d5 in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0
#8  0x00007fbc0a6ac6ba in start_thread (arg=0x7fbbf6ffd700) at pthread_create.c:333
#9  0x00007fbc0a3e241d in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109

Thread 11 (Thread 0x7fbc056c0700 (LWP 23954)):
#0  0x00007fbc0a3e2a13 in epoll_wait () at ../sysdeps/unix/syscall-template.S:84
#1  0x00007fbc0be4a0ec in ?? () from /usr/lib/x86_64-linux-gnu/libzmq.so.5
#2  0x00007fbc0be757fa in ?? () from /usr/lib/x86_64-linux-gnu/libzmq.so.5
#3  0x00007fbc0a6ac6ba in start_thread (arg=0x7fbc056c0700) at pthread_create.c:333
#4  0x00007fbc0a3e241d in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109

Thread 10 (Thread 0x7fbc066c2700 (LWP 23953)):
#0  0x00007fbc0a3e2a13 in epoll_wait () at ../sysdeps/unix/syscall-template.S:84
#1  0x00007fbc0be4a0ec in ?? () from /usr/lib/x86_64-linux-gnu/libzmq.so.5
#2  0x00007fbc0be757fa in ?? () from /usr/lib/x86_64-linux-gnu/libzmq.so.5
#3  0x00007fbc0a6ac6ba in start_thread (arg=0x7fbc066c2700) at pthread_create.c:333
#4  0x00007fbc0a3e241d in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109

Thread 9 (Thread 0x7fbbf7fff700 (LWP 23952)):
#0  0x00007fbc0a3e2a13 in epoll_wait () at ../sysdeps/unix/syscall-template.S:84
#1  0x000055ae9e5c8971 in epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::worker_thread() ()
#2  0x00007fbc0ae6b5d5 in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0
#3  0x00007fbc0a6ac6ba in start_thread (arg=0x7fbbf7fff700) at pthread_create.c:333
#4  0x00007fbc0a3e241d in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109

Thread 8 (Thread 0x7fbbf77fe700 (LWP 23951)):
#0  pthread_cond_wait@@GLIBC_2.3.2 () at ../sysdeps/unix/sysv/linux/x86_64/pthread_cond_wait.S:185
#1  0x000055ae9e5c8dd7 in epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::worker_thread() ()
#2  0x00007fbc0ae6b5d5 in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0
#3  0x00007fbc0a6ac6ba in start_thread (arg=0x7fbbf77fe700) at pthread_create.c:333
#4  0x00007fbc0a3e241d in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109

Thread 7 (Thread 0x7fbc04ebf700 (LWP 23885)):
#0  pthread_cond_wait@@GLIBC_2.3.2 () at ../sysdeps/unix/sysv/linux/x86_64/pthread_cond_wait.S:185
#1  0x000055ae9e83a628 in boost::asio::io_service::run() ()
#2  0x00007fbc0ae6b5d5 in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0
#3  0x00007fbc0a6ac6ba in start_thread (arg=0x7fbc04ebf700) at pthread_create.c:333
#4  0x00007fbc0a3e241d in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109

Thread 6 (Thread 0x7fbc05ec1700 (LWP 23882)):
#0  0x00007fbc0a3d85d3 in select () at ../sysdeps/unix/syscall-template.S:84
#1  0x00007fbc0b9f928c in ?? () from /usr/lib/x86_64-linux-gnu/libunbound.so.2
#2  0x00007fbc0b9cbcc7 in ?? () from /usr/lib/x86_64-linux-gnu/libunbound.so.2
#3  0x00007fbc0b9e25cd in ub_resolve () from /usr/lib/x86_64-linux-gnu/libunbound.so.2
#4  0x000055ae9e8938ad in tools::DNSResolver::get_record(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > (*)(char const*, unsigned long), bool&, bool&) ()
#5  0x000055ae9e893a7e in tools::DNSResolver::get_ipv4(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, bool&, bool&) ()
#6  0x000055ae9e773d73 in nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::init(boost::program_options::variables_map const&)::{lambda()#1}::operator()() const ()
#7  0x00007fbc0ae6b5d5 in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0
#8  0x00007fbc0a6ac6ba in start_thread (arg=0x7fbc05ec1700) at pthread_create.c:333
#9  0x00007fbc0a3e241d in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109

Thread 5 (Thread 0x7fbc06bc3700 (LWP 23880)):
#0  pthread_cond_wait@@GLIBC_2.3.2 () at ../sysdeps/unix/sysv/linux/x86_64/pthread_cond_wait.S:185
#1  0x000055ae9e8ab463 in tools::threadpool::run() ()
#2  0x00007fbc0ae6b5d5 in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0
#3  0x00007fbc0a6ac6ba in start_thread (arg=0x7fbc06bc3700) at pthread_create.c:333
#4  0x00007fbc0a3e241d in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109

Thread 4 (Thread 0x7fbc070c4700 (LWP 23879)):
#0  pthread_cond_wait@@GLIBC_2.3.2 () at ../sysdeps/unix/sysv/linux/x86_64/pthread_cond_wait.S:185
#1  0x000055ae9e8ab463 in tools::threadpool::run() ()
#2  0x00007fbc0ae6b5d5 in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0
#3  0x00007fbc0a6ac6ba in start_thread (arg=0x7fbc070c4700) at pthread_create.c:333
#4  0x00007fbc0a3e241d in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109

Thread 3 (Thread 0x7fbc075c5700 (LWP 23878)):
#0  pthread_cond_wait@@GLIBC_2.3.2 () at ../sysdeps/unix/sysv/linux/x86_64/pthread_cond_wait.S:185
#1  0x000055ae9e8ab463 in tools::threadpool::run() ()
#2  0x00007fbc0ae6b5d5 in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0
#3  0x00007fbc0a6ac6ba in start_thread (arg=0x7fbc075c5700) at pthread_create.c:333
#4  0x00007fbc0a3e241d in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109

Thread 2 (Thread 0x7fbc07ac6700 (LWP 23877)):
#0  pthread_cond_wait@@GLIBC_2.3.2 () at ../sysdeps/unix/sysv/linux/x86_64/pthread_cond_wait.S:185
#1  0x000055ae9e8ab463 in tools::threadpool::run() ()
#2  0x00007fbc0ae6b5d5 in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0
#3  0x00007fbc0a6ac6ba in start_thread (arg=0x7fbc07ac6700) at pthread_create.c:333
#4  0x00007fbc0a3e241d in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109

Thread 1 (Thread 0x7fbc0d052780 (LWP 23876)):
#0  pthread_cond_wait@@GLIBC_2.3.2 () at ../sysdeps/unix/sysv/linux/x86_64/pthread_cond_wait.S:185
#1  0x00007fbc0ae6d043 in boost::thread::join_noexcept() () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0
#2  0x000055ae9e7c2218 in epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::run_server(unsigned long, bool, boost::thread_attributes const&) ()
#3  0x000055ae9e7c3c1e in nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::run() ()
#4  0x000055ae9e5b9b75 in daemonize::t_p2p::run() ()
#5  0x000055ae9e5afeef in daemonize::t_daemon::run(bool) ()
#6  0x000055ae9e65efbb in daemonize::t_executor::run_non_interactive(boost::program_options::variables_map const&) ()
#7  0x000055ae9e665f6d in bool daemonizer::daemonize<daemonize::t_executor>(int, char const**, daemonize::t_executor&&, boost::program_options::variables_map const&) ()
#8  0x000055ae9e583366 in main ()
```

@moneromooo-monero 
this is all info

## moneromooo-monero | 2018-05-26T19:23:38+00:00
Your problem in this trace is that monerod has not started listening to RPC yet, it's busy starting up and apparently being blocked by some DNS timeout. You should make sure DNS queries work from that machine/VM, including DNSSEC.
Alternatively, wait till monerod finished, the timeout for these can be a couple minutes maybe.


## wwaayyaa | 2018-05-27T05:38:47+00:00
@moneromooo-monero 
i added ```--disable-dns-checkpoint```, then sync very quickly, but send tx still slow. 

## monerod
```
2018-05-27 05:40:54.423 [P2P5]  INFO    global  src/cryptonote_core/blockchain.cpp:1528 ----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 1580225
id:     <38100f5b262b768d2f015b2db95dc8cf89428565d805085a58d9b706769d9307>
PoW:    <f9d54a23254878cb0f32d6a0e0e9459284e5e406c3b783eeaa0c3b1300000000>
difficulty:     50104776174
2018-05-27 05:40:54.449 [P2P5]  INFO    global  src/cryptonote_core/blockchain.cpp:1528 ----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 1580226
id:     <7fbf3f247c2453cc7f0e289339bc8ded557db88bb628bb102627764dfc2d72d8>
PoW:    <0659f8e5dbb91147dd46ba030a6571d2748301999d57d5a7fcf5a10e00000000>
difficulty:     50196839822
2018-05-27 05:40:54.450 [P2P5]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1560  SYNCHRONIZED OK
2018-05-27 05:40:54.450 [P2P5]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1582
**********************************************************************
You are now synchronized with the network. You may now start monero-wallet-cli.

Use the "help" command to see the list of available commands.
**********************************************************************
2018-05-27 05:40:58.789 [P2P9]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:310   [185.147.82.250:18080 OUT] Sync data returned a new top block candidate: 1581686 -> 1581687 [Your node is 1 blocks (0 days) behind]
SYNCHRONIZATION started
2018-05-27 05:41:00.249 [P2P9]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1560  SYNCHRONIZED OK
```

## gdb info
```
Thread 27 (Thread 0x7f0925f10700 (LWP 25165)):
#0  0x00007f1ea0d4e5d3 in select () at ../sysdeps/unix/syscall-template.S:84
#1  0x00007f1ea236f28c in ?? () from /usr/lib/x86_64-linux-gnu/libunbound.so.2
#2  0x00007f1ea2341cc7 in ?? () from /usr/lib/x86_64-linux-gnu/libunbound.so.2
#3  0x00007f1ea23585cd in ub_resolve () from /usr/lib/x86_64-linux-gnu/libunbound.so.2
#4  0x000055e65c8b48ad in tools::DNSResolver::get_record(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > (*)(char const*, unsigned long), bool&, bool&) ()
#5  0x000055e65c8b4b1e in tools::DNSResolver::get_txt_record(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, bool&, bool&) ()
#6  0x000055e65c8b6697 in boost::detail::thread_data<tools::dns_utils::load_txt_records_from_dns(std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > >&, std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > const&)::{lambda()#1}>::run() ()
#7  0x00007f1ea17e15d5 in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0
#8  0x00007f1ea10226ba in start_thread (arg=0x7f0925f10700) at pthread_create.c:333
#9  0x00007f1ea0d5841d in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109
Thread 26 (Thread 0x7f0926711700 (LWP 25164)):
#0  0x00007f1ea0d4e5d3 in select () at ../sysdeps/unix/syscall-template.S:84
#1  0x00007f1ea236f28c in ?? () from /usr/lib/x86_64-linux-gnu/libunbound.so.2
#2  0x00007f1ea2341cc7 in ?? () from /usr/lib/x86_64-linux-gnu/libunbound.so.2
#3  0x00007f1ea23585cd in ub_resolve () from /usr/lib/x86_64-linux-gnu/libunbound.so.2
#4  0x000055e65c8b48ad in tools::DNSResolver::get_record(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > (*)(char const*, unsigned long), bool&, bool&) ()
#5  0x000055e65c8b4b1e in tools::DNSResolver::get_txt_record(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, bool&, bool&) ()
#6  0x000055e65c8b6697 in boost::detail::thread_data<tools::dns_utils::load_txt_records_from_dns(std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > >&, std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > const&)::{lambda()#1}>::run() ()
#7  0x00007f1ea17e15d5 in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0
#8  0x00007f1ea10226ba in start_thread (arg=0x7f0926711700) at pthread_create.c:333
#9  0x00007f1ea0d5841d in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109

Thread 25 (Thread 0x7f1e8cff6700 (LWP 25163)):
#0  0x00007f1ea0d4e5d3 in select () at ../sysdeps/unix/syscall-template.S:84
#1  0x00007f1ea236f28c in ?? () from /usr/lib/x86_64-linux-gnu/libunbound.so.2
#2  0x00007f1ea2341cc7 in ?? () from /usr/lib/x86_64-linux-gnu/libunbound.so.2
#3  0x00007f1ea23585cd in ub_resolve () from /usr/lib/x86_64-linux-gnu/libunbound.so.2
#4  0x000055e65c8b48ad in tools::DNSResolver::get_record(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > (*)(char const*, unsigned long), bool&, bool&) ()
#5  0x000055e65c8b4b1e in tools::DNSResolver::get_txt_record(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, bool&, bool&) ()
#6  0x000055e65c8b6697 in boost::detail::thread_data<tools::dns_utils::load_txt_records_from_dns(std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > >&, std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > const&)::{lambda()#1}>::run() ()
#7  0x00007f1ea17e15d5 in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0
#8  0x00007f1ea10226ba in start_thread (arg=0x7f1e8cff6700) at pthread_create.c:333
#9  0x00007f1ea0d5841d in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109

Thread 24 (Thread 0x7f1e8d7f7700 (LWP 25162)):
#0  0x00007f1ea0d4e5d3 in select () at ../sysdeps/unix/syscall-template.S:84
#1  0x00007f1ea236f28c in ?? () from /usr/lib/x86_64-linux-gnu/libunbound.so.2
#2  0x00007f1ea2341cc7 in ?? () from /usr/lib/x86_64-linux-gnu/libunbound.so.2
#3  0x00007f1ea23585cd in ub_resolve () from /usr/lib/x86_64-linux-gnu/libunbound.so.2
#4  0x000055e65c8b48ad in tools::DNSResolver::get_record(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > (*)(char const*, unsigned long), bool&, bool&) ()
#5  0x000055e65c8b4b1e in tools::DNSResolver::get_txt_record(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, bool&, bool&) ()
#6  0x000055e65c8b6697 in boost::detail::thread_data<tools::dns_utils::load_txt_records_from_dns(std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > >&, std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > const&)::{lambda()#1}>::run() ()
#7  0x00007f1ea17e15d5 in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0
#8  0x00007f1ea10226ba in start_thread (arg=0x7f1e8d7f7700) at pthread_create.c:333
#9  0x00007f1ea0d5841d in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109

Thread 23 (Thread 0x7f1e8dcf8700 (LWP 25161)):
#0  0x00007f1ea0d58a13 in epoll_wait () at ../sysdeps/unix/syscall-template.S:84
#1  0x000055e65c7a019d in epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread() ()
#2  0x00007f1ea17e15d5 in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0
#3  0x00007f1ea10226ba in start_thread (arg=0x7f1e8dcf8700) at pthread_create.c:333
#4  0x00007f1ea0d5841d in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109

Thread 22 (Thread 0x7f1e8e1f9700 (LWP 25160)):
#0  pthread_cond_wait@@GLIBC_2.3.2 () at ../sysdeps/unix/sysv/linux/x86_64/pthread_cond_wait.S:185
#1  0x000055e65c7a0609 in epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread() ()
#2  0x00007f1ea17e15d5 in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0
#3  0x00007f1ea10226ba in start_thread (arg=0x7f1e8e1f9700) at pthread_create.c:333
#4  0x00007f1ea0d5841d in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109

Thread 21 (Thread 0x7f1e8e6fa700 (LWP 25159)):
#0  pthread_cond_wait@@GLIBC_2.3.2 () at ../sysdeps/unix/sysv/linux/x86_64/pthread_cond_wait.S:185
#1  0x000055e65c7a0609 in epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread() ()
#2  0x00007f1ea17e15d5 in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0
#3  0x00007f1ea10226ba in start_thread (arg=0x7f1e8e6fa700) at pthread_create.c:333
#4  0x00007f1ea0d5841d in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109

Thread 20 (Thread 0x7f1e8ebfb700 (LWP 25158)):
#0  pthread_cond_wait@@GLIBC_2.3.2 () at ../sysdeps/unix/sysv/linux/x86_64/pthread_cond_wait.S:185
#1  0x000055e65c7a0609 in epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread() ()
#2  0x00007f1ea17e15d5 in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0
#3  0x00007f1ea10226ba in start_thread (arg=0x7f1e8ebfb700) at pthread_create.c:333
#4  0x00007f1ea0d5841d in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109

Thread 19 (Thread 0x7f1e8f0fc700 (LWP 25157)):
#0  pthread_cond_wait@@GLIBC_2.3.2 () at ../sysdeps/unix/sysv/linux/x86_64/pthread_cond_wait.S:185
#1  0x000055e65c7a0609 in epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread() ()
#2  0x00007f1ea17e15d5 in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0
#3  0x00007f1ea10226ba in start_thread (arg=0x7f1e8f0fc700) at pthread_create.c:333
#4  0x00007f1ea0d5841d in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109

Thread 18 (Thread 0x7f1e8f5fd700 (LWP 25156)):
#0  pthread_cond_wait@@GLIBC_2.3.2 () at ../sysdeps/unix/sysv/linux/x86_64/pthread_cond_wait.S:185
#1  0x000055e65c7a0609 in epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread() ()
#2  0x00007f1ea17e15d5 in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0
#3  0x00007f1ea10226ba in start_thread (arg=0x7f1e8f5fd700) at pthread_create.c:333
#4  0x00007f1ea0d5841d in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109

Thread 17 (Thread 0x7f1e8fafe700 (LWP 25155)):
#0  pthread_cond_wait@@GLIBC_2.3.2 () at ../sysdeps/unix/sysv/linux/x86_64/pthread_cond_wait.S:185
#1  0x000055e65c7a0609 in epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread() ()
#2  0x00007f1ea17e15d5 in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0
#3  0x00007f1ea10226ba in start_thread (arg=0x7f1e8fafe700) at pthread_create.c:333
#4  0x00007f1ea0d5841d in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109

Thread 16 (Thread 0x7f1e8ffff700 (LWP 25154)):
#0  pthread_cond_wait@@GLIBC_2.3.2 () at ../sysdeps/unix/sysv/linux/x86_64/pthread_cond_wait.S:185
#1  0x00007f1ea17e3043 in boost::thread::join_noexcept() () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0
#2  0x000055e65c8b73a7 in tools::dns_utils::load_txt_records_from_dns(std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > >&, std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > const&) ()
#3  0x000055e65c8cf2c8 in tools::check_updates(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&) ()
#4  0x000055e65c866dd8 in cryptonote::core::check_updates() ()
#5  0x000055e65c86274c in cryptonote::core::on_idle() ()
#6  0x000055e65c787ff9 in cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::on_idle() ()
#7  0x000055e65c7a2897 in epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::global_timer_handler(boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext_base>) ()
#8  0x000055e65c788a99 in boost::asio::detail::wait_handler<boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext_base> >, boost::_bi::list2<boost::_bi::value<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >*>, boost::_bi::value<boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext_base> > > > >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) ()
#9  0x000055e65c7a06b4 in epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread() ()
#10 0x00007f1ea17e15d5 in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0
#11 0x00007f1ea10226ba in start_thread (arg=0x7f1e8ffff700) at pthread_create.c:333
#12 0x00007f1ea0d5841d in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109

Thread 15 (Thread 0x7f1e948f7700 (LWP 25153)):
#0  pthread_cond_wait@@GLIBC_2.3.2 () at ../sysdeps/unix/sysv/linux/x86_64/pthread_cond_wait.S:185
#1  0x000055e65c7a0609 in epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread() ()
#2  0x00007f1ea17e15d5 in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0
#3  0x00007f1ea10226ba in start_thread (arg=0x7f1e948f7700) at pthread_create.c:333
#4  0x00007f1ea0d5841d in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109

Thread 14 (Thread 0x7f1e94df8700 (LWP 25152)):
#0  pthread_cond_timedwait@@GLIBC_2.3.2 () at ../sysdeps/unix/sysv/linux/x86_64/pthread_cond_timedwait.S:225
#1  0x000055e65c7ebaea in epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::connect(std::__cxx11::b
asic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, unsigned int, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&) ()
#2  0x000055e65c7ed19f in nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::try_to_connect_and_handshake_with_new_peer(epee::net_utils::network_address const&, bool, unsigned long, nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::PeerType, unsigned long) ()
#3  0x000055e65c7ef481 in nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::make_new_connection_from_peerlist(bool) ()
#4  0x000055e65c7efc99 in nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::make_expected_connections_count(nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::PeerType, unsigned long) ()
#5  0x000055e65c7f0659 in nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::connections_maker() ()
#6  0x000055e65c788210 in nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::idle_worker() ()
#7  0x000055e65c7a2897 in epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::global_timer_handler(boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext_base>) ()
#8  0x000055e65c788a99 in boost::asio::detail::wait_handler<boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext_base> >, boost::_bi::list2<boost::_bi::value<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >*>, boost::_bi::value<boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext_base> > > > >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) ()
#9  0x000055e65c7a06b4 in epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread() ()
#10 0x00007f1ea17e15d5 in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0
#11 0x00007f1ea10226ba in start_thread (arg=0x7f1e94df8700) at pthread_create.c:333
#12 0x00007f1ea0d5841d in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109

Thread 13 (Thread 0x7f1e955f9700 (LWP 25151)):
#0  pthread_cond_timedwait@@GLIBC_2.3.2 () at ../sysdeps/unix/sysv/linux/x86_64/pthread_cond_timedwait.S:225
#1  0x00007f1ea17e17e2 in boost::this_thread::hiden::sleep_for(timespec const&) () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0
#2  0x000055e65c791a4b in nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::run()::{lambda()#1}::operator()() const ()
#3  0x00007f1ea17e15d5 in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0
#4  0x00007f1ea10226ba in start_thread (arg=0x7f1e955f9700) at pthread_create.c:333
#5  0x00007f1ea0d5841d in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109

Thread 12 (Thread 0x7f1e95dfa700 (LWP 25150)):
#0  0x00007f1ea0d4c74d in poll () at ../sysdeps/unix/syscall-template.S:84
#1  0x00007f1ea27d912a in ?? () from /usr/lib/x86_64-linux-gnu/libzmq.so.5
#2  0x00007f1ea27c4176 in ?? () from /usr/lib/x86_64-linux-gnu/libzmq.so.5
#3  0x00007f1ea27da3f1 in ?? () from /usr/lib/x86_64-linux-gnu/libzmq.so.5
#4  0x00007f1ea27dabd0 in ?? () from /usr/lib/x86_64-linux-gnu/libzmq.so.5
#5  0x00007f1ea27f0a09 in ?? () from /usr/lib/x86_64-linux-gnu/libzmq.so.5
#6  0x000055e65c8e4c9f in cryptonote::rpc::ZmqServer::serve() ()
#7  0x00007f1ea17e15d5 in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0
#8  0x00007f1ea10226ba in start_thread (arg=0x7f1e95dfa700) at pthread_create.c:333
#9  0x00007f1ea0d5841d in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109

Thread 11 (Thread 0x7f1e965fb700 (LWP 25149)):
#0  0x00007f1ea0d58a13 in epoll_wait () at ../sysdeps/unix/syscall-template.S:84
#1  0x00007f1ea27c00ec in ?? () from /usr/lib/x86_64-linux-gnu/libzmq.so.5
#2  0x00007f1ea27eb7fa in ?? () from /usr/lib/x86_64-linux-gnu/libzmq.so.5
#3  0x00007f1ea10226ba in start_thread (arg=0x7f1e965fb700) at pthread_create.c:333
#4  0x00007f1ea0d5841d in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109

Thread 10 (Thread 0x7f1e96dfc700 (LWP 25148)):
#0  0x00007f1ea0d58a13 in epoll_wait () at ../sysdeps/unix/syscall-template.S:84
#1  0x00007f1ea27c00ec in ?? () from /usr/lib/x86_64-linux-gnu/libzmq.so.5
#2  0x00007f1ea27eb7fa in ?? () from /usr/lib/x86_64-linux-gnu/libzmq.so.5
#3  0x00007f1ea10226ba in start_thread (arg=0x7f1e96dfc700) at pthread_create.c:333
#4  0x00007f1ea0d5841d in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109

Thread 9 (Thread 0x7f1e9d038700 (LWP 25147)):
#0  pthread_cond_wait@@GLIBC_2.3.2 () at ../sysdeps/unix/sysv/linux/x86_64/pthread_cond_wait.S:185
#1  0x000055e65c5e9dd7 in epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::worker_thread() ()
#2  0x00007f1ea17e15d5 in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0
#3  0x00007f1ea10226ba in start_thread (arg=0x7f1e9d038700) at pthread_create.c:333
#4  0x00007f1ea0d5841d in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109

Thread 8 (Thread 0x7f1e97fff700 (LWP 25146)):
#0  0x00007f1ea0d58a13 in epoll_wait () at ../sysdeps/unix/syscall-template.S:84
#1  0x000055e65c5e9971 in epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::worker_thread() ()
#2  0x00007f1ea17e15d5 in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0
#3  0x00007f1ea10226ba in start_thread (arg=0x7f1e97fff700) at pthread_create.c:333
#4  0x00007f1ea0d5841d in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109

Thread 7 (Thread 0x7f1e977fe700 (LWP 25145)):
#0  pthread_cond_wait@@GLIBC_2.3.2 () at ../sysdeps/unix/sysv/linux/x86_64/pthread_cond_wait.S:185
#1  0x000055e65c85b628 in boost::asio::io_service::run() ()
#2  0x00007f1ea17e15d5 in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0
#3  0x00007f1ea10226ba in start_thread (arg=0x7f1e977fe700) at pthread_create.c:333
#4  0x00007f1ea0d5841d in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109

Thread 6 (Thread 0x7f1e9c837700 (LWP 25142)):
#0  0x00007f1ea0d4e5d3 in select () at ../sysdeps/unix/syscall-template.S:84
#1  0x00007f1ea236f28c in ?? () from /usr/lib/x86_64-linux-gnu/libunbound.so.2
#2  0x00007f1ea2341cc7 in ?? () from /usr/lib/x86_64-linux-gnu/libunbound.so.2
#3  0x00007f1ea23585cd in ub_resolve () from /usr/lib/x86_64-linux-gnu/libunbound.so.2
#4  0x000055e65c8b48ad in tools::DNSResolver::get_record(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > (*)(char const*, unsigned long), bool&, bool&) ()
#5  0x000055e65c8b4a7e in tools::DNSResolver::get_ipv4(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, bool&, bool&) ()
#6  0x000055e65c794d73 in nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::init(boost::program_options::variables_map const&)::{lambda()#1}::operator()() const ()
#7  0x00007f1ea17e15d5 in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0
#8  0x00007f1ea10226ba in start_thread (arg=0x7f1e9c837700) at pthread_create.c:333
#9  0x00007f1ea0d5841d in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109

Thread 5 (Thread 0x7f1e9d539700 (LWP 25140)):
#0  pthread_cond_wait@@GLIBC_2.3.2 () at ../sysdeps/unix/sysv/linux/x86_64/pthread_cond_wait.S:185
#1  0x000055e65c8cc463 in tools::threadpool::run() ()
#2  0x00007f1ea17e15d5 in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0
#3  0x00007f1ea10226ba in start_thread (arg=0x7f1e9d539700) at pthread_create.c:333
#4  0x00007f1ea0d5841d in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109

Thread 4 (Thread 0x7f1e9da3a700 (LWP 25139)):
#0  pthread_cond_wait@@GLIBC_2.3.2 () at ../sysdeps/unix/sysv/linux/x86_64/pthread_cond_wait.S:185
#1  0x000055e65c8cc463 in tools::threadpool::run() ()
#2  0x00007f1ea17e15d5 in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0
#3  0x00007f1ea10226ba in start_thread (arg=0x7f1e9da3a700) at pthread_create.c:333
#4  0x00007f1ea0d5841d in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109

Thread 3 (Thread 0x7f1e9df3b700 (LWP 25138)):
#0  pthread_cond_wait@@GLIBC_2.3.2 () at ../sysdeps/unix/sysv/linux/x86_64/pthread_cond_wait.S:185
#1  0x000055e65c8cc463 in tools::threadpool::run() ()
#2  0x00007f1ea17e15d5 in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0
#3  0x00007f1ea10226ba in start_thread (arg=0x7f1e9df3b700) at pthread_create.c:333
#4  0x00007f1ea0d5841d in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109

Thread 2 (Thread 0x7f1e9e43c700 (LWP 25137)):
#0  pthread_cond_wait@@GLIBC_2.3.2 () at ../sysdeps/unix/sysv/linux/x86_64/pthread_cond_wait.S:185
#1  0x000055e65c8cc463 in tools::threadpool::run() ()
#2  0x00007f1ea17e15d5 in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0
#3  0x00007f1ea10226ba in start_thread (arg=0x7f1e9e43c700) at pthread_create.c:333
#4  0x00007f1ea0d5841d in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109

Thread 1 (Thread 0x7f1ea39c8780 (LWP 25136)):
#0  pthread_cond_wait@@GLIBC_2.3.2 () at ../sysdeps/unix/sysv/linux/x86_64/pthread_cond_wait.S:185
#1  0x00007f1ea17e3043 in boost::thread::join_noexcept() () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0
#2  0x000055e65c7e3218 in epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::run_server(unsigned long, bool, boost::thread_attributes const&) ()
#3  0x000055e65c7e4c1e in nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::run() ()
#4  0x000055e65c5dab75 in daemonize::t_p2p::run() ()
#5  0x000055e65c5d0eef in daemonize::t_daemon::run(bool) ()
#6  0x000055e65c67ffbb in daemonize::t_executor::run_non_interactive(boost::program_options::variables_map const&) ()
#7  0x000055e65c686f6d in bool daemonizer::daemonize<daemonize::t_executor>(int, char const**, daemonize::t_executor&&, boost::program_options::variables_map const&) ()
#8  0x000055e65c5a4366 in main ()

```




## moneromooo-monero | 2018-05-27T07:56:07+00:00
That does not show anything wrong with RPC either. You're still having DNS threads (try --check-updates disabled) though. Probably unrelated though. Try adding --log-level 0,perf:DEBUG, this will add timings of each RPC call. We'll see if any of them is slow, and which.

## wwaayyaa | 2018-05-27T14:05:59+00:00
--check-updates has no effect.
i added ```--offline``` and ```--log-level=3```

### cli
```
Balance: 4.327351376052, unlocked balance: 4.327351376052
Background refresh thread started
[wallet 479Qqx]: transfer 479QqxhWGYJEfVy7HWtfnxGjqFpW5RiTLcdDMPXqaSodUt78LPLdu3hJWMhouzmjhb79avtXEPZBMQHZdbWYAqsaQpj91mM 0.01
Wallet password:
No payment id is included with this transaction. Is this okay?  (Y/Yes/N/No): y
// Still no response
// maybe 20minutes ,response below
There is currently a 1 block backlog at that fee level. Is this okay?  (Y/Yes/N/No):
```

### monerod

```
// more log

2018-05-27 13:56:03.757 [RPC1]  TRACE   blockchain.db.lmdb src/blockchain_db/lmdb/db_lmdb.cpp:2186 BlockchainLMDB::get_tx_count
2018-05-27 13:56:03.757 [RPC1]  TRACE   blockchain.db.lmdb src/blockchain_db/lmdb/db_lmdb.cpp:2820 BlockchainLMDB::block_rtxn_start
2018-05-27 13:56:03.757 [RPC1]  TRACE   blockchain.db.lmdb src/blockchain_db/lmdb/db_lmdb.cpp:315  mdb_txn_safe: destructor
2018-05-27 13:56:03.757 [RPC1]  TRACE   blockchain.db.lmdb src/blockchain_db/lmdb/db_lmdb.cpp:1542 BlockchainLMDB::get_txpool_tx_count
2018-05-27 13:56:03.757 [RPC1]  TRACE   blockchain.db.lmdb src/blockchain_db/lmdb/db_lmdb.cpp:2820 BlockchainLMDB::block_rtxn_start
2018-05-27 13:56:03.757 [RPC1]  TRACE   blockchain.db.lmdb src/blockchain_db/lmdb/db_lmdb.cpp:315  mdb_txn_safe: destructor
2018-05-27 13:56:03.757 [RPC1]  TRACE   blockchainsrc/cryptonote_core/blockchain.cpp:1658  Blockchain::get_alternative_blocks_count
2018-05-27 13:56:03.757 [RPC1]  TRACE   blockchain.db.lmdb src/blockchain_db/lmdb/db_lmdb.cpp:1891 BlockchainLMDB::get_block_cumulative_difficulty  height: 1581918
2018-05-27 13:56:03.757 [RPC1]  TRACE   blockchain.db.lmdb src/blockchain_db/lmdb/db_lmdb.cpp:2820 BlockchainLMDB::block_rtxn_start
2018-05-27 13:56:03.757 [RPC1]  TRACE   blockchain.db.lmdb src/blockchain_db/lmdb/db_lmdb.cpp:315  mdb_txn_safe: destructor
2018-05-27 13:56:03.757 [RPC1]  TRACE   blockchainsrc/cryptonote_core/blockchain.cpp:1163  Blockchain::get_current_cumulative_blocksize_limit
2018-05-27 13:56:03.757 [RPC1]  TRACE   blockchainsrc/cryptonote_core/blockchain.cpp:1169  Blockchain::get_current_cumulative_blocksize_median
2018-05-27 13:56:03.757 [RPC1]  DEBUG   perf    src/common/perf_timer.cpp:128      PERF      370    on_get_info_json
2018-05-27 13:56:03.757 [RPC1]  DEBUG   net.http  src/rpc/core_rpc_server.h:143    /json_rpc[get_info] processed with 0/370/0ms
2018-05-27 13:56:03.757 [RPC1]  TRACE   net.http  contrib/epee/include/net/http_protocol_handler.inl:567      HTTP_RESPONSE_HEAD: <<
HTTP/1.1 200 Ok
Server: Epee-based
Content-Length: 938
Content-Type: application/json
Last-Modified: Sun, 27 May 2018 13:56:03 GMT
Accept-Ranges: bytes


2018-05-27 13:56:03.757 [RPC1]  TRACE   net.throttle       contrib/epee/src/network_throttle-detail.cpp:183   Moving counter buffer by 1 second 1.97389e+06 < 1.97389e+06 (last time 1.97389e+06)
2018-05-27 13:56:03.757 [RPC1]  TRACE   net.throttle       contrib/epee/src/network_throttle-detail.cpp:218   Throttle throttle_speed_out: packet of ~160b  (from 160 b) Speed AVG=   0[w=9.146]    0[w=9.14
6] /  Limit=16 KiB/sec  [160 2684 0 0 0 0 0 0 0 0 ]
2018-05-27 13:56:03.757 [RPC1]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:537do_send() NOW SENSD: packet=160 B
2018-05-27 13:56:03.758 [RPC1]  TRACE   net.throttle       contrib/epee/src/network_throttle-detail.cpp:218   Throttle throttle_speed_out: packet of ~938b  (from 938 b) Speed AVG=   0[w=9.146]    0[w=9.14
6] /  Limit=16 KiB/sec  [1098 2684 0 0 0 0 0 0 0 0 ]
2018-05-27 13:56:03.758 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:599[127.0.0.1:44180 INC] [sock 29] Async send calledback 160
2018-05-27 13:56:03.758 [RPC1]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:522do_send() NOW just queues: packet=938 B, is added to queue-size=2
2018-05-27 13:56:03.758 [RPC1]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:525[127.0.0.1:44180 INC] [sock 29] Async send requested 160
2018-05-27 13:56:03.758 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:633handle_write() NOW SENDS: packet=938 B, from  queue size=1
2018-05-27 13:56:03.758 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:599[127.0.0.1:44180 INC] [sock 29] Async send calledback 938
2018-05-27 13:56:05.206 [P2P5]  DEBUG   net.p2p src/p2p/net_node.inl:1302  STARTED PEERLIST IDLE HANDSHAKE
2018-05-27 13:56:05.206 [P2P5]  DEBUG   net.p2p src/p2p/net_node.inl:1317  FINISHED PEERLIST IDLE HANDSHAKE
2018-05-27 13:56:06.406 [RPC1]  TRACE   net.throttle       contrib/epee/src/network_throttle-detail.cpp:183   Moving counter buffer by 1 second 1.97389e+06 < 1.97389e+06 (last time 1.97389e+06)
2018-05-27 13:56:06.406 [RPC1]  TRACE   net.throttle       contrib/epee/src/network_throttle-detail.cpp:183   Moving counter buffer by 1 second 1.97389e+06 < 1.97389e+06 (last time 1.97389e+06)
2018-05-27 13:56:06.406 [RPC1]  TRACE   net.throttle       contrib/epee/src/network_throttle-detail.cpp:183   Moving counter buffer by 1 second 1.97389e+06 < 1.97389e+06 (last time 1.97389e+06)
2018-05-27 13:56:06.406 [RPC1]  TRACE   net.throttle       contrib/epee/src/network_throttle-detail.cpp:218   Throttle throttle_speed_in: packet of ~219b  (from 219 b) Speed AVG=   0[w=9.795]    0[w=9.795
] /  Limit=16 KiB/sec  [219 0 0 1374 0 0 0 0 0 0 ]
2018-05-27 13:56:06.406 [RPC1]  TRACE   net.throttle       contrib/epee/src/network_throttle-detail.cpp:183   Moving counter buffer by 1 second 1.97389e+06 < 1.97389e+06 (last time 1.97389e+06)
2018-05-27 13:56:06.406 [RPC1]  TRACE   net.throttle       contrib/epee/src/network_throttle-detail.cpp:183   Moving counter buffer by 1 second 1.97389e+06 < 1.97389e+06 (last time 1.97389e+06)
2018-05-27 13:56:06.406 [RPC1]  TRACE   net.throttle       contrib/epee/src/network_throttle-detail.cpp:183   Moving counter buffer by 1 second 1.97389e+06 < 1.97389e+06 (last time 1.97389e+06)
2018-05-27 13:56:06.406 [RPC1]  TRACE   net.throttle       contrib/epee/src/network_throttle-detail.cpp:218   Throttle <<< global-IN: packet of ~219b  (from 219 b) Speed AVG=   0[w=9.795]    0[w=9.795] /
 Limit=8192 KiB/sec  [219 0 0 1374 0 0 0 0 0 0 ]
2018-05-27 13:56:06.406 [RPC1]  DEBUG   net.http  src/rpc/core_rpc_server.h:78     HTTP [127.0.0.1] GET /json_rpc
2018-05-27 13:56:06.406 [RPC1]  DEBUG   perf    src/common/perf_timer.cpp:104      PERF             ----------
2018-05-27 13:56:06.406 [RPC1]  DEBUG   perf    src/common/perf_timer.cpp:128      PERF        0    on_hard_fork_info
2018-05-27 13:56:06.406 [RPC1]  DEBUG   net.http  src/rpc/core_rpc_server.h:144    /json_rpc[hard_fork_info] processed with 0/0/0ms
2018-05-27 13:56:06.406 [RPC1]  TRACE   net.http  contrib/epee/include/net/http_protocol_handler.inl:567      HTTP_RESPONSE_HEAD: <<
HTTP/1.1 200 Ok
Server: Epee-based
Content-Length: 274
Content-Type: application/json
Last-Modified: Sun, 27 May 2018 13:56:06 GMT
Accept-Ranges: bytes


2018-05-27 13:56:06.406 [RPC1]  TRACE   net.throttle       contrib/epee/src/network_throttle-detail.cpp:183   Moving counter buffer by 1 second 1.97389e+06 < 1.97389e+06 (last time 1.97389e+06)
2018-05-27 13:56:06.406 [RPC1]  TRACE   net.throttle       contrib/epee/src/network_throttle-detail.cpp:183   Moving counter buffer by 1 second 1.97389e+06 < 1.97389e+06 (last time 1.97389e+06)
2018-05-27 13:56:06.406 [RPC1]  TRACE   net.throttle       contrib/epee/src/network_throttle-detail.cpp:218   Throttle throttle_speed_out: packet of ~160b  (from 160 b) Speed AVG=   0[w=9.795]    0[w=9.79
5] /  Limit=16 KiB/sec  [160 0 1098 2684 0 0 0 0 0 0 ]
2018-05-27 13:56:06.406 [RPC1]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:537do_send() NOW SENSD: packet=160 B
2018-05-27 13:56:06.406 [RPC1]  TRACE   net.throttle       contrib/epee/src/network_throttle-detail.cpp:218   Throttle throttle_speed_out: packet of ~274b  (from 274 b) Speed AVG=   0[w=9.795]    0[w=9.79
5] /  Limit=16 KiB/sec  [434 0 1098 2684 0 0 0 0 0 0 ]
2018-05-27 13:56:06.407 [RPC1]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:522do_send() NOW just queues: packet=274 B, is added to queue-size=2
2018-05-27 13:56:06.407 [RPC1]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:525[127.0.0.1:44180 INC] [sock 29] Async send requested 160
2018-05-27 13:56:06.407 [RPC1]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:599[127.0.0.1:44180 INC] [sock 29] Async send calledback 160
2018-05-27 13:56:06.407 [RPC1]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:633handle_write() NOW SENDS: packet=274 B, from  queue size=1
2018-05-27 13:56:06.407 [RPC1]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:599[127.0.0.1:44180 INC] [sock 29] Async send calledback 274
2018-05-27 13:56:09.206 [P2P3]  TRACE   net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1203  Checking for idle peers...
2018-05-27 13:56:09.206 [P2P3]  TRACE   blockchain.db.lmdb src/blockchain_db/lmdb/db_lmdb.cpp:1683 BlockchainLMDB::for_all_txpool_txes
2018-05-27 13:56:09.206 [P2P3]  TRACE   blockchain.db.lmdb src/blockchain_db/lmdb/db_lmdb.cpp:2820 BlockchainLMDB::block_rtxn_start
2018-05-27 13:56:09.206 [P2P3]  TRACE   blockchain.db.lmdb src/blockchain_db/lmdb/db_lmdb.cpp:315  mdb_txn_safe: destructor
2018-05-27 13:56:40.208 [P2P0]  TRACE   net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1203    Checking for idle peers...
2018-05-27 13:56:40.208 [P2P0]  TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:1683 BlockchainLMDB::for_all_txpool_txes
2018-05-27 13:56:40.209 [P2P0]  TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:2820 BlockchainLMDB::block_rtxn_start
2018-05-27 13:56:40.209 [P2P0]  TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:315  mdb_txn_safe: destructor
2018-05-27 13:57:06.210 [P2P7]  DEBUG   net.p2p src/p2p/net_node.inl:1302       STARTED PEERLIST IDLE HANDSHAKE
2018-05-27 13:57:06.210 [P2P7]  DEBUG   net.p2p src/p2p/net_node.inl:1317       FINISHED PEERLIST IDLE HANDSHAKE
2018-05-27 13:57:11.211 [P2P8]  TRACE   net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1203    Checking for idle peers...
2018-05-27 13:57:11.211 [P2P8]  TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:1683 BlockchainLMDB::for_all_txpool_txes
2018-05-27 13:57:11.212 [P2P8]  TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:2820 BlockchainLMDB::block_rtxn_start
2018-05-27 13:57:11.212 [P2P8]  TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:315  mdb_txn_safe: destructor
2018-05-27 13:57:40.212 [P2P1]  TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:1683 BlockchainLMDB::for_all_txpool_txes
2018-05-27 13:57:40.213 [P2P1]  TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:2820 BlockchainLMDB::block_rtxn_start
2018-05-27 13:57:40.213 [P2P1]  TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:315  mdb_txn_safe: destructor
2018-05-27 13:57:42.213 [P2P6]  TRACE   net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1203    Checking for idle peers...
2018-05-27 13:57:42.213 [P2P6]  TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:1683 BlockchainLMDB::for_all_txpool_txes
2018-05-27 13:57:42.213 [P2P6]  TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:2820 BlockchainLMDB::block_rtxn_start
2018-05-27 13:57:42.213 [P2P6]  TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:315  mdb_txn_safe: destructor
2018-05-27 13:58:07.214 [P2P2]  DEBUG   net.p2p src/p2p/net_node.inl:1302       STARTED PEERLIST IDLE HANDSHAKE
2018-05-27 13:58:07.214 [P2P2]  DEBUG   net.p2p src/p2p/net_node.inl:1317       FINISHED PEERLIST IDLE HANDSHAKE
2018-05-27 13:58:13.214 [P2P2]  TRACE   net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1203    Checking for idle peers...
2018-05-27 13:58:13.214 [P2P2]  TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:1683 BlockchainLMDB::for_all_txpool_txes
2018-05-27 13:58:13.214 [P2P2]  TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:2820 BlockchainLMDB::block_rtxn_start
2018-05-27 13:58:13.215 [P2P2]  TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:315  mdb_txn_safe: destructor
2018-05-27 13:58:44.217 [P2P7]  TRACE   net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1203    Checking for idle peers...
2018-05-27 13:58:44.217 [P2P7]  TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:1683 BlockchainLMDB::for_all_txpool_txes
2018-05-27 13:58:44.217 [P2P7]  TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:2820 BlockchainLMDB::block_rtxn_start
2018-05-27 13:58:44.217 [P2P7]  TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:315  mdb_txn_safe: destructor
2018-05-27 13:59:08.218 [P2P2]  DEBUG   net.p2p src/p2p/net_node.inl:1302       STARTED PEERLIST IDLE HANDSHAKE
2018-05-27 13:59:08.219 [P2P2]  DEBUG   net.p2p src/p2p/net_node.inl:1317       FINISHED PEERLIST IDLE HANDSHAKE
2018-05-27 13:59:15.219 [P2P5]  TRACE   net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1203    Checking for idle peers...
2018-05-27 13:59:15.219 [P2P5]  TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:1683 BlockchainLMDB::for_all_txpool_txes
2018-05-27 13:59:15.219 [P2P5]  TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:2820 BlockchainLMDB::block_rtxn_start
2018-05-27 13:59:15.219 [P2P5]  TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:315  mdb_txn_safe: destructor

// some repeat 
.........
//when i seen cli response this line "There is currently a 1 block backlog at that fee level. Is this okay?  (Y/Yes/N/No):", monerod log below

2018-05-27 14:20:26.959 [RPC1]  TRACE   blockchain.db.lmdb src/blockchain_db/lmdb/db_lmdb.cpp:1891 BlockchainLMDB::get_block_cumulative_difficulty  height: 1581912
2018-05-27 14:20:26.959 [RPC1]  TRACE   blockchain.db.lmdb src/blockchain_db/lmdb/db_lmdb.cpp:2820 BlockchainLMDB::block_rtxn_start
2018-05-27 14:20:26.959 [RPC1]  TRACE   blockchain.db.lmdb src/blockchain_db/lmdb/db_lmdb.cpp:315  mdb_txn_safe: destructor
2018-05-27 14:20:26.959 [RPC1]  TRACE   blockchain.db.lmdb src/blockchain_db/lmdb/db_lmdb.cpp:1830 BlockchainLMDB::get_block_timestamp
2018-05-27 14:20:26.959 [RPC1]  TRACE   blockchain.db.lmdb src/blockchain_db/lmdb/db_lmdb.cpp:2820 BlockchainLMDB::block_rtxn_start
2018-05-27 14:20:26.959 [RPC1]  TRACE   blockchain.db.lmdb src/blockchain_db/lmdb/db_lmdb.cpp:315  mdb_txn_safe: destructor
2018-05-27 14:20:26.959 [RPC1]  TRACE   blockchain.db.lmdb src/blockchain_db/lmdb/db_lmdb.cpp:1891 BlockchainLMDB::get_block_cumulative_difficulty  height: 1581913
2018-05-27 14:20:26.959 [RPC1]  TRACE   blockchain.db.lmdb src/blockchain_db/lmdb/db_lmdb.cpp:2820 BlockchainLMDB::block_rtxn_start
2018-05-27 14:20:26.959 [RPC1]  TRACE   blockchain.db.lmdb src/blockchain_db/lmdb/db_lmdb.cpp:315  mdb_txn_safe: destructor
2018-05-27 14:20:26.959 [RPC1]  TRACE   blockchain.db.lmdb src/blockchain_db/lmdb/db_lmdb.cpp:1830 BlockchainLMDB::get_block_timestamp
2018-05-27 14:20:26.959 [RPC1]  TRACE   blockchain.db.lmdb src/blockchain_db/lmdb/db_lmdb.cpp:2820 BlockchainLMDB::block_rtxn_start
2018-05-27 14:20:26.959 [RPC1]  TRACE   blockchain.db.lmdb src/blockchain_db/lmdb/db_lmdb.cpp:315  mdb_txn_safe: destructor
2018-05-27 14:20:26.959 [RPC1]  TRACE   blockchain.db.lmdb src/blockchain_db/lmdb/db_lmdb.cpp:1891 BlockchainLMDB::get_block_cumulative_difficulty  height: 1581914
2018-05-27 14:20:26.959 [RPC1]  TRACE   blockchain.db.lmdb src/blockchain_db/lmdb/db_lmdb.cpp:2820 BlockchainLMDB::block_rtxn_start
2018-05-27 14:20:26.959 [RPC1]  TRACE   blockchain.db.lmdb src/blockchain_db/lmdb/db_lmdb.cpp:315  mdb_txn_safe: destructor
2018-05-27 14:20:26.959 [RPC1]  TRACE   blockchain.db.lmdb src/blockchain_db/lmdb/db_lmdb.cpp:1830 BlockchainLMDB::get_block_timestamp
2018-05-27 14:20:26.959 [RPC1]  TRACE   blockchain.db.lmdb src/blockchain_db/lmdb/db_lmdb.cpp:2820 BlockchainLMDB::block_rtxn_start
2018-05-27 14:20:26.959 [RPC1]  TRACE   blockchain.db.lmdb src/blockchain_db/lmdb/db_lmdb.cpp:315  mdb_txn_safe: destructor
2018-05-27 14:20:26.960 [RPC1]  TRACE   blockchain.db.lmdb src/blockchain_db/lmdb/db_lmdb.cpp:1891 BlockchainLMDB::get_block_cumulative_difficulty  height: 1581915
2018-05-27 14:20:26.960 [RPC1]  TRACE   blockchain.db.lmdb src/blockchain_db/lmdb/db_lmdb.cpp:2820 BlockchainLMDB::block_rtxn_start
2018-05-27 14:20:26.960 [RPC1]  TRACE   blockchain.db.lmdb src/blockchain_db/lmdb/db_lmdb.cpp:315  mdb_txn_safe: destructor
2018-05-27 14:20:26.960 [RPC1]  TRACE   blockchain.db.lmdb src/blockchain_db/lmdb/db_lmdb.cpp:1830 BlockchainLMDB::get_block_timestamp
2018-05-27 14:20:26.960 [RPC1]  TRACE   blockchain.db.lmdb src/blockchain_db/lmdb/db_lmdb.cpp:2820 BlockchainLMDB::block_rtxn_start
2018-05-27 14:20:26.960 [RPC1]  TRACE   blockchain.db.lmdb src/blockchain_db/lmdb/db_lmdb.cpp:315  mdb_txn_safe: destructor
2018-05-27 14:20:26.960 [RPC1]  TRACE   blockchain.db.lmdb src/blockchain_db/lmdb/db_lmdb.cpp:1891 BlockchainLMDB::get_block_cumulative_difficulty  height: 1581916
2018-05-27 14:20:26.960 [RPC1]  TRACE   blockchain.db.lmdb src/blockchain_db/lmdb/db_lmdb.cpp:2820 BlockchainLMDB::block_rtxn_start
2018-05-27 14:20:26.960 [RPC1]  TRACE   blockchain.db.lmdb src/blockchain_db/lmdb/db_lmdb.cpp:315  mdb_txn_safe: destructor
2018-05-27 14:20:26.960 [RPC1]  TRACE   blockchain.db.lmdb src/blockchain_db/lmdb/db_lmdb.cpp:1830 BlockchainLMDB::get_block_timestamp
2018-05-27 14:20:26.960 [RPC1]  TRACE   blockchain.db.lmdb src/blockchain_db/lmdb/db_lmdb.cpp:2820 BlockchainLMDB::block_rtxn_start
2018-05-27 14:20:26.960 [RPC1]  TRACE   blockchain.db.lmdb src/blockchain_db/lmdb/db_lmdb.cpp:315  mdb_txn_safe: destructor
2018-05-27 14:20:26.960 [RPC1]  TRACE   blockchain.db.lmdb src/blockchain_db/lmdb/db_lmdb.cpp:1891 BlockchainLMDB::get_block_cumulative_difficulty  height: 1581917
2018-05-27 14:20:26.960 [RPC1]  TRACE   blockchain.db.lmdb src/blockchain_db/lmdb/db_lmdb.cpp:2820 BlockchainLMDB::block_rtxn_start
2018-05-27 14:20:26.960 [RPC1]  TRACE   blockchain.db.lmdb src/blockchain_db/lmdb/db_lmdb.cpp:315  mdb_txn_safe: destructor
2018-05-27 14:20:26.960 [RPC1]  TRACE   blockchain.db.lmdb src/blockchain_db/lmdb/db_lmdb.cpp:1830 BlockchainLMDB::get_block_timestamp
2018-05-27 14:20:26.960 [RPC1]  TRACE   blockchain.db.lmdb src/blockchain_db/lmdb/db_lmdb.cpp:2820 BlockchainLMDB::block_rtxn_start
2018-05-27 14:20:26.960 [RPC1]  TRACE   blockchain.db.lmdb src/blockchain_db/lmdb/db_lmdb.cpp:315  mdb_txn_safe: destructor
2018-05-27 14:20:26.960 [RPC1]  TRACE   blockchain.db.lmdb src/blockchain_db/lmdb/db_lmdb.cpp:1891 BlockchainLMDB::get_block_cumulative_difficulty  height: 1581918
2018-05-27 14:20:26.960 [RPC1]  TRACE   blockchain.db.lmdb src/blockchain_db/lmdb/db_lmdb.cpp:2820 BlockchainLMDB::block_rtxn_start
2018-05-27 14:20:26.960 [RPC1]  TRACE   blockchain.db.lmdb src/blockchain_db/lmdb/db_lmdb.cpp:315  mdb_txn_safe: destructor
2018-05-27 14:20:26.960 [RPC1]  TRACE   blockchainsrc/cryptonote_core/blockchain.cpp:2286  Blockchain::get_total_transactions
2018-05-27 14:20:26.960 [RPC1]  TRACE   blockchain.db.lmdb src/blockchain_db/lmdb/db_lmdb.cpp:2186 BlockchainLMDB::get_tx_count
2018-05-27 14:20:26.960 [RPC1]  TRACE   blockchain.db.lmdb src/blockchain_db/lmdb/db_lmdb.cpp:2820 BlockchainLMDB::block_rtxn_start
2018-05-27 14:20:26.960 [RPC1]  TRACE   blockchain.db.lmdb src/blockchain_db/lmdb/db_lmdb.cpp:315  mdb_txn_safe: destructor
2018-05-27 14:20:26.960 [RPC1]  TRACE   blockchain.db.lmdb src/blockchain_db/lmdb/db_lmdb.cpp:1542 BlockchainLMDB::get_txpool_tx_count
2018-05-27 14:20:26.960 [RPC1]  TRACE   blockchain.db.lmdb src/blockchain_db/lmdb/db_lmdb.cpp:2820 BlockchainLMDB::block_rtxn_start
2018-05-27 14:20:26.960 [RPC1]  TRACE   blockchain.db.lmdb src/blockchain_db/lmdb/db_lmdb.cpp:315  mdb_txn_safe: destructor
2018-05-27 14:20:26.960 [RPC1]  TRACE   blockchainsrc/cryptonote_core/blockchain.cpp:1658  Blockchain::get_alternative_blocks_count
2018-05-27 14:20:26.960 [RPC1]  TRACE   blockchain.db.lmdb src/blockchain_db/lmdb/db_lmdb.cpp:1891 BlockchainLMDB::get_block_cumulative_difficulty  height: 1581918
2018-05-27 14:20:26.960 [RPC1]  TRACE   blockchain.db.lmdb src/blockchain_db/lmdb/db_lmdb.cpp:2820 BlockchainLMDB::block_rtxn_start
2018-05-27 14:20:26.960 [RPC1]  TRACE   blockchain.db.lmdb src/blockchain_db/lmdb/db_lmdb.cpp:315  mdb_txn_safe: destructor
2018-05-27 14:20:26.960 [RPC1]  TRACE   blockchainsrc/cryptonote_core/blockchain.cpp:1163  Blockchain::get_current_cumulative_blocksize_limit
2018-05-27 14:20:26.960 [RPC1]  TRACE   blockchainsrc/cryptonote_core/blockchain.cpp:1169  Blockchain::get_current_cumulative_blocksize_median
2018-05-27 14:20:26.960 [RPC1]  DEBUG   perf    src/common/perf_timer.cpp:128      PERF      381    on_get_info_json
2018-05-27 14:20:26.960 [RPC1]  DEBUG   net.http  src/rpc/core_rpc_server.h:143    /json_rpc[get_info] processed with 0/381/0ms
2018-05-27 14:20:26.960 [RPC1]  TRACE   net.http  contrib/epee/include/net/http_protocol_handler.inl:567      HTTP_RESPONSE_HEAD: <<
HTTP/1.1 200 Ok
Server: Epee-based
Content-Length: 938
Content-Type: application/json
Last-Modified: Sun, 27 May 2018 14:20:26 GMT
Accept-Ranges: bytes

2018-05-27 14:20:26.960 [RPC1]  TRACE   net.throttle       contrib/epee/src/network_throttle-detail.cpp:183   Moving counter buffer by 1 second 1.97535e+06 < 1.97535e+06 (last time 1.97535e+06)
2018-05-27 14:20:26.960 [RPC1]  TRACE   net.throttle       contrib/epee/src/network_throttle-detail.cpp:218   Throttle throttle_speed_out: packet of ~160b  (from 160 b) Speed AVG=   2[w=9.349]    2[w=9.34
9] /  Limit=16 KiB/sec  [160 21410 0 0 0 0 0 0 0 0 ]
2018-05-27 14:20:26.961 [RPC1]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:537do_send() NOW SENSD: packet=160 B
2018-05-27 14:20:26.961 [RPC1]  TRACE   net.throttle       contrib/epee/src/network_throttle-detail.cpp:218   Throttle throttle_speed_out: packet of ~938b  (from 938 b) Speed AVG=   2[w=9.349]    2[w=9.34
9] /  Limit=16 KiB/sec  [1098 21410 0 0 0 0 0 0 0 0 ]
2018-05-27 14:20:26.961 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:599[127.0.0.1:44180 INC] [sock 29] Async send calledback 160
2018-05-27 14:20:26.961 [RPC1]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:522do_send() NOW just queues: packet=938 B, is added to queue-size=2
2018-05-27 14:20:26.961 [RPC1]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:525[127.0.0.1:44180 INC] [sock 29] Async send requested 160
2018-05-27 14:20:26.961 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:633handle_write() NOW SENDS: packet=938 B, from  queue size=1
2018-05-27 14:20:26.961 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:599[127.0.0.1:44180 INC] [sock 29] Async send calledback 938
2018-05-27 14:20:29.305 [P2P8]  DEBUG   net.p2p src/p2p/net_node.inl:1302  STARTED PEERLIST IDLE HANDSHAKE
2018-05-27 14:20:29.305 [P2P8]  DEBUG   net.p2p src/p2p/net_node.inl:1317  FINISHED PEERLIST IDLE HANDSHAKE
2018-05-27 14:20:57.400 [P2P0]  TRACE   net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1203  Checking for idle peers...
2018-05-27 14:20:57.400 [P2P0]  TRACE   blockchain.db.lmdb src/blockchain_db/lmdb/db_lmdb.cpp:1683 BlockchainLMDB::for_all_txpool_txes
2018-05-27 14:20:57.401 [P2P0]  TRACE   blockchain.db.lmdb src/blockchain_db/lmdb/db_lmdb.cpp:2820 BlockchainLMDB::block_rtxn_start
2018-05-27 14:20:57.401 [P2P0]  TRACE   blockchain.db.lmdb src/blockchain_db/lmdb/db_lmdb.cpp:315  mdb_txn_safe: destructor
2018-05-27 14:21:28.402 [P2P4]  TRACE   net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1203  Checking for idle peers...
2018-05-27 14:21:28.403 [P2P4]  TRACE   blockchain.db.lmdb src/blockchain_db/lmdb/db_lmdb.cpp:1683 BlockchainLMDB::for_all_txpool_txes
2018-05-27 14:21:28.403 [P2P4]  TRACE   blockchain.db.lmdb src/blockchain_db/lmdb/db_lmdb.cpp:2820 BlockchainLMDB::block_rtxn_start
2018-05-27 14:21:28.403 [P2P4]  TRACE   blockchain.db.lmdb src/blockchain_db/lmdb/db_lmdb.cpp:315  mdb_txn_safe: destructor
2018-05-27 14:21:30.309 [P2P9]  DEBUG   net.p2p src/p2p/net_node.inl:1302  STARTED PEERLIST IDLE HANDSHAKE
2018-05-27 14:21:30.309 [P2P9]  DEBUG   net.p2p src/p2p/net_node.inl:1317  FINISHED PEERLIST IDLE HANDSHAKE
2018-05-27 14:21:52.404 [P2P0]  TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:1683 BlockchainLMDB::for_all_txpool_txes
2018-05-27 14:21:52.404 [P2P0]  TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:2820 BlockchainLMDB::block_rtxn_start
2018-05-27 14:21:52.404 [P2P0]  TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:315  mdb_txn_safe: destructor
2018-05-27 14:21:59.405 [P2P9]  TRACE   net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1203    Checking for idle peers...
2018-05-27 14:21:59.405 [P2P9]  TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:1683 BlockchainLMDB::for_all_txpool_txes
2018-05-27 14:21:59.405 [P2P9]  TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:2820 BlockchainLMDB::block_rtxn_start
2018-05-27 14:21:59.405 [P2P9]  TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:315  mdb_txn_safe: destructor

.....
.....


```
i can see when i enter ```y```, the last log below
```
2018-05-27 13:56:06.407 [RPC1]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:599[127.0.0.1:44180 INC] [sock 29] Async send calledback 274
```




## wwaayyaa | 2018-05-27T14:42:30+00:00
# rpc
when i send tx by rpc, rpc show below info 
```
root@host:/work/monero-data/auto
# /work/monero-v0.12.1.0/monero-wallet-rpc --wallet-dir=`pwd` --rpc-bind-port xxxx --confirm-external-bind --rpc-login xxx:xxxxxxx --rpc-bind-ip 0.0.0.0 --log-level 1
This is the RPC monero wallet. It needs to connect to a monero
daemon to work correctly.

Monero 'Lithium Luna' (v0.12.1.0-master-release)
2018-05-27 14:33:25.004     7f8a4b43b780        INFO    wallet.wallet2  src/wallet/wallet_args.cpp:192       Setting log level = 1
2018-05-27 14:33:25.004     7f8a4b43b780        INFO    wallet.wallet2  src/wallet/wallet_args.cpp:195       Logging to: /work/monero-v0.12.1.0/monero-wallet-rpc.log
Logging to /work/monero-v0.12.1.0/monero-wallet-rpc.log
2018-05-27 14:33:25.005     7f8a4b43b780        INFO    wallet.wallet2  src/wallet/wallet2.cpp:5531 ringdb path set to /home/ops/.shared-ringdb
2018-05-27 14:33:25.030     7f8a4b43b780        INFO    wallet.rpc      src/wallet/wallet_rpc_server.cpp:161 Daemon is local, assuming trusted
2018-05-27 14:33:25.030     7f8a4b43b780        INFO    net     contrib/epee/include/net/abstract_tcp_server2.inl:803        Set server type to: 1 from name: RPC, prefix_name = RPC
2018-05-27 14:33:25.030     7f8a4b43b780        INFO    global  contrib/epee/include/net/http_server_impl_base.h:76  Binding on 0.0.0.0:19082
2018-05-27 14:33:25.030     7f8a4b43b780        WARN    wallet.rpc      src/wallet/wallet_rpc_server.cpp:3001        Starting wallet RPC server
2018-05-27 14:33:25.030     7f8a4b43b780        INFO    net.http        contrib/epee/include/net/http_server_impl_base.h:89  Run net_service loop( 1 threads)...
2018-05-27 14:33:51.923 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:5531     ringdb path set to /home/ops/.shared-ringdb
2018-05-27 14:33:51.971 [RPC0]  WARN    wallet.wallet2  src/wallet/wallet2.cpp:3762     Loaded wallet keys file, with public address: 439SfTiajENNXgeFdCTsnmGjGvGHAPVCqPK4XjNQ9n4TWNB6NYPgHgMLs7ocmgxxFYAWYJXLieS4E7t9otBUcqQES21PCJJ
2018-05-27 14:33:51.978 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:3781     Trying to decrypt cache data
2018-05-27 14:34:15.663 [RPC0]  WARN    wallet.wallet2  src/wallet/wallet2.cpp:1297     Received money: 1.359540955223, with tx: <35112c73807ca6cc42a24a0019d64fdae2f9f80ba980393b0e5edc8a049727ca>
2018-05-27 14:34:16.283 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:1990     Found new pool tx: <f496b995c99fe0f6febcd5e4f834810b54eac5dd46176baba4f41ff50c7bbb28>
2018-05-27 14:34:16.283 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:1990     Found new pool tx: <9fc150d64666f0423b39cc0682ce67b977cb86f5b2add34fc47cd7f4522d8a2f>
2018-05-27 14:34:16.283 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:1990     Found new pool tx: <0e30d9eb51dcd1ec99253c5e54a6f00bb2bf42e756a0f7364e09ce606ff91542>
2018-05-27 14:34:16.283 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:1990     Found new pool tx: <75305b78a28334dabe11c34530dc9fe510ee35b67c8604727eb87e47aceec061>
2018-05-27 14:34:16.283 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:1990     Found new pool tx: <aec6600ddb631d149816adbbb8a62d20ff2146166da2d465fe584659c6fba19d>
2018-05-27 14:34:16.283 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:1990     Found new pool tx: <1135449c230d9e4bfebe3625347abcd92044d4dd2dcbad38a1dcfab4f724cabb>
2018-05-27 14:34:16.283 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:1990     Found new pool tx: <c4f84df29d011813c5558e02a5922bd506a621b5012a24c10154379e632ebfd9>
2018-05-27 14:34:16.283 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:1990     Found new pool tx: <51e9f93bb0a9414319f5dd68036601753d4b02eb324838ee05bd53ad3270c0e2>
2018-05-27 14:34:16.283 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:1990     Found new pool tx: <d3c0a5b9e2b2b0c38eb85945dec1747bf89651cf38b3cc65d525e4609ed6a3f8>
2018-05-27 14:34:16.365 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:2333     Refresh done, blocks received: 2257, balance (all accounts): 1.423512515223, unlocked: 1.423512515223
2018-05-27 14:34:16.527 [RPC0]  WARN    wallet.wallet2  src/wallet/wallet2.cpp:5327     Requested ring size 1 too low for hard fork 7, using 7
2018-05-27 14:34:16.927 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:5357     We don't use the low priority because there's a backlog in the tx pool.
2018-05-27 14:34:17.007 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:7515     Found preferred rct inputs for rct tx: 12 (1.359540955223)
// now 10minutes passed, no more logs, and request timeout.
```
## // 23minutes later
```
2018-05-27 14:57:56.703      [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:10482    Found segregation height via DNS: asicflood fork height at 1564000
2018-05-27 14:57:56.959 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:6020     5926072 unlocked outputs of size 0.000000000000
2018-05-27 14:57:56.959 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:6042     Fake output makeup: 61 requested: 19 recent, 0 pre-fork, 20 post-fork, 22 full-chain
2018-05-27 14:57:56.959 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:6103     Selecting real output: 5922082 for 0.000000000000
2018-05-27 14:57:56.959 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:6180     asking for output 1208642 for 0.000000000000
2018-05-27 14:57:56.959 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:6180     asking for output 1309089 for 0.000000000000
2018-05-27 14:57:56.959 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:6180     asking for output 1328678 for 0.000000000000
// some repeat
2018-05-27 14:57:56.961 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:6180     asking for output 5925985 for 0.000000000000
2018-05-27 14:57:57.648 [RPC0]  WARN    wallet.wallet2  src/wallet/wallet2.h:1691       amount=1.359540955223, real_output=5, real_output_in_tx_index=5, indexes: 1818566 2847584 5916112 5918901 5921313 59
22082 5922143
2018-05-27 14:57:57.701 [RPC0]  INFO    construct_tx    src/cryptonote_core/cryptonote_tx_utils.cpp:596      transaction_created: <3ac3ad0518a116f943199a49c45a83f41cfa150a8deb8fad817d105b2be110ee>
{
  "version": 2,
  "unlock_time": 0,
  "vin": [ {
      "key": {
        "amount": 0,
        "key_offsets": [ 1818566, 1029018, 3068528, 2789, 2412, 769, 61
        ],
        "k_image": "...hash..."
      }
    }
  ],
  "vout": [ {
      "amount": 0,
      "target": {
        "key": "...hash..."
      }
    }, {
      "amount": 0,
      "target": {
        "key": "...hash..."
      }
    }
  ],
  "extra": [ 2, 33, 0, 114, 176, 245, 41, 129, 82, 72, 216, 134, 56, 158, 245, 122, 189, 236, 251, 143, 139, 126, 138, 126, 237, 67, 63, 187, 73, 202, 162, 127, 239, 212, 156, 1, 126, 10, 186, 251, 74, 52
, 60, 80, 4, 132, 163, 13, 43, 233, 210, 86, 239, 113, 75, 0, 111, 42, 29, 254, 201, 176, 51, 23, 101, 155, 57, 252
  ],
  "rct_signatures": {
    "type": 1,
    "txnFee": 9418760000,
    "ecdhInfo": [ {
        "mask": "...hash...",
        "amount": "...hash..."
      }, {
        "mask": "...hash...",
        "amount": "...hash..."
      }],
    "outPk": [ "...hash...", "...hash..."]
  },
  "rctsig_prunable": {
    "rangeSigs": [ {
        "asig": "...hash...",
        "Ci": "...hash..."
      }, {
        "asig": "...hash...",
        "Ci": "...hash..."
      }],
    "MGs": [ {
        "ss": [ [ "...hash...", "...hash..."], ...hash...],
        "cc": "...hash..."
      }]
  }
}
2018-05-27 14:57:57.796 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:10482    Found segregation height via DNS: asicflood fork height at 1564000
2018-05-27 14:57:57.939 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:6020     5926072 unlocked outputs of size 0.000000000000
2018-05-27 14:57:57.939 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:6042     Fake output makeup: 61 requested: 19 recent, 0 pre-fork, 20 post-fork, 22 full-chain
2018-05-27 14:57:57.939 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:6103     Selecting real output: 5922082 for 0.000000000000
2018-05-27 14:57:57.939 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:6020     5926072 unlocked outputs of size 0.000000000000
2018-05-27 14:57:57.939 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:6042     Fake output makeup: 61 requested: 20 recent, 0 pre-fork, 20 post-fork, 21 full-chain
2018-05-27 14:57:57.939 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:6103     Selecting real output: 5886649 for 0.000000000000
2018-05-27 14:57:57.940 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:6180     asking for output 800533 for 0.000000000000
2018-05-27 14:57:57.940 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:6180     asking for output 1377552 for 0.000000000000
2018-05-27 14:57:57.940 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:6180     asking for output 1391823 for 0.000000000000
2018-05-27 14:57:57.940 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:6180     asking for output 1874926 for 0.000000000000
2018-05-27 14:57:57.940 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:6180     asking for output 2164402 for 0.000000000000
2018-05-27 14:57:57.940 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:6180     asking for output 2271851 for 0.000000000000
// some repeat
2018-05-27 14:57:57.940 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:6180     asking for output 3741305 for 0.000000000000
2018-05-27 14:57:57.942 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:6180     asking for output 5924435 for 0.000000000000
2018-05-27 14:57:57.942 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:6180     asking for output 5925480 for 0.000000000000
2018-05-27 14:57:59.128 [RPC0]  WARN    wallet.wallet2  src/wallet/wallet2.h:1691       amount=1.359540955223, real_output=5, real_output_in_tx_index=5, indexes: 4466425 4836550 5917283 5919013 5921402 59
22082 5923169
2018-05-27 14:57:59.129 [RPC0]  WARN    wallet.wallet2  src/wallet/wallet2.h:1691       amount=0.063971560000, real_output=5, real_output_in_tx_index=1, indexes: 2024350 2410335 4986972 5394067 5624422 58
86649 5909448
2018-05-27 14:57:59.186 [RPC0]  INFO    construct_tx    src/cryptonote_core/cryptonote_tx_utils.cpp:596      transaction_created: <cc0ed241d8e161f785924909ab1178517ff8faa70a24cd4c3376f4ebb7cb54e0>
{
  "version": 2,
  "unlock_time": 0,
  "vin": [ {
      "key": {
        "amount": 0,
        "key_offsets": [ 2024350, 385985, 2576637, 407095, 230355, 262227, 22799
        ],
        "k_image": "...hash..."
      }
    }, {
      "key": {
        "amount": 0,
        "key_offsets": [ 4466425, 370125, 1080733, 1730, 2389, 680, 1087
        ],
        "k_image": "...hash..."
      }
    }
  ],
  "vout": [ {
      "amount": 0,
      "target": {
        "key": "...hash..."
      }
    }, {
      "amount": 0,
      "target": {
        "key": "...hash..."
      }
    }
  ],
  "extra": [ 2, 33, 0, 114, 176, 245, 41, 129, 82, 72, 216, 134, 56, 158, 245, 122, 189, 236, 251, 143, 139, 126, 138, 126, 237, 67, 63, 187, 73, 202, 162, 127, 239, 212, 156, 1, 221, 122, 12, 136, 104, 8
8, 126, 153, 15, 20, 120, 161, 196, 163, 161, 91, 128, 38, 149, 56, 76, 109, 127, 133, 88, 126, 202, 129, 194, 25, 95, 0
  ],
  "rct_signatures": {
    "type": 2,
    "txnFee": 10143280000,
    "pseudoOuts": [ "...hash...", "...hash..."],
    "ecdhInfo": [ {
        "mask": "...hash...",
        "amount": "...hash..."
      }, {
        "mask": "...hash...",
        "amount": "...hash..."
      }],
    "outPk": [ "...hash...", "...hash..."]
  },
  "rctsig_prunable": {
    "rangeSigs": [ {
        "asig": "...hash...",
        "Ci": "...hash..."
      }, {
        "asig": "...hash...",
        "Ci": "...hash..."
      }],
    "MGs": [ {
        "ss": [ [ "...hash...", ...hash...],
        "cc": "...hash..."
      }, {
        "ss": [ [ "...hash...", "...hash..."], ...hash...],
        "cc": "...hash..."
      }]
  }
}

2018-05-27 14:57:59.220 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:7774     Done creating 1 transactions, 0.019562040000 total fee, 0.088409520000 total change
2018-05-27 14:57:59.221 [RPC0]  WARN    wallet.wallet2  src/wallet/wallet2.h:1691       amount=1.359540955223, real_output=5, real_output_in_tx_index=5, indexes: 4466425 4836550 5917283 5919013 5921402 59
22082 5923169
2018-05-27 14:57:59.221 [RPC0]  WARN    wallet.wallet2  src/wallet/wallet2.h:1691       amount=0.063971560000, real_output=5, real_output_in_tx_index=1, indexes: 2024350 2410335 4986972 5394067 5624422 58
86649 5909448

2018-05-27 14:57:59.275 [RPC0]  INFO    construct_tx    src/cryptonote_core/cryptonote_tx_utils.cpp:596      transaction_created: <8caa375f3a6ec7389c3d588653502a9f2d772ba4164f824076555ac3cdbbd2ba>
{
  "version": 2,
  "unlock_time": 0,
  "vin": [ {
      "key": {
        "amount": 0,
        "key_offsets": [ 2024350, 385985, 2576637, 407095, 230355, 262227, 22799
        ],
        "k_image": "...hash..."
      }
    }, {
      "key": {
        "amount": 0,
        "key_offsets": [ 4466425, 370125, 1080733, 1730, 2389, 680, 1087
        ],
        "k_image": "...hash..."
      }
    }
  ],
  "vout": [ {
      "amount": 0,
      "target": {
        "key": "...hash..."
      }
    }, {
      "amount": 0,
      "target": {
        "key": "...hash..."
      }
    }
  ],
"extra": [ 2, 33, 0, 114, 176, 245, 41, 129, 82, 72, 216, 134, 56, 158, 245, 122, 189, 236, 251, 143, 139, 126, 138, 126, 237, 67, 63, 187, 73, 202, 162, 127, 239, 212, 156, 1, 214, 145, 227, 231, 177,
232, 219, 13, 168, 101, 45, 61, 219, 123, 203, 67, 7, 138, 184, 62, 220, 204, 7, 21, 28, 213, 39, 176, 79, 182, 175, 114
  ],
  "rct_signatures": {
    "type": 2,
    "txnFee": 10143280000,
    "pseudoOuts": [ "...hash...", "...hash..."],
    "ecdhInfo": [ {
        "mask": "...hash...",
        "amount": "...hash..."
      }, {
        "mask": "...hash...",
        "amount": "...hash..."
      }],
    "outPk": [ "...hash...", "...hash..."]
  },
  "rctsig_prunable": {
    "rangeSigs": [ {
        "asig": "...hash...",
        "Ci": "...hash..."
      }, {
"asig": "...hash...",
        "Ci": "...hash..."
      }],
    "MGs": [ {
        "ss": [ [ "...hash...", "...hash..."], ],
        "cc": "...hash..."
      }, {
        "ss": [ [ "...hash...",...hash...],
        "cc": "...hash..."
      }]
  }
}

2018-05-27 14:57:59.296 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:7822       Transaction 1/1: 13825 bytes (14 kB), sending 1.423512515223 in 2 outputs to 1 destination(s), including 0.0101432
80000 fee, 0.075828280000 change
2018-05-27 14:57:59.373 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:4642     Transaction successfully sent. <<8caa375f3a6ec7389c3d588653502a9f2d772ba4164f824076555ac3cdbbd2ba>>
Commission: 0.010143280000 (dust sent to dust addr: 0.000000000000)
Balance: 0.075828280000
Unlocked: 0.000000000000
Please, wait for confirmation for your balance to be unlocked.
2018-05-27 14:57:59.655 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:1990     Found new pool tx: <a48f9b13b4ccc421fe1fd65409ae3fa9ff2bd0d5fc128e78f761d3adfcfdb563>
2018-05-27 14:57:59.655 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:1990     Found new pool tx: <8caa375f3a6ec7389c3d588653502a9f2d772ba4164f824076555ac3cdbbd2ba>
2018-05-27 14:57:59.655 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:2019     We sent that one
2018-05-27 14:57:59.756 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:2333     Refresh done, blocks received: 17, balance (all accounts): 0.075828280000, unlocked: 0.000000000000
2018-05-27 14:58:19.955 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:1990     Found new pool tx: <8caa375f3a6ec7389c3d588653502a9f2d772ba4164f824076555ac3cdbbd2ba>
2018-05-27 14:58:19.955 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:2019     We sent that one
2018-05-27 14:58:19.955 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:1990     Found new pool tx: <907ce76e17c6505964e2057ebf5f884706e2cc9b8aad280912ef866ba842eef0>
2018-05-27 14:58:20.056 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:2333     Refresh done, blocks received: 1, balance (all accounts): 0.075828280000, unlocked: 0.000000000000
2018-05-27 14:58:40.255 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:1990     Found new pool tx: <8caa375f3a6ec7389c3d588653502a9f2d772ba4164f824076555ac3cdbbd2ba>
2018-05-27 14:58:40.255 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:2019     We sent that one
```

## result
I can now see that the transaction <8caa375f3a6ec7389c3d588653502a9f2d772ba4164f824076555ac3cdbbd2ba> has been broadcast

@moneromooo-monero  
Is this information useful?



## moneromooo-monero | 2018-05-27T14:56:08+00:00
That wallet log looks like the slow RPC indeed.

In monero-wallet-cli, when you run "set", what is the value of segregation-height ?

What is the output of: dig -t TXT segheights.moneropulse.se


## wwaayyaa | 2018-05-27T15:25:53+00:00
@moneromooo-monero 
### cli setting
```
[wallet 48mHgh]: set
seed = English
always-confirm-transfers = 1
print-ring-members = 0
store-tx-info = 1
default-ring-size = 0
auto-refresh = 1
refresh-type = optimize-coinbase
priority = 0
confirm-missing-payment-id = 1
ask-password = 1
unit = monero
min-outputs-count = 0
min-outputs-value = 0.000000000000
merge-destinations = 0
confirm-backlog = 1
confirm-backlog-threshold = 0
confirm-export-overwrite = 1
refresh-from-block-height = 1550963
auto-low-priority = 1
segregate-pre-fork-outputs = 1
key-reuse-mitigation2 = 1
subaddress-lookahead = 50:200
segregation-height = 0
```

### dig
```
dig -t TXT segheights.moneropulse.se

; <<>> DiG 9.10.3-P4-Ubuntu <<>> -t TXT segheights.moneropulse.se
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 59413
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 4096
;; QUESTION SECTION:
;segheights.moneropulse.se.     IN      TXT

;; ANSWER SECTION:
segheights.moneropulse.se. 300  IN      TXT     "asicflood:1564000"

;; Query time: 2 msec
;; SERVER: 100.100.2.138#53(100.100.2.138)
;; WHEN: Sun May 27 23:25:38 CST 2018
;; MSG SIZE  rcvd: 84
```



## moneromooo-monero | 2018-05-27T15:35:56+00:00
All looking as expected. I'm confused why it'd be so slow then.


## wwaayyaa | 2018-05-27T15:41:19+00:00
I am also puzzled

## wwaayyaa | 2018-05-27T16:29:04+00:00
hope someone can help me. I need to make a few transactions every day. It wastes me a lot of time. I am very upset now. 
thanks.

## moneromooo-monero | 2018-05-27T18:01:15+00:00
I've added some logs in https://github.com/moneromooo-monero/bitmonero/tree/ogo-logs
This is on top of the 0.12 branch so you can use that directly. The interesting logs will be printed on default log level by monerod.

## wwaayyaa | 2018-05-28T05:32:12+00:00
@moneromooo-monero 
i got some error with your branch .
```
[ 68%] Built target performance_tests
[ 68%] Building CXX object tests/core_tests/CMakeFiles/core_tests.dir/ring_signature_1.cpp.o
[ 68%] Building CXX object tests/core_tests/CMakeFiles/core_tests.dir/transaction_tests.cpp.o
make[3]: Entering directory '/work/moneromooo-monero/build/release'
make[3]: Leaving directory '/work/moneromooo-monero/build/release'
[ 69%] Built target difficulty-tests
[ 70%] Building CXX object tests/core_tests/CMakeFiles/core_tests.dir/tx_validation.cpp.o
make[3]: Entering directory '/work/moneromooo-monero/build/release'
make[3]: Leaving directory '/work/moneromooo-monero/build/release'
make[3]: Entering directory '/work/moneromooo-monero/build/release'
[ 70%] Linking CXX executable net_load_tests_clt
/usr/bin/ld: /usr/lib/gcc/x86_64-linux-gnu/5/../../../../lib/libgtest.a(gtest-all.cc.o): relocation R_X86_64_32 against `.rodata' can not be used when making a shared object; recompile with -fPIC
/usr/lib/gcc/x86_64-linux-gnu/5/../../../../lib/libgtest.a: error adding symbols: Bad value
collect2: error: ld returned 1 exit status
tests/net_load_tests/CMakeFiles/net_load_tests_clt.dir/build.make:129: recipe for target 'tests/net_load_tests/net_load_tests_clt' failed
make[3]: *** [tests/net_load_tests/net_load_tests_clt] Error 1
make[3]: Leaving directory '/work/moneromooo-monero/build/release'
CMakeFiles/Makefile2:4583: recipe for target 'tests/net_load_tests/CMakeFiles/net_load_tests_clt.dir/all' failed
make[2]: *** [tests/net_load_tests/CMakeFiles/net_load_tests_clt.dir/all] Error 2
make[2]: *** Waiting for unfinished jobs....
[ 70%] Building CXX object tests/core_tests/CMakeFiles/core_tests.dir/v2_tests.cpp.o
[ 70%] Building CXX object tests/core_tests/CMakeFiles/core_tests.dir/rct.cpp.o
[ 71%] Linking CXX executable core_tests
make[3]: Leaving directory '/work/moneromooo-monero/build/release'
[ 71%] Built target core_tests
make[2]: Leaving directory '/work/moneromooo-monero/build/release'
Makefile:138: recipe for target 'all' failed
make[1]: *** [all] Error 2
make[1]: Leaving directory '/work/moneromooo-monero/build/release'
Makefile:64: recipe for target 'release-all' failed
make: *** [release-all] Error 2
```

## stoffu | 2018-05-28T05:41:32+00:00
As the error message says:

> libgtest.a(gtest-all.cc.o): relocation R_X86_64_32 against `.rodata' can not be used when making a shared object; recompile with -fPIC

Your system's gtest wasn't built using -fPIC causing the error. You can simply uninstall it from your system and let CMake build the vendored GTest with -fPIC. Alternatively, you can omit building tests by `make release` or `make release-static`.


## wwaayyaa | 2018-05-28T08:15:25+00:00
@stoffu  thank you,i remove libgtest-dev and built successful.

## wwaayyaa | 2018-05-28T08:34:08+00:00
@moneromooo-monero 
i use your branch monerod with --log-level 0, and logs has ```Monero 'Lithium Luna' (v0.12.1.0-master-cbd74ce)``` 

## monerod 
```
 ./monerod --p2p-bind-ip=0.0.0.0 --p2p-bind-port=xxxx --rpc-bind-ip=0.0.0.0 --rpc-bind-port=xxxx --non-interactive --confirm-external-bind  --data-dir /work/monero-data/monero --config-file /work/monero-data/config.conf  --disable-dns-checkpoint --check-updates=disabled --log-level 0 --log-file /work/monero-debug/monerod.log
2018-05-28 08:24:47.443     7fb060843780        INFO    global  src/daemon/main.cpp:279 Monero 'Lithium Luna' (v0.12.1.0-master-cbd74ce)
2018-05-28 08:24:47.443     7fb060843780        INFO    global  src/daemon/protocol.h:53        Initializing cryptonote protocol...
2018-05-28 08:24:47.443     7fb060843780        INFO    global  src/daemon/protocol.h:58        Cryptonote protocol initialized OK
2018-05-28 08:24:47.444     7fb060843780        INFO    global  src/daemon/p2p.h:63     Initializing p2p server...
2018-05-28 08:25:11.454     7fb060843780        INFO    global  src/daemon/p2p.h:68     p2p server initialized OK
2018-05-28 08:25:11.454     7fb060843780        INFO    global  src/daemon/rpc.h:63     Initializing core RPC server...
2018-05-28 08:25:11.454     7fb060843780        INFO    global  contrib/epee/include/net/http_server_impl_base.h:76   Binding on 0.0.0.0:18081
2018-05-28 08:25:11.454     7fb060843780        INFO    global  src/daemon/rpc.h:69     core RPC server initialized OK on port: 18081
2018-05-28 08:25:11.454     7fb060843780        INFO    global  src/daemon/core.h:86    Initializing core...
2018-05-28 08:25:11.455     7fb060843780        INFO    global  src/cryptonote_core/cryptonote_core.cpp:427   Loading blockchain from folder /work/monero-data/monero/lmdb ...
2018-05-28 08:25:11.504     7fb060843780        INFO    global  src/cryptonote_core/cryptonote_core.cpp:525   Loading checkpoints
2018-05-28 08:25:11.504     7fb060843780        INFO    global  src/daemon/core.h:92    Core initialized OK
2018-05-28 08:25:11.504     7fb060843780        INFO    global  src/daemon/rpc.h:74     Starting core RPC server...
2018-05-28 08:25:11.504 [SRV_MAIN]      INFO    global  src/daemon/rpc.h:79     core RPC server started ok
2018-05-28 08:25:11.505 [SRV_MAIN]      INFO    global  src/daemon/p2p.h:78     Starting p2p net loop...
2018-05-28 08:25:12.505 [P2P1]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1353
**********************************************************************
The daemon will start synchronizing with the network. This may take a long time to complete.

You can set the level of process detailization through "set_log <level|categories>" command,
where <level> is between 0 (no details) and 4 (very verbose), or custom category based levels (eg, *:WARNING).

Use the "help" command to see the list of available commands.
Use "help <command>" to see a command's documentation.
**********************************************************************
2018-05-28 08:25:13.744 [P2P1]  INFO    global  src/cryptonote_core/blockchain.cpp:1528 ----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 1581881
id:     <7109e6c518717d56f4ea9eb58812f03b98363dbcf78cd8a613df74523d854886>
PoW:    <d3c693d2083888c03bc8dfbca4f32d9692e094722d8cbf4a90aa4c1400000000>
difficulty:     50454937567
2018-05-28 08:25:13.772 [P2P1]  INFO    global  src/cryptonote_core/blockchain.cpp:1528 ----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 1581882
id:     <fade9c6c28337e945198e747d391f9e57d725e1def6d9c7cf99edfb7e32865ac>
PoW:    <c1ca2169cf89d7d4dc76fc7b86c1dc012c4567ff5eb0651ee8736a0b00000000>
difficulty:     50327383695
2018-05-28 08:25:13.799 [P2P1]  INFO    global  src/cryptonote_core/blockchain.cpp:1528 ----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 1581883
id:     <21bd3e12be99b5155193797996a77c96de2fe55bafdb60abcb6a6957abe22232>
PoW:    <7f4089a4d9c01173c77e9bb506fbadd8810bd43520f2371da7cb540200000000>
difficulty:     50328137674
2018-05-28 08:25:13.826 [P2P1]  INFO    global  src/cryptonote_core/blockchain.cpp:1528 ----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 1581884
id:     <869782996021166249c8894afd91eeff6b4fc981c42e58a44e80c23db503f625>
PoW:    <e3ee2aa3cf476db4362a03dfb445ebc50868827de74c9a47c379be0700000000>
difficulty:     50287474850
2018-05-28 08:25:13.852 [P2P1]  INFO    global  src/cryptonote_core/blockchain.cpp:1528 ----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 1581885
id:     <1a3573e19dd618d463feb05ac131924c487e0ffe427e475c0a28ac3d78567265>
PoW:    <83023ae3dae254d2294305b304d930007c69c209ac82745b273a560000000000>
difficulty:     50232957166
2018-05-28 08:25:13.878 [P2P1]  INFO    global  src/cryptonote_core/blockchain.cpp:1528 ----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 1581886
id:     <f0f5b8d1f64e3675461be86ba8dd579e3b2c52d0c442ddbadbedee382632bdb6>
PoW:    <d0617609bf78e503591add05f412e6354101886635ed5d54b0e76d1300000000>
difficulty:     50431113356
2018-05-28 08:25:13.904 [P2P1]  INFO    global  src/cryptonote_core/blockchain.cpp:1528 ----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 1581887
id:     <ce5ad40194fddb26d14eca5e4b560010124de5508160bbd21ce14601b41241bc>
PoW:    <2e0157e844c1c6d22995259e09176f3d67d7a0dbe1e02c2a66c5431100000000>
difficulty:     50433581067
2018-05-28 08:25:13.905 [P2P1]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1560  SYNCHRONIZED OK
2018-05-28 08:25:13.905 [P2P1]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1582
**********************************************************************
You are now synchronized with the network. You may now start monero-wallet-cli.

Use the "help" command to see the list of available commands.
**********************************************************************
2018-05-28 08:25:14.268 [P2P5]  INFO    global  src/cryptonote_core/blockchain.cpp:1528 ----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 1580196
id:     <67b6cb49425c849dc3d46e6cb279e5afec020dd3c066341c9b6748ffd5c2079b>
PoW:    <e366f3fe48427dcefe2c03ec43fcf9525d8da328d6905ea7b9d9ea0600000000>
difficulty:     50576146473
2018-05-28 08:25:14.294 [P2P5]  INFO    global  src/cryptonote_core/blockchain.cpp:1528 ----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 1580197
id:     <521ad1dbcf0a02a9eff25802564bdb4fc47b7533251109aec581af274e6d0656>
PoW:    <c67fc60330afe0362bbd440c9bcfa9676bf2a2373f8f7efd563bf30900000000>
difficulty:     50763612025
2018-05-28 08:25:14.319 [P2P5]  INFO    global  src/cryptonote_core/blockchain.cpp:1528 ----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 1580198
id:     <dc9e43f1a549979c7474d9af6cf49d2e100bb8c8c08c8d5063a6c11f30f97ee4>
PoW:    <878b376a2f2166d9ad06e2e5ba71f0a1f13d60a3cafd793f17c9e00100000000>
difficulty:     50727772038
2018-05-28 08:25:14.345 [P2P5]  INFO    global  src/cryptonote_core/blockchain.cpp:1528 ----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 1580199
id:     <5a0e107670a7240439aebdb5ad01d680a1f5cb7401b81f2ee989e288c1e58548>
PoW:    <dce1dec0e25772a4a02a5e33c4aa0ea237eaafb5b83d6d6734f1b40e00000000>
difficulty:     50718302137
2018-05-28 08:25:14.372 [P2P5]  INFO    global  src/cryptonote_core/blockchain.cpp:1528 ----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 1580200
id:     <dca863d171e35c2e8c0e7dd982799f677b1e920313036036bcf5daf33fbba9c5>
PoW:    <8fa359c891ccf7414cb6714edcb29a238421a87898b07a3b2ab1660200000000>

// .....
//  same block info 

2018-05-28 08:25:15.026 [P2P5]  INFO    global  src/cryptonote_core/blockchain.cpp:1528 ----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 1580225
id:     <38100f5b262b768d2f015b2db95dc8cf89428565d805085a58d9b706769d9307>
PoW:    <f9d54a23254878cb0f32d6a0e0e9459284e5e406c3b783eeaa0c3b1300000000>
difficulty:     50104776174
2018-05-28 08:25:15.053 [P2P5]  INFO    global  src/cryptonote_core/blockchain.cpp:1528 ----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 1580226
id:     <7fbf3f247c2453cc7f0e289339bc8ded557db88bb628bb102627764dfc2d72d8>
PoW:    <0659f8e5dbb91147dd46ba030a6571d2748301999d57d5a7fcf5a10e00000000>
difficulty:     50196839822
2018-05-28 08:25:15.811 [P2P2]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1560  SYNCHRONIZED OK
2018-05-28 08:25:16.674 [P2P5]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:310   [92.53.90.28:18080 OUT] Sync data returned a new top block candidate: 1582479 -> 1582480 [Your node is 1 blocks (0 days) behind]
SYNCHRONIZATION started
2018-05-28 08:25:18.884 [P2P3]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1170  [92.53.90.28:18080 OUT]  Synced 1582480/1582480
2018-05-28 08:25:18.884 [P2P3]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1560  SYNCHRONIZED OK

// 10 mimutes later, no more logs, and cli already enter "No payment id is included with this transaction. Is this okay?  (Y/Yes/N/No): y", 

2018-05-28 08:34:10.154 [P2P4]  INFO    global  src/cryptonote_core/blockchain.cpp:1528 ----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 1581888
id:     <9d1e707347b528b6b4e5dfcc15a59b22634b94b26524efcda954d9106a99e12e>
PoW:    <0a9ebeb25ba37aedc0aadb5fbe5aa30c609bfe850083cf51a780a80f00000000>
difficulty:     50399794788
// this is all.

```
finally, no more logs about transfer.


## cli 
```
[wallet 442zNf]: transfer 442zNfHF32k2YgmAv4ZUVpd47T7cF7jxk6K8WqvEuQkn73mnhuLm5X5HkJVWrxSyfwYTrSWznJ1N7RJAb5PMAMR8GKd2za5 0.01
Wallet password:
No payment id is included with this transaction. Is this okay?  (Y/Yes/N/No): y
//30minutes passed
There is currently a 1 block backlog at that fee level. Is this okay?  (Y/Yes/N/No): y

Transaction 1/1:
Spending from address index 0
Sending 0.010000000000.  The transaction fee is 0.002352350000
Is this okay?  (Y/Yes/N/No): y
Transaction successfully submitted, transaction <669e6346df2fcd7473e9290548e47bf0b8e0de89d2e06f8ac059b0ac5b3943e7>
You can check its status by using the `show_transfers` command.
```

is the --log-level setting wrong?
------
sorry , i paste the monerod.log, please wait.

## moneromooo-monero | 2018-05-28T10:05:32+00:00
Sorry, I was wrong, they'll show up with --log-level 0,daemon.rpc:INFO


## wwaayyaa | 2018-05-28T10:11:34+00:00
@moneromooo-monero 
i use your branch monerod with --log-level 0, and logs has ```Monero 'Lithium Luna' (v0.12.1.0-master-cbd74ce)``` 

i find 2 error.
1. Exception: cryptonote::BLOCK_DNE      - Very much 
1. Exception: boost::thread_interrupted    - just once

## monerod.log details
```
 ./monerod --p2p-bind-ip=0.0.0.0 --p2p-bind-port=xxxx --rpc-bind-ip=0.0.0.0 --rpc-bind-port=xxxx --non-interactive --confirm-external-bind  --data-dir /work/monero-data/monero --config-file /work/monero-data/config.conf  --disable-dns-checkpoint --check-updates=disabled --log-level 0 --log-file /work/monero-debug/monerod.log
2018-05-28 08:24:47.443     7fb060843780        INFO    global  src/daemon/main.cpp:279 Monero 'Lithium Luna' (v0.12.1.0-master-cbd74ce)
2018-05-28 08:24:47.443     7fb060843780        INFO    global  src/daemon/protocol.h:53        Initializing cryptonote protocol...
2018-05-28 08:24:47.443     7fb060843780        INFO    global  src/daemon/protocol.h:58        Cryptonote protocol initialized OK
2018-05-28 08:24:47.444     7fb060843780        INFO    global  src/daemon/p2p.h:63     Initializing p2p server...
2018-05-28 08:25:11.454     7fb060843780        INFO    global  src/daemon/p2p.h:68     p2p server initialized OK
2018-05-28 08:25:11.454     7fb060843780        INFO    global  src/daemon/rpc.h:63     Initializing core RPC server...
2018-05-28 08:25:11.454     7fb060843780        INFO    global  contrib/epee/include/net/http_server_impl_base.h:76   Binding on 0.0.0.0:18081
2018-05-28 08:25:11.454     7fb060843780        INFO    global  src/daemon/rpc.h:69     core RPC server initialized OK on port: 18081
2018-05-28 08:25:11.454     7fb060843780        INFO    global  src/daemon/core.h:86    Initializing core...
2018-05-28 08:25:11.455     7fb060843780        INFO    global  src/cryptonote_core/cryptonote_core.cpp:427   Loading blockchain from folder /work/monero-data/monero/lmdb ...
2018-05-28 08:25:11.504     7fb060843780        INFO    global  src/cryptonote_core/cryptonote_core.cpp:525   Loading checkpoints
2018-05-28 08:25:11.504     7fb060843780        INFO    global  src/daemon/core.h:92    Core initialized OK
2018-05-28 08:25:11.504     7fb060843780        INFO    global  src/daemon/rpc.h:74     Starting core RPC server...
2018-05-28 08:25:11.504 [SRV_MAIN]      INFO    global  src/daemon/rpc.h:79     core RPC server started ok
2018-05-28 08:25:11.505 [SRV_MAIN]      INFO    global  src/daemon/p2p.h:78     Starting p2p net loop...
2018-05-28 08:25:12.505 [P2P1]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1353
**********************************************************************
The daemon will start synchronizing with the network. This may take a long time to complete.

You can set the level of process detailization through "set_log <level|categories>" command,
where <level> is between 0 (no details) and 4 (very verbose), or custom category based levels (eg, *:WARNING).

Use the "help" command to see the list of available commands.
Use "help <command>" to see a command's documentation.
**********************************************************************
2018-05-28 08:25:13.744 [P2P1]  INFO    global  src/cryptonote_core/blockchain.cpp:1528 ----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 1581881
id:     <7109e6c518717d56f4ea9eb58812f03b98363dbcf78cd8a613df74523d854886>
PoW:    <d3c693d2083888c03bc8dfbca4f32d9692e094722d8cbf4a90aa4c1400000000>
difficulty:     50454937567
2018-05-28 08:25:13.772 [P2P1]  INFO    global  src/cryptonote_core/blockchain.cpp:1528 ----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 1581882
id:     <fade9c6c28337e945198e747d391f9e57d725e1def6d9c7cf99edfb7e32865ac>
PoW:    <c1ca2169cf89d7d4dc76fc7b86c1dc012c4567ff5eb0651ee8736a0b00000000>
difficulty:     50327383695
2018-05-28 08:25:13.799 [P2P1]  INFO    global  src/cryptonote_core/blockchain.cpp:1528 ----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 1581883
id:     <21bd3e12be99b5155193797996a77c96de2fe55bafdb60abcb6a6957abe22232>
PoW:    <7f4089a4d9c01173c77e9bb506fbadd8810bd43520f2371da7cb540200000000>
difficulty:     50328137674
2018-05-28 08:25:13.826 [P2P1]  INFO    global  src/cryptonote_core/blockchain.cpp:1528 ----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 1581884
id:     <869782996021166249c8894afd91eeff6b4fc981c42e58a44e80c23db503f625>
PoW:    <e3ee2aa3cf476db4362a03dfb445ebc50868827de74c9a47c379be0700000000>
difficulty:     50287474850
2018-05-28 08:25:13.852 [P2P1]  INFO    global  src/cryptonote_core/blockchain.cpp:1528 ----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 1581885
id:     <1a3573e19dd618d463feb05ac131924c487e0ffe427e475c0a28ac3d78567265>
PoW:    <83023ae3dae254d2294305b304d930007c69c209ac82745b273a560000000000>
difficulty:     50232957166
2018-05-28 08:25:13.878 [P2P1]  INFO    global  src/cryptonote_core/blockchain.cpp:1528 ----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 1581886
id:     <f0f5b8d1f64e3675461be86ba8dd579e3b2c52d0c442ddbadbedee382632bdb6>
PoW:    <d0617609bf78e503591add05f412e6354101886635ed5d54b0e76d1300000000>
difficulty:     50431113356
2018-05-28 08:25:13.904 [P2P1]  INFO    global  src/cryptonote_core/blockchain.cpp:1528 ----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 1581887
id:     <ce5ad40194fddb26d14eca5e4b560010124de5508160bbd21ce14601b41241bc>
PoW:    <2e0157e844c1c6d22995259e09176f3d67d7a0dbe1e02c2a66c5431100000000>
difficulty:     50433581067
2018-05-28 08:25:13.905 [P2P1]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1560  SYNCHRONIZED OK
2018-05-28 08:25:13.905 [P2P1]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1582
**********************************************************************
You are now synchronized with the network. You may now start monero-wallet-cli.

Use the "help" command to see the list of available commands.
**********************************************************************
2018-05-28 08:25:14.268 [P2P5]  INFO    global  src/cryptonote_core/blockchain.cpp:1528 ----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 1580196
id:     <67b6cb49425c849dc3d46e6cb279e5afec020dd3c066341c9b6748ffd5c2079b>
PoW:    <e366f3fe48427dcefe2c03ec43fcf9525d8da328d6905ea7b9d9ea0600000000>
difficulty:     50576146473
2018-05-28 08:25:14.294 [P2P5]  INFO    global  src/cryptonote_core/blockchain.cpp:1528 ----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 1580197
id:     <521ad1dbcf0a02a9eff25802564bdb4fc47b7533251109aec581af274e6d0656>
PoW:    <c67fc60330afe0362bbd440c9bcfa9676bf2a2373f8f7efd563bf30900000000>
difficulty:     50763612025
2018-05-28 08:25:14.319 [P2P5]  INFO    global  src/cryptonote_core/blockchain.cpp:1528 ----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 1580198
id:     <dc9e43f1a549979c7474d9af6cf49d2e100bb8c8c08c8d5063a6c11f30f97ee4>
PoW:    <878b376a2f2166d9ad06e2e5ba71f0a1f13d60a3cafd793f17c9e00100000000>
difficulty:     50727772038
2018-05-28 08:25:14.345 [P2P5]  INFO    global  src/cryptonote_core/blockchain.cpp:1528 ----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 1580199
id:     <5a0e107670a7240439aebdb5ad01d680a1f5cb7401b81f2ee989e288c1e58548>
PoW:    <dce1dec0e25772a4a02a5e33c4aa0ea237eaafb5b83d6d6734f1b40e00000000>
difficulty:     50718302137
2018-05-28 08:25:14.372 [P2P5]  INFO    global  src/cryptonote_core/blockchain.cpp:1528 ----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 1580200
id:     <dca863d171e35c2e8c0e7dd982799f677b1e920313036036bcf5daf33fbba9c5>
PoW:    <8fa359c891ccf7414cb6714edcb29a238421a87898b07a3b2ab1660200000000>

// .....
//  same block info 

2018-05-28 08:25:15.026 [P2P5]  INFO    global  src/cryptonote_core/blockchain.cpp:1528 ----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 1580225
id:     <38100f5b262b768d2f015b2db95dc8cf89428565d805085a58d9b706769d9307>
PoW:    <f9d54a23254878cb0f32d6a0e0e9459284e5e406c3b783eeaa0c3b1300000000>
difficulty:     50104776174
2018-05-28 08:25:15.053 [P2P5]  INFO    global  src/cryptonote_core/blockchain.cpp:1528 ----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 1580226
id:     <7fbf3f247c2453cc7f0e289339bc8ded557db88bb628bb102627764dfc2d72d8>
PoW:    <0659f8e5dbb91147dd46ba030a6571d2748301999d57d5a7fcf5a10e00000000>
difficulty:     50196839822
2018-05-28 08:25:15.811 [P2P2]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1560  SYNCHRONIZED OK
2018-05-28 08:25:16.674 [P2P5]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:310   [92.53.90.28:18080 OUT] Sync data returned a new top block candidate: 1582479 -> 1582480 [Your node is 1 blocks (0 days) behind]
SYNCHRONIZATION started
2018-05-28 08:25:18.884 [P2P3]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1170  [92.53.90.28:18080 OUT]  Synced 1582480/1582480
2018-05-28 08:25:18.884 [P2P3]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1560  SYNCHRONIZED OK

2018-05-28 08:27:15.918 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:124  Exception: cryptonote::BLOCK_DNE
2018-05-28 08:27:15.919 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:125  Unwound call stack:
2018-05-28 08:27:15.922 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:163      [1] ./monerod:__cxa_throw+0x10e [0x55bd4280c7ce]
2018-05-28 08:27:15.922 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:163      [2] ./monerod+0x3e3bd9 [0x55bd42734bd9]
2018-05-28 08:27:15.922 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:163      [3] ./monerod:cryptonote::BlockchainLMDB::get_block_height(crypto::hash const&) const+0x437 [0x55bd42742c77]
2018-05-28 08:27:15.922 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:163      [4] ./monerod:cryptonote::BlockchainLMDB::get_block_blob[abi:cxx11](crypto::hash const&) const+0x144 [0x55bd4273
59b4]
2018-05-28 08:27:15.922 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:163      [5] ./monerod:bool cryptonote::Blockchain::get_blocks<std::__cxx11::list<crypto::hash, std::allocator<crypto::ha
sh> >, std::__cxx11::list<std::pair<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, cryptonote::block>, std::allocator<std::pair<std::__cxx11::basic_string<char, std::char
_traits<char>, std::allocator<char> >, cryptonote::block> > >, std::__cxx11::list<crypto::hash, std::allocator<crypto::hash> > >(std::__cxx11::list<crypto::hash, std::allocator<crypto::hash> > const&, std
::__cxx11::list<std::pair<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, cryptonote::block>, std::allocator<std::pair<std::__cxx11::basic_string<char, std::char_traits<ch
ar>, std::allocator<char> >, cryptonote::block> > >&, std::__cxx11::list<crypto::hash, std::allocator<crypto::hash> >&) const+0x1f1 [0x55bd427996d1]
2018-05-28 08:27:15.922 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:163      [6] ./monerod:cryptonote::Blockchain::handle_get_objects(cryptonote::NOTIFY_REQUEST_GET_OBJECTS::request&, crypt
onote::NOTIFY_RESPONSE_GET_OBJECTS::request&)+0x1de [0x55bd427806de]
2018-05-28 08:27:15.922 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:163      [7] ./monerod:cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::handle_request_get_objects(int, crypt
onote::NOTIFY_REQUEST_GET_OBJECTS::request&, cryptonote::cryptonote_connection_context&)+0x18f [0x55bd426f974f]
2018-05-28 08:27:15.922 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:163      [8] ./monerod:int epee::net_utils::buff_to_t_adapter<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>
, cryptonote::NOTIFY_REQUEST_GET_OBJECTS::request, cryptonote::cryptonote_connection_context, boost::_bi::bind_t<int, boost::_mfi::mf3<int, cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, int
, cryptonote::NOTIFY_REQUEST_GET_OBJECTS::request&, cryptonote::cryptonote_connection_context&>, boost::_bi::list4<boost::_bi::value<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*>, boost::a
rg<1>, boost::arg<2>, boost::arg<3> > > >(cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, boost::
_bi::bind_t<int, boost::_mfi::mf3<int, cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, int, cryptonote::NOTIFY_REQUEST_GET_OBJECTS::request&, cryptonote::cryptonote_connection_context&>, boos
t::_bi::list4<boost::_bi::value<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*>, boost::arg<1>, boost::arg<2>, boost::arg<3> > >, cryptonote::cryptonote_connection_context&)+0x24f [0x55bd425
83aff]
2018-05-28 08:27:15.922 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:163      [9] ./monerod:int cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::handle_invoke_map<cryptonote::cry
ptonote_connection_context>(bool, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char>
 >&, cryptonote::cryptonote_connection_context&, bool&)+0x2aa [0x55bd425932aa]
2018-05-28 08:27:15.922 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:163      [10] ./monerod:int nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::handle_invoke_map<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >(bool, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&, bool&)+0xc2 [0x55bd42593532]
2018-05-28 08:27:15.922 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:163      [11] ./monerod:nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::notify(int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&)+0x50 [0x55bd42593900]
2018-05-28 08:27:15.922 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:163      [12] ./monerod:epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >::handle_recv(void const*, unsigned long)+0x4ad [0x55bd42715a0d]
2018-05-28 08:27:15.922 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:163      [13] ./monerod:epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::handle_read(boost::system::error_code const&, unsigned long)+0x1f8 [0x55bd4272d948]
2018-05-28 08:27:15.922 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:163      [14] ./monerod:void boost::asio::detail::strand_service::dispatch<boost::asio::detail::binder2<boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::system::error_code, unsigned long> >(boost::asio::detail::strand_service::strand_impl*&, boost::asio::detail::binder2<boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::system::error_code, unsigned long>&)+0x7a [0x55bd426f665a]
2018-05-28 08:27:15.922 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:163      [15] ./monerod:boost::asio::detail::completion_handler<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > > >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long)+0x188 [0x55bd426f6ac8]
2018-05-28 08:27:15.922 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:163      [16] ./monerod:void boost::asio::detail::strand_service::dispatch<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > > >(boost::asio::detail::strand_service::strand_impl*&, boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > >&)+0x226 [0x55bd426f6eb6]
2018-05-28 08:27:15.922 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:163      [17] ./monerod:boost::asio::detail::reactive_socket_recv_op<boost::asio::mutable_buffers_1, boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running> >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long)+0x253 [0x55bd426f7193]
2018-05-28 08:27:15.922 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:163      [18] ./monerod:boost::asio::detail::epoll_reactor::descriptor_state::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long)+0x1f4 [0x55bd42512924]
2018-05-28 08:27:15.922 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:163      [19] ./monerod:epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread()+0x854 [0x55bd426daf74]
2018-05-28 08:27:15.922 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:163      [20] /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0+0x115d5 [0x7fb05e4175d5]
2018-05-28 08:27:15.922 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:163      [21] /lib/x86_64-linux-gnu/libpthread.so.0+0x76ba [0x7fb05dc586ba]
2018-05-28 08:27:15.922 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:163      [22] /lib/x86_64-linux-gnu/libc.so.6:clone+0x6d [0x7fb05d98e41d]
2018-05-28 08:27:15.922 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:163
2018-05-28 08:27:15.922 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:124  Exception: cryptonote::BLOCK_DNE
2018-05-28 08:27:15.922 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:125  Unwound call stack:
2018-05-28 08:27:15.925 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:163      [1] ./monerod:__cxa_throw+0x10e [0x55bd4280c7ce]
2018-05-28 08:27:15.925 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:163      [2] ./monerod+0x3e3bd9 [0x55bd42734bd9]
2018-05-28 08:27:15.925 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:163      [3] ./monerod:cryptonote::BlockchainLMDB::get_block_height(crypto::hash const&) const+0x437 [0x55bd42742c77]
2018-05-28 08:27:15.925 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:163      [4] ./monerod:cryptonote::BlockchainLMDB::get_block_blob[abi:cxx11](crypto::hash const&) const+0x144 [0x55bd427359b4]
2018-05-28 08:27:15.925 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:163      [5] ./monerod:bool cryptonote::Blockchain::get_blocks<std::__cxx11::list<crypto::hash, std::allocator<crypto::hash> >, std::__cxx11::list<std::pair<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, cryptonote::block>, std::allocator<std::pair<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, cryptonote::block> > >, std::__cxx11::list<crypto::hash, std::allocator<crypto::hash> > >(std::__cxx11::list<crypto::hash, std::allocator<crypto::hash> > const&, std::__cxx11::list<std::pair<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, cryptonote::block>, std::allocator<std::pair<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, cryptonote::block> > >&, std::__cxx11::list<crypto::hash, std::allocator<crypto::hash> >&) const+0x1f1 [0x55bd427996d1]
2018-05-28 08:27:15.925 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:163      [6] ./monerod:cryptonote::Blockchain::handle_get_objects(cryptonote::NOTIFY_REQUEST_GET_OBJECTS::request&, cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request&)+0x1de [0x55bd427806de]
2018-05-28 08:27:15.925 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:163      [7] ./monerod:cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::handle_request_get_objects(int, cryptonote::NOTIFY_REQUEST_GET_OBJECTS::request&, cryptonote::cryptonote_connection_context&)+0x18f [0x55bd426f974f]
2018-05-28 08:27:15.925 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:163      [8] ./monerod:int epee::net_utils::buff_to_t_adapter<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, cryptonote::NOTIFY_REQUEST_GET_OBJECTS::request, cryptonote::cryptonote_connection_context, boost::_bi::bind_t<int, boost::_mfi::mf3<int, cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, int, cryptonote::NOTIFY_REQUEST_GET_OBJECTS::request&, cryptonote::cryptonote_connection_context&>, boost::_bi::list4<boost::_bi::value<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*>, boost::arg<1>, boost::arg<2>, boost::arg<3> > > >(cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, boost::_bi::bind_t<int, boost::_mfi::mf3<int, cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, int, cryptonote::NOTIFY_REQUEST_GET_OBJECTS::request&, cryptonote::cryptonote_connection_context&>, boost::_bi::list4<boost::_bi::value<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*>, boost::arg<1>, boost::arg<2>, boost::arg<3> > >, cryptonote::cryptonote_connection_context&)+0x24f [0x55bd42583aff]
2018-05-28 08:27:15.925 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:163      [9] ./monerod:int cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::handle_invoke_map<cryptonote::cryptonote_connection_context>(bool, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&, cryptonote::cryptonote_connection_context&, bool&)+0x2aa [0x55bd425932aa]
2018-05-28 08:27:15.925 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:163      [10] ./monerod:int nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::handle_invoke_map<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >(bool, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&, bool&)+0xc2 [0x55bd42593532]
2018-05-28 08:27:15.925 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:163      [11] ./monerod:nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::notify(int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&)+0x50 [0x55bd42593900]
2018-05-28 08:27:15.925 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:163      [12] ./monerod:epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >::handle_recv(void const*, unsigned long)+0x4ad [0x55bd42715a0d]
2018-05-28 08:27:15.925 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:163      [13] ./monerod:epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::handle_read(boost::system::error_code const&, unsigned long)+0x1f8 [0x55bd4272d948]
2018-05-28 08:27:15.925 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:163      [14] ./monerod:void boost::asio::detail::strand_service::dispatch<boost::asio::detail::binder2<boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::system::error_code, unsigned long> >(boost::asio::detail::strand_service::strand_impl*&, boost::asio::detail::binder2<boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::system::error_code, unsigned long>&)+0x7a [0x55bd426f665a]
2018-05-28 08:27:15.925 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:163      [15] ./monerod:boost::asio::detail::completion_handler<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > > >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long)+0x188 [0x55bd426f6ac8]
2018-05-28 08:27:15.925 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:163      [16] ./monerod:void boost::asio::detail::strand_service::dispatch<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > > >(boost::asio::detail::strand_service::strand_impl*&, boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > >&)+0x226 [0x55bd426f6eb6]
2018-05-28 08:27:15.925 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:163      [17] ./monerod:boost::asio::detail::reactive_socket_recv_op<boost::asio::mutable_buffers_1, boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running> >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long)+0x253 [0x55bd426f7193]
2018-05-28 08:27:15.925 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:163      [18] ./monerod:boost::asio::detail::epoll_reactor::descriptor_state::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long)+0x1f4 [0x55bd42512924]
2018-05-28 08:27:15.925 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:163      [19] ./monerod:epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread()+0x854 [0x55bd426daf74]
2018-05-28 08:27:15.925 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:163      [20] /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0+0x115d5 [0x7fb05e4175d5]
2018-05-28 08:27:15.925 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:163      [21] /lib/x86_64-linux-gnu/libpthread.so.0+0x76ba [0x7fb05dc586ba]
2018-05-28 08:27:15.925 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:163      [22] /lib/x86_64-linux-gnu/libc.so.6:clone+0x6d [0x7fb05d98e41d]
2018-05-28 08:27:15.925 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:163
//
// Very much the same logs, lasting to 2018-05-28 08:36:41.771
//
2018-05-28 08:36:41.771 [P2P8]  INFO    stacktrace      src/common/stack_trace.cpp:163      [20] /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0+0x115d5 [0x7fb05e4175d5]
2018-05-28 08:36:41.771 [P2P8]  INFO    stacktrace      src/common/stack_trace.cpp:163      [21] /lib/x86_64-linux-gnu/libpthread.so.0+0x76ba [0x7fb05dc586ba]
2018-05-28 08:36:41.771 [P2P8]  INFO    stacktrace      src/common/stack_trace.cpp:163      [22] /lib/x86_64-linux-gnu/libc.so.6:clone+0x6d [0x7fb05d98e41d]
2018-05-28 08:36:41.771 [P2P8]  INFO    stacktrace      src/common/stack_trace.cpp:163
//
2018-05-28 08:43:38.390     7fb059244700        INFO    stacktrace      src/common/stack_trace.cpp:124  Exception: boost::thread_interrupted
2018-05-28 08:43:38.390     7fb059244700        INFO    stacktrace      src/common/stack_trace.cpp:125  Unwound call stack:
2018-05-28 08:43:38.391     7fb059244700        INFO    stacktrace      src/common/stack_trace.cpp:163      [1] ./monerod:__cxa_throw+0x10e [0x55bd4280c7ce]
2018-05-28 08:43:38.391     7fb059244700        INFO    stacktrace      src/common/stack_trace.cpp:163      [2] /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0:boost::this_thread::interruption_point()+0x76 [0x7fb05e417506]
2018-05-28 08:43:38.391     7fb059244700        INFO    stacktrace      src/common/stack_trace.cpp:163      [3] ./monerod:nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::init(boost::program_options::variables_map const&)::{lambda()#1}::operator()() const+0x2b8 [0x55bd426cf788]
2018-05-28 08:43:38.391     7fb059244700        INFO    stacktrace      src/common/stack_trace.cpp:163      [4] /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0+0x115d5 [0x7fb05e4175d5]
2018-05-28 08:43:38.391     7fb059244700        INFO    stacktrace      src/common/stack_trace.cpp:163      [5] /lib/x86_64-linux-gnu/libpthread.so.0+0x76ba [0x7fb05dc586ba]
2018-05-28 08:43:38.391     7fb059244700        INFO    stacktrace      src/common/stack_trace.cpp:163      [6] /lib/x86_64-linux-gnu/libc.so.6:clone+0x6d [0x7fb05d98e41d]
2018-05-28 08:43:38.391     7fb059244700        INFO    stacktrace      src/common/stack_trace.cpp:163
2018-05-28 08:46:30.286 [P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:124  Exception: cryptonote::BLOCK_DNE
2018-05-28 08:46:30.286 [P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:125  Unwound call stack:
2018-05-28 08:46:30.289 [P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:163      [1] ./monerod:__cxa_throw+0x10e [0x55bd4280c7ce]
2018-05-28 08:46:30.289 [P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:163      [2] ./monerod+0x3e3bd9 [0x55bd42734bd9]
2018-05-28 08:46:30.289 [P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:163      [3] ./monerod:cryptonote::BlockchainLMDB::get_block_height(crypto::hash const&) const+0x437 [0x55bd42742c77]
2018-05-28 08:46:30.289 [P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:163      [4] ./monerod:cryptonote::BlockchainLMDB::get_block_blob[abi:cxx11](crypto::hash const&) const+0x144 [0x55bd427359b4]
2018-05-28 08:46:30.289 [P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:163      [5] ./monerod:bool cryptonote::Blockchain::get_blocks<std::__cxx11::list<crypto::hash, std::allocator<crypto::hash> >, std::__cxx11::list<std::pair<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, cryptonote::block>, std::allocator<std::pair<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, cryptonote::block> > >, std::__cxx11::list<crypto::hash, std::allocator<crypto::hash> > >(std::__cxx11::list<crypto::hash, std::allocator<crypto::hash> > const&, std::__cxx11::list<std::pair<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, cryptonote::block>, std::allocator<std::pair<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, cryptonote::block> > >&, std::__cxx11::list<crypto::hash, std::allocator<crypto::hash> >&) const+0x1f1 [0x55bd427996d1]
2018-05-28 08:46:30.289 [P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:163      [6] ./monerod:cryptonote::Blockchain::handle_get_objects(cryptonote::NOTIFY_REQUEST_GET_OBJECTS::request&, cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request&)+0x1de [0x55bd427806de]
2018-05-28 08:46:30.289 [P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:163      [7] ./monerod:cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::handle_request_get_objects(int, cryptonote::NOTIFY_REQUEST_GET_OBJECTS::request&, cryptonote::cryptonote_connection_context&)+0x18f [0x55bd426f974f]
2018-05-28 08:46:30.289 [P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:163      [8] ./monerod:int epee::net_utils::buff_to_t_adapter<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, cryptonote::NOTIFY_REQUEST_GET_OBJECTS::request, cryptonote::cryptonote_connection_context, boost::_bi::bind_t<int, boost::_mfi::mf3<int, cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, int, cryptonote::NOTIFY_REQUEST_GET_OBJECTS::request&, cryptonote::cryptonote_connection_context&>, boost::_bi::list4<boost::_bi::value<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*>, boost::arg<1>, boost::arg<2>, boost::arg<3> > > >(cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, boost::_bi::bind_t<int, boost::_mfi::mf3<int, cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, int, cryptonote::NOTIFY_REQUEST_GET_OBJECTS::request&, cryptonote::cryptonote_connection_context&>, boost::_bi::list4<boost::_bi::value<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*>, boost::arg<1>, boost::arg<2>, boost::arg<3> > >, cryptonote::cryptonote_connection_context&)+0x24f [0x55bd42583aff]
2018-05-28 08:46:30.289 [P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:163      [9] ./monerod:int cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::handle_invoke_map<cryptonote::cryptonote_connection_context>(bool, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&, cryptonote::cryptonote_connection_context&, bool&)+0x2aa [0x55bd425932aa]
2018-05-28 08:46:30.289 [P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:163      [10] ./monerod:int nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::handle_invoke_map<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >(bool, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&, bool&)+0xc2 [0x55bd42593532]
2018-05-28 08:46:30.289 [P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:163      [11] ./monerod:nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::notify(int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&)+0x50 [0x55bd42593900]
2018-05-28 08:46:30.289 [P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:163      [12] ./monerod:epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >::handle_recv(void const*, unsigned long)+0x4ad [0x55bd42715a0d]
2018-05-28 08:46:30.289 [P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:163      [13] ./monerod:epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::handle_read(boost::system::error_code const&, unsigned long)+0x1f8 [0x55bd4272d948]
2018-05-28 08:46:30.289 [P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:163      [14] ./monerod:void boost::asio::detail::strand_service::dispatch<boost::asio::detail::binder2<boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::system::error_code, unsigned long> >(boost::asio::detail::strand_service::strand_impl*&, boost::asio::detail::binder2<boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::system::error_code, unsigned long>&)+0x7a [0x55bd426f665a]
2018-05-28 08:46:30.289 [P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:163      [15] ./monerod:boost::asio::detail::completion_handler<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > > >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long)+0x188 [0x55bd426f6ac8]
2018-05-28 08:46:30.289 [P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:163      [16] ./monerod:void boost::asio::detail::strand_service::dispatch<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > > >(boost::asio::detail::strand_service::strand_impl*&, boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > >&)+0x226 [0x55bd426f6eb6]
2018-05-28 08:46:30.289 [P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:163      [17] ./monerod:boost::asio::detail::reactive_socket_recv_op<boost::asio::mutable_buffers_1, boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running> >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long)+0x253 [0x55bd426f7193]
2018-05-28 08:46:30.289 [P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:163      [18] ./monerod:boost::asio::detail::epoll_reactor::descriptor_state::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long)+0x1f4 [0x55bd42512924]
2018-05-28 08:46:30.289 [P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:163      [19] ./monerod:epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread()+0x854 [0x55bd426daf74]
2018-05-28 08:46:30.289 [P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:163      [20] /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0+0x115d5 [0x7fb05e4175d5]

2018-05-28 08:46:30.289 [P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:163      [21] /lib/x86_64-linux-gnu/libpthread.so.0+0x76ba [0x7fb05dc586ba]
2018-05-28 08:46:30.289 [P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:163      [22] /lib/x86_64-linux-gnu/libc.so.6:clone+0x6d [0x7fb05d98e41d]
2018-05-28 08:46:30.289 [P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:163

2018-05-28 08:46:30.289 [P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:124  Exception: cryptonote::BLOCK_DNE
//same details

```
 
## cli 
```
[wallet 442zNf]: transfer 442zNfHF32k2YgmAv4ZUVpd47T7cF7jxk6K8WqvEuQkn73mnhuLm5X5HkJVWrxSyfwYTrSWznJ1N7RJAb5PMAMR8GKd2za5 0.01
Wallet password:
No payment id is included with this transaction. Is this okay?  (Y/Yes/N/No): y
//30minutes passed
There is currently a 1 block backlog at that fee level. Is this okay?  (Y/Yes/N/No): y

Transaction 1/1:
Spending from address index 0
Sending 0.010000000000.  The transaction fee is 0.002352350000
Is this okay?  (Y/Yes/N/No): y
Transaction successfully submitted, transaction <669e6346df2fcd7473e9290548e47bf0b8e0de89d2e06f8ac059b0ac5b3943e7>
You can check its status by using the `show_transfers` command.
```
until TX is sent, I can't search txhash or the amount in the monerod.log.





## moneromooo-monero | 2018-05-28T10:31:03+00:00
Use: --log-level 0,daemon.rpc:INFO

The BLOCK_DNE exceptions are OK when they come from handle_get_objects. 

## wwaayyaa | 2018-05-28T11:01:17+00:00
like this ? 
./monerod --p2p-bind-ip=0.0.0.0 --p2p-bind-port=18080 --rpc-bind-ip=0.0.0.0 --rpc-bind-port=18081 --non-interactive --confirm-external-bind  --data-dir /work/monero-data/monero --config-file /work/monero-data/config.conf  --disable-dns-checkpoint --check-updates=disabled --log-level 0,daemon.rpc:INFO --log-file /work/monero-v0.12.0.0-debug/monerod.log

## moneromooo-monero | 2018-05-28T11:21:12+00:00
Yes

## wwaayyaa | 2018-05-28T11:29:04+00:00
![image](https://user-images.githubusercontent.com/6279538/40612348-acb82b08-62ac-11e8-8b47-6012e13e538a.png)

1. iam +8 timezone. So you can see that I have waited for 10 minutes
2. no more log
3. cli no response

Is the log you added visible after the tx was sent out?


## wwaayyaa | 2018-05-28T11:34:45+00:00
![image](https://user-images.githubusercontent.com/6279538/40612653-1819bc08-62ae-11e8-9c77-e48e8045551f.png)

the newer logs below
```
2018-05-28 11:31:00.515 [RPC1]  INFO    daemon.rpc      src/rpc/core_rpc_server.cpp:1731        on_get_output_histogram: 1 amounts: 0
2018-05-28 11:31:00.515 [RPC1]  INFO    daemon.rpc      src/rpc/core_rpc_server.cpp:1732        unlocked 1, cutoff 1527351540, min count 0
2018-05-28 11:31:00.515 [RPC1]  INFO    daemon.rpc      src/rpc/core_rpc_server.cpp:1736        start
2018-05-28 11:31:00.631 [RPC1]  INFO    daemon.rpc      src/rpc/core_rpc_server.cpp:1738        stop
2018-05-28 11:31:00.631 [RPC1]  INFO    daemon.rpc      src/rpc/core_rpc_server.cpp:1753        exit
2018-05-28 11:31:00.671 [RPC0]  INFO    daemon.rpc      src/rpc/core_rpc_server.cpp:2098        on_get_output_distribution: 1 amounts: 0
2018-05-28 11:31:00.671 [RPC0]  INFO    daemon.rpc      src/rpc/core_rpc_server.cpp:2099        from 1562704 to 1564001
2018-05-28 11:31:00.671 [RPC0]  INFO    daemon.rpc      src/rpc/core_rpc_server.cpp:2175        exit

```

## moneromooo-monero | 2018-05-28T11:41:04+00:00
OK, so that's not those RPC, they're pretty fast as expected.
Maybe it's the wallet itself being slow:
gdb /path/to/monero-wallet-rpc `pidof monero-wallet-rpc`
thread apply all bt full
while it is stuck.

## wwaayyaa | 2018-05-28T11:45:34+00:00
## rpc

```
(gdb) thread apply all bt full

Thread 7 (Thread 0x7f0303fff700 (LWP 12848)):
#0  0x00007f031ccff5d3 in select () at ../sysdeps/unix/syscall-template.S:84
No locals.
#1  0x00007f031e6ae28c in ?? () from /usr/lib/x86_64-linux-gnu/libunbound.so.2
No symbol table info available.
#2  0x00007f031e680cc7 in ?? () from /usr/lib/x86_64-linux-gnu/libunbound.so.2
No symbol table info available.
#3  0x00007f031e6975cd in ub_resolve () from /usr/lib/x86_64-linux-gnu/libunbound.so.2
No symbol table info available.
#4  0x00005636f7c3ec1d in tools::DNSResolver::get_record(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > (*)(char const*, unsigned long), bool&, bool&) ()
No symbol table info available.
#5  0x00005636f7c3ee8e in tools::DNSResolver::get_txt_record(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, bool&, bool&) ()
No symbol table info available.
#6  0x00005636f7c40a07 in boost::detail::thread_data<tools::dns_utils::load_txt_records_from_dns(std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator
std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > const&)::{lambda()#1}>::run() ()
No symbol table info available.
#7  0x00007f031ed545d5 in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0
No symbol table info available.
#8  0x00007f031cfd36ba in start_thread (arg=0x7f0303fff700) at pthread_create.c:333
        __res = <optimized out>
        pd = 0x7f0303fff700
        now = <optimized out>
        unwind_buf = {cancel_jmp_buf = {{jmp_buf = {139650928736000, 1785358111940395848, 0, 139651298059759, 139650928736704, 139651197204336, -1819214274488057016, -1819203267810573496},
              mask_was_saved = 0}}, priv = {pad = {0x0, 0x0, 0x0, 0x0}, data = {prev = 0x0, cleanup = 0x0, canceltype = 0}}}
        not_first_call = <optimized out>
        pagesize_m1 = <optimized out>
        sp = <optimized out>
        freesize = <optimized out>
        __PRETTY_FUNCTION__ = "start_thread"
#9  0x00007f031cd0941d in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109
No locals.

Thread 6 (Thread 0x7f031893c700 (LWP 12847)):
#0  pthread_cond_wait@@GLIBC_2.3.2 () at ../sysdeps/unix/sysv/linux/x86_64/pthread_cond_wait.S:185
No locals.
#1  0x00005636f7c4bf13 in tools::threadpool::run() ()
No symbol table info available.
#2  0x00007f031ed545d5 in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0
No symbol table info available.
#3  0x00007f031cfd36ba in start_thread (arg=0x7f031893c700) at pthread_create.c:333
        __res = <optimized out>
        pd = 0x7f031893c700
        now = <optimized out>
        unwind_buf = {cancel_jmp_buf = {{jmp_buf = {139651273967360, 1785358111940395848, 0, 139651298094079, 139651273968064, 139651210369400, -1819194106932247736, -1819203267810573496},
              mask_was_saved = 0}}, priv = {pad = {0x0, 0x0, 0x0, 0x0}, data = {prev = 0x0, cleanup = 0x0, canceltype = 0}}}
        not_first_call = <optimized out>
        pagesize_m1 = <optimized out>
        sp = <optimized out>
        freesize = <optimized out>
        __PRETTY_FUNCTION__ = "start_thread"
#4  0x00007f031cd0941d in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109
No locals.

Thread 5 (Thread 0x7f0318e3d700 (LWP 12846)):
#0  pthread_cond_wait@@GLIBC_2.3.2 () at ../sysdeps/unix/sysv/linux/x86_64/pthread_cond_wait.S:185
No locals.
#1  0x00005636f7c4bf13 in tools::threadpool::run() ()
No symbol table info available.
#2  0x00007f031ed545d5 in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0
No symbol table info available.
#3  0x00007f031cfd36ba in start_thread (arg=0x7f0318e3d700) at pthread_create.c:333
        __res = <optimized out>
        pd = 0x7f0318e3d700
        now = <optimized out>
        unwind_buf = {cancel_jmp_buf = {{jmp_buf = {139651279214336, 1785358111940395848, 0, 139651298094079, 139651279215040, 139651200795160, -1819194241686846648, -1819203267810573496},
              mask_was_saved = 0}}, priv = {pad = {0x0, 0x0, 0x0, 0x0}, data = {prev = 0x0, cleanup = 0x0, canceltype = 0}}}
        not_first_call = <optimized out>
        pagesize_m1 = <optimized out>
        sp = <optimized out>
        freesize = <optimized out>
        __PRETTY_FUNCTION__ = "start_thread"
#4  0x00007f031cd0941d in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109
No locals.

Thread 4 (Thread 0x7f031933e700 (LWP 12845)):
#0  pthread_cond_wait@@GLIBC_2.3.2 () at ../sysdeps/unix/sysv/linux/x86_64/pthread_cond_wait.S:185
No locals.
#1  0x00005636f7c4bf13 in tools::threadpool::run() ()
No symbol table info available.
#2  0x00007f031ed545d5 in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0
No symbol table info available.
#3  0x00007f031cfd36ba in start_thread (arg=0x7f031933e700) at pthread_create.c:333
        __res = <optimized out>
        pd = 0x7f031933e700
        now = <optimized out>
        unwind_buf = {cancel_jmp_buf = {{jmp_buf = {139651284461312, 1785358111940395848, 0, 139651298094079, 139651284462016, 139651200792392, -1819190530298231992, -1819203267810573496},
              mask_was_saved = 0}}, priv = {pad = {0x0, 0x0, 0x0, 0x0}, data = {prev = 0x0, cleanup = 0x0, canceltype = 0}}}
        not_first_call = <optimized out>
        pagesize_m1 = <optimized out>
        sp = <optimized out>
        freesize = <optimized out>
        __PRETTY_FUNCTION__ = "start_thread"
#4  0x00007f031cd0941d in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109
No locals.

Thread 3 (Thread 0x7f031983f700 (LWP 12844)):
#0  pthread_cond_wait@@GLIBC_2.3.2 () at ../sysdeps/unix/sysv/linux/x86_64/pthread_cond_wait.S:185
No locals.
#1  0x00005636f7c4bf13 in tools::threadpool::run() ()
No symbol table info available.
#2  0x00007f031ed545d5 in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0
No symbol table info available.
#3  0x00007f031cfd36ba in start_thread (arg=0x7f031983f700) at pthread_create.c:333
        __res = <optimized out>
        pd = 0x7f031983f700
        now = <optimized out>
        unwind_buf = {cancel_jmp_buf = {{jmp_buf = {139651289708288, 1785358111940395848, 0, 139651298094079, 139651289708992, 139651218658280, -1819191768859425976, -1819203267810573496},
              mask_was_saved = 0}}, priv = {pad = {0x0, 0x0, 0x0, 0x0}, data = {prev = 0x0, cleanup = 0x0, canceltype = 0}}}
        not_first_call = <optimized out>
        pagesize_m1 = <optimized out>
        sp = <optimized out>
        freesize = <optimized out>
        __PRETTY_FUNCTION__ = "start_thread"
#4  0x00007f031cd0941d in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109
No locals.

Thread 2 (Thread 0x7f031a040700 (LWP 12825)):
#0  pthread_cond_wait@@GLIBC_2.3.2 () at ../sysdeps/unix/sysv/linux/x86_64/pthread_cond_wait.S:185
No locals.
#1  0x00007f031ed56043 in boost::thread::join_noexcept() () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0
No symbol table info available.
#2  0x00005636f7c41717 in tools::dns_utils::load_txt_records_from_dns(std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > >&, std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > const&) ()
No symbol table info available.
#3  0x00005636f7a8eb8b in tools::wallet2::get_segregation_fork_height() const ()
No symbol table info available.
#4  0x00005636f7acc5ef in tools::wallet2::get_outs(std::vector<std::vector<std::tuple<unsigned long, crypto::public_key, rct::key>, std::allocator<std::tuple<unsigned long, crypto::public_key, rct::key> > >, std::allocator<std::vector<std::tuple<unsigned long, crypto::public_key, rct::key>, std::allocator<std::tuple<unsigned long, crypto::public_key, rct::key> > > > >&, std::vector<unsigned long, std::allocator<unsigned long> > const&, unsigned long) ()
No symbol table info available.
#5  0x00005636f7b01c6c in tools::wallet2::transfer_selected_rct(std::vector<cryptonote::tx_destination_entry, std::allocator<cryptonote::tx_destination_entry> >, std::vector<unsigned long, std::allocator<unsigned long> > const&, unsigned long, std::vector<std::vector<std::tuple<unsigned long, crypto::public_key, rct::key>, std::allocator<std::tuple<unsigned long, crypto::public_key, rct::key> > >, std::allocator<std::vector<std::tuple<unsigned long, crypto::public_key, rct::key>, std::allocator<std::tuple<unsigned long, crypto::public_key, rct::key> > > > >&, unsigned long, unsigned long, std::vector<unsigned char, std::allocator<unsigned char> > const&, cryptonote::transaction&, tools::wallet2::pending_tx&, bool) ()
No symbol table info available.
#6  0x00005636f7b0877d in tools::wallet2::create_transactions_2(std::vector<cryptonote::tx_destination_entry, std::allocator<cryptonote::tx_destination_entry> >, unsigned long, unsigned long, unsigned int, std::vector<unsigned char, std::allocator<unsigned char> > const&, unsigned int, std::set<unsigned int, std::less<unsigned int>, std::allocator<unsigned int> >, bool) ()
No symbol table info available.
#7  0x00005636f797b128 in tools::wallet_rpc_server::on_transfer(tools::wallet_rpc::COMMAND_RPC_TRANSFER::request const&, tools::wallet_rpc::COMMAND_RPC_TRANSFER::response&, epee::json_rpc::error&) ()
No symbol table info available.
#8  0x00005636f7a5440b in bool tools::wallet_rpc_server::handle_http_request_map<epee::net_utils::connection_context_base>(epee::net_utils::http::http_request_info const&, epee::net_utils::http::http_resp
onse_info&, epee::net_utils::connection_context_base&) ()
No symbol table info available.
#9  0x00005636f7a65c79 in tools::wallet_rpc_server::handle_http_request(epee::net_utils::http::http_request_info const&, epee::net_utils::http::http_response_info&, epee::net_utils::connection_context_base&) ()
No symbol table info available.
#10 0x00005636f7a3b31a in epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base>::handle_request(epee::net_utils::http::http_request_info const&, epee::net_utils::http::http_response_info&) ()
No symbol table info available.
#11 0x00005636f79e297e in epee::net_utils::http::simple_http_connection_handler<epee::net_utils::connection_context_base>::handle_request_and_send_response(epee::net_utils::http::http_request_info const&) ()
No symbol table info available.
#12 0x00005636f79e2d42 in epee::net_utils::http::simple_http_connection_handler<epee::net_utils::connection_context_base>::handle_retriving_query_body() ()
No symbol table info available.
#13 0x00005636f7a67430 in epee::net_utils::http::simple_http_connection_handler<epee::net_utils::connection_context_base>::handle_buff_in(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&) ()
No symbol table info available.
#14 0x00005636f7a6789b in epee::net_utils::http::simple_http_connection_handler<epee::net_utils::connection_context_base>::handle_recv(void const*, unsigned long) ()
No symbol table info available.
#15 0x00005636f7a67af8 in epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::handle_read(boost::system::error_code const&, unsigned long)
    ()
No symbol table info available.
#16 0x00005636f7a1c1da in void boost::asio::detail::strand_service::dispatch<boost::asio::detail::binder2<boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::system::error_code, unsigned long> >(boost::asio::detail::strand_service::strand_impl*&, boost::asio::detail::binder2<boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::system::error_code, unsigned long>&) ()
No symbol table info available.
#17 0x00005636f7a1c449 in void boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>::operator()<boost::system::error_code, unsigned long>(boost::system::error_code const&, unsigned long const&) ()
No symbol table info available.
#18 0x00005636f7a1c5fa in boost::asio::detail::completion_handler<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > > >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) ()
No symbol table info available.
#19 0x00005636f7a1c946 in void boost::asio::detail::strand_service::dispatch<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code con
st&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > > >(boost::asio::detail::strand_service::strand_impl*&, boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > >&) ()
No symbol table info available.
#20 0x00005636f7a1cc23 in boost::asio::detail::reactive_socket_recv_op<boost::asio::mutable_buffers_1, boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running> >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) ()
No symbol table info available.
#21 0x00005636f79998d4 in boost::asio::detail::epoll_reactor::descriptor_state::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) ()
No symbol table info available.
#22 0x00005636f79b74d4 in epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::worker_thread() ()
No symbol table info available.
#23 0x00007f031ed545d5 in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0
No symbol table info available.
#24 0x00007f031cfd36ba in start_thread (arg=0x7f031a040700) at pthread_create.c:333
        __res = <optimized out>
        pd = 0x7f031a040700
        now = <optimized out>
        unwind_buf = {cancel_jmp_buf = {{jmp_buf = {139651298100992, 1785358111940395848, 0, 140730711768975, 139651298101696, 94794122863472, -1819197265880693944, -1819203267810573496},
              mask_was_saved = 0}}, priv = {pad = {0x0, 0x0, 0x0, 0x0}, data = {prev = 0x0, cleanup = 0x0, canceltype = 0}}}
        not_first_call = <optimized out>
        pagesize_m1 = <optimized out>
        sp = <optimized out>
        freesize = <optimized out>
        __PRETTY_FUNCTION__ = "start_thread"
#25 0x00007f031cd0941d in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109
No locals.

Thread 1 (Thread 0x7f031fa1d780 (LWP 12824)):
#0  pthread_cond_wait@@GLIBC_2.3.2 () at ../sysdeps/unix/sysv/linux/x86_64/pthread_cond_wait.S:185
No locals.
#1  0x00007f031ed56043 in boost::thread::join_noexcept() () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0
No symbol table info available.
#2  0x00005636f7a3fa08 in epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::run_server(unsigned long, bool, boost::thread_attributes const&) ()
No symbol table info available.
#3  0x00005636f7a410d9 in epee::http_server_impl_base<tools::wallet_rpc_server, epee::net_utils::connection_context_base>::run(unsigned long, bool) ()
No symbol table info available.
#4  0x00005636f79807c4 in tools::wallet_rpc_server::run() ()
No symbol table info available.
#5  0x00005636f795f917 in main ()
No symbol table info available.

```

## moneromooo-monero | 2018-05-28T12:02:18+00:00
Ah, so it is stuck making a DNS query and timing out.

in src/wallet/wallet2.cpp, find this line:

static const bool use_dns = true;

replace true with false.

Alternatively, find why DNS queries can get stuck on your system.


## wwaayyaa | 2018-05-28T12:49:11+00:00
@moneromooo-monero 
Brother, you are my savior. 
I love you , lol.
The problem is solved. So cool.

## wwaayyaa | 2018-05-28T14:02:30+00:00
my issue's solution is here  [#1535](https://github.com/monero-project/monero/issues/1535) 
when i write
 ```
nameserver 8.8.8.8
nameserver 8.8.4.4
 ``` 
into etc/resolv.conf

the issue solved.

# Action History
- Created by: wwaayyaa | 2018-05-26T08:55:56+00:00
- Closed at: 2018-05-28T12:54:49+00:00
