---
title: Monero Research Lab Meeting - Wed 14 May 2025, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1204
author: Rucknium
assignees: []
labels: []
created_at: '2025-05-13T22:57:34+00:00'
updated_at: '2025-05-22T21:14:23+00:00'
type: issue
status: closed
closed_at: '2025-05-22T21:14:23+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/meeting.html?p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3. [_Maldo Map_ spy nodes research by jhendrix](http://maldomapyy5d5wn7l36mkragw3nk2fgab6tycbjlpsruch7kdninhhid.onion/) (Tor hidden service link)

4. FCMP++ & divisors.

5. FCMP stressnet preparation.

6. [FCMP++ transaction weight formula](https://github.com/seraphis-migration/monero/pull/26). And PoW for high-input txs.

7. Unit test for implementation of [subnet deduplication in peer selection algorithm](https://github.com/Rucknium/misc-research/blob/main/Monero-Peer-Subnet-Deduplication/pdf/monero-peer-subnet-deduplication.pdf).

8. Web-of-Trust for node peer selection.

9. Any other business

10. Confirm next meeting agenda

Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#1200 

# Discussion History
## Rucknium | 2025-05-15T18:26:00+00:00
Logs

> __< r​ucknium:monero.social >__ Meeting time! https://github.com/monero-project/meta/issues/1204     

> __< r​ucknium:monero.social >__ 1) Greetings     

> __< 0​xfffc:monero.social >__ Hi everyone     

> __< v​tnerd:monero.social >__ Hi     

> __< rbrunner >__ Hello     

> __< j​effro256:monero.social >__ Howdy     

> __< a​rticmine:monero.social >__ Hi     

> __< b​oog900:monero.social >__ hi     

> __< j​hendrix:imagisphe.re >__ Hello     

> __< s​yntheticbird:monero.social >__ Hello     

> __< j​berman:monero.social >__ *waves*     

> __< b​randon:cypherstack.com >__ hi     

> __< c​haser:monero.social >__ hello     

> __< r​ucknium:monero.social >__ 2) Updates. What is everyone working on?     

> __< rbrunner >__ My improved peer selection code reached beta state. Rucknium is able to tell more.     

> __< v​tnerd:monero.social >__ Me: finished lws-frontend tx construction and is in testing     

> __< s​yntheticbird:monero.social >__ Tor support in cuprate. I hate epee with a passion.     

> __< 0​xfffc:monero.social >__ Just warming up. Last week I was absent from meeting. Fixing minor issues here and there. But most of my time spent on: new tx telay protocol https://github.com/0xFFFC0000/monero/pull/60     

> __< j​berman:monero.social >__ me: continuing FCMP++ PR wrangling and debugging     

> __< j​effro256:monero.social >__ Me: more FCMP&Carrot integration work/review     

> __< r​ucknium:monero.social >__ me: Performing statistical tests on rbrunner's draft implementation of subnet deduplication for outbound peer selection to reduce spy node risk. (Can we link the branch publicly, rbrunner?). And made good progress on a custom loss function for neural net analysis to evaluate the risk of multiple decoy selection algorithms being used at the same time in the wild.     

> __< rbrunner >__ No problem to link. I will make an official PR soon if your test results are favorable     

> __< d​iego:cypherstack.com >__ hi     

> __< r​ucknium:monero.social >__ Good. Here is the subnet deduplication code: https://github.com/monero-project/monero/compare/master...rbrunner7:monero:peers     

