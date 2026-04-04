---
title: Monero Research Lab Meeting - Wed 05 February 2025, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1152
author: Rucknium
assignees: []
labels: []
created_at: '2025-02-04T21:31:46+00:00'
updated_at: '2025-02-14T16:21:59+00:00'
type: issue
status: closed
closed_at: '2025-02-14T16:21:59+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/meeting.html?p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3. Prize contest to optimize some FCMP cryptography code.

6. Research on [Autonomous System (AS) peer connection rules](https://github.com/monero-project/monero/pull/7935) to reduce spy node risk.

7. Reliability of [MRL technical note 0010](https://www.getmonero.org/resources/research-lab/pubs/MRL-0010.pdf).

8. Any other business

9. Confirm next meeting agenda

Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#1148 

# Discussion History
## Rucknium | 2025-02-06T17:50:17+00:00
Logs

> __< r​ucknium:monero.social >__ Meeting time! https://github.com/monero-project/meta/issues/1152     

> __< r​ucknium:monero.social >__ 1) Greetings     

> __< rbrunner >__ Hello     

> __< c​haser:monero.social >__ hello     

> __< j​berman:monero.social >__ *waves*     

> __< v​tnerd:monero.social >__ hi     

> __< s​yntheticbird:monero.social >__ hello     

> __< r​ucknium:monero.social >__ 2) Updates. What is everyone working on?     

> __< v​tnerd:monero.social >__ testing/fixing some timeout stuff in the epee tcp server     

> __< r​ucknium:monero.social >__ me: I achieved a 15x speedup in some short but time-consuming portion of OSPEAD R code by re-writing it in Rust. Also working on analyzing a subnet de-duplication algorithm for selecting peer nodes to reduce the effectiveness of spy nodes.     

> __< j​berman:monero.social >__ me: made significant progress on plugging FCMP++ into consensus and testing the full flow of tx construction -> node validates the tx. I have one core piece remaining to get it working locally (the balance check i.e. sum of inputs == sum of outputs), then touching up remains     

> __< r​ucknium:monero.social >__ 3) Prize contest to optimize some FCMP cryptography code.     

> __< j​berman:monero.social >__ We discussed the FCMP++ optimization contest in the NWLB group on Monday. I proposed an idea to re-scope the contest to a wider scope, and kayabanerve  provided solid reasoning to NACK that idea     

> __< j​berman:monero.social >__ I direct anyone following along to check that group for that proposal/discussion     

> __< j​effro256:monero.social >__ Howdy, sorry I'm late     

> __< j​effro256:monero.social >__ Me: Carrot integration. Today I'm working on FCMP++-ready input selection and plugging that into `wallet2     

> __< r​ucknium:monero.social >__ #no-wallet-left-behind:monero.social  is the room     

> __< j​berman:monero.social >__ The next step on my end (still) is a test suite. To implement tests correctly, I need to profile the respective functions used in prove/verify/tree building, to make sure the benchmark tests in the contest capture exactly what we want to optimize     

> __< s​yntheticbird:monero.social >__ sounds tiresome, what about a contest for the best test suite     

> __< j​berman:monero.social >__ Apologies I've put off on my deliverables for the contest. I've been focusing more time and effort on the FCMP++ integration work     

> __< v​tnerd:monero.social >__ you might want to publish what machine this will be verified on too     

> __< r​ucknium:monero.social >__ I've read a little about Rust's single instruction, multiple data (SIMD) capability. Will SIMD be prohibited, since it could rely on CPU instructions sets that are not universal?     

> __< j​berman:monero.social >__ I think it's a sound goal for the contest to have a generally applicable lib that doesn't have major speed-ups on one target machine versus another     

> __< s​yntheticbird:monero.social >__ so contest is really aiming at algorithmic optimization rather code optimization     

> __< s​yntheticbird:monero.social >__ rather than*     

> __< rbrunner >__ That's a very good way to put it IMHO     

> __< rbrunner >__ At least as the first approximation that sounds like a good explanation of the goal to me     

> __< j​berman:monero.social >__ seems like a fair way to put it     

> __< s​yntheticbird:monero.social >__ \* release dopamine \*     

> __< rbrunner >__ After better algorithms you could still go on and optimize the code implementing them, of course     

> __< s​yntheticbird:monero.social >__ rbrunner sounds good to me     

> __< s​yntheticbird:monero.social >__ portability is the requirement for code optimization     

> __< s​yntheticbird:monero.social >__ algorithmic is up to participant brains     

