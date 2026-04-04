---
title: 'Monero Research Lab Meeting - Wed 17 April 2024, 17:00 UTC '
source_url: https://github.com/monero-project/meta/issues/992
author: Rucknium
assignees: []
labels: []
created_at: '2024-04-16T21:49:03+00:00'
updated_at: '2024-04-30T17:22:49+00:00'
type: issue
status: closed
closed_at: '2024-04-30T17:22:49+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

[Join the Monero Matrix server if you don't already have a Matrix account.](https://web.archive.org/web/20230128130949/https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211027T170000&p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3. [Potential measures against a black marble attack](https://github.com/monero-project/research-lab/issues/119).

4. Research [Pre-Seraphis Full-Chain Membership Proofs](https://gist.github.com/kayabaNerve/0e1f7719e5797c826b87249f21ab6f86). 

5. Any other business

6. Confirm next meeting agenda


Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#989 

# Discussion History
## jeffro256 | 2024-04-17T16:55:31+00:00
Howdy! Sorry for missing the last couple meetings, a lot has happened. I wanted to discuss @kayabaNerve's network FCMP+SA+L-on-RingCT upgrade proposal in this comment: https://gist.github.com/kayabaNerve/0e1f7719e5797c826b87249f21ab6f86?permalink_comment_id=5027156#gistcomment-5027156. The post basically summarizes almost every concern I have with FCMPs-on-RingCT, assuming we upgrade to Seraphis in the future. 

I think we should also discuss the possibility of FCMP+SA+L-on-RingCT completely replacing the Seraphis protocol, since we apparently now have a path for complete feature parity in that proposal. I don't necessarily like the idea of being tied to RingCT forever in terms of efficiency and the way that proofs are monolithic, but practically, doing FCMP+SA+L-on-RingCT would probably get FCMPs into Monero faster, if that is what the network's foremost concern is.

## Rucknium | 2024-04-17T19:41:00+00:00
Logs:

> __< d​angerousfreedom:monero.social >__ I cant make it for today's meeting but I would like to share my initial thoughts about the proposed FCMP+SA+L. First, it is really amazing to see kayaba and tevador exploring new ways to integrate FCMP into Monero now. IIUC, the proposed scheme would replace Seraphis entirely (from the functional POV) if it can solve the FS problem. The question is then what do we do? I dont have <clipped     

> __< d​angerousfreedom:monero.social >__ enough knowledge to give an educated answer now so my immediate task is to understand it since it will have a huge impact on all development tasks of everyone. I do see a relatively clear and conservative path to regtest/testnet/mainnet with seraphis (regarding implementation and its crypto solidity). I do not see the same for FCMP+SA+L as I dont grok it. So I will try, for the ne<clipped     

> __< d​angerousfreedom:monero.social >__ xt weeks, to only focus on understanding it.     

> __< r​ucknium:monero.social >__ MRL meeting in this channel in one hour.     

> __< k​ayabanerve:matrix.org >__ I'd clarify "would" to "could" and continue my immediate advocacy for a shorter timeline, FCMP for RingCT with large amounts of work reusable by Seraphis. If once that's done, there's interest in adding F-S, we can. If once that's done, there's interest in adding the wallet code for it (can be done at any point, not a hard fork), we can. If once that's done, we want to move to JAM<clipped message     

> __< k​ayabanerve:matrix.org >__ TIS, or to Seraphis + JAMTIS, or release a new TX version, we can. It's a literal sea of options which can be discussed nearly infinitely. That's why I'm saying the core of this, FCMPs on RingCT, faster than Seraphis, with large swaths reusable for Seraphis, is a good proposal we should move forward with now (as prior discussed).     

> __< r​ucknium:monero.social >__ Meeting time! https://github.com/monero-project/meta/issues/992     

> __< r​ucknium:monero.social >__ 1) Greetings     

> __< c​haser:monero.social >__ hello     

> __< rbrunner >__ Hello     

> __< j​effro256:monero.social >__ On the contrary (which hopefully we can did into more in the meeting), I'm opposed to doing this upgrade AND Seraphis for these reasons: https://gist.github.com/kayabaNerve/0e1f7719e5797c826b87249f21ab6f86?permalink_comment_id=5027156#gistcomment-5027156. If we are going to do the FCMP+SA+L networj upgrade, we should ditch the idea of doing Seraphis altogether. Trying to do 2 monu<clipped messag     

> __< j​effro256:monero.social >__ mental changes to the protocol back-to-back is not a great idea in my opinion.     

> __< j​effro256:monero.social >__ Howdy btw     

> __< k​ayabanerve:matrix.org >__ 👋     

> __< h​into.janaiyo:matrix.org >__ hello     

> __< jberman >__ hello     

> __< r​ucknium:monero.social >__ 2) Updates. What is everyone working on?     

> __< k​ayabanerve:matrix.org >__ jeffro256: The whole point was to minimize the amount of changes it is. It's theoretically only a replacement for the CLSAG with the new tree database from a protocol point of view. It doesn't inherently introduce new keys/TX structures/wallet send protocols.     

> __< r​ucknium:monero.social >__ Let's discuss FCMP and Seraphis when we get to that agenda item. Thanks.     

