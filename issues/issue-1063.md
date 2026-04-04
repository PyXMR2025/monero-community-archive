---
title: Monero Research Lab Meeting - Wed 28 August 2024, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1063
author: Rucknium
assignees: []
labels: []
created_at: '2024-08-26T20:27:21+00:00'
updated_at: '2024-09-06T19:42:57+00:00'
type: issue
status: closed
closed_at: '2024-09-06T19:42:56+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

[Join the Monero Matrix server if you don't already have a Matrix account.](https://web.archive.org/web/20230128130949/https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211027T170000&p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3. [Stress testing `monerod`](https://github.com/monero-project/monero/issues/9348)

4. Research [Pre-Seraphis Full-Chain Membership Proofs](https://www.getmonero.org/2024/04/27/fcmps.html).

5. [Change how transactions are broadcasted to significantly reduce P2P bandwidth usage](https://github.com/monero-project/monero/issues/9334).

6. Any other business

7. Confirm next meeting agenda


Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#1061 

# Discussion History
## Rucknium | 2024-09-03T20:39:12+00:00
Logs

> __< r​ucknium:monero.social >__ Meeting time! https://github.com/monero-project/meta/issues/1063     

> __< j​effro256:monero.social >__ howdy     

> __< r​ucknium:monero.social >__ 1) Greetings     

> __< x​mrack:monero.social >__ Hey 👋🏽   

> __< b​oog900:monero.social >__ Hi     

> __< rbrunner >__ Hello     

> __< v​tnerd:monero.social >__ Hi     

> __< o​ne-horse-wagon:monero.social >__ Hello.     

> __< a​rticmine:monero.social >__ Hi     

> __< j​berman:monero.social >__ *waves*     

> __< r​ucknium:monero.social >__ 2) Updates. What is everyone working on?     

> __< k​ayabanerve:matrix.org >__ 👋     

> __< k​ayabanerve:matrix.org >__ I spent a few hours drafting feedback on Carrot. Still trying to wrangle review.     

> __< r​ucknium:monero.social >__ Me: Wrote a comment on possible risks of current txpool queries and the new proposed transaction propagation methods: "[Proposal] Change how transactions are broadcasted to significantly reduce P2P bandwidth usage" : https://github.com/monero-project/monero/issues/9334#issuecomment-2307824031     

> __< j​effro256:monero.social >__ Starting to get review quotes back from auditors regarding Carrot     

> __< j​berman:monero.social >__ me: continuing fcmp integration, next task is addressing init pr comments and trimming the tree on reorgs / pop blocks     

> __< j​effro256:monero.social >__ And writing in feedback from kayabanerve     

> __< r​ucknium:monero.social >__ 3) Stress testing monerod https://github.com/monero-project/monero/issues/9348     

> __< r​ucknium:monero.social >__ 0xfffc made some edits to the dynamic block-size-sync PR: https://github.com/spackle-xmr/monero/pull/26     

> __< x​mrack:monero.social >__ I tasked myself with writing more fuzzing targets to get better coverage. The current ones for oss-fuzz I believe were written a long time ago. Let me know If anyone has experience working with AFL++ and would like to help.     

> __< r​ucknium:monero.social >__ I think that's all for stressnet.     

> __< 0​xfffc:monero.social >__ Thanks for mentioning it. My apologies for being absent from meeting. ( I am on road ). This PR is updated, there will be one or two other separated PRs related to  this fix. Fixing issues that we found during implementing this.     

> __< r​ucknium:monero.social >__ 4) Research Pre-Seraphis Full-Chain Membership Proofs  https://www.getmonero.org/2024/04/27/fcmps.html     

> __< k​ayabanerve:matrix.org >__ I don't have much to say on FCMP++s today and will defer to jberman for any integration news.     

> __< k​ayabanerve:matrix.org >__ I will bring up Carrot. I spent a few hours with jeffro256 going over the documentation, with regards to its definitions, accuracy, layout, etc. While I haven't completely finished my review, and there's still a topic to discuss on the Generate Address tier, I did suggest and strongly endorse changes regarding key derivation.     

> __< k​ayabanerve:matrix.org >__ The current version doesn't solve the burning bug without an additional consensus rule. While minor and likely fine, I don't support such consensus rules due to their unforeseeable implications on collaborative transactions (a niche use-case yet one which may become more relevant with L2 discussions).     

