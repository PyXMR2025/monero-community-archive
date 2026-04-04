---
title: Monero Research Lab Meeting - Wed 30 April 2025, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1197
author: Rucknium
assignees: []
labels: []
created_at: '2025-04-29T21:21:20+00:00'
updated_at: '2025-05-12T15:04:28+00:00'
type: issue
status: closed
closed_at: '2025-05-12T15:04:28+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/meeting.html?p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3. [Gao, Y., Piškorec, M., Zhang, Y., Vallarano, N., & Tessone, C. J. (2025). "Charting the Uncharted: The Landscape of Monero Peer-to-Peer Network"](https://moneroresearch.info/267).

4. [FCMP++ transaction weight formula](https://github.com/seraphis-migration/monero/pull/26).

5. Unit test for implementation of [subnet deduplication in peer selection algorithm](https://github.com/Rucknium/misc-research/blob/main/Monero-Peer-Subnet-Deduplication/pdf/monero-peer-subnet-deduplication.pdf).

6. [Release of OSPEAD HackerOne and CCS milestone submissions](https://github.com/Rucknium/OSPEAD). [Analysis of risk of new decoy selection algorithm without a hard fork](https://gist.github.com/Rucknium/fb638bcb72d475eeee58757f754acbee).

7. Any other business

8. Confirm next meeting agenda

Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#1192 

# Discussion History
## Rucknium | 2025-05-01T19:50:46+00:00
Logs:

> __< r​ucknium:monero.social >__ Yu Gao, first author of recent paper ["Charting the Uncharted: The Landscape of Monero Peer-to-Peer Network"](https://moneroresearch.info/267)  has joined the room. Welcome, Yu Gao !     

> __< r​ucknium:monero.social >__ The paper will be the first agenda item of the meeting in two hours.     

> __< 0​xfffc:monero.social >__ Hi everyone.     

> __< r​ucknium:monero.social >__ Meeting time! https://github.com/monero-project/meta/issues/1197     

> __< r​ucknium:monero.social >__ 1) Greetings     

> __< y​ugao:ifi.uzh.ch >__ Hello, ALL, thanks for the warm welcome, glad to talk with you here.     

> __< rbrunner >__ Hello     

> __< v​tnerd:monero.social >__ hi     

> __< s​yntheticbird:monero.social >__ Hello     

> __< j​berman:monero.social >__ *waves*     

> __< y​ugao:ifi.uzh.ch >__ my coauthor is joining also     

> __< s​packle:monero.social >__ hi     

> __< r​ucknium:monero.social >__ Yu Gao: Wonderful. Thanks.     

> __< a​rticmine:monero.social >__ Hi     

> __< s​gp_:monero.social >__ hello     

> __< s​yntheticbird:monero.social >__ Proposal: when an author join the meeting rucknium should replace "Greetings" section with "MRL. Assemble!"     

> __< r​ucknium:monero.social >__ 2) Updates. What is everyone working on?     

> __< m​atijapiskorec:matrix.org >__ Hi everyone!     

> __< v​tnerd:monero.social >__ me: mostly lws-frontend stuff, with some odds-and-ends in monerod     

> __< r​ucknium:monero.social >__ Matija Piskorec is also an author of [Gao, Y., Piškorec, M., Zhang, Y., Vallarano, N., & Tessone, C. J. (2025). "Charting the Uncharted: The Landscape of Monero Peer-to-Peer Network".](https://moneroresearch.info/267)     

> __< 0​xfffc:monero.social >__ Thanks to help from boog900 I have started working on new tx relay protocol.      

> __< 0​xfffc:monero.social >__ Few general PRs on the side.     

> __< j​berman:monero.social >__ me: shared analysis on the FCMP++ weight calculation and proposed an algorithm (https://github.com/seraphis-migration/monero/pull/26#discussion_r2057203539), continuing on including the FCMP++ tree root in the PoW hash (after discussions with jeffro, I'm currently working on keeping the tree 9 blocks ahead of the tip i.e. growing the tree with outputs that unlock 10 blocks higher <clipped message>     

> __< j​berman:monero.social >__ than the tip which includes normal outputs from the tip block, so that SPV sync via block headers can have solid assurance the latest usable tree root for FCMP++ txs has multiple blocks of PoW on top)     

> __< r​ucknium:monero.social >__ me: Working on the "unit test" of subnet deduplication for peer selection. I have something that seems to be working well for the `white_list`, but maybe not for the `gray_list`.     

> __< j​berman:monero.social >__ Also if if a monero twitter account handler is watching, would be good to announce the FCMP++ optimization contest is now open for submissions     

> __< r​ucknium:monero.social >__ jberman: "SPV" means a wallet using a remote node?     

> __< j​berman:monero.social >__ It could. It means "Simplified Payment Verification": https://wiki.bitcoinsv.io/index.php/Simplified_Payment_Verification     

> __< r​ucknium:monero.social >__ Here is the link for the FCMP++ optimization contest, by the way: https://web.getmonero.org/2025/04/05/fcmp++-contest.html     

> __*__ m-relay <s​yntheticbird:monero.social> whispers there is a 95k$ prize     

> __< r​ucknium:monero.social >__ Yes, SPV is usually a term used in BTC-like blockchains. I was wondering how it is explained in Monero.     

> __< r​ucknium:monero.social >__ I mean, you are trying to have nodes "prove" to wallets that they are not being malicious, right?     

> __< j​berman:monero.social >__ You could sync block headers, and then verify that the user is spending an output that is a member of the chain by checking it against the FCMP++ root included in the block header (that is PoW-verified)     

> __< r​ucknium:monero.social >__ AFAIK, wallet2 did some checks on the outputs distribution histogram to try to detect if nodes were giving bad distributions for ring construction     

> __< j​berman:monero.social >__ Or on the wallet side, the wallet can have stronger assurance the tree it's using to construct the proof is the correct tree (i.e. a malicious node has to provide PoW to feed fake tree data to the wallet)     

> __< s​yntheticbird:monero.social >__ sounds awesome     

> __< r​ucknium:monero.social >__ Sounds great. Is this related to the issue that tevador found in the current PoW?     

> __< r​ucknium:monero.social >__ I mean, is it a way to reduce/eliminate that issue?     

> __< r​ucknium:monero.social >__ And are you talking with sech1 about it?     

> __< j​berman:monero.social >__ Another interesting benefit: a node can sync block headers first, checking PoW, and then start doing verification/tree building in parallel with a solidly optimal construction that maximizes CPU utilization (how I believe evoskuli is doing for Bitcoin)     

> __< j​berman:monero.social >__ Not familiar, what issue are you referring to there?     

> __< r​ucknium:monero.social >__ Let's move on to the agenda items. Maybe pick this back up after     

> __< r​ucknium:monero.social >__ 3) [Gao, Y., Piškorec, M., Zhang, Y., Vallarano, N., & Tessone, C. J. (2025). "Charting the Uncharted: The Landscape of Monero Peer-to-Peer Network".](https://moneroresearch.info/267)     

> __< r​ucknium:monero.social >__ There was some initial discussion of this paper in #monero-research-lounge:monero.social : https://libera.monerologs.net/monero-research-lounge/20250424#c520278-c520470     

> __< r​ucknium:monero.social >__ And now, thanks to xmrack , we have two of the paper's authors here: Yu Gao  and Matija Piskorec     

> __< r​ucknium:monero.social >__ Welcome!     

> __< m​atijapiskorec:matrix.org >__ Me and Yu Gao read the discussion that you linked!     

> __< r​ucknium:monero.social >__ Great. Well, how do you want to discuss? Any way is fine.     

> __< m​atijapiskorec:matrix.org >__ We are open to answer any questions you might have     

> __< y​ugao:ifi.uzh.ch >__ We have already read it before     

> __< r​ucknium:monero.social >__ If I recall correctly, the paper wasn't completely clear on whether you were measuring just outbound connections or both inbound and outbound. Of course, one node's outbound is another's inbound, so you can estimate the whole graph, still. But if you wanted to focus on a specific node's connections based only on its data, then you may want to know its inbound connections, too.     

> __< r​ucknium:monero.social >__ So can you directly measure an node's inbound connections?     

> __< y​ugao:ifi.uzh.ch >__ We regard each "connection" as an undirected link; to detect the architecture is the primary task, and we didn't include the incoming or outgoing detection.     

> __< m​atijapiskorec:matrix.org >__ We don't get information about whether a peer is outgoing or incoming from a peer list. So we cannot distinguish between the two     

> __< r​ucknium:monero.social >__ I see. Thank you. Like I stated in the #monero-research-lounge:monero.social  discussion, I am skeptical that an adversary could use the topology measurement to harm the network's integrity or privacy because the topology estimate must be taken over a long period of time, e.g. a week. By the time an adversary has that information, it is not useful for malicious behavior.     

> __< s​pirobel:kernal.eu >__ would the good nodes find each other again in case there is a network shutdown? do you expect the topology to reappear or could it end up differently?     

> __< j​effro256:monero.social >__ I guess you could rule out incoming by connecting to that peer and seeing if its ports are open, yeah? Would distinguishing between incoming/outgoing make a meaningful difference to partitioning attacks? It might make a privacy difference for Dandelion++...     

> __< m​atijapiskorec:matrix.org >__ I agree with this - we have to collect data for a period of time in order to calculate a statistic     

> __< a​ntilt:we2.ee >__ i stumbled upon 8 outbound cx you chose. Isn't the default 12 ?     

> __< r​ucknium:monero.social >__ flip flop: I also noticed that. I assume it was a typo (BTC uses 8).     

> __< m​atijapiskorec:matrix.org >__ We don't know whether the topology would be identical between the shutdowns. I would assume most probably not. However, this depends on how peers (white and gray lists) are stored in the node between different runs. I guess that these lists can be used to try to reestablish the connections, but it is not guarantied that this will succeed, so topology would probably be different (e<clipped mess     

> __< m​atijapiskorec:matrix.org >__ specially is enough time elapsed)     

> __< y​ugao:ifi.uzh.ch >__ My understanding is that, from the graph theory perspective, it is not really a big issue, but of course, from the security perspective, it is meaningful, because it allows incoming connections to pose risks.     

> __< a​ck-j:matrix.org >__ Hey Yu and Matija thanks again for joining the meeting. I was wondering if you were aware of the large number of Monero proxy nodes discovered by boog900.  Would these “fake” nodes have an impact on your analysis?     

> __< a​ck-j:matrix.org >__ Feel free to continue your discussion and come back to my question later     

> __< r​ucknium:monero.social >__ I think some of the in/out measurement depends on what actions, exactly, trigger an update to `last_seen`. Actually, recently I have been investigating how that all works.     

> __< m​atijapiskorec:matrix.org >__ I think this is a typo, you are right!     

> __< a​ntilt:we2.ee >__ The only way to find out is to observe the network under real stress. Simulations (i've done those) are notoriously hard to do and need to be optimized against real-world case studies.      

> __< a​ntilt:we2.ee >__ Would it be feasable to collect data regularily ?     

> __< y​ugao:ifi.uzh.ch >__ Do these fake nodes play an active role in the network?     

> __< r​ucknium:monero.social >__ From what I understand of the paper, if inbound connections do not trigger an update to `last_seen`, then the method may only be measuring a specific node's outbound connections (but all connections of reachable nodes if this is measured at all reachable nodes).     

> __< r​ucknium:monero.social >__ Yu Gao: It seems that these nodes only accept inbound connections, but do not establish their own outbound connections     

> __< j​effro256:monero.social >__ They become potential outgoing connections for honest nodes, just like any other node.     

> __< s​yntheticbird:monero.social >__ There are no reasons to believe that they don't participate in block propagation and consensus requirements.     

> __< s​yntheticbird:monero.social >__ but yeah, they are just here to grab poor ignorant nodes and weaken tx anonymity.     

> __< r​ucknium:monero.social >__ Info on the suspected malicious nodes: https://github.com/monero-project/research-lab/issues/126     

> __< m​atijapiskorec:matrix.org >__ We are continuously collecting peer list data from the three Monero nodes that we are running from various locations     

> __< r​ucknium:monero.social >__ MRL has recommended that node operators ban the suspected spy nodes from having connections to their nodes: https://github.com/monero-project/meta/issues/1124     

> __< y​ugao:ifi.uzh.ch >__ Network shutdown is a chance for an eclipse attack, they can refresh the peerlist, top grey_list with fake IPs. The shutdown is a base for this kind of attack     

> __< r​ucknium:monero.social >__ There were some recent patches to vulnerabilities that could crash nodes through p2p communication.     

> __< s​yntheticbird:monero.social >__ don't forget to say it's padillac who found it. I know he want this to be insisted upon.     

> __< m​atijapiskorec:matrix.org >__ We were not aware of these fake proxy nodes! Is there a way to identify them?     

> __< s​yntheticbird:monero.social >__ great question     

> __< j​effro256:monero.social >__ The method to identify them hasn't yet been made public     

> __< r​ucknium:monero.social >__ Matija Piskorec: Yes. Last MRL meeting, it was loosely decided to disclose the method to detect the nodes once an intermediate countermeasure is written.     

> __< r​ucknium:monero.social >__ Which will hopefully happen in a few months or less.     

> __< a​ntilt:we2.ee >__ Looking foreward to the next stressful event... ! Seriously, this data will be helpful.     

> __< 0​xfffc:monero.social >__ Until we have counter measures ready, it is naive to disclose the method.     

> __< s​yntheticbird:monero.social >__ 0xfffc tbf there are other methods available     

> __< r​ucknium:monero.social >__ Info about the recent p2p crash vulnerability patches are in the release nodes: https://github.com/monero-project/monero/releases/tag/v0.18.4.0 and HackerOne disclosures: https://hackerone.com/monero/hacktivity?type=team     

> __< y​ugao:ifi.uzh.ch >__ there is, like active methods     

> __< r​ucknium:monero.social >__ Matija Piskorec: If you look at your data again, these spy nodes should be obvious because they "saturate" their /24 IP address subnets.     

> __< m​atijapiskorec:matrix.org >__ We don't yet have a plan to publish this data. It would be technically challenging (it's GBs of data). But we are open for suggestions and collaboration! :-)     

> __< o​frnxmr:monero.social >__ Xmr used to use 8     

> __< r​ucknium:monero.social >__ That suggests that a malicious party is renting whole /24 subnets to run proxy nodes     

> __< r​ucknium:monero.social >__ ofrnxmr: Do you know when that changed?     

> __< r​ucknium:monero.social >__ Matija Piskorec, Yu Gao : Do you plan to present this paper anywhere at a conference soon?     

> __< m​atijapiskorec:matrix.org >__ Thank you for the suggestion! In the future we might decide to exclude them.     

> __< a​ntilt:we2.ee >__ Can you expand on this scenario ?     

> __< m​atijapiskorec:matrix.org >__ Yu Gao: is presenting in on IEEE ICBC conference in Pisa, 2-6 June. https://icbc2025.ieee-icbc.org/     

> __< r​ucknium:monero.social >__ Matija Piskorec: Well, maybe still include them and write a narrative about them or something. You could elaborate a lot about the facts you found, if you want to speculate a little. On a related topic, you found "supernodes" with very high number of connections (different from the spy nodes that boog900  discovered. As you know, this paper also found that supernodes existed: [Gao<clipped message     

> __< r​ucknium:monero.social >__ , Y., Piškorec, M., Zhang, Y., Vallarano, N., & Tessone, C. J. (2025). "Charting the Uncharted: The Landscape of Monero Peer-to-Peer Network".](https://moneroresearch.info/267)     

> __< r​ucknium:monero.social >__ Great!     

> __< y​ugao:ifi.uzh.ch >__ This is another research idea I am going to simulate, but it is very early stage, maybe I will share it in the future?     

> __< r​ucknium:monero.social >__ I wonder if the supernodes are nodes of mining pools that want to propagate their blocks as quickly as possible. Or other honest services. Or they could be trying to spy, but Dandelion++ is designed to defend against supernodes since the stem phase propagates txs to outbound connections.     

> __< s​pirobel:kernal.eu >__ is there the possibility to implement a reputation system to prevent these kinds of eclipse attacks? It seems like using ips to make it expensive to run fake peers is duct tape. would be a great research topic     

> __< y​ugao:ifi.uzh.ch >__ Rucknium: I am also going to your MorKon5 workshop.     

> __< o​frnxmr:monero.social >__ 2020 https://github.com/monero-project/monero/commit/c67fa324965268cd1c01cbcb513038e7344f35d1     

> __< r​ucknium:monero.social >__ Fantastic. I will be presenting there, too, but remotely.     

> __< a​ntilt:we2.ee >__ i have some ideas regarding WoT -- last agenda item.     

> __< s​yntheticbird:monero.social >__ WebOfTrust?     

> __< 0​xfffc:monero.social >__ Videos will be available immediately?     

> __< a​rticmine:monero.social >__ Thanks. I actually thought the number of connections change was earlier     

> __< r​ucknium:monero.social >__ 0xfffc: My videos will be available immediately since they will be pre-recorded and available on Vimeo (or possibly another public site). I think MoneroKon organizers need some time to post edited versions of most in-person presentations. You can ask in #monerokon:matrix.org  for more info.     

> __< r​ucknium:monero.social >__ boog900 has suggested that the default number of outbound connections could go even higher if and when a more bandwidth-efficient tx relay protocol is implemented. 0xfffc  said at the beginning of the meeting that he was working on it.     

> __< a​ck-j:matrix.org >__ Yu Gao: maybe I missed it but did you publish the list of super node IP addresses?     

> __< y​ugao:ifi.uzh.ch >__ no     

> __< y​ugao:ifi.uzh.ch >__ We totally understand the responsibility of analysing DLT networks.     

> __< r​ucknium:monero.social >__ Here is the new tx relay proposal: https://github.com/monero-project/monero/issues/9334     

> __< o​frnxmr:monero.social >__ A higher number would probably improve a majority pruned-node environment, but w/o tx-relay improvements, it adds a lot of latency     

> __< 0​xfffc:monero.social >__ Yes. Boog is implementing for cuprate. I have started monerod tx relay     

> __< 0​xfffc:monero.social >__ Let me find the links     

> __< o​frnxmr:monero.social >__ Theres also in-progress code for this     

> __< o​frnxmr:monero.social >__ The main problem with increasing outbound is putting a bottleneck on the minority nodes who accept incoming connections     

> __< a​ck-j:matrix.org >__ Yu Gao: would you consider disclosure of the super node IP addresses to the Monero VRP via hackerone?     

> __< o​frnxmr:monero.social >__ In a network where only 1/10 nodes have incoming connections, the singke node has to handle all of the traffic. We set incoming to unlimited by default, bur in practice most node will bottleneck-out at 100-1000 connections, depending on network haedware, operating system, and uplink speed     

> __< 0​xfffc:monero.social >__ Rucknium

> __< 0​xfffc:monero.social >__ Cuprate:     

> __< 0​xfffc:monero.social >__ https://github.com/Cuprate/cuprate/pull/407     

> __< 0​xfffc:monero.social >__ Monerod:      

> __< 0​xfffc:monero.social >__ https://github.com/0xFFFC0000/monero/pull/60     

> __< a​ntilt:we2.ee >__ for the record, in a stress situation, less cx will be more resilient (in all likelyhood)     

> __< o​frnxmr:monero.social >__ So increasing outbound is, imo, abbad idea at a certain point. Cant use up "all" of the incoming slots by abusing our outbound connections     

> __< m​atijapiskorec:matrix.org >__ In principle we are open to disclosing any information (data, code) related to our paper to the Monero team.     

> __< r​ucknium:monero.social >__ The paper says, "Our results show that the network is highly centralized around several super nodes with significant betweenness centrality and high degrees. While this centralization strengthens security and robustness, it also introduces potential vulnerabilities."     

> __< r​ucknium:monero.social >__ Technically, yes the graph metrics would show more centrality when a few nodes decide to set a high non-default number of outbound connections. However, is it centralized in a meaningful way? If the supernodes didn't exist, would the network be in a better or worse state?     

> __< o​frnxmr:monero.social >__ i assume the supernodes are what i am referring to. Most non-supernodes are exhausted much more easily     

> __< o​frnxmr:monero.social >__ Increasing outbound connections exacerbates this problem     

> __< 0​xfffc:monero.social >__ Skimmed the paper, my questions too 👆🏻   

> __< o​frnxmr:monero.social >__ (Even with improved tx-relay)     

> __< o​frnxmr:monero.social >__ If the supernodes didnt exist, the question is: do the remaining nodes have enough inbound slots to service the nerwork     

> __< b​oog900:monero.social >__ I'm not saying we should wack the number of connections stupid high, but with the new protocol reducing bandwidth usage by 75%+ we could double the number connections and still be using less bandwidth overall (assuming linear growth which isn't the case with the new protocol, it should be less).     

> __< o​frnxmr:monero.social >__ Bandwidth isnt the bottleneck here, its the number of inbound connections available to the network     

> __< r​ucknium:monero.social >__ IIRC, there have been a couple of papers that worry that BTC's default 8 outbound connections is too low.     

> __< a​ntilt:we2.ee >__ The view needs to be dynamic and individualistic. nodes may decide for themselves (UI?)     

> __< o​frnxmr:monero.social >__ In would assume that less than 50% kf nodes on the network are reachable via incoming due to nat, shared ip, etc     

> __< rbrunner >__ I uploaded 41 GB over 11 hours today on an unrestricted node. So not sure about " Bandwidth isnt the bottleneck here" ...     

> __< r​ucknium:monero.social >__ rbrunner: found the supernode operator :P     

> __< rbrunner >__ Lol     

> __< o​frnxmr:monero.social >__ what is an "unrestricted node"?     

> __< y​ugao:ifi.uzh.ch >__ It depends on how we define centralisation. If the nodes have a lot of connections, for instance is the mining pool nodes, then it has super computing power and an advantage to get more rewards, something like this, and also if the super nodes shut down, the network is easily disconnected     

> __< rbrunner >__ No limits on number of incoming, no speed limit     

> __< o​frnxmr:monero.social >__ and is your rpc public?     

> __< rbrunner >__ No     

> __< o​frnxmr:monero.social >__ 41gb isnt a lot. Its like 1/4 of a node syced from you     

> __< o​frnxmr:monero.social >__ i highly doubt the 42gb is due to txrelay     

> __< 0​xfffc:monero.social >__ > and also if the super nodes shut down, the network is easily disconnected     

> __< 0​xfffc:monero.social >__ I have problem with this part. I can’t imagine what kind of network / graph is that.     

> __< a​ntilt:we2.ee >__ thats hard to predict.     

> __< o​frnxmr:monero.social >__ Its because most nodes dont have incoming connections, so those nkdes _must_ make their connections to those who do, leading to centralization around the ones that do     

> __< b​oog900:monero.social >__ how many connections rbrunner? on average doesn't have to be exact     

> __< rbrunner >__ 100 or so     

> __< o​frnxmr:monero.social >__ If 80% of the connections on the network are directed at supernodes, that implies that the rest of the network's incoming is likely exhausted     

> __< r​ucknium:monero.social >__ Yu Gao: Matija Piskorec : By the way, MRL has powerful scientific computing hardware if you ever did want to share data with MRL so that MRL researchers could look at it, too. Or if something needed a lot of RAM and threads.     

> __< y​ugao:ifi.uzh.ch >__ I believe a general node would not intentionally modify its config file to get a lot of connections.     

> __< r​ucknium:monero.social >__ One machine with 256GB of RAM and another with 1TB of RAM.     

> __< j​effro256:monero.social >__ Current impl of the node node picks more-recently-succeeded outgoings with high probability, so perhaps the network strongly coalesces around nodes which have high uptime     

> __< r​ucknium:monero.social >__ About 100 inbound connections on nodes with open ports is very common, AFAIK.     

> __< r​ucknium:monero.social >__ Yu Gao: By default, Monero nodes accept an unlimited number of inbound connections.     

> __< m​atijapiskorec:matrix.org >__ My opinion is that centralization is a bit ambiguous word - we can measure centrality in many different ways. And of course, more or less centralization is not necessarily a good or a bad thing, because it affects the network in different ways. So it's hard to say whether removing the supernodes would make the network better or worse.     

> __< 0​xfffc:monero.social >__ ofrnxmr

> __< a​ntilt:we2.ee >__ it would slow down the network, but consensus may be robust. The spam attack hints at that. Future will tell.     

> __< a​ntilt:we2.ee >__ it would slow down the network, but consensus may be robust. The spam attack hints at that. Future will tell.     

> __< a​ntilt:we2.ee >__ Unless a bad actor takes advantage of the situation... i think i get your idea.     

> __< a​rticmine:monero.social >__ This is under 10Mbps. It does indicate that upstream bandwidth can be a limitation     

> __< y​ugao:ifi.uzh.ch >__ But inbound connections can be a burden for a general node?     

> __< b​oog900:monero.social >__ from my data in 9334 I would expect about 10GB of that to be tx-relay FWIW     

> __< b​oog900:monero.social >__ the rest is probably a node syncing     

> __< r​ucknium:monero.social >__ Yu Gao: Yes. In the suspected tx spam attack last year, many nodes had big problems because too many txs and too many conenctions.     

> __< r​ucknium:monero.social >__ That is a reason why a Monero "stressnet" was organized last year. A large number of txs were spammed to test problems and correct them.     

> __< o​frnxmr:monero.social >__ Not if they are behind a nat etc, and in practice that is limited by uplink speed and network hardware or os (anywhere from 10-1000 connections)     

> __< a​rticmine:monero.social >__ It can be if they are in a cable as opposed to fibre Internet connection. This is because of the mindset of the cable tv companies     

> __< m​atijapiskorec:matrix.org >__ I have to go now, but thank you everyone for your questions and interest in our paper! You can always reach us via email (they are in the paper) if you have any additional questions or you want to discuss potential collaboration     

> __< o​frnxmr:monero.social >__ Upnp rarely works in my experience, meaning that unless a user manually enables port forwarding, their node does not have incoming.     

> __< b​oog900:monero.social >__ IMO we can double the number of outbound connections with the new relay protocol and still be fine, if individual nodes need to limit connections they should be doing that already.     

> __< o​frnxmr:monero.social >__ Imo we should definitely not     

> __< r​ucknium:monero.social >__ Here is info on what happened on the stressnet: https://www.reddit.com/r/Monero/comments/1eoana8/the_stressnet_so_far/     

> __< b​oog900:monero.social >__ if that is enough to kill the network then the network is more at risk now with the current protocol and connection count     

> __< o​frnxmr:monero.social >__ Not without knowing how many non-superpeer nodes have incoming connections     

> __< j​effro256:monero.social >__ Thank you!     

> __< y​ugao:ifi.uzh.ch >__ sorry Rucknium, I also need to go now. Thanks for reaching out; it's a pleasure to join here, and the great discussions. Feel free to connect with us by email.     

> __< r​ucknium:monero.social >__ Matija Piskorec: Yu Gao Thank you very much for discussing here! I think we will be in touch.     

> __< o​frnxmr:monero.social >__ Its a very simple problem. If there are 150 network participants, but only 10 of them have incoming connections, and limited to 100 connections each = max 1000 incoming connections can be served. If the other 140 nodes have 12 outgoing connections, that is 1680 outgoing slots to fill.     

> __< 0​xfffc:monero.social >__ Why are you saying that? With new tx relay protocol, what’s the problem? Once new tx relay kicks in, the bandwidth usage almost halves     

> __< a​rticmine:monero.social >__ For example here in British Columbia Canada, the Telco offers up to 3 Gbps symmetrical and in some cases 5Gbps symmetrical. The Cable co maxes out at 200 Mbps upstream and in most cases much lower     

> __< o​frnxmr:monero.social >__ This isnt about bandwidth, its about slots     

> __< 0​xfffc:monero.social >__ No, my point was, I don’t see issues doubling slots when we reduced bandwidth usage     

> __< o​frnxmr:monero.social >__ You're not doubling incomibg slots     

> __< o​frnxmr:monero.social >__ Youre doubling the amount of incoming slots that are used up     

> __< a​ntilt:we2.ee >__ move on ?     

> __< o​frnxmr:monero.social >__ Instead of 1680, now those 140 nodes are trying to hold 3360 outgoing connections against 1000 available incoming slots     

> __< r​ucknium:monero.social >__ Nodes with open ports have a strangely high number of inbound connections. If there are no supernodes with non-default outbound conenctions, then about 90% of nodes are unreachable. But probably there are supernodes.     

> __< r​ucknium:monero.social >__ There are a couple more agenda items.     

> __< s​pirobel:kernal.eu >__ web of trust, web of trust (if you chant it, it sounds a bit like one of us, one of us) hyped for this topic as it seems to be at the bottom of all of this     

> __< a​rticmine:monero.social >__ We have to distinguish here between initial node synchronization and ongoing node relay. Nodes with closed ports still have to deal with ongoing node relay     

> __< r​ucknium:monero.social >__ 4) FCMP++ transaction weight formula. https://github.com/seraphis-migration/monero/pull/26     

> __< r​ucknium:monero.social >__ jberman and jeffro256  are working on the requirements for this. They have been discussing in #no-wallet-left-behind:monero.social     

> __< r​ucknium:monero.social >__ Transaction weight is used for the dynamic block weight algorithm and tx fees.     

> __< j​berman:monero.social >__ my latest analysis on FCMP++ tx weight formula is here: https://github.com/seraphis-migration/monero/pull/26#discussion_r2057203539     

> __< 0​xfffc:monero.social >__ Honestly, if we would’ve opened a separate repo for FCMP++ migration would been much more clear. I still have problem understanding what is going on. We do FCMP++ under seraphis migration, we used to have seraphis as protocol. Now we are doing FCMP++     

> __< a​rticmine:monero.social >__ The clawback was implemented to account for verification time with l6 outputs. It is overkill when we are limiting the number of outputs to 8. So I would recommend against it     

> __< 0​xfffc:monero.social >__ ( anyway, not wanna hijack the topic )     

> __< o​frnxmr:monero.social >__ Outputs, and not inputs, right 😏     

> __< j​berman:monero.social >__ Wonder how verification time on an 8-input FCMP++ membership proof compares to a 16-output BP/BP+, guessing it's higher by a solid amount/and the scaling properties much more pronounced for FCMP++ than for BP/BP+?     

> __< j​effro256:monero.social >__ Verification is still >5x slower for an 8-input tx, whereas the size is only <2x     

> __< o​frnxmr:monero.social >__ i'm 100% against limiting inputs to 8     

> __< o​frnxmr:monero.social >__ tobtoht

> __< j​effro256:monero.social >__ Or are you referring to the BP+ clawback?     

> __< b​oog900:monero.social >__ but what about the load on nodes 😏     

> __< a​rticmine:monero.social >__ Yes     

> __< o​frnxmr:monero.social >__ what about load on nodes when i need to chain 10 tx together.     

> __< j​effro256:monero.social >__ We can re-use the BP+ clawback code for FCMP++ weight, it's like less than 10 extra lines, so it's not too much of a hassle if it brings us a more accurate pricing IMO     

> __< o​frnxmr:monero.social >__ Its not like we magically limit the number of inputs used per day by limiting the number usable per tx to some unrealistically low number     

> __< j​berman:monero.social >__ reusing BP+ clawback code exaclty had the problem of incentivizing fewer input combinations into more txs versus 1 tx for all inputs, which is why I made that algo similar to bp+ clawback with those tweaks     

> __< a​rticmine:monero.social >__ It does not improve pricing especially if we can improve on parallel processing for verification. Unbound bandwidth is the biggest limitation     

> __< b​oog900:monero.social >__ they scale up the next power of 2 right? 1 17 input tx is more expensive to verify than a 16 + 1 input txs or whatever.     

> __< o​frnxmr:monero.social >__ Not from my understanding (or lackthereof)     

> __< a​rticmine:monero.social >__ This comes down to the cost and availability of bandwidth vs parallel processing compute time     

> __< a​rticmine:monero.social >__ More correctly unbound bandwidth     

> __< j​berman:monero.social >__ you wouldn't need to chain fwiw if you want to have comparable ux to today, you could construct multiple txs at one time. the idea behind the 8-input limit was to be able to verify a single tx in reasonable time for tx pool processing     

> __< o​frnxmr:monero.social >__ thats what i mean by chaining     

> __< j​effro256:monero.social >__ Yes this is sort of true. It's not exactly powers of two like Bulletproofs, but this is more or less correct     

> __< o​frnxmr:monero.social >__ Making me send 5 separate tx for 1 payment     

> __< a​rticmine:monero.social >__ The limit makes sense but it makes additional weights redundant     

> __< j​effro256:monero.social >__ Sorry, not like Bulletproofs *as we use them for range proofs*     

> __< j​effro256:monero.social >__ B/c FCMPs also use Bulletproofs underneath     

> __< j​effro256:monero.social >__ Rather, a variation named GBPs     

> __< r​ucknium:monero.social >__ I think that last time MAX_INPUTS/MAX_OUTPUTS was discussed, it was decided to take up the question again once the optimized code is settled and there are benchmarks for everything.     

> __< o​frnxmr:monero.social >__ from a purely UX standpoint, i'm against a limit below... the tx size limit 🙃     

> __< a​rticmine:monero.social >__ I recall that discussion     

> __< r​ucknium:monero.social >__ So maybe stay on the topic of just tx weight formula.     

> __< r​ucknium:monero.social >__ Unless the questions cannot be separated at all.     

> __< a​rticmine:monero.social >__ I am saying we don't need  weights just for verification time     

> __< b​oog900:monero.social >__ we must we only have 1 FCMP per tx?     

> __< b​oog900:monero.social >__ why must we only have 1 FCMP per tx?     

> __< b​oog900:monero.social >__ can't we have 1 for each block of 8 or something     

> __< j​berman:monero.social >__ that's a good point^     

> __< a​ck-j:matrix.org >__ kayabanerve:     

> __< j​effro256:monero.social >__ AFAIK, there isn't anything stopping us cryptographically     

> __< a​rticmine:monero.social >__ Also FCMP has to use a fixed weight for a given number of outputs to address changes in the number of layers     

> __< j​effro256:monero.social >__ I remember that there was code written just like this for Bulletproofs, where it broke down the number of outputs into its bit-wise decomposition, and put as many BPs as there were 1 bits in the output count. I can't remember why it wasn't used in production     

> __< j​berman:monero.social >__ interesting, I didn't know that     

> __< b​oog900:monero.social >__ yeah the number of BPs in a tx is dynamic per serialization it is enforced to 1 though by consensus.     

> __< j​berman:monero.social >__ jeffro256 proposed an idea to use a constant number of layers in the weight calculation and I support the idea, reasoning is here:  https://github.com/jeffro256/monero/blob/fcmp%2B%2B-stage-weight/src/cryptonote_basic/cryptonote_format_utils.cpp#L510-L531     

> __< r​ucknium:monero.social >__ I guess I am wrong, but I thought more inputs added to the same FCMP does not increase the verification time per input. So breaking them up does not improve verification time. And the storage size per input of a FCMP actually _decreases_ as input number increases. These were my interpretation of kayabaNerve's numbers, which were theoretical, but not direct code benchmarks.     

> __< a​rticmine:monero.social >__ Yes I agree. If the number of layers changes the weight does not change. I support this     

> __< j​effro256:monero.social >__ jberman: I removed the multiple-BP construction code in this PR: https://github.com/monero-project/monero/pull/9717. This is what it used to look like:https://github.com/jeffro256/monero/blob/2e8a128c752a3cee2a0bee43b3c15ae7ec344792/src/ringct/rctSigs.cpp#L1202-L1240     

> __< a​rticmine:monero.social >__ Keeping the weight constant over a layer change is very important for scaling     

> __< j​effro256:monero.social >__ It does increase time-per-input once you hop over a power-of-2 boundary, which I think is what happens for a 5-input under jberman's benchmarks, I would have to check again. Much like how going from proving 8 range proofs to 9 means you pay for 16     

> __< r​ucknium:monero.social >__ I think this will be an ongoing discussion. Let's try to get a few words in about the Web of Trust for peer selection idea.     

> __< r​ucknium:monero.social >__ 5) Web-of-Trust for node peer selection     

