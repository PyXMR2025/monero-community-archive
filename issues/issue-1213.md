---
title: Monero Research Lab Meeting - Wed 28 May 2025, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1213
author: Rucknium
assignees: []
labels: []
created_at: '2025-05-27T21:50:54+00:00'
updated_at: '2025-06-05T21:54:40+00:00'
type: issue
status: closed
closed_at: '2025-06-05T21:54:40+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/meeting.html?p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3. [FCMP++ & divisors.](https://github.com/cypherstack/divisor_deep_dive)

4. Unit test for implementation of [subnet deduplication in peer selection algorithm](https://github.com/Rucknium/misc-research/blob/main/Monero-Peer-Subnet-Deduplication/pdf/monero-peer-subnet-deduplication.pdf).

5. Web-of-Trust for node peer selection.

6. Any other business

7. Confirm next meeting agenda

Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#1208 

# Discussion History
## Rucknium | 2025-05-30T16:45:30+00:00
Logs:

> __< 0​xfffc:monero.social >__ Hi everyone     

> __< r​ucknium:monero.social >__ Meeting time! https://github.com/monero-project/meta/issues/1213     

> __< r​ucknium:monero.social >__ 1) Greetings     

> __< a​rticmine:monero.social >__ Hello     

> __< rbrunner >__ hello     

> __< g​ingeropolous:monero.social >__ hi     

> __< v​tnerd:monero.social >__ Hi     

> __< a​ntilt:we2.ee >__ hi     

> __< j​berman:monero.social >__ *waves*     

> __< a​ck-j:matrix.org >__ hi     

> __< c​haser:monero.social >__ hello     

> __< r​ucknium:monero.social >__ 2) Updates. What is everyone working on?     

> __< 0​xfffc:monero.social >__ Working on addressing reviews / comments on new tx relay v2      

> __< 0​xfffc:monero.social >__ https://github.com/monero-project/monero/pull/9933     

> __< j​effro256:monero.social >__ Howdy     

> __< a​ntilt:we2.ee >__ finished brief rundown (20 lines) of scoring methods found in ~50 papers for today     

> __< r​ucknium:monero.social >__ me: Analysis of subnet deduplication for node peer selection as a countermeasure to spy nodes. I simulated a network with 90 percent unreachable (closed-port) nodes and found that honest reachable nodes would have 133 median inbound connections with the status quo algorithm and 182 median inbound connections with subnet deduplication. This would put more load on the honest reachable nodes.     

> __< r​ucknium:monero.social >__ Docs here: https://rucknium.github.io/xmrpeers/reference/gen.network.html     

> __< j​effro256:monero.social >__ me: still working on cold/hot wallet stuff. I had to re-work a big part of the carrot_impl lib to get a clean solution for some problems, but I think I should be wrapping it up soon within the next couple of days     

> __< j​berman:monero.social >__ me: Finished FCMP++ scan_tx, an RPC endpoint to fetch paths by global output id, and worked on getting all tests to pass with the latest code     

> __< v​tnerd:monero.social >__ Me: fixed all remaining send tx issues with lws-frontend except priority fees, which requires Daemon+LWS api changes. Otherwise fees are correctly computed now, and txes can be split if there is a high number of destinations just like wallet2     

> __< r​ucknium:monero.social >__ 3) FCMP++ & divisors. https://github.com/cypherstack/divisor_deep_dive     

> __< r​ucknium:monero.social >__ Is Liam Eagen here? xmrack  invited him.     

> __< r​ucknium:monero.social >__ Any Cypher Stack staff here? There is a new document from them:     

> __< r​ucknium:monero.social >__ Goodell, B., Salazar, R., Slaughter, F., & Szramowski, L. (2025). A Further Review of the DL Gadget Of Interest. https://moneroresearch.info/268     

> __< d​iego:cypherstack.com >__ hi     

> __< a​ck-j:matrix.org >__ Rucknium: I’m not sure, they said they would be free but I havent seen them join     

> __< r​ucknium:monero.social >__ I read the new doc ^ and have some questions and comments.     

> __< d​iego:cypherstack.com >__ Question and comment away     

> __< r​ucknium:monero.social >__ The divisors would use probabilistically checkable proofs (PCP). Does this open a new potential attack vector or does Monero already use this type of technique somewhere critical?     

> __< r​ucknium:monero.social >__ And does it make it harder to compute the N bit security of Monero's cryptography?     

> __< b​randon:cypherstack.com >__ hello everyone, sorry about my delay     

> __< b​randon:cypherstack.com >__ PCPs are not problematic on their own, it's just a description of what sort of algorithm it is.     

