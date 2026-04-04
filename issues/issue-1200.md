---
title: Monero Research Lab Meeting - Wed 07 May 2025, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1200
author: Rucknium
assignees: []
labels: []
created_at: '2025-05-06T22:28:52+00:00'
updated_at: '2025-05-15T18:26:19+00:00'
type: issue
status: closed
closed_at: '2025-05-15T18:26:19+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/meeting.html?p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3. FCMP stressnet preparation.

4. [FCMP++ transaction weight formula](https://github.com/seraphis-migration/monero/pull/26). And PoW for high-input txs.

5. Web-of-Trust for node peer selection.

6. Unit test for implementation of [subnet deduplication in peer selection algorithm](https://github.com/Rucknium/misc-research/blob/main/Monero-Peer-Subnet-Deduplication/pdf/monero-peer-subnet-deduplication.pdf).

7. Any other business

8. Confirm next meeting agenda

Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#1197

# Discussion History
## Rucknium | 2025-05-12T15:04:16+00:00
Logs:

> __< r​ucknium:monero.social >__ Meeting time! https://github.com/monero-project/meta/issues/1200     

> __< r​ucknium:monero.social >__ 1) Greetings     

> __< v​tnerd:monero.social >__ Hi     

> __< rbrunner >__ Hello     

> __< a​rticmine:monero.social >__ Hi     

> __< c​haser:monero.social >__ hello     

> __< a​ntilt:we2.ee >__ seawas     

> __< j​berman:monero.social >__ *waves*     

> __< r​ucknium:monero.social >__ 2) Updates. When is everyone working on?     

> __< rbrunner >__ Better subnet de-duplication when connecting to peers, to connect to less "spy nodes". Made good progress in the last few days.     

> __< r​ucknium:monero.social >__ me: Working with rbrunner7  on subnet deduplication for peer selection and setting up tests. I took over as maintainer for the `IP` package on CRAN: https://cran.r-project.org/package=IP . My `xmrpeers` package depends on it: https://github.com/rucknium/xmrpeers , but it was removed from CRAN in January due to issues that I've now fixed (with some help from moneromooo ). Working o<clipped message     

> __< r​ucknium:monero.social >__ n a custom loss function for neural net classification of real spends when multiple decoy selection algorithms are used in the wild.     

> __< j​berman:monero.social >__ me: moving forward outstanding PR's, pushed a draft PR demonstrating memory safe FFI usage (https://github.com/seraphis-migration/monero/pull/39), currently working on removing the FCMP++ input limit for the alpha stressnet May 21st (we seemed to have solid support in favor of PoW-enabled relay for larger input txs >8 last MRL meeting, so that nodes don't expose a vector to hog CP<clipped message>     

> __< j​berman:monero.social >__ U verifying invalid FCMP++'s)     

> __< v​tnerd:monero.social >__ Me: finished lws-frontend subaddress support and restore from height. Currently working on tx construction for same frontend and x25519 updates for arm64     

> __< r​ucknium:monero.social >__ jeffro256: ping in case you want to join the meeting.     

> __< r​ucknium:monero.social >__ 3) FCMP stressnet preparation.     

> __< j​effro256:monero.social >__ me: successfully tested Carrot+FCMP transaction construction and scanning in the GUI wallet. Working on improving code quality wrt documentation and error handling     

> __< r​ucknium:monero.social >__ It has been brought to my attention that a few PRs intended to fix issues found on the last stressnet have not yet been merged into the main Monero repo.     

> __< r​ucknium:monero.social >__ ✅ mean merged. ❌ means not merged     

