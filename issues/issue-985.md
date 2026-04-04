---
title: 'Arch Linux: Daemon failed to start'
source_url: https://github.com/monero-project/monero-gui/issues/985
author: Coehill
assignees: []
labels:
- resolved
created_at: '2017-12-03T18:02:12+00:00'
updated_at: '2018-11-18T14:54:33+00:00'
type: issue
status: closed
closed_at: '2018-11-18T14:54:33+00:00'
---

# Original Description
I just installed the Arch Linux package monero-wallet-qt for the first time, created a wallet, and then got this error message:

> Daemon failed to start
> Please check your wallet and daemon log for errors. You can also try to start monerod manually.

Here is the output of bitmonero.log


```
cat bitmonero.log 
2017-12-02 18:37:00.780	    7fe5ee0ebbc0	INFO 	logging	contrib/epee/src/mlog.cpp:148	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-12-02 18:37:00.780	    7fe5ee0ebbc0	INFO 	global	src/daemon/main.cpp:279	Monero 'Helium Hydra' (v0.11.1.0-release)
2017-12-02 18:37:00.780	    7fe5ee0ebbc0	INFO 	global	src/daemon/protocol.h:55	Initializing cryptonote protocol...
2017-12-02 18:37:00.780	    7fe5ee0ebbc0	INFO 	global	src/daemon/protocol.h:60	Cryptonote protocol initialized OK
2017-12-02 18:37:00.780	    7fe5ee0ebbc0	INFO 	global	src/daemon/p2p.h:63	Initializing p2p server...
2017-12-02 18:37:08.172	    7fe5ee0ebbc0	INFO 	global	src/daemon/p2p.h:68	P2p server initialized OK
2017-12-02 18:37:08.172	    7fe5ee0ebbc0	INFO 	global	src/daemon/rpc.h:58	Initializing core rpc server...
2017-12-02 18:37:08.172	    7fe5ee0ebbc0	INFO 	global	contrib/epee/include/net/http_server_impl_base.h:70	Binding on 127.0.0.1:18081
2017-12-02 18:37:08.173	    7fe5ee0ebbc0	INFO 	global	src/daemon/rpc.h:63	Core rpc server initialized OK on port: 18081
2017-12-02 18:37:08.173	    7fe5ee0ebbc0	INFO 	global	src/daemon/core.h:73	Initializing core...
2017-12-02 18:37:08.173	    7fe5ee0ebbc0	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:323	Loading blockchain from folder /home/my_username/.bitmonero/lmdb ...
2017-12-02 18:37:08.173	    7fe5ee0ebbc0	WARN 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:72	Error attempting to retrieve a hard fork version at height 0 from the db: MDB_NOTFOUND: No matching key/data pair found
2017-12-02 18:37:08.173	    7fe5ee0ebbc0	INFO 	stacktrace	src/common/stack_trace.cpp:120	Exception: cryptonote::DB_ERROR
2017-12-02 18:37:08.173	    7fe5ee0ebbc0	INFO 	stacktrace	src/common/stack_trace.cpp:121	Unwound call stack:
2017-12-02 18:37:08.174	    7fe5ee0ebbc0	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [1] monerod:__cxa_throw+0x111 [0x55636d7a2051]
2017-12-02 18:37:08.174	    7fe5ee0ebbc0	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [2] monerod+0x316769 [0x55636d6dd769]
2017-12-02 18:37:08.174	    7fe5ee0ebbc0	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [3] monerod:cryptonote::BlockchainLMDB::get_hard_fork_version(unsigned long) const+0x3dd [0x55636d6fda5d]
2017-12-02 18:37:08.174	    7fe5ee0ebbc0	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [4] monerod:cryptonote::HardFork::init()+0x175 [0x55636d7efb85]
2017-12-02 18:37:08.174	    7fe5ee0ebbc0	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [5] monerod:cryptonote::Blockchain::init(cryptonote::BlockchainDB*, bool, cryptonote::test_options const*)+0x227 [0x55636d72b8d7]
2017-12-02 18:37:08.174	    7fe5ee0ebbc0	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [6] monerod:cryptonote::core::init(boost::program_options::variables_map const&, cryptonote::test_options const*)+0xbc0 [0x55636d742920]
2017-12-02 18:37:08.174	    7fe5ee0ebbc0	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [7] monerod:daemonize::t_daemon::run(bool)+0x205 [0x55636d545c15]
2017-12-02 18:37:08.174	    7fe5ee0ebbc0	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [8] monerod:daemonize::t_executor::run_interactive(boost::program_options::variables_map const&)+0x30 [0x55636d613f30]
2017-12-02 18:37:08.174	    7fe5ee0ebbc0	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [9] monerod:bool daemonizer::daemonize<daemonize::t_executor>(int, char const**, daemonize::t_executor&&, boost::program_options::variables_map const&)+0x197 [0x55636d6158b7]
2017-12-02 18:37:08.174	    7fe5ee0ebbc0	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [10] monerod:main+0x174e [0x55636d51a81e]
2017-12-02 18:37:08.174	    7fe5ee0ebbc0	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [11] /usr/lib/libc.so.6:__libc_start_main+0xea [0x7fe5eb0bdf6a]
2017-12-02 18:37:08.174	    7fe5ee0ebbc0	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [12] monerod:_start+0x2a [0x55636d522dea]
2017-12-02 18:37:08.174	    7fe5ee0ebbc0	INFO 	stacktrace	src/common/stack_trace.cpp:159	
2017-12-02 18:37:08.347	    7fe5ee0ebbc0	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:421	Loading checkpoints
2017-12-02 18:37:10.475	    7fe5ee0ebbc0	INFO 	global	src/daemon/core.h:78	Core initialized OK
2017-12-02 18:37:10.475	    7fe5ee0ebbc0	INFO 	global	src/daemon/rpc.h:68	Starting core rpc server...
2017-12-02 18:37:10.475	[SRV_MAIN]	INFO 	global	src/daemon/rpc.h:73	Core rpc server started ok
2017-12-02 18:37:10.476	[SRV_MAIN]	INFO 	global	src/daemon/p2p.h:78	Starting p2p net loop...
2017-12-02 18:37:10.476	[SRV_MAIN]	INFO 	global	src/daemon/p2p.h:80	p2p net loop stopped
2017-12-02 18:37:10.476	[SRV_MAIN]	INFO 	global	src/daemon/rpc.h:78	Stopping core rpc server...
2017-12-02 18:37:10.476	[SRV_MAIN]	INFO 	global	src/daemon/daemon.cpp:145	Node stopped.
2017-12-02 18:37:10.476	[SRV_MAIN]	INFO 	global	src/daemon/rpc.h:90	Deinitializing rpc server...
2017-12-02 18:37:10.476	[SRV_MAIN]	INFO 	global	src/daemon/p2p.h:90	Deinitializing p2p...
2017-12-02 18:37:10.476	[SRV_MAIN]	INFO 	global	src/daemon/core.h:89	Deinitializing core...
2017-12-02 18:37:10.483	[SRV_MAIN]	INFO 	global	src/daemon/protocol.h:77	Stopping cryptonote protocol...

```

# Discussion History
## erciccione | 2018-11-18T14:13:27+00:00
Related to old version. Please opne an other issue if problem still exists.

+resolved

# Action History
- Created by: Coehill | 2017-12-03T18:02:12+00:00
- Closed at: 2018-11-18T14:54:33+00:00
