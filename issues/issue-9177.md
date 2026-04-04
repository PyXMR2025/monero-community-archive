---
title: monero-wallet-rpc can't work via socks5
source_url: https://github.com/monero-project/monero/issues/9177
author: longnetwork
assignees: []
labels:
- duplicate
created_at: '2024-02-17T22:50:43+00:00'
updated_at: '2024-02-19T19:09:42+00:00'
type: issue
status: closed
closed_at: '2024-02-18T00:06:13+00:00'
---

# Original Description
I use the --proxy option to specify a local proxy. My proxy responds with an error that version 4 for socks is not correct.
full run command monero-wallet-rpc:
`monero-wallet-rpc --log-level 0 --trusted-daemon --daemon-ssl autodetect --daemon-ssl-allow-any-cert --max-concurrency 6 --non-interactive --disable-rpc-login --rpc-bind-port {{RPC_WALLET_PORT}} --rpc-bind-ip 127.0.0.1 --disable-rpc-ban --wallet-dir {{WALLET_DIR}} --proxy 127.0.0.1:{{SOCKS5_PORT}}`

**monero-wallet-rpc** does not support socks5

# Discussion History
## vtnerd | 2024-02-18T00:01:35+00:00
This is a duplicate of #8562 

## vtnerd | 2024-02-19T19:09:15+00:00
@selsta I don't think this is completed, but we definitely don't need two bug reports for this.

## vtnerd | 2024-02-19T19:09:41+00:00
Nevermind, I see you added the `duplicate` label also.

# Action History
- Created by: longnetwork | 2024-02-17T22:50:43+00:00
- Closed at: 2024-02-18T00:06:13+00:00
