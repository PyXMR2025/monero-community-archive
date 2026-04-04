---
title: Fee estimation / tx backlog command fee returning error in Helium Hydra cli
  wallet
source_url: https://github.com/monero-project/monero/issues/2409
author: marvin8
assignees: []
labels: []
created_at: '2017-09-08T00:56:38+00:00'
updated_at: '2017-09-15T07:42:24+00:00'
type: issue
status: closed
closed_at: '2017-09-15T07:42:24+00:00'
---

# Original Description
Using the new Helium Hydra wallet-cli and trying out the fee command I am getting an error consistently.

I've downloaded the official binaries for Linux 64 bit and running it on Ubuntu 16.04. I am connecting to my own remote node also running official binaries for Linux 64 bit also running on Ubuntu 16.04.

cli wallet log file shows the following entries.

    2017-09-08 00:48:56.366	    7fe0ff3fc740	INFO 	logging	contrib/epee/src/mlog.cpp:148	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
    2017-09-08 00:48:56.366	    7fe0ff3fc740	INFO 	msgwriter	src/common/scoped_message_writer.h:102	Monero 'Helium Hydra' (v0.11.0.0-release)
    2017-09-08 00:48:56.367	    7fe0ff3fc740	INFO 	msgwriter	src/common/scoped_message_writer.h:102	Logging to /home/mark/bin/monero/monero-wallet-cli.log
    2017-09-08 00:49:01.556	    7fe0ff3fc740	WARN 	wallet.wallet2	src/wallet/wallet2.cpp:2505	Loaded wallet keys file, with public address: <removed>
    2017-09-08 00:49:02.328	    7fe0ff3fc740	INFO 	msgwriter	src/common/scoped_message_writer.h:102	Opened wallet: <removed>
    2017-09-08 00:49:02.328	    7fe0ff3fc740	INFO 	msgwriter	src/common/scoped_message_writer.h:102 **********************************************************************
    Use "help" command to see the list of available commands.
    **********************************************************************
    2017-09-08 00:49:08.367	    7fe0ff3fc740	INFO 	msgwriter	src/common/scoped_message_writer.h:102	Starting refresh...
    2017-09-08 00:49:29.151	    7fe0ff3fc740	INFO 	msgwriter	src/common/scoped_message_writer.h:102	Refresh done, blocks received: 0
    2017-09-08 00:49:29.151	    7fe0ff3fc740	INFO 	msgwriter	src/common/scoped_message_writer.h:102	Balance: 5.192745438285, unlocked balance: 5.192745438285
    2017-09-08 00:49:29.151	    7fe0ff3fc740	INFO 	msgwriter	src/common/scoped_message_writer.h:102	Background refresh thread started
    2017-09-08 00:49:46.627	    7fe0ff3fc740	INFO 	msgwriter	src/common/scoped_message_writer.h:102	Current fee is 0.000259100000 monero per kB
    2017-09-08 00:50:02.185	    7fe0ff3fc740	INFO 	stacktrace	src/common/stack_trace.cpp:120	Exception: std::runtime_error
    2017-09-08 00:50:02.185	    7fe0ff3fc740	INFO 	stacktrace	src/common/stack_trace.cpp:121	Unwound call stack:
    2017-09-08 00:50:02.190	    7fe0ff3fc740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [1] /home/mark/bin/monero/monero-wallet-cli:__wrap___cxa_throw+0x102 [0x85b342]
    2017-09-08 00:50:02.190	    7fe0ff3fc740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [2] /home/mark/bin/monero/monero-wallet-cli:epee::serialization::convert_to_integral<epee::serialization::section, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, false>::convert(epee::serialization::section const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&)+0x177 [0x733ff7]
    2017-09-08 00:50:02.190	    7fe0ff3fc740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [3] /home/mark/bin/monero/monero-wallet-cli:bool epee::serialization::portable_storage::get_value<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&, epee::serialization::section*)+0x68 [0x734368]
    2017-09-08 00:50:02.190	    7fe0ff3fc740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [4] /home/mark/bin/monero/monero-wallet-cli:bool epee::serialization::kv_serialization_overloads_impl_is_base_serializable_types<true>::kv_unserialize<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, epee::serialization::portable_storage>(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&, epee::serialization::portable_storage&, epee::serialization::portable_storage::hsection, char const*)+0x3d [0x73447d]
    2017-09-08 00:50:02.190	    7fe0ff3fc740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [5] /home/mark/bin/monero/monero-wallet-cli:bool epee::json_rpc::response<cryptonote::COMMAND_RPC_GET_TRANSACTION_POOL_BACKLOG::response, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >::load<epee::serialization::portable_storage>(epee::serialization::portable_storage&, epee::serialization::portable_storage::hsection)+0x2a1 [0x7f25c1]
    2017-09-08 00:50:02.190	    7fe0ff3fc740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [6] /home/mark/bin/monero/monero-wallet-cli:bool epee::net_utils::invoke_http_json<epee::json_rpc::request<cryptonote::COMMAND_RPC_GET_TRANSACTION_POOL_BACKLOG::request>, epee::json_rpc::response<cryptonote::COMMAND_RPC_GET_TRANSACTION_POOL_BACKLOG::response, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, epee::net_utils::http::http_simple_client>(boost::basic_string_ref<char, std::char_traits<char> >, epee::json_rpc::request<cryptonote::COMMAND_RPC_GET_TRANSACTION_POOL_BACKLOG::request> const&, epee::json_rpc::response<cryptonote::COMMAND_RPC_GET_TRANSACTION_POOL_BACKLOG::response, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >&, epee::net_utils::http::http_simple_client&, std::chrono::duration<long, std::ratio<1l, 1000l> >, boost::basic_string_ref<char, std::char_traits<char> >)+0x38d [0x7fa00d]
    2017-09-08 00:50:02.190	    7fe0ff3fc740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [7] /home/mark/bin/monero/monero-wallet-cli:tools::wallet2::estimate_backlog(unsigned long, unsigned long, std::vector<unsigned long, std::allocator<unsigned long> > const&)+0x39d [0x77e1cd]
    2017-09-08 00:50:02.190	    7fe0ff3fc740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [8] /home/mark/bin/monero/monero-wallet-cli:cryptonote::simple_wallet::print_fee_info(std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > const&)+0x248 [0x6bc108]
    2017-09-08 00:50:02.190	    7fe0ff3fc740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [9] /home/mark/bin/monero/monero-wallet-cli:epee::command_handler::process_command_vec(std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > const&)+0xfb [0x70324b]
    2017-09-08 00:50:02.190	    7fe0ff3fc740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [10] /home/mark/bin/monero/monero-wallet-cli:epee::command_handler::process_command_str(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&)+0xf0 [0x718770]
    2017-09-08 00:50:02.190	    7fe0ff3fc740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [11] /home/mark/bin/monero/monero-wallet-cli:bool epee::async_console_handler::run<bool epee::async_console_handler::run<boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::command_handler, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&>, boost::_bi::list2<boost::_bi::value<epee::console_handlers_binder*>, boost::arg<1> > > >(boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::command_handler, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&>, boost::_bi::list2<boost::_bi::value<epee::console_handlers_binder*>, boost::arg<1> > >, std::function<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > ()>, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::function<void ()>)::{lambda(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&)#1}>(std::function<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > ()>, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, bool epee::async_console_handler::run<boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::command_handler, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&>, boost::_bi::list2<boost::_bi::value<epee::console_handlers_binder*>, boost::arg<1> > > >(boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::command_handler, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&>, boost::_bi::list2<boost::_bi::value<epee::console_handlers_binder*>, boost::arg<1> > >, std::function<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > ()>, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::function<void ()>)::{lambda(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&)#1} const&, std::function<void ()>)+0x7a3 [0x6fbca3]
    2017-09-08 00:50:02.190	    7fe0ff3fc740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [12] /home/mark/bin/monero/monero-wallet-cli:cryptonote::simple_wallet::run()+0x324 [0x6bbb24]
    2017-09-08 00:50:02.190	    7fe0ff3fc740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [13] /home/mark/bin/monero/monero-wallet-cli:main+0x532 [0x69e4d2]
    2017-09-08 00:50:02.190	    7fe0ff3fc740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [14] /lib/x86_64-linux-gnu/libc.so.6:__libc_start_main+0xf0 [0x7fe0fe72d830]
    2017-09-08 00:50:02.190	    7fe0ff3fc740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [15] /home/mark/bin/monero/monero-wallet-cli:_start+0x29 [0x6a6199]
    2017-09-08 00:50:02.190	    7fe0ff3fc740	INFO 	stacktrace	src/common/stack_trace.cpp:159	
    2017-09-08 00:50:02.190	    7fe0ff3fc740	ERROR	net.http	contrib/epee/include/net/jsonrpc_structs.h:58	Exception on unserializing: WRONG DATA CONVERSION: from type=N4epee13serialization7sectionE to type NSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEE
    2017-09-08 00:50:02.190	    7fe0ff3fc740	ERROR	wallet.wallet2	src/wallet/wallet2.cpp:5771	!r. THROW EXCEPTION: error::no_connection_to_daemon
    2017-09-08 00:50:02.190	    7fe0ff3fc740	WARN 	net.http	src/wallet/wallet_errors.h:707	/DISTRIBUTION-BUILD/src/wallet/wallet2.cpp:5771:N5tools5error23no_connection_to_daemonE: no connection to daemon, request = Failed to connect to daemon
    2017-09-08 00:50:02.190	    7fe0ff3fc740	INFO 	stacktrace	src/common/stack_trace.cpp:120	Exception: tools::error::no_connection_to_daemon
    2017-09-08 00:50:02.190	    7fe0ff3fc740	INFO 	stacktrace	src/common/stack_trace.cpp:121	Unwound call stack:
    2017-09-08 00:50:02.194	    7fe0ff3fc740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [1] /home/mark/bin/monero/monero-wallet-cli:__wrap___cxa_throw+0x102 [0x85b342]
    2017-09-08 00:50:02.194	    7fe0ff3fc740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [2] /home/mark/bin/monero/monero-wallet-cli:void tools::error::throw_wallet_ex<tools::error::no_connection_to_daemon, char [28]>(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&&, char const (&) [28])+0x16a [0x7cf26a]
    2017-09-08 00:50:02.194	    7fe0ff3fc740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [3] /home/mark/bin/monero/monero-wallet-cli:tools::wallet2::estimate_backlog(unsigned long, unsigned long, std::vector<unsigned long, std::allocator<unsigned long> > const&)+0x4b2 [0x77e2e2]
    2017-09-08 00:50:02.194	    7fe0ff3fc740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [4] /home/mark/bin/monero/monero-wallet-cli:cryptonote::simple_wallet::print_fee_info(std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > const&)+0x248 [0x6bc108]
    2017-09-08 00:50:02.194	    7fe0ff3fc740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [5] /home/mark/bin/monero/monero-wallet-cli:epee::command_handler::process_command_vec(std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > const&)+0xfb [0x70324b]
    2017-09-08 00:50:02.194	    7fe0ff3fc740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [6] /home/mark/bin/monero/monero-wallet-cli:epee::command_handler::process_command_str(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&)+0xf0 [0x718770]
    2017-09-08 00:50:02.195	    7fe0ff3fc740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [7] /home/mark/bin/monero/monero-wallet-cli:bool epee::async_console_handler::run<bool epee::async_console_handler::run<boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::command_handler, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&>, boost::_bi::list2<boost::_bi::value<epee::console_handlers_binder*>, boost::arg<1> > > >(boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::command_handler, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&>, boost::_bi::list2<boost::_bi::value<epee::console_handlers_binder*>, boost::arg<1> > >, std::function<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > ()>, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::function<void ()>)::{lambda(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&)#1}>(std::function<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > ()>, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, bool epee::async_console_handler::run<boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::command_handler, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&>, boost::_bi::list2<boost::_bi::value<epee::console_handlers_binder*>, boost::arg<1> > > >(boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::command_handler, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&>, boost::_bi::list2<boost::_bi::value<epee::console_handlers_binder*>, boost::arg<1> > >, std::function<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > ()>, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::function<void ()>)::{lambda(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&)#1} const&, std::function<void ()>)+0x7a3 [0x6fbca3]
    2017-09-08 00:50:02.195	    7fe0ff3fc740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [8] /home/mark/bin/monero/monero-wallet-cli:cryptonote::simple_wallet::run()+0x324 [0x6bbb24]
    2017-09-08 00:50:02.195	    7fe0ff3fc740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [9] /home/mark/bin/monero/monero-wallet-cli:main+0x532 [0x69e4d2]
    2017-09-08 00:50:02.195	    7fe0ff3fc740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [10] /lib/x86_64-linux-gnu/libc.so.6:__libc_start_main+0xf0 [0x7fe0fe72d830]
    2017-09-08 00:50:02.195	    7fe0ff3fc740	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [11] /home/mark/bin/monero/monero-wallet-cli:_start+0x29 [0x6a6199]
    2017-09-08 00:50:02.195	    7fe0ff3fc740	INFO 	stacktrace	src/common/stack_trace.cpp:159	
    2017-09-08 00:50:02.195	    7fe0ff3fc740	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Error: failed to estimate backlog array size: no connection to daemon


# Discussion History
## marvin8 | 2017-09-08T00:59:12+00:00
Also attaching the logfile in case that's easier to work with ;-)

[Issue2409.monero-wallet-cli.log.txt](https://github.com/monero-project/monero/files/1286453/Issue2409.monero-wallet-cli.log.txt)


## moneromooo-monero | 2017-09-08T08:56:32+00:00
Is the daemon synced ? Are you sure it's the release version ? Any errors in the daemon log when running with log level 1 while you're running the fee command from the wallet ?

## marvin8 | 2017-09-08T09:17:34+00:00
Yes, daemon is synced, confirmed it's version:

    7ffa4e7c5740	INFO 	global	src/daemon/main.cpp:279	Monero 'Helium Hydra' (v0.11.0.0-release)

No errors showing in the deamon with log level 1... sorry.

I am starting the daemon with the following flags:

    monerod --fluffy-blocks --block-sync-size 10 --rpc-bind-port 18089 --restricted-rpc --confirm-external-bind --rpc-bind-ip <ip removed>

## marvin8 | 2017-09-08T09:21:01+00:00
I do however get the following warnings when starting up the daemon:

    [1504862324] libunbound[25532:0] info: warning: unsupported algorithm for trust anchor . DS IN
    [1504862324] libunbound[25532:0] warning: trust anchor . has no supported algorithms, the anchor is ignored (check if you need to upgrade unbound and openssl)


## moneromooo-monero | 2017-09-08T10:12:06+00:00
--restricted-rpc is preventing access to that RPC.

## marvin8 | 2017-09-08T20:30:27+00:00
Thanks moneromooo-monero 

Looking at the command line options with --help it says that --restrict-rpc "Restrict RPC to view only commands"   Wouldn't / Shouldn't looking at the fee estimation be a view only command?

## moneromooo-monero | 2017-09-08T21:07:56+00:00
Yes, but it's still blocked by it if you look at core_rpc_server.h

## marvin8 | 2017-09-08T21:50:03+00:00
Had a look at core_rpc_server.h .... I've done so little coding in C that it might as well be Chinese :D

The point I was trying to make in my previous comment, was that maybe restricting the fee command with --restrict-rpc could be reconsidered? I don't know the reason why it's restricted, just asking :)

Either way, I trust you and the other contributors had good reasons to restrict it and will just live with it :)

## moneromooo-monero | 2017-09-08T22:16:48+00:00
Yes, it could be reconsidered. I tend to default to restricted when I'm not sure, and that was overly restrictive. For now, you can change that for your daemon by changing line 128 (the one which has get_txpool_backlog in it), and replace "!m_restricted" with "true".


## marvin8 | 2017-09-08T22:39:24+00:00
Cool... Thanks moneromooo-monero ... I might try that later.

Opening up that function when monerod is started with --restrict-rpc might be good for any open node hosted for the community.

Thanks again for taking the time... really appreciate it!

## moneromooo-monero | 2017-09-08T22:48:30+00:00
https://github.com/monero-project/monero/pull/2417

## moneromooo-monero | 2017-09-15T07:40:47+00:00
+resolved

# Action History
- Created by: marvin8 | 2017-09-08T00:56:38+00:00
- Closed at: 2017-09-15T07:42:24+00:00