> __< k​ayabanerve:matrix.org >__ (sorry for breaking the meeting timeline, I'll hold off on further comments)     

> __< r​ucknium:monero.social >__ me: I developed the first version of `xmrpeers`, an R package for analysis of Monero's peer-to-peer node network: https://github.com/Rucknium/xmrpeers . A few people are using it to collect data on peer-to-peer network latency when using `set_log net.p2p.msg:INFO`.     

> __< jberman >__ me: recently finished the async scanner using the Seraphis lib, I'm seeing 50-60% faster syncing over clearnet using one of gingeropolous ' remote nodes, and wrote up a proposed plan to deprecate wallet2 + replace with Seraphis lib while keeping the existing wallet API: https://github.com/seraphis-migration/strategy/issues/3     

> __< c​haser:monero.social >__ @Rucknium that's nice. to be clear, the data can be collected without handling R, right?     

> __< h​into.janaiyo:matrix.org >__ me: finishing last bits of Cuprate's database API, somewhat equivalent to `monerod`'s BlockchainLMDB     

> __< r​ucknium:monero.social >__ chaser: You can use the `set_log net.p2p.msg:INFO`  to get the info on who is sending you txs and when, but you don't get a ping network latency measurement from just the logs. It is best to know when your peer is _sending_ that data, not just when you receive it. The latency measurement in `xmrpeers` is for the latency measurement.     

> __< r​ucknium:monero.social >__ Or anyone can write their own pinger and parse the log to get their peer IP addresses.     

> __< c​haser:monero.social >__ I see, thanks     

> __< j​effro256:monero.social >__ Good work Rucknium. Would this work allow us to empirically test the privacy of Dandelion++?     

> __< r​ucknium:monero.social >__ jeffro256: I hope so. I can discuss more in the next agenda item     

> __< j​effro256:monero.social >__ kk     

> __< r​ucknium:monero.social >__ 3) Discuss: Potential measures against a black marble attack https://github.com/monero-project/research-lab/issues/119     

> __< r​ucknium:monero.social >__ There was possible spam on April 12-13 again. Then a large number of consolidation transactions April 16-17.     

> __< r​ucknium:monero.social >__ I have been working on collecting data that can help guess the node origin of the spam transactions. I originally was going to use the techniques in Cao, Yu, Decouchant, Luo, & Verissimo (2020) "Exploring the Monero peer-to-peer network." https://moneroresearch.info/index.php?action=resource_RESOURCEVIEW_CORE&id=99     

> __< r​ucknium:monero.social >__ to collect the node list and edge list of the P2P network graph. Then I noticed the relevant log messages had `last_seen: Never`. Cao et al. (2020) used `last_seen` to figure out which peers were connected (i.e. the get the network edge list).     

> __< j​effro256:monero.social >__ Why would a spam attacker consolidate funds if they intend to produce more spam? Maybe they had a very limited budget and each enote is worth less than the fees required to create a 1 input tx with that enote?     

> __< r​ucknium:monero.social >__ jeffro256: Maybe they don't intend to produce more spam. But your other hypothesis is possible. Their spamming script may require more fees per output.     

> __< r​ucknium:monero.social >__ I did some searching and found that moneromooo patched the `last_seen` potential privacy issue: https://github.com/monero-project/monero/pull/5481  https://github.com/monero-project/monero/pull/5682     

> __< r​ucknium:monero.social >__ So that would make it much harder to do statistical analysis to defeat Dandelion++ like suggested by the simulations of Sharma, Gosain, & Diaz (2022) "On the anonymity of peer-to-peer network anonymity schemes used by cryptocurrencies." https://moneroresearch.info/index.php?action=resource_RESOURCEVIEW_CORE&id=130     

> __< r​ucknium:monero.social >__ But with a strong enough signal by the spam, maybe we can still narrow down the spam origin, which would provide more evidence that this is actually spam.     

> __< rbrunner >__ If they do us the "favor" to continue to spam?     

> __< r​ucknium:monero.social >__ Those hundreds of consolidation txs are a very strong signal. I am collecting data now because without log data collection, the p2p message data is lost forever. Then I can analyze later.     

> __< r​ucknium:monero.social >__ We should have several sets of log data for the April 12-13 and 16-17 incidents already.     

> __< rbrunner >__ Interesting.     

> __< r​ucknium:monero.social >__ So I could analyze just that data if no more suspected spam occurs.     

> __< r​ucknium:monero.social >__ My opinion: If Cypher Stack is not able to produce a mathematics security proof for Generalized Bulletproofs in their expected 1.5 months of work, a hard fork to increase ring size and maybe change tx fees should be considered and prepared for.     

> __< r​ucknium:monero.social >__ In that situation, it is not clear that FCMP will be possible with the Curve Trees design.     

> __< rbrunner >__ That possible mitigations GitHub issue excludes the "hot topic" everybody is talking about, FCMPs ...     

> __< r​ucknium:monero.social >__ rbrunner: It is listed under "omitted measures" https://github.com/monero-project/research-lab/issues/119 : "introduce full-chain membership proofs (FCMP) with Seraphis: FCMPs are the ultimate solution to attacks related to ring signatures, but they are currently not in a deployable state. ideally, they would be introduced together with the Seraphis transaction protocol. these two<clipped message     

> __< r​ucknium:monero.social >__ , presuming the current rate of progress won't change, are estimated to be ready in 5+ years."     

> __< rbrunner >__ Yeah, "omitted", not "excluded"     

> __< k​ayabanerve:monero.social >__ I agree with that omission.     

> __< j​effro256:monero.social >__ I think that it be be worth researching into how effective FCMPs would actually be from large rings in REAL terms, in regards to decoy flood attacks. if I, as a flooder, own 90% of all enotes, and thus 90% of decoys, what is the actual privacy impact for non-specifically targeted individuals if the EFFECTIVE ref set size is 16 versus half the chain?     

