---
title: Monero Research Lab Meeting - Wed 29 January 2025, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1148
author: Rucknium
assignees: []
labels: []
created_at: '2025-01-29T14:47:42+00:00'
updated_at: '2025-02-06T17:50:44+00:00'
type: issue
status: closed
closed_at: '2025-02-06T17:50:44+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/meeting.html?p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3. Prize contest to optimize some FCMP cryptography code.

4. [v17 hard fork consensus rules to reject nonzero unlock time, large tx_extra, and v1 unmixable sweep transactions](https://github.com/monero-project/monero/pull/9751).

5. Research on [Autonomous System (AS) peer connection rules](https://github.com/monero-project/monero/pull/7935) to reduce spy node risk.

6. Reliability of [MRL technical note 0010](https://www.getmonero.org/resources/research-lab/pubs/MRL-0010.pdf).

7. Any other business

8. Confirm next meeting agenda

Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#1145 

# Discussion History
## Rucknium | 2025-01-30T19:42:39+00:00
Logs

> __< r​ucknium:monero.social >__ Meeting time! https://github.com/monero-project/meta/issues/1148     

> __< r​ucknium:monero.social >__ 1) Greetings     

> __< s​yntheticbird:monero.social >__ hi     

> __< rbrunner >__ Hello     

> __< a​rticmine:monero.social >__ Hi     

> __< c​haser:monero.social >__ hello     

> __< j​effro256:monero.social >__ Howdy     

> __< s​agewilder:unredacted.org >__ Hello     

> __< r​ucknium:monero.social >__ 2) Updates. What is everyone working on?     

> __< r​ucknium:monero.social >__ me: Working on researching Autonomous System (AS) peer connection rules to reduce spy node risk. Also starting to learn Rust 🦀     

> __< s​yntheticbird:monero.social >__ The last part is an incredibly great news     

> __< j​effro256:monero.social >__ Me: Trying to integrate Carrot/FCMP++ transaction construction together     

> __< j​berman:monero.social >__ me: continuing FCMP++ tx construction (filling out the pieces for FCMP++ in genRctSimple at the moment). Unfortunately I don't have tests to share for the FCMP++ optimization contest this week, got sucked into FCMP++ tx construction. Will prioritize test suites to advance the contest for next week's meeting     

> __< r​ucknium:monero.social >__ 3) Prize contest to optimize some FCMP cryptography code.     

> __< j​berman:monero.social >__ Nothing new to share from me this week on this front. Last week we discussed a few topics that perhaps we can bring up again today     

> __< j​berman:monero.social >__ Setting up a repo to host the contest, bumping payouts, and proposing using the dev fund for payouts     

> __< j​berman:monero.social >__ Any comments on those?     

> __< c​haser:monero.social >__ flip flop had reservations regarding the size of the prizes I think     

> __< r​ucknium:monero.social >__ Maybe sagewilder  can comment, since they expressed interest in being a contestant IIRC     

> __< s​agewilder:unredacted.org >__ No comments aside having the pleasure to hunt a bigger payout.     

> __< r​ucknium:monero.social >__ xmrack: Are you very familiar with contests on Kaggle? Different domain, I know, but maybe you have some opinions about prize amounts and attracting talent.     

> __< rbrunner >__ Things like these? https://www.kaggle.com/competitions     

> __< r​ucknium:monero.social >__ Yes     

> __< rbrunner >__ There seems to be a wide range of price sums ...     

> __< s​yntheticbird:monero.social >__ maybe im too naive or optimistic but it really seems to me like the payout bump is already a good incentive     

> __< s​yntheticbird:monero.social >__ is it still really that low to worry?     

> __< rbrunner >__ Say again, where does that price proposal stay?     

> __< c​haser:monero.social >__ I think this was the latest proposal ^     

> __< j​berman:monero.social >__ Initial proposal was 150 XMR for ec divisors 1st place, 50 XMR for helioselene 1st place. Last week I brought up raising to 500 XMR and 200 XMR respectively. I don't see comparable contests on Kaggle to form a constructive opinion on that     

> __< rbrunner >__ Thanks     

