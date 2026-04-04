---
title: Monero Research Lab Meeting - Wed 16 July 2025, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1239
author: Rucknium
assignees: []
labels: []
created_at: '2025-07-15T21:57:30+00:00'
updated_at: '2025-07-25T20:47:38+00:00'
type: issue
status: closed
closed_at: '2025-07-25T20:47:38+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/meeting.html?p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3.  [SLVer Bullet: Straight Line Verification for Bulletproofs](https://github.com/cypherstack/silver-bullet).  [Cypher Stack review of divisors for FCMP](https://github.com/cypherstack/divisor_deep_dive).

4. [FCMP++ optimization coding competition](https://www.getmonero.org/2025/04/05/fcmp++-contest.html).

5. [FCMP alpha stressnet planning](https://github.com/seraphis-migration/monero/issues/53#issuecomment-3053493262).

6. [Spy nodes](https://github.com/monero-project/research-lab/issues/126).

7.  CCS proposal: [Monero Network Simulation Tool](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/589).

8. Any other business

Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#1235 

# Discussion History
## Rucknium | 2025-07-18T20:11:27+00:00
Logs

> __< k​ayabanerve:matrix.org >__ 👋     

> __< a​rticmine:monero.social >__ Hi     

> __< rbrunner >__ Hello     

> __< j​berman:monero.social >__ *waves*     

> __< r​ucknium:monero.social >__ Meeting time! https://github.com/monero-project/meta/issues/1239     

> __< r​ucknium:monero.social >__ 1) Greetings     

> __< j​effro256:monero.social >__ Howdy     

> __< s​gp_:monero.social >__ hello     

> __< b​oog900:monero.social >__ hi     

> __< s​packle:monero.social >__ hi     

> __< v​tnerd:monero.social >__ hi     

> __< a​ntilt:we2.ee >__ seas     

> __< r​ucknium:monero.social >__ 2) Updates. What is everyone working on?     

> __< k​ayabanerve:matrix.org >__ Hm. I just got the messages from monero.social with a delay of ten to thirty seconds. I'm unsure if that's my environment, or if the Matrix bridge is quirky again...     

> __< a​rticmine:monero.social >__ I have the scaling and fees document     

> __< ArticMine >__ https://github.com/ArticMine/Monero-Documents/blob/master/MoneroScaling2025-07.pdf     

> __< a​rticmine:monero.social >__ I posted this directly on IRC via my laptop     

> __< r​ucknium:monero.social >__ me: Set up experimental API and Tor onion hidden service for https://moneronet.info/ :  `https://api.moneronet.info/__docs__/` (you need the trailing slash or it won't take you to the docs)   http://moneronet7hxetyzkewttitl3w6p2oxwvss4arzvlcyfmyavlw23skqd.onion/     

> __< r​ucknium:monero.social >__ 3) [SLVer Bullet: Straight Line Verification for Bulletproofs](https://github.com/cypherstack/silver-bullet).  [Cypher Stack review of divisors for FCMP](https://github.com/cypherstack/divisor_deep_dive).     

> __< v​tnerd:monero.social >__ me: finally switched to monero_c+lwsf integration     

> __< j​berman:monero.social >__ me: mostly contest handling     

> __< r​ucknium:monero.social >__ Updates on SLVer Bullet?     

> __< s​gp_:monero.social >__ For SLVer Bullet (and divisors generally), I expect a proposal for a zkSecurity review next meeting or the following     

> __< s​gp_:monero.social >__ Not much to discuss this second     

> __< r​ucknium:monero.social >__ sgp_: Thanks. Please give at least 24 hours between posting the proposal and the MRL meeting time.     

> __< b​asses:matrix.org >__ new paper     

> __< b​asses:matrix.org >__ Scaling privacy-preserving cryptocurrencies with toxic decoys     

> __< b​asses:matrix.org >__ https://crypto.unibe.ch/2025/07/11/decoys.html     

> __< b​asses:matrix.org >__ >A detailed simulation of the new technique, using a transaction data set gathered from the Monero cryptocurrency, shows that the storage space can be reduced by approximately 60% while maintaining the same degree of privacy.     

> __< r​ucknium:monero.social >__ rando: Thanks. My black marble attack paper is cited by this paper :D     

> __< r​ucknium:monero.social >__ >  Our estimation approach can be compared with the analysis presented by Rucknium [Ruc24]. That study applies a slightly more sophisticated metric to estimate corruption levels during the attack, but our approach yields a roughly similar number of corrupted outputs. Our estimation metric is also lightweight, which aligns with an on-chain dynamic adjustment of k.     

> __< r​ucknium:monero.social >__ 4) [FCMP++ optimization coding competition](https://www.getmonero.org/2025/04/05/fcmp++-contest.html).     

> __< j​berman:monero.social >__ We'd like to officially declare fabrizio the winner of the ec-divisors contest. fabrizio's submission was excellent. We're all very excited for the 95%+ speed-up it brings to blinds construction. It will simplify the FCMP++ integration a significant degree by removing the need for a distinct cache to pre-calculate and store blinds. Further, it largely removes any need for further <clipped message>     

> __< j​berman:monero.social >__ optimization to this particular section of code in the future. We want to thank fabrizio for participating!     

> __< j​berman:monero.social >__ We'll make a more formal announcement soon     

> __< j​berman:monero.social >__ We'd like to return to helioselene later in this meeting     

> __< r​ucknium:monero.social >__ 5) [FCMP alpha stressnet planning](https://github.com/seraphis-migration/monero/issues/53#issuecomment-3053493262).     

> __< j​effro256:monero.social >__ Blocker tasks: https://github.com/seraphis-migration/monero/issues/53#issuecomment-3053493262     

> __< s​packle:monero.social >__ Friendly reminder that there are open PRs from the first stressnet to consider including in upcoming testing. This was discussed in early May, but I don't believe it was ever settled.     

> __< j​berman:monero.social >__ We've been more focused on the contest this past week, so hopefully will make more progress on those alpha stressnet tasks for next week's meeting. kayabanerve has been helping us with contest follow-up as well     

> __< j​berman:monero.social >__ spackle / Rucknium can one of you guys re-share those other PRs in that issue that jeffro linked so we can also track them there?     

> __< s​gp_:monero.social >__ fwiw for the purposes of a stressnet, I don't consider "Divisors re-impl from SLVer bullet" to be a strict blocker. If that scheme is chosen then obviously that implementation needs to be tested at some point, but even without it, a stressnet could be useful (for everything else)     

> __< j​berman:monero.social >__ Probably fair considering it's not expected to have much of an impact on performance in any case nor much of the rest of the code, as it's mostly an internal detail     

> __< r​ucknium:monero.social >__ Speaking for myself, I don't want to struggle with slow tx construction when spamming stressnet     

> __< r​ucknium:monero.social >__ It is already slow enough for CLSAG     

> __< s​gp_:monero.social >__ I mean use the current divisors technique for the stressnet, if the SLVer Bullet option is selected AND not ready when everything else is ready     

> __< s​packle:monero.social >__ jberman: Will do     

> __< r​ucknium:monero.social >__ I plan to help with tx spamming on alpha stressnet, at least until everything breaks (and hopefully it doesn't break).     

> __< j​berman:monero.social >__ divisors re-impl shouldn't have a significant impact on tx construction time anyway fwiw (integrating fabrizio's submission will, and also obviously speeding up prove() will / is also effectively a required pre-req for >8 input txs)     

> __< r​ucknium:monero.social >__ jberman: When did you want to discuss Heliosene part of the contest? In this agenda item, or do you plan for it to be the last agenda item today?     

> __< j​berman:monero.social >__ We can do that now     

> __< j​effro256:monero.social >__ We'd like to officially declare lederstrumpf the winner of the helioselene contest. This was a more challenging decision as we received a number of quality submissions. We want to thank all contestants for making the decision process interesting. Overall, we the judges, believe lederstrumpf's submission provides the strongest base to continue from. It performed competitively again<clipped messag     

> __< j​effro256:monero.social >__ st the other unmodified submissions, outperformed in WASM, and consistently performed the best after replacing variable-time arithmetic in rafael-xmr's submission and reverting ed25519 changes in Tritonn204's submission. We provide a more detailed summary on github here: https://github.com/j-berman/fcmp-plus-plus-optimization-competition/blob/main/docs/helioselene-decision.pdf     

> __< k​ayabanerve:matrix.org >__ Anecdotally, I believe lederstrumpf's submisison out-right outperformed the submission by tritonn, regardless of our changes which re-introduced bespoke field arithmetic.     

> __< j​berman:monero.social >__ I also want to advocate for a 2nd place prize for helioselene. Ignoring the 1st place submission, we agree on a 2nd submission which we would have used instead. My primary original reasoning for removing a 2nd place prize was because it could be gamed by a single contestant making multiple submissions. Considering we ended up receiving distinct submissions from distinct contestant<clipped message>     

> __< j​berman:monero.social >__ s, I'm now in favor of bringing back a 2nd place prize     

> __< r​ucknium:monero.social >__ Could you explain the impact of the discrepancy between the real-life CPU benchmark speedup and the WASM speedup? Practically, should we be looking at the real-life CPU benchmarks as what is actually gained?     

> __< j​effro256:monero.social >__ I want to put out there that if any of the Helios-Selene contestants would like more detailed feedback that isn't present in the decision document, please reach out to the judges, j-berman and I, and we would be happy to give it. We can also post the comments publicly if you are okay with it     

> __< k​ayabanerve:matrix.org >__ They're two different platforms and two different scoring mechanisms. We included the WASM benchmark as it was canonical and universal (avoiding 'well it's 500x faster on my machine'), yet included the x86-64 benchmark as it is our primary target. The performance obviously trends together, with deviated scores within WASM indicating an anecdote on the code's portability (which may<clipped message     

