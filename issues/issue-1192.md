---
title: Monero Research Lab Meeting - Wed 23 April 2025, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1192
author: Rucknium
assignees: []
labels: []
created_at: '2025-04-22T23:21:46+00:00'
updated_at: '2025-05-01T19:50:52+00:00'
type: issue
status: closed
closed_at: '2025-05-01T19:50:51+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/meeting.html?p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3. Decide on publicising the method to find [proxy nodes](https://github.com/monero-project/research-lab/issues/126).

4. Unit test for implementation of [subnet deduplication in peer selection algorithm](https://github.com/Rucknium/misc-research/blob/main/Monero-Peer-Subnet-Deduplication/pdf/monero-peer-subnet-deduplication.pdf).

5. [Release of OSPEAD HackerOne and CCS milestone submissions](https://github.com/Rucknium/OSPEAD). [Analysis of risk of new decoy selection algorithm without a hard fork](https://gist.github.com/Rucknium/fb638bcb72d475eeee58757f754acbee).

6. Any other business

7. Confirm next meeting agenda

Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#1189 

# Discussion History
## Rucknium | 2025-04-25T15:27:07+00:00
Logs

> __< r​ucknium:monero.social >__ Meeting time! https://github.com/monero-project/meta/issues/1192     

> __< r​ucknium:monero.social >__ 1) Greetings     

> __< kedihacker >__ hii     

> __< c​haser:monero.social >__ hello     

> __< b​oog900:monero.social >__ hi     

> __< a​ntilt:we2.ee >__ hi     

> __< r​ucknium:monero.social >__ 2) Updates. What is everyone working on?     

> __< j​effro256:monero.social >__ Howdy     

> __< j​berman:monero.social >__ *waves*     

> __< j​effro256:monero.social >__ me: Carrot+FCMP sending/receiving (using the `transfer` command) is working for non-multisig wallets in the CLI wallet: https://github.com/seraphis-migration/monero/pull/32     

> __< r​ucknium:monero.social >__ me:  Fixing bugs and writing statistical unit tests for the function to generate old/new decoy selection algorithm rings and the rings of their antecedent txs. Working on a statistical unit test for implementation of subnet deduplication for node peer selection. Unfortunately I did not get to writing the review of the Clover paper yet.     

> __< j​berman:monero.social >__ me: completed the FCMP++ blinds cache (implemented serialization to save pre-calculated blinds to the wallet cache), implemented composition changes prior discussed (hash y coords in the leaf layer in addition to x coords), implemented comments on latest PR's for banning torsion at consensus and modifying the PoW hash for FCMP++, and did some debugging in the torsion checking cryp<clipped message>     

> __< j​berman:monero.social >__ to code. Continuing this week taking a look at FCMP++ fees (will likely discuss with articmine once I'm further along in my looking into)     

> __< r​ucknium:monero.social >__ 3) Decide on publicising the method to find proxy nodes. https://github.com/monero-project/research-lab/issues/126     

> __< j​effro256:monero.social >__ Anything new to discuss since last week on this topic?     

> __< b​oog900:monero.social >__ well they haven't changed IPs yet AFAIK :)     

