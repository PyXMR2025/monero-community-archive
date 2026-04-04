---
title: Monero Research Lab Meeting - Wed 22 May 2024, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1012
author: Rucknium
assignees: []
labels: []
created_at: '2024-05-21T21:55:47+00:00'
updated_at: '2024-06-03T21:53:29+00:00'
type: issue
status: closed
closed_at: '2024-06-03T21:53:29+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

[Join the Monero Matrix server if you don't already have a Matrix account.](https://web.archive.org/web/20230128130949/https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211027T170000&p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3. [Potential measures against a black marble attack](https://github.com/monero-project/research-lab/issues/119).

4. Research [Pre-Seraphis Full-Chain Membership Proofs](https://www.getmonero.org/2024/04/27/fcmps.html). [Eagen Review Quotes](https://gist.github.com/kayabaNerve/7b3572e633ace8aca6e4b27e09acd9d0).

5. Any other business

6. Confirm next meeting agenda


Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#1007 

# Discussion History
## Rucknium | 2024-05-22T21:07:52+00:00
Log:

> __< r​ucknium:monero.social >__ Meeting time!     

> __< r​ucknium:monero.social >__ https://github.com/monero-project/meta/issues/1012     

> __< r​ucknium:monero.social >__ 1) Greetings     

> __< v​tnerd:monero.social >__ Hi     

> __< rbrunner >__ Hello     

> __< s​gp_:monero.social >__ hello     

> __< c​haser:monero.social >__ hello     

> __< jberman >__ *waves*     

> __< h​into:monero.social >__ hi     

> __< j​effro256:monero.social >__ howdy     

> __< k​ayabanerve:matrix.org >__ 👋     

> __< r​ucknium:monero.social >__ 2) Updates. What is everyone working on?     

> __< r​ucknium:monero.social >__ me: Monitoring the high 1in/16out transaction volume. Finishing the draft of the cost-effectiveness analysis of different ring size and fee options to defend against black marble flooding.     

> __< j​effro256:monero.social >__ me: I believe I found a way for a DLP solver to find view-balance key in Jamtis on Seraphis if they know the address index extensions for a public address and a linking tag spending an enote to that address https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d17024?permalink_comment_id=5064990#gistcomment-5064990     

> __< jberman >__ me: implemented growing an existing tree for fcmp's, currently making it cleaner, then implementing in the DB, then implementing `trim`     

> __< k​ayabanerve:monero.social >__ Just audit management, and I noticed an improvement to the composition after submitted for review which is... blarg. ~5% penalty, can try to pick up late.     

> __< k​ayabanerve:monero.social >__ *later     

> __< v​tnerd:monero.social >__ Me: still working on LWS remote scanning :/ taking longer than expected but I am making good progress     

> __< r​ucknium:monero.social >__ 3) Potential measures against a black marble attack. https://github.com/monero-project/research-lab/issues/119     

> __< r​ucknium:monero.social >__ I made a table. The volume of 1in/16outs is still high: https://gist.github.com/Rucknium/567fc52380acaf2991a2f1ad91a95b9e     

> __< r​ucknium:monero.social >__ Transactions with 1 input and 8-16 outputs are producing about 45% of all outputs now. Seems suspicious.     

> __< c​haser:monero.social >__ perhaps our previous spammer is trying to sneak under the radar.     

> __< r​ucknium:monero.social >__ I will give a preview of what my cost-effectiveness analysis is showing.     

> __< r​ucknium:monero.social >__ Current ring size is 16. Current minimum fee/byte is 20 nanoneros/byte. The set of possible ring sizes that were considered were 11 to 60. The set of possible min fees that were considered was 20 to 400 nanonero/byte. Remember that cost-effectiveness is measured by summing the cost to users in tx fee and the cost to all node operators by storage costs, then dividing that sum by th<clipped message     

> __< r​ucknium:monero.social >__ e effective ring size when a black male flooder spends some specified budget on flooding transactions.     

> __< r​ucknium:monero.social >__ Excerpt from the draft:     

