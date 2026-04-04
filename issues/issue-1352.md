---
title: Monero Research Lab Meeting - Wed 11 March 2026, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1352
author: Rucknium
assignees: []
labels: []
created_at: '2026-03-11T16:45:07+00:00'
updated_at: '2026-04-01T15:10:17+00:00'
type: issue
status: closed
closed_at: '2026-04-01T15:10:17+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

Live log: https://libera.monerologs.net/monero-research-lab

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/meeting.html?p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3. [FCMP code integration audit overview](https://github.com/seraphis-migration/monero/issues/294).

4. [FCMP beta stressnet](https://github.com/seraphis-migration/monero/issues/166).

5. Any other business

Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#1349 

# Discussion History
## Rucknium | 2026-03-18T16:23:06+00:00
Log

> __< rucknium >__ Meeting time! https://github.com/monero-project/meta/issues/1352     

> __< rucknium >__ 1. Greetings     

> __< vtnerd >__ Hi     

> __< rbrunner >__ Hello     

> __< UkoeHB >__ Hi     

> __< jberman >__ waves     

> __< jeffro256 >__ Howdy     

> __< gingeropolous >__ howdy do     

> __< yiannisbot:matrix.org >__ Hi     

> __< rucknium >__ 2. Updates. What is everyone working on?     

> __< gingeropolous >__ ironing out kinds in monerosim with rucknium:monero.social 's help     

> __< iamnew117:matrix.org >__ hello     

> __< yiannisbot:matrix.org >__ Apologies I didn't add it to the issue. We've been working on the Monero Network Topology, which my colleague dennis_tra:matrix.org has posted here before: https://probelab.io/blog/peering-into-privacy-a-deep-dive-into-the-monero-network-topology/.     

> __< rucknium >__ me: Started analysis of the output of gingeropolous:monero.social 's https://github.com/Fountain5405/monerosim. So far it is mostly as expected, i.e. not very different from the characteristics of mainnet log data.     

> __< rucknium >__ yiannisbot:matrix.org: Thanks. Do you want to discuss it at the end of the meeting?     

> __< vtnerd >__ Me: mostly completed zmq tx pub issues, but still one remains. Also got websocket /feed working between lws and lwsf, such that instant updates and reduced API chatter is now possible      

> __< yiannisbot:matrix.org >__ We wanted to get feedback on the study and discuss how we could improve our setup, i.e., what extra metrics would be of interest, as well as, whether there's interest to run our scripts continuously and present results at: https://probelab.io      

> __< yiannisbot:matrix.org >__ rucknium: Sure. What time is the end, roughly?      

> __< UkoeHB >__ Rereading papers. Planning to review carrot stuff, coordinate discussion for wallet design around carrot, figure out multisig for fcmp++     

> __< rucknium >__ yiannisbot:matrix.org: Probably at about 17:30 or 17:40 UTC.     

> __< jberman >__ Me: Had some discussion with koe re: integration audit plans (excited to have koe back!!), koe proposed combining phases 1 & 2 together since phase 1 is a fairly small amount of work. I'm currently preparing the PR's for phase 2 right now (about to submit PR's after this meeting), and will begin comms with audit firms today. A [... too long, see https://mrelay.p2pool.observer/e/gsb8uu4KZExDcjlw ]     

> __< rucknium >__ Welcome back, UkoeHB  :)     

> __< rucknium >__ 3. FCMP code integration audit overview (https://github.com/seraphis-migration/monero/issues/294).     

> __< UkoeHB >__ :)     

> __< jberman >__ Basically shared my update on it above     

> __< rucknium >__ Anything else on this agenda item?     

> __< jberman >__ Aiming to have a fleshed out proposal to raise funds for audits by next week's meeting      

> __< rucknium >__ 4. FCMP beta stressnet.     

> __< rucknium >__ AFAIK, beta stressnet will use tx relay v2 by default. monerosim's 1000-node run switched to tx relay v2 midway through. Things seemed to work properly in the simulation.     

> __< jberman >__ Scaling is done and in the branch (thank you jeffro256:monero.social, ArticMine , boog900:monero.social  and everyone involved in landing on a solution), beta stressnet branch is created. We have some final simple checklist items to cross off on our end from here https://github.com/seraphis-migration/monero/issues/166 , and  [... too long, see https://mrelay.p2pool.observer/e/9b2eu-4KUGNoVkY1 ]     

> __< jberman >__ Correct beta stressnet will use tx relay v2 by default     

> __< jberman >__ It's in the branch already as well     

> __< rucknium >__ Anything else on beta stressnet?     

> __< rucknium >__ yiannisbot:matrix.org: Do you want to discuss https://probelab.io/blog/peering-into-privacy-a-deep-dive-into-the-monero-network-topology/ ?     

> __< yiannisbot:matrix.org >__ rucknium: Sure.     

> __< yiannisbot:matrix.org >__ We're mainly looking for feedback as well as a sustainable way to keep this running and producing results continuously, i.e., funding :)      

> __< rucknium >__ A lot of the data is similar to what I've collected in https://xmrnetscan.redteam.cash/ (the backup domain to moneronet.info , which is down for now possibly due to an erroneous abuse report to the domain registrar).     

> __< rucknium >__ So you would want to go beyond that.     

> __< rbrunner >__ Do you plan further research? Or is "ongoing cost" mostly letting the infrastructure run long-term and update charts from time to time?     

> __< rucknium >__ You could each IP:port combination as s separate node. Technically, those are separate nodes, but monerod considers all nodes at the same IP address as the same node when it runs the node connection selection algorithm.     

> __< rbrunner >__ Oh, you have already a chapter "Looking Ahead" at the end of the report :)     

> __< yiannisbot:matrix.org >__ rbrunner: We can do a few things: i) at the base level we would set up infra to automate and produce these results continuously, but ii) we're also very interested to dive deeper into the pubsub protocol (dandelion++) to see how efficient it is in propagating messages. This could result in quite few critical metrics, such as duplicates.     

