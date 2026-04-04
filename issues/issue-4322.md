---
title: Changing unit in CLI wallet breaks balance in GUI wallet
source_url: https://github.com/monero-project/monero-gui/issues/4322
author: LegoLivesMatter
assignees: []
labels:
- bug
created_at: '2024-06-08T11:10:28+00:00'
updated_at: '2024-06-08T17:52:52+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
The GUI wallet does not seem to support the unit setting present in the CLI wallet. If the unit is set to millinero in the CLI wallet, the GUI wallet will continue to believe that the balance is in monero and show the millinero value as if it were the monero value. This makes it seem like I have 1000 times more XMR than I actually do. Resetting the unit to monero in the CLI wallet makes the GUI wallet behave normally again.

# Steps to reproduce
1. Open wallet in CLI
2. Execute `set unit millinero`
3. Close CLI
4. Open wallet in GUI

# Discussion History
# Action History
- Created by: LegoLivesMatter | 2024-06-08T11:10:28+00:00
