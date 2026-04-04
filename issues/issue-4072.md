---
title: After upgrading to release v0.12.2, rpc wallet spams with "No connection to
  daemon" and works only for a day or two without restart
source_url: https://github.com/monero-project/monero/issues/4072
author: cotinco
assignees: []
labels: []
created_at: '2018-06-28T05:16:22+00:00'
updated_at: '2018-09-08T19:44:37+00:00'
type: issue
status: closed
closed_at: '2018-06-28T10:09:01+00:00'
---

# Original Description
After I pulled and recompiled release v0.12.2 (commit e2c39f6...) under my Ubuntu 16.04 server, all my RPC wallets behave very strange. Just after restart, they start spamming to their logs with error "No connection to daemon" every 40 seconds (first time 20 seconds after restart), but work, receive and send transactions for some period of time, about a day or two. Then I need to restart them again because every operation leads to an error and so on. Daemon works fine, with no strange things in the log (which is very hard to monitor because of usual spam of BLOCK_DNE exceptions, but that's the thing that always exists in all previous versions of Monero and other coins forked from Monero also, so I got used to it). What could be wrong? The other thing I touched in addition to pulling the new release was the versions of miniupnp and unbound, I took them from Monero repository for this build (branch monero), but that should not harm anything? Release v0.12.1 worked fine without this problem. But even if I downgrade just wallet to v0.12.1, it spams with the same error, so the problem should be with my daemon? I have completely no idea of what could go wrong :(

Here is the corresponding part of log:
2018-06-28 00:49:57.947     7f6ff0a2f780        WARN    wallet.rpc      src/wallet/wallet_rpc_server.cpp:2948   Loading wallet...
2018-06-28 00:49:57.984     7f6ff0a2f780        WARN    wallet.wallet2  src/wallet/wallet2.cpp:3762     Loaded wallet keys file, with public address: [private]
2018-06-28 00:49:58.283     7f6ff0a2f780        INFO    global  contrib/epee/include/net/http_server_impl_base.h:76     Binding on 127.0.0.1:[private]
2018-06-28 00:49:58.283     7f6ff0a2f780        WARN    wallet.rpc      src/wallet/wallet_rpc_server.cpp:3001   Starting wallet RPC server
2018-06-28 00:50:18.283 [RPC0]  ERROR   net.http        contrib/epee/include/net/http_client.h:397      HTTP_CLIENT: Failed to SEND
2018-06-28 00:50:18.283 [RPC0]  ERROR   wallet.wallet2  src/wallet/wallet2.cpp:1684     !r. THROW EXCEPTION: error::no_connection_to_daemon
2018-06-28 00:50:18.283 [RPC0]  WARN    net.http        src/wallet/wallet_errors.h:794  /home/[private]/monero/src/wallet/wallet2.cpp:1684:N5tools5error23no_connection_to_daemonE: no connection to da
emon, request = getblocks.bin
2018-06-28 00:50:18.284 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:124  Exception: tools::error::no_connection_to_daemon
2018-06-28 00:50:18.284 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:125  Unwound call stack:
2018-06-28 00:50:18.286 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:163      [1] ./monero-wallet-rpc:__cxa_throw+0x10e [0x55e8469cb98e]
2018-06-28 00:50:18.286 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:163      [2] ./monero-wallet-rpc:void tools::error::throw_wallet_ex<tools::error::no_connection_to_daemon, char [14]>(std
::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&&, char const (&) [14])+0x187 [0x55e8468ac497]
2018-06-28 00:50:18.286 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:163      [3] ./monero-wallet-rpc:tools::wallet2::pull_blocks(unsigned long, unsigned long&, std::__cxx11::list<crypto::ha
sh, std::allocator<crypto::hash> > const&, std::__cxx11::list<cryptonote::block_complete_entry, std::allocator<cryptonote::block_complete_entry> >&, std::vector<cryptonote::COMMAND_RPC_GET_BLOCKS_FAST::bl
ock_output_indices, std::allocator<cryptonote::COMMAND_RPC_GET_BLOCKS_FAST::block_output_indices> >&)+0x72c [0x55e84682e31c]
2018-06-28 00:50:18.286 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:163      [4] ./monero-wallet-rpc:tools::wallet2::refresh(unsigned long, unsigned long&, bool&)+0x275 [0x55e846857835]
2018-06-28 00:50:18.286 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:163      [5] ./monero-wallet-rpc:tools::wallet2::refresh(unsigned long, unsigned long&)+0x23 [0x55e846858a93]
2018-06-28 00:50:18.286 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:163      [6] ./monero-wallet-rpc:tools::wallet2::refresh()+0x26 [0x55e846858ad6]
2018-06-28 00:50:18.286 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:163      [7] ./monero-wallet-rpc+0x301141 [0x55e8466db141]
2018-06-28 00:50:18.286 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:163      [8] ./monero-wallet-rpc:epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net
_utils::connection_context_base> >::global_timer_handler(boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::idle_
callback_conext_base>)+0x27 [0x55e846729cd7]
2018-06-28 00:50:18.286 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:163      [9] ./monero-wallet-rpc:boost::asio::detail::wait_handler<boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::
net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_cust
om_handler<epee::net_utils::connection_context_base> >::idle_callback_conext_base> >, boost::_bi::list2<boost::_bi::value<epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epe
e::net_utils::connection_context_base> >*>, boost::_bi::value<boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::
idle_callback_conext_base> > > > >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long)+0x109 [0x55e846702a
89]
2018-06-28 00:50:18.286 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:163      [10] ./monero-wallet-rpc:epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::ne
t_utils::connection_context_base> >::worker_thread()+0x854 [0x55e846724b84]
2018-06-28 00:50:18.286 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:163      [11] /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0+0x115d5 [0x7f6fefd685d5]
2018-06-28 00:50:18.286 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:163      [12] /lib/x86_64-linux-gnu/libpthread.so.0+0x76ba [0x7f6fedddc6ba]
2018-06-28 00:50:18.286 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:163      [13] /lib/x86_64-linux-gnu/libc.so.6:clone+0x6d [0x7f6fedb1241d]
2018-06-28 00:50:18.286 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:163  


# Discussion History
## moneromooo-monero | 2018-06-28T10:06:30+00:00
Fixed in current master.

If you still get this with current master, please reopen.

+resolved

## psychocrypt | 2018-09-08T19:44:37+00:00
@moneromooo-monero How was this issue solved?

# Action History
- Created by: cotinco | 2018-06-28T05:16:22+00:00
- Closed at: 2018-06-28T10:09:01+00:00
