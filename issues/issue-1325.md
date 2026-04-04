---
title: 'Monero Tech Meeting #154 - Monday, 2026-01-19, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1325
author: rbrunner7
assignees: []
labels: []
created_at: '2026-01-17T19:15:17+00:00'
updated_at: '2026-01-19T19:31:10+00:00'
type: issue
status: closed
closed_at: '2026-01-19T19:31:10+00:00'
---

# Original Description
Location is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting [here](https://github.com/monero-project/meta/issues/1322).


# Discussion History
## rbrunner7 | 2026-01-19T19:31:10+00:00
````
<r​brunner7> Meeting time. Hello! monero-project/meta #1325
<s​needlewoods> Hey
<j​berman> *waves*
<r​brunner7> Alright, let's start already with the reports from last week
<s​needlewoods> worked a little more on vtnerds review comments, let me know if I missed to address something
<s​needlewoods> and almost done with rbrunners review of #10233
<r​brunner7> Will you comment my review comments "en masse" then? I did not yet see any comments of yours there.
<s​needlewoods> Yes, that's the plan
<r​brunner7> Ok
<s​needlewoods> wanted to go through all of them first
<j​berman> me: followed up on jeffro256 's unbiased hash to point impl (a blocker for beta stressnet) and did a bit of refactoring of my own code for that impl and for the FCMP++/Carrot integration. Unrelated to the unbiased hash to point, I have some more refactoring ideas to implement in line with my changes there before opening up the FCMP++ integration for auditing and upstreaming more s<clipped messag
<j​berman> tructural PR's. Also will follow up on tx relay v2 this week
<j​berman> Unrelated, but I also started on some Serai work
<r​brunner7> That is inching closer to some beta now, I suppose?
<j​berman> I think we're closer than inching at this point. By my read, the stressnet channel seems significantly more relaxed than it's been in the past before v1.5, which I attribute mainly to v1.5 fixing the major issues people were experiencing in the past
<j​berman> The major blockers to beta are basically out of the way I'd say
<s​needlewoods> my v1.5 stressnet node is still ~30.000 blocks behind, been syncing since it's released, without any OOM or other crashes
<o​frnxmr> The "tasks for beta" issue needs to be updated - had someone asking about it the other day and noticed that a bunch of the tasks have been completed
<j​berman> Was planning to complete those once we have a beta branch and those items are merged into it
<j​berman> e.g. runaway span PR's are only on the alpha stressnet branch right now
<o​frnxmr> ah i see
<o​frnxmr> And beta branch will fork off of fcmo++-stage, yeah?
<j​berman> yep
<r​brunner7> Sounds like the real fun is starting soon :)
<j​berman> so anything in fcmp++-stage right now can be marked as complete on that TODO list I'd say
<ofrnxmr> +1
<r​brunner7> Ok. If we are through with the reports already, I have something that I want to throw into the round.
<r​brunner7> I consider implementing Polyseed for the CLI and the GUI wallet app and wanted to get comments.
<joshbabb> +1
<r​brunner7> Does anybody see anything that would speak *against* doing so?
<r​brunner7> I asked tobtoht by PM about their opinion, but they did not yet answer.
<j​berman> IIRC I don't think it's been audited yet, and I think that would be a good idea
<r​brunner7> Hmm, interesting point
<s​needlewoods> I saw the chat the other day, I think this issue is the blocker tevador/polyseed #13
<s​needlewoods> I can't comment on the crypto stuff, but as a user, having polyseed in cli sounds cool
<r​brunner7> Well, yes, you could be of the opinion that you don't want Polyseed in the core software as long as it does not have perfect plausible deniability, but that would be more of a matter of opinion, not really a technical problem
<r​brunner7> How would the road to an audit look?
<r​brunner7> Making a CCS for it?
<r​brunner7> And finding somebody who may audit?
<r​brunner7> Contrary to doing implementation work, that would be completey new terrain to me ...
<r​brunner7> *completely
<j​berman> I don't know what's best re: that issue 13 personally, I'd have to think on it more. But I think the benefits of polyseed's embedded birthday significantly outweigh that potential downside there, and so I think it would be better to integrate as it's currently implemented
<r​brunner7> Currently I also think that the number of additional people who would escape a 5$ wrench attack successfully if Polyseed would cancel that "Encrypted?" feature bit would be very, very small.
<j​berman> The way auditing has been going so far for FCMP++ research is: get a list of candidates, reach out for quotes, then identify best candidate, then pull funds from the CCS research proposal. I can help out with that as I'm about to start reaching out for audit work on the FCMP++ integration soon
<r​brunner7> Probably a scheme audit *and* a code / implementation audit would be perfect?
<j​berman> I don't think you should be blocked on integrating polyseed into core monero, I'm personally ok with that work proceeding. I doubt an audit would cause a major change to the API / integration
<r​brunner7> Yeah, a number of wallets offer it already, heavyweights like Cake and Feather
<j​berman> right
<s​needlewoods> thank you for taking the initiative on this rbrunner
<jberman> +1
<r​brunner7> Hah, it's early days, maybe I will drop it like a hot potato :)
<s​needlewoods> At least you got the potato rolling then
<r​brunner7> Maybe, with that audit question, and thus not a pure implementation question, it would be worth to bring the subject also to the MRL meeting?
<sneedlewoods> +1
<joshbabb> +1
<j​berman> sure, no objection to that
<r​brunner7> I see. Will think about it. I guess no hurry, Polyseed in the core software is waiting literally for years already after all
<r​brunner7> Alright. Anything else for today?
<r​brunner7> Does not look like it. Thanks everybody for attending, read you again next week!
<s​needlewoods> Thank you
<j​berman> thanks!
````


# Action History
- Created by: rbrunner7 | 2026-01-17T19:15:17+00:00
- Closed at: 2026-01-19T19:31:10+00:00
