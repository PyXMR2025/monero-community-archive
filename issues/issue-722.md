---
title: Monero Research Lab Meeting - Wed 27 July 2022
source_url: https://github.com/monero-project/meta/issues/722
author: Rucknium
assignees: []
labels: []
created_at: '2022-07-25T15:08:55+00:00'
updated_at: '2022-08-01T17:01:57+00:00'
type: issue
status: closed
closed_at: '2022-08-01T17:01:57+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

[Join the Monero Matrix server if you don't already have a Matrix account.](https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211027T170000&p1=1440)

Main discussion topics:

1. Greetings

2. Improvements to the decoy selection algorithm ( [Decoy Selection Algorithm - Areas to Improve](https://github.com/monero-project/research-lab/issues/86), [Binning PoC](https://github.com/monero-project/research-lab/issues/88), [OSPEAD](https://ccs.getmonero.org/proposals/Rucknium-OSPEAD-Fortifying-Monero-Against-Statistical-Attack.html) ) @j-berman @Rucknium

3. Seraphis. ( [UkoeHB's Seraphis Proof of Concept work](https://ccs.getmonero.org/proposals/seraphis-wallet-poc-2.html), [Seraphis repo](https://github.com/UkoeHB/Seraphis) ).

4. MRL Meta: "Cat herding", i.e. prioritization of research areas and features. Active recruitment of technical talent, MRL structure, funding (@Rucknium & others) [MoneroResearch.info repository of Monero-related research papers](https://moneroresearch.info/), [Reddit discussion](https://www.reddit.com/r/Monero/comments/pkg3d6/the_monero_project_should_actively_recruit/)

5. Any other business

6. Confirm next meeting agenda


Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: UkoeHB

Previous meeting agenda/logs:

#720 

# Discussion History
## UkoeHB | 2022-07-27T18:10:41+00:00
`[07-27-22 17:00:17] <kayabanerve[m]> Greetings, everyone :)`
`[07-27-22 17:01:23] <rbrunner> Hello`
`[07-27-22 17:01:43] <Rucknium[m]> Hi`
`[07-27-22 17:01:49] <dangerousfreedom> Hello`
`[07-27-22 17:02:08] <ArticMine[m]> Hi`
`[07-27-22 17:02:28] <jberman[m]> hello`
`[07-27-22 17:02:46] <UkoeHB> oh hi meeting time lol `
`[07-27-22 17:03:08] <UkoeHB> here's the agenda: https://github.com/monero-project/meta/issues/722`
`[07-27-22 17:03:40] <UkoeHB> 2. updates, what has everyone been working on?`
`[07-27-22 17:04:31] <UkoeHB> me: I've been updating my seraphis library to support scanning for legacy enotes.`
`[07-27-22 17:05:01] <UkoeHB> Which is required in order to make a wallet that's independent of wallet2`
`[07-27-22 17:05:02] <Rucknium[m]> Me: OSPEAD`
`[07-27-22 17:05:32] <kayabanerve[m]> I implemented BP and BP+ in Rust, which I don't believe has been done before. It offers another point of reference towards it while overall providing more commentary on the algorithm. While an audit did say they would do a Rust impl, they ended up identifying a non-Monero-compliant Rust impl as 'similar' and left it at this. This is confirmed to be compliant.`
`[07-27-22 17:05:45] <kayabanerve[m]> *specifically proving, so only half of the problem`
`[07-27-22 17:07:50] <dangerousfreedom> I have been rescanning the Borromean signatures as I thought it was a bug on my software or a connection problem when I found the frist wrong signature stored and I found three more. So 6 in total so far. I didnt debug the addKeys2 (ge_double_scalarmult_base_vartime) to find exactly what is happening but as I far as I could see, half the bits are correct and half are wrong (therefore the interpretation of the wrong`
`[07-27-22 17:07:50] <dangerousfreedom> Scalar). I could not find the exact mapping yet though.`
`[07-27-22 17:09:17] <dangerousfreedom> And I started looking how to implement the verification_bp function in Rust as I believe I wont be able to scan the whole BP era with my accurate and slow python tools :p`
`[07-27-22 17:09:32] <dangerousfreedom> kayabanerve: is helping me with that :)`
`[07-27-22 17:09:35] <Rucknium[m]> dangerousfreedom: Referring to the "malleability" issues, what is the approximate date of the most recent transaction that has had this issue?`
`[07-27-22 17:10:39] <dangerousfreedom> Rucknium[m]: So far the last I found is this one:https://xmrchain.net/search?value=e4b7982b081a17892525f1b1d3011ec06a0820cbf451d3a64f8ea998104a753c`
`[07-27-22 17:10:48] <dangerousfreedom> 2018-02-04`
`[07-27-22 17:11:15] <UkoeHB> 3. discussion`
`[07-27-22 17:11:19] <kayabanerve[m]> dangerousfreedom: Security of this should be prove-able so long as we can provide a scalar transformation, globally applied, as an alternative for the normal deserialization process.`
`[07-27-22 17:13:26] <dangerousfreedom> kayabanerve[m]: Yes. I think so. I just didnt find the mapping yet. (Didnt try hard either)`
`[07-27-22 17:14:57] <rbrunner> How did those transactions get mined? Lack of certain tests in the daemon?`
`[07-27-22 17:15:29] <kayabanerve[m]> People specified scalars > l. The daemon didn't care.`
`[07-27-22 17:15:36] <dangerousfreedom> rbrunner: I think so. There were not enough enforcement on the scalars and Points stored in the blockchain`
`[07-27-22 17:15:40] <Rucknium[m]> The Zcash blockchain is being spammed and most of their wallets are struggling with tx scanning. The only wallet that seems to be handling the spam is one that has "Warp Sync". We probably can't use anything from the Warp Sync method, but I wanted to bring it up just in case we can incorporate something into Monero:`
`[07-27-22 17:15:42] <kayabanerve[m]> So that could be phrased as lack of tests, it could be phrased as indifference, or could be phrased as a bug.`
`[07-27-22 17:15:43] <Rucknium[m]> https://forum.zcashcommunity.com/t/warp-sync-a-full-scan-method/39462`
`[07-27-22 17:16:09] <kayabanerve[m]> Isn't Warp Sync syncing in reverse in order to not need to scan old notes you've already spent?`
`[07-27-22 17:17:13] <kayabanerve[m]> Oh. No, sorry. That's a different thing of theirs.`
`[07-27-22 17:17:29] <Rucknium[m]> Warp Sync does more than that.`
`[07-27-22 17:17:35] <kayabanerve[m]> Warp Sync is calculating the Merkle tree, which they use for their membership proofs (close enough), at the end so they only calculate it once.`
`[07-27-22 17:17:48] <kayabanerve[m]> Instead of calculating it for [] and then constantly updating.`
`[07-27-22 17:18:02] <kayabanerve[m]> *and yes, other improvements, yet that's the primary one`
`[07-27-22 17:18:42] <rbrunner> So indeed no inspiration for Monero to get there, probably, because wholly different?`
`[07-27-22 17:19:14] <rbrunner> Don't know much about Merkle trees, but never saw one in Monero :)`
`[07-27-22 17:20:29] <UkoeHB> it's a good reference for if we ever go to a zk proof relying on a merkle tree`
`[07-27-22 17:21:08] <kayabanerve[m]> rbrunner: someone hasn't looked :p`
`[07-27-22 17:21:11] <kayabanerve[m]> we use them in blocks lol`
`[07-27-22 17:21:26] <kayabanerve[m]> but no, we don't use a merkle tree to store output indexes... yet 👀`
`[07-27-22 17:21:38] <kayabanerve[m]> So Warp Sync isn't notably relevant now`
`[07-27-22 17:22:16] <rbrunner> You mean also a chain is a tree?`
`[07-27-22 17:22:57] <kayabanerve[m]> Merkle trees are used all the way back in Bitcoin`
`[07-27-22 17:23:08] <UkoeHB> rbrunner: there's a merkle tree for tx ids in blocks iirc`
`[07-27-22 17:23:12] <kayabanerve[m]> Monero block headers contain a tree root of TXs`
`[07-27-22 17:23:34] <rbrunner> Interesting. Will have a look. Saw blocks as mere linear arrays so far, in my mind.`
`[07-27-22 17:23:51] <kayabanerve[m]> Same thing BTC does. ETH has merkle patricia trees they use for storage, and they also include a few different roots for different parts of the codebase.`
`[07-27-22 17:23:55] <UkoeHB> there was actually an ancient bug in the merkle tree code that led to a hardfork to handle a broken block`
`[07-27-22 17:24:22] <sech1> 512 transactions bug`
`[07-27-22 17:24:24] <kayabanerve[m]> While processing is linear, merkle trees are used for logarithmic membership proofs. Bitcoin light clients can prove TX inclusion without sending the entire block. Same with Monero`
`[07-27-22 17:24:26] <UkoeHB> https://web.getmonero.org/resources/research-lab/pubs/MRL-0002.pdf`
`[07-27-22 17:24:58] <kayabanerve[m]> It's why they're discussed here as well, for transaction membership. They're log 2. We can verify membership within 2^64 TXs with just 64 ops.`
`[07-27-22 17:25:19] <kayabanerve[m]> The difficulty is in a ZK transformation of that proof, hence circuits, yet that does get a bit off topic for now`
`[07-27-22 17:25:31] <kayabanerve[m]> Not that this isn't the place. Just that we've sufficiently discussed merkles :p`
`[07-27-22 17:26:23] <Rucknium[m]> "elaborates upon exactly what the offending blcok did to the network." I can tell they wrote this quickly :)`
`[07-27-22 17:27:27] <Rucknium[m]> I will need to correct "out-of-order" timestamps on XMR blocks (and other blockchains, but that's less important.) I have not tried to read existing work on block time stamp correction. Anyone know a reference implementation/method? And what are the main hypotheses about why timestamps are sometimes out of order?`
`[07-27-22 17:27:45] <UkoeHB> that was an 8-day paper lol, not too shabby`
`[07-27-22 17:28:02] <kayabanerve[m]> ... i despise blockchain NTP`
`[07-27-22 17:28:28] <Rucknium[m]> The hypotheses are important since it is good to do a statistical correction based on some understanding of the "data generating process".`
`[07-27-22 17:28:35] <kayabanerve[m]> Bit of an off topic. Rucknium the algorithm is sufficiently simple, you can read it quickly, yet it's expensive/annoying to calculate on the spot when we shouldn't even track time.`
`[07-27-22 17:29:04] <kayabanerve[m]> Timestamps can be out of order because we don't enforce they're sequential, which is an opinionated discussion.`
`[07-27-22 17:29:20] <kayabanerve[m]> So it's whatever your local view on time is. When blocks are mined in close proximity, that drift can be especially notable.`
`[07-27-22 17:29:22] <UkoeHB> Rucknium[m]: the main reason I can think of is unsychronized clocks`
`[07-27-22 17:29:37] <rbrunner> I never saw anything else mentioned.`
`[07-27-22 17:29:55] <kayabanerve[m]> There's also a variety of discussions on historic NTP. I've read posts saying a few minutes is acceptable, posts saying ~30 seconds, and now I'd be horrified to hear >10s tbh`
`[07-27-22 17:29:57] <rbrunner> As I can't remember a reason why somebody would stamp wrongly on purpose`
`[07-27-22 17:30:10] <UkoeHB> kayabanerve[m]: how about you define NTP for us.....`
`[07-27-22 17:30:16] <kayabanerve[m]> Which is relevant when you remember BTC isn't from the last ten years`
`[07-27-22 17:30:31] <Rucknium[m]> I think gingeropolous mentioned a "time warp" attack as a possible motivation by a set of coordinated miners`
`[07-27-22 17:30:31] <kayabanerve[m]> Network Time Protocol`
`[07-27-22 17:30:42] <kayabanerve[m]> It's an actual protocol. Monero has its own NTP... algorithm? though`
`[07-27-22 17:31:00] <kayabanerve[m]> Where it's the median of the last 15 blocks IIRC, which is used for TX timestamp acceptance`
`[07-27-22 17:31:14] <kayabanerve[m]> And then I assume we also require new blocks have a timestamp past the median.`
`[07-27-22 17:31:19] <kayabanerve[m]> *past whatever Monero's clock says it is.`
`[07-27-22 17:31:53] <kayabanerve[m]> I believe it's a median, yet I don't remember off the top of my head.`
`[07-27-22 17:32:36] <kayabanerve[m]> So the clock does effect difficulty. Lowering it, by claiming to be in the future, will hit a future time limit. Raising it, by claiming to be in the past, is possible.`
`[07-27-22 17:32:42] <Rucknium[m]> Ideally what a block timestamp would tell me is that all txs in the block were broadcast before that real-life time. (Even better, for blocks that are not full, is that all txs were broadcast between the previous block and the block that the tx was confirmed in.)`
`[07-27-22 17:32:50] <kayabanerve[m]> It's just also a 51% attack lowering distribution.`
`[07-27-22 17:32:54] <UkoeHB> kayabanerve[m]: Rucknium[m] asked about block timestamps, not how the difficulty algo works`
`[07-27-22 17:33:18] <kayabanerve[m]> UkoeHB: I'm saying there is no attack based on time manipulation except via difficulty.`
`[07-27-22 17:33:47] <Rucknium[m]> If I understand correctly, there are timestamp rules to "bound" difficulty adjustments, as a consensus rule.`
`[07-27-22 17:33:57] <kayabanerve[m]> My next comment was going to be there are ways you can spike/drop difficulty, mine, then leave and come back.`
`[07-27-22 17:34:48] <kayabanerve[m]> It was frequent in the BTC fork scene for small coins. Miners mine 3 at a time, or however many, screw with one, then screw with the next. By the end of the line, the original corrects itself and you can come back. That's the only attack I remember as making sense`
`[07-27-22 17:34:55] <UkoeHB> kayabanerve[m]: and yet... he is asking about tx timing, not the difficulty algo...`
`[07-27-22 17:34:58] <Rucknium[m]> I suppose one thing I could look for is timestamps that are at the boundary of what the consensus rules would accept`
`[07-27-22 17:35:04] <kayabanerve[m]> I don't see it as an active concern to Monero given our size`
`[07-27-22 17:36:27] <kayabanerve[m]> ... oh. Sorry then.`
`[07-27-22 17:36:37] <Rucknium[m]> Alternatively, if someone(s) had reliable logs on the time that blocks have been received by their node for the last year or two...that could be a good replacement for the timestamp in the blocks. Obviously, those logs would be dependent on that particular node's position in the network.`
`[07-27-22 17:37:29] <kayabanerve[m]> It's all perspective, besides the definition used for TX timelocks. I'd suggest whatever we used as seeds for the relevant years if you want higher-accuracy timestamps.`
`[07-27-22 17:37:52] <rbrunner> "I will need to correct "out-of-order" timestamps on XMR blocks" I am a bit surprised this should be somehow important. After all you have the block numbers.`
`[07-27-22 17:38:03] <Rucknium[m]> Whatever we used as seeds?`
`[07-27-22 17:38:51] <Rucknium[m]> rbrunner: I expect that the necessary correction would be minor. But it's good to be more precise.`
`[07-27-22 17:38:56] <UkoeHB> Rucknium[m]: we added deterministic unlock_times here, which is probably the best way to estimate each block's timestamp https://github.com/monero-project/monero/pull/6745`
`[07-27-22 17:39:06] <UkoeHB> if you don't trust the block timestamp`
`[07-27-22 17:40:02] <kayabanerve[m]> Seed nodes. Nodes people first connect to when we join the network. If you get logs from those nodes, not only are they presumed reliable with high bandwidth and connections, they'll be epicenters (assuming the network isn't perfect at distributing itself in this whole p2p thing, yet p2p isn't my specialty)`
`[07-27-22 17:40:27] <Rucknium[m]> Put another way, human behavior is based on real-life time, not on Monero's "NTP". So having the real life time is important.`
`[07-27-22 17:40:30] <kayabanerve[m]> I'm not even sure we have "seed nodes" versus a list of nodes usable as seeds, which would be my assumption...`
`[07-27-22 17:41:59] <Rucknium[m]> kayabanerve: I see what you mean. I think position in the network is not extremely important as long as its position doesn't change much. The positioning that matters is, I suppose, network distance to the mining nodes. `
`[07-27-22 17:42:32] <Rucknium[m]> Would anyone have those logs though?`
`[07-27-22 17:43:12] <Rucknium[m]> neptune has some code on GitHub to have an archiving node, complete with mempool data. I'm not sure if that is being actively run now.`
`[07-27-22 17:43:44] <Rucknium[m]> https://github.com/neptuneresearch/monerod-archive`
`[07-27-22 17:46:24] <UkoeHB> any other topics to discuss in this meeting?`
`[07-27-22 17:46:32] <UkoeHB> there has been some discussion about the tx_extra...`
`[07-27-22 17:46:45] <UkoeHB> I felt sgp_'s response was reasonble`
`[07-27-22 17:47:16] <sgp[m]> <3`
`[07-27-22 17:48:08] <Rucknium[m]> This, right? https://github.com/monero-project/monero/issues/6668`
`[07-27-22 17:48:17] <UkoeHB> yeah`
`[07-27-22 17:49:48] <rbrunner> You mean some more recent discussion :)`
`[07-27-22 17:50:28] <Rucknium[m]> I would agree that the issue with tx_extra and similar issues is not "spam" from on-chain "data storage", but rather privacy implications from tx non-uniformity.`
`[07-27-22 17:50:37] <ArticMine[m]> The toxic content attack `
`[07-27-22 17:51:07] <rbrunner> With a break since start of May until recently`
`[07-27-22 17:51:25] <kayabaNerve> I personally most prefer steganography`
`[07-27-22 17:51:27] <rbrunner> Oh, May last year :)`
`[07-27-22 17:51:32] <ArticMine[m]> Allowing it only for miners is reasonable `
`[07-27-22 17:51:52] <kayabaNerve> Encrypted steganography would be completely indistinguishable, maintaining privacy.`
`[07-27-22 17:51:52] <sgp[m]> what do you mean by allow?`
`[07-27-22 17:52:16] <ArticMine[m]> Only for coinbase `
`[07-27-22 17:52:25] <ArticMine[m]> Tx extra `
`[07-27-22 17:52:45] <kayabaNerve> If we don't care to encourage steganography, and its computational cost, then my suggestion would be a 255 byte limited field, as it is now.`
`[07-27-22 17:53:22] <kayabaNerve> UkoeHB: suggested enforcing TLV. I don't believe that's valuable in any way. If we're removing all wallet data from it, so it's just arbitrary data, any users will solely waste bytes define PADDING + re-defining length imo`
`[07-27-22 17:53:28] <sgp[m]> steganography seems.... prone to mistakes`
`[07-27-22 17:54:02] <kayabaNerve> we can specify a protocol and a reference`
`[07-27-22 17:54:12] <sgp[m]> for reference, the encrypted memo for zcash is 512 bytes, which seems super long`
`[07-27-22 17:54:22] <kayabaNerve> Also, ArticMine[m], do you have any reason to allow it in coinbase? Merge mining, I'd guess?`
`[07-27-22 17:54:50] <UkoeHB> sgp[m]: do they have much larger txs? maybe it's proportionally small`
`[07-27-22 17:54:58] <kayabaNerve> For most uses case, 128 should be enough. I noted a case relevant to Monero when you'd want 256 though`
`[07-27-22 17:55:47] <kayabaNerve> (2 JAMTIS addresses, one for a return address, one for... whatever would exceed 128 bytes yet not exceed 255, while leaving room in said 255 for additional messages)`
`[07-27-22 17:55:58] <ArticMine[m]> Merge mining `
`[07-27-22 17:55:58] <xmrack[m]> I would also like to see the removal of tx_extra in favor of better uniformity. Not trying to give anyone ideas but from a redteaming perspective, you could possibly abuse the blockchain and put signed commands within the field to control a botnet.`
`[07-27-22 17:59:11] <ArticMine[m]> I see tx_extra as a possible attack vector `
`[07-27-22 18:00:59] <UkoeHB> ok we are at the end of the hour so I'll call it here; thanks for attending everyone`

# Action History
- Created by: Rucknium | 2022-07-25T15:08:55+00:00
- Closed at: 2022-08-01T17:01:57+00:00