> __< rbrunner >__ The long and detailed comments that jeffro256 linked to right at the start of the meeting look interesting at first glance, but I think time would be needed to digest it all     

> __< k​ayabanerve:monero.social >__ We should have a fallback for if FCMPs don't work out, which they may simply 'politically'.     

> __< r​ucknium:monero.social >__ I think we are moving to the next agenda item:     

> __< c​haser:monero.social >__ I favor the FCMP+SA+L proposal, but I don't consider FCMPs as a short/mid-term solution to the black marble flood threat, not even with the best-case timeline (12 months). I think a fork with any one or multiples of the listed countermeasures is warranted, because right now, we have our guards down.     

> __< r​ucknium:monero.social >__ 4) Research Pre-Seraphis Full-Chain Membership Proofs  https://gist.github.com/kayabaNerve/0e1f7719e5797c826b87249f21ab6f86     

> __< j​effro256:monero.social >__ FCMPs are amazing and necessary for preventing EAE, EABE, and other counterparty de-anonymizing attacks, but how useful are they really against decoy flood attacks versus large rings? I don't have any formal answers, although if you want to perform a deterministic tx graph analysis with a decoy flood, it gets exponentially larger with a bigger ring size     

> __< j​effro256:monero.social >__ *larger->harder     

> __< rbrunner >__ Assuming that we do that research, and it would produce results, how would we *judge* those results then?     

> __< rbrunner >__ There is in any case a large "psychological" factor in all this     

> __< k​ayabanerve:monero.social >__ @jeffro256 Rings fundamentally don't stop attacks such as the EAE and have explicitly bad spend patterns.     

> __< k​ayabanerve:monero.social >__ Spam under FCMPs is ignored. Spam under CLSAG needs to be proportionately adjusted to.     

> __< k​ayabanerve:monero.social >__ That's incredibly surface commentary but it doesn't change it's not wrong.     

> __< r​ucknium:monero.social >__ rbrunner: First, define an economic utility function for Monero users....     

> __< k​ayabanerve:monero.social >__ (And you acknowledged the first set, I know)     

> __< r​ucknium:monero.social >__ Should we take 5 minutes to read jeffro256 's comments on FCMP/Seraphis that he posted before the meeting? https://gist.github.com/kayabaNerve/0e1f7719e5797c826b87249f21ab6f86?permalink_comment_id=5027156#gistcomment-5027156     

> __< j​effro256:monero.social >__ I wouldn't say spam is ignored under FCMPs, just from a privacy perspective. From a decentralization perspective, spam still needs to be considered and adjusted to if we don't want to end up like Ethereum with an unmanagebly larger L1, that doesn't allow for end users to run nodes     

> __< rbrunner >__ To read "Quick Summary of Concerns with FCMP-RCT" then, in 5 minutes     

> __< r​ucknium:monero.social >__ Ok. Do we know if this assumption is true? "For efficiency, security, cryptographic clarity, elliptic curve changes, perfect forward secrecy, or other inherent protocol properties, the network WILL want to migrate to Seraphis at SOME point. If this assumption is NOT true (which could possibly be the case since FCMP-RCT achieves feature parity with Seraphis with F-S added), then yo<clipped message     

> __< r​ucknium:monero.social >__ u can ignore this entire post altogether."     

> __< rbrunner >__ Can't judge. Just want to make sure everybody understand that Seraphis and Jamtis are already *implemented*, by an effort of about 1.5 man years     

> __< v​tnerd:monero.social >__ Sorry forgot about meeting, hi     

> __< rbrunner >__ It took that much for a careful, solidly engineered Seraphis and Jamtis library     

> __< rbrunner >__ "only" you could say     

> __< rbrunner >__ (I mean that "only a library" of all this effort may look small)     

> __< rbrunner >__ What is missing is all the rest, a decent wallet, a new tx class, and more     

> __< j​effro256:monero.social >__ The post is mainly against doing FCMP-RCT as a stop-gap measure. It has theoretically feature parity with Seraphis. So we should decide to do one or the other for the health of the protocol IMO. Seraphis (even with FCMPs) is *probably* always going to have less CPU required for nodes, unless there's something that I'm not seeing. Seraphis has more upfront work. Seraphis has less t<clipped messag     

> __< j​effro256:monero.social >__ echnical debt for future upgrades inherently because of the proof structure. FCMP-RCT can be done sooner. If we do Jamtis on RingCT after FCMPs, that will likely cement us into FCMP-RCT for a long time. Seraphis integration has a head start. FCMP-RCT probably takes less work to first hard fork. There are a lot of considerations to make     

> __< j​effro256:monero.social >__ But just to re-iterate, because I think it's impiortant, that post is against doing FCMP-RCT AND Seraphis     

> __< k​ayabanerve:monero.social >__ I have so many disagreements there yet I don't want to be a dick.     

> __< j​effro256:monero.social >__ It's okay, you can be a dick     

> __< rbrunner >__ It might take weeks to discuss all this to a good extent ...     

> __< k​ayabanerve:monero.social >__ I disagree every listed section is so notably modified.     

> __< k​ayabanerve:monero.social >__ The Seraphis design would be simpler and potentially more efficient. The exact bounds aren't known yet.     

> __< k​ayabanerve:monero.social >__ We don't need to increase reliance on wallet2. cc jberman     

> __< r​euben:firo.org >__ Better weeks to discuss then make the wrong decision imo     

