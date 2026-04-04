---
title: Monero Research Lab Meeting - Wed 06 November 2024, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1105
author: Rucknium
assignees: []
labels: []
created_at: '2024-11-05T20:34:02+00:00'
updated_at: '2024-11-19T20:53:37+00:00'
type: issue
status: closed
closed_at: '2024-11-19T20:53:37+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

[Join the Monero Matrix server if you don't already have a Matrix account.](https://web.archive.org/web/20230128130949/https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211027T170000&p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

4. [FCMP++ tx size and compute cost](https://gist.github.com/kayabaNerve/c42aeae1ae9434f2678943c3b8da7898) and [MAX_INPUTS/MAX_OUTPUTS](https://github.com/monero-project/research-lab/issues/100#issuecomment-2433524326)

5. [FCMP++ Optimization Competition](https://github.com/kayabaNerve/fcmp-plus-plus-optimization-competition).

6. Reviews for [Carrot](https://github.com/jeffro256/carrot/blob/master/carrot.md).

7. [Discussion: preventing P2P proxy nodes](https://github.com/monero-project/research-lab/issues/126).

8. [Proposal for FCMP++ HF Activation Rule to Retroactively Ignore Future `unlock_time`](https://github.com/monero-project/research-lab/issues/125)

9. Any other business

10. Confirm next meeting agenda

Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#1102 

# Discussion History
## Rucknium | 2024-11-07T18:55:03+00:00
Logs:

> __< r​ucknium:monero.social >__ Meeting time! https://github.com/monero-project/meta/issues/1105     

> __< r​ucknium:monero.social >__ 1) Greetings     

> __< rbrunner >__ Hello     

> __< c​haser:monero.social >__ hello     

> __< j​berman:monero.social >__ *waves*     

> __< 0​xfffc:monero.social >__ hi everyone     

> __< b​oog900:monero.social >__ Hi     

> __< r​ucknium:monero.social >__ 2) Updates. What is everyone working on?     

> __< r​ucknium:monero.social >__ me: Analyzed p2p connection logs to provide more supporting evidence for the proxy node banlist and estimated the empirical risk to user privacy: https://github.com/monero-project/research-lab/issues/126#issuecomment-2460261864     

> __< 0​xfffc:monero.social >__ Like last week I was sick with covid19/flu, so haven't been that productive either. Only trivial reviews. Today I got back to work. First will review #9441, then fix issue raised at #9362     

> __< r​ucknium:monero.social >__ 3) FCMP++ tx size and compute cost and MAX_INPUTS/MAX_OUTPUTS https://gist.github.com/kayabaNerve/c42aeae1ae9434f2678943c3b8da7898  https://github.com/monero-project/research-lab/issues/100#issuecomment-2433524326     

> __< r​ucknium:monero.social >__ kayabanerve kayabanerve : Anything to discuss today about this?     

> __< j​berman:monero.social >__ me: Continuing local wallet tree building     

> __< r​ucknium:monero.social >__ I haven't gone deeper into the MAX_INPUTS/MAX_OUTPUTS analysis yet because my main "database" process is occupied.     

> __< r​ucknium:monero.social >__ 4) FCMP++ Optimization Competition. https://github.com/kayabaNerve/fcmp-plus-plus-optimization-competition     

> __< r​ucknium:monero.social >__ Anything to discuss on this?     

> __< k​ayabanerve:matrix.org >__ Apologies. I have nothing to add     

> __< j​effro256:monero.social >__ Howdy, sorry I'm late. Daylight savings got me     

> __< k​ayabanerve:matrix.org >__ On either topic, I haven't personally worked on Monero this past week.     

> __< r​ucknium:monero.social >__ 5) Reviews for Carrot. https://github.com/jeffro256/carrot/blob/master/carrot.md     

> __< r​ucknium:monero.social >__ jeffro256: , anything on Carrot today?     

> __< j​effro256:monero.social >__ AFAIK, Cypherstack is still working on the review. No updates from them yet     

> __< r​ucknium:monero.social >__ That reminds me that I wanted to note a personnel change that's relevant to MRL: About a month ago, Aaron Feickert (Sarang Noether) left Cypher Stack. At about the same time, Brandon Goodell (Surae Noether) joined Cypher Stack.     

> __< r​ucknium:monero.social >__ 6) Discussion: preventing P2P proxy nodes. https://github.com/monero-project/research-lab/issues/126     

> __< k​ayabanerve:matrix.org >__ Rucknium: Do you want to add a research topic to these meetings re: making fee a pure fn of inputs/outputs/TX extra len? Or is that not an active discussion topic, solely a item of work for you?     

