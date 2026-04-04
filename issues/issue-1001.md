---
title: 'Seraphis wallet workgroup meeting #69 - Monday, 2024-05-06, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1001
author: rbrunner7
assignees: []
labels: []
created_at: '2024-05-03T16:57:59+00:00'
updated_at: '2024-05-06T19:38:30+00:00'
type: issue
status: closed
closed_at: '2024-05-06T19:38:30+00:00'
---

# Original Description
On Monday, November 14 2022, we started with regular weekly meetings of the Seraphis wallet workgroup, and all interested parties from the community that want to join. Time is 18:00 UTC on each Monday. "Location" is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting here: https://github.com/monero-project/meta/issues/997

# Discussion History
## plowsof | 2024-05-06T07:19:02+00:00
If appropriate could the seraphis general paper [ccs.getmonero.org](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/441) review be mentioned and if the release of CypherStacks GBP paper [monerologs.net](https://libera.monerologs.net/monero-research-lab/20240503#c372182) effects it in anyway? https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/441

## rbrunner7 | 2024-05-06T19:38:30+00:00
````
<r​brunner7:> Meeting time. Hello! https://github.com/monero-project/meta/issues/1001
<jberman> *waves*
<s​needlewoods:> hey
<o​ne-horse-wagon:> Hello.
<d​angerousfreedom:> Hello
<r​brunner7:> So what happened last week?
<s​needlewoods:> I began to implement `WalletSettings` and tried to come up with unit tests for simple testing of functions in `api/wallet.h`, I got stuck a few times so there is not much done yet.
<s​needlewoods:> Here is the code so far, I'd say it's an experimental construction site, but early feedback could help, before I move too far in the wrong direction: https://github.com/UkoeHB/monero/compare/seraphis_lib...SNeedlewoods:seraphis_wallet:x_feature_complete_api_1
<d​angerousfreedom:> From my side I will keep implementing things in the following structure: wallet3_interface->wallet3_implementation->wallet3_cli.
<d​angerousfreedom:> It was interesting to see the birth of wallet2_api here: https://github.com/monero-project/monero/pull/728 and fluffypony comment on it "Ok so then I would suggest we aim at deprecating wallet2 later on in favour of this new API, so please try keep it as flexible and well documented as possible:)" 03/2016.
<d​angerousfreedom:> I also just saw that Koe merged jeffro's PR to make the serializations shorter (thank you both for working on that). I will work again on the EnoteStore serialization now.
<r​brunner7:> Interesting find, dangerousfreedom
<r​brunner7:> It will be *much* later :)
<jberman> update: updated the async wallet scanner from koe's comments, starting fcmp integration this week
<r​brunner7:> What's that, more or less, "FCMP integration"? What will you work on there first?
<j​effro256:> howdy
<jberman> implement the tree and grow algorithm in C++ (when you construct a tx, the node calls grow to add the constructed enotes to the tree)
<d​angerousfreedom:> Great that it will be in c++ :p
<jberman> (not exactly at tx construction-time -- it's described in section 6 of this paper here: https://github.com/kayabaNerve/fcmp-ringct/blob/develop/fcmp%2B%2B.pdf)
<j​effro256:> Seems like the first layer is still being actively debated though, what are you planning on putting on there?
<k​ayabanerve:> Hello, sorry for being late
<r​brunner7:> Hmm, did we lose jberman already in the cracks between Matrix servers and IRC bridges?
* jeffro256 (~jerfo@static-198-44-128-185.cust.tzulo.com) has joined
<k​ayabanerve:> The tree benefits extensively from pointers. I've prior done it in Rust, yet so long as it's extensively reviewed *and since it needs DB access*, I support it in C++.
<k​ayabanerve:> <a data-mention-type="user" href="https://matrix.to/#/@jeffro256:" contenteditable="false">@jeffro256</a> First layer is either O.x I.x I.y C.x or O.x I.x C.x. I'm moving forward on the latter.
<j​effro256:> w/o ristretto or ristretto variants?
<k​ayabanerve:> But because it's a one element difference, I don't expect too much pain to change our minds.
<k​ayabanerve:> Without Ristretto. I'll clarify I never endorsed it (and am not making drastic changes constantly) and it was solely an idea being reviewed. Even if we agreed it was a good idea, I said I'm unsure we have the development capacity. It's now been found to be only marginally better and not worth the complexity.
<j​effro256:> SNeedlewoods: what's the main goal of `WalletSettings`0?
<j​effro256:> So we're doing mul8 on the key images into the tree, or are we doing permissibility at time of output verification?
<s​needlewoods:> I'm following jbermans suggestion from here https://github.com/seraphis-migration/wallet3/issues/64#issuecomment-2070568200 (if I didn't misunderstand)
<r​brunner7:> Yeah, I wanted to study that approach, and then comment about it, but did not yet come around to do it ...
<jberman> (not lost, I was planning to start with lmdb table design fwiw)
<r​brunner7:> But I think that there is enough "options stuff" to merit a nice little class is pretty clear for a long time already, if you ask me
<k​ayabanerve:> <a data-mention-type="user" href="https://matrix.to/#/@jeffro256:" contenteditable="false">@jeffro256</a> Key images don't go into the tree.
<jberman> ya that approach is pretty much what I had in mind there
<j​effro256:> Sorry, key image generators
<k​ayabanerve:> We're sending keys and commitments inv 8, then doubling thrice for new outputs. Old outputs are torsion cleared.
<k​ayabanerve:> Key image generators are already prime order and aren't affected.
<k​ayabanerve:> Also, sorry for the @ which was HTML spamming. I forgot about that and will try to not ping people as such.
<r​brunner7:> Spontanious question: You intend to switch from *output* to *enote* as term for your code as well, kayabanerve ?
<r​brunner7:> Little detail, but still.
<k​ayabanerve:> That seems loaded.
<k​ayabanerve:> I did not intend to. Are you asking me to?
<r​brunner7:> Well, for our Seraphis work, we once agreed to follow Koe's lead there and make the terminology switch. Seemed to make sense, IMHO.
<k​ayabanerve:> And could you further comment the distinction in definition?
<r​brunner7:> Not sure what you mean. *enote* is the thing. *output* and *input* become terms merely to express how the enote gets actually used in the case at hand.
<k​ayabanerve:> What thing?
<k​ayabanerve:> Please define enote
<r​brunner7:> Probably exactly what you now call *output*.
<k​ayabanerve:> So an enote is a positioned tuple of a spend key, a generator for its linking tag, and an amount key?
<k​ayabanerve:> Emphasis on positioned. Two tuples with matching elements are not equivalent. They're solely interchangeable.
<r​brunner7:> I am already out of my depth here. Wasn't expecting that it's unclear what the term *output* is used so far in the Monero codebase.
<jberman> https://github.com/UkoeHB/monero/blob/c7422607385a070d9e0069f96598be78336f1ef8/src/seraphis_core/legacy_enote_types.h#L106-L142
<k​ayabanerve:> I'd define an output as its core, a key determining how it's spent/linked, a key image generator, and an amount commitment.
<k​ayabanerve:> A Monero TX has its own structure to communicate and create said outputs.
<r​brunner7:> I wrote this once: https://github.com/seraphis-migration/wallet3/issues/1
<k​ayabanerve:> jberman: The inclusion of a view tag there is irrelevant IMO. I don't care to spend the next hour being opinionated on what isn't my code however.
<j​effro256:> Well as i understand it is that the term "enote" is used as a term to describe the "noun" of what we formerly called "tx outputs" in isolation, so when we use the term "input" or "output", we know its use case in that context. Whereas before, an "output" is also sometimes an "input" as also sometimes a "decoy", etc
<k​ayabanerve:> Though I'm unsure why view tag is there. It doesn't help with scanning without additional data anyways.
<k​ayabanerve:> I think my hot take is they should still be outputs as the transaction should simply wrap outputs into a communicable format, additionally providing proofs and scan assistance.
<j​effro256:> It's there since the current tx format guarantees a 1-to-1 relationship of outputs to view tags, whereas that isn't true with ephemeral pubkeys in tx_extra
<r​brunner7:> The proposal to retire the term *output* for new code and replace it with *enote* has very few technical aspects, if any at all. The same "thing" or "things" are named. It just shall be a better i.e. more descriptive term, and less prone to misunderstanding.
<k​ayabanerve:> It's fine if that's disagreed with. You're welcome to consider output tuples enotes.
<jberman> eh, probably should have linked this then: https://github.com/UkoeHB/monero/blob/c7422607385a070d9e0069f96598be78336f1ef8/src/seraphis_main/enote_record_types.h#L104-L124
<k​ayabanerve:> jeffro256: Yeah, but both should be kicked to a scan data struct, I say as someone who didn't work on that code and didn't participate in these discussions.
<r​brunner7:> Not sure what you mean with "consider". I try to win you over to use the term for naming classes, variables, parameters and so in the code you write.
<jberman> I think it's fine as is considering the 1-to-1 relationship
<k​ayabanerve:> I'm having personal problems and will for now primarily apologize and ask jberman to keep enote in mind for their work on integration into Monero.
<jberman> *thumbs up*
<jberman> jeffro256 do you have thoughts on the wallet settings class idea?
<r​brunner7:> Hell, yeah, don't let us get into a tussle about something like that :)
<j​effro256:> we still use the term "output" when an enote is in its creation context: the output of a transaction. But once's its on the chain, it becomes its own referencable thing outside of its tx, and can be used as an "input" to a proof of another tx. We can also have enote data that isn't tied to a specific transaction in fakechains, enote records, etc, so isn't correct to call it an "ou<clipped mess
<j​effro256:> tput" in that context. Idk, to me, it's made it a ton easier to call the "thing" an e-note (like a dollar bill that holds information), and then use the terms "input" and "output" like contextual adjectives
<sneedlewoods> +1
<j​effro256:> That's all I'll say on that issue
<j​effro256:> jberman: yeah it would be nice to group the information we need to load a wallet that is NOT contained in the cache
<jberman> yep yep
<r​brunner7:> Why not group options as contained in the .keys file as well in a class?
<r​brunner7:> In today's .keys file of course
<jberman> The options in the .keys file I also would think fall under the category of "Wallet Settings"
<j​effro256:> should the PR be on the seraphis_lib or seraphis-migration repo? (So we can avoid jumping back and forth)
<jberman> There's a further distinction between run-time settings (command line args), and the ones saved in the .keys file, that I do think is worth separate classes also
<r​brunner7:> Seems to me to be the latter, as it's probably wallet stuff, no?
<j​effro256:> agreed
<r​brunner7:> Yes, why not two clearly separated classes
<j​effro256:> .keys settings already have a class: `wallet2_basic::keys`
<r​brunner7:> Hmm, but that's just the "compatibility thing" :)
<s​needlewoods:> iirc someone suggested that some of the code could be PR'd directly into monero-project so wallet devs get early access
<r​brunner7:> Ah, yes, right, if it gets part of `wallet2_api`. Does it?
<r​brunner7:> I mean that option stuff we discuss right now
<k​ayabanerve:> If there's a moment, I can give my own update. I don't want to intrude on an existing ongoing conversation though.
<s​needlewoods:> I put the changes in `api/wallet.h` so far, because I don't quite understand `wallet2_api` tbh
<s​needlewoods:> I'm fine with hearing your update kayaba
<r​brunner7:> Yes, shoot :)
<jberman> where's wallet2_basic::keys again
<k​ayabanerve:> I have worked the past week or so on FCMP++s, and probably put in... 100 hours?
<r​brunner7:> Should be somewhere in "our" repo
<j​effro256:> seraphis-migration/seraphis_wallet
<k​ayabanerve:> It's extremely hard to bench mark reliably. My implementations of Helios and Selene didn't yield usable numbers when I tried benchmarking them. I got 50x slower multiexp, 3x slower point arithmetic, yet 4x faster field arithmetic.
<k​ayabanerve:> If we assume tevador's impl, which they did say is on their TODO list, achieves 2x across the board, we are at 20% faster my original expectation for a batch of 10.
<j​effro256:> Is the code public rn? You could solicit benchmark runs from multiple entities. I'd be willing to run it
<k​ayabanerve:> I'm hopeful the final result gets quite faster, yet I don't want to over promise.
<k​ayabanerve:> GBPs were proven and move to obtaining review. I have a specific candidate for that. The GBP lib is implemented, yet needs to be moved to GGBP (the version proven). Then, with more tests, it can move to auditing so long as we don't believe further optimizations will be so intrusive.
<r​brunner7:> Crypto noob asks whether it isn't very bad if something takes 50 times longer?
<k​ayabanerve:> I've solicited various parties for reviewing our application of divisors and have a pair of meetings tomorrow I believe.
<j​effro256:> (Gigachad Generalized Bullet-proofs)
<SyntheticBird> +1
<sneedlewoods> +1
<k​ayabanerve:> rbrunner7: Not when we're currently there meaning we're looking at becoming 50x faster?
<plowsof> i was wondering where the new GBP paper puts the general seraphis paper review ccs proposal + on that note, for visibility: jbermans new ccs proposal is up (alot of seraphis/fcmp/core goodies in there) https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/453
<k​ayabanerve:> Except we aren't, that's not plausible. I'd hope for 3-5x in total.
<jberman> ah ya forgot to mention
<plowsof> :D
<k​ayabanerve:> jeffro256: Generalized Generalized :p GBP added support for PVCs over G bold, GGBP realized you also get PVCs over H bold and GBP is just the case where you ignore those H bold terms.
<r​brunner7:> Yes, plowsof suggested we talk about the Seraphis review CCS in today's meeting. That's this here: https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/441, but well, maybe we run out of time. Unless it's pretty clear we should put that on hold now.
<k​ayabanerve:> I asked jberman to clarify what they aren't doing in the list of everything they are.
<k​ayabanerve:> The list of what they're doing is so long it's difficult to track what is left out.
<r​brunner7:> What do people think, with all the things that FCMP++s put in motion, starting a "Seraphis pure" review probably does not make much sense, right?
<k​ayabanerve:> rbrunner7: Considering how well and expedient FCMP++ dev has been, and priorities shifting with it, I'd agree.
<jberman> That list should cover everything, but I'm not taking claim on all the tasks there except the ones I'm guaranteeing for my CCS. I'll work on the others too unless others want to take some of it
<k​ayabanerve:> It doesn't have 6.8
<s​yntheticbird:> If the GF can't afford a redundant review, there are not much of a point at reviewing "Seraphis Pure"
<plowsof> if the stance is to not review seraphis then surely all sponsored seraphis work should cease? or
<k​ayabanerve:> I also don't remember 6.8 off the top of my head after spending so much time 7.9.2.d paragraph 5 /s
<jberman> ah right, OVK's + forward secrecy
<k​ayabanerve:> At this point in time, I support the FCMP++ protocol and the Seraphis codebase plowsof. That is my opinion.
<jberman> seemed like a second-pass after integration thing
<r​brunner7:> plowsof: Things are pretty mixed up. What is work on a new wallet? Is that now Seraphis or not? I think even if we will, in the end, kill Seraphis outright, there is much to do.
<jberman> also didn't plan to include "downloading the complete tree when scanning" on first implementation
<k​ayabanerve:> That's delineating Seraphis as the new key/linking tag format vs all the dev work that's been done. Of FCMP++s continue as-is, I see no reason to force the migration which isn't incredibly minor.
<plowsof> ah yes, understood rbrunner thanks
<k​ayabanerve:> jberman: wallet support for those? Agreed
<r​brunner7:> Ok, whathever confusion we produce here today, I am pretty sure nobody wants to push that Seraphis pure review to funding ASAP :)
<r​brunner7:> If somebody still does please contradict me now.
<k​ayabanerve:> I have work I'd like done through CS so I'm additionally fine on that note.
<j​effro256:> The potential benefit that Seraphis could being is being more performant
<j​effro256:> *bring
<k​ayabanerve:> (fine not moving forward with Seraphis review)
<r​brunner7:> By the way, I am always a bit uneasy if I hear that somebody does intense dev work for maybe 100 hours a week. Please be careful people, nobody wants anybody to burn out.
<jberman>  personally I would like to prioritize FCMP's via CS fwiw
<k​ayabanerve:> jeffro256: My work beats squashed enotes as-is.
<k​ayabanerve:> Unsquashed enotes it does not. Unsquashed enotes have one less leaf element than FCMP++s, and maybe 10-20 less rows in the inner product statement. That isn't notable.
<k​ayabanerve:> You'd have to be betting on future research being more performant with Seraphis in ways inapplicable to the FCMP++ design.
<k​ayabanerve:> (input range proofs are more expensive than multi-set membership)
<k​ayabanerve:> (and multiple rerandomizations)
<k​ayabanerve:> rbrunner7: I did it because I was burned out with my primary work :D I return to working 16 hours a day on that today or tomorrow.
<k​ayabanerve:> Thank you for your concern though.
<r​brunner7:> Alright :) We are already past the hour. Any important last minute thing for this very meeting?
<s​needlewoods:> Not really important, just want to say that I'll continue with `WalletSettings` and I don't expect a review, but some feedback in the next days, if it's going the right direction would be really appreciated
<s​needlewoods:> thanks for the meeting everyone
<d​angerousfreedom:> So we are finally leaning towards implement [jamtis-rct](https://gist.github.com/tevador/d3656a217c0177c160b9b6219d9ebb96) instead of [jamtis](https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d17024) ?
<d​angerousfreedom:> So we are finally leaning towards implementing [jamtis-rct](https://gist.github.com/tevador/d3656a217c0177c160b9b6219d9ebb96) instead of [jamtis](https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d17024) ?
<r​brunner7:> Maybe, maybe not, who really knows that right now :)
<r​brunner7:> With so many things in flux
<d​angerousfreedom:> I couldnt have time to look at it yet but it would definitely impact seraphis and its implementation
<r​brunner7:> Sure, all this uncertainty does not make dev work exactly easy. I hope this phase will pass within a reasonable time frame
<r​brunner7:> Ok, thanks everybody for attending. Interesting times indeed. Read you again next week!
<d​angerousfreedom:> The great thing is that it is backwards compatible
<d​angerousfreedom:> So yeah I think we should decide the addresses scheme and protocol before doing the seraphis review
<d​angerousfreedom:> Thanks rbrunner7
<j​effro256:> Mainly it would affect the onetime address recomputation and key image derivation steps, so not API related
<d​angerousfreedom:> Yeah, but I mean these parts should also be in the 'seraphis review' when someone does it
````


# Action History
- Created by: rbrunner7 | 2024-05-03T16:57:59+00:00
- Closed at: 2024-05-06T19:38:30+00:00
