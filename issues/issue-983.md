---
title: Monero Research Lab Meeting - Wed 27 March 2024, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/983
author: Rucknium
assignees: []
labels: []
created_at: '2024-03-26T22:25:02+00:00'
updated_at: '2024-04-03T19:38:45+00:00'
type: issue
status: closed
closed_at: '2024-04-03T19:38:45+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

[Join the Monero Matrix server if you don't already have a Matrix account.](https://web.archive.org/web/20230128130949/https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211027T170000&p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3. Update from CypherStack on [Bulletproofs++ Peer Review](https://ccs.getmonero.org/proposals/bulletproofs-pp-peer-review.html).

4. [Possible spam incident](https://bitinfocharts.com/comparison/monero-transactions.html#3m)

5. @jeffro256 [ I think we can improve how the nodes handle alternative blocks in a way that might naturally reduce the number of reorgs on the network.](https://github.com/monero-project/meta/issues/966#issuecomment-1936243293)

6. Any other business

7. Confirm next meeting agenda


Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#981 

# Discussion History
## Rucknium | 2024-03-27T22:52:12+00:00
> __< r​ucknium:monero.social >__ Meeting time! https://github.com/monero-project/meta/issues/983     

> __< r​ucknium:monero.social >__ 1) Greetings     

> __< a​aron:cypherstack.com >__ Hello!     

> __< rbrunner >__ Hello     

> __< s​yntheticbird:monero.social >__ Hi     

> __< jberman >__ hello!     

> __< r​ucknium:monero.social >__ 2) Updates. What is everyone working on?     

> __< plowsof >__ Hi     

> __< d​iego:cypherstack.com >__ Hi hi     

> __< r​ucknium:monero.social >__ me: More analysis of the suspected spam. I think I can push the new draft by the time we get to the spam agenda item 😅     

> __< a​rticmine:monero.social >__ Hi     

> __< s​yntheticbird:monero.social >__ Working on a monitoring software for monero nodes. I'll use it to build a dataset on which I want to train a neural network to identify network anomalies. This will be part of webpanel idea I had for a little while     

> __< jberman >__ me: finished reviewing @jeffro256 's PR to write txs to disk once instead of twice on sync (https://github.com/monero-project/monero/pull/9135), and wrapping up the Seraphis lib async scanner to speed up wallet scanning another ~20-40%     

> __< a​rticmine:monero.social >__ Working on fees and scaling. In particular to support FCMP and ring sizes of 40 or higher     

> __< a​rticmine:monero.social >__ Along the lines of what I mentioned before. Also taking a close look at minimum node relay fees     

> __< r​ucknium:monero.social >__ 3) Update from CypherStack on Bulletproofs++ Peer Review: https://ccs.getmonero.org/proposals/bulletproofs-pp-peer-review.html     

> __< d​iego:cypherstack.com >__ That's us!     

> __< d​iego:cypherstack.com >__ Progress continues. Things are going smoothly. We expect to complete this proposal by the end of the month.     

> __< plowsof >__ 0xFFFF has paused his current ccs for the foreseeable future (he is working on the lmdb read/write lock PR, so just wanted to share for visibility)     

> __< rbrunner >__ In a few days then? Splendid.     

> __< a​aron:cypherstack.com >__ We're nearly finished with the report, yes     

> __< a​aron:cypherstack.com >__ It will no doubt require some additional polish after that. I would be shocked if it were free of typos :D     

> __< rbrunner >__ Hoping for a positive outcome of course, i.e. that it will indeed make sense for Monero to switch to ++     

> __< r​ucknium:monero.social >__ Were you able to figure out if the security proofs were sound?     

> __< r​ucknium:monero.social >__ You can wait if you want, but I thought maybe you wanted to be on the agenda to give more details :)     

> __< a​aron:cypherstack.com >__ We still have doubts based on a significant lack of clarity and some of the "base" results     

> __< r​ucknium:monero.social >__ When the full report is released I may have to figure out if "doubts" is a diplomatic way to say that the soundness proofs are not clearly safe.     

> __< r​ucknium:monero.social >__ "Base" = lemmas in the paper?     

> __< a​aron:cypherstack.com >__ We haven't identified any particular exploits, if that's what you mean.     

> __< a​aron:cypherstack.com >__ Generally, the idea is that the proof should convince the reader about the correctness of its reasoning. I will certainly say that several of the proofs in the preprint did not do that for this reader.     

> __< r​ucknium:monero.social >__ That's not really what I mean, but a conjecture is still unproven even if no counterexamples have been found yet.     

> __< a​aron:cypherstack.com >__ For some we were able to determine the actual intent and make corrections, but for others we were not.     

> __< a​aron:cypherstack.com >__ Can you be more specific?     

> __< a​aron:cypherstack.com >__ I do want to be clear that "this proof does not appear to substantiate the claims to our satisfaction" is certainly not the same as "the protocol under question is definitively unsafe"     

> __< r​ucknium:monero.social >__ I think you answered my question with "Generally...". Thanks.     