> __< r​ucknium:monero.social >__ Yes I could do that     

> __< k​ayabanerve:matrix.org >__ Sorry for interrupting you mid-topic, it's just kinda FCMP++ related and one thing I wanted to quickly check in on.     

> __< r​ucknium:monero.social >__ Do you want to discuss now or next meeting?     

> __< k​ayabanerve:matrix.org >__ If we have time today, we can open the discussion today. It should be brief. I'll leave you to decide when we get to it as the current agenda item is P2P proxy nodes :p     

> __< r​ucknium:monero.social >__ Ok. We can put it in the "Any other business" item if there is time at the end of the meeting     

> __< r​ucknium:monero.social >__ boog900: Do you want to open the discussion on p2p proxy nodes?     

> __< b​oog900:monero.social >__ Sure, a few weeks ago I found some nodes displaying behavior which can only be explained by them being proxy nodes. These nodes make up a large portion of the network, 40% of the IPs I found and 75% of the IP:Ports.     

> __< b​oog900:monero.social >__ The only reason I can think to run proxy nodes is to try and link IPs to transactions.     

> __< r​ucknium:monero.social >__ A "proxy node" is an IP address that pretends to run its own node, but actually it just relays messages between a "victim" node and another node (possibly honest node or controlled by the adversary)     

> __< b​oog900:monero.social >__ They use 6 main IP ranges, all under the LionLink-Networks ASN     

> __< j​effro256:monero.social >__ 40% is nuts. I want to link this Bitcoin issue here: https://github.com/bitcoin/bitcoin/issues/16599. Seems like some people might have already done some research in this area. ASN bucketing would almost certainly help here     

> __< r​ucknium:monero.social >__ A lot of the threat models for network integrity and privacy assume that it is expensive for an adversary to run many nodes. Basically a proxy node reduces this expense by appearing to run a real node, but not actually running it     

> __< r​ucknium:monero.social >__ In my p2p log data, from April-May 2024, about 15% of outbound connections of the honest nodes are to IP addresses in the ban list, so the privacy risk isn't as high as 40%, probably.     

> __< k​ayabanerve:matrix.org >__ We could add a PoW puzzle to any network requests which can be MITMd but not without replicating the work. I don't like the idea of PoW for any P2P req but also, it makes proxy nodes expensive again.     

> __< k​ayabanerve:matrix.org >__ The question is is that an asymmetric cost or does it just make every node more expensive while massively degrading the P2P network.     

> __< r​ucknium:monero.social >__ Connections to the banlist IP addresses have a shorter duration. And the node software prefers to connect to IP addreses ranges that are not in the same subnet     

> __< b​oog900:monero.social >__ If they operated the node being proxied they could probably get around this right?     

> __< 0​xfffc:monero.social >__ This is very interesting approach. Particularly there is every kind of PoW defense available.  But for adversary with $, this is not going to solve the problem.     

> __< r​ucknium:monero.social >__ I don't know what the long-term solution is, but in the short term, monerod could be hard-coded with the LinkingLion IP addresses and instruct monerod not to establish outbound connections to them. Inbound connections could be allowed, so no "innocent" nodes would be excluded from the network. Outbound connections are the privacy-sensitive ones for Dandelion++     

> __< k​ayabanerve:matrix.org >__ It'd also need PoW on responses :/     

> __< r​ucknium:monero.social >__ LinkingLion has been publicly discussed for years, yet they have not changed their IP addresses. Maybe something prevents them from doing so. Maybe an IP address hardcode would stop them for a while.     

> __< k​ayabanerve:matrix.org >__ They'd serve 10x the responses if they have 10 nodes, even if they only make 1x the requests for their one node     

> __< c​haser:monero.social >__ you can't prevent it from happening, but raising the fence is a good idea IMHO.     

> __< k​ayabanerve:matrix.org >__ We could discuss introduction of a mixnet as an alternative to D++     

> __< r​ucknium:monero.social >__ I don't know if a mixnet would prevent eclipse or network partitioning attacks.     

> __< k​ayabanerve:matrix.org >__ I think that'd be excessively long-term and I'm not immediately sure it actually solves the problems we have     

> __< j​effro256:monero.social >__ Yes but that would mean either 1) the proxy is doing the PoW which makes it expensive, or 2) the central node is doing all the PoW which will bottleneck the operation after a certain period of time     

> __< r​ucknium:monero.social >__ Wasn't Kovri the "mixnet" attempt in the past?     

> __< b​oog900:monero.social >__ I would support banning every IP under LionLink-Networks, even the ones not currently running proxies.     

