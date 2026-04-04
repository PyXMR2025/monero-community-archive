---
title: Wallet is Synchronized , but shows not mining
source_url: https://github.com/monero-project/monero-gui/issues/4272
author: cancer09
assignees: []
labels: []
created_at: '2024-01-31T07:09:58+00:00'
updated_at: '2024-01-31T11:12:21+00:00'
type: issue
status: closed
closed_at: '2024-01-31T11:12:21+00:00'
---

# Original Description
[31-01-2024 12:34] 2024-01-31 07:04:29.965 I Monero 'Fluorine Fermi' (v0.18.3.1-release) 
Height: 3073795/3073795 (100.0%) on mainnet, not mining, net hash 2.27 GH/s, v16, 12(out)+0(in) connections, uptime 0d 0h 6m 21s

I am trying to do on xmring and that shows accepted, but this still shows like no mining

# Discussion History
## selsta | 2024-01-31T11:12:13+00:00
XMRig is a separate miner. Only if you use the internal miner built in in monerod then it will say "mining". You have to look at the status on XMRig.

# Action History
- Created by: cancer09 | 2024-01-31T07:09:58+00:00
- Closed at: 2024-01-31T11:12:21+00:00