> __< r​ucknium:monero.social >__ It's not just the prize, but also the number and quality of possible competitors that will affect a programmer's decision to enter the competition. If it's 500 XMR and I think I would have 1/5th probability of winning it, then my expected revenue is 100 XMR. Expected utility? That depends on risk preferences.     

> __< j​berman:monero.social >__ fair. I think we can move on. I'll come back next week with stronger deliverables for the contest     

> __< rbrunner >__ My current gut feeling says that if we can indeed afford such sums we will be able to attract talent     

> __< r​ucknium:monero.social >__ Sounds good. Thanks!     

> __< r​ucknium:monero.social >__ 4) v17 hard fork consensus rules to reject nonzero unlock time, large tx_extra, and v1 unmixable sweep transactions. https://github.com/monero-project/monero/pull/9751     

> __< r​ucknium:monero.social >__ jeffro256: ^     

> __< j​effro256:monero.social >__ Just wanted to ask if anyone would be opposed to these rules. The first two solidify relay rules we already have , and the third disallows v1 txs at the same time as FCMP++ txs     

> __< r​ucknium:monero.social >__ I think they all sound good. Relay rules are leaky IMHO, so putting 1 and 2 as consensus is a good idea.     

> __< r​ucknium:monero.social >__ There should be tests written to double check that those outputs in (3) can be spent by FCMP. Have they been written?     

> __< c​haser:monero.social >__ I can't comment on #3, but #1 and #2 have been low hanging fruits, the advantage is obvious     

> __< rbrunner >__ I am not 100% sure about the 3rd rule. Just to confirm, nothing becomes unspendable with that after the FCMP++ hardfork, right?     

> __< rbrunner >__ There are just some limits *how* I can spend it.     

> __< rbrunner >__ In what kind of transactions     

> __< j​effro256:monero.social >__ Yup, it just disallows *new* v1 transactions. The FCMP tree lets you spend all outputs, including pre-RingCT     

> __< j​berman:monero.social >__ #1 and #3 sgtm. Since pre-RCT can be spent in FCMP++ proofs, no reason to allow unmixable rings anymore     

> __< rbrunner >__ Splendid. Nothing to say against all 3 rules from me     

> __< j​berman:monero.social >__ #2 initially sgmt as well     

> __< j​berman:monero.social >__ not yet, I don't have FCMP++ tx test yet. They'll be written     

> __< j​effro256:monero.social >__ And what about enforcing sorted extra ?     

> __< s​yntheticbird:monero.social >__ what is sorted extra ?     

> __< rbrunner >__ To get that extra micron towards tx uniformity despite having something in the tx_extra? :)     

> __< j​effro256:monero.social >__ Tx_extra has values which are prefixes by a tag value. The core reference code sorts these values by tag value when constructing transactions. Koe proposed enforcing they are sorted by node rule     

> __< j​effro256:monero.social >__ It wouldn't really help nonstandard tx_extra values, but it would help uniformity for bad wallet implementations that forget to sort     

> __< r​ucknium:monero.social >__ That sounds good to me. Verification of the sort would be very quick, right?     

> __< j​effro256:monero.social >__ A downside of this would be that it would take a hardfork to add new tag values     

> __< j​berman:monero.social >__ An alternative to sorting would be to create dedicated types for the fields we currently use tx extra for, which imo seems a saner long-term path     

> __< r​ucknium:monero.social >__ By "node rule" do you mean consensus or relay?     

> __< rbrunner >__ I dimmly remember to propose that as well, but jeffro256 was not immediately enthusiastic if I remember correctly     

> __< j​effro256:monero.social >__ Either, it would be a hardfork for consensus , or a messy upgrade for relay     

