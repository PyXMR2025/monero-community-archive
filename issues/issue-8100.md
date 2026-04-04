---
title: 'Error: Couldn''t connect to daemon: 127.0.0.1:18081'
source_url: https://github.com/monero-project/monero/issues/8100
author: denroede
assignees: []
labels: []
created_at: '2021-12-01T08:59:54+00:00'
updated_at: '2023-06-06T01:38:00+00:00'
type: issue
status: closed
closed_at: '2023-06-06T01:38:00+00:00'
---

# Original Description
[**ORIGINAL THREAD**](https://www.reddit.com/r/monerosupport/comments/r5ki11/usual_error/)
&#x200B;
&#x200B;
&#x200B;
Hello to all!

I am writing to try to find a definitive solution to the usual error (**Couldn't connect to daemon: 127.0.0.1:18081**) that has appeared to me over and over again since using Monero from years ago.

I have always solved by recovering the blockchain from a backup created specifically from another disk, but now I would like to understand why this error keeps repeating to me so frequently.

My system is Arch Linux.

Every time it presented itself to me with a few remaining blocks from the end of the synchronization: the daemon loses its connection and from that moment on, it cannot reconnect. I've tried pretty much everything: disabling the firewall, deleting .bitmonero, `--db-salvage`, and more.

The blockchain resides on an external **encrypted** SSD: could this be the problem?

In fact, if I do `monerod` without specifying `--data-dir`, it starts normally (although I never tried to let it finish downloading the blockchain until the end).

The last 100 lines of my .log are as follows:

    2021-11-30 08:57:25.592	    7f56d46cba00	INFO	stacktrace	src/common/stack_trace.cpp:172	    [4]  0x7a) [0x55dcdfd2f33a]:_ZN5boost6detail12shared_stateINS_4asio19basic_stream_socketINS2_2ip3tcpENS2_15any_io_executorEEEE3getERNS_11unique_lockINS_5mutexEEE+0x7a) [0x55dcdfd2f33a]
    2021-11-30 08:57:25.592	    7f56d46cba00	INFO	stacktrace	src/common/stack_trace.cpp:172	    [5]  0xa05) [0x55dcdfc5b635]:_ZN4epee9net_utils19blocked_mode_client11try_connectERKNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEES9_NSt6chrono8durationIlSt5ratioILl1ELl1000EEEE+0xa05) [0x55dcdfc5b635]
    2021-11-30 08:57:25.592	    7f56d46cba00	INFO	stacktrace	src/common/stack_trace.cpp:172	    [6]  0x19d) [0x55dcdfc60c0d]:_ZN4epee9net_utils19blocked_mode_client7connectERKNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEES9_NSt6chrono8durationIlSt5ratioILl1ELl1000EEEE+0x19d) [0x55dcdfc60c0d]
    2021-11-30 08:57:25.592	    7f56d46cba00	INFO	stacktrace	src/common/stack_trace.cpp:172	    [7]  0x41) [0x55dcdfc61331]:_ZN4epee9net_utils4http27http_simple_client_templateINS0_19blocked_mode_clientEE7connectENSt6chrono8durationIlSt5ratioILl1ELl1000EEEE+0x41) [0x55dcdfc61331]
    2021-11-30 08:57:25.592	    7f56d46cba00	INFO	stacktrace	src/common/stack_trace.cpp:172	    [8]  0x1e5) [0x55dcdfc39a55]:_ZN9daemonize22t_rpc_command_executor9sync_infoEv+0x1e5) [0x55dcdfc39a55]
    2021-11-30 08:57:25.592	    7f56d46cba00	INFO	stacktrace	src/common/stack_trace.cpp:172	    [9]  0x10a) [0x55dcdfb280ca]:_ZN9daemonize16t_command_server19process_command_vecERKSt6vectorINSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEESaIS7_EE+0x10a) [0x55dcdfb280ca]
    2021-11-30 08:57:25.593	    7f56d46cba00	INFO	stacktrace	src/common/stack_trace.cpp:172	    [10] /usr/bin/monerod(main+0xe0c) [0x55dcdfb0936c] 
    2021-11-30 08:57:25.593	    7f56d46cba00	INFO	stacktrace	src/common/stack_trace.cpp:172	    [11]  0xd5) [0x7f56d4812b25]:__libc_start_main+0xd5) [0x7f56d4812b25]
    2021-11-30 08:57:25.593	    7f56d46cba00	INFO	stacktrace	src/common/stack_trace.cpp:172	    [12]  0x2e) [0x55dcdfb187be]:_start+0x2e) [0x55dcdfb187be]
    2021-11-30 08:57:25.593	    7f56d46cba00	INFO	stacktrace	src/common/stack_trace.cpp:172	
    2021-11-30 08:57:25.593	    7f56d46cba00	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
    2021-11-30 08:57:28.631	    7f2c47aa4a00	INFO	logging	contrib/epee/src/mlog.cpp:273	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
    2021-11-30 08:57:28.631	    7f2c47aa4a00	INFO	global	src/daemon/main.cpp:294	Monero 'Oxygen Orion' (v0.17.2.3-release)
    2021-11-30 08:57:28.955	    7f2c47aa4a00	INFO	stacktrace	src/common/stack_trace.cpp:133	Exception: boost::wrapexcept<boost::system::system_error>
    2021-11-30 08:57:28.955	    7f2c47aa4a00	INFO	stacktrace	src/common/stack_trace.cpp:134	Unwound call stack:
    2021-11-30 08:57:28.956	    7f2c47aa4a00	INFO	stacktrace	src/common/stack_trace.cpp:172	    [1]  0x119) [0x55879f9510c8]:__cxa_throw+0x119) [0x55879f9510c8]
    2021-11-30 08:57:28.956	    7f2c47aa4a00	INFO	stacktrace	src/common/stack_trace.cpp:172	    [2]  0x119) [0x55879f8fd1bb]:_ZNK5boost10wrapexceptINS_6system12system_errorEE7rethrowEv+0x119) [0x55879f8fd1bb]
    2021-11-30 08:57:28.956	    7f2c47aa4a00	INFO	stacktrace	src/common/stack_trace.cpp:172	    [3]  0x24) [0x55879fbc0d64]:_ZN5boost16exception_detail18rethrow_exception_ERKNS_13exception_ptrE+0x24) [0x55879fbc0d64]
    2021-11-30 08:57:28.956	    7f2c47aa4a00	INFO	stacktrace	src/common/stack_trace.cpp:172	    [4]  0x7a) [0x55879fbc533a]:_ZN5boost6detail12shared_stateINS_4asio19basic_stream_socketINS2_2ip3tcpENS2_15any_io_executorEEEE3getERNS_11unique_lockINS_5mutexEEE+0x7a) [0x55879fbc533a]
    2021-11-30 08:57:28.956	    7f2c47aa4a00	INFO	stacktrace	src/common/stack_trace.cpp:172	    [5]  0xa05) [0x55879faf1635]:_ZN4epee9net_utils19blocked_mode_client11try_connectERKNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEES9_NSt6chrono8durationIlSt5ratioILl1ELl1000EEEE+0xa05) [0x55879faf1635]
    2021-11-30 08:57:28.956	    7f2c47aa4a00	INFO	stacktrace	src/common/stack_trace.cpp:172	    [6]  0x19d) [0x55879faf6c0d]:_ZN4epee9net_utils19blocked_mode_client7connectERKNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEES9_NSt6chrono8durationIlSt5ratioILl1ELl1000EEEE+0x19d) [0x55879faf6c0d]
    2021-11-30 08:57:28.956	    7f2c47aa4a00	INFO	stacktrace	src/common/stack_trace.cpp:172	    [7]  0x41) [0x55879faf7331]:_ZN4epee9net_utils4http27http_simple_client_templateINS0_19blocked_mode_clientEE7connectENSt6chrono8durationIlSt5ratioILl1ELl1000EEEE+0x41) [0x55879faf7331]
    2021-11-30 08:57:28.956	    7f2c47aa4a00	INFO	stacktrace	src/common/stack_trace.cpp:172	    [8]  0x1e5) [0x55879facfa55]:_ZN9daemonize22t_rpc_command_executor9sync_infoEv+0x1e5) [0x55879facfa55]
    2021-11-30 08:57:28.956	    7f2c47aa4a00	INFO	stacktrace	src/common/stack_trace.cpp:172	    [9]  0x10a) [0x55879f9be0ca]:_ZN9daemonize16t_command_server19process_command_vecERKSt6vectorINSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEESaIS7_EE+0x10a) [0x55879f9be0ca]
    2021-11-30 08:57:28.956	    7f2c47aa4a00	INFO	stacktrace	src/common/stack_trace.cpp:172	    [10] /usr/bin/monerod(main+0xe0c) [0x55879f99f36c] 
    2021-11-30 08:57:28.956	    7f2c47aa4a00	INFO	stacktrace	src/common/stack_trace.cpp:172	    [11]  0xd5) [0x7f2c47bebb25]:__libc_start_main+0xd5) [0x7f2c47bebb25]
    2021-11-30 08:57:28.956	    7f2c47aa4a00	INFO	stacktrace	src/common/stack_trace.cpp:172	    [12]  0x2e) [0x55879f9ae7be]:_start+0x2e) [0x55879f9ae7be]
    2021-11-30 08:57:28.956	    7f2c47aa4a00	INFO	stacktrace	src/common/stack_trace.cpp:172	
    2021-11-30 08:57:28.957	    7f2c47aa4a00	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
    2021-11-30 08:57:31.994	    7fa7c803ba00	INFO	logging	contrib/epee/src/mlog.cpp:273	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
    2021-11-30 08:57:31.994	    7fa7c803ba00	INFO	global	src/daemon/main.cpp:294	Monero 'Oxygen Orion' (v0.17.2.3-release)
    2021-11-30 08:57:32.074	    7fa7c803ba00	INFO	stacktrace	src/common/stack_trace.cpp:133	Exception: boost::wrapexcept<boost::system::system_error>
    2021-11-30 08:57:32.074	    7fa7c803ba00	INFO	stacktrace	src/common/stack_trace.cpp:134	Unwound call stack:
    2021-11-30 08:57:32.075	    7fa7c803ba00	INFO	stacktrace	src/common/stack_trace.cpp:172	    [1]  0x119) [0x556efe4c50c8]:__cxa_throw+0x119) [0x556efe4c50c8]
    2021-11-30 08:57:32.075	    7fa7c803ba00	INFO	stacktrace	src/common/stack_trace.cpp:172	    [2]  0x119) [0x556efe4711bb]:_ZNK5boost10wrapexceptINS_6system12system_errorEE7rethrowEv+0x119) [0x556efe4711bb]
    2021-11-30 08:57:32.075	    7fa7c803ba00	INFO	stacktrace	src/common/stack_trace.cpp:172	    [3]  0x24) [0x556efe734d64]:_ZN5boost16exception_detail18rethrow_exception_ERKNS_13exception_ptrE+0x24) [0x556efe734d64]
    2021-11-30 08:57:32.075	    7fa7c803ba00	INFO	stacktrace	src/common/stack_trace.cpp:172	    [4]  0x7a) [0x556efe73933a]:_ZN5boost6detail12shared_stateINS_4asio19basic_stream_socketINS2_2ip3tcpENS2_15any_io_executorEEEE3getERNS_11unique_lockINS_5mutexEEE+0x7a) [0x556efe73933a]
    2021-11-30 08:57:32.075	    7fa7c803ba00	INFO	stacktrace	src/common/stack_trace.cpp:172	    [5]  0xa05) [0x556efe665635]:_ZN4epee9net_utils19blocked_mode_client11try_connectERKNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEES9_NSt6chrono8durationIlSt5ratioILl1ELl1000EEEE+0xa05) [0x556efe665635]
    2021-11-30 08:57:32.075	    7fa7c803ba00	INFO	stacktrace	src/common/stack_trace.cpp:172	    [6]  0x19d) [0x556efe66ac0d]:_ZN4epee9net_utils19blocked_mode_client7connectERKNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEES9_NSt6chrono8durationIlSt5ratioILl1ELl1000EEEE+0x19d) [0x556efe66ac0d]
    2021-11-30 08:57:32.075	    7fa7c803ba00	INFO	stacktrace	src/common/stack_trace.cpp:172	    [7]  0x41) [0x556efe66b331]:_ZN4epee9net_utils4http27http_simple_client_templateINS0_19blocked_mode_clientEE7connectENSt6chrono8durationIlSt5ratioILl1ELl1000EEEE+0x41) [0x556efe66b331]
    2021-11-30 08:57:32.075	    7fa7c803ba00	INFO	stacktrace	src/common/stack_trace.cpp:172	    [8]  0x1e5) [0x556efe643a55]:_ZN9daemonize22t_rpc_command_executor9sync_infoEv+0x1e5) [0x556efe643a55]
    2021-11-30 08:57:32.075	    7fa7c803ba00	INFO	stacktrace	src/common/stack_trace.cpp:172	    [9]  0x10a) [0x556efe5320ca]:_ZN9daemonize16t_command_server19process_command_vecERKSt6vectorINSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEESaIS7_EE+0x10a) [0x556efe5320ca]
    2021-11-30 08:57:32.075	    7fa7c803ba00	INFO	stacktrace	src/common/stack_trace.cpp:172	    [10] /usr/bin/monerod(main+0xe0c) [0x556efe51336c] 
    2021-11-30 08:57:32.075	    7fa7c803ba00	INFO	stacktrace	src/common/stack_trace.cpp:172	    [11]  0xd5) [0x7fa7c8182b25]:__libc_start_main+0xd5) [0x7fa7c8182b25]
    2021-11-30 08:57:32.075	    7fa7c803ba00	INFO	stacktrace	src/common/stack_trace.cpp:172	    [12]  0x2e) [0x556efe5227be]:_start+0x2e) [0x556efe5227be]
    2021-11-30 08:57:32.075	    7fa7c803ba00	INFO	stacktrace	src/common/stack_trace.cpp:172	
    2021-11-30 08:57:32.075	    7fa7c803ba00	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
    2021-11-30 08:57:35.110	    7f36a471aa00	INFO	logging	contrib/epee/src/mlog.cpp:273	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
    2021-11-30 08:57:35.110	    7f36a471aa00	INFO	global	src/daemon/main.cpp:294	Monero 'Oxygen Orion' (v0.17.2.3-release)
    2021-11-30 08:57:36.850	    7f36a471aa00	INFO	stacktrace	src/common/stack_trace.cpp:133	Exception: boost::wrapexcept<boost::system::system_error>
    2021-11-30 08:57:36.850	    7f36a471aa00	INFO	stacktrace	src/common/stack_trace.cpp:134	Unwound call stack:
    2021-11-30 08:57:36.852	    7f36a471aa00	INFO	stacktrace	src/common/stack_trace.cpp:172	    [1]  0x119) [0x55afa99070c8]:__cxa_throw+0x119) [0x55afa99070c8]
    2021-11-30 08:57:36.852	    7f36a471aa00	INFO	stacktrace	src/common/stack_trace.cpp:172	    [2]  0x119) [0x55afa98b31bb]:_ZNK5boost10wrapexceptINS_6system12system_errorEE7rethrowEv+0x119) [0x55afa98b31bb]
    2021-11-30 08:57:36.852	    7f36a471aa00	INFO	stacktrace	src/common/stack_trace.cpp:172	    [3]  0x24) [0x55afa9b76d64]:_ZN5boost16exception_detail18rethrow_exception_ERKNS_13exception_ptrE+0x24) [0x55afa9b76d64]
    2021-11-30 08:57:36.852	    7f36a471aa00	INFO	stacktrace	src/common/stack_trace.cpp:172	    [4]  0x7a) [0x55afa9b7b33a]:_ZN5boost6detail12shared_stateINS_4asio19basic_stream_socketINS2_2ip3tcpENS2_15any_io_executorEEEE3getERNS_11unique_lockINS_5mutexEEE+0x7a) [0x55afa9b7b33a]
    2021-11-30 08:57:36.852	    7f36a471aa00	INFO	stacktrace	src/common/stack_trace.cpp:172	    [5]  0xa05) [0x55afa9aa7635]:_ZN4epee9net_utils19blocked_mode_client11try_connectERKNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEES9_NSt6chrono8durationIlSt5ratioILl1ELl1000EEEE+0xa05) [0x55afa9aa7635]
    2021-11-30 08:57:36.852	    7f36a471aa00	INFO	stacktrace	src/common/stack_trace.cpp:172	    [6]  0x19d) [0x55afa9aacc0d]:_ZN4epee9net_utils19blocked_mode_client7connectERKNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEES9_NSt6chrono8durationIlSt5ratioILl1ELl1000EEEE+0x19d) [0x55afa9aacc0d]
    2021-11-30 08:57:36.852	    7f36a471aa00	INFO	stacktrace	src/common/stack_trace.cpp:172	    [7]  0x41) [0x55afa9aad331]:_ZN4epee9net_utils4http27http_simple_client_templateINS0_19blocked_mode_clientEE7connectENSt6chrono8durationIlSt5ratioILl1ELl1000EEEE+0x41) [0x55afa9aad331]
    2021-11-30 08:57:36.852	    7f36a471aa00	INFO	stacktrace	src/common/stack_trace.cpp:172	    [8]  0x1e5) [0x55afa9a85a55]:_ZN9daemonize22t_rpc_command_executor9sync_infoEv+0x1e5) [0x55afa9a85a55]
    2021-11-30 08:57:36.852	    7f36a471aa00	INFO	stacktrace	src/common/stack_trace.cpp:172	    [9]  0x10a) [0x55afa99740ca]:_ZN9daemonize16t_command_server19process_command_vecERKSt6vectorINSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEESaIS7_EE+0x10a) [0x55afa99740ca]
    2021-11-30 08:57:36.852	    7f36a471aa00	INFO	stacktrace	src/common/stack_trace.cpp:172	    [10] /usr/bin/monerod(main+0xe0c) [0x55afa995536c] 
    2021-11-30 08:57:36.852	    7f36a471aa00	INFO	stacktrace	src/common/stack_trace.cpp:172	    [11]  0xd5) [0x7f36a4861b25]:__libc_start_main+0xd5) [0x7f36a4861b25]
    2021-11-30 08:57:36.852	    7f36a471aa00	INFO	stacktrace	src/common/stack_trace.cpp:172	    [12]  0x2e) [0x55afa99647be]:_start+0x2e) [0x55afa99647be]
    2021-11-30 08:57:36.852	    7f36a471aa00	INFO	stacktrace	src/common/stack_trace.cpp:172	
    2021-11-30 08:57:36.852	    7f36a471aa00	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
    2021-11-30 08:57:39.890	    7fe626a33a00	INFO	logging	contrib/epee/src/mlog.cpp:273	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
    2021-11-30 08:57:39.890	    7fe626a33a00	INFO	global	src/daemon/main.cpp:294	Monero 'Oxygen Orion' (v0.17.2.3-release)
    2021-11-30 08:57:40.340	    7fe626a33a00	INFO	stacktrace	src/common/stack_trace.cpp:133	Exception: boost::wrapexcept<boost::system::system_error>
    2021-11-30 08:57:40.340	    7fe626a33a00	INFO	stacktrace	src/common/stack_trace.cpp:134	Unwound call stack:
    2021-11-30 08:57:40.342	    7fe626a33a00	INFO	stacktrace	src/common/stack_trace.cpp:172	    [1]  0x119) [0x5644cdc990c8]:__cxa_throw+0x119) [0x5644cdc990c8]
    2021-11-30 08:57:40.342	    7fe626a33a00	INFO	stacktrace	src/common/stack_trace.cpp:172	    [2]  0x119) [0x5644cdc451bb]:_ZNK5boost10wrapexceptINS_6system12system_errorEE7rethrowEv+0x119) [0x5644cdc451bb]
    2021-11-30 08:57:40.342	    7fe626a33a00	INFO	stacktrace	src/common/stack_trace.cpp:172	    [3]  0x24) [0x5644cdf08d64]:_ZN5boost16exception_detail18rethrow_exception_ERKNS_13exception_ptrE+0x24) [0x5644cdf08d64]
    2021-11-30 08:57:40.342	    7fe626a33a00	INFO	stacktrace	src/common/stack_trace.cpp:172	    [4]  0x7a) [0x5644cdf0d33a]:_ZN5boost6detail12shared_stateINS_4asio19basic_stream_socketINS2_2ip3tcpENS2_15any_io_executorEEEE3getERNS_11unique_lockINS_5mutexEEE+0x7a) [0x5644cdf0d33a]
    2021-11-30 08:57:40.342	    7fe626a33a00	INFO	stacktrace	src/common/stack_trace.cpp:172	    [5]  0xa05) [0x5644cde39635]:_ZN4epee9net_utils19blocked_mode_client11try_connectERKNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEES9_NSt6chrono8durationIlSt5ratioILl1ELl1000EEEE+0xa05) [0x5644cde39635]
    2021-11-30 08:57:40.342	    7fe626a33a00	INFO	stacktrace	src/common/stack_trace.cpp:172	    [6]  0x19d) [0x5644cde3ec0d]:_ZN4epee9net_utils19blocked_mode_client7connectERKNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEES9_NSt6chrono8durationIlSt5ratioILl1ELl1000EEEE+0x19d) [0x5644cde3ec0d]
    2021-11-30 08:57:40.342	    7fe626a33a00	INFO	stacktrace	src/common/stack_trace.cpp:172	    [7]  0x41) [0x5644cde3f331]:_ZN4epee9net_utils4http27http_simple_client_templateINS0_19blocked_mode_clientEE7connectENSt6chrono8durationIlSt5ratioILl1ELl1000EEEE+0x41) [0x5644cde3f331]
    2021-11-30 08:57:40.342	    7fe626a33a00	INFO	stacktrace	src/common/stack_trace.cpp:172	    [8]  0x1e5) [0x5644cde17a55]:_ZN9daemonize22t_rpc_command_executor9sync_infoEv+0x1e5) [0x5644cde17a55]
    2021-11-30 08:57:40.342	    7fe626a33a00	INFO	stacktrace	src/common/stack_trace.cpp:172	    [9]  0x10a) [0x5644cdd060ca]:_ZN9daemonize16t_command_server19process_command_vecERKSt6vectorINSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEESaIS7_EE+0x10a) [0x5644cdd060ca]
    2021-11-30 08:57:40.342	    7fe626a33a00	INFO	stacktrace	src/common/stack_trace.cpp:172	    [10] /usr/bin/monerod(main+0xe0c) [0x5644cdce736c] 
    2021-11-30 08:57:40.342	    7fe626a33a00	INFO	stacktrace	src/common/stack_trace.cpp:172	    [11]  0xd5) [0x7fe626b7ab25]:__libc_start_main+0xd5) [0x7fe626b7ab25]
    2021-11-30 08:57:40.342	    7fe626a33a00	INFO	stacktrace	src/common/stack_trace.cpp:172	    [12]  0x2e) [0x5644cdcf67be]:_start+0x2e) [0x5644cdcf67be]
    2021-11-30 08:57:40.342	    7fe626a33a00	INFO	stacktrace	src/common/stack_trace.cpp:172	
    2021-11-30 08:57:40.342	    7fe626a33a00	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
    2021-11-30 09:22:06.902	    7f735b7dca00	INFO	logging	contrib/epee/src/mlog.cpp:273	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
    2021-11-30 09:22:06.903	    7f735b7dca00	INFO	global	src/daemon/main.cpp:294	Monero 'Oxygen Orion' (v0.17.2.3-release)
    2021-11-30 09:22:07.183	    7f735b7dca00	INFO	stacktrace	src/common/stack_trace.cpp:133	Exception: boost::wrapexcept<boost::system::system_error>
    2021-11-30 09:22:07.183	    7f735b7dca00	INFO	stacktrace	src/common/stack_trace.cpp:134	Unwound call stack:
    2021-11-30 09:22:07.184	    7f735b7dca00	INFO	stacktrace	src/common/stack_trace.cpp:172	    [1]  0x119) [0x56374b0f40c8]:__cxa_throw+0x119) [0x56374b0f40c8]
    2021-11-30 09:22:07.184	    7f735b7dca00	INFO	stacktrace	src/common/stack_trace.cpp:172	    [2]  0x119) [0x56374b0a01bb]:_ZNK5boost10wrapexceptINS_6system12system_errorEE7rethrowEv+0x119) [0x56374b0a01bb]
    2021-11-30 09:22:07.184	    7f735b7dca00	INFO	stacktrace	src/common/stack_trace.cpp:172	    [3]  0x24) [0x56374b363d64]:_ZN5boost16exception_detail18rethrow_exception_ERKNS_13exception_ptrE+0x24) [0x56374b363d64]
    2021-11-30 09:22:07.184	    7f735b7dca00	INFO	stacktrace	src/common/stack_trace.cpp:172	    [4]  0x7a) [0x56374b36833a]:_ZN5boost6detail12shared_stateINS_4asio19basic_stream_socketINS2_2ip3tcpENS2_15any_io_executorEEEE3getERNS_11unique_lockINS_5mutexEEE+0x7a) [0x56374b36833a]
    2021-11-30 09:22:07.184	    7f735b7dca00	INFO	stacktrace	src/common/stack_trace.cpp:172	    [5]  0xa05) [0x56374b294635]:_ZN4epee9net_utils19blocked_mode_client11try_connectERKNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEES9_NSt6chrono8durationIlSt5ratioILl1ELl1000EEEE+0xa05) [0x56374b294635]
    2021-11-30 09:22:07.184	    7f735b7dca00	INFO	stacktrace	src/common/stack_trace.cpp:172	    [6]  0x19d) [0x56374b299c0d]:_ZN4epee9net_utils19blocked_mode_client7connectERKNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEES9_NSt6chrono8durationIlSt5ratioILl1ELl1000EEEE+0x19d) [0x56374b299c0d]
    2021-11-30 09:22:07.184	    7f735b7dca00	INFO	stacktrace	src/common/stack_trace.cpp:172	    [7]  0x82) [0x56374b2ec032]:_ZN5tools12t_rpc_client11rpc_requestIN4epee10misc_utils11struct_initIN10cryptonote20COMMAND_RPC_GET_INFO9request_tEEENS4_INS6_10response_tEEEEEbRT_RT0_RKNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEESM_+0x82) [0x56374b2ec032]
    2021-11-30 09:22:07.184	    7f735b7dca00	INFO	stacktrace	src/common/stack_trace.cpp:172	    [8]  0x2c7) [0x56374b27cdc7]:_ZN9daemonize22t_rpc_command_executor11show_statusEv+0x2c7) [0x56374b27cdc7]
    2021-11-30 09:22:07.184	    7f735b7dca00	INFO	stacktrace	src/common/stack_trace.cpp:172	    [9]  0x10a) [0x56374b1610ca]:_ZN9daemonize16t_command_server19process_command_vecERKSt6vectorINSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEESaIS7_EE+0x10a) [0x56374b1610ca]
    2021-11-30 09:22:07.184	    7f735b7dca00	INFO	stacktrace	src/common/stack_trace.cpp:172	    [10] monerod(main+0xe0c) [0x56374b14236c] 
    2021-11-30 09:22:07.184	    7f735b7dca00	INFO	stacktrace	src/common/stack_trace.cpp:172	    [11]  0xd5) [0x7f735b923b25]:__libc_start_main+0xd5) [0x7f735b923b25]
    2021-11-30 09:22:07.184	    7f735b7dca00	INFO	stacktrace	src/common/stack_trace.cpp:172	    [12]  0x2e) [0x56374b1517be]:_start+0x2e) [0x56374b1517be]
    2021-11-30 09:22:07.184	    7f735b7dca00	INFO	stacktrace	src/common/stack_trace.cpp:172	
    2021-11-30 09:22:07.184	    7f735b7dca00	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081

