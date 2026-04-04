---
title: Trouble synchronizing wallet?
source_url: https://github.com/monero-project/monero-gui/issues/4097
author: Toekneetwo
assignees: []
labels: []
created_at: '2023-01-08T17:28:46+00:00'
updated_at: '2023-01-08T19:10:01+00:00'
type: issue
status: closed
closed_at: '2023-01-08T19:10:01+00:00'
---

# Original Description
Hello... I haven't been able to synchronize my wallet. I am using a remote node (selsta2.featherwallet.net:18081), which has completed more blocks than my local node, but still slows way down at ~80%. Is it normal for synchronization to take hours? On the log page, it says "Error: Couldn't connect to daemon: 127.0.0.1:18081", and won't let me enter anything in the command box below, which doesn't fill me with confidence. I've tried resetting the block height, to no avail. Help?

# Discussion History
## selsta | 2023-01-08T17:31:17+00:00
Please go to Settings -> Info and post:

- Version
- Wallet restore height

Also ehat kind of computer hardware do you have? Are you using a hardware wallet like Ledger or Trezor? Are you using Tor / VPN?

> and won't let me enter anything in the command box below, which doesn't fill me with confidence

You can't send commands to a remote node.

## Toekneetwo | 2023-01-08T17:36:35+00:00
GUI version: 0.18.1.2-unknown (Qt 5.15.6)
Embedded Monero version: 0.18.1.2-unknown
Wallet restore height: 2092000
Wallet mode: Advanced mode (Remote node)
Graphics mode: OpenGL

Windows 10, yes VPN (Nord), no hardware wallet. Thanks for the quick response!

## Toekneetwo | 2023-01-08T19:10:01+00:00
Never mind, it eventually synched. Thanks anyway!

# Action History
- Created by: Toekneetwo | 2023-01-08T17:28:46+00:00
- Closed at: 2023-01-08T19:10:01+00:00
