---
title: monero-wallet-cli ignores --max-log-files option
source_url: https://github.com/monero-project/monero/issues/6790
author: garlicgambit
assignees: []
labels: []
created_at: '2020-08-30T17:49:56+00:00'
updated_at: '2026-07-10T14:47:21+00:00'
type: issue
status: closed
closed_at: '2026-07-10T14:47:21+00:00'
---

# Original Description
monero-wallet-cli ignores the `--max-log-files` option. It will keep on creating log files. It also ignores the default maximum of 50 log files.  
  
On monerod log rotation works as expected.

# Discussion History
## garlicgambit | 2020-08-31T18:21:05+00:00
monero-wallet-rpc also ignores the `--max-log-files` option.

## selsta | 2026-07-10T14:47:21+00:00
Resolved in https://github.com/monero-project/monero/pull/9392

# Action History
- Created by: garlicgambit | 2020-08-30T17:49:56+00:00
- Closed at: 2026-07-10T14:47:21+00:00