> __< r​ucknium:monero.social >__ 3) Maldo Map spy nodes research by jhendrix  (Tor hidden service link:  http://maldomapyy5d5wn7l36mkragw3nk2fgab6tycbjlpsruch7kdninhhid.onion/ )     

> __< r​ucknium:monero.social >__ jhendrix: Do you want to explain a little what you did and what you found?     

> __< j​hendrix:imagisphe.re >__ Sure. The plan was to run remote/reachable nodes for all privacy coins, but I ended up focusing exclusively on Monero because it was the only network I found to be active. I discovered spy nodes by accident, which led me to the original GitHub issue.     

> __< r​ucknium:monero.social >__ If I am understanding your findings right, your main criteria for labeling a node as a spy node is whether they advertise multiple ports from the same IP address as having Monero nodes. Is that correct?     

> __< r​ucknium:monero.social >__ You found a new set of spy nodes that has recently turned on, right?     

> __< r​ucknium:monero.social >__ In two "PEG TECH" ASNs?     

> __< j​hendrix:imagisphe.re >__ That's right.     

> __< j​hendrix:imagisphe.re >__ When I confirmed that the spy nodes actually exist, I ran the node as any normal user would. I concluded that normal users would have, on average, two spies in their peer list, all from the known ISP Lionlink.     

> __< b​randon:cypherstack.com >__ isthmus and neptune mapped spy nodes a few years ago, which I believe they defined by whether they relayed or not. are you aware of previous work on spy nodes?     

> __< r​ucknium:monero.social >__ You may already know this, but an IP addess that has multiple advertised ports does not have a higher probability of being selected as an outbound peers. So, if the adversary(ies) is think they can gain an advantage  in selection probability by using multiple ports, they would be mistaken.     

> __< j​hendrix:imagisphe.re >__ Yes, the last time I checked, they became unreachable again.     

> __< b​oog900:monero.social >__ I have been scanning the network for the past few days and haven't been able to make a connection to these nodes. I can confirm that these nodes are in peer lists.     

> __< b​oog900:monero.social >__ I am pretty sure there are nodes in the network purposefully injecting these address into peer list messages     

> __< r​ucknium:monero.social >__ I pulled the json data from the Maldo Map and filtered on "PEG TECH". Then I tabulated them by `/24` subnet:     

> __< b​oog900:monero.social >__ as some nodes send quite a few PEG TECH addresses.     

> __< r​ucknium:monero.social >__ ```txt     

> __< r​ucknium:monero.social >__ 154.199.217.0 156.229.183.0   198.2.210.0   198.2.248.0    38.6.155.0    38.6.156.0    38.6.157.0      

> __< r​ucknium:monero.social >__           253           243             5             5           253           253           253      

> __< r​ucknium:monero.social >__ ```     

> __< r​ucknium:monero.social >__ So it looks like subnet deduplication would also be an effective countermeasure against these suspected spy nodes, too.     

> __< rbrunner >__ Good to hear     

> __< b​oog900:monero.social >__ my normal node also only has these peers in its gray list, none in its white list which tells me it never made a successful connection to these nodes.     

> __< r​ucknium:monero.social >__ Those last three are all in the same `/16` subnet, too.     

> __< rbrunner >__ And yes, there is also defense against peers with many ports per single IP number, i.e. not give them undue weight / chance to win the selection     

> __< r​ucknium:monero.social >__ This multiple-port defense has existed for years. And rbunner's draft code for subnet deduplication keeps it, but the implementation is a little different AFAIK.     

> __< j​hendrix:imagisphe.re >__ No, like everyone else, I suspected they existed, but the topic of spy nodes is new to me and I am only aware of #1124 published 5 months ago. I started working on maldomap a little more than a month ago and am still learning about other, more advanced methods I could use to spot them.     

> __< g​ingeropolous:monero.social >__ (but its still defense via the scarcity of ipv4, right?)     

> __< r​ucknium:monero.social >__ gingeropolous: Yes. Basically the idea for subnet deduplication is to require the adversary to spend more money on spy node IP addresses. It isn't a fantastic long-term solution, but its feasible today and easy to implement and analyze.     

> __< rbrunner >__ Essentially, yes, as we assume the IP numbers of spy nodes are not all over the place, but concentrated in /24 subnets     

> __< r​ucknium:monero.social >__ Well, we _know_ they are concentrated in /24 subnets today, not just assume.     

> __< b​randon:cypherstack.com >__ I'll tell isthmus to reach out to you     

> __< rbrunner >__ Right :) Thanks to your work     

> __< r​ucknium:monero.social >__ Probably because it is cheaper to rent a whole /24 subnet than to rent individual IPs scattered between many /24 subnets     

> __< r​ucknium:monero.social >__ > Spy nodes use that data to see if a node is fully synced or not, because only fully synced nodes can send transactions. They are managing their own resources effectively by not making lots of connections to nodes which are not fully synced. They are interested in spying only and not providing a public service by hosting a copy of the blockchain.     

> __< r​ucknium:monero.social >__ I think this is a new finding, unless boog900  found it earlier.     

> __< r​ucknium:monero.social >__ Probably they don't want to "waste" the bandwidth by giving newborn nodes old blocks.     

> __< o​frnxmr:monero.social >__ Doesnt account for simple-mode     

> __< o​frnxmr:monero.social >__ Rather, bootstrap + no-sync nodes     

> __< r​ucknium:monero.social >__ Boostrap mode?     

> __< r​ucknium:monero.social >__ Yes     

> __< 0​xfffc:monero.social >__ I am thinking how we can use this information to detect spy nodes. I mean there is no easy way to detect this (?)     

> __< r​ucknium:monero.social >__ You could try to detect them probabilistically. Or maybe there is a distinct message that the spy nodes send when they disconnect from newborn nodes.     

> __< g​ingeropolous:monero.social >__ i mean ultimately its an open network. an adversary could run a full node and still be spying. just need to find a way to make the spying unfruitful.     

> __< r​ucknium:monero.social >__ By the way, my observations are consistent with jhendrix : On average, about 15% of outbound connections of a default-settings node are established to a node on boog900 's spy node ban list, at any given time.     

> __< r​ucknium:monero.social >__ rbrunner's draft subnet deduplication implementation is reducing this to about 5%     

> __< b​oog900:monero.social >__ I think this could be more todo with monerod crawling the network when synced, while syncing it does not disconnect from peers like it does when synced.     

> __< r​ucknium:monero.social >__ And a spy node's precision against honest nodes' transactions is roughly p^2, so a reduction from 15% to 5% is a big reduction in precision     

> __< b​oog900:monero.social >__ I haven't noticed these nodes disconnecting from me my tool tells these nodes I am not synced.     

