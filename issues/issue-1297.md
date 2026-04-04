---
title: 'Monero Tech Meeting #146 - Monday, 2025-11-17, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1297
author: rbrunner7
assignees: []
labels: []
created_at: '2025-11-14T17:55:39+00:00'
updated_at: '2025-11-17T19:42:21+00:00'
type: issue
status: closed
closed_at: '2025-11-17T19:42:21+00:00'
---

# Original Description
Location is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting [here](https://github.com/monero-project/meta/issues/1294).


# Discussion History
## rbrunner7 | 2025-11-17T19:42:21+00:00
````
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/1297
<s​needlewoods> hello
<j​berman> *waves*
<h​into> hello
<r​brunner7> Ok, what are the reports from last week?
<j​berman> SNeedlewoods: I think a 2 round PR makes sense like you have it for the commits (add functions to wallet API first, then separate PR's for using that new API exclusively for the CLI and another for RPC)
<j​berman> the latter PR's could include the commit from the first PR in the history, and build off it with a new separate commit
<h​into> me: working on PoWER: https://github.com/seraphis-migration/monero/pull/230, have been testing hardware for difficulty parameters
<s​needlewoods> I noticed the situation is a little more complex, there is [#9915](https://github.com/monero-project/monero/pull/9915) which fits in between "updated Wallet API" and "simplewallet without wallet2 based on Wallet API", but I did a lot of rebasing and cleaning up and I think I'll be able to push soon
<r​brunner7> Altogether too many possibilities with those commits and PRs :)
<j​effro256> Howdy
<s​needlewoods> And for now I would focus on master branch only, and then add PRs for release once the one on master is merged
<j​effro256> me: got `fcmp++-alpha-stressnet` branch to compile on Ubuntu 18 with GCC 7
<j​berman> me: finished up deadlock PR upstream, finished first round review on tx relay v2 (will work with 0xfffc  on further changes this week), tested and integrated kayabanerve's  new change to the FCMP++ lib that brings memory usage of FCMP++ verification down to 250mb per call to verify (down from ~800mb), started looking into an apparently simple cause of slow sync in the stressnet right now (should have a fix for that out today)
<j​effro256> Did a massive overhaul of the Carrot device interface which should help HW devs integrate and prepare for Hybrid/Carrot hierarchy account derivation integration
<j​effro256> Writing up the docs soon
<r​brunner7> SNeedlewoods: Not a good idea to include what is now in #9915 in the "Updated Wallet API" PR as well? Or, a good reason to keep that separate?
<r​brunner7> jberman: 250 MB sounds downright reasonable :)
<j​berman> agree, 250mb is solid. Unfortunately it's still doing lots of small allocations (as discussed last week), and so OOM's are still plausible for same reason as discussed (a machine with lots of malloc arenas may keep freed memory allocated / not release back to the OS). Someone reported an OOM on an 8gb 4 core machine running with the 250mb change
<s​needlewoods> I thought about that, but because I already made a PR for it and it's a pretty small PR compared to the Wallet API update and it's relatively separated from it, I concluded to use it, but I'm open to suggestions, so if you think I should close #9915 and add it to #9464, I can do that
<r​brunner7> As far as I understand, a submitter is indeed free to close a commit, if reasons appeared to do so since it was opened.
<s​needlewoods> lmk when it's ready :)
<jberman> +1
<j​berman> jeffro256 you raised the argument that since many small allocations = the bane of most memory allocators, we should prioritize allocating all memory before in a large slice before mainnet. One relevant point: I also tested using jemalloc and mimalloc on the rust side as the memory allocator instead of the default system allocator (which is glibc on most systems), and found that those memory allocators did not have the issue of increasing RSS, and that they were releasing already freed memory
<j​effro256> Interesting
<j​berman> But using one of those memory allocators would introduce a pretty significant dependency (jemalloc isn't maintained anymore, and mimalloc is microsoft)
<j​effro256> Did you do performance checks too?
<j​berman> that was a main reason why I felt going with a simpler option to tune glibc makes solid sense
<j​effro256> It might be a tradeoff
<j​berman> no, but we do have a framework set up! I can check that out too
<r​brunner7> I think significant performance differences in something lie allocating would be a bit surprising
<j​berman> it is interesting that kayabanerve 's latest change speeds up 128-input verification by around 10% on my machine, which does suggest the allocations may be having a perf impact
<jeffro256> +1
<j​effro256> It would be interesting to see those results IG, but like you said, it would probably be difficult to recommend adding this new allocator as a dependency
<j​effro256> I remember Koe saying that during a final tuning of the Seraphis lib, he sped it up by 5-10% by simply adding 'reserve()' statements where applicable
<jeffro256> +1
<r​brunner7> You mean for things like vectors?
<j​effro256> Yup
<j​berman> One reason I bring up jemalloc / mimalloc now is also to note how it lends some support to just tuning glibc / that being an acceptable first step, since other memory allocators do seem to handle releasing memory fine (we also have some mac and windows testers in the stressnet channel)
<r​brunner7> With "tuning" you mean using those "arenas" in the best possible way?
<j​berman> https://github.com/seraphis-migration/monero/pull/228
<j​berman> that PR sets max n areans equal to the number of threads on the machine, so there is 1 arena per thread
<j​berman> which from the docs, sounds like it would even benefit performance and avoid contention since some machines may default to having fewer than 1 arena per thread
<j​berman> (and of course, our issue is that some machines seem to allow more than 1 arena per thread)
<r​brunner7> Sounds like many tests will be needed to be sure about the behavior in all reasonable circumstances ...
<j​effro256> That's fair, I just want to point out that the tuning may or may not come with CPU time tradeoffs.
<j​effro256> I wonder how many arenas a typical Linux + GNU system will use for a 128 thread CPU
<j​berman> I think solid perf observed in stressnet (+ no OOM's reported by anyone with that PR in) should be considered major support
<jeffro256> +1
<j​berman> I'm excited for v1.5 that includes this + other sync improvements + potentially tx relay v2
<j​berman> that includes the improved memory profile / threading approach
<j​berman> I think this PR is good: https://github.com/seraphis-migration/monero/pull/224
<r​brunner7> "omeone reported an OOM on an 8gb 4 core machine running with the 250mb change" Was that with or without that #228 arena change?
<j​berman> without
<j​berman> and they're on a linux
<r​brunner7> Ah, ok, that's somewhat reassuring
<r​brunner7> Because 8 GB is pretty decent, I don't think we make many friends with a Monero daemon that does not run in such a config ...
<r​brunner7> For Linux at least
<s​needlewoods> 2 or 8 if I understand this correctly
<s​needlewoods> > The default value for the M_ARENA_TEST parameter is 2 on
<s​needlewoods>               systems where sizeof(long) is 4; otherwise the default
<s​needlewoods>               value is 8.
<r​brunner7> So next step is that v1.5 with everything significant in, and the hope that it will work pretty well already?
<j​berman> yep
<r​brunner7> That will get interesting :)
<j​effro256> So maybe we limit the arenas IFF default is greater than thread count , and available RAM is relatively low?
<j​berman> this does sound reasonable to me
<r​brunner7> Alright, that seems to converge towards a plan. SNeedlewoods , do you want to go back to your PRs again for some more clarifications, or do you feel you there is enough clarity?
<s​needlewoods> Maybe someone can give their opinion if I should merge the "remove cached password" into "updated Wallet API" so we are at 2 PRs
<s​needlewoods> so close this https://github.com/monero-project/monero/pull/9915
<s​needlewoods> and add the code to https://github.com/monero-project/monero/pull/9464
<r​brunner7> Would certainly make moving it over to release simpler - if that will even become necessary, depending on timeline
<r​brunner7> Less PRs, less problems
<sneedlewoods> +1
<j​berman> funny.. I was about to say the opposite. Before looking much deeper into it, it may make it easier to review and get this code across the line if "remove cached password" was done first, and then adding functions to the wallet API was done building on that. In fact it might be easier if you split multiple PR's like that
<j​berman> and that also brings me to discussion of upstreaming PR's for FCMP++ / Carrot. I think it would help to re-discuss strategy for that too
<s​needlewoods> remove cached password came after and is also based on #9464
<r​brunner7> It needs things in that PR, i.e. is not stand-alone
<j​berman> right, so maybe would work to isolate that feature as its own PR first
<s​needlewoods> So I would do it this way
<s​needlewoods> 1. PR = 2 commits: "Wallet API round one" + "Wallet API round two"
<s​needlewoods> 2. PR = 1 commit based on top of 1. PR: "remove cached password"
<s​needlewoods> 3. PR = 1 commit based on top of 2. PR: "replace wallet2 with Wallet API in simplewallet"
<j​berman> the reason I bring up splitting / isolating a feature like "remove cached password" is that it's a nice change in its own right, that would be a lot easier to review as its own standalone piece. So you could break off that feature and make only the wallet API changes necessary for that change
<j​berman> that reduces the diff size for modifying the wallet API and brings a nice easier-to-review feature into the code sooner
<r​brunner7> You propose to switch the order of 1. and 2., and make that possible by just dragging along the necessary base changes from 1. to make that possible?
<j​berman> yes
<j​berman> and then using that strategy for other changes to the wallet API
<s​needlewoods> iirc that may be just one method `verifyPassword()`
<r​brunner7> For possibly even more, smaller PRs, with better "reviewability"
<j​berman> right
<j​berman> that's basically how I've started with FCMP++ PR's, although that's kind of blocked at this point
<r​brunner7> Well, I am not sure. It's not that terrible, because it's mostly quite straightforwards stuff. I had no problems to review 1. , round 1, in any case
<j​berman> fair counter argument
<r​brunner7> I also think about people later, that just want to see when and how Wallet API was extended, and it may be comfortable for *them* to have it "all in one"
<s​needlewoods> that sounds like a good idea to me in regards to Wallet API, but not sure if that approach works as well for 3. PR simplewallet
<s​needlewoods> or we would have `m_wallet` (old wallet2 object) and `m_wallet_impl` (new Wallet API object) at the same time
<r​brunner7> Oh, simplewallet using both is a bit strange, no?
<j​berman> I think this strategy is ok considering rbrunner7 's arguments
<s​needlewoods> also good point
<s​needlewoods> it would only if we split it up, now it does not
<r​brunner7> Alright, I think we can "sleep over it" for a night :)
<s​needlewoods> thanks for all the feedback, appreciate it a lot
<j​berman> we can revisit this discussion next week as well. Will work primarily on getting to the big v1.5 this week
<r​brunner7> Do we have anything other left to discuss? Nearing the full hour ...
<j​berman> (worth updating I've also started dabbling in Serai a bit too, I am hoping to pick up more time on Serai soon enough)
<r​brunner7> Ok, seems we can close the meeting for today. Thanks everybody for attending, read you again next week!
<s​needlewoods> thanks everyone
<k​ayabanerve:matrix.org> As I said in a GH comment, my PR minimizing RAM may aggravate glibc less but does not fix glibc.
<k​ayabanerve:matrix.org> jberman @jberman: We prior iterated over 1000 empty vectors and checked they were empty 99% of the time. We know immediately iterate over the non-empty vectors. That likely explains the speedup.
<j​berman> fair
````


# Action History
- Created by: rbrunner7 | 2025-11-14T17:55:39+00:00
- Closed at: 2025-11-17T19:42:21+00:00