> __< j​effro256:monero.social >__ Do you want to lay out the details here? I'd be happy to open the floor on this issue     

> __< k​ayabanerve:matrix.org >__ We did successfully propose a scheme which didn't require a consensus rule while maintaining the same goals however.     

> __< j​effro256:monero.social >__ If that's okay with everyone     

> __< k​ayabanerve:matrix.org >__ I'll also note there wasn't enough entropy in the scheme, opening a multi-target attack under specific circumstances, yet jeffro256 proposed a solution without increasing the entropy/transaction size so thankfully no performance penalty there.     

> __< k​ayabanerve:matrix.org >__ I don't personally have a need to be specific. That's my high-level overview of the fixes we worked on. The new schemes seem unequivocally better by my view? I don't believe I'm censoring any downsides, even inadvertently?     

> __< k​ayabanerve:matrix.org >__ So while we can be specific, if everyone is fine with hearing "identified issues resolved", we can move on :p     

> __< rbrunner >__ Well, there will be reviews and reviewers to hopefully catch anything left.     

> __< j​effro256:monero.social >__ Yeah, I guess the only real downside is that collaborative transactions might stick out on the chain due to duplicated output pubkeys, commitments, etc     

> __< k​ayabanerve:matrix.org >__ Malicious signers can always make their TXs stick out.     

> __< j​effro256:monero.social >__ True. So yeah it's not a huge deal and might not be worth going into here     

> __< j​effro256:monero.social >__ Smart collaborative protocols are always free to add additional rounds/rules to their participants if they want to prevent this fingerprint     

> __< k​ayabanerve:matrix.org >__ The existing protocol had a DoS which would require a commit-reveal scheme to avoid. Removing the consensus rule enables saving a round of complexity in theoretical collaborative protocols.     

> __< k​ayabanerve:matrix.org >__ This specific fingerprint, of which there are still several others to cause non-uniformity :p     

> __< k​ayabanerve:matrix.org >__ TXs will always only be as private as to those who know about them. The fact in a collaborative TX, someone else knows about it and can point it out, is unavoidable.     

> __< rbrunner >__ It will take a while until we get to implement any such collaborative scheme, I guess?     

> __< rbrunner >__ Much other stuff ahead on the way there     

> __< k​ayabanerve:matrix.org >__ Oh, yes, we're not doing that.     

> __< k​ayabanerve:matrix.org >__ I just noted there would be a problem if someone tried and we don't have to have that problem.     

> __< k​ayabanerve:matrix.org >__ Making it easier to try doesn't mean we are trying.     

> __< rbrunner >__ I certainly see the worth of the approach to try to see far into the future with fundamental protocol decisions.     

> __< k​ayabanerve:matrix.org >__ Considering we resolved it without penalty (opening fingerprintable behavior when we already fundamentally have that, so another flavor isn't impactful), I support the changes I proposed.     

> __< rbrunner >__ I already see people fret "Buuuuut ... is it quantum proof" :)     

> __< j​effro256:monero.social >__ The other big point was the different key exchange. To do it efficiently, we will need a Curve25519 library with full scalar multiplication, distinct from mx25519 (unless that lib was updated to support that functionality)     

> __< j​effro256:monero.social >__ So that adds tech debt, but at least it's optional tech debt. You can use the ed25519 scalar-point multiplication and then convert the y coordinate at the end     

> __< k​ayabanerve:matrix.org >__ Oh yes. The proposed key exchange was pointlessly complex in theory and would slow down scanning by multiple percent.     

> __< k​ayabanerve:matrix.org >__ The practical reason for it is to avoid this extra library. We should be able to use most of an x25519 library to avoid the "new code" being notable, or we can implement the optimal theoretic key exchange in an even-slower-than-prior-theoretic practical manner.     

> __< k​ayabanerve:matrix.org >__ The prior key exchange mapped from Curve25519 to Ed25519. cc jberman on how much mapping between curves harms performance due to the performance costs of the inversion.     

> __< rbrunner >__ Is anything of this possibly relevant for the implementation of atomic swaps post-Carrot-introdution?     

> __< rbrunner >__ *introduction     