> __< k​ayabanerve:monero.social >__ They rewrote the wallet2 API around the Seraphis lib, which includes RingCT, for cleanliness.     

> __< k​ayabanerve:monero.social >__ We can discuss deploying that pre-Seraphis.     

> __< rbrunner >__ Right, but there are young horses here that just long to finally start the race :)     

> __< j​effro256:monero.social >__ I'm also looking through the lens of someone who looks at the Blockchain code a lot, is currently working on implementation of a network upgrade, someone who values L1 simplicity seriously, and doesn't necessarily have FCMPs as my firstmost priority     

> __< r​euben:firo.org >__ kayabanerve @kayabanerve:monero.social: did you figure out the offloading for signing (for hardware wallets?)     

> __< k​ayabanerve:monero.social >__ "Overkill" They're more efficient than large CLSAGs IIRC, and the research carries to Seraphis.     

> __< k​ayabanerve:monero.social >__ @Reuben same proof separation as Lelantus (Spark)/Seraphis.     

> __< r​euben:firo.org >__ Nice     

> __< k​ayabanerve:monero.social >__ rbrunner: Seraphis is years out. I made a proposal for 6-12m. Every week in meetings is another week I wouldn't call Monero more sender private than plausible deniability.     

> __< r​euben:firo.org >__ What about multisig ?     

> __< k​ayabanerve:monero.social >__ So yes, I want to actually want to move forward and not debate in committee ad infinitum.     

> __< rbrunner >__ Yeah, if you can make those 6-12m.     

> __< r​euben:firo.org >__ Iirc Triptych wasn't implemented cause of poo multisig.     

> __< j​effro256:monero.social >__ Overkill from an engineering perspective in terms of effort required, changes in how we model privacy, etc. Again, we can do FCMPs on Seraphis, I'm not opposed to that, but as stated in the post, spam attacks shouldn't be a factor each which way     

> __< k​ayabanerve:monero.social >__ It's a generalized schnorr protocol and Schnorr multisig quite directly applies (by eye, not by academic proofs).     

> __< r​euben:firo.org >__ Nice     

> __< k​ayabanerve:monero.social >__ @jeffro256 The spam attacks, if for poisoned outputs, should be. Rings are at best a stop gap there.     

> __< plowsof >__ Jeffro what would you need to put kayabas proposal to funding as-is?      

> __< k​ayabanerve:monero.social >__ Also, larger attack surface due to SA+L???     

> __< k​ayabanerve:monero.social >__ It's using a proof proven from 2009. Seraphis uses a novel proof.     

> __< k​ayabanerve:monero.social >__ (Though i did suggest replacing the Seraphis proof with that 2009 proof as well)     

> __< rbrunner >__ plowsof: I don't understand the question. Do you mean "need" financially?     

> __< k​ayabanerve:monero.social >__ Yes, we have to argue the statement composition secure, yet how is that a "much larger attack surface"?     

> __< r​ucknium:monero.social >__ On technical debt: Current monerod code did not handle the suspected spam very well. If tx verification is a lot slower with FCMP, won't the monerod code have to improve to avoid major problems?     

> __< k​ayabanerve:monero.social >__ > then background syncing will necessarily consume more storage/RAM.     

> __< k​ayabanerve:monero.social >__ ???     

> __< rbrunner >__ It's explained later down, in more detail, I think     

> __< plowsof >__ Not financial, just unknowns to be known if any or its a fundamental disagreement of our near futures dorection      

> __< k​ayabanerve:monero.social >__ Wallets wouldn't sync FCMPs, they'd be pruned. There's no impact there.     

> __< j​effro256:monero.social >__ Each individual proof component in Seraphis has a lower attack surface being split into ownership, unspentness, membership. Overall is a different story. But in effect, one would have change larger portions of the proof assuming proof changes in the future, and those changes are more compartamentalized under Seraphis     

> __< jberman >__ To get FCMP-RCT done within the timeframe, it would probably make sense to do implement wallet2 FWIW     

> __< jberman >__ to implement in wallet2*     

> __< j​effro256:monero.social >__ And I'd probably agree w those changes BTW     

> __< k​ayabanerve:monero.social >__ Oh, literally due to storing more potential key images, yet that ignores how it adds ovks.     

> __< jberman >__ the wallet API is not rewritten yet for Seraphis lib, I just wrote up a proposal to do that here and estimated full-time work minimum of 3-6 months: https://github.com/seraphis-migration/strategy/issues/3     

> __< rbrunner >__ That is what some people here fear to hear, jberm, that "yet more complicated wallet2" story     

> __< jberman >__ Assuming Seraphis after FCMP-RCT, it's probably a fair assessment that the Seraphis lib would then be extended to also construct FCMP-RCT txs in order to deprecate wallet2     

> __< j​effro256:monero.social >__ Yes but background view key syncers have to store key images that they don't know whether or not are theirs (since they don't have the spend key)     

> __< k​ayabanerve:monero.social >__ My literal take is the document is overly critical and conflates a variety of different things. It says FCMPs is worse because X, yet not because X disappears with Seraphis, because it's just under a different name for whose problem it is. That applies to several of these points.     

> __< j​effro256:monero.social >__ With OVK, depending on the definiton, that issue might disappear     

> __< k​ayabanerve:monero.social >__ The "attack surface" and "sync" comments trivially classify there.     

> __< j​effro256:monero.social >__ Do OVKs require changes to the cryptonote addressing scheme?     

