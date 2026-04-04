---
title: 'Problems at read: Operation canceled with local node'
source_url: https://github.com/monero-project/monero/issues/3234
author: cialu
assignees: []
labels: []
created_at: '2018-02-05T14:31:47+00:00'
updated_at: '2022-03-16T15:32:25+00:00'
type: issue
status: closed
closed_at: '2022-03-16T15:32:25+00:00'
---

# Original Description
Hi all!

I have compiled Helium Hydra, Point Release 1 code on a **Raspberry Pi ARMv6** and I'm running a local node on it. It's fully working and synchronized.

I have an issue trying to connect cli wallet from another PC running **Linux Ubuntu 17.10** and I'm not able to use the wallet through the local node.

The Raspberry Pi has 192.168.1.50 as static IP, the PC with the wallet has dinamic IP from DHCP.

I start the node with this command:

`./monerod --rpc-bind-ip 192.168.1.50 --rpc-bind-port=4008 --confirm-external-bind`

I get this:

```
2018-02-05 13:49:06.596          b486a3d0        INFO    global  contrib/epee/include/net/http_server_impl_base.h:70     Binding on 192.168.1.50:4008
...
2018-02-05 13:49:50.908  [P2P9]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1521    SYNCHRONIZED OK
```

I start the wallet with this command:

`./monero-wallet-cli --daemon-address 192.168.1.50:4008 --wallet-file mywallet --log-level 2
`

And I get this:

```
Monero 'Helium Hydra' (v0.11.1.0-release)
Logging to ./monero-wallet-cli.log
Wallet password: ********
Opened watch-only wallet: 48xxx
**********************************************************************
Use "help" command to see the list of available commands.
**********************************************************************
Starting refresh...
Error: refresh failed: no connection to daemon. Please make sure daemon is running.. Blocks received: 0
Background refresh thread started
[wallet 48xxx (no daemon)]: refresh
Error: wallet failed to connect to daemon: 192.168.1.50:4008. Daemon either is not started or wrong port was passed. Please make sure daemon is running or restart the wallet with the correct daemon address.

```
I have checked the wallet log file:

