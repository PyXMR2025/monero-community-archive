---
title: Monero Research Lab Meeting - Wed 28 February 2024, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/973
author: Rucknium
assignees: []
labels: []
created_at: '2024-02-26T23:26:55+00:00'
updated_at: '2024-04-02T15:50:39+00:00'
type: issue
status: closed
closed_at: '2024-03-06T16:23:58+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

[Join the Monero Matrix server if you don't already have a Matrix account.](https://web.archive.org/web/20230128130949/https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211027T170000&p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3. Discuss: [Removing/Fixing/Encrypting monero's timelocks](https://github.com/monero-project/research-lab/issues/78)

4. @jeffro256 ["In short, I want to make `Blockchain::get_adjusted_time()` monotonic (barring reorgs) on the next network upgrade."](https://github.com/monero-project/meta/issues/966#issuecomment-1936243293)

5. @jeffro256  [I'd like to discuss disallowing v1 transactions for "unmixable" input amounts in the next network upgrade.](https://github.com/monero-project/meta/issues/966#issuecomment-1936243293)

6. @jeffro256 [ I think we can improve how the nodes handle alternative blocks in a way that might naturally reduce the number of reorgs on the network.](https://github.com/monero-project/meta/issues/966#issuecomment-1936243293)

7. Any other business

8. Confirm next meeting agenda


Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#970 

# Discussion History
## Rucknium | 2024-03-06T16:23:58+00:00
> __< r​ucknium:monero.social >__ Meeting time! https://github.com/monero-project/meta/issues/973     

> __< r​ucknium:monero.social >__ 1) Greetings     

> __< rbrunner >__ Hello     

> __< j​effro256:monero.social >__ Howdy     

> __< v​tnerd:monero.social >__ Hi     

> __< d​angerousfreedom:matrix.org >__ hi     

> __< h​into.janaiyo:matrix.org >__ hello     

> __< r​ucknium:monero.social >__ 2) Updates. What is everyone working on?     

> __< r​ucknium:monero.social >__ me: OSPEAD. I think I will complete Milestone 2 in two weeks.     

> __< v​tnerd:monero.social >__ Me: working on too many files open bug in LWS - the first attempt at a fix segfaults but I cannot reproduce     

> __< 0​xfffc:matrix.org >__ me: understanding the wallet code, to add lmdb as its cache.     

> __< h​into.janaiyo:matrix.org >__ working on cuprate's 2nd DB backend, the actual DB used has been changing around     

> __< j​effro256:monero.social >__ Working on the Seraphis lib serialization and tx handling     

> __< r​ucknium:monero.social >__ 3) Discussion. I think jeffro256 has an item or two to discuss.     

> __< j​effro256:monero.social >__ Yeah I wanted to bring up the issue we missed last week which is that there isn't a way to break "ties" between alt chains of the same difficulty     

> __< r​ucknium:monero.social >__ How do other blockchains handle it?     

> __< rbrunner >__ Also my first thought, together with "how probably this may be"     

> __< rbrunner >__ *probable     

> __< rbrunner >__ (that such a tie occurs)     

> __< j​effro256:monero.social >__ Very probable: everytime there is a 1 block difference in the chain     

> __< r​ucknium:monero.social >__ Doesn't it happen almost every time there is an orphaned block?     

> __< j​effro256:monero.social >__ Yes basically everytime, unless it skips from 0 to more than 1 orphaned block     

> __< rbrunner >__ Hmm, and why don't we run into problems with that all the time, half of the daemons running this way and the other half that way?     

> __< r​ucknium:monero.social >__ BLOCK ADDED AS ALTERNATIVE is the evidence, right?     

> __< j​effro256:monero.social >__ It resolves after 2 blocks, which is why you never see reorg messages that say that the alt chain was 1 block deep     

> __< j​effro256:monero.social >__ yup     

> __< r​ucknium:monero.social >__ Probably the status quo reduces the effective network hashpower     

> __< j​effro256:monero.social >__ It'd be better if it resolved after 1 block tho to prevent as much PoW being lost and to help merchants be more confident accepting 0-conf     

> __< j​effro256:monero.social >__ Here's the condition where we switch to an alt chain: https://github.com/monero-project/monero/blob/7b7958bbd9d76375c47dc418b4adabba0f0b1785/src/cryptonote_core/blockchain.cpp#L2122     

> __< j​effro256:monero.social >__ Right now, we only switch if the PoW of our current chain is strictly less     

> __< rbrunner >__ Regardless of how many blocks that may take?     

> __< r​ucknium:monero.social >__ IMHO, we should research best practices. I worry that certain tiebreaking rules could provoke undesirable miner behavior. Block withholding for selfish mining, etc.     

> __< j​effro256:monero.social >__ I'm not sure I understand the question     

> __< rbrunner >__ Say, the two "second" competing blocks have again the same difficulty - waiting for a third block starts which hopefully brings a difference     

> __< j​effro256:monero.social >__ Yes     

> __< rbrunner >__ "Research best practices" sounds good. We are hardly the first ones with this question, one would think.     

> __< j​effro256:monero.social >__ In reality, since the difficulty is calculated as a function of the last 60 timestamps, usually ties are naturally broken up by a second alt block, but if the timestamp of the 1st differing block is the same, then the second blocks will have the same difficulty     

> __< rbrunner >__ I really wonder what second or third criterium you could possibly look at to break ties already at the first pair of competing blocks     

> __< rbrunner >__ beyond difficulty     

> __< rbrunner >__ Do you already have any candidates there, jeffro256?     

> __< j​effro256:monero.social >__ I propose something pretty simple: the BlockID. Since block hashing is a one-way function, you can't "cheat" by adding certain input bytes to get an expected output without trying it (AKA the whole basis of PoW). And trying to change the BlockID will invalidate the PoW with a probability of (difficulty-1)/difficulty     

> __< j​effro256:monero.social >__ The lower blockID wins the tie breaker     

> __< rbrunner >__ Sounds somehow almost too easy ...     

> __< rbrunner >__ But I can't come up with an argument against it.     

> __< v​tnerd:monero.social >__ Why does the existing code for this need to change?     

> __< 0​xfffc:matrix.org >__ I think I have to ask this question after the meeting since I am not sure I have a firm grasp of this. But wouldn't something like that fundamentally change our consensus algorithm?     

> __< rbrunner >__ I think that needs a hardfork to intruce     

> __< j​effro256:monero.social >__ Because the status quo makes orphan chains stick around for 1 block longer than they normally would and divides the network temporarily. This wastes PoW and makes the recent block order more uncertain     

> __< b​oog900:monero.social >__ difficulty is calculated using 720 block timestamps with a delay of 15 btw     

> __< j​effro256:monero.social >__ A hardfork is not needed since it is already an undecided problem which "side" the network takes based on ephemeral timings for two competing blocks with the same PoW     

> __< rbrunner >__ I don't understand. Don't tell me we don't have deterministic consensus, if that even exists     

> __< j​effro256:monero.social >__ You're right, I'm getting mixed up with the timestamp 60 block median from the other issue I was discussing last week. Same issue applies tho     

> __< j​effro256:monero.social >__ It's deterministic after a one block delay     

> __< rbrunner >__ Yes, and wouldn't it be a problem if half of all daemons see the question already as decided after one block, and the not-updated other half not?     

> __< j​effro256:monero.social >__ (most times unless the timestamps are the same)     

> __< r​ucknium:monero.social >__ IIRC Satoshi originally wrote bitcoin to follow the chain with the most blocks. That was a mistake. The bitcoin code was changed to follow the most PoW. It seems Monero has the "corrected" method for competing chains when the alternative chains have block length greater than 1, but the old rule when the block length is 1.     

> __< a​js_:matrix.org >__ How would the BlockID be generated?     

> __< j​effro256:monero.social >__ I'm just talking about about the current block id we already use (e.g. you can see the hash on xmrchain.net)     

> __< a​js_:matrix.org >__ The block hash?     

> __< j​effro256:monero.social >__ rbrunner7: that's exactly the problem: for 1 block (most of the time) reorgs, the network gets "sticky" and splits into 2, with both halfs not switching to the other's until another block comes on top of one side and breaks the tie     

> __< j​effro256:monero.social >__ Yes, block ID and block hash mean the same thing in this context. I use the term blockID to differentiate it from the PoW block hash     

> __< r​ucknium:monero.social >__ Why isn't it a good idea to use the PoW block hash? Lowest hash would win.     

> __< j​effro256:monero.social >__ That's also a good option     

> __< a​js_:matrix.org >__ How would two different hashes be compared to determine the “lower” one?     

> __< rbrunner >__ Just take them to be numbers     

> __< rbrunner >__ Very long numbers     

> __< j​effro256:monero.social >__ Rucknium: any deterministic property that is a result of a one-way function should work. I think I like using the lower PoW hash because it feels cleaner and can't be pre-scanned like the BlockID can     

> __< rbrunner >__ So a hardfork would not strictly be needed, but as long as miners are around that stubbornly continue to build on top of a chain the others already kind of discarded, it does not really work, seems to me     

> __< rbrunner >__ Because sometimes they will win     

> __< r​ucknium:monero.social >__ AFAIK, lower PoW hash also would not create any contradiction between the rule for +1 chains and +2,3,4 etc. Probably we don't want a block to be considered more valid at one point in time and less valid in another.     

> __< j​effro256:monero.social >__ Well yes, a miner can always happen to jump ahead of others doing weird things, but the idea is to reduce the amount of lost work under normal circumstances. Right now, nodes and miners which are being completely honest can have a temporary split and waste PoW     

> __< rbrunner >__ Anyway, that's probably a minor question whether this would or would not need a hardfork     

> __< r​ucknium:monero.social >__ jeffro256's proposed change also would give a little bit more safety margin to the N block lock on spending outputs     

> __< rbrunner >__ compared with the decision to try it at all     

> __< j​effro256:monero.social >__ rbrunner7: a minor question or a miner question?? ;)     