> __< 0​xfffc:monero.social >__ I agree. As short term solution, right? eventually we want to have a better defense for this.     

> __< rbrunner >__ Kovri was just a I2P implementation, as far as I remember.     

> __< r​ucknium:monero.social >__ u/oh-chase on Reddit posted this: https://xmr.nodes.pub/  It cross-references node IP addresses with ASNs. "LIONLINK-NETWORKS" is 55% now.     

> __< b​oog900:monero.social >__ If the PoW was also for responses yes but if the PoW is only for requests then by using their own main node they can just ignore the PoW requirement for their proxies.     

> __< k​ayabanerve:matrix.org >__ Rucknium: Every however often, we can have a node declare a mix. In this mix, every participating node submits an encrypted TX or an encryption of nothing. The publishing node of a TX becomes any one of the honest nodes in the network per cryptography (regardless of network analysis).     

> __< r​ucknium:monero.social >__ Isn't that just broadcast a tx by proxy, which was already analyzed by the D++ designers?     

> __< k​ayabanerve:matrix.org >__ That would also mean any one node can DoS the mix. We'd need a local reputation system for selecting mixes and a way to decline participation (if spammed with participation requests).     

> __< k​ayabanerve:matrix.org >__ Possibly? "any one of the honest nodes" sounds stronger than simply using a proxy.     

> __< k​ayabanerve:matrix.org >__ Eh. Presumably, the mix would only be conducted within the locally connected to region of the network. That means you can identify a TX as belonging to a subgraph of the P2P network. With D++, the fact it travels multiple hops prevents that.     

> __< j​effro256:monero.social >__ I see what you're saying, since creating a stem would be a request made by the honest node to the spy node in this case     

> __< r​ucknium:monero.social >__ >  A natural strategy for breaking symmetry about the source is to ask someone else to spread the message. That is, for every transaction, the source node chooses a peer uniformly at random from the pool of all nodes. It transmits the message to that node, who then broadcasts the message. More generally, the network could forward each message a few hops (each hop choosing a new no<clipped message     

> __< r​ucknium:monero.social >__ de at random) before diffusing it. We call this approach diffusion-by-proxy, and it is conceptually equivalent to propagating over a line that changes for every transmission. Diffusion-by-proxy might seem like it should have low precision because the graph is so dynamic, but that intuition turns out to be false.     

> __< r​ucknium:monero.social >__ ^ D++ paper     

> __< r​ucknium:monero.social >__ A long term solution will require time to research and develop. Can we discuss boog900's proposal to hardcode the banlist in monerod?     

> __< k​ayabanerve:matrix.org >__ I'll leave my commentary as the idea and decline to claim to be knowledgeable enough to continue the discussion.     

> __< j​effro256:monero.social >__ But even if adding PoW to D++ stem creation, it really doesn't happen that often, so it wouldn't be that much of a deterrent without crippling tx propagation for all nodes     

> __< r​ucknium:monero.social >__ ^ since that is a short-term solution that can be acted on quickly     

> __< j​berman:monero.social >__ I can't recall, is there precedent for including a hardcoded ban list?     

> __< r​ucknium:monero.social >__ I don't see any downsides to preventing nodes from establishing outbound connections to the proposed banlist nodes.     

> __< rbrunner >__ I think so far we carefully avoided any such things     

> __< r​ucknium:monero.social >__ I don't think there is precedent     

> __< 0​xfffc:monero.social >__ this time seems a little bit different. scale is huge IMHO. Please feel free to correct me.     

> __< 0​xfffc:monero.social >__ I have another question. If we implement such approach. https://xmr.nodes.pub/ are we losing 55% of nodes basically?     

> __< r​ucknium:monero.social >__ Those nodes aren't real     

> __< s​yntheticbird:monero.social >__ they are proxies so no     

> __< j​effro256:monero.social >__ Why hardcode it in over propogating a banlist file with a concise explanation?     

> __< rbrunner >__ If we really take that drastic measure, maybe also create a new command-line switch to disable that hardcoded banlist? To uphold people's freedom to decide.     

> __< 0​xfffc:monero.social >__ Ah, yes. thanks for clarification.     

> __< j​berman:monero.social >__ The main downside is risk of centralized censorship decisionmaking. Other downside is "what if they're honest for reasons we aren't seeing". Although generally I think it's reasonable / "within ethos" to seek to seek to ban centralized chokepoints     

> __< r​ucknium:monero.social >__ A non-hardcoded banlist file can possibly be used for corrupt purposes without a node running updating their software. Probably     

> __< rbrunner >__ And the reach and effect of such a separate file would certainly be smaller     

