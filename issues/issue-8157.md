---
title: '"No Wallet Left Behind" - Make Sure Our Wallets Survive the Fork to Monero
  2.0'
source_url: https://github.com/monero-project/monero/issues/8157
author: rbrunner7
assignees: []
labels: []
created_at: '2022-01-25T16:55:54+00:00'
updated_at: '2023-04-13T03:46:19+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
# "No Wallet Left Behind" - Make Sure Our Wallets Survive the Fork to Monero 2.0

## The Short Version

If things proceed as currently planned Monero will, maybe sometime in 2023 or 2024, hardfork to a second-generation protocol called *Seraphis* and a new addressing scheme called *Jamtis*. These changes are so extensive that you could very well call the resulting cryptocurrency *Monero 2.0*.

Monero wallets of all types - desktop, smartphone, web - will need larger functional / UI changes to fully support this.

The even bigger problem for wallets however, as I see it: The Monero core software will probably offer a quite different programming interface / API that Monero wallets must use in order to continue to function. And this in turn will require an extensive refactoring of the code of the wallets, regardless of the programming language used and the OS they run on. This is difficult, expensive and can take a lot of time.

Personally I see a real danger that at least some important and widely used Monero wallets won't be ready for the hardfork, and that we might even loose wallets because the challenge will be too great for their authors and they will be forced to discontinue their apps.

I propose to start a dedicated effort to prevent such a very unfortunate outcome by working out a clear and well-documented migration path for wallets towards Seraphis and Jamtis, and start this effort not with the hardfork already looming at the horizon mere months away, but **right now**.

This effort will probably be as much about project management as it will be about technology and programming interfaces.

## Background

Work is well under way to implement something you could call a "second-generation protocol" for Monero called *Seraphis*. You can find details on the author @UkoeHB 's GitHub [here](https://github.com/UkoeHB/Seraphis). In parallel @tevador designs a new addressing and wallet tiers scheme to be used with Seraphis called *Jamtis* that is currently documented and discussed [here](https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d17024).

The changes compared with the current Monero protocol and addressing scheme will be extensive: Better privacy through much larger rings, with a quite different structure of transactions as recorded in the blockchain, migration to new address formats (every wallet will get new addresses), wallet types (going far beyond merely 2 wallet types "full" and "view-only"), seed format (16 words instead of 25), and more. In a recent IRC chat UkoeHB called this half-jokingly *Monero 2.0* which personally I find spot-on and use here in earnest to make clear the magnitude of the changes.

As I see it Seraphis and Jamtis bring Monero forward enormously, but at the same time their introduction is a monumental endeavor in every respect, and not only technically difficult, but also a formidable project management challenge for a team of open-source devs as large and as diverse as Monero's.

If we stay on this course I would roughly estimate that the hardfork to Seraphis and Jamtis could take place in 2023 or 2024.

## Monero's Wallet "API"