> __< j​hendrix:imagisphe.re >__ I don't think it is useful in the long run. Different spy node operators might use different methods. The best solution I can think of, which has already been shared, is to allow peers based on their ASN, so that 12 peers would come from 12 different entities.     

> __< r​ucknium:monero.social >__ See https://github.com/monero-project/research-lab/issues/126#issuecomment-2460261864 for more info on precision when Dandelion++ is used (D++ is always being used in Monero).     

> __< rbrunner >__ Useful in the short and medium run is already something. Basing things on ASNs is probably considerably more complex than /24 subnet deduplication.     

> __< r​ucknium:monero.social >__ We have a pretty full agenda today. More points that you want to make, jhendrix  ? You can come back next week for more discussion and/or continue discussing after the end of the meeting.     

> __< j​berman:monero.social >__ Sorry, I think this is an important conversation, but want to be respectful also to CS folks in this meeting and we have an important matter to discuss for FCMP++. Proposing we come back to spy node discussion     

> __< o​frnxmr:monero.social >__ Always being used over clearner*. Can skip straight to fluff is using tx-proxy     

> __< o​frnxmr:monero.social >__ if* using     

> __< j​berman:monero.social >__ Hah, thank you ruck     

> __< r​ucknium:monero.social >__ jhendrix has an XMR donation address at the bottom of http://maldomapyy5d5wn7l36mkragw3nk2fgab6tycbjlpsruch7kdninhhid.onion/     

> __< r​ucknium:monero.social >__ 4) FCMP++ & divisors.     

> __< j​hendrix:imagisphe.re >__ Sure thing, let's move on. Thanks for the feedback on my work and the invitation. 🙂     

> __< k​ayabanerve:matrix.org >__ One moment, as I wrote my message for this please.     

> __< k​ayabanerve:matrix.org >__ While divisors has had a much more turbulent than expected development, my prior expectations were it'd all resolve properly. Unfortunately there, Cypher Stack yielded a document regarding divisors, with the summary they don't endorse deployment at this time.     

> __< r​ucknium:monero.social >__ Good thing it was caught     

> __< r​ucknium:monero.social >__ Thank you very much, surae  and Diego Salazar     

> __< r​ucknium:monero.social >__ That means larger tx sizes and/or longer verification times? Or do more math to find a way to use the divisors?     

> __< r​ucknium:monero.social >__ Can a link to the document be posted? Is it ready?     

> __< k​ayabanerve:matrix.org >__ As we have organization for, one organization against, yet also the positing by Eagen and inclusion of the technique since in the eVRF paper (Boneh, Haitner, Lindell, Segev, accepted to EUROCRYPT), we could ask an alternative organization to work on the problem.     

> __< r​ucknium:monero.social >__ What was the basis for the non-endorsement?     

> __< b​randon:cypherstack.com >__ I can comment on that     

> __< k​ayabanerve:matrix.org >__ We must ask two questions though, on sunk cost and on timeline. Divisors must either work, with proofs before we sign off on the hard fork, or we need enough time to transition to an alternative solution.     

> __< b​randon:cypherstack.com >__ The non-endorsement was, essentially, due to our team not coming to a consensus. Some folks on our team are convinced that the divisors stuff will work out just fine. Some are convinced that there are mistakes which are correctable. Some are convinced that there is a deep problem that we haven't identified yet. And, we were not convinced of past proofs from Veridise, and unable to<clipped messag     

> __< b​randon:cypherstack.com >__  write our own. Without proofs to fall back on, and without a consensus on the team, we did not endorse it.     

> __< b​randon:cypherstack.com >__ Having said that, work on divisors at CS is continuing, at least for now. Finality on our decision was due to our impression of timeline requirements at Monero.     

> __< d​iego:cypherstack.com >__ also clarification that "unable to write our own" was due to lack of time, not lack of skill     

> __< c​haser:monero.social >__ also not lack of error in the theoretical construction?     

> __< s​yntheticbird:monero.social >__ no one is doubting about CS skills     

> __< rbrunner >__ Not being convinced by a proof sounds a bit strange     

> __< k​ayabanerve:matrix.org >__ To that end, sgp is organizing a meeting with another organization, and I'll be attending the meeting for the necessary technical support. While I consider this proper to ensure we exhaust our options, my current opinion is it's more likely to be sane to transition away from divisors.     

> __< d​iego:cypherstack.com >__ the complete formalization of divisors would be needed rather than the rag tag collection of ideas and documents that it currently is before CS would be comfortable recommending that billion dollar coin that is Monero transition to it     

> __< d​iego:cypherstack.com >__ there are no proofs     

> __< r​ucknium:monero.social >__ IMHO, not being convinced by a proof is not completely unusual.     

> __< b​randon:cypherstack.com >__ There may be correctable errors; see my comments above. We are working on that.     

> __< k​ayabanerve:matrix.org >__ For the PDF, Rucknium, I defer to CS. I am not trying to ignore your question, I just am not the best person to ask.     

> __< c​haser:monero.social >__ Diego Salazar: Surae wrote "we were not convinced of past proofs from Veridise,"     