> __< k​ayabanerve:matrix.org >__  be beneficial to those who attempt to run the same code on ARM devices, or RISC-V devices).     

> __< r​ucknium:monero.social >__ Thank you jberman , and jeffro256  for all your judging effort!     

> __< k​ayabanerve:matrix.org >__ ('we' = me when I originally sketched the contest)     

> __< k​ayabanerve:matrix.org >__ TL;DR Canonicity + some idea of portability without benching across 100 different real-world devices     

> __< r​ucknium:monero.social >__ jberman: Do you want this 2nd place prize suggestion to be discussed, or do you think it is within the judges' right to make that call on your own?     

> __< a​rticmine:monero.social >__ I would support what the judges decide     

> __< r​ucknium:monero.social >__ Would this keep the total XMR value of the Heliosene prize the same (i.e. split the pot as it exists), or do you suggest that the top prize XMR stay the same and some additional XMR be allocated for 2nd place?     

> __< j​berman:monero.social >__ The former. I'd also like to propose an additional 30 XMR from the General Fund allocated toward the 2nd place prize     

> __< j​berman:monero.social >__ the former being "Do you want this 2nd place prize suggestion to be discussed" :)     

> __< j​berman:monero.social >__ I suggest that the top prize XMR stay the same and 30 additional XMR be allocated for 2nd place     

