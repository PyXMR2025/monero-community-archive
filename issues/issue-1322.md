---
title: 'Monero Tech Meeting #153 - Monday, 2026-01-12, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1322
author: rbrunner7
assignees: []
labels: []
created_at: '2026-01-09T16:04:29+00:00'
updated_at: '2026-01-12T18:35:36+00:00'
type: issue
status: closed
closed_at: '2026-01-12T18:35:36+00:00'
---

# Original Description
Location is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting [here](https://github.com/monero-project/meta/issues/1319).


# Discussion History
## rbrunner7 | 2026-01-12T18:35:36+00:00
````
<r​brunner7> Meeting in 1 hour
<r​brunner7> Meeting time. Hello! monero-project/meta #1322
<j​effro256> Howdy
<j​berman> *waves*
<s​needlewoods> Hello
<r​brunner7> Alright, let's start with the reports from last week
<v​tnerd> Hi
<s​needlewoods> mainly worked on vtnerds review comments [here](monero-project/monero #10232#pullrequestreview-3623648856)
<s​needlewoods> also updated #9464 and left a comment monero-project/monero #9464#issuecomment-3724414260
<v​tnerd> Me: no tangible updates on lws/lwsf, working on something unrelated
<s​needlewoods> and created a new branch for "replace wallet2 with Wallet API in `monero-wallet-rpc`" (but not much happened on it)
<r​brunner7> That work just got financed, right? Nice.
<s​needlewoods> Yes, huge thanks to all supporters and donors
<j​berman> me: we released v1.5 of the alpha stressnet (seems to be holding up reasonably well), completed a solution for the xmrig segfault (upstream PR incoming), 0xfffc merged my tx relay v2 changes into his branch (thank you!), we may be in solid shape for beta soon
<sneedlewoods> +1
<r​brunner7> Any news about any ongoing Carrot related reviews, jeffro256 ?
<j​effro256> Me: I'm working on implementing the scaling changes for beta stressnet
<j​effro256> On of the firms reached out to maybe perform a partial or full audit of carrot_core, which would be awesome. I won't mention it more until they commit
<r​brunner7> Changes designed to trigger effects earlier, as discussed recently? Different from the "real" Mainnet scaling parameters
<r​brunner7> Anyway. I have something that may make sense to discuss in this round, maybe enough "brains" currently present to make sense
<r​brunner7> Recently I glanced over vtnerd 's review of the expanded Wallet API, as an API, where some mention of `monero_c` got me thinking
<j​berman> ( believe the latter, the "real" mainnet scaling params)
<r​brunner7> If I am not mistaken, it's about this one: github.com/MrCyjaneK/monero_c
<r​brunner7> I think it was some question about compatibility of the new Wallet API release with a "C only" wrapper, regarding callbacks?
<j​effro256> For free btw
<r​brunner7> Which leads me to the question: Is it our responsibility, while modifying and expanding the Wallet API, to make such C based wrappers not unnecessarily hard and complicated, or is this out of scope, so to say?
<s​needlewoods> the comment for reference monero-project/monero #10232#discussion_r2658678511
<r​brunner7> Thanks, sneedlewoods, exactly that :)
<r​brunner7> But there may be other possible pain points
<s​needlewoods> I don't know much about monero_c, but AFAIK it's important enough that we should not break it
<v​tnerd> Yes the monero_c code doesn't support listeners as it's a bit messy to support. So the password change for listeners hopefully won't be required for API users or monero _c has a bunch of work (and so does dart bindings et al)
<r​brunner7> I was mistaken, I first thought it is still based directly on wallet2 ...
<v​tnerd> Monero_c is used by cake afaik
<j​berman> +1 to keeping the C wrapper in mind
<j​berman> and therefore +1 to avoid required callbacks
<v​tnerd> Skylight definitely is too
<r​brunner7> Ah, so you can get everything running with ignoring callbacks entirely?
<s​needlewoods> That's all related to `unattended` setting, iamamyth also left a comment I need to dig into monero-project/monero #10232#discussion_r2674328535
<r​brunner7> Was wondering about that "unattended"
<v​tnerd> Currently, yes. But needed SNeedlewoods @sneedlewoods: to respond about newer changes as I haven't gone through the implementation, primarily just went through the API which is still pretty lengthy
<v​tnerd> Currently yes -> listeners are not required
<s​needlewoods> AFAICT they're still not required if you keep `unattended = true` as it was the default before, but have to double check
<rbrunner7> +1
<v​tnerd> Ah ok, will have to go back through and verify all of this then
<r​brunner7> By the way, is the author "MrCyjaneK" active around here, in the Matrix rooms and/or on IRC? Maybe it would be good for them to have a look what we are up to here ...
<r​brunner7> Easier to correct / adjust things now than later
<v​tnerd> I would tag them on GitHub, they've commented on something I've done before
<r​brunner7> Maybe even ready to help reviewing, who knows
<r​brunner7> So things are probably safe. Good to hear.
<r​brunner7> Anything else to discuss today?
<s​needlewoods> Not from me, will post updates on the PRs or in here during the week when I figured things out+
<r​brunner7> Well then. Thanks everybody for attending, read you again next week!
<jberman> thanks
<sneedlewoods> thanks everyone, see ya
````


# Action History
- Created by: rbrunner7 | 2026-01-09T16:04:29+00:00
- Closed at: 2026-01-12T18:35:36+00:00
