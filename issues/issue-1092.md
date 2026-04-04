---
title: Monero Research Lab Meeting - Wed 16 October 2024, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1092
author: Rucknium
assignees: []
labels: []
created_at: '2024-10-15T17:35:16+00:00'
updated_at: '2024-10-29T21:06:00+00:00'
type: issue
status: closed
closed_at: '2024-10-29T21:06:00+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

[Join the Monero Matrix server if you don't already have a Matrix account.](https://web.archive.org/web/20230128130949/https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211027T170000&p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3. Research [Pre-Seraphis Full-Chain Membership Proofs](https://www.getmonero.org/2024/04/27/fcmps.html). Reviews for [Carrot](https://github.com/jeffro256/carrot/blob/master/carrot.md).

4. CCS proposal: [Audit monero-serai and monero-wallet](https://gist.github.com/kayabaNerve/3723d0a3f2b62ef8ef00c0c4a574fb8e)

5. Monero Research Computing Server hardware needs.

6. Reviving the [MRL research bulletin/technical note paper series](https://www.getmonero.org/resources/research-lab/).

7. Any other business

8. Confirm next meeting agenda


Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#1090 

# Discussion History
## Rucknium | 2024-10-17T15:54:52+00:00
Logs:

> __< r​ucknium:monero.social >__ Meeting time! https://github.com/monero-project/meta/issues/1092     

> __< r​ucknium:monero.social >__ 1) Greetings     

> __< t​obtoht:monero.social >__ hi     

> __< c​haser:monero.social >__ hello     

> __< b​oog900:monero.social >__ Hi     

> __< v​tnerd:monero.social >__ Hi     

> __< j​berman:monero.social >__ *waves*     

> __< j​effro256:monero.social >__ howdy     

> __< r​ucknium:monero.social >__ 2) Updates. What is everyone working on?     

> __< k​ayabanerve:monero.social >__ 👋     

> __< k​ayabanerve:monero.social >__ FCMP++ stuff for jberman.     

> __< j​berman:monero.social >__ wallet sync for fcmp++     

> __< j​effro256:monero.social >__ Carrot shtuff     

> __< v​tnerd:monero.social >__ Fixed LWS bug, working on more http async stuff for lws, and a bit of work on span code in daemon     

> __< r​ucknium:monero.social >__ Posted summary for Milestone 1 of my statistical research CCS: https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/439#note_26679 . Now working on OSPEAD.     

> __< rbrunner >__ Hello. A bit late, but here     

> __< 0​xfffc:monero.social >__ Hi everyone.     

> __< r​ucknium:monero.social >__ rbrunner: Was it because I posted only one hour notice for the meeting instead of two? :P     

> __< rbrunner >__ :) No, mea culpa     

> __< r​ucknium:monero.social >__ 3) Research Pre-Seraphis Full-Chain Membership Proofs. Reviews for Carrot. https://www.getmonero.org/2024/04/27/fcmps.html  https://github.com/jeffro256/carrot/blob/master/carrot.md     

> __< r​ottenwheel:kernal.eu >__ OSPEAD... Cue meme gif... It's been 84 years.     

> __< j​effro256:monero.social >__ The CCS for Carrot review got merged, congrats Cypherstack!     

> __< r​ottenwheel:kernal.eu >__ Hopefully getting some news on that front soon! We know you've been busy with other stuff, not pissing on it. Just saying it has been long since we last got anything on it. 👍     

> __< r​ottenwheel:kernal.eu >__ 🚀👍     

> __< 0​xfffc:monero.social >__ Finished dynamic-span and dynamic-bss, going through review. Will push few minor updates I have this week ( rpc limit fix, and a PR related to public-node flag )     

> __< r​ucknium:monero.social >__ Here is the Carrot review CCS for reference: https://ccs.getmonero.org/proposals/cypherstack-carrot-spec-review.html     

> __< j​effro256:monero.social >__ Throwing the idea out there to have the GF help fund the review. Good idea or bad idea?     

> __< r​ucknium:monero.social >__ Do we want to talk about the custom lock time outputs and FCMP?     

> __< j​effro256:monero.social >__ Yes     

> __< j​berman:monero.social >__ yes     

> __< r​ucknium:monero.social >__ Discussion begins here: https://github.com/monero-project/research-lab/issues/78#issuecomment-2415324570     

> __< j​effro256:monero.social >__ I'll publish that script to determine the running size of the wallet locked output cache today btw, I fell asleep coding it last night haha     

> __< j​berman:monero.social >__ Feeling a pretty solid "rough consensus" on removing custom timelocks     

> __< r​ucknium:monero.social >__ `git blame` really earns its name with this "feature".     

> __< j​berman:monero.social >__ I figure that comment should be enough to move it over the goal line for the fcmp++ fork: to remove a dos vector / vector to slow down scanning under fcmp++     

> __< j​effro256:monero.social >__ I'm in favor of making a public announcement to stop honoring custom timelocks after height X in the FCMP hard fork, and not actually soft forking now     

> __< k​ayabanerve:matrix.org >__ I support removing timelocks entirely at the fork due to concerns re: wallets.     

> __< rbrunner >__ Which variant is currently favored - not honoring *any* timelocks, starting at genesis block, or only honoring them up to a fixed height X?     

> __< k​ayabanerve:matrix.org >__ NACK, I'm not in favor of invalidation at this time.     

> __< r​ucknium:monero.social >__ I also support removing the ability to create new custom time locks at the next hard fork.     

> __< j​berman:monero.social >__ ya can you clarify the approach there jeffro256 ? do you mean that a tx currently in the chain with timlock set to unlock past X is now unlocked at X?     

> __< j​effro256:monero.social >__ Let me be clear: not invalidating currently on-chain timelocks, just ignoring non-zero unlock times for *future* outputs that have yet to be created when building the FCMP tree     

> __< rbrunner >__ Yeah, I think that pretty much consensus. I would not feel too good however stopping to honor any existing locks at all.     

> __< j​berman:monero.social >__ makes more sense, I misunderstood     

