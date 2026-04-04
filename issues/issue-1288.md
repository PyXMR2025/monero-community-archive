---
title: Monero Research Lab Meeting - Wed 22 October 2025, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1288
author: Rucknium
assignees: []
labels: []
created_at: '2025-10-28T20:40:36+00:00'
updated_at: '2025-11-04T23:00:38+00:00'
type: issue
status: closed
closed_at: '2025-11-04T23:00:38+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/meeting.html?p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3. Security proofs for Generalized Bulletproofs.

4. [Proof-of-Work-Enabled Relay ("PoWER")](https://github.com/monero-project/research-lab/issues/133).

5. [Transaction volume scaling parameters after FCMP hard fork](https://github.com/ArticMine/Monero-Documents/blob/master/MoneroScaling2025-07.pdf). [Revisit FCMP++ transaction weight function](https://github.com/seraphis-migration/monero/issues/44).

6. [FCMP alpha stressnet](https://monero.town/post/6763165).

7. Mining pool centralization: [Temporary rolling DNS checkpoints](https://github.com/monero-project/monero/issues/10064), [Share or Perish](https://github.com/monero-project/research-lab/issues/146), and [Lucky transactions](https://github.com/monero-project/research-lab/issues/145).

8. Any other business

Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#1281 

# Discussion History
## Rucknium | 2025-10-28T20:41:02+00:00
Logs
> __< jberman >__ rucknium:monero.social available?     

> __< rbrunner >__ I couldn't see the usual "meeting in 1 hour" announcement ...     

> __< jberman >__ Hm, and he didn't make the usual Meeting issue: https://github.com/monero-project/meta/issues     

> __< jberman >__ Hope Ruck is alright     

> __< rbrunner >__ Yeah, pretty unusual     

> __< sgp_ >__ Hopefully they are okay     

> __< jberman >__ rbrunner: do you want to lead a meeting w/same topics from last week?     

> __< kayabanerve:matrix.org >__ 😱     

> __< rbrunner >__ Hmm, maybe you are a better moderator here?     

> __< kayabanerve:matrix.org >__ They did thumbs up my message from a few days ago, IIRC.     

> __< mayhem69:matrix.org >__ I had DMs with them yesterday around this time so I can confirm they were alive then     

> __< kayabanerve:matrix.org >__ Or actively impersonated around then     

> __< kayabanerve:matrix.org >__ Has anyone asked Mr. Plum if they were in the Library last night?     

> __< jberman >__ Sure, I'll moderate     

> __< jberman >__ 1. Greetings     

> __< articmine >__ Hi     

> __< rbrunner >__ Thanks!     

> __< sgp_ >__ hello     

> __< kayabanerve:matrix.org >__ 👋     

> __< rucknium >__ Hi. Sorry I'm late.     

> __< spirobel:kernal.eu >__ hi     

> __< rbrunner >__ Last week's topic list: https://github.com/monero-project/meta/issues/1281     

> __< hinto >__ hello     

> __< kayabanerve:matrix.org >__ Rucknium and/or impersonater!     

> __< rucknium >__ I can PGP sign if you require     

> __< rucknium >__ 2. Updates. What is everyone working on?     

> __< syntheticbird >__ hi     

> __< kayabanerve:matrix.org >__ Returned from a conference, oxide, book, Serai, trying to merge the first FCMP++ lib into oxide and oxide's BBP.     

> __< vtnerd >__ Me: official lws docker builds for stable and master are published and use the ci process. Like to get cosign with static key working eventually. Now doing further testing of subaddresses with carrot, specially incoming only accounts     

> __< jberman >__ me: we released v1.3 of the FCMP++ & Carrot alpha stressnet which included a number of Quality of Life improvements, continuing stressnet debugging / investigating, and close to continuing reviewing p2p ssl (probably continuing in earnest today)     

> __< rucknium >__ me: Increased CPU and RAM efficiency of monerod-monitor http://github.com/rucknium/monerod-monitor , which runs stressnetnode1.moneronet.info . Also wrote local deployment instructions so stressnet node operators can run it with their own node. Node operators can also just collect the performance data in a DB instead of displaying it in charts, too.     

> __< sgp_ >__ cool vtnerd; I'll make sure the truenas app is updated to use your official one. MAGIC had just shy of 2k installs of our unofficial docker image for lws     

> __< kayabanerve:matrix.org >__ FYI, oxide has received 166 reports with 12 paid with some reward (sometimes just a small amount as a tip, not an acknowledged bug with the full kebab) since launching, what, a couple months ago?     

> __< kayabanerve:matrix.org >__ A month and a half ago.     

> __< vtnerd >__ The readme for lws contains url/path info for docker     

> __< articmine >__ I am reviewing the proposed weights based upon roughly total transaction size  and it can be the basis for a solution      

> __< sgp_ >__ 12 interesting reports is pretty good     

> __< kayabanerve:matrix.org >__ 12 reports either valid, or we try to reward anything invalid we still make improvements due to, even if just a basic documentation update.     

> __< syntheticbird >__ how much of the interesting reports were powered by ✨Web 4.0 Quantum AGI ✨     

> __< kayabanerve:matrix.org >__ One noted we allocate and could OOM, and was a bullshit report because of course allocating functions allocate, but we still offered a small amount because I noted that function could be written to not allocate _and_ we could've included a sanity check to prevent allocating more than a few bytes (even though we allocated less memory than given to us as input).     

> __< tevador >__ Me: post-quantum Jamtis, research phase/feasibility study     

> __< kayabanerve:matrix.org >__ syntheticbird:monero.social: what's 166 - 12 or so     

> __< rucknium >__ 3. Security proofs for GBP     

> __< rucknium >__ > Hello, I [ kayabanerve:matrix.org  ] reached out to Cypher Stack to request they review the security proofs for GBPs. While Goodell reviewed Aaron's proofs prior, Aaron updated the protocol to a prior draft due to it being a more efficient variation (a few hundred bytes) at my request. Goodall, while reviewing the proofs, n [... too long, see https://mrelay.p2pool.observer/e/pM-xs8EKVTNZYTFW ]     

> __< kayabanerve:matrix.org >__ My point was it's gotten a lot of attention and has yielded credible improvements. Some of those 154 reports simply weren't valid, but weren't absolute spam, and I look forward to the FCMP++ libraries also being covered as part of ensuring the hard fork's security.     

> __< kayabanerve:matrix.org >__ I don't have more to add other than boog900 reviewed the library, pending its merge into FCMP++, and signed off pending just a few nits. The only blocker is confirmation of the academia.     

> __< sgp_ >__ on topic 3, this is a blocker that stands in the way of other GBP review (likely from zksecurity), so it should be supported and completed asap imo     

> __< kayabanerve:matrix.org >__ jberman:monero.social: Thoughts?     

> __< jberman >__ all sgtm     

> __< sgp_ >__ did CS provide an ETA on delivery for this? is this something that they can work on in the immediate term?     

> __< kayabanerve:matrix.org >__ I think the amount is incredibly low, especially given it directly coves the code     

> __< jberman >__ > <kayabanerve:matrix.org> Hello,I reached out to Cypher Stack to request they review the security proofs for GBPs. While Goodell reviewed Aaron's proofs prior, Aaron updated the protocol to a prior draft due to it being a more efficient variation (a few hundred bytes) at my request.Goodall, while reviewing the proofs, no [... too long, see https://mrelay.p2pool.observer/e/-p3Os8EKUzdIdm5v ]     

> __< jberman >__ This original post got 7 thumbs up, so seems it has good support     

> __< kayabanerve:matrix.org >__ Should only be a week or two, I believe, but I'd have to check     

> __< kayabanerve:matrix.org >__ *the code in relation to the protocol. I don't present it as an audit of the rust     

> __< jberman >__ I guess 1 q, would we maybe want zksecurity to start on divisors sooner and not be blocked?     

> __< kayabanerve:matrix.org >__ I don't think this will take so long to complete it's posited as a blocker     

> __< sgp_ >__ I'll aim to get a combined quote for discussion in time for the meeting of November 5th, ideally covering both scopes. If GBP isn't ready yet, then it may be pushed to the following. If it's any longer than that, then yes I agree it makes sense to take out GBP and start with just divisors     

> __< rucknium >__ Can you explain more what the 0 and 1 indexing issue is about?     

> __< rucknium >__ Juts informational     

> __< rucknium >__ just*     

> __< kayabanerve:matrix.org >__ There's a list of commitments to a polynomial, where the polynomial is indexed from 0.     

> __< rucknium >__ I know what 0 and 1 indexing is, but how does it affect the work here?     

> __< kayabanerve:matrix.org >__ The original BP protocol committed commuting to 0th coefficient because it was 0 and inherent.     

> __< kayabanerve:matrix.org >__ GBP sets it to a non-zero value and must commit to it, communicating and summing the commitment when doing the maths.     

> __< kayabanerve:matrix.org >__ I knew that and explicitly made that change, and immediately answered when Goodell asked about it.     

> __< kayabanerve:matrix.org >__ I just don't know why I knew that, as apparently that wasn't reflected in the formalizations 🤔     

> __< kayabanerve:matrix.org >__ Presumably a DM with Aaron     

> __< kayabanerve:matrix.org >__ It will update the proofs to some degree as this value is communicated now but wasn't prior, and that may not have been accurately reflected?     

> __< kayabanerve:matrix.org >__ But I believe Goodell believes the implemented protocol will work out. This discrepancy just needs to be written out (vastly simplifying, of course)     

> __< rucknium >__ Not the first confusion with 0 and 1 index. And won't be the last (in the world).     

> __< kayabanerve:matrix.org >__ *omitted commuting to the 0th coefficient     

> __< kayabanerve:matrix.org >__ **omitted committing     

> __< kayabanerve:matrix.org >__ I'm so sorry, autocorrect 😅     

> __< kayabanerve:matrix.org >__ Yeah, the formalization just updates communicate 1 to end to 0 to end. The proofs... bla bla bla     

> __< rucknium >__ Is action needed at this meeting, or are you still working out the work scope and quote?     

> __< kayabanerve:matrix.org >__ Approval, it's a request from the research fund was has MRL oversight     

> __< kayabanerve:matrix.org >__ *which has     

> __< rucknium >__ Any more questions from anyone here about the quote and scope of work?     

> __< rucknium >__ Any more discussion or any objections to the quote and scope of work?     

> __< jberman >__ I support     

> __< rbrunner >__ Sound good, yes     

> __< rucknium >__ It sounds good to me.     

> __< rbrunner >__ Such 0-1 stuff can be tricky     

> __< rucknium >__ I see loose consensus in favor of expending 8000 USD equivalent for Cypher Stack's work on security proofs for Generalized Bulletproofs.     

> __< kayabanerve:matrix.org >__ Thank you!     

> __< rucknium >__ 3. Proof-of-Work-Enabled Relay ("PoWER"). https://github.com/monero-project/research-lab/issues/133     

> __< hinto >__ I noted a point from the last meeting: https://github.com/monero-project/research-lab/issues/133#issuecomment-3423958055     

> __< hinto >__ Both boog900:monero.social and jeffro256:monero.social's proposals sound good to me, although they take different tradeoffs (maybe others can weigh in here). I think PoW per connection for P2P/ZMQ and PoW per TX for RPC could be an alternative, other than that I don't have anything else to add.     

> __< kayabanerve:matrix.org >__ rucknium:monero.social: that is #4     

> __< jberman >__ > PoW per connection for P2P/ZMQ and PoW per TX for RPC     

> __< jberman >__ This sounds ok to me. Then in some future optimization, there could be PoW per connection for RPC implemented as well, though probably won't end up worth the hassle     

> __< rucknium >__ kayabanerve:matrix.org: If the agenda items are indexed from 0, then it's item 3 :P     

> __< kayabanerve:matrix.org >__ Except GBPs also had 3 :p     

> __< jberman >__ PoW per tx for RPC shouldn't have the issue of expiring PoW that needs to be updated     

> __< hinto >__ Yup, just a required PoW field added to existing TX relay endpoints     

> __< jberman >__ Could probably just use the most recent block hash too?     

> __< jberman >__ allowing a window of 2 blocks     

> __< rbrunner >__ Almost sounds a little than the "pay with hashes" system of yesteryears, from moneromooo ...     

> __< rbrunner >__ *a little like     

> __< hinto >__ Ok, seems similar to the original proposal, I think we could figure out those details in the PR     

> __< jberman >__ (just to clarify, I meant could use most recent block hash for RPC PoW per tx, but challenge/response still makes sense for p2p connections)     

> __< hinto >__ boog900:monero.social jeffro256:monero.social: if there are no objections then I'll be starting the implementation assuming PoW per TX for RPC     

> __< jeffro256 >__ Sounds good to me      

> __< articmine >__ Sounds fine to me      

> __< rucknium >__ 5. Transaction volume scaling parameters after FCMP hard fork. Revisit FCMP++ transaction weight function. https://github.com/ArticMine/Monero-Documents/blob/master/MoneroScaling2025-07.pdf  https://github.com/seraphis-migration/monero/issues/44     

> __< jberman >__ I think makes sense to continue to next topic while we wait to hear from boog on above^ thank you for pushing this forward hinto :)     

> __< jberman >__ nice     

> __< jberman >__ Repeating from an earlier message:     

> __< jberman >__ Here is a simple proposal to make tx weight roughly equal to byte size with justification: https://github.com/seraphis-migration/monero/issues/44#issuecomment-3423391977     

> __< jberman >__ Of note, you can still calculate tx weight in an offline context with just n inputs, n outputs, and extra length.     

> __< jberman >__ Considering the ongoing difficulty to reach rough consensus on the FCMP++ tx weight calculation, I figure this would be a simple solution that has the smallest surface for disagreement. Imo it's easiest to justify     

> __< articmine >__ I believe that this is a viable approach. We are setting fixed weights for the whole transaction except for TX extre     

> __< articmine >__ Extra     

> __< jeffro256 >__ Tx extra should be included in the byte size / weight calculation AFAIK      

> __< jeffro256 >__ There would be 3 paramaters to weight calculation: # ins, # outs, # extra bytes     

> __< articmine >__ Of course, but not in the fixed weight     

> __< jeffro256 >__ What do you mean by "fixed weight"?     

> __< articmine >__ Extra bytes being TX extrea     

> __< jberman >__ kayabanerve:monero.social: you may have thoughts on calculating weight roughly equal to byte size, but with constant 8 bytes for the fee, and constant 7 layers assumed in the tree to allow calculating weight from # ins, # outs, # extra bytes     

> __< jberman >__ (meant to tag kayabanerve:matrix.org )     

> __< articmine >__ The one concern I have heard here is people stuffing data into various parts of the TX     

> __< jeffro256 >__ With the current consensus rules, AFAICT, you can't really add any extra data into a transaction outside of the tx_extra field and have the transaction still verify      

> __< articmine >__ Then this should be fine.      

> __< articmine >__ As for the fixed 7 layers that is a must for scaling      

> __< articmine >__ Are there any objections to this approach      

> __< jeffro256 >__ I support weight appriox eq to byte size approach      

> __< spirobel:kernal.eu >__ +1      

> __< spirobel:kernal.eu >__ kiss      

> __< spirobel:kernal.eu >__ this is a much better approach. The complexity seemed to get out of hand before      

> __< kayabanerve:matrix.org >__ I explicitly don't as it encourages large-input TXs, they aren't even equally considered.     

> __< kayabanerve:matrix.org >__ But I agree it should be a formula solely derivative of inputs, outputs, and extra length.     

> __< articmine >__ kayabanerve:matrix.org: My take is that the quadratic penalty will penalize large transactions at node relay.     

> __< kayabanerve:matrix.org >__ Sorry, which quadratic penalty is this?     

> __< kayabanerve:matrix.org >__ I stepped away for a moment and only returned to the proposition roughly equal to byte size.     

> __< articmine >__ Block weight scalung     

> __< kayabanerve:matrix.org >__ That seems indirectly relevant to the TX fees users pay at best      

> __< articmine >__ Penalty to increase the block weight above the short term median      

> __< kayabanerve:matrix.org >__ I'd support a flat cost for the next power of two for inputs, outputs, before corresponding to bytes fwiw     

> __< jberman >__ What do you mean they aren't equally considered? > <kayabanerve:matrix.org> I explicitly don't as it encourages large-input TXs, they aren't even equally considered.     

> __< articmine >__ kayabanerve:matrix.org: I am actually supported of that     

> __< articmine >__ It is easy to implement      

> __< kayabanerve:matrix.org >__ jberman: One 128-byte transaction is what, 10x cheaper 64 2-input TXs?     

> __< kayabanerve:matrix.org >__ *one 128-inout transaction     

> __< kayabanerve:matrix.org >__ *cheaper than     

> __< kayabanerve:matrix.org >__ Sorry, I'm a bit distracted by a saucepan boiling over right now...     

> __< rbrunner >__ Put a range proof on it     

> __< articmine >__ I do not see how > <kayabanerve:matrix.org> jberman: One 128-byte transaction is what, 10x cheaper 64 2-input TXs?     

> __< rbrunner >__ Simply by being 10 times less bytes, presumably?     

> __< jberman >__ 64-2 is 78132 bytes, 128-2 is 150133 bytes. 2x 64-2 = 156624     

> __< kayabanerve:matrix.org >__ jberman:monero.social: 64x2 though     

> __< jberman >__ oh misread     

> __< kayabanerve:matrix.org >__ Isn't it ~500k bytes, so that case, 3x 128-inputs, despite having significantly better computational performance?     

> __< rucknium >__ IMHO, the encouragement of large-input txs won't affect behavior much for anyone except p2pool miners. Solution: transparent consolidation for coinbase tx. Save a lot of fees.     

> __< jberman >__ ya ~500k bytes for 64x 2-in/2-out, versus ~150k bytes for 128-in/2-out      

> __< kayabanerve:matrix.org >__ I don't like that :C     

> __< kayabanerve:matrix.org >__ You can introduce a log2(i) scaling factor so 128 has a 7x though, while 2-in is 1x     

> __< jberman >__ That creates 126 more outputs that are going to be spent in FCMP++ proofs...     

> __< rbrunner >__ Even if taking PoWER into account?     

> __< kayabanerve:matrix.org >__ And those 126 outputs are reflective of ~300 FCMP inputs? Because that how it corresponds to 128-2     

> __< kayabanerve:matrix.org >__ *ceil(log2(i))     

> __< jberman >__ I don't follow     

> __< kayabanerve:matrix.org >__ You noted 126 more outputs, for a difference in weight of 350kb.     

> __< articmine >__ kayabanerve:matrix.org: So if I understand this correctly you would want the 128-2; to pay a higher fee     

> __< kayabanerve:matrix.org >__ In those 350kb, I could fit 2.33x 128-2 TXs.     

> __< kayabanerve:matrix.org >__ That's approximately 300-5 being treated equivalent to 0-126 w.r.t. weight     

> __< articmine >__ Enforcement of the scaling requirements at node relay, my original proposal would take care of that     

> __< jberman >__ Ok I see your point. Trying to identify a path to rough consensus here     

> __< kayabanerve:matrix.org >__ Linear cost to inputs, outputs, or scaling factor of ceil(log2(i))?     

> __< articmine >__ Just use the quadratic penalty formula for scaling and fees. No need to change the weights      

> __< articmine >__ We can keep the linear weight approach and be stricter on node relay     

> __< articmine >__ Which by the way prevents uneconomic transactions to mine as spam     

> __< spirobel:kernal.eu >__ the goal is to disincentivize spam. How much would a high input transaction currently cost? is it really 10x cheaper after adding in the quadratic penalty?  > <kayabanerve:matrix.org> jberman: One 128-byte transaction is what, 10x cheaper 64 2-input TXs?     

> __< articmine >__ Not at all      

> __< kayabanerve:matrix.org >__ I'm concerned about annoying users, not malicious miners, primarily     

> __< kayabanerve:matrix.org >__ Users who create large-input transactions create annoying transactions and are annoying users     

> __< kayabanerve:matrix.org >__ jberman:monero.social: Can you achieve consensus if you ignore me, or do you agree I raised a valid criticism?     

> __< kayabanerve:matrix.org >__ I get I'm in a minority here and don't intend to be a blocker     

> __< articmine >__ kayabanerve:matrix.org: I am not so sure     

> __< spirobel:kernal.eu >__ kayabanerve:matrix.org: maybe the quadratic penality is also over complex. we could add a tx size limit that is reasonable and then just make a fee per inputs and outputs      

> __< articmine >__ spirobel:kernal.eu: It is not     

> __< articmine >__ It actually solves a concern without adding complexity      

> __< jberman >__ "Can you achieve consensus if you ignore me" -> I think probably. "do you agree I raised a valid criticism?" -> I think there's pros/cons to every approach. I think simple on this front is nice and has major pros (e.g. while yes, you can create more high input txs instead of creating many low input txs, this does also mean you're creating fewer outputs which will then go on chain with more proofs)     

> __< articmine >__ jberman: Actually using your proposal works for the issue that was raised     

> __< articmine >__ We simply enforce the scaling requirements on large transactions      

> __< jeffro256 >__ kayabanerve:matrix.org: I think you raise a valid criticism, but I'm not very worried about people creating compact, if heavy to verify, valid high-input TXs, as long as they are correctly subsidizing their marginal cost to block emission by being included in a block      

> __< jeffro256 >__ We pay FCMP CPU cost 1 time (0 if checkpointed), but pay cost of storage in perpetuity      

> __< articmine >__ jeffro256: At the point of the scaling penalty or before reaching the penalty?     

> __< articmine >__ There is a big difference      

> __< articmine >__ Or we compromise somewhere in between      

> __< jeffro256 >__ IMO There should be a minimal fee for spam prevention even when no penalty is applied, but a transaction should also pay for its marginal cost when the penalty is applied      

> __< jeffro256 >__ The minimal fee should factor in what the penalty would be if this transaction were to be included     

> __< articmine >__ This is what we have      

> __< articmine >__ The point of disagreement is on what size of the transaction are we enforcing this     

> __< articmine >__ 1 in 2 out or 128 in 16 out?     

> __< articmine >__ It is not the same fee per byte.     

> __< tevador >__ The fee rate is calculated from a reference size. If we calculate the scaling fee from the actual size, then a 150 KB transaction would need to pay 1/4 of the block reward in fees.     

> __< articmine >__ correct      

> __< rucknium >__ Ready to discuss stressnet?     

> __< jeffro256 >__ IMO We should enforce it for whatever weight a transaction is, there shouldn't be a "reference tx size". We should take expected sum total tx size in next block (including this tx) -> calculate penalty -> amortize fee across that set of txs      

> __< articmine >__ ... but if people are concerned about the large transactions we can take a portion of the extra and enforce that     

> __< articmine >__ jeffro256: This does not work because of the game theory     

> __< articmine >__ Between the miner and the user     

> __< jeffro256 >__ Why would a miner not want to increase their net reward?     

> __< jeffro256 >__ If my fee for my tx is greater than its marginal cost, a rational miner would include it, no?     

> __< articmine >__ The miner included the highest paying transactions first before reaching the penalty      

> __< jeffro256 >__ Yes, I'm talking about minimum fees     

> __< articmine >__ So there is always a profit for the miner over the penalty      

> __< articmine >__ The minimum fees are based on the reference transaction size currently 3000 bytes      

> __< articmine >__ For FCMP++ proposal is 10000 bytes      

> __< articmine >__ Just larger than 2 in 2 out      

> __< tevador >__ It depends if we want to discourage 150 KB transactions. Nobody will pay a 0.15 XMR fee for it. It will be much cheaper to submit 64 2/2 transactions.     

> __< articmine >__ There is an in-between      

> __< jeffro256 >__ Right, I'm saying that the minimum fee shouldn't be based on a reference transaction size when the size of an FCMP++ transaction can vary wildly. Actually calculating expected marginal penalty loss will give you a closer estimate to the tipping point where a miner will include a transaction in a block over A) assuming small re [... too long, see https://mrelay.p2pool.observer/e/gpKStsEKSXM5X2VO ]     

> __< articmine >__ So you are now saying that the minimum fee per byte for a transaction should depend on the transaction weight?     

> __< articmine >__ I have to leave in 4 minutes      

> __< articmine >__ We can discuss this after the meeting      

> __< jeffro256 >__ articmine: Ideally, yes, as it gives the closest approximation to whether a miner will include it or not.      

> __< jeffro256 >__ Fair enough, we can move to the next item.     

> __< DataHoarder >__ (late and out of order) hi, implemented carrot/FCMP++ partial view-only functions and wallet for both legacy and new wallets on go p2pool code; plus confirmed a few parts of how it's preferable to work under p2pool after network upgrade; nothing else to add besides:     

> __< DataHoarder >__ adding the regular reminder that P2Pool sweeps can be 100+ inputs for aggregate value of ~0.04 XMR total like on https://mini.p2pool.observer/transaction-lookup?txid=a41077d3af644a2690a58888516e9abdcc62bcc8351a96a035263a9bff69e903 so if fees are going to be this big, maybe https://github.com/monero-project/research-lab/issues/108 can be discussed     

> __< DataHoarder >__ at a later point     

> __< rucknium >__ 6. Stressnet     

> __< DataHoarder >__ I upgraded to v1.2 and it kept 12-9 peers all the time, before it was at most 3 if not disconnected. Running v1.3 now and looks happy     

> __< jeffro256 >__ Has anyone else observed any differences, positive or negative, with v1.3?     

> __< DataHoarder >__ it has not OOM'd recently, neither did v1.2. I will test some p2pool mining with it to see if it improved submit_block -> ZMQ mining data wise     

> __< jberman >__ Overall status report on stressnet: it's progressing well. We've identified and fixed some FCMP++ & Carrot integration bugs in every release, we've identified and fixed monerod issues in every release, and we've made improvements both to existing monerod/wallet code and to the integration in every release     

> __< jberman >__ Actually all the integration bug fixes have been FCMP++ integration related, not Carrot     

> __< rucknium >__ Any specific requests to stressnet node operators? tx volume has been low. Do you want it increased again?     

> __< jberman >__ Update to v1.3 first and foremost. And then perhaps wait 24 hours for others to update too, and start ramping up the stress again     

> __< jberman >__ v1.3 (and v1.2) patched and improved some connectivity issues, so it will be good to observe how nodes hold up with those changes     

> __< jberman >__ tx relay v2 + avoiding re-validating txs will be the next major improvements that should result in much smoother operation under stress as well     

> __< jberman >__ I think once we have no more observed integration bugs (maybe for a week?), and we see smooth perf with 300mb pool and 5mb blocks, we can move toward beta stressnet. But for now we're making progress with alpha and can continue with what we're doing     

> __< rucknium >__ Congrats all around!     

> __< rucknium >__ Anything more on stressnet?     

> __< jberman >__ nothing from me     

> __< jberman >__ a big thank you to participants :)     

> __< rucknium >__ 7. Mining pool centralization: Temporary rolling DNS checkpoints, Share or Perish, and Lucky transactions.     

> __< jberman >__ Share or Perish still seems the most promising solution to me and definitely worthy of continued research     

> __< tevador >__ Any updates about checkpoints?     

> __< DataHoarder >__ work is still blocked on the monero bug     

> __< DataHoarder >__ I haven't seen any updates on this since last week     

> __< tevador >__ Any qubic news?     

> __< DataHoarder >__ Not much from them since last week, quiet on that front, not selfish mining. they sit at 1.3-1GH/s     

> __< DataHoarder >__ some of their code is affected by the FourQ Circle library CVE due to lack of full verification of points on decoding     

> __< rucknium >__ We can end the meeting here. Thanks everyone.     

> __< syntheticbird >__ thanks     

> __< spirobel:kernal.eu >__ tevador: it seems like no one is responsible      

> __< spirobel:kernal.eu >__ I asked the last time and there was no answer      

> __< spirobel:kernal.eu >__ about fixing the logic issue with the checkpointing rule     

> __< spirobel:kernal.eu >__ vs longest chain rule      

> __< spirobel:kernal.eu >__ maybe that is something that kayabanerve:matrix.org  could be interested in as it directly affects the code path that the finality layer would touch     

> __< spirobel:kernal.eu >__ here is the related issue https://github.com/monero-project/monero/pull/10075      

> __< spirobel:kernal.eu >__ maybe we can still add this to the meeting notes rucknium:monero.social so it does not get lost. it seems like it is an important topic. I am wondering why there is not more focus on this. I added some of the MRL conversation chat log from earlier to the end of the issue.     

> __< jberman >__ I'm personally not interested in focusing on or prioritizing centralized solutions     

> __< boog900 >__ hinto: Yeah sounds good to me     

> __< boog900 >__ Might be good to include something specific to the node so you can't reuse PoW across multiple nodes RPC      

> __< boog900 >__ Like the nodes address or something      

> __< kayabanerve:matrix.org >__ Except I have no interest in writing C++ as I haven't for more than ~1 month in total over the past 8 years.     

> __< jeffro256 >__ C++ is so invigorating. Don't you love analyzing each mission-critical line for UB?     

> __< kayabanerve:matrix.org >__ I spent a few years with Nim, which in hindsight was likely largely wasted.     

> __< kayabanerve:matrix.org >__ Today, and for the past ~4 years, I've preferred Rust for the exceptionally strong type system which attempts to minimize UB.     

> __< preland >__ jeffro256: I like c++, but only when I don’t have to worry about my code actually mattering     

> __< kayabanerve:matrix.org >__ In a parallel timeline, I only write Haskell and Ada however.     

> __< kayabanerve:matrix.org >__ In another, Erlang     

> __< articmine >__ This is actually also my preference since it avoids certain spam attacks based upon un economical for the miner transactions . We have to keep in mind that because of the discrete fee levels currently 4 this has to apply on for ranges of transactions. > <jeffro256> Ideally, yes, as it gives the closest approximation to whether a miner will include it or not.      

> __< articmine >__ The current approach has been to do this only for the most common transactions and "fly by the seat of our pants" for the large edge case.     

> __< articmine >__ For a minimum penalty free zone ZM of 1000009 bytes, and a 1% scaling rate this means 10000 bytes, the reference transaction size.      

> __< articmine >__ 10000 bytes.      

> __< articmine >__ We can raise fees and increase the economic scaling level to 2% or 20000 bytes, which I am likely to recommend since I believe that this will attract consensus. This will take care of up to 8 inputs with the weight approximately following the size which seems to have at least loose  consensus.     

> __< articmine >__ At this point we move the conversation to node relay with:     

> __< articmine >__ 1) Do nothing and "fly by the seat of our pants", the current approach      

> __< articmine >__ 2) Enforce economic scaling with various levels of minimum node relay fees depending on the transaction weight range.[... more lines follow, see https://mrelay.p2pool.observer/e/2peSusEKMnpweUMz ]     

> __< articmine >__ Personally I am neutral to leaning against the large input transactions, but I will support where the consensus ends up.     

> __< jberman >__ tevador boog900:monero.social do either of you guys have thoughts on the proposal to use approximate byte size as tx weight?     

> __< boog900 >__ nope, I haven't really thought about fees at all       

> __< boog900 >__ beyond thinking current fees are too low, although ig that is a different topic to tx weights      



# Action History
- Created by: Rucknium | 2025-10-28T20:40:36+00:00
- Closed at: 2025-11-04T23:00:38+00:00
