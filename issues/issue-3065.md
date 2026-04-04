---
title: 'Feature request: alert on detection of possible "dust" input'
source_url: https://github.com/monero-project/monero-gui/issues/3065
author: OrvilleRed
assignees: []
labels: []
created_at: '2020-09-02T17:46:04+00:00'
updated_at: '2020-09-02T23:23:58+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
While scanning the chain for new txns, take note of any inputs having a value less than some amount, DUST_THRESHOLD
If an input is found with value less than DUST_THRESHOLD, display a warning to the user.

The warning should indicate that a very small amount was received, and that if the user was not expecting such, then this may be a "dust attack" and as such the sender may be trying to watch where the resulting funds are spent.

The message should include a link to a longer description of dust attacks in Monero (possibly to relevant Breaking Monero vids). Ideally, the message should also include a link to a description of how to mitigate such an attack once the "dust" is received.

# Discussion History
## selsta | 2020-09-02T23:23:25+00:00
Can you open this on monero repo? https://github.com/monero-project/monero/issues/new

This has to get implemented into CLI first.

# Action History
- Created by: OrvilleRed | 2020-09-02T17:46:04+00:00