> __< j​effro256:monero.social >__ Interestingly, rafael-xmr and Trintonn204 both used different inversion algorithms, whereas lederstrumpf used the default inversion algorithm provided in `crypto_bigint`. We have looked into using either Bernstein-Yang or binary GCD inversion on lederstrumpf's submission and have already observed benefits onto of lederstrumpf's speed from doing so. We can't actually use either inv<clipped messag     

> __< j​effro256:monero.social >__ ersion code directly because of field representations and u128 arithmetic discussions.     

> __< r​ucknium:monero.social >__ I think this is OK if the Core General Fund would be OK with contributing the 30 additional XMR     

> __< rbrunner >__ Same     

> __< k​ayabanerve:matrix.org >__ I personally believe Rafael invested notable time and effort to produce a quality entry and deserve acknowledgement appropriately. I wrote such a prize in when sketching the contest to reward those, and ensure contributors don't walk away with nothing due to being great, yet not the best.     

> __< j​berman:monero.social >__ To be clear, Rafael is the contestant in mind for the 2nd place prize, also considering their submission is a clear 2nd best     

> __< j​effro256:monero.social >__ If lederstrumpf's submissions wasn't submitted, rafael's submission would have been the most performant, and most likely the submission that we would moved forward with in code. So even though now rafael-xmr's code directly might not make it into the final product, the idea of using Bernstein-Yang inversion was valuable, especially when comparing Tritonn204's usage of the binary G<clipped messag     