> __< a​aron:cypherstack.com >__ I was particularly concerned with the lack of clarity around a key soundness proof     

> __< d​iego:cypherstack.com >__ There is a certain amount of diplomacy here, yes. :P     

> __< a​aron:cypherstack.com >__ The idea is that the proof needs to build an algorithm called an extractor that has to do very specific things     

> __< a​aron:cypherstack.com >__ In this case, the proof is extremely informal about this, without detail that convinces me of its construction     

> __< a​aron:cypherstack.com >__ You will also find the word "presumably" in many places in the report, where we had to make assumptions about intent     

> __< a​aron:cypherstack.com >__ I'm certainly not trying to be wishy-washy here. Just professional and accurate.     

> __< rbrunner >__ This all also seems to confirm something you mentioned last time, that things are considerably more complex compared to "+". IMHO, that doesn't help either     

> __< a​aron:cypherstack.com >__ Yeah, the second "+" in the name carries a _lot_ of weight     

> __< rbrunner >__ We will already have a quite a serious step up in complexity with Seraphis and Jamtis.     

> __< a​rticmine:monero.social >__ What are the advantages of ++ in terms of size and verification time?     

> __< a​aron:cypherstack.com >__ The authors claim single-proof verification time with BP++ (over secp256k1) at 0.840 ms     

> __< a​aron:cypherstack.com >__ whereas for BP over secp256k1 they saw 2.223 ms     

> __< a​aron:cypherstack.com >__ (There are other numbers for other implementations, but those are really hard to compare fairly)     

> __< a​aron:cypherstack.com >__ They also get single proofs at 416 bytes, compared to BP+ at 576 bytes or so     

> __< a​aron:cypherstack.com >__ I do have one question that wasn't directly addressed. Typically such a review will issue findings and corrections as appropriate, which is what our report does. But it's obviously not a pass/fail sort of thing (though I have seen this before...)     

> __< a​aron:cypherstack.com >__ Is the community looking for something more cut and dry as a top-level sort of thing?     

> __< r​ucknium:monero.social >__ IMHO, cryptographers on the MRL end should give their interpretation of the final report instead of you needing to summarize it like that. I think I caused some confusion by saying "unsafe". I meant that something that is not definitely proven is not safe enough for Monero mainnet, even if it is not definitely proven wrong in the mathematics meaning.     

> __< r​ucknium:monero.social >__ In other words I don't think you need to put FAIL in bold red letters at the top. Or PASS in bold green as needed.     

> __< a​aron:cypherstack.com >__ Rucknium: I would agree that Monero-specific interpretation should certainly be left up to community researchers     

> __< a​aron:cypherstack.com >__ And no, there will not be a big red or green stamp at the top =p     

> __< a​rticmine:monero.social >__ This can be a tough question. In my view we are looking at an incremental improvement vs what I see as serious concerns regarding the proofs themselves.     

> __< a​aron:cypherstack.com >__ (I saw one audit that did issue a pass/fail, and was immediately suspicious...)     

> __< a​aron:cypherstack.com >__ And anyone who has gone through journal- or conference-style review surely knows that three different reviewers may have three wildly different conclusions     

> __< jberman >__ "I will certainly say that several of the proofs in the preprint did not [convince the reader about the correctness of its reasoning] for this reader" -> I think this is a reasonable conclusion and a report that backs up that conclusion in its contents would be satisfactory, rather than a PASS/FAIL     

> __< a​rticmine:monero.social >__ I agree this is not a pass / fail question, but the benefit of doubt has to be with the reader and auditor not the prover.      

> __< a​rticmine:monero.social >__ In the case of doubt or concerns it becomes a fail     

> __< a​rticmine:monero.social >__ For inclusion into the Monero code     

> __< a​aron:cypherstack.com >__ We do certainly hope that the authors can find value in the report too, to make corrections and improvements as they see fit     

> __< r​euben:firo.org >__ What about BP+ verification vs BP?     

> __< r​ucknium:monero.social >__ I agree. The stakes are very high. Any real doubts would mean not adopting it into Monero mainnet IMHO.     

> __< a​aron:cypherstack.com >__ Reuben: they include numbers for that, but it's with different implementations over different curves. Not comparable IMO     

> __< r​euben:firo.org >__ 🥲     

> __< a​aron:cypherstack.com >__ In terms of raw numbers, I can say that at least one BP+ implementation (in Rust over Ristretto) is likely comparable to their BP++ implementation. But I haven't tested their benchmark on the same machine     

> __< a​aron:cypherstack.com >__ Unless you're using the same curve library and fair optimizations between implementations, it's a crapshoot to make claims about raw numbers     

> __< jberman >__ +1 based on that conclusion, it would seem ideal next step would be to share the final report with the authors and see if able to fill in the gaps / beef up the proofs     

> __< a​aron:cypherstack.com >__ Oh Reuben maybe I misread... you weren't asking about BP++ at all?     

> __< a​rticmine:monero.social >__ Yes. I agree.     