> __< r​ucknium:monero.social >__ ✅   [Blockchain: fix temp fails causing alt blocks to be permanently invalid](https://github.com/monero-project/monero/pull/9395)     

> __< r​ucknium:monero.social >__ ❌   [Daemons processing big blocks may bump against serializer sanity checks and fail to sync](https://github.com/monero-project/monero/issues/9388)     

> __< r​ucknium:monero.social >__ ✅    [tx\_pool: update internal data structure to boost::bimap.](https://github.com/monero-project/monero/pull/9376)     

> __< r​ucknium:monero.social >__ ✅    [cryptonote\_core: only verify txpool when the hardfork value has changed.](https://github.com/monero-project/monero/pull/9404)     

> __< r​ucknium:monero.social >__ ❌   [src: dynamic span, to calculate span limit dynamically](https://github.com/monero-project/monero/pull/9495)     

> __< r​ucknium:monero.social >__ ❌   [src: dynamic block sync size](https://github.com/monero-project/monero/pull/9494)     

> __< r​ucknium:monero.social >__ So, will the FCMP stressnet have these PRs, or not? If yes, then it would be assumed that these are necessary PRs to deploy before or at the time of the FCMP hard fork.     

> __< r​ucknium:monero.social >__ The three that have not been merged are important to be able to not have a netsplit when blocks are large, IIRC     

> __< j​effro256:monero.social >__ The last 2 *should* be less controversial IMO, and could probably be merged before then. But the "Daemons processing big blocks may bump against serializer sanity checks and fail to sync" is a little tricky in that directly increasing serialization limits directly increases area of attack for DoS     

> __< rbrunner >__ Looks like #9388 fell through the cracks, as nobody looked at the possible dangers of higher limits in detail ...     

> __< j​effro256:monero.social >__ > The three that have not been merged are important to be able to not have a netsplit when blocks are large, IIRC     

> __< j​effro256:monero.social >__ If anything it's the opposite for the 9388. Everyone having the same low limits means no netsplit, the block is just rejected outright. If people had *different* limits, that's what would actually cause a netsplit     

> __< j​berman:monero.social >__ would need to review these all in more depth     

> __< r​ucknium:monero.social >__ I recall differently.     

> __< rbrunner >__ Aren't connections drop after receiving big blocks with the current limits in place? If I remember correctly it's also a security issue     

> __< s​pirobel:kernal.eu >__ >Block sizes at this height were about 1.5MB. Then it banned some peers. The bans expired after 2 minutes because we set a new ban duration in the code.     

> __< r​ucknium:monero.social >__ Or maybe possible netsplit in both scenarios.     

> __< rbrunner >__ Problem is, the blocks were perfectly legit, just chock full with valid transactions     

> __< r​ucknium:monero.social >__ IIRC, what happened early in the stressnet was that miners started mining just on top of their own blocks because they started banning other miners with big blocks.     

> __< j​effro256:monero.social >__ True, might just be different types of net splits, I need to look at it again. I can imagine where the serialization limit is enforced when the packet is formatted a certain way, but if the packet changes, but contains the same block, it's accepted     

> __< b​oog900:monero.social >__ here is a PR increasing the limits: https://github.com/monero-project/monero/pull/9433     

> __< j​effro256:monero.social >__ Ah, makes sense     

> __< s​pirobel:kernal.eu >__ and another one https://github.com/spackle-xmr/monero/pull/12/files     

> __< b​oog900:monero.social >__ if its a fluffy block the number of txs sent depend on the number of txs already known     

> __< j​effro256:monero.social >__ Excellent point     

> __< rbrunner >__ Ah, yes, I now remember #9433. So we just did not achieve consensus there, and merged the bloody thing :)     

> __< j​effro256:monero.social >__ So it's deeper than just simply increasing limits, since the method by which it's limited inherently causes net splits     

> __< r​ucknium:monero.social >__ IIRC, things got bad when a node fell behind by more than one block. Then, probably, the node needed to do a normal full-block sync instead of a fluffy block sync.     

> __< rbrunner >__ Not sure whether the net will split, or whether the daemons with too-low limits for all the huge blocks simply stop working     

> __< r​ucknium:monero.social >__ And then got banned     

> __< b​oog900:monero.social >__ yeah I think to properly solve this we need a better epee bin impl     

> __< j​effro256:monero.social >__ Perhaps we could name this PR "Replace serialization functions"     

> __< rbrunner >__ Anyway, as I said, it's also a security problem, somebody could now spam the network so hard as to create mayhem because of those limits     

> __< s​pirobel:kernal.eu >__ are the epee limits to prevent a memory leak? what if all kind of throttling / banning  was removed and rethought from the ground up? it seems so entangled everywhere. be it rpc code, serialization, p2p     

> __< rbrunner >__ Good luck with replacing those functions :)     

> __< rbrunner >__ No, I think they are there to prevent out-of-memory attacks with specially crafted packets     

> __< rbrunner >__ There are some details in the PR discussion     

> __< r​ucknium:monero.social >__ IIRC, some of the limits were put in place to handle deserialization explosion during the December 2020 network attack.     

> __< rbrunner >__ at #9433     

> __< j​effro256:monero.social >__ Yeah what if we used a streaming serialization model instead of DOM? And maybe put it in a cool number PR number like 8867     

> __< r​ucknium:monero.social >__ AFAIK, a good solution would be to prevent deserialization explosion in the first place.     

> __< s​pirobel:kernal.eu >__ rbrunner: how come something like protobuf never runs into issues like this. what is wrong with epee? :D     

> __< b​oog900:monero.social >__ cuprate has no limits like this 😏     

> __< rbrunner >__ Maybe nobody feels like attacking protobuf?     

> __< rbrunner >__ And it's not possible to exhaust the memory with Cuprate?     

> __< rbrunner >__ If we just take out those limits, we don't have any either :)     

> __< r​ucknium:monero.social >__ Monero Unlimited     

> __< b​oog900:monero.social >__ We don't use a DOM, I don't want to say impossible but I don't know a way.     

> __< b​oog900:monero.social >__ or epee bin impl is also zero copy for the most part, using references into the original bytes.     

> __< j​effro256:monero.social >__ A couple things: most protobuf libraries are SAX instead of DOM meaning that they stream the data directly into the deserialized types and constrain that data to the type's requirements, which greatly reduces the funkiness of the packet you can send to a Protobuf deserializer. This is effectively what PR #8867 aims to do. Second, the epee binary format is a lot like JSON: it is se<clipped messag     

> __< j​effro256:monero.social >__ lf-describing and can have fields in any order with unlimited nesting. So even when you have a SAX-like API to deserialize epee binary format, you have to contend with jumping around in different places when deserialiing member fields or implement something like lookup tables. You also generally have to ignore valid key-values in objects when you don't know the name of the field, <clipped messag     

> __< j​effro256:monero.social >__ which means an attack can stuff a weird payload in there     

> __< v​tnerd:monero.social >__ Protobuf doesn't use a dom, so it partially prevents the issue, although it should still be possible to explode memory with a vector of strings     

> __< v​tnerd:monero.social >__ Protobufs also typically have smaller limits on total payload size, whereas we have a big buffer for block fetching     

> __< v​tnerd:monero.social >__ Like if we could limit the payload to 1mb, we probably wouldn't need to place additional limita     

> __< v​tnerd:monero.social >__ *limits     

> __< j​effro256:monero.social >__ It might cause a netsplit, but could a good long term option, when multiple blocks are fetched, be to stream the blocks one at a time over a keepalive connection, each limited to say, 1 MB? And the receiver would only deserialize the next packet after completely processing the former ?     

> __< s​pirobel:kernal.eu >__ (sounds a bit like grpc :D )     

> __< r​ucknium:monero.social >__ Some ideas have been proposed and discussed. I doubt this will be settled today. Next meeting, the PRs to be included in the alpha stressnet could be decided.     

> __< r​ucknium:monero.social >__ Any more issues for stressnet prep that should be discussed today?     

> __< a​rticmine:monero.social >__ What happens when the block size is over 1MB?     

> __< s​yntheticbird:monero.social >__ connection dropped     

> __< r​ucknium:monero.social >__ The #monero-stressnet:monero.social  room still exists. Some coordination can be done there. It is bridged to ##monero-stressnet on Libera IRC, I think.     

> __< a​rticmine:monero.social >__ So are we capping the block size?     

> __< rbrunner >__ Indirectly, yes     

> __< a​rticmine:monero.social >__ There is no consensus for this     

> __< rbrunner >__ And blow holes into the network as a second effect     

> __< a​rticmine:monero.social >__ Period This has to go.     

> __< j​effro256:monero.social >__ The other option would be to split a large block over multiple discrete packets, but this has another DoS effect: the node sits there waiting around for the 2nd packet, wasting RAM until the connection drop     

> __< s​yntheticbird:monero.social >__ akshually we could add some PoW for the block fragmentation     

> __< s​yntheticbird:monero.social >__ yes this is a mad idea     

> __< s​yntheticbird:monero.social >__ but i don't have a better one     

> __< b​oog900:monero.social >__ I have thought for a while that the P2P messages need to be rethought, we already currently have a cap on block size.     

> __< b​oog900:monero.social >__ everything needs to be able to broken down to sending 1 tx at a time as that is the thing that actually has a size limit     

> __< r​ucknium:monero.social >__ The stressnet continues to provide valuable feedback, even almost one year later.     

> __< a​rticmine:monero.social >__ That is a sensible idea     

> __< b​oog900:monero.social >__ things _can_ be batched but if they are too large they should be broken down, this also needs to happen on the response side as the requester often doesn't know the size of things they ask for     

> __< b​oog900:monero.social >__ i.e. someone asks for a block but that block is 500 MB, we need to send multiple messages to actually send the block     

> __< a​rticmine:monero.social >__ ... But still multiple packet connections are the norm on the Internet     

> __< b​oog900:monero.social >__ also things like the tx-pool request have to be a DOS if the tx-pool is huge, it can't be good to load all the txs into memory.     

> __< rbrunner >__ Uh, the tx pool is a whole other can of worms ...     

> __< j​effro256:monero.social >__ And when syncing a single block header to check PoW, you only need <96 bytes. The transaction list inside a block is actually a merkle tree, so you don't even need to send the entire transaction list at once     

> __< a​rticmine:monero.social >__ In fact more often than not the transactions may already be at the receiving end     

> __< b​oog900:monero.social >__ yeah let alone the fact now we send every tx, in full,when syncing not just the hashes.     

> __< b​oog900:monero.social >__ before we know the chain is even valid     

> __< j​effro256:monero.social >__ Exactly     

> __< b​oog900:monero.social >__ rename FCMP++ to Monero 2 and change everything?     

> __< s​yntheticbird:monero.social >__ I've the impression that in many aspects, the original monero code has been done the "naive way"     

> __< s​yntheticbird:monero.social >__ or maybe they were ultra optimistic     

> __< r​ucknium:monero.social >__ 4) FCMP++ transaction weight formula. And PoW for high-input txs. https://github.com/seraphis-migration/monero/pull/26     

> __< j​effro256:monero.social >__ I think they just hacked something together with 2013 cryptocurrency knowledge until it started working     

> __< j​effro256:monero.social >__ Which, like, fair     

> __< b​oog900:monero.social >__ they had to get the scam out quick     

> __< a​rticmine:monero.social >__ Bytecoin     

> __< r​ucknium:monero.social >__ So, it is thought that PoW for high-input txs is a good compromise that prevents the DoS attack vector of verification of invalid inputs proofs and allows high-input txs for good user/service experience.     

> __< r​ucknium:monero.social >__ So maybe everyone can be happy     

> __< rbrunner >__ Yes, somewhat surprisingly     

> __< r​ucknium:monero.social >__ At the cost of more protocol complexity     

> __< r​ucknium:monero.social >__ The RandomX difficulty threshold and the max allowable number of inputs is still to be decided, AFAIK. But maybe those exact values can wait until there are benchmarks on the optimized verification code.     

> __< a​rticmine:monero.social >__ I don't have a case against this POW thing over 8 inputs.. This being said large transactions will have to pay a higher minimum fee so that they don't depend on smaller transactions to do the scaling for them     

> __< a​rticmine:monero.social >__ As is the case bow     

> __< a​rticmine:monero.social >__ Now     

> __< a​rticmine:monero.social >__ Right now scaling is based upon 3000 bytes. After FCMP++ this will rise to 10000 bytes. Anything larger will need to pay a higher fee so that it can scale on its own     

> __< a​rticmine:monero.social >__ Essentially every transaction needs to pay a large enough fee so that it can pay the penalty at the start of the penalty     

> __< r​ucknium:monero.social >__ Is that at the minimum fee level (first tier), or a higher fee level?     

> __< a​rticmine:monero.social >__ The minimum fee is currently based upon 3000 bytes and will rise to 10000 bytes. So these large transactions will have to pay a higher minimum fee depending on their size     

> __< r​ucknium:monero.social >__ 5) Web-of-Trust for node peer selection.     

> __< r​ucknium:monero.social >__ flip flop gave some thoughts about this at last meeting     

> __< j​effro256:monero.social >__ Why isn't the minimum fee set as a factor of the weight of that transaction ?     

> __< a​ntilt:we2.ee >__ Some thoughts:     

> __< a​ntilt:we2.ee >__ a) We operate in an environment where a global actor may rent CPUs. I think in the long run relying on hashrate alone for consensus will be difficult. If solo-mining becomes more profitable that might raise the bar for an adversary.       

> __< a​ntilt:we2.ee >__ b) WoT: A naive rating system as in pgp key signing may backfire. I thought about the concept of "anchor nodes". Would it be feasabile to zk-proof good behaviour such as availability, contribution to consensus, or even taking on a watchdog role? The idea is that an adversary might have trouble faking such a track record.      

> __< a​ntilt:we2.ee >__ Just brainstorming.     

> __< r​ucknium:monero.social >__ https://libera.monerologs.net/monero-research-lab/20250430#c522508-c522510     

> __< a​rticmine:monero.social >__ This is the change that I will be proposing     

> __< rbrunner >__ Won't the introduction of FMCP++ take away a lot of the possible / plausible reasons of attacking / subverting the network, like the "spy nodes" now?     

> __< r​ucknium:monero.social >__ If I understand correctly, BTC has a ban score that raises if a node seems to be misbehaving. When ban score 100 (I think) is exceeded, the peer is banned. I think Monero does not have a ban score. An offense is either bannable immediately or not bannable.     

> __< rbrunner >__ Ah, no, trying to defeat Dandelion++ stays of course     

> __< r​ucknium:monero.social >__ Ban score is not exactly web of trust, but similar     

> __< a​rticmine:monero.social >__ The main attack it takes away is Flood XMR / black marble     

> __< r​ucknium:monero.social >__ Maybe IP-based de-anonymization is all that an adversary would have left, so more effort would go into it.     

> __< r​ucknium:monero.social >__ AFAIK, Nym has done interesting things in this area, since they have some mechanism to check if a mixnet node is actually providing the bandwidth it says it does. This check is necessary for their economic rewards to mixnet nodes.     

> __< a​rticmine:monero.social >__ True but Monero privacy uses the whole is greater than the sum of its parts     

> __< a​ntilt:we2.ee >__ no... worst case is Monero becomes sucessful ad adopted. Then the attack vector is 50% hashrate.     

> __< a​rticmine:monero.social >__ So completely breaking tracing will have an impact on IP address based attacks     

> __< r​ucknium:monero.social >__ And Tor does something like Nym to measure node bandwidth, but simpler I think. Maybe their method isn't trustless.     

> __< c​haser:monero.social >__ re `a)`: not relying on heaviest-aggregate-PoW as the fork choice rule on a PoW chain seems to be contradictory. I've been thinking about a short-term PoS overlay for reducing the n-block lock depth, but the eventual chain should follow heaviest-aggregate-PoW.     

> __< r​ucknium:monero.social >__ I don't think p2p web-of-trust could prevent a 51% attack.     

> __< a​ntilt:we2.ee >__ yeah, WoT is ot the way to go. I thought about the concept of "anchor nodes".     

> __< a​ntilt:we2.ee >__ *not     

> __< a​rticmine:monero.social >__ We have to be very careful reaching conclusions here regarding POW. Accounting for the value and cost of the heat produced by POW and environmental considerations strongly favor decentralization     

> __< a​ntilt:we2.ee >__ articmine:monero.social I am with you. Is solo mining profitable right now ?     

> __< a​rticmine:monero.social >__ It depends on the temperature outside     

> __< a​ntilt:we2.ee >__ I want some chinese miners, also.     

> __< r​ucknium:monero.social >__ By a standard economic argument, mining XMR is unlikely to be very profitable as long as it is only feasibly mined by CPUs. CPU mining allows free entry, which drive economic profits to zero.     

> __< r​ucknium:monero.social >__ On average     

> __< a​rticmine:monero.social >__ I January are you in Alice Springs, AU or Winnipeg, CA?     

> __< r​ucknium:monero.social >__ Solo mining vs pool mining are only different in the frequency of payouts, and therefore the risk.     

> __< c​haser:monero.social >__ "anchor nodes" turn economically incentivized, permissionless consensus into social consensus.     

> __< a​rticmine:monero.social >__ Or is the outside temperature 40 C or - 40 C?     

> __< a​ntilt:we2.ee >__ yes, thats my argument: adding a trust score to augment PoW -- in case of a 51% attack.     

> __< r​ucknium:monero.social >__ Having a rolling checkpoint would be a simpler 51% attack defense. It would require nodes to stay online to avoid being confused by which chain is the "correct" one.     

> __< a​ntilt:we2.ee >__ yes, thats my argument: adding a trust score to augment PoW -- in case of a 51% attack. It happened to Firo. They had to augment PoW with "masternodes"     

> __< c​haser:monero.social >__ how do you do that "augmentation"? the idea of PoW consensus is that you rarely if ever have to rely on social consensus, and social coordination happens outside the protocol. if you include it in the protocol, the anchors can 51% attack consensus for cheaper than adversarial hash power could.     

> __< a​ntilt:we2.ee >__ yes, i thought about "light nodes" to do that     

> __< a​ntilt:we2.ee >__ catch 2:2. The question is open.     

> __< c​haser:monero.social >__ this would add a novel liveness assumption to the consensus model, and it's exactly something that Nakamoto consensus is designed to partially remedy.     

> __< r​ucknium:monero.social >__ chaser: Right.     

> __< a​rticmine:monero.social >__ Still Monero defeated a 51% attack in 2018 with the ASIC dock.     

> __< a​rticmine:monero.social >__ Food for thought     

> __< a​rticmine:monero.social >__ Fork     

> __< r​ucknium:monero.social >__ This is in the bitcoin white paper abstract:     

> __< r​ucknium:monero.social >__ > Messages are broadcast on a best effort basis, and nodes can leave and rejoin the network at will, accepting the longest proof-of-work chain as proof of what happened while they were gone.     

> __< a​ntilt:we2.ee >__ I just want to raise awareness that the $ cost is about 500k per month to rent 5G hashes     

> __< r​ucknium:monero.social >__ So the block checkpoint defense is contrary to the bitcoin white paper protocol.     

> __< r​ucknium:monero.social >__ Arguably     

> __< a​ntilt:we2.ee >__ I'd like to see more rewards for miners.     

> __< r​ucknium:monero.social >__ Let's "officially" end the meeting here since we are 50 minutes past the hour, but feel free to continue discussing. Thanks everyone.     

> __< c​haser:monero.social >__ yes. notably, Nakamoto consensus can't answer what to do if you come online and see two equally heavy chains, or solve the problem of not hearing about a heavier chain, but it reduces the probability of those events considerably.     

> __< c​haser:monero.social >__ that you can achieve only through a higher inflation rate *while* the fiat price of XMR stays the same, or an absurdly high minimum fee requirement in the consensus. both are unlikely, especially the former. there is a very strong consensus on Monero's monetary policy, and the demand for XMR wouldn't increase in proportion to the added supply.     

> __< a​ntilt:we2.ee >__ You tough on an interesting point here... but I am so innocent, miners could get donations, right ?     

> __< c​haser:monero.social >__ if the $/second PoW "security budget" for Monero is too low compared to a level you'd prefer, I hear you. the way to improve on that is to make XMR more valuable through research, development, adoption, education, community building, UX improvements, and so on.     

> __< a​ntilt:we2.ee >__ Well, it could be a self-adjusting system, where the price of XMR rises with adoption, which in turn makes 51% attacks way harder to do, because hashrate increases. Thats an optimistic outlook. I like that.     

> __< c​haser:monero.social >__ they already can, but you can't make sure they'll use those funds for hashing. that would  require some kind of on-chain donation box that would drip its contents over time to the miners.     

> __< c​haser:monero.social >__ was there an actual 51% attack in 2018?     

> __< j​berman:monero.social >__ Going to share some preliminary thoughts on using groups of max 8-input membership proofs in a single tx for txs with more than 8 inputs, versus just using a single n-input membership proof     

> __< j​berman:monero.social >__ Pinging kayabanerve  (especially in case there are inaccuracies in here)     

> __< j​berman:monero.social >__ Pros:     

> __< j​berman:monero.social >__ 1) Constructing proofs for large-input txs takes forever (minute+ for 32-input+, and looks like potentially double digit minutes for >100-input proofs)     

