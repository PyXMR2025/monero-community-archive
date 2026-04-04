---
title: Monero Research Lab Meeting - Wed 18 June 2025, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1223
author: Rucknium
assignees: []
labels: []
created_at: '2025-06-17T22:29:25+00:00'
updated_at: '2025-06-27T21:52:19+00:00'
type: issue
status: closed
closed_at: '2025-06-27T21:52:19+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/meeting.html?p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3.  [SLVer Bullet: Straight Line Verification for Bulletproofs](https://github.com/cypherstack/silver-bullet).  [Cypher Stack review of divisors for FCMP](https://github.com/cypherstack/divisor_deep_dive).

4. FCMP alpha stressnet

5. Disclosure of method to detect [spy nodes](https://github.com/monero-project/research-lab/issues/126).

6.  CCS proposal: [Monero Network Simulation Tool](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/589).

7. Peer Scoring Metrics.

8. Any other business

Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#1220 

# Discussion History
## Rucknium | 2025-06-19T18:10:40+00:00
Logs:

> __< r​ucknium:monero.social >__ Meeting time! https://github.com/monero-project/meta/issues/1223     

> __< r​ucknium:monero.social >__ 1) Greetings     

> __< a​rticmine:monero.social >__ Hi     

> __< c​haser:monero.social >__ hello     

> __< rbrunner >__ Hello     

> __< d​oedl...:zano.org >__ [btw antilt's nick today] seas     

> __< v​tnerd:monero.social >__ Hi     

> __< j​berman:monero.social >__ *waves*     

> __< g​ingeropolous:monero.social >__ hi     

> __< s​yntheticbird:monero.social >__ Hi     

> __< r​ucknium:monero.social >__ 2) Updates. What is everyone working on?     

> __< d​oedl...:zano.org >__ me: looked into anchor nodes logic.     

> __< r​ucknium:monero.social >__ me: Finished my MoneroKon talks for this weekend: "OSPEAD: Optimal Ring Signatures" and "Defeating Spy Nodes on the Monero Network", which is joint work with boog900     

> __< a​rticmine:monero.social >__ I have completed the scaling and fee proposal for FCMP++ which I am presenting at MoneroKon 5 here in Prague     

> __< j​berman:monero.social >__ me: destroying FFI types correctly ready for re-review, continuing allowing support for >8-input FCMP++ txs (includes grouping multiple FCMP++ proofs into one tx primarily so that proof construction doesn't take minutes for large txs), next reviewing outstanding PR's and will look deeper into reported bugs in FCMP++/Carrot     

> __< r​ucknium:monero.social >__ A few announcements:     

> __< r​ucknium:monero.social >__ On Monday, Douglas Tuman of MoneroTalk interviewed Luke Szramowski  and Diego Salazar of Cypher Stack about their recent FCMP Divisors work (MoneroTalk episode 353): https://rumble.com/v6uv9ol-moneros-fcmp-upgrade-status-with-diego-salazar-of-cypher-stack-epi-353.html     

> __< r​ucknium:monero.social >__ This weekend is MoneroKon! Lots of interesting talks about Monero R&D. Schedule here: https://cfp.twed.org/mk5/schedule/     

> __< r​ucknium:monero.social >__ Someone created a new Twitter account that tweets updates from MRL. IMHO, they are doing a great job so far :) https://xcancel.com/MoneroResearchL     

> __< r​ucknium:monero.social >__ Definitely much better than the time someone wrote MRL logs into the blockchain in protest of tx_extra 😉     

> __< v​tnerd:monero.social >__ Me: finally implemented the old fee algorithm in LWS, thanks ArticMine:     

