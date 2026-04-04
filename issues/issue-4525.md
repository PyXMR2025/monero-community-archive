---
title: Proposal - keep version compatibility connected to fork heights
source_url: https://github.com/monero-project/monero/issues/4525
author: Gingeropolous
assignees: []
labels: []
created_at: '2018-10-08T14:10:58+00:00'
updated_at: '2018-10-08T14:17:01+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
This is in regards to the fact that the current release cycle is breaking the public remote node system. Node operators that donate their nodes are upgrading to v0.13, but users continue to use wallets based on 0.12.x wallet code. There is an incompatibility that doesn't make sense. Perhaps there is a good reason for this, and perhaps remote nodes are evil and the fact that this breaks them is good. But apparently 10k monerujo app users don't think they are evil. Or whatever their stats are.

In general, I think the continually forking nature of the monero network would benefit from all versioning being tied to the actually protocol changes. I.e., if you have a 0.12.x wallet and a 0.13.x daemon, the daemon will treat the 0.12.x wallet as valid until the daemon passes the fork height. 

We can't control when people will upgrade in preparation for forks, but we do know for sure that people should use upgraded software after the forks. 



# Discussion History
# Action History
- Created by: Gingeropolous | 2018-10-08T14:10:58+00:00
