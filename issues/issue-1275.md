---
title: Monero Research Lab Meeting - Wed 01 October 2025, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1275
author: Rucknium
assignees: []
labels: []
created_at: '2025-09-30T23:26:32+00:00'
updated_at: '2025-10-11T15:51:50+00:00'
type: issue
status: closed
closed_at: '2025-10-11T15:51:50+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/meeting.html?p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3. [Carrot follow-up audit](https://gist.github.com/jeffro256/12f4fcc001058dd1f3fd7e81d6476deb).

4. [FCMP Helios-Selene parameters rigidity](https://gist.github.com/tevador/4524c2092178df08996487d4e272b096?permalink_comment_id=5772654#gistcomment-5772654).

5. [Proof-of-Work-Enabled Relay ("PoWER")](https://github.com/monero-project/research-lab/issues/133).

6. [Transaction volume scaling parameters after FCMP hard fork](https://github.com/ArticMine/Monero-Documents/blob/master/MoneroScaling2025-07.pdf). [Revisit FCMP++ transaction weight function](https://github.com/seraphis-migration/monero/issues/44).

7. [FCMP alpha stressnet planning](https://github.com/seraphis-migration/monero/issues/53#issuecomment-3053493262).

8. Mining pool centralization: [Temporary rolling DNS checkpoints](https://github.com/monero-project/monero/issues/10064), [Share or Perish](https://github.com/monero-project/research-lab/issues/146), and [Lucky transactions](https://github.com/monero-project/research-lab/issues/145).

9. Any other business

Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#1272 

# Discussion History
## Rucknium | 2025-10-07T22:56:27+00:00
Logs

> __< rucknium >__ Meeting time! https://github.com/monero-project/meta/issues/1275     

> __< rucknium >__ 1. Greetings     

> __< tevador >__ Hi     

> __< rbrunner >__ Hello     

> __< plowsof >__ 👋     

> __< spackle >__ hi     

> __< rucknium >__ ping jeffro256:monero.social     

> __< jeffro256 >__ Howdy     

> __< rucknium >__ 2. Updates. What is everyone working on?     

> __< tevador >__ me: Helios and Selene updates and Share or Perish.     

> __< jberman >__ waves     

> __< jeffro256 >__ Me: polishing and testing Carrot Rust library, preparing for alpha stressnet, reviewing FCMP++ code      

> __< rucknium >__ me: Wrote an explainer about the 18-block reorg: https://rucknium.me/posts/monero-18-block-reorg/ . Thanks for anhdres for creating all the diagrams and jeffro256 and DataHoarder for reviewing early drafts. Set up performance visualizer for stressnet: https://stressnetnode1.moneronet.info/ (another node at stressnetnode2). Rel [... too long, see https://mrelay.p2pool.observer/e/yejs0boKNUV4QW5U ]     

> __< jberman >__ me: alpha stressnet debugging, submitted some piecemeal crypto PR's used in the FCMP++ integration to the main monero repo     

> __< rucknium >__ 3. Carrot follow-up audit (https://gist.github.com/jeffro256/12f4fcc001058dd1f3fd7e81d6476deb).     

> __< DataHoarder >__ me: awaiting fixes on monero for checkpoints / checkpointer further testing; also reproducing carrot / FCMP generators on go code     

> __< jberman >__ (nice issue with the generators spotted DataHoarder )     

> __< jeffro256 >__ Cypherstack responded to the follow-up audit request with the following deliverables: https://github.com/jeffro256/carrot/blob/master/audits/Cypherstack-v2.0-followup.pdf and https://github.com/jeffro256/carrot/blob/master/audits/Cypherstack-diagram.pdf     

> __< jeffro256 >__ The dependency diagram is much appreciated and may help readers understand the flow of enote construction much better      

> __< jeffro256 >__ TLDR; The Cypherstack follow-up result was generally positive, but encouraged documenting and implemting additional checks for robustness's sake where it does not greatly affect performance      

> __< jberman >__ this diagram is very nice     

> __< vtnerd >__ Me: got view balance keys tested and working in lws, just need to test outgoing spends as they are tracked differently internally      

> __< jeffro256 >__ Thanks to Cypherstack for this effort!!     

> __< rucknium >__ Yes, thank you. More to discuss on this now, or should we wait until people have more time to review the materials?     

> __< jeffro256 >__ That's it for now      

> __< rucknium >__ 4. FCMP Helios-Selene parameters rigidity (https://gist.github.com/tevador/4524c2092178df08996487d4e272b096?permalink_comment_id=5772654#gistcomment-5772654).     

> __< tevador >__ It has been decided to use D = -31750123 instead of the current value. I'm in the process of updating the gist.     

> __< jeffro256 >__ I can't remember, does this affect the Crandall reduction technique or is it mostly a drop-in change for the parameters?     

> __< tevador >__ Should be a drop-in change I think.     

> __< tevador >__ For Crandall, only some parameters need to be changed. The algorithm will work the same way as the new prime has the same basic properties.     

> __< rbrunner >__ kayabanerve in Monday's meeting: " No, it'll be trivial. Just updating constants in Rust, and the ones duplicated in C++ by jeffro256 if any exist."     

> __< rucknium >__ Anything more to discuss on this item?     

> __< rucknium >__ 5. Proof-of-Work-Enabled Relay ("PoWER") (https://github.com/monero-project/research-lab/issues/133).     

> __< jeffro256 >__ Maybe I can bring it up after the meeting as its slightly offtopic for this item, but I'd like to ask tevador where he/she currently stands on the double hash-to-point      

> __< jeffro256 >__ hinto:monero.social     

> __< jberman >__ (jeffro is referring to this issue: https://github.com/monero-project/research-lab/issues/142)     

> __< articmine >__ Sorry I am late      

> __< tevador >__ I'm quite OK with it since kayabanerve clarified the security implications.     

> __< jeffro256 >__ W.r.t collision resistance specifically?     

> __< tevador >__ Yes. FCMP++ relies on the collision resistance of Hp, while RCT does not.     

> __< jberman >__ I don't have anything to add on PoWER rn. The status is there are some disagreements over design decisions that we discussed at length last week. We decided at the end that it seems ok for hinto to proceed with the currently proposed design on the PoWER issue, seeking to minimize complexity and we can review that impl     

> __< jberman >__ jeffro256:monero.social: have you budged at all on the issue (per connection vs per txs)?     

> __< boog900 >__ Something I think needs to be mentioned is PoW would need to be opt out when done per connection      

> __< boog900 >__ Otherwise we risk the tx getting stuck      

> __< boog900 >__ And it could still get stuck if too many opt out      

> __< rucknium >__ Gossip networks are very fault-tolerant.     

> __< articmine >__ I see PoWER for large transactions as a necessary evil until we address parallel processing of verification time.     

> __< boog900 >__ I would support making pow mandatory for all tx relay connections though      

> __< boog900 >__ Not just for only txs with more than 8 inputs      

> __< articmine >__ I strongly disagree      

> __< rucknium >__ But maybe we don't want to have an empirical test of how fault-tolerant they are on mainnet 😅     

> __< jberman >__ boog900: I would support that for p2p connections, and not for RPC connections     

> __< boog900 >__ yeah     

> __< jeffro256 >__ boog900: What do you mean by making it mandatory for all tx relay connections but also opt-out ?     

> __< articmine >__ PoWER makes those who live in the global south second class users of Miner. Just based upon climate      

> __< boog900 >__ jeffro256: you can opt out but you can no longer send tx pool txs to nodes      

> __< articmine >__ Second class users of Monero      

> __< boog900 >__ you can ony receive txs and send/receive blocks       

> __< jeffro256 >__ Ah gotcha. So similar to Bitcoin's distinction between tx relay connections and block relay connections ?     

> __< jberman >__ articmine:monero.social: the PoW used in PoWER is going to be as CPU intensive as verifying a single large input tx. This has been repeated x1000 times     

> __< jeffro256 >__ jberman: I think I'm now less opposed to per-connection if an implementation can be done elegantly      

> __< boog900 >__ jeffro256: yeah      

> __< articmine >__ It is still a burden for someone to send a 2 in 2 out tx in +40 C weather      

> __< articmine >__ Especially now that this is proposed for all transactions      

> __< jberman >__ 2 in 2 out tx takes more CPU to construct than the CPU to construct this PoW (!!!!!!!!!!!!!!!!!!!!!!!!!!!!!)     

> __< boog900 >__ 1. they can use RPC     

> __< boog900 >__ 2. ^     

> __< articmine >__ Per input      

> __< hinto >__ hello, I don't have any inputs for the design, mostly worried about complexity and hacky interfaces      

> __< articmine >__ RPC to a node in the first world     

> __< boog900 >__ a node in the rest of the world isn't going to suffer from the extra 0.01% CPU load      

> __< articmine >__ If you force this on all transactions it is way more than .01%     

> __< boog900 >__ no its forced on connections who want to send txs, its still 1 per connection      

> __< jberman >__ The CPU to scan the chain is like 99.9% more intensive than the CPU for this PoW     

> __< articmine >__ So you double the verification time      

> __< articmine >__ Cost     

> __< articmine >__ To send transactions      

> __< boog900 >__ articmine: no verifying the PoW only happens on a handshake not when a tx is sent     

> __< jeffro256 >__ jberman: s/%/x perhaps? ;)     

> __< articmine >__ I know, but now it is forced to send     

> __< jberman >__ jeffro256: haha yes     

> __< boog900 >__ articmine: no its forced if you want to run your own node      

> __< articmine >__ Correct      

> __< boog900 >__ which takes wayyyyyy more CPU      

> __< jberman >__ I propose we move on from this discussion. Rehashing the same points x1000     

> __< hinto >__ jeffro256:monero.social: to respond to last week, I won't do wallet changes > <jeffro256> I see the argument, I don't know if I'm entirely convinced, but yeah I can definitely start on that wallet API point      

> __< boog900 >__ articmine: would you rather these non first world nodes be spammed with txs that take wayy longer to verify than PoW     

> __< articmine >__ So we are back to the 2017 mess?     

> __< articmine >__ boog900: I would prefer the verification time issues be addressed with parallel processing     

> __< rucknium >__ There's stressnet to discuss still and selfish mining mitigations.     

> __< articmine >__ Then the impact of any spam is drastically reduced      

> __< rucknium >__ 6. Transaction volume scaling parameters after FCMP hard fork (https://github.com/ArticMine/Monero-Documents/blob/master/MoneroScaling2025-07.pdf). Revisit FCMP++ transaction weight function (https://github.com/seraphis-migration/monero/issues/44).     

> __< rucknium >__ I will limit discussion of this item to 30 minutes, if there are no objections.     

> __< articmine >__ hinto: My comment     

> __< jeffro256 >__ articmine: I also want to move on, but for the record, parallel processing does nothing to mitigate the issue of invalid proof verification DoS      

> __< articmine >__ There is no need to limit discussion on this      

> __< articmine >__ I have nothing to add     

> __< rucknium >__ articmine:monero.social objected to the 30 minutes limit on this item, so it is open.     

> __< jberman >__ I haven't had a chance to review the latest yet in depth     

> __< rucknium >__ 7. FCMP alpha stressnet planning (https://github.com/seraphis-migration/monero/issues/53#issuecomment-3053493262).     

> __< jeffro256 >__ Me neither, will look soon     

> __< jberman >__ Alpha stressnet v1 launched :) we've had a few bugs which I'll talk about, and after this meeting will tag a v2 release fixing them     

> __< jberman >__ Bug 1: windows / 32-bit machines couldn't sync as a result of using an unsigned long in a crypto function and expecting it to be 64 bits, issue first reported by mayhem69, fixed here: https://github.com/seraphis-migration/monero/pull/118     

> __< rucknium >__ Stressnet's hard fork from testnet will happen Friday.     

> __< rucknium >__ The launch announcement is https://monero.town/post/6763165     

> __< jberman >__ Prior to the above bug being identified, I had opened a PR to master implementing that crypto function (and the same bug was present there): https://github.com/monero-project/monero/pull/10108     

> __< jberman >__ My general thoughts: I would like to have the crypto changes included for the FCMP++ integration audited. I'm thinking about best plan for that, thinking about pointing to snippets of isolated code for an audit     

> __< rucknium >__ This was a problem in the unaudited code that bridges the Rust FCMP and the monerod C++?     

> __< jberman >__ This in particular was in unaudited code that speeds up a function that's currently in use in monerod     

> __< jberman >__ It's more relevant for the FCMP++ integration (and was more important to speed up for the integration), because it's now called for all coinbase outputs (and transparent amounts) during wallet sync and daemon sync     

> __< jberman >__ Daemon sync currently calls this function for coinbase outputs     

> __< jberman >__ and some RPC's use it     

> __< jberman >__ Bug 2: CLI transfer/sweep pre-fork was borked (also reported by mayhem69), fixed here: https://github.com/seraphis-migration/monero/pull/122     

> __< rucknium >__ Should this be an agenda item next week or open the discussion now? > <jberman> My general thoughts: I would like to have the crypto changes included for the FCMP++ integration audited. I'm thinking about best plan for that, thinking about pointing to snippets of isolated code for an audit     

> __< jberman >__ We can make it an agenda item for next week, I'll come with a fleshed out plan     

> __< jberman >__ Bug 3: borked debug builds reproducing generators incorrectly (reported by datahoarder:monero.social ), fixed here: https://github.com/seraphis-migration/monero/pull/124     

> __< jberman >__ That's all the bugs reported so far (and then a small display logging issue during the migration by ofrnxmr:monero.social which will get to)     

> __< rucknium >__ IMHO, it was amazing to see the compiler pause the C++ compilation to compile the Rust FCMP and then follow the progress of the FCMP tree building the database. The result of a huge amount of work by many people 🧡     

> __< DataHoarder >__ ^ I noticed the rust compilation messages as I was compiling monero and had to do a double take :)     

> __< rucknium >__ I set up stressnet node monitors at https://stressnetnode1.moneronet.info/ and https://stressnetnode2.moneronet.info/ . Not much to see now since there's nothing happening on testnet, but it will come alive once the stressnet forks off.     

> __< rucknium >__ The stressnet discussion room is at #monero-stressnet:monero.social  and ##monero-stressnet on Libera IRC, IIRC.     

> __< DataHoarder >__ on the note of updating carrot document to match: please define what H_p^1/H_p^2/H_p^3 or desired notation actually correspond in code (or pseudocode) as from the document alone it was unclear     

> __< jeffro256 >__ Will do     

> __< rucknium >__ I released my xmrspammer package so that other users could produce spam: https://github.com/Rucknium/xmrspammer . IMHO, it's usable, but only lightly tested. Wait until after the stressnet fork to try it!     

> __< rucknium >__ The plan is still to have a bigger stressnet after this alpha one, right?     

> __< DataHoarder >__ also, if you end up seeing blocks with merge mining in FCMP++ stressnet- that means I got some p2pool-like setup to mine there as a bonus work :)     

> __< rucknium >__ Somehow it needs to be communicated that if people want to participate in only one stressnet, they should participate in the second one.     

> __< jeffro256 >__ rucknium: Ideally, yes      

> __< rucknium >__ IMHO, it would be a good idea to do a double fork for that one. One fork to fork off testnet, but normal RingCT rules. Then spam for a few days. Then fork to FCMP rules. It's not an experiment if there's no control 😉     

> __< rucknium >__ Anything else about stressnet?     

> __< rucknium >__ 8.  Mining pool centralization: Temporary rolling DNS checkpoints (https://github.com/monero-project/monero/issues/10064), Share or Perish (https://github.com/monero-project/research-lab/issues/146), and Lucky transactions (https://github.com/monero-project/research-lab/issues/145).     

> __< rucknium >__ ofrnxmr:monero.social and 0xfffc:monero.social  are trying to fix a rare bug that can halt block sync when rolling checkpoint enforcing is activated.     

> __< rucknium >__ Qubic hasn't attempted selfish mining in a week or more and their hashpower is lower now.     

> __< rbrunner >__ Good if we really are down to rare bugs :)     

> __< rucknium >__ Like I said in updates, I wrote this blog post about the 18-block reorg, aimed at the general Monero community member: https://rucknium.me/posts/monero-18-block-reorg/     

> __< rucknium >__ I think the post finally explains the purpose of the 10-block lock in understandable terms, just in time for rings to get deprecated 😆     

> __< rucknium >__ But FCMP txs will have a similar issue. The exact mechanism is different.     

> __< DataHoarder >__ something like the 19th-21st is when they did the last selfish attempts (minor)     

> __< rucknium >__ Discuss Share or Perish? https://github.com/monero-project/research-lab/issues/146     

> __< tevador >__ FCMP txs are even more fragile when it comes to 10+ block reorgs     

> __< tevador >__ Any questions or comments about SoP?     

> __< rucknium >__ tevador: Right. I discuss that at the end of the 20-minute post :)     

> __< DataHoarder >__ on the topic of the reorg, you can visualize their rings in blocks tool https://blocks.p2pool.observer/tx/d3e574c05b01f5d74815e3894f55e1645f402cdbf0415877f49e752a71b0d376/c46ae7df060e45f6ac40f1340264f8b61267c84bf52e43d2b0ac3155a75f3380/9489923b1773c2575e3320b84357e451b2dc625ba1cb9d2f4d6c352689c5ac7d     

> __< rucknium >__ Soon I will dig into this and try to set up the Markov Decision Process analyzer for SoP. Now I am focused on helping get stressnet stressed.     

> __< jberman >__ SoP seems the most promising proposal to me so far     

> __< rbrunner >__ For some long-time solution, right?     

> __< tevador >__ It's a good long-term solution for attackers <50%.     

> __< jberman >__ Yes     

> __< jberman >__ ^     

> __< tevador >__ >50% would need the Finality layer or Lucky transactions     

> __< rbrunner >__ I see     

> __< rbrunner >__ So not directly comparable     

> __< tevador >__ It's close to the best you can do with PoW only and a soft fork.     

> __< venture >__ Hi. SoP doesn't require a consensus change or hardfork correct? "Just" gossip protocol to account for shares and miner's tip selection change?     

> __< rucknium >__ IMHO, it would be a good idea to evaluate Monero's Difficulty Adjustment Algorithm (DAA) and alternatives for next hard fork. That doesn't fix selfish mining, but it could help a little. And controversial proposal: I think setting minimum tx fee based on network hashpower could be researched so that min fee stays roughly the s [... too long, see https://mrelay.p2pool.observer/e/pN-f1LoKbTc5UDNo ]     

> __< bawdyanarchist:matrix.org >__ Difficulty adjustment is definitely a factor in selfish mining attacks     

> __< rbrunner >__ Uh, a new can of worms :)     

> __< tevador >__ The first step towards a better DAA would be to enforce strictly increasing block timestamps.     

> __< DataHoarder >__ sorry, bridge went down midway, should come back up and removed offending line     

> __< jberman >__ tevador: seems a simple rule to include for next hard fork     

> __< rucknium >__ Need to resend this message to IRC: The debate about setting min relay fee higher or lower based on unpredictable changes in Monero's exchange rate could be solved by basing min fee on hashpower changes, IMHO.     

> __< jberman >__ I think tying min fee to network hashpower is a valid research avenue and interesting idea     

> __< radanne:matrix.org >__ Hey folks, just submitted a proposal at https://github.com/monero-project/research-lab/issues/147, wishing you all happy reading, and looking forward to some feedback🙏 I hope it's all self-explanatory, as I may be somewhat scarce until the 19th, so my responses may not be instant, but I'll keep an eye on the Git page and he [... too long, see https://mrelay.p2pool.observer/e/lKnM1LoKeC1Oa2xH ]     

> __< tevador >__ Updated Helios and Selene gist with the hopefully final set of parameters: https://gist.github.com/tevador/4524c2092178df08996487d4e272b096     

> __< tevador >__ The new search conditions are G4 and C3. G4 gives us a green checkmark and C3 gives us nice base points.     

> __< tevador >__ s/G4/Q4     

> __< sgp_ >__ ty tevador!     

> __< sgp_ >__ for PoP, if an attacker has >50% for a single day, they could very likely cause >10 block reorgs over that 1 day time period right? Just to further establish a remaining risk     

> __< venture >__ *SoP you probably mean. And yes. But I see it more as a feature than a risk compared to a PoS finality layer in which malicious behaviour is much harder to detect. The definition of "malicious" is also more subjective in PoS imho. Imagine a 34% / 66% split on consensus.      

> __< sgp_ >__ Sure, I only mean to say that the risk remains. I consider short-term instances of 50%+ hashrate to be unfortunately realistic     


# Action History
- Created by: Rucknium | 2025-09-30T23:26:32+00:00
- Closed at: 2025-10-11T15:51:50+00:00
