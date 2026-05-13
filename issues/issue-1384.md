---
title: Monero Research Lab Meeting - Wed 06 May 2026, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1384
author: Rucknium
assignees: []
labels: []
created_at: '2026-05-06T14:48:07+00:00'
updated_at: '2026-05-13T14:27:58+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

Live log: https://libera.monerologs.net/monero-research-lab

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/meeting.html?p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3. zksecurity review of Generalized Bulletproofs (GBP).

4. Audit of Helios/Selene Rust library.

5. [Post-quantum encryption](https://github.com/monero-project/research-lab/issues/151#issuecomment-4281932714).

6. [FCMP beta stressnet](https://github.com/seraphis-migration/monero/releases/).

7. [CCS proposal: ProbeLab P2P Network Metrics Proposal](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/667).

8. Any other business

Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#1380 

# Discussion History
## plowsof | 2026-05-06T15:28:21+00:00
a snapshot of the ccs ideas page here: https://web.archive.org/web/20260502230004/https://ccs.getmonero.org/ideas/
PropeLabs proposal here:so people can read  https://web.archive.org/web/20260502231314/https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/667

## Rucknium | 2026-05-13T14:27:58+00:00
Log

> __< rucknium >__ Meeting time! https://github.com/monero-project/meta/issues/1384     

> __< rucknium >__ 1. Greetings     

> __< articmine >__ Hi     

> __< vtnerd >__ Hi     

> __< rbrunner >__ Hello     

> __< gingeropolous >__ Hi     

> __< jpk68:matrix.org >__ Hello     

> __< iamnew117:matrix.org >__ Hello     

> __< tevador >__ Hi     

> __< jberman >__ waves     

> __< ack-j:matrix.org >__ Hey     

> __< UkoeHB >__ Hi     

> __< rucknium >__ 2. Updates. What is everyone working on?     

> __< UkoeHB >__ Me: sal multisig wip     

> __< tevador >__ me: Jamtis     

> __< rucknium >__ me: Helping with FCMP beta stressnet     

> __< jberman >__ beta stressnet, looking into GUI simple mode hard fork prep      

> __< vtnerd >__ Me: perf and unit testing the mempool patch for lws     

> __< vtnerd >__ It's otherwise merged with the new /feed code so it's just looking for buga at this pot     

> __< sgp_ >__ Hello, sorry I'm late     

> __< rucknium >__ 3. zksecurity review of Generalized Bulletproofs (GBP).     

> __< sgp_ >__ I think this can be a quick topic. I would like to get MRL research committee approval for a donation of $100,000 to review the composition and implementation of GBPs     

> __< rucknium >__ Does this come from the FCMP research budget?     

> __< sgp_ >__ CS suggested changes to GBPs after finding an issue. This will evaluate those changes and resolve the outstanding items for them     

> __< sgp_ >__ rucknium: yes, it would come from there     

> __< rbrunner >__ Not sure why to call this a "donation". Isn't it simply a payment?     

> __< jeffro256 >__ Howdy      

> __< rucknium >__ Will zksecurity just evaluate the changes or review the whole GBP?     

> __< sgp_ >__ whole shebang     

> __< sgp_ >__ > Note: The specification and the updated security proofs are in scope for review and not assumed to be correct. The goal is to ensure the correctness/security of the code, not just alignment with the "untrusted" specification.     

> __< jberman >__ Research fund currently has 597.89xmr, and owes $15k to CS for FCMP++ composition follow-up review (I'm not sure if this has been paid yet), so this would be a ways under half the remaining funds     

> __< jberman >__ At the current xmr price     

> __< rucknium >__ Probably the term is "donation" since MAGIC is a nonprofit organization with legal status.     

> __< rucknium >__ Discussion of this proposed expenditure?     

> __< articmine >__ I suspect legally it has to be a donation      

> __< rbrunner >__ I see. Just making sure it's not that a mysterious new donor suddenly appeared and left USD 100,000 behind :)     

> __< sgp_ >__ fwiw, this has been discussed in the past here multiple times, but it has been delayed after CS found issues with GBPs     

> __< jberman >__ I'm definitely a strong +1. I think it's clearly of critical importance to have this reviewed further, and bringing in another highly skilled independent team to do so makes strong sense to me     

> __< sgp_ >__ a review is necessary to safely use GBPs, a critical component of the FCMP++ upgrade     

> __< rbrunner >__ I did not follow closely, but I guess that finding of a problem by CS was a bit of a surprise, and thus a bit worrisome. I think it would be a good idea to become sure here.     

> __< rucknium >__ I agree with jberman:monero.social , sgp_:monero.social , and rbrunner .     

> __< rucknium >__ Any more discussion or objections to the proposal?     

> __< articmine >__  I agree      

> __< rucknium >__ I see loose consensus in favor of zksecurity reviewing Generalized Bulletproofs (GBP) in exchange for the equivalent of 100,000 USD.     

> __< rucknium >__ 4. Audit of Helios/Selene Rust library.     

> __< rucknium >__ Anything to discuss on this at the moment?     

> __< sgp_ >__ nope, other than if you are interested in submitting a proposal for this, please email justin⊙mo     

> __< rucknium >__ 5. Post-quantum encryption (https://github.com/monero-project/research-lab/issues/151#issuecomment-4281932714).     

> __< tevador >__ Quick update: Based on the last meeting, I decided to go with Option A for Jamtis and use the standard CSIDH-1024 parameters. The address length will be 400 characters. I'm working on an interactive payment protocol that will be able to provide full privacy without an on-chain key exchange (it will be an appendix to the address specs).     

> __< vtnerd >__ Not a fan of it being interactive - is that portion mandatory? The user cannot opt out of an interactive key exchange?     

> __< tevador >__ To clarify: there will be both options. A non-interactive PQ key exchange based on CSIDH-1024 and an optional interactive one based on symmetric crypto only.     

> __< vtnerd >__ Hmm. Symmetric crypto is a sure way to anger a QC      

> __< rucknium >__ More noob questions from me, about scan time. What happens when an old-style (non-quantum-resistant) wallet scans a quantum-resistant output. Any slowdown? And the reverse: Any speedup when a new-style wallet scans a non-quantum-resistant output?     

> __< jberman >__ I don't really see another feasible route on the table here tbh. If we want mobile wallets to be able to restore a wallet from seed, then the more secure PQ key exchange algos don't seem practical by the figures here      

> __< articmine >__ A related question is how effective is parallel processing here?     

> __< tevador >__ The goal is for all transactions to have a CSIDH-1024 public key in tx extra. Legacy wallets will simply ignore the key. Scan times will be about the same as now for both legacy and Jamtis.     

> __< tevador >__ enote scanning is obviously parallelizable, but the amount of computation required makes CSIDH view tags infeasible     

> __< rucknium >__ jberman: jberman:monero.social: Do you mean the interactive protocol or Option A for non-interactive?     

> __< jberman >__ That comment applies to both. I don't see another route on the table aside from those 2 routes: Option A for non-interactive, or the interactive protocol     

> __< rucknium >__ What if we wait until better PQ algorithms are discovered?     

> __< tevador >__ I also think that option A and an additional interactive protocol is the best compromise. Addresses will remain usable and the interactive protocol can be used by users who want more PQ privacy than Jamtis will offer.     

> __< rucknium >__ Hard to know what the future may hold, of course.     

> __< tevador >__ Waiting is not an option due to "harvest now, decrypt later".     

> __< rbrunner >__ At least with A we don't get astronomical scan times, with mobile wallets completely unable to scan themselves      

> __< jberman >__ It could theoretically be implemented and not deployed until the QC threat passes some threshold, and in that time if some better algo arises, perhaps we could swap it in     

> __< rucknium >__ With Option A, a quantum adversary cannot identify all the outputs sent to an address that it does not know, correct? There would be limited ability to try to cluster the behavioral information.     

> __< gingeropolous >__ but then there's n years of data to decrypt     

> __< jpk68:matrix.org >__ As rbrunner mentioned last week (I think), making scan times infeasible for mobile wallets (basically, anything that would force you to self-host something like LWS) would eliminate a huge amount of people from being able to use Monero     

> __< jpk68:matrix.org >__ In my opinion this is infinitely more of a UX burden than long addresses, for example     

> __< rucknium >__ I think people could still use Monero. But would not be protected from a quantum adversary.     

> __< jeffro256 >__ rucknium: With option A, a QA can identify all outputs sent to any address sharing that one's view key. And it can identify spends in most cases      

> __< rucknium >__ But not any outputs of a view key that it does not know any addresses of?     

> __< endogenic >__ all ecdh and signing is broken by qc guys     

> __< rucknium >__ It would ID spends because of change outputs sent to own addresses, I assume     

> __< endogenic >__ you can't still use monero     

> __< jeffro256 >__ rucknium: Yes. but that is true of CARROT and legacy addresses too      

> __< tevador >__ rucknium: With option A, if the QA knows one of your addresses, they can calculate primary and secondary view tags, but can only probabilistically identify enotes to unknown addresses unless the address is reused.     

> __< tevador >__ jeffro256: No, it cannot identify spends.     

> __< rucknium >__ If the adversary had the addresses of the sender and recipient, that would reveal the spending behavior fully. Not the amount. Correct?     

> __< tevador >__ Internal enotes use a symmetric key for view tags.     

> __< jeffro256 >__ tevador: I mean that it can sometimes identify the spend location of external enotes, not internal enotes      

> __< luke:cypherstack.com >__ I agree with Rucknium's comment of potentially waiting for more PQ options. Isogeny based scheme make me nervous.     

> __< tevador >__ If the adversary has Alice's and Bob's addresses, they can see enotes (without amounts) coming to Alice's and Bob's wallet, but can't infer they are transacting with each other.     

> __< endogenic >__ if mallory has a and b addrs then mallory can get a and b sec keys no ?     

> __< tevador >__ jeffro256: It cannot, at least not for Jamtis enotes.     

> __< rucknium >__ luke:cypherstack.com: luke:cypherstack.com: Thank you for your comment. Could you elaborate?     

> __< rucknium >__ (Luke S is with Cypher Stack https://cypherstack.com/about.html  )     

> __< endogenic >__ I guess he's talking about lattice etc problems     

> __< tevador >__ luke: I'm actually quite confident about CSIDH.     

> __< tevador >__ The original idea behind CSIDH is from 1996 IIRC, so fairly old.     

> __< luke:cypherstack.com >__ Sure. Me and the other mathematicians have spent a great deal of time talking about PQ security stuff, both at CS and in our academic careers and it is the loose consensus that isogeny based problems are the least favorite of the potential PQ primitives.     

> __< jeffro256 >__ > <tevador> If the adversary has Alice's and Bob's addresses, they can see enotes (without amounts) coming to Alice's and Bob's wallet, but can't infer they are transacting with each other.     

> __< jeffro256 >__ Maybe I'm remembering an attack which works on Seraphis, but not FCMP++ because of the key image composition. I'll look at it again. At least with Jamtis previously, if two enotes were spent from the same address, even if a QA didn't know the spend key extensions, they could tell that they were the same between 2 (one-time add [... too long, see https://mrelay.p2pool.observer/e/sJ6Pv4ALU1dNWmhh ]     

> __< jeffro256 >__ It's been a while since I looked at that particular attack      

> __< luke:cypherstack.com >__ Lattice based problems are fine but I personally am a big proponent of Code based cryptography. I think it is probably the most likely to retain its PQ status in the time to come.     

> __< tevador >__ jeffro256: IIRC that was a Seraphis-only attack, FCMP++ has perfectly hiding linking tags.     

> __< jeffro256 >__ Seraphis also had perfectly hiding linking tags, though. The foil might be the hash-to-point in FCMP++      

> __< tevador >__ luke: Yes, McEliece would have been great if it wasn't for the 250 KB public keys :)     

> __< tevador >__ A bit impractical for an address.     

> __< luke:cypherstack.com >__ I agree, but it is entirely possible that we might see some sort of improvement in the near future.      

> __< tevador >__ Yes, but waiting means more exposed legacy addresses that will be broken and deanonymized.     

> __< jberman >__ tevador: for the non key exchange route, Tachyon may have a better set of tradeoffs worth considering as well I think     

> __< tevador >__ I'm not familiar with Tachyon     

> __< rucknium >__ We should move on to the next item soon.     

> __< jberman >__ https://seanbowe.com/blog/tachyon-scaling-zcash-oblivious-synchronization/     

> __< jberman >__ As I understand it, there's an always-on server that scans state without leaking privacy, and there's no key exchange protocol     

> __< rucknium >__ 6. FCMP beta stressnet (https://github.com/seraphis-migration/monero/releases/).     

> __< jeffro256 >__ We have forked!     

> __< rucknium >__ Stressnet forked from testnet about 6 hours ago.     

> __< rucknium >__ My monitors with charts are viewable at https://stressnetnode1.redteam.cash/ and https://stressnetnode2.redteam.cash/     

> __< jberman >__ Cautiously awaiting bug reports :)     

> __< jeffro256 >__ I am working on integrating FCMP++/CARROT wallet knowledge proofs into wallet2 today      

> __< rucknium >__ AFAIK, other ways to view what's happening on stressnet are not available yet, e.g. onion block explorer and DataHoarder[m] 's alt blocks viewer.     

> __< DataHoarder >__ I plan to get my block viewer up and running next week     

> __< DataHoarder >__ $work has coincided and been quite busy     

> __< rucknium >__ Thanks, DataHoarder  !     

> __< rucknium >__ Anything more on stressnet?     

> __< jberman >__ nothing here     

> __< rucknium >__ Stressnet discussion room is #monero-stressnet:monero.social  or ``##monero-stressnet` on IRC.     

> __< rucknium >__ 7. CCS proposal: ProbeLab P2P Network Metrics Proposal (https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/667).     

> __< plowsof >__ can be accessed via this snapshot https://web.archive.org/web/20260502231314/https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/667     

> __< rucknium >__ Thanks, plowsof .     

> __< rucknium >__ Last time sgp_:monero.social  suggested "I think we need research on how dandelion++ works in an adversarial environment, with the presence of a community ban list that X% of honest nodes use and is Y% effective at fingerprinting adversarial nodes"     

> __< gingeropolous >__ seems like a reasonable thing for monerosim     

> __< rucknium >__ I wonder if there is much work involved to do that. The D++ paper showed, theoretically, that the recall that the adversary can achieve is p and the precision is p^2, where p is the percentage of spy nodes in the outbound connections of the targeted node(s).     

> __< rucknium >__ monerosim could definitely be helpful with that, if it were to be done.     

> __< rucknium >__ Also, the Clover paper empirically measured D++ efficacy with a closed bitcoind testnet.     

> __< gingeropolous >__ im finding scale is the issue. though i guess it could just be 1 user sending transactions amidst a network of mostly monerods., not the 1k users (monerods and wallets) i for some reason have set the bar at      

> __< rucknium >__ https://moneroresearch.info/222 Franzoni, F., & Daza, V. (2022). Clover: An anonymous transaction relay protocol for the bitcoin P2P network. Peer-to-Peer Networking and Applications, 15(1), 290–303.       

> __< rucknium >__ Section 7.3, page 12     

> __< rucknium >__ Measuring the effectiveness still does not solve the spy node issue, which is the ultimate goal.     

> __< yiannisbot:matrix.org >__ Hi folks, back online and available now. Great there is a mirror for the proposal - I was not aware.      

> __< rucknium >__ Can I assume that boog900:monero.social  does not want to comment about the proposal (or is just not checking pings in this room at this time)?     

> __< rucknium >__ A simulation could discover a problem with monerod's implementation of D++ if it existed, however. AFAIK, there hasn't been a realistic test of the actual implementation.     

> __< yiannisbot:matrix.org >__ Based on monerosim you mean?      

> __< rucknium >__ Yes. monerosim would be the obvious platform for a test like that.     

> __< rucknium >__ Code at https://github.com/Fountain5405/monerosim     

> __< yiannisbot:matrix.org >__ Yeah, it could be a good first step. Although I think that a real-world test would help - maybe as a second step.     

> __< yiannisbot:matrix.org >__ A few things that we've been thinking about regarding D++ are: if spy nodes can dominate or distract message propagation (before they're added to the ban list), what is the risk threshold of privacy guarantees for ban list adoption. I was also wondering what's the efficiency of "fluff timer" efficiency, e.g., if a malicious no [... too long, see https://mrelay.p2pool.observer/e/-cWJwIALYmZGdmc2 ]     

> __< yiannisbot:matrix.org >__ But rucknium:monero.social as you said, the spy node issues we've put in the proposal would come first IMO.     

> __< ofrnxmr >__ sorry to interject: The onion explorer rekt my blockchain. i think it might need to be updated for beta > <rucknium> AFAIK, other ways to view what's happening on stressnet are not available yet, e.g. onion block explorer and DataHoarder[m] 's alt blocks viewer.     

> __< boog900 >__ Sorry, I thought I had given some thoughts on it, but I don't support the proposal in its current form. I don't see that much value in a second network monitor.     

> __< boog900 >__ I think we already have a pretty good idea of how D++ performs from the paper. I would rather research on how to stop spy nodes all together, maybe looking at how to further increase their costs.      

> __< rucknium >__ Thank you, boog900:monero.social     

> __< yiannisbot:matrix.org >__ > we already have a pretty good idea of how D++ performs from the paper     

> __< yiannisbot:matrix.org >__ What ratio of spy to normal nodes did the paper investigate? I can't remember. Is that close to what we found at: https://probelab.io/blog/peering-into-privacy-a-deep-dive-into-the-monero-network-topology/ ?     

> __< articmine >__ One important aspect of the spy node issue is the role of blockchain surveillance (BS) companies in setting up these spy nodes, and the use of spy nodes to obtain  personally identifying information from wallet users by deceit. This was discussed in a leaked video.     

> __< boog900 >__ yiannisbot:matrix.org: they had graphs which plotted performance against fraction of spies      

> __< articmine >__  I am dressing the following comment from  Ssgp_  :     

> __< yiannisbot:matrix.org >__ boog900: Sure, but can't remember what's the fraction they used. Will have a look.      

> __< articmine >__ More fundamentally, what is the important problem that this dashboard is going to solve? Why do we need one so much so that the community should crowdfund for one?     

> __< rucknium >__ yiannisbot:matrix.org: I don't know what you mean by your question. The theoretical formula works for any ratio of spy nodes. I looked at the D++ paper recently again. They used a modified bitcoind on bitcoin mainnet, but for tx propagation speeds instead of estimating spy resistance. The D++ paper had plenty of python simulations for numerical estimates for the spy effects, however.     

> __< yiannisbot:matrix.org >__ articmine: Exactly and that's why I think a risk threshold study would be important.     

> __< articmine >__ One of the key elements I see in this dashboard is publicly exposing the BS company behaviour     

> __< rucknium >__ The Clover paper used actual bitcoind for a private testnet simulation to record the spy node effects (for Clover and D++). There is another paper that just did simulations that I will pull in a minute.     

> __< articmine >__ In my view both  the study and the dashboard is needed     

> __< rucknium >__ Sharma, P. K., Gosain, D., & Diaz, C. (2022). On the Anonymity of Peer-To-Peer Network Anonymity Schemes Used by Cryptocurrencies. arXiv.   https://moneroresearch.info/130     

> __< rucknium >__ The Sharma, Gosain, & Diaz paper was about learning the private D++ graph. More complicated and difficult for an adversary to achieve.     

> __< boog900 >__ I feel the result of any research on spy nodes is just going to be "spies bad".     

> __< boog900 >__ Even if we say the privacy impact is 0, just the impact on the security of the network is enough to warrant research into how to prevent them.      

> __< boog900 >__ so why not just skip to step 2 and work out how to get rid of them.      

> __< boog900 >__ it would be cool to know that the spies probably got X% of tx origins, but what real value does that give us?     

> __< rucknium >__ I shall end the meeting here since we are 30 minutes past the hour, but everyone should feel free to continue discussing any topic.     

> __< rucknium >__ boog900:monero.social: Would you suggest that research be put into something like this, but with fewer downsides? https://ieeexplore.ieee.org/document/10174897     

> __< yiannisbot:matrix.org >__ I obviously feel that the dashboard would be valuable and I can't see anywhere the metrics we published on the blogpost, but happy to skip that part for now and proceed with Milestone 2 only for now.      

> __< rucknium >__ The problem with open-ended research is that at the end, possibly nothing useful will come out of it. It's risky.     

> __< rucknium >__ https://ieeexplore.ieee.org/document/10174897 citation is J. W. Heo, G. Ramachandran and R. Jurdak, "PPoS : Practical Proof of Storage for Blockchain Full Nodes," 2023 IEEE International Conference on Blockchain and Cryptocurrency (ICBC), Dubai, United Arab Emirates, 2023, pp. 1-9, doi: 10.1109/ICBC56567.2023.10174897.     

> __< yiannisbot:matrix.org >__ rucknium: Do you refer to Milestone 2 of the proposal as open-ended? I would see a clear outcome out of it with recommendations and proof.     

> __< rucknium >__ yiannisbot:matrix.org: No. "work out how to get rid of them [spy nodes]" is the open-ended path     

> __< boog900 >__ Yes I do think PPoS or something Proof-of-Storage-esque is going to be the solution for spy nodes > <rucknium> boog900:monero.social: Would you suggest that research be put into something like this, but with fewer downsides? https://ieeexplore.ieee.org/document/10174897     

> __< rucknium >__ I asked the lead author of the D++ paper about how to get rid of spy nodes and she didn't have any great ideas.     

> __< rucknium >__ That's in a previous MRL log from about a year ago IIRC     

> __< articmine >__ boog900:monero.social: I agree with     

> __< articmine >__ > so why not just skip to step 2 and work out how to get rid of them.     

> __< articmine >__ I suggest that not only should we consider technical countermeasures, but  social and even set the stage for legal countermeasures should one or more members of the community wish to go that route.     

> __< boog900 >__ boog900: If they still pay the full storage cost if we impl PPoS then we are out of options really, as they would have the resources to run real nodes.     

> __< rucknium >__ This is an example of a research effort that did not produce the intended results: "Research to Defeat EAE Attack and Analyze Effectiveness of Churning Procedures" https://donate.magicgrants.org/monero/projects/eae_attack_and_churning     

> __< boog900 >__ boog900: At that point we would need to look at being a permissioned network, for tx-relay at least     

> __< rucknium >__ Reasonably, PoW is probably out of the question because it would hit honest nodes too hard.     

> __< rucknium >__ But cutting-edge research is often risky.     

> __< boog900 >__ rucknium: yeah I think so too     

> __< yiannisbot:matrix.org >__ Yeah, it's tricky.      

> __< tevador >__ PoW might hit malicious nodes much harder than honest ones. Honest nodes: 12 outgoing connections. Malicious nodes: 1000 outgoing connections.     

> __< articmine >__ We have to consider that the adversary is likely very vulnerable to out of network countermeasures such as public exposure and the risk of legal action     

> __< boog900 >__ spies use incoming connections for D++     

> __< boog900 >__ I think putting PoW for incoming would be a DoS right?     

> __< tevador >__ How do they get an incoming connection? By spamming the peer list.     

> __< tevador >__ If entering the peer list requires a PoW, it will be harder to spam.     

> __< boog900 >__ They have a few nodes that make outgoing and spread the addresses of the many that just listen     

> __< boog900 >__ that would be a 1 time cost though?     

> __< tevador >__ You can add a timestamp to the peer list and also hash the ID of the node keeping the list, so if they want to be included in 1000 peer lists, they need 1000x the PoW.     

> __< boog900 >__ presumably this advisory has quite a bit of resources, I don't think we can give them enough compute to discourage them without impacting normal nodes.     

> __< tevador >__ My main point is that I would not dismiss PoW as a possible solution.     

> __< articmine >__ I am not so sure. The adversary is also trying to hide. I am not the biggest fan of user POW but this may be an exception.      

> __< articmine >__ POW is worth looking into as an option. Especially if we can reliably detect the spy nodes.     

> __< articmine >__ There are interesting differences between honest and spy nodes that can be targeted     

> __< tevador >__ jberman: I checked the Tachyon blog post. It seems that Zcash wants to eliminate non-interactive transfers, which is probably not what we want?     

> __< tevador >__ quote: "As a start, we'll be assuming that Zcash's future payment flows involve out-of-band payments where the sender and recipient use a separate channel for secret distribution."     

> __< yiannisbot:matrix.org >__ So what I'm hearing is that it would be desirable to focus on Milestone 2 and consider some PoW aspect?     

> __< yiannisbot:matrix.org >__ Or leave PoW out for a later stage?      

> __< yiannisbot:matrix.org >__ articmine: I agree. I think we can come up with better and more reliable heuristics.     

> __< jberman >__ tevador: I agree. In any case, their intent seems to be to roll it out in phases, which implies a period of time where they'd support both. Considering how they've done things in the past, I'd assume the "tachyon" pool is incompatible with the existing anonymity pools though. And ya I would agree distinct anon pool is not what we'd want     

> __< jberman >__ But perhaps there could be some tweak that enables a compatible anon set with an interactive protocol     

> __< jberman >__ non-interactive*     

> __< jberman >__ I would be surprised if that design isn't achievable     

> __< ixr3:matrix.org >__ > <luke:cypherstack.com> I agree with Rucknium's comment of potentially waiting for more PQ options. Isogeny based scheme make me nervous.     

> __< ixr3:matrix.org >__ I hope Jeffro implements the carrot key hierarchy soon after the HF, or earlier if the HF is significantly delayed. Internal forward secrecy will help in the meantime until better PQ solutions are available. Churning will become increasingly important for anyone concerned with post‑quantum security.     

> __< ixr3:matrix.org >__ "harvest now, decrypt later" is bad and the Jamtis-PQ release will probably take longer than expected     

> __< intr:unredacted.org >__ out of curiosity, have Freeman Slaughter's comments from that MoneroTopia episode been addressed before?     

> __< tevador >__ jberman: it's not about the anon pool. It's the UX shift to interactive transactions that we don't want. Zcash is a for profit company, they can afford to run infrastructure to help users interact during payments, but it's not a viable solution for Monero.     

> __< jberman >__ I agree and am not raising it to shift UX to interactive payments     

> __< jberman >__ You mentioned exploring an optional interactive route that would require out of band communication, I'm mentioning a Tachyon-like design as worth considering for that optional component alongside the non interactive     

> __< jberman >__ Also it doesn't seem like the protocol requires a single centralized server, and a user could spin up their own instance. I imagine the UX would include some payment request that points to their own instance of choice     

> __< jberman >__ That design obviously seems worth considering if we're discussing interactive payments     

> __< tevador >__ I'm not going to place any infrastructure requirements in my proposal. The interactive payment protocol will be executed by passing 3 alphanumeric strings between the recipient and the sender over any communication channel of their choice.     

> __< sgp_ >__ some wallets already do this for payjoin. I hate implementations where this would be expected, but wallets often use stuff like this today for helper functions. The fewer that are needed, the better. https://github.com/cake-tech/cake_wallet/blob/dev/cw_bitcoin/lib/payjoin/manager.dart#L33     

> __< tevador >__ The flow in my sketch protocol is: Receipient -> Sender -> Recipient -> Sender, where each arrow is a ~400 character string.     

> __< jberman >__ A 3-round protocol is hard to see gaining traction without a server in between helping automate the flow     

> __< jberman >__ I would guess that wallet apps may implement a communication protocol with their own infra (or maybe work something out with some service provider)     

> __< jberman >__ And so long as a server would be involved, then it's worth thinking on further and weighing expected UX     

> __< sgp_ >__ I think that an interactive payment protocol would be a huge loss :(     

> __< sgp_ >__ if the requirement of max address length of 420 was dropped, would BC1024 be the most appealing? or would you still prefer A?     

> __< sgp_ >__ I admit to being tempted by BC512. Yes, the security guarantees are smaller with CSIDH-512 than CSIDH-1024. But the privacy gains with option B over A are considerable to me.     

> __< sgp_ >__ If we consider a "collect now and decrypt later" scenario as the most dangerous at the moment, it seems to suggest that we should prefer greater privacy (1/256 enote narrowing down vs knowing all received enotes) to the security margin. If it would take "65 thousand quantum computers running for 5 years" to break the security  [... too long, see https://mrelay.p2pool.observer/e/xYjqxoALbG1sclNo ]     

> __< sgp_ >__ Am I misinterpreting something?     

> __< tevador >__ sgp_: Why would and *additional* interactive protocol be a loss? If it's optional for people who want to use it. IMO it's a net gain.     

> __< sgp_ >__ I mean requiring it for PQ privacy of received enotes (even in the 1/256 form) would be unfortunate     

> __< sgp_ >__ If options A or B are selected, I'm not against an optional interactive thingy for even better post quantum privacy     

> __< tevador >__ Option B is kinda suboptimal, that's why I preferred A or C. B adds: some (but not a lot) of enote privacy, but the costs are: much larger addresses, a much larger pruned transactions (up to 2-3 KB for 16-out transactions) and awkward filter assist (light wallets are supposed to run the heavy CSIDH instead of the filter server).     

> __< tevador >__ And B still lacks PQ unlinkability, so if you have 2 online identities and use the same wallet, they can be linked in a PQ scenario.     

> __< tevador >__ Only option C gives full PQ privacy.     

> __< sgp_ >__ I definitely wasn't factoring in the filter assist, but I do think 1/256 is hugely better than nothing (it's like ring sigs, but better)     

> __< sgp_ >__ linkability is unfortunate but we deal with janus now, so advanced users should be aware of potential limitations, and they can be informed that limitations would persist     

> __< sgp_ >__ I suppose one argument for Option A is that senders already know what enotes they send to addresses they are aware of, so this could be a user education problem, where recipients are told to always use fresh addresses per sender. Address hygiene becomes more of a requirement. Basically, we try to UX our way out of most limitat [... too long, see https://mrelay.p2pool.observer/e/-uTZx4ALaFY5am02 ]     

> __< tevador >__ For maximum privacy, you should use a fresh wallet per sender, unless we go with Option C.     




# Action History
- Created by: Rucknium | 2026-05-06T14:48:07+00:00
