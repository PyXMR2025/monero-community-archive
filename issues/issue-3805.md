---
title: 'Error: Couldn''t connect to daemon'
source_url: https://github.com/monero-project/monero-gui/issues/3805
author: ghost
assignees: []
labels: []
created_at: '2021-12-15T09:15:01+00:00'
updated_at: '2022-06-30T19:31:41+00:00'
type: issue
status: closed
closed_at: '2022-04-27T04:50:07+00:00'
---

# Original Description
Way back, I started a local node for my Monero wallet and downloaded about 100GB of the blockchain so far. But then, all of a sudden, I can't connect to daemon anymore.

Every time I try, I get this error.
```
Daemon failed to start
Timed out, local node is not responding after 120 seconds.
Please check your wallet and daemon log for errors. You can also try to start monerod manually.
```

I recreated the error with Log level 2 and here are the following results.
```
Monero 'Oxygen Orion' (v0.17.2.3-release)
Error: Couldn't connect to daemon: 127.0.0.1:18081
```

Further info:
```
GUI version: 0.17.2.3-113efbf (Qt 5.15.2)
Embedded Monero version: 0.17.2.3-release
Wallet path: /home/user/Monero/wallets/user/user
Wallet restore height: 2470000
Wallet log path: /home/user/.bitmonero/monero-wallet-gui.log
Wallet mode: Advanced mode (Local node)
Graphics mode: OpenGL
```

I also tried monerod while setting my wallet in the --data-dir option
Here's what I got in the CLI.
```
$ sudo monerod --data-dir /media/user/adc2a35f-1c70-47aa-a3fb-bd1281fb9356/XMR --log-level 2
2021-12-15 08:55:29.525	I Monero 'Oxygen Orion' (v0.17.2.3-release)
2021-12-15 08:55:29.526	I Moving from main() into the daemonize now.
2021-12-15 08:55:29.526	I Initializing cryptonote protocol...
2021-12-15 08:55:29.526	I Cryptonote protocol initialized OK
2021-12-15 08:55:29.526	I Initializing core...
2021-12-15 08:55:29.526	I Loading blockchain from folder /media/user/adc2a35f-1c70-47aa-a3fb-bd1281fb9356/XMR/lmdb ...
2021-12-15 08:55:29.526	D option: fast
2021-12-15 08:55:29.526	D option: async
2021-12-15 08:55:29.526	D option: 250000000bytes
2021-12-15 08:55:29.526	W The blockchain is on a rotating drive: this will be very slow, use an SSD if possible
2021-12-15 08:55:29.605	D DB map size:     127079849984
2021-12-15 08:55:29.605	D Space used:      113424539648
2021-12-15 08:55:29.605	D Space remaining: 13655310336
2021-12-15 08:55:29.605	D Size threshold:  0
2021-12-15 08:55:29.606	D Percent used: 89.2545  Percent threshold: 90.0000
2021-12-15 08:55:29.606	D Setting m_height to: 2382847
malloc(): invalid size (unsorted)
Aborted
```