> __< rbrunner >__ Oh, there are two questions. Whether allowing new timelocks, or not, starting at a given height. And, not honoring locks anymore that would only expire past some horizon, block X.     

> __< k​ayabanerve:matrix.org >__ Tbf, I'm in favor of timelock invalidation when we do a PQ migration.     

> __< j​berman:monero.social >__ one quasi-issue with the approach to consider is that a miner (or someone who can get their txs to a miner running a daemon wtihout the relay rule) can spam timelocks up until the fork, which would still affect wallet scanning     

> __< j​effro256:monero.social >__ So for example, in your unlock_time -> unlock_block_index function, adding an `if` branch that says if the output creation block index is greater than 3300000 (a height which doesn't exist yet as of the time of this writing), then always use the default unlock block index     

> __< j​berman:monero.social >__ soft fork gives us the full knowledge of how many timelocks there will be at time of fcmp fork     

> __< k​ayabanerve:matrix.org >__ Because of that, it doesn't really hurt to get it over with now for the 0.001% affected.     

> __< j​effro256:monero.social >__ Yes miner's can still spam locked outputs     

> __< k​ayabanerve:matrix.org >__ I wouldn't ignore. I'd require 0     

> __< rbrunner >__ I am not sure I understand what you mean with "soft fork"     

> __< j​effro256:monero.social >__ Ignoring after height X would also let you know how many locked outputs before the actual deployment of the code     

> __< j​effro256:monero.social >__ rbrunner: restricting the content of transactions to things already allowed is a soft fork, not a hard fork     

> __< j​berman:monero.social >__ a soft fork that stops allowing future timelocked txs to be created at height X, before the fcmp fork     

> __< k​ayabanerve:matrix.org >__ It seems like we all agree on requiring timelock 0 at the fork. The question then becomes relay rules/soft forks/invalidation. I support relay rules over a soft fork.     

> __< j​berman:monero.social >__ we already have relay rules in place     

> __< rbrunner >__ Yes. It's already pretty difficult to put custom locks.     

> __< j​berman:monero.social >__ "Ignoring after height X would also let you know how many locked outputs before the actual deployment of the code" -> I don't follow this. The code would be deployed before the fork height     

> __< j​effro256:monero.social >__ I will say though, that during the fork to enforce zero unlock times, we could also integrate tevador's intermediate hash changes. This would turn it into a hard fork, but gives us extra time to mitigate problems that arise with the intermediate hash if they exist before the FCMP hard fork     

> __< k​ayabanerve:matrix.org >__ Are the relay rules for all timelocks or just time-based timelocks?     

> __< k​ayabanerve:matrix.org >__ I thought solely the latter     

> __< j​effro256:monero.social >__ For example, we could announce the ignore height to be 3300000 beforehand. Then, after height 3300000 we do analysis of existing time locked outputs. Then we plan FCMP hard fork for 3500000 and deploy sometime around block 3400000. So in order: announcement, ignore height hits, analysis, code deployment, hard fork activation     

> __< j​effro256:monero.social >__ All time locks     

> __< j​berman:monero.social >__ ah I see, that makes sense     

> __< j​effro256:monero.social >__ Coinbase transactions require non-zero unlock times, but the relay rule won't touch them     

> __< j​berman:monero.social >__ +1 to that approach from me     

> __< rbrunner >__ Unfortunately I am still not fully sure what people mean with "ignore height". Say, 2 years ago a made a transaction to unlock at block 5,000,000. When will it be free, according to proposals?     

> __< rbrunner >__ At an earlier "ignore height", or at 5,000,000 in any case?     

> __< j​berman:monero.social >__ With that approach: it's unaffected, still 5,000,000. Only *new* outputs created past the ignore height would be affected     

> __< r​ucknium:monero.social >__ So the proposed threat model is that there is an adversary that would spam locked outputs between now and the FCMP hard fork, yet would not spam locked outputs between the announcement and "height 3300000".     

> __< k​ayabanerve:matrix.org >__ Ah. Ignore w.r.t. accumulation. ACK.     

> __< j​effro256:monero.social >__ Any output *created* before the ignore height would have its unlock time respected in perpetuity. Any output *created* after that height is not guaranteed to have it's unlock time respected     

> __< j​berman:monero.social >__ fwiw even if they were to spam, it wouldn't be the end of the world. it would just take more analysis to be sure it's still ok     

> __< r​ucknium:monero.social >__ By "spam txs" I mean create the txs and somehow get around the relay rules to get the txs confirmed in mined blocks.     

> __< rbrunner >__ I see, thanks. I would be in favor of a blockheight pretty soon that stops to honor new locks, eventually. If we just keep "social contracts" in force earlier.     

> __< rbrunner >__ So there is not much to spam.     

> __< j​berman:monero.social >__ so to answer your question Rucknium yes, but this approach can yield 100% confidence wallets will sync smooth given whatever an adversary does     

> __< c​haser:monero.social >__ is anyone monitoring the growth of time-locked outputs? do we have an idea how sensitive this seems to be currently?     

> __< rbrunner >__ I mean, we could announce such a height today, right? Technically, no need to wait until the software is ready?     

> __< j​effro256:monero.social >__ I will released a script today to have the exact number at each step of the sync     

> __< j​berman:monero.social >__ in the worst case, wallets have to download 2x data for timelocked outputs     

> __< j​effro256:monero.social >__ rbunner: yup, exactly     

> __< j​berman:monero.social >__ 72 bytes extra per timelocked output*     

> __< rbrunner >__ I finally got it :)     

> __< c​haser:monero.social >__ given what we were showered this year, I agree with rbrunner, the sooner more obstacles are deployed, the better     

> __< c​haser:monero.social >__ *showered with     

> __< j​berman:monero.social >__ thank you jeffro256     

> __< c​haser:monero.social >__ great, thank you!     

> __< rbrunner >__ It's a bit unsual regarding forking customs, however, such an announcement ...     

> __< r​ucknium:monero.social >__ Well, isn't there a concern about centralisation of development? This topic wasn't even explicitly on today's agenda. And was just brought up less than 24 hours ago.     