Among other things, there are three strange things:

1. It does not seem that the blockchain file is corrupt because the related message does not appear in the log file.
2. By giving `monerod --data-dir /path/of/my/external/SSD`, Monero sees that disk is a *rotating drive* rather than an SSD.
3. The log file timestamps are wrong respect to my system time.

&#x200B;

What could be causing this error to occur so frequently that a second copy of the entire blockchain has to be kept on another disk?

&#x200B;

**EDIT:** I forgot to specify (but I think this is understood) that this is a full local node.

Also I do not use Ledger, Trezor and other various useless.

# Discussion History
## hyc | 2021-12-01T09:55:11+00:00
> By giving monerod --data-dir /path/of/my/external/SSD, Monero sees that disk is a rotating drive rather than an SSD.

That message is meaningless. The OS thinks all USB-attached drives are HDDs. Ignore it.

> The log file timestamps are wrong respect to my system time.

Logfile timestamps are in UTC timezone.


## DavidBruchmann | 2022-01-22T12:23:41+00:00
@PautassoEGiacomina perhaps #8151 is helping a bit?

## selsta | 2022-02-18T23:15:02+00:00
Did you ever try to use a different drive?

## selsta | 2023-06-06T01:38:00+00:00
No reply from issue creator.

# Action History
- Created by: denroede | 2021-12-01T08:59:54+00:00
- Closed at: 2023-06-06T01:38:00+00:00
