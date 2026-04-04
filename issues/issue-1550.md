---
title: Can't transfer from wallet cli in 0.10.1
source_url: https://github.com/monero-project/monero/issues/1550
author: arnuschky
assignees: []
labels: []
created_at: '2017-01-09T21:41:08+00:00'
updated_at: '2017-01-09T22:09:28+00:00'
type: issue
status: closed
closed_at: '2017-01-09T22:09:28+00:00'
---

# Original Description
I get this from a clean build, v0.10.1.0-release. Testnet on Ubuntu 16.04.
```
[wallet 9zpRpz]: transfer 4 9zpRpzzRBAx4neByW6Z5XEcRxs9KtdyEWSdbXQwuYBucUFvN9npe5iYYVoN51oLxEqKksPtrCUvjfgcP1qERjJur2EAT5YR 123 f90c0b1558eafe3fba8565bd16fde162c1a583f1d0cc1ecadb1585cb3a32fa37
Error: no connection to daemon. Please make sure daemon is running.
[wallet 9zpRpz]: transfer 4 9zpRpzzRBAx4neByW6Z5XEcRxs9KtdyEWSdbXQwuYBucUFvN9npe5iYYVoN51oLxEqKksPtrCUvjfgcP1qERjJur2EAT5YR 123 f90c0b1558eafe3fba8565bd16fde162c1a583f1d0cc1ecadb1585cb3a32fa37
Error: Daemon uses a different RPC major version (0) than the wallet (1): http://localhost:28081. Either update one of them, or use --allow-mismatched-daemon-version.
```

Daemon log:
```
2017-Jan-09 22:39:25.117109 [RPC1]ERROR monero.git/contrib/epee/include/net/abstract_tcp_server2.inl:355 Exception at [connection<t_protocol_handler>::handle_read], what=Attempting to get output pubkey by index, but key does not exist
```


# Discussion History
## arnuschky | 2017-01-09T21:42:43+00:00
Trying again with `--allow-mismatched-daemon-version` gives me this:

```
[wallet 9zpRpz]: transfer 4 9zpRpzzRBAx4neByW6Z5XEcRxs9KtdyEWSdbXQwuYBucUFvN9npe5iYYVoN51oLxEqKksPtrCUvjfgcP1qERjJur2EAT5YR 123 f90c0b1558eafe3fba8565bd16fde162c1a583f1d0cc1ecadb1585cb3a32fa37
Error: transaction <1217294809a5ad29e62c317b8165ab978839cb294b6c7e393f233aceb484fdef> was rejected by daemon with status: Failed
Error: Reason: double spend
```

Which is a bit worrying.

## moneromooo-monero | 2017-01-09T22:00:18+00:00
Use wallet and daemon built from the same tree.

## arnuschky | 2017-01-09T22:09:23+00:00
`refresh_bc` seemed to have solved the problem. No idea why.

(Wallet and daemon were built from clean 0.10.1 tree)

# Action History
- Created by: arnuschky | 2017-01-09T21:41:08+00:00
- Closed at: 2017-01-09T22:09:28+00:00