Last of all, here are the last 100 lines in my bitmonero.log file
```
2021-11-19 11:39:44.552	    72de8c807780	INFO	global	src/daemon/protocol.h:58	Cryptonote protocol initialized OK
2021-11-19 11:39:44.553	    72de8c807780	INFO	global	src/daemon/core.h:63	Initializing core...
2021-11-19 11:39:44.556	    72de8c807780	INFO	global	src/cryptonote_core/cryptonote_core.cpp:515	Loading blockchain from folder /media/user/BlockChains/XMR/lmdb ...
2021-11-19 11:39:44.558	    72de8c807780	WARNING	global	src/blockchain_db/lmdb/db_lmdb.cpp:1353	The blockchain is on a rotating drive: this will be very slow, use an SSD if possible
2021-11-19 11:42:34.931	    74f85d41b780	INFO	logging	contrib/epee/src/mlog.cpp:273	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
2021-11-19 11:42:34.932	    74f85d41b780	INFO	global	src/daemon/main.cpp:294	Monero 'Oxygen Orion' (v0.17.2.3-release)
2021-11-19 11:42:34.933	    74f85d41b780	INFO	msgwriter	src/common/scoped_message_writer.h:102	Forking to background...
2021-11-19 11:42:34.934	    74f85d41b780	WARNING	daemon	src/daemon/executor.cpp:61	Monero 'Oxygen Orion' (v0.17.2.3-release) Daemonised
2021-11-19 11:42:34.934	    74f85d41b780	INFO	global	src/daemon/protocol.h:53	Initializing cryptonote protocol...
2021-11-19 11:42:34.935	    74f85d41b780	INFO	global	src/daemon/protocol.h:58	Cryptonote protocol initialized OK
2021-11-19 11:42:34.935	    74f85d41b780	INFO	global	src/daemon/core.h:63	Initializing core...
2021-11-19 11:42:34.936	    74f85d41b780	INFO	global	src/cryptonote_core/cryptonote_core.cpp:515	Loading blockchain from folder /media/user/BlockChains/XMR/lmdb ...
2021-11-19 11:42:34.937	    74f85d41b780	WARNING	global	src/blockchain_db/lmdb/db_lmdb.cpp:1353	The blockchain is on a rotating drive: this will be very slow, use an SSD if possible
2021-11-19 12:38:21.986	    7e79e6526780	INFO	logging	contrib/epee/src/mlog.cpp:273	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
2021-11-19 12:38:22.014	    7e79e6526780	INFO	global	src/daemon/main.cpp:294	Monero 'Oxygen Orion' (v0.17.2.3-release)
2021-11-19 12:38:22.015	    7e79e6526780	INFO	msgwriter	src/common/scoped_message_writer.h:102	Forking to background...
2021-11-19 12:38:22.016	    7e79e6526780	WARNING	daemon	src/daemon/executor.cpp:61	Monero 'Oxygen Orion' (v0.17.2.3-release) Daemonised
2021-11-19 12:38:22.016	    7e79e6526780	INFO	global	src/daemon/protocol.h:53	Initializing cryptonote protocol...
2021-11-19 12:38:22.016	    7e79e6526780	INFO	global	src/daemon/protocol.h:58	Cryptonote protocol initialized OK
2021-11-19 12:38:22.017	    7e79e6526780	INFO	global	src/daemon/core.h:63	Initializing core...
2021-11-19 12:38:22.018	    7e79e6526780	INFO	global	src/cryptonote_core/cryptonote_core.cpp:515	Loading blockchain from folder /media/user/BlockChains/XMR/lmdb ...
2021-11-19 12:38:22.019	    7e79e6526780	WARNING	global	src/blockchain_db/lmdb/db_lmdb.cpp:1353	The blockchain is on a rotating drive: this will be very slow, use an SSD if possible
2021-11-22 13:06:34.891	    7a7fb3809780	INFO	logging	contrib/epee/src/mlog.cpp:273	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
2021-11-22 13:06:34.910	    7a7fb3809780	INFO	global	src/daemon/main.cpp:294	Monero 'Oxygen Orion' (v0.17.2.3-release)
2021-11-22 13:06:34.910	    7a7fb3809780	INFO	msgwriter	src/common/scoped_message_writer.h:102	Forking to background...
2021-11-22 13:06:34.912	    7a7fb3809780	WARNING	daemon	src/daemon/executor.cpp:61	Monero 'Oxygen Orion' (v0.17.2.3-release) Daemonised
2021-11-22 13:06:34.912	    7a7fb3809780	INFO	global	src/daemon/protocol.h:53	Initializing cryptonote protocol...
2021-11-22 13:06:34.912	    7a7fb3809780	INFO	global	src/daemon/protocol.h:58	Cryptonote protocol initialized OK
2021-11-22 13:06:34.913	    7a7fb3809780	INFO	global	src/daemon/core.h:63	Initializing core...
2021-11-22 13:06:34.914	    7a7fb3809780	INFO	global	src/cryptonote_core/cryptonote_core.cpp:515	Loading blockchain from folder /media/user/BlockChains/XMR/lmdb ...
2021-11-22 13:06:34.914	    7a7fb3809780	WARNING	global	src/blockchain_db/lmdb/db_lmdb.cpp:1353	The blockchain is on a rotating drive: this will be very slow, use an SSD if possible
2021-11-23 18:11:04.009	    79d493048780	INFO	logging	contrib/epee/src/mlog.cpp:273	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
2021-11-23 18:11:04.020	    79d493048780	INFO	global	src/daemon/main.cpp:294	Monero 'Oxygen Orion' (v0.17.2.3-release)
2021-11-23 18:11:04.021	    79d493048780	INFO	msgwriter	src/common/scoped_message_writer.h:102	Forking to background...
2021-11-23 18:11:04.023	    79d493048780	WARNING	daemon	src/daemon/executor.cpp:61	Monero 'Oxygen Orion' (v0.17.2.3-release) Daemonised
2021-11-23 18:11:04.023	    79d493048780	INFO	global	src/daemon/protocol.h:53	Initializing cryptonote protocol...
2021-11-23 18:11:04.023	    79d493048780	INFO	global	src/daemon/protocol.h:58	Cryptonote protocol initialized OK
2021-11-23 18:11:04.023	    79d493048780	INFO	global	src/daemon/core.h:63	Initializing core...
2021-11-23 18:11:04.025	    79d493048780	INFO	global	src/cryptonote_core/cryptonote_core.cpp:515	Loading blockchain from folder /media/user/BlockChains/XMR/lmdb ...
2021-11-23 18:11:04.026	    79d493048780	WARNING	global	src/blockchain_db/lmdb/db_lmdb.cpp:1353	The blockchain is on a rotating drive: this will be very slow, use an SSD if possible
2021-11-26 12:25:21.430	    7c8759506780	INFO	logging	contrib/epee/src/mlog.cpp:273	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
2021-11-26 12:25:21.472	    7c8759506780	INFO	global	src/daemon/main.cpp:294	Monero 'Oxygen Orion' (v0.17.2.3-release)
2021-11-26 12:25:21.473	    7c8759506780	INFO	msgwriter	src/common/scoped_message_writer.h:102	Forking to background...
2021-11-26 12:25:21.475	    7c8759506780	WARNING	daemon	src/daemon/executor.cpp:61	Monero 'Oxygen Orion' (v0.17.2.3-release) Daemonised
2021-11-26 12:25:21.475	    7c8759506780	INFO	global	src/daemon/protocol.h:53	Initializing cryptonote protocol...
2021-11-26 12:25:21.475	    7c8759506780	INFO	global	src/daemon/protocol.h:58	Cryptonote protocol initialized OK
2021-11-26 12:25:21.477	    7c8759506780	INFO	global	src/daemon/core.h:63	Initializing core...
2021-11-26 12:25:21.477	    7c8759506780	INFO	global	src/cryptonote_core/cryptonote_core.cpp:515	Loading blockchain from folder /media/user/BlockChains/XMR/lmdb ...
2021-11-26 12:25:21.479	    7c8759506780	WARNING	global	src/blockchain_db/lmdb/db_lmdb.cpp:1353	The blockchain is on a rotating drive: this will be very slow, use an SSD if possible
2021-11-26 19:45:17.162	    74929b24b780	INFO	logging	contrib/epee/src/mlog.cpp:273	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
2021-11-26 19:45:17.175	    74929b24b780	INFO	global	src/daemon/main.cpp:294	Monero 'Oxygen Orion' (v0.17.2.3-release)
2021-11-26 19:45:17.175	    74929b24b780	INFO	msgwriter	src/common/scoped_message_writer.h:102	Forking to background...
2021-11-26 19:45:17.176	    74929b24b780	WARNING	daemon	src/daemon/executor.cpp:61	Monero 'Oxygen Orion' (v0.17.2.3-release) Daemonised
2021-11-26 19:45:17.176	    74929b24b780	INFO	global	src/daemon/protocol.h:53	Initializing cryptonote protocol...
2021-11-26 19:45:17.176	    74929b24b780	INFO	global	src/daemon/protocol.h:58	Cryptonote protocol initialized OK
2021-11-26 19:45:17.177	    74929b24b780	INFO	global	src/daemon/core.h:63	Initializing core...
2021-11-26 19:45:17.178	    74929b24b780	INFO	global	src/cryptonote_core/cryptonote_core.cpp:515	Loading blockchain from folder /media/user/adc2a35f-1c70-47aa-a3fb-bd1281fb9356/XMR/lmdb ...
2021-11-26 19:45:17.178	    74929b24b780	WARNING	global	src/blockchain_db/lmdb/db_lmdb.cpp:1353	The blockchain is on a rotating drive: this will be very slow, use an SSD if possible
2021-12-15 08:52:24.849	    785ff5a30780	INFO	logging	contrib/epee/src/mlog.cpp:273	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
2021-12-15 08:52:24.866	    785ff5a30780	INFO	global	src/daemon/main.cpp:294	Monero 'Oxygen Orion' (v0.17.2.3-release)
2021-12-15 08:52:24.866	    785ff5a30780	INFO	global	src/daemon/protocol.h:53	Initializing cryptonote protocol...
2021-12-15 08:52:24.867	    785ff5a30780	INFO	global	src/daemon/protocol.h:58	Cryptonote protocol initialized OK
2021-12-15 08:52:24.867	    785ff5a30780	INFO	global	src/daemon/core.h:63	Initializing core...
2021-12-15 08:52:24.867	    785ff5a30780	INFO	global	src/cryptonote_core/cryptonote_core.cpp:515	Loading blockchain from folder /media/user/adc2a35f-1c70-47aa-a3fb-bd1281fb9356/XMR/lmdb ...
2021-12-15 08:52:24.867	    785ff5a30780	WARNING	global	src/blockchain_db/lmdb/db_lmdb.cpp:1353	The blockchain is on a rotating drive: this will be very slow, use an SSD if possible
2021-12-15 08:54:27.667	    7231fede8780	INFO	logging	contrib/epee/src/mlog.cpp:273	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
2021-12-15 08:54:27.667	    7231fede8780	INFO	logging	contrib/epee/src/mlog.cpp:273	New log categories: *:DEBUG
2021-12-15 08:54:27.667	    7231fede8780	INFO	global	src/daemon/main.cpp:294	Monero 'Oxygen Orion' (v0.17.2.3-release)
2021-12-15 08:54:27.667	    7231fede8780	INFO	daemon	src/daemon/main.cpp:356	Moving from main() into the daemonize now.
2021-12-15 08:54:27.667	    7231fede8780	INFO	global	src/daemon/protocol.h:53	Initializing cryptonote protocol...
2021-12-15 08:54:27.667	    7231fede8780	INFO	global	src/daemon/protocol.h:58	Cryptonote protocol initialized OK
2021-12-15 08:54:27.668	    7231fede8780	INFO	global	src/daemon/core.h:63	Initializing core...
2021-12-15 08:54:27.668	    7231fede8780	INFO	global	src/cryptonote_core/cryptonote_core.cpp:515	Loading blockchain from folder /media/user/adc2a35f-1c70-47aa-a3fb-bd1281fb9356/XMR/lmdb ...
2021-12-15 08:54:27.668	    7231fede8780	DEBUG	cn	src/cryptonote_core/cryptonote_core.cpp:543	option: fast
2021-12-15 08:54:27.668	    7231fede8780	DEBUG	cn	src/cryptonote_core/cryptonote_core.cpp:543	option: async
2021-12-15 08:54:27.668	    7231fede8780	DEBUG	cn	src/cryptonote_core/cryptonote_core.cpp:543	option: 250000000bytes
2021-12-15 08:54:27.668	    7231fede8780	WARNING	global	src/blockchain_db/lmdb/db_lmdb.cpp:1353	The blockchain is on a rotating drive: this will be very slow, use an SSD if possible
2021-12-15 08:54:27.668	    7231fede8780	DEBUG	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:608	DB map size:     127079849984
2021-12-15 08:54:27.668	    7231fede8780	DEBUG	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:609	Space used:      113424539648
2021-12-15 08:54:27.668	    7231fede8780	DEBUG	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:610	Space remaining: 13655310336
2021-12-15 08:54:27.668	    7231fede8780	DEBUG	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:611	Size threshold:  0
2021-12-15 08:54:27.669	    7231fede8780	DEBUG	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:613	Percent used: 89.2545  Percent threshold: 90.0000
2021-12-15 08:54:27.669	    7231fede8780	DEBUG	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1483	Setting m_height to: 2382847
2021-12-15 08:55:29.502	    75e8d24c3780	INFO	logging	contrib/epee/src/mlog.cpp:273	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
2021-12-15 08:55:29.525	    75e8d24c3780	INFO	logging	contrib/epee/src/mlog.cpp:273	New log categories: *:DEBUG
2021-12-15 08:55:29.525	    75e8d24c3780	INFO	global	src/daemon/main.cpp:294	Monero 'Oxygen Orion' (v0.17.2.3-release)
2021-12-15 08:55:29.526	    75e8d24c3780	INFO	daemon	src/daemon/main.cpp:356	Moving from main() into the daemonize now.
2021-12-15 08:55:29.526	    75e8d24c3780	INFO	global	src/daemon/protocol.h:53	Initializing cryptonote protocol...
2021-12-15 08:55:29.526	    75e8d24c3780	INFO	global	src/daemon/protocol.h:58	Cryptonote protocol initialized OK
2021-12-15 08:55:29.526	    75e8d24c3780	INFO	global	src/daemon/core.h:63	Initializing core...
2021-12-15 08:55:29.526	    75e8d24c3780	INFO	global	src/cryptonote_core/cryptonote_core.cpp:515	Loading blockchain from folder /media/user/adc2a35f-1c70-47aa-a3fb-bd1281fb9356/XMR/lmdb ...
2021-12-15 08:55:29.526	    75e8d24c3780	DEBUG	cn	src/cryptonote_core/cryptonote_core.cpp:543	option: fast
2021-12-15 08:55:29.526	    75e8d24c3780	DEBUG	cn	src/cryptonote_core/cryptonote_core.cpp:543	option: async
2021-12-15 08:55:29.526	    75e8d24c3780	DEBUG	cn	src/cryptonote_core/cryptonote_core.cpp:543	option: 250000000bytes
2021-12-15 08:55:29.526	    75e8d24c3780	WARNING	global	src/blockchain_db/lmdb/db_lmdb.cpp:1353	The blockchain is on a rotating drive: this will be very slow, use an SSD if possible
2021-12-15 08:55:29.605	    75e8d24c3780	DEBUG	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:608	DB map size:     127079849984
2021-12-15 08:55:29.605	    75e8d24c3780	DEBUG	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:609	Space used:      113424539648
2021-12-15 08:55:29.605	    75e8d24c3780	DEBUG	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:610	Space remaining: 13655310336
2021-12-15 08:55:29.605	    75e8d24c3780	DEBUG	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:611	Size threshold:  0
2021-12-15 08:55:29.606	    75e8d24c3780	DEBUG	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:613	Percent used: 89.2545  Percent threshold: 90.0000
2021-12-15 08:55:29.606	    75e8d24c3780	DEBUG	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1483	Setting m_height to: 2382847
```