> __< a​aron:cypherstack.com >__ @jberman: How would the community like that handled?     

> __< d​iego:cypherstack.com >__ It's always been the plan to release the report publicly and let the original authors know about the report. But we don't want to send and wait for their response before delivery. We also don't care to dictate how the whole process is handled.     

> __< r​euben:firo.org >__ Was just thinking if BP++ isn't a significant improvement over BP+ then I mean with the risks of BP++ doesn't seem to justify pushing too hard into it     

> __< a​aron:cypherstack.com >__ Oh OK, you were asking about BP++ vs. BP+. Got it     

> __< a​aron:cypherstack.com >__ (too many BPs floating around...)     

> __< r​euben:firo.org >__ FCMP currently uses BP only yes ?     

> __< r​ucknium:monero.social >__ "It's always been the plan to release the report publicly and let the original authors know about the report." This sounds fine to me. There is no need to wait for a response from the original authors. You've already contacted them about a few things anyway IIRC.     

> __< r​euben:firo.org >__ Forgot if we found a solution     

> __< a​aron:cypherstack.com >__ Yes. To my knowledge, no one has used BP+ or BP++ arithmetic circuit modifications for that     

> __< jberman >__ original plan laid out by @diego makes sense. I think we can assess next steps after that point     

> __< a​aron:cypherstack.com >__ Rucknium: We contacted them about a couple of initial findings, but nothing beyond that. We hadn't heard back from our latest question     

> __< rbrunner >__ I see things similarly to jberman     

> __< a​aron:cypherstack.com >__ As a courtesy, we would certainly like to inform them directly to let them know about the report and where to read it     

> __< a​rticmine:monero.social >__ In my opinion this comes down to the allocation of resources. For example are we better off coding parallel processing and graphics processing with the existing proofs to get the verification time advantage?      

> __< a​rticmine:monero.social >__ I know I am thinking as an engineer and not a mathematician.     

> __< a​aron:cypherstack.com >__ Development is likely to be quite complex compared to BP or BP+     

> __< a​aron:cypherstack.com >__ For BP and BP+, range proofs work differently than the more general arithmetic circuit proofs they also support     

> __< a​aron:cypherstack.com >__ For BP++, you basically need the full arithmetic circuit proving system implemented     

> __< r​ucknium:monero.social >__ IMHO the recent suspected spam has exposed a lot of cracks in the network that better engineering could patch. And some cracks that need better math or something.     

> __< a​aron:cypherstack.com >__ And that doesn't account for optimizations needed to presumably get the numbers they saw     

> __< a​aron:cypherstack.com >__ To be fair, they do have a reference implementation in C over secp256k1     

> __< a​aron:cypherstack.com >__ Regardless of the report findings, I think it's safe to say that a complete from-scratch implementation would pose nontrivial engineering risk in itself     

> __< rbrunner >__ Yeah, we definitely won't run out of important work soon, so with these shadows of doubts over BP++ ...     

> __< a​aron:cypherstack.com >__ I'm certainly not trying to influence any decisions here. Just wanted to provide my best assessment     

> __< a​rticmine:monero.social >__ For a marginal benefit     

> __< a​aron:cypherstack.com >__ Other reviewers may have different conclusions     

> __< a​aron:cypherstack.com >__ ArticMine: the proof size difference is impressive     

> __< a​aron:cypherstack.com >__ From a verification perspective, tough call. Batch verification is already pretty snappy, and it's not clear at what point the returns from that become diminished compared to the rest of transaction/network operations     

> __< a​aron:cypherstack.com >__ Anyway, it sounds like the final report should be publicly delivered to the community? And then we can inform the authors directly as a professional courtesy?     

> __< d​iego:cypherstack.com >__ Cool. Can we move on to the next thing for Cypher Stack?     

> __< r​ucknium:monero.social >__ Aaron Feickert: Thank you! Tremendous work. Extremely useful.     

> __< jberman >__ Yep, that sounds great to me     

> __< rbrunner >__ +1     

> __< a​aron:cypherstack.com >__ Thanks! Sorry to take up so much meeting time on it     

> __< r​ucknium:monero.social >__ Diego Salazar: Yes, you can move to the next CypherStack item.     

> __< d​iego:cypherstack.com >__ Thanks.     

> __< d​iego:cypherstack.com >__ Given that we're almost done with this proposal, I'd like to discuss the possibility of the next one.     

> __< a​aron:cypherstack.com >__ BP#     

> __< d​iego:cypherstack.com >__ We've been asked by a few MRL individuals what it would mean to do a Seraphis review.     

> __< d​iego:cypherstack.com >__ Before we give a quote and time estimate, I'd like to discuss with you all hear what exactly you'd want out of such a review.     

> __< d​iego:cypherstack.com >__ Are we looking to formalize Seraphis? A holistic review?     

> __< rbrunner >__ Uh, I think the word "exactly" here will prove to be tough :)     

> __< r​ucknium:monero.social >__ Can jberman give the current status of the Seraphis paper?     

