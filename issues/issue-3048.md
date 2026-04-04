---
title: Make GUI remote node config configurable before opening any wallet
source_url: https://github.com/monero-project/monero-gui/issues/3048
author: skironDotNet
assignees: []
labels: []
created_at: '2020-08-25T05:15:25+00:00'
updated_at: '2020-11-16T02:56:02+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
It never makes sense to load the wallet first and then see GUI auto run local daemon, or not knowing up front the configuration

# Discussion History
## selsta | 2020-08-25T22:14:16+00:00
Initially it gets configured during the wizard (wallet creation / wallet restore).

## ronohara | 2020-11-16T02:54:53+00:00
Perhaps limited 'Settings' should also be available from the Logon screen - specifically everything except the Wallet tab. The wallet tab is specific to the wallet that you open/create. The other settings are global.
  

# Action History
- Created by: skironDotNet | 2020-08-25T05:15:25+00:00