> __< b​randon:cypherstack.com >__ like a sigma protocol just describes a 3-round interaction, a PCP just means "this is a proof which is probabilitically checkable" (and therefore should be parameterized so that probabilities of security problems are negligible)     

> __< r​ucknium:monero.social >__ On the Schwartz-Zippel Lemma discussion: Usually, mathematicians love to generalize things. The fact that the SZ Lemma has not been generalized to the multivariate case makes me think that it is very hard to generalize, or cannot be generalized, period. How solid is Bassa's alternative approach that substitutes for the SZ Lemma?     

> __< r​ucknium:monero.social >__ 4.3.1 Developer watermarking     

> __< r​ucknium:monero.social >__ > This means that a malicious developer can insert additional points, or remove certain points, from a     

> __< r​ucknium:monero.social >__ statement. This won’t be detected if the proof remains valid, and the cryptographic size of G ensures that stashing a single random element in a divisor is essentially undetectable.     

> __< r​ucknium:monero.social >__ Check this paper. Maybe this malicious watermarking is already possible in RingCT: Guo, S. 2024, Secure Monero on Corrupted Machines with Reverse Firewalls. Paper presented at International Conference on Data Security and Privacy Protection.  https://moneroresearch.info/245     

> __< r​ucknium:monero.social >__ Abstract:     

> __< r​ucknium:monero.social >__ > Monero is known as a cryptocurrency for its ability to provide greater anonymity. At its core is the RingCT protocol that can hide the sender and the amount of money in a transaction. However, the Snowden revelation alerts us that the implementation of cryptographic algorithms in practice might be substituted covertly which would result in a complete breach of the security of th<clipped message     

> __< r​ucknium:monero.social >__ e cryptosystem. In this work, we turn to evaluate the potential hazards of algorithm substitution attacks (ASAs) against the RingCT protocol and explore feasible countermeasures. In specific, we first present the ASA model for RingCT where the goals of adversary include diminishing sender anonymity and recovering the spending key, then propose concrete ASAs against RingCT protocol<clipped message     

> __< r​ucknium:monero.social >__ s that are undetectable in terms of the output of algorithms. Finally, we show how to thwart ASAs on RingCT protocols with reverse firewalls.     

> __< b​randon:cypherstack.com >__ Re: Schwartz-Zippel: Generalizing to the multivariate case isn't hard. Bassa's work was insufficient in showing that the problem appropriately fits into that context, and the details of how it does so inform quantified assessments of probability of success     

> __< b​randon:cypherstack.com >__ malicious watermarking is admittedly hard to defend against. at least in this case, it would be checkable if code were doing that, but it could lead to fingerprinting and more. just like developer choices in terms of payment IDs in the past could be used to split monero's anonymity pool into puddles     

> __< b​randon:cypherstack.com >__ also, i believe we have nailed down some calculus problems in the specific divisor algorithms which don't impact completeness but impact soundness     

> __< r​ucknium:monero.social >__ Yes. I would be more concerned about accidental watermarks from custom implementations, but I don't know how likely custom implementations may be for this part of Monero's cryptography, deep in the system.     

> __< b​randon:cypherstack.com >__ getting into greater detail about that is still a little premature; we are deriving all equations rigorously from scratch     

> __< r​ucknium:monero.social >__ Theorems 2 & 3 in the document: Shouldn't these be labeled as conjectures instead of theorems?     

> __< b​randon:cypherstack.com >__ Yeah, that'd be more appropriate     

> __< b​randon:cypherstack.com >__ although we have a proof of theorem 2 now     

> __< b​randon:cypherstack.com >__ and theorem 3 is not far behind either     

> __< r​ucknium:monero.social >__ Great!     

> __< b​randon:cypherstack.com >__ it would be shocking to me if these were not true conjectures     

> __< f​reeman:cypherstack.com >__ I agree, intuition dictates it. But might as well be certain     

> __< r​ucknium:monero.social >__ This is a self-directed comment to MRL, not really Cypher Stack: I finally looked at Eagen's divisor paper:      

> __< r​ucknium:monero.social >__ Eagen, L. 2022. Zero Knowledge Proofs of Elliptic Curve Inner Products from Principal Divisors and Weil Reciprocity https://moneroresearch.info/index.php/269     

> __< r​ucknium:monero.social >__ Eagen says that the argument for his divisors technique is similar to the argument for Bulletproofs++. However, over a year ago, Aaron Feikert (sarang) reviewed BP++ and said there were questions about its validity: https://moneroresearch.info/217     