> __< r​ucknium:monero.social >__ The critical cryptography is Seraphis needs to be proven. I don't know what the journey there looks like.     

> __< r​ucknium:monero.social >__ The last thing I heard about the paper is that it is missing a few proofs at least. The entity that writes the proofs cannot be the one who peer reviews the proofs IMHO.     

> __< a​aron:cypherstack.com >__ It had previously been my recommendation that a holistic review is more likely to provide practical benefit and return than a more exploratory formalization     

> __< r​ucknium:monero.social >__ So holistic review means basically figuring out where it needs work and maybe a plan to get it to finalization?     

> __< r​ucknium:monero.social >__ If the cryptographers in MRL want Seraphis to move forward, they need to move it forward. I'm not the best person to move it forward.     

> __< a​aron:cypherstack.com >__ It would mean considering its security properties more informally, but from a more practical perspective than a strict security model and formalization     

> __< r​ucknium:monero.social >__ ^ This is not aimed at CypherStack, but at other MRL people     

> __< a​aron:cypherstack.com >__ Seeing as developing a security model after the fact (or trying to use an existing one) may not prove fruitful, and still may not capture all practical risks and threats     

> __< rbrunner >__ Could it be said that with a "holistic review" you will "read and think the whole thing through, to find any possible problems"?     

> __< r​ucknium:monero.social >__ Are you familiar with the paper that formalized Monero's current security model?     

> __< a​aron:cypherstack.com >__ One reason for my recommendation is also that the worst-case scenario for a formalization engagement is "we were not able to develop a security model that is amenable to the design", whereas the worst-case scenario for a holistic review is "here are findings and recommendations"     

> __< a​aron:cypherstack.com >__ I recall seeing it, but at the time hadn't reviewed it in detail     

> __< a​aron:cypherstack.com >__ Trying to hunt it down...     

> __< r​ucknium:monero.social >__ https://eprint.iacr.org/2023/321 "A Holistic Security Analysis of Monero Transactions" . It even has "holistic" in the name :P     

> __< a​aron:cypherstack.com >__ Cypher Stack has been engaged in the past to do non-security-model protocol reviews. And we've certainly provided findings.     

> __< r​ucknium:monero.social >__ AFAIK it will appear in EUROCRYPT 2024     

> __< a​aron:cypherstack.com >__ Rucknium: that's it, thanks     

> __< a​aron:cypherstack.com >__ Rucknium: keep in mind that AFAIK, reviewers are not required to even read security proofs for that conference     

> __< v​tnerd:monero.social >__ I forgot about the meeting, sorry. Still working on LWS remote account scanning     

> __< r​ucknium:monero.social >__ And this paper is huge anyway     

> __< r​ucknium:monero.social >__ 87 pages     

> __< a​aron:cypherstack.com >__ There are some aspects of its security definitions that would need modification for Seraphis     

> __< a​aron:cypherstack.com >__ and are fairly specific to Monero's RingCT     

> __< r​ucknium:monero.social >__ rbrunner: IMHO you or someone you are working with needs to guide the way on Seraphis formalization. I will not push it forward since it is out of my area.     

> __< jberman >__ @rucknium the Seraphis paper sketches a rough informal security model in section 1.2 that's light on details and the Seraphis tx protocol does not have formal security proofs     

> __< r​ucknium:monero.social >__ Thanks, jberman     

> __< jberman >__ A holistic review with an eye toward laying groundwork for a formalization of the protocol I think seems a solid route based on @aaron 's recommendations     

> __< rbrunner >__ I am pretty innocent regarding all things crypto, I wouldn't put much hope that I can really advance something here, even if I wanted     

> __< r​ucknium:monero.social >__ I suggested you since you are semi-official Seraphis project manager.     

> __< r​euben:firo.org >__ If a way is not found to formalize security, what then? Afaik some aspects of seraphis are hard to prove     

> __< rbrunner >__ I see. Yeah, for dev work, mostly, at least so far     

> __< r​ucknium:monero.social >__ If the Seraphis programmers want Seraphis on mainnet, they must get the math arranged.     

> __< a​aron:cypherstack.com >__ One example of where formalization often comes up short is something like the mempool... this bit an initial iteration of the Spark design, whose security model didn't capture it. I _think_ this linked preprint similarly wouldn't capture it (but am not 100% sure on this)     

> __< a​aron:cypherstack.com >__ @jberman: Right, an initial holistic review could certainly be done with an eye for future formalization     

> __< r​ucknium:monero.social >__ Probably mempool is out of scope IMHO.     

> __< a​aron:cypherstack.com >__ Rucknium: ah, I'd disagree. That's how you get things like certain types of burning attacks     

> __< d​iego:cypherstack.com >__ Alright, would you like us to draft up a proposal for a holistic review? All things considered, it seems the logical first step on this Seraphis journey.     

> __< a​aron:cypherstack.com >__ and is why protocols like Seraphis and Spark need to account for different structural components in transactions     