> __< rbrunner >__ You can't already say at some early point in a hash calculation that the resulting hash will be "big", if seen as a number, and stop early, right?     

> __< rbrunner >__ Only the very last step probably decides that     

> __< j​effro256:monero.social >__ Correct     

> __< j​effro256:monero.social >__ Last step is Blake2b of the register file     

> __< r​ucknium:monero.social >__ sech1: Do you have an opinion about jeffro256 's proposal?     

> __< sech1 >__ tldr? what proposal?     

> __< rbrunner >__ Maybe, surprisingly, nobody thought about this yet, because Bitcoin can't change anything anyway, and everything else is not that important, or sophisticated     

> __< j​effro256:monero.social >__ Using "lesser" top PoW hash as tiebroker between 2 chains with equal cumulative PoW     

> __< rbrunner >__ or already went PoS, like ETH     

> __< sech1 >__ so using some arbitrary random data (it is random) to resolve a tie?     

> __< sech1 >__ doubtful     

> __< sech1 >__ ideally, miner with better latency to the rest of the network will win     

> __< sech1 >__ and it will benefit the network as a whole - everyone will try to improve their latency and connectivity     

> __< sech1 >__ this random "tie break" rule can result in someone finding the alternative block a minute later and everyone else switching to it     

> __< sech1 >__ so first seen block is better solution     