> __< j​berman:monero.social >__ we're here doing the discussion now. can let the idea of this proposed announcement marinate longer for its "rough consensus"     

> __< k​ayabanerve:matrix.org >__ Not when it's a DoS causing the harsher crackdown of an already planned and agreed to crackdown (we have a relay rule).     

> __< c​haser:monero.social >__ Rucknium I don't see an issue with that. new ideas enter these conversations organically.     

> __< k​ayabanerve:matrix.org >__ I'm not saying it needs action overnight, I'm saying timelocks are at their end.     

> __< rbrunner >__ I think such an announcement does not make "centralization" worse. Even if we pre-announce all kinds of things about our next release, people are free to ignore it, as they ever were.     

> __< j​effro256:monero.social >__ I don't plan to decide the height today, but the announcement only *means* anything when the FCMP code is introduced. It's basically just a nicety to manage expectations for the future hard fork. If people don't merge the FCMP code into their daemons in the future, then the announcement means nothing to them. In other words, I think it has the same centralization implications as n<clipped messag     

> __< j​effro256:monero.social >__ ormal Monero hard forks     

> __< k​ayabanerve:matrix.org >__ If we tweak how they're at their end, I don't think we need months of work.     

> __< j​berman:monero.social >__ there's also years of "rough consensus" building to remove timelocks, this is the discussion on "how"     

> __< k​ayabanerve:matrix.org >__ Besides, deciding an ignore date isn't final. It's still a pending decision till the time of fork.     

> __< rbrunner >__ Wouldn't rule out that tomorrow it starts raining timelocked txs, just to mock us :)     

> __< j​effro256:monero.social >__ That'd suck ;) But IMO announcing a soft fork to remove unlock times for the exact same reason could just as easily trigger a malicious actor to precipitate that action up until the point of the fork     

> __< k​ayabanerve:matrix.org >__ IRC in TX extra D:     

> __< k​ayabanerve:matrix.org >__ We could say all timelocks from after this meeting will be ignored.     

> __< r​ucknium:monero.social >__ "Besides, deciding an ignore date isn't final. It's still a pending decision till the time of fork." This statement does not remove the centralisation of development concern. Makes it worse. At any time a small group of devs could decide what outputs are spendable and unspendable.     

> __< c​haser:monero.social >__ jeffro256 exactly.     

> __< rbrunner >__ "At any time a small group of devs could decide what outputs are spendable and unspendable" Well, it ever was like that, no? At least as a possibility.     

> __< 0​xfffc:monero.social >__ I don’t have enough information to discuss technical intricacies of such decisions. But wouldn’t it be better, if we decide to do it, do it in hardfork?     

> __< j​berman:monero.social >__ no one has made any decision yet? we are signalling support for a technical idea that makes sense for people to consider?     

> __< rbrunner >__ It always was a pretty small group of devs bringing out releases, after all.     

> __< k​ayabanerve:matrix.org >__ May I posit it this way?     

> __< k​ayabanerve:matrix.org >__ We already have consensus on ending time locks.     

> __< k​ayabanerve:matrix.org >__ Due to a DoS, it makes sense to potentially ignore some timelocks, anywhere from none to all timelocks after this meeting.     

> __< k​ayabanerve:matrix.org >__ We will decide at the hard fork which will have the expected community consensus process.     

> __< k​ayabanerve:matrix.org >__ The question is how do we want to make the community aware of this discussion and can we provide a firm estimate for which block we'll ignore timelocks from?     

> __< k​ayabanerve:matrix.org >__ Instead of the handwavy discussion of 'may or may not be invalidated at any point after this'     

> __< r​ucknium:monero.social >__ I'm not really against it. I'm just saying it has some centralisation downsides that should be brought up. Everything is a tradeoff.     

> __< k​ayabanerve:matrix.org >__ We're not planning a final decision in this meeting and doing a hard fork tonight.     

> __< j​effro256:monero.social >__ Well yes, in the technical sense, the behavior of the spendability only changes after hard fork activation. The decision on the height isn't actually finalized until the fork code is accepted by nodes. The announcement is just a management of expectations, although it does signal a break in way that unlock_times are respected for a subset of transactions that *may* exist in the future     

> __< rbrunner >__ Rucknium: It sure does shine a bright light on centralization issues that so far were mostly left out of limelight, but always existed, and that may turn into a problem     

> __< rbrunner >__ IMHO     

> __< r​ucknium:monero.social >__ We need to get to the next agenda item at least. Usually it's best to put the longest, most involved item last on the agenda, but I failed here :D     

> __< j​berman:monero.social >__ I guess individuals should probably just never propose / discuss ideas to limit dos concerns? I don't understand this downside / discussion     

> __< r​ucknium:monero.social >__ Let's do the next agenda item, then we can come back to this to maybe get to a rough consensus     

> __< k​ayabanerve:matrix.org >__ I think this can be argued as HF planning and HF community consensus is as it always has been. I'm not too concerned about centralization here so long as any announcement on ignoring timelocks is properly worded.     

> __< k​ayabanerve:matrix.org >__ Rucknium: oh I can take even more time with my topic     

> __< k​ayabanerve:matrix.org >__ I won't leave you as having failed     

> __< j​effro256:monero.social >__ Yes I do appreciate Rucknium for bringing the centralization issue, it shouldn't be taken lightly. My gut reaction is that it isn't *more* of a centralization issue than a regular hard fork, but I will certainly think about it     

> __< j​berman:monero.social >__ (in this context I don't understand it)     

> __< r​ucknium:monero.social >__ 4) CCS proposal: Audit monero-serai and monero-wallet https://gist.github.com/kayabaNerve/3723d0a3f2b62ef8ef00c0c4a574fb8e     

> __< t​obtoht:monero.social >__ A multisig implementation is useful for user-facing wallet applications if sensible UX can be built around it.     

