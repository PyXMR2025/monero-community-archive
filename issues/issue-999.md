---
title: Monero Research Lab Meeting - Wed 01 May 2024, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/999
author: Rucknium
assignees: []
labels: []
created_at: '2024-04-30T17:26:19+00:00'
updated_at: '2024-05-09T16:46:09+00:00'
type: issue
status: closed
closed_at: '2024-05-09T16:46:09+00:00'
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

#995 

# Discussion History
## vtnerd | 2024-04-30T20:56:11+00:00
Small nitpick, the date is may 1st (there is no April 31st).

## AaronFeickert | 2024-04-30T22:09:34+00:00
> Small nitpick, the date is may 1st (there is no April 31st).

"If you will it, Dude, it is no dream."

## Rucknium | 2024-05-01T01:28:37+00:00
"Where we're going, we don't need calendars." Thanks. Fixed.

## Rucknium | 2024-05-01T20:41:22+00:00
Logs:

> __< r​ucknium:monero.social >__ Meeting time! https://github.com/monero-project/meta/issues/999     

> __< tevador >__ Hi     

> __< r​ucknium:monero.social >__ 1) Greetings     

> __< o​ne-horse-wagon:monero.social >__ Hello!     

> __< s​gp_:monero.social >__ hello     

> __< rbrunner >__ hello     

> __< a​aron:cypherstack.com >__ Hello!     

> __< h​into:monero.social >__ hi     

> __< b​oog900:monero.social >__ hi     

> __< v​tnerd:monero.social >__ hi     

> __< r​ucknium:monero.social >__ 2) Updates. What is everyone working on?     

> __< tevador >__ Me: Jamtis-RCT specs: https://gist.github.com/tevador/d3656a217c0177c160b9b6219d9ebb96 and FCMP++ reviews.     

> __< j​effro256:monero.social >__ howdy     

> __< j​effro256:monero.social >__ Me: (attempting) Reviewing FCMP-RCT and writing Seraphis integration code     

> __< v​tnerd:monero.social >__ Worked primarily on debugging the p2p ssl code, and now hopefully finishing up the first cut at lws remote scanning     

> __< r​ucknium:monero.social >__ me: Starting to collect logs from people who `set_log net.p2p.msg:INFO` in `monerod` for analysis of possible node origin of the black marble flood transactions. Working on optimal ring size and fee/byte in terms of cost effectiveness during a black marble flood.     

> __< k​ayabanerve:matrix.org >__ I've been working on the FCMPs specification and implementation.     

> __< 0​xfffc:monero.social >__ Hi everyone     

> __< u​ntraceable:monero.social >__ Hi     

> __< 0​xfffc:monero.social >__ Me: did start working on performance suite and investigating ways to find bottleneck for rwlock. ( In parallel, I submit minor/simple PRs here and there ). Starting today I am full-time on Monero.     

> __< r​ucknium:monero.social >__ 3) Potential measures against a black marble attack. https://github.com/monero-project/research-lab/issues/119     

> __< r​ucknium:monero.social >__ If anyone has more comments about reasonable parameters for evaluating the cost effectiveness of raising ring size and/or increasing fee/byte to defeat black marble flooding ( https://github.com/monero-project/meta/issues/995#issuecomment-2077014407 ) , please tell me.     

> __< r​ucknium:monero.social >__ If anyone was collecting `net.p2p.msg:INFO` log data for black marble flood analysis, especially during April 12, 13, and 15, please DM me for submission instructions.     

> __< r​ucknium:monero.social >__ I evaluated the possibility of getting an analytical solution to the nonlinear optimization problem with inequality constraints by checking the Karush-Kuhn-Tucker conditions. IMHO, it is not worth the time to do that, but if someone has another opinion, please let me know. I already have a good, simple,  numerical solution algorithm.     

> __< r​ucknium:monero.social >__ The benefit of having an analytical solution is that we would have more information about the "deep" meaning of the optimization problem, could carry out comparative statics, etc.     

> __< j​effro256:monero.social >__ Which optimization problem?     

> __< r​ucknium:monero.social >__ I noticed there was more discussion on the GitHub issue about a network/node-based PoW requirement to send transactions. I won't be evaluating that idea since it would take a long time to consider all the complexity. I will evaluate a simple tx-PoW requirement to have a tx confirmed on the blockchain.     

> __< r​ucknium:monero.social >__ jeffro256: Finding the best cost effectiveness in terms of user fee and node storage requirements for effective ring size when black marble flooding is occurring     

> __< r​ucknium:monero.social >__ The objective function is cost/effective_ring_size. You want to minimize that by choosing ring size and fee/byte.     

> __< r​ucknium:monero.social >__ More comments on potential measures against a black marble attack?     

> __< r​ucknium:monero.social >__ The numerical solution is a simple grid search basically. It makes nice contour plots :)     