> __< j​effro256:monero.social >__ Huh? Banlist files already exist though     

> __< r​ucknium:monero.social >__ I think it's fine to have a switch that allows users to disable the banlist. But have it on by default IMHO     

> __< rbrunner >__ Yes, that's what I meant: on by default     

> __< r​ucknium:monero.social >__ jeffro256: I know. But they aren't on by default     

> __< b​oog900:monero.social >__ To be clear I want to hardcode a banlist for LionLink-Networks, not all IPs in the ban list.     

> __< rbrunner >__ Rucknium: Not sure what you mean with "corrupt uses" for banlists?     

> __< rbrunner >__ *corrupt purposes     

> __< j​effro256:monero.social >__ I agree with this. It sets the wrong precedent to have the devs hard code in banned IPs     

> __< r​ucknium:monero.social >__ There is a banlist that you can enable that checks a DNS record for which nodes to ban. If something like that is enabled by default, the DNS record could be hacked and har, the network     

> __< r​ucknium:monero.social >__ The IPs wouldn't really be banned from the network. They could still establish their own outbound connections.     

> __< 0​xfffc:monero.social >__ anyway to find out how many actual node are running? ( I want to understand what percentage of these 55% are proxies )     

> __< r​ucknium:monero.social >__ IPV6 is already disabled by default because there is a sybil attack risk with IPv6. At least, that is the reason I have read.     

> __< rbrunner >__ Somehow hardcoding IP4 numbers look like a grave defeat IMHO. And totally out of place.     

> __< b​oog900:monero.social >__ I haven't found a node in the 6 subnets that passed the not proxy test.     

> __< r​ucknium:monero.social >__ I get about 12,000 unique IP addresses in my log dataset from April-May that are not on boog900 's banlist.     

> __< 0​xfffc:monero.social >__ my other question, how computationally intensive is to run proxy node? to rephrase, I assume running a proxy node is cheaper than running actual node?     

> __< r​ucknium:monero.social >__ It really depends how you count. A lot of nodes that do not have open ports, so an active, short network scan wouldn't find them. And then nodes are turned off and on sometimes.     

> __< j​effro256:monero.social >__ Note that nodes without open ports are not going to be part of a D++ stem anyways     

> __< r​ucknium:monero.social >__ This spy node issue has been neglected for years. I assume because of dev resource constraints.     

> __< rbrunner >__ Won't "they" just rent a botnet and then have proxy nodes all over the planet?     

> __< 0​xfffc:monero.social >__ ( correct. so for simplicity let's not consider them in our discussion )     

> __< rbrunner >__ With quickly shifting IP numbers as well :)     

> __< 0​xfffc:monero.social >__ That is what I am trying to get at.     

> __< 0​xfffc:monero.social >__ I think we have to impose computational cost (PoW) to proxy nodes.     

> __< r​ucknium:monero.social >__ I get 4,600 non-banlist nodes with open ports in my dataset     

> __< 0​xfffc:monero.social >__ because, if this assumption is correct, they can switch very easily (?)     

> __< r​ucknium:monero.social >__ For some reason the adversary is still using Lion Link even though there has been public discussion of this for years. That may suggest that it is not easy for them to switch IP ranges.     

> __< rbrunner >__ Hmmm, that approach so far had zero downside in the particular case of our network, no? Why switch then     

> __< rbrunner >__ And it took years to becoming aware ...     

> __< r​ucknium:monero.social >__ They are spying on the bitcoin network, too. I don't recall if bitcoin did anything about them. boog900 , do you know?     

> __< rbrunner >__ Maybe the game will change now however     

> __< r​ucknium:monero.social >__ Bitcoin has a much better ASM diversity logic     

> __< 0​xfffc:monero.social >__ But privacy is not important aspect of Bitcoin.     

> __< rbrunner >__ Yeah, what would you even spy there :)     

> __< r​ucknium:monero.social >__ This is also a eclipse and network partition risk     

> __< r​ucknium:monero.social >__ Bitcoin cares about that     

> __< 0​xfffc:monero.social >__ Yes, that too. Makes sense.     

> __< 0​xfffc:monero.social >__ So what did Bitcoin do? Leave them alone?     

> __< b​oog900:monero.social >__ Some of their IPs have been on selsta's ban list for a while, you would think they would switch to get as many nodes as possible.     

> __< r​ucknium:monero.social >__ Thinking back... isn't there precedent for this when there was a network attack in December 2020? Not hardcoded, but the DNS record banlist, etc     

> __< r​ucknium:monero.social >__ But that was  abigger threat to network stability than this     