> __< r​ucknium:monero.social >__ > Consider an adversary with a daily budget of 12.5 XMR, five times higher than the daily expenditure of the suspected March 2024 black marble flooder. Table 2 says the most cost-effective combination of defense parameters are ring size 60 and minimum 60 nanonero per byte fee. Effective ring size would be 20.7 if the adversary spent its entire budget every day. The 2in/2out refere<clipped message     

> __< r​ucknium:monero.social >__ nce transaction with ring size 60 would be about 140% larger than the transaction with current ring size 16. The user's cost to send this transaction would be about 4 USD cents. The total time to verify all transactions in a block of normal transaction volume would increase from 0.5 seconds to 1.8 seconds. An unpruned node would grow 59 GB in a year instead of 25 GB. Pruned nodes <clipped message     

> __< r​ucknium:monero.social >__ would grow 14 GB instead of 8 GB.     

> __< r​ucknium:monero.social >__ These are potential options that could be discussed for a hard fork before FCMP++     

> __< r​ucknium:monero.social >__ You could consider implementing "Coinbase Consolidation Tx Type" https://github.com/monero-project/research-lab/issues/108     

> __< r​ucknium:monero.social >__ That would reduce the amount of blockchain data because coinbase consolidations would not have the much larger rings. In the 60 ring member scenario, annual blockchain growth would be 2.7 GB less. This could also be important for P2Pool.     

> __< r​ucknium:monero.social >__ If the ring size and/or fee/byte increases a lot, P2Pool mining may become uncompetitive compared to centralized pool mining, especially for the P2Pool mini chain. Consider the 10th percentile of multi-output coinbase outputs during February 2024: 0.000272 XMR. (10% of the likely P2Pool outputs are below this amount.) Right now, consolidating this P2Pool payout by adding an input <clipped message     

> __< r​ucknium:monero.social >__ to a transaction would cost the miner about 5% of the value of that output.     

> __< r​ucknium:monero.social >__ With the ring size 60 and 60 nanoneros/byte scenario considered above, about 49% of the value of that output would be consumed by the cost to spent the output in a transaction's output. But if coinbase outputs only have to have ring size 1, then even paying 60 nanoneros/byte would cost the miner only 3.6% of the output's value when you spent it in a 1-ring-member input (the cost d<clipped message     

> __< r​ucknium:monero.social >__ oes not include the bytes contributed by outputs or other tx data.)     

> __< s​gp_:monero.social >__ Would you support coinbase consolidation transaction types post FCMPs?     

> __< r​ucknium:monero.social >__ The analysis is showing that increasing the ring size is more cost-effective than increasing fees, as a defense against black marble flooding. You could do a combination of a large ring size increase and a modest fee increase.     

> __< r​ucknium:monero.social >__ I think koe didn't want to do a coinbase consolidation type because it adds technical debt. If it is only temporary, then the technical debt may be less. Anyway, if the FCMP++ tx types are expensive, especially the input part, then P2Pool would be less competitive compared to centralized pool mining.     

> __< r​ucknium:monero.social >__ Or you would want to raise the minimum payout for P2Pool. That could negatively affect small miners.     

> __< k​ayabanerve:matrix.org >__ I'm not against mitigating hard forks, at all, assuming proper spacing. cc jberman for an opinion on time till FCMP++ HF release announcement (code, audits, full PR, review, merged, release announced). I'd presume we'd need a few months spacing at the least for a mitigating hard fork to be worth it?     

> __< s​gp_:monero.social >__ the argument against coinbase consolidation type has been complexity, yes. And relatively small benefit relative to that complexity     

> __< k​ayabanerve:matrix.org >__ FCMPs can be made computationally expensive, not bandwidth expensive, quite nicely.     

> __< k​ayabanerve:matrix.org >__ Something about 2 inputs doubling the size yet BPs only growing 64 bytes as they double.     

> __< jberman >__ I think we're still on track for 16-18 months from now     

> __< r​ucknium:monero.social >__ I mean "expensive" as how much it costs in tx fees to broadcast a FCMP++ tx/. That's a function of min fee/byte and the size of the proof on the input side     

> __< k​ayabanerve:matrix.org >__ when the hell did the track become 16-18 months 0_o     

> __< jberman >__ code complete / full PR within 5-6 months still reasonable     

> __< jberman >__ 1.5 years was initial estimate     