> __< yiannisbot:matrix.org >__ rbrunner: :-D Yes, there's that as well, but I gave a summary above too.      

> __< rbrunner >__ Thanks!     

> __< rucknium >__ Something you could do that I do not do is to try to estimate the number of unreachable nodes. AFAIK, the best way to do that is to run many nodes and then infer the approximate number of unreachable nodes based on the number of unreachable nodes that initiate connections to your node, i.e. are inbound connections to your node.     

> __< yiannisbot:matrix.org >__ Yeah, thanks rucknium:monero.social - I think both of these are doable.     

> __< rucknium >__ > Our next technical objective is to measure how this spy node density impacts Dandelion++ propagation.     

> __< rucknium >__ See the "Empirical privacy impact" section of my https://github.com/monero-project/research-lab/issues/126#issuecomment-2460261864     

> __< yiannisbot:matrix.org >__ We track the reachability/availability of nodes for the IPFS network: https://probelab.io/ipfs/topology/#chart-availability-classified-ts. I guess we could do something similar for the Monero network.      

> __< yiannisbot:matrix.org >__ rucknium: Thanks, I haven't read through that.      

> __< rucknium >__ The reachable/unreachable node ratio is important because the Dandelion++ stem phase propagates txs only to outbound connections.     

> __< yiannisbot:matrix.org >__ For message propagation, check metrics we have for Ethereum (and other networks): https://probelab.io/ethereum/gossipsub/     

> __< yiannisbot:matrix.org >__ rucknium: I would be very interested to look into Dandelion++. I remember reviewing this paper before it was published 😅     

> __< rucknium >__ You can also check my https://github.com/Rucknium/misc-research/blob/main/Monero-Peer-Subnet-Deduplication/pdf/monero-peer-subnet-deduplication.pdf and rbrunner 's PR https://github.com/monero-project/monero/pull/9939     

> __< rucknium >__ The deduplication algorithm will affect how you would estimate the number of unreachable nodes. It may be tricky because you do not know how many nodes are running the updated monerod version     

> __< yiannisbot:matrix.org >__ rucknium: But can you not track that through the agent version? 🤔     