> __< t​obtoht:monero.social >__ This has turned out be quite difficult to achieve with monero's current multisig code, for reasons in part because of inherent issues like its O(n!) complexity. Other problems are message transport, state management, UX design, recovery and handling of failure modes, and the mess that is wallet2.     

> __< t​obtoht:monero.social >__ I haven't looked at this library or the FROST spec in detail yet, however the reduction in complexity, formalization of a standards-based protocol, as well as modularization of the code are all very welcome improvements.     

> __< t​obtoht:monero.social >__ I have some questions (feel free to answer after the meeting):     

> __< t​obtoht:monero.social >__ - Does this implementation require the use of a multisig-aware coordinator?      

> __< t​obtoht:monero.social >__ - Does this library define a standard message format (so messages can be passed to other participants or a coordinator)?     

> __< t​obtoht:monero.social >__ - Is there a potential path for `wallet2`-based applications to use this library specifically for multisig? (Just wondering if you see any problems with wallet projects adapting wallet2 to use this library.)     

> __< t​obtoht:monero.social >__ - Does `monero-wallet` manage state or are wallets expected to handle this?     

> __< t​obtoht:monero.social >__ - For my understanding of the library, are there any tests or documentation that show how a wallet would use this library to set up a multisig wallet and create a transaction proposal?     

> __< t​obtoht:monero.social >__ - Does FCMP++ require changes to the library, and if yes, would it make sense to audit once those changes are ready?     

> __< t​obtoht:monero.social >__ Some (minor) comments:     

> __< t​obtoht:monero.social >__ A link to monero-serai and monero-wallet in the gist would have been helpful, it took me a moment to find where these repositories live.     

> __< t​obtoht:monero.social >__ For reference: https://github.com/serai-dex/serai/tree/develop/networks/monero and https://github.com/serai-dex/serai/tree/develop/networks/monero/wallet     

> __< t​obtoht:monero.social >__ The "monero-wallet" name is a bit unfortunate, as "It also won't act as a wallet, just as a wallet functionality library". Perhaps something like `monero-tx-utils` or `monero-wallet-lib` would have been more fitting?     

> __< r​ucknium:monero.social >__ Thanks so much for your comments and questions, tobtoht     

> __< k​ayabanerve:matrix.org >__ The DKG does encrypt its messages and no FROST messages need encryption. Message transport is solely authenticated channels if you want the ability to blame participants.     

> __< k​ayabanerve:matrix.org >__ It is abstract however to whatever communication protocol you may want.     

> __< k​ayabanerve:matrix.org >__ For the DKG, you do need consensus on the result. The DKG is modular. Right now, all that's implemented is PedPoP, yet the Bitcoiners proposed ChillDKG which achieves consistency.     

> __< k​ayabanerve:matrix.org >__ One could implement that and then use that to remove the requirement of a consensus protocol.     

> __< k​ayabanerve:matrix.org >__ I'm just speaking to further argue the modularity/design     

> __< k​ayabanerve:matrix.org >__ The FROST code is uncoordinated. The library does define messages (without authentication). The FROST lib follows the IETF standard. The application to Monero obviously isn't IETF standard and is a bit bespoke however.     

> __< k​ayabanerve:matrix.org >__ This doesn't just expose multisig TX signing. It also exposes multisig CLSAG signing. A wallet2 app could do everything on its end and solely call out for each CLSAG.     

> __< k​ayabanerve:matrix.org >__ monero-wallet has no DB/DB API. It also doesn't define a transport layer, solely an API which must be met by a transport layer.     

> __< k​ayabanerve:matrix.org >__ There are tests, there aren't examples at this library.     

> __< k​ayabanerve:matrix.org >__ FCMP++ will cause changes. It doesn't make sense to delay the audit IMO. It makes sense to do a follow-up audit at that time.     

> __< k​ayabanerve:matrix.org >__ Apologies for the lack of links to the source.     

> __< k​ayabanerve:matrix.org >__ Considering that's the package name in the Rust ecosystem (not some global namespace), and it is the pieces to scan/sign/send Monero TXs, I find the name fine. `-lib` isn't convention in this ecosystem.     

> __< k​ayabanerve:matrix.org >__ Also, this isn't just TX utils, and there already is monero-wallet-utils for extra features not present in monero-wallet directly (for whatever reason).     

> __< j​effro256:monero.social >__ Would the parts of the codebase would be disjoint? IMO one nice property of audited files is to be able to SHA256 it and compare it directly to a hash in the audit report so that you know for a fact that no breaking changes have been added since the audit     

> __< j​effro256:monero.social >__ Would the parts of the codebase be disjoint? IMO one nice property of audited files is to be able to SHA256 it and compare it directly to a hash in the audit report so that you know for a fact that no breaking changes have been added since the audit     

> __< k​ayabanerve:matrix.org >__ This is a living codebase and it absolutely isn't expected to meet that criteria.     

> __< k​ayabanerve:matrix.org >__ The library is at the point the API shouldn't change, it should have all the features necessary, and it should be safe.     

> __< k​ayabanerve:matrix.org >__ That's why it's being proposed for audit.     

> __< k​ayabanerve:matrix.org >__ To keep exact file integrity would require we never add further documentation however. It's not feasible.     

> __< rbrunner >__ Maybe you could make a public walkthrough of the code? Like UkoeHB did with his Seraphis library? So people would get some nice first impression what this is all about?     

> __< k​ayabanerve:matrix.org >__ The plan is to audit a git commit so people can see the differences via git. That should allow the same degree of auditability.     

> __< rbrunner >__ Because it's a bit hard to support, or not, the idea of an audit for this with next to no idea what it is :)     

> __< k​ayabanerve:matrix.org >__ I'm actually unsure what that example is.     

> __< k​ayabanerve:matrix.org >__ monero-serai underlies Cuprate and is a complete reimplementation of the Monero transaction code in Rust.     

> __< rbrunner >__ It was an interactive (Jitsy?) walkthrough with audio explanations about key points of the code.     

> __< k​ayabanerve:matrix.org >__ monero-wallet is a reimplementation of scanning/signing/sending transactions in Rust built around monero-serai.     