> __< k​ayabanerve:matrix.org >__ discussion for later, for now we have context for a mitigating HF     

> __< jberman >__ was it not?     

> __< k​ayabanerve:matrix.org >__ Rucknium: Right. If we make it computationally expensive, not bandwidth expensive, it'd be cheap.     

> __< j​effro256:monero.social >__ When do we get to the state in development when FCMP-RCT becomes perpetually "2 years away"™?     

> __< k​ayabanerve:matrix.org >__ It's not 64 bytes an input cheap, it's... hmm. I actually don't know what'd it'd be off the top of my head. It may actually be comparable to a bit smaller CLSAG still due to the branch hashes not being so scalable :/     

> __< s​gp_:monero.social >__ how much support is there for an immediate hardfork? I didn't realize people still wanted this     

> __< k​ayabanerve:matrix.org >__ Let's assume additional inputs under FCMPs remain comparable to a bit-smaller CLSAG for now. I don't want to over promise.     

> __< k​ayabanerve:matrix.org >__ jeffro256: when i'm dead and my ghost fails to haunt you back to work     

> __< jberman >__ FCMP-RCT is moving forwards at expected pace or faster so far in my view     

> __< k​ayabanerve:matrix.org >__ I'm not against one, especially if we're discussing 1.5y till FCMP++. It'd mean a year spacing.     

> __< c​haser:monero.social >__ sgp: not literally "immediate", but I do support it. the way the chain is right now, it's vulnerable to a black marble attack at any time.     

> __< s​gp_:monero.social >__ I'm still a big fan of increasing fees to simultaneously 1) discourage micro-amount output spending in all cases, 2) make attacks more expensive, and 3) incur no on-chain cost to reduce the risk of an attack. Increasing the ringsize will help as well and should be considered, but the cost for each new decoy is pricey and adds bloat. Fees do not add bloat, and so long as transactio<clipped message>     

> __< s​gp_:monero.social >__ ns remain approximately 1 cent or less, users still have affordable transactions     

> __< c​haser:monero.social >__ then your and Rucknium's cost calculations use different models. right?     

> __< r​ucknium:monero.social >__ The cost of the bloat is low. You can try alternative calculations on that :)     

> __< rbrunner >__ Didn't Rucknium just carefully show that it's not pricey?     

> __< k​ayabanerve:monero.social >__ ring size 40 ring size 40 ring size 40     

> __< rbrunner >__ Maybe contraintuitive, but I trust Rucknium's math more that some gut feeling, frankly     

> __< k​ayabanerve:matrix.org >__ (without explicitly endorsing any specific ring size, I would ask any HF include a fee bump)     

> __< r​ucknium:monero.social >__ We can wait to discuss this more until next meeting, when the full methodological details will be posted. We have something, uh, expensive to approve now.     

> __< rbrunner >__ Still not a fan of such a pre-FCMP hardfork. I am still not impressed what such a black marble attack is able to achieve, realistically.     

> __< s​gp_:monero.social >__ Rucknium: did you share a copy of your draft?     

> __< r​ucknium:monero.social >__ sgp_: No. The cost to node operators is a simple function of the retail cost of a 1TB SSD drive (about 1 XMR now), the additional storage needed, and the number of nodes on the network (20,000). Then I multiply that time 2 to adjust for unmeasured costs.     

> __< k​ayabanerve:matrix.org >__ can we get to HDDs 🤔     

> __< r​ucknium:monero.social >__ basically node operators pay about 20 nanoneros/byte _in aggregate_, which is the same as the fee right now. Interesting that the numbers line up like that.     

> __< r​ucknium:monero.social >__ If the ring size increases a lot, HDDs will be really hard to sync.     

> __< s​gp_:monero.social >__ ok, so you're using 20 nanonero/byte for the cost to the network for each added byte from a larger ringsize? And then you factor that in somehow versus the attacker paid cost for on-chain fees?     

> __< r​ucknium:monero.social >__ the 20,000 nodes estimate is from monero.fail. Probably some of those nodes are not "real", so the true amount of aggregate storage required is lower     

> __< k​ayabanerve:monero.social >__ FCMPs change it quite a bit and was my thought Rucknium     

