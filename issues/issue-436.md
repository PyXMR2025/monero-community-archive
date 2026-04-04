---
title: Change default log level to avoid exposing public address and txids
source_url: https://github.com/monero-project/monero-gui/issues/436
author: monerohow
assignees: []
labels: []
created_at: '2017-01-23T20:42:49+00:00'
updated_at: '2017-01-28T14:42:46+00:00'
type: issue
status: closed
closed_at: '2017-01-28T14:42:46+00:00'
---

# Original Description
Request: change default log level for CLI wallet so that no logs are written unless otherwise specified.

Some users don't have encrypted file storage (either because they have unencrypted hard drives, or use unencrypted online backup, or keep their files on company/university storage which other people can inspect, or keep their wallet on an unencrypted flash drive).

For these people, it'd be useful if the CLI wallet did not log to disk by default, so that they can rely completely on the encryption provided by the wallet password. Otherwise, their public address and txids are exposed in the log file if anyone gets access to the location of their wallet.

# Discussion History
## moneromooo-monero | 2017-01-28T11:03:40+00:00
Can you refile this on https://github.com/monero-project/monero/issues/ please ?

## monerohow | 2017-01-28T14:42:46+00:00
Done

# Action History
- Created by: monerohow | 2017-01-23T20:42:49+00:00
- Closed at: 2017-01-28T14:42:46+00:00