> __< rbrunner >__ I think jberman attended that, and may remember     

> __< k​ayabanerve:matrix.org >__ It's to some degree a wallet2 alternative. wallet2 manages itself, while this expects the app to manage it (offering greater flexibility), but this still offers all the high-level API components necessary to send/receive Monero.     

> __< k​ayabanerve:matrix.org >__ Notably, it also includes a multisig protocol which tobtoht already independently noted the theoretical merits of.     

> __< k​ayabanerve:matrix.org >__ And sorry, I'm not trying to state everything here/now, in this very moment, and talk over people. I'm just trying to respond with as much clarifications as I can.     

> __< j​effro256:monero.social >__ How dare you talk about your own library     

> __< s​yntheticbird:monero.social >__ This meeting is sponsored by monero-wallet     

> __< k​ayabanerve:matrix.org >__ I'll also be honest and say I'm unsure I can do a video walkthrough and unlikely to. I'd prefer to add more examples to the codebase to achieve documentation in the first place, yet I'll also note I get about 10 fps on my laptop so I'm pretty sure video recording isn't possible.     

> __< r​ucknium:monero.social >__ Disclosure: I statistically verified that `monero-wallet`'s decoy selection distribution matches that of wallet2 last year in exchange for 1 XMR. At least I think it was last year.     

> __< j​effro256:monero.social >__ Was that after the 10-block-lock DSA bug ?     

> __< k​ayabanerve:matrix.org >__ I think I have a spare laying around I can boot into a live image on? It may not have a working wireless card in it though 🤔 Suffice to say, my setup is sufficiently insane video recording isn't great for me.     

> __< k​ayabanerve:matrix.org >__ jberman has also done their analysis of fingerprinting vectors, including the DSA. They were critical for their role in TX extra.     

> __< rbrunner >__ I think some well selected sample code using the libraries would go a long way towards giving an impression about power and extent of those libraries     

> __< k​ayabanerve:matrix.org >__ For example, who here knew you can specify multiple TX pub keys and wallet2 will scan for all of them?     

> __< j​berman:monero.social >__ Disclosure on my end too: kayabanerve has paid me to work on monero-wallet. I put a decent amount of work into it to reduce fingerprints to wallet2, and did a general pass-through review     

> __< k​ayabanerve:matrix.org >__ Yet wallet2 will only scan the first vector of additional keys specified in TX extra.     

> __< k​ayabanerve:matrix.org >__ It's this exact type of oddities which we've extensively worked to minimize. It truly has been worked on for years.     

> __< j​berman:monero.social >__ Personally I think it would be quite a bit of work to make wallet2 compatible with monero-wallet's general flow. I don't know if that would be a feasible approach, except potentially in the isolated components like CLSAG signing? But then, I'm not sure how everything else would work for multisig     

> __< k​ayabanerve:matrix.org >__ Oh. jberman also got the fees to match exactly.     

> __< rbrunner >__ I think we have tons of questions all at once with these 2 libraries. Switching to this new type of multisig for Monero in general being only 1 of them.     

> __< j​berman:monero.social >__ Unless maybe there is a way to lean on wallet2 for scanning, and then monero-wallet for DKG setup / constructing txs? I would assume not, and to get monero-wallet working in a functional end-wallet, I imagine would require a full implementation of wallet state handling     

> __< r​ucknium:monero.social >__ jeffro256: Yes. December 2023: https://github.com/serai-dex/serai/pull/384#issuecomment-1870597406     

> __< k​ayabanerve:matrix.org >__ Importing monero-clsag (a subset of the library linkable on its own without pulling in all other components) into a wallet2 app should be quite feasible IMO.     

> __< k​ayabanerve:matrix.org >__ The greater note is on the value in the academia done here and proposed however.     

> __< rbrunner >__ Is there any idea yet about the rough magnitude of work that the proposed audit would require?     

> __< k​ayabanerve:matrix.org >__ wallet2 apps don't have to adopt monero-clsag. The theory here, once proven, would allow C++ implementations to be done without repeating the prior multisig drama.     

> __< k​ayabanerve:matrix.org >__ The quote is expected to be 750-1000 XMR.     

> __< k​ayabanerve:matrix.org >__ I'll also note the current multisig in wallet2 still isn't proven. This isn't just proving an alternative protocol. It'd be the first implemented and proven Monero multisig.     

> __< j​effro256:monero.social >__ But to be fair, the monero-clsag won't be useful for multisig after the FCMP fork right? Unless it is compatible for syncing key images with the current core repo multisig implementation?     

> __< k​ayabanerve:matrix.org >__ I have no idea what you mean by "syncing key images".     

> __< k​ayabanerve:matrix.org >__ I'm just unfamiliar with that wallet2 flow, sorry.     

> __< k​ayabanerve:matrix.org >__ monero-clsag won't be useful after FCMP++. Any existing key image sync also won't be. Both will change.     

> __< r​ucknium:monero.social >__ At this moment, I really like the idea of proving and auditing the FROST multisig. On the remainder, I wonder why it is more important to audit this library instead of `monero-ts`, -python, -php, or even Monero's native C++ implementation.     

> __< j​effro256:monero.social >__ Current multisig implementation requires M participants in a M/N multisig wallet to come together to combine "partial key images". I'm assuming a similar technique is required for multisig in monero-clsag, but if the exact math isn't compatible, then it wouldn't carry over     

> __< k​ayabanerve:matrix.org >__ The same premise applies jeffro256.     

> __< k​ayabanerve:matrix.org >__ All of that will break with FCMP++, even whatever's currently in wallet2.     

> __< k​ayabanerve:matrix.org >__ Here's why I'm still asking to do this.     

> __< k​ayabanerve:matrix.org >__ rbrunner: How long until the FCMP++ HF activation in your opinion?     

> __< rbrunner >__ "why it is more important to audit this library instead of" Interesting question     

> __< rbrunner >__ 1 year? But not sure of the context of that question     

> __< k​ayabanerve:matrix.org >__ I believe the most recent estimate I saw from you was Q4 of 2025.     

