---
title: monerod syncs 100% at incorrect block height
source_url: https://github.com/monero-project/monero/issues/8589
author: ghost
assignees: []
labels: []
created_at: '2022-09-22T16:34:09+00:00'
updated_at: '2022-09-22T16:42:25+00:00'
type: issue
status: closed
closed_at: '2022-09-22T16:42:15+00:00'
---

# Original Description
OS: Void Linux
Monerod Version: Monero 'Oxygen Orion' (v0.17.2.3-unknown) directly from the Void Repository

Attempted:
- moving lmdb folder and trying to resync from scratch
- moving lmdb folder + deleting p2pstate.bin
- rebooting
- turning off VPN
- popping off the last 100000 blocks

It says 100% synced at block height 2688964 whereas localmonero.co says it's around 2717582

# Discussion History
## selsta | 2022-09-22T16:42:15+00:00
You are using a majorly outdated version, monero had a network upgrade. You need to use client v0.18.0.0 or newer.

# Action History
- Created by: ghost | 2022-09-22T16:34:09+00:00
- Closed at: 2022-09-22T16:42:15+00:00
