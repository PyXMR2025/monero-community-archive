---
title: Run Monero Daemon as service
source_url: https://github.com/monero-project/monero/issues/3777
author: 5-digits
assignees: []
labels:
- invalid
created_at: '2018-05-07T20:31:57+00:00'
updated_at: '2018-08-15T12:09:00+00:00'
type: issue
status: closed
closed_at: '2018-08-15T12:09:00+00:00'
---

# Original Description
How to run Monero Daemon as service ?

each time when start running the node i make it like this
`./monerod`
 when type monerod it doesn't works, so I will necessarily execute it like a linux executable
./app because i'm using ubuntu 16
but when hit [ CTRL + C ] every thing is stopped 
So how to run it like Zcash and bitcoin just by calling ( bitcoind --testnet for example ) 


# Discussion History
## moneromooo-monero | 2018-05-07T21:17:04+00:00
You mean make it fork like a daemon ? Add --detach.


## gene-telligent | 2018-05-07T21:53:49+00:00
If you're on Ubuntu and want to run it as a proper service managed by systemd, I'd also recommend using this https://github.com/monero-project/monero/blob/master/utils/systemd/monerod.service as a starting point!

## 5-digits | 2018-05-09T16:27:05+00:00
Doesn't work properly 
```
● monerod.service
   Loaded: loaded (/etc/systemd/system/monerod.service; enabled; vendor preset: enabled)
   Active: active (running) since Wed 2018-05-09 10:09:37 MDT; 6s ago
 Main PID: 11376 (monerod)
   CGroup: /system.slice/monerod.service
           └─11376 /home/Dragon/monerohss/monero-v0.12.0.0/monerod --testnet --config-file /home/Dragon/monerohss/monero-v0.12.0.0/monero.conf

May 09 10:09:42 server monerod[11376]: 2018-05-09 16:09:42.080            7f975c29c740        INFO         global        src/cryptonote_core/cryptonote_core.cpp:525        Loading checkpoints
May 09 10:09:42 server monerod[11376]: 2018-05-09 16:09:42.080            7f975c29c740        INFO         global        src/daemon/core.h:92        Core initialized OK
May 09 10:09:42 server monerod[11376]: 2018-05-09 16:09:42.080            7f975c29c740        INFO         global        src/daemon/rpc.h:74        Starting core RPC server...
May 09 10:09:42 server monerod[11376]: 2018-05-09 16:09:42.080        [SRV_MAIN]        INFO         global        src/daemon/rpc.h:79        core RPC server started ok
May 09 10:09:42 server monerod[11376]: 2018-05-09 16:09:42.082        [SRV_MAIN]        INFO         global        src/daemon/p2p.h:78        Starting p2p net loop...
May 09 10:09:42 server monerod[11376]: 2018-05-09 16:09:42.082        [SRV_MAIN]        INFO         global        src/daemon/p2p.h:80        p2p net loop stopped
May 09 10:09:43 server monerod[11376]: 2018-05-09 16:09:43.090        [SRV_MAIN]        INFO         global        src/daemon/rpc.h:84        Stopping core RPC server...
May 09 10:09:43 server monerod[11376]: 2018-05-09 16:09:43.091        [SRV_MAIN]        INFO         global        src/daemon/daemon.cpp:189        Node stopped.
May 09 10:09:43 server monerod[11376]: 2018-05-09 16:09:43.091        [SRV_MAIN]        INFO         global        src/daemon/rpc.h:96        Deinitializing core RPC server...
May 09 10:09:43 server monerod[11376]: 2018-05-09 16:09:43.092        [SRV_MAIN]        INFO         global        src/daemon/p2p.h:90        Deinitializing p2p...

```
the Monerod service file :: 

```
testnet=1
rpc-bind-ip=127.0.0.1
rpc-bind-port=18556
p2p-bind-port=18555
p2p-bind-ip=127.0.0.1
rpc-login=user:password
```
and when connecting to the wallet through the (monero-wallet-cli)


 ./monero-wallet-cli --testnet
 

> Error: wallet failed to connect to daemon: http://localhost:28081. Daemon either is not started or wrong port was passed. Please make sure daemon is running or change the daemon address using the 'set_daemon' command.



## moneromooo-monero | 2018-05-09T16:53:48+00:00
You don't seem to be using --detach as I said above.

## 5-digits | 2018-05-09T17:17:26+00:00
i'm also trying with --detach flag but the result is the same  
```
ExecStart=/home/Dragon/monerohss/monero-v0.12.0.0/monerod --testnet   --config-file /home/Dragon/monerohss/monero-v0.12.0.0/monero.conf \
   --detach
```

## moneromooo-monero | 2018-05-09T17:22:26+00:00
Is this systemd ? If so, there's a systemd config in utils/systemd. It is apparently a pita for daemons. --detach does all the normal daemon stuff and systemd just gets in the way unless you tell it specifically to keep its paws off.
--detach can be used standalone, like any normal daemon.


## papadave66 | 2018-05-10T02:27:47+00:00
you can run monerod with ` --non-interactive ` .and you can ctrl+z  +bg to run in background

## baryluk | 2018-05-16T15:38:12+00:00
With systemd you can leave it attached (it is actually even better), and even make it output log data to stderr or stdout, systemd will take care of it. Do not run it as root tho, but normal your account or separate user.

If you want easier route, just use crontab, either `crontab -e` and then add:
```text
@reboot cd /home/xyz/monero-directory && ./monerod --options --options --detach
```

Or if you want to make it smarter and automatically start it if it crashes, make a separate script that checks if it is started and if not start it, and then run it from crontab every 5 minutes.


## moneromooo-monero | 2018-08-15T11:28:45+00:00
No monero bug here.

+invalid

# Action History
- Created by: 5-digits | 2018-05-07T20:31:57+00:00
- Closed at: 2018-08-15T12:09:00+00:00
