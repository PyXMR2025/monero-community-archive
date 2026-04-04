---
title: stagenet dumps its logs into the same folder as mainnet
source_url: https://github.com/monero-project/monero/issues/3603
author: Gingeropolous
assignees: []
labels: []
created_at: '2018-04-11T02:36:32+00:00'
updated_at: '2018-05-16T11:16:57+00:00'
type: issue
status: closed
closed_at: '2018-05-16T11:16:57+00:00'
---

# Original Description
this was fixed for testnet a while ago, to put the log file in /bitmonero/testnet ..

i bet I could make a patch using the web git GUI ...

# Discussion History
## Gingeropolous | 2018-04-11T02:48:55+00:00
seems to be due to using a configuration file, because if I launch normally, the bitmonero.log file ends up in the stagenet subdirectory

## Gingeropolous | 2018-04-11T02:59:39+00:00
also happens with testnet

## stoffu | 2018-04-11T03:07:52+00:00
Could you provide the content of your config file so that the problem can be reproduced?

## Gingeropolous | 2018-04-14T04:38:55+00:00
```
user@node:~$ cat /etc/test_monerod.conf 
log-level=0
rpc-bind-ip=0.0.0.0
out-peers=1024
limit-rate-up=65536
limit-rate-down=65536
confirm-external-bind=1
rpc-restricted-bind-port=28089
add-priority-node=5.9.100.248:28080
testnet=1
```

@stoffu ^ ping

## stoffu | 2018-04-14T10:10:26+00:00
I think I see the problem now: if you run `monerod --config-file /etc/test_monerod.conf` without the `--testnet` flag, the program thinks that it's running for the mainnet and writes the log to the mainnet log file `~/.bitmonero/bitmonero.log` even though the config file contains `testnet=1`.

I think this is a minor bug that should be fixed. As a workaround, you could avoid this problem by making sure that you always specify `--testnet` (or `--stagenet`) when your config file contains `testnet=1` (or `stagenet=1`).


## stoffu | 2018-04-14T13:41:05+00:00
#3636

## DinoStray | 2018-04-16T08:51:50+00:00
While I put "log-file=xxx" in bitmonero.conf file, issue like this happened, too.

## moneromooo-monero | 2018-05-16T10:28:58+00:00
+resolved

# Action History
- Created by: Gingeropolous | 2018-04-11T02:36:32+00:00
- Closed at: 2018-05-16T11:16:57+00:00