> __< r​ucknium:monero.social >__ 4) Research Pre-Seraphis Full-Chain Membership Proofs. https://www.getmonero.org/2024/04/27/fcmps.html     

> __< r​ucknium:monero.social >__ Aaron Feickert: You have updates on the Generalized Bulletproofs security proof progress     

> __< a​aron:cypherstack.com >__ testing     

> __< a​aron:cypherstack.com >__ Are these messages going through?     

> __< a​aron:cypherstack.com >__ My Element client is acting funky     

> __< r​ucknium:monero.social >__ the "testing" message went through     

> __< u​ntraceable:monero.social >__ Yes     

> __< rbrunner >__ I see them     

> __< r​ucknium:monero.social >__ and the two after that     

> __< a​aron:cypherstack.com >__ OK, sorry about that     

> __< a​aron:cypherstack.com >__ Yes, I have an update!     

> __< a​aron:cypherstack.com >__ Cypher Stack has been reviewing the Generalized Bulletproofs design required for Curve Trees to work     

> __< a​aron:cypherstack.com >__ We're about halfway through, and identified a minor issue     

> __< k​ayabanerve:matrix.org >__ https://libera.monerologs.net/monero-research-lab/20240501 Aaron Feickert ;)     

> __< a​aron:cypherstack.com >__ The issue is that the proving relation informally described by the authors doesn't quite work with the soundness proof     

> __< a​aron:cypherstack.com >__ A solution is to modify how vector commitments are represented in the relation, which technically means they can use more generators     

> __< a​aron:cypherstack.com >__ Modifying that, and updating the proofs accordingly, fixes things     

> __< a​aron:cypherstack.com >__ But     

> __< a​aron:cypherstack.com >__ This change comes with a free benefit     

> __< a​aron:cypherstack.com >__ Because the commitments can use additional generators, we can add constraint matrices to the design, which could allow for more efficient proofs     

> __< a​aron:cypherstack.com >__ Adding these matrices is straightforward, and everything works fine even if you chose not to use them (just set them to zero and the algebra still works as expected)     

> __< a​aron:cypherstack.com >__ I spoke with kayabanerve to confirm (a) that the original fix (which changes commitment generators) doesn't introduce any issues with Curve Trees, and (b) that the matrix addition could be helpful     

> __< r​ucknium:monero.social >__ Is this size-efficient proofs or verification-time-efficient or both?     

> __< a​aron:cypherstack.com >__ Mostly size     

