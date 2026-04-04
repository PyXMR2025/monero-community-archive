---
title: status shows wrong version
source_url: https://github.com/monero-project/monero-gui/issues/3837
author: anonaddict
assignees: []
labels: []
created_at: '2022-02-12T16:16:01+00:00'
updated_at: '2022-02-12T16:26:52+00:00'
type: issue
status: closed
closed_at: '2022-02-12T16:26:34+00:00'
---

# Original Description
I installed monero-wallet-gui from monero-gui-linux-x64-v0.17.3.1.tar.bz2 but when running 

>>> status
[12.02.22 17:13] 2022-02-12 16:13:53.706 I Monero 'Oxygen Orion' (v0.17.3.0-release)
Height: 2530439/2557951 (98.9%) on mainnet, not mining, net hash 3.27 GH/s, v14, 12(out)+0(in) connections, uptime 0d 14h 42m 55s

it says v0.17.3.0-release instead of v0.17.3.1

# Discussion History
## selsta | 2022-02-12T16:26:34+00:00
That's the daemon version, v0.17.3.0 is correct.

See Settings -> Info.

# Action History
- Created by: anonaddict | 2022-02-12T16:16:01+00:00
- Closed at: 2022-02-12T16:26:34+00:00
