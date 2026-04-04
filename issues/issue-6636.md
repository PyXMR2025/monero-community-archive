---
title: Minor enhancement request - better console feedback
source_url: https://github.com/monero-project/monero/issues/6636
author: ronohara
assignees: []
labels: []
created_at: '2020-06-09T07:21:31+00:00'
updated_at: '2020-06-09T07:22:17+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
'Nitrogen Nebula' (v0.16.0.0-release)

2020-06-09 05:41:24.142	I SYNCHRONIZED OK
2020-06-09 05:41:24.143	I SYNCHRONIZED OK

The mode is running fine and these console message get displayed, but unless you increase the log_level or start a wallet, the message is not helpful as to the block height changes. This message only occurs at modest intervals so flooding of the console or log is not an issue.

Adding a trailing (current) block height would be more informative

For example.

2020-06-09 05:41:24.142	I SYNCHRONIZED OK 2112646
2020-06-09 05:41:24.143	I SYNCHRONIZED OK 2112666



# Discussion History
# Action History
- Created by: ronohara | 2020-06-09T07:21:31+00:00