> __< b​oog900:monero.social >__ I don't but IIRC their main concern was a DOS vector due to these nodes just passively listening and not participating in normal tx flow: https://github.com/0xB10C/banlist/issues/1#issuecomment-2407202886     

> __< r​ucknium:monero.social >__ This is a post about the 2020 attack: https://sethforprivacy.com/posts/moneros-ongoing-network-attack/     

> __< r​ucknium:monero.social >__ > 2020-11-02 - PR6961 implemented to allow passing a banlist to monerod     

> __< rbrunner >__ Yes, introduction of banlists I would say. Totally optional and fully under user control, I would say. Nothing like a hardcoded opt-out banlist     

> __< v​tnerd:monero.social >__ Sorry I'm late as well, daylights savings tripped me up too. Not much report really, same as last week     

> __< r​ucknium:monero.social >__ I forgot to say thank you to boog900  for uncovering this proxy node issue :D     

> __< rbrunner >__ Now we all have one worry more :)     

> __< 0​xfffc:monero.social >__ Sorry for this digression, any of you is familiar with DNS TXT messages and how they work? I will DM you to ask few general questions.     

> __< r​ucknium:monero.social >__ We are past the hour. One more hopefully quick one:     

> __< r​ucknium:monero.social >__ 7) Proposal for FCMP++ HF Activation Rule to Retroactively Ignore Future unlock_time . https://github.com/monero-project/research-lab/issues/125     

> __< r​ucknium:monero.social >__ jeffro256  suggested that this be discussed for hopefully the last time at this meeting     

> __< rbrunner >__ For asking whether somebody changed their mind or had some really new insights, arguments, etc?     

> __< j​berman:monero.social >__ none from me     

> __< r​ucknium:monero.social >__ "<j​effro256:monero.social> I propose tentatively setting ignore-unlock-time block index `J` to 3401782, with threat of setting earlier. monero-project/research-lab #125#issuecomment-2448077632. We can discuss this in the next meeting, though" https://libera.monerologs.net/monero-research-lab/20241030#c453599     

> __< r​ucknium:monero.social >__ I am ok with the proposal from last time     

> __< c​haser:monero.social >__ I would prefer an earlier `J` date to minimize the risk of potential harm.     

> __< rbrunner >__ None from me either.     

> __< j​effro256:monero.social >__ I think I like kayaba's approach of activating after a median block timestamp     

> __< c​haser:monero.social >__ this is the part from jeffro's write-up that see as a source of risk: "If everything is within acceptable bounds, we ship the code using the wallet locked output cache as designed. **If not, we go back to the drawing board.**" (emphasis mine.) there are ~6 months left and 70% of the hash rate seems to mine time-locked transactions, ignoring the relay rule.     

> __< r​ucknium:monero.social >__ To be absolutely clear, this isn't a soft fork, right? Therefore, there is nothing to activate at the time point. Just something to write in the code that would take effect retroactively when the FCMP++ hard fork is activated, correct?     

> __< j​effro256:monero.social >__ Yes     

> __< j​effro256:monero.social >__ Yeah I guess we will have to see what happens     

> __< j​effro256:monero.social >__ It all takes place retroactively, we're not actually deploying code at the moment, so we can also change the rule retroactively as long as people support it     

> __< r​ucknium:monero.social >__ If a malicious actor starts packing blocks with txs with nonzero unlock time before 6 months, then the credible threat can be carried out: move the ignore date earlier. That's how I understand the proposal.     

> __< k​ayabanerve:matrix.org >__ Hi. I'm so sorry. I had something come up personally and had to dip out.     

> __< k​ayabanerve:matrix.org >__ I prefer announcing a time and using programmatic rules when the time comes than hardcoded constants.     

> __< k​ayabanerve:matrix.org >__ I have a strong distaste for coding constants across networks and having to deal with that.     

> __< j​effro256:monero.social >__ Yes. Since we can ignore anything locked, the only annoyance in the case of moving the ignore height back would be to the people who honestly wanted to use the feature, even though deprecated     

> __< c​haser:monero.social >__ Rucknium's data shows that there is already a near-zero on-chain interest in non-zero time locks. retroactively changing the cut-off date seems to be arbitrary, wouldn't look good IMHO.     

> __< j​effro256:monero.social >__ I agree it wouldn't be ideal, but at the end of the day we're announcing and getting rough consensus to remove `unlock_time`, this proposed ignore date is mainly just a nicety     

> __< r​ucknium:monero.social >__ chaser seems to have a concern about the proposal's details. Hopefully it can be addressed before next meeting. If not, I will put this on the agenda again. How does that sound?     

> __< c​haser:monero.social >__ Rucknium I'm okay with continuing the discussion in the MRL issue     

