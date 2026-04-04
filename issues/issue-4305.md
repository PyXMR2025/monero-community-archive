---
title: '[suggestion/request] automatic churn'
source_url: https://github.com/monero-project/monero/issues/4305
author: aeon1234
assignees: []
labels: []
created_at: '2018-08-26T10:35:13+00:00'
updated_at: '2018-09-03T05:53:01+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
it would be nice to have automatic churn in your wallet, so you can run it 24/7 and it does it for you and uses delays which match good distribution.

it could look like this:

`[4ABCD]: churn`
`starting churn`
`[4ABCD]: transfer 4ABCD... 1`
`ERROR: please stop churn before manually using your wallet again.`

and command could look like this:

`churn [index=<N1>[,<N2>,...]] [<priority>]`

# Discussion History
## jtgrassie | 2018-08-26T12:43:08+00:00
Why the need for a churn?

## SamsungGalaxyPlayer | 2018-08-26T15:42:49+00:00
It would be nice at least for the CLI wallet. However, the best process for churning is still debated.

If I had to come up with a primitive technique right now, it would probably include 1) waiting for the output to be included in another transaction as a decoy, 2) waiting a random amount of time between 0.5-3 days, or 3) some combination of the two.

However, I have not tested if this is a good mechanism or not, and I think most mechanisms that people have hypothesized have not been tested yet either.

## aeon1234 | 2018-08-27T13:59:13+00:00
is it possible to use same distribution for new generated tx like #3528 does for decoys?

and in general is it not better to have any (semi perfect) automatic churn algorithm instead of people doing it manually?

## jtgrassie | 2018-08-27T14:11:02+00:00
Sorry to harp on about this but can you please explain _why_ there is a need for churning at all (automatic or manual aside).

## SamsungGalaxyPlayer | 2018-08-27T20:44:43+00:00
@jtgrassie I strongly recommend reading #4229, especially [this comment](https://github.com/monero-project/monero/issues/4229#issuecomment-415139034). Churning increases the entropy set more than a single transaction can provide.

## jtgrassie | 2018-08-27T23:23:06+00:00
@SamsungGalaxyPlayer thanks for the links but that discussion is related to ring-size, not churning. 

EDIT: OK I see what you're getting at. However I think the discussion is more nuanced than this suggestion to simply add an automatic churn. It certainly needs more thought.

## aeon1234 | 2018-08-28T16:49:05+00:00
> It certainly needs more thought.

can you clarify what exactly needs more thought?

people are currently manual churning or are maybe using their own scripts (with more or less good algorithm) for this.
so why not implementing it?

## jtgrassie | 2018-08-28T20:03:25+00:00
If you follow the thread sgp posted, it's not clear cut on the best route. Hence more discussion/thought.

## SamsungGalaxyPlayer | 2018-08-29T01:35:10+00:00
@aeon1234 it's because we currently don't have a good idea what the wallet behavior should be. Once we get a better idea, I agree that it should be added.

## aeon1234 | 2018-08-29T10:43:20+00:00
on the other side you guys from the MRL have way better understanding what to do than most of us users. also a user cannot create a tx at any time of the day, most have to work and sleep eventually. so most manual churns are worse than any algorithm from you, even if this algorithm is not perfect for now. so I hope you do not wait until there is a perfect churn behavior in the future.

## jtgrassie | 2018-08-29T11:23:33+00:00
@aeon1234 the discussion is wider than simply saying churning (any which way) is better than no churning. Fixed ring-size maybe all that's needed, or some kind of churning maybe needed. However, changes need to be grounded in _research_, not assumptions.

## aeon1234 | 2018-08-29T11:55:29+00:00
there are at least some examples in the linked thread #4229 (and also on reddit the last few years) where I understood that churning is needed sometimes. or did I just read this wrong and churning should not/never be done? also `Churning increases the entropy set more than a single transaction can provide.` as SamsungGalaxyPlayer said. my whole issue assumes that there was already consensus that churning is needed sometimes and/or increases privacy. if that's wrong, then I can close this issue.

## jtgrassie | 2018-08-29T12:11:40+00:00
@aeon1234 There is no linked _research_ in that thread regarding churning. You are _assuming_ consensus on churning. If there was solid research there would likely be some consensus, but that is not where we are at now. Most debate has been about ring-size (fixed, size, etc), not churning.

## jtgrassie | 2018-08-29T12:28:03+00:00
> my whole issue assumes that there was already consensus that churning is needed...  if that's wrong...

It's wrong. There is no hard research and no solid consensus. When there is research, there will undoubtedly be some consensus, until then, this kind of suggestion has no merit. If you have done some real research to point to a need for churning or ring-size changes, please add it to your suggestion so it can be debated.

## SamsungGalaxyPlayer | 2018-09-03T05:53:01+00:00
@jtgrassie after being involved in the research meetings, I can confidently state that research points towards churning having a positive or neutral impact in most circumstances, not a negative impact. The only possible negative impact I can think about at the moment is the increased attack surface from potential timing attack heuristics, eg: increasing the number of data points for transactions sent at a certain exact time each day. However, this is exactly something that a wallet feature can mitigate: reducing the feasibility of timing attacks for heuristics we know of. However, as I have stated, these have not been thoroughly defined.

From a strict ring signature perspective, churning increases the number of possible outputs spent in transactions. So, if we can incorporate churning while minimizing the timing and IP address metadata leaked, then it should be a clear win for privacy. However, since we have not defined these, I do not recommend its addition at this time until some heuristics are developed and tested.

In short, research is clearly pointing towards churning having potentially positive effects, but the best way to get these effects is not well-defined. As a result, we shouldn't incorporate this into the wallet yet, since we would need to have these definitions first. However, once we have a better idea, it should clearly be added.

# Action History
- Created by: aeon1234 | 2018-08-26T10:35:13+00:00