> __< r​ucknium:monero.social >__ So, MRL assumed that Eagen's divisors were OK despite the BP++ work falling short. And there was not much action taken on backup plans.     

> __< j​effro256:monero.social >__ The https://moneroresearch.info/index.php/269 link is broken I think btw     

> __< r​ucknium:monero.social >__ Does someone else have questions and comments about the latest divisor's analysis?     

> __< r​ucknium:monero.social >__ Thanks, should be https://moneroresearch.info/269     

> __< r​ucknium:monero.social >__ Papers and document relevant to FCMP are collected here by the way: https://moneroresearch.info/index.php?action=list_LISTSOMERESOURCES_CORE&method=subcategoryProcess&id=1     

> __< j​berman:monero.social >__ Would need more time to review the paper, but the general takeaway from it is the same as has been discussed in past meetings: divisors require more academic rigor and work and may fall short under further scrutiny, and CS appears to be continuing that work     

> __< j​berman:monero.social >__ "And there was not much action taken on backup plans." -> Luke was pretty clear on the backup from the start, which is that divisors could be swapped out in the impl. The vast majority of the meat of FCMP++ and code we've been working on is still useful in that backup scenario     

> __< r​ucknium:monero.social >__ I don't know if I would have been a +1 vote on the FCMP optimization competition timeline if I had investigated and thought about it more. Of course, cryptography is not my field, so I would tend to defer to others on those questions, anyway. And programming isn't my field either :)     

> __< r​ucknium:monero.social >__ Anyway, that is water under the bridge     

> __< s​yntheticbird:monero.social >__ Regarding the competition, i'm not shy to say the ban of the r/rust post was dramatic for reaching out potential competitors     

> __< j​berman:monero.social >__ I think in hindsight, maybe would have made sense to do a more general academic approach on divisors from the start with an open timeline, rather than the more piece-meal approach. Hindsight is 20/20     

> __< r​ucknium:monero.social >__ From what I understand now, Cypher Stack's review of Bassa's work has turned into much more: needing to prove things and make scientific progress. MRL is very thankful for that.     

> __< s​yntheticbird:monero.social >__ not xmrack fault (I think it was xmrack idr for sure), but it's been mostly our only card of reaching other communities     

> __< rbrunner >__ I think as long as CypherStack makes progress and does not declare defeat nothing is ultimately lost yet ...     

> __< r​ucknium:monero.social >__ surae, Freeman Slaughter , Luke Szramowski , Diego Salazar : Do you need anything specific from MRL at this time?     

> __< d​iego:cypherstack.com >__ Give us dominos pizza gift cards, please and thank you.     

> __< r​ucknium:monero.social >__ To MRL: Is there specific action/decisions that MRL needs to take about divisors? Proposals?     

> __< r​ucknium:monero.social >__ I assume that if there were news about non-divisor FCMP implementation, it would appear     

> __< rbrunner >__ You mean from third parties?     

> __< j​berman:monero.social >__ Nothing from me. Sorry, will share as soon as I have news to share on non-divisor impl     

> __< rbrunner >__ Ah, no, our own alternative     

> __< g​ingeropolous:monero.social >__ so does the non-divisor FCMP implementation need its own audits etc?     

> __< j​effro256:monero.social >__ Yes     

> __< j​effro256:monero.social >__ It would have a different cryptographic construction and needs to be audited separately     

> __< s​yntheticbird:monero.social >__ Will some parts benefits from the prior audit? or is this audit "practically" done from scratch again?     

> __< j​berman:monero.social >__ AFAIU we would need security proofs with the new construction and a new audit for that component, but most of the prior non-divisors research should be unaffected (like GBP research). Pinging kayabanerve to clarify     

> __< r​ucknium:monero.social >__ More comments or questions on FCMP divisors?     

> __< j​effro256:monero.social >__ SyntheticBird: A lot of non-membership-specific academic is reusable. If you look at https://moneroresearch.info/228, the SA/L proof doesn't have to be re-proved, the section 7 "composed proving system" doesn't have to be re-proved, and the general higher-level security properties of the system (section 8) don't have to be re-proved. We would basically just need to audit that the <clipped messag     

> __< j​effro256:monero.social >__ new non-divisor FCMP membership construction can prove the relation in section 5     

> __< r​ucknium:monero.social >__ 4) Unit test for implementation of subnet deduplication in peer selection algorithm. https://github.com/Rucknium/misc-research/blob/main/Monero-Peer-Subnet-Deduplication/pdf/monero-peer-subnet-deduplication.pdf     