> __< rucknium >__ No :D     

> __< rucknium >__ Monero is very private. Nodes are shy     

> __< rucknium >__ They don't tell you their version, deliberately.     

> __< rucknium >__ Reachable nodes, especially nodes with open RPC ports, can sometimes indirectly tell you by their behavior.     

> __< vtnerd >__ a hardfork is about the only way to tell     

> __< yiannisbot:matrix.org >__ I see :) It would be interesting to investigate if there's a way around it, through some heuristics or something.      

> __< rucknium >__ In the last few years, transactions with some characteristics were prohibited to be relayed. The size of the tx_extra field and custom lock time, IIRC.     

> __< rbrunner >__ Might be would treat such a possibility as something to correct ...     

> __< rucknium >__ So you can tell if a node is at least updated to a certain version by whether they reject those types of transactions.     

> __< rbrunner >__ Depending on what it would be exactly     

> __< rucknium >__ I will try to think of a good plan for you in the next few days and ping you in #monero-research-lounge:monero.social  for discussion. How does that sound?     

> __< rucknium >__ boog900:monero.social may have more ideas.     

> __< yiannisbot:matrix.org >__ rucknium: Sure, please ping me and dennis_tra:matrix.org . I'd like to understand how critical these items are for the community and if there's appetite to do some research and develop tooling for these topics.     

> __< rucknium >__ I think there is appetite :)     

> __< boog900 >__ I think trying to find another way to tell apart spy nodes would be good to try catch all the nodes now hiding the fingerprint. However this could be an almost impossible task.      

> __< rbrunner >__ It can give info, among other things, about spy nodes and their effects on the network, and I think it's probable that this will find support     

> __< rbrunner >__ Because it does have some importance     

> __< yiannisbot:matrix.org >__ Yeah, identifying spy nodes was one of the things we wanted to look more into as we did the study. But we ran out of time :)      

> __< yiannisbot:matrix.org >__ Great for all the input everyone! I would be more than happy to continue the discussion here or in the research lounge and see how we can take it further 👍     

> __< rucknium >__ I think I pointed Dennis to this paper, but just in case I didn't:  Kopyciok, Y., Schmid, S., & Victor, F. (2025). Friend or Foe? Identifying Anomalous Peers in Moneros P2P Network.   https://moneroresearch.info/280     

> __< rucknium >__ I ran the packet analysis software, but the results I got were hard to interpret. Or it seemed that there was a lot of scope for false positives.     

> __< UkoeHB >__ Would be interesting to analyze if spy nodes are all part of the same project or are split up. The topology graph implies they are the same project. And an analysis of nodes using Spruce Creek but not flagged as spy nodes.     

> __< rucknium >__ Here is the software: https://github.com/ykpyck/monero-traffic-analysis     

> __< rucknium >__ And my troubleshooting issue: https://github.com/ykpyck/monero-traffic-analysis/issues/1     

> __< rucknium >__ Anything else on this topic?     

> __< yiannisbot:matrix.org >__ Not from my end. Thanks for the feedback and the pointers. Let's be in touch in the coming days.      

> __< rucknium >__ We can end the meeting here. Thanks everyone.     

> __< jpk68 >__ Thanks :)     

> __< boog900 >__ > <rucknium> I think I pointed Dennis to this paper, but just in case I didn't:  Kopyciok, Y., Schmid, S., & Victor, F. (2025). Friend or Foe? Identifying Anomalous Peers in Moneros P2P Network.   https://moneroresearch.info/280     

> __< boog900 >__ I think this paper confirms they create outbound connections to random nodes to handle multiple inbound peers requests. The ping spam they mention is almost certainly the spy node checker being ran.     

> __< jpk68 >__ I don't mean to drag out the meeting, but I'd like to bring up a recent CCS proposal I've opened, if that's fine     

> __< rucknium >__ jpk68: Yes, you can bring it up.     

> __< jpk68 >__ It has to do with improving I2P support in monerod - StormyCloud, a nonprofit which works with the I2P project, has agreed to fund the proposal in full     

