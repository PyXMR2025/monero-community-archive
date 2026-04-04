---
title: 'Feature request: alert on detection of possible "dust" input'
source_url: https://github.com/monero-project/monero/issues/6795
author: OrvilleRed
assignees: []
labels: []
created_at: '2020-09-03T00:35:12+00:00'
updated_at: '2020-09-05T19:49:34+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
While scanning the chain for new txns, take note of any inputs having a value less than some amount, DUST_THRESHOLD
If an input is found with value less than DUST_THRESHOLD, display a warning to the user.

The warning should indicate that a very small amount was received, and that if the user was not expecting such, then this may be a "dust attack" and as such the sender may be trying to watch where the resulting funds are spent.

The message should include a link to a longer description of dust attacks in Monero (possibly to relevant Breaking Monero vids). Ideally, the message should also include a link to a description of how to mitigate such an attack once the "dust" is received.

Related / downstream issue for GUI: https://github.com/monero-project/monero-gui/issues/3065

# Discussion History
## sethforprivacy | 2020-09-05T19:49:33+00:00
My recent issue could be of interest, as one of the proposed goals is to make dusting attacks spendable post-churn:

#6801 

# Action History
- Created by: OrvilleRed | 2020-09-03T00:35:12+00:00