> __< r​ucknium:monero.social >__ Sort of a side concern: I think it would be good to release my [subnet deduplication paper](https://github.com/Rucknium/misc-research/blob/main/Monero-Peer-Subnet-Deduplication/pdf/monero-peer-subnet-deduplication.pdf) as a MRL research bulletin before a `monerod` binary release version that deploys subnet deduplication. The paper could include the method to find proxy nodes.     

> __< r​ucknium:monero.social >__ The paper already "assumes" a malicious node list in its empirical analysis. (The IP address space treemap plots.) It would be good to discuss where the assumption came from.     

> __< a​ntilt:we2.ee >__ "whistleblower"     

> __< b​oog900:monero.social >__ I do want to reiterate a point I made last meeting that constantly updating a ban list and requiring people to manually update it isn't a good solution.     

> __< b​oog900:monero.social >__ that's all keeping the method private allows us to do     

> __< b​oog900:monero.social >__ and we currently aren't even doing that as they haven't switched IPs yet even after they were outed years before I found them.     

> __< r​ucknium:monero.social >__ Keeping the method private also informs us how severe the problem may be (assuming that this entity suddenly fixes the problem and switches IP addresses, which may not happen anyway).     

> __< r​ucknium:monero.social >__ Maybe: Disclose once subnet deduplication has a valid and tested implementation, but before putting it in a release version binary.     

> __< r​ucknium:monero.social >__ as a middle ground     

> __< c​haser:monero.social >__ what's the benefit of having a time window between the disclosure and the binary release?     

> __< r​ucknium:monero.social >__ chaser: Community members would have time to review the evidence and give their approval/consent that subnet deduplication is an appropriate countermeasure.     

> __< c​haser:monero.social >__ thanks. didn't occur to me it could be insufficient.     

> __< c​haser:monero.social >__ (or controversial)     

> __< r​ucknium:monero.social >__ Maybe it won't be controversial at all, but some people were upset at the MRL recommendation to voluntarily run the ban list. So maybe best to err on the side of caution.     

> __< rbrunner >__ Agree     

> __< c​haser:monero.social >__ true     

> __< a​rticmine:monero.social >__ Sorry for being late.     

> __< a​rticmine:monero.social >__ My preference with this is full disclosure. My take is that the entity has a lot more to lose here with full disclosure than the.Monero community. This being said I am fine with the interim proposal of keeping it private until we have a full implementation in place.     

> __< j​effro256:monero.social >__ Rucknium: I agree that that is a reasonable minimum bar for disclosure. We'd be shooting ourselves in the foot if we disclosed without a proper (even sub-par) countermeasure already ready to run     

> __< rbrunner >__ It may just be that it will take quite some time before somebody comes around to program that deduplication ...     

> __< b​oog900:monero.social >__ we do have other ways to tell these nodes are not running default monerod, it's just the method we would reveal tells us they are defiantly proxies.     

> __< b​oog900:monero.social >__ Also they weren't exactly being sneaky with most of their nodes being in ~6 IP blocks.     

> __< r​ucknium:monero.social >__ rbrunner: I have considered posting a bounty for it. On the other hand, a bounty for this type of change is not easy to administer since the code has to do the correct thing, but also be up to Monero code standards.     

> __< rbrunner >__ True     

> __< r​ucknium:monero.social >__ And even publicly discussing a bounty may influence people not to implement it for free yet,  hoping for a bigger XMR bounty :D     

> __< b​oog900:monero.social >__ I am ok with waiting for a countermeasure but yeah I do worry about how long it will take also revealing it now could give more of a push to build a countermeasure.     

> __< r​ucknium:monero.social >__ It seems like "Disclose once subnet deduplication has a valid and tested implementation, but before putting it in a release version binary" may be a proposal everyone can live with.     

> __< b​oog900:monero.social >__ with more people _knowing_ these are proxies.     

> __< rbrunner >__ It's basically a different way to manage and connect / disconnect peers, right? So maybe less complicated that feared     

> __< rbrunner >__ *than feared     

> __< b​oog900:monero.social >__ yeah I think so too     

> __< a​ntilt:we2.ee >__ its just a test if its already in in the whitelist, then drop it - right ?     

> __< rbrunner >__ Well, maybe, but the Monero code base can be hard. Maybe not even easy to locate the code that manages lists now :)     

> __< r​ucknium:monero.social >__ rbrunner: Like we discussed last time, the hard part is probably understanding how the existing peer selection code code works. That's also a question I have for next agenda item!     

> __< rbrunner >__ So maybe just analysing and then documenting that would be a step forward?     

> __< r​ucknium:monero.social >__ flip flop: I think that jeffro256  suggested that an IP in a subnet not be dropped entirely from the `white_list`, but just "skipped" when deciding which node to connect to next. IIRC, there was a security concern about outright dropping the IPs from the `white_list`, but I cannot remember the exact details.     

> __< r​ucknium:monero.social >__ rbrunner: I always love documentation of undocumented Monero code!     

> __< rbrunner >__ Yeah, who doesn't :)     

> __< s​yntheticbird:monero.social >__ one day people will look at cuprate documentation to understand monerod     

> __< r​ucknium:monero.social >__ This paper has an old and high-level overview of things AFAIK: https://moneroresearch.info/99 Cao, T., Yu, J., Decouchant, J., Luo, X., & Verissimo, P. 2020, Exploring the Monero Peer-to-Peer Network.     

> __< r​ucknium:monero.social >__ Note that the PDF is the whole issue, so you have to search for the exact article.     

> __< rbrunner >__ Well, yes, is peer selection already understood and implemented in Cuprate?     

> __< j​effro256:monero.social >__ I already quote the Cuprate Monero book when talking about consensus rules     

> __< r​ucknium:monero.social >__ > In Monero, each node maintains a peer list consisting of two parts, i.e., a     

> __< r​ucknium:monero.social >__ white list, and a gray list. In the peer list of a peer A, the information of     

> __< r​ucknium:monero.social >__ each recorded peer not only contains its identity, its IP address, and the TCP     

> __< r​ucknium:monero.social >__ port number it uses, but also a special last seen data field, which is the time at     

> __< r​ucknium:monero.social >__ which the peer has interacted with peer A for the last time. All the peers in the     

> __< r​ucknium:monero.social >__ lists are ordered chronologically according to their last seen data, i.e., the most     