> __< j​berman:monero.social >__ On those grounds alone it probably makes sense for each tx to have groups of max 8-input proofs. Maybe kayabaNerve has thoughts on potential optimizing for that scenario?     

> __< j​berman:monero.social >__ 2) Looking at preliminary verification times, max 8-input proofs make a lot of sense too, even ignoring the benefits of batched verification for multiple 8-input proofs being superior to the aggregate (mentioned by kayabaNerve)     

> __< j​berman:monero.social >__ E.g. a 64-input proof is taking 2.4s to verify, compared to 1.4s for 8, 8-input proofs individually verified (179ms each)     

> __< j​berman:monero.social >__ 3) There is also the benefit boog900 highlighted last MRL meeting: if an attacker wants to hog a node's CPU with invalid txs, for maximum damage, they could include all valid proofs except the last, which means they have to do additional work to construct valid individual proofs (have all valid proofs except the last to hog node resources). Constructing valid proofs is not an ins<clipped message>     

> __< j​berman:monero.social >__ iginifcant amount of computational work     

> __< j​berman:monero.social >__ 4) More conducive to multithreaded verification of single txs     

> __< j​berman:monero.social >__ Cons:     

> __< j​berman:monero.social >__ Proof size. A 128-input membership proof is expected to be 79232 bytes, versus 16, 8-input proofs is 153600 bytes     