> __< rbrunner >__ Forgive if the question is not even wrong :)     

> __< k​ayabanerve:matrix.org >__ Not any more than usual.     

> __< rbrunner >__ Ok     

> __< j​effro256:monero.social >__ Also kayabanerve proposed removing the cofactor clearing multiplication by 8, which we do for the current key exchange. I can't see a problem with this on first glance since if the counterparty's pubkey is in the prime subgroup, multiplying by 8 does not yield a more "unique" result. However, I would like vtnerd's opinion on this since he worked on the fast scalar-point multiplic<clipped messag     

> __< j​effro256:monero.social >__ ation code used in wallet2     

> __< j​effro256:monero.social >__ *is *not* in the prime subgroup     

> __< rbrunner >__ I don't understand much of that, but I believe to remember that this was also discussed with UkoeHB at least once. Don't remember the outcome.     

> __< r​ucknium:monero.social >__ We have 15 minutes left in the hour. Let's more onto a new topic:     

> __< r​ucknium:monero.social >__ 5) Change how transactions are broadcasted to significantly reduce P2P bandwidth usage https://github.com/monero-project/monero/issues/9334     

> __< b​oog900:monero.social >__ I added a comment in response to Rucknium https://github.com/monero-project/monero/issues/9334#issuecomment-2315416552     

> __< r​ucknium:monero.social >__ Monero's current tx relay protocol is very wasteful with bandwidth. There could be a protocol that provides a good balance of bandwidth, propagation speed, privacy, and reliability.     

> __< UkoeHB >__ jeffro256: https://raw.githubusercontent.com/UkoeHB/Seraphis/master/implementing_seraphis/Impl-Seraphis-0-0-4.pdf footnote 11     

> __< r​ucknium:monero.social >__ boog900: I agree that the attacks using txpool queries would be expensive for an adversary. Yet, Dandelion++ is designed to improve privacy over bitcoin diffusion when the adversary is wealthy.     

> __< a​rticmine:monero.social >__ My question here is how many times is a full node broadcasting the same tx including as part of a mined node.     

> __< r​ucknium:monero.social >__ Anyway, I am not necessarily opposed to boog900 's proposal unchanged. I wanted to investigate the possible risks and take a long-term view.     

> __< r​ucknium:monero.social >__ I wonder "Where are we going?" with the tx relay protocol.     

> __< v​tnerd:monero.social >__ jeffro256: I can see the argument for removing it. If a subgroup pubkey was provided, the result is going to limited anyway     

> __< a​rticmine:monero.social >__ Can we get this excess bandwidth to ideally between 1x and 2x  the Tx size?     

> __< r​ucknium:monero.social >__ There are stacks of papers on gossip protocols.     

> __< b​oog900:monero.social >__ FWIW I would be for adding similar rate limits to what Bit coin does:     

> __< b​oog900:monero.social >__ > Bitcoin will only send 1 request for a tx every 60 seconds: https://github.com/bitcoin/bitcoin/blob/2c7a4231db35060fa1ab66d29e8139f04edc85a4/src/net_processing.cpp#L104 Although this attack would still be possible with RequestTxPoolTxs unless we limited that message as well. A simple way would just be to not allow more requests than TxPoolInvs that we have sent to that node.     

> __< r​ucknium:monero.social >__ ArticMine: Newer proposals Strokkur and Shrec are supposed to get in that 1-2x range. They are newer than Erlay.     

> __< a​rticmine:monero.social >__ That is close to the theoretical optimal     

> __< r​ucknium:monero.social >__ boog900: The method to get the missing txs when a node gets a fluffy block: Does a node check that the list is from an actual fluffy block, or does it respond to any list of txs? If the former, then the txs would have likely already propagated through the network because they were in a mined block.     

> __< a​rticmine:monero.social >__ Where does Early come in and where are we now?     

> __< a​rticmine:monero.social >__ This is critical for scaling.     

> __< b​oog900:monero.social >__ The node does not do PoW checks before sending the missing tx request     

> __< b​oog900:monero.social >__ erlay reduces the amount of tx-hash broadcasts needed, IMO erlay would not be as beneficial to us as our txs are much larger than Bitcoin's     