> __< jpk68 >__ -- with some changes to the milestones and funding structure     

> __< jpk68 >__ I'm just waiting to hear back from plowsof about some changes to it.     

> __< rucknium >__ This proposal? https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/650     

> __< jpk68 >__ Yes.     

> __< jpk68 >__ I thought I would mention this in case anyone was interested/wondering; the research portion of it also has to do with spy nodes to some extent     

> __< jpk68 >__ Not really in a direct sense, however I recently saw an issue opened by Gingeropolous (I think) about encouraging the use of anonymity networks to mitigate spy nodes. One of the major pain points with this, in my opinion is the fact that you can't fully sync a node over Tor or I2P     

> __< rucknium >__ vtnerd:monero.social: Do you have thoughts on this? ^     

> __< jpk68 >__ Perhaps if people are willing, the question of allowing node sync over I2P could be reopened - I think I2P (especially with SAM support) alleviates a lot of the bandwidth issues that were causing concerns     

> __< rucknium >__ Syncing everything over I2P also presents a sybil attack concern.     

> __< boog900 >__ It was the cheapness of generating addresses more than bandwidth that was the concern.      

> __< jpk68 >__ Yes, true. There is definitely more to discuss/consider in that regard     

> __< jpk68 >__ Aside from that specific issue though, I believe it would solve quite a few UX problems with anonymity networks :)     

> __< jpk68 >__ And even if you can't sync a node over I2P, spy nodes would perhaps be less of a problem, since you could more easily connect to a public I2P node if support is included in the GUI     

> __< vtnerd >__ we’ve kept off syncing over i2p/tor because it destroys the limited bandwidth + has eclipse attack issues (ipv4 is naturally a deterrent)     

> __< vtnerd >__ I thought I2P support was in the GUI? I don’t look at that (the gui) as often as I should     

> __< jpk68 >__ Nope :)     

> __< jpk68 >__ Well, you can configure SOCKS proxies in the GUI, I believe     

> __< vtnerd >__ I never saw an advantage to the SAM protocol because you still have to know/setup the port for the SAM protocol     

> __< vtnerd >__ yes, so there is support for it just indirectly     

> __< jpk68 >__ Do you mean from a UX standpoint?     

> __< vtnerd >__ yes theres still just as much friction, unless you just auto-assume the port     

> __< jpk68 >__ As mentioned in the link below, there is a lot of metadata leakage that can occur with I2P using SOCKS     

> __< jpk68 >__ https://i2p.net/en/docs/api/socks/     

> __< vtnerd >__ I guess its easier than manually setting up your hidden service address     

> __< jpk68 >__ I2P devs are strongly in favor of deprecating the I2P SOCKS route and using SAM instead     

> __< vtnerd >__ that disclaimer is for generic usage, not our specific case     

> __< jpk68 >__ vtnerd: Yes, that too. You won't need to manually configure tunnels     

> __< jpk68 >__ I agree with that, however there are many other reasons, as listed here:     

> __< vtnerd >__ as in, our p2p protocol can still leak metadata even with sam, its not specifically a socks issue     

> __< jpk68 >__ https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/454     

> __< jpk68 >__ From the standpoint of I2P nodes, yes     

> __< vtnerd >__ the only benefit is the auto-creation of services, but with the caveat your still typically setting up i2p + knowing the port     

> __< jpk68 >__ Users using I2P as an anonymizing layer also are negatively affected by support for only SOCKS, because addresses can be leaked/correlated with other services     

> __< vtnerd >__ are you putting SAM in gui or monerod? how are you going to: “Provide GUI indication of external router status up/down” in the gui?     

> __< vtnerd >__ because addresses can be leaked/correlated with other services -> you mean if they reuse an endpoint?     

> __< jpk68 >__ Yes. All applications which use the same SOCKS proxy (as an I2P bridge) share the same destination address     

> __< vtnerd >__ fwiw Im partially against syncing over I2P as its probably usually a bad idea, but more favorable to supporting SAM     

> __< vtnerd >__ same destination address? you mean in the reverse direction?     

