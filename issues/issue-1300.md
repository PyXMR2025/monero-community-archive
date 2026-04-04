---
title: 'Monero Tech Meeting #147 - Monday, 2025-11-24, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1300
author: rbrunner7
assignees: []
labels: []
created_at: '2025-11-21T15:59:55+00:00'
updated_at: '2025-11-24T18:20:37+00:00'
type: issue
status: closed
closed_at: '2025-11-24T18:20:37+00:00'
---

# Original Description
Location is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting [here](https://github.com/monero-project/meta/issues/1297).


# Discussion History
## rbrunner7 | 2025-11-24T18:20:37+00:00
````
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/1300
<s​needlewoods> hey
<r​brunner7> Seems people are preparing already for Black Friday :)
<r​brunner7> Ok, anyway, anything to report?
<s​needlewoods> made/updated the PRs [updated Wallet API](https://github.com/monero-project/monero/pull/9464), [remove cached password](https://github.com/monero-project/monero/pull/10232) and [replace wallet2 with Wallet API in CLI](https://github.com/monero-project/monero/pull/10233)
<s​needlewoods> There are still a few bugs in #10233, most noteworthy ones I mention in that PR, but there are also small things like the following, where I would like to match the old behavior:
<s​needlewoods> - old wallet-cli prints tx-ids and enote pub keys surrounded by "<>" in some places (e.g. `incoming_transfers`)
<s​needlewoods> and I'm a little worried I messed something up, so will keep testing and updating
<r​brunner7> So a bit too early to start with reviews?
<j​berman> hi sorry
<s​needlewoods> testers and reviewers are already welcome, but I'll notice when I find no more bugs
<r​brunner7> Yeah, I think for the CLI wallet we don't only need code reviews, but also people testing everything. Many things could possibly break.
<s​needlewoods> s/notice/announce
<j​berman> me: mainly worked on getting out a preliminary v1.5 stressnet build that people could test that hopefully solves OOM's. OOM's caused by FCMP++ verification do some mitigated, but there are still some issues to work on. Apparently there is an issue causing sync failures that needs further investigation: https://github.com/seraphis-migration/monero/issues/244
<r​brunner7> I use to quip that if the bugs get more mysterious, that's a good sign for real progress :)
<r​brunner7> It must be the most things waiting for funding for quite some time: https://ccs.getmonero.org/funding-required/
<r​brunner7> jeffro currently with a solid lead.
<sneedlewoods> +1
<r​brunner7> Alright, with everything moving along smoothly, do we have something to discuss today beyond these reports?
<s​needlewoods> I don't have anything else
<j​effro256> Howdy sorry I'm late
<j​effro256> Not much to report , but I'm preparing  to organize an audit of the carrot core library, will post more details in the MRL meeting probably
<r​brunner7> That will be a code audit?
<r​brunner7> Must be
<j​effro256> Yea
<r​brunner7> Nice.
<r​brunner7> Alright, looks like we are through already for today. Thanks everybody for attending. Read you again next week, being December already.
<sneedlewoods> thanks
````



# Action History
- Created by: rbrunner7 | 2025-11-21T15:59:55+00:00
- Closed at: 2025-11-24T18:20:37+00:00
