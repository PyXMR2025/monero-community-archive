---
title: monero-wallet-cli 0.11.1 segfaults with "Resource temporarily unavailable"
  when refreshing
source_url: https://github.com/monero-project/monero/issues/3415
author: emesik
assignees: []
labels: []
created_at: '2018-03-16T02:34:44+00:00'
updated_at: '2022-03-16T15:36:41+00:00'
type: issue
status: closed
closed_at: '2022-03-16T15:36:41+00:00'
---

# Original Description
I have `monero-wallet-cli` crashing on refresh upon opening an existing wallet. At the moment it's 100% reproducible, the only changing thing is the number of blocks it downloads before crashing (a couple hundreds up to 1.5k).

Console output:
```
Monero 'Helium Hydra' (v0.11.1.0-release)
Logging to monero-wallet-cli.log
Wallet password: ******************
Opened wallet: 43aeKax1ts4BoEbSyzKVbbDRmc8nsnpZLUpQBYvhUxs3KVrodnaFaBEQMDp69u4VaiEG3LSQXA6M61mXPrztCLuh7PFUAmd
**********************************************************************
Use "help" command to see the list of available commands.
**********************************************************************
Starting refresh...
Error: refresh failed: unexpected error: boost::thread_resource_error: Resource temporarily unavailable. Blocks received: 436
terminate called after throwing an instance of 'boost::exception_detail::clone_impl<boost::exception_detail::error_info_injector<boost::thread_resource_error> >'
  what():  boost::thread_resource_error: Resource temporarily unavailable
zsh: abort (core dumped)  monero-wallet-cli --wallet-file xmrlab --log-level 4
```
Log:

