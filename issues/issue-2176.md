---
title: 'Exception: boost::exception_detail::clone_impl...'
source_url: https://github.com/monero-project/monero/issues/2176
author: thinkier
assignees: []
labels: []
created_at: '2017-07-17T00:37:03+00:00'
updated_at: '2018-08-15T12:49:00+00:00'
type: issue
status: closed
closed_at: '2018-08-15T12:49:00+00:00'
---

# Original Description

Description: Didn't know what happened, monerod crashed 1 hour later. Then a similar thing was printed again when I rebooted ~15 minutes ago (didn't check if they were completely identical, see gist revisions.)

Server RAM size: 512M - Extra swap: 1.5G (Shouldn't be a memory problem, there's plenty.)
Disk is about half full. (Shouldn't be a disk problem.)

Stacktrace: https://gist.github.com/UninterestinAcc/8ab0830791803e3fa3660d0f3399c1d5
Start options: `"--limit-rate 160 --block-sync-size 1 --restricted-rpc --rpc-bind-ip <server ip address> --rpc-bind-port 18089 --confirm-external-bind"` (yes an open node config from https://moneroworld.com/#nodes)

# Discussion History
## moneromooo-monero | 2017-07-17T10:22:25+00:00
This doesn't seem to be the cause of the crash. Are you sure it is ?
Do you have a core file (or other similar way to get a stack trace on crash) ?

## thinkier | 2017-07-18T15:36:47+00:00
I dont think it caused the crash. Just saw it appear twice and thought about noting it here. And no I don't have a way to get a stacktrace on crash.

## moneromooo-monero | 2017-07-18T22:55:42+00:00
FWIW, --block-sync-size 1 is a silly setting, which will slow down sync by a fair amount. Why are you using this ?

## thinkier | 2017-07-19T07:12:52+00:00
That was a bad idea for progress tracking and saving my RAM. 🤷‍

## danbarta | 2017-08-02T20:44:23+00:00
I also receive this exception quite often (few times a day), mostly after BLOCK ADDED AS ALTERNATIVE ON HEIGHT.

2017-07-31 18:54:03.598 [P2P9]  INFO    global  src/cryptonote_core/blockchain.cpp:1420 ----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 1366460
id:     <e6d984f1b126206ff9d5dc340cfa1ff25e84d56ac31e1364868a672f7efb487d>
PoW:    <a9c483aa8e0d67f12187538e82a6ae2e21c359a7ddc11c44543ed13b00000000>
difficulty:     16566208035
2017-07-31 19:01:10.751 [P2P9]  INFO    stacktrace      src/common/stack_trace.cpp:119  Exception: boost::exception_detail::clone_impl<boost::exception_detail::error_info_injector<boost::system::system_error> >
2017-07-31 19:01:10.751 [P2P9]  INFO    stacktrace      src/common/stack_trace.cpp:120  Unwound call stack:
2017-07-31 19:01:10.788 [P2P9]  INFO    stacktrace      src/common/stack_trace.cpp:158      [1] monerod:__cxa_throw+0x84 [0x807a04]
2017-07-31 19:01:10.789 [P2P9]  INFO    stacktrace      src/common/stack_trace.cpp:158      [2] monerod:void boost::throw_exception<boost::system::system_error>(boost::system::system_error const&)+0x10d [0x638b0d]
2017-07-31 19:01:10.789 [P2P9]  INFO    stacktrace      src/common/stack_trace.cpp:158      [3] monerod:boost::asio::detail::do_throw_error(boost::system::error_code const&, char const*)+0x1e [0x638b9e]
2017-07-31 19:01:10.789 [P2P9]  INFO    stacktrace      src/common/stack_trace.cpp:158      [4] monerod:epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_con
nection_context> > >::connect(std::string const&, std::string const&, unsigned int, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&, std::string const&)+0x1447 [0x6f92c7]
2017-07-31 19:01:10.789 [P2P9]  INFO    stacktrace      src/common/stack_trace.cpp:158      [5] monerod:nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::check_connection_and_handshake_with_peer(nodetoo
l::net_address const&, unsigned long)+0x397 [0x6f9937]
2017-07-31 19:01:10.789 [P2P9]  INFO    stacktrace      src/common/stack_trace.cpp:158      [6] monerod:nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::gray_peerlist_housekeeping()+0x82 [0x6fa6d2]
2017-07-31 19:01:10.789 [P2P9]  INFO    stacktrace      src/common/stack_trace.cpp:158      [7] monerod:nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::idle_worker()+0xac [0x62c79c]
2017-07-31 19:01:10.789 [P2P9]  INFO    stacktrace      src/common/stack_trace.cpp:158      [8] monerod:epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_con
nection_context> > >::global_timer_handler(boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext_
base>)+0x1e [0x651a2e]
2017-07-31 19:01:10.789 [P2P9]  INFO    stacktrace      src/common/stack_trace.cpp:158      [9] monerod:boost::asio::detail::wait_handler<boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::net_utils::boosted_tcp_server<epee::levin::as
ync_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptono
te::cryptonote_connection_context> > >::idle_callback_conext_base> >, boost::_bi::list2<boost::_bi::value<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_c
onnection_context> > >*>, boost::_bi::value<boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext
_base> > > > >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long)+0xf7 [0x630787]
2017-07-31 19:01:10.789 [P2P9]  INFO    stacktrace      src/common/stack_trace.cpp:158      [10] monerod:boost::asio::detail::task_io_service::do_run_one(boost::asio::detail::scoped_lock<boost::asio::detail::posix_mutex>&, boost::asio::d
etail::task_io_service_thread_info&, boost::system::error_code const&)+0x2fd [0x63372d]
2017-07-31 19:01:10.789 [P2P9]  INFO    stacktrace      src/common/stack_trace.cpp:158      [11] monerod:epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_co
nnection_context> > >::worker_thread()+0x20b [0x652adb]
2017-07-31 19:01:10.789 [P2P9]  INFO    stacktrace      src/common/stack_trace.cpp:158      [12] /usr/local/lib/libboost_thread.so.1.64.0+0x116d9 [0x7ffbe5b416d9]
2017-07-31 19:01:10.789 [P2P9]  INFO    stacktrace      src/common/stack_trace.cpp:158      [13] /lib64/libpthread.so.0+0x7dc5 [0x7ffbe61aadc5]
2017-07-31 19:01:10.789 [P2P9]  INFO    stacktrace      src/common/stack_trace.cpp:158      [14] /lib64/libc.so.6:clone+0x6d [0x7ffbe49ed76d]
2017-07-31 19:01:10.789 [P2P9]  INFO    stacktrace      src/common/stack_trace.cpp:158
2017-07-31 20:12:59.085 [P2P9]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1099    SYNCHRONIZED OK

Server: CentOS 7.3 running in OpenVZ 3GB RAM

## moneromooo-monero | 2017-08-02T22:47:14+00:00
That should be fine, it's rying to connect to a new peer, and fails.

## moneromooo-monero | 2017-09-21T08:50:43+00:00
The crash might be fixed by https://github.com/monero-project/monero/pull/2492

## moneromooo-monero | 2018-08-15T12:20:50+00:00
I'll call it fixed, since the stack trace is not available anymore, I don't remember what it was, and my last comment says it might be fixed :)
Reopen if you still hit this and have more info.

+resolved

# Action History
- Created by: thinkier | 2017-07-17T00:37:03+00:00
- Closed at: 2018-08-15T12:49:00+00:00
