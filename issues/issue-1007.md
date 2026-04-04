---
title: Monero Research Lab Meeting - Wed 15 May 2024, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1007
author: Rucknium
assignees: []
labels: []
created_at: '2024-05-14T21:37:35+00:00'
updated_at: '2024-05-22T21:16:16+00:00'
type: issue
status: closed
closed_at: '2024-05-22T21:16:16+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

[Join the Monero Matrix server if you don't already have a Matrix account.](https://web.archive.org/web/20230128130949/https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211027T170000&p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3. [Potential measures against a black marble attack](https://github.com/monero-project/research-lab/issues/119).

4. Research [Pre-Seraphis Full-Chain Membership Proofs](https://www.getmonero.org/2024/04/27/fcmps.html). 

5. Any other business

6. Confirm next meeting agenda


Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#1003  

# Discussion History
## Rucknium | 2024-05-15T19:35:15+00:00
Logs:

> __< r​ucknium:monero.social >__ Meeting time! https://github.com/monero-project/meta/issues/1007     

> __< r​ucknium:monero.social >__ 1) Greetings     

> __< tevador >__ Hi     

> __< c​haser:monero.social >__ hello     

> __< rbrunner >__ Hello     

> __< a​rticmine:monero.social >__ Hi     

> __< j​effro256:monero.social >__ Howdy     

> __< jberman >__ hello     

> __< k​ayabanerve:matrix.org >__ :wave\     

> __< r​ottenwheel:kernal.eu >__ Hola.     

> __< s​gp_:monero.social >__ hello     

> __< h​into:monero.social >__ hi     

> __< r​ucknium:monero.social >__ 2) Updates. What is everyone working on?     

> __< k​ayabanerve:matrix.org >__ Continued work on FCMPs, met with various auditors and got various quotes.     

> __< jberman >__ me: implementing the curves tree tree in C++ for fcmp's     

> __< tevador >__ Jamtis specs, mainly forward-secrecy improvements and some updates based on recent discussions.     

> __< r​ucknium:monero.social >__ me: Estimating tx verification time with different ring sizes and inputs/outputs. Monitoring a recent increase of 1in/16out txs on the blockchain.     

> __< a​rticmine:monero.social >__ Working on scaling and fees for ~ 3000 bytes 2/2 tx and 1/2 tx weight     

> __< a​rticmine:monero.social >__ I do have a question. How does the number of inputs impact tx size under FCMP?     

> __< tevador >__ I heard ~2.2 KB per input.     

> __< k​ayabanerve:monero.social >__ It depends if we power of two structure or not.     

> __< tevador >__ Btw, we could restrict inputs to powers of two with dummy inputs.     

> __< c​haser:monero.social >__ tevador explained this in more detail here, and I think it's a neat idea, though not sure how it plays out re: scalability: https://github.com/monero-project/research-lab/issues/96#issuecomment-2107521580     

> __< k​ayabanerve:matrix.org >__ Additional inputs can only add an extra few hundred bytes, or each power of two we must sum to equal the input qulity may add that 2.2-2.5kB mark.     

> __< k​ayabanerve:monero.social >__ matrix.org has notable latency for sent messages :/     

> __< k​ayabanerve:matrix.org >__ It practically depends on if we want to limit inputs to 16, like we do outputs due to the aggregate range proof.     

> __< k​ayabanerve:matrix.org >__ And if the performance of any wasted inputs is acceptable.\     

> __< r​ucknium:monero.social >__ Ah, sorry. I had a problem.     

> __< tevador >__ The consensus limit would be 64 inputs, ~145 KB size. Most transactions would fit into the 2/2 envelope, so the overhead would be reasonable.     

> __< r​ucknium:monero.social >__ 3) Potential measures against a black marble attack     

> __< k​ayabanerve:monero.social >__ I'll respond to that during the proper section.     

> __< s​gp_:monero.social >__ The most common number of inputs are: 1, 2, and max for filling the max transaction size ~146     

> __< r​ucknium:monero.social >__ Transactions with 1 input and 8-16 outputs produced about 15% of outputs recently. Then starting on May 11 the number of these types of transactions started rising. By yesterday (May 14), they were producing 52% of outputs. But in the first twelve hours of today (May 15) their share of outputs was 33%.     

