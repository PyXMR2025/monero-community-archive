---
title: '`scan_tx` failing with error "Expected block not returned by daemon" in release
  branch'
source_url: https://github.com/monero-project/monero/issues/8951
author: woodser
assignees: []
labels: []
created_at: '2023-07-17T15:52:46+00:00'
updated_at: '2023-08-17T15:26:33+00:00'
type: issue
status: closed
closed_at: '2023-08-17T15:26:33+00:00'
---

# Original Description
`scan_tx` is failing in the release branch if the wallet is already synced, with the error message: "Expected block not returned by daemon".

The error message was introduced in the release branch with https://github.com/monero-project/monero/pull/8566.

# Discussion History
# Action History
- Created by: woodser | 2023-07-17T15:52:46+00:00
- Closed at: 2023-08-17T15:26:33+00:00