> __< r​ucknium:monero.social >__ Ok. Let's end the meeting here.     

> __< j​effro256:monero.social >__ Thanks everyone !     

> __< j​berman:monero.social >__ If we propose 3 months and someone spams in 2 months, it arguably looks even worse. I think 6 months is more reasonable in enabling lingering voices to be heard on the issue, and the option is still there to retroactively cut off     

> __< 0​xfffc:monero.social >__ Thanks everyone     

> __< r​ucknium:monero.social >__ A relevant issue and PR for ASN diversity: https://github.com/monero-project/monero/issues/7090 https://github.com/monero-project/monero/pull/7935     

> __< c​haser:monero.social >__ thank you all!     

> __< c​haser:monero.social >__ jberman: granted, it could happen at any time. why do you think it's worse though with 3 months? as for lingering voices, I have seen has been barely any since that post in September on Github.     

> __< c​haser:monero.social >__ and as for practical interest: there were 46 non-zero time locks during Sept 1 and Oct 13, out of which only one looked intentional (= locking for more than 10 blocks).     

> __< j​berman:monero.social >__ "We've moved up the timeline 3 months to reduce chances of an issue" *issue* would look a bit like incompetence. Moving the timeline doesn't make it significantly harder to pull off, unless we move it to a retroactive date, which the option is on the table to do still     

> __< c​haser:monero.social >__ yes, I see value in reducing the chance. (that's all that can be done aside from a retroactive decision.) as a rough consensus has already formed around May 1, I think the issue is I haven't voiced my concern in an explicit way earlier.     

> __< j​berman:monero.social >__ Re: hardcoding a banlist. Here is the DNS banlist PR, feature is disabled by default and enabled with `--enable-dns-blocklist`: https://github.com/monero-project/monero/pull/7138     

> __< j​berman:monero.social >__ Here are the hardcoded domains pointing to the banlist: https://github.com/monero-project/monero/blob/893916ad091a92e765ce3241b94e706ad012b62a/src/p2p/net_node.inl#L2030-L2038     

> __< j​berman:monero.social >__ IP's blocked by 1 as an example: https://www.nslookup.io/domains/blocklist.moneropulse.org/dns-records/txt/     

> __< j​berman:monero.social >__ For starters seems it makes sense to add boog900 's list there?     

> __< 3​21bob321:monero.social >__ Make it personal choice, your force a banlist and it might not be correct     

> __< b​oog900:monero.social >__ These nodes are defiantly not running `monerod`. I have 0 doubt. They are also almost certainly proxies, it's the only explanation of their behavior.     

> __< b​oog900:monero.social >__ I do not see a valid reason to run a proxy node.     

> __< 0​xfffc:monero.social >__ The key point is it is extremely cheap for them to run these proxies. We have to return the favour and attack there, make it costly. Some kind of PoW. Problem with that is ordinary nodes are going to pay a little bit of extra computation.     

> __< 0​xfffc:monero.social >__ IMHO     

> __< 0​xfffc:monero.social >__ Although if the attacker has a huge budget. That’s not gonna hurt either.     

> __< b​oog900:monero.social >__ I don't think a PoW that prevents proxies is possible. I did have one idea which is kinda like a mini proof-of-storage:     

> __< b​oog900:monero.social >__ If nodes build a lookup table of values using a sufficiently hard function, with the input being their address, then other nodes could request values from this table and verify their correctness. The function to create the table would have to be hard enough where nodes can't generate the values on the fly. Now if we say the table has to be 10GB big, for every address they need to <clipped message>     

> __< b​oog900:monero.social >__ create a 10GB lookup table.     

> __< b​oog900:monero.social >__ The problem is we are now adding 10GB to every nodes storage and it might take a while to startup the first time as the table is generated.     

> __< b​oog900:monero.social >__ And also it is still economical to run proxies, it's just more expensive now.     

> __< 0​xfffc:monero.social >__ Yes, you are right. They don’t even need to run all the proxies.     

> __< sech1 >__ boog900 you're thinking in the right direction, but I think it should be different. We need to find something monerod can do but a proxy can't do. For example, accessing some random bytes from the blockchain when connecting. It can't be proxied because real monerod will refuse this request for an already established connection, and it doesn't allow     

> __< sech1 >__ new connections from the same IP.     

> __< 0​xfffc:monero.social >__ How would the client verify the monerod answer? Random bytes from blockchain.     

> __< 0​xfffc:monero.social >__ By asking randomly from multiple other nodes (?) maybe.     

> __< sech1 >__ The client would ask for random bytes they already have themselves     

> __< b​oog900:monero.social >__ If they run the nodes they could just ask the main node for the bytes though     

> __< 0​xfffc:monero.social >__ s/asking/verifying/     

> __< 0​xfffc:monero.social >__ Yes, but I am thinking about cases where they don’t have it.     

> __< sech1 >__ right, they could ask their own node (which is modified), or they could just share a common network drive with the blockchain     

> __< sech1 >__ back to square one     

> __< 0​xfffc:monero.social >__ But nevermind.     

> __< b​oog900:monero.social >__ Proof of storage is the only actual way I think, stuff like the 10GB lookup table could be used to make it more expensive.     

> __< j​effro256:monero.social >__ Proof of storage doesn't prove that you're not running a proxy, just that you're running at least one node     

> __< 0​xfffc:monero.social >__ Quick question. This is the scenario I was thinking about.      

> __< 0​xfffc:monero.social >__ Imagine you have one proxy application. And you have 800 IP address that redirecting to that proxy application.     

> __< 0​xfffc:monero.social >__ Exactly. I was thinking about that and you beat me to it :))     