> __< r​ucknium:monero.social >__ These transactions could be related to Local Monero's cessation of operations. Maybe these are batched withdrawals.     

> __< r​ucknium:monero.social >__ I tried to set up koe's Seraphis performance test for CLSAG verification time estimates: https://github.com/UkoeHB/monero/blob/seraphis_perf/tests/performance_tests/main.cpp     

> __< r​ucknium:monero.social >__ I was mostly successful. koe's code only allows ring size in powers of two. Maybe that could be changed easily, but I don't know C++. My plan, which seems to be working, is to interpolate the verification time for different ring sizes by Ordinary Least Squares (OLS) regression. We need to estimate verification time for the 2in/2out reference transaction and for a diverse set of in<clipped message     

> __< r​ucknium:monero.social >__ /out tx types in a realistic "average" block.     

> __< r​ucknium:monero.social >__ I think by Monday I will have a draft for feedback of the different options for fee and ring sizes, effective ring size when a black marble flooder has different budgets, users' cost to send txs, the one year blockchain growth estimates, verification time, etc.     

> __< r​ucknium:monero.social >__ 4) Research Pre-Seraphis Full-Chain Membership Proofs. https://www.getmonero.org/2024/04/27/fcmps.html     

> __< r​ucknium:monero.social >__ By the way, thanks to nioCat for noticing the 1in/16out tx increase first.     

> __< tevador >__ kayabanerve: any comments on FCMP++ inputs?     

> __< k​ayabanerve:matrix.org >__ If we do a pow-two system, there's no wasted work. If we do an aggregate system (lowest overall bandwidth), 33 inputs causes 64 inputs of work to be completely clear there.     

> __< rbrunner >__ How do those p2pool payout transactions with 150 outputs fit there? Are they still outside, so to say, because different type of transaction?     

> __< k​ayabanerve:monero.social >__ On-chain limit is 16 outputs.     

> __< k​ayabanerve:monero.social >__ So I'm unsure what P2pool is or isn't doing.     

> __< tevador >__ So the choice is basically between wasted work or wasted space. Wasted space would come with the benefit of quantizing transaction shapes, leading to better uniformity.     

> __< r​ucknium:monero.social >__ kayabanerve: For coinbase outputs when FCMP++ is implemented, the limit is 16 outputs?     

> __< c​haser:monero.social >__ miner reward payouts are a different tx type, aren't they? I've seen 16+ output payouts from p2pool.     

> __< tevador >__ Coinbase txs have no limit because they have no range proofs.     

> __< r​ucknium:monero.social >__ A coinbase tx can have a huge number of outputs now.     

> __< a​rticmine:monero.social >__ Yes. If I understand correctly they are  in the clear.     

> __< a​rticmine:monero.social >__ Coinbase     

> __< j​effro256:monero.social >__ Let's say you have 15 inputs. Is there any verify time wasted doing a 8 + 4 + 2 + 1, versus adding 1 dummy to make 16?     

> __< tevador >__ IIUIC, 8+4+2+1 is only for storage. The work is still 16.     

> __< k​ayabanerve:matrix.org >__ Oh, I have no ideas/comments on coinbase outputs.     

> __< k​ayabanerve:matrix.org >__ FCMP++ only affects the input side of things.     

> __< rbrunner >__ 23 outputs: https://p2pool.io/explorer/tx/8bf3108a0ac267ca0e5d5ab4c622f05f816b1139f5ed1f9feae7e28445c3fe9a     

> __< k​ayabanerve:matrix.org >__ jeffro256: 15 * (256 + 128) gates vs 16 * (256 + 128) gates     

> __< tevador >__ Dummy inputs have some compute overhead due to the need to update the tree root.     

> __< k​ayabanerve:matrix.org >__ BUT you also have the overhead of the multiple proofs.     

> __< k​ayabanerve:matrix.org >__ No, 8 + 4 + 2 + 1 does multiple 'setups' (being mutiple proofs) but doesn't waste any multiplication gates.     

> __< j​effro256:monero.social >__ kk thank you     

> __< k​ayabanerve:matrix.org >__ Shall I move to discussing audits now?     

> __< r​ucknium:monero.social >__ I don't know how to evaluate the bandwidth (bytes) tradeoff with the verification time bandwidth until we have more certain numbers about verification time.     

