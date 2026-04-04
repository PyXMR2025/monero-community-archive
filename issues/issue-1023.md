---
title: 'Seraphis wallet workgroup meeting #74 - Monday, 2024-06-17, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1023
author: rbrunner7
assignees: []
labels: []
created_at: '2024-06-16T06:43:26+00:00'
updated_at: '2024-06-17T19:06:58+00:00'
type: issue
status: closed
closed_at: '2024-06-17T19:06:58+00:00'
---

# Original Description
On Monday, November 14 2022, we started with regular weekly meetings of the Seraphis wallet workgroup, and all interested parties from the community that want to join. Time is 18:00 UTC on each Monday. "Location" is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting here: https://github.com/monero-project/meta/issues/1016

# Discussion History
## rbrunner7 | 2024-06-17T19:06:58+00:00
````
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/1023
<o​ne-horse-wagon> Hello!
<s​needlewoods> hello
<j​berman> *waves*
<r​brunner7> Any report from last week?
<j​berman> Nothing to report from this past week on my end (was mostly afk, back at the keyboard tonight). Shooting to finish trim_tree this week and have an idea to clean up the grow_tree approach as well
<s​needlewoods> even though the state of the organize functions PR is unclear, I prepared the next PR based on that for comments only https://github.com/monero-project/monero/compare/master...SNeedlewoods:seraphis_wallet:x_api_comments
<0​xfffc> hello
<r​brunner7> For the record, once again a link to that "reordering PR": https://github.com/monero-project/monero/pull/9368
<r​brunner7> @selsta was quite sceptic, both about this PR proper and the general approach of basing the API of the wallet on that existing Wallet API
<r​brunner7> Their opinion has considerable weight, and rightfully so, because they organize PRs and hard forks for many years already
<r​brunner7> So it may help to make sentiment clear if people could comment at the PR, pro and contra
<selsta> Are we sure that the existing API isn't going to introduce limitations with the new wallet?
<r​brunner7> I guess that's hard to say until we try to make it feature complete first in earnest, and then start to migrate of course
<s​needlewoods> maybe we should ask for opinions in monero-dev too, probably not everyone is reading here
<selsta> from what i remember moneromooo always disliked wallet2_api
<selsta> or maybe he just disliked it because it's an unnecessary wrapper
<r​brunner7> Yeah, it mostly was, now with `wallet2` available. If you get rid of that the picture changes of course
<j​berman> It's going to take work to add features to the existing wallet API to make it work with the Seraphis lib. It's more work to start an API from scratch. If someone wants to take up the work to start a new API from scratch, then power to them
<r​brunner7> Well, I argued on Sunday morning here that we may miss an important chance if we start a brand-new API now, so far into the game, mostly the "FCMP game" nowadays :)
<selsta> anyway I'm not going to "block" it since i'm not involved enough with the seraphis wallet to have the full picture
<j​berman> The specific issue discussing synchronization in the wallet API (and its lack thereof) is valid. I wrote the async scanner with that specific issue in mind. I also introduced a lock around the refresh thread in my background sync PR for the wallet API. It's not inherently an issue with the wallet API. It's an issue that takes code to solve
<j​berman> Code that would need to be written either way
<r​brunner7> selsta: Appreciate your pragmatism.
<selsta> also another question, since a lot of existing wallets use wallet2_api, how would this work with incompatible changes?
<r​brunner7> As I see it, it should be possible to wait with incompatible changes until the hardfork to FCMP, who will require at least *some* changes anyway in wallet app code
<j​berman> The idea I proposed is to deprecate wallet2.h / .cpp, continue using the wallet API (which includes wallet2_api), and add features to the wallet API as needed so that wallet2.h/.cpp can be deprecated. So wallets that directly rely on wallet2.h/.CPP would need to do some legwork to migrate, but wallets that rely on the wallet API as is wouldn't need significant changes if any to th<clipped messag
<j​berman> eir wallet structure
<selsta> but for example your async scanner, I would assume that would require different APIs?
<j​berman> The CLI, RPC, Feather, and woodser's libs rely on wallet2.h/.cpp directly AFAIK. Not sure of other wallets that do
<j​berman> Nay, the async scanner can theoretically be a drop-in replacement
<r​brunner7> As far as I remember Feather is part, part
<j​berman> Right
<selsta> it would be good if tobtoht could add his feedback, he worked a lot with wallet2 and wallet2_api for feather
<r​brunner7> Well, anyway, whatever we do, some things will have to give, it's a question of getting the trade-offs right overall, for the whole ecosystem
<r​brunner7> Yes, I hope tobtoht will comment
<j​berman> For reference: https://github.com/seraphis-migration/wallet3/issues/64
<r​brunner7> I think they are aware, but can't document their opinion
<r​brunner7> Alright, will drop a note in the dev channel as well after the meeting, SNeedlewoods
<sneedlewoods> +1
<r​brunner7> Anything other in particular to discuss for this meeting?
<s​needlewoods> I'm not certain how to proceed, any ideas/suggestions what I should do while waiting for feedback?
<s​needlewoods> Something that needs review maybe?
<r​brunner7> Judging sentiment right now, if I was in your shoes I would probably risk to go ahead, with some residual risk to getting stopped. So that would mean to already work towards completing the API, if I am not mistaken.
<r​brunner7> jeffro256 mentioned this comment as a good candidate for review over in -dev, but it might be quite heavy stuff: https://github.com/monero-project/monero/pull/8996
<j​effro256> Hello
<j​effro256> so sorry im late
<r​brunner7> A few seconds after you got mentioned the first time :)
<j​berman> @SNeedlewoods I took a quick look at the reorganization code, on first pass it seems a little superfluous / not 100% necessary to me. I would probably recommend continuing working with the existing code for now, potentially just sectioning all your new functions in their own isolated section so they can be reorganized again later with minimal impact on the diff
<j​effro256> We should do an informal survey of the monero wallet ecosystem to see how many projects rely directly on the wallet2 interface vs the wallet2_api interface
<j​berman> That's a soft take on my end though, I could be convinced of necessity for reorganization
<j​effro256> this might've been done before
<j​effro256> but that would let us actually weight costs/benfit of keeping wallet2_api. If a good chunk of the ecosystem relies on it, we should probably keep it so that the amount of ecosystem churning is minimized. If it really isn't used in the wild, we can be more liberal about breaking changes
<r​brunner7> Such a survey may be interesting, but I somehow doubt that there is a possible outcome that will change our direction significantly
<s​needlewoods> alright, will try to follow your suggestions
<r​brunner7> Oh well, it's used for sure. Just don't ask for hard %.
<j​effro256> As for the synchronization issue, wasn't that more of an artifact of wallet2 than the interface itself?
<j​effro256> Ostensibly, that wouldn't be an issue as long as the order and synchronization of calls is well defined
<j​effro256> I guess if the requirement was already relaxed (e.g. the `refresh()` call can be made at any time), then we would have to adhere to this requirement when replacing the implementation
<j​berman> There's 2 issues: 1) refresh() shouldn't be allowed to be called multiple times but can (async scanner doesn't have this issue) 2) refresh() shouldn't be allowed to be called at the same time as other wallet functions like constructing a tx, scanning a single tx, reading wallet state, etc. (The new LOCK_REFRESH macro can help with this from 8619)
<r​brunner7> Sounds quite doable to assure both 1) and 2). It's probably a sign of that neglect / unmaintained state of the Wallet API that is to blame for nobody having corrected that already
<r​brunner7> It's a bit shameful if some fork gets at it first ... selsta linked some Oxen PR
<j​effro256> @selsta do you have that link BTW ?
<r​brunner7> https://github.com/oxen-io/oxen-core/pull/1466
<jeffro256> +1
<r​brunner7> Not sure how many other changes accumulated there in the meantime of course, fork happened years ago already
<selsta> oxen has implemented a completely new wallet
<r​brunner7> It must be one of the few surviving Monero forks from the old golden forking times :)
<r​brunner7> Oh, that PR is almost 3 years old
<r​brunner7> Yes, had a look at that new Oxen wallet, looking for ideas for a brand-new API for us. I wasn't exactly impressed, to be honest.
<j​effro256> Tbf, we will probably create a "new" wallet API underneath wallet2_api by default anyways since the underlying library is completely different
<r​euben:firo.org> Oxen is abandoning it's Blockchain in favour of becoming a token on a L2 to focus on their session app
<j​effro256> By virtue of the new code being more modular, we will likely have a composable wallet library that can be tweaked and messed around with regardless of the wallet2_api compatibility layer
<r​brunner7> Are they? Well, kind of sad. But can't everything of course.
<r​brunner7> *Can't have everything
<j​berman> +1
<r​brunner7> Yes, maybe we won't have an "API" proper beneath that Wallet API, but a nice collection of well-defined classes
<j​effro256> For example, the async wallet scanner PR is an API in its own right
<j​berman> Right
<j​effro256> When you design state machines well, you can drive them in numerous different ways
<r​brunner7> Don't give people ideas. I think it would not be a good idea if wallet apps started to use something like the new async scanner *directly* in their code
<j​effro256> So in that way, we should adopt this mindset that frees us up from having to forward design a perfect API *now*
<j​berman> Personally I think we can chart a long term path to deprecating the current wallet API, but it's more practical to start with deprecating wallet2 but keeping current api imo. The modular code underneath is what will make the long term path realistic
<j​effro256> Why not?
<j​effro256> If it matches their usecase, and they want lower level control, then they should use it directly
<r​brunner7> I am not sure we could assure a good degree of stability, something that you expect from something you call an "API", at least in my understanding
<j​effro256> Yes I guess so, that's more of a problem of managing downstream expectations. As long as we have have at least 1 "stable" API, and put reasonable disclaimers on the backwards compatibility of others components, then I think this should be fine
<j​effro256> Right now, we really have 1 *kind of* stable API that isn't fully functional
<r​brunner7> You can't stop anybody anyway, right? It's fully open source, and some kind of anarchy :)
<j​effro256> Exactly. When devs use lower level stuff and then upstream breaks them, they can always revert or keep a vendored version
<r​brunner7> But IMHO we still think that we tell clearly "This is meant to be our *public* API" and "This is more or less internal plumbing, subject to change on a whim"
<j​effro256> Sure. Realistically,  even implementation details tend to have an incredibly strong staying power in the Monero codebase though ;)
<r​brunner7> Every reasonable and mature framework has that.
<j​effro256> For better or for worse
<r​brunner7> Maybe we did not have a revolution like the introduction of FCMPs and Jamtis in one form or another for a bit too long
<jeffro256> +1
<j​berman> Point being things like the async scanner should be written in a way that they are expected to be isolated legos that people *could* use, but we wouldn't offer a guarantee of a stable API
<jeffro256> +1
<r​brunner7> Complacency and all
<r​brunner7> Yes of course, as long it does not eat too much time that you could well spend in better ways, if you ask me
<j​effro256> Btw the first draft of the Jamtis-RCT library is done: https://github.com/jeffro256/monero/tree/jamtis_rct. The tests creates pruned `cryptonote::transaction`s and puts Jamtis scanning info side tx_extra. Then the transaction is scanned for both plain and self-send enotes
<j​effro256> Working on legacy address integration today
<moneromooo> I disliked it because it has no point. It adds nothing except a small amount of async, just changes all APIs for no reason, is in our repo so used to force us to waste time updating it when updating wallet (I took it out of the default build for this reason, it was a dozen files or so, taking a lot of time to rebuild every time wallet2 got changed).
<moneromooo> But I do not contribute to monero anymore so I don't moan about people building on it. wallet_api is their problem now and if they like it, so be it.
<r​brunner7> True :)
<r​brunner7> "Like" is a bit much, seems like the least evil right now IMHO. But whatever :)
<r​brunner7> We are nearing the full hour. Any last minute comments?
<j​effro256> Kind of reminds me of:
<j​effro256> https://matrix.monero.social/_matrix/media/v1/download/monero.social/zFhUDVdRUSUQQruaaxYpkmIy
<j​effro256> https://xkcd.com/2730/
<j​effro256> Now people depend on wallet2_api for better or worse
<r​brunner7> Right, that's a good ending remark. Thanks everybody for attending, interesting meeting. Read you again next week!
<s​needlewoods> thanks everyone, bye
````


# Action History
- Created by: rbrunner7 | 2024-06-16T06:43:26+00:00
- Closed at: 2024-06-17T19:06:58+00:00
