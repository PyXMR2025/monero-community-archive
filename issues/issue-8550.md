---
title: monerod docker container 180% CPU usage (After full sync, public node, full
  node)
source_url: https://github.com/monero-project/monero/issues/8550
author: mattredact
assignees: []
labels: []
created_at: '2022-09-06T04:01:27+00:00'
updated_at: '2023-10-15T23:29:24+00:00'
type: issue
status: closed
closed_at: '2023-10-15T23:29:24+00:00'
---

# Original Description
Hello!
I am running a public node on a VPS but seem to be having an issue with Monerod utilizing too much CPU. For the first 10 hours it runs, it's completely fine and doesn't use more than 4-8% of CPU. (This is after sync, 100%, and running a full node).

After the 10 hours, I get a sharp uptake to pretty much a constant 180% CPU usage (4 core, 8GB RAM VPS). I'm not quite sure what's going on. It will stay like this until I restart monerod. Once I restart, it will be okay again for another 10-12 hours, and then it goes into the same pattern. Any help would be appreciated. I can post whatever logs you may require.

I am using this docker container https://hub.docker.com/r/sethsimmons/simple-monerod

Below is my docker-compose.

```
   monerod:
    image: sethsimmons/simple-monerod:latest
    restart: unless-stopped
    container_name: monerod
    volumes:
      - /mnt/volume-1/bitmonero:/home/monero/.bitmonero
    ports:
      - 18080:18080
      - 18089:18089
    command: >-
      --rpc-restricted-bind-ip=0.0.0.0
      --rpc-restricted-bind-port=18089
      --public-node
      --no-igd
      --no-zmq
      --enable-dns-blocklist
      --limit-rate-up 100000
      --limit-rate-down 100000
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.monero.rule=Host(`${MONERO_HOSTNAME}`)"
      - "traefik.http.routers.monero.entrypoints=websecure"
      - "traefik.http.routers.monero.tls.certresolver=selfhostedservices"
      - "traefik.http.services.monero.loadbalancer.server.port=18089"
```


Cheers

# Discussion History
## selsta | 2022-09-06T09:18:33+00:00
As a first step try to run a node without docker and without config. If there are no issues re-add the config and check if you still have this issue.

## mattredact | 2022-09-07T06:09:51+00:00
Thought I would add to this for more info.

