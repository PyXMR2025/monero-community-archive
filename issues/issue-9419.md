---
title: monerod.service - Failed to initiatize p2p server
source_url: https://github.com/monero-project/monero/issues/9419
author: jaredmo
assignees: []
labels:
- more info needed
created_at: '2024-08-03T11:45:57+00:00'
updated_at: '2024-12-14T00:06:19+00:00'
type: issue
status: closed
closed_at: '2024-12-14T00:06:19+00:00'
---

# Original Description
### System
- OS: `Arch Linux`
- Kernel: `6.10.2-arch1-1`
- Monero: `v0.18.3.3-release`

### Issue
`monerod.service` crashes on reboot with the options below in `/etc/monerod.conf`. If the service is restarted the issue is resolved.

```
zmq-pub=tcp://127.0.0.1:18083
out-peers=32
in-peers=64
add-priority-node=p2pmd.xmrvsbeast.com:18080
add-priority-node=nodes.hashvault.pro:18080
disable-dns-checkpoints=1
enable-dns-blocklist=1
```

### Logs
```
2024-08-03 11:17:49.737	    73bc1908b0c0	INFO	logging	contrib/epee/src/mlog.cpp:273	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
2024-08-03 11:17:49.737	    73bc1908b0c0	INFO	logging	contrib/epee/src/mlog.cpp:273	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
2024-08-03 11:17:49.738	    73bc1908b0c0	INFO	global	src/daemon/main.cpp:309	Monero 'Fluorine Fermi' (v0.18.3.3-release)
2024-08-03 11:17:49.738	    73bc1908b0c0	INFO	global	src/daemon/protocol.h:53	Initializing cryptonote protocol...
2024-08-03 11:17:49.738	    73bc1908b0c0	INFO	global	src/daemon/protocol.h:58	Cryptonote protocol initialized OK
2024-08-03 11:17:49.739	    73bc1908b0c0	INFO	global	src/daemon/core.h:64	Initializing core...
2024-08-03 11:17:49.741	    73bc1908b0c0	INFO	global	src/cryptonote_core/cryptonote_core.cpp:523	Loading blockchain from folder /var/lib/monero/lmdb ...
2024-08-03 11:17:50.970	    738453e006c0	INFO	stacktrace	src/common/stack_trace.cpp:133	Exception: std::bad_alloc
2024-08-03 11:17:50.970	    738453e006c0	INFO	stacktrace	src/common/stack_trace.cpp:134	Unwound call stack:
2024-08-03 11:17:50.972	    738453e006c0	INFO	stacktrace	src/common/stack_trace.cpp:172	    [1] /usr/bin/monerod(+0xc0dd5) [0x5eadc76a1dd5] 
2024-08-03 11:17:50.972	    738453e006c0	INFO	stacktrace	src/common/stack_trace.cpp:172	    [2] /usr/bin/monerod(+0xc0e55) [0x5eadc76a1e55] 
2024-08-03 11:17:50.972	    738453e006c0	INFO	stacktrace	src/common/stack_trace.cpp:172	    [3] /usr/bin/monerod(+0x3b4394) [0x5eadc7995394] 
2024-08-03 11:17:50.972	    738453e006c0	INFO	stacktrace	src/common/stack_trace.cpp:172	    [4] /usr/bin/monerod(+0x3b68bd) [0x5eadc79978bd] 
2024-08-03 11:17:50.972	    738453e006c0	INFO	stacktrace	src/common/stack_trace.cpp:172	    [5] /usr/lib/libc.so.6(+0x9439d) [0x73bc18ca339d] 
2024-08-03 11:17:50.972	    738453e006c0	INFO	stacktrace	src/common/stack_trace.cpp:172	    [6] /usr/lib/libc.so.6(+0x11949c) [0x73bc18d2849c] 
2024-08-03 11:17:50.972	    738453e006c0	INFO	stacktrace	src/common/stack_trace.cpp:172	
2024-08-03 11:17:51.301	    73bc1908b0c0	INFO	global	src/cryptonote_core/cryptonote_core.cpp:698	Loading checkpoints
2024-08-03 11:17:51.301	    73bc1908b0c0	INFO	global	src/daemon/core.h:81	Core initialized OK
2024-08-03 11:17:51.301	    73bc1908b0c0	INFO	global	src/daemon/p2p.h:64	Initializing p2p server...
2024-08-03 11:17:51.305	    73bc1908b0c0	INFO	stacktrace	src/common/stack_trace.cpp:133	Exception: std::runtime_error
2024-08-03 11:17:51.305	    73bc1908b0c0	INFO	stacktrace	src/common/stack_trace.cpp:134	Unwound call stack:
2024-08-03 11:17:51.305	    73bc1908b0c0	INFO	stacktrace	src/common/stack_trace.cpp:172	    [1] /usr/bin/monerod(+0x260e4) [0x5eadc76070e4] 
2024-08-03 11:17:51.305	    73bc1908b0c0	INFO	stacktrace	src/common/stack_trace.cpp:172	    [2] /usr/bin/monerod(+0x15f50d) [0x5eadc774050d] 
2024-08-03 11:17:51.305	    73bc1908b0c0	INFO	stacktrace	src/common/stack_trace.cpp:172	    [3] /usr/bin/monerod(+0x160a10) [0x5eadc7741a10] 
2024-08-03 11:17:51.305	    73bc1908b0c0	INFO	stacktrace	src/common/stack_trace.cpp:172	    [4] /usr/bin/monerod(+0x10d452) [0x5eadc76ee452] 
2024-08-03 11:17:51.306	    73bc1908b0c0	INFO	stacktrace	src/common/stack_trace.cpp:172	    [5] /usr/lib/libc.so.6(+0x25e08) [0x73bc18c34e08] 
2024-08-03 11:17:51.306	    73bc1908b0c0	INFO	stacktrace	src/common/stack_trace.cpp:172	    [6]  0x8c) [0x73bc18c34ecc]:__libc_start_main+0x8c) [0x73bc18c34ecc]
2024-08-03 11:17:51.306	    73bc1908b0c0	INFO	stacktrace	src/common/stack_trace.cpp:172	    [7] /usr/bin/monerod(+0x11ed05) [0x5eadc76ffd05] 
2024-08-03 11:17:51.306	    73bc1908b0c0	INFO	stacktrace	src/common/stack_trace.cpp:172	
2024-08-03 11:17:51.307	    73bc1908b0c0	INFO	global	src/daemon/core.h:102	Deinitializing core...
2024-08-03 11:17:51.321	    73bc1908b0c0	INFO	global	src/daemon/protocol.h:75	Stopping cryptonote protocol...
2024-08-03 11:17:51.321	    73bc1908b0c0	INFO	global	src/daemon/protocol.h:79	Cryptonote protocol stopped successfully
2024-08-03 11:17:51.322	    73bc1908b0c0	ERROR	daemon	src/daemon/main.cpp:377	Exception in main! Failed to initialize p2p server.
```

# Discussion History
## selsta | 2024-08-03T22:12:20+00:00
I don't see a crash here. Can you explain this in more detail? What do you mean with on reboot? Does monerod start correctly when you start it manually without systemd?

## jaredmo | 2024-08-03T22:25:49+00:00
Crash may be the wrong word. The p2p error at the end is the problem. It only occurs with the options listed above in `/etc/monerod.conf`, and leaves the service in a failed state. I have the systemd service enabled so it starts automatically at boot. If I restart the service later (i.e. systemctl restart) it starts successfully with the listed options.

`monerod` works fine manually. The systemd service works fine as well without the options above. However, I would like to use them. 

## selsta | 2024-08-03T22:27:34+00:00
Can you add `log-level=2` and share the logs? It currently doesn't show why it stops.

## jaredmo | 2024-08-03T23:56:28+00:00
I figured it out. The service file wasn't waiting for networking to be online before starting. That's needed for DNS resolution using `add-priority-node`. 

I changed the unit from `network.target` to `network-online.target`. Any chance of an upstream change?

```
[Unit]
Description=Monero Full Node
After=network-online.target
```

# Action History
- Created by: jaredmo | 2024-08-03T11:45:57+00:00
- Closed at: 2024-12-14T00:06:19+00:00