> __< j​effro256:monero.social >__ CD inversion, because the BY inversion proved to be faster than binary GCD in his implementation, even though previously we thought that binary GCD would be the fastest.     

> __< a​ck-j:matrix.org >__ Its interesting to see most submissions hovering just above the 20% requirement. Makes you wonder what would have happened if the threshold was 30%…     

> __< r​ucknium:monero.social >__ Was the 20% requirement for the real life CPU or WASM benchmarks?     

> __< j​effro256:monero.social >__ Both     

> __< r​ucknium:monero.social >__ In auction theory, I think the 20% requirement could be called the "reservation price" of the auctioneer.     

> __< r​ucknium:monero.social >__ Fun fact (or hypothesized fact). Anyway, More to discuss about the contest and/or alpha stressnet planning?     

> __< k​ayabanerve:matrix.org >__ I also spent *nine hours* working through an even further optimized binary GCD implementation to work through that theory jeffro256 :C     

> __< j​berman:monero.social >__ Reasonable / fair to ping binary fate asking if the GF would fund an additional prize given the above discussion?     

> __< r​ucknium:monero.social >__ Yes     

> __< a​rticmine:monero.social >__ Yes     

> __< rbrunner >__ Would say so     

> __< r​ucknium:monero.social >__ ArticMine: Do you want me to put this on the agenda for next meeting? https://github.com/ArticMine/Monero-Documents/blob/master/MoneroScaling2025-07.pdf     

> __< j​berman:monero.social >__ Thank you :)     

> __< a​rticmine:monero.social >__ Yes     

> __< a​rticmine:monero.social >__ Please put it on the agenda     

> __< r​ucknium:monero.social >__ Great. I will do so. Thanks for the write-up.     