> __< k​ayabanerve:matrix.org >__ Er, review/research/audits     

> __< k​ayabanerve:matrix.org >__ Rucknium: Currently at ~35ms for one, 12ms per in a batch of ten, 10ms per in a batch of one hundred, without tailored field implementations.     

> __< k​ayabanerve:matrix.org >__ Those are all 1-input proofs.     

> __< a​rticmine:monero.social >__ When it comes to verification time we need to consider parallel processing.     

> __< jberman >__ It would be a nice to get a table up with columns for # of inputs, tx size, verification time (for both approaches pow-2 / not). Similar to how koe did it for Seraphis here: https://github.com/monero-project/research-lab/issues/91     

> __< a​rticmine:monero.social >__ There is a very significant amount of underutilized CPU and GPU power here     

> __< r​ucknium:monero.social >__ If we can, when code audits are done we should try to audit parallelized implementations so they can be deployed confidently on mainnet.     

> __< a​rticmine:monero.social >__ Yea!     

> __< tevador >__ Beware of scope screep.     

> __< tevador >__ creep*     

> __< k​ayabanerve:matrix.org >__ I don'     

> __< rbrunner >__ One after the other :)     

> __< k​ayabanerve:matrix.org >__ *I don't believe current perf mandates parallelization, and you'd arguably only want to parallelize circuit instantiations (not the BP verifying proper, as that'll give you multiple multiexps)     

> __< k​ayabanerve:matrix.org >__ If you do want full parallelization, with multiple multiexps, wherever the TX verifies a list of proofs, it'd just make 4 proofs and do verification on 4 threads     

> __< k​ayabanerve:matrix.org >__ *4 lists and do verification...     

> __< k​ayabanerve:matrix.org >__ So it's quite trivial to so parallelize.     

> __< a​rticmine:monero.social >__ I am talking of verification of different transactions in parallel     

> __< k​ayabanerve:matrix.org >__ Regarding audits and review, we've collected 4 quotes and are waiting on 2 re: divisor review.     

> __< rbrunner >__ Quick ELI5 explanation what is a "divisor", maybe?     

> __< rbrunner >__ Or is it "complicated" anyway     

> __< k​ayabanerve:matrix.org >__ eli5: something mathemeticians made up, even I don't understand them     

> __< rbrunner >__ :)     

> __< jberman >__ *thumbs up* will parallelize verification of FCMP's where trivial as described there, including across txs     

> __< k​ayabanerve:matrix.org >__ Tbf, I also haven't learned how BP works internally, solely how to use it.     

> __< rbrunner >__ If they just work, and provably so, who cares :)     

> __< r​ucknium:monero.social >__ Thanks, jberman :)     

> __< k​ayabanerve:matrix.org >__ Anyways, I solicited 1 quote from Cypher Stack regarding the composition.     

> __< k​ayabanerve:matrix.org >__ I did not mass request quotes for that as it was not specified for just anyone to review the work. It does need someone familiar with Monero to 'run with it'     

> __< k​ayabanerve:matrix.org >__ (verify it achieves the desired properties, unlinkable, unforgeable, non-malleable linking tags, a correct composition, etc)     

> __< k​ayabanerve:matrix.org >__ https://gist.github.com/AaronFeickert/c24d42d9180ddba515462d4468f25831 2.5 weeks, 175 XMR was the quote from Diego Salazar     

> __< k​ayabanerve:matrix.org >__ I'd endorse moving forward with that, and given jberman and MRL oversight, such moving forward is allowed to occur per the earmarked fund.     

> __< k​ayabanerve:matrix.org >__ > kayabaNerve and jberman are the people primarily expected to find such parties, with the actual agreement on parties and amount to be by their endorsement, and a general agreement within MRL that the proposed expenditure is reasonable. The word choice of reasonable means that the proposed parties are reasonably trusted to be able to adequately perform the work proposed, the amou<clipped message     

> __< k​ayabanerve:matrix.org >__ nt to be paid is understandable and amenable, and if there are other potential parties, none are clearly, completely, and definitively better choices.     

> __< k​ayabanerve:matrix.org >__ For the relevant paragraph     

> __< jberman >__ I'm in favor of moving forward with CS for composition review     

> __< rbrunner >__ Only 2.5 weeks sounds pretty attractive, for whatever this is     

