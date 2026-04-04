---
title: failed to parse blob 1.5 tb storage but input output error at 85%
source_url: https://github.com/monero-project/monero/issues/9736
author: Lexonight1
assignees: []
labels:
- daemon
- database
- more info needed
created_at: '2025-01-26T16:13:46+00:00'
updated_at: '2025-01-29T20:23:01+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Any hints? well will probably have to resync the whole db
Fedora Server 41
no Sealerts Selinux is good just don't understand 
systemd file:
```
#service file
[Unit]
Description=Monero Daemon
After=network-online.target

[Service]
ExecStart=/usr/local/bin/monerod --detach --config-file /etc/monero/monerod.conf --pidfile /run/monero/monerod.pid
ExecStartPost=/bin/sleep 0.1
PIDFile=/run/monero/monerod.pid
Type=forking

Restart=on-failure
RestartSec=30

User=monero
Group=monero
RuntimeDirectory=monero

StandardOutput=journal
StandardError=journal

[Install]
WantedBy=multi-user.target
```

config file: 
```
# /etc/monero/monerod.conf
#
# Configuration file for monerod. For all available options see the MoneroDocs:
# https://docs.getmonero.org/interacting/monerod-reference/

# Data directory (blockchain db and indices)
data-dir=/var/lib/monero/bitmonero   # Blockchain storage location

# Optional pruning
#prune-blockchain=1           # Pruning saves 2/3 of disk space w/o degrading functionality but contributes less to the network
#sync-pruned-blocks=1         # Allow downloading pruned blocks instead of prunning them yourself

# Centralized services
check-updates=disabled         # Do not check DNS TXT records for a new version
enable-dns-blocklist=1           # Block known malicious nodes

# Log file
log-file=/var/log/monero/monero.log
log-level=0                    # Minimal logs, WILL NOT log peers or wallets connecting
max-log-file-size=2147483648   # Set to 2GB to mitigate log trimming by monerod; configure logrotate instead

# P2P full node
#p2p-bind-ip=0.0.0.0            # Bind to all interfaces (the default)
#p2p-bind-port=18080            # Bind to default port
#no-igd=1                       # Disable UPnP port mapping

# RPC open node
#public-node=1                  # Advertise to other users they can use this node for connecting their wallets
rpc-restricted-bind-ip=0.0.0.0 # Bind to all interfaces (the Open Node)
rpc-restricted-bind-port=18089 # Bind to a new RESTICTED port (the Open Node)

# RPC TLS
rpc-ssl=autodetect             # Use TLS if client wallet supports it (Default); A new certificate will be regenerated every restart

# ZMQ
#zmq-rpc-bind-ip=127.0.0.1      # Default 127.0.0.1
#zmq-rpc-bind-port=18082        # Default 18082
zmq-pub=tcp://127.0.0.1:18083  # ZMQ pub
#no-zmq=1                       # Disable ZMQ RPC server

# Mempool size
max-txpool-weight=2684354560   # Maximum unconfirmed transactions pool size in bytes (here ~2.5GB, default ~618MB)

# Database sync mode
#db-sync-mode=safe:sync        # Slow but reliable db writes

# Network limits
out-peers=70              # This will enable much faster sync and tx awareness; the default 8 is suboptimal nowadays
in-peers=30               # The default is unlimited; we prefer to put a cap on this

limit-rate-up=1048576     # 1048576 kB/s == 1GB/s; a raise from default 2048 kB/s; contribute more to p2p network
limit-rate-down=1048576   # 1048576 kB/s == 1GB/s; a raise from default 8192 kB/s; allow for faster initial sync

# Tor/I2P: broadcast transactions originating from connected wallets over Tor/I2P (does not concern relayed transactions)
#tx-proxy=i2p,127.0.0.1:4447,16.disable_noise  # I2P
#tx-proxy=tor,127.0.0.1:9050,16,disable_noise  # Tor

# Tor/I2P: tell monerod your onion address so it can be advertised on P2P network
#anonymous-inbound=PASTE_YOUR_I2P_HOSTNAME,127.0.0.1:18085,64         # I2P
#anonymous-inbound=PASTE_YOUR_ONION_HOSTNAME:18084,127.0.0.1:18084,64 # Tor

# Tor: be forgiving to connecting wallets
disable-rpc-ban=1
#possable speed up on sync
max-concurrency=3
block-sync-size=100
```
Error message:
```
2025-01-26 05:26:28.298	[P2P4]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1697	Synced 2840904/3333515 (85%, 492611 left)
2025-01-26 05:26:34.094	[P2P4]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1697	Synced 2841004/3333515 (85%, 492511 left)
2025-01-26 05:26:42.670	[P2P4]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1697	Synced 2841104/3333515 (85%, 492411 left)
2025-01-26 05:26:47.151	[P2P4]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1697	Synced 2841204/3333515 (85%, 492311 left)
2025-01-26 05:27:06.147	    7f17171ff6c0	WARNING	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:75	Failed to sync database: Input/output error
2025-01-26 05:27:06.150	    7f17171ff6c0	ERROR	blockchain	src/cryptonote_core/blockchain.cpp:497	Error syncing blockchain db: Failed to sync database: Input/output error-- shutting down now to prevent issues!
2025-01-26 05:32:49.132	    7fa5655eac00	INFO	logging	contrib/epee/src/mlog.cpp:274	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
2025-01-26 05:32:49.133	    7fa5655eac00	INFO	logging	contrib/epee/src/mlog.cpp:274	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
2025-01-26 05:32:49.133	    7fa5655eac00	INFO	global	src/daemon/main.cpp:309	Monero 'Fluorine Fermi' (v0.18.3.4-release)
2025-01-26 05:32:49.133	    7fa5655eac00	INFO	msgwriter	src/common/scoped_message_writer.h:102	Forking to background...
2025-01-26 05:32:49.134	    7fa5655eac00	WARNING	daemon	src/daemon/executor.cpp:61	Monero 'Fluorine Fermi' (v0.18.3.4-release) Daemonised
2025-01-26 05:32:49.135	    7fa5655eac00	INFO	global	src/daemon/protocol.h:53	Initializing cryptonote protocol...
2025-01-26 05:32:49.135	    7fa5655eac00	INFO	global	src/daemon/protocol.h:58	Cryptonote protocol initialized OK
2025-01-26 05:32:49.136	    7fa5655eac00	INFO	global	src/daemon/core.h:64	Initializing core...
2025-01-26 05:32:49.136	    7fa5655eac00	INFO	global	src/cryptonote_core/cryptonote_core.cpp:523	Loading blockchain from folder /var/lib/monero/bitmonero/lmdb ...
2025-01-26 05:32:51.052	    7fa5655eac00	ERROR	cn	src/cryptonote_basic/cryptonote_format_utils.cpp:1544	Failed to parse block from blob
2025-01-26 05:32:51.067	    7fa5655eac00	INFO	global	src/daemon/protocol.h:75	Stopping cryptonote protocol...
2025-01-26 05:32:51.067	    7fa5655eac00	INFO	global	src/daemon/protocol.h:79	Cryptonote protocol stopped successfully
2025-01-26 05:32:51.067	    7fa5655eac00	ERROR	daemon	src/daemon/main.cpp:377	Exception in main! Failed to parse block from blob retrieved from the db
2025-01-26 05:33:21.322	    7f890824ec00	INFO	logging	contrib/epee/src/mlog.cpp:274	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
2025-01-26 05:33:21.323	    7f890824ec00	INFO	logging	contrib/epee/src/mlog.cpp:274	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
2025-01-26 05:33:21.323	    7f890824ec00	INFO	global	src/daemon/main.cpp:309	Monero 'Fluorine Fermi' (v0.18.3.4-release)
2025-01-26 05:33:21.323	    7f890824ec00	INFO	msgwriter	src/common/scoped_message_writer.h:102	Forking to background...
2025-01-26 05:33:21.323	    7f890824ec00	WARNING	daemon	src/daemon/executor.cpp:61	Monero 'Fluorine Fermi' (v0.18.3.4-release) Daemonised
2025-01-26 05:33:21.324	    7f890824ec00	INFO	global	src/daemon/protocol.h:53	Initializing cryptonote protocol...
2025-01-26 05:33:21.324	    7f890824ec00	INFO	global	src/daemon/protocol.h:58	Cryptonote protocol initialized OK
2025-01-26 05:33:21.325	    7f890824ec00	INFO	global	src/daemon/core.h:64	Initializing core...
2025-01-26 05:33:21.325	    7f890824ec00	INFO	global	src/cryptonote_core/cryptonote_core.cpp:523	Loading blockchain from folder /var/lib/monero/bitmonero/lmdb ...
2025-01-26 05:33:21.347	    7f890824ec00	ERROR	cn	src/cryptonote_basic/cryptonote_format_utils.cpp:1544	Failed to parse block from blob
2025-01-26 05:33:21.372	    7f890824ec00	INFO	global	src/daemon/protocol.h:75	Stopping cryptonote protocol...
2025-01-26 05:33:21.372	    7f890824ec00	INFO	global	src/daemon/protocol.h:79	Cryptonote protocol stopped successfully
2025-01-26 05:33:21.372	    7f890824ec00	ERROR	daemon	src/daemon/main.cpp:377	Exception in main! Failed to parse block from blob retrieved from the db
2025-01-26 05:33:51.574	    7f88af69ec00	INFO	logging	contrib/epee/src/mlog.cpp:274	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
2025-01-26 05:33:51.574	    7f88af69ec00	INFO	logging	contrib/epee/src/mlog.cpp:274	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO

```

# Discussion History
## selsta | 2025-01-26T18:23:51+00:00
I don't remember seeing this error before. Re-syncing would be a good first step to rule out database corruption issues.

## Lexonight1 | 2025-01-26T18:28:28+00:00
tried --db-salvage still got the  
`ERROR	daemon	src/daemon/main.cpp:377	Exception in main! Failed to parse block from blob retrieved from the db`
yeah i deleted lmdb contents and put safe:sync in the config so just going to try again, see what happens. had a full-sync node before no problem

## selsta | 2025-01-28T16:52:04+00:00
--db-salvage only works in limited situations.

Do you remember a power outage or something else that could have caused database corruption?

# Action History
- Created by: Lexonight1 | 2025-01-26T16:13:46+00:00
