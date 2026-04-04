---
title: 'Seraphis wallet workgroup meeting #7 - Monday, 2023-01-02, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/774
author: rbrunner7
assignees: []
labels: []
created_at: '2022-12-30T15:02:46+00:00'
updated_at: '2023-01-19T19:17:49+00:00'
type: issue
status: closed
closed_at: '2023-01-19T19:17:49+00:00'
---

# Original Description
On Monday, November 14, we started with regular weekly meetings of the Seraphis wallet workgroup, and all interested parties from the community that want to join. Time is 18:00 UTC on each Monday. "Location" is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting here: #770

If enough people are around so early in the new year I propose to have a closer look where we currently stand with actual dev work for the Seraphis wallet.


# Discussion History
## rbrunner7 | 2023-01-02T18:50:28+00:00
````
<dangerousfreedom> Hello guys. I cant make it for the next hour but from my side I started implementing the audit proofs and I will probably have something to show in the next meeting.
<rbrunner7[m]1> Hello, welcome to the first meeting in the new year! Who is around?
<rbrunner7[m]1> Announcement here: https://github.com/monero-project/meta/issues/774
<woodser[m]1> hello
<jberman[m]> hello
<UkoeHB> Hi
<Rucknium[m]> Hi
<rbrunner7[m]1> Today I would like to get an overview, as far as we get given attending people, where we stand regarding start of programming, in some detail.
<rbrunner7[m]1> We know something from UkoeHB 's new CCS that he is still busy improving the Seraphis library: https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/369
<rbrunner7[m]1> I am pretty sure that this has no negative influence on starting to build on the library, because the interfaces should mostly stand I guess.
<UkoeHB> Yes I am still chipping away at cleanup and review, making minor adjustments and bug fixes
<rbrunner7[m]1> jberman has produced code using the library, maybe you can comment: https://github.com/j-berman/monero-cpp/commit/9f788b40c60d469381d8b9790a0d50aee917f59e
<UkoeHB> I don’t plan any more interface refactoring, although function signatures may change a bit
<rbrunner7[m]1> UkoeHB: Good confirmation
<UkoeHB> Yes I saw that, looks interesting
<jberman[m]> Yep, I implemented a basic "block scanner" using the Seraphis lib (it recovers legacy spends and receives) and I'm planning to use the lib to implement a legacy full wallet scanner that makes network requests for chain data to a daemon
<rbrunner7[m]1> Can we see this as part of an "experimenting and learning" phase?
<jberman[m]> The intent is for the code to be usable in an updated wallet
<UkoeHB> jberman[m]: are you planning to use the scanning framework or reimplement it in some way?
<jberman[m]> planning to use it
<UkoeHB> Ok
<rbrunner7[m]1> From your comments I got you "liked what you saw"?
<jberman[m]> I did :) major credit to UkoeHB the lib is nice to use, usable functions are easy to find, the code is clean and structured well
<rbrunner7[m]1> A very good start then!
<rbrunner7[m]1> dangerousfreedom[m] wrote shortly before the meeting started: "my side I started implementing the audit proofs"
<rbrunner7[m]1> I have a question that maybe UkoeHB can answer
<rbrunner7[m]1> Did he develop some of those proofs himself, because they did not yet exist? Or is this pure implementation work?
<rbrunner7[m]1> He also did some preliminary work with loading and saving wallets, and translating Jamtis addresses from binary to text, but seems to pause that for the moment.
<rbrunner7[m]1> Maybe next week we will hear more about that.
<rbrunner7[m]1> By the way, i can mention again what I mentioned already in an earlier meeting: The GitHub repo to PR against is hopefully ready here: https://github.com/seraphis-migration/monero
<rbrunner7[m]1> jberman: How much of your time, more or less, goes now already into Seraphis and Jamtis work?
<jberman[m]> most of it now
<UkoeHB> rbrunner7[m]1: you can see the discussion here https://github.com/seraphis-migration/wallet3/issues/42
<UkoeHB> some things require custom proofs, others can reuse existing proof structures
<rbrunner7[m]1> Ok, thanks, so it's a mix.
<rbrunner7[m]1> Well, if jberman can put most of his time into Seraphis work, things will really pick up speed now. Good.
<plowsof> +1
<UkoeHB> I think the only new proof needed is a schnorr signature on arbitrary base points. `crypto::signature` only works for the main generator `G`
<rbrunner7[m]1> I myself ran a bit out of subjects and problems to write issues, solely based on theory and thinking, so to say.
<rbrunner7[m]1> But I think soon there will be code for me to review and/or comment about.
<rbrunner7[m]1> Here again a quick link to earlier decisions, from meetings past, about coding conventions: https://github.com/seraphis-migration/strategy/wiki/Seraphis-Wallet-Coding-Conventions
<Rucknium[m]> UkoeHB: Did you see my comment on your CCS? https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/369#note_20224
<UkoeHB> Rucknium[m]: yes I saw. I can only do one thing at a time - right now my focus is on comprehensive review.
<rbrunner7[m]1> But I guess the proposed course of action is not controversial per se, right?
<rbrunner7[m]1> And hopefully makes sense.
<UkoeHB> the proposed course is to pause review and update the paper, I'm saying I will continue review until it is done
<rbrunner7[m]1> Ah, I see.
<rbrunner7[m]1> So this has to wait a bit more, but of course enventually the paper will get updated, and things can progress with that as a starting point.
<UkoeHB> yes
<Rucknium[m]> Ok. Sounds good.
<rbrunner7[m]1> I know that well as a dev, if you are deep in some work, you just hate to stop :)
<rbrunner7[m]1> Alright. Anybody with something more about coding, or some questions?
<rbrunner7[m]1> By the way, I don't want to over-promise, and can't obviously speak for them, but a new dev ghostway has said they are interested in programming work, and already played around a bit with the Monero codebase as a preparation.
<rbrunner7[m]1> Work for Seraphis and Jamtis in particular
<Rucknium[m]> If CypherStack or someone else later finds a problem with part of Seraphis's cryptography, who is going to fix it?
<Rucknium[m]> Since koe said he's going to move on from Seraphis soon
<rbrunner7[m]1> tevador may be a candidate if UkoeHB really cannot fix for whatever reason ...
<Rucknium[m]> +1
<rbrunner7[m]1> Or @kayabanerve maybe. I am optimistic, if it's fixable, we will probably wiggle through, even in the unlikely case that UkoeHB has no time.
<rbrunner7[m]1> Or throwing money at the problem and e.g. ask CypherStack :)
<UkoeHB> if it's relatively minor I can take care of it probably
<UkoeHB> if there is a major issue then who knows, maybe bin the whole thing
<rbrunner7[m]1> By the way, I have PR's my dev recruitment article to the getmonero.org website: https://github.com/monero-project/monero-site/pull/2119
<Rucknium[m]> +1
<rbrunner7[m]1> "maybe bin the whole thing" That would be quite a surprise, no?
<rbrunner7[m]1> Although of course you can't be sure.
<UkoeHB> if we are speculating, then anything goes
<rbrunner7[m]1> Right :)
<rbrunner7[m]1> I am more thinking about some probabilities. I would hate to read tomorrow on Reddit "koe doesn't trust Seraphis" or similar unqualified rumors
<rbrunner7[m]1> Alright, if nothing more, maybe that's it for todays meeting. Off to work.
<rbrunner7[m]1> This will really get interesting in the coming few weeks I think.
<rbrunner7[m]1> Thanks for attending everybody!
<UkoeHB> thanks rbrunner7[m]1
````


# Action History
- Created by: rbrunner7 | 2022-12-30T15:02:46+00:00
- Closed at: 2023-01-19T19:17:49+00:00