> __< r​ucknium:monero.social >__ I forgot to put this on the posted agenda 😬     

> __< j​berman:monero.social >__ tbc, we're at ~150mn or so outputs today, we bump to 7 layers at ~320mn, 8 layers at 12bn, 9 at 200bn+     

> __< r​ucknium:monero.social >__ flip flop: Do you want to discuss Web-of-Trust?     

> __< a​ntilt:we2.ee >__ i'll shoot a text but we can discuss next time     

> __< a​ntilt:we2.ee >__ A naive rating system as in pgp key signing may backfire - bad actors (20% spynodes) may be faster to sign each other than the rest of us. Local F2F nets are a different application compared to global consensus.      

> __< a​ntilt:we2.ee >__ I'd rather expand on /anchor nodes/ by proofing good behaviour such as availability, contribution to consensus, etc. The idea is that an adversary may have trouble faking such a track record (which may give more weight to old entries). Ideally a big database could be avoided. Thats just a theoretical idea atm.     

> __< r​ucknium:monero.social >__ flip flop: Sounds good.     

> __< r​ucknium:monero.social >__ We can end the meeting here. Thanks everyone.     

> __< a​ntilt:we2.ee >__ bye!     

> __< s​yntheticbird:monero.social >__ thanks     

> __< s​yntheticbird:monero.social >__ delicious meeting     

