---
title: 'Wallet cli does not connect to daemon, although curl works '
source_url: https://github.com/monero-project/monero/issues/8536
author: aghamir
assignees: []
labels: []
created_at: '2022-08-24T15:13:30+00:00'
updated_at: '2022-08-25T19:46:46+00:00'
type: issue
status: closed
closed_at: '2022-08-25T19:46:46+00:00'
---

# Original Description
## Version info
Monero cli/Monerod version: v0.18.1.0
## Issue description
I've run monerod under a domain(behind nginx) with https schema.
When I run this curl:
```
curl https://monero.example.com/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"get_info"}' -H 'Content-Type: application/json'
```
However, when I run `wallet-monero-cli` like this:
```
monero-wallet-cli --generate-new-wallet wallet_1 --mnemonic-language english --use-english-language-names --daemon-address  https://monero.example.com/ --subaddress-lookahead 5:1000 --max-concurrency 8
```
It cannot connect to the daemon and returns:
```
Error: wallet failed to connect to daemon: https://monero.example.com. Daemon either is not started or wrong port was passed. Please make sure daemon is running or change the daemon address using the 'set_daemon' command.
```

# Discussion History
## selsta | 2022-08-25T00:29:54+00:00
Try `--daemon-address monero.example.com` instead, or `--daemon-address monero.example.com:18081` if that's the RPC port.

## aghamir | 2022-08-25T19:38:26+00:00
@selsta 
Thanks a lot. It fixed with `--daemon-address monero.example.com:443`.

# Action History
- Created by: aghamir | 2022-08-24T15:13:30+00:00
- Closed at: 2022-08-25T19:46:46+00:00