> __< k​ayabanerve:matrix.org >__ Saying "there are no proofs" is a bit of an oversimplification of not agreeing with the validity of Veridise's 'proofs' (proofs in quotes as their validity is contested) IMO.     

> __< rbrunner >__ Are there, well, constructs, in sight already that maybe could replace divisors?     

> __< k​ayabanerve:matrix.org >__ Yet I'm aware the validity of Veridise's work has been questioned by CS to such a degree CS does not consider them worth continuing with, hence the discussion of CS's own proofs.     

> __< b​randon:cypherstack.com >__ For example, it is easy to sketch a proof of the Riemann hypothesis. But no sketch proof of the RH has been formalized into a convincing proof.      

> __< b​randon:cypherstack.com >__ So, the work presented so far in terms of proofs has been insufficient to get a passing grade, even if the overall sketch of the approach seems valid. Proof validation can be made formal with the lean programming language... encode the proof, see if the code type-checks... but this requires the fundamental material to be rather simple, and requires a degree of formality not yet se<clipped messag     

> __< b​randon:cypherstack.com >__ en in any of the proofs presented, so although it's technically possible, it's not a practical thing at the moment.     

> __< k​ayabanerve:matrix.org >__ The alternative is to replace divisors with a much more traditional scalar multiplication gadget which will cause a multiple times slower proof.     

> __< g​ingeropolous:monero.social >__ so how does this come about then? this degree of formality?     

> __< d​iego:cypherstack.com >__ many months of work     

> __< r​ucknium:monero.social >__ Lots of caffeine and mathematicians.     

> __< j​berman:monero.social >__ I think it's worth prioritizing a more conservative route at the moment (i.e. an alternative solution that does not rely on divisors), and also secondarily continuing R&D formalizing divisors (as it is would yield a significant speed-up over the conservative route and is therefore still worth pursuing)     

> __< d​iego:cypherstack.com >__ I'll speak bluntly, if you don't mind.     

> __< r​ucknium:monero.social >__ Diego Salazar: Please do     

> __< rbrunner >__ Does this also mean that our coding / optimizing contest may be for naught?     

> __< d​iego:cypherstack.com >__ Work of this caliber takes months or even up to a year or more. Veridise did the work they did in the short time span the execs of the company got the math people to do it in. It was too rushed and nowhere near comprehensive enough.     

> __< d​iego:cypherstack.com >__ On the surface, it seems sounds, and the proof sketches seem valid.     

> __< d​iego:cypherstack.com >__ When CS dug deeper to try to get a semblance of formalization, we kept running into bear trap after bear trap. None of them was enough to convince us that divisors was broken, but it happened with frequency (every couple of days) and showed no signs of slowing down.     

> __< k​ayabanerve:matrix.org >__ After the work on the scalar multiplication gadget, we'd have to update the circuit, and the API shouldn't be notably different. The main concern is the performance impact, then there's the requirement for a follow up audit on the now updated circuit, and the unfortunate impact to the contest.     

> __< d​iego:cypherstack.com >__ Internally we came to a point of confidence, only to a point of non-confidence a few days later as we hit another bear trap, back and forth and back and forth for weeks.     

> __< d​iego:cypherstack.com >__ This ultimately came to the internal consensus that if this was happening to this degree and to this frequency, that divisors isn't ready to go into Monero.     

> __< r​ucknium:monero.social >__ Did you solve some of the bear traps?     

> __< d​iego:cypherstack.com >__ yes     

> __< d​iego:cypherstack.com >__ Not trying to shit on the math people in Veridise. We also felt the same rush and pressure their math guys probably did.     

> __< d​iego:cypherstack.com >__ fwiw, in regards to Kayaba's comment on CS thinking Veridise not worth continuing with, our stance has softened as it became clearer to us how much work this was and how rushed things were on all ends. Towards the beginning the frequency of bear traps made us quite wary of their skill, indeed.     

> __< d​iego:cypherstack.com >__ But put in a similar position of trying to get this big math out quickly, it became clear the fault may have been timeilnes.     

> __< r​ucknium:monero.social >__ To Cypherstack: Do you want to and/or have available time to work more on this? AFAIK, the FCMP++ research CCS still has funds     

> __< c​haser:monero.social >__ kayabanerve: roughly which parts of FCMP++ would suffer from this performance impact, and how much?     

> __< d​iego:cypherstack.com >__ yes. We've never stopped. We're exploring both what it would take to shore up divisors, as well as if there's an alternative that accomplishes the same or similar things that would be easier/faster.     

> __< k​ayabanerve:matrix.org >__ Apologies for my own inaccuracy and thank you for clarifying.     

> __< j​berman:monero.social >__ It doesn't sound like divisors is going to be thrown out, it sounds like it needs more work that will take time. So it sounds like the contest may end up a cost that was just too early, but still likely not for nothing even assuming we end up with a valid submission     

> __< r​ucknium:monero.social >__ It seems like FCMP timeline will be pushed back by months regardless of what happens and is decided from this point in time. Is that correct?     

> __< j​berman:monero.social >__ We took the calculated risk of holding it early to accelerate the timeline of FCMP++     

