---
title: Monero dev meeting summary 20160305
source_url: https://github.com/monero-project/monero-site/issues/111
author: Gingeropolous
assignees: []
labels: []
created_at: '2016-03-16T02:38:07+00:00'
updated_at: '2017-10-20T22:13:39+00:00'
type: issue
status: closed
closed_at: '2017-08-31T09:25:16+00:00'
---

# Original Description
Open pull requests mostly just DB stuff by warptangent and hyc, and will be merged within next couple of hours. In the last couple of weeks, unit test fixes, threading fixes, "lots of little things". Hyc had some readtxn changes. Hyc's performance changes need to wait until some kind of migration system is implemented / developed. 

Fees are fine. Too soon for adjustment. Talk of "magic number automation" - fees will autoadjust one day! ArcticMine takes on researching / developing a proposal for automatically adjusting fees. 

Dev Branch - the buck stops here. Moneromoo is waiting for 0.9.2 to be tagged "so that no new patches go there". So once we have 0.9.2, dev branch goes upstream (to master).

We need a library that plays well with HTTPS and support authentication and is compatible with our license. 

RingCT - WarpTangent becoming familiar with what needs to be done, and RingCT development will go on newer database branch. There's some "floating point or fixed" issue that needs to be decided. Forum threads will be opened for that. Warptanget steps up to the plate to make the thread. 

Changing mixin to something else is a thing that might happen, but "its a community thing, not a dev thing"

Everybody shakes hands, gives themselves pats on the back and "attaboys", and venture off into the night to go meditate on the metaphysics of mixin 0 transactions. 


# Discussion History
## rehrar | 2017-07-11T20:00:15+00:00
@Gingeropolous Does this need to still be open?

# Action History
- Created by: Gingeropolous | 2016-03-16T02:38:07+00:00
- Closed at: 2017-08-31T09:25:16+00:00
