---
title: 'Monero Tech Meeting #137 - Monday, 2025-09-15, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1267
author: rbrunner7
assignees: []
labels: []
created_at: '2025-09-13T18:24:49+00:00'
updated_at: '2025-09-15T18:36:02+00:00'
type: issue
status: closed
closed_at: '2025-09-15T18:36:02+00:00'
---

# Original Description
Location is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting [here](https://github.com/monero-project/meta/issues/1265).


# Discussion History
## rbrunner7 | 2025-09-15T18:36:02+00:00
````
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/1267
<s​yntheticbird> Hello
<plowsof> *waves*
<r​brunner7> Wondering whether we will make it to meeting 1337 ...
<j​berman> *waves*
<s​needlewoods> Hey
<r​brunner7> Let's start with the reports from last week.
<r​brunner7> I studied the issue jberman explained in our last meeting and came to an opinion about approach: https://github.com/seraphis-migration/monero/pull/81#issuecomment-3289567931
<j​berman> me: mostly worked on implementing comments from that PR above^ (it was ready for review but looks like will be working on further changes), also implemented https://github.com/monero-project/monero/pull/10083
<j​effro256> Howdy
<j​effro256> Me: worked on https://github.com/monero-project/monero/pull/10077, https://github.com/monero-project/monero/pull/10081, and reviewing https://github.com/seraphis-migration/monero/pull/81
<s​needlewoods> `grep "\<m_wallet\>" src/simplewallet/simplewallet.cpp -c` yields 148 results (that's <25% left), but some of them are a little more tricky, like all the transfer/sweep commands are still left to do
<rbrunner7> +1
<r​brunner7> That wallet bug is somehow surprising. Did that escape so long, or did people encountering the bug not report?
<j​berman> I expect it's rare because it requires either a parallel wallet with same seed running, or for a tx to remain in the pool while a wallet is being restored (which probably takes longer than 2 mins usually)
<j​berman> Or for someone to submit a tx not via their wallet
<r​brunner7> By the way, I think that reviewing the code of #81 proper is beyond my knowledge, unfortunately ..
<r​brunner7> Ah, I see, pretty rare situations then
<j​berman> I think your point in #81 was ok. Especially in light of the latest round of changes, which added the caveat that m_blockchain can extend back further than the tree cache to handle granularized refresh and added more complexity to managing m_blockchain correctly
<r​brunner7> I saw in the debugger that "short blockchain history" or how it's called merely gets 27 elements in the list. Peanuts.
<j​berman> jeffro256: I think most interesting relevant concurrency change that will be necessary to make is the one from this PR: https://github.com/monero-project/monero/pull/9936
<j​berman> I *think* that will be necessary because otherwise scanning tasks can get queued and begin execution before the network request
<j​berman> But I'll test and spend some time on it. I do think the code will end up simpler
<jberman> +1
<r​brunner7> Thinking ahead I was asking myself recently how we will do it with reviewing when tons of code now in the staging repository will get into PR(s) to the main branch. Isn't that an almost impossible task for "outsiders" i.e. not jeffro256 and jberman ?
<j​effro256> This is something that I have been thinking about too
<j​effro256> The diff is getting pretty large, almost 50k lines of code
<r​brunner7> Wow
<j​berman> I was hoping to start discussing this soon too :) but these wallet issues may begin to take higher priority in the interim
<j​effro256> including tests, but still
<j​berman> In any case, I've been thinking about an approach for my side of FCMP++ integration stuff that would make the review process easier
<j​effro256> Do we want to start merging basic things now?
<r​brunner7> I am not sure a look back may help, when moneromooo also implemented a lot of code e.g. implementing RingCT and then (probably) made a monster PR
<r​brunner7> Are there substantial pieces that could get merged independently?
<j​berman> For curve trees related things, I was thinking of submitting smaller PR's in the following order: FFI first, then curve trees memory-based code (nothing plugged into consensus), then db curve trees code, then consensus changes
<j​effro256> We also want want to start refactoring things which change the logical flow of the codebase to make future FCMP++ integration easier to review, so that we're not mixing refactoring + logical + FCMP changes all together like we have been
<r​brunner7> Of course it would have been the same story, or even worse, with Seraphis, but we didn't get as far :(
<j​berman> This should knock out something like 5k-10k lines of code
<r​brunner7> Sounds good, as far as I can judge, which is not very far
<j​berman> And I was thinking of proposing a new fcmp++-stage branch in the core Monero repo, and making the piecemeal PR's to that branch. Then once all the pieces are in, a large PR to master with everything
<r​brunner7> With review for the pieces already?
<j​berman> Right
<r​brunner7> At least we would know early if that approach runs into roadblocks - if nobody reviews ...
<j​effro256> The big downside with this approach is that if PRing and reviewing takes many weeks, a lot of merge conflicts may come up and certain pieces may have to be re-reviewed
<j​effro256> Especially in regards to reorg handling
<j​effro256> Psychologically, it may also reduce pressure to review if PR'ing to a non-master branch. We want might lose information on how to bisect potentia issues if PR'ing to a branch all at once
<r​brunner7> This strikes me as something worth thinking about a bit, then rest, then thinking some more, then discussing, until things start to converge to a workable approach
<j​effro256> *We might lose
<j​berman> I *think* we can get many thousands of lines reviewed carefully this way before introducing the code that *would* conflict with master
<r​brunner7> It would be quite hard to enter reviewing in the middle, right? Best to follow reviewing over time
<j​berman> A lot of this code is like legos that don't rely on wider dependencies from across the repo. The curve trees handling part specifically. I think it would be beneficial to have that part reviewed separately. And then when a reviewer understands that lego, it becomes easier to review the whole
<r​brunner7> I remember koe's epic code walkthrough for his Seraphis library. I think something like that would be necessary at least for the curve tree management stuff
<j​berman> We could do a large PR and also provide some suggested instruction/guidance on how to review it piece by piece
<j​berman> I plan to write detailed documentation that would also help do that anyway^
<r​brunner7> Nice. Hopefully that won't take weeks, surprisingly
<j​effro256> The `carrot_core` library is also basically completely independent besides the `cncrypto` library and the `ringct_basic` library, which aren't really expected to change much
<r​brunner7> So maybe it's less bad than feared. Still *a lot* of code.
<r​brunner7> In any case, that will be quite some adventure, I am sure.
<j​effro256> Most of `carrot_impl` is independent, except for a handful of transaction format and rule changes
<r​brunner7> Ok, we will see. Do we have more things to discuss today?
<r​brunner7> Doesn't look like it. Thanks everybody for attending, read you again next week. With even more code produced that we will have to review :)
<s​needlewoods> thanks everybody
````


# Action History
- Created by: rbrunner7 | 2025-09-13T18:24:49+00:00
- Closed at: 2025-09-15T18:36:02+00:00