> __< r​ucknium:monero.social >__ Like I said in updates, I simulated a network with 90 percent unreachable (closed-port) nodes and found that honest reachable nodes would have 133 median inbound connections with the status quo algorithm and 182 median inbound connections with subnet deduplication. This would put more load on the honest nodes.     

> __< r​ucknium:monero.social >__ During last year's suspected black marble tx flooding, nodes with many connections had trouble keeping up with the blockchain.     

> __< g​ingeropolous:monero.social >__ what was total size of network?     

> __< r​ucknium:monero.social >__ I don't know if the projected increased load is something to really worry about. Anyway, the simulation assumes that all nodes update, which usually doesn't happen     

> __< rbrunner >__ Well, you can always limit the number of incoming connections with a parameter     

> __< r​ucknium:monero.social >__ With the 90 percent unreachable assumption, there would be 44,000 total honest nodes. That seems high, but some people who run reachable nodes report about 150 inbound connections, which would be roughly consistent with the 90% unreachable assumption, if everyone followed the status quo default peer selection algorithm and 12 outbound connections default.     

> __< r​ucknium:monero.social >__ 0xfffc's work on the more efficient tx transmission protocol would help here     

> __< r​ucknium:monero.social >__ If nodes start limiting inbound connections, then other honest nodes would have to pick up the slack.     

> __< r​ucknium:monero.social >__ Now, the network is using spy nodes as a crutch.     

> __< rbrunner >__ Hopefully mostly people with weak systems, or limited bandwidth, would limit     

> __< r​ucknium:monero.social >__ Since those spy nodes are absorbing a lot of those connections that "should" be going to honest nodes.     

> __< 0​xfffc:monero.social >__ Quick update, for anyone not in the loop: I am addressing the reviews and concerns about the code. No deal breaker. Hopefully the new implementation will be push in a day or two.     

> __< a​rticmine:monero.social >__ What is the current level of inefficiency? Name Ly how many times is the same transaction data, transmitted during transaction propagation and finally during propagation of the mined black ?     

> __< rbrunner >__ I think we will have to just try and see. Not bringing a better algorithm into service and continuing to connect to a lot of spy nodes can't be the solution :)     

> __< r​ucknium:monero.social >__ By the way, boog900  and my MoneroKon 2025 presentation on defeating spy nodes, which will include subnet deduplication analysis, is now scheduled for June 22. Abstract here: https://cfp.twed.org/mk5/talk/AE7CWF/     

> __< a​rticmine:monero.social >__ Getting a handle on this will go a long way to help overburdened nodes     

> __< 0​xfffc:monero.social >__ Congrats, looking forward to seeing it.     

> __< b​oog900:monero.social >__ Over 90% of tx broadcasts are redundant     

> __< r​ucknium:monero.social >__ A full txpool makes it worse, because the node will re-broadcast unconfirmed transactions half a dozen times, at intervals.     

> __< r​ucknium:monero.social >__ Which is probably one reason why the spam last year was so tough on nodes.     

> __< r​ucknium:monero.social >__ rbrunner had an update on his investigations of the peer connection code, I think.     

> __< rbrunner >__ Yeah, found a sweet bug that made most connection retries basically a waste of time internally. Without that bug finding new peers works faster and with a better success rate     

> __< r​ucknium:monero.social >__ Thank you, rbrunner :)     

> __< rbrunner >__ We probably live with that bug for about 6 years :)     

> __< a​rticmine:monero.social >__ So an inefficiency of 10x to 20x     

> __< r​ucknium:monero.social >__ I suspected that the connection attempts were failing too quickly from what I saw in the logs, but I could not read the C++ code     

> __< rbrunner >__ Yes, finding it was a nice teamwork. I can give back thanks, Rucknium!     

> __< r​ucknium:monero.social >__ We can move on to the next agenda item unless there are more comments/questions on this one.     

> __< a​ntilt:we2.ee >__ #9933 fits in nicely here.     

> __< r​ucknium:monero.social >__ 5) Web-of-Trust for node peer selection.     

> __< r​ucknium:monero.social >__ flip flop: What did you find?     

> __< a​ntilt:we2.ee >__ Brief rundown of peer scoring  found in ~50 papers. References on request.     

> __< a​ntilt:we2.ee >__ 1) Data collection:     

> __< a​ntilt:we2.ee >__   1a) Subjective scoring: node keeps track of /quality of service/ of its peers and never reveals its scores to others (bitcoin ban score, peerinfo_manager) Decay factors used to smooth. "Good scores" preferred to "Ban Score" metrics to avoid eclipse, DoS and defamation attack vectors. Reliable. Relatively low requiremets.      