> __< b​randon:cypherstack.com >__ contest? submission?     

> __< k​ayabanerve:matrix.org >__ chaser: The FCMP verification. Within an order of magnitude.     

> __< c​haser:monero.social >__ the contest is also for Helioselene, is that part also a sunken cost?     

> __< k​ayabanerve:matrix.org >__ Rucknium: No. If we expecting divisors, and divisors don't positively resolve, yes.     

> __< j​berman:monero.social >__ sorry context here: we opened a contest to speed up the divisors implementation (in addition to our Helios Selene lib), winner of the divisors contest gets 250 XMR     

> __< k​ayabanerve:matrix.org >__ chaser: No.     

> __< d​iego:cypherstack.com >__ fwiw, I don't think this was a misstep.     

> __< b​randon:cypherstack.com >__ ahhhh tyvm     

> __< k​ayabanerve:matrix.org >__ *if we continue expecting     

> __< k​ayabanerve:matrix.org >__ We still have adequate time to transition away.     

> __< r​ucknium:monero.social >__ So the switch to the "old" way would be quick, or at least not impact timeline     

> __< 0​xfffc:monero.social >__ Not possible to delay the contest?     

> __< r​ucknium:monero.social >__ The verification times without Divisors are scary     

> __< s​yntheticbird:monero.social >__ I think we can say unsuitable for production     

> __< r​ucknium:monero.social >__ Maybe manageable, but scary     

> __< j​berman:monero.social >__ We've already opened the contest for submissions, anyone who has started working on it would have terms changed under them. I don't think this is would be a fair route to take     

> __< s​yntheticbird:monero.social >__ Many are already scared by the verification time, if divisors are out then I can't see how this would be possible to push that into the mainnet     

> __< g​ingeropolous:monero.social >__ can we do like Diet FCMP++, only do half the chain? HCMP?     

> __< rbrunner >__ Well, with even higher verification times we more or less send out invitations to DoS us, no?     

> __< d​iego:cypherstack.com >__ I have four mathematicians / cryptographers, and they're pretty much all on this problem, though it will be some time to completion. Not to mention any talent here.     

> __< k​ayabanerve:matrix.org >__ SyntheticBird: I disagree they'd be unsuitable and would note we need the implementation to evaluate.     

> __< d​iego:cypherstack.com >__ One option is FCMP++ without divisors, and then another hard fork when divisors (or replacement) is finalized     

> __< d​iego:cypherstack.com >__ big privacy win followed by big efficiency win     

> __< j​berman:monero.social >__ With higher verification times, we would probably definitely want PoW-enabled relay at the hf, which may take 2-3 weeks to implement, maybe less. Would be a good defense to have set up for nodes I think regardless, even with divisors     

> __< s​yntheticbird:monero.social >__ ArticMine is not going to be happy about it     

> __< b​oog900:monero.social >__ not even sure PoW would help if valid txs are enough to DoS     

> __< r​ucknium:monero.social >__ The system's parameters must stay within the safe zone.     

> __< j​effro256:monero.social >__ I know this is sort of tongue in cheek, but technically yes. Although, it really doesn't help much in terms of performance . There's a large "base" cost to FCMPs , and reducing the size of the anon set by 2x 5x or even 10x won't really improve verification speeds.     

> __< j​effro256:monero.social >__ I'm scared by the verification time for *high input* txs with no protection against DoS , but not inherently high verification times within reasonable bounds     

> __< k​ayabanerve:matrix.org >__ The suggestion valid TXs would be enough to DoS sounds like a notable over statement to me but I'd have to defer to an actual implementation once provided.     

> __< a​rticmine:monero.social >__ What is the impact for 8 inputs or less?     

> __< k​ayabanerve:matrix.org >__ Also, bandwidth cost would go down. ArcticMine advocated months ago for raising verification times by a nontrivial factor to achieve that.     

> __< s​yntheticbird:monero.social >__ Regardless the stressnet planned to be launched in 7 days must continue...     

> __< b​oog900:monero.social >__ I mean didn't we have 179ms per 8-input proof, order of magnitude increase would be 1 second.     

> __< d​iego:cypherstack.com >__ My opinion is that such an implementation should be done, and we will continue to work in the background.     

> __< r​ucknium:monero.social >__ bandwidth = tx sizes, for those who don't know.     

> __< d​iego:cypherstack.com >__ Apologies to all for the frustrating news.     

> __< c​haser:monero.social >__ yet another opportunity to go 8/8 or 8/4?     

> __< s​yntheticbird:monero.social >__ rather thanks for brining them     

> __< s​yntheticbird:monero.social >__ no need to apologies     

> __< j​effro256:monero.social >__ Kayaba , do you have a ballpark estimate for membership proof size reduction w/o divisors ?     

> __< j​berman:monero.social >__ fwiw, helioselene is still a significant component of verification time (over 50%), so optimizations there should have a material impact on our current verification times     

> __< g​ingeropolous:monero.social >__ is this the location where we can find all the docs etc? https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/449  . I feel like its really difficult to stay on top of this if your not directly involved.     