> __< r​ucknium:monero.social >__ 3) [SLVer Bullet: Straight Line Verification for Bulletproofs](https://github.com/cypherstack/silver-bullet).  [Cypher Stack review of divisors for FCMP](https://github.com/cypherstack/divisor_deep_dive).     

> __< r​ucknium:monero.social >__ On Monday, sgp_  said:     

> __< r​ucknium:monero.social >__ > Quick heads up to for the room here. There were some questions about the CS silver bullet document, and this will likely (though not for certain) result in zkSec not having something "locked in" to review by the time we would need to lock them in for next week. In any case, I'll keep the room updated     

> __< r​ucknium:monero.social >__ > The ball appears to be back in our court now, thanks Brandon     

> __< r​ucknium:monero.social >__ Is the next step to look for firm(s) to review SLVer Bullet?     

> __< r​ucknium:monero.social >__ To perform a mathematical review, I mean     

> __< j​berman:monero.social >__ I don't know if I have the latest info, but AFAIK, kayabanerve  has some questions on the doc for CS. Those questions would need to be squared away before moving forward on contracting another firm to review     

> __< d​iego:cypherstack.com >__ We've been in contact and talking back and forth.     

> __< d​iego:cypherstack.com >__ May take a bit. Not too long.     

> __< r​ucknium:monero.social >__ Once those questions are resolved, would it be a green light to implement the needed code changes in the FCMP codebase and start searching for a review firm?     

> __< r​ucknium:monero.social >__ And who would take the task of implementing the code changes?     

> __< j​berman:monero.social >__ That would probably be the ideal scenario     

> __< j​berman:monero.social >__ We will see once those questions are resolved     

> __< j​berman:monero.social >__ Also, once those are resolved, it's likely a green light to move forward on implementing a blinds cache, which would ideally be completed before a wider testnet/stressnet as well. So imo it will make sense to re-open the conversation on a wider testnet/stressnet fairly soon     

> __< r​ucknium:monero.social >__ Oh yes. Actually, it is the next agenda item     

> __< j​berman:monero.social >__ Probably will line up with the end of the contest. On the contest, I've heard from one dev who may have a valid helioselene submission soon. But I have not seen any code yet     

> __< j​berman:monero.social >__ No valid submissions at this point     

> __< r​ucknium:monero.social >__ More discussion on FCMP divisors before moving on to FCMP alpha stressnet?     

> __< j​berman:monero.social >__ nothin from me     

> __< d​iego:cypherstack.com >__ Remind me the details of the contest?     

> __< r​ucknium:monero.social >__ Diego coming in with a late entry? :P     

> __< d​iego:cypherstack.com >__ Mebbe     

> __< r​ucknium:monero.social >__ https://web.getmonero.org/2025/04/05/fcmp++-contest.html     

> __< d​iego:cypherstack.com >__ Thx     

> __< j​berman:monero.social >__ TLDR: We opened a contest to optimize 2 libs used for FCMP++, helioselene (100 XMR prize) and ec-divisors (250 XMR prize), open to anyone to participate, closes for submissions June 30th     

> __< d​iego:cypherstack.com >__ Hmmmm     

> __< rbrunner >__ If working day and night, in shifts?     

> __< d​iego:cypherstack.com >__ If contest closes with no submissions reopen once new divisors lib?     

> __< r​ucknium:monero.social >__ IIRC, if no submission achieves greater than 20% speedup over the reference implementation, then there is no prize awarded, by the way.     

> __< j​berman:monero.social >__ possible     

> __< r​ucknium:monero.social >__ 4) FCMP alpha stressnet     

> __< r​ucknium:monero.social >__ It may be a good idea to create a checklist of tasks to be completed before alpha stressnet     

> __< r​ucknium:monero.social >__ jberman has a checklist of FCMP tasks, but I cannot recall the URL     

> __< j​berman:monero.social >__ https://github.com/seraphis-migration/monero/issues/53     

> __< r​ucknium:monero.social >__ I suppose the checklist could include Blinds cache, new divisors computations, and fixing the testnet bugs that ofrnxmr  encountered     

> __< j​berman:monero.social >__ Yep: FFI PR merged, new divisors impl, blinds cache, squash a few bugs (sweep issues, error handling, ofrnxmr 's issue, and wallet scan issue also reported by plowsof ). We may also want support for >8-input txs but not a requirement (may invite scope creep to need more changes for weight handling)     

> __< r​ucknium:monero.social >__ Sounds great. Thanks for keeping track of all those tasks.     

> __< r​ucknium:monero.social >__ Anything more on FCMP alpha stressnet?     

> __< j​berman:monero.social >__ Nothin here     

> __< r​ucknium:monero.social >__ 5) Disclosure of method to detect spy nodes. https://github.com/monero-project/research-lab/issues/126     

> __< r​ucknium:monero.social >__ At Monday's No Wallet Left Behind meeting, I asked jeffro256  if he was OK with boog900  and I disclosing boog900 's method for distinguishing spy nodes from honest nodes, at MoneroKon. He was Ok with it     

> __< d​oedl...:zano.org >__ after PR is merged ?     

> __< r​ucknium:monero.social >__ No, before the PR is merged. Our spy node talk is scheduled for Sunday     

> __< rbrunner >__ Won't be merged at MoneroKon     

> __< r​ucknium:monero.social >__ That's the plan. I think it would be ok, or even desirable, to post the information and make the repo public before then. I don't want to make this too much of a dramatic "show" revelation, since it is privacy-related information, not a shiny new product or something.     

> __< r​ucknium:monero.social >__ By "that's the plan" I mean the plan is to include it in the spy node talk     

> __< b​oog900:monero.social >__ I can make the code public now?     

> __< r​ucknium:monero.social >__ MRL has requested that users "trust" the ban list for over six months now, without verifying the method     

> __< r​ucknium:monero.social >__ IMHO, I think it would be fine to switch the repo to public.     