> __< r​ucknium:monero.social >__ Aaron Feickert: Thanks. I didn't think of that.     

> __< rbrunner >__ I think a first rough estimate how such a "holistic review" might cost would help to decide.     

> __< a​aron:cypherstack.com >__ Anyway, I would have a few questions regarding scope. Namely the following     

> __< s​yntheticbird:monero.social >__ Lacking knowledge but since each methods have requirements for seraphis to be mainnet. Having a holostic and formal review seems like a necessity     

> __< a​aron:cypherstack.com >__ 1. There are two papers on Seraphis: a general structure one, and an implementation-focused one that instantiates the protocol. Which should be in scope?     

> __< a​aron:cypherstack.com >__ 2. I know JAMTIS has been under design for a while, and it's included in Chapter 8 of the implementation paper. Is it in scope?     

> __< a​aron:cypherstack.com >__ 3. There are "information proofs" useful for proving various things about addresses and such to a third party, and they're in Appendix A of the implementation paper. Are they in scope?     

> __< a​aron:cypherstack.com >__ (these are not security proofs)     

> __< a​aron:cypherstack.com >__ 4. Are there other specific or general scope items we should consider?     

> __< jberman >__ The general structure paper is the paper in scope (the implementation-focused one is there as a helpful resource)     

> __< jberman >__ that should answer all 4 q's :)     

> __< a​aron:cypherstack.com >__ @jberman: Am I understanding right? "Implementing Seraphis" is _not_ in scope?     

> __< a​aron:cypherstack.com >__ If anything, I would have thought the opposite for a holistic review     

> __< d​iego:cypherstack.com >__ Perhaps one followed by the other?     

> __< jberman >__ hmm, a holistic review of the first paper I don't think should take too long in that case     

> __< a​aron:cypherstack.com >__ True     

> __< a​aron:cypherstack.com >__ Findings from it could be relevant to the implementation (if in fact the implementation is a proper instantiation of the general design)     

> __< a​aron:cypherstack.com >__ But it obviously wouldn't capture anything specific to the instantiation, like JAMTIS or other particular components     

> __< d​iego:cypherstack.com >__ I think doing things in a stepwise fashion gives the community the most bang for its buck     

> __< a​aron:cypherstack.com >__ That's fair. But any reason not to jump right to the implementation paper?     

> __< a​aron:cypherstack.com >__ It's much closer to what would actually go into a deployed implementation     

> __< d​iego:cypherstack.com >__ The odds are very small, but if something is found in the general paper that makes the community rethink Seraphis entirely, it's helpful that they haven't already raised the funds for the instantiation paper     

> __< a​aron:cypherstack.com >__ @Diego that's fair     

> __< r​euben:firo.org >__ Isn't it incomplete just for the general design? Since there are various ways to instantiate seraphis with different security implications no ?     

> __< r​euben:firo.org >__ Also assuming this doesn't include FCMPs either ?     

> __< a​aron:cypherstack.com >__ @Reuben: Yeah, any specific instantiation would have security and design aspects specific to it     

> __< a​aron:cypherstack.com >__ JAMTIS is probably the biggest example     

> __< r​euben:firo.org >__ Would it also affect security proofs ? Different instantiations have different proofs too no ?     

> __< a​aron:cypherstack.com >__ The best way to look at it would be that different components (_e.g._ a range proof, a membership proof) need particular security properties proven for any particular choice     

> __< a​aron:cypherstack.com >__ But ideally you build the overall security model such that things are as plug-and-play as possible     

> __< a​aron:cypherstack.com >__ So you get something like "assume a range proving system with security properties X, Y, Z"     

> __< jberman >__ I figure a review of the first paper could clarify areas in which it needs strengthening, and would be specifically helpful in laying a cleaner path toward formalization and structuring a security model     

> __< a​aron:cypherstack.com >__ You still need to pick a range proving system and prove those properties     

> __< a​aron:cypherstack.com >__ @jberman: Although I do wonder how many findings could be addressed simply by "read the implementation paper" =p     

> __< d​iego:cypherstack.com >__ Alright then. Aaron Feickert we'll first make a proposal for the first paper.     

> __< a​aron:cypherstack.com >__ Anyway, we can certainly do an initial review of just the general design paper     

> __< d​iego:cypherstack.com >__ And then explore further options once that's complete.     

> __< a​aron:cypherstack.com >__ It does provide a quicker stopping point in the event of major findings     

> __< a​aron:cypherstack.com >__ But the paper is significantly general that, TBH, I would be surprised (as @Diego notes) if this were the case     

> __< a​aron:cypherstack.com >__ and it's far more likely that relevant findings would exist for the implementation paper, where the nuts and bolts live     

> __< a​aron:cypherstack.com >__ Just want to make sure that expectations are set appropriately, given the structure of the papers     

> __< d​iego:cypherstack.com >__ Alright. Then I think that we here at Cypher Stack have our marching orders.     

> __< jberman >__ I figure the first paper would be the first thing to review before reviewing the implementation paper anyway     