> __< k​ayabanerve:matrix.org >__ Ideally ~30-50% jeffro256:     

> __< r​ucknium:monero.social >__ gingeropolous: All docs should be here, unless I am mistaken: https://moneroresearch.info/index.php?action=list_LISTSOMERESOURCES_CORE&method=subcategoryProcess&id=1&catId=1     

> __< j​effro256:monero.social >__ Now a 1-in would more expensive to verify than a 8 in our previous discussion , so PoW would basically be a necessity for all txs     

> __< r​ucknium:monero.social >__ And if I am mistaken, the missing doc(s) should be added     

> __< r​ucknium:monero.social >__ Now time for concrete proposals     

> __< r​ucknium:monero.social >__ Cypher Stack continuing to work on Divisors, with possible more funds from the research CCS? Start implementing and integrating the non-Divisor FCMP code? Can do both, of course     

> __< r​ucknium:monero.social >__ Another mathematics firm to try Divisors?     

> __< c​haser:monero.social >__ so, IIUC, verification times for low-in tx's without PoW are also scary     

> __< k​ayabanerve:matrix.org >__ jeffro256: That isn't necessarily the performance impact.     

> __< r​ucknium:monero.social >__ kayabanerve: You have draft code with the non-Divisors FCMP++, right? Or was that FCMP, without the ++?     

> __< rbrunner >__ Half seriously: Double our ring size to 32 as an intermediate measure? And then give everybody time to work out something really solid.     

> __< k​ayabanerve:matrix.org >__ No     

> __< rbrunner >__ I mean, see what transaction sizes and verification times we seem to be ready to accept, so ...     

> __< k​ayabanerve:matrix.org >__ (to Ruck)     

> __< k​ayabanerve:matrix.org >__ Unless I technically did something not representative years ago.     

> __< c​haser:monero.social >__ if there are enough funds left, or feasible to raise, following at least two paths simultaneously out of those three could be a strategy     

> __< j​berman:monero.social >__ I advocate prioritize the more conservative route at the moment, get figures, discuss, optimize further where possible. Allocate resources primarily toward this     

> __< r​ucknium:monero.social >__ Which resources would those be? Your and jeffro256 's time?     

> __< g​ingeropolous:monero.social >__ the way i see it, randomx got 3 independent audits, and i think they were done in serial. this seems even moreso important, and warrants at least the same treatment     

> __< rbrunner >__ Especially now with those "shadows" over it, yeah     

> __< rbrunner >__ Maybe the universe does not want use to progress to something decidedly better. Triptych, Seraphis, now FCMP++ :)     

> __< g​ingeropolous:monero.social >__ so id say cypher stack continues, another math firm, and integrate the non-divisor code, and bump the current ringsize. All the things. The last element could test the waters for the ddos susceptibility of the network.     

> __< a​rticmine:monero.social >__ Can we not mitigate this verification time issue with parallel processing of multiple transactions?     

> __< j​effro256:monero.social >__ No     

> __< 0​xfffc:monero.social >__ Depends on the nature of the algorithm.     

> __< 0​xfffc:monero.social >__ Question, why are you saying "No", the algorithm is not parallelized?     

> __< 0​xfffc:monero.social >__ s/parallelized/parallelizable/     

> __< j​effro256:monero.social >__ If we are talking specifically about the main issue, DoS, multi threading it doesn't make it better, it just opens up the attack to multiple threads on your machine     