```
2018-02-05 14:07:19.195	    7fb370c85b80	INFO 	logging	contrib/epee/src/mlog.cpp:148	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-02-05 14:07:19.195	    7fb370c85b80	INFO 	logging	contrib/epee/src/mlog.cpp:156	New log categories: *:DEBUG
2018-02-05 14:07:19.196	    7fb370c85b80	INFO 	msgwriter	src/common/scoped_message_writer.h:102	Monero 'Helium Hydra' (v0.11.1.0-release)
2018-02-05 14:07:19.196	    7fb370c85b80	INFO 	wallet.wallet2	src/wallet/wallet_args.cpp:171	Setting log level = 2
2018-02-05 14:07:19.196	    7fb370c85b80	INFO 	wallet.wallet2	src/wallet/wallet_args.cpp:174	Logging to: ./monero-wallet-cli.log
2018-02-05 14:07:19.196	    7fb370c85b80	INFO 	msgwriter	src/common/scoped_message_writer.h:102	Logging to ./monero-wallet-cli.log
2018-02-05 14:07:24.365	    7fb370c85b80	WARN 	wallet.wallet2	src/wallet/wallet2.cpp:2505	Loaded wallet keys file, with public address: 48xxx
2018-02-05 14:07:24.405	    7fb370c85b80	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:2524	Trying to decrypt cache data
2018-02-05 14:07:25.322	    7fb370c85b80	INFO 	msgwriter	src/common/scoped_message_writer.h:102	Opened watch-only wallet: 48xxx
2018-02-05 14:07:25.322	    7fb370c85b80	INFO 	msgwriter	src/common/scoped_message_writer.h:102	**********************************************************************
Use "help" command to see the list of available commands.
**********************************************************************
2018-02-05 14:07:25.322	    7fb370c85b80	DEBUG	net.http	src/common/util.cpp:569	Address '192.168.1.50:4008' is not local
2018-02-05 14:07:25.430	    7fb370c85b80	INFO 	msgwriter	src/common/scoped_message_writer.h:102	Starting refresh...
2018-02-05 14:07:25.531	    7fb370c85b80	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:1202	Daemon is recent enough, asking for pruned blocks
2018-02-05 14:10:55.531	    7fb370c85b80	DEBUG	net	contrib/epee/include/net/net_helper.h:392	Problems at read: Operation canceled
2018-02-05 14:10:55.531	    7fb370c85b80	ERROR	net.http	contrib/epee/include/net/http_client.h:444	Unexpected recv fail
2018-02-05 14:10:55.531	    7fb370c85b80	INFO 	net.http	contrib/epee/include/storages/http_abstract_invoke.h:81	Failed to invoke http request to  /getblocks.bin
2018-02-05 14:10:55.531	    7fb370c85b80	ERROR	wallet.wallet2	src/wallet/wallet2.cpp:1216	!r. THROW EXCEPTION: error::no_connection_to_daemon
2018-02-05 14:10:55.531	    7fb370c85b80	WARN 	net.http	src/wallet/wallet_errors.h:707	/DISTRIBUTION-BUILD/src/wallet/wallet2.cpp:1216:N5tools5error23no_connection_to_daemonE: no connection to daemon, request = getblocks.bin
2018-02-05 14:10:55.531	    7fb370c85b80	INFO 	stacktrace	src/common/stack_trace.cpp:120	Exception: tools::error::no_connection_to_daemon
2018-02-05 14:10:55.531	    7fb370c85b80	INFO 	stacktrace	src/common/stack_trace.cpp:121	Unwound call stack:
2018-02-05 14:10:55.535	    7fb370c85b80	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [1] ./monero-wallet-cli:__wrap___cxa_throw+0x102 [0x84e122]
2018-02-05 14:10:55.535	    7fb370c85b80	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [2] ./monero-wallet-cli:void tools::error::throw_wallet_ex<tools::error::no_connection_to_daemon, char [14]>(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&&, char const (&) [14])+0x16a [0x7bb27a]
2018-02-05 14:10:55.535	    7fb370c85b80	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [3] ./monero-wallet-cli:tools::wallet2::pull_blocks(unsigned long, unsigned long&, std::__cxx11::list<crypto::hash, std::allocator<crypto::hash> > const&, std::__cxx11::list<cryptonote::block_complete_entry, std::allocator<cryptonote::block_complete_entry> >&, std::vector<cryptonote::COMMAND_RPC_GET_BLOCKS_FAST::block_output_indices, std::allocator<cryptonote::COMMAND_RPC_GET_BLOCKS_FAST::block_output_indices> >&)+0x6b8 [0x77f208]
2018-02-05 14:10:55.535	    7fb370c85b80	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [4] ./monero-wallet-cli:tools::wallet2::refresh(unsigned long, unsigned long&, bool&)+0x1bc [0x791a9c]
2018-02-05 14:10:55.535	    7fb370c85b80	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [5] ./monero-wallet-cli:tools::wallet2::refresh(unsigned long, unsigned long&)+0x23 [0x792833]
2018-02-05 14:10:55.535	    7fb370c85b80	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [6] ./monero-wallet-cli:cryptonote::simple_wallet::refresh_main(unsigned long, bool)+0x203 [0x6acc83]
2018-02-05 14:10:55.535	    7fb370c85b80	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [7] ./monero-wallet-cli:cryptonote::simple_wallet::run()+0x36 [0x6ae636]
2018-02-05 14:10:55.535	    7fb370c85b80	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [8] ./monero-wallet-cli:main+0x532 [0x691092]
2018-02-05 14:10:55.535	    7fb370c85b80	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [9] /lib/x86_64-linux-gnu/libc.so.6:__libc_start_main+0xf1 [0x7fb36ff4b1c1]
2018-02-05 14:10:55.535	    7fb370c85b80	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [10] ./monero-wallet-cli:_start+0x29 [0x698d59]
2018-02-05 14:10:55.535	    7fb370c85b80	INFO 	stacktrace	src/common/stack_trace.cpp:159	
2018-02-05 14:10:55.535	    7fb370c85b80	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: refresh failed: no connection to daemon. Please make sure daemon is running.. Blocks received: 0
2018-02-05 14:10:55.535	    7fb370c85b80	INFO 	msgwriter	src/common/scoped_message_writer.h:102	Background refresh thread started
2018-02-05 14:10:55.662	    7fb36f310700	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:1202	Daemon is recent enough, asking for pruned blocks
2018-02-05 14:14:25.662	    7fb36f310700	DEBUG	net	contrib/epee/include/net/net_helper.h:392	Problems at read: Operation canceled
2018-02-05 14:14:25.662	    7fb36f310700	ERROR	net.http	contrib/epee/include/net/http_client.h:444	Unexpected recv fail
2018-02-05 14:14:25.663	    7fb36f310700	INFO 	net.http	contrib/epee/include/storages/http_abstract_invoke.h:81	Failed to invoke http request to  /getblocks.bin
2018-02-05 14:14:25.663	    7fb36f310700	ERROR	wallet.wallet2	src/wallet/wallet2.cpp:1216	!r. THROW EXCEPTION: error::no_connection_to_daemon
2018-02-05 14:14:25.663	    7fb36f310700	WARN 	net.http	src/wallet/wallet_errors.h:707	/DISTRIBUTION-BUILD/src/wallet/wallet2.cpp:1216:N5tools5error23no_connection_to_daemonE: no connection to daemon, request = getblocks.bin
2018-02-05 14:14:25.663	    7fb36f310700	INFO 	stacktrace	src/common/stack_trace.cpp:120	Exception: tools::error::no_connection_to_daemon
2018-02-05 14:14:25.663	    7fb36f310700	INFO 	stacktrace	src/common/stack_trace.cpp:121	Unwound call stack:
2018-02-05 14:14:25.665	    7fb36f310700	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [1] ./monero-wallet-cli:__wrap___cxa_throw+0x102 [0x84e122]
2018-02-05 14:14:25.665	    7fb36f310700	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [2] ./monero-wallet-cli:void tools::error::throw_wallet_ex<tools::error::no_connection_to_daemon, char [14]>(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&&, char const (&) [14])+0x16a [0x7bb27a]
2018-02-05 14:14:25.665	    7fb36f310700	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [3] ./monero-wallet-cli:tools::wallet2::pull_blocks(unsigned long, unsigned long&, std::__cxx11::list<crypto::hash, std::allocator<crypto::hash> > const&, std::__cxx11::list<cryptonote::block_complete_entry, std::allocator<cryptonote::block_complete_entry> >&, std::vector<cryptonote::COMMAND_RPC_GET_BLOCKS_FAST::block_output_indices, std::allocator<cryptonote::COMMAND_RPC_GET_BLOCKS_FAST::block_output_indices> >&)+0x6b8 [0x77f208]
2018-02-05 14:14:25.665	    7fb36f310700	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [4] ./monero-wallet-cli:tools::wallet2::refresh(unsigned long, unsigned long&, bool&)+0x1bc [0x791a9c]
2018-02-05 14:14:25.665	    7fb36f310700	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [5] ./monero-wallet-cli:tools::wallet2::refresh(unsigned long, unsigned long&)+0x23 [0x792833]
2018-02-05 14:14:25.665	    7fb36f310700	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [6] ./monero-wallet-cli:cryptonote::simple_wallet::wallet_idle_thread()+0x2bc [0x6ae38c]
2018-02-05 14:14:25.666	    7fb36f310700	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [7] ./monero-wallet-cli() [0x8f7f15]
2018-02-05 14:14:25.666	    7fb36f310700	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [8] /lib/x86_64-linux-gnu/libpthread.so.0+0x77fc [0x7fb3703117fc]
2018-02-05 14:14:25.666	    7fb36f310700	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [9] /lib/x86_64-linux-gnu/libc.so.6:clone+0x3f [0x7fb37003eb5f]
2018-02-05 14:14:25.666	    7fb36f310700	INFO 	stacktrace	src/common/stack_trace.cpp:159	
2018-02-05 14:14:40.666	    7fb370c85b80	DEBUG	net	contrib/epee/include/net/net_helper.h:392	Problems at read: Operation canceled
2018-02-05 14:14:40.667	    7fb370c85b80	ERROR	net.http	contrib/epee/include/net/http_client.h:444	Unexpected recv fail
2018-02-05 14:14:40.667	    7fb370c85b80	INFO 	net.http	contrib/epee/include/storages/http_abstract_invoke.h:50	Failed to invoke http request to  /json_rpc
2018-02-05 14:16:10.670	    7fb36f310700	DEBUG	net	contrib/epee/include/net/net_helper.h:392	Problems at read: Operation canceled
2018-02-05 14:16:10.670	    7fb36f310700	ERROR	net.http	contrib/epee/include/net/http_client.h:444	Unexpected recv fail
2018-02-05 14:16:10.670	    7fb36f310700	INFO 	net.http	contrib/epee/include/storages/http_abstract_invoke.h:50	Failed to invoke http request to  /json_rpc
2018-02-05 14:17:55.674	    7fb36f310700	DEBUG	net	contrib/epee/include/net/net_helper.h:392	Problems at read: Operation canceled
2018-02-05 14:17:55.674	    7fb36f310700	ERROR	net.http	contrib/epee/include/net/http_client.h:444	Unexpected recv fail
2018-02-05 14:17:55.674	    7fb36f310700	INFO 	net.http	contrib/epee/include/storages/http_abstract_invoke.h:50	Failed to invoke http request to  /json_rpc
2018-02-05 14:18:17.374	    7fb370c85b80	DEBUG	wallet.wallet2	contrib/epee/include/console_handler.h:361	Read command: refresh
2018-02-05 14:18:32.378	    7fb370c85b80	DEBUG	net	contrib/epee/include/net/net_helper.h:392	Problems at read: Operation canceled
2018-02-05 14:18:32.378	    7fb370c85b80	ERROR	net.http	contrib/epee/include/net/http_client.h:444	Unexpected recv fail
2018-02-05 14:18:32.378	    7fb370c85b80	INFO 	net.http	contrib/epee/include/storages/http_abstract_invoke.h:50	Failed to invoke http request to  /json_rpc
2018-02-05 14:18:32.378	    7fb370c85b80	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: wallet failed to connect to daemon: 192.168.1.50:4008. Daemon either is not started or wrong port was passed. Please make sure daemon is running or restart the wallet with the correct daemon address.
2018-02-05 14:18:47.384	    7fb370c85b80	DEBUG	net	contrib/epee/include/net/net_helper.h:392	Problems at read: Operation canceled
2018-02-05 14:18:47.384	    7fb370c85b80	ERROR	net.http	contrib/epee/include/net/http_client.h:444	Unexpected recv fail
2018-02-05 14:18:47.384	    7fb370c85b80	INFO 	net.http	contrib/epee/include/storages/http_abstract_invoke.h:50	Failed to invoke http request to  /json_rpc
2018-02-05 14:18:50.495	    7fb370c85b80	DEBUG	wallet.wallet2	contrib/epee/include/console_handler.h:361	Read command: exit
```

