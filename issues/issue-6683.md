---
title: Unexpected behavior on rate limit flags
source_url: https://github.com/monero-project/monero/issues/6683
author: MoneroArbo
assignees: []
labels: []
created_at: '2020-06-22T11:44:40+00:00'
updated_at: '2020-06-22T11:44:40+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Expected behavior: Setting --limit-rate-down or --limit-rate-up to -1 makes the rate unlimited

Actual behavior: Setting --limit-rate-down or --limit-rate up sets bandwidth limits to the defaults of 2048 / 8196.

The value -1 mapping to the default, limited positive number values of 2048 & 8196 is inconsistent with how the  --in-peers and --out-peers flags work, not to mention inconsistent with other software where -1 typically represents the "unlimited" value.

# Discussion History
# Action History
- Created by: MoneroArbo | 2020-06-22T11:44:40+00:00
