---
title: '[Linux] monerod dies on startup'
source_url: https://github.com/monero-project/monero-gui/issues/697
author: patrikr
assignees: []
labels: []
created_at: '2017-04-26T22:55:54+00:00'
updated_at: '2017-06-09T21:10:40+00:00'
type: issue
status: closed
closed_at: '2017-06-09T21:10:40+00:00'
---

# Original Description
I downloaded monero-linux-x64-v0.10.3.1.tar.bz2 and I'm trying to run it on Debian 8.7 (jessie), but monerod dies after a few seconds. Here are the last few lines of output:

> 2017-04-27 01:29:20.782      3afdc677740        INFO    global  src/daemon/core.h:73    Initializing core...
> 2017-04-27 01:29:20.784      3afdc677740        INFO    global  src/cryptonote_core/cryptonote_core.cpp:326   Loading blockchain from folder /home/users/patrikr/.bitmonero/lmdb ...
> 2017-04-27 01:29:21.422      3afdc677740        INFO    global  src/daemon/core.h:78    Core initialized OK
> 2017-04-27 01:29:21.422      3afdc677740        INFO    global  src/daemon/rpc.h:68     Starting core rpc server...
> 2017-04-27 01:29:21.423 [SRV_MAIN]      INFO    global  src/daemon/rpc.h:73     Core rpc server started ok
> 2017-04-27 01:29:21.423 [SRV_MAIN]      INFO    global  src/daemon/p2p.h:78     Starting p2p net loop...
> terminate called without an active exception
> Abort (core dumped)

Running ./monerod --log-level 4, these are the last lines:

> 2017-04-27 01:53:05.042 [SRV_MAIN]      INFO    net     contrib/epee/include/net/abstract_tcp_server2.inl:820 Run server thread name: P2P
> 2017-04-27 01:53:05.042 [SRV_MAIN]      INFO    net     contrib/epee/include/net/abstract_tcp_server2.inl:820 Run server thread name: P2P
> 2017-04-27 01:53:05.042 [SRV_MAIN]      INFO    net     contrib/epee/include/net/abstract_tcp_server2.inl:820 Run server thread name: P2P
> terminate called without an active exception
> Abort (core dumped)

Any ideas?

# Discussion History
## Jaqueeee | 2017-05-02T16:08:23+00:00
Hi @patrikr 

Don't have an answer for you, but this question will most likely get more answers if you post in main repo instead (https://github.com/monero-project/monero/issues). This is the GUI repo.

## patrikr | 2017-06-09T21:10:40+00:00
For the record, I solved this problem by downloading the 32-bit version instead of the 64-bit one. (Even though it's a 64-bit system.)

# Action History
- Created by: patrikr | 2017-04-26T22:55:54+00:00
- Closed at: 2017-06-09T21:10:40+00:00