> __< a​ntilt:we2.ee >__   1b) Recommedation based (pgp, GossipTrust, EigenTrust): in addition to a), nodes poll their peers requesting their subjective scores. Authors point out that a well defined "good" init state should exist: then malicious collectives may be broken up by cross-checking. Otherwise lying nodes may break the system with 21%-40% malicious addresses. Some authors suggest data structures <clipped message>     

> __< a​ntilt:we2.ee >__ or a parallel p2p network to store extensive reputation data.      

> __< a​ntilt:we2.ee >__   1c) Data driven: in addition to b) compagnion apps are used to collect big data, querying regular nodes and building a graph represented by nodes, edges and flow metrics (bandwidth, timing). Machine learning is used to detect outliers. Authors tend to promote their own models avoiding self-criticism. Potentially very powerful (yet expensive). May not scale to many nodes.      

> __< a​ntilt:we2.ee >__ 2) Actions:      

> __< a​ntilt:we2.ee >__   2a) The derived metrics may or may not inform /peer selection/: Some authors use scores to prioritize peers, gossip and ban others.      

> __< a​ntilt:we2.ee >__        

> __< a​ntilt:we2.ee >__   2b) At least three Authors design a PBFT based consusus algorithm centered around reputation scores (1b). Roles may be defined by reputation score, such as supernode, verifier, leader, witness, etc. One paper suggests a dual PoW and reputation-based PBFT consensus with variable weight.       

> __< a​ntilt:we2.ee >__        

> __< r​ucknium:monero.social >__ (1c) seems not feasible given that Monero p2p graph edges are deliberately hidden.     

> __< a​rticmine:monero.social >__ How do we identify nodes? Just based up IP address?     

> __< rbrunner >__ Can we say that part of PR #9933 is a case of 1a)?     

> __< 0​xfffc:monero.social >__ Yes.     

> __< a​ntilt:we2.ee >__ absolutely!     

> __< 0​xfffc:monero.social >__ It has a separate peer info management mechanism. Which I track every interaction. Missed, announced, received, send, etc. we can use that data to calculate a score. So far I am only using 70% rule. If they announce 100, but delivery fall less than 70, we drop them.     

> __< 0​xfffc:monero.social >__ But the data is there, ready for other calculations.     

> __< a​ntilt:we2.ee >__ two weeks ago, researchers mapped the net... i take this as viable     

> __< r​ucknium:monero.social >__ IMHO, systems that have been battle-tested in adversarial environments should be considered more seriously than those that have not. I am afraid of systems that would seem to work well in theory, but have hidden flaws that could blow the system apart.     

> __< 0​xfffc:monero.social >__ There was concern from vtnerd to not add it, and integrate it to our existing limited scoring mechanism. Right now I am looking into this.     

> __< a​ntilt:we2.ee >__ i was amazed to find this!  no need to lobby any further... :)     

> __< r​ucknium:monero.social >__ 0xfffc: Could you explain details of Monero's current limited scoring mechanism?     

> __< a​rticmine:monero.social >__ One issue I see is that some ISPs change dynamic IPs on residential  connections with a frequency of under 4 hours.     

> __< r​ucknium:monero.social >__ Originally I thought it was a binary system: One bannable offense gets you banned.     

> __< 0​xfffc:monero.social >__ That is the part I have started today. So my report will not be accurate. But I will write a doc and report send it to this group once I have (more) clear understanding. One of the big problems with our existing scoring is it is tightly integrated into low level networking code.      

> __< 0​xfffc:monero.social >__ I wanted completely abstracted away. Taking that logic out of our low level networking code is the hassle.     

> __< a​ntilt:we2.ee >__ >Failure Detection: Penalizes peers for: Unresponsive behavior     

> __< a​ntilt:we2.ee >__ The intuition is to ban spy nodes, but      

> __< a​ntilt:we2.ee >__ Wenjun Fan et. al [1] and [2] warn that a "good-score" is more effective -- given entries in white_list would be prioritized.      

> __< a​ntilt:we2.ee >__ So called "defamation attacks"... not shure if relevant, adversary might try to eclipse "superodes": dos'ing its peers, then inject fake entries in superode's gray_list.        

> __< a​ntilt:we2.ee >__ [1] The Security Investigation of Ban Score and     

> __< a​ntilt:we2.ee >__ Misbehavior Tracking in Bitcoin Network      

> __< a​ntilt:we2.ee >__ https://par.nsf.gov/servlets/purl/10407054     

> __< a​ntilt:we2.ee >__ [2] Positive Reputation Score for Bitcoin P2P Network     

> __< a​ntilt:we2.ee >__   "focusing on the peer’s behavior in relaying unique/new blocks and transactions."      