> __< r​ucknium:monero.social >__ 6) [Spy nodes](https://github.com/monero-project/research-lab/issues/126).     

> __< r​ucknium:monero.social >__ I set up experimental API and Tor onion hidden service for https://moneronet.info/ :  `https://api.moneronet.info/__docs__/` (you need the trailing slash or it won't take you to the docs)   http://moneronet7hxetyzkewttitl3w6p2oxwvss4arzvlcyfmyavlw23skqd.onion/     

> __< r​ucknium:monero.social >__ I am investigating having ditatompel's remote node list ( https://xmr.ditatompel.com/remote-nodes ) call the API and displaying the ban list status in its table so remote node users can be informed: https://github.com/ditatompel/xmr-remote-nodes/issues/191     

> __< r​ucknium:monero.social >__ I contacted a few public remote node operators about enabling the MRL ban list. I found that at least one of the node operators had unintentionally downloaded the HTML GitHub page instead of the raw text file for the ban list. I have edited the meta issue and left a comment there about it: https://github.com/monero-project/meta/issues/1124#issuecomment-3079469381     

> __< r​ucknium:monero.social >__ A side effect of the network crawler is a list of the `peer_id` that the proxy spy nodes fail to properly spoof. In other words, we can see which "honest" node, by their `peer_id`, each proxy spy node is pulling data from to try to act like a real, non-proxied node. Then, we can match the `peer_id`s to the real nodes in the dataset. To me, the proxied honest nodes seem to be a ran<clipped message     

> __< r​ucknium:monero.social >__ dom selection of honest node on the network. I didn't notice anything unusual about them on a quick glance.     

> __< r​ucknium:monero.social >__ Any ideas about what could be done with this info? I had an idea to set up one or more node "honeypots" that could be selected as proxied honest nodes by the spy nodes. Then, issue a ping "doorknock" to proxy spy nodes that could be logged on the honeypot(s). From there, you could figure out which IP addresses the proxying it happening from, and other characteristics. You might as<clipped message     

> __< r​ucknium:monero.social >__ sume that each spy nodes is performing the proxying from the same IP address as it appears in the network, but we do not observe that spy nodes make outbound connections (or, very rarely). Therefore, they may be using different IP address(es) for this. I hope this is clear. It could use a diagram.     

> __< r​ucknium:monero.social >__ The proxy behavior is maddening because the adversary is using honest nodes against each other.     

> __< a​rticmine:monero.social >__ This is an interesting way to spy on the spy nodes.      

> __< a​rticmine:monero.social >__ It may be helpful to identify who is behind this.     

> __< r​ucknium:monero.social >__ I also found that almost all of the node IP addresses on the DNS ban list disappeared from the network some time in the last year. Those IP addresses, except for four `/24` subnets in the DNS ban list, had been added a because of network attacks in 2020. I will suggest that 3 of those old, inactive IP addresses could be replaced by the remaining `/24` subnets on the MRL/boog900 ban list.     

> __< r​ucknium:monero.social >__ That won't get all of the MRL ban list IP addresses, but it will get a lot of then since the `/24` subnets have 254 spy nodes in them each (except for one of the subnets that has about have that number)     

> __< r​ucknium:monero.social >__ More info about that in a discussion today in #monero-dev:monero.social     

> __< r​ucknium:monero.social >__ Any more discussion on this?     

> __< r​ucknium:monero.social >__ 7) CCS proposal: [Monero Network Simulation Tool](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/589).     

> __< a​ntilt:we2.ee >__ ... set up a info web site ?     

> __< r​ucknium:monero.social >__ This proposal was discussed at Saturday's Monero Community Workgroup meeting: https://github.com/monero-project/meta/issues/1233     

> __< r​ucknium:monero.social >__ I also gave support and comments for it on the CCS page: https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/589#note_30729     

> __< r​ucknium:monero.social >__ Some people at the Community meeting did not like that gingeropolous is using AI to assist writing the code. I am pretty sure he is using AI     

> __< r​ucknium:monero.social >__ flip flop: I could add it to moneronet.info , at least as an API endpoint     

> __< a​ntilt:we2.ee >__ simply to inform nodes of their own status :;     

> __< r​ucknium:monero.social >__ Yes, I could make it another column in the node table. The table is getting crowded, but I could probably fit it in. (And users can optionally hide specific columns with the column visibility button on the table.)     

> __< r​ucknium:monero.social >__ Any other business?     

> __< s​gp_:monero.social >__ Yeah, xmrack and I want to bring attention to one fuzzing item     

> __< r​ucknium:monero.social >__ Go ahead :)     

> __< s​gp_:monero.social >__ The MAGIC Monero Fund recently raised funds and contracted ADA Logics to performing fuzzing for Monerod's RPC endpoints, and so far it's already yielded important results. But not about that, the important bit to get on people's radar is the emails attached to the OSS-Fuzz repo: https://github.com/google/oss-fuzz/blob/master/projects/monero/project.yaml#L4-L7     

> __< s​gp_:monero.social >__ xmrack: is reaching out to some people directly (feel free to chime in!), but at a high level, these emails should be updated to the current Monero HackerOne VRP reviewers, and we also strongly suggest adding ADA Logics to this list temporarily, while they are configuring Monero's OSS-Fuzz implementation     

> __< s​gp_:monero.social >__ All the emails on this list are informed of potential vulnerabilities from oss-fuzz     

> __< s​gp_:monero.social >__ No discussion needs to happen here, but I wanted to make sure it was raised here and to see if anyone had any questions     

> __< r​ucknium:monero.social >__ Sounds good to me. Thanks for paying attention to that important detail.     