> __< s​yntheticbird:monero.social >__ ah no i think jberman said there is some constraints on computed tables     

> __< rbrunner >__ Yeah, that was one of the contentious points in the discussion. Allow C? Allow assembler? Allow unsafe Rust? For how much of a speedup? And so on     

> __< rbrunner >__ Contestants could come up with a surprising number of things that are a bit problematic without a good contest description     

> __< s​yntheticbird:monero.social >__ ofc. kinda excited to see what people are gonna submit     

> __< r​ucknium:monero.social >__ Ok. More discussion on this? We can have more discussion when the tests get written.     

> __< j​berman:monero.social >__ nothing from me     

> __< r​ucknium:monero.social >__ 4) Research on Autonomous System (AS) peer connection rules to reduce spy node risk. https://github.com/monero-project/monero/pull/7935     

> __< s​yntheticbird:monero.social >__ also available as PR on cuprate side btw: https://github.com/Cuprate/cuprate/pull/339     

> __< r​ucknium:monero.social >__ I am analyzing an alternative peer selection algorithm. Instead of randomly choosing from candidate list of nodes that may be populated by many spy nodes on a few saturated /24 subnets (254 possible IP addresses in each /24 subnet), first de-duplicate the candidate list at the /16 subnet level (which are strict supersets of the /24 subnets) and _then_ randomly choose a peer from t<clipped message     

> __< r​ucknium:monero.social >__ he de-duplicated list.     

> __< r​ucknium:monero.social >__ I did a network scan using boog900's tool and coded some simulations. My preliminary results say that the de-duplication algorithm brings the share of connections to spy nodes down to only 2 percent, compared to about 30 percent for the status quo method.     

> __< r​ucknium:monero.social >__ Sounds great, but two potential downsides/side effects: 1) A spy node adversary can change their strategy to leasing subnet-distinct IP addresses instead of leasing whole subnets and 2) honest nodes in "popular" subnets would get fewer inbound connections and honest nodes in "lonely" subnets would get more inbound connections.     

> __< r​ucknium:monero.social >__ (2) is a little hard to analyze because we need data on the number of nodes with closed inbound ports, which boog's tool would not be able to count. I'll cover that another time.     

> __< r​ucknium:monero.social >__ On (1), honest Monero nodes are not perfectly dispersed across subnets. They are a little concentrated in subnets of VPS providers. Therefore, it might be possible that an adversary could turn the tables by only leasing subnet-distinct IP addresses instead of leasing whole subnets in bulk. Whether it is better for an adversary to try to turn the tables depends on the price premium<clipped message     

> __< r​ucknium:monero.social >__  on leasing subnet-distinct IP addresses compared to bulk subnet leasing.     

> __< r​ucknium:monero.social >__ I wrote a simple economic model and found the following:     

> __< r​ucknium:monero.social >__ Let `h_s` be the total number of honest nodes that accept inbound connections, including nodes in the same /16 subnet.     

> __< r​ucknium:monero.social >__ Let `h_d` be the number of distinct /16 subnets with at least one honest node that accepts inbound connections.     

> __< r​ucknium:monero.social >__ Let `w_s` be the price per IP address when leasing whole /24 subnets at a time. (If the price to lease a subnet per month is 150 USD, then the price per IP address is 150/254 = 0.59 USD.)     

> __< r​ucknium:monero.social >__ Let `w_d` be the price to lease one distinct IP address that is not in the same /16 subnet as other distinct IP addresses.     

> __< r​ucknium:monero.social >__ According to my preliminary model, an adversary would try to "turn the tables" if `w_d / w_s < h_d / h_s`     

> __< r​ucknium:monero.social >__ This is "nice" because the condition does not depend on the budget's adversary (which would have to be guessed), nor even on the absolute prices. Just the relative price. `h_d` and `h_s` can be estimated with a quick network scan, although of course it could change over time.     

> __< r​ucknium:monero.social >__ What I see now is `h_d / h_s = 1.36`, based on current network data. That means that an adversary would try to turn the tables if the price premium on subnet-distinct IP addresses was 36% or less, compared to leasing subnets in bulk. IMHO, probably the price premium is higher than that, but I will do more investigation of that. Therefore, it is likely that a subnet de-duplicated a<clipped message     

> __< r​ucknium:monero.social >__ lgorithm to select peers would reduce the effectiveness of spy nodes. According to preliminary results, of course.     

> __< r​ucknium:monero.social >__ Thoughts on this research and the alternative peer selection algorithm?     