> __< rbrunner >__ (Nothing that is standard for any transaction in tx_extra anymore. That's not really "extra")     

> __< r​ucknium:monero.social >__ Why would a hard fork be necessary for a new field? Just have the new field byte be sorted properly, right?     

> __< j​effro256:monero.social >__ Tx_extra fields are not self describing, which means adding a new tag means that the whole tx_extra is unparseable to old code     

> __< r​ucknium:monero.social >__ Is this why we get "tx_extra not in standard format" warning in logs sometimes?     

> __< c​haser:monero.social >__ if it's not self-describing, how can different implementations use different sorting?     

> __< j​effro256:monero.social >__ Yes I believe so     

> __< j​effro256:monero.social >__ The tag values are described in the format, but how each individual value is deserialized isn't described     

> __< d​oedl...:zano.org >__ +1     

> __< j​effro256:monero.social >__ The parsing code takes the first varint i n the buffer, and depending on that value , selects a different deserialization code     

> __< j​effro256:monero.social >__ If the tag value isnt recognized, then it doesn't know when this value ends and the next begins, so the whole tx_extra is unparseable     

> __< rbrunner >__ Ah, that's the problem, there is no field length info?     

> __< j​effro256:monero.social >__ Yeah basically     

> __< a​ck-j:matrix.org >__ Rucknium: Re: kaggle     

> __< a​ck-j:matrix.org >__ I’ve used it in the past but haven’t set up a competition. I can look into it as this sort of competition is a bit different like you mentioned. It would be ideal if we use Kaggle or something similar that handles the out sourcing of developers.     

> __< j​effro256:monero.social >__ So code that enforces sorting wouldnt be able to happen new tag values, unless new tag values were length prefixed     

> __< j​effro256:monero.social >__ s/happen/handle     

> __< j​effro256:monero.social >__ I think we should hold off on it personally     

> __< r​ucknium:monero.social >__ xmrack: Thanks. If you could get more info on best practices, that would be helpful :)     

> __< rbrunner >__ One argument more, if you ask me, for *not* putting any more essential and necessary standard tx info in there anymore     

> __< c​haser:monero.social >__ is there anything imaginable (rationally useful) that current tags can't service?     

> __< d​oedl...:zano.org >__ what is all this flexibility (used) for?     

> __< c​haser:monero.social >__ rbrunner: +100. although that will require redesigning the tx format, which is a longer term effort.     

> __< rbrunner >__ I just had a flashback to almost interminable discussions back and forth over weeks regarding tx_extra :)     

> __< r​ucknium:monero.social >__ IIRC, Serai is going to put something in tx_extra.     

> __< c​haser:monero.social >__ it will     

> __< rbrunner >__ Well, if the core software stops to use it people can freely put there whatever they want, in whatever order, nobody cares     

> __< j​effro256:monero.social >__ I will sat, tx_extra_nonce, an existing field, should work for their use case     

> __< j​effro256:monero.social >__ Maybe     

> __< c​haser:monero.social >__ IMHO only arguments against this are disabling something important/useful, and the risk that we don't know when we'll be able to fork next to rectify potential lack of foresight     

> __< r​ucknium:monero.social >__ IIRC, koe didn't like deprecating tx_extra because changes in tx format would require a hard fork, so why did he suggest requiring it be sorted by tag? Or did he not consider that issue?     

> __< rbrunner >__ To put it bluntly, for me is starting to sort there instead of moving standard tx stuff out of it like the proverbial "polishing of a turd"     

> __< c​haser:monero.social >__ I think sorting is a much smaller risk     

> __< c​haser:monero.social >__ vs deprecating tx_extra     

> __< c​haser:monero.social >__ rbrunner, I'm with you on that     

> __< rbrunner >__ I guess the issue really was to go towards tx conformity out of principle, even if it's a small step. I am not sure, but I think there also was a format requirement, including lengths to properly skip unknown stuff     

> __< c​haser:monero.social >__ I've recently looked at issues regarding tx_extra and they were colossal in length. I am afraid redesigning the tx format may not fit into the HF timeline, considering the urgency of deploying FCMP++ to reduce harms to privacy. I may be wrong though!     

> __< j​effro256:monero.social >__ He wanted the values to be in "TLV" format which encodes a length, so that regardless of the type, the consensus code can skip over it     

> __< rbrunner >__ How much stuff do we put in there anyway? I am only aware about something related to subadresses, some key material. One more field in the standard tx structure, and done already? No?     

> __< s​yntheticbird:monero.social >__ Not very constructive but any estimates on HF date so far ?     

> __< s​yntheticbird:monero.social >__ since chaser talked about timeline     

> __< j​effro256:monero.social >__ rbrunner: transaction pubkeys and encrypted payment IDs     

> __< rbrunner >__ Ok, ok, two fields then. Is this really a problem, or only sheer inertia against changes in tx format after so many years?     