> __< r​ucknium:monero.social >__ I may have already mention this to you, but according to my net scan, about 25% of honest reachable nodes have RPC enabled. It is important to detect vulnerabilities in RPC: https://moneronet.info/     

> __< r​ucknium:monero.social >__ I guess I have my own "other business": I have been updating the Qubic mining hashpower share plots every week. It looks like the last two or three weeks, their rise in hashpower share has halted. They get a max of about 15% (measured on a 24-hour basis) on the weekends, when they put up their highest effort: https://gist.github.com/Rucknium/0873b10b6d36ff6c9d6f8f54107d16f7     

> __< s​gp_:monero.social >__ is this 25% with _any_ RPC open, restricted or unrestricted?     

> __< r​ucknium:monero.social >__ Any RPC. Unrestricted RPC is very insecure.     

> __< s​gp_:monero.social >__ Yeah, hopefully no one has that open :p     

> __< r​ucknium:monero.social >__ I mean, unrestricted RPC open to the wide internet     

> __< r​ucknium:monero.social >__ I could try to check for that specifically in the net scan, but I don't want to publish that info since it's a big target on those nodes, if they exist (and may not exist for long if they have that open, anyway).     

> __< r​ucknium:monero.social >__ We can end the meeting here. Thanks everyone.     

> __< s​gp_:monero.social >__ Thank you     

> __< a​rticmine:monero.social >__ Thanks     

> __< j​effro256:monero.social >__ Thanks everyone     

> __< a​ck-j:matrix.org >__ The benefit of adding david from adalogics (temporarily) to the email list of OSS-Fuzz is that his team will be able to more effectively troubleshoot the harnesses as they can potentially hit edge cases and need to be updated. Monero’s OSS-Fuzz integration has been neglected for a while now and having david (the #1 contributor to the OSS-Fuzz project) making sure everything is r<clipped message>     

> __< a​ck-j:matrix.org >__ unning smoothly would IMHO be a great asset to the monero community.     

> __< a​ntilt:we2.ee >__ rucknium Are you refering to reusing the "peer-id" here ?     

> __< r​ucknium:monero.social >__ They are making honest nodes do the actual work of hosting the blockchain databases and responding to p2p requests. Then, they just capture the traffic as man-in-the-middle.     

> __< r​ucknium:monero.social >__ At least, that's the leading hypothesis. A honeypot system like I described could confirm it.     

> __< r​ucknium:monero.social >__ Spy vs. Spy, if you will     

> __< a​ck-j:matrix.org >__ jeffro256: jberman is the helio selene winner’s code public yet?     

> __< k​ayabanerve:matrix.org >__ tritonn: rafael_xmr: boog900: lederstr umpf:  are the participants mentioned in the codebase who have not made their repositories public. While that would be preferable, I can also publish those submissions as passed on to me when I'm home as they are FOSS licensed.     

> __< k​ayabanerve:matrix.org >__ https://github.com/rafael-xmr/fcmp-plus-plus-optimization-competition-private     

> __< k​ayabanerve:matrix.org >__ https://github.com/Boog900/fcmp-plus-plus-optimization-competition/tree/entry1     

> __< k​ayabanerve:matrix.org >__ Thanks to the two of y'all for being prompt :)     

> __< t​ritonn:matrix.org >__ published     

> __< k​ayabanerve:matrix.org >__ tritonn: Sorry, what's your username on GitHub?     

> __< t​ritonn:matrix.org >__ Tritonn204     

> __< k​ayabanerve:matrix.org >__ Thank you!     

> __< k​ayabanerve:matrix.org >__ https://github.com/Tritonn204/fcmp-plus-plus-optimization-competition     

> __< k​ayabanerve:matrix.org >__ PR with lederstrumpf: 's submission: https://github.com/kayabaNerve/fcmp-plus-plus/pull/32     

> __< a​ntilt:we2.ee >__ I like the idea. May strengthen the argument for reviewing the de-doubling code, too.    

# Action History
- Created by: Rucknium | 2025-07-15T21:57:30+00:00
- Closed at: 2025-07-25T20:47:38+00:00
