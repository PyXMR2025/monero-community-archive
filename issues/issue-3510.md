---
title: The win64 v0.12 release binary daemon shows lots of "Failed to parse bin body
  data"
source_url: https://github.com/monero-project/monero/issues/3510
author: Lafudoci
assignees: []
labels: []
created_at: '2018-03-28T10:24:04+00:00'
updated_at: '2021-08-13T06:46:34+00:00'
type: issue
status: closed
closed_at: '2021-08-13T06:46:34+00:00'
---

# Original Description
After I updated my v0.11.1 to v0.12 on win7x64 by release binary, lots of these error show up.
Do I need to worry about these error?
There is no such error on testnet and stagenet in the meantime.
```
2018-03-28 10:04:04.020 [RPC0]  ERROR   net.http        src/rpc/core_rpc_server.h:84    Failed to parse bin body data, body size=0
2018-03-28 10:04:04.114 [RPC0]  ERROR   net.http        src/rpc/core_rpc_server.h:84    Failed to parse bin body data, body size=0
2018-03-28 10:04:04.207 [RPC0]  ERROR   net.http        src/rpc/core_rpc_server.h:84    Failed to parse bin body data, body size=0
2018-03-28 10:04:04.301 [RPC0]  ERROR   net.http        src/rpc/core_rpc_server.h:84    Failed to parse bin body data, body size=0
2018-03-28 10:04:04.395 [RPC0]  ERROR   net.http        src/rpc/core_rpc_server.h:84    Failed to parse bin body data, body size=0
2018-03-28 10:04:04.488 [RPC0]  ERROR   net.http        src/rpc/core_rpc_server.h:84    Failed to parse bin body data, body size=0
2018-03-28 10:04:04.582 [RPC1]  ERROR   net.http        src/rpc/core_rpc_server.h:84    Failed to parse bin body data, body size=0
2018-03-28 10:04:04.675 [RPC0]  ERROR   net.http        src/rpc/core_rpc_server.h:84    Failed to parse bin body data, body size=0
2018-03-28 10:04:04.753 [RPC0]  ERROR   net.http        src/rpc/core_rpc_server.h:84    Failed to parse bin body data, body size=0
status
Height: 1539510/1539510 (100.0%) on mainnet, not mining, net hash 1.03 GH/s, v6(next fork in 9.0 days), up to date, 8(out)+0(in) connections, uptime 0d 6h 28m
45s
```


# Discussion History
## moneromooo-monero | 2018-03-28T10:35:22+00:00
What is callng those RPC ?

## Lafudoci | 2018-03-28T10:39:18+00:00
It's a node for public, so these are the error messages respond to the requests made by someone?

## moneromooo-monero | 2018-03-28T10:45:57+00:00
Try this patch: http://paste.debian.net/hidden/b4f712d5/
This will tell us what RPC is being called.

## Lafudoci | 2018-03-28T10:58:17+00:00
Thanks moneromooo, but I still couldn't make v0.12 build successfully on win64 in these days. Once I figure out how then I'll try it. But If these messages are not affecting node function and not security issue then this could be closed, thank you.

## moneromooo-monero | 2018-03-28T10:59:34+00:00
It almost certainly cannot be a security issue since this just cancels the call early. It probably affects node function since it prevents the caller from getting the RPC results.

## Keksov | 2018-04-04T13:27:13+00:00
@moneromooo-monero How to build monerod for Windows?

## moneromooo-monero | 2018-08-15T12:55:15+00:00
There is a README.md file with the instructions.

## selsta | 2021-08-13T06:46:34+00:00
Closing as the issue is old and there are no other reports. If someone has this issue with v0.17.2.0 please comment and I can reopen.

# Action History
- Created by: Lafudoci | 2018-03-28T10:24:04+00:00
- Closed at: 2021-08-13T06:46:34+00:00