> __< r​ucknium:monero.social >__ recently seen peers are at the top of the list.     

> __< r​ucknium:monero.social >__ ^ Then the paper adds more details. One thing that is definitely out of date is that nodes no longer disclose `last_seen` data to other nodes, nor to restricted RPC requests, because it revealed some network topology info     

> __< b​oog900:monero.social >__ rbrunner: cuprate's peer selection is more vulnerable than monerod currently, it's something I have been meaning to work on.     

> __< b​oog900:monero.social >__ monerod only makes an average of 15% of outbound connections to these nodes, cuprated would be in the 40 to 75% range I think.     

> __< r​ucknium:monero.social >__ It seems like there may be loose consensus to wait until there is a subnet deduplication implementation to disclose the spy node discovery method. MRL can return to this question if desired.     

> __< a​rticmine:monero.social >__ Yes     

> __< r​ucknium:monero.social >__ 4) Unit test for implementation of subnet deduplication in peer selection algorithm. https://github.com/Rucknium/misc-research/blob/main/Monero-Peer-Subnet-Deduplication/pdf/monero-peer-subnet-deduplication.pdf     

> __< r​ucknium:monero.social >__ I have been writing a statistical unit test for an anticipated subnet deduplication implementation. It records new connections and then sees if the connections are clustered within subnets. Not without problems, however.     

> __< r​ucknium:monero.social >__ For example, it seems that the `get_connections` RPC call sometimes "misses" connections.     

> __< r​ucknium:monero.social >__ I see some IP addresses as a connection, then next poll period (30 seconds currently), it is not there. Then it reappears in the next poll period.     

> __< a​ntilt:we2.ee >__ is there a max_connections limit set ?     

> __< r​ucknium:monero.social >__ I'm not necessarily calling this a `monerod` bug. It did cause me problems before I realized it was happening, then implemented a workaround.     

> __< r​ucknium:monero.social >__ flip flop: Yes, theses are all outbound connections by the way. I just use the default, which is 12     

> __< r​ucknium:monero.social >__ Maybe `monerod` thinks "I should only have 12 connections, but I actually have 13 (maybe one or more "in transition"), so I should report just 12.     

> __< r​ucknium:monero.social >__ Probably the bigger issue here is that I am not sure exactly how `monerod` currently chooses the next connection. I assumed that it would select randomly with equal probability from `white_list`, but I am not sure.     

> __< r​ucknium:monero.social >__ And what happens to the IP once the connection ends? Does it go back to the white_list? And can gray_list IPs be directly promoted from gray_list to an actual connection?     

> __< j​berman:monero.social >__ IIRC the impl will delete 1 non-syncing connection over an interval and will then add another peer to reach the max. Seems possible it's re-adding the same peer     

> __< j​berman:monero.social >__ I don't recall the whitelist selection process     

> __< r​ucknium:monero.social >__ jberman: Possible, yes. Then why is it doing that?     

> __< r​ucknium:monero.social >__ If it is re-adding them, then it is re-selecting those IPs at a far higher probability than random uniform selection from the white_list     

> __< r​ucknium:monero.social >__ According to what I've seen.     

> __< rbrunner >__ "Why" questions are often the hardest. You can find out what the code does, but why, well ...     

> __< b​oog900:monero.social >__ monerod maintains a certain number of connections from peers originally from the gray list (which get upgraded to white once connected to) IIRC it's 70% gray but would have to check ....     

> __< r​ucknium:monero.social >__ There are also long-lived "anchor connections" that I am not trying to analyze at this time. I assume there is much less churn in anchor conenctions.     

> __< j​berman:monero.social >__ could also be the other node re-adding yours. would need to double check the code     

> __< j​berman:monero.social >__ log level 2 may help there too     

> __< r​ucknium:monero.social >__ jberman: I am only looking at outbound connections. The nodes I am working with now have closed ports actually.     

> __< j​berman:monero.social >__ ah true     

> __< r​ucknium:monero.social >__ I may look into logs, but parsing logs for data analysis can be tedious.     

> __< b​oog900:monero.social >__ ah no it is 70% white https://github.com/monero-project/monero/blob/02fba21846f5274318a0b8a082256f08ba00313f/src/cryptonote_config.h#L149     

> __< r​ucknium:monero.social >__ Maybe a peer went "silent" and my node thought the conenction ended, but then the peer woke up and responded again.     

> __< r​ucknium:monero.social >__ Anyway, I am trialing statistical tests for node connection behavior, but if I don't get the "null" behavior correct, then the tests won't exactly give correct results.     

> __< j​berman:monero.social >__ log level 2 and grep for `Random connection index=` could yield some insight here     

> __< r​ucknium:monero.social >__ I have set up a crude simulation of subnet deduplication by sending IP ban commands to the node, to see how it sets connections. But things seem not quite aligned with my naive expectations.     