> __< r​ucknium:monero.social >__ boog900's proposal could be a stepping stone toward Erlay. In current bitcoin core, there is the check to see if the "receiving" node already has the tx. That method is assumed to exist in the Erlay proposal. Erlay also has a set reconciliation method that is not in boog900 's proposal.     

> __< r​ucknium:monero.social >__ Basically Monero is much more wasteful than even current-day bitcoin     

> __< b​oog900:monero.social >__ With FCMP++ this gap would widen as well     

> __< a​rticmine:monero.social >__ Yes but not by much     

> __< r​ucknium:monero.social >__ Right. The ratio of tx hash to the full tx data is much smaller in Monero than bitcoin     

> __< j​effro256:monero.social >__ UkoeHB: thanks for the link!     

> __< b​oog900:monero.social >__ so the amount of data we could save in P2P broadcasts compared to the amount used would be significantly less than Bitcoin     

> __< b​oog900:monero.social >__ double?     

> __< a​rticmine:monero.social >__ The figures I have heard are 3-4kB     

> __< r​ucknium:monero.social >__ The set reconciliation method of Erlay has quadratic time complexity in the number of txs that each node is missing.     

> __< a​rticmine:monero.social >__ So yes about double     

> __< r​ucknium:monero.social >__ For BTC-level tx volume, that is ok, but the Shrec paper did some experiments and found that 800 tx/sec volume would occupy four CPU threads just with the set reconciliations.     

> __< a​rticmine:monero.social >__ My concern is minimizing the number of the tx is transferred as opposed to tx hashes     

> __< r​ucknium:monero.social >__ Possible alternative set reconciliation methods with different-order time complexities are evaluated in Boskov, N., Trachtenberg, A., & Starobinski, D. (2022). "GenSync: A New Framework for Benchmarking and Optimizing Reconciliation of Data."     

> __< b​oog900:monero.social >__ we should be close to optimal just looking at full tx blob transfers with the new method, I think     

> __< a​rticmine:monero.social >__ You mean under 2x including the mined blocks     

> __< b​oog900:monero.social >__ I think so yes     

> __< b​oog900:monero.social >__ We should probably look into what's eating the rest of our bandwidth as it seems pretty high     

> __< b​oog900:monero.social >__ roughly 38MB in 2.5 hours excluding tx messages     

> __< a​rticmine:monero.social >__ Yes that would be very helpful     

> __< b​oog900:monero.social >__ with 12 connections     

> __< a​rticmine:monero.social >__ Is that excess bandwidth tx dependent?     

> __< b​oog900:monero.social >__ with the new method tx broadcasts including hashes and blobs would have used ~15 MB     

> __< b​oog900:monero.social >__ It includes block broadcasts and everything except tx-pool broadcasts     

> __< a​rticmine:monero.social >__ Yes block broadcasting is another issue. Are we broadcasting the whole block or just the tx hashes to reassemble the block from the tx pool     

> __< k​ayabanerve:monero.social >__ UkoeHB's comment is correct in what was my failure to consider. Apologies. You can so probe the last three bits. cc jeffro256 vtnerd     

> __< b​oog900:monero.social >__ just tx hashes although the miner tx is always included     

> __< b​oog900:monero.social >__ and the block is sent to every node, even if they have already sent it     

> __< j​effro256:monero.social >__ This attack mentioned in the Seraphis impl footnote is mitigated by checking the ephemeral pubkey is in the prime subgroup, yeah? Normally this would be too slow to consider, but if you do it after a view tag check, then you only do the check rarely or in the malicious case     

> __< r​ucknium:monero.social >__ Nodes consume GB of RAM when relaying KB of txs. Do we know why?     

> __< r​ucknium:monero.social >__ The relative scale doesn't make sense to me     

> __< b​oog900:monero.social >__ duplicating txs in the fluff queue is my guess     

> __< r​ucknium:monero.social >__ Say that there are five 100-KB transactions in 100 fluff queues. That's 50MB.     

> __< j​effro256:monero.social >__ IIRC, unexpanded `cryptonote::transaction`s requires at least `5 + m` allocations where `m` is the number of inputs. Then that class is copied into `p` peer fluff queues for a total of `p (5 + m)` memory allocations during relaying (as a lower bound). That's not counting all the allocations during {de}serialization and any reallocations of containers during processing     