> __< k​ayabanerve:monero.social >__ I'm fine respecting @jeffro256 as a developer while completely disagreeing with at least the presentation of their analysis. I don't care to bicker with a friend for the next hour in public so I'm fine leaving them the "opposition" and the community to think about it independently.     

> __< k​ayabanerve:monero.social >__ No.     

> __< k​ayabanerve:monero.social >__ OVKs and F-S don't require a new protocol. Solely newly generated addresses to take advantage of those featurez.     

> __< k​ayabanerve:monero.social >__ *features     

> __< rbrunner >__ kayabanerve, if you say 6-12m, what point would be reached then? Feature complete, and in *theory*, from a purely technical standpoint, ready for hardfork?     

> __< k​ayabanerve:monero.social >__ jberman: Thank you for the context.     

> __< r​ucknium:monero.social >__ IMHO, we need to bicker on this because it is a very important fork in the road.     

> __< rbrunner >__ Agree, even it may turn out to be hard     

> __< k​ayabanerve:monero.social >__ I'm confident, within 6m, we can have an impl for auditing. For integration, please ask jberman who is my deferred to.     

> __< k​ayabanerve:monero.social >__ Let's also clarify as impl + audits of impl + PR integrating, and drop the integration review when discussing timeline.     

> __< rbrunner >__ Maybe I am bit overly dramatic, but this has the potential that in the end 2 teams walk into 2 different directions, which would be quite unfortunate     

> __< k​ayabanerve:monero.social >__ No. I need to write a full response to jeffro256 when I'm not on an IM platform, and potentially privately reach out to form a mutual summary which provides clear comments for review (without conflicts).     

> __< k​ayabanerve:monero.social >__ I don't need to feel like I need to immediately respond, and write short/snappy messages which don't best represent myself nor my thoughts.     

> __< rbrunner >__ Sounds good to me. Might mean that the discussion today won't get much further, but then be it so.     

> __< r​ucknium:monero.social >__ Ok. We can wait for a full response to jeffro256 's comments.     

> __< k​ayabanerve:monero.social >__ The core of the FCMP work, 80% of this proposal, should be reusable under Seraphis. I keep saying that to show we're not yet actually deciding and to try and move forward as I can :/     

> __< j​effro256:monero.social >__ I might be wrong, but I think the confusion here might stem from the fact that I'm looking through the lens on a person that has to look at and maintain BOTH protocols if they BOTH get implemented. A lot of these points aren't harping on something lacking in FCMP-RCT, it's harping on the added complexities and worse overall timelines regarding X if we try to do both     

> __< k​ayabanerve:monero.social >__ That way, we can make distinct discussions when we're farther down the road. That wastes effort at worst, that doesn't leave us with the wrong decision.     

> __< h​into.janaiyo:matrix.org >__ jberman: is there a rough timeline on your side of the integration for FCMPs? (excluding review time)     

> __< jberman >__ 4-6 months on my end     

> __< v​tnerd:monero.social >__ Is the addressing change/work a re-computation for sending only? Meaning calculating received funds and spent funds will not change?     

> __< rbrunner >__ I for one don't see anybody pressuring kayabanerve into fast snappy answers, and if he fails to come up with them, he will have lost :)     

> __< k​ayabanerve:monero.social >__ There is no address change proposed with FCMPs.     

> __< k​ayabanerve:monero.social >__ Old addresses won't have OVKs and F-S. Newly generated wallets will.     

> __< k​ayabanerve:monero.social >__ (if implemented. Implementation isn't required for full set privacy alone)     

> __< v​tnerd:monero.social >__ Ok, are you still adding view balance key to FCMP proposal? I'm eyeballing LWS changes needed     

> __< k​ayabanerve:monero.social >__ That means finding received works as it prior did.     

> __< j​effro256:monero.social >__ I probably need to clarify, I'm not entirely opposed to do FCMP-RCT. I'm biased towards Seraphis obviously, but I'm okay with ONLY doing FCMP-RCT, especially since feature parity seems to be achieved. But what is unacceptable to me is trying to do both for numerous reasons related to health of future Monero Core code     

> __< k​ayabanerve:monero.social >__ New wallets would be able to output an outgoing view key to calculate key images. I believe that's view balance     

> __< rbrunner >__ Maybe it would simplify things for the discussion if anything beyond pure FCMP-RCT is left out for the time being. Things like OVK and F-S on top of that.     

> __< rbrunner >__ I understand those are not really essential to the proposal.     

> __< rbrunner >__ Things can fly already without them.     

> __< v​tnerd:monero.social >__ yes, the view key currently cannot compute key images, so LWS only knows "candidate" spends. Sounds like I may need a slight LWS update for this     

> __< jberman >__ adding the OVK scheme to wallets would add maybe 1-2mo+ to the 4-6mo estimate     

> __< k​ayabanerve:monero.social >__ I also don't want to be rude and propose we get rid of Seraphis. If jeffro256 wants to discuss one or the other, I'll say it's feature complete with Seraphis, on a potentially quicker timeline, with much more incremental changes and no migration.     

> __< k​ayabanerve:monero.social >__ rbrunner: It is for jeffro who wants to discuss one or the other.     

> __< jberman >__ my main disagreement with the post is the implication that funds are either-or for this or Seraphis     

> __< k​ayabanerve:monero.social >__ @jberman Though that can be done outside any hard fork. It's purely wallet side.     

> __< jberman >__ I've seen no reason to suggest this would be the case, I think Seraphis will have no problem getting the funds it needs either     

> __< jberman >__ The most significant impact on current dev resources for Seraphis I think is that it would pull me away from coding on Seraphis     

> __< j​effro256:monero.social >__ jberman:  I don't think thats true for funds, but could be true for current usable manpower     

> __< rbrunner >__ If anything, people may find it easier to compromise on a FCMP+RCT proposal that is as small as possible     

> __< k​ayabanerve:monero.social >__ I disagree with that premise as well, and it's why I've been trying to move forward this CCS which is largely reusable for Seraphis. It isn't explicitly one or the other.     

> __< jberman >__ I also disagree about the relative importance of FCMPs, I personally see it as priority #1 even assuming black marble attacks don't matter, strictly for EAE     

> __< j​effro256:monero.social >__ Like a lot of R&D/charity/etc, Monero community has shown it has deeper pockets than the people that are physically able to enact the change     

> __< jberman >__ so I don't think I will be convinced to not work on it     

> __< k​ayabanerve:monero.social >__ rbrunner: RingCT and Seraphis have different first layers in the circuit. I would have to pick one.     

> __< rbrunner >__ A bit unfortunate that my "crypto" knowledge is not sufficient to understand that ...     

> __< k​ayabanerve:monero.social >__ I see removing rings and F-S as our only first priority with literally everything else secondary, so long as it meets setup (trustless)/performance requirements.     

> __< rbrunner >__ I as assuming a clear and reasonable path first to FCMP+RCT and then Seraphis+FCMP is possible     

> __< rbrunner >__ *I was     

> __< k​ayabanerve:monero.social >__ Ignoring the tech debt concerns, the work for the former covers most of the latter.     

> __< rbrunner >__ Is this a "yes" to my assumption? Sorry, I am not sure     

> __< k​ayabanerve:monero.social >__ Pretty much     

> __< rbrunner >__ Ok, thanks :)     