> __< r​ucknium:monero.social >__ By the way, I will start daily data gathering of reachable nodes on the network. It's just good data to have available in the future, but more importantly, it could help figure out if the spy nodes try to move to another set of IP addresses if they were to patch their spy fingerprint.     

> __< rbrunner >__ Yeah, why not. May also motivate to review my PR     

> __< b​oog900:monero.social >__ ok I am going to make it public     

> __< b​oog900:monero.social >__ https://github.com/Boog900/p2p-proxy-checker     

> __< b​oog900:monero.social >__ The spy nodes leak the peer_id of the nodes they proxy from during a ping     

> __< rbrunner >__ Chuckle     

> __< r​ucknium:monero.social >__ Here is boog900 's draft explanation for how it works:     

> __< r​ucknium:monero.social >__ ```     

> __< r​ucknium:monero.social >__ Every node in the Monero P2P network has a self-assigned 64-bit identifier called a peer_id. This peer_id is      

> __< r​ucknium:monero.social >__ randomly generated at startup and stays static until the node is shutdown[^1].     

> __< r​ucknium:monero.social >__ The peer_id is shared in handshake (request and response) and ping (just response) messages. When a node does a handshake,      

> __< r​ucknium:monero.social >__ the peer_id it returns, with high probability, should not match with any other peers on the network. For proxy     

> __< r​ucknium:monero.social >__ nodes this is the same, the peer_id they return will be unique, and it will also be constant across connection attempts.     

> __< r​ucknium:monero.social >__ However, when a ping is sent to a proxy node, they return a peer_id that does not match the one they sent during the      

> __< r​ucknium:monero.social >__ handshake. This peer_id is going to be called the inner peer_id compared to the outer one they give during a handshake.      

> __< r​ucknium:monero.social >__ There are two classes of proxy nodes that have been detected:     

> __< r​ucknium:monero.social >__ - Class A: these nodes have inner peer_ids that directly match another real node's peer_id. These nodes are not a part      

> __< r​ucknium:monero.social >__   of the big subnets and are the single IP addresses.     

> __< r​ucknium:monero.social >__ Hopefully that didn't hurt the IRC side too much     

> __< rbrunner >__ It's ok     

> __< r​ucknium:monero.social >__ I will add this text to the draft subnet deduplication MRL bulletin soon.     

> __< s​yntheticbird:monero.social >__ great explanation     

> __< r​ucknium:monero.social >__ jhendrix: ^ Here is the method to identify spy nodes on the Monero network.     

> __< r​ucknium:monero.social >__ I pinged you because you did the Maldo map research about them.     

> __< s​yntheticbird:monero.social >__ i know no one asked but fai the proxies are written in java     

> __< r​ucknium:monero.social >__ Great job everyone who worked on the spy node identification! Especially boog900 , of course     

> __< r​ucknium:monero.social >__ "fai"?     

> __< s​yntheticbird:monero.social >__ for anyone interests     

> __< r​ucknium:monero.social >__ 6) CCS proposal: Monero Network Simulation Tool. https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/589     

> __< r​ucknium:monero.social >__ Were gingeropolous  and 0xfffc  able to have a conversation about network simulation requirements?     

> __< g​ingeropolous:monero.social >__ no, there was no movement on this from my end unfortunately.     

> __< r​ucknium:monero.social >__ Ok. In the next few days will try to contact the developer of EthShadow about the amount of work that could be involved, whether he could possibly implement it, and at what cost.     

> __< r​ucknium:monero.social >__ * I will try to contact     

> __< r​ucknium:monero.social >__ 7) Peer Scoring Metrics.     

> __< d​oedl...:zano.org >__ In a nutshell, anchor_list stores a snapshot of outgoing connections with a uniq first_seen field. connections_maker() uses anchor_list first (before white_list and gray_list). Anchor peers may therefore telescope back to the first and most reliable peers a node has seen.      

> __< d​oedl...:zano.org >__ "When the node restarts to establish outgoing connections, it will give priority to the peer node with the smallest first_seen field in anchor_list." Shi [1], p.16 (Appendix B) claims there might be a logic error in the source, likely in get_and_empty_anchor_peerlist(apl) if apl is a reference to an empty object.     

> __< d​oedl...:zano.org >__ Hu [2] points out that a single anchor node connection (not vulnerable to gray_list spam) may prevent an eclipse. Anchor nodes can protect against diffamation-style counter-attacks [1] when taking more punitive action, i.e disconnecting or blacklisting misbehaving nodes.     

> __< d​oedl...:zano.org >__ Afaik there is no way to list anchor nodes with the --print_pl command atm.      

> __< d​oedl...:zano.org >__ Refs:     

> __< d​oedl...:zano.org >__ [1] Shi, R., Peng, Z., Lan, L., Ge, Y., Liu, P., Wang, Q., & Wang, J. (2025). Eclipse attack on menero’s peer to peer network. In Proceedings of Network and Distributed System Security Symposium (NDSS).      

> __< d​oedl...:zano.org >__ https://www.ndss-symposium.org/wp-content/uploads/2025-95-paper.pdf     

> __< d​oedl...:zano.org >__ [2] Security Analysis of Monero’s Peer-to-Peer System     

> __< d​oedl...:zano.org >__ https://courses.csail.mit.edu/6.857/2018/project/Hu-Macias-Jachymiak-Siabi-Monero.pdf     

> __< r​ucknium:monero.social >__ diffamation = defamation?     

> __< r​ucknium:monero.social >__ (If so, remember _not_ to edit this long post on the Matrix side because it spams the IRC side)     

> __< r​ucknium:monero.social >__ So is anchor list mostly relevant when restarting a node? The anchoring criteria is just a low last_seen value?     

> __< d​oedl...:zano.org >__ defamation = getting nodes to disconnect honest peers     

> __< d​oedl...:zano.org >__ that depends on the handling of anchor_list.     

> __< d​oedl...:zano.org >__ atm yes.     

> __< r​ucknium:monero.social >__ By the way, jhendrix  produced an interesting and thorough analysis of network privacy problems on Zano mainnet. Tor hidden service link accessible through Tor Browser:  http://g7cpug4k6ydyq5dlxrji35xnfq5n5rba3n7holux4tmdsm42ju543tad.onion     

> __< r​ucknium:monero.social >__ AFAIK, Zano is considered a Cryptonote-style blockchain like Monero. But Zano doesn't use the privacy-improving Dandelion++ protocol for transaction propagation.     

> __< d​oedl...:zano.org >__ I could not verify if apl is a reference to an empty object, btw     

> __< rbrunner >__ Yes, Zanbo ultimately derives from CryptoNote, like Monero     

> __< rbrunner >__ *Zano     

> __< r​ucknium:monero.social >__ I guess one could try to test that in a debugger     

> __< rbrunner >__ I can recommend to analysis     

> __< rbrunner >__ *that     

> __< d​oedl...:zano.org >__ https://github.com/monero-project/monero/blob/master/src/p2p/net_peerlist.h#L:502     

> __< d​oedl...:zano.org >__ m_peers_anchor.get<by_time>().clear(); //then clear m_peers_anchor from boost container (?)     

> __< r​ucknium:monero.social >__ flip flop: Thank you for looking into the anchor list :)     

> __< r​ucknium:monero.social >__ By the way, did you find the "Security Analysis of Monero’s Peer-to-Peer System" paper through an internet search or through MoneroResearch.info?     

> __< d​oedl...:zano.org >__ de nada. sounds unlikely to me.       

> __< d​oedl...:zano.org >__ std::vector<anchor_peerlist_entry> apl;  // is this a reference or a new object     

> __< r​ucknium:monero.social >__ Just wanting to check the usefulness of MR.info :)     

> __< d​oedl...:zano.org >__ it IS useful. But I used google.scholar     

> __< r​ucknium:monero.social >__ More discussion on this topic for now?     

> __< r​ucknium:monero.social >__ We can end the meeting here. Thanks everyone     

> __< s​yntheticbird:monero.social >__ thanks     

> __< rbrunner >__ doedl: I don't see any problem with the code of `get_and_empty_anchor_peerlist` method and they way it gets called. Maybe I overlook something     

> __< s​yntheticbird:monero.social >__ delicious meeting     

> __< rbrunner >__ With "std::vector<anchor_peerlist_entry> apl;" you have a perfectly fine vector, just with zero elements     

> __< rbrunner >__ You can hand that to the method, and it will fill it, as a reference parameter is used     

> __< d​oedl...:zano.org >__ yes and it gets filled later     

> __< a​rticmine:monero.social >__ Thanks     

> __< rbrunner >__ The method name tells exactly what happens     

> __< d​oedl...:zano.org >__ for_each(...) // fill     

> __< rbrunner >__ Right     

> __< d​oedl...:zano.org >__ thats what I assumed all along     

> __< d​oedl...:zano.org >__ tx - very important to me     

> __< rbrunner >__ Just checked in the debugger, I have that set up for debugging my PR - looks all ok, no "logic error" in sight if you ask me     

> __< d​oedl...:zano.org >__ It keeps the "oldest" peers around (might be seed nodes even) and uses 2 of them with priority.     

> __< d​oedl...:zano.org >__ That adds tremendously to Monero's resiliance imho    


# Action History
- Created by: Rucknium | 2025-06-17T22:29:25+00:00
- Closed at: 2025-06-27T21:52:19+00:00
