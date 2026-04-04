---
title: Sensitive info visible when UI locks due to inactivity
source_url: https://github.com/monero-project/monero-gui/issues/2586
author: ArtS
assignees: []
labels: []
created_at: '2019-12-12T08:20:47+00:00'
updated_at: '2019-12-20T01:06:54+00:00'
type: issue
status: closed
closed_at: '2019-12-20T01:06:54+00:00'
---

# Original Description
Steps to reproduce:

1. Open a wallet
2. Go to Settings => Show seeds & keys
3. Wait for the 'Lock wallet on inactivity' time limit to pass
4. UI locks, prompting for password. Keys and recovery info is still visible.

Expected behaviour:
No sensitive information is displayed.

GUI Version v0.15.0.1 (Qt 5.9.7)
Embedded Monero version  v0.15.0.1

Related to https://github.com/monero-project/monero-gui/issues/2564

# Discussion History
# Action History
- Created by: ArtS | 2019-12-12T08:20:47+00:00
- Closed at: 2019-12-20T01:06:54+00:00