> __< a​ntilt:we2.ee >__ https://drive.google.com/file/d/17S4N3eJvUePvO92ob_cIseeusQSMG0ly/view     

> __< 0​xfffc:monero.social >__ We have score field. But we don’t use much IIRC.      

> __< 0​xfffc:monero.social >__ And the bigger issue imho is its integration to our low level networking. Which means you should not and cannot touch it unless you are pretty familiar with our low level networking stack ( asio, etc )     

> __< 0​xfffc:monero.social >__ (9933  it does have other parts than peer info management mechanism )     

> __< rbrunner >__ Would splitting this into two more single-thematic PRs be something? Might also speed up getting the better tx distribution through review and testing     

> __< rbrunner >__ Just brainstorming     

> __< 0​xfffc:monero.social >__ Possible, might be even a good idea. But there is mutual dependency. You need 70% rule for tx relay v2.     

> __< a​ntilt:we2.ee >__ rucknium you had a concern with Tx Relay v2 and D++ ?     

> __< 0​xfffc:monero.social >__ I will talk to boog900 about this though.     

> __< b​oog900:monero.social >__ I suggested splitting the new code for accepting these messages from the code that initiates them. But the code that initiates is like 5% of it.     

> __< r​ucknium:monero.social >__ flip flop: I think the benefits outweigh the potential risks. I wrote a GitHub comment about it.     

> __< rbrunner >__ Initiates what?     

> __< a​ntilt:we2.ee >__ thats what i thought, too     

> __< b​oog900:monero.social >__ rbrunner: tx broadcasts.     

> __< b​oog900:monero.social >__ pretty much the code in levin_notify     

> __< 0​xfffc:monero.social >__ Separate peer info management mechanism, with accurate data for every interaction with the nodes, is something we can use a lot. Does that look like something useful to you Rucknium     

> __< 0​xfffc:monero.social >__ Let’s call it Scoring mechanism. Not peer management ( at this point )     

> __< r​ucknium:monero.social >__ It was mostly about discovery of the p2p network's edges (connections between each node). And apparently the Zurich researchers were about to get a weekly estimate of that from just the white_list peer selection behavior (which could be changed, but the estimate is not very useful to an adversary, as it stands.)     

> __< 0​xfffc:monero.social >__ Every missed, every send, every received, speed. Etc.     

> __< r​ucknium:monero.social >__ Here was my comment: https://github.com/monero-project/monero/issues/9334#issuecomment-2307824031     

> __< a​ntilt:we2.ee >__ it possible to track block delivery, right?     

> __< 0​xfffc:monero.social >__ In hypothetical scoring mechanism, absolutely. I don’t see why not.      

> __< 0​xfffc:monero.social >__ We don’t want to keep the actual data ( that is huge ). We want to keep track of metadata.     

> __< r​ucknium:monero.social >__ 0xfffc: IMHO, it could probably help if spy nodes are trying to save bandwidth by not relaying as many txs and blocks.     

> __< b​oog900:monero.social >__ spy nodes could just not send any invs to save bandwidth, currently we only keep track of this info to stop nodes from advertising txs and then not responding with them when asked.     

> __< a​ntilt:we2.ee >__ the 30 point window could be reduced by a 1-pole recursive filter.     

> __< 0​xfffc:monero.social >__ This is one area I think we don’t use much. I have to talk to boog and other devs more. But data is gold. Once we had the data, we can detect behaviour or the peers.     

> __< 0​xfffc:monero.social >__ And keeping that data is very simple. It is strange we don’t have more robust mechanism for that.     

> __< b​oog900:monero.social >__ I somewhat disagree if I am honest, I think for now it can complicate the system. Once the structure is agreed on how this data is stored we can track more as needed.     

> __< a​ntilt:we2.ee >__ Again, i think of good behavior a  spy node might avoid. And scoring that.     

> __< 0​xfffc:monero.social >__ Yes. The mechanism to keeping that data in code base is gonna be controversial.     

> __< 0​xfffc:monero.social >__ Anyway, I am here in case anyone had any questions. Don’t want to monopolize the meeting time.     

> __< b​oog900:monero.social >__ also vtnerd just suggested to put the current per-peer data that is kept in `peer_info_manager` inside the `connection_context` which i think is reasonable.     

> __< 0​xfffc:monero.social >__ Yes. We have to add all those data to `connection_context`.     

> __< b​oog900:monero.social >__ we already have other monero protocol stuff in there, not just underlying p2p protocol stuff.     