> __< r​ucknium:monero.social >__ Given some budget per day, an attacker can reduce effective ring size to some level because they produce a certain share of all outputs on the chain.     

> __< r​ucknium:monero.social >__ The attacker's budget is not "added" to the cost in the cost effectiveness analysis since we are considering "Alice's" decisions. Alice considers to cost to node storage and to real users who send txs.     

> __< r​ucknium:monero.social >__ 4) Research Pre-Seraphis Full-Chain Membership Proofs ( https://www.getmonero.org/2024/04/27/fcmps.html ). Eagen Review Quotes ( https://gist.github.com/kayabaNerve/7b3572e633ace8aca6e4b27e09acd9d0 )     

> __< r​ucknium:monero.social >__ kayabanerve: Do you want to introduce these quotes?     

> __< k​ayabanerve:matrix.org >__ Sure.     

> __< k​ayabanerve:matrix.org >__ We have a list of quotes from a list of auditors, many familiar to Monero, some not prior contracted AFAIK     

> __< k​ayabanerve:matrix.org >__ We believe this is an exhaustive and fair view of the field. With that, one candidate believed competent stood out on price, Veridise.     

> __< k​ayabanerve:matrix.org >__ Due to this, despite some questions over if the timeline truly could be so short (resolved by our belief of competence), that is our endorsement.     

> __< k​ayabanerve:matrix.org >__ I believe the request here is 10k to MAGIC.     

> __< r​ucknium:monero.social >__ Of the list, only Veridise and Goodell offered to attempt a mathematical proof or disproof, correct?     

> __< r​ucknium:monero.social >__ (IIRC, Goodell was contributing as Surae Noether with MRL for years.)     

> __< k​ayabanerve:matrix.org >__ Please note other firms were anonymized in the most recent revision by request of someone helping facilitate solicitation, in order to not aggravate the firms.     

> __< k​ayabanerve:matrix.org >__ The names of the recommendation, Cypher Stack (currently occupied on another task), and JP Aumasson (who did not submit a quote, yet I wanted to note we contacted) were left transparent as they should be sufficient. Please let me know if that's contested.     

> __< k​ayabanerve:matrix.org >__ *The request is 10k USD to MAGIC for the reasons noted in the gist. The Veridise audit is not XMR denominated and MAGIC will handle the value preservation and non-XMR payouts.     

> __< k​ayabanerve:matrix.org >__ cc sgp_ for any other MAGIC commentary.     

> __< k​ayabanerve:matrix.org >__ Correct. Not all groups were asked, as that discussion was a result of my scoping with CS. Aaron believed review made more sense than attempting to fill in the proof in my document, and so submitted a SoW for just review. Goodell had the choice of which, and was told to submit two quotes with their opinions or one their recommendation, and did the proof. Veridise similarly stepped up.     

> __< r​ucknium:monero.social >__ On Veridise, do you know what is their intended proof technique? Will it use https://github.com/Veridise/Picus ?     

> __< s​gp_:monero.social >__ From my side: I'm confident that we have pooled a broad number of competent candidates, and the Veridise amount is easily justifiable for having them serve as the first reviewer     

> __< rbrunner >__ Could it be that Veridise already reviewed this or something quite similar for somebody else?     

> __< k​ayabanerve:matrix.org >__ No. We're not discussing formal verification yet a traditional proof.     

> __< k​ayabanerve:matrix.org >__ Veridise's talent in formal verification is why I originally noted them, and they are a shoe-in *by experience* for future efforts if we find them amenable and want to outsource performing formal verification.     

> __< k​ayabanerve:matrix.org >__ rbrunner: Not impossible yet I'd doubt it. Their researcher has multiple credits to their name, and they all seemed to be on finite fields.     

> __< k​ayabanerve:matrix.org >__ My belief is they truly are just very familiar with the field     

> __< k​ayabanerve:matrix.org >__ (I'lm here every Wednesday, 5pm UTC folks)     

> __< a​aron:cypherstack.com >__ T__T     

> __< k​ayabanerve:matrix.org >__ Jokes aside, they may also have independent interest as it does have wider applicability     

> __< rbrunner >__ So we may be lucky     

> __< k​ayabanerve:matrix.org >__ But I doubt they are reselling prior done work     

> __< c​haser:monero.social >__ do non-XMR-accepting candidates accept other cryptos?     

> __< rbrunner >__ I think the general fund must have some BTC left ...     

> __< r​euben:firo.org >__ kayabanerve: just a note I spoke to Mikerah from Hashcloak on this who was surprised on the number of hours estimated by Veridise which seemed pretty low for the scope.     

> __< k​ayabanerve:matrix.org >__ Some USDC, USDT.     

> __< r​euben:firo.org >__ This is of course her opinion but thought it was worth bringing up esp since Hashcloak isn't in the running     

> __< k​ayabanerve:matrix.org >__ Agreed. I explicitly asked and they believe it feasible. I'm willing to move forward with them. If they request an extension, we'd need to review progress first.     

> __< k​ayabanerve:matrix.org >__ $4,000 is only upon result which is positive.     

> __< c​haser:monero.social >__ does Veridise accept non-XMR crypto?     

> __< k​ayabanerve:matrix.org >__ Bahhhhh I should've asked them     

> __< r​ucknium:monero.social >__ 4K USD for a disproof too, right?     

> __< r​euben:firo.org >__ I mean the amount is low enough that I think it's okay to do it and see how they go     

> __< k​ayabanerve:matrix.org >__ That would count as a result.     

> __< k​ayabanerve:matrix.org >__ chaser: USDC, USDT.     

> __< c​haser:monero.social >__ then why do we need Magic for the payout?     

> __< k​ayabanerve:matrix.org >__ The contradiction would be with the math itself, not my specification (so a bug in the gadget would not auto-trigger that).     

> __< k​ayabanerve:matrix.org >__ Sorry, is the general fund actively willing to acquire and hold 10k USDC/USDT over the next month and a half, and can it facilitate payout of said USDC/USDT within 1 week?     

> __< k​ayabanerve:matrix.org >__ Also, if a contract is posited, will a member of the general fund sign?     

> __< r​ucknium:monero.social >__ kayabanerve: I assume that you want this expense approved at this meeting. Am I correct?     

> __< rbrunner >__ I think along the same lines as reuben: With a payment so low, we can just try and see how it goes     

> __< k​ayabanerve:matrix.org >__ Yes     

> __< k​ayabanerve:matrix.org >__ The point of this earmarked fund is for expediency.     

> __< k​ayabanerve:matrix.org >__ We do need jberman to confirm their endorsement.     

> __< jberman >__ Confirmed. I was also surprised Veridise price quote was low and time to complete was low. They seem qualified and the specific researcher they intend to assign to the task seems qualified as well. Risk-reward they seem a clear yes to me     

> __< k​ayabanerve:matrix.org >__ I'll also note the two days review given (gist only available today) was suboptimal. I made it when we received the final quote, and the gist delay was my own personal issues. I'd hope to at least offer 2 days, yet 3-4, in the future.     

> __< r​ucknium:monero.social >__ I see a proposal from kayabanerve to award a contract to Veridise to review and possibly prove what is specified here: https://gist.github.com/kayabaNerve/7b3572e633ace8aca6e4b27e09acd9d0     

> __< k​ayabanerve:matrix.org >__ I'd also note the days will always be <7 as if it was >7, I'd ask for it to be signed off on in the prior meeting.     

> __< r​ucknium:monero.social >__ Are there objections to this expense? More support?     

> __< c​haser:monero.social >__ kayaba: okay, my bad. I see why it goes through Magic.     

> __< r​ucknium:monero.social >__ IMHO kayabanerve 's proposal is reasonable.     

> __< k​ayabanerve:matrix.org >__ chaser: Fair questions, not your bad.     

> __< s​gp_:monero.social >__ fwiw, I want to stress that MAGIC isn't charging a fee for this     

> __< k​ayabanerve:matrix.org >__ I said "Sorry,", because when you legitimately asked why not GF after I said USD*, I thought there may be precedent I was unaware of     

> __< r​ucknium:monero.social >__ I should say that kayabanerve and I are on the MAGIC Monero Fund's committee. I don't think there are any significant conflicts of interest involved.     

> __< r​ucknium:monero.social >__ AFAIK some previous audit/review payments to firms that don't accept payment in XMR were handled by binaryFate's Digital Renegades firm.     

> __< j​effro256:monero.social >__ Sorry maybe it was already mentioned, but why were the other auditor options' names redacted?  Also, IIRC, I thought that Cypherstack previously claimed that they unable to perform the review     

> __< c​haser:monero.social >__ Rucknium: sounds good to me as long as there are no good XMR->* pathways     

> __< s​gp_:monero.social >__ I was the one who asked for them to be "redacted" just in case the vendors didn't want their quotes to be so openly discussed with their names attached. Some firms are more conservative about that than others     

> __< j​effro256:monero.social >__ Typically an auditor's value is related to their reputation, which might make comparing options difficult if the options are hidden     

> __< k​ayabanerve:monero.social >__ Sorry. I sent messages from matrix.org which aren't populating     

> __< k​ayabanerve:monero.social >__ Please stay with me a moment     

> __< k​ayabanerve:monero.social >__ If it doesn't, I'll dup them     

> __< r​ucknium:monero.social >__ I hope it is ok for me to say that the info is already in the online log: https://libera.monerologs.net/monero-research-lab/20240521     

> __< s​gp_:monero.social >__ gist -> revisions\     

> __< k​ayabanerve:matrix.org >__ I'd expect this to be through MAGIC, not the committee.     

> __< k​ayabanerve:matrix.org >__ It was requested by a person helping with solicitation to not aggravate the auditors.     

> __< k​ayabanerve:matrix.org >__ It also isn't deemed relevant enough to be necessary.     

> __< k​ayabanerve:matrix.org >__ I followed back up with Cypher Stack and we did work out a proper understanding, hence their submission of a quote.     

> __< k​ayabanerve:matrix.org >__ jeffro256: Agreed there. Eagen was not a candidate (the author of the work). There were notable firms, yet CS is presumably of equivalent respect to the community and was tens of thousands of dollars cheaper. Accordingly, a notable firm would presumably be disqualified on price.     

> __< j​effro256:monero.social >__ Makes sense, but it *would* be nice to try to attach names to quotes for those who give explicit permission from each firm, if it hasn't already been tried     

> __< k​ayabanerve:matrix.org >__ If anyone wants to contest the reasoning there, feel free to.     

> __< k​ayabanerve:monero.social >__ I'll try to make it a Q we ask in the futue.     

> __< s​gp_:monero.social >__ I can definitely share the names as relevant with anyone who is interested, I just don't want a public record in case the companies are sensitive about their quotes. That's all :) Hopefully that makes sense     

> __< k​ayabanerve:monero.social >__ boog900     

> __< k​ayabanerve:monero.social >__ > yeah sounds simple enough, we can do this now.      

> __< k​ayabanerve:monero.social >__ >     

> __< k​ayabanerve:monero.social >__ > Another idea, instead of a migration for monerod, is to change the LMDB comparison function for that table to just ignore the last bit. I would still lean towards migration being a better idea but thought I'd put this out there as a way to avoid one.     

> __< r​ucknium:monero.social >__ kayabanerve: Sorry about the homeserver issues. You have copy-pasted the wrong message I think.     

> __< k​ayabanerve:matrix.org >__ I did not     

> __< k​ayabanerve:matrix.org >__ That is an unrelated note on impl boog900 posted in Cuprate, and I wanted to note here     

> __< k​ayabanerve:matrix.org >__ Sorry for jumping topics as such. I just saw they said they couldn't join and I should quote them, so I quoted them without thinking of waiting to do so. That's my bad     

> __< k​ayabanerve:matrix.org >__ (though we are wrapping up the prior topic)     

> __< k​ayabanerve:matrix.org >__ Anyone have explicit objections/belief another option is clearly better?     

> __< k​ayabanerve:matrix.org >__ Or want to further support Veridise?     

> __< r​ucknium:monero.social >__ jeffro256: Did you have more comments about the proposal?     

> __< s​gp_:monero.social >__ we're not getting a competent review for under $10k from anyone else     

> __< j​effro256:monero.social >__ Just noting that it's hard to compare options without names, so my opinion is inconclusive. It does appear on the surface that Veridise is competent though. I would just hope we avoid falling prey to underbidding     

> __< s​gp_:monero.social >__ jeffro256: let me DM you the names of all     

> __< c​haser:monero.social >__ Rucknium already linked the chat logs     

> __< k​ayabanerve:matrix.org >__ Or again, revision history, IRC log     

> __< j​effro256:monero.social >__ Ah I see     

> __< s​gp_:monero.social >__ anyone else who wants the list do that or DM me, it's not meant to be a secret     

> __< a​aron:cypherstack.com >__ I obviously have a conflict of interest but am following along with interest     

> __< a​aron:cypherstack.com >__ (my company submitted a quote)     

> __< j​effro256:monero.social >__ I wonder if Veridise is up to tackling the more academic math side, since their audits seem to mostly consist of reviewing smart contracts, ZK circuit implementations, etc     

> __< r​ucknium:monero.social >__ jeffro256: I had the same thought. That's why I asked if they were going to use https://github.com/Veridise/Picus . kayabanerve said that they wouldn't. They would do a traditional mathematics proof for the proof attempt.     

> __< k​ayabanerve:monero.social >__ Their researcher, again, has a history of academix works around finite fields.     

> __< a​aron:cypherstack.com >__ Are you allowed to say who this researcher is?     

> __< k​ayabanerve:monero.social >__ It was this history which convinced us of their competency.     

> __< r​ucknium:monero.social >__ Computer-assisted proof are legitimate proofs, of course, but it could be harder to get an independent review of a computer-assisted proof. But Veridise are not doing that, anyway.     

> __< k​ayabanerve:monero.social >__ Alp Bassa     

> __< k​ayabanerve:monero.social >__ Other researchers at Veridise do appear on various preprints     

> __< b​asses:matrix.org >__ Pretty sure tools like that are hell of false positives     

> __< j​effro256:monero.social >__ Will do more research, but I don't have any objections so far. Thanks for all the info     

> __< plowsof >__ Rucknium , iirc binaryFate handled the BP++ peer review payments personally at his own cost     

> __< r​ucknium:monero.social >__ I don't know much about computer-assisted proofs except they were famously used in the first proof of the four colour theorem :)     

> __< r​ucknium:monero.social >__ IMHO, there is rough consensus for kayabanerve 's proposal to award review work to Veridise: https://gist.github.com/kayabaNerve/7b3572e633ace8aca6e4b27e09acd9d0     

> __< r​ucknium:monero.social >__ More agenda items?     

> __< r​ucknium:monero.social >__ We didn't hear from tevador about the Eagen review, but it was posted in this channel in advance of the meeting.     

> __< tevador >__ Sorry, what did I miss?     

> __< r​ucknium:monero.social >__ Maybe we should have name pinged you     

> __< r​ucknium:monero.social >__ kayabanerve wants to have Veridise review some things specified here: https://gist.github.com/kayabaNerve/7b3572e633ace8aca6e4b27e09acd9d0     

> __< tevador >__ Btw, I had some comments about black marble attacks, posted my thoughts in the github issue.     

> __< r​ucknium:monero.social >__ Thank you!     

> __< tevador >__ FWIW, the Veridise quote is clearly the best option, if they can deliver.     

> __< r​ucknium:monero.social >__ Thank you for your input :)     

> __< c​haser:monero.social >__ said comment: https://github.com/monero-project/research-lab/issues/119#issuecomment-2125473270     

> __< r​ucknium:monero.social >__ I asked for more agenda items and didn't hear anything, so we can end the meeting here. Thanks everyone.     

> __< tevador >__ For comparison, the most costly RandomX audit was 53K (5 years ago) and the scope was much larger (the specs + the whole implementation). I find most of the quotes rather high for the divisors.     

> __< k​ayabanerve:monero.social >__ Eh, it is highly skilled labor.     

> __< tevador >__ Regardless of the hourly rate, 150 hours is a bit too much IMO.   

# Action History
- Created by: Rucknium | 2024-05-21T21:55:47+00:00
- Closed at: 2024-06-03T21:53:29+00:00