Here is also an image of the normal CPU usage to the left, versus when it goes into full CPU hog mode. Taken directly from the monerod CPU usage via Netdata.
![Screenshot-from-2022-09-06-22-22-13](https://user-images.githubusercontent.com/98937938/188795780-f557af9a-4494-4d57-8a94-71e80582d990.png)

Here are some logs that look concerning.

                                                                                                                                                                                                                                                                                                           
```
2022-09-06 04:53:44.913 [P2P0]  INFO    stacktrace      src/common/stack_trace.cpp:172  
2022-09-06 04:53:44.913 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:133  Exception: boost::wrapexcept<boost::bad_weak_ptr>
2022-09-06 04:53:44.913 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:134  Unwound call stack:
2022-09-06 04:53:44.913 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:172  
2022-09-06 04:53:44.913 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:133  Exception: boost::wrapexcept<boost::bad_weak_ptr>
2022-09-06 04:53:44.913 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:134  Unwound call stack:
2022-09-06 04:53:44.913 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:172  
2022-09-06 05:29:42.699 [P2P2]  INFO    stacktrace      src/common/stack_trace.cpp:133  Exception: boost::wrapexcept<boost::bad_weak_ptr>
2022-09-06 05:29:42.699 [P2P2]  INFO    stacktrace      src/common/stack_trace.cpp:134  Unwound call stack:
2022-09-06 05:29:42.699 [P2P2]  INFO    stacktrace      src/common/stack_trace.cpp:172  
2022-09-06 05:29:42.700 [P2P2]  INFO    stacktrace      src/common/stack_trace.cpp:133  Exception: boost::wrapexcept<boost::bad_weak_ptr>
2022-09-06 05:29:42.700 [P2P2]  INFO    stacktrace      src/common/stack_trace.cpp:134  Unwound call stack:
2022-09-06 05:29:42.700 [P2P2]  INFO    stacktrace      src/common/stack_trace.cpp:172  
2022-09-06 05:43:14.208     7fdd7e6ccb20        INFO    logging contrib/epee/src/mlog.cpp:273   New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
2022-09-06 05:43:14.208     7fdd7e6ccb20        INFO    global  src/daemon/main.cpp:296 Monero 'Fluorine Fermi' (v0.18.1.0-release)
2022-09-06 05:43:18.525     7f2320d78b20        INFO    logging contrib/epee/src/mlog.cpp:273   New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
2022-09-06 05:43:18.525     7f2320d78b20        INFO    global  src/daemon/main.cpp:296 Monero 'Fluorine Fermi' (v0.18.1.0-release)
2022-09-06 05:43:19.385     7f2320d78b20        INFO    msgwriter       src/common/scoped_message_writer.h:102  Height: 2705751/2705751 (100.0%) on mainnet, not mining, net hash 2.82 GH/s, v16, 12(out)+58(in) connections, uptime 0d 1h 38m 13s
2022-09-06 05:43:26.662     7f4ef8ca8b20        INFO    logging contrib/epee/src/mlog.cpp:273   New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
2022-09-06 05:43:26.662     7f4ef8ca8b20        INFO    global  src/daemon/main.cpp:296 Monero 'Fluorine Fermi' (v0.18.1.0-release)
2022-09-06 05:43:27.450     7f4ef8ca8b20        INFO    msgwriter       src/common/scoped_message_writer.h:102  Received 143285549 bytes (136.65 MB) in 81143 packets in 1.6 hours, average 23.71 kB/s = 0.02% of the limit of 97.66 MB/s
2022-09-06 05:43:27.450     7f4ef8ca8b20        INFO    msgwriter       src/common/scoped_message_writer.h:102  Sent 638502725 bytes (608.92 MB) in 58214 packets in 1.6 hours, average 105.67 kB/s = 0.11% of the limit of 97.66 MB/s
2022-09-06 05:44:41.983     7f675ed91b20        INFO    logging contrib/epee/src/mlog.cpp:273   New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
2022-09-06 05:44:41.983     7f675ed91b20        INFO    global  src/daemon/main.cpp:296 Monero 'Fluorine Fermi' (v0.18.1.0-release)
2022-09-06 05:44:59.104     7f32e65bcb20        INFO    logging contrib/epee/src/mlog.cpp:273   New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
2022-09-06 05:44:59.104     7f32e65bcb20        INFO    global  src/daemon/main.cpp:296 Monero 'Fluorine Fermi' (v0.18.1.0-release)
2022-09-06 05:44:59.664 [RPC0]  INFO    logging contrib/epee/src/mlog.cpp:273   New log categories: *:INFO,global:INFO,stacktrace:INFO,logging:INFO,msgwriter:INFO,perf.*:DEBUG
2022-09-06 05:44:59.664 [RPC0]  INFO    perf.daemon.rpc src/common/perf_timer.cpp:156   PERF       71    set_log_level
2022-09-06 05:44:59.664     7f32e65bcb20        INFO    msgwriter       src/common/scoped_message_writer.h:102  Log level is now 1
2022-09-06 05:44:59.666 [P2P6]  INFO    net.p2p.traffic contrib/epee/include/net/levin_protocol_handler_async.h:56      [185.107.95.88:54624 INC] 3779 bytes received for category command-2002 initiated by peer
```








```

2022-09-06 06:50:51.654 [P2P3]  INFO    stacktrace      src/common/stack_trace.cpp:133  Exception: boost::wrapexcept<boost::bad_weak_ptr>
2022-09-06 06:50:51.654 [P2P3]  INFO    stacktrace      src/common/stack_trace.cpp:134  Unwound call stack:
2022-09-06 06:50:51.654 [P2P3]  INFO    stacktrace      src/common/stack_trace.cpp:172  
2022-09-06 07:34:01.893 [P2P1]  INFO    stacktrace      src/common/stack_trace.cpp:133  Exception: boost::wrapexcept<boost::bad_weak_ptr>
2022-09-06 07:34:01.894 [P2P1]  INFO    stacktrace      src/common/stack_trace.cpp:134  Unwound call stack:
2022-09-06 07:34:01.895 [P2P1]  INFO    stacktrace      src/common/stack_trace.cpp:172  
2022-09-06 07:56:26.889 [P2P4]  INFO    stacktrace      src/common/stack_trace.cpp:133  Exception: boost::wrapexcept<boost::bad_weak_ptr>
2022-09-06 07:56:26.889 [P2P4]  INFO    stacktrace      src/common/stack_trace.cpp:134  Unwound call stack:
2022-09-06 07:56:26.889 [P2P4]  INFO    stacktrace      src/common/stack_trace.cpp:172  
2022-09-06 07:58:20.865     7fd990eb2b20        INFO    logging contrib/epee/src/mlog.cpp:273   New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:I>
2022-09-06 07:58:20.865     7fd990eb2b20        INFO    global  src/daemon/main.cpp:296 Monero 'Fluorine Fermi' (v0.18.1.0-release)
2022-09-06 07:58:22.080     7fd990eb2b20        INFO    msgwriter       src/common/scoped_message_writer.h:102  Received 163183427 bytes (155.62 MB) in 93250 packets in 1.5 hours, average 28.78 kB/s = 0.03% of the limit of 97.66 MB/s
2022-09-06 07:58:22.081     7fd990eb2b20        INFO    msgwriter       src/common/scoped_message_writer.h:102  Sent 1476208529 bytes (1.37 GB) in 87716 packets in 1.5 hours, average 260.36 kB/s = 0.26% of the limit of 97.66 MB/s
2022-09-06 08:28:04.244 [SRV_MAIN]      INFO    global  src/daemon/p2p.h:81     p2p net loop stopped
2022-09-06 08:28:04.245 [SRV_MAIN]      INFO    global  src/daemon/rpc.h:84     Stopping core RPC server...
2022-09-06 08:28:04.245 [SRV_MAIN]      INFO    global  src/daemon/rpc.h:84     Stopping restricted RPC server...
2022-09-06 08:28:04.245 [SRV_MAIN]      INFO    global  src/daemon/daemon.cpp:228       Node stopped.
2022-09-06 08:28:04.245 [SRV_MAIN]      INFO    global  src/daemon/rpc.h:96     Deinitializing core RPC server...
2022-09-06 08:28:04.247 [SRV_MAIN]      INFO    global  src/daemon/rpc.h:96     Deinitializing restricted RPC server...
2022-09-06 08:28:04.249 [SRV_MAIN]      INFO    global  src/daemon/p2p.h:91     Deinitializing p2p...
2022-09-06 08:28:04.268 [SRV_MAIN]      INFO    global  src/daemon/core.h:102   Deinitializing core...
2022-09-06 08:28:04.472 [SRV_MAIN]      INFO    global  src/daemon/protocol.h:75        Stopping cryptonote protocol...
2022-09-06 08:28:04.472 [SRV_MAIN]      INFO    global  src/daemon/protocol.h:79        Cryptonote protocol stopped successfully
2022-09-06 08:28:06.137     7f29c9ca5b20        INFO    logging contrib/epee/src/mlog.cpp:273   New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:I>
2022-09-06 08:28:06.137     7f29c9ca5b20        INFO    global  src/daemon/main.cpp:296 Monero 'Fluorine Fermi' (v0.18.1.0-release)
2022-09-06 08:28:06.138     7f29c9ca5b20        INFO    global  src/daemon/protocol.h:53        Initializing cryptonote protocol...
2022-09-06 08:28:06.138     7f29c9ca5b20        INFO    global  src/daemon/protocol.h:58        Cryptonote protocol initialized OK
2022-09-06 08:28:06.139     7f29c9ca5b20        INFO    global  src/daemon/core.h:64    Initializing core...
2022-09-06 08:28:06.139     7f29c9ca5b20        INFO    global  src/cryptonote_core/cryptonote_core.cpp:519     Loading blockchain from folder /home/monero/.bitmonero/lmdb ...
2022-09-06 08:28:23.637     7f29c9ca5b20        INFO    global  src/cryptonote_core/cryptonote_core.cpp:694     Loading checkpoints
2022-09-06 08:28:23.637     7f29c9ca5b20        INFO    global  src/daemon/core.h:81    Core initialized OK
2022-09-06 08:28:23.637     7f29c9ca5b20        INFO    global  src/daemon/p2p.h:64     Initializing p2p server...
2022-09-06 08:28:23.644     7f29c9ca5b20        INFO    global  src/daemon/p2p.h:69     p2p server initialized OK
2022-09-06 08:28:23.644     7f29c9ca5b20        INFO    global  src/daemon/rpc.h:63     Initializing core RPC server...
2022-09-06 08:28:23.645     7f29c9ca5b20        INFO    global  contrib/epee/include/net/http_server_impl_base.h:79     Binding on 127.0.0.1 (IPv4):18081
2022-09-06 08:28:23.655     7f29c9ca5b20        INFO    global  src/daemon/rpc.h:69     core RPC server initialized OK on port: 18081
2022-09-06 08:28:23.655     7f29c9ca5b20        INFO    global  src/daemon/rpc.h:63     Initializing restricted RPC server...
2022-09-06 08:28:23.656     7f29c9ca5b20        INFO    global  contrib/epee/include/net/http_server_impl_base.h:79     Binding on 0.0.0.0 (IPv4):18089
2022-09-06 08:28:24.013     7f29c9ca5b20        INFO    global  src/daemon/rpc.h:69     restricted RPC server initialized OK on port: 18089
2022-09-06 08:28:24.013     7f29c9ca5b20        INFO    global  src/daemon/rpc.h:74     Starting core RPC server...
2022-09-06 08:28:24.013 [SRV_MAIN]      INFO    global  src/daemon/rpc.h:79     core RPC server started ok
2022-09-06 08:28:24.013 [SRV_MAIN]      INFO    global  src/daemon/rpc.h:74     Starting restricted RPC server...
2022-09-06 08:28:24.013 [SRV_MAIN]      INFO    global  src/daemon/rpc.h:79     restricted RPC server started ok
2022-09-06 08:28:24.013 [SRV_MAIN]      INFO    global  src/daemon/daemon.cpp:214       Public RPC port 18089 will be advertised to other peers over P2P
2022-09-06 08:28:24.013 [SRV_MAIN]      INFO    global  src/daemon/p2p.h:79     Starting p2p net loop...
2022-09-06 08:28:24.333 [P2P9]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:2478    
2022-09-06 08:28:24.333 [P2P9]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:2478    **********************************************************************
2022-09-06 08:28:24.333 [P2P9]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:2478    You are now synchronized with the network. You may now start monero-wallet-cli.
2022-09-06 08:28:24.333 [P2P9]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:2478    
2022-09-06 08:28:24.333 [P2P9]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:2478    Use the "help" command to see the list of available commands.
2022-09-06 08:28:24.333 [P2P9]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:2478    **********************************************************************
2022-09-06 08:28:25.014 [P2P4]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1808    
2022-09-06 08:28:25.014 [P2P4]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1808    **********************************************************************
2022-09-06 08:28:25.014 [P2P4]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1808    The daemon will start synchronizing with the network. This may take a long time to complete.
2022-09-06 08:28:25.014 [P2P4]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1808    
2022-09-06 08:28:25.014 [P2P4]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1808    You can set the level of process detailization through "set_log <level|categories>" command,
2022-09-06 08:28:25.014 [P2P4]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1808    where <level> is between 0 (no details) and 4 (very verbose), or custom category based levels (eg, *:WARNING).
2022-09-06 08:28:25.014 [P2P4]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1808    
2022-09-06 08:28:25.014 [P2P4]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1808    Use the "help" command to see the list of available commands.
2022-09-06 08:28:25.014 [P2P4]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1808    Use "help <command>" to see a command's documentation.
2022-09-06 08:28:25.014 [P2P4]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1808    
```**********************************************************************


```




## selsta | 2022-09-07T14:22:06+00:00
There isn't anything interesting in that log. Can you try to post the output of log level 2 while there is high CPU usage?

## mattredact | 2022-09-08T07:19:37+00:00
> 

I am trying a pruned node from scratch. Set log level 2, will see how it behaves after the sync and report back.

## sethforprivacy | 2022-09-14T12:46:34+00:00
I just had the same on v0.18.1.0 (Dockerized) running alongside p2pool, with the following spammed in logs:

`Unable to send ZMQ/Pub - ZMQ server destroyed`

## jeffro256 | 2022-10-02T04:13:58+00:00
Sounds possibly related to the issue @vtnerd is working on ironing out: https://github.com/monero-project/monero/pull/8592

## hajes | 2022-10-05T17:28:50+00:00
I am having same issues. After last two upgrades, there is something funky. 

After initial sync, all was ok...then it got stuck at high CPU usage around 180% and 32% of memory (~10GB).

I will try log level 2 because I have no idea why

## selsta | 2022-10-05T21:12:12+00:00
@hajes can you post more information? Do you also use docker? What is your monerod config? Are you p2pool mining?

## hajes | 2022-10-06T15:18:27+00:00
Debian Linux full server (no VPS, no VM), no pool mining. I am running at least full node (as a part of contribution) because mining is not profitable.

After hard fork, for some unknown reason git pull didn't finish as suppose to...and my node was 20 days not synced because it was running old version. After upgrade, sync did run for like 2 days...but it got stuck at 180% cpu, even if fully synced. It run for a week or so before I noticed.

I restarted daemon (running systemd service)...it is running ok, and then something happens...cpu load 180% as described above by.

I have restarted daemon last night...so far no issues. This time, loglevel 2 activated. Once, I know more...I provide logs.

I was suggested following config

---------------------------------------------
data-dir=/home/hajes/.bitmonero
log-file=/var/log/monero/monerod.log
max-log-file-size=0            # Prevent monerod from managing the log files; we want logrotate to take care of that
log-level=2

p2p-bind-ip=0.0.0.0            # Bind to all interfaces (the default)
p2p-bind-port=18080            # Bind to default port

rpc-bind-ip=0.0.0.0            # Bind to all interfaces
rpc-bind-port=18081            # Bind on default port
confirm-external-bind=1        # Open node (confirm)
restricted-rpc=1               # Prevent unsafe RPC calls
no-igd=1                       # Disable UPnP port mapping

db-sync-mode=safe

enforce-dns-checkpointing=1

out-peers=64              # This will enable much faster sync and tx awareness; the default 8 is suboptimal nowadays
in-peers=1024             # The default is unlimited; we prefer to put a cap on this

limit-rate=1024

## hajes | 2022-10-12T17:16:48+00:00
no luck in CPU hog department, but monerod is currently hogging 49% of RAM (16GB). Is it normal?

I have over 1GB of logs...at level 2, it is producing 300MB/hour

## hajes | 2022-10-19T19:56:41+00:00
it finally happened. from 2am...monerod runs `210.0%  CPU 46.9% RAM (about 14GB) monerod `

flat out for almost a day, without any signs to end up

there is gigabytes of logs. where should I send it guys?

## jeffro256 | 2022-10-20T04:24:21+00:00
Put it in a `.tar.gz` and upload it somewhere and share the link

## hajes | 2022-10-20T14:51:48+00:00
something happened on 2022-10-19 around 4am UTC - monerod jumped from usual cpu usage to 200%+
it runs flat out for days if you don't kill it...I have killed the daemon after about 1.5 day...it sadly, increases my server consumption by 40-50Wh...in modern energy climate, it is not possible no keep it running if there is something misconfigured or bug.

there are logs [https://www.transfernow.net/dl/202210200YSsVt5L/3mzqXun1](url)
~800MB compressed...available for 7 days before they erase it from sharing service. I erased anything older than 17/10.

In previous days, nothing happened. Logging kills my server...it logs about 200MB per hour uncompressed.

if you need something to test, let me know and thanks guys



## selsta | 2022-10-20T15:50:26+00:00
I took a look through the last log and so far didn't see anything interesting. Can you disable public RPC access and see if you can still reproduce the issue?

## hajes | 2022-10-20T17:28:01+00:00
I have removed from config

rpc-bind-ip=0.0.0.0 # Bind to all interfaces
rpc-bind-port=18081 # Bind on default port
confirm-external-bind=1 # Open node (confirm)
restricted-rpc=1 # Prevent unsafe RPC calls
no-igd=1 # Disable UPnP port mapping

and enabled level 2 logging.

see what happens...i see lots of p2p but nothing useful


## hajes | 2022-11-07T16:15:48+00:00
So far no issues, looks like RPC was main cause.

## selsta | 2022-12-22T23:05:54+00:00
Related: #8685

From what I can tell it's a dependency issue and it does not show up with official release binaries.

## Jayd603 | 2023-10-15T18:52:25+00:00
FYI - this resolved itself for me with an upgrade to the latest monerod.  It now uses a fraction of the CPU.



# Action History
- Created by: mattredact | 2022-09-06T04:01:27+00:00
- Closed at: 2023-10-15T23:29:24+00:00
