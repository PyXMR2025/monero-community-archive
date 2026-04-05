---
title: failed to connect on the daemon
source_url: https://github.com/xmrig/xmrig/issues/2054
author: username1565
assignees: []
labels: []
created_at: '2021-01-22T04:29:42+00:00'
updated_at: '2021-01-23T04:32:41+00:00'
type: issue
status: closed
closed_at: '2021-01-23T04:32:41+00:00'
---

# Original Description
**Describe the bug**
>A clear and concise description of what the bug is.

Failed to initialize solo-mining on daemon, with cn-pico algorithm.

**To Reproduce**
>Steps to reproduce the behavior.

xmrig.exe --algo=cn-pico --url=127.0.0.1:RPC_PORT --user=walletAddress --daemon --daemon-pool-interval=1000

**Expected behavior**
>A clear and concise description of what you expected to happen.

Must to be sucessfull connect on the daemon RPC, but connection is fail.

**Required data**
 - Miner log as text or screenshot
 - Config file or command line (without wallets)
 - OS: [e.g. Windows]
 - For GPU related issues: information about GPUs and driver version.

**Additional context**
>Add any other context about the problem here.

You can test this yourself. 

1. go to https://miningpoolstats.stream
2. put `turtle`-keyword in filter Algo.
3. select some coin with `cryptonight-pico/turtle` algorithm.
4. Go to their github.
5. Download daemon, and sync it.
6. Try to do solo-mining, using xmrig.
7. See fail connection on the daemon.

# Discussion History
## SChernykh | 2021-01-22T11:10:41+00:00
Solo mining is only supported for Monero, Dero and coins that have the exact same daemon RPC API. Adding support for every API variation of small cap coins is too cumbersome.

# Action History
- Created by: username1565 | 2021-01-22T04:29:42+00:00
- Closed at: 2021-01-23T04:32:41+00:00