> __< s​yntheticbird:monero.social >__ thoughts? good job.     

> __< r​ucknium:monero.social >__ Ah, already saw a transcription error. The condition should be  about `h_s / h_d`, not `h_d / h_s`     

> __< rbrunner >__ Not sure I am on a good path of thought here, but wouldn't our better algorithm lead to very different incentives for the adversary?     

> __< rbrunner >__ Say, in extreme, they have two choices, have their spy nodes more or less useless, or spend more money?     

> __< r​ucknium:monero.social >__ rbrunner: Yes, exactly. I am analyzing at which point the incentives create conditions so that it is actually better to stay in the status quo peer selection algorithm.     

> __< rbrunner >__ To buy addresses that make their nodes effective again, because dispersed in the IP space     

> __< r​ucknium:monero.social >__ Since the adversary can react     

> __< rbrunner >__ Ah, I see!     

> __< s​yntheticbird:monero.social >__ on the verge of having monerod fetch the real time price of IP to change its peer selection algorithm dynamically     

> __< r​ucknium:monero.social >__ According to my mode, the adversary's total budget does not affect whether  one peer selection algorithm is better than the other     

> __< r​ucknium:monero.social >__ model*     

> __< j​effro256:monero.social >__ Here `h_s` and `h_d` are using the unit of /16 subnets, whereas `w_s` and `w_d` are using the unit of /24 subnets. Is this intended?     

> __< r​ucknium:monero.social >__ According to a recent network scan, h_s = 2572  and h_d = 1895. These are honest nodes with open ports, not all honest nodes. So ether are 2572 total honest nodes with open ports, dispersed across 1895 /16 subnets     

> __< r​ucknium:monero.social >__ Yes. In practice, the LinkingLion adversary is leasing /24 subnets.     

> __< rbrunner >__ Do I understand correctly that the final intended outcome of this investigation is an advice whether now we should switch the algorithm, or stay put?     

> __< s​yntheticbird:monero.social >__ rbrunner yes     

> __< rbrunner >__ Alright, looking forward to this, very interesting     

> __< r​ucknium:monero.social >__ An adversary can lease larger subnet chunks, but the bulk discount about /24 doesn't really get much better as you increase the subnet size. Some example: https://www.logicweb.com/bulk-ip-address-leasing/     

> __< rbrunner >__ If I think that this all only takes place in IP4 space whereas the whole world should use IP6 for a long time already ...     

> __< rbrunner >__ That would probably result in a different game, right? IP6     

> __< r​ucknium:monero.social >__ For laypeople: confusingly, a /23 subnet is larger than a /24 subnet. A /24 subnet has 254 usable ip addresses and a /16 one has about 256^2 IP addresses.     

> __< r​ucknium:monero.social >__ Yes, basically this anti-Sybil measure only works in the IPv4 protocol since IPv4 costs money since it's scarce (only about 4 billion total IPv4 addresses for the whole planet).     

> __< r​ucknium:monero.social >__ AFAIK, Monero nodes have IPv6 is disabled by default to try to reduce the Sybil risk from IPv6     

> __< rbrunner >__ Maybe a fresh look at the situation there that includies massive spying in the IP4 space would shift the arguments for that?     

> __< r​ucknium:monero.social >__ The little economic model includes a simple game theory model where the two players each have two possible strategies to deploy. I am proving the Nash equilibrium.     

> __< rbrunner >__ Slowly it must become a shame anyway that we are almost totally absent in IP6, no?     

> __< s​yntheticbird:monero.social >__ to be fair ipv6 is part of these years open issues     

> __< rbrunner >__ Maybe we can motivate vtnerd to look at this in some way :)     

> __< r​ucknium:monero.social >__ I think enabling IPv6 by default would increase Sybil resistance only if (1) we care only about the current known adversary (i.e. LinkingLion) and (2) LinkingLion doesn't try to Sybil attack on IPv6 because it is just getting to spy on the Monero network as a "freebie" because it actually cares most about Bitcoin.     

> __< r​ucknium:monero.social >__ These spy IP addresses were first noticed on the BTC network.     

> __< s​yntheticbird:monero.social >__ spying on monero as a "freebie" => for a freebie they put substantial efforts into their proxy software     

