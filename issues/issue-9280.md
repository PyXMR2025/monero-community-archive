---
title: Monero RPC Wallet loosing connection to the daemon
source_url: https://github.com/monero-project/monero/issues/9280
author: maksemen2
assignees: []
labels: []
created_at: '2024-04-05T21:15:22+00:00'
updated_at: '2024-04-05T21:57:43+00:00'
type: issue
status: closed
closed_at: '2024-04-05T21:57:43+00:00'
---

# Original Description
```
2024-04-05 21:09:39.918 W Transaction extra has unsupported format: <af664d349c576495663c35933e6f3a460979d920b2eb069e8d53e17a9fc4ff3f>
2024-04-05 21:09:39.918 W Transaction extra has unsupported format: <d98e65a432e61234705787307d519bb1384ad6b7cd3bc5558dc5981ffa23f703>
2024-04-05 21:09:39.935 W Transaction extra has unsupported format: <987d3ac9c470961bb57257f841fa3389e56cf434b06f84851c839232bd1591e2>
2024-04-05 21:09:39.935 W Transaction extra has unsupported format: <bc922c6cd944160f66aa41adfa4cbebd086e8f859d61da0b6635176b9a458b5e>
2024-04-05 21:09:39.935 W Transaction extra has unsupported format: <566fce8d92b301850e27d909a0d5150318306a4836e392f7ac293f911c7f4dd6>
2024-04-05 21:09:39.935 W Transaction extra has unsupported format: <79384d8ceba764e7b767c2dd5759b87aa37e17feef4da2326465a7b5eff8c7b2>
2024-04-05 21:09:39.949 W Transaction extra has unsupported format: <31e2da20412edf4cbf8fbe5e56a501148b9041ce36c4c35b4c3abb4c66038674>
2024-04-05 21:09:40.249 I Binding on 127.0.0.1 (IPv4):28088
2024-04-05 21:09:41.387 W Starting wallet RPC server
```

It works for about 10 seconds, but then start throwing exceptions:
```
2024-04-05 21:10:02.662 E !r. THROW EXCEPTION: tools::error::no_connection_to_daemon
2024-04-05 21:10:02.664 E !r. THROW EXCEPTION: tools::error::no_connection_to_daemon
2024-04-05 21:10:02.664 E !r. THROW EXCEPTION: tools::error::no_connection_to_daemon
2024-04-05 21:10:02.664 E !r. THROW EXCEPTION: tools::error::no_connection_to_daemon
2024-04-05 21:10:02.664 E pull_blocks failed, try_count=3
```

I run rpc wallet with this command:
`monero-wallet-rpc.exe --wallet-file wallet_name --password "<password>" --rpc-bind-port 28088 --disable-rpc-login --daemon-host xmr-node.cakewallet.com`

# Discussion History
## selsta | 2024-04-05T21:34:35+00:00
Did you reproduce this when running your own node?

## maksemen2 | 2024-04-05T21:53:54+00:00
> Did you reproduce this when running your own node?

my own node works correctly

## selsta | 2024-04-05T21:55:40+00:00
It's possible that Cake Wallet nodes are simply overloaded, they have a lot of users simultaneously using the same node(s).

## maksemen2 | 2024-04-05T21:57:43+00:00
> It's possible that Cake Wallet nodes are simply overloaded, they have a lot of users simultaneously using the same node(s).

yeah, i suppose this is the problem. Thank you.

# Action History
- Created by: maksemen2 | 2024-04-05T21:15:22+00:00
- Closed at: 2024-04-05T21:57:43+00:00
