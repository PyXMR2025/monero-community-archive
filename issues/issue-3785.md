---
title: Trying to run Monerod and p2p net loop stopped
source_url: https://github.com/monero-project/monero/issues/3785
author: 5-digits
assignees: []
labels:
- invalid
created_at: '2018-05-09T00:01:04+00:00'
updated_at: '2018-08-15T12:01:00+00:00'
type: issue
status: closed
closed_at: '2018-08-15T12:01:00+00:00'
---

# Original Description
The monerod Node as service doesn't works and i don't know what's wrong exactly : 

> Dragon@server:/etc/systemd/system$ sudo systemctl status  monerod.service
> ● monerod.service
>    Loaded: loaded (/etc/systemd/system/monerod.service; enabled; vendor preset: enabled)
>    Active: inactive (dead) since Tue 2018-05-08 17:52:28 MDT; 34s ago
>   Process: 7209 ExecStart=/home/Dragon/monerohss/monero-v0.12.0.0/monerod --config-file /home/Dragon/monerohss/monero-v0.12.0.0/monero.conf (code=exited, status=0/S
>  Main PID: 7209 (code=exited, status=0/SUCCESS)
> 
> May 08 17:52:23 server monerod[7209]: 2018-05-08 23:52:23.610        [SRV_MAIN]        INFO         global        src/daemon/rpc.h:79        core RPC server started ok
> May 08 17:52:23 server monerod[7209]: 2018-05-08 23:52:23.613        [SRV_MAIN]        INFO         global        src/daemon/p2p.h:78        Starting p2p net loop...
> May 08 17:52:23 server monerod[7209]: 2018-05-08 23:52:23.613        [SRV_MAIN]        INFO         global        src/daemon/p2p.h:80        p2p net loop stopped
> May 08 17:52:24 server monerod[7209]: 2018-05-08 23:52:24.620        [SRV_MAIN]        INFO         global        src/daemon/rpc.h:84        Stopping core RPC server...
> May 08 17:52:24 server monerod[7209]: 2018-05-08 23:52:24.620        [SRV_MAIN]        INFO         global        src/daemon/daemon.cpp:189        Node stopped.
> May 08 17:52:24 server monerod[7209]: 2018-05-08 23:52:24.621        [SRV_MAIN]        INFO         global        src/daemon/rpc.h:96        Deinitializing core RPC ser
> May 08 17:52:24 server monerod[7209]: 2018-05-08 23:52:24.621        [SRV_MAIN]        INFO         global        src/daemon/p2p.h:90        Deinitializing p2p...
> May 08 17:52:28 server monerod[7209]: 2018-05-08 23:52:28.627        [SRV_MAIN]        INFO         global        src/daemon/core.h:103        Deinitializing core...
> May 08 17:52:28 server monerod[7209]: 2018-05-08 23:52:28.629        [SRV_MAIN]        INFO         global        src/daemon/protocol.h:75        Stopping cryptonote pr
> May 08 17:52:28 server monerod[7209]: 2018-05-08 23:52:28.629        [SRV_MAIN]        INFO         global        src/daemon/protocol.h:79        Cryptonote protocol st
> lines 1-16/16 (END)
> 
My monero.conf file 

```
testnet=1
rpc-bind-ip=127.0.0.1
```


# Discussion History
## moneromooo-monero | 2018-05-09T08:22:11+00:00
Add --log-level 1, you'll get more info about what's going on.

## 5-digits | 2018-05-09T16:18:10+00:00
Nothing to change 

## moneromooo-monero | 2018-05-18T08:33:03+00:00
Since this seems to be systemd, are you using the systemd config from the monero tree, or your own ? If the latter, then use the former. systemd is a bit of a prick with terminating processes.

## moneromooo-monero | 2018-06-20T21:53:38+00:00
ping

## 5-digits | 2018-06-21T13:45:26+00:00
@moneromooo-monero  why ping ?

## moneromooo-monero | 2018-06-21T16:04:50+00:00
To get a reply on whether you're running with the systemd config from monero, or a custom one.

## moneromooo-monero | 2018-08-15T11:20:31+00:00
No reply, thought to be systemd's fault, reopen if you have evidence it's not.

+invalid

# Action History
- Created by: 5-digits | 2018-05-09T00:01:04+00:00
- Closed at: 2018-08-15T12:01:00+00:00
