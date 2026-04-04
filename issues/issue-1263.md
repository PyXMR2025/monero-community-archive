---
title: Monero Research Lab Meeting - Wed 03 September 2025, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1263
author: Rucknium
assignees: []
labels: []
created_at: '2025-09-02T23:53:53+00:00'
updated_at: '2025-09-12T20:00:17+00:00'
type: issue
status: closed
closed_at: '2025-09-12T20:00:17+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/meeting.html?p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3. [Carrot follow-up audit](https://gist.github.com/jeffro256/12f4fcc001058dd1f3fd7e81d6476deb).

4. [Discussion: Replace Monero's hash-to-point function with the FCMP++ Upgrade](https://github.com/monero-project/research-lab/issues/142).

5. [Transaction volume scaling parameters after FCMP hard fork](https://github.com/ArticMine/Monero-Documents/blob/master/MoneroScaling2025-07.pdf).

6. [FCMP alpha stressnet planning](https://github.com/seraphis-migration/monero/issues/53#issuecomment-3053493262).

7. Mining pool centralization: [Temporary rolling DNS checkpoints](https://github.com/monero-project/monero/issues/10064) and [Publish or Perish](https://github.com/monero-project/research-lab/issues/144).

8. Any other business

Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#1261 

# Discussion History
## Rucknium | 2025-09-04T21:50:42+00:00
Logs:
```
> __< br-m >__ <rucknium> Meeting time! https://github.com/monero-project/meta/issues/1263     

> __< br-m >__ <rucknium> 1. Greetings     

> __< br-m >__ <articmine> Hi     

> __< rbrunner >__ Hello     

> __< br-m >__ <vtnerd> hi     

> __< br-m >__ <jberman> waves     

> __< br-m >__ <boog900> hi      

> __< br-m >__ <venture> Hello     

> __< br-m >__ <0xfffc> Hi everyone     

> __< ArticMine >__ hi connecting from IRC     

> __< br-m >__ <rucknium> We are probably missing people from matrix.org Matrix servers. Logging into the Libera IRC network still works.     

> __< br-m >__ <rucknium> 2. Updates. What is everyone working on?     

> __< br-m >__ <vtnerd> me: primarily bugs in lws and lwsf. sadly several were reported nearly the same time, and I’ve been going through them     

> __< br-m >__ <rucknium> me: Testing rolling DNS checkpoints and created this issue about it: https://github.com/monero-project/monero/issues/10064  . Reading papers about selfish mining. Productionizing transaction spamming code for FCMP alpha stressnet.     

> __< DataHoarder >__ me: For fun implemented a  DNS + DNSSEC server that can server a single DNS checkpointing domain directly, via nameserver delegation https://git.gammaspectra.live/P2Pool/monero-highway and holding own keys. Supports Ed25519/ECDSA and other keys     

> __< br-m >__ <rucknium> jeffro256: Ping     

> __< br-m >__ <jberman> me: sped up popping blocks/reorg handling in the wallet to handle trimming the fcmp++ tree quickly, fixed a bug in the wallet's tree builder path member reference counter, benchmarked tx and membership proof verification using kayaba's latest     

> __< br-m >__ <jeffro256> Howdy     

> __< br-m >__ <venture> I have been working on a monte carlo simulation of Publish-Or-Perish     

> __< br-m >__ <rucknium> 3. https://gist.github.com/jeffro256/12f4fcc001058dd1f3fd7e81d6476deb.     

> __< br-m >__ <jeffro256> me: lots of review, documenting and refining HW wallet support for FCMP++, and refactoring in preparation of a key image generator hash function change proposed by kayabanerve    

> __< ArticMine >__ I have updated the fee calculations in https://github.com/seraphis-migration/monero/issues/44 With an increase in the penalty free zone, ZM from 1000000 bytes to 200000 bytes, an increase in the reference transaction size from 10000 bytes to 20000 bytes and an increase in fees by 4x by elimination the lo fee in the implementation. Then we can have a flat fee structure with fee proportional to weight up to 128 inputs.      

> __< br-m >__ <jeffro256> diego reached out to me with a first draft of the follow up audit, we're discussing it now. Thanks Cypherstack! Not too much to report until after that's done tho     

> __< br-m >__ <jeffro256> Haven't heard back in a couple days, I wonder if it might have to do with the Matrix federation security issues      

> __< br-m >__ <rucknium> 4. https://github.com/monero-project/research-lab/issues/142.     

> __< br-m >__ <rucknium> 4. https://github.com/monero-project/research-lab/issues/142.     

> __< br-m >__ <rucknium> Do markdown links not appear properly on IRC side, or is it just the monerologs.net parsing that erases the text?     

> __< rbrunner >__ So far no problems for me with the links of today     

> __< br-m >__ <rucknium> Anything to say about hash-to-point now?     

> __< ArticMine >__ In some cases it is lag. I am actually on IRC at the same time     

> __< br-m >__ <articmine> See my comment above     

> __< br-m >__ <rucknium> I am feeling some lag on the Matrix side. Maybe because martix.org is coming back online?     

> __< br-m >__ <rucknium> matrix.org*     

> __< br-m >__ <rucknium> 5. https://github.com/ArticMine/Monero-Documents/blob/master/MoneroScaling2025-07.pdf. https://github.com/seraphis-migration/monero/issues/44     

> __< DataHoarder >__ 19:17:08 <br-m> <rucknium> Do markdown links not appear properly on IRC side, or is it just the monerologs.net parsing that erases the text?     

> __< DataHoarder >__ there is a markdown parser, but it removes the description as I could not find a proper format for it. Let's discuss alternate formats for that after the meeting     

> __< br-m >__ <rucknium> Ok I will post them as regular, separate links for now.     

> __< br-m >__ <rucknium> The current agenda item is "Transaction volume scaling parameters after FCMP hard fork. "     

> __< ArticMine >__ As I mentioned before I am recommending both an increase in the minimum penalty free zone and an increase in fee to address these issues.      

> __< ArticMine >__ this is also after reviewing the comments in the last MRL regarding the use of 4 in transactions     

> __< br-m >__ <jeffro256> Personally, I think that the penalty free zone shouldn't be increased to much over 2x the max tx size + a coinbase tx size. A 6x increase is pretty aggressive when the average FCMP++ transaction isn't going to be 6x the size of a 16-member CLSAG tx. What's the primary thrust of why it would be increased so much ?     

> __< br-m >__ <jberman> My initial read of this latest is that fees are determined entirely by overall tx byte size, and unaffected by tx verif time, or membership proof size/verification (aside from the effect of the memb proof on the overall tx size)     

> __< ArticMine >__ Yes this is correct     

> __< tevador >__ A larger penalty free zone means a malicious miner can spam the blockchain more.     

> __< br-m >__ <jeffro256> ^^^     

> __< ArticMine >__ Yes but there is also an increase in fees     

> __< tevador >__ Fees don't affect the miner.     

> __< br-m >__ <jeffro256> not if colluding with a miner      

> __< ArticMine >__ A penalty free zone 2x the max tx fee was tried in 2017 and it did not work     

> __< ArticMine >__ The fees are just too high     

> __< br-m >__ <jeffro256> Only for max size txs, though, right?     

> __< br-m >__ <jeffro256> Assuming other traffic      

> __< ArticMine >__ in 2017 it was all txs     

> __< ArticMine >__ We had a 2in 2 out tx at 135000 bytes and a penalty free zone of 60000 bytes     

> __< br-m >__ <jeffro256> 2017 was before bulletproofs. I feel like the change to bulletproofs (a huge drop in transaction size) lowered the fees more than the increase in the minimum penalty-free zone     

> __< br-m >__ <jeffro256> But I'm just spitballing      

> __< ArticMine >__ Even after the increase to 300000 bytes fee were still very hihg     

> __< ArticMine >__ It was only by not reducing the penalty free zone after bulletprrof that we go reasonable fees     

> __< br-m >__ <jeffro256> I'm a bit biased because I'm also of the opinion that the fees should be higher than they currently are      

> __< tevador >__ If the tx volume is sufficient, the penalty free zone will adjust. A smaller minimum value is more spam resistant.     

> __< ArticMine >__ I am actually proposing both a fee increase and an increase in the penalty free zone     

> __< ArticMine >__ The current fee structure is very well received by the users. A massive increase in fees is something I cannot support     

> __< br-m >__ <jeffro256> > Even after the increase to 300000 bytes fee were still very hihg     

> __< br-m >__ <jeffro256> > So you agree that increasing the penalty-free zone didn't do much to lower small-tx fees?     

> __< ArticMine >__ It did not go far enough in 2017     

> __< br-m >__ <jeffro256> So if you also want to raise fees, then why are we raising the penalty free zone?      

> __< ArticMine >__ We needed a penalty free zone in the 1000000 - 200000 bytes back then     

> __< ArticMine >__ to 2000000 bytes     

> __< ArticMine >__ We need both      

> __< ArticMine >__ raise fees and the penalty free zone     

> __< br-m >__ <boog900> why do we need it     

> __< tevador >__ What would be the verification time for a 2MB block?     

> __< br-m >__ <rucknium> ofrnxmr: Insight about that ^ with FCMP private testnet experiments?     

> __< ArticMine >__ ~12.5x that of a 128 input tx      

> __< ArticMine >__ we have to be realistic here     

> __< br-m >__ <jeffro256> If all 1-in,2-out, then 2MB*(1 tx / 6261 B)*(30 ms / tx) ~ 9600 ms of CPU time      

> __< ArticMine >__ One we can use parallel processing to the block, unlike single large txs     

> __< br-m >__ <jeffro256> (in response to tevador's question)     

> __< br-m >__ <boog900> IMO 1 MB blocks is already too big     

> __< br-m >__ <boog900> which was the original proposal      

> __< ArticMine >__ I have said for a long time that we are going to need parallel processing to address verification time     

> __< br-m >__ <jberman> you can parallel process at every level theoretically, even within verifying a single 128-in tx. but finding the sweet spot of where to apply the parallel verif to maximize CPU utilization is another q     

> __< br-m >__ <jeffro256> jeffro256 Also that 9.6s figure for 2MB of FCMP++ transactions didn't include BP+ range proof verification. It is a small, but certainly noticeable part of the verification time     

> __< br-m >__ <jberman> right now the implementation batch verifies all FCMP++ proofs synchronously     

> __< br-m >__ <jberman> so verification time of a large block should be somewhat faster than time to verify each proof in the block individually, ignoring parallelism at any level     

> __< ArticMine >__ are you excluding any palatalization implementations at the OS level?     

> __< br-m >__ <jeffro256> This is true, I am not considering batching. That's if verifying independently      

> __< br-m >__ <jeffro256> But we already do multi-threaded verification in monerod     

> __< br-m >__ <jberman> fcmp++ verification is currently batched, and not multi-threaded     

> __< ArticMine >__ On a CPU with say 64 threads this cam make a major difference     

> __< br-m >__ <jberman> yes     

> __< br-m >__ <rucknium> I will limit this agenda item to 30 minutes of discussion. That means ending at 17:52     

> __< br-m >__ <jberman> I think it could be easily updated to batch in groups of some max size, and do parallel batch verification within each block     

> __< br-m >__ <ofrnxmr> Jeffro,that must be 9600ms if firsttime seeing the txs?     

> __< br-m >__ <jeffro256> ofrnxmr: yes for full verification     

> __< br-m >__ <ofrnxmr> Ok, because if i aready have the txs, a 15mb block takes about 5 seconds     

> __< br-m >__ <jeffro256> During block propagation, assuming the tx is already in the pool, the FCMP would have already been verified, so it won't take that long when verifying an incoming block      

> __< br-m >__ <ofrnxmr> 5 seconds from notified to "synced". So not all verification time, some of that is bandwidth     

> __< tevador >__ I don't think I would support going above 600 KB with the minimum penalty free zone. That's still ~80 tx per block. Min tx fee for 8000 byte tx would be ~0.0001, about $0.03.     

> __< tevador >__ If my calculations are correct.     

> __< br-m >__ <articmine> I cannot support anything below 1000000     

> __< br-m >__ <articmine> bytes      

> __< tevador >__ I don't find a fee of $0.03 to be excessive. Might even be too low IMO.     

> __< br-m >__ <rucknium> Let's continue the agenda:     

> __< br-m >__ <rucknium> 6. FCMP alpha stressnet planning https://github.com/seraphis-migration/monero/issues/53#issuecomment-3053493262     

> __< br-m >__ <rucknium> There has been movement in https://github.com/seraphis-migration/monero/pull/81 , the last thing to be merged before alpha stressnet     

> __< br-m >__ <jberman> In PR 81, I modified some of wallet2's reorg handling logic to:     

> __< br-m >__ <jberman> -- always request blocks starting from 1 higher from current known tip     

> __< br-m >__ <jberman> -- if reorg detected, then request 3 blocks back     

> __< br-m >__ <jberman> -- if reorg still detected, then request 100 blocks back (100 is the default max reorg depth)     

> __< br-m >__ <jberman> jeffro256 highlighted how this incurs extra cost for daemons to handle reorgs (e.g. in a 10 block reorg, wallets will end up requesting 100 blocks back from tip to handle the reorg)     

> __< br-m >__ <jberman> I'm planning to revert back to behavior that does not incur extra cost to handle such a reorg, hopefully will complete that today     

> __< br-m >__ <jeffro256> I honestly don't think that 81 should be a blocker personally      

> __< br-m >__ <jberman> ofrn reported various refresh issues similar to issue #45 that the PR solved for him     

> __< br-m >__ <jeffro256> Okay fair      

> __< br-m >__ <jeffro256> Which part of the PR actually fixeD the reorg issue ?     

> __< br-m >__ <jeffro256> it was an issue with reorgs right ?     

> __< br-m >__ <jberman> yep, the reason I widened the PR's scope to remove init hash download was because that part touches on similar areas that would need changing. So I figured better to kill 2 birds with 1 stone and not need to make more changes separately     

> __< br-m >__ <ofrnxmr> jeffro256: There were numerous isues     

> __< br-m >__ <ofrnxmr> One of them was that the wallet was broken if you had a non-0 restore height     

> __< br-m >__ <ofrnxmr> I dm'd you another one a moment ago and will send another in a few mins     

> __< br-m >__ <rucknium> IMHO, with stressnet, keeping wallets working without manual fixes will be important.     

> __< br-m >__ <rucknium> Starting with my scripts that I used to spam last year's stressnet, I have written "easy-to-use" functions that can create an arbitrary number of wallets and monero-wallet-rpc instances. Wallets need to be generated programatically because 1in/2out tx creation times seem to go from 0.1 seconds to 5 seconds with current FCMP  [... too long, see https://mrelay.p2pool.observer/e/-auB0rEKcmJKZXYx ]     

> __< br-m >__ <rucknium> On last year's stressnet, I had 3-4 wallets spamming at a time IIRC. I could manually fix them when they encountered problems, but dozens of wallets would be harder.     

> __< br-m >__ <ofrnxmr> Lots of wallets or slow blocktimes     

> __< br-m >__ <ofrnxmr> I'm testing 15 subaccounts right now - i think subaccounts might be broken     

> __< br-m >__ <rucknium> ofrnxmr: On FCMP?     

> __< br-m >__ <ofrnxmr> Yeab     

> __< br-m >__ <rucknium> My spamming functions don't work without accounts.     

> __< br-m >__ <rucknium> I was promised accounts work 😢     

> __< br-m >__ <rucknium> Did you limit subaddress lookahead? I don't know if that could help anything.     

> __< br-m >__ <jeffro256> They should work AFAIK and are planned to worl but plz lmk if they don't      

> __< br-m >__ <ofrnxmr> check dm     

> __< br-m >__ <rucknium> More discussion of stressnet planning can happen in #monero-stressnet:monero.social  ( ##monero-stressnet on IRC I think).     

> __< br-m >__ <rucknium> I am wondering if the spamming code should be published or not. That discussion can happen at another time or asynchronously.     

> __< br-m >__ <rucknium> Any other major things about FCMP alpha stressnet to discuss?     

> __< br-m >__ <jberman> nothing from me     

> __< br-m >__ <rucknium> 7. Mining pool centralization: Temporary rolling DNS checkpoints https://github.com/monero-project/monero/issues/10064 and Publish or Perish https://github.com/monero-project/research-lab/issues/144     

> __< br-m >__ <rucknium> Do we talk to talk about DNS checkpoints and PoP together, or separately and in which order?      

> __< br-m >__ <ofrnxmr> bug found: when checkpointed chain reverts a reorg, the shared-ring-db gets borked     

> __< br-m >__ <rucknium> Does that happen with every re-org, or just ones involving checkpointing?     

> __< br-m >__ <ofrnxmr> just checkpointing     

> __< tevador >__ DNS checkpoints can work by themselves, so I think it can be discussed separately. They can prevent deep reorgs that are bad for UX. But they can't stop selfish mining and might even help the selfish miner in some cases.     

> __< br-m >__ <rucknium> Note that the network connectivity of the Qubic adversary is quite poor. They are losing almost every block propagation race. DataHoarder: is that correct?     

> __< DataHoarder >__ Only if it's a race. usually it's not a race and they are ahead     

> __< br-m >__ <ofrnxmr> I think they are losing because they have to broadcast their txs with the blocks     

> __< DataHoarder >__ They take an extra penalty for unknown txs having to get verified     

> __< br-m >__ <rucknium> But maybe they could improve their network connectivity in the future.     

> __< DataHoarder >__ Plus sometimes their blocks or changes are delayed 8-20 seconds     

> __< br-m >__ <ofrnxmr> If they were doing just empty blocks, would be faster     

> __< tevador >__ What might help would be to connect the checkpointing node directly to a few large honest pool nodes.     

> __< br-m >__ <rucknium> DNS checkpoints help the selfish miner if they can push their blocks to honest miners faster/earlier.     

> __< br-m >__ <rucknium> AFAIK     

> __< DataHoarder >__ p2pool is testing a few changes to broadcast non-p2pool blocks across its network     

> __< DataHoarder >__ which submits to monerod directly     

> __< tevador >__ It's enough if they push their blocks faster to the checkpointing node.     

> __< DataHoarder >__ so that makes all blocks spread across faster, alt or not     

> __< br-m >__ <rucknium> tevador: Right. maintaining connectivity and a common view of the network's block is important.     

> __< br-m >__ <venture> Regarding PoP, basic monte carlo sim is set up (honest miner case, with fork-resolution-policy, the soft fork proposal, no vesting / reward-splitting). The selfish-miner is implemented as well but lacks "proficiency" in my model. it performs not well / based on a simple heuristic currently.     

> __< DataHoarder >__ I am testing a "connector" network where they share view of multiple monerod nodes, local or remote, and share available information across (for checkpointing purposes). It needs more work to show as a proof of concept, but has more uses besides checkpointing (good for pools to broadcast blocks to each other quick and other information)     

> __< br-m >__ <venture> i noticed (probably obvious) that the fork probability (even in the honest case only), depends on the window and the block frequency. so D=5s on 1 min blocks (more forks) than on 2 min blocks. up to 3.5%     

> __< Guest28 >__ couldn't qubic just join p2pool?     

> __< br-m >__ <rucknium> I wrote some thoughts about the heart of selfish mining last meeting, but didn't post because they were related to changing the hashpower sampling rate. tevador has some good points against increasing the sampling rate. But I think it's useful to think about common network view:     

> __< br-m >__ <bawdyanarchist:matrix.org> Speaking of Monte Carlo, I released my first rev of a Monero sim. Still a WIP, but normal honest miner behavior appears to be working, the structure is solid, and it's at a point that adding new strategies is fully pluggable.     

> __< br-m >__ <bawdyanarchist:matrix.org> https://github.com/BawdyAnarchist/Monero-Simulator     

> __< DataHoarder >__ Guest28: in regards to what? No need to even join p2pool, it's just to speed up block transmission across the network. any monerod from a user using p2pool will have its blocks also broadcasted     

> __< br-m >__ <rucknium> In "Lay Down the Common Metrics: Evaluating Proof-of-Work Consensus Protocols' Security", the authors have a section "What Goes Wrong: Information Asymmetry" that gets to the heart of the matter. I think it explains why an attacker with minority hashpower can gain an advantage over honest miners (and honest merchants). A minor [... too long, see https://mrelay.p2pool.observer/e/s5C70rEKOXlsQzRM ]     

> __< br-m >__ <rucknium> I have developed my own analogy.     

> __< br-m >__ <rucknium> It's a gambling analogy, of course.     

> __< br-m >__ <rucknium> In blackjack, "the house always wins" because the ruleset creates biased odds...or does it? https://en.wikipedia.org/wiki/Card_counting can help a blackjack player get an advantage over the casino. If, by chance, the cards remaining in the dealing deck are high-numbered cards, then the player is temporarily at an advantage. In [... too long, see https://mrelay.p2pool.observer/e/wOa80rEKM0FsNEVB ]     

> __< br-m >__ <rucknium> A selfish miner acts in the same way. It knows the blocks produced by itself and the honest miners. When it is ahead of the honest miners because of randomly being luckier than its hashrate would normally allow, it "bets big" by withholding blocks. I think this analogy can help us understand why minority-hashpower selfish miners can get an advantage and maybe how they could be defeated.     

> __< br-m >__ <rucknium> Aumayr et al. (2025) "Optimal Reward Allocation via Proportional Splitting" https://arxiv.org/abs/2503.10185  is like re-shuffling the deck often, which decreases the card-counter's edge. But that costs RandomX hash verification time. Too much, probably. And it would require a hard fork.     

> __< br-m >__ <bawdyanarchist:matrix.org> rucknium: The "Optimal Reward Allocation" team said that they followed closely the MDP implementation from "Laying Down the Common Metrics" (cited the same MATLAB source you found.     

> __< br-m >__ <bawdyanarchist:matrix.org> > In our case, we only adapted the "reward splitting" MDP to follow our reward sharing variant ("proportional reward splitting" - PRS), so it is mostly the same as this repo's implementation.     

> __< br-m >__ <bawdyanarchist:matrix.org> https://github.com/commonprefix/proportional-reward-splitting-MDP     

> __< DataHoarder >__ in those same analogues, a checkpoint would be a "deck change" rucknium where any new information from old deck is useless unless it was already abused?     

> __< br-m >__ <rucknium> bawdyanarchist: Awesome. Thank you!     

> __< tevador >__ The DNS checkpointing issue didn't receive many comments. So I guess we can go ahead with it? Are any changes in monerod needed? It can stay opt-in since it's a soft fork.     

> __< br-m >__ <rucknium> DataHoarder: I think it would be similar. Here are other card counting countermeasures: https://en.wikipedia.org/wiki/Card_counting#Countermeasures     

> __< DataHoarder >__ "20:13:19 <br-m> <ofrnxmr> bug found: when checkpointed chain reverts a reorg, the shared-ring-db gets borked"     

> __< DataHoarder >__ ^ that'd need addressing     

> __< br-m >__ <vtnerd> the thing about opt-in is the solo miners joining the selfish-mining, etc     

> __< DataHoarder >__ also, alt blocks even close to a tip do not get shared across peers unless they are longer, or forced flushed     

> __< br-m >__ <rucknium> vtnerd has done some "procedure smoothing" coding on monerod.     

> __< DataHoarder >__ if we want the network to switch, at least, some of these should get broadcasted across the network and not just kept locally     

> __< tevador >__ If the majority of the network hashrate opts in, everyone will eventually end up on the checkpointed chain.     

> __< br-m >__ <rucknium> DataHoarder has been thinking of ways to get alt blocks propagated more reliably.     

> __< br-m >__ <vtnerd> there’s also whether we have one source publishing checkpoints or multiple (as they could disagree and cause some headaches)     

> __< DataHoarder >__ the problem is for the majority of the network to even get those blocks in the first place, if it's a race     

> __< br-m >__ <ofrnxmr> Tevador - need changes to frequency of checking and reduction of bantime. Patches for that are ready     

> __< DataHoarder >__ we can "manage" for public nodes. additionally RPC has some issues with old blocks (which Qubic encountered and blamed pools instead!)     

> __< br-m >__ <vtnerd> tevadoryour correct, its just that having people on the “wrong chain” temporarily hurts my head a bit     

> __< br-m >__ <vtnerd> I guess its no different than a reorg though     

> __< DataHoarder >__ I have some of my own local WiP patches for me to address this, but some proper solution might be nice. Can talk a bit after discussion     

> __< br-m >__ <rucknium> I think kayabanerve 's idea for an RPC method to checkpoint blocks is a good idea for the checkpointing nodes. You want them to stand on a block without the round-trip latency of querying DNS.     

> __< DataHoarder >__ ^ local temporary checkpoint that doesn't survive restarts?     

> __< br-m >__ <venture> https://mrelay.p2pool.observer/m/monero.social/FvzPJgCrjLhCvYkHEvibiqMv.svg (test_run2.svg)     

> __< DataHoarder >__ call it, block pinning?     

> __< br-m >__ <venture> is this received on IRC side     

> __< br-m >__ <venture> ?     

> __< DataHoarder >__ yes, nice svg     

> __< br-m >__ <vtnerd> my other thought with banning is whether we create a semi-permanent netsplit, the banning side would need to keeping retrying those nodes for a bit     

> __< br-m >__ <rucknium> Some group of nodes tell a checkpointing script that they all (or a {super} majority) have some block and wish to "finalize" it. Then the checkpointing script sends a finalize command to all those nodes and updates the TXT DNS record.     

> __< br-m >__ <venture> it's the simulation. with view for each miner (lane) .. including their branches (which they would have to maintain up to k , with the soft fork proposal)     

> __< br-m >__ <vtnerd> Im not sure if the current retry algorithm is sufficient for that potential netsplit case     

> __< tevador >__ I guess the fact that the checkpointed chain won't be relayed if qubic's chain is longer might be an issue.     

> __< br-m >__ <venture> the last lane is the selfish one     

> __< DataHoarder >__ rucknium I had that "finalize" step on majority on my test tool but didn't involve getting these back to monerod somehow, I should incorporate that in my simulations     

> __< DataHoarder >__ indeed tevador. There are workarounds *now* but a .patch release that allows broadcasts would help a lot     

> __< DataHoarder >__ even just a couple of nodes doing so would unclog most of the network if we want these altchains     

> __< br-m >__ <bawdyanarchist:matrix.org> venture: Did you publish your code yet for it? Can you share the link?     

> __< DataHoarder >__ we can reach public nodes directly, but not hidden or outbound only nodes     

> __< br-m >__ <rucknium> My basic checkpointing script on testnet just assume that the single checkpointing node will get the DNS checkpoint instruction soon after it's posted, but there are gaps there with DNS caching and having 4 domains.     

> __< tevador >__ I think it would be quite safe to relay alt block up to a certain depth even if the chain is shorter.     

> __< br-m >__ <venture> bawdyanarchist: i will. but no, it's not yet on github     

> __< DataHoarder >__ an alternative would be querying a local DNS server that the checkpointing script runs, rucknium, that has the most recent fetched value faster     

> __< br-m >__ <rucknium> I wonder what the reason for not relaying alt blocks that clear the difficulty threshold is? If they clear difficulty, DDoS risk is low.     

> __< DataHoarder >__ tevador: something like max desired reorg depth, or, up to last randomx epoch, those were my two "sane" min/max bounds for that distance     

> __< tevador >__ Exactly, the DoS risk is nonexistent if the PoW is checked first.     

> __< br-m >__ <rucknium> By the way, on testnet we were able to produce empirical evidence that a 10-block re-org can invalidate txs: https://libera.monerologs.net/monero-research-lounge/20250903#c579433-c579443     

> __< DataHoarder >__ I'm looking at nodes out there with open rpc and over time checking their /get_alt_blocks_hashes output too, fetching the full blocks, then relaying these blocks around     

> __< br-m >__ <rucknium> I'm not 100% sure if the 7 invalidated txs were actually mined in a block or were just waiting in txpool. (If in txpool, they would have been included in the next block).     

> __< rbrunner7 >__ Thanks for that, Rucknium! Nice to have it documented     

> __< tevador >__ The fact that transactions get stuck in the mempool for a week is much worse than just invalidating.     

> __< br-m >__ <boog900> DataHoarder: Ah I saw someone sent my node a deep alt block and was a bit confused :D     

> __< br-m >__ <rucknium> ofrnxmr was able to spend those outputs later because he cleared his node's txpool. I think another node mined it, not his. But ofrnxmr  can confirm     

> __< DataHoarder >__ to make it more obvious, the transactions with the key image stay in mempool so other new transactions can't replace this invalid one     

> __< DataHoarder >__ just in case the old chain comes back     

> __< br-m >__ <rucknium> And clear some things in the wlalet cache I think.     

> __< br-m >__ <rucknium> Ordinary users would find it difficulty to clear everything.     

> __< DataHoarder >__ boog900: it might not have been me, snatching some of qubic lost chains is tricky so these are the ones I'm focused in finding     

> __< DataHoarder >__ and it'd stay in other node mempools     

> __< DataHoarder >__ so it'd block transmission or broadcasts, or mining     

> __< br-m >__ <rucknium> In a scenario where the community and other agents are reluctant to enable DNS checkpoints, a grim trigger strategy can be followed https://en.wikipedia.org/wiki/Grim_trigger     

> __< br-m >__ <rucknium> Set up infrastructure for DNS checkpoints, but don't post checkpointed blocks to the DNS records unless Qubic re-orgs more than 9 blocks (or they facilitate a short-chain double-spend tx). If they do, issue checkpointed blocks indefinitely.     

> __< br-m >__ <rucknium> Rolling DNS checkpoints reduces Monero's decentralization, so it isn't idea for the Monero protocol, either.     

> __< br-m >__ <rucknium> I don't see  much opposition to it at the moment.     

> __< DataHoarder >__ it's understood it's a bandaid until measures can be implemented in the longer term     

> __< br-m >__ <rucknium> The Core Team would need to agree since they manage the DNS records. You need most big mining pools to agree and enable checkpoint enforcing (and probably a new monerod release with procedure smoothing).     

> __< br-m >__ <rucknium> It's in the mining pools' interest to enable checkpointing enforcement if they are mostly all in it together.     

> __< DataHoarder >__ the cadence changes and improvements can be done ahead of time, as they also smooth over any future need of it even if it's not for qubic     

> __< DataHoarder >__ (broadcasts, reorg ring db fix, check intervals, etc.) before agreeing to issuing them or not     

> __< DataHoarder >__ that way it's ready, instead of lagging for all that to be available. monero users can sometimes delay updates quite a bit     

> __< br-m >__ <rucknium> If there are not objections here, then timeline, tasks, and personnel should be decided.     

> __< br-m >__ <rucknium> i.e. who does what, and when.     

> __< br-m >__ <rucknium> DataHoarder has good understanding of the DNS issues involved. And the block propagation issues. He could lead on that. vtnerd  could help with additional smoothing changes to monerod.     

> __< tevador >__ Tracking issues can be openened first.     

> __< br-m >__ <rucknium> The Core Team would need to reach a consensus on this. articmine  could lead on that if desired.     

> __< br-m >__ <rucknium> Mining pools need to be contacted and their internal decision processes need to be worked through, and their decision communicated.     

> __< ArticMine >__ i will bring it up with the core team     

> __< br-m >__ <rucknium> ArticMine: Thank you!     

> __< br-m >__ <rucknium> From previous experience,  hashvault, moneroocean, supportxmr, and nanopool seemed quick to implement changes to their mining procedures when contacted:  https://rucknium.me/posts/monero-transactions-60-seconds-faster/     

> __< DataHoarder >__ I have a list of issues that we encountered while monitoring and operating monerod in a different capacity, and data to back the reasoning behind these fixes. as long as scope is limited rucknium I can take care of that part     

> __< br-m >__ <rucknium> DataHoarder: Fantastic. Thank you!     

> __< br-m >__ <rucknium> Try to pass improvements to ofrnxmr  and myself, which are performing checkpointing experiments on testnet.     

> __< tevador >__ hashvault, moneroocean, supportxmr, and nanopool are together >50%, enough for a soft fork.     

> __< br-m >__ <rucknium> Who will craft the message and contact mining pools? Last time, at least ofrnxmr  and ack-j  helped contact mining pools.     

> __< br-m >__ <ofrnxmr> Plowsof also helped     

> __< br-m >__ <ofrnxmr> "ofrnxmr was able to spend those outputs later because he cleared his node's txpool. I think another node mined it, not his. But ofrnxmr  can confirm"  correct     

> __< br-m >__ <rucknium> By last time, I mean the block template updating config fix: https://rucknium.me/posts/monero-transactions-60-seconds-faster/     

> __< br-m >__ <rucknium> selsta would be the person to coordinate a new point release of monerod. He has said he is standing by to assist on that.     

> __< br-m >__ <rucknium> What else would need to be done?     

> __< DataHoarder >__ address MoneroPulse page if it's decided to change so people are informed on their opt-in decision if wanted     

> __< br-m >__ <rucknium> If anyone thinks of something else that can be done and/or wants to take on a task, say it later in this room and/or on the GitHub issue: https://github.com/monero-project/monero/issues/10064     

> __< br-m >__ <rucknium> DataHoarder: Good idea. That could be folded in with crafting a blog post on getmonero.org and  broadcasting info to Core'e email list so that the message is consistent.     

> __< br-m >__ <venture> i wanted to ask, do we have numbers on orphan rate pre qubic? that way the propagation time can be inferred from the poisson distribution     

> __< br-m >__ <rucknium> rucknium: I may take on these communication tasks if no one else wants to.     

> __< DataHoarder >__ venture we have historical p2pool logs and what miners were mining when they found their shares, every 10 seconds. sometimes you see half the miners mining on an orphan block. unknown if we have other longer term data besides monero nodes keeping alternate blocks pre-qubic     

> __< br-m >__ <rucknium> venture: Did you see my info about empirical block propagation times in issue 10064?     

> __< br-m >__ <rucknium> There is also an analysis of logs in a research-lab issue by chaser  IIRC     

> __< br-m >__ <venture> ah nice. will check it out. no, wasn't aware of 10064      

> __< br-m >__ <rucknium> Next: Publish or Perish: https://github.com/monero-project/research-lab/issues/144     

> __< br-m >__ <venture> ah shit. Thought was already on the agenda. my svg related. but work in progress :)     

> __< br-m >__ <rucknium> I have been considering the methodology of these papers.     

> __< br-m >__ <rucknium> Most of these papers use Markov Decision Process (MDP) to decide the adversary's optimal behavior.     

> __< br-m >__ <rucknium> But there are two limitations to MDP. They can only model stationary processes. MDP is a subset of Stochastic Dynamic Programming (SDP), which can also model non-stationary processes.     

> __< br-m >__ <venture> my guess is they implement a miner from scratch (without PoW), and have a gloval eventqueue that calls on_mine based on poisson distribution and thinning by shares.     

> __< br-m >__ <venture> That queue gets emptied at each t and calls on_deliver     

> __< br-m >__ <rucknium> MDP also can only model a single agent's decision. The honest miners are basically on autopilot and inert.     

> __< br-m >__ <venture> and once that was set-up, they did the policy MDP..      

> __< br-m >__ <rucknium> A process is stationary if its statistical/probability processes do not depend on time.     

> __< br-m >__ <venture> rucknium: yes, autopilot, ie always broadcasts on_mine     

> __< br-m >__ <rucknium> Mining is a Poisson process, which is memoryless. So far, so good. But difficulty adjustment is not memoryless. And a selfish minor alters difficulty adjustment.     

> __< br-m >__ <venture> yeah.. diff adjustment is often not considered in these papers. only the one with selfish-mining re-examined     

> __< br-m >__ <rucknium> Grunspan & Pérez-Marco (2019) "On profitability of selfish mining" https://arxiv.org/abs/1805.08281 give a critique of modeling selfish mining in a MDP framework in this ^ basis.     

> __< br-m >__ <rucknium> on this basis*     

> __< br-m >__ <rucknium> I don't know how much this critique matters in the current scenario.     

> __< br-m >__ <rucknium> Related, I winder if the objective function in the PoP's MDP could be easily modified from relative revenue to "propaganda value", or something, since Qubic seems to care a lot about that.     

> __< br-m >__ <venture> unfortunately they didn't publish their solved MDP I thinik     

> __< br-m >__ <rucknium> On the single-player limitation to MDP, I have only seem two-player modeling in Aumayr et al. (2025) "Optimal Reward Allocation via Proportional Splitting" https://arxiv.org/abs/2503.10185     

> __< br-m >__ <rucknium> They say their protocol has a Nash equilibrium for some parameter values. Maybe other papers do game theory modeling. I haven't read them all in this area.     

> __< br-m >__ <rucknium> Aumayr et al. (2025) also does MDP as a complement to their game theory modeling.     

> __< br-m >__ <rucknium> venture: Here was the orphan analysis by chaser  https://github.com/monero-project/research-lab/issues/102#issuecomment-1577827259     

> __< br-m >__ <rucknium> Did Negy, Rizun, & Sirer (2020) "Selfish mining re-examined" use MDP?     

> __< br-m >__ <rucknium> My big-picture impression of PoP is that it bites most fiercely in its k parameter. The other changes seem to have the biggest effect for tie/races/near-ties. For a very strong adversary, k rules.     

> __< br-m >__ <venture> rucknium: around 15 reorgs per month, that's insanely low, good propagation. man qubic seems well connected in sniping in between with their blocks     

> __< br-m >__ <rucknium> k is a mirror image of the rule in Bitcoin Cash (for example) that won't re-org to a chain when the re-org is more than n blocks deep. The k rule is that a node will not re-org to a chain that is less than k deep. k = infinity means that both the N and k rules are in effect, basically. That is what I understand.     

> __< br-m >__ <bawdyanarchist:matrix.org> ls     

> __< br-m >__ <bawdyanarchist:matrix.org> *sorry. stray keypres     

> __< br-m >__ <rucknium> It is possible that Negy, Rizun, & Sirer (2020) "Selfish mining re-examined" doesn't use MDP because they agree with the critique of Grunspan & Pérez-Marco (2019) , but say they don't go far enough.     

> __< br-m >__ <antilt:we2.ee> > In case of two competing chains of equal weight, the PoP paper calls for a random selection to be made, but I would suggest to use a deterministic tie breaking rule (e.g. with hashing).     

> __< br-m >__ <antilt:we2.ee> tevador: how would that work ?     

> __< tevador >__ rucknium: with k=∞ you can still reorg, just not to a selfish chain that will have a weight of zero     

> __< br-m >__ <venture> i think diff adjustment is not elastic enough in monero for a selfish-miner.. def. worth looking into, but "static" is also valuable and should help short-term selfish-mine mitigation     

> __< tevador >__ antilt: I've been thinking about this and it seems that the random selection they propose has a reason. The attacker can't know in advance if they will win a race.     

> __< tevador >__ With deterministic selection, you plug in both chains into a hash function and that will tell you which chain to select. The attacker can do this check before deciding to publish its chain.     

> __< br-m >__ <venture> yeah. that's a downside. but uniform splits the hashrate in half     

> __< br-m >__ <venture> but even with deterministic selection, he can't the uncle in...     

> __< br-m >__ <venture> can't *get     

> __< br-m >__ <rucknium> "About 80 percent of blocks arrived at all five Monero nodes within a one-second interval." https://rucknium.me/posts/monero-pool-transaction-delay/     

> __< br-m >__ <rucknium> In early 2023     

> __< br-m >__ <rucknium> The magic of fluffy blocks     

> __< br-m >__ <rucknium> Stochastic dynamic programming could relax the stationarity assumption. In theory I could try that since Stochastic dynamic programming is used in economics a lot, but I don't know how difficult it would be in this case.     

> __< tevador >__ With deterministic selection, the attacker will only release a block if it wins the selection. So a probability of 1.0 to win. With random selection, the chance is (1.0+α)/2, which is < 1.0.     

> __< br-m >__ <venture> probability of 1 omits the cases where he lost hashrate effort and never broadcasts (that's not visible, but still there)     

> __< br-m >__ <antilt:we2.ee> tevador with k=3 this case would happen quite often. How do checkpoints fit in here?     

> __< tevador >__ If he loses the selection, he mines a secret block N+2 with the honest uncle.     

> __< br-m >__ <rucknium> Doesn't the attacker have to waste more hashpower to get a winning block wit deterministic selection? Throw a whole block away if it is losing?     

> __< br-m >__ <venture> tevador: i need to get my head around this memoryless thing. he would start over at this point.. but maybe that has no downside..     

> __< tevador >__ He wouldn't throw it away, he'd continue mining N+2, so his chain will have an equal weight if N+2 is released in time using the honest N+1 uncle. So the overall chance of winning is 75% for the 2 attempts.     

> __< br-m >__ <venture> i hope i can share some simulation numbers soon, with the 2 variants, uniform, deterministic     

> __< br-m >__ <venture> but what about changing the second rule, to only go for the heighest weight, if it is >= 2      

> __< tevador >__ ^ Then you would have longer honest chain splits.     

> __< tevador >__ All this will probably need to be simulated first.     

> __< br-m >__ <rucknium> We can end the meeting here. Feel free to continue discussing. Thanks everyone.     

> __< tevador >__ antilt: the idea was to use k=∞ with checkpoints.     

> __< tevador >__ k=3 makes more sense without checkpoints     

> __< br-m >__ <articmine> I will respond to the fee and minimum penalty free issue in the GitHub issue      

> __< br-m >__ <articmine> tevador: ping     

> __< br-m >__ <antilt:we2.ee> thx. an attacker would <<51% and a custom strategy iiuc     

> __< br-m >__ <antilt:we2.ee> *would need     

> __< sech1 >__ Rucknium next p2pool release will fast propagate all Monero blocks, so we can expect <1 second propagation times once enough p2pool miners update. My tests show propagation delay <3 ms per one hop, compared to Monero's 400+ ms     

> __< DataHoarder >__ relevant code https://github.com/SChernykh/p2pool/commit/50634e5e79292dcd16ac4fb45593525bd6287b4d :)     

> __< DataHoarder >__ I touched on it lightly sech1 as well :)     

> __< DataHoarder >__ so if pools want faster propagation, all they have to do is run *a* p2pool instance, no need to mine on it, connected to one of their monerod     

> __< DataHoarder >__ p2pool should receive blocks via ZMQ and broadcast to other peers who don't have it, which in turn if these have other p2pool (like mini/nano) they would also broadcast it to most participants     

> __< DataHoarder >__ p2pool will also submit_block to that monerod with new incoming blocks     

> __< br-m >__ <rucknium> sech1: Great :)     

> __< br-m >__ <rucknium> According to my network construction simulations, all reachable nodes should get a message within 4 hops: https://github.com/monero-project/monero/pull/9939#discussion_r2285992169     

> __< DataHoarder >__ so it's a two-way bridge for faster blocks     

> __< br-m >__ <rucknium> Add reachable nodes and you would get a max of 5 total since all unreachable nodes must have an outbound connection to a reachable node (unreachable nodes cannot connect to each other).     

> __< sech1 >__ Yeah, most important is that major Monero pools start running p2pool nodes connected to their block producing nodes, via zmq     

> __< sech1 >__ But even without it, this change will speed up the network     

> __< sech1 >__ I expect pools' effective hashrate to get >1% free boost :) Just because everyone will get new blocks faster     

> __< br-m >__ <venture> put my current simulator online here https://github.com/venture-life/mining-simulator     
```


# Action History
- Created by: Rucknium | 2025-09-02T23:53:53+00:00
- Closed at: 2025-09-12T20:00:17+00:00
