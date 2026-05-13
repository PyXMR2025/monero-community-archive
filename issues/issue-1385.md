---
title: 'Monero Tech Meeting #169 - Monday, 2026-05-11, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1385
author: rbrunner7
assignees: []
labels: []
created_at: '2026-05-08T19:06:33+00:00'
updated_at: '2026-05-11T18:41:31+00:00'
type: issue
status: closed
closed_at: '2026-05-11T18:41:31+00:00'
---

# Original Description
Location is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting [here](https://github.com/monero-project/meta/issues/1382).


# Discussion History
## rbrunner7 | 2026-05-11T18:41:31+00:00
````
<rbrunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/1385
<jpk68> Hello
<jberman> waves
<koe000> Hi
<vtnerd> Hi
<rbrunner7> Alright, on to the reports about last week. Me: Made some more progress with Polyseed, and got a problem explained with Polyseed based background wallets that I will soon start to investigate
<koe000> Me: multisig wip, might have a PR this week or next if things go well
<jberman> +1
<jbabb> +1
<jpk68> +1
<jpk68> Made several random patches to the daemon and GUI; made more progress on I2P work (which I would consider to be mostly done). Just have to fix a few bugs/issues and then it
<rbrunner7> Cool, @koe000 !
<jpk68> *and then it's time for testing :)
<koe000> The multisig stuff is on top of jeffro’s hotcold branch so merging will take a while.
<jberman> stressnet fun, fixed an RPC serialization issue reported and diagnosed by @redsh4de, moving towards looking into recently reported issues
<rbrunner7> Stressnet had a good start, from what I am reading in the room, right? Compared with all the bad things that could have happened :)
<jberman> I'd say so. The current bugs I think are either simple to solve or known/understood. There was a mega deep reorg over the weekend that caused issues and I think I know why, and am looking into it now
<rbrunner7> Mega deep? Hundreds of blocks or so?
<koe000> jberman: I think we need a timeline/plan for merging to the Monero repo, otherwise there will be a crunch/delays. eg carrot_core is just sitting and gtg afaik.
<jberman> 200 blocks I think
<selsta> i'm currently trying to get our open PR list lower on the monero repo, if something is ready please ping me
<selsta> smaller
<selsta> will check carrot_core PR
<jberman> I figured the hot/cold wallet impl might have an impact on carrot_core too, which is nearing completion 
<jberman> but actually looks like not
<koe000> Can make smaller follow-ups I imagine. The no-squashing rule means modified large prs are annoying to validate.
<jberman> I agree @koe000. On FCMP++ stuff, I've been thinking I would begin to set up the PR's for the follow-up phases, and tbh would love to have the architecture of those PR's reviewed before audits (e.g. of the tree building approach). I think that would be nice to avoid bad audit
<koe000> +1
<jberman> Beta is kind of getting a little in the way of things / makes it a little hard to make progress on review front, but I do generally think it would be good to get moving on upstream PR's sooner rather than later
<rbrunner7> What is the "no-squashing rule"? Something that you follow in the FCMP++ repo?
<jberman> I can discuss a more concrete plan for FCMP++ stuff, and when @jeffro256:monero.social is available I think it would be good for him to lay out a plan for Carrot
<koe000> rbrunner7: Monero repo merged PRs need one reviewed commit each. The maintainer can’t squash and the author can’t submit multiple commits.
<selsta> it's not a strict rule but it depends, like fixup should be squashed
<rbrunner7> Maybe I misunderstood. You mean you have to squash to always arrive at a single commit per PR?
<jberman> I can shoot to have all the PR's for the FCMP++ integration opened within 2 weeks, we get architecture reviewed on those PR's within 2 weeks after that, then we have those PR's audited. That should cover the timeline for when we finish with Audit Phase 1. So within 4-6 weeks, I'd say we aim to get Phase 1 PR's merged as well
<selsta> there are cases where multiple commits in a single PR can make sense if they build upon each other
<tobtoht> +1
<koe000> +1
<jberman> And Phases 2 & 3 PR's have architecture reviewed within that period as well
<jberman> Then Phases 2 & 3 audits, and PR's fully reviewed after each round of audits
<jberman> How does that sound?
<koe000> +1
<rbrunner7> Who is expected to do "architecure reviews"?
<rbrunner7> *architecture reviews
<koe000> Be sure to ping me if you want my review on something.
<jberman> +1
<jberman> koe jeffro vtnerd are good candidates I'd say
<jberman> very nice to have you back koe :D
<koe000> +1
<rbrunner7> Ah, I see, "our people", not externs mostly
<selsta> carrot_core depends on multiple PRs that require an audit before merging
<jberman> good news is that audit has begun! :D
<jberman> estimated completion date of 2 weeks + corrections round
<rbrunner7> Nice.
<rbrunner7> Alright, looks like we got FCMP++ work covered. Something else to discuss today?
<jpk68> Would the I2P stuff be fine to mention here?
<rbrunner7> Think so, yes.
<jpk68> Great, thanks. If anyone is interested, it would be super useful to have some feedback on general implementation details, though it isn't urgent of course
<rbrunner7> Where can we see that, in order to get able to give you feedback?
<jpk68> In terms of how it's supposed to integrate into the daemon (like how SOCKS does), I am not super experienced with that, so others might have opinions on it
<jpk68> rbrunner7: The two PRs are currently mirrored on GH by ofrnxmr
<jpk68> #10523 and #10458
<ofrnxmr> https://github.com/monero-project/monero/pull/10523
<jpk68> Comments can be left on GitHub or Matrix, and I will try to respond on Matrix
<rbrunner7> I get it that GitHub is out of reach for you personally?
<jpk68> Yes, it is right now, haha
<jpk68> I am still trying to get that solved
<rbrunner7> Ok, no problem, just good to know
<jpk68> +1
<tobtoht> I would like to gauge support for (finally) removing RPC payments. I resubmitted jeffro's removal PR from three years ago here: https://github.com/monero-project/monero/pull/10578
<rbrunner7> Ok, let's see whether somebody comes around to comment. Probably not me, unfortunately, that's too far from my areas of knowledge ...
<jpk68> No problem, thanks anyways :)
<rbrunner7> Ah, yes, the daemon side is still there, right? Just the wallet code was removed until now.
<tobtoht> Correct
<rbrunner7> Well, that gets a +1 from me. Unfortunate story that this feature did not get used, but it is like it is.
<ofrnxmr> Wasnt that program "primo" using it (but dead, i guess)
<rbrunner7> Yeah, gosts from the past still wandering around :)
<rbrunner7> Will leave a comment at the PR
<tobtoht> +1
<ofrnxmr> https://github.com/selene-kovri/primo
<rbrunner7> 7 years ago, oh my. I feel old.
<rbrunner7> Ok. Looks like we are through now. Thanks everybody for attending, read you again next week!
<jpk68> +1
````


# Action History
- Created by: rbrunner7 | 2026-05-08T19:06:33+00:00
- Closed at: 2026-05-11T18:41:31+00:00