> __< vtnerd >__ that sounds like a sh** implementation in I2P to me, but I dunno     

> __< vtnerd >__ tor just creates tunnels on the fly iirc     

> __< jpk68 >__ vtnerd: At present, the plan is to replace the I2P SOCKS code path with SAM, as well as to add a page in the GUI for configuring router connections. Plus a rewrite of docs, and migration options for current i2p-zero users     

> __< jpk68 >__ vtnerd: That's what SAM does, it allows the application to create specific tunnels     

> __< jpk68 >__ If you look at the link I sent above, there is more information about I2P SOCKS issues under the "What's wrong with SOCKS?" header     

> __< vtnerd >__ yes, but there’s zero reason this couldn’t be done over SOCKS, unless Im missing something. its not like every SOCKS connections uses the same ip+port coming in     

> __< vtnerd >__ yes, they’re primarily complaining about routing arbitrary stuff over SOCKS as its typically a bad idea. But monerod+socks+i2p has already been investigating for scrubbing, so its a non-argument     

> __< jpk68 >__ I'm restating what has already been said in the original CCS the I2P devs opened a few years ago. You may find the information there informative     

> __< vtnerd >__ and there’s nothing about re-using i2p destination addresses     

> __< jpk68 >__ Thanks for sharing your perspective though, I appreciate it     

> __< jpk68 >__ Again, they share the return address     

> __< vtnerd >__ then why don’t they say that in this writeup? They wasted a bunch of words to say that generic protocols over i2p is bad.     

> __< jpk68 >__ I'm not sure to be honest. I must admit though, after looking into this I am pretty convinced that SAM would be a huge improvement. Bitcoin Core has already done this and it works really well.     

> __< vtnerd >__ I really doubt they re-use connections, or need to for their implementation, but I could be missing something     

> __< vtnerd >__ yes, if it reduces friction for starting inbound services its probably a win     

> __< jpk68 >__ You also have to trust users to set up the SOCKS tunnel correctly, which is done differently for every I2P implementation. Whereas SAM is a standardized protocol that does everything for you, including managing keys     

> __< jpk68 >__ Yes :)     

> __< jpk68 >__ It is also worth noting that the CCS will be changed to a commit/feature-based milestone structure rather than a time-based one     

> __< jpk68 >__ That is in the works, I am just waiting to hear back from some people     

> __< vtnerd >__ setup the socks correctly? its the same level of difficulty of setting up i2p+sam port     

> __< vtnerd >__ thats been my complaint - you can basically get everything but inbound working with same level of friction     

> __< jpk68 >__ No, because users will have to use a different SOCKS tunnel for every application to avoid correlation     

> __< vtnerd >__ ….again …. why? each socks tunnel can be a unique i2p tunnel.     

> __< vtnerd >__ and they never mention this in the writeups, this should be highlighted on that page     

> __< jpk68 >__ Because it's a pain and fixing it would improve UX     

> __< jpk68 >__ I'm not sure what you mean by 'not mentioned in the writeups'     

> __< vtnerd >__ as in each SOCK connection is a unique i2p connection     

> __< vtnerd >__ the fact that app A and app B use the same socks port is irrelevant as each connection will be unique anyway     

> __< jpk68 >__ I'm not quite sure, to be honest.     

> __< jpk68 >__ Regarding your last message, again, they share the same destination address     

> __< jpk68 >__ This is still a heuristic     

> __< vtnerd >__ an example, tor would have massive correlation issues with its exit nodes if SOCKS were inherently this bad     

> __< jpk68 >__ Yes, and this is why I2P devs have never recommended SOCKS for applications like this. You can put any protocol over I2P, pretty much     

> __< vtnerd >__ I guess I should explain - with SOCKS you only get to make one proxied request. You can’t re-use the connection     

> __< jpk68 >__ That doesn't mean it's going to be good or work well     

> __< vtnerd >__ so you can’t footgun yourself with SOCKs, except for the issue with privacy within the proxied data     

> __< vtnerd >__ otherwise tor+socks would’ve been a disaster long ago with its exit nodes     