> __< a​rticmine:monero.social >__ Thanks     

> __< o​frnxmr:monero.social >__ Ty     

> __< r​ucknium:monero.social >__ jeffro256: Maybe what I was seeing was the total verification time cost, given current user behavior. In other words, the txs that used to have many inputs would have to follow a consolidation sequence. The consolidation sequence would use the max power of two to do the consolidations, so it would be efficient.     

> __< 0​xfffc:monero.social >__ Thanks everyone for great meeting     

> __< r​ucknium:monero.social >__ In here: "Monero FCMP MAX_INPUTS/MAX_OUTPUTS empirical analysis" https://gist.github.com/Rucknium/784b243d75184333144a92b3258788f6     

> __< j​berman:monero.social >__ fwiw kayabanerve  did also discuss including multiple proofs in 1 tx here: https://gist.github.com/kayabaNerve/dbbadf1f2b0f4e04732fc5ac559745b7     

> __< j​berman:monero.social >__ reasoned against it for bandwidth reasons and to avoid having a single tx take seconds to verify. I think the latter is still a reasonable point of contention when allowing multiple proofs in 1 tx (imagine including many valid proofs and then 1 invalid at the back)     

> __< j​effro256:monero.social >__ I don't think including very many almost-correct proofs in 1 transaction is any different from including very many txs in an almost-correct set of txs, as long as you verify each FCMP individually     