> __< a​aron:cypherstack.com >__ But could also be time (I haven't run the numbers on that portion)     

> __< r​ucknium:monero.social >__ So probably no worse performance on time than the original design?     

> __< a​aron:cypherstack.com >__ Nope, and totally optional to use     

> __< a​aron:cypherstack.com >__ Adding the matrices also has minimal impact on the complexity of the security analysis     

> __< a​aron:cypherstack.com >__ (above the changes already required for the initial design fix)     

> __< r​ucknium:monero.social >__ The summary is that the original design appears to not work, but an adjustment to the design will probably work and will be even more size efficient. Your next move it to try to write a security proof for the adjusted design. Does this fit within the allocated labor time and funds?     

> __< a​aron:cypherstack.com >__ Anyway, this is all detailed in the report     

> __< a​aron:cypherstack.com >__ To be clear, it's only the original design's (informal) proving relation, which could be problematic for other uses that might require certain generators     

> __< a​aron:cypherstack.com >__ The initial adjustment absolutely works, and the matrix addition is just being finalized and integrated easily into the existing security proof work already done and in progress     

> __< a​aron:cypherstack.com >__ We expect no change to the timeline     

> __< r​ucknium:monero.social >__ Fantastic. Thank you!     

> __< a​aron:cypherstack.com >__ Like I said, the matrix change is very straightforward to include     

> __< r​ucknium:monero.social >__ "Anyway, this is all detailed in the report". Is this an internal draft or does it exist publicly?     

> __< k​ayabanerve:matrix.org >__ The decreased size usage does avoid increased verification time. If we have a set bandwidth target, we can either increase verification time OR increase bandwidth efficiency.     

> __< a​aron:cypherstack.com >__ Oh, I should have said that it's included in the report as I'm writing it, and will therefore be included in the final report     

> __< r​ucknium:monero.social >__ What does "bandwidth" mean?     

> __< tevador >__ tx size     

> __< a​aron:cypherstack.com >__ The effect of the matrix change is to double the number of vector commitment constraints for a given number of vector commitments included in a proof     

> __< a​aron:cypherstack.com >__ without a size increase     

> __< a​aron:cypherstack.com >__ (there are some subtleties though)     

> __< a​aron:cypherstack.com >__ But barring anything unexpected, we expect that the report will provide a satisfactory security proof for the modified construction     

> __< k​ayabanerve:matrix.org >__ More data in less bytes Rucknium     

> __< a​aron:cypherstack.com >__ (and which reduces to the "original" GBP design trivially if desired/needed)     

> __< a​aron:cypherstack.com >__ Heck, it might end up being useful enough to warrant submission to a conference /shrug     

> __< a​aron:cypherstack.com >__ I'd have to see if the original author(s) would be interested in such a thing, but that's for another day     

> __< r​ucknium:monero.social >__ Do kayabaNerve and tevador want to give updates on FCMP++?     

> __*__ m-relay <a​aron:cypherstack.com> quietly exits     

> __< tevador >__ Did anyone have time to review Jamtis-RCT?     

> __< j​effro256:monero.social >__ I've only skimmed it so far     

> __< k​ayabanerve:matrix.org >__ I need a few minutes to fully comment, sorry.     

> __< k​ayabanerve:matrix.org >__ *before I can fully comment.     

> __< tevador >__ We also discussed how to handle torsioned points in FCMPs and we came back to Ristretto, which was discussed here some time ago. Specifically, if we adopted Ristretto for point serialization, it could save a lot fo headache.     

> __< rbrunner >__ Maybe while we wait I can throw in a quick question     

> __< k​ayabanerve:matrix.org >__ I have yet to review JAMTIS RingCT but I'm extremely interested in the claim it mitigated Janus for existing addresses (except for main <-> subaddress relations).     

> __< k​ayabanerve:matrix.org >__ It means new address become about functionality, not privacy (barring that one remaining edge case)     

> __< rbrunner >__ Are Bulletproofs++ more or less "off the table" after that quite mixed result of the review, and the move to FCMPs with GBP?     

> __< k​ayabanerve:matrix.org >__ I'd shelve BP++ for now, which were never explicitly posited for FCMPs.     

> __< j​effro256:monero.social >__ What operations are involved in Ristretto decompressing, and is it faster than (mul x8) ? I saw tevador and kayabanerve have a little back and forth about that. [TBH i don't really care about tx builder side performance within reason]     

> __< tevador >__ Yes, it should be faster than mul8, pending benchmarks.     

> __< tevador >__ It avoids at least 1 field inversion and 6 point doublings per output.     

> __< k​ayabanerve:matrix.org >__ I have Python which is less than 100 lines for Ristretto.     

> __< a​aron:cypherstack.com >__ Plus the Ristretto serialization is intended as a thin wrapper around existing Edwards operations     

> __< k​ayabanerve:matrix.org >__ Yep     

> __< k​ayabanerve:matrix.org >__ The specification has incorporated feedback. I won't claim it's complete, as I want to implement the math behind the gadgets and ensure a lack of typos in that manner, but I don't expect major changes.     

> __< j​effro256:monero.social >__ Who would we get to review the divisors? I     

> __< k​ayabanerve:matrix.org >__ I've started cleaning up the prior code ('productionizing it'), fixing edge cases and bugs, and making it something I'd endorse auditing.     

> __< r​ucknium:monero.social >__ jeffro256: Don't we have to prove the security of the divisors and then review the proofs?     

> __< k​ayabanerve:matrix.org >__ On divisors, I've already solicited two quotes/statements of work.     

> __< k​ayabanerve:matrix.org >__ Divisors come with a correctness proof. Arguably, we need it reviewed and an audit a literal protocol aligns with its mathematics.     

> __< k​ayabanerve:matrix.org >__ We don't need a ZK proof, solely a soundness proof, as we execute it in a ZK context. The section on correctness covers what we'd call soundness.     

> __< k​ayabanerve:matrix.org >__ And then the literal protocol, my draft proposal in the LaTeX I published, would be literally implemented (secure hash functions and so on) and audited.     

> __< k​ayabanerve:matrix.org >__ Also, Rucknium, clarifying: one of the reasons I've been a bit annoying on not formally proving all of this, and instead solely auditing, is as vast sections of the math is primitive.     

> __< k​ayabanerve:matrix.org >__ I probably have a page of latex which reduces to `a - b = 0; a - b + b = 0 + b; a = b` and similar     

> __< j​effro256:monero.social >__ How "modular" is the application of divisors? Can we review the soundness of an isolated Prove/Verify divisor "algorithm", which then guarantees all uses under certain conditions is sound? Or do just have to have a full contextual working protocol before we can audit our implementation/use of divisors within that protocol?     

> __< k​ayabanerve:matrix.org >__ (the first being the check, the last line being the statement, the intemediary being the proof)     

> __< k​ayabanerve:matrix.org >__ But moving forward, the plan is to review/audit the divisor proof (review the theory which has a section on correction, audit our literal instantiation and impl), and formally verify said primitive math.     

> __< k​ayabanerve:matrix.org >__ I've reviewed tooling and one of the entities I solicited a quote from is explicitly experienced with formally verifying circuits.     

> __< k​ayabanerve:matrix.org >__ jeffro256: They're a concept. I wrote a 'gadget' which assumes a challenge function with proper transcripting (trivial to instantiate with GBPs). The gadget is then a black box.     

> __< k​ayabanerve:matrix.org >__ Specifically, the gadget says there's some unreliable representation of a discrete logarithm which is usable to prove `X = x G`, for a public `G`, AND if `x` is reused, `x1 = x2`, where `1, 2` are the instance of use. The unreliability of the representation does not make it unreliable on reuse within a proof.     

> __< k​ayabanerve:matrix.org >__ It's a whole thing, it's documented     

> __< k​ayabanerve:matrix.org >__ Eagen's work does describe divisor construction, evaluation, and the challenge evaluation. We'd argue our gadget follows it.     

> __< k​ayabanerve:matrix.org >__ Once I confirm the lack of notational issues, we'd have the spec within the LaTeX audited.     

> __< k​ayabanerve:matrix.org >__ Later, we'd audit the impl to match the spec.     

> __< k​ayabanerve:matrix.org >__ I'll also note my work has been proceeding at a much quicker rate than I would've expected. I'm wondering if that time will be saved OR paid for on the back end (there's always *something* that still needs to be done)     

> __< k​ayabanerve:matrix.org >__ I've also been discussing with jberman about them starting their work on integration and topics such as FFI'ing, and what exactly is exposed over FFI (and what helpers provided)     

> __< k​ayabanerve:matrix.org >__ The tree has been the main discussion.     

> __< r​ucknium:monero.social >__ FFI = Foreign Function Interface?     

> __< k​ayabanerve:monero.social >__ Also, performance *if research holds* is looking to be quite favorable and only with minor overhead to a variant using Seraphis's linking tag definition     

> __< k​ayabanerve:monero.social >__ Yes re: FFI     

> __< k​ayabanerve:matrix.org >__ In summary, moving ahead in all aspects, and progress is going well.     

> __< r​ucknium:monero.social >__ More comments? Other topics?     

> __< r​ucknium:monero.social >__ We can end the meeting here. Thank you all!     

> __< j​effro256:monero.social >__ Thank you everyone! Thanks Aaron Feickert ! Fascinating stuff     


# Action History
- Created by: Rucknium | 2024-04-30T17:26:19+00:00
- Closed at: 2024-05-09T16:46:09+00:00