> __< vtnerd >__ its literally the same thing for outbound connections, thats my only point, and if you think you can make it easier for setup have at it     

> __< jpk68 >__ Thank you :)     

> __< vtnerd >__ Im just not convinced that people can setup i2p but not the hidden service element. there’s already tons of friction     

> __< jpk68 >__ Of course there is still much to discuss and I am very open to taking input from people about this. Nothing is set in stone, and I'm just saying I think it's worth looking into     

> __< jpk68:matrix.org >__ Not sure why my IRC connection dropped. I'm still here if there are any other questions/concerns :)     

> __< vtnerd >__ jpk68_looks like i2p uses the same source address for socks, per run, instead of cycling through them like tor.     

> __< vtnerd >__ if you can hook into SAM to create a new circuit/tunnel per tx-relayed that would definitely be a win     

> __< vtnerd >__ we may have to randomize when this occurs though, as that too could leak metadata about when a tx is relayed     

> __< vtnerd >__ but I forgot this is an outstanding issue with tor that someone pointed out (although typically with tor we are cycling through connections anyway, which is probably better than manually requesting one)     

> __< vtnerd >__ although with fcmp++ I guess it doesnt really matter anymore     

> __< jpk68:matrix.org >__ Yes, for sure :)     

> __< jpk68:matrix.org >__ That is one of the main research areas in the proposal     

> __< vtnerd >__ er nevermind (most) of this, creating new tunnels per tx relay is likely problematic. anyway we randomize which tor/i2p connections a tx gets relayed over anyway, to mitigate this issue     

> __< vtnerd >__ can you be more specific?     

> __< vtnerd >__ with tor we likely need randomized destructions of connections. that way we slowly cycle through circuits+rarely re-use same connection to relay tx.     

> __< vtnerd >__ with i2p it looks trickier, because socks never cycles through routes, but then we are left to do this “on our own” which is unfortunate compared to tor     

> __< vtnerd >__ jpk68:matrix.org: the ccs proposal doesn’t mention anything about what I’ve just said?     

> __< jpk68:matrix.org >__ vtnerd: Have you checked the updated version?     

> __< jpk68:matrix.org >__ "Decide on ACCEPT vs FORWARD for incoming connections, permanent vs transient destinations"     

> __< jpk68:matrix.org >__ That's the same thing, no?     

> __< jpk68:matrix.org >__ Whether or not new tunnels/identities are created per transaction, etc.     

> __< vtnerd >__ I dont see how that relates. incoming here refers to the people accepting the txes to be relayed (and so to does destination); transient circuits/tunnels outgoing is more useful in our context     

> __< jpk68:matrix.org >__ That could be part of it as well     

> __< vtnerd >__ transient destinations just makes the connections less stable (as the p2p sharing is constantly “old”), whereas transient outgoing provides protection against sending 2 txes to the same peer     

> __< vtnerd >__ *transient outgoing -> transient connections/circuits/tunnels, etc     

> __< vtnerd >__ as in, if you want inbound addresses to constantly change, you’ll have thoroughly test that it doesn’t destroy the ability to make new p2p connections in sane way. imagine if every ipv4+port inbound p2p just randomly changed its ip every hour, the peerlist sharing will be terrible     

> __< vtnerd >__ in fact, this is a point against SAM, in practice we want long-lived inbounds to keep the p2p system health     

> __< vtnerd >__ I’ll just start a discussion on ccs site.     

> __< jpk68:matrix.org >__ It does seem like a bad idea to have transient destinations for I2P nodes (P2P traffic), but is that even something we have to worry about if I2P nodes can't sync the chain right now?     

> __< vtnerd >__ yes, it should make it harder for nodes to relay to such peers     

> __< vtnerd >__ As an exaggerated  example, if the destination cycled every minute, the majority of the connections are likely to nodes using the “existing” long-term destination setup. we would have tons of peers making useless entry points, and slow down p2p connection making     

> __< plowsof >__ thanks vtnerd     



# Action History
- Created by: Rucknium | 2026-03-11T16:45:07+00:00
- Closed at: 2026-04-01T15:10:17+00:00