> __< j​effro256:monero.social >__ We would want to put a max size on each FCMP obviously     

> __< j​berman:monero.social >__ Presumably the RPC would limit to 1 tx per submission, and I guess blocks other RPC submissions     

> __< b​oog900:monero.social >__ yeah we are going to be paying the bandwidth cost anyway just over many txs     

> __< b​oog900:monero.social >__ for UX I think having a single tx is better and the verification/bandwidth cost is the same as if it was split into multiple txs     

> __< j​effro256:monero.social >__ It's also better for services which depend on certain on-chain actions being atomic     

> __< j​effro256:monero.social >__ True, which isn't much different than blocking to verify each FCMP individually     

> __< j​berman:monero.social >__ Fair counter-points imo     

> __< j​berman:monero.social >__ There's also the argument that requiring more txs = more outputs = more FCMP++ proofs to verify longer term too     

> __< b​oog900:monero.social >__ kayabanerve: also said here that 5 4 input FCMP would verify quicker than 1 16: https://github.com/monero-project/meta/issues/1102     

> __< b​oog900:monero.social >__ > <k​ayabanerve:matrix.org > If the block only has a single 16-input transaction, that single proof will cost us thousands of scalar multiplications alone. If we had 5 4-input transactions (which is how they'd be aggregated under MAX_INPUTS=4), the computational complexity would be a fraction.     

> __< b​oog900:monero.social >__ > < k​ayabanerve:matrix.org > (as the 4-input TXs would reasonably share their base cost with other TXs, making their cost an amortized percentage of the base cost and only the per-proof costs)     

> __< b​oog900:monero.social >__ If I understand correctly.     

> __< j​effro256:monero.social >__ Maybe I'm misunderstanding, but I think the point Kayaba is trying to make is that you can verify four 4-input TXs at a time, whereas you can only use 1 core for a 16-input, so your real-time difference between starting to verify and stopping is 4x, even though total CPU time is the same     

> __< j​effro256:monero.social >__ Which is especially important for tx propagation time     

> __< j​effro256:monero.social >__ That's also assuming that the 16-input tx is using 1 FCMP, not multiple     

> __< a​rticmine:monero.social >__ Yes of course. One can parallel process the 4 4input txs     

> __< a​rticmine:monero.social >__ Independently of each other     

> __< j​berman:monero.social >__ Steel-manning kayaba's argument using mine and kayaba's figures:     

> __< j​berman:monero.social >__ To DoS a node, an attacker would hammer it perpetually, hogging bandwidth/CPU time     

> __< j​berman:monero.social >__ Allowing uncapped input limits, each malicious IP gets an estimated/untested 2s of a CPU thread for a bad tx (and more bandwidth expended over a shorter period)     

> __< j​berman:monero.social >__ Capping input limits to 8: each malicious IP gets ~200ms of a CPU thread for a bad tx     

> __< j​berman:monero.social >__ So the same attack when capping limits would require 10x more IP's to perpetually pull off the same attack     

> __< j​berman:monero.social >__ If you spread out more txs with input limits, it still requires more IP's to submit the bad txs that maliciously hog the node get your IP blocked     

> __< j​effro256:monero.social >__ > Allowing uncapped input limits, each malicious IP gets an estimated/untested 2s of a CPU thread for a bad tx (and more bandwidth expended over a shorter period)     

> __< j​effro256:monero.social >__ This is assuming 1 FCMP per transaction though, yeah?     

> __< b​oog900:monero.social >__ I mean txs are sent in batch + we could verify each FCMP in a tx one by one     

> __< b​oog900:monero.social >__ If the batching is seen as a potential issue     

> __< b​oog900:monero.social >__ Which should work out the same if we have multiple fcmp per tx or multiple txs     

> __< j​berman:monero.social >__ I don't think batching is the primary issue. Even if you do allow batching and then process serially, each good tx is fine. The problem is that a bad tx would take (hypothetically) 2s to verify which is then hogging the CPU     

> __< j​berman:monero.social >__ That's on verification time alone. If we also factor in bandwidth and the RPC limits to 1 per submission, then the same underlying issue kayaba is pointing out is there (each bad tx per IP hogs significantly more bandwidth)     

> __< a​rticmine:monero.social >__ A large number of input TX because of it's size would attract a very large penalty if it is added at the penalty threshold. This type of TX should require a much larger node relay fee to ensure it is mined.      

> __< a​rticmine:monero.social >__ This leads to a spam attack where nodes are flooded with large input TXs the majority of which would not get mined.      

> __< a​rticmine:monero.social >__ If large input TXs are allowed the best way I see to deal with them is to have a significantly higher minimum node relay fee that would pay the penalty at the threshold. Increasing the weight for  these TXs is not a solution and can actually make the problem worse     

> __< j​berman:monero.social >__ Ya, we could require node relay fees for large input txs and moneromoo did already set that sort of thing up     

> __< a​rticmine:monero.social >__ I am not in favor of large input TXs  by the way     

> __< j​berman:monero.social >__ to be clear, I'm referring to a node relay fee not included in the tx, but would need to be paid to a node directly in order for the node to accept processing a large input tx     

> __< a​rticmine:monero.social >__ Keep it simple and pop at the fee to the miner. Why would the miner mine these TXs at a loss?     

> __< b​oog900:monero.social >__ I'm not even sure fees really help here, someone could create double spends of the same inputs and then got a lot of txs for "free" as they wont ever be mined     

> __< a​rticmine:monero.social >__ Pay the fee to the miner     

> __< j​berman:monero.social >__ (and then it becomes a problem on the p2p relay side though)     

> __< b​oog900:monero.social >__ the maximum you could go is 1 double spend per node     

> __< a​rticmine:monero.social >__ Why should nodes relay a mass of doubly spends?     

> __< b​oog900:monero.social >__ if a tx take a while to verify a lot of double spends will cause a DoS with little cost + no banning     

> __< j​berman:monero.social >__ maybe we layer on pow hashing for submitting/relaying txs lol, pow hash paid for by tx creator     

> __< j​effro256:monero.social >__ I was thinking the same thing     

> __< a​rticmine:monero.social >__ No . This discriminates against rho who live in the tropics     

> __< b​oog900:monero.social >__ I do think that is the only valid solution     

> __< b​oog900:monero.social >__ fees only count for txs in blocks     

> __< b​oog900:monero.social >__ even paying fees to transfer only counts if the tx is included in a block     

> __< a​rticmine:monero.social >__ It is not a solution. Just launch the attack from Canada during the winter A good -40 temperature should do the trick     

> __< a​rticmine:monero.social >__ POW hashing to send transactions is a terrible idea     

> __< j​effro256:monero.social >__ The computational cost wouldn't be anywhere close to block difficulty, just enough that it's some multiple >1 of cost to verify an FCMP , and the hash wouldn't be re-usable for mining     

> __< a​rticmine:monero.social >__ Russia would also work     

> __< b​oog900:monero.social >__ p2pool has PoW for connections ....     

> __< b​oog900:monero.social >__ i guess that is mining so it doesn't matter as much     

> __< j​berman:monero.social >__ tor introduced it ya?     

> __< a​rticmine:monero.social >__ The computational cost is very dependent on the outside temperature. This kind of thing does not belong in Monero     

> __< j​effro256:monero.social >__ Doing a PoW-based attack, even in Russia or Canada, where the heating is "free", still costs something because of opportunity cost. If you're expending all this effort, that's CPU time that isn't being used for mining XMR     

> __< a​rticmine:monero.social >__ One is using CPUs     

> __< b​oog900:monero.social >__ For non-attackers this cost should be minimal     

> __< a​rticmine:monero.social >__ Not if you are in the Australian outback during the summer or in India during a heat wave     

> __< j​berman:monero.social >__ It should be fine even for them     

> __< a​rticmine:monero.social >__ Your device is already overheating and one forces POW?     

> __< a​rticmine:monero.social >__ Charge a fee in XMR intead     

> __< a​rticmine:monero.social >__ Instead     

> __< j​effro256:monero.social >__ Single-digit seconds of CPU time won't be enough to even warm your hand. By that logic, Monero requiring stealth addresses, and thus 1 ECDH per enote to scan is discriminatory. That takes way more CPU time for honest users     

> __< j​berman:monero.social >__ 1) I'm betting it's almost certainly going to be less CPU power than scanning the chain, 2) it could only be required for higher input txs     

