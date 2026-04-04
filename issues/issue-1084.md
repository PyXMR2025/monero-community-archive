---
title: 'Monero Tech Meeting #89 - Monday, 2024-09-30, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1084
author: rbrunner7
assignees: []
labels: []
created_at: '2024-09-27T05:55:45+00:00'
updated_at: '2024-09-30T18:38:30+00:00'
type: issue
status: closed
closed_at: '2024-09-30T18:38:30+00:00'
---

# Original Description
Location is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting [here](https://github.com/monero-project/meta/issues/1080).


# Discussion History
## rbrunner7 | 2024-09-30T18:38:30+00:00
````
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/1084
<s​needlewoods> hey
<j​berman> *waves*
<r​brunner7> With that Matrix stuff you can never be sure only few people are around, or the servers run amok ...
<r​brunner7> Whatever! I hope there is something to report from last week?
<s​needlewoods> Mostly cleaning up and working on rbrunners review comments. Now I'm down to ~15 TODOs and 5 QUESTIONS (2 are just about comments). I don't think the PR is ready for full reviews, but a little bit of feedback would be very much appreciated so I don't run out of work. The majority of work should be done (I hope), but probably there will be a couple things that need to be changed wh<clipped m
<s​needlewoods> en more eyes look into the code
<r​brunner7> I think sneurlax over in -dev showed interest in your work, maybe you can trick them into giving some feedback
<j​effro256> Hi
<j​berman> me: made progress on wallet syncing the tree storing minimal data necessary, syncing is functioning (link: https://github.com/j-berman/monero/commits/fcmp%2B%2B-tree-sync/), estimating 1-2 weeks to complete
<sneurlax> I have been giving it a good look over the past week or two, thanks for the effort, SNeedleWoods, I support updating the API in general, strong concept ACK
<r​brunner7> Interesting. Does that already use some sort of extended CyptoNote transaction type?
<r​brunner7> jberman:
<s​needlewoods> thank you sneurlax, feel free to leave comments on github if you think something needs to be changed
<r​brunner7> The more eyes on that, the better. I will be a very important API after all, if things go according to plan
<j​berman> @rbrunner7 I'm implementing all logic in a new `TreeSync` class (name isn't finalized), which is all in its own file, the idea being eventually wallet2 and the async scanner both will be able to reuse it
<r​brunner7> Ok. Will be interesting to have a look once it's ready.
<j​berman> this is the class right now: https://github.com/j-berman/monero/blob/ca100ec4d8b58eb920931e226e46b17260577dbb/src/fcmp_pp/tree_sync.h#L101-L172
<r​brunner7> The .h does not look too threatening :)
<j​effro256> I'm excited to see how this turns out !
<j​effro256> Maybe this is thinking too far in advance but we might want to make this a virtual interface so that a different storage medium can be used (e.g. LMDB)
<j​berman> I was thinking that too, could be reusable by LWS in that case too
<j​effro256> because this has the possibility of being one of the bigger structures stored by the wallet
<r​brunner7> Hmm. We have code that is about 8 years old, for different blockchain DB backends, which now is probably just bloat ...
<r​brunner7> Never materialized
<j​berman> I think a lot of the inner logic can be reusable even with a different storage layer, so I might end up playing with it a bit to see if I can get something nice
<j​effro256> Yeah I blame that on LMDB being too good of a back end for Monero currently
<r​brunner7> The stored tree elements have to cover all enotes, I guess?
<j​effro256> I see more of an argument for wallet software since there's a lot of different types of devices they may go on
<j​effro256> Its not a super important issue tho
<j​effro256> There's not one element per output (I.e. there's not 100 million ). The pruned tree covers the whole chain bit not all elements in the tree need to be stored on the wallet side
<r​brunner7> Ok. Hopefully you will write a nice blog post how this stuff works, or make some good slides
<j​berman> @rbrunner7 the idea is to store all the wallet's owned enotes, their paths in the tree, and minimal data from the tree necessary in order to sync the next block and update owned paths and handle reorgs N blocks deep (which is the last chunk of elems at each layer in the tree, for the last N blocks)
<r​brunner7> Once it's life and you have some free time again
<r​brunner7> *live
<j​berman> I was thinking about presenting on the integration + the approach for this class at monerotopia
<r​brunner7> Nice
<r​brunner7> Ok. Anything else to discuss today? Seems people are all busy for the time being, with pretty clear paths forward
<s​needlewoods> Would it be impertinent to consider opening a CCS proposal?
<s​needlewoods> I could dm you a draft proposal if anyone of you would be interested to give feedback.
<r​brunner7> For your work going forward? Not at all, if you ask me.
<r​brunner7> I think if you do, you may do it soon. Retroactive financing is a bit difficult, as far as I understand.
<s​needlewoods> I don't intend to ask for retroactive funding for what I done, my intention is to continue with general dev work without clear milestones and receive funding  for that.
<jeffro256> +1
<r​brunner7> I think the only way to find out is actually submitting a proposal.
<s​needlewoods> I'm actually a little afraid, seeing how stressed out people get sometimes with the CCS
<s​needlewoods> Until now everything was pretty chill, except the stress I make myself
<r​brunner7> Yeah, it can be rough. See what happened with the proposal to put the Monero website on a Astro based backend. But if you are mentally prepared, and not getting homeless if things take longer, or even worse, I think it's doable.
<r​brunner7> Did you already make a PR to one of the core repos that was merged? Or only Seraphis stuff so far?
<s​needlewoods> I consider part time, wouldn't quit my job for it yet.
<s​needlewoods> Only one very minor PR merged to core
<r​brunner7> That *might* happen, that people advice you to prove yourself first with a decent-size merged PR. Not sure. Maybe just try and watch the fireworks :)
<s​needlewoods> I thought the API PR would be good for resume, but it took way longer than anticipated, which is not a good sign I guess.
<s​needlewoods> Anyways, thanks for the talk, nothing else from me
<r​brunner7> Because the job became way bigger
<r​brunner7> Not because you are not up to the task, IMHO
<r​brunner7> Alright, I think we can close. Thanks for attending everybody, read you again in 1 week!
<s​needlewoods> Thanks everyone, cioa
<j​berman> +1 on a CCS, go for it
````

# Action History
- Created by: rbrunner7 | 2024-09-27T05:55:45+00:00
- Closed at: 2024-09-30T18:38:30+00:00
