---
title: Monero Research Lab Meeting - Wed 03 December 2025, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1307
author: Rucknium
assignees: []
labels: []
created_at: '2025-12-02T22:54:47+00:00'
updated_at: '2025-12-12T00:20:09+00:00'
type: issue
status: closed
closed_at: '2025-12-12T00:20:09+00:00'
---

# Original Description

Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/meeting.html?p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3. [Bulletproofs* (more efficient membership and range proofs)](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/626).

4. P2Pool consolidation fees after FCMP hard fork. [Coinbase Consolidation Tx Type](https://github.com/monero-project/research-lab/issues/108).

5. [Transaction volume scaling parameters after FCMP hard fork](https://github.com/ArticMine/Monero-Documents/blob/master/MoneroScaling2025-12-01.pdf). [Revisit FCMP++ transaction weight function](https://github.com/seraphis-migration/monero/issues/44).

6. [Proposal: Limit blocks to 32 MB, regardless of context](https://github.com/monero-project/research-lab/issues/154).

7. [FCMP alpha stressnet](https://monero.town/post/6763165).

8. Post-FCMP scaling concepts.

9. Any other business

Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#1303 

# Discussion History
## Rucknium | 2025-12-06T16:44:34+00:00
Log

> __< rucknium >__ Meeting time! https://github.com/monero-project/meta/issues/1307     

> __< rucknium >__ 1. Greetings     

> __< spackle >__ Hello     

> __< boog900 >__ Hi     

> __< emsczkp:matrix.org >__ Hi     

> __< vtnerd >__ Hi     

> __< kayabanerve:matrix.org >__ 👋     

> __< jberman >__ waves     

> __< rucknium >__ 2. Updates. What is everyone working on?     

> __< rucknium >__ me: Starting to use Markov Decision Process to analyze selfish mining countermeasures.     

> __< vtnerd >__ me: completed subaddress lookahead in lwsf, just needs a few tests. otherwise been tracking down bug reports in lws, several of which have been solved     

> __< jberman >__ stressnet, identified a cause of disconnected stressnet nodes when the pool exceeds max weight and submitted a PR for it (this was a bug in the fcmp++ integration code, not an existing issue), continuing to v1.5 stressnet release     

> __< emsczkp:matrix.org >__ me: refining the BP* CCS proposal to introduce potential application scenarios in Monero with the help of kayabanerve:matrix.org     

> __< articmine >__ Hi     

> __< articmine >__ Sorry I am late     

> __< gingeropolous >__ me: making adaptive blocksize simulation websites, gearing up to get working on monerosim again     

> __< articmine >__ I have updated my scaling proposal by incorporating Tevador's concept as a sanity cap     

> __< rucknium >__ 3. Bulletproofs* (more efficient membership and range proofs) (https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/626).     

> __< emsczkp:matrix.org >__ Hi and thank you for this time slot     

> __< rucknium >__ I liked "BulletStar" more :)     

> __< rucknium >__ Bulletproofs* will be harder to search for in a search engine.     

> __< emsczkp:matrix.org >__ Discussing with kayabanerve we've identified several application scenarios for folding in Monero, including (but not limited to) the following:     

> __< emsczkp:matrix.org >__ “Chain proving”. Suppose Alice and Bob each include their own membership proof in a single transaction without revealing their witnesses to each other: Alice creates her proof, passes it to Bob, and Bob adds his proof on top. In this case, we aggregate single-input transactions into one many-input transaction and create a single folded proof.     

> __< emsczkp:matrix.org >__ “Stream proving”. This would enable zkRollups, where many statements are collected across transactions and a folded proof is generated for a batch of transactions.     

> __< emsczkp:matrix.org >__ “Transaction uniformity”. In this scenario, all transactions have a fixed number of inputs and outputs so that all transactions look the same, improving privacy. We currently lack such a feature because larger transactions are too expensive for it to be worth the benefit to privacy. Cheaper standalone multi-input transactions through folding would address this issue.     

> __< emsczkp:matrix.org >__ [... more lines follow, see https://mrelay.p2pool.observer/e/ob7D9c4KUm5QR0Qy ]     

> __< rucknium >__ Any prediction of the computational cost of these applications?     

> __< articmine >__ There may be a case to defer FCMP++ until we obtain these proofs      

> __< jberman >__ No there is no such case     

> __< articmine >__ Especially given the concerns over the state of the code     

> __< gingeropolous >__ these are optimizations right?     

> __< kayabanerve:matrix.org >__ Ones requiring hard forks, such as MLSAG -> CLSAG.     

> __< jberman >__ That design goal sounds like it would apply to all 3 of those applications ya?     

> __< emsczkp:matrix.org >__ rucknium: the most promising benefits in terms of computational costs is the reduction of memory consumption of membership proofs verification. Theoretically and asymptotically this would reduce to log time      

> __< kayabanerve:matrix.org >__ The obvious use-case is within a transaction, across inputs (or even within a single input), assuming the overhead from folding is sufficiently small.     

> __< kayabanerve:matrix.org >__ That inherently leads to uniformity being worth the performance hit due to the performance being so improved.     

> __< kayabanerve:matrix.org >__ Larger efforts, folding across transactions, are theoretically enabled by this but would require much more work on integration.     

> __< kayabanerve:matrix.org >__ (presumably, block builders would need to form a meta-proof, but I did once propose a way for a pool of proofs which anyone could fold onto)     

> __< kayabanerve:matrix.org >__ That's my view of it, at least     

> __< emsczkp:matrix.org >__ jberman: Yes, and I believe independently of the top-level design.     

> __< jberman >__ That design goal sounds fine to me. Imo "stream proving" is by far the most useful followed by "tx uniformity" followed by "chain proving". I hear how implementing within a single tx would be much simpler to integrate. I think we can cross that bridge when we get to it though once the foundational research is more firmly established     

> __< rucknium >__ IMHO, this sounds like a worthy CCS. Good applications and a reasonable budget.     

> __< jberman >__ small nit: "stream proving" sounds like it's interactive at time of tx construction, but the goal is to be able to fold already constructed proofs into 1 proof AFAIU i.e. you can separate folder from provers      

> __< kayabanerve:matrix.org >__ Not quite, AFAIK, jberman:monero.social:     

> __< kayabanerve:matrix.org >__ In general, folding requires creating the proof on top of prior proofs. Folding proven proofs would require proving a meta-proof and folding that.     

> __< kayabanerve:matrix.org >__ (To my understanding, obviously emsczkp:matrix.org: should be deferred to here for their work)     

> __< jeffro256 >__ jberman: If true, then this wouldn't be a nit, it would be a complete overhaul in the privacy model expected in Monero which turns the privacy battlefield to the network level. I don't think that it would ever be acceptable to require interaction from the folder IMO      

> __< kayabanerve:matrix.org >__ While I'm unsure if the results will be applicable, and applicable in a timely fashion given other potential developments (quantum computers), I find the work reasonable and the concept of folding universally relevant to Monero's future. I also find the rate incredibly reason and see no reason we shouldn't be happy to have emsczkp:matrix.org: working on Monero as a researcher.     

> __< kayabanerve:matrix.org >__ Sorry, I responded to the wrong thing. I was thinking of "chain proving". Durr.     

> __< emsczkp:matrix.org >__ i outlined "stream proving" as different case of "chian proving". The first should be done by a separate "folder" that aggregates statements (such as a sequencer in zkRollups) and it may have knowledge of witness. The chain proving does not     

> __< kayabanerve:matrix.org >__ For "stream proving", yes, I believe the pitch would be for the block builder to perform the aggregation without a loss in privacy     

> __< kayabanerve:matrix.org >__ 🤔 I'll be quiet and leave it to emsczkp:matrix.org:     

> __< jberman >__ kayabanerve:matrix.org: this was my thought as well. My nit is just highlighting how the name "stream proving" sounds like it could require interaction from tx provers. "stream folding" may be better here     

> __< jberman >__ or just "rollups"     

> __< jberman >__ in any case, I'll reiterate I'm a strong +1 on the proposal too :)     

> __< jeffro256 >__ emsczkp:matrix.org: "Stream proving" may have knowledge of the witness or must have knowledge of the witness to do its job?  For the record, I'm supportive of the CCS proposal either way.     

> __< kayabanerve:matrix.org >__ I think the next question here is "what's the witness"? Is the witness the opening of the membership proofs, or is the witness the original proofs which were folded into this succinct proof?     

> __< kayabanerve:matrix.org >__ Because the folder of proofs into a theoretical meta-proof, across the entire chain, produces a proof whose witness is the original proofs. Therefore, they know the witness to their proof (the meta-proof attesting such proofs originally existed) but there's no loss of privacy.     

> __< rucknium >__ More discussion on this item?     

> __< kayabanerve:matrix.org >__ rucknium: jeffro and I asked for clarifications on theoretical applicability to folding proofs across transactions, but seems the CCS itself is well-liked :)     

> __< rucknium >__ 4. P2Pool consolidation fees after FCMP hard fork. Coinbase Consolidation Tx Type (https://github.com/monero-project/research-lab/issues/108).     

> __< rucknium >__ datahoarder:monero.social: More on this?     

> __< rucknium >__ Thank you emsczkp:matrix.org     

> __< datahoarder >__ Nothing currently.     

> __< datahoarder >__ As said last week, working on it and building a schema for it. No updates until then, I'll bring it up once it's ready     

> __< rucknium >__ datahoarder:monero.social: Do you want me to take it off the agenda until you say to put it back on?     

> __< datahoarder >__ Maybe a minor update, a different derivation for coinbase outputs is considered internal to P2Pool that would be ephemeral (not need to be proved in a future turnstile) to allow efficient multisig per block ahead of time     

> __< datahoarder >__ rucknium: Let's do that     

> __< emsczkp:matrix.org >__ jeffro256: I believe it must as the sequencer has to be also trusted, but i need further invesitagion on the current design of rollups     

> __< rucknium >__ Regarding the next agenda item:     

> __< rucknium >__ Others' views on decision making processes are welcome. IMHO, trying to get "loose consensus" in MRL is a good goal, in general for two reasons. And on this specific topic for one practical reason.     

> __< rucknium >__ 1. Compared to majority vote, seeking consensus can help prevent people from being entrenched in their positions. It can encourage creative compromise.     

> __< rucknium >__ 2. Defining a voting body is not easy in MRL. With majority voting, you would have to say who can and cannot vote.     

> __< rucknium >__ 3. ArticMine seems to have a small minority position, but he is in the Monero Core Team. I don't know if Core would approve a Monero node release with a scaling algorithm that ArticMine strongly opposes.     

> __< rucknium >__ 5. Transaction volume scaling parameters after FCMP hard fork (https://github.com/ArticMine/Monero-Documents/blob/master/MoneroScaling2025-12-01.pdf). Revisit FCMP++ transaction weight function (https://github.com/seraphis-migration/monero/issues/44).     

> __< kayabanerve:matrix.org >__ Does this also include my proposal or not yet?     

> __< articmine >__ No     

> __< articmine >__ It includes Tevador's      

> __< rucknium >__ kayabanerve:matrix.org: No. Your proposal is next on the agenda.     

> __< kayabanerve:matrix.org >__ articmine:monero.social: I was asking rucknium:monero.social: about the agenda item, not about you about your proposal.     

> __< boog900 >__ I don't agree with coding in exponential growth of the sanity cap with no extra usage.      

> __< kayabanerve:matrix.org >__ Thank you for clarifying rucknium:monero.social:     

> __< spackle >__ I think supporters of this proposal owe it to the community to confirm that the daemon can handle a steady stream of 10 to 16 MB blocks.     

> __< spackle >__ If supporters can make their case from evidence, are willing to pin their reputations to that claim, and there are not objections from others preventing consensus on the matter, then I have nothing to add.     

> __< kayabanerve:matrix.org >__ I agree with boog900:monero.social: with disliking how the sanity cap may become progressively insane     

> __< jberman >__ emsczkp:matrix.org: this sounds like "stream proving" actually would be the more accurate term in that case, since sounds like there would be some privacy loss if the sequencer is indepedent. I think the design goal of an untrusted sequencer would be ideal, but the applications described would still be useful even if not     

> __< sgp_ >__ fwiw, progress was made by ArticMine adding a ~40% max growth per year cap. This cap increases without any consummate increase in block demand, but there may be more restrictive caps (e.g. the long term median) at any given moment. One dispute seems to be whether scaling should permit "catching up" to this cap with a time peri [... too long, see https://mrelay.p2pool.observer/e/9Z3i9s4KRzFnek1F ]     

> __< rucknium >__ Polynomial growth instead of exponential?     

> __< ofrnxmr >__ From discussion in mrlounge, id agree with a kayaba-style "or" condition that limits the to higher of exponential cap vs packet size limit (or serialization limit)     

> __< ofrnxmr >__ Limits the sanity cap*     

> __< articmine >__ Catching up is critical      

> __< articmine >__ This is now the essence of the disagreement      

> __< boog900 >__ I also disagree with the rest of the changes to the scaling that have undergone very little discussion      

> __< sgp_ >__ as you can see ArticMine is in strong favor of it, whereas others (including me; make your voices heard everyone else) prefer not to have this catch-up     

> __< ofrnxmr >__ Since we cant actually sync blocks > 100mb under any circumstances. 40% would keep us under 100mb for 6 more years. The last hf was 3yrs ago     

> __< sgp_ >__ boog900: I agree; the increase of the long term median is an example of something that seems unnecessary     

> __< articmine >__ sgp_: This has been discussed at length going back to 2020     

> __< sgp_ >__ but after only weeks and weeks of discussion, we convinced one person that multi-gig blocks within one year is not acceptable. yay     

> __< jeffro256 >__ sgp_: By the "increase long term median", do you mean without prior increased chain activity, b/c the median has always had the potential to grow given that the priot median block size has increased      

> __< spackle >__ I also find the design to be disagreeable and agree with boog900's perspective. That said, I hold myself to the statements I made above (at the start of this topic).     

> __< articmine >__ sgp_: I knew code rot     

> __< sgp_ >__ I mean the rate, sorry for the confusion     

> __< ofrnxmr >__ spackle: from 1.7x -> 2x     

> __< ofrnxmr >__ Replie to wrong msg     

> __< articmine >__ While ignoring that the short term median cap is dropped from 50 to 16     

> __< articmine >__ ...  and the maximum block weight is dropped from 100 to 16     

> __< kayabanerve:matrix.org >__ When I disagreed with the input limit, I acknowledged I was the minority and while I kept my position clear, I understood consensus was for a much higher input limit than I'd personally reasonably support. I understand ArticMine's history not just within the project yet on this specific topic, but given the work on the stressn [... too long, see https://mrelay.p2pool.observer/e/uL2C984KRkhGUmpp ]     

> __< kayabanerve:matrix.org >__ I do understand some of this is part of the discussion process, a process ongoing for months, and I'm happy this latest proposal has improved from a wider belief of critically-flawed to solely disagreed-with (after incorporating a design from tevador as a safety mechanism, tevador themselves a voice held in high regard) though.     

> __< kayabanerve:matrix.org >__ It _feels to me_ like we're talking down to an agreeable design instead of working out an agreeable design from the start.     

> __< kayabanerve:matrix.org >__ (If that's even possible, I understand in a room of such different opinions, there isn't an agreeable starting point)     

> __< articmine >__ Then go back to eliminating the long term median entirely     

> __< articmine >__ That is in Tevador's concept      

> __< ofrnxmr >__ The limit is the lower of the LTM and the Sanity Cap     

> __< jeffro256 >__ I'm actually in support of some long term sanity cap on the long term median that doesn't require chainstate  besides block height, for quicker failures in block handling, given that it is an ADDITIONAL restriction, not a loosening of some other parameter. I think an exponential factor around 1.4 is reasonable and gives us time to cap if further.      

> __< articmine >__ Correct      

> __< ofrnxmr >__ in eli5, isnt this "16mb max short term median, but really capped to 10.8 at current time. Max long term median of 2x 16mb, but really still capped to 10.8mb. So the actual median cant go above 10.8mb"     

> __< jeffro256 >__ What is the current proposed rate of change of this long-term cap? (just to be sure i'm not mixing numbers)     

> __< articmine >__ The cap starts at 10     

> __< datahoarder >__ jeffro256: an attack is to submit a block with zero txs but with extremely large miner tx. That after FCMP++ is no longer possible. Given we are checking on height, maybe it'd be reasonable to limit this input as well     

> __< jeffro256 >__ 10 MB?     

> __< ofrnxmr >__ jeffro256: 38.8% per yr     

> __< articmine >__ jeffro256: ~1.39 x a year     

> __< jeffro256 >__ datahoarder: Are coinbase txs not also limited to 1MB? Lemme check     

> __< datahoarder >__ they are post FCMP++ afaik     

> __< kayabanerve:matrix.org >__ I don't like how the net will break after 7 years/the net's fundamental limits will cause 'valid' blocks to be rejected after 7 years.     

> __< datahoarder >__ extra data can bloat it before the limit.      

> __< kayabanerve:matrix.org >__ Coinbase TXs have no limit other than block size until FCMP++ which enforces extra and output limits.     

> __< boog900 >__ I wont support a block size bomb which will require a future fork to change scaling vs just changing the long term median growth rate to an acceptable level      

> __< kayabanerve:matrix.org >__ We may upgrade the net in seven years. We presumably will as the network hasn't ossified. I don't see why we shouldn't update the sanity limit five years from now via hard fork given we know this will definitively become incongruent with reality at time of deployment.     

> __< kayabanerve:matrix.org >__ But that leads into the next agenda topic, so I'll leave my criticism there for now.     

> __< articmine >__ kayabanerve:matrix.org: At least people have notice     

> __< boog900 >__ articmine:monero.social: would you support exponential to a hard limit of 90 MB?     

> __< articmine >__ No     

> __< ofrnxmr >__ boog900: (under the packet size limit)     

> __< rucknium >__ boog900:monero.social: Some alternatives to exponential growth are: 1) Polynomial growth, 2) Logistic Growth  https://en.wikipedia.org/wiki/Logistic_function#In_economics_and_sociology:_diffusion_of_innovations 3) Bitcoin Cash's block size algorithm with a control function https://gitlab.com/0353F40E/ebaa#technical-description     

> __< boog900 >__ ofrnxmr: have to account for overhead      

> __< articmine >__ Can we not fix this in 5 years      

> __< kayabanerve:matrix.org >__ boog900:monero.social:  Isn't that the next agenda topic? Have the lines disappeared? :(     

> __< ofrnxmr >__ articmine: Will need a hard fork to remove the limit afaik (?)     

> __< kayabanerve:matrix.org >__ articmine: Can we not have the net blow up in five years if we don't fix it?     

> __< ofrnxmr >__ So can cross that road at the same time     

> __< kayabanerve:matrix.org >__ We need a HF, either to:     

> __< kayabanerve:matrix.org >__ A) Stop the net from blowing up     

> __< kayabanerve:matrix.org >__ B) Not have overly limited capacity     

> __< kayabanerve:matrix.org >__ I'd rather be slower than incongruent and unstable     

> __< articmine >__ kayabanerve:matrix.org: What you are telling me is that someone put in a scaling bomb in the code     

> __< kayabanerve:matrix.org >__ Even if a new relay protocol isn't a HF itself, it will force old nodes to update if they can't download new blocks unless they update to it.     

> __< articmine >__ No wonder everyone is up in arms     

> __< kayabanerve:matrix.org >__ articmine:monero.social: Your proposal will force a hard fork in ~7 years if this growth occurs.     

> __< boog900 >__ rucknium: I would much rather it take usage to increase the limit but slower growth would be better.      

> __< kayabanerve:matrix.org >__ Or we'll have a netsplit     

> __< articmine >__ kayabanerve:matrix.org: I understand. This is a scaling bomb that needs a HF to fix     

> __< kayabanerve:matrix.org >__ ... so if you acknowledge you're proposing putting a clock on blowing up the network, can you agree to not do that and accept a 90 MB hard cap?     

> __< kayabanerve:matrix.org >__ Or no, you're acknowledging you're proposing a bomb and you refuse to not do so?     

> __< rucknium >__ boog900:monero.social: The BCH algorithm does require usage to increase the limit FWIW.     

> __< jeffro256 >__ To be fair, a 100 MB serialization limit does not necessarily limit the block size to 100 MB if the block is sent over multiple packets. I will need to check again, but I think that the syncing protocol already supports syncing individual txs from other nodes at a time, and only ~60 bytes per block is needed to validate PoW     

> __< ofrnxmr >__ Caveat that removing the 90mb sanity cap can/will be done at the same time as the packet size removal/fix     

> __< articmine >__ No I am not proposing a bomb. I am proposing fixing this in the next HF     

> __< ofrnxmr >__ jeffro256: 100mb packet size limit     

> __< jeffro256 >__ Sorry yes, packet size limit      

> __< kayabanerve:matrix.org >__ articmine:monero.social: That is a bomb though. You're saying this will blow up unless there is a next HF. That's the whole reason it's being called a bomb.     

> __< kayabanerve:matrix.org >__ jeffro256:monero.social: Yeah, I did wonder if we could shim such networking protocols.     

> __< articmine >__ Which means not supporting ANY HF that doesn't fix this      

> __< kayabanerve:matrix.org >__ Clarifying, I'm saying your proposal, if enacted with the FCMP++ HF, will require yet another HF after in order to not cause a net split (unless we create radically new networking proposals which are also backwards compatible).     

> __< jeffro256 >__ ArticMine is saying that it can blow up now, the bomb is already planted. Albeit, his proposed scaling changes would make it trigger faster, but we need to fix it even if we didn't HF to FCMP++     

> __< articmine >__ Then defuse the bomb     

> __< jberman >__ packet size limit has been there from the start fwiw: https://github.com/monero-project/monero/blob/1a8f5ce89a990e54ec757affff01f27d449640bc/contrib/epee/include/net/levin_base.h#L71     

> __< kayabanerve:matrix.org >__ Your proposal doesn't articmine:monero.social: , not without the 90 MB limit boog900:monero.social:  asked you for and you declined     

> __< articmine >__ Why is it so difficult to fix this?     

> __< jeffro256 >__ kayabanerve:matrix.org: It's possible to defuse w/o the 90MB limit by a smart syncing protocol      

> __< kayabanerve:matrix.org >__ I'm sorry, this is going in circles so I'm withdrawing until the next agenda item. Your proposal, which assumes and mandates yet another network upgrade later (though as jeffro256 notes, one POTENTIALLY backwards compatible) is itself a bomb.     

> __< ofrnxmr >__ Various other limits adde here https://github.com/monero-project/monero/commit/3c7eec152cd5663c461f64699574943d3619f0b9     

> __< jberman >__ I think the added sanity cap following tevador's proposal makes sense, with a hard cap at 90mb that can be eliminated once the daemon is rearchitected to actually be able to support it     

> __< jbabb:cypherstack.com >__ Please do not delay the FCMP HF for any reason.     

> __< boog900 >__ jeffro256: we are betting on that happening before the 100 MB is hit. ngl I gave 90 MB as an example, I knew artic would not agree to it. The exponential growth will get out of hand eventually we will need to HF to decrease it.     

> __< jbabb:cypherstack.com >__ It is the single most important change and controversial changes should not be paired with it if at all possible.     

> __< ofrnxmr >__ 90mb wont be hit for 6 years     

> __< ofrnxmr >__ (sanity cap)     

> __< articmine >__ We need to separate the 90 MB hard cap from my proposal      

> __< articmine >__ Is it acceptable otherwise      

> __< boog900 >__ boog900: This is what I originally said was a bomb, the fact that in enough years the sanity cap grows so much it is no longer in play.      

> __< ofrnxmr >__ articmine: its just an "or" on top of your proposal     

> __< boog900 >__ articmine: TO YOU.     

> __< kayabanerve:matrix.org >__ jeffro256:monero.social: Wallets, RPC also breaks     

> __< ofrnxmr >__ Lower of 90mb vs exponential growth vs LTM vs STM     

> __< jeffro256 >__ kayabanerve:matrix.org: Sure, but also those limits can be changed very easily in comparison to p2p limits      

> __< jbabb:cypherstack.com >__ as spackle said earlier: essentially, what can the daemon handle today?  what can stressnet actually prove as feasible?     

> __< kayabanerve:matrix.org >__ Even if the nodes syncs the blocks, it can't serve them and an upgrade is mandated     

> __< rucknium >__ AFAIK, stressnet hasn't hit any hard limits yet. Just hitting annoying snags.     

> __< jberman >__ jbabb:cypherstack.com: we're still not at the stage where we can answer definitively unfortunately. pool exceeding max default size triggered other issues that took time to investigate and deal with     

> __< ofrnxmr >__ txpool is a fiasco :)     

> __< datahoarder >__ rucknium: It might be easier to test/prove limits on beta stressnet, but if it can't reach "hard" limits these soft limits are effectively the scaling limits     

> __< articmine >__ As for as the 100 MB bomb there are only two options:     

> __< articmine >__ Fix it      

> __< articmine >__ Put in a hard cap     

> __< articmine >__ This has nothing to do with my proposal      

> __< boog900 >__ temporary hard cap that will be HF'd away from just as we will HF to lower the sanity growth rate      

> __< articmine >__ My proposal does have a built in temporary hard cap      

> __< boog900 >__ that grows exponentially ... yes we know      

> __< articmine >__ That is irrelevant      

> __< articmine >__ It is temporary      

> __< kayabanerve:matrix.org >__ I actually do think this agenda item is best served by discussion on the rest of the proposal since the next item is on such a hard cap.     

> __< articmine >__ kayabanerve:matrix.org: I agree     

> __< kayabanerve:matrix.org >__ That encouragement follows AM's question here ^ > <articmine> Is it acceptable otherwise      

> __< rucknium >__ 6. Proposal: Limit blocks to 32 MB, regardless of context (https://github.com/monero-project/research-lab/issues/154).     

> __< kayabanerve:matrix.org >__ Oh, there we are     

> __< datahoarder >__ ^ afaik it was withdrawn > <kayabanerve:matrix.org> I'm sorry, this is going in circles so I'm withdrawing until the next agenda item. Your proposal, which assumes and mandates yet another network upgrade later (though as jeffro256 notes, one POTENTIALLY backwards compatible) is itself a bomb.     

> __< kayabanerve:matrix.org >__ I'm fine with 16-90 MB, I just support 32 MB.     

> __< kayabanerve:matrix.org >__ I'd like to discuss this (some hard cap) independently to any/all other proposals. 32 MB is due to the stability of the current stressnet. 90 MB is an actual hard requirement of the P2P and RPC layers.     

> __< articmine >__ I am not. Fix the bonb     

> __< kayabanerve:matrix.org >__ Shall we get consensus on a 90 MB hard cap and fine grain from there?     

> __< kayabanerve:matrix.org >__ At worst, the network is artificially limited and we have to issue a new HF in some years to remove the limit, when we upgrade the P2P and RPC.     

> __< kayabanerve:matrix.org >__ At best, we stop a net split which will occur unless we upgrade the P2P layer.     

> __< articmine >__ Like I said there are two choices      

> __< articmine >__ Fix     

> __< articmine >__ 90 MB hard cap     

> __< sgp_ >__ I'd rather have a hard cap until we know the network won't break, personally. Removing it would only be symbolic not functional (if the network would break anyway if reached)     

> __< jbabb:cypherstack.com >__ kayabanerve:matrix.org: I'd prefer a much much lower hard cap until a "scalenet" proves technical feasibility for larger blocks on a sustained basis     

> __< kayabanerve:matrix.org >__ The fact this stops an inevitable net split if such larger blocks were to naturally occur should make 90 MB without disagreement IMO, even if I'd like to discuss from there a bit more moderation (32 or 64 MB).     

> __< kayabanerve:matrix.org >__ articmine:monero.social: The intent is a N MB hard cap _until_ it's fixed.     

> __< jberman >__ articmine: "Fix" = a hard fork since older daemons won't be compatible, so it's not ingenuous to characterize it as strictly a fix     

> __< kayabanerve:matrix.org >__ As right now, it isn't fixed and can break.     

> __< kayabanerve:matrix.org >__ Now, large blocks aren't working but also won't break the net (under this proposal).     

> __< articmine >__ Let me start with No to any hard cap below 90 MB     

> __< ofrnxmr >__ tevadors proposal limits growth to below 90mb for another 5.5yrs. Adding a 90mb hard cap (kayaba) means that in 6yrs it will stop growing     

> __< ofrnxmr >__ We dont need to demonstrate that TODAYS nodes can handle 90mb, as that test is 5yrs away     

> __< sgp_ >__ And if it's fixed by a fork in the meantime, it can be removed before the limit is ever reached     

> __< jeffro256 >__ If we go with a semi-permanent fixed hardcap, I also support 90MB     

> __< kayabanerve:matrix.org >__ jbabb:cypherstack.com: That's the 32 MB number, but it sounds like you agree with *a* cap, as does sgp_:monero.social:  :)     

> __< sgp_ >__ Add it until it's fixed imo     

> __< kayabanerve:matrix.org >__ jeffro256:monero.social: Heard on if. Do you support 90 MB with FCMP++ though?     

> __< sgp_ >__ When fixed, I don't think anyone here will be hard-line for a permanent cap ala Bitcoin style. So it's fine     

> __< jbabb:cypherstack.com >__ ofrnxmr: we should, lest an attacker demonstrate for us that we can't     

> __< kayabanerve:matrix.org >__ Also, ping boog900:monero.social: to specifically state their opinion on this so I don't assume their stance from the prior agenda item     

> __< articmine >__ I cannot support any hard cap. On 90MB  I ABSTAIN      

> __< kayabanerve:matrix.org >__ I'd also so love ofrnxmr and jberman:monero.social: and rucknium:monero.social: 's opinions     

> __< sgp_ >__ This gets us out of a potential emergency fork in the future, which hopefully we don't need. But no need to sign us up for one now     

> __< articmine >__ Anything below NO     

> __< ofrnxmr >__ Im in favor of a 90mb cap that wone be reached for over 5yrs due to a sanity cap of 1.4x yearly max growth     

> __< kayabanerve:matrix.org >__ Abstain is much better than I thought we'd receive, and I truly appreciate you willing to not block this motion even if you don't support it articmine:monero.social:     

> __< boog900 >__ I would be ok with a 90 MB cap, as a separate thing from artic's scaling proposal.      

> __< kayabanerve:matrix.org >__ I also will note I do want to stop this from ever being relevant. I do want to improve the node to the point this can be removed and we can defer yo the standard policy     

> __< rucknium >__ How difficult is it to remove the 100MB packet size limit?     

> __< ofrnxmr >__ Im not in favor of ballooning to 90mb within 2026     

> __< kayabanerve:matrix.org >__ But as we are still deciding a standard policy, and as we already have such a hard limit (albeit poorly defined), I support this     

> __< jeffro256 >__ Sure, only to prevent mentioned aforementioned net splits  > <kayabanerve:matrix.org> jeffro256:monero.social: Heard on if. Do you support 90 MB with FCMP++ though?     

> __< articmine >__ ofrnxmr: My proposal speaks for itself     

> __< ofrnxmr >__ rucknium: Its been there since genesis, and there are a bunch of other limits that have been added on top. Likely sue to hackerone stuff     

> __< kayabanerve:matrix.org >__ rucknium:monero.social: The concern is the potential DoS effects from that, not the removal itself, of course     

> __< ofrnxmr >__ due*     

> __< boog900 >__ rucknium: it may require a new p2p block propagation and syncing protocol      

> __< kayabanerve:matrix.org >__ ofrnxmr:monero.social: Of course, this is in conjunction with scaling policies, not as the sole scaling policy     

> __< sgp_ >__ Yay, we agreed to a thing within one meeting 🎉     

> __< rucknium >__ That goes back to what I said many meetings ago: Lost of technical debt from "temporary" limits that do not fix the core issues.     

> __< kayabanerve:matrix.org >__ And RPC updates     

> __< datahoarder >__ kayabanerve:matrix.org: so the compromise is a hard limit, like your proposal, but 90 MB. seems the last piece that would vote no is abstaining     

> __< jeffro256 >__ rucknium: We shouldn't remove the 100MB packet size limit IMO, we should just download chain data correctly.     

> __< rucknium >__ lots*     

> __< kayabanerve:matrix.org >__ rucknium:monero.social: Promoting this to a well-defined item is fixing a core issue.     

> __< kayabanerve:matrix.org >__ A core issue existed. We add spot checks to avoid resolving the underlying issue. Promoting those spot checks as to not conflict with consensus smooths this out.     

> __< vtnerd >__ the other issue is that a new serialization system would need to be in place. We probably hit unpack lots on blocks well before the 100 mib lomit     

> __< vtnerd >__ *unpack limits     

> __< kayabanerve:matrix.org >__ The limitation itself can then be discussed as a suboptimality, but this turns from a house of cards into a proper building: just one which needs more floors built on top.     

> __< articmine >__ sgp_: 90 MB blocks is enough to destroy BS with no additional privacy     

> __< rucknium >__ I would support a 90MB hard cap, then linear increases every year (+10MB/year, for example). That would prevent complete ossification in the event that another hard fork were infeasible.     

> __< ofrnxmr >__ jeffro256: to add to this: monero bans peers that take too long to send packets. so just removing limit would just cause widespread banning if upload speeds arent fast enough     

> __< kayabanerve:matrix.org >__ vtnerd:monero.social: Do you feel 90 MB, leaving 10 MB of room, sufficient for the overhead?     

> __< articmine >__ rucknium: That is my proposal     

> __< articmine >__ Simi     

> __< articmine >__ Similar      

> __< sgp_ >__ monero will not ossify this second because post-quantum is a must anyway     

> __< kayabanerve:matrix.org >__ rucknium:monero.social: While I love the linearity for sanity, that reintroduces the fundamental problem blocks exceed the actually supported size and the goal of promoting the actual limit into a well-defined limit     

> __< rucknium >__ IMHO, non-spam demand for p2p electronic cash is niche according to data that I've seen and analyzed. The limits are useful for defense against a malicious actor, including a malicious actor with large hashpower share.     

> __< sgp_ >__ anyone 5 years from now who says Monero ossification is more important than post quantum protection will be laughed out of the room. I'll make that my mission :p     

> __< kayabanerve:matrix.org >__ I'll note 90 MB was a number boog900:monero.social: mentioned as leaving room for overhead, yet vtnerd:monero.social: is noting that overhead is non-trivial. We may technically end up on a number approximate to 90 MB but not exactly/so literally, as necessary for the intended space for overhead.     

> __< rucknium >__ Data and analysis: https://github.com/Rucknium/presentations/blob/main/Rucknium-Monerotopia-2024-Banking-the-Unbanked.pdf     

> __< ofrnxmr >__ vtnerd: kayaba i think he's referring to 8867 etc, because blocks ~30mb become hard or impossible to sync due to serialization unpacking     

> __< kayabanerve:matrix.org >__ But I'm happy we appear to have large support, and no explicit rejections, for adopting an additional sanity limit of approximately 90 MB: the packet limit with clear space for the inherent overhead.     

> __< ofrnxmr >__ Which is seperate from the packet limit     

> __< jberman >__ I think tevador's proposal + 90mb hard limit due to packet serialization limit is reasonable, and think we re-open discussion on it once stress testing gets further along in helping answer what the daemon can actually handle     

> __< ofrnxmr >__ you can see serialization limits in play by syncing stressnet with --batch-max-weight=50 or --block-sync-size=20 etc     

> __< kayabanerve:matrix.org >__ Ah, thanks for clarifying it's the performance aspect of it, not the static limits.     

> __< vtnerd >__ The issue is the hard limits on objects and strings in the current serialization system. Otherwise 90 mib is likely sufficient      

> __< ofrnxmr >__ kayabanerve:matrix.org: Its actually a static limit 🥲     

> __< articmine >__ vtnerd: It is an absolute mess     

> __< ofrnxmr >__ ofrnxmr: https://github.com/monero-project/monero/pull/9433  pr to increase the limits to, iirc, roughly match 100mb     

> __< boog900 >__ ofrnxmr: for current tx sizes, and for non-pruned blocks.      

> __< vtnerd >__ Even better ofrnxmr:monero.social: that eased the transition to bigger blocks     

> __< kayabanerve:matrix.org >__ Got it. So this 90 MB limit also requires a PR such as https://github.com/monero-project/monero/pull/9433 to align the literal constants at this time, and ideally vtnerd's long-standing serialization PR.     

> __< kayabanerve:matrix.org >__ Sounds like a clear/immediate path forward then, without any objections yet.     

> __< kayabanerve:matrix.org >__ Unfortunately, the consensus seems to be 90 MB and not 32 MB (sorry to myself and jbabb:cypherstack.com:  :( )     

> __< kayabanerve:matrix.org >__ But I'm happy we're planning suboptimality over collapse :)     

> __< ofrnxmr >__ Without tevador's sanity median, id say 32mb. But with it, 90mb (5yrs away) is fine to me     

> __< rucknium >__ I saw a few people, including me, suggest that the 90MB hard cap should still raise slowly     

> __< articmine >__ It is not a median I is a cap     

> __< ofrnxmr >__ rucknium: It does raise slowly with tevadors sanity cap. 10mb * 1.4x per yr     

> __< kayabanerve:matrix.org >__ We can write 90 MB for now and leave 32 MB to be done with the other proposal which will inevitably occur ofrnxmr:monero.social:     

> __< ofrnxmr >__ articmine: Sorry, i mistyped     

> __< kayabanerve:matrix.org >__ rucknium:monero.social: I saw you do so without explicitly objecting to 90 MB, and I saw AM abstain.     

> __< articmine >__ kayabanerve:matrix.org: Why other proposal     

> __< articmine >__ For what reason?     

> __< rucknium >__ I object if it's an indefinite 90MB cap.     

> __< kayabanerve:matrix.org >__ articmine:monero.social: You have a scaling proposal. That's still being discussed, even if 90 MB sanity is agreed to today.     

> __< kayabanerve:matrix.org >__ I'm saying I'm fine with 32 MB, a lower sanity limit, being discussed with other scaling proposals in the context of other proposals, such as yours.     

> __< kayabanerve:matrix.org >__ Note how ofrnxmr said they'd support a lower sanity limit if a median such as tevador's isn't accepted.     

> __< articmine >__ I understand that      

> __< kayabanerve:matrix.org >__ I'm saying I'd try to corral agreement on the higher limit today, and leave lower limits _and other scaling discussions_ independent and open.     

> __< kayabanerve:matrix.org >__ That's all, I wasn't proposing dropping it or saying that itself will be a proposal. Just a discussion item eligible as the rest is.     

> __< kayabanerve:matrix.org >__ But I hear rucknium:monero.social: is now objecting, the first explicit objection to a 90 MB sanity cap :/     

> __< kayabanerve:matrix.org >__ rucknium:monero.social: Care to say more?     

> __< kayabanerve:matrix.org >__ I know I can repeat how Monero will break without this, and will continue with this, but that's been stated already.     

> __< rucknium >__ Raise it linearly by 10MB/year, starting 5 years from now. That's an escape hatch.     

> __< kayabanerve:matrix.org >__ ... An escape hatch into it breaking once again.     

> __< sgp_ >__ removing it is only symbolic if it would in practice break     

> __< kayabanerve:matrix.org >__ I really don't know how to say the protocol will literally break with such large blocks.     

> __< articmine >__ rucknium: It does not help. The only other answer is to fix the underlying issues     

> __< rucknium >__ Can't you just cut the block into pieces? How hard is the engineering, really? (I say as a non-engineer)     

> __< kayabanerve:matrix.org >__ The intent is to remove it as soon as the protocol is improved. Hopefully, the protocol is improved before this ever is actually applied to any blocks.     

> __< kayabanerve:matrix.org >__ rucknium:monero.social: The P2P and RPC layers aren't designed for this. Yes, we can improve the layers. That has to be done.     

> __< articmine >__ kayabanerve:matrix.org: Now I see a path to consensus     

> __< kayabanerve:matrix.org >__ Will this be done over the next give years, making this irrelevant? Probably and hopefully.     

> __< kayabanerve:matrix.org >__ But if those improvements don't happen, will the network break? Yes     

> __< kayabanerve:matrix.org >__ Will this sanity limit stop it from breaking? Yes     

> __< kayabanerve:matrix.org >__ It just also sets an outrageous limit that, assuming a current scaling proposal is adopted (AM or tevador's), will become relevant in ~6 years     

> __< articmine >__ My proposal includes Tevador's      

> __< articmine >__ It is the lower of both      

> __< kayabanerve:matrix.org >__ jeffro did suggest a backwards-compatible p2p improvement could happen but that doesn't resolve the RPC layer and wallet scanning protocol, which likely would need more invasive changes (we currently scan blocks and would likely want to scan outputs?)     

> __< kayabanerve:matrix.org >__ articmine:monero.social: I'm aware, but your proposal incorporating tevador's does not outright invalidate tevador's, which is why I still mentioned tevador's.     

> __< kayabanerve:matrix.org >__ I do support the existence of median's over tevador's alone, personally.     

> __< articmine >__ Of course. Tevador's proposal can be implemented without the long term median      

> __< articmine >__ It is right in the proposal      

> __< ofrnxmr >__ i'd prefer to keep the long term median as a sanity check on the short term median     

> __< kayabanerve:matrix.org >__ So, with the intent to remove this, but with the comment our current stack _will not work_ past the limit defined here, this limit existing in order to stop the stack from entering this broken state of existence, do you still object rucknium:monero.social: ?     

> __< articmine >__ It is more than that. It provides fee stability see issue 70     

> __< kayabanerve:matrix.org >__ Again, I agree we should split blocks into pieces and solve this.     

> __< kayabanerve:matrix.org >__ That just hasn't been done and I don't believe is scheduled to be done before the next HF. It'd be some months of work.     

> __< rucknium >__ Let's hire some engineers from big tech to fix it.     

> __< ofrnxmr >__ articmine: Yes, yes. To be more correct, i oppose removing it     

> __< rucknium >__ Many of them have been laid off recently.     

> __< articmine >__ It can be a CCS     

> __< kayabanerve:matrix.org >__ rucknium:monero.social: docker microservices on the cloud with serverless would fix this     

> __< rucknium >__ The indefinite 90MB cap seems too similar to BTC's "temporary" 1MB cap burned into consensus.     

> __< sgp_ >__ how about we agree not to add the cap by the next hardfork if it's fixed by then? :)     

> __< articmine >__ rucknium: It is     

> __< kayabanerve:matrix.org >__ Anyways. We're all assuming Monero will be upgraded to fix these limitations. This proposal just means we won't break if we don't upgrade, for whatever reason.     

> __< articmine >__ sgp_: I support this     

> __< datahoarder >__ rucknium: suggestion. 90 MB cap would only exist on next fork 2 versions. while this could be adjusted * next * hardfork again, it's more symbolical that it's to be kept ONLY for the specific next one     

> __< sgp_ >__ it's different because it's set at the limit that prevents breakage, not a lower value     

> __< datahoarder >__ (2 versions, initial transition + final)     

> __< kayabanerve:matrix.org >__ If someone redoes the P2P layer and RPC by the FCMP++ HF, with appropriate testing and review, I'm fine not adding this limit with the FCMP++ HF.     

> __< kayabanerve:matrix.org >__ I'm not fine delaying the HF for those milestones however.     

> __< sgp_ >__ a limit to prevent breakage is different philosophically than a limit to enforce a "value" of small blocks     

> __< kayabanerve:matrix.org >__ And not just 'is what nodes can handle'. Nodes can only handle 32 MB. That's the current limit.     

> __< kayabanerve:matrix.org >__ 90 MB is when things _definitively_ break without reworking multiple parts of Monero.     

> __< kayabanerve:matrix.org >__ And, under current discussions, is five years away anyways.     

> __< kayabanerve:matrix.org >__ Suggesting we break in five years if this isn't fixed is a gun to our head. This just removes the round from the chamber.     

> __< articmine >__ This is going to come down to material progress. If so we can keep consensus      

> __< kayabanerve:matrix.org >__ This limit is only proposed as a sanity limit due to fundamental limitations in the current stack. If the limitations are removed, this limit should be removed.     

> __< kayabanerve:matrix.org >__ But we should never allows blocks so big they break the network, whether regarding live operation, syncing the blockchain, or running wallets.     

> __< articmine >__ Still I have to say I commented in the original 1MB BitcoinTalk thread     

> __< articmine >__ In 2013     

> __< articmine >__ Before Monero even existed      

> __< rucknium >__ BCH was testing 256MB blocks in 2022: https://bitcoincashresearch.org/t/assessing-the-scaling-performance-of-several-categories-of-bch-network-software/754     

> __< rucknium >__ Monero can't do it because why?     

> __< ofrnxmr >__ kayabanerve:matrix.org: tbf, the txpool breaks wallets when the pool limit is exceeded 😆     

> __< rucknium >__ Just on the p2p layer     

> __< kayabanerve:matrix.org >__ Because our stack assumes a 100 MB limit in several different places.     

> __< ofrnxmr >__ Why cant we just s/100/256? No clue     

> __< articmine >__ BCH has one problem: Otherwise they can be a brutal competitor     

> __< kayabanerve:matrix.org >__ We can go through and correct each one. We should and will have to.     

> __< articmine >__ The one problem No tail emission      

> __< datahoarder >__ rucknium: we break currently when setting checkpoints :D, so technical debt and specially old code inherited     

> __< kayabanerve:matrix.org >__ But we can potentially break before we do so or we can acknowledge our reality.     

> __< rucknium >__ You're saying that BCH programmers are better than Monero programmers? (Meant to provoke)     

> __< boog900 >__ we did inherit a scam coin      

> __< ofrnxmr >__ boog900: a crippled* scamcoin     

> __< kayabanerve:matrix.org >__ rucknium:monero.social: Would you be fine with a 90 MB sanity limit with the FCMP++ HF if these improvements are not made by the FCMP++ HF?     

> __< articmine >__ rucknium: I am saying that a lack of a tail emission is what is keeping BCH back     

> __< jberman >__ BitcoinSV blocks got up to 3.8gb, they have the best of the best     

> __< kayabanerve:matrix.org >__ Is that the compromise phrasing I can ask to get you to replace your objection with an abstain?     

> __< articmine >__ Actually 4 GB      

> __< rucknium >__ What if cuprate can do it? FWIW, Zcash is completely transitioning to their Rust zebra node.     

> __< articmine >__ For BSV     

> __< kayabanerve:matrix.org >__ BSV also hard forked without admitting it, had an explorer shut down due to all the fallout, and is moving towards just ~6 nodes with a legal framework to arbitrarily move coins before we start seriously discussing them     

> __< boog900 >__ rucknium: its the p2p protocol - we don't have the serialization limits tho      

> __< rucknium >__ The BSV example just drives home the point further.     

> __< boog900 >__ we could make our own p2p protocol     

> __< boog900 >__ then we might fork from monerod :(     

> __< articmine >__ kayabanerve:matrix.org: BSV is a very useful stressnet for Monero     

> __< kayabanerve:matrix.org >__ Rucknium: Would you be fine with a 90 MB sanity limit with the FCMP++ HF if these improvements are not made by the FCMP++ HF, or unless monerod is deprecated for Cuprate (assuming Cuprate fixes this) by the FCMP++ HF?     

> __< jbabb:cypherstack.com >__ BCH does this, BSV does that--anecdotally, I know no real-world users of either in real life.  their block size over time seems to show that despite allowing a lot, they don't actually do a lot that's not spam or token spam     

> __< ofrnxmr >__ Theae transparent coins doing have the verification requirments of private ones     

> __< ofrnxmr >__ Dont* have     

> __< kayabanerve:matrix.org >__ Suggesting a project with less than ten nodes (or attempting to move in that direction) which is attempting to define a legal framework for the blockchain itself is anything for Monero is deeply unserious     

> __< rucknium >__ kayabanerve:matrix.org: kayabanerve:matrix.org: No, I would not be fine with it. But my objection shouldn't stop it from being implemented in the HF release software.     

> __< articmine >__ ofrnxmr: They can bury BS in data     

> __< kayabanerve:matrix.org >__ Then with a sole explicit objection from someone who says their objection shouldn't be a blocker, I'd like to thank you and say we appear to have consensus in favor.     

> __< articmine >__ Even ETH     

> __< ofrnxmr >__ articmine: Eth funds are frozen all the time     

> __< boog900 >__ I think a sufficiently slow scaling algo, which requires years of spam before hitting 100 MB would be fine without the hard cap.     

> __< kayabanerve:matrix.org >__ Even if not unanimous consensus.     

> __< ofrnxmr >__ boog900: I think this would relegate monero to not allowing scaling when needed     

> __< kayabanerve:matrix.org >__ ofrnxmr: Ether itself has not been frozen at any time, and the only unilateral movement I'm aware of was the DAO HF.     

> __< articmine >__ boog900: Let us be reasonable. Like burning XMR by looking it for longer than the age of the universe     

> __< sgp_ >__ fwiw, I think the aversion to a hard limit is healthy. It is scary. It's good to really question why they are there. This is a good Monero community value     

> __< ofrnxmr >__ kayabanerve:matrix.org: Im referring to BS freezes     

> __< ofrnxmr >__ I'd also be ok with doing an s/100/256 etc and using a higher limit than 90     

> __< ofrnxmr >__ But in any event, we need to fix the p2p protocol before we hit those numbers, and that may or may not require a hard fork     

> __< kayabanerve:matrix.org >__ I don't think we could do that without checking every line to ensure every silent limit hodge-podged over the years was considered, but heard that'd be another _acceptable_ option.     

> __< boog900 >__ articmine: how much growth does the current scaling allow?     

> __< boog900 >__ in 1 year of spam      

> __< boog900 >__ a very reasonable amount I assume?      

> __< datahoarder >__ kayabanerve:matrix.org: a network fuzzer for these things would be lovely, and afaik RPC is currently in the books. for P2Pool I included fuzzers for most of the network as well on my code     

> __< ofrnxmr >__ 16 mb * 2 * 2 * 1.24 = 79mb? I think?     

> __< articmine >__ One can push the short term median to 50x 100x for the blocksize      

> __< sgp_ >__ speaking of fuzzing, the MAGIC Monero Fund got another quote for that!     

> __< sgp_ >__ so expect a fundraise for that shortly     

> __< boog900 >__ articmine: 425 MB     

> __< boog900 >__ so reasonable      

> __< rucknium >__ Is preland:monero.social  here?     

> __< articmine >__ My proposal cut this down to 16x for both the short term median and the blocks Less if the sanity cap is triggered      

> __< preland >__ rucknium: I am now lol     

> __< rucknium >__ Did you want to discuss Post-FCMP scaling concepts?     

> __< rucknium >__ at this meeting     

> __< articmine >__ I have a proposal on the table      

> __< boog900 >__ articmine: your first allowed gigabyte blocks, for this one you know the exponential growth makes the limit meaningless after some years     

> __< preland >__ rucknium: Unless anyone has anything else to add, I think we can discuss it next week     

> __< articmine >__ boog900: Never for the short term median     

> __< kayabanerve:matrix.org >__ My proposal is for a solution now because while the try solution is a P2P/RPC rework, that isn't being proposed now. Instead, that can is being kicked. My proposal just makes it safe to kick.     

> __< kayabanerve:matrix.org >__ I'm fine not discussing the can itself at this meeting, or even before the FCMP++ HF.     

> __< kayabanerve:matrix.org >__ If someone else picks up the can and responsibly disposes of it at a recycling center before the FCMP++ HF, I'm fine withdrawing my proposal.     

> __< boog900 >__ articmine: yes eventually we have to rely on only the long term median, which allows gigabyte blocks in a year.     

> __< articmine >__ boog900: No the sanity cap is in place     

> __< kayabanerve:matrix.org >__ But the time for these reworks is reasonably believable to be a year after the FCMP++ HF. While that's plenty before the 5 years of safety bought here, without trade-off, it still justifies safety now.     

> __< gingeropolous >__ finally caught up. silly real work meeting. The way I see it, if we put in a hard, permanent cap, it has the chance to get stuck. Same as with the bitcorn. If we do this 90MB + 10MB a year starting +5 yrs from now, it gives us time to fix whatever in the daemon is capping it, and it can be rolled out without the coordination [... too long, see https://mrelay.p2pool.observer/e/sq_w-c4KX0YtZU5p ]     

> __< jbabb:cypherstack.com >__ do we not already have a hard technical cap that would allow someone to burn fees to incapacitate the network?     

> __< kayabanerve:matrix.org >__ gingeropolous:monero.social: 90+10*(y-5) breaks the network in 5 years unless we HF before then.     

> __< articmine >__ gingeropolous: If my proposal is approved the real test is will the sanity cap exceed 90 MB. If so we have a real problem     

> __< kayabanerve:matrix.org >__ Unless we assume miners self-limit and update to remove the self-limit in a pseudo-network-upgrade as you note as a technicality.     

> __< gingeropolous >__ kayabanerve:matrix.org: , if monerod isn't fixed by then, right?     

> __< rucknium >__ End of meeting is now. Feel free to continue discussing, of course.     

> __< kayabanerve:matrix.org >__ Right, with the immediate fix being the limit, and when those layers are fixed, part of the fix being to remove this limit     

> __< kayabanerve:matrix.org >__ But we either have to fix those layers, or have this cap, or have a bomb.     

> __< articmine >__ kayabanerve:matrix.org: Yes that would remove the ossification issue     

> __< kayabanerve:matrix.org >__ Because no one is proposing the design, effort, and manpower to fix those layers in time, and because the bomb is unaccepted, the sanity limit is the option in front of us.     

> __< kayabanerve:matrix.org >__ Monero isn't ossified, and it'd still require a coordinated upgrade by a majority of hash power while we trust people to forfeit including transactions which would pay them fees until then.     

> __< sgp_ >__ ty rucknium     

> __< articmine >__ For my miner idea to work the cap has to be set at 45 MB     

> __< gingeropolous >__ i mean we're talking about 63GB blocks so im fine with 90MB     

> __< kayabanerve:matrix.org >__ By that argument, we can solely and entirely rely on the median and trusting the miners to do the right thing.     

> __< gingeropolous >__ in a day. sorry.     

> __< kayabanerve:matrix.org >__ Thank you for noting you're fine with it gingeropolous:monero.social:     

> __< gingeropolous >__ if we're filling 63GB in a day and can't find the resources to make it bigger with the serialization and the whatsits... then thats the real problem     

> __< articmine >__ kayabanerve:matrix.org: ...but yes it requires a majority of the hashrate to keep the cap     

> __< gingeropolous >__ but i still don't like hard caps     

> __< gingeropolous >__ and i guess none of us really do     

> __< kayabanerve:matrix.org >__ By my count, and somewhat railroading of ensuring I collected options and trying to declare consensus, we have one explicit objection from Rucknium who said it shouldn't be blocking and even the grace of abstaining by ArticMine. I am happy with that as I believe a solution is needed, and this is the only solution available to  [... too long, see https://mrelay.p2pool.observer/e/l7aL-s4Kd1VRNk5i ]     

> __< kayabanerve:matrix.org >__ Agreed. Do we prefer things not working?     

> __< kayabanerve:matrix.org >__ This just codifies existing hard caps until things are reworked.     

> __< gingeropolous >__ i prefer there being a reason to make things resilient. I worry that strange reasons will arise for keeping 90MB in place regardless of optimizations.      

> __< gingeropolous >__ but these are nebulous fears that probably shouldn't be used to justify time bombs     

> __< kayabanerve:matrix.org >__ I actually believe we should target net-0 blockchain growth and should reject any new transactions after the local database exceeds 300 GB /s     

> __< datahoarder >__ kayabanerve:matrix.org: ring blockchain, starts writing over old ones ;)     

> __< kayabanerve:matrix.org >__ I think the practical argument for a static limit, if any, is if the extra space can only be considered beneficial for the purposes of spam. I don't believe we should allow unnecessary space for the hell of it, yet the medians and relation to the fee policy aim to resolve that without requiring a static limit.     

> __< gingeropolous >__ right, because if we put in the +10 per year thing at year 5, then it has to be fixed. If we slap 90 on it, "it's fine". "its a feature, not a bug!"     

> __< kayabanerve:matrix.org >__ datahoarder:monero.social: boog900:monero.social: Saved 70 GB in Cuprate simply by improving the schema :)     

> __< datahoarder >__ don't doubt it :)\     

> __< kayabanerve:matrix.org >__ There's also a proposal to fold ZK proofs 😱 Imagine the space savings there 😱😱😱     

> __< kayabanerve:matrix.org >__ And what's this? MRL issue for payment channels????     

> __< gingeropolous >__ who knows in 5 years we may have star trek universe and not need money. Boom, problem solved.      

> __< kayabanerve:matrix.org >__ gingeropolous:monero.social: Then it's just the current behavior. This is already scheduled to break in six years with the proposals currently under discussion.     

> __< datahoarder >__ kayabanerve:matrix.org: yep! brought that up on lounge around future scaling hardforks. that'd allow a middle between pruned and full archival node, one that saves pruned txs but proofs per block (and still fully verified)     

> __< kayabanerve:matrix.org >__ Having a limit for five years that breaks after six doesn't solve how the existing proposals break after six years. That's the sole and entire purpose to this proposal.     

> __< ofrnxmr >__ kayabanerve:matrix.org: or break in like a month under current conditions     

> __< gingeropolous >__ indeed     

> __< articmine >__ Must say I am sad.     

> __< articmine >__ 😂     

> __< ofrnxmr >__ i think +10mb / yr is underestimating and doesnt take into accountbthat resources grow exponentially     

> __< ofrnxmr >__ If we did this in 2014, we'd have added like 10kb per yr     

> __< articmine >__ I will of course add the 90 MB cap to my proposal given that it did get at least loose consensus      

> __< kayabanerve:matrix.org >__ To stop things from breaking in six years, unless we do this work, which we should do in the next couple of years.     

> __< gingeropolous >__ me too. but i'd rather a functioning network with 63GB a day than a non-functioning network     

> __< ofrnxmr >__ numbers should reflect reality, and im in favor of 1.4x yearly sanity cap growth     

> __< ofrnxmr >__ Which has been grounded in fact based numbers thusfar (1.4x)     

> __< ofrnxmr >__ If the world changes in 6yrs and growth slows to 1.1x, then we change the sanity cap to reflect that.. but to date, that has not been the case     

> __< boog900 >__ I don't think our capacity will grow at 1.4x forever, I don't think we will hit gigabyte block capacity in 15 years.     

> __< datahoarder >__ Remember https://github.com/monero-project/monero/issues/8827 considered the 8MB/year overhead :)     

> __< boog900 >__ and I would much rather this growth only happen if our usage actually increases      

> __< gingeropolous >__ well i think thats a given     

> __< kayabanerve:matrix.org >__ Thank you ArticMine articmine:monero.social:  ♥     

> __< ofrnxmr >__ boog900: The stm and ltm should deal with this, not the sanity cap     

> __< boog900 >__ the limit increases each year no matter if there is any extra activity of not     

> __< ofrnxmr >__ the stm and ltm dont increase w/o activity     

> __< boog900 >__ the stm and ltm allow gigabyte blocks in a year from 0 so are not exactly safe      

> __< sgp_ >__ yeah but not for several years is the point, which does make it less bad     

> __< ofrnxmr >__ I dont understand how those work, but imo shouldnt allow greater thanmin(sanity, stm) * 2 (or 1.7 etc)per 100k blocks     

> __< kayabanerve:matrix.org >__ I'd prefer if the 38% YoY sanity cap from AM's proposal was instead 38% of the last year or so     

> __< sgp_ >__ ofrnxmr: there is also the short-term "boost" allowance     

> __< kayabanerve:matrix.org >__ or even if it was 60% but still restricted by use, not accumulation regardless of use     

> __< sgp_ >__ kayabanerve:matrix.org: I agree     

> __< ofrnxmr >__ sgp_: isnt that supposed to be limited as well?     

> __< kayabanerve:matrix.org >__ (Not to commit to a larger number, to note I'd prefer a larger number in exchange for limited by actual use)     

> __< ofrnxmr >__ kayabanerve:matrix.org: But then why start at 10mb? Why not start at 110kb 😭     

> __< sgp_ >__ it was picked per tevador's suggestion     

> __< ofrnxmr >__ The avg of the last yr is like 110kb     

> __< ofrnxmr >__ sgp_: Due to 1.4x YoY from genesis     

> __< ofrnxmr >__ Tevadors #s are based on external factors, not volume     

> __< ofrnxmr >__ So if were using volume moving fwd, we should be using volume backward too. Which is like 110kb     

> __< gingeropolous >__ so whats the consensus? 90MB until its proven that the reference client can process x MB blocks something something ... ?     

> __< sgp_ >__ it's due to the estimated sync time at the median speed     

> __< ofrnxmr >__ 90mb unless someone fixes p2p before hf     

> __< gingeropolous >__ sure, but after that.     

> __< ofrnxmr >__ sgp_: Its based on download speeds of the blockchain     

> __< gingeropolous >__ testing these large blocks is gonna be a pita     

> __< ofrnxmr >__ actual sync speeds arent in the proposal, such as w/ or w/o checkpoints, or verification speeda     

> __< sgp_ >__ I'm just telling you where it comes from :)     

> __< rucknium >__ articmine:monero.social: fluffypony used to recruit developers AFAIK. To fix the 100MB packet limit you could do the same. Core has a general fund, too. Code changes would have to pass review, of course.     

> __< ofrnxmr >__ i'd prefer that p2p, serialization, and packet limits be fixed before adding a limit, but cest la vie     

> __< ofrnxmr >__ add torrenting to the node to split blocks into pieces /s not/s     

> __< gingeropolous >__ so at 1.5kb / tx, 90MB puts us at 44 million txs/day.      

> __< gingeropolous >__ how big are FCMP txs? wait there's an explorer somewhere     

> __< ofrnxmr >__ 6-7kb for a 1-2in     

> __< ofrnxmr >__ http://stressgguj7ugyxtqe7czeoelobeb3cnyhltooueuae2t3avd5ynepid.onion     

> __< sgp_ >__ I've been using 10 kB as an approximation     

> __< ofrnxmr >__ the block sizes are wrong, as they use an old weighting calc     

> __< gingeropolous >__ ok so only 6 million tx/day     

> __< sgp_ >__ the horror     

> __< gingeropolous >__ yeah if we're at 6 million tx/day in 5 years i'll eat my hat     

> __< gingeropolous >__ plus we getting that folding math up in here     

> __< hinto >__ "simply improving the schema" by implementing a DB from scratch 😭 > <kayabanerve:matrix.org> datahoarder:monero.social: boog900:monero.social: Saved 70 GB in Cuprate simply by improving the schema :)     

> __< sgp_ >__ that only gets us up to 8.4 billion transactions a year 10 years from now so it would mean monero is a failure per previous expectations     

> __< datahoarder >__ hinto: the best improvement is to throw the code away     

> __< datahoarder >__ "oops I needed it" then make it anew with learned knowledge     

> __< kayabanerve:matrix.org >__ hinto:monero.social: Improving LMDB's schema by complete replacement, yep, mhm     

> __< kayabanerve:matrix.org >__ I for one love our new rust db overlord     

> __< hinto >__ We'll still have a data.mdb as well     

> __< kayabanerve:matrix.org >__ (I know, I know)     

> __< hinto >__ boog900:monero.social: please make a rust LMDB while you're at it     

> __< boog900 >__ Don't tempt me, we could have fully atomic updates when adding a block then.      

> __< boog900 >__ I have thought about it lol     

> __< ack-j:matrix.org >__ Wait until you see the size of a post quantum fcmp++++ transaction > <boog900> I don't think our capacity will grow at 1.4x forever, I don't think we will hit gigabyte block capacity in 15 years.     

> __< articmine >__ 1 GB blocks are like 100 Mbps bandwidth.  Multi Gig Internet is available. The only reason why we can't support this is: > <boog900> I don't think our capacity will grow at 1.4x forever, I don't think we will hit gigabyte block capacity in 15 years.     

> __< articmine >__ Very serious code issues     

> __< articmine >__ The willingness to pay for hardware. The latter is closely related to price of Monero     

> __< articmine >__ They would very likely break BS even with no privacy at all     

> __< sech1 >__ Even my 5G mobile internet is 930 Mbit down/91 Mbit up. It's not 1995 anymore.     

> __< boog900 >__ Sech1 you think the network would be fine with gigabyte blocks assuming no stupid code issues?       

> __< articmine >__ I have 5Gbps symmetrical over fibre      

> __< sech1 >__ If there is enough bandwidth, yes. The problem can be software that is not optimized enough, but that is fixable.     

> __< sech1 >__ Cuprate is looking good already, stressnet also helps to fix monerod     

> __< boog900 >__ It will be interesting to see how high we can get cuprate, I doubt even we can process that many txs though      

> __< sgp_ >__ to be fair we are nerds who seek out good internet (selection bias). my dumb apartment provides only 40up/40down by default     

> __< boog900 >__ boog900: Assuming no p2p packet limits     

> __< articmine >__ sgp_: Nerds that believe in privacy are a major demographic for running Monero nodes     

> __< sgp_ >__ Optimizing for the median is good for decentralization if possible     

> __< articmine >__ This is the reason that I consider mid to high end Internet speeds appropriate for determining what a node can support      

> __< articmine >__ sgp_: I have tuned down houses over this kind of thing     

> __< sgp_ >__ Yeah I think many of us here have, ha     

> __< sech1 >__ sgp_ that's exactly why I mentioned mobile connection speed. Everyone has it in major cities now.     

> __< ravfx:xmr.mx >__ Not long ago I could only access to like 35/2     

> __< ravfx:xmr.mx >__ Now I have like 200/25     

> __< sgp_ >__ fwiw in the US at least, cell home internet providers deprioritize your service level after 1 TB or so of use a month     

> __< sgp_ >__ in any case I agree it's not 1995 anymore lol     



# Action History
- Created by: Rucknium | 2025-12-02T22:54:47+00:00
- Closed at: 2025-12-12T00:20:09+00:00