> __< v​tnerd:monero.social >__ Yes, sech1, my thoughts here were mainly just if it's working now, don't break it     

> __< sech1 >__ plus some malicious miners can "steal" already mined blocks by trying to find better hash     

> __< j​effro256:monero.social >__ You could argue that, but you can already do that by mining an "old" blocks. You're wasting valuable compute time unless you have 51%     

> __< sech1 >__ it can open some new ways for 51% attacks     

> __< j​effro256:monero.social >__ Ostensibly the rest of the network is mining on the "better" block so you're racing against the network     

> __< j​effro256:monero.social >__ Same as if you're doing selfish mining     

> __< sech1 >__ current solution (first seen block) incentivizes miners to improve their network     

> __< sech1 >__ with random tie break rule, they can just ignore it and mine through Tor or whatever else slow network     

> __< r​ucknium:monero.social >__ But doesn't that give advantage to mining pools over solo miners?     

> __< sech1 >__ it will result in many more alternative chains, and possibly some more ways to attack     

> __< rbrunner >__ Not sure I understand the argument. Now it's also possible to arrive a full minute late with an alternative block, if there is no second one yet, no?     

> __< j​effro256:monero.social >__ They're still incentivized to mine through a fast network with random tie break because if they don't, then they're wasting mining time through network latency     

> __< sech1 >__ rbrunner if second block arrives a minute late, no one will start mining on top of it and it will lose     

> __< sech1 >__ with new system, it can disrupt the whole network and everyone will switch to this late block     

> __< rbrunner >__ I see     

> __< sech1 >__ plus I don't know how it will affect the difficulty adjustment     

> __< sech1 >__ if we start getting a lot of late blocks, so overall slower blockchain progress (more than 2 minutes per block on average)     

> __< sech1 >__ maybe it will spiral down into lower and lower network difficulty even if miner hashrate doesn't change     

> __< rbrunner >__ Interesting that nobody saw this arguments so far. Tricky stuff, only *looking* simple     

> __< r​ucknium:monero.social >__ AFAIK, mining on top of the most recent block you see has been PoW's principle from the beginning. I don't fully believe sech1's story, but he is more expert than me!     

> __< r​ucknium:monero.social >__ We don't know what the research papers say. Do we even know what bitcoin and its cousins do?     

> __< sech1 >__ not the most recent, the opposite     

> __< sech1 >__ I mean, the rule is to mine on top of the block with most PoW     

> __< sech1 >__ what to do in case of a tie - I haven't seen papers on that     

> __< sech1 >__ why is the current solution bad?     

> __< j​effro256:monero.social >__ 2 miners submit block at roughly equal time, network gets split in 2 undecided pieces until next block comes around     

> __< r​ucknium:monero.social >__ The meeting has gone past the hour mark. We'll end here. jeffro256 : Maybe make a GitHub issue on this?     

> __< j​effro256:monero.social >__ Thanks everyone!     

> __< 0​xfffc:matrix.org >__ And it is good idea to have related paper list to this issue. I believe there should be a substantial amount of papers with detailed data about this behaviour. Maybe we can do a literature review.     

> __< 0​xfffc:matrix.org >__ Thanks everyone.     

> __< j​effro256:monero.social >__ I'd react with a thumbs up but emoji banned     

> __< sech1 >__ currently, network splits don't happen too often - once every few thousand blocks only https://paste.debian.net/hidden/a8e8591e/   

# Action History
- Created by: Rucknium | 2024-02-26T23:26:55+00:00
- Closed at: 2024-03-06T16:23:58+00:00
