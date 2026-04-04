---
title: 'Seraphis wallet workgroup meeting #42 - Monday, 2023-10-23, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/911
author: rbrunner7
assignees: []
labels: []
created_at: '2023-10-20T12:57:11+00:00'
updated_at: '2023-10-23T19:18:11+00:00'
type: issue
status: closed
closed_at: '2023-10-23T19:18:10+00:00'
---

# Original Description
On Monday, November 14 2022, we started with regular weekly meetings of the Seraphis wallet workgroup, and all interested parties from the community that want to join. Time is 18:00 UTC on each Monday. "Location" is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting here: https://github.com/monero-project/meta/issues/909

# Discussion History
## rbrunner7 | 2023-10-23T19:18:10+00:00
````
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/911
<d​angerousfreedom> hello
<j​berman> hello
<f​ullmetalScience> hello
<j​effro256> Howdy
<r​brunner7> Ah, nice attendance today
<plowsof> hello
<r​brunner7> So, what is there to report from the past week?
<r​brunner7> I wrote my 1 year report, this one here, for the protocol: https://old.reddit.com/r/Monero/comments/17duyvo/seraphis_wallet_development_1_year_report/
<dangerousfreedom> +1
<jeffro256> +1
<hundehausen> +1
<plowsof> +1
<fullmetalScience> +1
<r​brunner7> It was quite well received, I think the broader community likes to hear from us devs every now and then
<plowsof> +1
<d​angerousfreedom> From my side I just would like to ask UkoeHB  if he is on vacation or how we can get things PRed into the seraphis_lib since he is the only owner of that? It took me more than a month for a small PR and would be nice if he could merge another one that I opened...
<plowsof> looking
<j​effro256> I updated the wallet2_basic library. It can now load and store the .keys file in PEM ASCII-friendly format. I also fixed a bug that can been eluding me for a while, so now it can also load using multiple password KDF rounds
<plowsof> clapping
<j​effro256> Thanks to all the reviewers!
<r​brunner7> jeffro256: Nice, I would say from my side that's ready to merge then
<j​berman> Implemented review comments on the background sync PR 8619 (thank you reviewers), pushed a first commit on the fcmp integration that runs the Rust fcmp benchmark test from C++ perf tests (https://github.com/j-berman/monero/commit/722f266edd75e3ad521b01a9b6b92dae72c1ffa9) [goal for this is to construct Seraphis txs using fcmp's], continued work on the async scanner exploring using libcurl (I'm testing libcurl perf just to see before moving forward without it, hoping to get a larger draft PR for the async scanner up this week), and I apologize to dangerousfreedom I still need to review their latest that's still high on my list
<plowsof> clapping
<g​hostway> Still looking for tasks
<d​angerousfreedom> jberman: No worries, I will break the PR so you can review when it is broken into small parts. I'm just waiting to clear the dependencies on the seraphis_lib but I dont know if Koe is away or if I should continue assuming that it would be merged later
<r​brunner7> I would say try to juggle things, as if your PRs to the Seraphis library were already merged. Maybe that turns out to be too much of a hassle, but I think it's worth a try.
<j​effro256> jberman: which curve cycle is that PR using? Is it the one that tevador proposed?
<r​brunner7> Still, good question about @UkoeHB, would be good to have a statement from him
<d​angerousfreedom> Then it wont compile. Maybe it is better to merge the seraphis_lib dependencies too and in the future try to merge all the dependencies from the seraphis_wallet into the seraphis_lib
<r​brunner7> ghostway: Will try to come up with something suitable this week
<ghostway> +1
<r​brunner7> dangerousfreedom: You will have to cherry-pick things into your working branches to get them to compile, like I did when I compiled your stuff and missed the wallet2 compat loading code
<j​berman> the pasta curves, but the repo has an implementation of tevador's proposed curve cycle (which I believe wasn't optimally implemented and so kayabanerve  stuck with the pasta curves for the benchmarks)
<d​angerousfreedom> I can do that sure, but I dont think it is nice for the reviewers
<r​brunner7> Let's wait anyway for word from koe before rushing anything there. I have really some fears about running into git hell later ...
<j​effro256> If we move to a curve cycle, we may have to update every time the "proof keys" type (every use besides DHKE) is used in the code, and the function calls for each. I'm wondering would it be better now to start the refactoring then later? This will affect hundreds, if not thousands, of lines of code in Seraphis. Until we actually implement in the new curve types and functions, we co<clipped mess
<j​effro256> uld just `typedef` it to `rct::key`. But I want to know if y'all want to start now
<UkoeHB> sorry I wasn't getting emails for PRs to my monero fork, should be more responsive now
<dangerousfreedom> +1
<jeffro256> +1
<rbrunner7> +1
<plowsof> +1
<rbrunner> UkoeHB, you got 3 thumbs up on Matrix that you may not see here on IRC :)
<r​brunner7> jeffro256: Hmm, hard to say, but maybe wait with such sweeping changes until it's a bit more probable that FCMPs will indeed fly, and until we have that tx type question settled and can go through the code for that as well
<j​effro256> jberman: might be too early, but how do the performance tests look as of today in your opinion?
<j​berman> agree with rbrunner there^, maybe I'll see an easier way to implement it without thousands of lines of changes? I'm not sure there
<j​effro256> Might be a good task to do if someone is looking for something to do, since it could clean up the code a little bit anyways even if we don't end up using FCMPs
<r​brunner7> dangerousfreedom is, in my understanding, making an attempt re: tx classes
<r​brunner7> That's the last info that I remember, anyway ...
<r​brunner7> Waiting for some question regarding that :)
<d​angerousfreedom> Well, I dont understand enough about what should be done yet. I'm working on my understanding still
<d​angerousfreedom> What was the problem again?
<j​effro256> We might be talking about two different things. Are you talking about the combined Seraphis-Cryptonote transaction class? I'm talking about making a new class / `typedef`ing all instances of `rct::key` and their corresponding functions out of the Seraphis lib since the underlying curve changes
<j​berman> I haven't implemented any changes to kayaba's code that affect perf (I just got the Rust code built and running when called from the C++), so it's exactly as it was when presented at monerokon (which imo was solid)
<j​effro256> Sweet , I'm glad to hear that!
<r​brunner7> Yup, we are talking about 2 different things. That's why I was thinking maybe go through all the code only *once*, for both things, even if different code parts are involved, mostly
<r​brunner7> But maybe not a good idea, hard to say at this early stage
<r​brunner7> Better have a good look at that in some quiet hour with just the two of us, if that's ok for you :)
<dangerousfreedom> +1
<j​berman> fcmp benchmarks currently sitting at 100ms per proof in a batch of 10, with clear room on the table to get it down to ~33ms, with likely room on the table to get it down further, compared to grootle's 3.7ms per proof in a batch of 10 (had to relook at the presentation)
<r​brunner7> Well, 100ms would sound a bit scary
<r​brunner7> Let's see where you land mid-term
<j​effro256> How does batching performance scale with the batch size ?
<j​effro256> Say batch of 100 vs 10
<d​angerousfreedom> Linearly in time
<d​angerousfreedom> I mean for grootle proofs
<d​angerousfreedom> For fcmp doesnt make sense
<d​angerousfreedom> Ops sorry, I dont know
<d​angerousfreedom> Good question
<j​effro256> Because 100 ms is gonna be pretty rough for a node syncing from scratch (*especially* without checkpoints), but if you're syncing from scratch, you can do batches much bigger than 10
<j​effro256> As long as the 10-block-lock is applicable, you could batch all proofs for all inputs for every tx in 10 block chunks
<j​berman> I don't recall, pinging kayabanerve. kayaba also wrote up this issue asserting it could be possible to use recursive proofs to be able to sync the Seraphis point of the chain from scratch with a single proof: https://github.com/monero-project/research-lab/issues/110
<r​brunner7> Uh, now this thing wanders into magic territory, seems to me ...
<j​berman> ~33ms for a batch of 10 compared to 3.7ms for a batch of 10 (~10x slower for >1000x anon set size increase seems a tradeoff that's worth it without any of this magic anyway)
<r​brunner7> But proving this speedup is still ahead of you, right?
<j​berman> yep
<j​berman> with code at least
<j​berman> and theory proving sure
<j​effro256> Godspeed
<r​brunner7> Likewise
<r​brunner7> We count on you :)
<j​berman> yes kayabanerve , you hear that ? :)
<j​effro256> If we were to do FCMPs, could we retroactively expand the anon set to RingCT outputs? That should be possible, yeah?
<j​effro256> Wait no... not on the cycle
<r​brunner7> Really robust third party blockchain scanning that we can recommend with a reasonably good conscience could become more important with those FCMP
<jberman> +1
<j​berman> right there still needs to be a migration tx, which is the same for Seraphis
<j​berman> as is
<j​effro256> Why's that
<r​brunner7> Because maybe smartphones doing fully local scanning may break a sweat with those, at least if you don't have this year's model?
<r​ucknium> FCMP doesn't affect wallet scan time.
<r​ucknium> According to...
<j​effro256> Yeah wallets don't verify proofs AFAIK
<r​brunner7> Ah, I see, not the wallet's job to prove transactions valid. Good then.
<r​ucknium> https://libera.monerologs.net/monero-community/20230916#c280601
<j​effro256> They *could*, but if the wallet verifies only PoW, that'll cover 99% of abuse by third-parties. You would need to create a fork which has higher difficulty to trick a wallet like that
<r​ucknium> With verification time, you must consider tx volume with batch size 1 because nodes must verify txs before they propagate them.
<jeffro256> +1
<j​effro256> Do you have current numbers on that @jberman?
<j​effro256> Just for curiosity's sake
<j​berman> 3rd party wallet scanners will be able to collect more info that affects the privacy of their users, which they can aggregate and affect the anon set for users of non 3rd party wallet scanners. FCMP's reduce the harm that could cause to users of non 3rd party wallet scanners. that's what I was thinking rbrunner meant in the context of FCMP's relevance to 3rd party wallet scanners
<jeffro256> +1
<r​ucknium> And CPU requirements to run a rode would increase. That may increase the number of people using remote nodes or light wallets
<r​brunner7> No, the speed was on top of my mind when I wrote, but seems that's more or less off the table for wallets, fortunately
<jeffro265> +1
<r​ucknium> run a node*
<r​brunner7> Yeah, with more CPU load, and bigger-again transactions, more people might be driven out of running their own node. Trade-offs, as everywhere in this universe.
<r​brunner7> Anyway, such things are almost impossible to predict, seems to me we have to actually try. Probably will work out, but maybe we will have a problem on our hands, who knows
<j​berman> I could definitely be misremembering and I don't have the numbers offhand right now, but IIRC I think it was on the order of 30ms for verifying 1 proof in the current benchmark which again has a lot of room for improvement. I'll try to get a cleaner framework up to benchmark like the Seraphis benchmarks and have a more apples-to-apples comparison
<r​brunner7> Hah, we want the results yesterday.
<r​brunner7> What do they say - this is not a sprint, it's a marathon.
<r​brunner7> Alright, the hour is full. Anything important left for this very meeting?
<r​brunner7> Seems we got it for today. Thanks for attending, nice to see how things accelerate. Read you next week!
<j​effro256> Thanks!
````


# Action History
- Created by: rbrunner7 | 2023-10-20T12:57:11+00:00
- Closed at: 2023-10-23T19:18:10+00:00
