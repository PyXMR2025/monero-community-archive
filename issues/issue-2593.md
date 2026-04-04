---
title: '[Qt Warning] Populating font family aliases took 210 ms.'
source_url: https://github.com/monero-project/monero-gui/issues/2593
author: selsta
assignees: []
labels: []
created_at: '2019-12-14T02:25:47+00:00'
updated_at: '2020-04-22T18:37:59+00:00'
type: issue
status: closed
closed_at: '2020-04-22T18:37:59+00:00'
---

# Original Description
Using Qt 5.14, the following warning appears when opening the GUI:

> Populating font family aliases took 210 ms. Replace uses of missing font family "White" with one that exists to avoid this cost.

Looks like something we can optimise.

# Discussion History
# Action History
- Created by: selsta | 2019-12-14T02:25:47+00:00
- Closed at: 2020-04-22T18:37:59+00:00