> __< j​effro256:monero.social >__ Adding one more field into the transaction would require we bump the version to 3, and deal with the consensus logic there, or put the information in `rctSigBase` after the rct type is deserialized     

> __< j​effro256:monero.social >__ Putting it in `rctSigBase` is weird in terms of organization, but would be pretty easy to do     

> __< rbrunner >__ I can't judge - is this significantly more and riskier work than starting to sort tx_extra and add a rule there?     

> __< j​effro256:monero.social >__ jberman: what do you think about the `rctSigBase` idea? We're already modifying it for FCMP++     

> __< j​effro256:monero.social >__ It would save us a few bytes versus putting it in extra     

> __< rbrunner >__ "is weird in terms of organization" tx standard stuff in tx_extra is also weird. Just saying :)     

> __< d​oedl...:zano.org >__ that would keep the wallets out, right?     

> __< rbrunner >__ Oh, things even get a little bit smaller. Wonderful :)     

> __< r​ucknium:monero.social >__ We are beyond the hour. Should this topic be rolled over into next week? I have an update on autonomous system (AS) spy node research too, but it's pretty long, so I'll hold it until next week.     

> __< j​effro256:monero.social >__ I think it would save four bytes: 1 for the additional_tx_pubkeys tag, 1 for the additional_tx_pubkeys vector length, 1 for the tx_extra_nonce tag, and 1 for the internal encrypted payment id tag     

> __< j​effro256:monero.social >__ Maybe five actually since we also save the tx_extra_nonce length value     

> __< j​berman:monero.social >__ personally I would prefer to focus on the core necessary changes for the upgrade first and not try to make many changes at once. We had prior discussed bumping tx version a while back but landed on maintaining rctSigBase as is for simplicity of the upgrade. I would prefer to streamline the upgrade     

> __< d​oedl...:zano.org >__ that would keep the wallets out, right? ("node rule")     

> __< j​effro256:monero.social >__ Fair enough     

> __< d​oedl...:zano.org >__ #1,2,3 are already big leaps     

> __< j​effro256:monero.social >__ I think we discussed it enough for now. I'd like to hear about the ASN stuff     

> __< j​effro256:monero.social >__ If someone objects to it,  it can be re-opened     

> __< r​ucknium:monero.social >__ Ok sure     

> __< r​ucknium:monero.social >__ I read four papers on autonomous system (AS) selection for Tor.     

> __< r​ucknium:monero.social >__ Tor's network threat modeling is more complicated than Monero's. Tor has three hops that make up a circuit, but Monero nodes are only aware of immediate peers on the network. A Tor client's routing decisions are affected by the bandwidth of relays, which are measured and reported. And the bandwidth is an explicit cost of a Tor adversary (not just IP address leasing), unlike a Monero adversary.     

> __< r​ucknium:monero.social >__ Wan et al. (2019) "Guard Placement Attacks on Path Selection Algorithms for Tor"     

> __< r​ucknium:monero.social >__ Oh, oops, let me put the agenda item     

> __< r​ucknium:monero.social >__ 5) Research on Autonomous System (AS) peer connection rules to reduce spy node risk. https://github.com/monero-project/monero/pull/7935     

> __< r​ucknium:monero.social >__ This paper criticizes earlier papers that had designed Tor circuit selection algorithms that were supposed to reduce Tor's vulnerability to spying. The paper's point is that adversaries are free to change behavior, so your algorithm need to be resistant to the status quo in the network, but also defend against an adversary deliberately placing spy Tor relays in "vulnerable" parts <clipped message     

> __< r​ucknium:monero.social >__ of the network. They suggest a "meta-algorithm" that tries to anticipate possible attacks on the circuit selection algorithm, given the network state and the economic costs that an adversary would incur when deploying any given strategy. To me, it looks like sort of a brute force algorithm.     

> __< r​ucknium:monero.social >__ Rochet et al. (2020) "CLAPS: Client-Location-Aware Path Selection in Tor"     

> __< r​ucknium:monero.social >__ Similar to Wan et al. (2019), but they use a more formal linear programming optimization algorithm and try to reduce client-to-destination latency.     

> __< r​ucknium:monero.social >__ Jansen & Goldberg (2021) "Once is Never Enough: Foundations for Sound Statistical Inference in Tor Network Experimentation"     