```
2018-03-16 02:24:23.906	    7f6f8fa9b780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:1131	Processed block: <6f2e6c0fc063cfc10a6c793c03fdd6fa6096477b4e9b6705c3240f5a53e8b597>, height 1524178, 5(0/5)ms
2018-03-16 02:24:23.909	    7f6f8fa9b780	INFO 	stacktrace	src/common/stack_trace.cpp:120	Exception: boost::exception_detail::clone_impl<boost::exception_detail::error_info_injector<boost::thread_resource_error> >
2018-03-16 02:24:23.909	    7f6f8fa9b780	INFO 	stacktrace	src/common/stack_trace.cpp:121	Unwound call stack:
2018-03-16 02:24:23.911	    7f6f8fa9b780	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [1] monero-wallet-cli:__cxa_throw+0x111 [0x562b69568081]
2018-03-16 02:24:23.911	    7f6f8fa9b780	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [2] monero-wallet-cli:void boost::throw_exception<boost::thread_resource_error>(boost::thread_resource_error const&)+0x148 [0x562b69402938]
2018-03-16 02:24:23.911	    7f6f8fa9b780	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [3] monero-wallet-cli:boost::thread* boost::thread_group::create_thread<boost::_bi::bind_t<unsigned long, boost::_mfi::mf0<unsigned long, boost::asio::io_context>, boost::_bi::list1<boost::_bi::value<boost::asio::io_context*> > > >(boost::_bi::bind_t<unsigned long, boost::_mfi::mf0<unsigned long, boost::asio::io_context>, boost::_bi::list1<boost::_bi::value<boost::asio::io_context*> > >)+0x735 [0x562b694d08c5]
2018-03-16 02:24:23.911	    7f6f8fa9b780	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [4] monero-wallet-cli:tools::wallet2::process_new_transaction(crypto::hash const&, cryptonote::transaction const&, std::vector<unsigned long, std::allocator<unsigned long> > const&, unsigned long, unsigned long, bool, bool)+0x1e57 [0x562b6948aa87]
2018-03-16 02:24:23.911	    7f6f8fa9b780	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [5] monero-wallet-cli:tools::wallet2::process_new_blockchain_entry(cryptonote::block const&, cryptonote::block_complete_entry const&, crypto::hash const&, unsigned long, cryptonote::COMMAND_RPC_GET_BLOCKS_FAST::block_output_indices const&)+0x225 [0x562b6948eb35]
2018-03-16 02:24:23.911	    7f6f8fa9b780	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [6] monero-wallet-cli:tools::wallet2::process_blocks(unsigned long, std::__cxx11::list<cryptonote::block_complete_entry, std::allocator<cryptonote::block_complete_entry> > const&, std::vector<cryptonote::COMMAND_RPC_GET_BLOCKS_FAST::block_output_indices, std::allocator<cryptonote::COMMAND_RPC_GET_BLOCKS_FAST::block_output_indices> > const&, unsigned long&)+0xc41 [0x562b69490301]
2018-03-16 02:24:23.911	    7f6f8fa9b780	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [7] monero-wallet-cli:tools::wallet2::refresh(unsigned long, unsigned long&, bool&)+0x41c [0x562b694bcf7c]
2018-03-16 02:24:23.911	    7f6f8fa9b780	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [8] monero-wallet-cli:tools::wallet2::refresh(unsigned long, unsigned long&)+0x23 [0x562b694bdbf3]
2018-03-16 02:24:23.911	    7f6f8fa9b780	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [9] monero-wallet-cli:cryptonote::simple_wallet::refresh_main(unsigned long, bool)+0x22f [0x562b693c1ddf]
2018-03-16 02:24:23.911	    7f6f8fa9b780	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [10] monero-wallet-cli:cryptonote::simple_wallet::run()+0x3c [0x562b693c384c]
2018-03-16 02:24:23.911	    7f6f8fa9b780	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [11] monero-wallet-cli:main+0x514 [0x562b693abcf4]
2018-03-16 02:24:23.911	    7f6f8fa9b780	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [12] /usr/lib/libc.so.6:__libc_start_main+0xea [0x7f6f8cc83f4a]
2018-03-16 02:24:23.911	    7f6f8fa9b780	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [13] monero-wallet-cli:_start+0x2a [0x562b693b638a]
2018-03-16 02:24:23.911	    7f6f8fa9b780	INFO 	stacktrace	src/common/stack_trace.cpp:159	
2018-03-16 02:24:23.915	    7f6f8fa9b780	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:1769	Another try pull_blocks (try_count=0)...
2018-03-16 02:24:23.915	    7f6f8fa9b780	INFO 	stacktrace	src/common/stack_trace.cpp:120	Exception: boost::exception_detail::clone_impl<boost::exception_detail::error_info_injector<boost::thread_resource_error> >
2018-03-16 02:24:23.915	    7f6f8fa9b780	INFO 	stacktrace	src/common/stack_trace.cpp:121	Unwound call stack:
2018-03-16 02:24:23.917	    7f6f8fa9b780	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [1] monero-wallet-cli:__cxa_throw+0x111 [0x562b69568081]
2018-03-16 02:24:23.917	    7f6f8fa9b780	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [2] monero-wallet-cli:void boost::throw_exception<boost::thread_resource_error>(boost::thread_resource_error const&)+0x148 [0x562b69402938]
2018-03-16 02:24:23.917	    7f6f8fa9b780	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [3] monero-wallet-cli:tools::wallet2::refresh(unsigned long, unsigned long&, bool&)+0x9c3 [0x562b694bd523]
2018-03-16 02:24:23.917	    7f6f8fa9b780	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [4] monero-wallet-cli:tools::wallet2::refresh(unsigned long, unsigned long&)+0x23 [0x562b694bdbf3]
2018-03-16 02:24:23.917	    7f6f8fa9b780	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [5] monero-wallet-cli:cryptonote::simple_wallet::refresh_main(unsigned long, bool)+0x22f [0x562b693c1ddf]
2018-03-16 02:24:23.917	    7f6f8fa9b780	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [6] monero-wallet-cli:cryptonote::simple_wallet::run()+0x3c [0x562b693c384c]
2018-03-16 02:24:23.917	    7f6f8fa9b780	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [7] monero-wallet-cli:main+0x514 [0x562b693abcf4]
2018-03-16 02:24:23.917	    7f6f8fa9b780	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [8] /usr/lib/libc.so.6:__libc_start_main+0xea [0x7f6f8cc83f4a]
2018-03-16 02:24:23.917	    7f6f8fa9b780	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [9] monero-wallet-cli:_start+0x2a [0x562b693b638a]
2018-03-16 02:24:23.917	    7f6f8fa9b780	INFO 	stacktrace	src/common/stack_trace.cpp:159	
2018-03-16 02:24:23.917	    7f6f8fa9b780	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:1769	Another try pull_blocks (try_count=1)...
2018-03-16 02:24:23.917	    7f6f8fa9b780	INFO 	stacktrace	src/common/stack_trace.cpp:120	Exception: boost::exception_detail::clone_impl<boost::exception_detail::error_info_injector<boost::thread_resource_error> >
2018-03-16 02:24:23.917	    7f6f8fa9b780	INFO 	stacktrace	src/common/stack_trace.cpp:121	Unwound call stack:
2018-03-16 02:24:23.918	    7f6f8fa9b780	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [1] monero-wallet-cli:__cxa_throw+0x111 [0x562b69568081]
2018-03-16 02:24:23.918	    7f6f8fa9b780	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [2] monero-wallet-cli:void boost::throw_exception<boost::thread_resource_error>(boost::thread_resource_error const&)+0x148 [0x562b69402938]
2018-03-16 02:24:23.918	    7f6f8fa9b780	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [3] monero-wallet-cli:tools::wallet2::refresh(unsigned long, unsigned long&, bool&)+0x9c3 [0x562b694bd523]
2018-03-16 02:24:23.918	    7f6f8fa9b780	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [4] monero-wallet-cli:tools::wallet2::refresh(unsigned long, unsigned long&)+0x23 [0x562b694bdbf3]
2018-03-16 02:24:23.918	    7f6f8fa9b780	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [5] monero-wallet-cli:cryptonote::simple_wallet::refresh_main(unsigned long, bool)+0x22f [0x562b693c1ddf]
2018-03-16 02:24:23.918	    7f6f8fa9b780	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [6] monero-wallet-cli:cryptonote::simple_wallet::run()+0x3c [0x562b693c384c]
2018-03-16 02:24:23.918	    7f6f8fa9b780	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [7] monero-wallet-cli:main+0x514 [0x562b693abcf4]
2018-03-16 02:24:23.918	    7f6f8fa9b780	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [8] /usr/lib/libc.so.6:__libc_start_main+0xea [0x7f6f8cc83f4a]
2018-03-16 02:24:23.918	    7f6f8fa9b780	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [9] monero-wallet-cli:_start+0x2a [0x562b693b638a]
2018-03-16 02:24:23.918	    7f6f8fa9b780	INFO 	stacktrace	src/common/stack_trace.cpp:159	
2018-03-16 02:24:23.918	    7f6f8fa9b780	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:1769	Another try pull_blocks (try_count=2)...
2018-03-16 02:24:23.918	    7f6f8fa9b780	INFO 	stacktrace	src/common/stack_trace.cpp:120	Exception: boost::exception_detail::clone_impl<boost::exception_detail::error_info_injector<boost::thread_resource_error> >
2018-03-16 02:24:23.918	    7f6f8fa9b780	INFO 	stacktrace	src/common/stack_trace.cpp:121	Unwound call stack:
2018-03-16 02:24:23.920	    7f6f8fa9b780	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [1] monero-wallet-cli:__cxa_throw+0x111 [0x562b69568081]
2018-03-16 02:24:23.920	    7f6f8fa9b780	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [2] monero-wallet-cli:void boost::throw_exception<boost::thread_resource_error>(boost::thread_resource_error const&)+0x148 [0x562b69402938]
2018-03-16 02:24:23.920	    7f6f8fa9b780	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [3] monero-wallet-cli:tools::wallet2::refresh(unsigned long, unsigned long&, bool&)+0x9c3 [0x562b694bd523]
2018-03-16 02:24:23.920	    7f6f8fa9b780	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [4] monero-wallet-cli:tools::wallet2::refresh(unsigned long, unsigned long&)+0x23 [0x562b694bdbf3]
2018-03-16 02:24:23.920	    7f6f8fa9b780	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [5] monero-wallet-cli:cryptonote::simple_wallet::refresh_main(unsigned long, bool)+0x22f [0x562b693c1ddf]
2018-03-16 02:24:23.920	    7f6f8fa9b780	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [6] monero-wallet-cli:cryptonote::simple_wallet::run()+0x3c [0x562b693c384c]
2018-03-16 02:24:23.920	    7f6f8fa9b780	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [7] monero-wallet-cli:main+0x514 [0x562b693abcf4]
2018-03-16 02:24:23.920	    7f6f8fa9b780	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [8] /usr/lib/libc.so.6:__libc_start_main+0xea [0x7f6f8cc83f4a]
2018-03-16 02:24:23.920	    7f6f8fa9b780	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [9] monero-wallet-cli:_start+0x2a [0x562b693b638a]
2018-03-16 02:24:23.920	    7f6f8fa9b780	INFO 	stacktrace	src/common/stack_trace.cpp:159	
2018-03-16 02:24:23.920	    7f6f8fa9b780	ERROR	wallet.wallet2	src/wallet/wallet2.cpp:1774	pull_blocks failed, try_count=3
2018-03-16 02:24:23.927	    7f6f8fa9b780	ERROR	wallet.simplewallet	src/simplewallet/simplewallet.cpp:1975	unexpected error: boost::thread_resource_error: Resource temporarily unavailable
2018-03-16 02:24:23.927	    7f6f8fa9b780	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: refresh failed: unexpected error: boost::thread_resource_error: Resource temporarily unavailable. Blocks received: 436
2018-03-16 02:24:23.927	    7f6f8fa9b780	INFO 	stacktrace	src/common/stack_trace.cpp:120	Exception: boost::exception_detail::clone_impl<boost::exception_detail::error_info_injector<boost::thread_resource_error> >
2018-03-16 02:24:23.927	    7f6f8fa9b780	INFO 	stacktrace	src/common/stack_trace.cpp:121	Unwound call stack:
2018-03-16 02:24:23.928	    7f6f8fa9b780	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [1] monero-wallet-cli:__cxa_throw+0x111 [0x562b69568081]
2018-03-16 02:24:23.928	    7f6f8fa9b780	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [2] monero-wallet-cli:void boost::throw_exception<boost::thread_resource_error>(boost::thread_resource_error const&)+0x148 [0x562b69402938]
2018-03-16 02:24:23.928	    7f6f8fa9b780	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [3] monero-wallet-cli:cryptonote::simple_wallet::run()+0x54c [0x562b693c3d5c]
2018-03-16 02:24:23.928	    7f6f8fa9b780	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [4] monero-wallet-cli:main+0x514 [0x562b693abcf4]
2018-03-16 02:24:23.928	    7f6f8fa9b780	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [5] /usr/lib/libc.so.6:__libc_start_main+0xea [0x7f6f8cc83f4a]
2018-03-16 02:24:23.928	    7f6f8fa9b780	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [6] monero-wallet-cli:_start+0x2a [0x562b693b638a]
2018-03-16 02:24:23.928	    7f6f8fa9b780	INFO 	stacktrace	src/common/stack_trace.cpp:159	
```