> __< k​ayabanerve:matrix.org >__ I disagree with that estimate being likely, but it means I have to either:     

> __< k​ayabanerve:matrix.org >__ 1) Delay Serai a year     

> __< k​ayabanerve:matrix.org >__ 2) Deploy an unproven multisig for ~6-9 months and just pray nothing happens     

> __< k​ayabanerve:matrix.org >__ The fact CLSAG will be replaced doesn't mean it isn't here now.     

> __< j​babb:cypherstack.com >__ disclosure: cypher stack employee.  I originally made monero-php years ago.  recanman has been redoing it to reimplement monero crypto in pure php.  MrCyjaneK bound wallet2 to PHP via the monero_c repo recently in order to provide the last missing pieces and prepare for FCMPs &etc. by outsourcing crypto to monero-project/monero     

> __< j​babb:cypherstack.com >__ in my opinion we shouldn't allow these wrappers to handle crypto but rather rely upon the c++ we know and love and the rust we need.  rust is much easier to build and build with for me so I prefer focusing on c++ and rust rather than all the other, higher-level languages     

> __< k​ayabanerve:matrix.org >__ And that's my personal involvement with it. There are other multisig use cases which either aren't feasible due to the current multisig's failings, or are also YOLO'ing it.     

> __< k​ayabanerve:matrix.org >__ Rucknium jberman jeffro256 Is it possible to audit wallet2?     

> __< k​ayabanerve:matrix.org >__ Isn't a lot of it in a single 10k line file?     

> __< k​ayabanerve:matrix.org >__ Doesn't it depend on epee, a bespoke never audited lib?     

> __< r​ucknium:monero.social >__ ...exactly     

> __< k​ayabanerve:matrix.org >__ I'm legitimately unsure it is feasible. If the Monero project can put forth a version of wallet2 to audit and have an auditor who doesn't look at us like we're insane to ask, I'd support such a CCS.     

> __< r​ucknium:monero.social >__ My wallet2 question was a little rhetorical since I have seen tobtoht  say that a wallet2 audit right now would be very hard because it is spaghetti. But do we know the current Monero tx functions are working correctly?     

> __< k​ayabanerve:matrix.org >__ I have built a library I believe can be audited. I have prepared it for auditing. I have an auditor (Cypher Stack) finalizing their quote. I made a CCS.     

> __< k​ayabanerve:matrix.org >__ Even if wallet2 could be audited, I'd treat it as a distinct topic.     

> __< r​ucknium:monero.social >__ Won't part of the proposed audit be to check that the library does what the Monero C++ implementation does? There is cryptography, which is separate, and then other parts that need to be checked.     

> __< j​berman:monero.social >__ wallet2 multisig still doesn't have security proofs for its relatively makeshift protocol, nor someone willing to carry it forward at the moment. getting it audited isn't the only task necessary to get its multisig across the line. monero-serai has implemented a peer-reviewed, widely known protocol for multisig, that is also orders of magnitude more performant than wallet2's multisig impl     

> __< k​ayabanerve:matrix.org >__ The lib is tested to have the expect fee on every TX it makes. It's also been reviewed and cites links for all the weird quirks it has.     

> __< k​ayabanerve:matrix.org >__ https://github.com/serai-dex/serai/blob/599b2dec8fada40c9f213fbc04d81871e24aff46/networks/monero/wallet/src/send/mod.rs#L321     

> __< rbrunner >__ What I currently have still trouble wrapping my head around it is libary use cases. Or is it alread "worth it all" just for Serai and any use cases beyond that just bonus, to put it bluntly?     

> __< j​berman:monero.social >__ given resources at hand, I personally think monero-wallet is a clear choice for where to allocate continued effort and resources for multisig efforts     

> __< k​ayabanerve:matrix.org >__ The tests do also test against monero-wallet-rpc.     

> __< k​ayabanerve:matrix.org >__ https://github.com/serai-dex/serai/blob/599b2dec8fada40c9f213fbc04d81871e24aff46/networks/monero/wallet/src/scan.rs#L150     

> __< k​ayabanerve:matrix.org >__ Just as a pair of examples of our citations to Monero which I do aim to demonstrate they do try to match behavior exactly.     

> __< k​ayabanerve:matrix.org >__ Rucknium: The audit will be to confirm this code sane and that comes with some level of comparing to C++. It doesn't come with auditing the C++.     

> __< k​ayabanerve:matrix.org >__ rbrunner: Cuprate.     

> __< rbrunner >__ Ah, yes, of course     

> __< r​ucknium:monero.social >__ IIRC, kayabanerve has said Serai hasn't received Monero community funding. IMHO, if this full audit gets CCS funding, then that claim should change.     

> __< k​ayabanerve:matrix.org >__ The CCS is actively funding a dependent of this, has been for several months, and they've received more in funding than I plan to ask for here.     

> __< k​ayabanerve:matrix.org >__ Rucknium: NACK.     

> __< k​ayabanerve:matrix.org >__ None of this code is Serai specific and monero-serai is planned to be transferred into monero-oxide after.     

> __< k​ayabanerve:matrix.org >__ I'm fine saying the CCS paid for the audits of the Monero library Serai built. That doesn't change this isn't Serai proper.     

> __< rbrunner >__ More and more I come to believe that this is much bigger than just "Do we move this to CCS for funding?" We are talking about the future of the whole Monero codebase in a way.     

> __< rbrunner >__ Which is pretty difficult and is pretty far-reaching.     

> __< k​ayabanerve:matrix.org >__ I see this as comparable to Cuprate.     

> __< k​ayabanerve:matrix.org >__ It does potentially 'endorse' a completely non-wallet2 wallet which is notable.     

> __< k​ayabanerve:matrix.org >__ But the academia is mutually beneficial and we aren't yet discussing ripping out wallet2's multisig.     

> __< k​ayabanerve:matrix.org >__ That is a proposal which comes up occasionally but we're not there yet.     

> __< r​ucknium:monero.social >__ rbrunner: That's my cue to move back to the question of whether there should be an ASAP announcement that the next hard fork will not honor custom timelocks after a certain date.     

