---
title: Unable to run public node behind firewall, unable to bind restricted rpc to
  0.0.0.0
source_url: https://github.com/monero-project/monero/issues/8255
author: Morpheus0x
assignees: []
labels: []
created_at: '2022-04-12T15:56:57+00:00'
updated_at: '2022-04-12T16:40:24+00:00'
type: issue
status: closed
closed_at: '2022-04-12T16:13:47+00:00'
---

# Original Description
I have a hypervisor with a firewall in front that manages the public IPs. I setup a new VM which I intend to run a fully public monero node. With any other software(other crypto nodes or any other like for example a web server) I am able to setup port forwarding but for some reason, `monerod` doesn't like to that setup, because I am unable to get this working.

Below is my full monerod.conf file, but the problematic setting is `rpc-restricted-bind-ip`. If I set it to the private IP of eth0, it complains that the IP isn't publicly routable, which is the case and I can understand that completely. If I set it to 0.0.0.0 I get the the error `Failed to bind IPv4 (set to required)`, here the full log:
```
2022-04-12 15:46:14.322	    7f16f22a6780	INFO	global	src/daemon/rpc.h:69	core RPC server initialized OK on port: 18081
2022-04-12 15:46:14.322	    7f16f22a6780	INFO	global	src/daemon/rpc.h:63	Initializing restricted RPC server...
2022-04-12 15:46:14.322	    7f16f22a6780	INFO	global	contrib/epee/include/net/http_server_impl_base.h:79	Binding on 0.0.0.0 (IPv4):18081
2022-04-12 15:46:16.326	    7f16f22a6780	FATAL	net	contrib/epee/include/net/abstract_tcp_server2.inl:1084	Error starting server: Failed to bind IPv4 (set to required)
2022-04-12 15:46:16.328	    7f16f22a6780	INFO	global	src/daemon/rpc.h:96	Deinitializing core RPC server...
2022-04-12 15:46:16.328	    7f16f22a6780	INFO	global	src/daemon/p2p.h:91	Deinitializing p2p...
2022-04-12 15:46:16.334	    7f16f22a6780	INFO	global	src/daemon/core.h:102	Deinitializing core...
2022-04-12 15:46:16.341	    7f16f22a6780	INFO	global	src/daemon/protocol.h:75	Stopping cryptonote protocol...
2022-04-12 15:46:16.341	    7f16f22a6780	INFO	global	src/daemon/protocol.h:79	Cryptonote protocol stopped successfully
2022-04-12 15:46:16.341	    7f16f22a6780	ERROR	daemon	src/daemon/main.cpp:364	Exception in main! Failed to initialize restricted RPC server.
2022-04-12 15:46:22.403	    7f4461c3f780	INFO	logging	contrib/epee/src/mlog.cpp:273	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
2022-04-12 15:46:22.403	    7f4461c3f780	INFO	logging	contrib/epee/src/mlog.cpp:273	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
2022-04-12 15:46:22.405	    7f4461c3f780	INFO	global	src/daemon/main.cpp:296	Monero 'Oxygen Orion' (v0.17.3.0-release)
2022-04-12 15:46:22.406	    7f4461c3f780	INFO	global	src/daemon/protocol.h:53	Initializing cryptonote protocol...
2022-04-12 15:46:22.407	    7f4461c3f780	INFO	global	src/daemon/protocol.h:58	Cryptonote protocol initialized OK
2022-04-12 15:46:22.409	    7f4461c3f780	INFO	global	src/daemon/core.h:64	Initializing core...
2022-04-12 15:46:22.410	    7f4461c3f780	INFO	global	src/cryptonote_core/cryptonote_core.cpp:517	Loading blockchain from folder /data/monero/lmdb ...
2022-04-12 15:46:22.516	    7f4461c3f780	INFO	global	src/cryptonote_core/cryptonote_core.cpp:692	Loading checkpoints
2022-04-12 15:46:22.539	    7f4461c3f780	INFO	global	src/daemon/core.h:81	Core initialized OK
2022-04-12 15:46:22.539	    7f4461c3f780	INFO	global	src/daemon/p2p.h:64	Initializing p2p server...
2022-04-12 15:46:22.543	    7f4461c3f780	INFO	global	src/daemon/p2p.h:69	p2p server initialized OK
2022-04-12 15:46:22.543	    7f4461c3f780	INFO	global	src/daemon/rpc.h:63	Initializing core RPC server...
2022-04-12 15:46:22.544	    7f4461c3f780	INFO	global	contrib/epee/include/net/http_server_impl_base.h:79	Binding on 127.0.0.1 (IPv4):18081
2022-04-12 15:46:23.685	    7f4461c3f780	INFO	global	src/daemon/rpc.h:69	core RPC server initialized OK on port: 18081
2022-04-12 15:46:23.685	    7f4461c3f780	INFO	global	src/daemon/rpc.h:63	Initializing restricted RPC server...
2022-04-12 15:46:23.685	    7f4461c3f780	INFO	global	contrib/epee/include/net/http_server_impl_base.h:79	Binding on 0.0.0.0 (IPv4):18081
2022-04-12 15:46:25.411	    7f4461c3f780	FATAL	net	contrib/epee/include/net/abstract_tcp_server2.inl:1084	Error starting server: Failed to bind IPv4 (set to required)
2022-04-12 15:46:25.411	    7f4461c3f780	INFO	global	src/daemon/rpc.h:96	Deinitializing core RPC server...
2022-04-12 15:46:25.411	    7f4461c3f780	INFO	global	src/daemon/p2p.h:91	Deinitializing p2p...
2022-04-12 15:46:25.417	    7f4461c3f780	INFO	global	src/daemon/core.h:102	Deinitializing core...
2022-04-12 15:46:25.423	    7f4461c3f780	INFO	global	src/daemon/protocol.h:75	Stopping cryptonote protocol...
2022-04-12 15:46:25.423	    7f4461c3f780	INFO	global	src/daemon/protocol.h:79	Cryptonote protocol stopped successfully
2022-04-12 15:46:25.424	    7f4461c3f780	ERROR	daemon	src/daemon/main.cpp:364	Exception in main! Failed to initialize restricted RPC server.
```
And finally if I try to set `rpc-restricted-bind-ip` to the public IP which I setup the port forwarding for 18080 and 18081(and setting the outbound NAT to the same IP) I get the same error:
```
2022-04-12 15:49:39.055	    7f5696306780	INFO	logging	contrib/epee/src/mlog.cpp:273	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
2022-04-12 15:49:39.055	    7f5696306780	INFO	logging	contrib/epee/src/mlog.cpp:273	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
2022-04-12 15:49:39.058	    7f5696306780	INFO	global	src/daemon/main.cpp:296	Monero 'Oxygen Orion' (v0.17.3.0-release)
2022-04-12 15:49:39.059	    7f5696306780	INFO	global	src/daemon/protocol.h:53	Initializing cryptonote protocol...
2022-04-12 15:49:39.060	    7f5696306780	INFO	global	src/daemon/protocol.h:58	Cryptonote protocol initialized OK
2022-04-12 15:49:39.061	    7f5696306780	INFO	global	src/daemon/core.h:64	Initializing core...
2022-04-12 15:49:39.062	    7f5696306780	INFO	global	src/cryptonote_core/cryptonote_core.cpp:517	Loading blockchain from folder /data/monero/lmdb ...
2022-04-12 15:49:39.171	    7f5696306780	INFO	global	src/cryptonote_core/cryptonote_core.cpp:692	Loading checkpoints
2022-04-12 15:49:39.250	    7f5696306780	INFO	global	src/daemon/core.h:81	Core initialized OK
2022-04-12 15:49:39.251	    7f5696306780	INFO	global	src/daemon/p2p.h:64	Initializing p2p server...
2022-04-12 15:49:39.255	    7f5696306780	INFO	global	src/daemon/p2p.h:69	p2p server initialized OK
2022-04-12 15:49:39.256	    7f5696306780	INFO	global	src/daemon/rpc.h:63	Initializing core RPC server...
2022-04-12 15:49:39.257	    7f5696306780	INFO	global	contrib/epee/include/net/http_server_impl_base.h:79	Binding on 127.0.0.1 (IPv4):18081
2022-04-12 15:49:39.788	    7f5696306780	INFO	global	src/daemon/rpc.h:69	core RPC server initialized OK on port: 18081
2022-04-12 15:49:39.789	    7f5696306780	INFO	global	src/daemon/rpc.h:63	Initializing restricted RPC server...
2022-04-12 15:49:39.789	    7f5696306780	INFO	global	contrib/epee/include/net/http_server_impl_base.h:79	Binding on 93.x.x.5 (IPv4):18081
2022-04-12 15:49:43.521	    7f5696306780	FATAL	net	contrib/epee/include/net/abstract_tcp_server2.inl:1084	Error starting server: Failed to bind IPv4 (set to required)
2022-04-12 15:49:43.523	    7f5696306780	INFO	global	src/daemon/rpc.h:96	Deinitializing core RPC server...
2022-04-12 15:49:43.523	    7f5696306780	INFO	global	src/daemon/p2p.h:91	Deinitializing p2p...
2022-04-12 15:49:43.530	    7f5696306780	INFO	global	src/daemon/core.h:102	Deinitializing core...
2022-04-12 15:49:43.536	    7f5696306780	INFO	global	src/daemon/protocol.h:75	Stopping cryptonote protocol...
2022-04-12 15:49:43.537	    7f5696306780	INFO	global	src/daemon/protocol.h:79	Cryptonote protocol stopped successfully
2022-04-12 15:49:43.538	    7f5696306780	ERROR	daemon	src/daemon/main.cpp:364	Exception in main! Failed to initialize restricted RPC server.
```
Real IP redacted.
Here Is my full config:
```
data-dir=/data/monero
log-file=/var/log/monero/monero.log
log-level=0
max-log-file-size=0
public-node=true
rpc-restricted-bind-ip=0.0.0.0
rpc-restricted-bind-port=18081
prune-blockchain=false
db-sync-mode=safe
enforce-dns-checkpointing=true
enable-dns-blocklist=true
no-igd=true
no-zmq=true
out-peers=64
in-peers=64
limit-rate-up=1048576
limit-rate-down=1048576 
```
Monero Version: v0.17.3.0

Please tell my if my config is wrong or if this is a problem with monerod!

# Discussion History
## Morpheus0x | 2022-04-12T16:03:44+00:00
I think the problem is, that there is no separate option to define a specific public IP. If the option `rpc-restricted-bind-ip` is set to a private IP, monerod should take the public IP set in that new option and use that to advertise it's public rpc connection.

## hyc | 2022-04-12T16:13:18+00:00
You need to set the rpc-bind-ip to something else because that is already being opened by default, which prevents you from binding the rpc-restricted-bind-ip.

## hyc | 2022-04-12T16:13:47+00:00
There's no bug here, and this issue tracker is only for bug reports.

## Morpheus0x | 2022-04-12T16:40:24+00:00
Ah yes, thank you, I got it working!

# Action History
- Created by: Morpheus0x | 2022-04-12T15:56:57+00:00
- Closed at: 2022-04-12T16:13:47+00:00