> __< r​ucknium:monero.social >__ This paper uses Shadow, a network simulator that has been under development for 15 years. Shadow executes actual application code instead of just being an abstraction. We could possibly use it to simulate the Monero network with `monerod` and/or `cuprate`, especially now that we have a machine with 1TB of RAM. The paper shows that you need to sample network behavior many times to <clipped message     

> __< r​ucknium:monero.social >__ get a statistically valid measurement for your Tor network tests. It looks like a 1%-scale Tor is unreliable, but a 10%-scale is OK.     

> __< r​ucknium:monero.social >__ Gegenhuber et al. (2023) "An extended view on measuring Tor AS-level adversaries"     

> __< r​ucknium:monero.social >__ This paper tries to figure out which, if any, ASes could be a threat to Tor user privacy. They find that Hetzner theoretically poses the greatest threat. From some data I've seen, that's probably true for Monero, too. Many "honest" Monero nodes are hosted on Hetzner.     

> __< r​ucknium:monero.social >__ I got a reply from Giulia Fanti, the lead author of the Dandelion++ paper ( https://www.ece.cmu.edu/directory/bios/fanti-giulia.html ). She said she hadn't read the Clover paper yet, but would take a look. Clover is an alternative to D++ that is supposed to have better privacy for nodes with closed inbound ports.     

> __< r​ucknium:monero.social >__ She said that she doesn't have a good solution for the proxy node problem, but pointed me to her paper here that penalized peers that relay fewer transactions than honest peers: https://arxiv.org/abs/2205.06837     

> __< r​ucknium:monero.social >__ I re-analyzed the transaction relay log data from last year, and there is no big difference between the volume of txs relayed by suspected spy node IP addresses and honest peers.     

> __< r​ucknium:monero.social >__ She said she would think about it more. Best case scenario, she gets interested in it enough to write a paper and solve the problem for us :)     

> __< r​ucknium:monero.social >__ At this point in time I am skeptical of the value of an AS diversity rule. I plan to sketch a basic economic model to see what bulk discount adversaries would have to get from leasing many IPs from the same AS, but in different subnets. Adversaries get a discount for leasing whole subnets, but Monero nodes already have a rule against connecting to nodes within the same /16 subnet <clipped message     

> __< r​ucknium:monero.social >__ (same with Tor circuit building).     