> __< r​ucknium:monero.social >__ By the way, the tidy `w_d / w_s < h_s / h_d` hold when we simplify the probability problem into draw-with-replacement (actually, we draw without replacement because you don't connect to the same node twice) and monerod already doesn't connect to a node in a /16 that it already has connected to (but it doesn't now do the de-duplication step).     

> __< r​ucknium:monero.social >__ But the realistic case can be checked with simple Monte Carlo simulations     

> __< d​oedl...:zano.org >__ rucknium: thats great news (30%->2%). Does game theory account for a sleepy, lazy opponent, too, who perceives a threat to Fiat as a whole (eventually) ?     

> __< r​ucknium:monero.social >__ No. I don't know how the opponent's payoff functions would change if they are like that, if at all.     

> __< j​effro256:monero.social >__ I'm thinking about how the deduplication would actually work in code. Do we only keep around one IP per /24 subnet ? If so, which one do we choose ? A spy node that is smart might actively try to be the first one to reach out to all the nodes to effectively blacklist the others on its /24 subnet. Or are you saying that we store all IP addresses, but treat them as one pickable obje<clipped messag     

> __< j​effro256:monero.social >__ ct when doing peer selection?     

> __< j​effro256:monero.social >__ IIRC there is a relatively low limit (or there used to be) on the number of peers stored in `p2pstate.bin`. We might want to increase that as long as we have asymptotically efficient peer selection algorithms     

> __< r​ucknium:monero.social >__ jeffro256: The whitelist and graylist and their limits (1000 and 5000, respective, IIRC), complicate things a little. I have ignored that complication for now     

> __< r​ucknium:monero.social >__ I would keep the lists as-is. Then do the de-duplication each time you select a new peer. You would have an ephemeral candidate list each time you activate the peer selection function.     

> __< j​effro256:monero.social >__ If we're keeping all IP addresses, which is probably a good idea, we should expand the limits on that list IMO     

> __< r​ucknium:monero.social >__ Of course, we could simulate the more complicated, realistic code.     

> __< r​ucknium:monero.social >__ Or, deploy Shadow on the new 1TB RAM machine, with the two peer selection code versions :D     

> __< r​ucknium:monero.social >__ Deploying shadow isn't a very serious suggestion in the short term since it would take time to figure out how to get it to work with monerod     

> __< c​haser:monero.social >__ what is Shadow?     

> __< r​ucknium:monero.social >__ But if we _do_ want to get shadow set up, I have been thinking that we could hire the person who wrote ethshadow instead of trying to learn it from scratch     

> __< r​ucknium:monero.social >__ chaser: A realistic network emulator that runs real application code, originally designed for Tor     

> __< s​yntheticbird:monero.social >__ chaser: A userspace network syscall intercepter. Permit to simulate internet level networking on a program without the program actually communicating on the internet. It's extremely efficient and performant     

> __< r​ucknium:monero.social >__ SyntheticBird: Have you looked into Shadow independently?     

> __< s​yntheticbird:monero.social >__ Briefly, the promise really excite me     

> __< d​oedl...:zano.org >__ would the use of the important whitelist be disabled for the first simulatios?     

> __< r​ucknium:monero.social >__ My current basic simulations with R don't use the limited whitelist concept. It just assume that all nodes with open ports are on each node's "whitelist".     

> __< d​oedl...:zano.org >__ i would rather drop dynamic peer discovery for first atempts and precalc static lists.     

> __< r​ucknium:monero.social >__ For more info about how the whitelist/graylist work, see page 4 of https://eprint.iacr.org/2019/411.pdf It may be out of date     

> __< r​ucknium:monero.social >__ 5) Reliability of MRL technical note 0010. https://www.getmonero.org/resources/research-lab/pubs/MRL-0010.pdf     

> __< d​oedl...:zano.org >__ tx, will have a look     

> __< r​ucknium:monero.social >__ In a Serai room, kayabanerve  said that MRL-0010 is "unsound". When I asked if it should be retracted he said, "I don't remember if it's been updated in any way and don't care to argue for its retraction, just caution with it."     

> __< r​ucknium:monero.social >__ Does anyone know anything about this?     

> __< r​ucknium:monero.social >__ By the way, retracted doesn't mean it would be deleted from getmonero.org . Just that a note would be added saying that some major part of the paper is incorrect.     

> __< c​haser:monero.social >__ no, other than being on the list of topics last week, totally news to me.     

> __< r​ucknium:monero.social >__ I have a long-term goal in my mind of making the MRL technical notes more "research official" by getting DOIs (document object identifiers) assigned to them. That costs some money, though.     

> __< c​haser:monero.social >__ in case thin unsoundness induced a vulnerability, which parts of Monero would be affected?     

> __< r​ucknium:monero.social >__ I guess DOI means digital object identifier, not document object identifier.     

> __< c​haser:monero.social >__ *this     

> __< d​oedl...:zano.org >__ what happend to university contacts?     

> __< r​ucknium:monero.social >__ I don't think MRL-0010 was used in Monero's protocol. I could be wrong.     

> __< r​ucknium:monero.social >__ Contacts are ongoing     

> __< r​ucknium:monero.social >__ Ok, well if someone knows something about MRL-0010, please bring it up after the meeting     

> __< r​ucknium:monero.social >__ We'll end the meeting here.     

> __< o​frnxmr:monero.social >__ Thanks ruck     

> __< s​yntheticbird:monero.social >__ Thanks     

> __< k​ayabanerve:matrix.org >__ MRL-0010 isn't used in Monero, a derivative of it used by some Monero atomic swap protocols.     

> __< k​ayabanerve:matrix.org >__ This was discussed in MRL years ago if someone wants to search the archive for "PlasmaPower".     

> __< k​ayabanerve:matrix.org >__ Having redownloaded the PDF, yes, it's unsound.      

> __< k​ayabanerve:matrix.org >__ > Given this, we wish to prove that, given only the values xG′ and xH′ (and other proof     

> __< k​ayabanerve:matrix.org >__ elements as needed), the discrete logarithm of each is a representation of the same integer. In particular, we     

> __< k​ayabanerve:matrix.org >__ do not wish to reveal x to the verifier     

> __< k​ayabanerve:matrix.org >__ The issue is the proof doesn't output xG', xH' yet xG'yG xH'zH     

> __< k​ayabanerve:matrix.org >__ The discrete logarithm of the former over G' is not necessarily an equivalent integer to the discrete logarithm of the latter over H'     

> __< k​ayabanerve:matrix.org >__ You need the two Schnorr PoKs well discussed since.     

> __< a​ck-j:matrix.org >__ Sorry I missed the meeting. I looked into hosting platforms and Kaggle seems like a no-go unfortunately. The competition would need to have a machine learning component according to their requirements, which it doesn’t.     

> __< a​ck-j:matrix.org >__ There isn’t any platforms specifically designed for what we are looking for but the closest I’ve found is HackerEarth, HackerRank, CodeChef, Codeforces     

> __< c​haser:monero.social >__ kayaba: thank you. Element can't search for usernames, and I managed to find the message only from my matrix[dot]org account, but here it is. (Monerologs doesn't cover the period either). 2020-10-11 23:48 UTC:     