Any help would be much appreciated.
Thank you.

# Discussion History
## selsta | 2021-12-15T09:18:14+00:00
It means the blockchain is corrupted. That can happen if you unplug the external hard drive during sync for example.

Unfortunately you will have to delete the blockchain and resync. Also I would recommend to use v0.17.3.0, it will sync a bit faster due to fresh checkpoints.

## ghost | 2021-12-15T10:26:02+00:00
Thank you.

I just upgraded Monero and reformatted my external drive to an XFS partition.
However, I just ran into the same error as before.
```
Daemon failed to start
Timed out, local node is not responding after 120 seconds.
Please check your wallet and daemon log for errors. You can also try to start monerod manually.
```
Here's what I got from my monero-wallet-gui.log file
```
2021-12-15 10:19:24.689	    78b580efec40	INFO	logging	contrib/epee/src/mlog.cpp:273	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
2021-12-15 10:19:24.690	    78b580efec40	WARNING	frontend	src/wallet/api/wallet.cpp:412	Logging to "/home/user/.bitmonero/monero-wallet-gui.log"
2021-12-15 10:19:24.692	    78b580efec40	WARNING	frontend	src/wallet/api/wallet.cpp:412	qrc:/qt-project.org/imports/QtQuick/Controls/ApplicationWindow.qml:259:9: QML ContentItem: Binding loop detected for property "implicitWidth"
2021-12-15 10:20:18.580	    78b580efec40	INFO	logging	contrib/epee/src/mlog.cpp:273	New log categories: *:DEBUG
2021-12-15 10:20:18.581	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	transfer page loaded
2021-12-15 10:20:18.582	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	opening wallet at:  /home/user/Monero/wallets/user/user , network type:  mainnet
2021-12-15 10:20:18.582	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Displaying processing splash
2021-12-15 10:20:18.583	    78b53d587700	INFO	net	contrib/epee/include/net/net_parse_helpers.h:141	[PARSE URI] regex not matched for uri: ^((.*?)://)?(\[(.*)\](:(\d+))?)(.*)?
2021-12-15 10:20:18.583	    78b53cd86700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Wallet* WalletManager::openWallet(const QString&, const QString&, NetworkType::Type, quint64): opening wallet at /home/user/Monero/wallets/user/user, nettype = 0 
2021-12-15 10:20:18.585	    78b53cd86700	DEBUG	device.ledger	src/device/device_ledger.cpp:305	Device 0 Created
2021-12-15 10:20:18.586	    78b53d587700	INFO	net.ssl	contrib/epee/src/net_ssl.cpp:131	Generating SSL certificate
2021-12-15 10:20:18.589	    78b53cd86700	INFO	wallet.wallet2	src/wallet/wallet2.cpp:7649	ringdb path set to /home/user/.shared-ringdb
2021-12-15 10:20:18.671	    78b53cd86700	INFO	wallet.wallet2	src/wallet/wallet2.cpp:7673	caching ringdb key
2021-12-15 10:20:18.713	    78b53cd86700	WARNING	wallet.wallet2	src/wallet/wallet2.cpp:5619	Loaded wallet keys file, with public address: 42kZ7DYvXBcTA6SwdbfuReQKcxgC2o9NZSDbiUZZEqf17yRjpA3L91rFPtwsgoDd5iHNZxpzPaKEUbmBBCtpLwZGKNGZPjS
2021-12-15 10:20:18.714	    78b53cd86700	INFO	wallet.wallet2	src/wallet/wallet2.cpp:5650	Trying to decrypt cache data
2021-12-15 10:20:18.747	    78b53cd86700	INFO	wallet.mms	src/wallet/message_store.cpp:779	No message store file found: /home/user/Monero/wallets/user/user.mms
2021-12-15 10:20:18.747	    78b53cd86700	DEBUG	wallet.wallet2	src/wallet/api/address_book.cpp:94	Refreshing addressbook
2021-12-15 10:20:18.747	    78b53cd86700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Wallet* WalletManager::openWallet(const QString&, const QString&, NetworkType::Type, quint64): opened wallet: 42kZ7DYvXBcTA6SwdbfuReQKcxgC2o9NZSDbiUZZEqf17yRjpA3L91rFPtwsgoDd5iHNZxpzPaKEUbmBBCtpLwZGKNGZPjS, status: 0
2021-12-15 10:20:18.943	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Hiding processing splash
2021-12-15 10:20:18.945	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	>>> wallet opened: Wallet(0x653e73449a60)
2021-12-15 10:20:18.947	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Recovering from seed:  true
2021-12-15 10:20:18.947	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	restore Height 2470000
2021-12-15 10:20:18.947	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	initializing with daemon address:  localhost:18081
2021-12-15 10:20:18.948	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	"initAsync: localhost:18081"
2021-12-15 10:20:18.948	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Wallet connection status changed 3
2021-12-15 10:20:18.948	    78b53cd86700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	init non async
2021-12-15 10:20:18.948	    78b53cd86700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	RESTORING
2021-12-15 10:20:18.948	    78b57bd17700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	sending external cmd:  ("sync_info")
2021-12-15 10:20:18.948	    78b53cd86700	INFO	wallet.wallet2	src/wallet/wallet2.cpp:1361	setting daemon to localhost:18081
2021-12-15 10:20:18.948	    78b53cd86700	INFO	net	contrib/epee/include/net/net_parse_helpers.h:141	[PARSE URI] regex not matched for uri: ^((.*?)://)?(\[(.*)\](:(\d+))?)(.*)?
2021-12-15 10:20:18.948	    78b53cd86700	INFO	net.ssl	contrib/epee/src/net_ssl.cpp:131	Generating SSL certificate
2021-12-15 10:20:21.001	    78b57bd17700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	"2021-12-15 10:20:20.065\tI Monero 'Oxygen Orion' (v0.17.3.0-release)\nError: Couldn't connect to daemon: 127.0.0.1:18081\n"
2021-12-15 10:20:26.915	    78b57bd17700	DEBUG	net.http	contrib/epee/include/net/http_client.h:246	Reconnecting...
2021-12-15 10:20:27.088	    78b57bd17700	DEBUG	net	contrib/epee/include/net/net_helper.h:238	Some problems at connect, message: Connection refused
2021-12-15 10:20:27.088	    78b57bd17700	DEBUG	net.http	contrib/epee/include/net/http_client.h:249	Failed to connect to localhost:18081
2021-12-15 10:20:27.088	    78b53d587700	DEBUG	net.http	contrib/epee/include/net/http_client.h:246	Reconnecting...
2021-12-15 10:20:27.099	    78b57bd17700	INFO	net.http	contrib/epee/include/storages/http_abstract_invoke.h:53	Failed to invoke http request to  /mining_status
2021-12-15 10:20:27.299	    78b53d587700	DEBUG	net	contrib/epee/include/net/net_helper.h:238	Some problems at connect, message: Connection refused
2021-12-15 10:20:27.299	    78b53d587700	DEBUG	net.http	contrib/epee/include/net/http_client.h:249	Failed to connect to localhost:18081
2021-12-15 10:20:27.299	    78b53d587700	INFO	net.http	contrib/epee/include/storages/http_abstract_invoke.h:53	Failed to invoke http request to  /mining_status
2021-12-15 10:20:28.118	    78b57bd17700	DEBUG	net.http	contrib/epee/include/net/http_client.h:246	Reconnecting...
2021-12-15 10:20:28.270	    78b57bd17700	DEBUG	net	contrib/epee/include/net/net_helper.h:238	Some problems at connect, message: Connection refused
2021-12-15 10:20:28.270	    78b57bd17700	DEBUG	net.http	contrib/epee/include/net/http_client.h:249	Failed to connect to localhost:18081
2021-12-15 10:20:28.270	    78b57bd17700	INFO	net.http	contrib/epee/include/storages/http_abstract_invoke.h:53	Failed to invoke http request to  /mining_status
2021-12-15 10:20:28.796	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Settings page loaded
2021-12-15 10:20:30.118	    78b53d587700	DEBUG	net.http	contrib/epee/include/net/http_client.h:246	Reconnecting...
2021-12-15 10:20:30.267	    78b53d587700	DEBUG	net	contrib/epee/include/net/net_helper.h:238	Some problems at connect, message: Connection refused
2021-12-15 10:20:30.267	    78b53d587700	DEBUG	net.http	contrib/epee/include/net/http_client.h:249	Failed to connect to localhost:18081
2021-12-15 10:20:30.267	    78b53d587700	INFO	net.http	contrib/epee/include/storages/http_abstract_invoke.h:53	Failed to invoke http request to  /mining_status
2021-12-15 10:20:32.151	    78b57bd17700	DEBUG	net.http	contrib/epee/include/net/http_client.h:246	Reconnecting...
2021-12-15 10:20:32.307	    78b57bd17700	DEBUG	net	contrib/epee/include/net/net_helper.h:238	Some problems at connect, message: Connection refused
2021-12-15 10:20:32.307	    78b57bd17700	DEBUG	net.http	contrib/epee/include/net/http_client.h:249	Failed to connect to localhost:18081
2021-12-15 10:20:32.307	    78b57bd17700	INFO	net.http	contrib/epee/include/storages/http_abstract_invoke.h:53	Failed to invoke http request to  /mining_status
2021-12-15 10:20:34.075	    78b53d587700	DEBUG	net.http	contrib/epee/include/net/http_client.h:246	Reconnecting...
2021-12-15 10:20:34.243	    78b53d587700	DEBUG	net	contrib/epee/include/net/net_helper.h:238	Some problems at connect, message: Connection refused
2021-12-15 10:20:34.243	    78b53d587700	DEBUG	net.http	contrib/epee/include/net/http_client.h:249	Failed to connect to localhost:18081
2021-12-15 10:20:34.243	    78b53d587700	INFO	net.http	contrib/epee/include/storages/http_abstract_invoke.h:53	Failed to invoke http request to  /mining_status
2021-12-15 10:20:35.273	    78b580efec40	WARNING	frontend	src/wallet/api/wallet.cpp:412	Model size of -9 is less than 0
2021-12-15 10:20:36.023	    78b57bd17700	DEBUG	net.http	contrib/epee/include/net/http_client.h:246	Reconnecting...
2021-12-15 10:20:36.173	    78b57bd17700	DEBUG	net	contrib/epee/include/net/net_helper.h:238	Some problems at connect, message: Connection refused
2021-12-15 10:20:36.174	    78b57bd17700	DEBUG	net.http	contrib/epee/include/net/http_client.h:249	Failed to connect to localhost:18081
2021-12-15 10:20:36.174	    78b57bd17700	INFO	net.http	contrib/epee/include/storages/http_abstract_invoke.h:53	Failed to invoke http request to  /mining_status
2021-12-15 10:20:37.943	    78b53d587700	DEBUG	net.http	contrib/epee/include/net/http_client.h:246	Reconnecting...
2021-12-15 10:20:38.092	    78b53d587700	DEBUG	net	contrib/epee/include/net/net_helper.h:238	Some problems at connect, message: Connection refused
2021-12-15 10:20:38.092	    78b53d587700	DEBUG	net.http	contrib/epee/include/net/http_client.h:249	Failed to connect to localhost:18081
2021-12-15 10:20:38.092	    78b53d587700	INFO	net.http	contrib/epee/include/storages/http_abstract_invoke.h:53	Failed to invoke http request to  /mining_status
2021-12-15 10:20:38.977	    78b53cd86700	INFO	net	contrib/epee/include/net/net_parse_helpers.h:141	[PARSE URI] regex not matched for uri: ^((.*?)://)?(\[(.*)\](:(\d+))?)(.*)?
2021-12-15 10:20:39.123	    78b53cd86700	DEBUG	util	src/common/util.cpp:915	Address 'localhost:18081' is local
2021-12-15 10:20:39.123	    78b53cd86700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	init async finished - starting refresh
2021-12-15 10:20:39.123	    78b53cd86700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Checking connection status
2021-12-15 10:20:39.268	    78b53cd86700	DEBUG	net	contrib/epee/include/net/net_helper.h:238	Some problems at connect, message: Connection refused
2021-12-15 10:20:39.273	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Wallet connection status changed 0
2021-12-15 10:20:39.422	    78b57b516700	DEBUG	net	contrib/epee/include/net/net_helper.h:238	Some problems at connect, message: Connection refused
2021-12-15 10:20:39.422	    78b57b516700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	refreshed
2021-12-15 10:20:39.422	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	>>> wallet refreshed
2021-12-15 10:20:39.422	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	>>> wallet updated
2021-12-15 10:20:39.424	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	>>> wallet updated
2021-12-15 10:20:40.548	    78b580efec40	WARNING	frontend	src/wallet/api/wallet.cpp:412	QXcbConnection: XCB error: 3 (BadWindow), sequence: 2113, resource id: 33589082, major code: 40 (TranslateCoords), minor code: 0
2021-12-15 10:20:45.879	    78b53d587700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Checking connection status
2021-12-15 10:20:45.880	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Wallet connection status changed 3
2021-12-15 10:20:46.068	    78b53d587700	DEBUG	net	contrib/epee/include/net/net_helper.h:238	Some problems at connect, message: Connection refused
2021-12-15 10:20:46.069	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Wallet connection status changed 0
2021-12-15 10:20:49.654	    78b57b516700	DEBUG	net	contrib/epee/include/net/net_helper.h:238	Some problems at connect, message: Connection refused
2021-12-15 10:20:49.654	    78b57b516700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	refreshed
2021-12-15 10:20:49.655	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	>>> wallet refreshed
2021-12-15 10:20:49.655	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	>>> wallet updated
2021-12-15 10:20:49.655	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	>>> wallet updated
2021-12-15 10:20:53.734	    78b53cd86700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Checking connection status
2021-12-15 10:20:53.735	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Wallet connection status changed 3
2021-12-15 10:20:53.919	    78b53cd86700	DEBUG	net	contrib/epee/include/net/net_helper.h:238	Some problems at connect, message: Connection refused
2021-12-15 10:20:53.928	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Wallet connection status changed 0
2021-12-15 10:20:59.881	    78b57b516700	DEBUG	net	contrib/epee/include/net/net_helper.h:238	Some problems at connect, message: Connection refused
2021-12-15 10:20:59.881	    78b57b516700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	refreshed
2021-12-15 10:20:59.882	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	>>> wallet refreshed
2021-12-15 10:20:59.882	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Checking connection status
2021-12-15 10:20:59.882	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	>>> wallet updated
2021-12-15 10:20:59.883	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Wallet connection status changed 3
2021-12-15 10:20:59.883	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	>>> wallet updated
2021-12-15 10:21:00.031	    78b53d587700	DEBUG	net	contrib/epee/include/net/net_helper.h:238	Some problems at connect, message: Connection refused
2021-12-15 10:21:00.039	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Wallet connection status changed 0
2021-12-15 10:21:05.621	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	" [] "
2021-12-15 10:21:05.621	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	"starting monerod /usr/bin/monerod"
2021-12-15 10:21:05.621	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	With command line arguments  ("--detach", "--data-dir", "/media/user/Crypto/XMR", "--prune-blockchain", "--check-updates", "disabled", "--non-interactive", "--max-concurrency", "1")
2021-12-15 10:21:07.101	    78b53cd86700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Checking connection status
2021-12-15 10:21:07.102	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Wallet connection status changed 3
2021-12-15 10:21:07.290	    78b53d587700	DEBUG	net	contrib/epee/include/net/net_helper.h:238	Some problems at connect, message: Connection refused
2021-12-15 10:21:07.300	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Wallet connection status changed 0
2021-12-15 10:21:07.682	    78b57bd17700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	sending external cmd:  ("sync_info")
2021-12-15 10:21:09.956	    78b57bd17700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	"2021-12-15 10:21:08.745\tI Monero 'Oxygen Orion' (v0.17.3.0-release)\nError: Couldn't connect to daemon: 127.0.0.1:18081\n"
2021-12-15 10:21:09.956	    78b57bd17700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	daemon not running. checking again in 2 seconds.
2021-12-15 10:21:11.956	    78b57bd17700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	sending external cmd:  ("sync_info")
2021-12-15 10:21:13.398	    78b57bd17700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	"2021-12-15 10:21:12.997\tI Monero 'Oxygen Orion' (v0.17.3.0-release)\nError: Couldn't connect to daemon: 127.0.0.1:18081\n"
2021-12-15 10:21:13.398	    78b57bd17700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	daemon not running. checking again in 2 seconds.
2021-12-15 10:21:14.348	    78b53cd86700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Checking connection status
2021-12-15 10:21:14.348	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Wallet connection status changed 3
2021-12-15 10:21:14.520	    78b53cd86700	DEBUG	net	contrib/epee/include/net/net_helper.h:238	Some problems at connect, message: Connection refused
2021-12-15 10:21:14.522	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Wallet connection status changed 0
2021-12-15 10:21:15.399	    78b57bd17700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	sending external cmd:  ("sync_info")
2021-12-15 10:21:16.739	    78b57bd17700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	"2021-12-15 10:21:16.464\tI Monero 'Oxygen Orion' (v0.17.3.0-release)\nError: Couldn't connect to daemon: 127.0.0.1:18081\n"
2021-12-15 10:21:16.739	    78b57bd17700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	daemon not running. checking again in 2 seconds.
2021-12-15 10:21:18.740	    78b57bd17700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	sending external cmd:  ("sync_info")
2021-12-15 10:21:20.328	    78b57bd17700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	"2021-12-15 10:21:19.793\tI Monero 'Oxygen Orion' (v0.17.3.0-release)\nError: Couldn't connect to daemon: 127.0.0.1:18081\n"
2021-12-15 10:21:20.328	    78b57bd17700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	daemon not running. checking again in 2 seconds.
2021-12-15 10:21:20.456	    78b53d587700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Checking connection status
2021-12-15 10:21:20.457	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Wallet connection status changed 3
2021-12-15 10:21:20.636	    78b53d587700	DEBUG	net	contrib/epee/include/net/net_helper.h:238	Some problems at connect, message: Connection refused
2021-12-15 10:21:20.642	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Wallet connection status changed 0
2021-12-15 10:21:22.329	    78b57bd17700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	sending external cmd:  ("sync_info")
2021-12-15 10:21:23.655	    78b57bd17700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	"2021-12-15 10:21:23.382\tI Monero 'Oxygen Orion' (v0.17.3.0-release)\nError: Couldn't connect to daemon: 127.0.0.1:18081\n"
2021-12-15 10:21:23.655	    78b57bd17700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	daemon not running. checking again in 2 seconds.
2021-12-15 10:21:25.655	    78b57bd17700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	sending external cmd:  ("sync_info")
2021-12-15 10:21:26.538	    78b53cd86700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Checking connection status
2021-12-15 10:21:26.539	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Wallet connection status changed 3
2021-12-15 10:21:26.686	    78b53d587700	DEBUG	net	contrib/epee/include/net/net_helper.h:238	Some problems at connect, message: Connection refused
2021-12-15 10:21:26.689	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Wallet connection status changed 0
2021-12-15 10:21:27.147	    78b57bd17700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	"2021-12-15 10:21:26.713\tI Monero 'Oxygen Orion' (v0.17.3.0-release)\nError: Couldn't connect to daemon: 127.0.0.1:18081\n"
2021-12-15 10:21:27.147	    78b57bd17700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	daemon not running. checking again in 2 seconds.
2021-12-15 10:21:29.148	    78b57bd17700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	sending external cmd:  ("sync_info")
2021-12-15 10:21:30.308	    78b57bd17700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	"2021-12-15 10:21:30.208\tI Monero 'Oxygen Orion' (v0.17.3.0-release)\nError: Couldn't connect to daemon: 127.0.0.1:18081\n"
2021-12-15 10:21:30.308	    78b57bd17700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	daemon not running. checking again in 2 seconds.
2021-12-15 10:21:32.308	    78b57bd17700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	sending external cmd:  ("sync_info")
2021-12-15 10:21:32.617	    78b53cd86700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Checking connection status
2021-12-15 10:21:32.619	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Wallet connection status changed 3
2021-12-15 10:21:32.772	    78b53cd86700	DEBUG	net	contrib/epee/include/net/net_helper.h:238	Some problems at connect, message: Connection refused
2021-12-15 10:21:32.772	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Wallet connection status changed 0
2021-12-15 10:21:33.649	    78b57bd17700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	"2021-12-15 10:21:33.351\tI Monero 'Oxygen Orion' (v0.17.3.0-release)\nError: Couldn't connect to daemon: 127.0.0.1:18081\n"
2021-12-15 10:21:33.649	    78b57bd17700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	daemon not running. checking again in 2 seconds.
2021-12-15 10:21:35.649	    78b57bd17700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	sending external cmd:  ("sync_info")
2021-12-15 10:21:36.812	    78b57bd17700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	"2021-12-15 10:21:36.712\tI Monero 'Oxygen Orion' (v0.17.3.0-release)\nError: Couldn't connect to daemon: 127.0.0.1:18081\n"
2021-12-15 10:21:36.813	    78b57bd17700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	daemon not running. checking again in 2 seconds.
2021-12-15 10:21:38.813	    78b57bd17700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	sending external cmd:  ("sync_info")
2021-12-15 10:21:40.216	    78b57bd17700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	"2021-12-15 10:21:39.872\tI Monero 'Oxygen Orion' (v0.17.3.0-release)\nError: Couldn't connect to daemon: 127.0.0.1:18081\n"
2021-12-15 10:21:40.216	    78b57bd17700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	daemon not running. checking again in 2 seconds.
2021-12-15 10:21:40.598	    78b53cd86700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Checking connection status
2021-12-15 10:21:40.599	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Wallet connection status changed 3
2021-12-15 10:21:40.782	    78b53cd86700	DEBUG	net	contrib/epee/include/net/net_helper.h:238	Some problems at connect, message: Connection refused
2021-12-15 10:21:40.783	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Wallet connection status changed 0
2021-12-15 10:21:42.216	    78b57bd17700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	sending external cmd:  ("sync_info")
2021-12-15 10:21:43.514	    78b57bd17700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	"2021-12-15 10:21:43.280\tI Monero 'Oxygen Orion' (v0.17.3.0-release)\nError: Couldn't connect to daemon: 127.0.0.1:18081\n"
2021-12-15 10:21:43.514	    78b57bd17700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	daemon not running. checking again in 2 seconds.
2021-12-15 10:21:45.515	    78b57bd17700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	sending external cmd:  ("sync_info")
2021-12-15 10:21:46.732	    78b53d587700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Checking connection status
2021-12-15 10:21:46.740	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Wallet connection status changed 3
2021-12-15 10:21:46.891	    78b53d587700	DEBUG	net	contrib/epee/include/net/net_helper.h:238	Some problems at connect, message: Connection refused
2021-12-15 10:21:46.901	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Wallet connection status changed 0
2021-12-15 10:21:47.364	    78b57bd17700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	"2021-12-15 10:21:46.551\tI Monero 'Oxygen Orion' (v0.17.3.0-release)\nError: Couldn't connect to daemon: 127.0.0.1:18081\n"
2021-12-15 10:21:47.364	    78b57bd17700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	daemon not running. checking again in 2 seconds.
2021-12-15 10:21:49.364	    78b57bd17700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	sending external cmd:  ("sync_info")
2021-12-15 10:21:50.552	    78b57bd17700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	"2021-12-15 10:21:50.405\tI Monero 'Oxygen Orion' (v0.17.3.0-release)\nError: Couldn't connect to daemon: 127.0.0.1:18081\n"
2021-12-15 10:21:50.553	    78b57bd17700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	daemon not running. checking again in 2 seconds.
2021-12-15 10:21:52.553	    78b57bd17700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	sending external cmd:  ("sync_info")
2021-12-15 10:21:52.891	    78b53cd86700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Checking connection status
2021-12-15 10:21:52.894	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Wallet connection status changed 3
2021-12-15 10:21:53.043	    78b53cd86700	DEBUG	net	contrib/epee/include/net/net_helper.h:238	Some problems at connect, message: Connection refused
2021-12-15 10:21:53.044	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Wallet connection status changed 0
2021-12-15 10:21:54.094	    78b57bd17700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	"2021-12-15 10:21:53.604\tI Monero 'Oxygen Orion' (v0.17.3.0-release)\nError: Couldn't connect to daemon: 127.0.0.1:18081\n"
2021-12-15 10:21:54.094	    78b57bd17700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	daemon not running. checking again in 2 seconds.
2021-12-15 10:21:56.095	    78b57bd17700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	sending external cmd:  ("sync_info")
2021-12-15 10:21:57.668	    78b57bd17700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	"2021-12-15 10:21:57.162\tI Monero 'Oxygen Orion' (v0.17.3.0-release)\nError: Couldn't connect to daemon: 127.0.0.1:18081\n"
2021-12-15 10:21:57.668	    78b57bd17700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	daemon not running. checking again in 2 seconds.
2021-12-15 10:21:58.992	    78b53d587700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Checking connection status
2021-12-15 10:21:58.992	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Wallet connection status changed 3
2021-12-15 10:21:59.156	    78b53d587700	DEBUG	net	contrib/epee/include/net/net_helper.h:238	Some problems at connect, message: Connection refused
2021-12-15 10:21:59.158	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Wallet connection status changed 0
2021-12-15 10:21:59.668	    78b57bd17700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	sending external cmd:  ("sync_info")
2021-12-15 10:22:01.308	    78b57bd17700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	"2021-12-15 10:22:00.720\tI Monero 'Oxygen Orion' (v0.17.3.0-release)\nError: Couldn't connect to daemon: 127.0.0.1:18081\n"
2021-12-15 10:22:01.308	    78b57bd17700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	daemon not running. checking again in 2 seconds.
2021-12-15 10:22:03.310	    78b57bd17700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	sending external cmd:  ("sync_info")
2021-12-15 10:22:05.106	    78b53cd86700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Checking connection status
2021-12-15 10:22:05.112	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Wallet connection status changed 3
2021-12-15 10:22:05.269	    78b53cd86700	DEBUG	net	contrib/epee/include/net/net_helper.h:238	Some problems at connect, message: Connection refused
2021-12-15 10:22:05.275	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Wallet connection status changed 0
2021-12-15 10:22:06.226	    78b57bd17700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	"2021-12-15 10:22:04.359\tI Monero 'Oxygen Orion' (v0.17.3.0-release)\nError: Couldn't connect to daemon: 127.0.0.1:18081\n"
2021-12-15 10:22:06.226	    78b57bd17700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	daemon not running. checking again in 2 seconds.
2021-12-15 10:22:08.227	    78b57bd17700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	sending external cmd:  ("sync_info")
2021-12-15 10:22:09.933	    78b57bd17700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	"2021-12-15 10:22:09.286\tI Monero 'Oxygen Orion' (v0.17.3.0-release)\nError: Couldn't connect to daemon: 127.0.0.1:18081\n"
2021-12-15 10:22:09.933	    78b57bd17700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	daemon not running. checking again in 2 seconds.
2021-12-15 10:22:11.211	    78b53d587700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Checking connection status
2021-12-15 10:22:11.220	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Wallet connection status changed 3
2021-12-15 10:22:11.387	    78b53d587700	DEBUG	net	contrib/epee/include/net/net_helper.h:238	Some problems at connect, message: Connection refused
2021-12-15 10:22:11.395	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Wallet connection status changed 0
2021-12-15 10:22:11.936	    78b57bd17700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	sending external cmd:  ("sync_info")
2021-12-15 10:22:13.771	    78b57bd17700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	"2021-12-15 10:22:12.998\tI Monero 'Oxygen Orion' (v0.17.3.0-release)\nError: Couldn't connect to daemon: 127.0.0.1:18081\n"
2021-12-15 10:22:13.771	    78b57bd17700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	daemon not running. checking again in 2 seconds.
2021-12-15 10:22:15.773	    78b57bd17700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	sending external cmd:  ("sync_info")
2021-12-15 10:22:17.338	    78b53cd86700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Checking connection status
2021-12-15 10:22:17.344	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Wallet connection status changed 3
2021-12-15 10:22:17.411	    78b57bd17700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	"2021-12-15 10:22:16.841\tI Monero 'Oxygen Orion' (v0.17.3.0-release)\nError: Couldn't connect to daemon: 127.0.0.1:18081\n"
2021-12-15 10:22:17.411	    78b57bd17700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	daemon not running. checking again in 2 seconds.
2021-12-15 10:22:17.493	    78b53cd86700	DEBUG	net	contrib/epee/include/net/net_helper.h:238	Some problems at connect, message: Connection refused
2021-12-15 10:22:17.493	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Wallet connection status changed 0
2021-12-15 10:22:19.412	    78b57bd17700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	sending external cmd:  ("sync_info")
2021-12-15 10:22:20.892	    78b57bd17700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	"2021-12-15 10:22:20.474\tI Monero 'Oxygen Orion' (v0.17.3.0-release)\nError: Couldn't connect to daemon: 127.0.0.1:18081\n"
2021-12-15 10:22:20.892	    78b57bd17700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	daemon not running. checking again in 2 seconds.
2021-12-15 10:22:22.892	    78b57bd17700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	sending external cmd:  ("sync_info")
2021-12-15 10:22:23.481	    78b53d587700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Checking connection status
2021-12-15 10:22:23.481	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Wallet connection status changed 3
2021-12-15 10:22:23.627	    78b53d587700	DEBUG	net	contrib/epee/include/net/net_helper.h:238	Some problems at connect, message: Connection refused
2021-12-15 10:22:23.633	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Wallet connection status changed 0
2021-12-15 10:22:24.680	    78b57bd17700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	"2021-12-15 10:22:23.933\tI Monero 'Oxygen Orion' (v0.17.3.0-release)\nError: Couldn't connect to daemon: 127.0.0.1:18081\n"
2021-12-15 10:22:24.680	    78b57bd17700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	daemon not running. checking again in 2 seconds.
2021-12-15 10:22:26.680	    78b57bd17700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	sending external cmd:  ("sync_info")
2021-12-15 10:22:28.287	    78b57bd17700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	"2021-12-15 10:22:27.741\tI Monero 'Oxygen Orion' (v0.17.3.0-release)\nError: Couldn't connect to daemon: 127.0.0.1:18081\n"
2021-12-15 10:22:28.287	    78b57bd17700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	daemon not running. checking again in 2 seconds.
2021-12-15 10:22:29.533	    78b53cd86700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Checking connection status
2021-12-15 10:22:29.534	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Wallet connection status changed 3
2021-12-15 10:22:29.694	    78b53cd86700	DEBUG	net	contrib/epee/include/net/net_helper.h:238	Some problems at connect, message: Connection refused
2021-12-15 10:22:29.703	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Wallet connection status changed 0
2021-12-15 10:22:30.288	    78b57bd17700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	sending external cmd:  ("sync_info")
2021-12-15 10:22:31.463	    78b57bd17700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	"2021-12-15 10:22:31.342\tI Monero 'Oxygen Orion' (v0.17.3.0-release)\nError: Couldn't connect to daemon: 127.0.0.1:18081\n"
2021-12-15 10:22:31.463	    78b57bd17700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	daemon not running. checking again in 2 seconds.
2021-12-15 10:22:33.467	    78b57bd17700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	sending external cmd:  ("sync_info")
2021-12-15 10:22:34.979	    78b57bd17700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	"2021-12-15 10:22:34.582\tI Monero 'Oxygen Orion' (v0.17.3.0-release)\nError: Couldn't connect to daemon: 127.0.0.1:18081\n"
2021-12-15 10:22:34.979	    78b57bd17700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	daemon not running. checking again in 2 seconds.
2021-12-15 10:22:35.591	    78b53d587700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Checking connection status
2021-12-15 10:22:35.596	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Wallet connection status changed 3
2021-12-15 10:22:35.776	    78b53d587700	DEBUG	net	contrib/epee/include/net/net_helper.h:238	Some problems at connect, message: Connection refused
2021-12-15 10:22:35.777	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Wallet connection status changed 0
2021-12-15 10:22:36.980	    78b57bd17700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	sending external cmd:  ("sync_info")
2021-12-15 10:22:38.082	    78b57bd17700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	"2021-12-15 10:22:38.035\tI Monero 'Oxygen Orion' (v0.17.3.0-release)\nError: Couldn't connect to daemon: 127.0.0.1:18081\n"
2021-12-15 10:22:38.082	    78b57bd17700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	daemon not running. checking again in 2 seconds.
2021-12-15 10:22:40.082	    78b57bd17700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	sending external cmd:  ("sync_info")
2021-12-15 10:22:41.621	    78b53cd86700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Checking connection status
2021-12-15 10:22:41.627	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Wallet connection status changed 3
2021-12-15 10:22:41.666	    78b57bd17700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	"2021-12-15 10:22:41.120\tI Monero 'Oxygen Orion' (v0.17.3.0-release)\nError: Couldn't connect to daemon: 127.0.0.1:18081\n"
2021-12-15 10:22:41.666	    78b57bd17700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	daemon not running. checking again in 2 seconds.
2021-12-15 10:22:41.779	    78b53cd86700	DEBUG	net	contrib/epee/include/net/net_helper.h:238	Some problems at connect, message: Connection refused
2021-12-15 10:22:41.788	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Wallet connection status changed 0
2021-12-15 10:22:43.666	    78b57bd17700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	sending external cmd:  ("sync_info")
2021-12-15 10:22:45.539	    78b57bd17700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	"2021-12-15 10:22:44.726\tI Monero 'Oxygen Orion' (v0.17.3.0-release)\nError: Couldn't connect to daemon: 127.0.0.1:18081\n"
2021-12-15 10:22:45.539	    78b57bd17700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	daemon not running. checking again in 2 seconds.
2021-12-15 10:22:47.540	    78b57bd17700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	sending external cmd:  ("sync_info")
2021-12-15 10:22:47.644	    78b53d587700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Checking connection status
2021-12-15 10:22:47.647	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Wallet connection status changed 3
2021-12-15 10:22:47.812	    78b53d587700	DEBUG	net	contrib/epee/include/net/net_helper.h:238	Some problems at connect, message: Connection refused
2021-12-15 10:22:47.812	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Wallet connection status changed 0
2021-12-15 10:22:48.829	    78b57bd17700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	"2021-12-15 10:22:48.582\tI Monero 'Oxygen Orion' (v0.17.3.0-release)\nError: Couldn't connect to daemon: 127.0.0.1:18081\n"
2021-12-15 10:22:48.829	    78b57bd17700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	daemon not running. checking again in 2 seconds.
2021-12-15 10:22:50.829	    78b57bd17700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	sending external cmd:  ("sync_info")
2021-12-15 10:22:51.990	    78b57bd17700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	"2021-12-15 10:22:51.894\tI Monero 'Oxygen Orion' (v0.17.3.0-release)\nError: Couldn't connect to daemon: 127.0.0.1:18081\n"
2021-12-15 10:22:51.990	    78b57bd17700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	daemon not running. checking again in 2 seconds.
2021-12-15 10:22:53.712	    78b53cd86700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Checking connection status
2021-12-15 10:22:53.712	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Wallet connection status changed 3
2021-12-15 10:22:53.880	    78b53cd86700	DEBUG	net	contrib/epee/include/net/net_helper.h:238	Some problems at connect, message: Connection refused
2021-12-15 10:22:53.881	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Wallet connection status changed 0
2021-12-15 10:22:53.994	    78b57bd17700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	sending external cmd:  ("sync_info")
2021-12-15 10:22:55.545	    78b57bd17700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	"2021-12-15 10:22:55.050\tI Monero 'Oxygen Orion' (v0.17.3.0-release)\nError: Couldn't connect to daemon: 127.0.0.1:18081\n"
2021-12-15 10:22:55.545	    78b57bd17700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	daemon not running. checking again in 2 seconds.
2021-12-15 10:22:57.546	    78b57bd17700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	sending external cmd:  ("sync_info")
2021-12-15 10:22:58.856	    78b57bd17700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	"2021-12-15 10:22:58.611\tI Monero 'Oxygen Orion' (v0.17.3.0-release)\nError: Couldn't connect to daemon: 127.0.0.1:18081\n"
2021-12-15 10:22:58.856	    78b57bd17700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	daemon not running. checking again in 2 seconds.
2021-12-15 10:22:59.782	    78b53d587700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Checking connection status
2021-12-15 10:22:59.782	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Wallet connection status changed 3
2021-12-15 10:22:59.962	    78b53d587700	DEBUG	net	contrib/epee/include/net/net_helper.h:238	Some problems at connect, message: Connection refused
2021-12-15 10:22:59.969	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Wallet connection status changed 0
2021-12-15 10:23:00.857	    78b57bd17700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	sending external cmd:  ("sync_info")
2021-12-15 10:23:02.076	    78b57bd17700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	"2021-12-15 10:23:01.918\tI Monero 'Oxygen Orion' (v0.17.3.0-release)\nError: Couldn't connect to daemon: 127.0.0.1:18081\n"
2021-12-15 10:23:02.077	    78b57bd17700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	daemon not running. checking again in 2 seconds.
2021-12-15 10:23:04.077	    78b57bd17700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	sending external cmd:  ("sync_info")
2021-12-15 10:23:05.641	    78b57bd17700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	"2021-12-15 10:23:05.136\tI Monero 'Oxygen Orion' (v0.17.3.0-release)\nError: Couldn't connect to daemon: 127.0.0.1:18081\n"
2021-12-15 10:23:05.642	    78b57bd17700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	daemon not running. checking again in 2 seconds.
2021-12-15 10:23:05.835	    78b53cd86700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Checking connection status
2021-12-15 10:23:05.836	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Wallet connection status changed 3
2021-12-15 10:23:06.022	    78b53cd86700	DEBUG	net	contrib/epee/include/net/net_helper.h:238	Some problems at connect, message: Connection refused
2021-12-15 10:23:06.022	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Wallet connection status changed 0
2021-12-15 10:23:07.642	    78b57bd17700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	sending external cmd:  ("sync_info")
2021-12-15 10:23:09.420	    78b57bd17700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	"2021-12-15 10:23:08.684\tI Monero 'Oxygen Orion' (v0.17.3.0-release)\nError: Couldn't connect to daemon: 127.0.0.1:18081\n"
2021-12-15 10:23:09.420	    78b57bd17700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	daemon not running. checking again in 2 seconds.
2021-12-15 10:23:09.421	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	daemon start failed
2021-12-15 10:23:09.591	    78b57b516700	DEBUG	net	contrib/epee/include/net/net_helper.h:238	Some problems at connect, message: Connection refused
2021-12-15 10:23:09.591	    78b57b516700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	refreshed
2021-12-15 10:23:09.592	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	>>> wallet refreshed
2021-12-15 10:23:09.592	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	>>> wallet updated
2021-12-15 10:23:09.594	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	>>> wallet updated
2021-12-15 10:23:11.893	    78b53d587700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Checking connection status
2021-12-15 10:23:11.899	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Wallet connection status changed 3
2021-12-15 10:23:12.060	    78b53d587700	DEBUG	net	contrib/epee/include/net/net_helper.h:238	Some problems at connect, message: Connection refused
2021-12-15 10:23:12.060	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Wallet connection status changed 0
2021-12-15 10:23:19.820	    78b57b516700	DEBUG	net	contrib/epee/include/net/net_helper.h:238	Some problems at connect, message: Connection refused
2021-12-15 10:23:19.820	    78b57b516700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	refreshed
2021-12-15 10:23:19.821	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	>>> wallet refreshed
2021-12-15 10:23:19.821	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Checking connection status
2021-12-15 10:23:19.821	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	>>> wallet updated
2021-12-15 10:23:19.821	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Wallet connection status changed 3
2021-12-15 10:23:19.825	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	>>> wallet updated
2021-12-15 10:23:19.891	    78b53cd86700	DEBUG	net.http	contrib/epee/include/net/http_client.h:246	Reconnecting...
2021-12-15 10:23:19.984	    78b57bd17700	DEBUG	net	contrib/epee/include/net/net_helper.h:238	Some problems at connect, message: Connection refused
2021-12-15 10:23:19.989	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Wallet connection status changed 0
2021-12-15 10:23:20.043	    78b53cd86700	DEBUG	net	contrib/epee/include/net/net_helper.h:238	Some problems at connect, message: Connection refused
2021-12-15 10:23:20.043	    78b53cd86700	DEBUG	net.http	contrib/epee/include/net/http_client.h:249	Failed to connect to localhost:18081
2021-12-15 10:23:20.044	    78b53cd86700	INFO	net.http	contrib/epee/include/storages/http_abstract_invoke.h:53	Failed to invoke http request to  /mining_status
2021-12-15 10:23:25.875	    78b53cd86700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Checking connection status
2021-12-15 10:23:25.875	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Wallet connection status changed 3
2021-12-15 10:23:26.026	    78b53cd86700	DEBUG	net	contrib/epee/include/net/net_helper.h:238	Some problems at connect, message: Connection refused
2021-12-15 10:23:26.032	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Wallet connection status changed 0
2021-12-15 10:23:30.045	    78b57b516700	DEBUG	net	contrib/epee/include/net/net_helper.h:238	Some problems at connect, message: Connection refused
2021-12-15 10:23:30.046	    78b57b516700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	refreshed
2021-12-15 10:23:30.047	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	>>> wallet refreshed
2021-12-15 10:23:30.047	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	>>> wallet updated
2021-12-15 10:23:30.050	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	>>> wallet updated
2021-12-15 10:23:34.126	    78b57bd17700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Checking connection status
2021-12-15 10:23:34.126	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Wallet connection status changed 3
2021-12-15 10:23:34.293	    78b57bd17700	DEBUG	net	contrib/epee/include/net/net_helper.h:238	Some problems at connect, message: Connection refused
2021-12-15 10:23:34.303	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Wallet connection status changed 0
2021-12-15 10:23:40.291	    78b57b516700	DEBUG	net	contrib/epee/include/net/net_helper.h:238	Some problems at connect, message: Connection refused
2021-12-15 10:23:40.292	    78b57b516700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	refreshed
2021-12-15 10:23:40.302	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	>>> wallet refreshed
2021-12-15 10:23:40.302	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Checking connection status
2021-12-15 10:23:40.303	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	>>> wallet updated
2021-12-15 10:23:40.303	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Wallet connection status changed 3
2021-12-15 10:23:40.303	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	>>> wallet updated
2021-12-15 10:23:40.467	    78b53cd86700	DEBUG	net	contrib/epee/include/net/net_helper.h:238	Some problems at connect, message: Connection refused
2021-12-15 10:23:40.471	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Wallet connection status changed 0
2021-12-15 10:23:42.405	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	showing status message
2021-12-15 10:23:45.423	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	resetting android close
2021-12-15 10:23:48.019	    78b53d587700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Checking connection status
2021-12-15 10:23:48.019	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Wallet connection status changed 3
2021-12-15 10:23:48.183	    78b53d587700	DEBUG	net	contrib/epee/include/net/net_helper.h:238	Some problems at connect, message: Connection refused
2021-12-15 10:23:48.187	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Wallet connection status changed 0
2021-12-15 10:23:50.504	    78b57b516700	DEBUG	net	contrib/epee/include/net/net_helper.h:238	Some problems at connect, message: Connection refused
2021-12-15 10:23:50.504	    78b57b516700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	refreshed
2021-12-15 10:23:50.510	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	>>> wallet refreshed
2021-12-15 10:23:50.511	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	>>> wallet updated
2021-12-15 10:23:50.519	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	>>> wallet updated
2021-12-15 10:23:56.073	    78b53cd86700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Checking connection status
2021-12-15 10:23:56.073	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Wallet connection status changed 3
2021-12-15 10:23:56.278	    78b53cd86700	DEBUG	net	contrib/epee/include/net/net_helper.h:238	Some problems at connect, message: Connection refused
2021-12-15 10:23:56.279	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Wallet connection status changed 0
2021-12-15 10:24:00.916	    78b57b516700	DEBUG	net	contrib/epee/include/net/net_helper.h:238	Some problems at connect, message: Connection refused
2021-12-15 10:24:00.916	    78b57b516700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	refreshed
2021-12-15 10:24:00.916	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	>>> wallet refreshed
2021-12-15 10:24:00.916	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	>>> wallet updated
2021-12-15 10:24:00.916	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	>>> wallet updated
2021-12-15 10:24:04.063	    78b53d587700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Checking connection status
2021-12-15 10:24:04.065	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Wallet connection status changed 3
2021-12-15 10:24:04.262	    78b53d587700	DEBUG	net	contrib/epee/include/net/net_helper.h:238	Some problems at connect, message: Connection refused
2021-12-15 10:24:04.262	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Wallet connection status changed 0
2021-12-15 10:24:11.156	    78b57b516700	DEBUG	net	contrib/epee/include/net/net_helper.h:238	Some problems at connect, message: Connection refused
2021-12-15 10:24:11.156	    78b57b516700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	refreshed
2021-12-15 10:24:11.162	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	>>> wallet refreshed
2021-12-15 10:24:11.162	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Checking connection status
2021-12-15 10:24:11.162	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	>>> wallet updated
2021-12-15 10:24:11.162	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Wallet connection status changed 3
2021-12-15 10:24:11.163	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	>>> wallet updated
2021-12-15 10:24:11.318	    78b53cd86700	DEBUG	net	contrib/epee/include/net/net_helper.h:238	Some problems at connect, message: Connection refused
2021-12-15 10:24:11.328	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Wallet connection status changed 0
2021-12-15 10:24:18.019	    78b57bd17700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Checking connection status
2021-12-15 10:24:18.024	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Wallet connection status changed 3
2021-12-15 10:24:18.185	    78b57bd17700	DEBUG	net	contrib/epee/include/net/net_helper.h:238	Some problems at connect, message: Connection refused
2021-12-15 10:24:18.185	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Wallet connection status changed 0
2021-12-15 10:24:18.262	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	blocking close event
2021-12-15 10:24:18.262	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Displaying processing splash
2021-12-15 10:24:18.267	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Hiding processing splash
2021-12-15 10:24:18.268	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	close accepted
2021-12-15 10:24:18.268	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	DaemonManager: exit()
2021-12-15 10:24:18.271	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Displaying processing splash
2021-12-15 10:24:18.273	    78b53cd86700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	~Wallet: Closing wallet
2021-12-15 10:24:18.305	    78b53cd86700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Wallet cache stored successfully
2021-12-15 10:24:18.305	    78b53cd86700	INFO	WalletAPI	src/wallet/api/wallet.cpp:453	~WalletImpl
2021-12-15 10:24:18.305	    78b53cd86700	DEBUG	WalletAPI	src/wallet/api/wallet.cpp:2294	pauseRefresh: refresh paused...
2021-12-15 10:24:18.305	    78b53cd86700	INFO	WalletAPI	src/wallet/api/wallet.cpp:770	closing wallet...
2021-12-15 10:24:18.305	    78b53cd86700	INFO	WalletAPI	src/wallet/api/wallet.cpp:781	Calling wallet::stop...
2021-12-15 10:24:18.305	    78b53cd86700	INFO	WalletAPI	src/wallet/api/wallet.cpp:783	wallet::stop done
2021-12-15 10:24:18.305	    78b53cd86700	INFO	WalletAPI	src/wallet/api/wallet.cpp:466	~WalletImpl finished
2021-12-15 10:24:18.305	    78b53cd86700	DEBUG	net	contrib/epee/include/net/net_helper.h:647	Problems at ssl shutdown: uninitialized
2021-12-15 10:24:18.305	    78b53cd86700	DEBUG	net	contrib/epee/include/net/net_helper.h:571	Problems at cancel: Bad file descriptor
2021-12-15 10:24:18.305	    78b53cd86700	DEBUG	net	contrib/epee/include/net/net_helper.h:574	Problems at shutdown: Bad file descriptor
2021-12-15 10:24:18.307	    78b53cd86700	DEBUG	net	contrib/epee/include/net/net_helper.h:647	Problems at ssl shutdown: uninitialized
2021-12-15 10:24:18.307	    78b53cd86700	DEBUG	net	contrib/epee/include/net/net_helper.h:571	Problems at cancel: Bad file descriptor
2021-12-15 10:24:18.307	    78b53cd86700	DEBUG	net	contrib/epee/include/net/net_helper.h:574	Problems at shutdown: Bad file descriptor
2021-12-15 10:24:18.315	    78b53cd86700	DEBUG	frontend	src/wallet/api/wallet.cpp:404	m_walletImpl deleted
2021-12-15 10:24:18.316	    78b580efec40	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Hiding processing splash
2021-12-15 10:24:18.426	    78b580efec40	DEBUG	net	contrib/epee/include/net/net_helper.h:647	Problems at ssl shutdown: uninitialized
2021-12-15 10:24:18.426	    78b580efec40	DEBUG	net	contrib/epee/include/net/net_helper.h:571	Problems at cancel: Bad file descriptor
2021-12-15 10:24:18.427	    78b580efec40	DEBUG	net	contrib/epee/include/net/net_helper.h:574	Problems at shutdown: Bad file descriptor
2021-12-15 10:24:18.747	    78b580efec40	DEBUG	device.ledger	src/device/device_ledger.cpp:310	Device 0 Destroyed
```

