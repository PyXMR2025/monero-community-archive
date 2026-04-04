---
title: 'Monero Tech Meeting #145 - Monday, 2025-11-10, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1294
author: rbrunner7
assignees: []
labels: []
created_at: '2025-11-09T17:58:29+00:00'
updated_at: '2025-11-10T18:55:15+00:00'
type: issue
status: closed
closed_at: '2025-11-10T18:55:15+00:00'
---

# Original Description
Location is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting [here](https://github.com/monero-project/meta/issues/1290).


# Discussion History
## rbrunner7 | 2025-11-10T18:55:15+00:00
````
<rbrunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/1294
<s​needlewoods> hey
<j​berman> *waves*
<plowsof> waves
<r​brunner7> Ok, let's hear the reports from last week
<s​needlewoods> still TODOs and bug fixes, fixed an issue where the wallet would crash with SIGABORT, which took a while because it was hidden behind macros `SCOPED_WALLET_UNLOCK*`
<s​needlewoods> finally implemented methods for `--restore-multisig-wallet` (not tested yet) and `--generate-from-json` (simple tests succeeded)
<s​needlewoods> AFAICT the JSON file format is mostly undocumented (found it's mentioned here https://monero.stackexchange.com/a/11045 )
<s​needlewoods> Tried to explain all the fields in a comment, as far as I figured them out from the source code (in `wallet2::generate_from_json()`).
<j​berman> Submitted PR's to address OOM's from batch verifying FCMP++'s, reviewed ofrnxmr  and 0xfffc  's PR's to also address OOM's during sync (and dynamic span PR), fixed a deadlock in the daemon. Continuing by addressing vtnerd 's comment on deadlock PR, continuing investigation on one of my OOM PR's that modifies a glibc setting in response to jeffro256  and @ComputeryPony's comments, then continuing PR review toward tx re-relay (started on that last week as well)
<j​effro256> Howdy
<r​brunner7> Sounds like a very busy week, jberman  :)
<j​berman> definitely was a long week
<s​needlewoods> jberman the binary I'm running since last Friday still without OOM issues
<jberman> +1
<j​effro256> Working on performance issues around popping blocks and mempool handling. Trying to determine the cause of some consistent consensus warnings that have cropped up. Working on extending Carrot device support in the integration. Reviewing @j-berman's proposed stressnet changes
<r​brunner7> Are those OOM problems something introduced recently, over the course of implementing FCMP++, or are they more or less a side-effect of the much larger tx sizes?
<s​needlewoods> the stressnet also stress testing the devs
<r​brunner7> Indeed
<j​berman> I think multithreaded batch verifying introduced in v1.3 exacerbated the issue
<j​berman> But 128-input FCMP++ verifying currently takes ~1.2GB, which is higher than I originally anticipated / has been there since the change to bump to 128 inputs. kayabanerve dropped it to ~800mb with a nice change recently
<j​berman> Runaway spans during IBD causing OOM is upstream and is also exacerbated by much larger blocks
<r​brunner7> Oh, that's almost in the region of memory earlier Zcash versions needed, more or less disqualifying it for use on mobile devices back then ...
<j​berman> This is on the verifying side btw. I haven't looked closely at memory footprint on the prove side
<r​brunner7> Still crazy somehow that this should need such data that it amounts to 800 MB. I mean, that's what, 5 MB per input?
<r​brunner7> More like 6
<r​brunner7> This boomer remembers computers with less RAM in total than that :)
<j​berman> When I looked closer at some of the fn's, it's doing lots of allocations and holding them in place in ways that seem optimizable, but done for ease of implementation. When first implemented we were talking about capping at 8 inputs max, so makes sense it was implemented this way
<r​brunner7> Yeah, we are certainly at the very beginning of a long journey.
<r​brunner7> If that's it about the reports, some bit of info about the CCS PR we discussed last week: https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/621
<r​brunner7> It was, among many other PRs, subject of last Saturday's community meeting
<r​brunner7> I did not read the log closely, only skimmed it, but I think it was looked at favorably
<j​effro256> My gut says that since we know the total size of a batch beforehand, we can do all the allocations at once which would be more performant on just about *any* allocator scheme, but particularly more performant in the case of glibc pertaining to arena usage. How easy would this be do refactoe the code to do? This wouldn't need a custom allocator impl
<j​berman> that's basically kayabanerve 's idea I linked, ya?
<j​berman> https://github.com/monero-oxide/monero-oxide/issues/136
<r​brunner7> But that's more a question of more speed, than a question of much lower RAM usage?
<j​berman> personally I think we have a solid simple short term solution here with setting max arenas to n threads, which is a commonly used pattern that is sane. I think it makes sense to move forward with it
<r​brunner7> Or do we run into problems with heap fragmentation?
<r​brunner7> What is an "arena"? One big chunk of memory to allocate into?
<j​effro256> Oh yeah I didn't see this. Exactly this
<j​effro256> IMO I think it can be okay as a short term solution for the alpha stressnet, but we absolutely shouldn't rely on it and should fix the underlying issue b4 beta stressnet
<s​needlewoods> you can find some info here https://www.man7.org/linux/man-pages/man3/mallopt.3.html
<s​needlewoods> under `M_ARENA_MAX`
<j​effro256> More or less. The glibc allocator allocates a big chunk all at once expecting certain allocations to have a similar lifetime, then de-allocates the chunk all at once when it's no longer used
<j​berman> Personally I think the underlying issue is with glibc for even doing this (not releasing memory back to the OS even after freed), so it makes sense to tune the allocator not to do that weird behavior in this case
<r​brunner7> I see, thanks to both
<r​brunner7> Seems to me a bit optimistic to assume to be able to reliably free up all allocated pieces in such an arena up to the very last one so that the memory can go back to the OS ...
<r​brunner7> Or is the arena parameter somehow when allocating, so you have finegrained control how you use it?
<j​berman> The memory appears to be getting freed properly, the issue appears to be that glibc is holding on to already freed memory because it's keeping already allocated memory cached in these arenas
<j​berman> And there can be more arenas than threads
<j​berman> So SNeedlewoods's 2 thread machine is OOM'ing because glibc isn't releasing already freed memory back to the OS
<r​brunner7> Well, seems to me a big chunk can only go back if you free the very last bit that you allocated in there, no? Allocate 1000, free only 999, big memory chunk stays
<j​berman> changing the allocation behavior on the Rust side isn't even guaranteed to fix other allocator's weird behaviors we might not know about too...
<j​berman> hence why I think it makes sense not to let glibc's allocator do something that doesn't make a lot of sense in our case imo
<j​berman> yea, that's the behavior of arenas as I understand it as well
<r​brunner7> It's quite unfortunate to have to worry, and speculate, about the inner workings of allocators, IMHO, but maybe very hard to avoid in our case
<tobtoht_> Hmm, it might be time to dust off https://github.com/monero-project/monero/pull/9207
<jberman> +1
<j​effro256> But in general, tons and tons of small allocations is the bane of almost every allocation scheme. I feel like it trying to limit the number of allocations will improve performance on basically all real-world systems
<tobtoht_> Statically linking glibc would at least guarantee consistent behavior across Linux distributions (even on musl libc based systems).
<r​brunner7> Does everything have to be fully dynamic? Can't we pack some of those pieces simply into vectors? Maybe dumb question, but who knows :)
<j​berman> I guess my main argument is not to block beta on this (nor would even argue mainnet should be blocked on this), since I think it's a reasonable step to tune glibc in this way
<j​berman> I'm not arguing that it's not worthwhile to pursue the change to refactor the lib's memory usage
<r​brunner7> Well, you would need to address the pieces somehow
<r​ucknium> Should all verification code be audited before deployment on mainnet? (And you could audit a code refactor after the hard fork, of course.)
<j​berman> of course
<rucknium> +1
<j​berman> the verification code has been audited already too fwiw
<r​ucknium> So you would not want to use a different allocation method on beta stressnet if you would not plan to get it audited before mainnet.
<r​brunner7> Ok, the adventure of getting FCMP++ to fly continues in full stride. Some problems with high weight for takeoff, lol
<r​brunner7> Do we have any different subject still to discuss today?
<j​effro256> I think it would depend on how much harder to would be to review the changes after the rework commit
<rucknium> +1
<j​berman> I think kayabanerve would have the best idea of amount of work involved
<j​effro256> Like just b/c we have an audit doesn't mean *all* of the code is frozen in time in perpetuity, but ideally we want to be able to confidently say that changes after the audit don't effect security
<j​effro256> *affect
<j​effro256> Could we agree that it should be a blocker for mainnet?
<j​berman> If we still have OOM issues from verifying FCMP++'s and/or notice perf regressions, yes absolutely :)
<r​brunner7> Maybe testing on some mobile devices has the potential of showing some problems that don't occur on bigger machines
<jeffro256> +1
<r​brunner7> Later, if everything is more mature I mean
<r​brunner7> Alright, let me close the meeting proper, while discussions may continue. Thanks for attending everybody, read you again next week!
<s​needlewoods> thanks everybody
````


# Action History
- Created by: rbrunner7 | 2025-11-09T17:58:29+00:00
- Closed at: 2025-11-10T18:55:15+00:00