> __< b​oog900:monero.social >__ I would bet creating the tx would cost more than the PoW     

> __< s​yntheticbird:monero.social >__ 2) is an interesting twist     

> __< b​oog900:monero.social >__ the PoW only has to be more than verification     

> __< j​berman:monero.social >__ ^     

> __< j​berman:monero.social >__ ^ in reponse to "I would bet creating the tx would cost more than the PoW"     

> __< a​rticmine:monero.social >__ Why not simply require a higher fee?     

> __< b​oog900:monero.social >__ you can't - this only effects txs in blocks     

> __< b​oog900:monero.social >__ tx-pool txs can be double spent     

> __< j​berman:monero.social >__ we're discussing nodes processing the txs before they enter their pool     

> __< j​effro256:monero.social >__ The point is that you can't validate a transaction until after you do. You could require a higher fee, but you can't actually check it w/o expending CPU time for verification     

> __< a​rticmine:monero.social >__ A node relay fee     

> __< b​oog900:monero.social >__ ay yes the tx before the tx     

> __< b​oog900:monero.social >__ which also needs a tx ...     

> __< b​oog900:monero.social >__ or we paying with fiat?     

> __< j​berman:monero.social >__ also this     

> __< j​berman:monero.social >__ would have to pay fees for every relay to every node too     

