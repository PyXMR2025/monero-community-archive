---
title: Monero Research Lab Meeting - Wed 12 August 2026, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1440
author: Rucknium
assignees: []
labels: []
created_at: '2026-08-11T17:15:36+00:00'
updated_at: '2026-08-26T13:35:51+00:00'
type: issue
status: closed
closed_at: '2026-08-26T13:35:51+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

Live log: https://libera.monerologs.net/monero-research-lab

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/meeting.html?p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3. [PQ turnstile spend enables a Carrot/Jamtis distinguisher (privacy leak)](https://github.com/jeffro256/carrot/issues/10).

4. FCMP++ to-do list status. [Programming tasks](https://github.com/seraphis-migration/monero/issues/53). [Reviews and audits](https://cryptpad.fr/sheet/#/2/sheet/view/yPVIUywwA9-deE9VF6GYm9bXbPdCerdST3UDEEfBxcM/embed/). [FCMP++ Integration Audit Overview](https://github.com/seraphis-migration/monero/issues/294). [Network upgrade schedule Gantt chart](https://html-preview.github.io/?url=https://github.com/jeffro256/fcmp-carrot-plan/blob/master/fcmp%2B%2B-carrot.html).

5. [Relative locks with FCMP++](https://github.com/monero-project/research-lab/issues/161).

6. [Shi, Zhang, Ge, Lan, Zhang, & Wang (2026) "Deanonymizing Monero Transactions in Tor Network."](https://arxiv.org/abs/2607.07062)

7. [FCMP beta stressnet](https://github.com/seraphis-migration/monero/releases/).

8. [PoW-Admitted Zero-Fee Transactions for P2Pool](https://gist.github.com/SChernykh/aae5b2d414095e742437134ab20d4353).

9. Any other business

10. Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs: #1435   

# Discussion History
## SChernykh | 2026-08-12T15:00:19+00:00
I would like to have a short discussion of this: https://gist.github.com/SChernykh/aae5b2d414095e742437134ab20d4353 under "8. Any other business", and maybe a separate agenda item for this (if today's discussion goes well) for the next week's meeting.

Participants are recommended to read "1. Summary" and "2. Motivation" sections before discussing. Other sections contain technical implementation details which are not relevant right now.

## Rucknium | 2026-08-17T21:39:12+00:00
Logs

> __< rucknium >__ Meeting time! https://github.com/monero-project/meta/issues/1440     

> __< rucknium >__ 1. Greetings     

> __< jberman >__ waves     

> __< sech1 >__ hi     

> __< articmine >__ Hi     

> __< vtnerd >__ hi     

> __< jpk68:matrix.org >__ Hello     

> __< rucknium >__ 2. Updates. What is everyone working on?     

> __< slowbeardigger:matrix.org >__ Good afternoon legends     

> __< sech1 >__ I'm working on adding FCMP++/Carrot/RandomX v2 support to P2Pool, this will take a few weeks and I'll probably be more active in the meetings during this time     

> __< jeffro256 >__ Howdy      

> __< tevador >__ Hi     

> __< jeffro256 >__ Me: working on bug fixes and reviewing upstream PRs, and generally trying to get the FCMP++/Carrot merges through      

> __< jberman >__ me: various PR's to monerod upstream / reviews, updated subsequent FCMP++ integration PR's (the next few in a row are ready to go)     

> __< vtnerd >__ me: fixed + unit tested a bug in lws (after fixing another issue), and got my guix setup with signing key ready for 0.19 bootstrappable builds     

> __< rucknium >__ me: Writing scripts to analyze network-level transaction privacy using monerosim. Finding an reporting issues in monerosim: https://github.com/Fountain5405/monerosim/issues . Keeping stressnet stressed.     

> __< jeffro256 >__ I think this week I'm going to switch back into working on Carrot coding tasks like hot-cold and knowledge proofs, now that some big refactor/review PRs are out of the way      

> __< vtnerd >__ me: still need to work on a bug for selsta, and the d++ privacy leak discussed last week     

> __< UkoeHB >__ Me: working on a validator for pending_tx (multisig and cold signing workflows)     

> __< jpk68:matrix.org >__ Me: trying to fix some hardware wallet bugs     

> __< rucknium >__ 3. PQ turnstile spend enables a Carrot/Jamtis distinguisher (privacy leak) (https://github.com/jeffro256/carrot/issues/10).     

> __< tevador >__ Maybe jeffro256 can comment. It's possible we can just accept the leak. But the fix is relatively cheap IMO.     

> __< jeffro256 >__ Sorry for not answering, I have been looking into this and I think that, since the Carrot code has evolved since I originally unbound K^j_v, the original suggestion of re-including K^j_v won't add too much complexity. I will have an enginneed solution by EoW     

> __< tevador >__ Thanks     

> __< tevador >__ I think we can move to the next agenda item.     

> __< rucknium >__ 4. FCMP++ to-do list status. Programming tasks (https://github.com/seraphis-migration/monero/issues/53). Reviews and audits (https://cryptpad.fr/sheet/#/2/sheet/view/yPVIUywwA9-deE9VF6GYm9bXbPdCerdST3UDEEfBxcM/embed/). FCMP++ Integration Audit Overview (https://github.com/seraphis-migration/monero/issues/294). Network upgrade  [... too long, see https://mrelay.p2pool.observer/e/usfSg6ALYkIteVRY ]     

> __< jberman >__ The Rust FFI PR was merged into upstream master (hooray), next on the FCMP++ integration list is: https://github.com/monero-project/monero/pull/10360     

> __< jberman >__ That is the final PR from the Phase 1 FCMP++ integration audit     

> __< jeffro256 >__ I have updated the planner here: https://html-preview.github.io/?url=https://github.com/jeffro256/fcmp-carrot-plan/blob/master/fcmp%2B%2B-carrot.html     

> __< jeffro256 >__ OOps that's already linked      

> __< jberman >__ For Phases 2 & 3, right now I'm thinking it would be best to just keep going reviewing on our end and merging code, and once all code is in we audit then (perhaps we get Phase 2 audited once all that code is in). I think that would be most efficient     

> __< jeffro256 >__ Biggest blocker on the Carrot side seems to be licensing around mx25519: https://github.com/monero-project/monero/pull/10964. tevador has mx25519 licensed under LGPL, which has some restrictive terms.     

> __< jberman >__ No major update at the moment on the final Research Task audits. The Least Authority helioselene audit is very close to the finish line     

> __< jeffro256 >__ There's some discussion around how exactly Monero will comply with the terms in section 6 of LGPL v3: https://github.com/monero-project/monero/pull/10964#issuecomment-5208353737. IDK if anyone has something to throw in here, because it doesn't seem to be going anywhere quickly...     

> __< jberman >__ And we still need quotes for divisors impl audit rd. 2 + fcmp-plus-plus lib audit     

> __< jpk68:matrix.org >__ jeffro256: It does seem like this would complicate things a fair bit, which would be quite inconvenient. Adopting LGPL dependencies, I mean     

> __< jpk68:matrix.org >__ The amount of complexity surrounding this upgrade is already pretty extreme     

> __< jpk68:matrix.org >__ Downstream users of Monero code would also be affected by this (i.e. wallet applications)     

> __< tevador >__ The "restriction" of LGPL § 6 would imply we would need to provide a link to the tag commit the release was built from. Which is hardly a restriction.     

> __< jpk68:matrix.org >__ tevador: You mentioned that you didn't want to relicense your code after companies made proprietary forks of RandomX code.     

> __< tevador >__ Example: https://github.com/monero-project/monero/tree/v0.18.5.1     

> __< jeffro256 >__ Yeah, that does involve some changes to monero-site, though.     

> __< jpk68:matrix.org >__ I'm wondering how the same concern applies to general cryptography code, rather than PoW     

> __< vtnerd >__ the primary objective of the lgpl is to force changes to mx25519 to be made public … ?     

> __< jpk68:matrix.org >__ Yes, but how is that practically relevant here? I can see how it is for RandomX     

> __< tevador >__ The exactly same thing applies to a Curve25519 library. If someone makes optimizations, we want to be able to upstream them.     

> __< vtnerd >__ I guess a wallet could be made faster in secret, similar to the issue in randomX     

> __< slowbeardigger:matrix.org >__ In xmrpay-carrot I already use a BSD-3 Rust implementation based on curve25519-dalek that matches the upstream CARROT vectors.     

> __< slowbeardigger:matrix.org >__ It only covers the receiver side CARROT operation for now, not the full mx25519 API.     

> __< slowbeardigger:matrix.org >__ would a permissively licensed rust implementation be useful, or does Monero specifically need C/C++?     

> __< vtnerd >__ c/c++ is more useful to the project I think, but opinions may differ     

> __< tevador >__ I'm pretty sure mx25519 is faster than curve25519-dalek     

> __< tevador >__ But both are usable for a wallet implementation     

> __< jeffro256 >__ Espeially after considering Rust FFI      

> __< jeffro256 >__ *Especially     

> __< slowbeardigger:matrix.org >__ hmmmm     

> __< slowbeardigger:matrix.org >__ what about a small portable BSD-3 C/C++ implementation be useful as a starting point if it matches the full unclamped API and existing vectors, or would optimized amd64/arm64 backends be required from the start?     

> __< slowbeardigger:matrix.org >__ just wondering if I can be of any help     

> __< vtnerd >__ this is assuming we are rejecting lgpl for some reason, it doesn’t seem to be a clear consensus on that     

> __< jeffro256 >__ If you can get a portable implementation as fast as the amd64x version, I'd be impressed      

> __< tevador >__ A portable permissively licensed implementation could be made quite easily from the ref10 public domain code. But it's quite slow.     

> __< vtnerd >__ every wallet is open source already, if Im not mistaken     

> __< tevador >__ LGPL is open source.     

> __< slowbeardigger:matrix.org >__ jeffro256: I’ll try my best     

> __< vtnerd >__ I meant a wallet trying to use mx25519 but closed source somehow. I’m just not seeing any reason to worry about lgpl but maybe Im missing something     

> __< tobtoht >__ LGPL § 6 is not the only restriction and its restrictions would apply to all downstream projects, not just Monero.     

> __< tobtoht >__ LGPL is incompatible with the CoC: "All contributions to the project source code ("patches") MUST use the same license as the project."     

> __< jpk68:matrix.org >__ This is my point, we have already had enough trouble trying to get, for example, hardware wallet companies to integrate Monero     

> __< jpk68:matrix.org >__ Making licensing matters more complicated is shooting ourselves in the foot     

> __< slowbeardigger:matrix.org >__ I’m not assuming LGPL will be rejected. I’ll treat this as a small benchmark experiment first, compare it against the portable and amd64x implementations, and only suggest it if the result is actually useful…     

> __< slowbeardigger:matrix.org >__ I’ll start working on it     

> __< tevador >__ The CoC is clearly meant for other cases, like someone submitting a random patch under GPL.     

> __< tevador >__ AFAIK we already have at least one LGPL dependency     

> __< jpk68:matrix.org >__ Also, the LGPL wouldn't prevent proprietary freeloading, since they could link dynamically     

> __< jpk68:matrix.org >__ IIRC the only "copyleft" library we use currently is ZeroMQ, which is MPL     

> __< jpk68:matrix.org >__ That's somewhat less restrictive compared to LGPL     

> __< tobtoht >__ "The CoC is clearly meant for other cases" <- I don't agree. Quoting myself from the issue: "If we allow non-permissive licenses in required dependencies, the rule becomes meaningless: contributors can just work around the rule by introducing code with a non-permissive license via a submodule, which is what is happening here."     

> __< vtnerd >__ whats the other lgpl depdendency? polyseed? or something else     

> __< tevador >__ Quoting myself from the issue: "It's clear that both libraries are non-trivial and usable outside of the Monero repository. I didn't implement them to circumvent a rule."     

> __< tevador >__ The other one is polyseed     

> __< jeffro256 >__ > Also, the LGPL wouldn't prevent proprietary freeloading, since they could link dynamically     

> __< jeffro256 >__ It would prevent modifying mx25519 itself, and not publishing the modifications, which is the point     

> __< rucknium >__ More discussion on this issue?     

> __< jeffro256 >__ Ideally, we should figure this out soon, because it is a blocker for Carrot and Polyseed support      

> __< rucknium >__ Can the licensing discussion be moved to No Wallet Left Behind #no-wallet-left-behind:monero.social  meetings or should it stay here for next week? Or moved back to GitHub?     

> __< jberman >__ tevador: do you see yourself budging on this issue and relicensing?     

> __< tobtoht >__ I will honor a vote     

> __< jeffro256 >__ tobtoht: Since we have maintainers and approval processes, it is always at our discretition to block the changes that are superfulously adding non-permissive licensing for their own sake. I don't believe that Polyseed and mx25519 are those cases.      

> __< jeffro256 >__ We will need to do some infra work on the monero-site side to support  LGPL license terms. Is someone willing to make those changes? Also, we need to implement a license command or something along those lines correct?     

> __< jeffro256 >__ To display the license body from the object code      

> __< jeffro256 >__ rucknium: If the relevant people will join NWLB on Monday, then it could be moved there      

> __< jberman >__ my opinion on this is whatever moves this forward as fast as possible, I don't have a strong opinion on the license discussion itself     

> __< jberman >__ I think we should move on and if tevador wants to add to above tevador can     

> __< tevador >__ jeffro256: AFAIK we could just add the license file(s) to the release archive.     

> __< tevador >__ I have already explained why I'm not going to relicense.     

> __< jberman >__ ok, if tevador isn't going to relicense then I think let's just find a way to move forward with that     

> __< tobtoht >__ My personal opinion is that we should not burden every downstream ecosystem project with a restrictive license.     

> __< jberman >__ I think that's a fine opinion but we're stuck at an impasse here and I think it's best we move forward with it     

> __< tevador >__ The "restrictions" of LGPL are quite mild, even for closed-source projects that use the library.     

> __< UkoeHB >__ I am also against restrictive licenses both on principle and pragmatically (how much time wasted already on this? MIT gets no such drama). Is it possible an LGPL fork will just patent any changes they make, rendering the whole endeavor meaningless?     

> __< jeffro256 >__ What exactly is the burden for downstream eco? That they must point to the Monero source ? Does that resolve section 6 since our repo would point to mx25519?     

> __< tevador >__ AFAIK there was no issue until tobtoht started to dispute the license.     

> __< jpk68:matrix.org >__ I don't want to be annoying and keep insisting on not having permissive licenses (at the expense of delaying things), but I feel like it's not a great idea to keep making non-ideal decisions, causing later technical debt, for the sake of finishing things faster     

> __< jeffro256 >__ TBF looking over license terms is exactly what we need to avoid licensing issues ...     

> __< jpk68:matrix.org >__ At some point, one has to wonder how many concessions we're willing to make (Rust, LGPL, etc.) just to jam things through quicker     

> __< jberman >__ in this case I don't think there is much room for significant issues either way and both sides raise fine points     

> __< jberman >__ yes yes just to jam things through quicker than the 2 and a half years this has taken     

> __< rucknium >__ Given tevador 's statements, isn't a clean-room reimplementation of mx25519 the only way to avoid the LGPL in the Monero codebase? Anyone want to do that? If no, there seems to be only one option.     

> __< jpk68:matrix.org >__ jberman: Rewriting FCMP++ code in C/C++ would probably take longer than using the Rust library, no?     

> __< jberman >__ absolutely not     

> __< tevador >__ AFAICS the only change that would need to be made is to add the (L)GPL text to the release tarball. The rest is already solved.     

> __< jberman >__ sorry, absolutely yes*     

> __< sech1 >__ Any code rewrite will require another code audit     

> __< jeffro256 >__ tevador: Does does downstream have to do this if they use Monero as a library, instead of downloading releases?     

> __< jpk68:matrix.org >__ My point is simply that we shouldn't keep making compromises which will incur future technical debt under the excuse of saving time. In other words, I agree with tobtoht here     

> __< rucknium >__ IMHO, this issue should go on No Wallet Left Behind's agenda next week.     

> __< tevador >__ jeffro: It depends if they use the part that links to mx25519, then they have to also include the license file.     

> __< rucknium >__ Let's continue.     

> __< rucknium >__ 5. Relative locks with FCMP++ (https://github.com/monero-project/research-lab/issues/161).     

> __< jberman >__ I'm not going to rehash the argument over Rust for the millionth time fwiw, I don't think you're raising a valid point there and it's frustrating to keep bringing it up in contexts like this. It's (an invalid) negative framing that doesn't need to be re-argued every other conversation     

> __< rucknium >__ Last we left this, koe said:     

> __< rucknium >__ > < UkoeHB > I think we should get a prod-oriented PR for the change and aim further discussion at that.     

> __< rucknium >__ Do we have a prod-oriented PR for relative locks?     

> __< tevador >__ This PR needs a review: https://github.com/seraphis-migration/monero/pull/445     

> __< rucknium >__ UkoeHB: Any comments on relative locks for now?     

> __< UkoeHB >__ no, I will add review for 445 to my list     

> __< rucknium >__ Thanks.     

> __< rucknium >__ 6. Shi, Zhang, Ge, Lan, Zhang, & Wang (2026) "Deanonymizing Monero Transactions in Tor Network." (https://arxiv.org/abs/2607.07062)     

> __< rucknium >__ In his update, vtnerd said the Dandelion++ privacy leak was on his to-do list. > <vtnerd> me: still need to work on a bug for selsta, and the d++ privacy leak discussed last week     

> __< rucknium >__ Last meeting, boog900:monero.social  suggested that discussion of this PR be revived: https://github.com/monero-project/monero/pull/9295 "Fix embargo timeout in dandelion++"     

> __< vtnerd >__ and possible hardening of when certain messages can be sent, that was specifically used as a vector to run timing analysis     

> __< rucknium >__ I've started to write some code that can analyze the resistance of the tx relay protocol to spy nodes, using monerosim. I had in mind possibly doing a comparison test with and without PR #9295     

> __< rucknium >__ I'm not sure if I should run the simulations with tx relay v1 or v2. jberman:monero.social  or boog900:monero.social , do you have any opinions or info on when tx relay v2 might be deployed to mainnet?     

> __< jberman >__ boog900:monero.social reviewed the latest changes to tx relay v2 here: https://github.com/seraphis-migration/monero/pull/450     

> __< rucknium >__ In theory, there shouldn't be a big difference in the privacy of v1 and v2, but I would want to test what's most reasonable.     

> __< jberman >__ I think we will want to get that tested in beta, as testing uncovered the issues that PR solved (including with a change to the p2p messaging protocol)     

> __< jberman >__ I was going to raise this in discussion of stressnet, but with that review, I think that gives the green light for including those changes in tx relay v2 and moving forward with them for beta     

> __< rucknium >__ Thanks for the info. I think I will start with v1 because deployment of v2 seems to be a little further in the future.     

> __< rucknium >__ More discussion of this item?     

> __< jberman >__ boog900:monero.social also raised the point that this PR should help as well: https://github.com/monero-project/monero/pull/11048     

> __< jberman >__ which should land in next release (I'd figure it's maximally helpful when the whole network is running it, though)     

> __< sech1 >__ from the description, it does help     

> __< rucknium >__ By the way, the simulation analysis is going to have to handle some interesting statistical issues to separate the noise of different simulation seeds from actual true differences in privacy levels of any proposed change. I will look into it myself, but input from others is appreciated.     

> __< rucknium >__ 7. FCMP beta stressnet (https://github.com/seraphis-migration/monero/releases/).     

> __< rucknium >__ The people cry out for a new fork from testnet :D     

> __< slowbeardigger:matrix.org >__ rucknium: indeed     

> __< slowbeardigger:matrix.org >__ I can’t wait xd     

> __< jberman >__ Yes looks like people want a fresh chain, and jeffro256:monero.social 's idea to raise the min penalty fee zone to current stressnet's max block size to allow for larger blocks right away seems reasonable to me     

> __< jeffro256 >__ yay     

> __< jberman >__ With boog's green light on this PR https://github.com/seraphis-migration/monero/pull/450 , I think now we should be good to have all code for a beta v3 ready     

> __< jberman >__ So will aim for next week to have latest master on the beta stressnet branch + a new v3 ready to go     

> __< jberman >__ jeffro256:monero.social we could maybe reuse that logic from v2 to have nodes auto pop back to the prior fork height     

> __< rucknium >__ I may halt my spammers on the current stressnet.     

> __< jberman >__ I can turn this into the v3 checklist and people can follow along there as we knock out the tasks: https://github.com/seraphis-migration/monero/pull/415     

> __< vtnerd >__ crap my ssl patch needs another rebase, adding that to my list this week     

> __< jberman >__ I think maybe wait til we have all of master in to avoid another round of conflicts     

> __< vtnerd >__ ok     

> __< rucknium >__ Anything more on stressnet?     

> __< rucknium >__ 8.  PoW-Admitted Zero-Fee Transactions for P2Pool (https://gist.github.com/SChernykh/aae5b2d414095e742437134ab20d4353).     

> __< rucknium >__ sech1     

> __< sech1 >__ In a few words: I think I found a way to introduce 0-fee transactions without their downsides (tx spam), by requiring PoW for them (PoW solutions are cryptographically bound to each tx). Read the link above     

> __< sech1 >__ The main purpose is to use them for miner payout consolidations     

> __< sech1 >__ and to add more incentives to mine with P2Pool     

> __< rucknium >__ Are these txs broadcast throughout the network, or only accepted in the txpool of nodes that have a p2pool miner attached?     

> __< sech1 >__ They are broadcast through P2Pool network layer, not Monero     

> __< sech1 >__ P2Pool only sends mined blocks to monerod (blocks with 0-fee transactions, if any)     

> __< rucknium >__ OK. I read the first two sections, but I did not remember seeing a clear statement on that.     

> __< sech1 >__ monerod doesn't accept/relay such transactions, so it's the only way     

> __< rucknium >__ Doesn't that slow down block propagation because those txs need to be requested instead of pure fluffy blocks propagation?     

> __< sech1 >__ hmm, it does     

> __< sech1 >__ By how much - it's another question that will need testing     

> __< jeffro256 >__ For p2pool consolidations, you can also do it with out PoW by having the p2pool nodes build a set of all p2pool outputs, then attaching FCMPs on the side of the tx that prove the inputs are in the set of p2pool outputs. This, of course, leaks that the tx is a consolidation tx.      

> __< sech1 >__ Note that 0-fee transactions as described are already possible already today, just no one does it. P2Pool proposal just makes it more viable to use.     

> __< sech1 >__ jeffro256 I think DataHoarder is looking into this     

> __< tevador >__ The consolidation tx may be quite large, 128-input FCMP++ is ~180 KB.     

> __< DataHoarder[m] >__ I am and reimplementing some stuff yes. Even aggregation of outputs (but that is more complex)     

> __< sech1 >__ Yes, consolidation tx are large, but they will happen anyway because P2Pool miners do need to use their mined coins     

> __< sech1 >__ The proposal just exchanges monetary fee with a PoW fee (electricity, time spent)     

> __< tevador >__ My point is that each node at each hop will need to download 180 KB from the sending peer, slowing block propagation. Maybe it's acceptable.     

> __< rucknium >__ You could have all nodes accept these txs so that block propagation would not be delayed. But that's risky because a flaw in the p2pool implementation side could open the door to malicious spamming throughout the network.     

> __< sech1 >__ Don't forget that P2Pool submits mined blocks to all its nodes, and 0-fee tx will also be submitted to all P2Pool nodes at the same time     

> __< sech1 >__ which limits the number of hops to the entire Monero network to 1-2     

> __< sech1 >__ Because all P2Pool nodes will mine the same 0-fee tx once its broadcasted (through P2Pool network)     

> __< rucknium >__ Mining pools could attach p2pool to their nodes that produce block templates to speed up propagation where it matters the most, but that would require action by the operators of the mining pools. And it could leave out solo miners who don't do that.     

> __< sech1 >__ IIRC supportxmr runs P2Pool instances on their servers     

> __< sech1 >__ It's in the interest of mining pools to receive P2Pool blocks faster, and they can just run a node - they don't have to diverge hashrate to it     

> __< sech1 >__ solo miners can do the same, if they're informed about it     

> __< boog900 >__ I recently made an issue for making it so normal nodes can fast relay blocks like p2pool: https://github.com/seraphis-migration/monero/issues/454     

> __< jberman >__ rucknium: Relevant: boog900:monero.social's idea to relay blocks that pass PoW before doing validation would help, so nodes can at least start doing the work in parallel (but yes would still need to request and verify said txs)  https://github.com/seraphis-migration/monero/issues/454     

> __< sech1 >__ Yes, P2Pool implementation must be rock solid in terms of verifying that a specific PoW solution does bind to a specific transaction - but all the machinery is already in P2Pool (merge mining) and it's battle tested     

> __< jberman >__ ha, jinx     

> __< sech1 >__ Monero relaying PoW-checked blocks will not be faster than P2Pool unless it also enables RandomX dataset (+2 GB on RAM requirements) by default     

> __< sech1 >__ P2Pool does it, Monero daemon is more restricted     

> __< slowbeardigger:matrix.org >__ i think i have the right idea…     

> __< sech1 >__ It can be enabled with an environment variable, by it's off by default     

> __< sech1 >__ *but     

> __< boog900 >__ It should still make the network as a whole faster rather than just p2pool doing it      

> __< sech1 >__ true     

> __< boog900 >__ And it removes the requirement of running p2pool to get fast blocks, for example stressnet has no p2pool at all      

> __< sech1 >__ P2Pool does bring the block relay to only 1-2 hops on the scale of the whole network, already, so the improvement will be marginal     

> __< sech1 >__ Because each Monero node is either connected to P2Pool, or 1-2 hops away from a P2Pool-connected node     

> __< sech1 >__ and P2Pool relays all Monero blocks, not just its own     

> __< sech1 >__ but we digress from the 0-fee PoW transactions topic     

> __< boog900 >__ Its an easy change to allow blocks to be invalid if the pow is valid      

> __< sech1 >__ I don't argue that, I'm just saying the improvement will be marginal (but there will be an improvement)     

> __< rucknium >__ More discussion on this? I will keep it on the agenda next time.     

> __< jberman >__ 1-2 hops could be >5-10s if the block has 128-in txs fwiw     

> __< sech1 >__ also true, especially for FCMP++     

> __< sech1 >__ then it's not so marginal improvement, I'm for https://github.com/seraphis-migration/monero/issues/454     

> __< boog900 >__ I would rather specific miner consolidation txs rather than 0 fee txs      

> __< sech1 >__ Same, but there were strong arguments against a specialized tx type     

> __< sech1 >__ so it was decided not to introduce them in the next hardfork     

> __< sech1 >__ I think (?)     

> __< sech1 >__ My preference is: (1) miner consolidation tx type (2) PoW-admitted 0-fee tx     

> __< sech1 >__ and (3) regular consolidation tx paying regular fee - the worst for P2Pool adoption     

> __< boog900 >__ I think 2 can be done with a hope to eventually get to 1      

> __< boog900 >__ I don't think 1 can be done for the next fork      

> __< sech1 >__ which is why I started woring on (2). Right now it's in draft/concept phase only, the actual implementation will take a lot of work due to many edge cases there (this is why that document is so long)     

> __< rucknium >__ We can end the meeting here. Thanks everyone.     

> __< sech1 >__ for example, P2Pool will need to track key images, duplicating some mempool functionality - because the 0-fee tx is not a part of monerod's mempool, and there can be conflicting transactions there     

> __< slowbeardigger:matrix.org >__ i think adapting Emill’s CC0 AArch64 implementation to CARROT’s scalar semantics, with Fiat-Crypto as a permissive portable fallback… > <slowbeardigger:matrix.org> hmmmm     

> __< slowbeardigger:matrix.org >__ would it be ok if I published a small standalone repo so people here can evaluate the idea? I think it may take a couple of days but, doing some research atm.     

> __< tevador >__ After some consideration, I think I'd be willing to relicense from LGPLv3 to MPL 2.0, which should provide sufficient protection with less friction for Monero.     

> __< jeffro256 >__ Not sure how MPL 2.0 is materially different from LGPLv3 in terms of its impact for downstream. If downstream ships release binaries with mx25519 "executable form" inside of it, it sounds like they have to do the same thing as in LGPLv3: provide instructions and licensing text alongside the binary form to access the source code for mx25519      

> __< jeffro256 >__ I honestly don't mind at all the one-time low-effort hurdles that Monero itself needs to do to comply with LGPL or MPL, but the downstream effect is the real sticking point for me.      

> __< jeffro256 >__ It seems to me that the ideal license would be one which differentiates between modified works and non-modified works, requiring modified works in source and object form to be distructed with instructions to copy the source, but relinquishing those requirements for non-modified works.      

> __< jeffro256 >__ Like should we require that Btcpayserver, due to integrating Monero payments/scanning, which uses the carrot_core library, which links mx25519, needs to point to the mx25519 repo in its release archives? Seems kind of silly. But if Btcpayserver had an optimized version of mx25519, then yeah, I'd hope that they publish that     

> __< slowbeardigger:matrix.org >__ your downstream concern makes sense…     

> __< slowbeardigger:matrix.org >__ If the priority is making this easy for Monero and every downstream wallet, would BSD-3-Clause, matching Monero, be the cleanest path? MPL 2.0 still requires a source notice for binaries built from unchanged code I think, while a custom exception might create more legal review.     

> __< slowbeardigger:matrix.org >__ If an explicit patent grant matters, perhaps Apache-2.0 could be the middle ground?     

> __< tevador >__ (1) No "prominent notice that the Library is used". (2) No relinking requirement. (3) No need to bundle GPLv3/LGPLv3 text. (4) Somewhat less strict source code availability requirement.     

> __< tevador >__ ^ For MPL 2.0 vs LGPLv3     

> __< tevador >__ BSD-3 is unacceptable for me because it allows modifications of the library without releasing the modified source code.     

> __< slowbeardigger:matrix.org >__ jeffro256: Just an example here     

> __< slowbeardigger:matrix.org >__ XMRPay’s php mainnet scanner actually vendors unchanged MIT-licensed primitives from MoneroPHP, keeps their attribution and license notices, and builds the payment scanning logic on top (the good stuff).     

> __< slowbeardigger:matrix.org >__ The permissive license makes that integration straightforward. If I modified or optimized those primitives, publishing those changes would also feel like the right thing to do….     

> __< slowbeardigger:matrix.org >__ tevador: hmmm     

> __< tevador >__ MPL 2.0 is my effort to make downstreaming easier. Binary releases using the unmodified version would not have to do much at all.     

> __< slowbeardigger:matrix.org >__ removing the relinking requirement and prominent notice is a meaningful improvement over LGPLv3, maybe It sounds like the remaining downstream question is much narrower: whether including the exact mx25519 source URL in the usual third party notices would be sufficient for untouched builds. If that’s the case, MPL 2.0 seems like a reasonable middle ground.     

> __< jeffro256 >__ tevador: how do you interpret this clause in section 3.2: "If You distribute Covered Software in Executable Form then:     

> __< jeffro256 >__ such Covered Software must also be made available in Source Code Form, as described in Section 3.1, and *You must inform recipients of the Executable Form how they can obtain a copy of such Source Code Form* by reasonable means in a timely manner, ..."      

> __< jeffro256 >__ sorry formatting     

> __< jeffro256 >__ Where "Covered Software" is the work with or without modifications      

> __< tevador >__ I interpret is as giving an URL to the Monero repo or the mx25519 repo. GPL has a stonger wording "Regardless of what server hosts the Corresponding Source, you remain obligated to ensure that it is available"     

> __< jeffro256 >__ So e.g. Btcpayserver still has to provide a link to the mx25519 repo (if not vendored) in their release archives, correct?      

> __< jeffro256 >__ Whether modified or not      

> __< slowbeardigger:matrix.org >__ BTCPayServer would still need to inform recipients where the corresponding mx25519 source is available, whether modified or not.     

> __< slowbeardigger:matrix.org >__ But i think, i maybe wrong… that for an untouched build, a version-pinned URL in the usual third-party notices seems like a relatively small obligation compared with LGPLv3     

> __< jpk68:matrix.org >__ jeffro256: I would also like to know this     

> __< slowbeardigger:matrix.org >__ jpk68:matrix.org: For BTCPay specifically, if BTCPay builds or packages a binary that links unmodified mx25519, FAQ Q8 says BTCPay must inform recipients where the exact corresponding MPL source can be obtained. MPL does not require that link to be inside every release archive, so a visible third-party notice or release p [... too long, see https://mrelay.p2pool.observer/e/8qSTiaALSkFYaTk0 ]     

> __< slowbeardigger:matrix.org >__ as per my AI agent research     

> __< slowbeardigger:matrix.org >__ I provided the chat context too     

> __< tobtoht >__ https://www.mozilla.org/en-US/MPL/2.0/FAQ/ (Link to FAQ)     

> __< jeffro256 >__ Also, neither GPL nor LGPL nor MPL protect people from modifying the code and not publishing the modifications, as long as they don't "distribute" the modified work, right? So e.g. let's say that a LWS made a faster vesion of mx25519. If they are modifying and running the software on their own machines, and not distrubuting th [... too long, see https://mrelay.p2pool.observer/e/oPyaiaALeUNUdFh6 ]     

> __< slowbeardigger:matrix.org >__ How annoying this licensing thing is     

> __< jeffro256 >__ So would GPL even have protected RandomX from private mining pools optmizing it? I don't think it would have, as long as the distribution remained private, which makes sense to do because optimizations are only beneficial if other people don't have them      

> __< tevador >__ The issue of RandomX was closed-source mining software, not pools. Mining software definitely counts as distributing.     

> __< jeffro256 >__ Fair enough, but we agree that the protection is only for out-of-house software?     

> __< tevador >__ Yes, but that's the main point. BSD-3 has zero protection.    

# Action History
- Created by: Rucknium | 2026-08-11T17:15:36+00:00
- Closed at: 2026-08-26T13:35:51+00:00
