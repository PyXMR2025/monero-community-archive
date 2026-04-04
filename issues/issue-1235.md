---
title: Monero Research Lab Meeting - Wed 09 July 2025, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1235
author: Rucknium
assignees: []
labels: []
created_at: '2025-07-08T22:43:55+00:00'
updated_at: '2025-07-18T20:12:01+00:00'
type: issue
status: closed
closed_at: '2025-07-18T20:12:01+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/meeting.html?p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3.  [SLVer Bullet: Straight Line Verification for Bulletproofs](https://github.com/cypherstack/silver-bullet).  [Cypher Stack review of divisors for FCMP](https://github.com/cypherstack/divisor_deep_dive).

4. [FCMP++ optimization coding competition](https://www.getmonero.org/2025/04/05/fcmp++-contest.html).

5. [FCMP alpha stressnet planning](https://github.com/seraphis-migration/monero/issues/53).

6. [Spy nodes](https://github.com/monero-project/research-lab/issues/126).

7.  CCS proposal: [Monero Network Simulation Tool](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/589).

8. Any other business

Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#1231 

# Discussion History
## Rucknium | 2025-07-10T21:24:53+00:00
Logs

> __< g​ingeropolous:monero.social >__ so i never know where i'll be at meeting time, so my updates for today re: monerosim : I think i have an mvp working. well, mvp might be too strong. the nodes start, make blocks, relay them, and im working on confirming that txs get created and relayed.      

> __< g​ingeropolous:monero.social >__ so far though, my thoughts have wandered, and I ponder whether shadow is indeed the best approach for what we want. I think in some perspectives, what shadow offers can be helpful. But, for instance, for testing like the effect of FCMP load on the network, shadows design might be too ... simulated. For instance, they treat CPUs as having infinite speed. So I think the best route f<clipped me     

> __< g​ingeropolous:monero.social >__ or the network as a distributed computational network might be best simulated via some docker thing i came across (we lose reproducability, but I think that can be augmented by just performing repeat sims... like a monte carlo kinda thing). However, if we're interested in how txs and blocks get slung around the network, then I think shadow is the way, due to its internal tick tock<clipped me     

> __< g​ingeropolous:monero.social >__  of events. We might get the best of both worlds by using shadow and figuring out how to simulate the time required for each kind of computation, but for me that is down the line.     

> __< r​ucknium:monero.social >__ MRL meeting in this room in about two hours.     

> __< s​yntheticbird:monero.social >__ 9zsjcz.gif     

> __< g​ingeropolous:monero.social >__ deterministic. thats what i wanted. not reproducible. well, i guess they are related.     

> __< r​ucknium:monero.social >__ Meeting time! https://github.com/monero-project/meta/issues/1235     

> __< r​ucknium:monero.social >__ 1) Greetings     

> __< v​tnerd:monero.social >__ Hi     

> __< a​rticmine:monero.social >__ Hi     

> __< s​gp_:monero.social >__ hi     

> __< j​berman:monero.social >__ *waves*     

> __< rbrunner >__ Hello     

> __< a​ntilt:we2.ee >__ seas     

> __< r​ucknium:monero.social >__ 2) Updates. What is everyone working on?     

> __< r​ucknium:monero.social >__ me: Improvements to the reachable node network scanner. Thread-safe database writing, added Autonomous System (AS) data, AS treemap and concentration index, domain data for the nodes that use domains for public remote nodes, better performance with default static image treemaps, and searchable/filterable table of individual node data in the webapp: https://moneronet.info     

> __< v​tnerd:monero.social >__ Me: docs for LWS, rounding out the lwsf implementation, then getting a fork prepped for lwsf+monero_c     

> __< j​berman:monero.social >__ me: continuing scan_tx for FCMP++ (in discussions with jeffro256 , we agreed it would make sense to remove the ability to scan *future* txs relative to the wallet's current sync height, and to implement ~instant restore at arbitrary height so wallets don't sit downloading any block hashes, see: https://github.com/seraphis-migration/monero/pull/49) and other PR wrangling     

> __< j​effro256:monero.social >__ Howdy     

> __< j​effro256:monero.social >__ Me: catching up on math for divisors review and getting back to working on hot/cold wallets     

> __< r​ucknium:monero.social >__ `lwsf` = Light-wallet server frontend.     

> __< s​gp_:monero.social >__ great! I'm looking forward to the fork/PR     

> __< g​ingeropolous:monero.social >__ heya, i made it. copy pasta from above for the logs: me: so i never know where i'll be at meeting time, so my updates for today re: monerosim : I think i have an mvp working. well, mvp might be too strong. the nodes start, make blocks, relay them, and im working on confirming that txs get created and relayed.      

> __< g​ingeropolous:monero.social >__ so far though, my thoughts have wandered, and I ponder whether shadow is indeed the best approach for what we want. I think in some perspectives, what shadow offers can be helpful. But, for instance, for testing like the effect of FCMP load on the network, shadows design might be too ... simulated. For instance, they treat CPUs as having infinite speed. So I think the best route f<clipped me     

> __< g​ingeropolous:monero.social >__ or the network as a distributed computational network might be best simulated via some docker thing i came across (we lose reproducability, but I think that can be augmented by just performing repeat sims... like a monte carlo kinda thing). However, if we're interested in how txs and blocks get slung around the network, then I think shadow is the way, due to its internal tick tock<clipped me     

> __< g​ingeropolous:monero.social >__  of events. We might get the best of both worlds by using shadow and figuring out how to simulate the time required for each kind of computation, but for me that is down the line.     

> __< r​ucknium:monero.social >__ Thanks for the updates, everyone.     

> __< r​ucknium:monero.social >__ 3) [SLVer Bullet: Straight Line Verification for Bulletproofs](https://github.com/cypherstack/silver-bullet).  [Cypher Stack review of divisors for FCMP](https://github.com/cypherstack/divisor_deep_dive).     

> __< r​ucknium:monero.social >__ Are there update on this item?     

> __< j​berman:monero.social >__ From an implementation standpoint, I believe kayabanerve is still working on implementing the proposed changes     

> __< r​ucknium:monero.social >__ 4. [FCMP++ optimization coding competition](https://www.getmonero.org/2025/04/05/fcmp++-contest.html).     

> __< j​berman:monero.social >__ Divisors still in review (no objections raised so far), helioselene contest ongoing with no new submissions. Reminder the new deadline is tomorrow (July 10, 17:00 UTC)     

> __< j​berman:monero.social >__ New deadline for helioselene*     

> __< j​berman:monero.social >__ Thanks to all for participating in last week's meeting and helping us settle on the decision to open the helioselene contest for all again for 1 additional week     

> __< s​yntheticbird:monero.social >__ lightning fast meeting     

> __< r​ucknium:monero.social >__ There are still three items :)     

> __< r​ucknium:monero.social >__ 5. [FCMP alpha stressnet planning](https://github.com/seraphis-migration/monero/issues/53).     

> __< r​ucknium:monero.social >__ The link^ is to the overall FCMP checklist.     

> __< r​ucknium:monero.social >__ It seems that putting the blinds cache implementation later in the schedule was a lucky decision.     

> __< j​berman:monero.social >__ I wouldn't say lucky exaaaaactly, but yes :)     

> __< r​ucknium:monero.social >__ Luck favors the well-prepared :)     

> __< j​effro256:monero.social >__ I think that we could organize this TODO list in "must-haves" and "nice-to-haves" for a stressnet launch. For example, multisig and vendor-specific HW implemenations probably aren't exactly required for a stressnet     

> __< j​effro256:monero.social >__ And both of those could take a very long time, it doesn't make sense to wait for those for stressnet     

> __< j​berman:monero.social >__ Main must-have TODO's I'd say for a stressnet are: divisors re-impl from SLVer bullet, and settling on fabrizio's submission / pulling it into the code (so that blinds calculations don't take forever)     

> __< j​berman:monero.social >__ The highest priority nice-to-haves I'd say are: optimizing prove, supporting >8 inputs per tx, helioselene contest optimizations, AND dynamic block weight / tx weight changes (ping ArticMine)      

> __< j​berman:monero.social >__ Aside from that, I think the integration code is pretty much ready for an alpha stressnet     

> __< j​effro256:monero.social >__ I would put >8-in on "must-have" for a stressnet, since >8-in would be extremely useful for stressing     

> __< r​ucknium:monero.social >__ Sounds good to me. How much work is >8-in?     

> __< j​effro256:monero.social >__ Other than that, I agree     

> __< r​ucknium:monero.social >__ I wonder if >8-in could be scheduled for the "public" stressnet, later.     

> __< j​berman:monero.social >__ Well, integration side for >8-in is mostly done, it's optimizing prove that I'd say is the main impediment (prove currently is extremely slow far many-input txs when it's not supposed to be)     

> __< a​rticmine:monero.social >__ Noted regarding scaling TX weight dynamic blocksize     

> __< j​berman:monero.social >__ ArticMine possible we can get a pdf like you made for last hf that documents proposed changes? https://github.com/monero-project/monero/pull/7819#issuecomment-889795966     

> __< a​rticmine:monero.social >__ Yes     

> __< r​ucknium:monero.social >__ jeffro256: Do you want to take change of an alpha stressnet TODO list?     

> __< j​effro256:monero.social >__ Yes I can do that today, and just post a distilled list as a comment under the original issue. Would that be good?     

> __< r​ucknium:monero.social >__ Here? I don't see it: https://github.com/seraphis-migration/monero/issues/53     

> __< j​effro256:monero.social >__ Yes that's the GH issue I was talking about. I haven't made the comment yet     

> __< r​ucknium:monero.social >__ Ah, I misunderstood. Sounds good to me. Thank you.     

> __< r​ucknium:monero.social >__ 6) [Spy nodes](https://github.com/monero-project/research-lab/issues/126).     

> __< r​ucknium:monero.social >__ I improved the network node scan webapp: https://moneronet.info     

> __< r​ucknium:monero.social >__ Source code here: https://github.com/Rucknium/xmrnetscan     

> __< r​ucknium:monero.social >__ I improved the network crawler itself. It's thread-safe now and writes most of the data to a SQLite database instead of just a text file.     

> __< r​ucknium:monero.social >__ The first version had to run in a single thread because many threads writing to the same text file caused "corruption". The single-threaded version seemed to not completely finish the scan in a 24-hour window. The new thread-safe implementation, using the `tokio-sqlite` Rust crate, uses 10 threads and finishes in about 3 hours.     

> __< r​ucknium:monero.social >__ I added Autonomous System (AS) data by making API calls to Team Cymru. I got data on the (few) domains that may be associated with remote nodes from ditatompel's API: https://xmr.ditatompel.com/remote-nodes     

> __< r​ucknium:monero.social >__ I added an AS treemap and timeline of AS concentration (the Herfindahl-Hirschman Index). You can see from the AS treemap that all suspected spy nodes seem to be in just three ASes: LionLink, Hetzner, and DigitalOcean. There are also honest nodes in Hetzner and Digital Ocean, but no honest nodes in LionLink.     

> __< r​ucknium:monero.social >__ I also added a searchable/filterable table of individual nodes. From there, you can see if specific remote nodes (with domains) are using the MRL and/or DNS ban lists. I have started to contact some remote node operators to see if they would enable the spy node ban list.     

> __< r​ucknium:monero.social >__ Next, I want to do a write-up of why it may be a good idea to rotate out a few IP addresses from the DNS ban list, which is at maximum capacity, and put in at least the big subnets from the MRL ban list.     

> __< r​ucknium:monero.social >__ And I removed the part of the stacked line graph with the unreachable node data, since there is not really a reliable way, yet, to estimate the number of unreachable nodes.     

> __< r​ucknium:monero.social >__ If you have any ideas about more data and/or plots to add, let me know.     

> __< r​ucknium:monero.social >__ The Herfindahl-Hirschman Index is used in economics to measure market concentration. It is supposed to be a basic metric of industry competitiveness and the risk of large firms using their market power to harm consumer interests.     

> __< c​haser:monero.social >__ this tool is very neat, thank you Rucknium!     

> __< g​ingeropolous:monero.social >__ yeah, really cool. can use it to find "trustable" remote nodes :P     

> __< r​ucknium:monero.social >__ You compute the square of the market share of every firm in a market, then sum those squares.     

> __< r​ucknium:monero.social >__ I was thinking that maybe the info on enabling ban lists can be pulled back into ditatompel's remote node table.     

> __< s​yntheticbird:monero.social >__ would be actually interesting to see on the map which nodes are registered by monero.fail     

> __< s​yntheticbird:monero.social >__ maybe there is some overlap with the spy nodes?     

> __< s​yntheticbird:monero.social >__ They have their RPC port open     

> __< r​ucknium:monero.social >__ This webapp can get far more interactive. The server side of it runs an ordinary R process. Now, it is set up as a dashboard, but it can go further, within reason.     

> __< r​ucknium:monero.social >__ monero.fail has a simple API, but I would have to query each of the domains to get the IP addresses.     

> __< s​yntheticbird:monero.social >__ yes     

> __< s​yntheticbird:monero.social >__ or maybe you could do a reverse dns yourself     

> __< s​yntheticbird:monero.social >__ expanding outside of monero.fail     

> __< s​yntheticbird:monero.social >__ just check which ip have a dns record associated to it     

> __< r​ucknium:monero.social >__ Ah, another thing I did was to confirm that the RPC ports were actually enabled and open. I ping every RPC port that the nodes claim to have. If it responds appropriately to a `get_info` request, then it is counted as having RPC available. Before, I just assume that each node was telling the trust in its Levin handshake.     

> __< r​ucknium:monero.social >__ I looked into reverse DNS. It is more complicated than I thought.     

> __< s​yntheticbird:monero.social >__ fyi, spy nodes have 4 rpc ports opened on the same ip     

> __< j​effro256:monero.social >__ The webapp has a beautiful visualization BTW     

> __< j​effro256:monero.social >__ Were any nodes lying about their RPC port being open? Perhaps some people didn't set up their ports correctly     

> __< r​ucknium:monero.social >__ A "standard" reverse DNS does not get domains. You have to get an API key to a proprietary service like VirusTotal to actually get domains.     

> __< r​ucknium:monero.social >__ I originally wanted to do a full "reverse DNS", but the proprietary API stopped me. Then I went to ditatompel's API.     

> __< s​yntheticbird:monero.social >__ I'm honestly surprised by that     

> __< r​ucknium:monero.social >__ I think it went down from 30% to 25% of honest nodes having RPC, after I did the port RPC calls.     

> __< j​effro256:monero.social >__ Who would we contact about this?     

> __< g​ingeropolous:monero.social >__ i wonder how possible it would be to add this filtering to the gui simple mode.     

> __< j​effro256:monero.social >__ Are you talking about the deduplication change?     

> __< r​ucknium:monero.social >__ My rucknium.me node actually says during its Levin handshake that it doesn't have an RPC port enabled, but I actually do. I think it's just piped through NGINX. Maybe I should check my config (hypocrite  😁). Or, wait, maybe it does say it during the handshake, but i have ports locked down     

> __< j​effro256:monero.social >__ Or DNS ban list?     

> __< r​ucknium:monero.social >__ jeffro256: AFAIK, Core manages the DNS records.     

> __< g​ingeropolous:monero.social >__ something. currently it just uses the advertised rpc on the monero p2p network. im not sure if it has the DNS ban list to remove the ones from the p2p     

> __< r​ucknium:monero.social >__ I just checked the full database. No, my node even says during the handshake that it does not have the RPC port enabled.     

> __< r​ucknium:monero.social >__ gingeropolous: That's those nodes with the `--public-node` flag enabled, right?     

> __< g​ingeropolous:monero.social >__ yeah     

> __< j​effro256:monero.social >__ I would have to check if bootstap daemons are not used if on the banlist ..     

> __< j​effro256:monero.social >__ i would hope so     

> __< r​ucknium:monero.social >__ Does anyone know anything about the opennode.xmr-tw.org remote node domain, by the way? Its DNS record points to three IP addresses, one of which is plowsof  's monerodevs.org remote node IP     

> __< r​ucknium:monero.social >__ Is the webapp loading OK now? I tried to make it load faster in this iteration.     

> __< g​ingeropolous:monero.social >__ yeah, the name of the dude that runs it will come to me eventually. i think its lza menace, or is that the monero.fail guy...     

> __< s​yntheticbird:monero.social >__ that's comfortable enough to use     

> __< s​yntheticbird:monero.social >__ 7.5/10     

> __< r​ucknium:monero.social >__ The data exclude the few nodes with IPv6 IP addresses. I will have to decide how to handle them.     

> __< s​yntheticbird:monero.social >__ promising     

> __< s​yntheticbird:monero.social >__ will be back     

> __< s​yntheticbird:monero.social >__ will return     

> __< r​ucknium:monero.social >__ lza menace runs monero.fail AFAIK     

> __< g​ingeropolous:monero.social >__ or lafudoci . https://github.com/Lafudoci/moneriote-python     

> __< g​ingeropolous:monero.social >__ they used to run the moneriote script and have it populate the DNS of that domain in a geo-located manner, but i guess they just handpicked after the infestation     

> __< r​ucknium:monero.social >__ 7) CCS proposal: [Monero Network Simulation Tool](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/589).     

> __< r​ucknium:monero.social >__ gingeropolous: Thanks for making progress on Shadow-Monero. I agree that Shadow isn't necessarily suited for replacing a live stressnet. Still, it can help a lot with testing new network code that doesn't have to go through a full stressnet.     

> __< g​ingeropolous:monero.social >__ i put the main update above in the status, but briefly, i have something working. I wouldn't say its production ready at all.     

> __< g​ingeropolous:monero.social >__ yeah, i think i was hoping more for a stressnet-in-a-can kinda thing     

> __< r​ucknium:monero.social >__ Were you able to talk with 0xfffc  about requirements and comparison with...that other system?     

> __< g​ingeropolous:monero.social >__ but i also see the value is shadows ability to test dandelion parameters or clover or etc     

> __< g​ingeropolous:monero.social >__ no, they are busy at the moment.     

> __< g​ingeropolous:monero.social >__ but if anyone has any requested features of a monero shadow network sim, please let me know so i can bake them in early     

> __< j​effro256:monero.social >__ After skimming the p2p code, the candidates for the RPC bootstrap daemon are collected from the public RPC entries in the P2P peerlist. When one opens `monerod` with a ban list, the spy nodes are evicted from the P2P peerlist and put on a blacklist from being added back in. So since the P2P peerlist is filtered of spies, the RPC bootstrap daemon candidates should be filtered of spies.     

> __< j​effro256:monero.social >__ ... I think, haven't tested yet     

> __< r​ucknium:monero.social >__ Did you publish the XMRshadow code somewhere?     

> __< g​ingeropolous:monero.social >__ again, this will be more focused on the network / p2p side of the monero protocol, not necessarily performance  / blockchainy stuff     

> __< r​ucknium:monero.social >__ (And what will this thing be called? XMRshadow, Shadow-Monero Monero-Shadow...?     

> __< gingeropolous >__ its currently monerosim     

> __< gingeropolous >__ sorry, element crashed      

> __< r​ucknium:monero.social >__ jeffro256: The P2P peerlist being filtered of spies is the basis of my detection that a node is using either of the ban lists. If no IP addresses on the ban list appear in the peerlist shared during a P2P handshake, then it is assumed that the node has the ban list enabled.     

> __< g​ingeropolous:monero.social >__ Rucknium: , and i haven't shared yet. the code is sorta in an embarasing state :     

> __< r​ucknium:monero.social >__ Just post it under a CRAPL license     

> __< r​ucknium:monero.social >__ https://matt.might.net/articles/crapl/     

> __< a​ntilt:we2.ee >__ gingeropolous can the dynamic aspects be simulated? For ex. If a supernode goes down - will others take their place?     

> __< r​ucknium:monero.social >__ > It's not the kind of code one is proud of.     

> __< r​ucknium:monero.social >__ > I think a lot of academics are embarrassed to release their code.     

> __< r​ucknium:monero.social >__ > But, it doesn't matter. We should release our code, warts and all.     

> __< r​ucknium:monero.social >__ (Technically I don't know if CRAPL satisfies the FSF requirements for an open source license. Check on that.)     

> __< g​ingeropolous:monero.social >__ flip flop: , yeah. in shadow, you can create instances of things (thats the best name i have) with set parameters, so you could create an instance that is a supernode, set to start at time n, then set to die at time x, and see how the network responds.     

> __< g​ingeropolous:monero.social >__ Rucknium: regarding sharing, im also not at a point to welcome PRs if anyone got ambitious. i dunno. this fiddlin on my own is my current comfort level     

> __< r​ucknium:monero.social >__ I think if it is still in the CCS process, it would be a very good idea to give it an open source license and post it. CC: plowsof     

> __< g​ingeropolous:monero.social >__ yeah it has the the same license as monero i think     

> __< r​ucknium:monero.social >__ In Shadow you can also set network parameters like bandwidth and latency at the node and even connection level, IIRC. SO you can have some far away nodes and bandwidth-constricted node, etc.     

> __< r​ucknium:monero.social >__ More discussion of `monerosim`?     

> __< g​ingeropolous:monero.social >__ aight, well then, in the spirit of crapl, https://github.com/Fountain5405/monerosim     

> __< r​ucknium:monero.social >__ Nice! Thank you, gingeropolous     

> __< r​ucknium:monero.social >__ Any information about how much RAM one of the Monero nodes uses when it is in `monerosim`?     

> __< r​ucknium:monero.social >__ I am interested in how it would scale.     

> __< g​ingeropolous:monero.social >__ i dunno yet. Im not at the optimization stage. From what i gather from the bitcoin-shadow plugin (yeah, one exists), you can get thousands of nodes on one machine     

> __< r​ucknium:monero.social >__ Any other business?     

> __< a​ntilt:we2.ee >__ network topology:     

> __< a​ntilt:we2.ee >__       

> __< a​ntilt:we2.ee >__ thought about Yu Gao's "supernodes" (pool operators) and how they might be hardened against gray_list spam: preparing a --add-priority-node might come in handy for pool ops if we don't want to slow down gossiping. And DDoS protection for fcmp++ of course     

> __< r​ucknium:monero.social >__ IIRC, sech1 helped set up a network "backbone" between pool nodes.     

> __< r​ucknium:monero.social >__ For faster block propagation IIRC     

> __< a​ntilt:we2.ee >__ i heard that     

> __< sech1 >__ not exactly helped, I just found pool nodes (both public and non-public ones), and added them all to my nodes' priority lists     

> __< sech1 >__ so my nodes connect all major pool nodes with max 1 hop between them (pool 1 node -> my node -> pool 2 node)     

> __< a​ntilt:we2.ee >__ iirc that prevents a eclipse already     

> __< r​ucknium:monero.social >__ We can end the meeting here. Thanks everyone.     

> __< a​ntilt:we2.ee >__ (connections_maker uses priority-node before gray_list)     

> __< sech1 >__ plus my nodes run RandomX in fast mode, that saves another 10 ms on block propagation     

> __< r​ucknium:monero.social >__ Interesting research on a 2023 BTC DDoS that seemed to cause an increase in the rate of orphaned blocks: https://b10c.me/observations/15-inv-to-send-queue/     

> __< a​rticmine:monero.social >__ May 2023 coincided with the second highest spike at the  time in the Bitcoin fee in reward.      

> __< a​rticmine:monero.social >__ This makes the Bitcoin network very vulnerable to a DDoS attack consisting of transactions that do not for the most part get mined.     

> __< a​rticmine:monero.social >__ It can be relevant to Monero with transactions that on their own in large numbers would not get mined if the fee is too low for the transaction weight.     

> __< g​ingeropolous:monero.social >__ Rucknium: , what would be super cool at some point is if we can bootstrap a monerosim configuration that uses the current snapshot of the network. I imagine we could use your recent work to create a connectivity map that we could plug into monerosim. I imagine we'd need some kind of database that has nodes and edges. Monerosim would parse that to craft a simulated network.     

> __< r​ucknium:monero.social >__ Maybe some data could be obtained from the work of Gao et al. https://moneroresearch.info/267 https://moneroresearch.info/278     

> __< r​ucknium:monero.social >__ Yu Gao ^     

> __< j​ack_ma_blabla:matrix.org >__ Can xmr support rbf ? allow usage of same inputs/decoys, just the output amount would change which is private anyways.     

> __< l​m:matrix.baermail.fr >__ AFAIK that's just rejected by nodes ? But you can say good bye to zero conf with rbf     

> __< d​iego:cypherstack.com >__ RBF is also much less useful due to dynamic blocksize     

> __< a​rticmine:monero.social >__ rbf  does not address this type of spam attack     

> __< a​rticmine:monero.social >__ The whole point of the spam attack is that the transactions are not muned     

> __< a​rticmine:monero.social >__ Mined     

> __< o​frnxmr:monero.social >__ RBF would only make sense, imo, if it was only possible to bump the fee w/o changing any other details of the tx     

> __< o​frnxmr:monero.social >__ Dynamic blocks can still cause tx's to be dropped from the txpool under big spam attacks. Particularly when the fees of the spam attack are "normal" (lvl 2). There is a PR open to further elevate fees to "elevated" (lvl 3), to try to avoid having any dropped txs or delays longer than 12hrs     

> __< o​frnxmr:monero.social >__ This pr should only elevate fees to "elevated" if there is a 12hr backlog at lvl 2. A spammed txpool of low fee wont cause the fees to elevate beyond "normal".     

> __< d​iego:cypherstack.com >__ ye, hence why I didn't say useless     

> __< d​iego:cypherstack.com >__ under ideal scenarios where nobody is attacking, RBF is less useful, because the blocks will expand until activity goes back down, so you won't have to wait as long even with a full mempool than with something like Bitcoin     

> __< j​effro256:monero.social >__ You *could* prove that all the outputs are addressed to the same addresses with the same amounts, except for the "change" output amount, which has the same private spend key as all the inputs inside of a ZK proof........     

> __< j​effro256:monero.social >__ but don't do that     



# Action History
- Created by: Rucknium | 2025-07-08T22:43:55+00:00
- Closed at: 2025-07-18T20:12:01+00:00