> __< k​ayabanerve:matrix.org >__ With FCMP++, monero-serai will share code with monerod however.     

> __< s​yntheticbird:monero.social >__ rbrunner: Rust will eventually grow upon monero's lands.     

> __< r​ucknium:monero.social >__ Since it seems that meeting attendees wanted a decision on that today     

> __< k​ayabanerve:matrix.org >__ They'll both use the same FCMP++ set of libraries and the plan is for my FCMP++ libraries, in Rust, to handle multisig.     

> __< k​ayabanerve:matrix.org >__ So FCMP++ multisig is Rustifying, and this provides a Rusty alternative for CLSAG.     

> __< j​berman:monero.social >__ There shouldn't be an ASAP announcement that next hard fork will not honor custom timelocks after a certain date     

> __< rbrunner >__ I didn't understand meeting sentiment to long for a timelock decision today, and I would like to come back to it in 1 week, after some thinking it over     

> __< rbrunner >__ syntheticbird: Our C++ codebase is already rusting all on its own, thank you very much :)     

> __< j​berman:monero.social >__ jeffro256 is going to look more into numbers of timelocked outputs. I or jeffro256 can write up another MRL issue fleshing out the idea in a clearer/cleaner way. Then we can discuss it again and gauge sentiment to the idea. Imo if it gains rough consensus, it wouldn't need to be officially announced until the fcmp++ research is all audited / formalized, and honestly probably not<clipped message>     

> __< j​berman:monero.social >__  til code is ready     

