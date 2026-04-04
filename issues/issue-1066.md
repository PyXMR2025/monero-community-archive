---
title: 'Monero Tech Meeting #85 - Monday, 2024-09-02, 18:00'
source_url: https://github.com/monero-project/meta/issues/1066
author: rbrunner7
assignees: []
labels: []
created_at: '2024-09-01T05:01:08+00:00'
updated_at: '2024-09-02T18:43:20+00:00'
type: issue
status: closed
closed_at: '2024-09-02T18:43:20+00:00'
---

# Original Description
Location is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting [here](https://github.com/monero-project/meta/issues/1062).


# Discussion History
## rbrunner7 | 2024-09-02T18:43:20+00:00
````
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/1066
<s​needlewoods> hi
<j​berman> *waves*
<r​brunner7> Second week of absence for dangerousfreedom , hopefully we will have him back next week, work is waiting :)
<tobtoht_> hey
<h​into> hello
<r​brunner7> So, what is there to report from last week?
<r​brunner7> I tried to help SNeedlewoods a bit with his surprisingly complex and large work: https://github.com/monero-project/monero/pull/9464
<j​berman> me: took a brief hiatus no report from last week, jumping back into fcmp's this week
<s​needlewoods> made some progress on that PR, thanks to your review
<tobtoht_> Can I report on fcmp++ related things, or would that fit better with research lab? I forget.
<s​needlewoods> tobtoht mentioned [here](https://github.com/monero-project/monero/pull/9464#discussion_r1740033984) it may be a potential risk to expose `wallet2::find_and_save_rings()` to the API because "it can leak all wallet txids to the daemon". Would like to know if you have any opinions on that, else I'd remove it. Though it's used by `simple_wallet::save_known_rings()` and from the API by<clipped m
<s​needlewoods>  `WalletImpl::doRefresh()`.
<j​berman> nice to see progress on that front thank you @SNeedlewoods#2751
<r​brunner7> FCMP++ is ok, that's "Monero tech"
<s​needlewoods> And should we discuss blackballing? It's proposed to get removed [here](https://github.com/monero-project/monero/pull/8758). jeffro said "If/when full-chain membership proofs get merged into mainnet, then it would be safe to remove blackballing entirely.". So with getting closer to FCMPs each day, I don't think it makes sense to add any blackball functionality to the API, but maybe I'm wron
<r​brunner7> I was also wondering why tobtoht's PR seem to hang in limbo for so long.
<tobtoht_> I'm still in favor of removing blackballing in master and being done with it. Won't make it into a release branch before a hardfork anyway.
<r​brunner7> So a case of just nobody pushing strongly enough to get it merged?
<tobtoht_> I guess so
<j​berman> find_and_save_rings is there for ring signature protection, it would also make sense to remove once fcmp's are in place and consensus stops allowing ring sigs like tobtoht mentioned here
<j​berman> that whole ringdb stuff can be removed then too
<r​brunner7> I guess we can agree to not add something to Wallet API now that will already become obsolete again with FCMP?
<s​needlewoods> totally
<tobtoht_> Yes
<r​brunner7> I think that new Wallet API won't go online much sooner anyway, realistically, no?
<j​berman> +1
<tobtoht_> me: I'm making headway on reproducible fcmp++ builds. For current status see: https://github.com/monero-project/monero/pull/9440.
<tobtoht_> No unsolvable roadblocks towards completion as far as I can tell. Just optimization, cleanup, splitting into separate PRs, and testing remaining.
<r​brunner7> So wether somebody manages to push blackballing over the edge early or not, we don't add it to the Wallet API
<tobtoht_> I added an image that shows the PR dependency graph. It's getting complex, but it's doable. We shouldn't, however, wait until the last moment to get these reviewed. I'll repeat what I said earlier today in -dev for greater visibility:
<tobtoht_> To anyone interested in helping to get our build system ready for FCMP++: please consider running builds for #8929 and posting the results. It only takes a minute to set up on any Linux distribution. Follow the short instructions under 'How to test?' here: https://github.com/monero-project/monero/pull/8929. Reviews are also very welcome.
<j​berman> noted, thank you tobtoht
<r​brunner7> Have a direct link to that picture / graph? Could not see it at first glance
<r​brunner7> It's very welcome that somebody cares about compiling. I was already fearing a situation that everything is implemented and nothing can get compiled in a good way because nobody thought of that :)
<r​brunner7> That PR dependency thing
<tobtoht_> Github image link too long, rehosted here: https://i.postimg.cc/RZCFxptr/trtf.png
<r​brunner7> Thanks!
<r​brunner7> Oh, pretty wild!
<r​brunner7> selsta will be busy helping to coordinate I guess
<p​reland> Wdym? I think it’s completely fine that the entire “reproducible” depends CI pipeline is completely dependent on the platform being a *very specific* version of Ubuntu, and will fail if it deviates from that version in any way, by definition making it effectively only reproducable via sterile building
<p​reland> Or debian-12-xfce from QubesOS, for some reason
<p​reland> That’s about it
<r​brunner7> No, I meant the danger that everybody forgets about the seemingly little "detail" of reproducible builds, and then with the code pretty much finished already release is held up for weeks or months because of that detail
<r​brunner7> tobtoht to the rescue, won't happen, they picked up the job
<p​reland> Well yeah dependency hell sucks
<vthor> :D always
<r​brunner7> We don't exactly overdose with coordination meetings, plans and project planning. Some things can fall through the cracks if we are not careful. A *lot* of things have to come together nicely for that FCMP++ hardfork.
<p​reland> I honest to goodness spent 15 minutes checking if woodser’s fork (used in monero-cpp) was actually based on the new release or was modified in some way
<p​reland> (They’re the same….I think)
<r​brunner7> *project management
<h​into> I'm going to be implementing RPC handlers in Cuprate soon and wanted some consensus on binary+json RPC output, will it continue to exist?
<h​into> jberman: are you willing to make changes to close #9422? Or, would it be okay if I did? I don't mind doing it I just need confirmation that this is the way forward. If FCMP++ will need to make changes to the affected endpoints anyway, that would be useful to know too (actually, all the RPC changes would be useful to know)
<vthor> How is the plan with the FCMP++ hardfork, at the moment there still FCMP++ (pure), seraphis (pure) and the legacy monero, if I get it right, or is there already stuff interconnected? And the changes for the wallet_api are not yet defined, or? (sorry if I still make ignorant questions)
<j​berman> Seems we have rough agreement to move forward with deprecating bad json endpoints following the model we arrived at there. Curious if @tobtoht has an opinion on that approach there too. I'm ok if you did it
<r​brunner7> Did somebody check already whether other clients than from within the Monero codebase itself might use these calls?
<r​brunner7> Probably not, I would guess
<tobtoht_> jberman: I'm in favor of deprecating the non-conforming endpoints. Will read up on on 9422 to see what was proposed.
<r​brunner7> vthor: Seraphis is more or less on hold, at least until the hardfork to FCMP I would guess. And the changes to the wallet API are what we mentioned in the first 15 minutes of the meeting, SNeedlewoods is deep in the woods with that (sorry for the pun).
<j​berman> like @kaybanerve mentioned we could aim to time get_output_distribution deprecation in line with the fork, although get_txpool_backlog won't be affected by the fork. for now I think makes sense to get the pr ready and we can discuss timeline again then
<h​into> okay thanks
<vthor> :D , thank you, so tracking here https://github.com/monero-project/monero/pull/9464#discussion_r1740033984 is the best way to see what is moving for now, correct?
<s​needlewoods> vthor the wallet_api is currently just for legacy, no seraphis or FCMP stuff in there just to be clear
<r​brunner7> vthor: I think you could do dumber things than also having a look at that work in progress, the API is important, and more eyes and more opinions could make a difference
<s​needlewoods> yes I guess
<r​brunner7> Yeah, no Seraphis and no FCMP++ stuff *in the implementation* for sure. The API should more or less survive the switch to FCMP++ I hope
<vthor> okay, but so there is not complete clear how FCMP stuff will be merged with the rest and how much from the legacy code will exist after the merge, is that correct?
<r​brunner7> The words "clear" and "FCMP" in one sentence is a difficult combination, at least for now :)
<j​berman> personally not planning to remove significant (or really any) swathes of legacy code in the fcmp PR
<j​babb:cypherstack.com> there's a WIP FCMP PR from jberman at least which lays out how things should largely work iirc, vthor
<vthor> :D
<j​babb:cypherstack.com> the diagram on that PR lays out what should change or stay the same pretty well imo
<s​needlewoods> https://github.com/monero-project/monero/pull/9436
<j​berman> can see this PR only has 208 lines deleted so far and almost 7k additions https://github.com/monero-project/monero/pull/9436
<j​berman> and I think most of those lines deleted are just git diff moving lines around
<vthor> jbabb: thank you will search for it. It is really weird for me, somehow it feels everything is staying still and moving "blazingly fast" at the same time - but that could also only be because I need to digest a lot of different stuff at the same time, and greedy how I am I try always to swallow everything at once :D
<j​babb:cypherstack.com> I won't jinx us thrice then :D
<r​brunner7> I think we can't affor to delete much anyway because we have to stay able to check all transactions from all generations
<r​brunner7> Speculating that vthor is most interested in things that may have any connection with their proposed lean signing library
<r​brunner7> Alright, any additional subject to touch in this very meeting?
<r​brunner7> Doesn't look like it. So thanks everybody for attending, nice to see how things progress, read you again next week.
````


# Action History
- Created by: rbrunner7 | 2024-09-01T05:01:08+00:00
- Closed at: 2024-09-02T18:43:20+00:00