> __< a​aron:cypherstack.com >__ I think the best way to look at it would be the following     

> __< a​aron:cypherstack.com >__ A "positive review" of the first paper could basically say "there exist Seraphis instantiations that are likely secure"     

> __< a​aron:cypherstack.com >__ Whereas a "negative review" could basically say "no Seraphis instantiation meets this informal security goal"     

> __< a​aron:cypherstack.com >__ Any more specific conclusions would depend on the implementation paper, which could certainly be a follow-up engagement that I'd be excited to do :D     

> __< a​aron:cypherstack.com >__ So I'll get information to @Diego for a proposal ASAP     

> __< d​iego:cypherstack.com >__ Great! Nothing else for us then?     

> __< r​ucknium:monero.social >__ Thank you, Diego Salazar  and Aaron Feickert . Please put suggested milestones in the proposal if you want them.     

> __< a​aron:cypherstack.com >__ Thanks everyone     

> __*__ m-relay <a​aron:cypherstack.com> hops out of the meeting     

> __< jberman >__ sounding reasonable to me     

> __< a​rticmine:monero.social >__ Thanks everyone     

> __< r​ucknium:monero.social >__ We are past the hour. The suspected spam is still a topic: https://bitinfocharts.com/comparison/monero-transactions.html#3m     

> __< r​ucknium:monero.social >__ I will just post a few more plots. The spam looks like it stopped recently. May be temporary. So, mean effective ring size is rising: https://github.com/Rucknium/misc-research/blob/main/Monero-Black-Marble-Flood/pdf/images/empirical-effective-ring-size.png     

> __< r​ucknium:monero.social >__ I compared current suspected spam with the Chervinski et al. (2021) simulations: https://github.com/Rucknium/misc-research/blob/main/Monero-Black-Marble-Flood/pdf/images/effective-ring-size-binomial-pmf.png     

> __< r​ucknium:monero.social >__ There are more favorable parameters now (higher ring size and lower spam share of outputs), so less than 1% of rings have an effective ring size of 1. The Chervinski simulation had the share of rings with effective ring size one at 12%.     

> __< r​ucknium:monero.social >__ Chervinski also did a chain reaction analysis, which increased the effectiveness of the attack a little: https://github.com/Rucknium/misc-research/blob/main/Monero-Black-Marble-Flood/pdf/images/chervinski-chain-reaction.png     

> __< r​ucknium:monero.social >__ Mean delay to first confirmation from the mempool archive data: https://github.com/Rucknium/misc-research/blob/main/Monero-Black-Marble-Flood/pdf/images/mean-delay-first-confirmation.png     

> __< r​ucknium:monero.social >__ Mostly below 15 minutes except for two periods that increased to 2+ hours     

> __< r​ucknium:monero.social >__ Input/Output tx types that show 1in/2out increased on March 4, but other types did not: https://github.com/Rucknium/misc-research/blob/main/Monero-Black-Marble-Flood/pdf/images/in-out-tx-type-volume.png     

> __< r​ucknium:monero.social >__ Fee tiers. More non-spam txs paid the 2nd fee tier after the spam started: https://github.com/Rucknium/misc-research/blob/main/Monero-Black-Marble-Flood/pdf/images/share-tx-in-fee-tier-spam-removed.png     

> __< a​rticmine:monero.social >__ ... but the spam stayed at the low fee tier?     

> __< r​ucknium:monero.social >__ Two ways to look at the data. Maybe all spam was at 20 nanoneros/byte. But there was a burst of 320 nanoneros/byte (3rd tier) on March 12-13 that may have been the spammer switching tiers: https://github.com/Rucknium/misc-research/blob/main/Monero-Black-Marble-Flood/pdf/images/share-tx-in-fee-tier-all-txs.png     

> __< r​ucknium:monero.social >__ There was also a burst of 320 nanonero/byte 1in/2out in the last day or two before the spammed appeared to stop.     

> __< a​rticmine:monero.social >__ This is very helpful     

> __< r​ucknium:monero.social >__ We don't know the budget of the suspected spammer. Maybe they can go to 320 nanoneros/byte. That level would stop txs from the GUI/CLI using the auto fee level from confirming since auto only move from the 1st tier (20) to the 2nd (80).     

> __< a​rticmine:monero.social >__ I am also trying to understand the psychology of both the ham and the soam     

> __< r​ucknium:monero.social >__ I have two sets of analysis. One assuming only 80 nanoneros/byte 1in/2out are spam. The other assuming both 20 and 320 nanoneros/byte 1in/2out are spam.     

> __< a​rticmine:monero.social >__ If as I suspect the spammer is testing the waters then moving the ham to tier 2 would force the spam to tier 3     

> __< r​ucknium:monero.social >__ The 320 nanoneros/byte could be a central service that tried to get its txs confirmed quickly, too.     

> __< a​rticmine:monero.social >__ ... but primarily 1/2?     

> __< r​ucknium:monero.social >__ But I doubt that some large number of ordinary users in unison decided to switch to 320 for a day or two and then switch back.     