> __< rbrunner >__ So we could make it as small as possible, and look at OVK and F-S and possibly other things only later     

> __< k​ayabanerve:monero.social >__ The CCS is so small. The initial deployment proposed is so small.     

> __< rbrunner >__ You said it wonderfully, that we are swimming in a veritable sea of options. This makes it difficult, no?     

> __< k​ayabanerve:monero.social >__ So we don't need to make it as small as possible because I already did that to minimize contention :/     

> __< plowsof >__ :D     

> __< rbrunner >__ It would help at least me to leave out any mention of stuff like OVK, F-S and whatnot *for the time being*     

> __< rbrunner >__ Everything is so complicated and multifacted already without that stuff.     

> __< rbrunner >__ Just saying :)     

> __< j​effro256:monero.social >__ Idk if it's helpful to leave out, unfortunately, because Seraphis will 100% add those things in the key migration     

> __< j​effro256:monero.social >__ FCMP-RCT can do it incrementally, though     

> __< k​ayabanerve:monero.social >__ It's the potential path forward after and notes the benefits of this work, even if not realized yet.     

> __< j​effro256:monero.social >__ ^^^     

> __< k​ayabanerve:monero.social >__ So yes, it's simpler to leave out but less fair to the proposal.     

> __< rbrunner >__ Now I am totally confused. I hope that's only a temporary state.     

> __< j​effro256:monero.social >__ Tbh, I wouldn't really consider FCMP-RCT over Seraphis for the network if those things weren't possible at some point in the future     

> __< k​ayabanerve:monero.social >__ And jeffro will only consider FCMP-RCT if over Seraphis.     

> __< r​euben:firo.org >__ jeffro256: any particular reason why ?     

> __< k​ayabanerve:monero.social >__ rbrunner: do you want to buy a computer with 8 GB of RAM soldered in, or upgradeable to 32 GB?     

> __< rbrunner >__ Well, if everything goes as planned, Seraphis will arrive in a reasonable timeframe, to the rescue. Thinking positively     

> __< k​ayabanerve:monero.social >__ My CCS is for 8 GB. I am noting the option for 32 GB in the future as my due diligence because that's a notable feature.     

> __< j​effro256:monero.social >__ Because then assuming we want those things, we would have to do another non-trivial network upgrade to get them. Seraphis already does that, so we should go with that instead.     

> __< k​ayabanerve:monero.social >__ Though, to be fair, that assumes Seraphis is better.     

> __< r​euben:firo.org >__ If feature parity though why bother with Seraphis?     

> __< r​euben:firo.org >__ Iirc it would only be marginally better     

> __< k​ayabanerve:monero.social >__ Migration     

> __< k​ayabanerve:monero.social >__ Incremental, with more immediate benefits and no new anonset     

> __< j​effro256:monero.social >__ That's the point up for debate     

> __< k​ayabanerve:monero.social >__ Seraphis is a simpler design in theory that could lead to as much as... ~25% faster membership proofs, at the cost of ~six hundred bytes in bandwidth?     

> __< rbrunner >__ I think you have to look at some things that are details, but maybe important details     

> __< k​ayabanerve:monero.social >__ Seraphis, with squashed enotes, does a range proof on inputs. This doesn't squash so it doesn't.     

> __< rbrunner >__ And, to say it again, Seraphis is *implemented*. It's existing code. 1.5 man years went into that, remember?     

> __< k​ayabanerve:monero.social >__ Seraphis could not squash. Due to padding rules, I don't think that shaves the necessary power of 2 to have a faster membership proof at this time.     

> __< k​ayabanerve:monero.social >__ So there's a bandwidth/computation trade off to discuss.     

> __< r​euben:firo.org >__ Best not to consider that since it might be a sunk cost fallacy though I guess FCMP-RCT might have unknown roadblocks     

