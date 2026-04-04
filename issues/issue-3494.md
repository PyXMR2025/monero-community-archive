---
title: Limit ability of old wallets to function with upgraded daemons
source_url: https://github.com/monero-project/monero/issues/3494
author: iamsmooth
assignees: []
labels: []
created_at: '2018-03-24T21:00:39+00:00'
updated_at: '2018-03-24T21:08:40+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
It appears some high volume users (in this case an exchange) continue to use the old wallet despite upgrading the daemon: [reddit discussion](https://www.reddit.com/r/Monero/comments/8659wj/exchanges_still_using_old_selection_bad_selection/dw5qf57/?context=3)

This is a problem because many of the improvements in output selection that help maintain the privacy are wallet-based. Continued use of obsolete wallet implementations increases the susceptibility of the chain to timing and other analysis.

Therefore, we should implementing versioning and reject usage of the old wallet whenever there are significant improvements (as there have been in the past).

# Discussion History
# Action History
- Created by: iamsmooth | 2018-03-24T21:00:39+00:00