> __< j​effro256:monero.social >__ How do you check the node relay fee without verifying a transaction?     

> __< a​rticmine:monero.social >__ One just increases the node relay fee paid to the miner. This would provide deterrence     

> __< s​yntheticbird:monero.social >__ no     

> __< a​rticmine:monero.social >__ One cannot stop invalid transactions with source POW     

> __< s​yntheticbird:monero.social >__ at least if i wanted to dos the network I wouldn't be deter     

> __< s​yntheticbird:monero.social >__ (I want to dos the network and this is a confession that im a bad actor acting against monero's interest)     

> __< b​oog900:monero.social >__ currently ~5k nodes on the network I can double spend an input ~5k times and send a different tx to each node cutting my cost by 5000     

> __< b​oog900:monero.social >__ no but it adds cost     

> __< b​oog900:monero.social >__ to make my node do work, you must have to do work     

> __< a​rticmine:monero.social >__ I can do the work when it is -40 C and make you work at 40 C     

> __< s​yntheticbird:monero.social >__ *Equal rights for monero p2p agents!*     

> __< j​berman:monero.social >__ there is a question of if it's enough PoW to even stop the DoS. If this holds, which I believe it does thanks to ec divisors, then the PoW really only max 2x's the cost to the attacker. It would really have to be a more significant PoW to work     

> __< j​effro256:monero.social >__ The nature of PoW is that it is much easier to verify work than to create work. It wouldn't necessarily be a 1-to-1 cost     

> __< j​berman:monero.social >__ the PoW could only be required for large input counts though and scale up as input counts increase     

> __< b​oog900:monero.social >__ If we are talking about getting rewarded for work then yes that would be bad. You have to solve 1 puzzle to send a tx, the puzzle will cost less than creating the tx (probably).     

> __< b​oog900:monero.social >__ If we are talking about discriminating against attackers then yes you are right.     

> __< j​effro256:monero.social >__ That doesn't really matter to the verifier. A valid transaction could take 24 hours to create, but the verifier only cares about verification time. It takes 0ms to make a bad elliptic curve divisor     

> __< a​rticmine:monero.social >__ One of the biggest misconceptions of POW is that people ignore the value or cost or the heat producedi     

> __< j​berman:monero.social >__ that's true, but point being, it would probably have to be a solidly costing PoW     

> __< b​oog900:monero.social >__ the goal isn't for someone to be pumping PoW all day to send txs     

> __< b​oog900:monero.social >__ the tx generation/scanning process will generate more heat     

> __< s​yntheticbird:monero.social >__ Are there really no distinguishable characteristics that could permit a node to "predict" a margin of computation time it would take ?     

> __< r​ucknium:monero.social >__ Won't a RandomX PoW requirement (even for high-input txs) entrench RandomX in wallet code? IIRC, there was a suggestion to eventually eliminate all PoW-related code from wallets to reduce malware false positives.     

> __< s​yntheticbird:monero.social >__ Monero CEO will have to buy the 999k$ Micro(talent)soft approved certificate     

> __< j​berman:monero.social >__ curious if equix gets flagged too https://spec.torproject.org/hspow-spec/v1-equix.html     

> __< a​rticmine:monero.social >__ This is a very valid point. One more reason to keep POW away from wallets     

> __< j​berman:monero.social >__ we could see how long it would take a reference CPU to construct the PoW and enforce that difficulty     

> __< j​effro256:monero.social >__ Yes and no. No if, like in the current situation today, all wallets submit transactions to daemons's RPC. Daemons inherently already have RandomX code. It would prevent a hypothetical wallet from existing which submits transactions to the p2p interface of another daemon, *and* doesn't need RandomX code.     

> __< s​yntheticbird:monero.social >__ lr     

> __< j​berman:monero.social >__ fwiw I also don't think windows hostile and easily reversible decisions should affect Monero protocol decisions in this regard     

> __< j​effro256:monero.social >__ But submitting transactions to another's daemon p2p interface directly as a non-daemon is obviously horrible for privacy if not done correctly.     

> __< s​yntheticbird:monero.social >__ Sorry, I meant for FCMP tx verification     

> __< s​yntheticbird:monero.social >__ not PoW     

> __< j​berman:monero.social >__ oh I see, ya! by looking at how many inputs are the proof, the node can predict a margin of computation time it would take     

> __< j​berman:monero.social >__ to verify     

> __< j​berman:monero.social >__ sort of     

> __< a​rticmine:monero.social >__ ... and not relay, or at least delay relay     

> __< j​berman:monero.social >__ I mean ya for sure. the node could theoretically even verify all input combos on boot and measure timings. I'm sure there's a better way to do it though     

> __< s​yntheticbird:monero.social >__ There could be a formula for forcing source PoW or other mechanism on (predicted) time consuming txs     

> __< a​rticmine:monero.social >__ Realistically if large input TXs are an attack vector, which I agree with, can't we just limit this at the protocol level?     

> __< j​effro256:monero.social >__ Yeah FCMP verification time is more-or-less a constant function of (number of inputs, number of tree layers), both of which are provided explicitly in the transaction.     

> __< j​effro256:monero.social >__ Yes, but at the cost of not having large input TXs: UX degradation, the time delay that input consolidation brings, and worse liveness / atomicity guarantees for services     

> __< j​effro256:monero.social >__ If we allow high-input TXs at a consensus level, we can always tack on relay rules or PoW or miner relay fees or whatever else afterwards. But if we reject it at a consensus level, then we would need a hard fork to bring them back     

> __< b​oog900:monero.social >__ wont txs with multiple FCMPs naturally have PoW built in. The worry is if the last proof is invalid the whole thing has the be thrown away but the person still has to construct multiple valid proofs then they had to put in work     

> __< a​rticmine:monero.social >__ This is a very valid point. We can restrict or penalize  them at node relay     

> __< a​rticmine:monero.social >__ I am fine with that     

> __< j​berman:monero.social >__ boog900: this why I'm arguing the PoW should probably be significantly greater than cost to construct the tx for txs with higher n inputs, and should scale by n inputs in the tx     

> __< j​effro256:monero.social >__ Not if it's an invalid FCMP, then it's basically free to make     

> __< j​effro256:monero.social >__ The cost should scale, not because of honest construction time, but because of verification time     

> __< j​berman:monero.social >__ boog is saying the earlier FCMPs packed in would be valid, and then a later one would be invalid     

> __< b​oog900:monero.social >__ yeah but the argument was that multiple FCMPs was equivalent to a single FCMP if the last is invalid, as they both waste significant work if invalid     

> __< b​oog900:monero.social >__ but they aren't as you need to put work in for multiple valid FCMPs     

> __< a​rticmine:monero.social >__ I have a serious concern with POW at the wallet level. Requiring POW to access P2P pool is completely different since the users in that are contributing hash power     

> __< j​effro256:monero.social >__ Ah yes true, sorry my misunderstanding     

> __< b​oog900:monero.social >__ here^     

> __< j​effro256:monero.social >__ Tbf, it wouldn't be at the wallet level, it would be at the daemon level in the p2p protocol     

> __< b​oog900:monero.social >__ this makes multiple FCMPs per tx equivalent to multiple txs with 1 FCMP, right?     

> __< j​berman:monero.social >__ I would think it would be at the wallet level too to protect public RPC's     

> __< r​ucknium:monero.social >__ Why would nodes be the entities creating the PoW? If I am a node, why would I bother creating PoW to relay a tx?     

> __< r​ucknium:monero.social >__ Relaying anything is actually a favor.     

> __< s​yntheticbird:monero.social >__ *You will thanks me for relaying your transaction and you will be happy*     

> __< j​effro256:monero.social >__ Because either A) it's your node and your wallet and you want the tx relayed, B) your node, and users you care about, or C) you're running a public RPC node     