> __< j​berman:monero.social >__ The former is pretty comparable to CLSAG. So we're talking about large input txs nearly doubling byte size     

> __< j​effro256:monero.social >__ Another benefit (or con?) that I haven't seen mentioned: it opens the door for collaborative multi-sender transaction building without the need for MPC as long as the inputs are grouped in different FCMPs. It wouldn't be very dependable since one of the parties need 8 contiguously ordered key images that don't overlap with the other party, so ....     

> __< j​effro256:monero.social >__ That is, without revealing the true spent output to the other party. If you don't care about that, you can always have the other party prove the FCMP for all inputs in the group.     

> __< j​effro256:monero.social >__ Although, if we write the code to support multiple FCMPs per transaction, we could likely trivially configure it so that the transaction creator can provide an arbitrary grouping of FCMPs (as long as they're of size <= 8). For example, if only a 2-in, the tx could provide 2 1-input FCMPs. That's actually sort of usable for collaborative transaction building     

> __< j​effro256:monero.social >__ There's the uniformity issue of allowing arbitrary groupings, though     

> __< j​effro256:monero.social >__ IDK just food for thought     

> __< j​effro256:monero.social >__ > There is also the benefit boog900 highlighted last MRL meeting: if an attacker wants to hog a node's CPU with invalid txs, for maximum damage, they could include all valid proofs except the last, which means they have to do additional work to construct valid individual proofs (have all valid proofs except the last to hog node resources). Constructing valid proofs is not an insi<clipped messag     

> __< j​effro256:monero.social >__ ginifcant amount of computational work     

> __< j​effro256:monero.social >__ On this, we can always shuffle the order in which we verify FCMPs so it's not predictable to the sender. Then in the best case (for us) we fail after the first FCMP. The attacker can only expect 1/2 of the FCMPs to verify on average     

> __< j​berman:monero.social >__ Yep^ that would make it even harder on attackers with the max 8-input proof construction     

> __< j​berman:monero.social >__ main point being the max 8-input groups obligates the attacker to do more computational work on their end to attack a node     

> __< j​effro256:monero.social >__ Depending on our threat model, this might be enough to thwart most of the DoS attacks without explicit PoW. Let's assume two things A) it is more expensive to prove a *valid* FCMP than to verify one, and B) we are okay with an 8-input FCMP verification worth of turnaround time before the sender must prove that they spent more work on this FCMP than we will take to verify it. If th<clipped messag     

> __< j​effro256:monero.social >__ e tx has 1 8-input FCMP, then we try this one and if it fails, ban the peer. If it has 2 FCMPs, then if the first fails, then ban the peer. If the first succeeds, and the second fails, ban the peer. We spent time verifying two FCMPs, but we know the attack spent time *proving* at least one FCMP, so they spent more time than us.     

> __< j​effro256:monero.social >__ This scheme could be hardened by rejecting very old FCMP reference blocks by consensus. IIRC, 3 days is the mempool timeout, so that could be the consensus timeout for FCMP reference blocks too. This would prevent building up FCMP work for weeks on end (or more) and dumping it all at once.     

> __< j​effro256:monero.social >__ This won't effect cold signers or other people who sign transactions very far in advance since FCMPs can always be proved after SA/L signatures     

> __< j​effro256:monero.social >__ This is also probably a good rule anyways to prevent silly wallet implementation mistakes like what happened with Wownero     

> __< b​oog900:monero.social >__ it would be sad to not be able to batch verification of these single tx FCMPs     

> __< j​effro256:monero.social >__ You could still batch them if they were inside a block for which PoW verification passed, i.e. during block sync     

> __< j​effro256:monero.social >__ As I see it though, I really can't recommend it for mempool txs     

> __< b​oog900:monero.social >__ It will be interesting to see timings if we are getting 1.4s for 64 inputs without batch verification, this could be pretty comparable to current CLSAG right? IIRC that was 1 second for the max size tx.     

> __< j​effro256:monero.social >__ A 16-input CLSAG takes 3.7ms to verify on my machine, so it would be ~237ms for 64 inputs, ~5.9x faster. But you would also have to include SA/L verification times in the FCMP++ measurement if you wanted to be fair to CLSAG...     

> __< j​effro256:monero.social >__ Sorry 16-*member*, not input     

> __< j​effro256:monero.social >__ Btw CLSAG verification time scales perfectly linearly by number of inputs, since they don't batch at all, so you can freely extrapolate the verification time for N CLSAGs based on the measurement for 1 CLSAG     




# Action History
- Created by: Rucknium | 2025-05-06T22:28:52+00:00
- Closed at: 2025-05-15T18:26:19+00:00