> __< j​berman:monero.social >__ First someone to implement (I don't know if I would be ideal candidate here, perhaps kayabanerve if possible and if not, then we figure it out from there), and then independent audit/review (I would propose CS handle this and prioritize they work on this)     

> __< r​ucknium:monero.social >__ Some nodes are running on machines with 2-4 threads.     

> __< k​ayabanerve:matrix.org >__ I'll note we don't have firm numbers on the alternative FCMP nor from the contest.     

> __< g​ingeropolous:monero.social >__ yeah im curious what the performance is like on zen 5     

> __< r​ucknium:monero.social >__ kayabanerve: I recall some high verification time numbers from your 2023(?) MoneroKon talk. I thought those might have been non-Divisor FCMP times     

> __< k​ayabanerve:matrix.org >__ I am otherwise occupied now and will be back to clarify further later.     

> __< a​rticmine:monero.social >__ Yes. The issue here is the cost of the attack vs the cost of the defense? Still the attacker has to construct the fake proofs     

> __< k​ayabanerve:matrix.org >__ Rucknium: No, those would've been with divisors and also an entire alternative proving system.     

> __< r​ucknium:monero.social >__ Diego Salazar: Any estimate on when the public can see the doc that doubts Divisors?     

> __< d​iego:cypherstack.com >__ I don't have an issue sharing it.     

> __< d​iego:cypherstack.com >__ There are two documents actually.     

> __< r​ucknium:monero.social >__ Please share soon. Thanks.     

> __< j​effro256:monero.social >__ It's not expensive if the proofs are invalid     

> __< r​ucknium:monero.social >__ Back to concrete proposals: Ready to decide some courses of action today, or think about it and decide next week?     

> __< j​berman:monero.social >__ I think it would be good to get some agreement on pursuing the more conservative route for now, which tbh seems like there is agreement on that. And concrete action items can be discussed further next week with more time to prepare     

> __< j​berman:monero.social >__ Oh there is another thing to mention     

> __< j​berman:monero.social >__ I think evidently we want to keep the alpha stressnet on hold     

> __< o​frnxmr:monero.social >__ Why?     

> __< r​ucknium:monero.social >__ I agree to put the alpha stressnet on hold for now     

> __< o​frnxmr:monero.social >__ just rename it to "pre-alpha-stressnet"     

> __< a​rticmine:monero.social >__ ...  but it is more expensive to detect the invalid proof     

> __< r​ucknium:monero.social >__ You want the alpha stressnet/testnet to use the actual implementation (or close to it) that will be used on mainnet.     

> __< o​frnxmr:monero.social >__ Thats what testnet is for     

> __< j​berman:monero.social >__ Seems like it would be unnecessary to bring community members in to test current code. I don't see a major benefit to it     

> __< r​ucknium:monero.social >__ The conservative route is "think about and decide who will try to write a non-divisors FCMP implementation", correct?     

> __< j​berman:monero.social >__ Correct     

> __< j​berman:monero.social >__ Well the conservative route is non-divisors FCMP     

> __< o​frnxmr:monero.social >__ and if CS finishes with "divisors are OK"     

> __< o​frnxmr:monero.social >__ and if CS finishes with "divisors are OK"?     

> __< j​berman:monero.social >__ they are saying the timeline for that is months     

> __< c​haser:monero.social >__ the conservative solution would surely need focus to prepare for the chance that divisors don't turn out to be safe to deploy     

> __< o​frnxmr:monero.social >__ the conservative approach is to abandon divisors until further notice *     

> __< j​effro256:monero.social >__ And what is the timeline for writing and auditing a new construction without divisors ?     

> __< r​ucknium:monero.social >__ The mathematics of the non-divisors FCMP need to be proved & reviewed, or no?     

> __< o​frnxmr:monero.social >__ Divisors impl (was) supposed to be stressnet ready in a week (may 21)?     

> __< j​berman:monero.social >__ writing: hopefully weeks. auditing: probably also months     

> __< j​effro256:monero.social >__ Yes divisors code has been done for a while     

> __< o​frnxmr:monero.social >__ Seems to me that it would still make sense to get stressnet ready (barely a fee days out), and then move on to conservative approach     

> __< j​berman:monero.social >__ why?     

> __< o​frnxmr:monero.social >__ Because thats plan A     

> __< j​berman:monero.social >__ That's not really an answer?     

> __< j​berman:monero.social >__ We can alternatively allocate focus on continuing to have more integration-related tasks completed, rather than allocating focus on a premature stressnet that uses code we don't presently have academic confidence in     

> __< r​ucknium:monero.social >__ Alpha stressnet will consume some labor hours AFAIK. For example, I planned to do some spamming on it. But instead I could work on something else. I don't know exactly what needs to be done by jberman/jeffro256/ tobtoht , but it is probably non-negligible     

> __< j​berman:monero.social >__ *that uses code that has an academic NACK, tbc     

> __< o​frnxmr:monero.social >__ The conservative approach also takes months     

> __< o​frnxmr:monero.social >__ And has no academic ack     

> __< j​berman:monero.social >__ jeffro256 do you want to do the stressnet still? I don't personally see a strong argument in favor of allocating some resources toward that versus completing integration tasks given where divisors stands at the moment     

> __< o​frnxmr:monero.social >__ Towards focusing on stress testing? I agree. I'm saying the impl should be finished and bins released as oer schedule     

> __< j​effro256:monero.social >__ Hmmmmmm yeah I think we should put it off. While there are shared components in the code that could be tested now, the biggest performance variable (FCMPs) would be all out of sack     

> __< j​effro256:monero.social >__ Assuming we end up not using divisors     

> __< j​effro256:monero.social >__ Out of wack     

> __< o​frnxmr:monero.social >__ So we wait months, do a second impl     

> __< o​frnxmr:monero.social >__ And potential not use the 2nd one, considering it might also get NACK'd     

> __< j​berman:monero.social >__ Ideally not months     

> __< j​effro256:monero.social >__ Most of the integration doesn't change     

> __< o​frnxmr:monero.social >__ And dont finish the first one, since it only has some ack's and a nack based on time     

> __< j​effro256:monero.social >__ Just the performance of FCMPs     

> __< j​berman:monero.social >__ You're complaining just to complain right now, not presenting an argument in favor of stressnet next week     

> __< j​berman:monero.social >__ ofrnxmr     

> __< o​frnxmr:monero.social >__ Yes     

> __< o​frnxmr:monero.social >__ Seems like wasted resources     

> __< c​haser:monero.social >__ do we know what resources CS would need to keep analyzing divisors?     

> __< r​ucknium:monero.social >__ Diego Salazar: ^     

> __< r​ucknium:monero.social >__ I think the plan is: 1) Immediately investigate a non-Divisor FCMP++ implementation, 2) No alpha stressnet starting next week (further scheduling TBD), 3) Continuing discussions of "trying harder" to rigorously prove Divisors, with more Cypher Stack work and/or another firm     