> __< r​ucknium:monero.social >__ What does "review" mean in the gist?     

> __< k​ayabanerve:matrix.org >__ And a steal at just 175 XMR! Buy now and get a copy of Diego's 10 best hits, including their Christmas songs, free!     

> __< d​iego:cypherstack.com >__ I've published two novels.     

> __< k​ayabanerve:matrix.org >__ The composition composes already proved proofs. The only necessity is to verify they compose as expected to the intended effects. I'd leave Aaron Feickert to comment in more detail though.     

> __< d​iego:cypherstack.com >__ One MRL member gets a free novel if we move forward on this proposal. ;)     

> __< r​ucknium:monero.social >__ Will we get a security proof of the composability of this system?     

> __< tevador >__ Forward secrecy should be among the properties to be audited.     

> __< r​ucknium:monero.social >__ (I barely understand composability on a surface level 😬)     

> __< k​ayabanerve:matrix.org >__ Diego Salazar: no kickbacks     

> __< k​ayabanerve:matrix.org >__ It;d be a proof of the composition, not of the composability. I'd agree to including F-S if it wasn't for the fact I wrote a script effectively proving F-S     

> __< k​ayabanerve:matrix.org >__ (if it was a proof tbc)     

> __< r​ucknium:monero.social >__ Well, I have _proven_ that I don't know the difference between composition and composability ;)     

> __< tevador >__ kayabanerve: your script/proof should be reviewed.     

> __< r​ucknium:monero.social >__ kayabanerve: Is your goal to get loose consensus at this MRL meeting about this expense? Would the work schedule be delayed if we review this quote for another week? AFAIK this meeting is the first time we have this quote and scope of work to review.     

> __< k​ayabanerve:matrix.org >__ I don't mind including F-S again if Aaron Feickert or Diego Salazar want to chime in there.     

> __< rbrunner >__ So, strongly simplified, security should be ok if the proofs that get composed are all ok, because what could go wrong when composing? ...     

> __< k​ayabanerve:matrix.org >__ No, my goal is for the MRL to agree it reasonable. Presumably, yes, Diego will not work on this without the contract in hand, so this would delay work.     

> __< d​iego:cypherstack.com >__ we at CS would appreciate getting to work on this     

> __< k​ayabanerve:matrix.org >__ Considering CS also submitted a distinct quote, their time is in demand and waiting an extra week does impact other milestones.     

> __< k​ayabanerve:matrix.org >__ If composed correctly, hence the explicit review towards the desired properties.     

> __< k​ayabanerve:matrix.org >__ (assuming they're picked for said distinct quote, but even if not, I have other quotes to request from them)     

> __< tevador >__ FWIW, I think the audit quote is reasonable and might even result in a more efficient proof, so I'd go for it.     

> __< k​ayabanerve:matrix.org >__ I'd be amazed if at the 2.5w mark, something didn't click into being lined up.     

> __< r​ucknium:monero.social >__ Personally I would be OK with approving it at this meeting. In the future, if the quote and scope is available before the meeting, try to share it before the meeting.     

> __< rbrunner >__ I would tend to give my own "go" given that the size is "small" in comparison to the whole "pot"     

> __< k​ayabanerve:matrix.org >__ Heard, Rucknium.     

> __< s​gp_:monero.social >__ Generally I'm in favor of multiple quotes given how wonky audit prices can be, but this current proposal doesn't concern me     

> __< rbrunner >__ Agree with Rucknium, especial if we arrive at the bigger parts     

> __< rbrunner >__ I guess reviewing that "divisor" wizardry will be considerably bigger already?     

> __< k​ayabanerve:matrix.org >__ I agree on the value of multiple quotes when I don't see a candidate clearly optimal who responds with a reasonable quote. I personally believe CS optimal for this work and the quote reasonable.     

> __< s​gp_:monero.social >__ understood, and those justifications make sense to me     

> __< r​ucknium:monero.social >__ I don't see any objections so far for MRL loose consensus on this expense. Anyone else want to say something?     

> __< d​iego:cypherstack.com >__ tell me where to send the book     

> __< j​effro256:monero.social >__ Im okay with CS reviewing FCMP-RCT composition for 175 XMR (including F-S variant)     

> __< tevador >__ ^ AFAIK only the F-S variant is on the table.     

> __< k​ayabanerve:matrix.org >__ tevador is correct.     

> __< j​effro256:monero.social >__ Even better     

> __< r​ucknium:monero.social >__ Is tevador's F-S comment still a loose end?     

> __< tevador >__ I'm unsure if the provided quote included the F-S property. If not, it should be added.     

> __< k​ayabanerve:matrix.org >__ We'd have to ask Diego Salazar Aaron Feickert the impact of them reviewing the premise of F-S (a DLog oracle can find solutions for all components given an arbitrary output, and accordingly can't disprove arbitrary outputs) and to also review said script for sanity. That may be trivial enough, may be a few XMR more?     