Did I do something wrong? Is there a problem with my LAN? Or is it an issue of monero-wallet-cli?


# Discussion History
## moneromooo-monero | 2018-02-05T15:20:33+00:00
Can you reach 192.168.1.50:4008 with telnet from the DHCP box ?

## cialu | 2018-02-05T15:50:06+00:00
@moneromooo-monero I can reach 192.168.1.50 through ssh without issue because the Pi is headless and I manage it remotely. 

If I do `nmap -p 4008 192.168.1.50`, I get:

```
Starting Nmap 7.60 ( https://nmap.org ) at 2018-02-05 16:42 CET
Nmap scan report for raspberrypi.box (192.168.1.50)
Host is up (0.0039s latency).

PORT     STATE SERVICE
4008/tcp open  netcheque

Nmap done: 1 IP address (1 host up) scanned in 0.06 seconds
```

With `telnet 192.168.1.50 4008`, I get:

```
Trying 192.168.1.50...
Connected to 192.168.1.50.
Escape character is '^]'.

```


## moneromooo-monero | 2018-02-05T20:12:50+00:00
Run the wallet with `--log-level 2`.
Run the daemon with `--log-level 0,perf:DEBUG`.

The first one should show more information on the timeout. The second one should show whether the RPC is actually hit.

## cialu | 2018-02-06T14:36:23+00:00
The wallet was already running with `--log-level 2` and the log output is the one above. Maybe, if you need, I can run `--log-level 3` or `--log-level 4` and post the new log.