> __< c​haser:monero.social >__ https://matrix.to/#/!toFcRZtpaiwiyapgVO:matrix.org/$4GGbCkt2TzVfujUW4Et2XhenNhTr0LidCw79NvoFbGE?via=matrix.org&via=monero.social&via=unredacted.org     

> __< r​ucknium:monero.social >__ Thanks chaser. The freenode logger has it: https://freenode.monerologs.net/monero-research-lab/20201011     

> __< c​haser:monero.social >__ (my link to the message doesn't work from a monero[dot]social account either...)     

> __< d​oedl...:zano.org >__ rucknium: "2) honest nodes in "popular" subnets would get fewer inbound connections and honest nodes in "lonely" subnets would get more inbound connections."     

> __< d​oedl...:zano.org >__ optimistically, given the data in  https://eprint.iacr.org/2019/411.pdf this^ could have a net positive effect on resiliance imo.     

> __< r​ucknium:monero.social >__ There are good things and bad things about it. You would have greater "decentralization" since there would be fewer connections to the centralized VPS providers. But 1) Honest node operators who run nodes on VPSes would have fewer connections, which means they would get txs and blocks with a little more latency. Of course, they could compensate for that by manually raising their n<clipped message     

> __< r​ucknium:monero.social >__ umber of outbound connections.     

> __< r​ucknium:monero.social >__ 2) Nodes that are alone in their subnets would have more connections, which may stretch their resources because the number of incoming connections is unlimited by default. During the tx spam last year, some node operators reduced their incoming connections. Hopefully, the bandwidth and CPU resources of connections will decrease when the proposed new tx relay process is implemented and deployed     

> __< r​ucknium:monero.social >__ which is here: https://github.com/monero-project/monero/issues/9334     

> __< d​oedl...:zano.org >__ exactely. the network is complex enough, so that trial&error would be a scientific approach.  the PR looks very helpful in this regard!     



# Action History
- Created by: Rucknium | 2025-02-04T21:31:46+00:00
- Closed at: 2025-02-14T16:21:59+00:00