> __< a​aron:cypherstack.com >__ If there's a particular design (related to F-S or not) that should be in scope, please ensure it's either included in the referenced technical note or specifically documented otherwise     

> __< a​aron:cypherstack.com >__ That way there's no scope ambiguity     

> __< k​ayabanerve:matrix.org >__ It is the in the FCMP++ PDF, including the premise and a link to the supporting script.     

> __< a​aron:cypherstack.com >__ Checking, one sec     

> __< a​aron:cypherstack.com >__ (or if you have the section handy, please let me know)     

> __< a​aron:cypherstack.com >__ Do you mean the link in Section 5.5?     

> __< a​aron:cypherstack.com >__ Oh geez, after quickly reviewing the meeting notes, I assumed you meant Fiat-Shamir...     

> __< a​aron:cypherstack.com >__ you mean forward secrecy     

> __*__ m-relay <a​aron:cypherstack.com> flips a switch somewhere in his brain     

> __< k​ayabanerve:matrix.org >__ 5.5     

> __< k​ayabanerve:matrix.org >__ Sorry for the delay     

> __< a​aron:cypherstack.com >__ OK, so AIUI the scope, which was originally Section 3 (and anything required from Section 2), should add Section 5.5     

> __< a​aron:cypherstack.com >__ ?     

> __< a​aron:cypherstack.com >__ np     

> __< k​ayabanerve:matrix.org >__ Ideally :)     

> __< a​aron:cypherstack.com >__ Sorry for the confusion on F-S :D     

> __< k​ayabanerve:matrix.org >__ Sorry for causing it     

> __< a​aron:cypherstack.com >__ I'd say just add a couple of days     

> __< a​aron:cypherstack.com >__ Nah, I was catching up on the meeting notes too quickly :/     

> __< k​ayabanerve:matrix.org >__ Diego Salazar: What's the + XMR for that?     

> __< d​iego:cypherstack.com >__ Add 23 XMR     

> __< k​ayabanerve:matrix.org >__ 198 total then. I'm fine with it, cc jberman tevador Rucknium everyone_else_here     

> __< jberman >__ +1     

> __< tevador >__ Looks fine to me.     

> __< a​aron:cypherstack.com >__ For completeness, I'll update that gist to include the relevant sections of the technical note     

> __< a​aron:cypherstack.com >__ Just so nothing slips through the cracks     

> __< r​ucknium:monero.social >__ IMHO, at this MRL meeting there is loose consensus for this 198 XMR expense with the Forward-Secrecy modification: https://gist.github.com/AaronFeickert/c24d42d9180ddba515462d4468f25831     

> __< a​aron:cypherstack.com >__ The scope is Sections 2, 3, and 5.5     

> __< a​aron:cypherstack.com >__ (gist updated just now)     

> __< k​ayabanerve:matrix.org >__ 👍 then     

> __< r​ucknium:monero.social >__ Thank you all! More FCMP++ items to discuss?     

> __< d​iego:cypherstack.com >__ Great! We'll start tomorrow.     

> __< k​ayabanerve:matrix.org >__ That's it from me     

> __< r​ucknium:monero.social >__ Any other business?     

> __< a​aron:cypherstack.com >__ A preview of what my notebook will look like while working on the project :D https://i.kym-cdn.com/entries/icons/original/000/022/524/pepe_silvia_meme_banner.jpg     

> __< r​ucknium:monero.social >__ We can end the meeting here.     


# Action History
- Created by: Rucknium | 2024-05-14T21:37:35+00:00
- Closed at: 2024-05-22T21:16:16+00:00
