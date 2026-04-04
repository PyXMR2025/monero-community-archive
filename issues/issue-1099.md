---
title: 'Monero Tech Meeting #93 - Monday, 2024-10-28, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1099
author: rbrunner7
assignees: []
labels: []
created_at: '2024-10-25T17:41:24+00:00'
updated_at: '2024-10-28T18:56:04+00:00'
type: issue
status: closed
closed_at: '2024-10-28T18:56:03+00:00'
---

# Original Description
Location is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting [here](https://github.com/monero-project/meta/issues/1094).


# Discussion History
## rbrunner7 | 2024-10-28T18:56:03+00:00
````
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/1099
<0​xfffc> Hi everyone
<s​needlewoods> hey
<j​berman> *waves*
<r​brunner7> jeffro256 left a note that he won't be able to make the meeting, but had good news nevertheless, reviewing SNeedlewoods 's PR
<0xfffc> +1
<r​brunner7> Alright, what are the reports from last weeks?
<r​brunner7> *last week
<s​needlewoods> Added [this](https://github.com/monero-project/monero/pull/9464/commits/f9e2bcf2ef3798f08aa0a7cd0f875a767935ea81) commit, which may be the most controversial, because it touches `wallet2`.
<s​needlewoods> Also tried to figure out how to set up an easily reproducible private testnet environment for the Wallet API. I got `libwallet_api_tests` to build (17/36 tests fail), but I haven't studied the code deeply enough to be able to judge if we rather should revive libwallet tests or start fresh somewhere else. From my current understanding some tests I have in mind will not fit into `un<clipped m
<s​needlewoods> it_tests`, because they rely on a testnet.
<k​ayabanerve:matrix.org> *waves"
<k​ayabanerve:matrix.org> I wrote the multi-input prover/verifier for FCMPs, as needed by jberman to make progress on their end.
<k​ayabanerve:matrix.org> Rucknium also asked me for the numbers on the proofs sizes/computational effort to inform the MAX_INPUTS discussion. I believe I have the initial estimates but I'm still working on their confirmation/a summary with my opinions.
<r​brunner7> SNeedlewoods: I think there are some Python based test that *can* use wallets and daemons - jberman knows more
<j​berman> Me: tested wallet sync building the tree locally. My initial tests were very slow, tree build time took almost 4x as long as current sync on my machine. I discussed with kayaba and worked on some optimizations (some solid crypto ones from kayaba that can also speed up daemon sync a bit today), and brought it down to 2-2.5x
<s​needlewoods> I remember asking about libwallet a long time ago, but can't remember where it happened
<j​berman> I have more thoughts on tree build sync can get into a bit more in the meeting
<r​brunner7> Interesting. 2 times slower is still quite some hit, seems to me. Hopefully not yet the end of the line :)
<r​brunner7> Or better said, half as fast?
<r​brunner7> If we are already through with the reports, maybe you can already elaborate a bit, jberman ?
<0​xfffc> SNeedlewoods: i will dm you. I might be able to help about that task.
<sneedlewoods> +1
<j​berman> @SNeedlewoods#2887 @rbrunner7 I set up what I think is a pretty decent framework for testing c++ wallet stuff <> private testnet daemon when working on the async scanner: https://github.com/UkoeHB/monero/blob/83331b6aea0b01add566c4b75d939ec48a84c877/tests/functional_tests/wallet_scanner.cpp
<j​berman> it executes as part of the python functional tests
<j​berman> https://github.com/UkoeHB/monero/blob/83331b6aea0b01add566c4b75d939ec48a84c877/tests/functional_tests/functional_tests_rpc.py#L158-L160
<s​needlewoods> thanks, will look into it
<r​brunner7> Almost a bit nostalgic already to look at code connected with the Seraphis library ...
<jberman> god my matrix client sucks
<jberman> ok switching to irc
<jberman> https://github.com/monero-project/monero/pull/9464/commits/f9e2bcf2ef3798f08aa0a7cd0f875a767935ea81
<jberman> ^this would be the easiest place to review that logic, although I made some minor changes to the actual execution based on koe's comment there
<jberman> lol, wrong link
<jberman> https://github.com/UkoeHB/monero/pull/23/commits/7b4a088acb7f91e82f7ff4522589979fa90b42ca
<s​needlewoods> noted
<jberman> in that commit, I'm not using any Seraphis code
<r​brunner7> Sounds promising then
<jberman> that commit actually could even be added to the main monero repo today pretty easily, but I figured would be a little redundant some of the things it's testing
<s​needlewoods> so I'll ignore libwallet_api_tests for now
<s​needlewoods> ?*
<jberman> it's just checking wallet2 scanner
<jberman> if you feel you have to/want to use a live daemon for your tests, I think that framework would be easier to use
<jberman> I think it would be a solid foundation for your tests
<s​needlewoods> got it, thanks, will maybe contact you if I'm getting stuck
<jberman> also needs this commit: https://github.com/UkoeHB/monero/pull/23/commits/c3bdad3023269e9ad08dfd6ad1a826e1a065c290
<jberman> sounds good
<jberman> ok, discussing wallet sync + tree build. I'll elaborate some more
<r​brunner7> Do go ahead
<jberman> - As currently implemented, scanning does 3 heavy tasks: 1) download data, 2) scan for receives, 3) build the fcmp++ curve tree. 
<jberman> - Tree build time currently is roughly 2-2.5x the time to scan for receives.
<jberman> - In my local, I'm testing building the tree in parallel to scanning for receives.
<jberman> - My CPU hovers around 60-70% utilization using the wallet2 scanner.
<jberman> - Since building the tree is slower than scanning for receives, building the tree is the bottleneck (i.e. overall sync time == tree build time).
<jberman> Profiling scanning:
<jberman> - 57% of tree build time is converting valid outputs into leaf tuples (~94% of conversion time is clearing torsion, which is multithreaded)
<jberman> - 41% of tree build time is calculating hashes (~97% of hash time is hashing the leaves, which is multithreaded)
<jberman> - 2% of tree build time is calculating zeroCommit for transparent amounts (currently not multithreaded)
<jberman> @kayabaNerve says we should be able to cut time to clear torsion down by half, and we can pencil in a guess that we may be able to halve time to calculate hashes by optimizing arithmetic on Helios/Selene
<jberman> - That means that with further optimizations, we could get tree build time to be faster than current wallet2 sync.
<jberman> - Since wallet2 sync does not reach 100% CPU utilization, we can expect that scanning for receives will end up the bottleneck as opposed to tree building (i.e. overall wallet2 sync time will be == scanning for receives, same as today).
<jberman> - However, it's worth keeping in mind that at 100% CPU utilization, which the async scanner achieved IIRC (and is the theoretical optimum), building the tree will compete with scanning over the CPU, and so scanning will likely be slower with tree building (by the duration of tree building).
<jberman> Recall that we can instead download necessary tree elems to re-form the tree in memory, instead of rebuilding the tree locally by computing hashes. This means wallets would need to download roughly 2-4% more data when syncing, and client-side computation should not have any impact on scanning.
<jberman> Thus, overall scan time building the tree locally versus downloading necessary tree elems ONLY if building the tree locally is FASTER than downloading 2-4% more data to the client.
<r​brunner7> So, basically local tree building eats about all the speedup you gained with your improved async scanner, to arrive at roughly the same sync time as today?
<k​ayabanerve:matrix.org> https://github.com/monero-project/research-lab/issues/100#issuecomment-2435545727 proposes building multiple trees for greater efficiency overall (assuming a reasonably low MAX_INPUTS) and notably smaller proofs. That will cause more burden on wallets if they either must compute more trees or must download more trees. I'd like to encourage moving discussions to GPU-premised wallet<clipped messa
<k​ayabanerve:matrix.org>  scanning, even on mobile devices.
<k​ayabanerve:matrix.org> I understand that's not a viable immediate-term goal, nor short-term.
<jberman> @rbrunner A little more complicated than that, I think. The async scanner's most significant scan time improvements came from downloading data to the client faster, hence why the remote daemon speed-up was so significant, whereas local sync was only 10-15% faster on my tested machine IIRC
<jberman> however, for local sync, yes we might lose some of the benefit of the async scanner
<r​brunner7> Just curious: This is wallet sync. Do we already know something about the daemon syncing speeds / blockchain download and verify?
<jberman> I can comment on tree build time for daemons, @kayabaNerve can speak on download/verify. I've made some optimizations to tree building that would also improve daemon sync time to build the tree, so my numbers won't be perfect, but last I checked, tree build time was roughly 15-25% of total daemon sync time (i.e. building the tree slowed down sync
<jberman> from genesis by around that much)
<r​brunner7> Does not sound too bad
<k​ayabanerve:matrix.org> I can't comment on daemon tree building speed nor blockchain download. The proofs should batch verify nicely. We've observed <15ms in batches of 100, without optimized helios/selene arithmetic.
<jberman> ya and halving time to clear torsion + halving helios/selene arithmetic would potentially cut that down 75%
<k​ayabanerve:matrix.org> I'll propose a topic on this at the next MRL meeting.
<r​brunner7> I think we can be carefully optimistic about these results so far, but quite some work remains. Hopefully smartphone wallets won't be impacted too much.
<r​brunner7> Their CPU are also quite powerful nowadays, if you have a reasonably recent model.
<k​ayabanerve:matrix.org> If wallets download the tree, it's solely the 4-5% per tree cost jberman mentioned.
<k​ayabanerve:matrix.org> I'd still prefer to discuss optimized CPU implementations and GPU work however.
<r​brunner7> Is some good candidate in sight already for doing such Helios/Selene arithmetic optimizations?
<jberman> Ya just something to continue to keep in mind: let's say tree building ends up really slow, we always have the option to just not do it in wallets, and download the 2-4% more data necessary to keep track of path elems 
<r​brunner7> Yeah, smartphone wallets are already compromising a bit, by not running a daemon locally, so not building the tree locally won't be the end of the world.
<r​brunner7> But the core software has to offer both ways, with a bit more complexity.
<r​brunner7> Alright. Anything else to discuss today?
<r​brunner7> Does not look like it. So thanks everybody for attending, read you again next week!
<s​needlewoods> thanks everyone, ciao
<r​brunner7> Soon is Monerotopia, I just saw. Do you guys speak there?
<r​brunner7> Ah, yes, just saw the speaker lineup.
<jberman> yep :)
<r​brunner7> With today's "modern" website you just have to scroll, scroll, scroll some more :)
<r​brunner7> "John Murphy, founder of Wownero". Huh?
<k​ayabanerve:matrix.org> rbrunner7: I'll make a proposal at the next MRL meeting.
<rbrunner7> +1
````


# Action History
- Created by: rbrunner7 | 2024-10-25T17:41:24+00:00
- Closed at: 2024-10-28T18:56:03+00:00