> __< j​effro256:monero.social >__ The point of public RPC is that it's a public service     

> __< s​yntheticbird:monero.social >__ or better     

> __< j​berman:monero.social >__ "this makes multiple FCMPs per tx equivalent to multiple txs with 1 FCMP, right?" -> sorry I'm not following fully following the thread of your argument here. can you rephrase?     

> __< s​yntheticbird:monero.social >__ We allow both mode. If node allows it you can request it to generate the PoW. Otherwise the node can say "nah sorry not to day, please do it yourself"     

> __< a​rticmine:monero.social >__ Very good point     

> __< j​berman:monero.social >__ We probably expect public RPC's to reasonably exist and don't want public RPC's to be exposed to a dos vector, so I think it would make sense that wallets would construct the PoW in the first place     

> __< b​oog900:monero.social >__ The problem was multiple FCMPs in a tx allows for someone to use up a lot of CPU if all the FCMPs are valid except the last. Which is the same as 1 big FCMP in cost to the node.     

> __< b​oog900:monero.social >__ This is different than splitting the tx into multiple different ones with 1 FCMP each as the valid ones will still be added to the pool, therefor are not a waste.     

> __< b​oog900:monero.social >__ However the multiple FCMPs per tx still have a significant cost adding a pseudo-PoW meaning it isn't the same as 1 big FCMP. Also individual txs can be double spent still wasting work.     

