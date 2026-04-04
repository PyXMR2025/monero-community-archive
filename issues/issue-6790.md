---
title: monero-wallet-cli ignores --max-log-files option
source_url: https://github.com/monero-project/monero/issues/6790
author: garlicgambit
assignees: []
labels: []
created_at: '2020-08-30T17:49:56+00:00'
updated_at: '2020-08-31T18:21:05+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
monero-wallet-cli ignores the `--max-log-files` option. It will keep on creating log files. It also ignores the default maximum of 50 log files.  
  
On monerod log rotation works as expected.

# Discussion History
## garlicgambit | 2020-08-31T18:21:05+00:00
monero-wallet-rpc also ignores the `--max-log-files` option.

# Action History
- Created by: garlicgambit | 2020-08-30T17:49:56+00:00