> __< g​ingeropolous:monero.social >__ i mean, a malicious entity could just act good to get in the good graces of the network, and then launch an attack of some kind, right?     

> __< a​ntilt:we2.ee >__ personally i'd prototype stuff like scoring in a compagion app. we only need to reveal the data - taking action is a lot more complex and must be simulated     

> __< a​ck-j:matrix.org >__ Rucknium: Liam messaged me back, there was a miscommunication with times and our MRL meeting conflicted with his Bitcoin conference talk. I’ll try to see if he can join sometime in the next few weeks. Sorry about that     

> __< r​ucknium:monero.social >__ xmrack: Sounds good. Thanks. Try to clarify the goals of his appearance so we know if Cypher Stack staff should be specifically invited.     

> __< g​ingeropolous:monero.social >__ i guess i'm just hoping to clarify what it is we're defending against. Spy nodes? lazy nodes? ddos?     

> __< r​ucknium:monero.social >__ gingeropolous: They can do that now without acting like honest nodes. Though, I would be concerned about an adversary manipulating the scoring system to lower the score of honest nodes. For example, showing even _higher_ bandwidth use than an honest node would.     

> __< b​oog900:monero.social >__ for 9933, a sort of DoS. Nodes could advertise a tx and never send it leaving our node waiting for it until we re-request it after 30 seconds.     

> __< g​ingeropolous:monero.social >__ yeah. i mean, with 9933, it seems there's a need for some scoring system, because if you need to request txs from a peer, then you should drop peers that don't respond.     

> __< b​oog900:monero.social >__ although now thinking about it, it should be windowed, i.e. should only take into account the last 100 txs.     

> __< g​ingeropolous:monero.social >__ and i feel like there's gotta be some middle ground between our current "blast all trasnactions everywhere all the time" and "lets just take a little sip of some data here, and some there"     

> __< g​ingeropolous:monero.social >__ efficiency and resilience are uh.... not the best bedfellows.     

> __< r​ucknium:monero.social >__ We can end the meeting now. Feel free to continue discussing items. Thanks everyone.     

> __< s​yntheticbird:monero.social >__ thanks     

> __< s​yntheticbird:monero.social >__ delicious meeting as always     

> __< a​ntilt:we2.ee >__ thanks     

> __< 0​xfffc:monero.social >__ Thanks everyone     

> __< g​ingeropolous:monero.social >__ thanks all!     

> __< b​oog900:monero.social >__ this probably is the middle ground, we could go even further with protocols like erlay     

> __< a​ntilt:we2.ee >__ if a spy node /demonstrates/ a lot of bandwidth and bandwidth is the only metric... that would be a problem of course.     

> __< s​yntheticbird:monero.social >__ Some will quickly start to realize that I love heuristics, but wouldn't it possible to estimate a median of response time from a specific node and estimate that after say a factor of this median we discard this request and ask for tx from another node     

> __< s​yntheticbird:monero.social >__ "respond in your usual time, or i'll forget you"     

> __< s​yntheticbird:monero.social >__ a little like Tcp round-trip time     

> __< b​oog900:monero.social >__ what if a node never responds     

> __< s​yntheticbird:monero.social >__ well then disconnect     

> __< s​yntheticbird:monero.social >__ why would you stay connected to a node that don't respond     

> __< b​oog900:monero.social >__ but they might have just innocently dropped the tx from their pool     

> __< a​ck-j:matrix.org >__ Have we used tools like shodan or censys to fingerprint nodes before? Rather than looking at peer connections.     

> __< a​ck-j:matrix.org >__ https://www.shodan.io/search?query=%22Monero%22+port%3A18081     

> __< s​yntheticbird:monero.social >__ sorry, i've assumed that nodes would send a response saying that they do not know the tx being requested     

> __< a​ntilt:we2.ee >__ it does not get promoted... if innocent, they are not punished by disconnecting at least     

> __< s​yntheticbird:monero.social >__ if it do not send such then it effectively can't work     

> __< a​ntilt:we2.ee >__ but have a lower rank in white_list     

> __< s​yntheticbird:monero.social >__ No because no one here have shodan keys     

> __< s​yntheticbird:monero.social >__ but that promise to be interesting     

> __< b​oog900:monero.social >__ what if they say they don't know the tx after 25 seconds, meaning we waited on them to tell us they don't have it, during which we can;t request from other peers.     

> __< b​oog900:monero.social >__ They are still within the 30 second limit and will be responding after a constant time meaning it wont be below the median     

> __< a​ck-j:matrix.org >__ I have a bunch of keys if anyone wants     

