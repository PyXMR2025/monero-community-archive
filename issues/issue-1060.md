---
title: '[Feature Request] Option to split transaction fees between miners and developers'
source_url: https://github.com/monero-project/monero/issues/1060
author: ghost
assignees: []
labels: []
created_at: '2016-09-08T16:14:17+00:00'
updated_at: '2016-09-30T00:21:01+00:00'
type: issue
status: closed
closed_at: '2016-09-30T00:21:01+00:00'
---

# Original Description
How about a flag in the wallet that allows us to send 50% of our transaction fee to the miners and 50% to a fixed address to fund development. It could be explicitly introduced in hard fork X, and deactivated again in hard fork Y a year later.


# Discussion History
## perl5577 | 2016-09-08T18:59:26+00:00
is beautifull idea. 
Is it motivating for the dev to reduce costs transaction ?


## ghost | 2016-09-08T20:48:25+00:00
Well I think the next step is to make transaction fees float rather than fixed, so it shouldn't change that incentive. They don't get a split at the moment so the financial incentive to keep the fees static doesn't exist. 


## moneromooo-monero | 2016-09-16T19:57:13+00:00
It'd increase the tx size by a fair bit (50% more outputs on average).


## ghost | 2016-09-20T22:21:21+00:00
That's a shame. Is there any way that this would be possible in a post-RingCT world?


## ghost | 2016-09-30T00:21:01+00:00
Closing to increase the signal to noise ratio


# Action History
- Created by: ghost | 2016-09-08T16:14:17+00:00
- Closed at: 2016-09-30T00:21:01+00:00