> __< b​oog900:monero.social >__ My argument is that we should allow multiple FCMPs per tx as there is no difference.     

> __< s​yntheticbird:monero.social >__ if PoW for relay is introduced I would like it the update to be called FCMP++/Carrot/POWER. because PoW Enabled Relaying.     

> __< s​yntheticbird:monero.social >__ do i welcome any more creative naming     

> __< s​yntheticbird:monero.social >__ tho*     

> __< j​effro256:monero.social >__ I'm not against public RPC operators choosing to block/allow any traffic that they see fit since it's by definition a public service and they're paying for their own server / own internet hookup. But you're inherently opening yourself up to DoS vectors that don't exist if you don't turn on public RPC, so I don't see why it wouldn't be an option     

> __< j​berman:monero.social >__ "My argument is that we should allow multiple FCMPs per tx as there is no difference." -> Not in place of PoW, ya? But as a separate (but related) point?     

> __< b​oog900:monero.social >__ yeah I am saying PoW or not having multiple FCMPs per tx is no worse than multiple txs     

> __< j​berman:monero.social >__ Ya I think that is a reasonable point     

> __< j​effro256:monero.social >__ They only difference I can think of rn is that in between each "checkpoint", or smallest meaningful indivisible unit of computation, if the transaction with 1 FCMP succeeds, someone somewhere is paying a transaction fee. Whereas with a transaction with N FCMPs succeeds and N-1 verify, but the last fails, then no-one pays a tx fee     

> __< j​berman:monero.social >__ Well wait no, I understand. Let's just assume no PoW for now     

> __< j​berman:monero.social >__ The node gets stuck processing a large bad tx that the node would not use. Yes, the client has done work to construct this bad tx, but that work is wasted work compared to having constructed a complete valid tx.     

> __< j​berman:monero.social >__ That would be categorically worse than node getting stuck for 10x less time processing a bad tx     

> __< j​berman:monero.social >__ "Also individual txs can be double spent still wasting work" -> w/current policy, nodes can just quickly reject a key image it has already seen, no? Not following how that is consequential here     

> __< j​berman:monero.social >__ I can (I think) see the argument that with PoW, it still makes sense to have multiple FCMPs per tx     

> __< j​berman:monero.social >__ (Going to have to step away in a sec and come back unfortunately)     

> __< b​oog900:monero.social >__ > w/current policy, nodes can just quickly reject a key image it has already seen, no? Not following how that is consequential here     

> __< b​oog900:monero.social >__ Yeah I thought double spending was checked after the input checks but looking at the code it is checked first, non-input checks like bulletproofs are still checked before the double spend check tho my bad.     

> __< b​oog900:monero.social >__ and yeah it could've just been changed if it was     

> __< j​berman:monero.social >__ np, I actually didn't remember if it is or not, but was just making a point that it could be     

> __< b​oog900:monero.social >__ I do remember bringing that up now as a way to find out if a node has a stem tx or not ...     

> __< b​oog900:monero.social >__ literally unfixable though without introducing this DoS     

> __< j​berman:monero.social >__ tevador explains relevant rationale here for why equix over randomx in tor: https://github.com/tevador/equix/blob/master/devlog.md     

> __< j​berman:monero.social >__ TL;DR faster verification to prevent flooding attacks, and high memory requirement     

> __< j​berman:monero.social >__ Worth thinking it through in our case. Probably don't want to impose too strict of memory requirements on clients, though our allowed verification time could potentially be significantly higher if we don't impose PoW relay reqs on lower input txs     

> __< j​berman:monero.social >__ So maybe the low memory RandomX variant could make sense in our use case     

> __< r​ucknium:monero.social >__ jberman: This is the issue I referred to previosuly: https://github.com/monero-project/monero/issues/8827     

> __< r​ucknium:monero.social >__ > Better security for wallets using untrusted remote nodes. Malicious remote nodes can feed wallets fake blockchain data. With this proposal, wallets could partially verify the integrity of the blocks received from untrusted remote nodes with the cost of a few hashes.     

> __< j​berman:monero.social >__ gotcha thank you     

> __< j​berman:monero.social >__ this seems relatively simple to include in next fork     

> __< j​berman:monero.social >__ and to answer your q "Is this related to the issue that tevador found in the current PoW?" -> checking PoW on block headers is related to including the tree root yep. That idea by tevador would speed up the PoW verification / benefit the approach     

> __< j​berman:monero.social >__ sech1 selsta do you know if anyone has started working on bringing that change into monero for next fork? we can add it to the list of TODO's if not     

> __< selsta >__ sech1 knows best the current status     

> __< sech1 >__ tevador was working on it but he's not active anymore     

> __< sech1 >__ He actually did submit it https://github.com/tevador/RandomX/pull/265     

> __< sech1 >__ It's just RandomX V2 which is not finished yet (RISC-V code is missing for it)     

> __< j​berman:monero.social >__ got it ya, so looks like it's just a matter of implementing that specific change in the monero repo     

> __< j​berman:monero.social >__ / integrating that PR     

> __< j​berman:monero.social >__ *thumbs up* good bump rucknium     

> __< j​berman:monero.social >__ I hope tevador is alright     

> __< r​ucknium:monero.social >__ That's one reason we have regular meetings. To discuss current work plans to make sure possible synergies aren't missed :)     

> __< k​ayabanerve:matrix.org >__ Rucknium: bytes can decrease upon an increase in inputs. It still trends upwards.     

> __< k​ayabanerve:matrix.org >__ jeffro256: Batch verification of four small FCMPs is faster than verification of one large FCMP, even on a single core.     

> __< j​berman:monero.social >__ One thing worth mentioning: if the PoW puzzle also hashes a ref to the latest block in addition to the tx, it removes the attacker's ability to slowly accumulate many bad txs + PoW solutions over a long period of time     

> __< j​berman:monero.social >__ (could also expand the window to be n blocks in case the chain advances after constructing)     


# Action History
- Created by: Rucknium | 2025-04-29T21:21:20+00:00
- Closed at: 2025-05-12T15:04:28+00:00