## selsta | 2021-12-15T10:30:54+00:00
> However, I just ran into the same error as before.

Were you able to sync up and after some time the same error started appearing, or did the error not go away in the first place?

Also what kind of drive is that where you are storing the blockchain? External hard drive? Network drive?

Can you also post logs like this? `sudo monerod --data-dir /media/user/adc2a35f-1c70-47aa-a3fb-bd1281fb9356/XMR --log-level 2`

## ghost | 2021-12-15T11:02:02+00:00
In answer to your question.
I attempted to start my local node but it timed out after 120 seconds, just like before.
I was not able to start it up.

I am using a Seagate 3TB HDD in a Sabrent USB HDD Enclosure, effectively an external hard drive.

I just started monerod on CLI and, actually, it's working fine for now.

I'll keep you posted over whatever turns up next.

## ghost | 2021-12-15T11:09:57+00:00
I can give you an excerpt of the output on my CLI from the running sync process.
```
<ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff>
2021-12-15 11:08:46.400	I HEIGHT 44127, difficulty:	36872002
2021-12-15 11:08:46.401	I block reward: 16.873457030344(16.873457030344 + 0.000000000000), coinbase_weight: 388, cumulative weight: 388, 0(0/0)ms
2021-12-15 11:08:46.401	D Invalidating block template cache
2021-12-15 11:08:46.401	D [5.133.65.82:18080 OUT] skipping 9737/9737 blocks
2021-12-15 11:08:46.401	E [5.133.65.82:18080 OUT] Nothing we can request from this peer, and we did not request anything previously
2021-12-15 11:08:46.401	E [5.133.65.82:18080 OUT] Failed to request missing objects, dropping connection
2021-12-15 11:08:46.401	D [5.133.65.82:18080 OUT] dropping connection id 32d3617c-1682-4b0d-9065-f148706edd7c (pruning seed 0), score 0, flush_all_spans 0
2021-12-15 11:08:46.402	E Setting timer on a shut down object
2021-12-15 11:08:46.402	I [5.133.65.82:18080 OUT] [0] state: closed in state synchronizing
2021-12-15 11:08:46.402	I [5.133.65.82:18080 32d3617c-1682-4b0d-9065-f148706edd7c OUT] CLOSE CONNECTION
2021-12-15 11:08:46.402	D Destructing connection #362 to 5.133.65.82
2021-12-15 11:08:46.405	D Miner tx hash: <35d9d0028e4a6d29efc35175501ebe93f50a7030301b9589ea8f0b98179517ff>
2021-12-15 11:08:46.431	I +++++ BLOCK SUCCESSFULLY ADDED
2021-12-15 11:08:46.431	I id:	<533f08c7c6dab31d3b8672bb6a6498ed0c7f16fa7de6d10a14e92e2574900e1c>
2021-12-15 11:08:46.431	I PoW:	<ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff>
```