Running the daemon with `--log-level 0,perf:DEBUG`, I get:

```
2018-02-06 14:19:47.502	        b491d3d0	INFO 	global	contrib/epee/include/net/http_server_impl_base.h:70	Binding on 192.168.1.50:4008
2018-02-06 14:19:47.508	        b491d3d0	INFO 	global	src/daemon/rpc.h:63	Core rpc server initialized OK on port: 4008
2018-02-06 14:19:47.511	        b491d3d0	INFO 	global	src/daemon/core.h:73	Initializing core...
2018-02-06 14:19:47.519	        b491d3d0	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:323	Loading blockchain from folder /home/pi/.bitmonero/lmdb ...
...
2018-02-06 14:25:20.594	[P2P4]	DEBUG	perf	src/common/perf_timer.h:75	PERF     1480      verRange
2018-02-06 14:25:21.687	[P2P4]	DEBUG	perf	src/common/perf_timer.h:75	PERF     1074      verRange
2018-02-06 14:25:21.692	[P2P4]	DEBUG	perf	src/common/perf_timer.h:75	PERF     2691    verRctSimple
2018-02-06 14:25:23.218	[P2P5]	DEBUG	perf	src/common/perf_timer.h:54	PERF             ----------
2018-02-06 14:25:23.335	[P2P5]	DEBUG	perf	src/common/perf_timer.h:62	PERF             check_tx_inputs
2018-02-06 14:25:23.342	[P2P5]	DEBUG	perf	src/common/perf_timer.h:75	PERF        6      expand_transaction_2
2018-02-06 14:25:23.361	[P2P5]	DEBUG	perf	src/common/perf_timer.h:62	PERF               verRct
2018-02-06 14:25:23.468	[P2P5]	DEBUG	perf	src/common/perf_timer.h:75	PERF      106        verRctMG
2018-02-06 14:25:23.473	[P2P5]	DEBUG	perf	src/common/perf_timer.h:75	PERF      127      verRct
2018-02-06 14:25:23.476	[P2P5]	DEBUG	perf	src/common/perf_timer.h:75	PERF      257    check_tx_inputs
2018-02-06 14:25:23.592	[P2P5]	DEBUG	perf	src/common/perf_timer.h:54	PERF             ----------
2018-02-06 14:25:23.655	[P2P5]	DEBUG	perf	src/common/perf_timer.h:62	PERF             check_tx_inputs
2018-02-06 14:25:23.662	[P2P5]	DEBUG	perf	src/common/perf_timer.h:75	PERF        6      expand_transaction_2
2018-02-06 14:25:23.681	[P2P5]	DEBUG	perf	src/common/perf_timer.h:62	PERF               verRct
2018-02-06 14:25:23.787	[P2P5]	DEBUG	perf	src/common/perf_timer.h:75	PERF      105        verRctMG
2018-02-06 14:25:23.793	[P2P5]	DEBUG	perf	src/common/perf_timer.h:75	PERF      127      verRct
2018-02-06 14:25:23.796	[P2P5]	DEBUG	perf	src/common/perf_timer.h:75	PERF      204    check_tx_inputs
2018-02-06 14:25:23.813	[P2P5]	DEBUG	perf	src/common/perf_timer.h:54	PERF             ----------
2018-02-06 14:25:23.858	[P2P5]	DEBUG	perf	src/common/perf_timer.h:62	PERF             check_tx_inputs
2018-02-06 14:25:23.864	[P2P5]	DEBUG	perf	src/common/perf_timer.h:75	PERF        5      expand_transaction_2
2018-02-06 14:25:23.883	[P2P5]	DEBUG	perf	src/common/perf_timer.h:62	PERF               verRct
2018-02-06 14:25:23.990	[P2P5]	DEBUG	perf	src/common/perf_timer.h:75	PERF      106        verRctMG
2018-02-06 14:25:23.997	[P2P5]	DEBUG	perf	src/common/perf_timer.h:75	PERF      129      verRct
2018-02-06 14:25:24.000	[P2P5]	DEBUG	perf	src/common/perf_timer.h:75	PERF      186    check_tx_inputs
2018-02-06 14:25:24.054	[P2P5]	DEBUG	perf	src/common/perf_timer.h:54	PERF             ----------
2018-02-06 14:25:24.108	[P2P5]	DEBUG	perf	src/common/perf_timer.h:62	PERF             check_tx_inputs
2018-02-06 14:25:24.114	[P2P5]	DEBUG	perf	src/common/perf_timer.h:75	PERF        6      expand_transaction_2
2018-02-06 14:25:24.133	[P2P5]	DEBUG	perf	src/common/perf_timer.h:62	PERF               verRct
2018-02-06 14:25:24.239	[P2P5]	DEBUG	perf	src/common/perf_timer.h:75	PERF      105        verRctMG
2018-02-06 14:25:24.245	[P2P5]	DEBUG	perf	src/common/perf_timer.h:75	PERF      126      verRct
2018-02-06 14:25:24.248	[P2P5]	DEBUG	perf	src/common/perf_timer.h:75	PERF      194    check_tx_inputs
2018-02-06 14:25:24.372	[P2P5]	DEBUG	perf	src/common/perf_timer.h:54	PERF             ----------
2018-02-06 14:25:24.439	[P2P5]	DEBUG	perf	src/common/perf_timer.h:62	PERF             check_tx_inputs
2018-02-06 14:25:24.445	[P2P5]	DEBUG	perf	src/common/perf_timer.h:75	PERF        6      expand_transaction_2
2018-02-06 14:25:24.464	[P2P5]	DEBUG	perf	src/common/perf_timer.h:62	PERF               verRct
2018-02-06 14:25:24.571	[P2P5]	DEBUG	perf	src/common/perf_timer.h:75	PERF      106        verRctMG
2018-02-06 14:25:24.579	[P2P5]	DEBUG	perf	src/common/perf_timer.h:75	PERF      130      verRct
2018-02-06 14:25:24.582	[P2P5]	DEBUG	perf	src/common/perf_timer.h:75	PERF      210    check_tx_inputs
2018-02-06 14:25:25.810	[P2P4]	DEBUG	perf	src/common/perf_timer.h:54	PERF             ----------
2018-02-06 14:25:25.826	[P2P4]	DEBUG	perf	src/common/perf_timer.h:62	PERF             add_tx
2018-02-06 14:25:25.833	[P2P5]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154	[191.96.249.221:18080 OUT]  Synced 1503641/1503641
2018-02-06 14:25:26.306	[P2P4]	DEBUG	perf	src/common/perf_timer.h:62	PERF               check_tx_inputs
2018-02-06 14:25:26.312	[P2P4]	DEBUG	perf	src/common/perf_timer.h:75	PERF        6        expand_transaction_2
2018-02-06 14:25:26.349	[P2P4]	DEBUG	perf	src/common/perf_timer.h:62	PERF                 verRctSimple
2018-02-06 14:25:26.439	[P2P4]	DEBUG	perf	src/common/perf_timer.h:75	PERF       90          verRctMGSimple
2018-02-06 14:25:26.531	[P2P4]	DEBUG	perf	src/common/perf_timer.h:75	PERF       85          verRctMGSimple
2018-02-06 14:25:26.536	[P2P4]	DEBUG	perf	src/common/perf_timer.h:75	PERF      220        verRctSimple
2018-02-06 14:25:26.540	[P2P4]	DEBUG	perf	src/common/perf_timer.h:75	PERF      714      check_tx_inputs
2018-02-06 14:25:26.604	[P2P5]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1521	SYNCHRONIZED OK
2018-02-06 14:25:26.707	[P2P4]	DEBUG	perf	src/common/perf_timer.h:75	PERF 18446744070  add_tx
2018-02-06 14:25:26.765	[P2P2]	DEBUG	perf	src/common/perf_timer.h:54	PERF             ----------
2018-02-06 14:25:26.800	[P2P2]	DEBUG	perf	src/common/perf_timer.h:62	PERF             verRctSimple
2018-02-06 14:25:27.931	[P2P2]	DEBUG	perf	src/common/perf_timer.h:75	PERF     1130      verRange
2018-02-06 14:25:28.991	[P2P2]	DEBUG	perf	src/common/perf_timer.h:75	PERF     1050      verRange
2018-02-06 14:25:29.018	[P2P2]	DEBUG	perf	src/common/perf_timer.h:75	PERF     2252    verRctSimple
2018-02-06 14:25:29.045	[P2P2]	DEBUG	perf	src/common/perf_timer.h:54	PERF             ----------
2018-02-06 14:25:29.085	[P2P2]	DEBUG	perf	src/common/perf_timer.h:62	PERF             add_tx
2018-02-06 14:25:29.593	[P2P2]	DEBUG	perf	src/common/perf_timer.h:62	PERF               check_tx_inputs
2018-02-06 14:25:29.600	[P2P2]	DEBUG	perf	src/common/perf_timer.h:75	PERF        6        expand_transaction_2
2018-02-06 14:25:29.615	[P2P2]	DEBUG	perf	src/common/perf_timer.h:62	PERF                 verRctSimple
2018-02-06 14:25:29.726	[P2P2]	DEBUG	perf	src/common/perf_timer.h:75	PERF      111          verRctMGSimple
2018-02-06 14:25:29.817	[P2P2]	DEBUG	perf	src/common/perf_timer.h:75	PERF       84          verRctMGSimple
2018-02-06 14:25:29.823	[P2P2]	DEBUG	perf	src/common/perf_timer.h:75	PERF      219        verRctSimple
2018-02-06 14:25:29.826	[P2P2]	DEBUG	perf	src/common/perf_timer.h:75	PERF      740      check_tx_inputs
2018-02-06 14:25:29.933	[P2P2]	DEBUG	perf	src/common/perf_timer.h:75	PERF      888    add_tx
2018-02-06 14:28:50.222	[P2P0]	DEBUG	perf	src/common/perf_timer.h:54	PERF             ----------
2018-02-06 14:28:50.298	[P2P4]	DEBUG	perf	src/common/perf_timer.h:54	PERF             ----------
2018-02-06 14:28:50.326	[P2P0]	DEBUG	perf	src/common/perf_timer.h:62	PERF             verRctSimple
2018-02-06 14:28:50.342	[P2P4]	DEBUG	perf	src/common/perf_timer.h:62	PERF             verRctSimple
...
2018-02-06 14:29:19.721	[P2P6]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154	[138.197.147.125:18080 OUT]  Synced 1503643/1503643
2018-02-06 14:29:19.910	[P2P6]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1521	SYNCHRONIZED OK
2018-02-06 14:29:19.950	[P2P7]	DEBUG	perf	src/common/perf_timer.h:54	PERF             ----------
2018-02-06 14:29:19.955	[P2P7]	DEBUG	perf	src/common/perf_timer.h:62	PERF             verRct
2018-02-06 14:29:21.124	[P2P7]	DEBUG	perf	src/common/perf_timer.h:75	PERF     1168      verRange
2018-02-06 14:29:21.533	[P2P6]	DEBUG	perf	src/common/perf_timer.h:54	PERF             ----------
2018-02-06 14:29:21.561	[P2P6]	DEBUG	perf	src/common/perf_timer.h:62	PERF             verRct
2018-02-06 14:29:22.083	[P2P4]	DEBUG	perf	src/common/perf_timer.h:54	PERF             ----------
2018-02-06 14:29:22.147	[P2P4]	DEBUG	perf	src/common/perf_timer.h:62	PERF             verRct
2018-02-06 14:29:22.280	[P2P0]	DEBUG	perf	src/common/perf_timer.h:54	PERF             ----------
2018-02-06 14:29:22.299	[P2P0]	DEBUG	perf	src/common/perf_timer.h:62	PERF             verRct
2018-02-06 14:29:23.993	[P2P7]	DEBUG	perf	src/common/perf_timer.h:75	PERF 18446744072    verRange
2018-02-06 14:29:24.018	[P2P7]	DEBUG	perf	src/common/perf_timer.h:75	PERF 18446744073  verRct
2018-02-06 14:29:24.070	[P2P7]	DEBUG	perf	src/common/perf_timer.h:54	PERF             ----------
2018-02-06 14:29:24.081	[P2P7]	DEBUG	perf	src/common/perf_timer.h:62	PERF             add_tx
2018-02-06 14:29:24.364	[P2P7]	DEBUG	perf	src/common/perf_timer.h:62	PERF               check_tx_inputs
2018-02-06 14:29:24.378	[P2P7]	DEBUG	perf	src/common/perf_timer.h:75	PERF        5        expand_transaction_2
2018-02-06 14:29:24.440	[P2P7]	DEBUG	perf	src/common/perf_timer.h:62	PERF                 verRct
2018-02-06 14:29:24.835	[P2P7]	DEBUG	perf	src/common/perf_timer.h:75	PERF      395          verRctMG
2018-02-06 14:29:24.873	[P2P7]	DEBUG	perf	src/common/perf_timer.h:75	PERF      488        verRct
2018-02-06 14:29:24.876	[P2P7]	DEBUG	perf	src/common/perf_timer.h:75	PERF      794      check_tx_inputs
2018-02-06 14:29:25.098	[P2P7]	DEBUG	perf	src/common/perf_timer.h:75	PERF     1028    add_tx
2018-02-06 14:29:25.594	[P2P6]	DEBUG	perf	src/common/perf_timer.h:75	PERF 18446744073    verRange
2018-02-06 14:29:26.216	[P2P4]	DEBUG	perf	src/common/perf_timer.h:75	PERF 18446744073    verRange
2018-02-06 14:29:26.400	[P2P0]	DEBUG	perf	src/common/perf_timer.h:75	PERF 18446744073    verRange
2018-02-06 14:29:29.242	[P2P6]	DEBUG	perf	src/common/perf_timer.h:75	PERF 18446744073    verRange
2018-02-06 14:29:29.253	[P2P6]	DEBUG	perf	src/common/perf_timer.h:75	PERF 18446744072  verRct
2018-02-06 14:29:29.738	[P2P4]	DEBUG	perf	src/common/perf_timer.h:75	PERF 18446744072    verRange
2018-02-06 14:29:29.752	[P2P4]	DEBUG	perf	src/common/perf_timer.h:75	PERF 18446744072  verRct
2018-02-06 14:29:29.760	[P2P0]	DEBUG	perf	src/common/perf_timer.h:75	PERF 18446744072    verRange
2018-02-06 14:29:29.770	[P2P0]	DEBUG	perf	src/common/perf_timer.h:75	PERF 18446744072  verRct
2018-02-06 14:29:29.822	[P2P4]	DEBUG	perf	src/common/perf_timer.h:54	PERF             ----------
...
```