> __< b​oog900:monero.social >__ we weren't talking about 5 txs during the spam though     

> __< r​ucknium:monero.social >__ That's about how long the queues are going to last, right?     

> __< b​oog900:monero.social >__ if a lot of re-broadcasts line up the queue could get _a lot_ longer     

> __< b​oog900:monero.social >__ the queue is made of tx-blobs right?     

> __< j​effro256:monero.social >__ Oh you're right, nvm my comment if so     

> __< b​oog900:monero.social >__ re-broadcasts happen after 5 mins then 10, then 15 increasing the wait by 5 mins each time upto 4 hours where it is capped     

> __< b​oog900:monero.social >__ and they only happen when the function is called not exactly at the time the tx should be re-broadcasted     

> __< r​ucknium:monero.social >__ This is the first time I'm hearing about re-broadcasts 👀. So if the txpool is congested, the re-broadcasts would multiply.     

> __< b​oog900:monero.social >__ which I found to be every 2 mins IIRC     

> __< b​oog900:monero.social >__ using my PoC     

> __< b​oog900:monero.social >__ https://github.com/monero-project/monero/issues/9348#issuecomment-2170629015     

> __< b​oog900:monero.social >__ and the logs from monerod     

> __< r​ucknium:monero.social >__ The re-broadcast is just to provide even more reliability of tx propagation. Or something else?     

> __< b​oog900:monero.social >__ yeah that, if we had no connections we would need the tx to be broadcasted again     

> __< r​ucknium:monero.social >__ That would help explain why performance is much worse when the txpool is congested     

> __< r​ucknium:monero.social >__ Wait, is re-broadcast part of routine operation or just under special circumstances?     

> __< b​oog900:monero.social >__ routine     

> __< b​oog900:monero.social >__ only based on time IIRC     

> __< r​ucknium:monero.social >__ We are 30 minutes into the next hour. Maybe continue the conversation next meeting? Or is there enough info to say that the methods should be implemented as-is?     

> __< b​oog900:monero.social >__ I think work can begin on the new protocol, but I am biased :)     

> __< r​ucknium:monero.social >__ I would say leave some room for noise to be injected into the timings, to avoid spaghetti code later, but there are already some methods that allow txpool querying that could/should be modified. 🤔 The risk of an adversary inferring network topology increases with tx volume.     

> __< o​frnxmr:monero.social >__ i thought this was implemented because of tx that _failed_ to broadcast     

> __< o​frnxmr:monero.social >__ Sounds like a bug if its rebroadcasting tx that did not fail     

> __< a​rticmine:monero.social >__ Does this assume no increase in network size?     

> __< r​ucknium:monero.social >__ The number of txs needed to infer network topology increases with log(n). n being the number of nodes.     

> __< b​oog900:monero.social >__ not as far as I can see, it is re-broadcasting every tx     

> __< o​frnxmr:monero.social >__ That sounds like a bug     

> __< b​oog900:monero.social >__ if we add rate limits we should be fine right?     

> __< b​oog900:monero.social >__ if we only had 1 connection that dropped the tx we would need to re-broadcast     

> __< o​frnxmr:monero.social >__ We had issues with tx-proxy failing to relay tx, and then changed the behavior to attempt to retry the broadcast     

> __< r​ucknium:monero.social >__ https://github.com/monero-project/monero/issues/9334#issuecomment-2307824031     

> __< o​frnxmr:monero.social >__ Iirc this was changed at or around the hardfork     

> __< r​ucknium:monero.social >__ > Under some conditions, an estimator needs O ( s log ⁡ ( n ) ) cascades, where s is the number of edges of the node with the most edges in the network and n is the number of nodes on the network. The O ( ) order estimate of the number of cascades is interesting because it suggests that network inference with transaction arrival timestamps would become more feasible as transacti<clipped message     

> __< r​ucknium:monero.social >__ on volume rises. Assume that the number of nodes on the network grows at the same rate as the growth of transaction volume. This assumption would be roughly true if (1) each user makes a constant number of transactions, (2) the growth of transactions is due to new users, and (3) new users boot up new nodes in the same proportion as old users.     

