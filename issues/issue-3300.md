---
title: 'Feature Request: Noob-friendly behavior for fork errors'
source_url: https://github.com/monero-project/monero/issues/3300
author: Gingeropolous
assignees: []
labels: []
created_at: '2018-02-21T12:45:07+00:00'
updated_at: '2018-02-21T12:48:38+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Currently, a user running the GUI or the CLI wallet can very easily send monero on a dead chain. E.g., if they forget to update their software, and then make a transaction, the wallet will think everything is fine and try and put a new output on the dead chain.

First, the software should try to prevent this behavior by communicating to the user that they are attempting to spend on a dead chain. Perhaps the wallet can check the daemon and see if the daemon is throwing the "you are past an update" flag, or the "you are probably forked" flag. 

Second, in the wallet, there should be a simple and obvious command that users will recognize as a tool to fix their wallet if they miss an update and send on a dead chain. Apparently these two commands need to be run:

```flush_txpool txid in the daemon```
 ```rescan_spent in the wallet```

I'd propose combining these as one command in the wallet, called "fix_fork_problem", that will execute both the wallet and daemon command. 

# Discussion History
# Action History
- Created by: Gingeropolous | 2018-02-21T12:45:07+00:00