> __< k​ayabanerve:monero.social >__ Hence why I didn't want to have this discussion, though I'll note the remaining work on Seraphis is still taking longer than estimates for the initial improvements here *and they're not incompatible*.     

> __< k​ayabanerve:monero.social >__ They're only incompatible if you refuse a year of full sender privacy for less tech debt :/     

> __< rbrunner >__ I really wonder how timelines will develop. If you ask me, and that is maybe a bit unfair as a comment, your journey until hardfork may take twice as long as currently estimated     

> __< k​ayabanerve:monero.social >__ It could.     

> __< rbrunner >__ (That's about on par with estimates that Seraphis may be 5 years out)     

> __< k​ayabanerve:monero.social >__ I prefer the 1.5-3y estimate, and .5-1y for FCMPs.     

> __< j​effro256:monero.social >__ Basically. Again, I'm willing to be a complete dick about this ("either this or that") since I personally highly value protocol and library simplicity for practical adoption and decentralization reasons     

> __< j​effro256:monero.social >__ But my affinity for certain protocol design over full sender privacy is subjective     

> __< k​ayabanerve:monero.social >__ I care about Monero's privacy not being as arguable as plausible deniability and not being a honeypot of historical data for QCs to deanon.     

> __< plowsof >__ No input from koe on this yet?      

> __< rbrunner >__ Not that I know of.     

> __< k​ayabanerve:monero.social >__ I also appreciate the lack of an explicit migration, yet I can concede the Seraphis design's benefit in theory.     

> __< plowsof >__ He doesnt want to learn rust iirc :)      

> __< r​euben:firo.org >__ For FCMPs, what state are the circuit designs ?     

> __< rbrunner >__ Yeah, but I don't think that any substantial implementation work is in his future     

> __< a​lex:agoradesk.com >__ Is there a necessity to commit to the upgradable RAM now, or can we wait until FCMPs are in the protocol (to see how long it takes in actuality and whether Seraphis really is unnecessary) kayabanerve ?     

> __< j​effro256:monero.social >__ I've been working on it some, and I'm pretty sure we *can* migrate without changing addresses or having non-mixed anon sets within inputs, assuming we don't switch curves.     

> __< k​ayabanerve:monero.social >__ That's not how it works.     

> __< k​ayabanerve:monero.social >__ It inherently has upgradeable RAM. The entire point is we don't need to commit to the upgrade.     

> __< rbrunner >__ Just remember, if we ditch Seraphis now, that would already be the second protocol we murder :)     

> __< k​ayabanerve:monero.social >__ @jeffro256 You'd need to break HW wallet support, always have a dummy input output by membership over the historical set (literally the work I'm proposing now) which would be expensive, or solve the dlog problem AFAIK.     

> __< a​lex:agoradesk.com >__ In that case talking about discarding seraphis now is a bit early, since we still haven't gotten to the decision point, which will only be relevant after FCMP is in the chain, right? And at that point we'll have more information to guide the decision.     

> __< rbrunner >__ It's a bit unfortunate then that we would have to continue to work on Seraphis, or we would not have that available within a reasonable time     

> __< a​lex:agoradesk.com >__ Seraphis's time is way beyond reasonable even with the current workforce, which is why kaya's FCMP's are so attractive.     

> __< rbrunner >__ I mean, we can talk about FCMP+RCT yes or no, but if we really consider to throw away Seraphis completely, you lost me     

> __< jberman >__ my take on this general discussion: I don't see cold water on kayabaNerve's R&D proposal, I only see cold water on potentially merging FCMP-RCT before Seraphis     

> __< a​lex:agoradesk.com >__ Seraphis being "two years away" is almost a meme at this point.     