> __< r​ucknium:monero.social >__ I don't know if rate limits would eliminate the issue. There are papers on the amount of noise that network inference estimators can overcome.     

> __< b​oog900:monero.social >__ When tx broadcasts are tx-hashes re-broadcasts should become less of a problem     

> __< r​ucknium:monero.social >__ MEETING END. Discussion can continue of course.     

> __< b​oog900:monero.social >__ But this is also the case when the adversary just listens for tx messages without probing     

> __< b​oog900:monero.social >__ with enough connections/txs you could perform a similar attack     

> __< r​ucknium:monero.social >__ With more connections you can multiply your rate-limited queries :)     

> __< b​oog900:monero.social >__ Sure but if we removed that possibility this attack is still possible     

> __< b​oog900:monero.social >__ and the rate limits should at least help     

> __< r​ucknium:monero.social >__ And there are many methods to query txpools. Could be better to feign ignorance of specific txs. Ignorance could apply globally to all txpool query methods.     

> __< r​ucknium:monero.social >__ Bitcoin developers implemented diffusion since they thought it was probably good enough. The Dandelion++ creators showed that it was not good enough.     

> __< b​oog900:monero.social >__ Maybe? maybe not? we need definitive numbers on how effective different attacks are before deciding on countermeasures that effect the protocol in that way IMO     

> __< r​ucknium:monero.social >__ And it took them two tries to get a robust protocol     

> __< b​oog900:monero.social >__ how would we handle double spends?     

> __< b​oog900:monero.social >__ if we ignore knowledge of txs     

> __< r​ucknium:monero.social >__ I can try to work on those numbers, but it will take a while since there are other things to do. I decided to look into this tx propagation issue instead of finishing up some black marble research since I knew devs were eager to get started on it.     

> __< r​ucknium:monero.social >__ The node knows it has txs, but it doesn't indicate to its peer that it knows. The node dumps the double spend.     

> __< b​oog900:monero.social >__ Fair IMHO these attacks are extremely expensive/impossible so not a priority     

> __< b​oog900:monero.social >__ dumping is what happens when the tx is known     

> __< b​oog900:monero.social >__ unless we are going to ignore new txs randomly as well, I guess that would work     

> __< r​ucknium:monero.social >__ Does the node have to tell the peer that it's dumping the tx? I thought a recent change made it so a double spend was not a droppable offense?     

> __< b​oog900:monero.social >__ no, it drops the tx before doing all the checks:     

> __< b​oog900:monero.social >__ > Double spend checks, we check for tx-pool double spends before checking other consensus rules. It would be possible to create an invalid tx which uses a key-image of a tx you want to check for, send this tx to a node, then if you disconnect they didn't have the tx, and if you stay connected they had the tx (the invalid one was ignore for being a double spend). Although this atta<clipped message>     

> __< b​oog900:monero.social >__ ck was added in tx_memory_pool: make double spends a no-drop offense #9218, 9218 is needed for network security and it would still be possible to perform a timing attack based on the time to disconnect. This attack also exposes the stem pool. Preventing this attack would require checking all consensus rules before checking for double spends, although this would allow a DOS, where <clipped message>     

> __< b​oog900:monero.social >__ the attacker could spam a node with double spends that wont be accepted but the node will still do all the expensive crypto checks. It's also not just a statistical attack, this can be performed on a single tx to expose the nodes in the stem path it took.     