> __< b​oog900:monero.social >__ It does. It connects an address to the storage so to have multiple address you must store the blockchain multiple times     

> __< 0​xfffc:monero.social >__ Aha. You are generating some data based on the node specific address.      

> __< 0​xfffc:monero.social >__ And the client will use that address to query authenticity of your node.     

> __< j​effro256:monero.social >__ Oh so the order of the random data is bound to your IPv4 address?     

> __< sech1 >__ Or IPv6 address, or TOR address     

> __< j​effro256:monero.social >__ How does the requester verify a memory hard function bound to a network address without building the table for every single peer?     

> __< 0​xfffc:monero.social >__ I am not sure. But I believe there should be a lot of algorithms for doing that kind of asymmetric thing.     

> __< b​oog900:monero.social >__ it only has to compute a few of the values, randomly, not the whole table, and then request those values and check they line up.     

> __< 0​xfffc:monero.social >__ Kind of zkp :))     

> __< j​effro256:monero.social >__ Sounds like it     

> __< j​effro256:monero.social >__ Guess I just gotta look into the moon math.....     

> __< j​effro256:monero.social >__ Also sounds like an expensive operation for the prover. We then need some kind of PoW by the sender to start that computation....     

> __< 0​xfffc:monero.social >__ Very innovative. Basically:      

> __< 0​xfffc:monero.social >__ 1. Client should be able to verify with acceptable computation.      

> __< 0​xfffc:monero.social >__ 2. Node has to have the data to be able to respond in time.      

> __< 0​xfffc:monero.social >__ 3. Client will try as much as possible, say 100 times, to rest assure the node has the data.      

> __< 0​xfffc:monero.social >__ 4. For node it should not be easy to just compute correct answer without the storage.     

> __< 0​xfffc:monero.social >__ I see. Since it is expensive, it can introduce a new surface for another kind of DDoS.     

> __< b​oog900:monero.social >__ ah if you are talking about proof of storage, then that is done by "encrypting" the whole blockchain using your nodes identifier/address and then to verify you requests random, sequential, blockchain data and check that you can decrypt it. The decryption should be fast and the encryption should be relatively slow.     

> __< r​ucknium:monero.social >__ `A` --outboundConnection---> `B`     

> __< r​ucknium:monero.social >__ With these types of things, an honest Node `B` is just going to reduce its incoming connection count if the connection proving step is too expensive. With the Linking Lion threat model, it's node `B` that needs to do the proving that it's a real node.     

> __< r​ucknium:monero.social >__ Not a blocker to these types of proposals, but you have to look at incentives     

> __< b​oog900:monero.social >__ The proving should be cheep once nodes encrypt the data/create the lookup table     

> __< b​oog900:monero.social >__ FWIW I am not advocating for proof-of-storage, encrypting every new block is probably too expensive IMO for all nodes.     

> __< b​oog900:monero.social >__ The lookup table could work to make it more expensive for them, but might not fully stop them.     

> __< 0​xfffc:monero.social >__ Maybe we can have that as feature and optional layer of security.      

> __< 0​xfffc:monero.social >__ If user does not want it can opt in. And client can decide whether they pass txis to that node or not based on the user input.     

> __< 0​xfffc:monero.social >__ s/opt in/opt out/     

> __< 0​xfffc:monero.social >__ Nah. Makes it too complicated.     

> __< r​ucknium:monero.social >__ IMHO, if an opt-out list that avoids outbound connections is not acceptable, then the ASmap PR could be reviewed/updated and merged: https://github.com/monero-project/monero/pull/7935     