> __< j​effro256:monero.social >__ AFAIK (haven't looked into the specific details for FCMPs on Seraphis), but for a general, abstract membership proof, it would only be an extra point addition per legacy enote     

> __< jberman >__ Considering the potential for FCMP-RCT to offer the same feature set as Seraphis (minus a lot of JAMTIS), or the potential for the academic work to fall through, or considering a large number of unknowns, the nature of this discussion can change materially with more information     

> __< jberman >__ This is information which kaybaNerve's R&D proposal will yield, so I think we can take this one step at a time so as to not get bogged down, and move forward with the proposal as is     

> __< j​effro256:monero.social >__ rbrunner7: TBF tryptych was insecure     

> __< rbrunner >__ "Seraphis being "two years away" is almost a meme at this point." Absolutely brilliant.     

> __< k​ayabanerve:monero.social >__ Thank you @jberman.     

> __< k​ayabanerve:monero.social >__ The CCS proposal is upgradeable, not upgraded. Most of the work carries. It also only would take jberman, exept it wouldn't because they're doing a separate CCS.     

> __< k​ayabanerve:monero.social >__ I don't want to argue this for weeks/months and just want to do something, before this becomes 8-14m and then 12-18 and then Seraphis is here so no need.     

> __< rbrunner >__ Now, looking at the time, we may be more or less forced to continue next week.     

> __< j​effro256:monero.social >__ Also this FCMP-RCT  work is "breaking HW support" (making tx construction not backwards compatible) anyways, yeah? Since HW wallets are doing different ownership proofs     

> __< k​ayabanerve:monero.social >__ @jeffro256 Do you have explicit issues with the CCS?     

> __< k​ayabanerve:monero.social >__ It doesn't do the circuit on device. They need an update, but tjey can do the new proof.     

> __< j​effro256:monero.social >__ I think it was edited since I looked at it last, but I definitely don't have problems at the moment with *research* which largely overlaps with Seraphis     

> __< k​ayabanerve:monero.social >__ If you add 1 as the denominator, you get screwed by the fact they have distinct generators.     

> __< k​ayabanerve:monero.social >__ Normalizing the denominator to generate that generator requires solving the dlog of the key image generator and the Seraphis generator used.     

> __< k​ayabanerve:monero.social >__ It's also development, yet the only development in CCS which would go unused is Helios/Selene, the GSP, and the first layer. The GBPs and gadgets, most of the work, carry.     

> __< k​ayabanerve:monero.social >__ And circling back to my prior comments, unless you can actually provide the math, I simply don't believe you UNLESS it's not for a generalized membership proof.     

> __< k​ayabanerve:monero.social >__ It does become much easier if you keep rings for historical outputs.     

> __< j​effro256:monero.social >__ Even Helios/Selene development can overlap, yeah? Also GSP can overlap if we replace the composition proof in Seraphis, right?     

> __< k​ayabanerve:monero.social >__ Only if Seraphis doesn't switch curves yet then you likely lose some of the performance you want to claim. The impact of that is unknown.     

> __< k​ayabanerve:monero.social >__ Yes re: GSPs.     

> __< j​effro256:monero.social >__ So yeah, all that considered (will need to read fine details again), I'm not opposed to the CCS     

> __< k​ayabanerve:monero.social >__ To be clear, Helios/Selene were chosen to contain 2**255-19. That limits our candidates and makes us pick the best of the candidates. Removing that requirement adds more candidates, some presumably better.     

> __< k​ayabanerve:monero.social >__ Then the squashed enote model may offer more efficient membership yet costs additional range proofs on inputs, adding hundreds of bytes (though sorry, my bad, those can be aggregated with output range proofs for no bandwidth increase. Just some of that perf taken back)     

> __< j​effro256:monero.social >__ You're right about this: burden of proof is on me for this point     

> __< k​ayabanerve:monero.social >__ Happy to hear. cc @plowsof and I'll find the others who were pausing prior to hearing you out.     

> __< k​ayabanerve:monero.social >__ I'd be extremely interested in it. The distinct generators makes me believe it'd be my circuit, and all the debt/performance of it, to full set privacy migrate RCT to Seraphis (and you'd also need a dummy Seraphis input).     

> __< r​ucknium:monero.social >__ kayabanerve: Do you have more details on the possible who and when for the code audits and mathematics proofs reviews?     

> __< k​ayabanerve:monero.social >__ I met with Veridise, who implemented multiple formal verification tools for ZK circuits. I've discussed with them both gadget proving and a soundness proof for divisors.     

> __< k​ayabanerve:monero.social >__ I'll also circle back with CS on the latter *once the protocol is explicitly defined*.     

> __< k​ayabanerve:monero.social >__ As Diego prior declined the work, yet I believe due to Aaron believing its to vague to discuss.     

> __< k​ayabanerve:monero.social >__ Then jberman also talked with auditors, and I was recommended one.     

> __< r​ucknium:monero.social >__ That's formal verification from Veridise for the code, not the mathematics, right?     

> __< k​ayabanerve:monero.social >__ No. Of the circuit itself.     

> __< k​ayabanerve:monero.social >__ We'd distinctly audit the implementation matches.     

> __< k​ayabanerve:monero.social >__ (Though the verified specification can be read into the code and then we just ensure the parser lines up)     

> __< k​ayabanerve:monero.social >__ Even I may be able to do the formal verification to be honest. It depends on if the verifiers model challenges, as proposed for use here.     

> __< k​ayabanerve:monero.social >__ Set membership is dead simple. It's literally that the product of set_member_i - claimed member is 0. That's only true if one factor is 0, which is only true if the member is equivalent to the claimed member (when over a prime field).     

> __< r​ucknium:monero.social >__ I think we can end the meeting here. We don't need to be in a meeting to discuss FCMP/Seraphis in this channel. Feel free to discuss here when needed.     

> __< v​tnerd:monero.social >__ Since I missed my status above: still working on remote account scanning on lws. The protocol has to be revamped but I think the feature is still doable. Will have to run perf tests to verify it actually performs better as a whole     

> __< j​effro256:monero.social >__ Thanks all! Thanks kayabanerve ! The discussion here was very insightful and makes me hopeful for the future of Monero. In reality,  as much as we talk downsides of A vs B, we're deciding between two excellent paths for the future, thanks to a ton of great work by all parties involved     

> __< o​ne-horse-wagon:monero.social >__ Thanks.     

> __< c​haser:monero.social >__ thank you, everyone!     

> __< k​ayabanerve:monero.social >__ Thanks for doing your part for Monero <a data-mention-type="user" href="https://matrix.to/#/@jeffro256:monero.social" contenteditable="false">@jeffro256</a> :)     

> __< j​effro256:monero.social >__ You too :)  

## reuben | 2024-04-18T08:45:30+00:00
hey hello hi,

Might I humbly suggest escaping the mentions from chat logs when posting them on GitHub, to avoid tagging unsuspecting bystanders? You can do that by wrapping mentions in code formatting e.g. `@reuben` or including an empty comment in between @ and username (`@<!-- -->reuben`) - @<!-- -->reuben

best,
the other @reuben

# Action History
- Created by: Rucknium | 2024-04-16T21:49:03+00:00
- Closed at: 2024-04-30T17:22:49+00:00
