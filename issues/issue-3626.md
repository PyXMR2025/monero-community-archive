---
title: 'Suggestion: start_mining should que if daemon is busy'
source_url: https://github.com/monero-project/monero/issues/3626
author: ghost
assignees: []
labels: []
created_at: '2018-04-12T20:52:22+00:00'
updated_at: '2018-10-12T20:30:11+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
instead of spitting an error (Error: Mining did not start -- BUSY) it would be helpfull for automation purposes if the start_mining command was accepted without error and would initiate when the daemon is ready to start mining.

Would save me creating a custom Shell script with a grep loop to detect when the daemon is ready for the start_mining command before actually sending it.

# Discussion History
## moneromooo-monero | 2018-10-12T20:30:11+00:00
If you want to mine when not busy, then you can use the --bg-mining\* options.

# Action History
- Created by: ghost | 2018-04-12T20:52:22+00:00