# Discussion History
## moneromooo-monero | 2018-03-16T08:50:28+00:00
Can you get a stack trace of the crash too please ? "bt" in gdb.

## emesik | 2018-03-16T23:15:24+00:00
Hmmm... Today it's just working fine, and I can't reproduce it.

When the crash happened, the node was also syncing after I had brought it back online. It was about 5 days behind the network, catching up slowly because some of the peers seemed to serve invalid data.

The daemon's log from the same time:

```
2018-03-16 02:23:18.430 [P2P9]  ERROR   net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025    [139.224.233.220:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2018-03-16 02:23:34.309 [P2P0]  WARN    net.p2p src/p2p/net_node.inl:1567       [0.0.0.0:0 OUT] back ping connect failed to 172.125.28.15:18080
2018-03-16 02:23:35.872 [P2P9]  WARN    net.p2p src/p2p/net_node.inl:1629       [136.144.152.214:18080 OUT] COMMAND_REQUEST_SUPPORT_FLAGS invoke failed. (-3, LEVIN_ERROR_CONNECTION_DESTROYED)
2018-03-16 02:23:42.977 [P2P5]  WARN    net.p2p src/p2p/net_node.inl:1567       [0.0.0.0:0 OUT] back ping connect failed to 178.164.107.59:18080
2018-03-16 02:24:27.045 [P2P0]  ERROR   net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1063    [139.224.233.220:18080 OUT] transaction verification failed on NOTIFY_RESPONSE_GET_OBJECTS, tx_id = 6d7701bf4a8121de3c2dbe708de881c57eb50f6e1216aa4c8a2a56ac09266f03, dropping connection
2018-03-16 02:24:27.045 [P2P0]  WARN    net.p2p src/p2p/net_node.inl:834        [139.224.233.220:18080 OUT] COMMAND_TIMED_SYNC invoke failed. (-3, LEVIN_ERROR_CONNECTION_DESTROYED)
2018-03-16 02:24:29.273 [P2P5]  ERROR   net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025    [91.185.217.2:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2018-03-16 02:24:29.311 [P2P8]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:305     [24.80.70.163:18080 OUT] Sync data returned a new top block candidate: 1526988 -> 1530607 [Your node is 3619 blocks (5 days) behind] 
SYNCHRONIZATION started
2018-03-16 02:24:29.743 [P2P9]  ERROR   net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025    [138.197.182.114:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2018-03-16 02:24:33.696 [P2P5]  WARN    net.p2p src/p2p/net_node.inl:834        [76.102.81.127:54718 INC] COMMAND_TIMED_SYNC invoke failed. (-4, LEVIN_ERROR_CONNECTION_TIMEDOUT)
2018-03-16 02:24:57.492 [P2P6]  ERROR   net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1063    [91.185.217.2:18080 OUT] transaction verification failed on NOTIFY_RESPONSE_GET_OBJECTS, tx_id = 6d7701bf4a8121de3c2dbe708de881c57eb50f6e1216aa4c8a2a56ac09266f03, dropping connection
```

Perhaps this can help? I doubt I could provide more details.

## selsta | 2022-03-16T15:36:41+00:00
If someone continues to have this issue with the latest version please open a new issue.

# Action History
- Created by: emesik | 2018-03-16T02:34:44+00:00
- Closed at: 2022-03-16T15:36:41+00:00