How does that look?

Checking on the GUI, I can tell that it is syncing and building up the blockchain in my external HDD.

## selsta | 2021-12-17T15:31:14+00:00
> Checking on the GUI, I can tell that it is syncing and building up the blockchain in my external HDD.

So which issue is remaining now? The "Timed out, local node is not responding after 120 seconds." issue?

## NainKirito | 2022-01-28T17:23:52+00:00
Build a text document in Monero GUI Wallet says “ monerod.exe --db-salvage”，then trans it into a BAT program by changing its file extension into “.bat".This might work.


## NainKirito | 2022-01-28T17:27:15+00:00
Oh sorry, and you have to run it by yourself.

## selsta | 2022-04-27T04:50:07+00:00
Closing as it's not really clear if an issue remains.

## CopyPasteFail | 2022-06-19T16:59:20+00:00
For the sake of others having this issue and stumbled upon this, the way to fix it on Linux:
Close monero
Navigate to '~/.bitmonero'
delete the folder 'lmdb'
Restart the daemon

## markonine | 2022-06-30T18:56:07+00:00
And where did you find the /.bitmonero file? The same problem on linux


## selsta | 2022-06-30T19:31:40+00:00
@markonine `cd ~/.bitmonero`

# Action History
- Created by: ghost | 2021-12-15T09:15:01+00:00
- Closed at: 2022-04-27T04:50:07+00:00