> __< j​berman:monero.social >__ it does look like it's attempting to make a random selection     

> __< r​ucknium:monero.social >__ jberman: Thanks. I will look into that.     

> __< r​ucknium:monero.social >__ I wish I could read the C++. Working on learning Rust for now.     

> __< j​berman:monero.social >__ suggestion: turn on log level 2, do print_cn, then later on do print_cn again and see if the issue presented itself among those connections, then sharing those logs would be helpful     

> __< r​ucknium:monero.social >__ jberman: Thank you. I will try those things.     

> __< j​berman:monero.social >__ sorry, 3 print_cn's (1 for each polling period) with log level 2 on would help explain     

> __< b​oog900:monero.social >__ it seems like it is only selecting from the top 20 most recent peers, right (if using the white list).     

> __< b​oog900:monero.social >__ https://github.com/monero-project/monero/blob/master/src/p2p/net_node.inl#L1692     

> __< r​ucknium:monero.social >__ boog900: That could explain why I'm not seeing the "correct" distribution when I assume equal probability of selection for every IP in the white_list.     

> __< j​berman:monero.social >__ and it's also filtering further among the white_list, so looks like it could be less than 20     

> __< b​oog900:monero.social >__ this seems easy to game by just pinging nodes to get more recent last seen timestamps     

> __< b​oog900:monero.social >__ to increase your chance of them making a connection to you     

> __< b​oog900:monero.social >__ if an inbound ping causes a timestamp update that is     

> __< b​oog900:monero.social >__ or just handshake then disconnect frequently.     

> __< j​berman:monero.social >__ considering ruck is consistently seeing the same node being re-added, it seems like either there is an issue with that random function, or it's filtering the list down even further from 20 (assuming honest connections not attempting to game)?     

> __< b​oog900:monero.social >__ well considering monerod wont reconnect to 12 of the top 20 as it is already connected ....     

> __< b​oog900:monero.social >__ if we assume connected peers will have high last seen timestamps     

> __< r​ucknium:monero.social >__ From previous empirical analysis, I found that the median duration of outbound connections was about 24 minutes, by the way.     

> __< j​berman:monero.social >__ true, then it should be still 1/8, ya?     

> __< r​ucknium:monero.social >__ Figure 14 on page 21 of https://github.com/Rucknium/misc-research/blob/main/Monero-Black-Marble-Flood/pdf/monero-black-marble-flood.pdf     

> __< j​berman:monero.social >__ is this a pruned node ruck?     

> __< r​ucknium:monero.social >__ jberman: I don't think so. Let me check.     

> __< r​ucknium:monero.social >__ I forget the commands. I am 95% sure that these nodes are not pruned because they are the same ones I am pulling the whole blockchain data from, through RPC     

> __< r​ucknium:monero.social >__ Thanks. Now I have some leads to work on.     

> __< r​ucknium:monero.social >__ 5) Release of OSPEAD HackerOne and CCS milestone submissions. Analysis of risk of new decoy selection algorithm without a hard fork. https://gist.github.com/Rucknium/fb638bcb72d475eeee58757f754acbee     

> __< r​ucknium:monero.social >__ I don't have a lot to report about this at this meeting, except I write some unit tests to make sure I am producing the correct statistical distributions: https://github.com/Rucknium/OSPEAD/blob/main/CCS-milestone-2/decoyanalysis/tests/testthat/test-monte-carlo.R     

> __< r​ucknium:monero.social >__ It does a series of chi-squared tests for the checks and makes sure that the null hypothesis is rejected or not, depending on what is appropriate.     

> __< r​ucknium:monero.social >__ For this, I also worked out the closed for of what the mixed distribution probabilities are supposed to be. That's a little useful, but nothing major.     

> __< r​ucknium:monero.social >__ closed form*     

> __< r​ucknium:monero.social >__ Any more items anyone wishes to discuss? As always, suggestions for agenda items for future meetings are welcome.     

> __< a​ntilt:we2.ee >__ peer selection may be topic, if the env gets more toxic. Agenda item would be: We Of Trust ?     

> __< r​ucknium:monero.social >__ Web of trust?     

> __< a​ntilt:we2.ee >__ peer selection may be topic, if the env gets more toxic. Agenda item would be: Web Of Trust ?     

> __< r​ucknium:monero.social >__ I will add to next week's agenda     

> __< r​ucknium:monero.social >__ I was just making sure it was the typo that I thought it was     

> __< r​ucknium:monero.social >__ We can end the meeting here. Thanks everyone.     

> __< a​rticmine:monero.social >__ Thanks



# Action History
- Created by: Rucknium | 2025-04-22T23:21:46+00:00
- Closed at: 2025-05-01T19:50:51+00:00