There is a large and complicated C++ class named `Wallet2` that is an integral part of the Monero core code base. You find its header file [here](https://github.com/monero-project/monero/blob/master/src/wallet/wallet2.h).

You could say that this class is the "center of the universe" they revolve around as far as most Monero "consumer" wallet apps are concerned. Internally the typical wallet app ends up calling methods of this class extensively to manage Monero wallets, either directly or through some thin layer like `wallet.h` that the GUI wallet uses (source is [here](https://github.com/monero-project/monero/blob/master/src/wallet/api/wallet.h)).

If you look at this class as Monero's wallet handling API, as far as I know this interface has stayed remarkably stable since Monero's birth in 2014. It has certainly grown with the introduction of multisig, RingCT, subaddresses and other things, but was probably never fully "overturned"- a fortunate fact for Monero wallet apps because they could count on a solid fundament over many years.

## The Problem

During the already-mentioned chat about Seraphis and Jamtis wallets on IRC the following problem suddenly dawned on me: It will probably not be possible in a sensible way to merely somewhat extend `wallet2.h` as an API once more to accomodate Seraphis and Jamtis. Right now the functional changes seem simply too great to me for that, and IMHO this class is not particularly well designed to serve as such an important API in the first place, and it has a quite low level of abstraction which makes it vulnerable to any larger functional changes.

Anyway, while the header file might still look quite reasonable, `wallet2.cpp` is a gigantic complicated mass of C++ code (its over 14,000 LOCs are [here](https://github.com/monero-project/monero/blob/master/src/wallet/wallet2.cpp)) that cries out for refactoring for years already, but so far no Monero dev really dared to take on the challenge, because of the amount of work involved and the very central role of the class for the whole Monero software universe already described.

Somehow stuffing Seraphis wallet handling and Jamtis address management into `wallet2` would probably be sheer madness from an engineering point of view, and UkoeHB has, rightfully so IMHO, already made clear that he has no intention whatsoever to even try.

If you followed me so far maybe you start to see the same problem I see: If this API falls away and gets replaced by something new and considerably different the very fundament most Monero wallet apps rely on will get pulled out from under their feet. This will require large and time-consuming changes in their codebase.

And this in turn will lead to a serious project management problem: How can we make it possible for wallet app authors to start early enough with adapting their code to be ready for the hardfork to Seraphis and Jamtis in time?

If we are not careful here we might end up with a situation where on the day of the hardfork only the CLI wallet is fully functional, the GUI wallet is still on its way, and it's unclear when smartphone wallets like Monerujo and Cake Wallet will be functional again thanks to updates. Or, the other way round, we might have to postpone the hardfork many months, maybe even more than once, despite everything being ready in the core software already.

## Proposal

I propose to work out a clear and well-documented migration path for Monero wallet apps towards Seraphis and Jamtis, and start with this work more or less immediately.

How could that path look? In a very first round of brainstorming I had the following idea that may be worth discussing further after starting a corresponding project:

Maybe it's possible to define a new API - let's call it `wallet3` as a working title - that is abstract and flexible enough to be suitable for Seraphis and Jamtis on the one hand, but on the other hand can be used to handle current Monero wallets as well. In this scenario the first implementation of `wallet3` would be a reasonably thin layer above `wallet2`, with that former class still doing almost all the "heavy lifting".

Advantage: With this API available e.g. at the end of this year 2022, wallet app authors could already start migrating during 2023 and then switch to it well ahead of the Seraphis and Jamtis hardfork. The final switch to the new technologies would be relatively simple and could avoid painful deadline troubles.

Another thought that crossed my mind was deprecating any direct "binary" interfaces outright and starting to fully rely on RPC. There is already now an almost fully feature-complete RPC wallet interface - the header file describing it is [here](https://github.com/monero-project/monero/blob/master/src/rpc/core_rpc_server_commands_defs.h) - and I think this interface has a much better chance of getting successfully extended to accomodate Seraphis and Jamtis than `wallet2.h`.

What I don't know however right now is how difficult it is to put smartphone wallets on such an RPC-based fundament.

It's worth to mention here that Monero dev @woodser has defined a new and clean wallet API quite a while ago already and implemented it in C++, Java and JavaScript. The design is documented [here](https://moneroecosystem.org/monero-java/monero-spec.pdf), its C++ implementation is [here](https://github.com/monero-ecosystem/monero-cpp). It's only for the current Monero technology of course, but maybe it could serve as a good starting point for `wallet3`.

@UkoeHB is currently working on a "proof-of-concept" implementation of a Seraphis wallet. As far as I understand it will have a "fresh" structure and interface designed from the ground up for Seraphis. It may be a good idea to wait for the publication of that work before starting to define something like `wallet3`, but the whole migration project could probably start already before that which an attempt to find consensus about the general strategy.

## Requirements for Success

To sucessfully pull off a "Monero wallet migration" project like I decribe it here two things are crucial in my opinion:

People are needed to work on it, preferably people with knowledge already about the architecture and structure of the Monero codebase, and ideally some experience in API design plus project management on top of it.

But secondly the Monero dev community and the broader Monero ecosystem must come to stand behind the worked-out strategy and support it as the agreed way forward. Wallet app authors must come around to trust it enough to bank the future of their apps on the resulting migration strategy and API, based on at least a "loose consensus" that it's solid and suitable.

Regardless of quality it's quite easy to ignore to death something like that and turn it into a failure. Build it, and nobody comes, for many possible reasons: because of "I don't care enough", because of "Nobody ever asked me", because of "Not Invented Here", because of "I can do better", or even "I just don't like the people in this workgroup".

Of course I am well aware that you can't force anything here; acceptance must come as a natural consequence of the quality of the work and the trust earned by the devs involved.



# Discussion History
## paulshapiro | 2022-01-25T19:25:02+00:00
Hey Rene,

I read your post excitedly but think I have got all the relevant details.

Thanks for making the post.

I notice that you focus on Seraphis/Jamtis as needing specific accommodations in the wallet-client API because of its significant distinctness from previous wallet level usage changes. This is true, of course, but IMO Seraphis/Jamtis will not be the end of such updates nor the start. There are very valid behavior patterns that ring signatures and consensus rules currently do support, but which still leave some metadata in the clear that could fingerprint themselves or let users be fingerprinted by others [1]. One solution we know about to this problem in these use-cases probably be accomplished with Seraphis-Squashed [2]? Those are cash-like use-cases too, plus ring sigs will hopefully be ripped out eventually,.. all this to say, the actual API to spending may end up taking some non-trivial modifications, and downstream consumers of the API are still going to need to know of every change, analyze its relevance to their requirements of the code they're embedding, and make sure they stay updated.

For this reason, documenting common (embedded/consumed) code interfaces is certainly a great idea, and the documentation should be associated with release versions as well, etc. I'd love to see the Monero project keeping up with other open source efforts that do have systems like this in place, but third party embedding has been somewhat deprioritized over having an utterly functioning mainline wallet executable.

But all this stuff related to code interfaces has been a problem for years. The only way to solve it is by keeping the code as simple as possible, and generally, interfaces should simply relay the underlying technologies and building blocks themselves so that consumers can use them like legos. It's a fine line between creating code that can live forever and dictating APIs and abstractions. 

Right now we have this problem with the existence of the inaccurately named `monero/src/wallet/api`, for example. There is no concrete "domain matter" (problem) specified by such a name as "api" except in "wallet". But what is a wallet, anyway? We already have accounts and addresses. This is a common trap that programmers can fall into when trying to come up with shared/common code and I would like to contribute to making sure we can solve it. `wallet2` is already an API - its header file, and various 'public' declarations, virtually are the interface to consumers already. So that's why it's been a common suggestion that creating that `api` subdirectory was a mistake. So one of the best ways to avoid all these problems is that wherever possible - for starters, at least, looking at wherever there is no need to hold state on an object - *all* "institutional knowledge"/"protocol"/ etc functionality  - anything that would require work to rediscover how to do - anything that encapsulates non-trivial work, anything related to chunks of code that might need to be ever used by more than one consumer in the future - should be extracted to a "pure function" that is named precisely and concretely to what it does, without complication with other domain-problems. Usually in wallet2, domain-problems are conflated, so you end up with all sorts of code which actually can live entirely in a separate file with... maybe 2 dependencies (none of which are libunbound)!

One big question is how to get people on board with actually writing code like this because it doesn't matter if we make some PRs that factor out some things if people go and duplicate code for some reason.

I have to mention as well one other thing from your post that worried me.

> Anyway, while the header file might still look quite reasonable, wallet2.cpp is a gigantic complicated mass of C++ code (its over 14,000 LOCs are here) that cries out for refactoring for years already, but so far no Monero dev really dared to take on the challenge, because of the amount of work involved and the very central role of the class for the whole Monero software universe already described. 

It's actually not a daunting task whatsoever.

Factoring wallet2 can be mostly *completely done* within a few days of development work, believe it or not. All one does it pull out the implementations or declarations one wants to move, and the compiler in an IDE will give you a list of places which reference the older declarations, signatures, and namespaces which need updating, and one just updates them, simple as that. 
The harder part for people is knowing what abstractions or namespace organizations to create because they dont have the precise boundary in their mind around the problem domains matters, and the experience to tell what makes a sustainable or long-lived definition which does not have to be changed. 

I'm not too worried about this personally but I can see that if someone were to do this work of factoring wallet2, and given it could be done so quickly, and if they were to PR their work to mainline, they'd have to worry about convincing everyone it's okay to touch all that code at once.

There are a few solutions to this. For starters, I've already gotten the verbal support of numerous monero devs in the community who know I've been working on this, so I think PRs will not struggle too hard to get approved. I think this can be accomplished by mitigating the review overhead by splitting PRs up into very small chunks and by absolutely minimizing changes to code - so these PRs must be atomic changes that incorporate zero changes to implementations, if at all possible, so that the exceptions are the cases that would trigger cause for deep review.

One reason I haven't done these PRs yet is that I had like 3-4 jobs since I started working at MyMonero, one of which was talking with numerous enterprise customers (dozens of software and hardware wallet companies I was pitching Monero to) who wanted to use this sort of embeddable Monero code, not the least of which for their own apps and firmwares, which took me away from even iterating on user-facing features on the app, at the time. Other things included paying back our own often somewhat pressing technical debt.

In fact it was at MyMonero that we first established a process for keeping up with conforming to Monero's hardforks and maintaining fungibility best practices in how we formed transactions etc.. MyMonero was at first entirely browser based, meaning the Monero cryptography and wallet and transaction level code had to be written *by hand* and ensured updated at each hardfork so that it could be run in the browser itself. I recall luigi1111 saved our bacon, for example, by writing RingCT in JS by hand. Extremely few people in the world would have been able to do that. We were going to have to do it with bulletproofs later, and there were multiple other deltas within e.g. tx creation at various consensus updates.
Point is, it wasnt fair to rely on luigi nor was it quite safe to attempt to keep the JS hand-updated by myself for each minor change, so even though luigi'd end up hand-writing bulletproofs in JS, I had set about investigating and had succeeded in factoring an embeddable form of Monero's relevant code, both core crypto and my C++ port of e.g. tx creation, much of which is convergent with wallet2's tx creation, and transpiling that to a browser executable form in WASM/ASM.JS. In fact this transpilation had been done in 2014 when MyMonero was initially born but the author only transpiled crypto.c and hand-wrote the rest in JS, so the transpilation had still lacked all the accounts and other code etc.,
And it is the case that during the process of factoring Monero's code into an embeddable form which we call `core-custom` (the stripped mainline) and `core-cpp` (code which we've factored out and want to PR back to mainline) [4, 5], I had even written a class called wallet3 because I wanted our code to be able to live alongside or converge with and be PRd to what we call wallet2 right now. But I discovered it wasn't really the solution, nor even the real problem, even if there are multiple improvements and simplifications which could be made to a hypothetical wallet3, even including a means to support both full and lightwallet modes. The real problem is that devs to Monero keep adding code into wallet2 and we keep approving it even though it needs to reside elsewhere, because it is not actually owned by wallet2, if that makes sense? So I continued to maintain my pure function factorizations for the time being.

In the past 2 years I've been working in private on anew project without any dev contributors til recently and only one financial supporter who reached out to me after he saw my talk at the Monero Konferenco in 2019 where I actually gave a talk about this very code quality problem [3]. Please have a look and let me know what you think.

At this new stealth project of mine I have been maintaining my own "core-cpp", which I have made some significant code quality and usage improvements to. We also have a "core-custom" The biggest take-away I have to share from it right now is related to namespacing. Most of the content of wallet2 can be organized into isolated/independent namespaces that are much more accessible than we've been thinking about. Suppose we have some code to decode an address and it's kept within a function that wallet2 thinks it owns. We can just go like this:

`namespace monero { namespace addresses { bool decode_address_str(…); } }`

Then call it from anywhere with

`monero::addresses::decode_address_str(…)` without importing the world.

So I have quite a few functions that have been very simply extracted from wallet2 like this which are ready for PR, I just have been mad busy and need extra hands!

On that note I think this is a good time for me to share that I have had a full-time C++ developer (@vdero133) working with me for a number of months now and kicking tail, and he and I are set to post a CCS proposal in a few weeks detailing some of the work that we'd like to do to help out the wallet2 situation. He's a long-time lurker, quite passionate about Monero, grad level CS degree, and solid experience doing enterprise and open source C++ build chain and code management, and he and I are pretty closely on the same page about sustainable code management. The project has been funding his efforts internally but it would be great to receive a little bit of financial coverage for his work on wallet2 we'll propose (though we do not use wallet2 internally, we'd be very pleased to converge with it). So I'm happy to confirm I can take the lead on the factoring effort as it is highly aligned with our work with Monero, and I think it'll be a good way to start sharing some of the work we've kept under wraps since 2020. 

Also would like to share that though it was slow going during the holidays I've been working with counsel and am trying to establish a foundation to protect the Monero codebase. Eager to share more about that when things are more concrete, and I warmly welcome those who'd like to get involved to drop me a line. 

1. https://github.com/monero-project/research-lab/issues/95
2. https://github.com/monero-project/research-lab/issues/96#issuecomment-1007556464
3. https://www.youtube.com/watch?v=DY0iE0cBXbc
4. https://github.com/mymonero/monero-core-custom/tree/0b6680c3bec256efa084747fd2fee67c242af919
5. https://github.com/mymonero/mymonero-core-cpp



## elibroftw | 2022-01-26T00:12:33+00:00
I believe wallet3 should be made right after or even with seraphis. Then the new protocol should run on the testnet for 3 months. The testnet is experimental so there should be 0 harm done to developers who need fake transactions as they should be using stagenet. During this time, someone should inform these wallet developers:

Monerogui
Cake
Feather
Moneroju
Mymonero
Edge
Exodus

about the new hard fork, a brief summary about it, and how to update their codebase (wallet3). As well as telling them that the hard fork is already up on test net. What should also be mentioned is the approximate week the hard fork will go up and the day they will get a followup to confirm a time (preferably a month before the hard fork). To ensure broader communication, as even I have ambitions to create a monero wallet in the future, a blog post (+ shared on social media) should be made with the same information. That way my rss reader can catch it and people like me will be good. All monero 3rd party developers should be in the loop someway or another, so as long as the core communication channels have mentions it clearly (title mentions developers), the onus is no longer on the monero protocol devs. 

This way wallet devs can write their code to ensure their users won't have to update AFTER the hard fork has gone through. They can have an if statement based on time for when to use the new API. The only users hurt are ones who have modified their system time. I'm not sure what happens to transactions that use the old protocol once the new protocol goes up, but if we know how these transactions will behave, then wallet developers could also just catch this exception to toggle another flag or something to use seraphis. Recap: test net flag, hard fork time flag, transaction failure due seraphis; flag. Honestly, the error for transactions using the old protocol should be unqiue so that the wallet apps can catch and refresh the entire UI to reflect the logic of the new protocol. 

Thus the only users who end up getting "hurt" are those who don't bother with updating important things! And for the users who hodl, there should be a script in a FAQ on how to convert their seed to the new seed. That feature could be added to wallets as well but it's not really a hard requirement. 

## rbrunner7 | 2022-01-26T06:48:28+00:00
Thanks for your comment, @elibroftw.

What you describe is basically the approach used for most if not all previous hardforks. It's sensible, it's "battle-tested", it has served well.

What I wanted to bring over with some many words: Not this time. This time it's different. And the sooner we recognize this, adapt our course and hammer out a new approach, the better.

> Then the new protocol should run on the testnet for 3 months.  ... During this time, someone should inform these wallet developers:

Because this time it's different, 3 months are too short. Much too short in my estimates. How about 1 year instead? That may indeed be the time a larger wallet app needs from starting to look into this until release of a new "live" / production version. And here you can very well ask whether we can afford to wait a full year, with basically everything ready in the Monero base layer, for wallets to catch up.

> They can have an if statement based on time for when to use the new API.

It will be much more than one `if` statement. Even many `if` statements might not do. Just look at Jamtis, the new address formats, the new types of wallets, the new type of seed, and then think about all the UI / UX changes this will require.

I can imagine that Cake Wallet and Monerujo won't try to make a single app that works pre-fork as well as past-fork and publish a new, **second** app to use after the hardfork, after import of the wallets from the "old" app - a quite radical approach, with many ramifications, but maybe the "lesser evil".

## 3h5t4tvz8etx1op2 | 2022-01-26T15:37:09+00:00
I'm standing against the idea of `wallet3` thing.
I'm a Golang/Dart developer so my knowledge sums up to linking already existing c++ code to Go binaries using CGO. And do you know what gives the most pain all the time? ` libc.so` it is not backwards compatible, I can't simply do `go build` on my desktop and send it to a co-worker to test it simply because I'm on ubuntu 21.10  and he is still on LTS. So my usual way is to either push the code to a separate branch and wait for the CI to pick up the job, compile the binary.. etc. (or I fire docker on my computer and clean-build everything in `debian:oldoldstable`) but then we have other problems! i686 toolchain is not in the debian oldoldstable repo. Then we find out that the libraries are old (which is understandable).
Then, despite all the hate I have to android, it is doing perfect job. I have a game that I used to played with my father around android 2 times (it is Paper Soccer) that app targets API 0, and not a single update was made to the app since Android Market times. Despite the fact that permissions changed, android is 32 major API versions older the old things are still working, including bluetooth multiplayer.
Same thing is with Linux kernel, Torvalds is against breaking changes, and there are api interfaces that didn't change since the very first push to the Linux mainline git (or at least since 2.x versions).
Exactly the same thing is happening inside of `ioutil` library which now is partially deprecated, but instead of telling developers _Just change imports to "io" it have the very same interface_ they simply made `ioutil` a wrapper around `io` library. Which is awesome, because the `Just change one line` solution is not that perfect. There are parts of code that depend on old, forked versions of some libraries, and then suddenly being forced to change one line in each of them, to update the dependencies, make sure that it is actually working, is much more work, that some people may prefer not to do.

So my proposal is to not go the GLIBC way because
`/lib/x86_64-linux-gnu/libc.so.6: version `GLIBC_2.34' not found (required by ./...)`
it is not the answer that people in future will be happy about. 

Let's go the Android or Golang way instead, and make sure that people who learned how to use `wallet2` will be able to use it. Because there could be a group of people who is not willing to do anything more than `git pull` and `make`. And any kind of work may just end up with delisting Monero from CEXes (or even DEXes?), because not everybody is as committed to monero as Monerujo, Cake, and this whole community, some people are here strictly for profit, and when some exchenge or payment processor, such as coinpayments, notice that they need to rewrite their whole code because of some update.. they aren't going to do that.

If wallet2 can't be upgraded.. let's at least make it a wrapper around the wallet3 with as much functionality included as possible, with the important features such as creating and restoring wallets, accounds, subaddresses(in new format, if possible), sending and receiving monero.. So people will have choice to go the shiny new way, or stick to the `it still works and it's good enough for me` way.

Don't make the next big change of monero the change that will break compatibility with software that is already written and 'works'. 

edit: I think that we also should avoid 16 word seeds to not make any UI/UX changes during core update. It's like asking people to change color of their walls to match the new fiber cable color, those who care will do that but majority may just stick to whatever is being used now. So address format can change but without breaking compatibility with the old addresses.. somehow? Think about all the archived repos with monero donate address... all the youtube videos

Please, make it similar to segwit on bitcoin...

## hyc | 2022-01-26T15:54:43+00:00
> I'm standing against the idea of wallet3 thing.

In other words: "Please accumulate and support technical debt forever." Horrible idea.

> some people are here strictly for profit,

That is not what Monero is about. If they drop out, no big deal, they were in the wrong place to begin with.

## 3h5t4tvz8etx1op2 | 2022-01-26T16:06:32+00:00
> In other words: "Please accumulate and support technical debt forever." Horrible idea.

@hyc What about the `bc1*` and `1*` addresses on bitcoin, hence even in Bitcoin Cash? Bitcoin Cash despite being rapidly developed still support old address formats, you still can use them (with higher fees).

Think about it in other way @hyc, what if there are people who run monerujo on old phone, and in 2023 when the update reach mainline they will not be able to install it because of some change in ndk or whatever else?

> That is not what Monero is about. If they drop out, no big deal, they were in the wrong place to begin with.

Yeah sure, I have big respect for those who use monero but it's like with regular money, there are people who do business with it. And if 1xbit, fixedfloat or other exchanges halt the monero transaction option just because some technical thing they don't understand, people who used to buy/use monero are simply going to switch to other currency.

It's like saying everybody should use arch linux with coreboot because that's the way. Well yes, but some people prefer to run Pop!_OS and get their nvidia drivers and games out of the box.
Just because something `should` be used differently doesn't mean that it is supposed to go that way no matter what.

I'm standing strong against the idea of breaking backwards compatibility in any form, such as breaking old ui, breaking old wallet formats, old seeds etc.. Just think about all the developers that would need to fix that. Some instead of that will go and drop monero support (such as 999dice did back in the days.)

## sedited | 2022-01-26T16:17:51+00:00
> Think about it in other way @hyc, what if there are people who run monerujo on old phone, and in 2023 when the update reach mainline they will not be able to install it because of some change in ndk or whatever else?

That's a problem right now, with hardforking updates. If you don't update the app every year or so, you won't be able to transact.

## UkoeHB | 2022-01-26T16:17:58+00:00
> I think that we also should avoid 16 word seeds to not make any UI/UX changes during core update.

The 16-word seeds would only be for new wallets (they incorporate a 'creation date' which is very useful for scanning UX). Old wallet seeds would still be supported.

> I'm standing strong against the idea of breaking backwards compatibility in any form, such as breaking old ui, breaking old wallet formats, old seeds etc.. 

I will keep your point of view in mind. Be aware though, that it may be impossible to continue supporting at least a subset of the existing API. For example, we are [changing](https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d17024) address indices from 64-bit to 56-bit, to accommodate robust output recovery (in place of subaddress hash tables). This means it is _possible_ for some rare users to have accounts with weird indices (>= 2^16) that won't, semantically, be able to receive XMR after the update. Also, old view-only wallets will be useless except for backward-compatibility (finding pre-update outputs). Also, it is impossible to support old addresses due to underlying cryptography changes.

## iamamyth | 2022-01-26T16:45:34+00:00
> Then, despite all the hate I have to android, it is doing perfect job. I have a game that I used to played with my father around android 2 times (it is Paper Soccer) that app targets API 0, and not a single update was made to the app since Android Market times. Despite the fact that permissions changed, android is 32 major API versions older the old things are still working, including bluetooth multiplayer.
> Same thing is with Linux kernel, Torvalds is against breaking changes, and there are api interfaces that didn't change since the very first push to the Linux mainline git (or at least since 2.x versions).

There's a huge difference between a wallet API and an operating system (both examples you provide are of operating systems providing strong backwards compatibility) in terms of what users can and should expect, and, therefore, a wholly different cost benefit analysis. Examples simply do not matter here because they fail to address all the tradeoffs of this specific situation (effectively the equivalent of trying to engineer a five foot long bridge by saying, "well, the longest bridge in the world has all of these various support features, therefore we need them, too"). I will note two massive downsides to retaining backwards-compatibility, both of which apply here:

1. Retaining backwards-compatibility forever, as you seem to propose, creates a forever maintenance burden, slowing development. It's worth noting that Linux doesn't even provide permanent backwards-compatibility, rather, the rule is "don't break userspace", i.e. some backwards-compatible changes can and do happen, iff actual userspace software won't break because of them. Monero has made many upgrades in the past few years, and even after the one proposed here, won't have reached an ideal state relative to its goals (in particular, the anonymity set would ideally be even larger, wallets would be able to scan for transactions faster, and many other things, per the MRL issue list). So, adopting a policy of doing everything possible to retain backwards compatibility will require a lot of development effort.

2. Backwards-compatibility creates impedance mismatches, slowing third-party development and making bugs in third-party software more likely. Per the original issue description, the new protocol scheme looks very different from the existing one; trying to pretend they're compatible or identical imposes a huge cognitive burden both for Monero developers and ecosystem participants. Anyone building new wallet-dependent software in the future effectively has to determine: 1) how does the protocol work? and 2) how does the protocol map onto the ill-suited, backwards-compatible abstraction. Or, if there's a compatibility layer and a new API, that option makes for the probable result of bugs present only in one interface, which substantially complicates debugging and reporting of issues ("which interface did you use?"; "are you attempting to use the new interface with data exported by the old one?"; "what if a project uses both interfaces, depending on version, or subsystem?" etc.).

## 3h5t4tvz8etx1op2 | 2022-01-26T16:57:51+00:00
So if I'm understanding correctly the plan is to make new format incompatible with the previous one..? Or only one way incompatible (old coins can be sent to new address)?

Yes I'm talking about the don't break the userspace thing, I believe that monero should follow that philosophy by 'not breaking external apps'.
Also wouldn't that break things such as p2pool?
And, is 16 words seed more secure than current 25 word one..?

## chaserene | 2022-01-26T22:11:32+00:00
thank you a lot UkoeHB for spearheading this effort. I want to chime in with regards to the branding. my advice is not to call this Monero 2/2.0/NG, or anything like that.

I've witnessed how this renaming went in Ethereum since 2018. the coming upgrades under the Serenity banner were/are so fundamental that the effort was dubbed Ethereum 2.0 or Eth2. looked like an excellent idea. but the confusion it created was understood only after it widely proliferated into the public. people outside the technical circles became unsure: "is this a new chain? will this be a new cryptocurrency? will I have to buy ETH2 to use the new system? will I be able transfer my ETH to the new chain? will I *have to*? will Ethereum 1.x stop once Ethereum 2.0 starts?" and so on. the answer to all those is that they won't have to do anything, but the bad naming introduced all these doubts. scam tokens claiming to be "ETH2" popped up. it also brought up the question of serialization -- when another fundamental change occurs in the future, will that be called Ethereum 3.0? how far can you take that? at which number will it look embarrassing enough to abandon the scheme?

to try to reverse this damage, the whole Eth1/Eth2 terminology was recently [abandoned](https://blog.ethereum.org/2022/01/24/the-great-eth2-renaming/) and that created the additional big task of having to rename everything.

my main point is that the human mind values reliability and continuity over implementation details. Seraphis+Jamtis will be a complete technological overhaul, it *will* be a new era for developers, so it's attractive to acknowledge that work by using a new name. but to users, this will be another hard fork. sure, it will be more rocky because (if my understanding is correct) they will need to generate new addresses if they have addresses shared with people or published online and want to continue to receive XMR that way. but what really matters to them is that it's a hard fork from the same group they've been receiving forks from for 8 years, the network will have the same participants, and their sweet moneroj will remain unchanged in their wallets, with 1 XMR =  1 XMR.

also, suffixing "Monero" with anything can easily trigger people's [affinity scam](https://www.cryptocompare.com/coins/guides/monero-quick-rundown-of-monero-s-various-hard-forks/) PTSD.

## UkoeHB | 2022-01-26T22:16:45+00:00
Maybe the title should just be `Make Sure Our Wallets Survive the Seraphis Fork`.

# Action History
- Created by: rbrunner7 | 2022-01-25T16:55:54+00:00