> __< j​effro256:monero.social >__ If we make it optional, then that's going to incentivize a higher fraction of spy nodes connections since honest, low-resource, node runners will opt out, but the spy nodes won't     

> __< r​ucknium:monero.social >__ That could reduce the Linking Lion share of an honest node's outbound connections to 1/12 = 8.3%     

> __< j​effro256:monero.social >__ This keeps looking like the best option with the fewest downsides: diversify outgoing connections with structural information about the network     

> __< j​effro256:monero.social >__ And it has other decentralization benefits not related to spying     

> __< 0​xfffc:monero.social >__ I vote + on asmap     

> __< r​ucknium:monero.social >__ I did a quick search of research papers on proving you are not a proxy node. Didn't find anything promising. Maybe I will ask the lead author of the D++ paper if she has any ideas. D++ requires running a node to be expensive for the threat model defense to work.     

> __< 0​xfffc:monero.social >__ But in addition to this discussion. I wish there was a way to verify the node is running monerod or not.     

> __< 0​xfffc:monero.social >__ Basically proof of storage might worth it in long run:      

> __< 0​xfffc:monero.social >__ 1. Client solves a hard puzzle. Send it to node.      

> __< 0​xfffc:monero.social >__ 2. Node verifies that hard puzzle is correct.      

> __< 0​xfffc:monero.social >__ 3. Proves to client that it is running monerod.      

> __< 0​xfffc:monero.social >__ Appears to me this will be useful in many places.     

> __< j​effro256:monero.social >__ Guys I've figured it out: captchas!!!     

> __< 0​xfffc:monero.social >__ It is not fair. Ruck can use reaction. We can’t :)     

> __< o​frnxmr:monero.social >__ asmap is a bad idea, i think     

> __< r​ucknium:monero.social >__ Will any mods in this channel re-enable emoji reactions please.     

> __< j​effro256:monero.social >__ I promise I won't abuse them.........     

> __< r​ucknium:monero.social >__ Nym has some node proofing. Maybe I will go re-read their white paper to see if it could help the Monero case.     

> __< knownsec >__ I know I'm not a dev but just wanted to say, asmap will reduce the risk of eclipse and Sybil attack but it also will reduce the overall network connectivity, overall I think it's a good short-term solution imho     

> __< j​effro256:monero.social >__ why would it reduce overall network connectivity ?     

> __< knownsec >__ because honest nodes can be "skipped", am I wrong?     

> __< knownsec >__ maybe it's not critical      

> __< r​ucknium:monero.social >__ If the ASmap criteria is used for outgoing connections only, probably it doesn't change the total number of connections in the network. Just changes the distribution, i.e. Hetzner nodes would get fewer incoming connections and nodes in ASNs with few nodes would get many more connections. You could hit the maximum feasible incoming connections, though.     

> __< r​ucknium:monero.social >__ That's my hypothesis at least.     

> __< r​ucknium:monero.social >__ Which reminds me of all sorts of papers about the effects of network connectivity distribution of gossip message propagation speed, etc. 😁     

> __< j​effro256:monero.social >__ knownsec: depends on how the selection policy uses the ASN information. If we selected more nodes "close" to us, that might make propagation faster, but reduce decentralization. If we selected nodes "far" from us, that might open us up to more Sybill attacks. You can also select a mix of the two, or choose ougoing connections such that they have a "diverse" ASN makeup as a whole. <clipped messag     

> __< j​effro256:monero.social >__ A good selection policy should be based in research, but there is probably some good balance of selecting IPs by ASN that allows for protecting from Sybill attacks and spy nodes, while also giving good connectivity     

> __< j​effro256:monero.social >__ Assuming the ASN information is accurate     

> __< knownsec >__ It's more complex than I thought : )     

> __< j​effro256:monero.social >__ Yes, very. ASN information is just information. There's an infinite number of algorithms we could posit to make decisions based on that information, most of them probably bad. In short, the ASN info and the decisions we make based on the ASN info is largely separate. So importing ASN information by itself shouldn't make connectivity worse, although a bad algorithm using ASN inform<clipped messag     

> __< j​effro256:monero.social >__ ation might make worse decisions than `monerod` currently makes     

> __< s​yntheticbird:monero.social >__ only solution is test in production /s     

> __< 3​21bob321:monero.social >__ Is there info on how these proxy nodes were identified ?     

> __< s​yntheticbird:monero.social >__ the MRL github issue gives an explanation     



# Action History
- Created by: Rucknium | 2024-11-05T20:34:02+00:00
- Closed at: 2024-11-19T20:53:37+00:00
