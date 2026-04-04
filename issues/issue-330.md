---
title: 'Research meeting: 15 April 2019 @ 17:00 UTC'
source_url: https://github.com/monero-project/meta/issues/330
author: SarangNoether
assignees: []
labels: []
created_at: '2019-04-13T19:19:14+00:00'
updated_at: '2019-04-15T17:27:42+00:00'
type: issue
status: closed
closed_at: '2019-04-15T17:27:42+00:00'
---

# Original Description
Join in for the weekly Monero Research Lab meeting.

**When**: Monday, 15 April 2019 @ 17:00 UTC
**Where**: #monero-research-lab (freenode/matrix)

**Agenda**
1. Greetings

2. Roundtable
a. Sarang: [Lelantus](https://eprint.iacr.org/2019/373) transaction flow [code](https://github.com/SarangNoether/skunkworks/tree/lelantus/lelantus), CLSAG [updated code](https://github.com/SarangNoether/skunkworks/tree/clsag/hashes)
b. Surae
c. Others?

3. Questions

4. Action items

# Discussion History
## SarangNoether | 2019-04-15T17:27:42+00:00
    [2019-04-15 12:59:14] * sarang set the topic to Research meeting NOW: https://github.com/monero-project/meta/issues/330. Be excellent to each other.
    [2019-04-15 12:59:33] <sarang> Let's begin our meeting!
    [2019-04-15 12:59:36] ⇐ cardboardoranges quit (~cardboard@65.112.8.13): Quit: cardboardoranges
    [2019-04-15 12:59:38] <sarang> 1. GREETINGS
    [2019-04-15 12:59:41] <sarang> Hi
    [2019-04-15 12:59:44] <[-mugatu-]> o/
    [2019-04-15 13:00:40] <sarang> Quiet day today...
    [2019-04-15 13:00:51] <sarang> But I suppose we can still move to 2. ROUNDTABLE
    [2019-04-15 13:00:57] <sarang> suraeNoether: care to go first today?
    [2019-04-15 13:01:18] <suraeNoether> sure, my cat is missing and i want to go look for her, so i'm going to make this quick
    [2019-04-15 13:01:23] <sarang> :(
    [2019-04-15 13:01:26] <sarang> Understood
    [2019-04-15 13:01:53] <suraeNoether> CLSAG signatures are fast and small, they are so fast and small that my naive colored-coin approach could support two assets and still be faster and smaller than our present MLSAG scheme
    [2019-04-15 13:02:06] <suraeNoether> i'm not recommending coloring monero, but commenting on overall speed, it's nuts
    [2019-04-15 13:02:16] <suraeNoether> however, as sarang mentioned, there is a key image problem i'm looking into
    [2019-04-15 13:02:27] <suraeNoether> it's possible rectifying them will cost us some of those gains
    [2019-04-15 13:02:37] <sarang> Yeah, I don't think a straightforward LSAG reduction works here
    [2019-04-15 13:02:49] <suraeNoether> in the meantime, i'm handing CLSAG off to sarang for at least 7 days so i can focus on MRL11
    [2019-04-15 13:03:04] <sarang> But I wonder if a redefinition of the security requirements to accommodate the new linking will be sufficient
    [2019-04-15 13:03:18] <suraeNoether> since we're rounding the corner on that, it's my top priority, and i want to get CLSAG out of sight for a few days
    [2019-04-15 13:03:26] <sarang> righto
    [2019-04-15 13:03:40] <suraeNoether> okay, i'll be back later today, hopefully with suraecat
    [2019-04-15 13:03:57] <sarang> Thanks, and best of luck with your search
    [2019-04-15 13:04:34] <sarang> I completed the building blocks for a simple Lelantus transaction flow (insecure example code in agenda)
    [2019-04-15 13:04:52] <sarang> and am in contact with the paper's author to discuss some privacy aspects of the construction
    [2019-04-15 13:05:02] <sarang> the CLSAG example code has been updated to reflect some changes
    [2019-04-15 13:05:13] <sarang> and, as suraeNoether said, still working on proper formalization, which is trickier than expected
    [2019-04-15 13:06:07] <sarang> The output selection algorithm discussed here still has an open PR from moneromooo that needs eyeballs
    [2019-04-15 13:06:15] <sarang> PR 5389
    [2019-04-15 13:06:42] <needmoney90> Hi
    [2019-04-15 13:06:45] <sarang> yo
    [2019-04-15 13:06:50] <needmoney90> Will lurk mostly.
    [2019-04-15 13:07:00] <sarang> Does anyone else have research to share?
    [2019-04-15 13:07:01] <needmoney90> Just announcing presence
    [2019-04-15 13:07:24] <sarang> Otherwise we can keep waxing poetic about CLSAG definitions
    [2019-04-15 13:07:25] <sgp_> here now
    [2019-04-15 13:07:26] <sarang> :/
    [2019-04-15 13:07:28] <sarang> Hi suraeNoether 
    [2019-04-15 13:07:30] <sarang> sgp_: 
    [2019-04-15 13:07:35] <sarang> bah, silly autocomplete
    [2019-04-15 13:07:52] <moneromooo> I have these multi user txes going in the background, and I am wondering whether the 'a' values can be reuesd for multiple outputs.
    [2019-04-15 13:08:17] <sarang> Remind me what these values are/
    [2019-04-15 13:08:19] <needmoney90> What's the status on M-of-N multisig?
    [2019-04-15 13:08:25] <sarang> (our notation is often inconsistent)
    [2019-04-15 13:08:25] <moneromooo> The idea is to make 16 actual outs for the "same" logical output, so they get shuffled as new outputs are added.
    [2019-04-15 13:08:51] <moneromooo> And I don't know whether it's safe to keep those. I assume sharing them with other usesr of the same tx is not good.
    [2019-04-15 13:09:04] <dEBRUYNE> <suraeNoether> however, as sarang mentioned, there is a key image problem i'm looking into <= This is referring to CSLAG right?
    [2019-04-15 13:09:20] <sarang> dEBRUYNE: yes
    [2019-04-15 13:09:26] <sarang> there are no such issues with MLSAG
    [2019-04-15 13:09:37] — xmrmatterbridge <oneiric> lurks
    [2019-04-15 13:09:42] <dEBRUYNE> All right, thanks for clarifying
    [2019-04-15 13:09:48] <sarang> The problem refers to the fact that trying to reduce CLSAG to LSAG with an aggregated key yields the wrong key image
    [2019-04-15 13:09:51] <moneromooo> a is the random secret keys generated at proive time to create the pseudoOuts.
    [2019-04-15 13:09:59] <sarang> Hmm ok
    [2019-04-15 13:12:46] <sarang> You asked me to review this earlier, and it completely slipped my mind
    [2019-04-15 13:13:12] <sarang> I'll look for the code snippet you sent in PM
    [2019-04-15 13:13:28] <sarang> to ensure I don't get wrong the terms you're referring to
    [2019-04-15 13:13:51] <moneromooo> ty
    [2019-04-15 13:14:37] <sarang> sgp_: did you have something you wished to discuss too?
    [2019-04-15 13:15:00] <sgp_> I don't believe so
    [2019-04-15 13:15:21] <sarang> Well, this meeting is turning out to be quite short :D
    [2019-04-15 13:15:43] <sarang> moneromooo: anything specific, aside from the reuse question you posed?
    [2019-04-15 13:15:52] <sarang> (to discuss here, I mean)
    [2019-04-15 13:16:23] <moneromooo> Not at the moment I think.
    [2019-04-15 13:16:33] <sarang> OK, I suppose we can move right along then
    [2019-04-15 13:16:44] <sarang> to 3. QUESTIONS and 4. ACTION ITEMS
    [2019-04-15 13:16:58] <sarang> While suraeNoether continues working on matching/churn via MRL-0011, I have several things for the week
    [2019-04-15 13:17:31] <sarang> Now that CLSAG reduction to LSAG is proving so problematic, I want to see if definition modifications for the LSAG proofs will suffice for our use case
    [2019-04-15 13:17:59] <sarang> I'll be checking on moneromooo's question shortly (apologies for letting that slip by)
    [2019-04-15 13:18:20] <sarang> as well as more work on Lelantus transaction flows
    [2019-04-15 13:18:27] <dEBRUYNE> sarang: Have you consulted RandomRun regarding this problem btw?
    [2019-04-15 13:18:52] <sarang> suraeNoether and I have been in contact with him throughout the development process
    [2019-04-15 13:19:39] <sarang> I don't believe this problem has practical effects on CLSAG's security, only in the complexity of the formalization
    [2019-04-15 13:20:22] <sarang> Any other questions or action items on people's minds?
    [2019-04-15 13:20:30] <dEBRUYNE> I see, so it does not render the scheme infeasible?
    [2019-04-15 13:20:39] <sarang> Heh, depends
    [2019-04-15 13:20:50] <sarang> If we end up not being able to prove secure under proper definitions, that's a bit of a quandry
    [2019-04-15 13:21:43] <sarang> but in the worst case, we decide not to adopt the scheme, and are right back to where we are now
    [2019-04-15 13:22:06] <dEBRUYNE> True, better safe than sorry I guess :p
    [2019-04-15 13:22:48] <sarang> However, the space and time savings are so compelling that it's worth the effort
    [2019-04-15 13:23:03] <sarang> ~25% space savings and 15% time savings for a 2-2 transaction
    [2019-04-15 13:23:07] <sarang> (in the signature portion)
    [2019-04-15 13:23:19] <needmoney90> Not bad
    [2019-04-15 13:24:16] <sarang> OK, any last questions before we formally adjourn?
    [2019-04-15 13:25:16] <sarang> Righto, in that case, we are adjourned. Discussion can of course continue
    [2019-04-15 13:25:23] <sarang> Logs will be posted shortly to the GitHub agenda issue
    [2019-04-15 13:25:36] * sarang set the topic to Research meeting Mondays @ 17:00 UTC. Be excellent to each other.

# Action History
- Created by: SarangNoether | 2019-04-13T19:19:14+00:00
- Closed at: 2019-04-15T17:27:42+00:00