> __< a​rticmine:monero.social >__ I agree given the past behavior of the ham     

> __< r​ucknium:monero.social >__ Yes. When I use the broad definition of spam, I still use the 1in/2out definition. Just increase the criteria to include the 320 fee level, too. Actually, it is the level of txs that we observe minus the pre-spam "normal" volume of 1in/2out 320/byte txs.     

> __< r​ucknium:monero.social >__ Figuring out if 320 is spam is important to anticipate if increasing the fee may have a large effect on the spam. We don't know much about the suspected spammer.     

> __< a​rticmine:monero.social >__ I suspect a BS company  testing the waters., as a possible if not likely candidate     

> __< r​ucknium:monero.social >__ And even if this spammer would respond to a fee increase, maybe the next one would have a lower response.     

> __< a​rticmine:monero.social >__ My take is that a ring size increase combined with a fee increase could deter this. The ultimate deterrent is FCMP.      

> __< a​rticmine:monero.social >__ This brings me to my next question. Do we have a good estimate of a 2/2 tx under FCMP?     

> __< a​rticmine:monero.social >__ At least a ballpark. Say between 5000 and 6000 bytes?     

> __< r​ucknium:monero.social >__ The last I heard was probably the same as you. 5.5kB for 2/2, estimated by kayabanerve  in June 2023: https://github.com/monero-project/research-lab/issues/100#issuecomment-1609536076     

> __< UkoeHB >__ aaron thanks for your work and clarity on the way forward with the Seraphis papers. I honestly have no input beyond 'here are the papers I wrote as best I could'.     

> __< a​rticmine:monero.social >__ Thanks. I have to read this thread carefully, but from what I see a 400000 minimum penalty free zone combined with a 8000 byte reference transaction size will do the trick.      

> __< a​rticmine:monero.social >__ This will mean a 4x increase in fees for a 2% minimum growth rate for the short term median. With a dynamic suggested surge this means a 16x increase in fees      

> __< a​rticmine:monero.social >__ It would also support ring 40 with the current proofs and tighten the number of transactions in the minimum penalty free zone.      

> __< a​rticmine:monero.social >__ As for quadratic fee scaling this can be replaced with a one time additional fee level of 1/4 the minimum fee once the sanity median reaches a predetermined level 1600000 bytes or higher     

> __< r​ucknium:monero.social >__ I'm not familiar enough with the block size scaling model to comment on the dynamic rules. Ring size 40 seems to provide a good safety margin. A modest fee increase seems OK.     

> __< r​ucknium:monero.social >__ The Chervinski et al. (2021) simulation had high attack effectiveness because 1) Ring size was lower (obviously), but just as important (2) The spam assumptions they had only allowed the spam to grow to the 300kB block size. Because the non-spam txs filled less of the 300kB block than now in March 2024, Chervinski filled the rest of the block with a higher share of black marbles than we have now     

> __< r​ucknium:monero.social >__ Of course the spammer can push up the block size gradually. That hasn't happened yet, above 400kB at least.     

> __< r​ucknium:monero.social >__ IMHO more research is needed on fee prediction. The dynamic scaling requires full blocks, which usually requires mempool congestion. As much as possible, users should be able to avoid long waits if they are willing to pay for that convenience.     

> __< r​ucknium:monero.social >__ This goes for congestion due to spam and "real" usage growth.     

> __< r​ucknium:monero.social >__ And users cannot change their bid for block space. There is no replace-by-fee nor child-pays-for-parent in Monero. So users just have to wait in the queue if they don't know that the mempool is congested and they choose a low fee.     

> __< d​ave.jp:matrix.org >__ Rucknium: how many txs/day would attacker need to lower the effective ringsize to 5-6 if we increase ringsize to 40 and honest txs is average 10k ?     

> __< d​ave.jp:matrix.org >__ And how much they are expected to pay in case we bump fees 5x or 10x     

> __< d​ave.jp:matrix.org >__ And how much they are expected to pay in fees, in case we bump fees 5x or 10x     

> __< r​ucknium:monero.social >__ dave.jp: This says that blocks would have to be 1-1.25MB to lower effective ring size to 5-6 when nominal ring size is 40, assuming current "real" transaction volume: https://github.com/Rucknium/misc-research/blob/main/Monero-Black-Marble-Flood/pdf/images/projected-effective-ring-size-log-log.png     

> __< a​rticmine:monero.social >__ They currently can but the evidence is that psychologically they don't. At least initially.     

> __< a​rticmine:monero.social >__ Dynamically changing the suggested fee based upon the transaction pool size together with increasing the initial default growth rate will mitigate this     

> __< r​ucknium:monero.social >__ Let me see if I can quickly get the exact number of spam txs per block     

> __< a​rticmine:monero.social >__ Also my proposal of increasing the default growth rate from 1% to 2% will roughly reduce the number of transactions in the minimum penalty free zone to 1/2     