> __< r​ucknium:monero.social >__ No one got my joke about mathematicians and caffeine. Not even an emoji reaction 😭     

> __< o​frnxmr:monero.social >__ 1) weeks to impl, potentially months beyond that for academics     

> __< o​frnxmr:monero.social >__ 2) months or not at all for divisors. Wait for 1 otherwise (months)     

> __< o​frnxmr:monero.social >__ 3)     

> __< c​haser:monero.social >__ sounds good. I saw the willingness from CS's side, and that, given more time, a higher certainty could be reached without going the full formalization route that could a take a year     

> __< c​haser:monero.social >__ it's not a joke because it's real :)     

> __< o​frnxmr:monero.social >__ nacking a stressnet w/o academic ack, means we should also nack a stressnet for conservative route w/o academic ack. So got 6 in one hand and half a dozen in the other     

> __< o​frnxmr:monero.social >__ Just one hand is ready, pending ack, now     

> __< j​effro256:monero.social >__ I liked it Ruck I just can't emote until someone else does 🥲     

> __< r​ucknium:monero.social >__ > A mathematician is a machine for turning coffee into theorems.     

> __< r​ucknium:monero.social >__ `-  Alfred Reny`     

> __< o​frnxmr:monero.social >__ that should have been fixed     

> __< r​ucknium:monero.social >__ Renyi*     

> __< r​ucknium:monero.social >__ For the IRC record, I see 5 👍 on my "I think the plan is..." message. jberman, chaser, ArticMine, tobtoht, and boog900     

> __< r​ucknium:monero.social >__ We can end the meeting here. Feel free to continue discussing. Thank you everyone.     

> __< j​berman:monero.social >__ I disagree with this. Stressnet w/academic NACK < stressnet with conservative approach that has stronger academic theory w/o academic ACK. The former I think is more likely to be wasted effort     

> __< o​frnxmr:monero.social >__ Thats assuming that cs work ends up nacking it     

> __< a​ntilt:we2.ee >__ >and/or another firm      

> __< a​ntilt:we2.ee >__ who could that be ?     

> __< o​frnxmr:monero.social >__ But their nack was based on rushed time and mainnet     

> __< j​berman:monero.social >__ I don't think we're going to agree on this     

> __< o​frnxmr:monero.social >__ .     

> __< j​berman:monero.social >__ I don't think we're going to agree that stressnet next week is not the best use of resources     

> __< o​frnxmr:monero.social >__ Is the divisor impl ready, can be built on my own?     

> __< j​effro256:monero.social >__ Yeah I mean feel free to start your own stressnet     

> __< d​iego:cypherstack.com >__ None at present. Power Up Privacy is covering this work outside the scope of our completed MRL work.     

> __< j​berman:monero.social >__ ^     

> __< o​frnxmr:monero.social >__ What repo do i build off of? all of the tools are "ready"? (carrot, wallets, etc?)     

> __< d​iego:cypherstack.com >__ If anyone wants to join and be a part of the effort let me know. I can set up a room with my researchers. Though experience in this area or similar would be best so we dont have to take so much time getting people up to speed.     

> __< j​effro256:monero.social >__ Its scattered over a few branches in the seraphis-migration repo     

> __< j​effro256:monero.social >__ DM me for details     

> __< j​effro256:monero.social >__ If you come to find concrete findings and its generally relevant I will happily (attempt to) fix     

> __< j​effro256:monero.social >__ But I probably won't participate outright in a stressnet with divisor FCMPs next week given the discussion today     

> __< c​haser:monero.social >__ that's absolutely stellar. this means no funds need to be expended from the FCMP Research CCS to keep the divisors pathway alive (at least for now). thanks Power Up Privacy.     

> __< r​ucknium:monero.social >__ It doesn't involve calculus at all, does it? And the tough parts aren't linear algebra, right?     

> __< r​ucknium:monero.social >__ Maybe one of the firms listed here: https://cryptpad.fr/sheet/#/2/sheet/view/yPVIUywwA9-deE9VF6GYm9bXbPdCerdST3UDEEfBxcM/embed/     

> __< g​ingeropolous:monero.social >__ that sheet is what ive been looking for! Thank you     

> __< d​iego:cypherstack.com >__ surae: ^ :D     

> __< d​iego:cypherstack.com >__ also, the interns that have been onboarded (Freeman Slaughter, Luke     

> __< d​iego:cypherstack.com >__ Luke Szramowski, and Rigo are all hard workers and doing great work for privacy behind the scenes     

> __< a​ck-j:matrix.org >__ Hurricane electric is a great resource to search and investigate ASNs      

> __< a​ck-j:matrix.org >__ https://bgp.he.net/search?search%5Bsearch%5D=PEG+TECH&commit=Search     



# Action History
- Created by: Rucknium | 2025-05-13T22:57:34+00:00
- Closed at: 2025-05-22T21:14:23+00:00