> __< k​ayabanerve:monero.social >__ jeffro256: Really interesting trade off. When using halvings (we don't), I believe the torsion check is roughly half a scalar mul. Without halvings, it's a scalar mul and three doublings. Over 100 TXs, we'd have     

> __< k​ayabanerve:monero.social >__ 100 * 3 doublings     

> __< k​ayabanerve:monero.social >__ Or     

> __< k​ayabanerve:monero.social >__ 3 doublings + 1 mul     

> __< k​ayabanerve:monero.social >__ 1 mul will presumably be more expensive than 297 doublings. It's inherently 256 doublings.     

> __< k​ayabanerve:monero.social >__ The halving version may be more performant but that requires we impl and bench it     

> __< k​ayabanerve:monero.social >__ I'd just do the cofactor clear     

> __< r​ucknium:monero.social >__ AFAIK, feigning ignorance in push methods would increase bandwidth use. (The node sends us the full tx even though we already know it.) Feigning ignorance in a pull method like reconciliation would slow tx propagation.     

> __< b​oog900:monero.social >__ seen as we are already using D++ the main problem I think would be learning the P2P graph as that could make certain attacks more easy by targeting certain nodes.     

> __< b​oog900:monero.social >__ Knowing if a peer has a fluff tx is not a problem otherwise IMO.     

> __< b​oog900:monero.social >__ so it would be good to know how effect diffusion is at preventing graph learning     

> __< b​oog900:monero.social >__ effective*     

> __< b​oog900:monero.social >__ which as far as I seen wasn't in your right up? except for a note it would be harder than Bitcoins old protocol     

> __< b​oog900:monero.social >__ which as far as I seen wasn't in your write up? except for a note it would be harder than Bitcoins old protocol     

> __< r​ucknium:monero.social >__ You saw my comment that the original paper authors of the bitcoin-network-influence-through-tx-relay paper said it would be harder, but they didn't say how much     

> __< r​ucknium:monero.social >__ Exercise left to the reader I guess :D     

> __< r​ucknium:monero.social >__ AFAIK, it won't be simple because their original statistical method was tailored to the earlier "trickle" protocol. Somehow that would have to be modified.     

> __< r​ucknium:monero.social >__ Or maybe it would be easier to start with one of the papers that does network inference from cascades with noisy data.     

> __< b​oog900:monero.social >__ Yeah probably     

> __< r​ucknium:monero.social >__ It could be nice to set up a tx propagation simulator one day. There are a couple of them from some papers.     

> __< b​oog900:monero.social >__ I tried to run the one from D++ but I ran into a few issues and struggled to follow the code     

> __< r​ucknium:monero.social >__ Especially since now the fluff timers are set by a Poisson distribution instead of exponential. AFAIK almost all gossip papers with continuous time use exponential timers. None use Poisson. One used truncated normal I think. But then the protocol could be put into alignment with the theory, instead     

> __< r​ucknium:monero.social >__ In July the maintainer updated the D++ code to Python3 IIRC     

> __< r​ucknium:monero.social >__ The memorylessness of exponential timers helps with theoretical analysis a lot.     

> __< b​oog900:monero.social >__ Yeah I definitely think we should move fluff timers to the exponential distribution     

> __< r​ucknium:monero.social >__ I don't see any downsides to doing that. Probably a good idea.     

> __< b​oog900:monero.social >__ I would expect the first spy estimator to be a lot better using the Poisson distribution     

> __< b​oog900:monero.social >__ maybe not a lot but at least better     

> __< r​ucknium:monero.social >__ You've seen it, but here is my comment on that for reference: https://github.com/monero-project/monero/pull/9295#issuecomment-2260998091     

> __< b​oog900:monero.social >__ just by following the logic of what must happen for the first spy estimator to fail. The node must broadcast to a connection and then that connection has to broadcast to the adversary, before the node broadcasts to the adversary     

> __< b​oog900:monero.social >__ (many hops could happen in the middle but that's unlikely)     

> __< b​oog900:monero.social >__ with the Poisson distribution the chance of this is less     

> __< UkoeHB >__ jeffro256: it's not really relevant if you're using X25519 for the ecdh.     

> __< j​effro256:monero.social >__ But doesn't X25519 solve that by clamping the private key, so that all private keys are divisible by 8? If we wanted to use legacy keys (anything mod `l`), then we still need to clear cofactor, right?     

> __< j​effro256:monero.social >__ (and/or otherwise ignoring the bottom 3 bits of the key)     

> __< v​tnerd:monero.social >__ Yes jeffro I see what you mean. The view pubkey used by the sender needs to be computed with the clamping, or the shared secret will differ. You'd have to add a new "tag" to addresses to know whether a mul8 was needed at the end. It's probably not worth the hassle, otoh I don't know the specific timings of the mul8 operation     

> __< UkoeHB >__ jeffro256: yes, Ed25519 keys need to clear the cofactor     

> __< UkoeHB >__ mul8 is quite fast compared to a full multiplication    

# Action History
- Created by: Rucknium | 2024-08-26T20:27:21+00:00
- Closed at: 2024-09-06T19:42:56+00:00
