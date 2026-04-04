---
title: '[UX] monero-wallet-rpc Should Log That it''s Syncing on Default Log Level'
source_url: https://github.com/monero-project/monero/issues/8058
author: elibroftw
assignees: []
labels: []
created_at: '2021-11-13T03:29:02+00:00'
updated_at: '2021-11-19T17:34:22+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
When the `monero-wallet-rpc` needs to sync the wallet, it never opens any connection making the API inaccessible, the IO locked (takes no input), and the last output is about loading the wallet not syncing the wallet!

I propose that the log should include "Starting to sync wallet (# of blocks to sync)." That way I can just copy my wallet files used by the Gui wallet rather than spending 5+ hours wondering what I was doing wrong and landing up on another Monero Issue telling that user the wallet needed to be synced. 

This would save developers tons of time and is a simple log.

Another UX issue is with the CLI. The CLI takes so long just to process simple commands like help and exit. Makes no sense!

### Additional Information
Start the RPC with required arguments and the wallet-file as a wallet file that has not been synced in weeks, maybe a month.
The command line argument should be similar to the link below. Note that a ./ will be required to run the command on Linux.
Assume that local moderod is 1 month behind and so cannot be used.

https://monerodocs.org/interacting/monero-wallet-rpc-reference/#windows-development-example

Here is the important lines of the log output. I have indicated where a syncing thatement should go.

```
2021-11-13 01:23:59.895    16244    INFO    logging    contrib/epee/src/mlog.cpp:273    New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
2021-11-13 01:23:59.896    16244    WARNING    wallet.rpc    src/wallet/wallet_rpc_server.cpp:4495    Loading wallet...
2021-11-13 01:24:01.289    16244    WARNING    wallet.wallet2    src/wallet/wallet2.cpp:5642    Loaded wallet keys file, with public address: REMOVED

**The RPC at this point should log "WARNING Cannot bind server because wallet is syncing (# of blocks to sync)" 

2021-11-13 01:43:49.449    1308    INFO    global    contrib/epee/include/net/http_server_impl_base.h:79    Binding on 127.0.0.1 (IPv4):28088
2021-11-13 01:43:50.329    1308    WARNING    wallet.rpc    src/wallet/wallet_rpc_server.cpp:4559    Starting wallet RPC server
```
In addition, the warning statements shown here should be INFO statements, except for the new syncing statement which is definitely a warning, since it is of higher importance.

# Discussion History
## selsta | 2021-11-15T00:04:07+00:00
> The CLI takes so long just to process simple commands like help and exit.

While the wallet is scanning? Or always?

## elibroftw | 2021-11-15T00:09:35+00:00
That's while scanning. I switched over to the Gui instead since the wallet files I use with the Gui are more up to date.

# Action History
- Created by: elibroftw | 2021-11-13T03:29:02+00:00
