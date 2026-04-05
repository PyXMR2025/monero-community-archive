---
title: 怎么去解决这个问题，我重新弄了也不行
source_url: https://github.com/xmrig/xmrig/issues/2721
author: qiuanfu
assignees: []
labels: []
created_at: '2021-11-26T11:26:32+00:00'
updated_at: '2021-12-19T15:29:20+00:00'
type: issue
status: closed
closed_at: '2021-12-19T15:29:20+00:00'
---

# Original Description
**Describe the bug**
A clear and concise description of what the bug is.

**To Reproduce**
Steps to reproduce the behavior.

**Expected behavior**
A clear and concise description of what you expected to happen.

**Required data**
 - Miner log as text or screenshot
 - Config file or command line (without wallets)
 - OS: [e.g. Windows]
 - For GPU related issues: information about GPUs and driver version.

**Additional context**
Add any other context about the problem here.
![微信截图_20211126192555](https://user-images.githubusercontent.com/95081199/143574005-c59b7e2e-9389-4e32-9890-b051fbdef9b4.png)


# Discussion History
## Lonnegan | 2021-11-26T11:35:27+00:00
You can't connect to a rx pool and select BTT as your coin. BTT (Bittorrent) is not a rx coin. You have to use XMR as coin and add your Monero address, not your Bittorrent address.

## SChernykh | 2021-11-26T12:00:24+00:00
It's unmineable.com and that's what they do (mining RandomX/Monero and auto-converting to other coins). Why "operation cancelled" is another question though. Probably ISP blocking.

## Spudz76 | 2021-11-26T15:42:18+00:00
DNS is filtered or otherwise blocked for mining pool hosts.  Whitelist and/or bypass ISP censorship using public unfiltered DNS or VPN.

qiuanfu in the command line is not in the right place, it says

## qiuanfu | 2021-12-04T02:20:00+00:00
如何解决呢？我之前都做得好好的

## felix920506 | 2021-12-04T03:02:52+00:00
ping看看能不能ping的到矿池

# Action History
- Created by: qiuanfu | 2021-11-26T11:26:32+00:00
- Closed at: 2021-12-19T15:29:20+00:00