And more and more messages similar to the messages above.

## ontje-dev | 2018-02-06T22:15:06+00:00
Hi, had the exact same problem using a Raspberry Pi 3.

I removed the port argument from the daemon and the port was the default one. The connection worked and i got no "Unexpected recv fail" error anymore. The wallet refreshed. 
Do not know if its a "Pi-thing" or daemon-specific.


## cialu | 2018-02-07T08:20:57+00:00
@eybeestudios If I remove the port argument, I have the same exact issue but on standard port 18081.

## ontje-dev | 2018-02-07T09:03:35+00:00
Apparently it seems to work not all the time. I had a few tries, where i got the "Unexpected recv fail" while the wallet refreshes 3.5 min (210s) after "Daemon is recent enough, asking for pruned blocks". After a fresh restart of the daemon it worked in most cases.

## cialu | 2018-02-07T11:04:10+00:00
@eybeestudios it isn't my case. Nor a relaunch nor a re-installation make it working.

## moneromooo-monero | 2018-02-07T13:12:19+00:00
That daemon log shows no daemon RPC being hit (or failing in the network code before it is). The recv fail is usually a timeout.

I have no idea what could be wrong right now.

## moneromooo-monero | 2019-06-15T10:56:55+00:00
Does it work with current release ? 

## cialu | 2019-06-17T08:32:03+00:00
> Does it work with current release ?

Sorry, I have no more a Raspberry Pi with Monero local node to test this.

# Action History
- Created by: cialu | 2018-02-05T14:31:47+00:00
- Closed at: 2022-03-16T15:32:25+00:00