> __< r​ucknium:monero.social >__ Right now, I can think of a possible improvement to the /16 subnet diversity rule. (Maybe it already works like this, but I don't know where in the code the peer selection happens.) Instead of taking the candidate peer list and drawing a peer from it, then rejecting the peer if we have already connected to a /16 subnet sibling, do this: First randomly eliminate all peers but one t<clipped message     

> __< r​ucknium:monero.social >__ hat are in the same /16 subnets from the candidate list. Then pick a peer from that reduced list (also discarding the peer if it violates the subnet sibling rule). That would reduce the probability that you select your next peer from the adversary's saturated subnet(s) in the first place.     

> __< r​ucknium:monero.social >__ This revised algorithm would also reduce the probability of selecting honest nodes within the same subnet, e.g. nodes on VPSes.     

> __< r​ucknium:monero.social >__ That's my update. Any comments or questions?     

> __< j​effro256:monero.social >__ The threat from Hetzner being that they spy on network traffic, or take down the honest nodes?     

> __< r​ucknium:monero.social >__ Either. My research focus is on spy node risk, but network partitioning, eclipse, and censorship are concerns, too     

> __< d​oedl...:zano.org >__ "discarding the peer if it violates the subnet sibling rule" <- overdue     

> __< j​effro256:monero.social >__ At first glance, that seems like a pretty sane rule: don't trust peers to not shill their subnet siblings. Could be an issue for many honest nodes on a single provider, but again, if we can trivially distinguish them as being centralized, then we shouldn't be over-picking them anyways     

> __< r​ucknium:monero.social >__ It would help me if any C++ readers can confirm exactly how the /16 subnet rule works. Or point me to where in the code it does that and I could try to figure it out.     

> __< d​oedl...:zano.org >__ "discarding the peer if it violates the subnet sibling rule" <- overdue     

> __< d​oedl...:zano.org >__  "To me, it looks like sort of a brute force algorithm." <- it is. In the long run a Web  Of Trust based approach is inevitable. That is already viable now, only requires community orga     

> __< j​effro256:monero.social >__ Thanks for reaching out to Fanti btw     

> __< malinero >__ https://github.com/monero-project/monero/blob/master/src/p2p/net_node.inl#L1589     

> __< malinero >__ ^ rucknium     

> __< r​ucknium:monero.social >__ I also told her about the Chainalysis presentation's comments praising (in a way) Dandelion++. She hadn't heard about it and thanked me for sharing.     

> __< r​ucknium:monero.social >__ Thanks, malinero     

> __< j​effro256:monero.social >__ Does Dandelion++ factor in the length of outgoing connection time to the privacy model?     

> __< r​ucknium:monero.social >__ AFAIK, no. IIRC, there isn't a big spread in how long connections last anyway. Let me see if I have the plot     

> __< r​ucknium:monero.social >__ See Figure 14 on page 21: https://github.com/Rucknium/misc-research/blob/main/Monero-Black-Marble-Flood/pdf/monero-black-marble-flood.pdf     

> __< r​ucknium:monero.social >__ Pretty concentrated around 25 minutes connection duration, but there are a few long-lived outliers.     

> __< r​ucknium:monero.social >__ We can end the meeting here. Thanks everyone.     

> __< j​effro256:monero.social >__ Thanks everyone!     

> __< s​yntheticbird:monero.social >__ thanks     

> __< c​haser:monero.social >__ thank you all!     

> __< a​rticmine:monero.social >__ Thanks     

> __< a​ck-j:matrix.org >__ Is there a github issue describing the competition? I thought there was but cant find it jberman     

> __< s​needlewoods:monero.social >__ there is this draft by kayaba https://github.com/kayabaNerve/fcmp-plus-plus-optimization-competition     

> __< k​ayabanerve:matrix.org >__ Why? Checking the prior tag had lesser value than the next tag doesn't sound like it'd need a hard fork? Is it because you now require being able to fully decode the TX extra, and don't just yield the fraction recognizable?     

> __< k​ayabanerve:matrix.org >__ Except the whole TX extra isn't unparseable. Only the remainder.     

> __< k​ayabanerve:matrix.org >__ That leads into the question the value of sorting for this partial case. I don't care and would wait for the time we strongly type all wallet data (my advocacy) leaving TX extra arbitrary.     

> __< sech1 >__ IIRC tx_extra have length field, with just one or two exceptions     

> __< sech1 >__ so it's possible to parse them and skip over the unknown ones     

> __< k​ayabanerve:matrix.org >__ sech1: The entire TX extra does. The individual tags aren't required to be Type Length Value. Some tags used by Monero are solely Type Value as length is fixed to type.     

> __< sech1 >__ yes, some tags are known and have known length, but other tags are supposed to have length field     

> __< sech1 >__ IIRC the sorting code assumes this     

> __< sech1 >__ and if it can't find length, it says that sort failed     

> __< sech1 >__ or maybe it fails when it sees an unknown tag - I don't remember     

> __< k​ayabanerve:matrix.org >__ Except if it's an unknown tag, Monero would have to assume if it's supposed to have a length or not.     

> __< moneromooo >__ Pretty sure the sorting code does not assume this, and that is why it fails on unknown tags.     

> __< k​ayabanerve:matrix.org >__ Right now, it fails on unknown tag.     

> __< k​ayabanerve:matrix.org >__ (They aren't assumed to be length-prefixed)     

> __< k​ayabanerve:matrix.org >__ Though failure is partial? Monero will yield whatever it does manage to read     

> __< sech1 >__ well, new consensus rules can enforce the length field for all tags except the ones that have fixed length     

> __< k​ayabanerve:matrix.org >__ jeffro256: FYI, monero-wallet uses Nonce(127). It's the highest Nonce type which won't be interpretable as a multi-byte varint.     

> __< k​ayabanerve:matrix.org >__ As long as wallet2 doesn't introduce Nonce(2 ..= 126), and then finally its own Nonce(127), we're fine.     



# Action History
- Created by: Rucknium | 2025-01-29T14:47:42+00:00
- Closed at: 2025-02-06T17:50:44+00:00