> __< r​ucknium:monero.social >__ What I see is that to get effective ring size to 5.5 when nominal ring size is 40, there will be 403 black marbles in each block (88.4% of all outputs in a block). About 290,000 spam txs per day. That's with the 4 week pre-spam txs considered as a "normal" level of real user txs     

> __< a​rticmine:monero.social >__ So combining this with halving the penalty free zone interns it the number of transactions this puts our spammer deep into the penalty     

> __< a​rticmine:monero.social >__ In terms of transactions     

> __< r​ucknium:monero.social >__ `(total_block_kb - real_tx_kn) * kb_to_byte * lowest_fee_tier_in_nanoneros * convert_nanoneros_to_XMR * blocks_per_hour * hours_in_day * higher_fee_factor`     

> __< r​ucknium:monero.social >__ `(1205.595 - 208) * 1000 * 20 * 0.000000001 * 30 * 24 * 10 = 143.7 XMR/day` to send spam at that level     

> __< a​rticmine:monero.social >__ What was it costing the spammer now     

> __< a​rticmine:monero.social >__ Per day     

> __< r​ucknium:monero.social >__ 2.68 XMR/day, assuming the spam is the 1/2 20 nanonero/byte.     

> __< r​ucknium:monero.social >__ 3.53 XMR/day, assuming the spam is the 1/2 20 _and_ 320 nanonero/byte.     

> __< r​ucknium:monero.social >__ But the 320 nanonero/byte suspected spam was low and only happened a couple of days.     

> __< a​rticmine:monero.social >__ I believe your figure of 143 XMR per day is in the ballpark. The issue is surge vs maintenance in the penalty zone     

> __< a​rticmine:monero.social >__ The spammer can maintain for less but if the spam stops for 100 blocks then the spammer has to surge the short term median again. There is where the cost is     

> __< d​ave.jp:matrix.org >__ How much less if they limit it ?     

> __< a​rticmine:monero.social >__ To what?     

> __< d​ave.jp:matrix.org >__ Sorry I misunderstood, so ~140xmr if they continue the spam and would cost more if they stop for 100blocks     

> __< d​ave.jp:matrix.org >__ This looks good on paper, any idea when we go ahead with this fork ? do we wait for 6month or can expedite it.     

> __< a​rticmine:monero.social >__ It is more like 80 XMR for maintenance but each drop would cost the spammer up 480 XMR     

> __< a​rticmine:monero.social >__ The latter is the hard part for a spammer     

> __< a​rticmine:monero.social >__ This is why these kinds of spammers tend to shy away from the penalty     

> __< a​rticmine:monero.social >__ Well I have to develop the algorithms. Then it has to be coded. We have to get consensus, give notice etc     

> __< a​rticmine:monero.social >__ I will do my best to get this started     

> __< d​ave.jp:matrix.org >__ Thanks articmine, looking forward to it.     

> __< b​lurt4949:matrix.org >__ Late to the party, but it's maybe worth mentioning that 2/2 FCMP transactions could be <4kb with proof aggregation, if I'm interpreting kayabanerve correctly. AFAICT it's similar to BP(+) aggregation, just on the input side rather than the output side. I haven't really heard of this before though. https://github.com/monero-project/research-lab/issues/100#issuecomment-1609586250     

> __< d​ave.jp:matrix.org >__ Rucknium: anything to change in decoy selection to get better effective ring size even if they spam and fill recent outputs ?     

> __< r​ucknium:monero.social >__ IMHO automatic spam detection is too difficult. An adversary can see the rules for spam detection in the wallet source code and just form the spam to fall outside of the rules.     

> __< a​lex:agoradesk.com >__ ArticMine: assuming that the black marble attack can be combatted without a hard fork prior to FCMP, would you still support the ring bump hard fork?     

> __< r​ucknium:monero.social >__ New version of my black marble flooding analysis: https://github.com/Rucknium/misc-research/blob/main/Monero-Black-Marble-Flood/pdf/monero-black-marble-flood.pdf     

> __< r​ucknium:monero.social >__ I added sections "Chain reaction graph attacks", "Transaction confirmation delay", "Real user fee behavior", and "Evidence for and against the spam hypothesis"     

> __< a​rticmine:monero.social >__ Yes.      

> __< a​rticmine:monero.social >__ This is the second time this kind of attack has occurred recently and yes the first one fizzled out  this one may also fizzle out.      

> __< a​rticmine:monero.social >__ This type of attack looks attractive and when the spammer figures out the real cost tends to stop. Still it makes sense to harden Monero against this kind of thing. Furthermore once this HF is in place scaling and fees would support FCMP. There is also a good case to make the scaling change now when the transaction rates are low. For example transaction rates could increase sharpl<clipped messag     

> __< a​rticmine:monero.social >__ y before FCMP making the scaling change much harder on the network then.     

> __< a​lex:agoradesk.com >__ Fair.   

# Action History
- Created by: Rucknium | 2024-03-26T22:25:02+00:00
- Closed at: 2024-04-03T19:38:45+00:00