> __< t​obtoht:monero.social >__ I continue to have concerns about Rust and its ecosystem, which I find are especially relevant for consensus level code, but I will detail those later in a comment under the fcmp++ integration PR (#9436).     

> __< t​obtoht:monero.social >__ (And to be clear, my intent is not to NACK, but to make sure we understand its implications on supply chain security, build system complexity, long-term maintainability, cross-architecture reproducibility, bootstrappability, and third-party packaging and to make sure we have the necessary tools in place to maintain it.)     

> __< r​ucknium:monero.social >__ Maybe the _option_ of not honoring custom time locks past a certain date is enough to deter a potential vandal. In a game theoretic sort of way.     

> __< k​ayabanerve:matrix.org >__ I'm fine letting the monero-serai/monero-wallet audits marinate to next week yet I would like MRL to issue an opinion by the next community meeting if possible. If it's not, so be it, just an unfortunate delay in the bureaucracy.     

> __< k​ayabanerve:matrix.org >__ I'll also note, rbrunner, the libs do have 100% documentation. I'll try to set up a hosted copy of the docs as that may be useful per your notes.     

> __< r​ucknium:monero.social >__ Let's end the meeting here. Feel free to continue discussing things. Thanks everyone.     

> __< k​ayabanerve:matrix.org >__ If anyone wants to locally see them, it's     

> __< k​ayabanerve:matrix.org >__ git clone git⊙gc/serai-dex/serai     

> __< k​ayabanerve:matrix.org >__ cargo doc -p monero-wallet --all-features -- --open     

> __< k​ayabanerve:matrix.org >__ Rucknium: All topics took longer than their last :D     

> __< k​ayabanerve:matrix.org >__ If anyone wants to locally see them, it's     

> __< k​ayabanerve:matrix.org >__ git clone git⊙gc:serai-dex/serai     

> __< k​ayabanerve:matrix.org >__ cargo doc -p monero-wallet --all-features -- --open     

> __< k​ayabanerve:matrix.org >__ If anyone wants to locally see them, it's     

> __< k​ayabanerve:matrix.org >__ git clone https://github.com/serai-dex/serai     

> __< k​ayabanerve:matrix.org >__ cd serai     

> __< k​ayabanerve:matrix.org >__ cargo doc -p monero-wallet --all-features -- --open     

> __< k​ayabanerve:matrix.org >__ (Sorry to the IRC people for my edits of the above commands)     

> __< j​effro256:monero.social >__ Great success     

> __< j​effro256:monero.social >__ Thanks everyone!     

> __< r​ucknium:monero.social >__ jberman: Let me put it this way. If the developers of a cryptocurrency stated that all coins sent to burn addresses would become spendable in the next hard fork, that would change the total effective supply of the cryptocurrency. Users would be free to upgrade or not upgrade to the hard fork, of course. The custom time locks issue isn't too different.     

> __< k​ayabanerve:monero.social >__ I'll note again we kinda have to invalidate timelocks for the PQ migration.     

> __< k​ayabanerve:monero.social >__ This is inevitable to a nontrivial degree.     

> __< j​berman:monero.social >__ the issue I take with this comment is you characterizing the discussion today as "the developers of a cryptocurrency stated that <x is going to happen>"     

> __< j​berman:monero.social >__ that isn't what happened nor what's happening     

> __< c​haser:monero.social >__ kayabanerve: just curious, what is the critical point of interference between timelocks and PQ signatures?     

> __< j​berman:monero.social >__ we discussed a dos vector and technically reasonable mitigation to the dos vector. we didn't say the mitigation is now set in stone and going to happen     

> __< k​ayabanerve:monero.social >__ We need to allow a migration or the outputs will be burnt/available to steal. The migration will be to a PQ key. That PQ key may be held by a distinct entity, meaning a transfer did occur prior to the timelock expiry.     

> __< k​ayabanerve:monero.social >__ We then either have to maintain the timelock, despite allowing a transfer, or drop it as we don't care.     

> __< k​ayabanerve:monero.social >__ The best solution is to just remove to the no-transfer restriction we can't actually enforce.     

> __< j​berman:monero.social >__ I think that would be reasonable logic to invalidate timelocks at a PQ migration fork. I wouldn't push to invalidate timelocks today for a future fork     

> __< s​yntheticbird:monero.social >__ pardon me PQ meaning?     

> __< j​berman:monero.social >__ post-quantum     

> __< s​yntheticbird:monero.social >__ I must have missed an episode. We're doing PQ already ?     

> __< c​haser:monero.social >__ kayabanerve: a-ha. checks out, thank you.     

> __< j​effro256:monero.social >__ Not as this moment, kayaba is just making the point that we will have to invalidate unlock times at some point assuming we do a PQ migration     

> __< s​yntheticbird:monero.social >__ Ah ok thx make more sense     

> __< s​yntheticbird:monero.social >__ so excited to share my 3MB McEliece address to receive my piconeros.     

> __< c​haser:monero.social >__ base85-encoded Carrot addresses, here we go     

> __< rbrunner >__ base85?     

> __< k​ayabanerve:monero.social >__ jberman: We won't be ideological purists about it then so there's no point in being it now is the argument. I'm not arguing for invalidation now. Solely justifying an ignore height (as those will be 'invalidated').     

> __< c​haser:monero.social >__ rbrunner: to save on screen estate (half-joking). maybe bech85 (doesn't exist yet) so there's error checking. notably higher bases seem dangerous to me.     

> __< s​yntheticbird:monero.social >__ how is it more dangerous?     

> __< c​haser:monero.social >__ those would use non-ASCII characters, which may cause loss of data during encoding/decoding when passing through certain environments.     

> __< s​yntheticbird:monero.social >__ oh ok     

> __< c​haser:monero.social >__ on a more serious note, the conservative choice for PQ so far seems to be SPHINCS+ (https://gist.github.com/tevador/23a84444df2419dd658cba804bf57f1a), which has public key sizes between 32--64 bytes, depending on the targeted security level. so I *guess*, even with a base32-variant encoding, addresses wouldn't be colossal.     

> __< s​yntheticbird:monero.social >__ ah ok seems fine. I've experimented with it recently (as it got standardized) its performance are kinda shocking (in the bad sense).     

> __< s​yntheticbird:monero.social >__ in debug mode sphincs signature could take several seconds to complete     

> __< s​yntheticbird:monero.social >__ release mode max 2 seconds.     

> __< a​surar0:monero.social >__ These numbers in release mode seems unrealistic. I've also experimented with several post-quantum signature crates recently. If taking SPHINC+SHA2+256s (the slowest algorithm available in my tool) keypair generation, signature generation, and verification are all subsecond operations. I'm using PQClean implementation. Tool repository here: https://github.com/Asurar0/mikomikagi     

> __< s​yntheticbird:monero.social >__ ok ill test. i dont remember which crate i used     

> __< a​surar0:monero.social >__ edit SPHINCS not SPHINC     

> __< k​ayabanerve:matrix.org >__ chaser chaser:monero.social: SPHINCS+ isn't a good choice though     

> __< k​ayabanerve:matrix.org >__ it'd require an interactive transfer protocol or it'd require wrapping in a commitment where we do a ZK proof opening the commitment and verifying the SPHINCS+ signature     

> __< k​ayabanerve:matrix.org >__ At that point, we can use a SHA2 hash as a public key and collapse all of SPHINCS+ to that.     

> __< k​ayabanerve:matrix.org >__ My guess is we end up on Ajtai commitments with a combination of MSIS and (some variant of) LWE at this point of time.     

> __< s​yntheticbird:monero.social >__ we're cooking home made post quantum algorithm now?     

> __< c​haser:monero.social >__ kayabanerve I was unaware of that limitation, happy to learn more. I was thinking along the same lines as SyntheticBird, will that require creating a custom crypto scheme? (not that I'm entirely opposed to that.)     

> __< k​ayabanerve:matrix.org >__ SyntheticBird: We'll need to develop a PQ composition when the time comes. That PQ composition cannot solely rely on SHA2. If we end up relying on LWE for the composition, we don't benefit from choosing a slower, less functional signature without LWE.     

> __< k​ayabanerve:matrix.org >__ We need a signature scheme where we can re-randomize the public key though.     

> __< k​ayabanerve:matrix.org >__ So we open the commitment to get the underlying key, then output said underlying key with some rerandomization. Then we do a traditional PQ signature verification.     

> __< k​ayabanerve:matrix.org >__ Or we remove the membership/spend-auth proof delineation and the commitment opening itself is spend-auth.     

> __< k​ayabanerve:matrix.org >__ cc chaser too, ofc     

> __< k​ayabanerve:matrix.org >__ If we put a SPHINCS+ key in a commitment on-chain, yet we can't re-randomize the key, then yeah, you have to verify the SPHINCS+ signature in ZK. Even an interactive protocol is insufficient for the necessary privacy properties.     

> __< k​ayabanerve:matrix.org >__ You could technically still achieve membership/spend-auth separation? You'd produce a SPHINCS+ signature, then make a proof opening the rerandomized commitment from the membership proof and verifying the signature. So sorry, it is possible, it's just a bad idea.     

> __< k​ayabanerve:matrix.org >__ It adds a massive ZK proof (which won't be on the same conservative assumptions) solely because a non-rerandomizable scheme wasn't chosen.     

> __< s​yntheticbird:monero.social >__ didn't understand the whole thing not gonna lie but i got the important line. 👍     

> __< s​yntheticbird:monero.social >__ lines*     

> __< c​haser:monero.social >__ kayaba, thank you for expanding on that. are there other routes? tevador unfavored CRYSTALS-Dilithium because it relies on lattice hardness assumptions. this is the first time I hear about Ajtai commitments, and my uneducated guess, based on the name, is that they have *something* to do with lattice-based crypto. I don't know about the re-randomizability though in CRYSTALS-Dilithium.     

> __< d​iego:cypherstack.com >__ So...     

> __< d​iego:cypherstack.com >__ if Cypher Stack was to do some research after Carrot pro bono.     

> __< d​iego:cypherstack.com >__ What would you all want us to look at? :)     

> __< s​yntheticbird:monero.social >__ P=NP obviously     

> __< s​yntheticbird:monero.social >__ (jk i'm curious about the next chain of event)   

# Action History
- Created by: Rucknium | 2024-10-15T17:35:16+00:00
- Closed at: 2024-10-29T21:06:00+00:00
