---
title: '[Feature Request] Low bandwidth mode'
source_url: https://github.com/monero-project/monero-gui/issues/708
author: Gingeropolous
assignees: []
labels:
- feature
created_at: '2017-05-03T22:07:49+00:00'
updated_at: '2017-08-09T13:30:09+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Somewhere in settings, it would be nice to have a button to switch on "Low Bandwidth Mode" for people that have data caps or whatever.

What that button does is another story. It could either limit the download / upload rates, or it could just select a random node to exclusively peer to, or it could opt out of providing synchronization to the network, so it just stays updated with the blockchain, but doesn't do any relaying. 

# Discussion History
## Gingeropolous | 2017-05-03T22:11:03+00:00
this would address user concerns (no idea where they came from) like this: https://www.reddit.com/r/Silverbugs/comments/691lsg/litecoin_has_overtaken_silver/dh3ae0l/

## SamsungGalaxyPlayer | 2017-05-06T11:25:53+00:00
I'd suggest completely turning off incoming connections with this mode. I think the target should be less than 100GB/month, so perhaps limit outgoing connection speeds to 300kbps. Then, there is no way Monero will use more than 100GB/month.

Alternatively, this can be reduced to less than 50GB/month with a 150kbps limit, or 75GB/month with a 230kbps limit. This assumes the bandwidth is capped 24/7, which is unrealistic.

I'm afraid the initial synchronization will take forever with these methods, so perhaps they should only limit the speed when the blockchain is over 95% synchronized? I haven't tried syncing from scratch on such a poor connection before.

## dEBRUYNE-1 | 2017-08-09T13:25:39+00:00
+feature

# Action History
- Created by: Gingeropolous | 2017-05-03T22:07:49+00:00
