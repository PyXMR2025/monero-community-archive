---
title: 'Monero Tech Meeting #177 - Monday, 2026-07-13, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1422
author: rbrunner7
assignees: []
labels: []
created_at: '2026-07-10T15:23:49+00:00'
updated_at: '2026-07-13T18:19:15+00:00'
type: issue
status: closed
closed_at: '2026-07-13T18:19:15+00:00'
---

# Original Description
Location is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting [here](https://github.com/monero-project/meta/issues/1416).


# Discussion History
## rbrunner7 | 2026-07-13T18:19:15+00:00
````
<rbrunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/1422
<jberman> waves
<sneedlewoods> hi
<rbrunner7> Maybe quite a number of people making holidays :)
<rbrunner7> Anyway, what is there to report from last week?
<sneedlewoods> Again reviews, resolved most smaller review comments from rbrunner on the wallet-rpc PR (thanks for the review), but for the error code issue I need a little more time, and some functional test failures sneaked in from rebasing.
<sneedlewoods> Also made another attempt to rebase "remove cached password from Wallet API" into a single commit (instead of basing onto and depending on #9464 (https://github.com/monero-project/monero/pull/9464) as I did for PR #10232 (https://github.com/monero-project/monero/pull/10232)), with the goal to split things up into smaller independent chunks, not sure if I should force push that into #10232, or rather create a new clean PR.
<rbrunner7> I started to review the "Move RPC wallet server to Wallet API" PR from @sneedlewoods
<rbrunner7> Somehow, GitHub seems to have troubles finding that PR. If I tried with you as the author, it was not among the search results. Strange.
<jberman> me: finalized the next round of upstream FCMP++ integration PR's from audits (unbiased hash to point & ed to wei conversion), and did some digging in collab with @selsta on the still present double spend issue @Rucknium is running into. This PR indicates the latest status on the later: https://github.com/seraphis-migration/monero/pull/433
<sneedlewoods> +1
<jberman> latter*
<sneedlewoods> @rbrunner7: you mean #10819 (https://github.com/monero-project/monero/pull/10819)? for me it shows up normally
<rbrunner7> Hmm. Anyway, found it finally.
<rbrunner7> Looks like we are already through with the reports.
<rbrunner7> I have a small question that crossed my mind, would be interested what you think
<rbrunner7> I think for the Polyseed support in the core software a blog post on GetMonero.org, and a copy of that posted to the Monero subreddit, would be something.
<rbrunner7> After the release, of course.
<jberman> sgtm
<rbrunner7> I think that would be my first blog post there, can't let that chance go past :)
<sneedlewoods> +1
<sneedlewoods> Good idea
<selsta> small advertising from my side for https://github.com/monero-project/monero/pull/10905
<selsta> this fixes a long existing issue with self compiled logs being spammed with exceptions 
<rbrunner7> You mean self-compiled software throwed exceptions so far, but our release software does not?
<selsta> our release software has stack trace disabled in logs
<rbrunner7> Ah, ok
<rbrunner7> Alright. Anything left for this hot summer day? (At least here in Europe ...)
<jberman> selsta: nice
<rbrunner7> Doesn't look like it. So thanks everybody for attending, read you again next week!
<sneedlewoods> Thanks everyone, see you
````


# Action History
- Created by: rbrunner7 | 2026-07-10T15:23:49+00:00
- Closed at: 2026-07-13T18:19:15+00:00