> __< s​yntheticbird:monero.social >__ 30 second would be an upper bound without a doubt. what im saying is that we should measure the round trip time to this particular node and ask for other nodes after say 10x this delay. But if nodes mostly respond in dozens of milliseconds, we could forget them before 2 seconds pass     

> __< s​yntheticbird:monero.social >__ So if nodes*     

> __< s​yntheticbird:monero.social >__ and ask other peers     

> __< s​yntheticbird:monero.social >__ oh sorry last sentence     

> __< s​yntheticbird:monero.social >__ mhm yeah that's not wrong     

> __< s​yntheticbird:monero.social >__ I guess it needs to be coherent with the other peer request     

> __< b​oog900:monero.social >__ I think you are still thinking in terms of honest nodes, we are trying to protect against people being malicious.     

> __< s​yntheticbird:monero.social >__ that's indeed what im trying to do     

> __< s​yntheticbird:monero.social >__ If the node take 25 sec to send a requested tx, but respond to your timesynced in under 100 milliseconds i mean come on     

> __< s​yntheticbird:monero.social >__ it is malicious     

> __< b​oog900:monero.social >__ now my timed sync takes 25 seconds :)     

> __< s​yntheticbird:monero.social >__ requested tx = batch of requested txs     

> __< a​ntilt:we2.ee >__ how does this work?     

> __< s​yntheticbird:monero.social >__ you would never sustain a connection with a node that slow     

> __< s​yntheticbird:monero.social >__ in a real world scenario     

> __< b​oog900:monero.social >__ sounds like a challenge :)     

> __< s​yntheticbird:monero.social >__ the most intense delay you would ever experience with honest nodes would be at the extreme most 5 sec     

> __< s​yntheticbird:monero.social >__ more than that bro is streaming morse code through low frequency radio     

> __< s​yntheticbird:monero.social >__ At 2 sec you would have at least 50% packet drop     

> __< b​oog900:monero.social >__ it wouldn't be like that, I would just sleep before sending the whole message after 25 seconds     

> __< s​yntheticbird:monero.social >__ mhm     

> __< b​oog900:monero.social >__ tracking amount of missed tx requests is much easier :)     

> __< s​yntheticbird:monero.social >__ in the current state of things monerod would just blindly accept it. My stance is that this type of node should be disconnected from     

> __< s​yntheticbird:monero.social >__ 25 seconds is ridiculously high     

> __< s​yntheticbird:monero.social >__ yes that can do it too without a doubt     

> __< s​yntheticbird:monero.social >__ but the DoS could be operated during a short period of time     

> __< s​yntheticbird:monero.social >__ at least reduce the upper bound of response latency to limit the damage in that small period     

> __< s​yntheticbird:monero.social >__ no honest nodes would take more than 10sec to responid     

> __< s​yntheticbird:monero.social >__ even a potato computer     

> __< b​oog900:monero.social >__ we can do that     

> __< b​oog900:monero.social >__ maybe we should give them a very short ban too     

> __< b​oog900:monero.social >__ like 10 mins     

> __< s​yntheticbird:monero.social >__ sounds good     

> __< s​yntheticbird:monero.social >__ we wouldn't penalize accidental ISP blackout of honest nodes     

> __< s​yntheticbird:monero.social >__ "Your Internet is down? DIE SPY NODE DIE!!!!"     

> __< s​yntheticbird:monero.social >__ more like ISP occasional latency. If the internet was down, the connection would be reset i suppose.     

> __< s​yntheticbird:monero.social >__ I'll call it Internet Weather™     

> __< a​ck-j:matrix.org >__ Censys has a monero_p2p filter already which returns 8,987 nodes.     

> __< a​ck-j:matrix.org >__ https://search.censys.io/search?q=services.extended_service_name%3D%22MONERO_P2P%22&resource=hosts     

> __< a​ck-j:matrix.org >__ We can query for monero p2p nodes within the LinkingLion ASN which returns 1,596 unique IPs.     

> __< a​ck-j:matrix.org >__ https://search.censys.io/search?resource=hosts&sort=RELEVANCE&per_page=25&virtual_hosts=EXCLUDE&q=services.extended_service_name%3D%22MONERO_P2P%22+and+autonomous_system.name%3D%60LIONLINK-NETWORKS%60     

> __< 1​7lifers:matrix.org >__ censys mentioned!     

> __< 1​7lifers:matrix.org >__ we the security community <3 you     

> __< 1​7lifers:matrix.org >__ we the cybersecurity community \<3 you     



# Action History
- Created by: Rucknium | 2025-05-27T21:50:54+00:00
- Closed at: 2025-06-05T21:54:40+00:00
