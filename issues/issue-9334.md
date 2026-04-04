---
title: '[Proposal] Change how transactions are broadcasted to significantly reduce
  P2P bandwidth usage '
source_url: https://github.com/monero-project/monero/issues/9334
author: Boog900
assignees: []
labels:
- proposal
- daemon
created_at: '2024-05-20T15:37:23+00:00'
updated_at: '2024-08-28T14:04:52+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
monerod uses dandelion++ to propagate txs around the network, this happens in 2 stages: stem and fluff. This proposal will only affect txs in the fluff stage.

When monerod receives a fluff tx, it will queue it for broadcasting to every peer except the one that sent it to us first, it doesn't matter if the peer(s) need it or not.

Because monerod sends the whole tx blob this is extremely inefficient, as the majority of the time the peer already has the tx.

## The Proposal

Instead of sending the whole tx-blob just send the hash and allow the peer to request the tx if they need it. This requires 2 new P2P messages:  `TxPoolInv`, `RequestTxPoolTxs` (names not important for now).

Adding support for these P2P messages should be done before changing how txs are broadcasted.

### `TxPoolInv`

This message will contain a list of new tx hashes and will be used when fluffing txs instead of `NewTransactions` which is currently used. 

When a node receives this it will request the txs with `RequestTxPoolTxs` if they are not in the tx-pool.

### `RequestTxPoolTxs`

This message will also contain a list of tx hashes. When a peer receives this message it should look in the _public_ tx pool and respond with as many txs as possible in a `NewTransactions` message.

A peer should not be punished for not responding to a `RequestTxPoolTxs` as the tx(s) could have been dropped from the peers pool.

## How inefficient is the current method?

Using the same technique as was done in the [Erlay paper](https://arxiv.org/abs/1905.10518) we can work out the expected number of wasted broadcasts: 

Each tx is sent _at least_ once along each connection, most of time it's more. If the number of nodes in the Monero network is N then the number of links is 12N as each node by default makes 12 outbound connections, then the number of redundant broadcasts is 12N - N = 11N.

So this means that ~90% of current tx broadcasts are redundant. Although we can't drop the 90% number without introducing a protocol like Erlay, we can redefine what a broadcast is. This would also lay the ground work for potentially adding Erlay in the future although that is not what this proposal is for.

To validate this I ran some tests on a local, fully synced, Monero node (monerod), the node was set to keep 12 outbound connections and 0 inbound.

In 2 hours 30 minutes I collected around 250MBs of data, in which there were 96268 tx broadcasts.

When you send a tx to a peer, if the peer doesn't also send the tx you know you were the first to send that tx to them, if they do send the tx as well you were not the first to send it to them.

So if a tx is sent more than once in a connection I added the amount of times it was sent to the total wasted. In total I got 90562 wasted broadcasts, I didn't take into account re-broadcasts which happen after 5 mins because they don't happen too often.

The total size of the wasted data: 200MB.

With the new method those 90562 wasted broadcasts would be tx hashes, and the 5706 valid broadcasts would require 2 tx hashes which comes to just over 3MB of data.

So I think we could save ~75% of the currently used p2p bandwidth. (250-53)/250 = 0.78. Under heavy load, like seen in the spam waves recently, this percentage should be higher.

## Other benefits

I suspect the current broadcasting method is what lead to nodes getting killed: #9317. 
 

# Discussion History
## SChernykh | 2024-05-20T16:19:22+00:00
> Instead of sending the whole tx-blob just send the hash and allow the peer to request the tx if they need it.

Bad wording maybe? What is really needed is to track which peer has sent each tx id to us, and don't send them the full blob back. Because if you send only the tx hash to everyone first, it will spam unnecessary messages before sending full blobs to peers which haven't seen this tx.

Although sending tx hashes to everyone first can save on broadcasts from them to you, so it makes sense.

## SChernykh | 2024-05-20T16:26:09+00:00
One issue I see with this approach, is while it saves the bandwidth, it will double the latency. Instead of `peer1 -> tx -> peer2`, 
there will be `peer1 -> hash -> peer2 -> request tx -> peer1 -> tx -> peer2` - a full round trip time is added.

Maybe some dynamic algorithm which chooses what to do, based on the current available bandwidth, will be better. For example, sending full tx to 2-3 random peers, and sending only hashes to all other peers - this will ensure fast fluff phase, and a reasonable bandwidth.

## Boog900 | 2024-05-20T16:30:16+00:00
> What is really needed is to track which peer has sent each tx id to us, and don't send them the full blob back. Because if you send only the tx hash to everyone first, it will spam unnecessary messages before sending full blobs to peers which haven't seen this tx.

> Although sending tx hashes to everyone first can save on broadcasts from them to you, so it makes sense.

Also we don't immediately broadcast txs that we receive, we add them to a queue with a randomized timer, so it is still wasteful as some of our peers would potentially have the tx without having sent it yet.

> One issue I see with this approach, is while it saves the bandwidth, it will double the latency

This is true, if this is seen as a problem we can decrease the average fluff timer. Although I don't think the added latency would require this.



 

## Boog900 | 2024-05-20T16:31:06+00:00
> Maybe some dynamic algorithm which chooses what to do, based on the current available bandwidth, will be better. For example, sending full tx to 2-3 random peers, and sending only hashes to all other peers - this will ensure fast fluff phase, and a reasonable bandwidth.

I think decreasing the fluff timer would be better.

## Boog900 | 2024-05-20T16:35:49+00:00
I will just mention stem phase should stay using the current method, so we don't increase latency there, as it would have more impact because the tx is only sent to 1 peer at a time.

## SChernykh | 2024-05-20T16:38:20+00:00
I just checked the code, and the fluff timer is currently at 5 seconds, so an additional round trip delay doesn't really matter. But I'd wait for comments from people who know Dandelion++ better.

## vtnerd | 2024-05-20T16:40:21+00:00
What about the privacy implications? You'll probably have to "lie" during the stem phase (or the path could be leaked), and during the fluff phase this still might help in identifying the stem path ... no? It's not dead simple, but at the same time it's leaking information that is currently unavailable.

## SChernykh | 2024-05-20T16:47:52+00:00
@vtnerd Do you mean some node could spam "Request TX ID" to everyone, and try to observe TX propagation in real time? Yes, that seems too dangerous for Dandelion++ integrity.

## Boog900 | 2024-05-20T16:49:11+00:00
> What about the privacy implications? You'll probably have to "lie" during the stem phase

Yes you would lie, but it's currently possible to pull this kind of attack of now as monerod will immediately fluff stem txs it receives twice from _any_ connection. Allowing someone to send stem txs that it has received to loads of nodes and seeing which immediately fluff.

IIRC we lie for some other requests as well.

> fluff phase this still might help in identifying the stem path ... no

I don't _think_ so, for a tx to enter the fluff stage it has to be seen twice in stem or once in fluff, so I can't see a way to exploit this.

I will just mention that any attack would first require the tx id.

Also this method of tx propagation is what Bitcoin uses, which is what the d++ protocol was made for. 


## Boog900 | 2024-05-20T16:51:49+00:00
> Do you mean some node could spam "Request TX ID" to everyone, and try to observe TX propagation in real time? Yes, that seems too dangerous for Dandelion++ integrity.

You can just do this with fluffy blocks, send a fluffy block containing a tx id and if they don't request it, they have it 

## SyntheticBird45 | 2024-05-20T17:03:03+00:00
> I don't think so, for a tx to enter the fluff stage it has to be seen twice in stem or once in fluff

Sending an already existing transaction in stem mode trigger the fluff mode => We imply by this logic that the transaction should already have been fluff to the network otherwise the node wouldn't have it in the first place.

Meaning, we're supposing (from a threat model perspective) that a bad actor shouldn't have the Tx ID in the first place. And I think this is a safe assumption. 

How is a bad actor supposed to collect the Tx ID from a stem tx ? It have to be part of the stem path. Best it can do is broadcasting this stem to every node and eventually triggering a fluff from nodes prior to itself in the path. If the stem broadcast triggers multiple nodes, then it can't distinguish which one is the first. If only one node is triggered then it is the first node. But it is already something assumed by D++ and is possible without these additional messages. So it shouldn't cause any privacy downgrades per say

## SChernykh | 2024-05-20T17:03:34+00:00
Right, so if there is already a way to do this, then replacing all tx broadcasts with "tx hash broadcasts first" should be safe, assuming that nodes lie both in stem and fluff phases.

- When in stem, they lie that they don't know this tx (request a full tx every time). 
- When in fluff, they lie sometimes with some high enough probability

Lying when in fluff is needed to confuse possible attackers - they won't be sure if some node knows a tx or not.

## jeffro256 | 2024-05-20T17:04:18+00:00
> You can just do this with fluffy blocks,

TBF, the node could theoretically check PoW before requesting the missing transactions, so the tracing attack would require doing PoW (a time intensive calculation) before tracing (a time sensitive operation). 

## SChernykh | 2024-05-20T17:05:56+00:00
@jeffro256 no need for fluffy blocks and PoW, there is already a protocol message to straight up request a tx id. If I understood it right.

## Boog900 | 2024-05-20T17:10:48+00:00
> Lying when in fluff is needed to confuse possible attackers - they won't be sure if some node knows a tx or not.

When a tx has been fluffed it is as good as public, no need to lie, only stem txs need to be hidden.

For a tx to be in fluff mode a node must see it in fluff mode or see a stem tx twice, meaning the attacker should not be able to find the stem route.

> no need for fluffy blocks and PoW, there is already a protocol message to straight up request a tx id. If I understood it right.

IIRC I don't think there is a request for a txpool transaction?

## jeffro256 | 2024-05-20T17:24:26+00:00
> IIRC I don't think there is a request for a txpool transaction?

There's `NOTIFY_GET_TXPOOL_COMPLEMENT`, but that only returns TXIDs that the requester *doesn't* mention and that are already in fluff phase. 

> When a tx has been fluffed it is as good as public, no need to lie, only stem txs need to be hidden.

Not being an expert in Dand++, this statement seems like it should be true. The point of Dand++ is to hide the originator node of a transaction, which the stem phase accomplishes. Once it is out of the stem phase and flooding the network, I don't know why we would need to lie about whether we know the tx or not. The only information that would give the attacker is how close my node is to the first fluffer. 

## Boog900 | 2024-05-20T17:33:36+00:00
> There's NOTIFY_GET_TXPOOL_COMPLEMENT, but that only returns TXIDs that the requester doesn't mention and that are already in fluff phase.

Ah yeah, that would be even worse as you don't even need the TXID first 

## SChernykh | 2024-05-20T17:36:05+00:00
In this case yes, lying in fluff phase doesn't make sense because it's already possible to get mempool contents (transactions in fluff phase) from each node.

## jeffro256 | 2024-05-20T17:37:02+00:00
Why would it ever make sense to lie in fluff phase theoretically? 

## SChernykh | 2024-05-20T17:43:21+00:00
I thought it was impossible to know which node knows which tx until it broadcasts it to you. So lying in fluff phase would maintain this property. But it turned out it's already possible.

## vtnerd | 2024-05-20T17:52:49+00:00
@SChernykh 

> @vtnerd Do you mean some node could spam "Request TX ID" to everyone, and try to observe TX propagation in real time? Yes, that seems too dangerous for Dandelion++ integrity.

Yes. An attacker node A would get a notification from node B that a new tx was observed, then node A (attacker) asks node C for the tx. This can be mitigated by only responding to a node that you previously sent the txid too, but requires more state tracking (and memory usage). Since the nodes will "lie" in the stem phase, this may be enough to thwart the attack (and make it similar to the already existing case).

@Boog900 
>> What about the privacy implications? You'll probably have to "lie" during the stem phase
>
> Yes you would lie, but it's currently possible to pull this kind of attack of now as monerod will immediately fluff stem txs it receives twice from any connection. Allowing someone to send stem txs that it has received to loads of nodes and seeing which immediately fluff.
>
> IIRC we lie for some other requests as well.

The target node doesn't respond to the attacker node directly (the tx is never relayed back); the attacker only knows a fluff occurred _somewhere_ in the network. Although a slim chance, another attacker could've targeted another machine in the same way, and so your target wasn't the initiator of the fluffing. The randomized delay timers per link should help hide the source of the fluff too.

After some thought, I think this txid request is no worse than this - iif the node lies during the stem phase.

>>fluff phase this still might help in identifying the stem path ... no
>
> I don't think so, for a tx to enter the fluff stage it has to be seen twice in stem or once in fluff, so I can't see a way to exploit this.
>
> I will just mention that any attack would first require the tx id.

Yes. I was thinking that an attacking node could fluff, and then try to immediately determine who had the tx. This would be similar to the existing fluff attack you mentioned, except the response would be immediate instead of randomly delayed. I don't think you can do much after some further thought though.

> Also this method of tx propagation is what Bitcoin uses, which is what the D++ protocol was made for.

I thought about this, this is another decent argument in favor of the proposal. Although it doesn't mean that the D++ authors overlooked something. We may need to investigate what Bitcoin does here too - does it respond immediately to such a request or does it delay? IIRC, it just does an immediate response.

>> Do you mean some node could spam "Request TX ID" to everyone, and try to observe TX propagation in real time? Yes, that seems too dangerous for Dandelion++ integrity.
>
> You can just do this with fluffy blocks, send a fluffy block containing a tx id and if they don't request it, they have it

This isn't the same though. You cannot "choose" when todo this attack - you have to wait until you find a valid PoW hash (and if not, the logic probably needs changing).

@jeffro256 
> Why would it ever make sense to lie in fluff phase theoretically?

It depends on how the RPC is setup. In the most dead-simple way, you ask for a txid, and the node responds if it has the tx. An attacker would then need to be selected in the stem phase (which depends on the D++ settings), and then just probes other nodes for the tx. If the blackhole delay is long enough, the entire stem can be revealed. While it doesn't guarantee finding the source, the D++ talks about hiding txes in the stem phase, etc. The attacker should only know the prior hop in the stem, not the entire stem.

## jeffro256 | 2024-05-20T18:03:30+00:00
> If the blackhole delay is long enough, the entire stem can be revealed.

Ah, I think I see. If the stem nodes wait too long to tell other nodes they know about the transaction after the fluff period, then they will be the only nodes claiming that they don't know about the transaction?

## Boog900 | 2024-05-20T18:08:54+00:00
> We may need to investigate what Bitcoin does here too - does it respond immediately to such a request or does it delay

I don't think we need to delay, the sender would have already added their own delay.

Delaying in my mind doesn't do anything, the node will still know we wanted the tx.

> This isn't the same though. You cannot "choose" when todo this attack - you have to wait until you find a valid PoW hash (and if not, the logic probably needs changing).

I am pretty sure you can do this without valid PoW.



## vtnerd | 2024-05-20T18:13:54+00:00
>> This isn't the same though. You cannot "choose" when todo this attack - you have to wait until you find a valid PoW hash (and if not, the logic probably needs changing).
> 
> I am pretty sure you can do this without valid PoW.

The complement request? I forgot about that one, this new proposal is basically equivalent to that.

## Boog900 | 2024-05-20T18:31:38+00:00
> The complement request? I forgot about that one, this new proposal is basically equivalent to that.

yes but also you can send a fluffy block and the peer will request missing txs even if the PoW is invalid, the node will lie and say it doesn't have stem txs though.

## vtnerd | 2024-05-20T21:13:24+00:00
@Boog900 
>>The complement request? I forgot about that one, this new proposal is basically equivalent to that.
>
> yes but also you can send a fluffy block and the peer will request missing txs even if the PoW is invalid, the node will lie and say it doesn't have stem tts though.

Yes, I see what you are saying now, I would argue this is a bug in the current implementation (the node should check PoW first afaik). Although, I'm not sure of the "fallout" from making this subtle change.

@jeffro256 
>> If the blackhole delay is long enough, the entire stem can be revealed.
>
> Ah, I think I see. If the stem nodes wait too long to tell other nodes they know about the transaction after the fluff period, then they will be the only nodes claiming that they don't know about the transaction?

No, during the stem phase you just probe other nodes for the txid. Only the stem nodes know about the txid and return a response. It requires that the attacker be chosen as a stem node itself though, and the parameters for D++ matter a lot.

A sybil attack on the Grin network showed that this isn't terribly difficult, especially when the fluff probability is **low** (where the stem is typically longer). In this case, they were trying to undo the MimbleWimble tx combining (where inputs/outputs from multiple txes are combined into a single tx). Since a sybil node was often selected during the stem phase, they were able to undo that privacy feature entirely in many cases. I don't recall the success rate percentage unfortunately, and the writeup was on Twitter (so I am trusting a random Twitter person). However, their technique and numbers were all reasonable.

## Boog900 | 2024-05-20T23:07:57+00:00
> It depends on how the RPC is setup. In the most dead-simple way, you ask for a txid, and the node responds if it has the tx. An attacker would then need to be selected in the stem phase (which depends on the D++ settings), and then just probes other nodes for the tx. If the blackhole delay is long enough, the entire stem can be revealed. While it doesn't guarantee finding the source, the D++ talks about hiding txes in the stem phase, etc. The attacker should only know the prior hop in the stem, not the entire stem.

I am unsure how this attack would work. Are you suggesting a black hole attack, while constantly probing _every_ peer? This would reveal one of the stems (at random), the first embargo timer to fire, but I don't think it would reveal the others and seems very invasive/ pretty impossible to be constantly probing every peer. I think you could get the same result just by passively connecting to every peer and waiting to see which fluffs first.

The reason I think it would only reveal one stem peer is once the embargo timer fires it will start fluffing to all connections not giving a chance for the other stems embargo timers to fire.

> No, during the stem phase you just probe other nodes for the txid. Only the stem nodes know about the txid and return a response. It requires that the attacker be chosen as a stem node itself though, and the parameters for D++ matter a lot.

They shouldn't return a response as the tx would be in their stem pool, right? 

The original question was for why we should lie in the fluff stage: 

`Why would it ever make sense to lie in fluff phase theoretically?`

> A sybil attack on the Grin network showed that this isn't terribly difficult

I don't know about this particular attack but Grin used (might still use I would have to check) a constant embargo timer, so the original node is always the one to fluff in a black hole.

## vtnerd | 2024-05-21T16:35:59+00:00
> I am unsure how this attack would work. Are you suggesting a black hole attack, while constantly probing every peer? This would reveal one of the stems (at random) but I don't think it would reveal the others and seems very invasive/ pretty impossible to be constantly probing every peer. I think you could get the same result just by passively connecting to every peer and waiting to see which fluffs first.

I agree this would be a noisy attack. This could be mitigated if you were only interested in certain outputs or IP addresses. FCMP would make this limited approach less viable.

A passive attack should be difficult, that's the purpose of D++.

> The original question was for why we should lie in the fluff stage:
>
> Why would it ever make sense to lie in fluff phase theoretically?

There's just never a good reason for a node to request a txid during the stemphase, it will always be from an attacker/spy trying to gain information. A node should only request a txid from a node that sent it a txid fluff first. Enforcing this strict rule is probably too much code and memory, but lying during stemphase is fairly easy.

As per your other comments about it being similar to a fluff leak: a node that receives a stem tx then fluffs was either part of the stem phase or is fluffing all txes. An attacker/spy could send another tx orginating with them to determine which case occurred, but then there is the case that this targeted node recently switched to fluff mode. An attacker could just spam a node to learn about the epoch settings, but this is way more spammy/active attack.

If this leak via spamming txes is a concern, I have a few ideas, but it will break from the algorithms in the D++ paper a bit.

> I don't know about this particular attack but Grin used (might still use I would have to check) a constant embargo timer, so the original node is always the one to fluff in a black hole.

I probably shouldn't have brought up Grin, because this attack wasn't really related to the discussion here.

## Boog900 | 2024-05-21T21:40:07+00:00
> I agree this would be a noisy attack. This could be mitigated if you were only interested in certain outputs or IP addresses. FCMP would make this limited approach less viable.
>
> A passive attack should be difficult, that's the purpose of D++.

I should have been more clear, I meant doing a black hole attack and then passive listening for the first node to fluff would give the same result. Nodes who have the tx in the stem stage will lie and say they do not have the tx so I don't think probing would allow you to gain any more information on the stem path than just passively listening for the first to fluff during a black hole.

>  A node should only request a txid from a node that sent it a txid fluff first. Enforcing this strict rule is probably too much code and memory, but lying during stemphase is fairly easy.

This is true, however I don't think an attacker would actually gain any information from knowing a node has a tx in the fluff stage.

A node with the tx in the stem phase will lie and a node with the tx in the fluff stage would have to have received it twice or received it from another node that fluffed it. 

> As per your other comments about it being similar to a fluff leak: a node that receives a stem tx then fluffs was either part of the stem phase or is fluffing all txes. An attacker/spy could send another tx orginating with them to determine which case occurred, but then there is the case that this targeted node recently switched to fluff mode. An attacker could just spam a node to learn about the epoch settings, but this is way more spammy/active attack.

True, although I don't think you would have to send too many txs for this to work. First you would launch a supernode, that connects to all peers and monitor which ones are sending fluff txs, epochs last 10 mins with a little bit of randomization added on. Then when you have a stem tx send it to all nodes you have not seen fluff recently, and for the ones who fluff immediately send a test tx straight after to see if the node is fluffing txs, still invasive to do this for every tx but feasible if you only want to target a subset. 

> If this leak via spamming txes is a concern, I have a few ideas, but it will break from the algorithms in the D++ paper a bit.

In Cuprate we keep track of nodes who have sent us a stem tx and if the same node sends the tx twice we fluff, this should stop the finding stem routes attack.
 
 



## vtnerd | 2024-05-23T15:54:49+00:00
> This is true, however I don't think an attacker would actually gain any information from knowing a node has a tx in the fluff stage.

I agree.

> In Cuprate we keep track of nodes who have sent us a stem tx and if the same node sends the tx twice we fluff, this should stop the finding stem routes attack.

`monerod` does something similar, except it fluffs when _any_ node sends the tx twice via stem. I believe that came from the original D++ paper - it was the stem loop case.

> True, although I don't think you would have to send too many txs for this to work. First you would launch a supernode, that connects to all peers and monitor which ones are sending fluff txs, epochs last 10 mins with a little bit of randomization added on. Then when you have a stem tx send it to all nodes you have not seen fluff recently, and for the ones who fluff immediately send a test tx straight after to see if the node is fluffing txs, still invasive to do this for every tx but feasible if you only want to target a subset.

Yes, this is a weak point in D+. The only mitigation I can think of is to switch to fluff mode in an epoch after you've been forced to fluff once. But this probably has some downsides too.

## Boog900 | 2024-05-24T23:48:15+00:00
> Yes, this is a weak point in D+. The only mitigation I can think of is to switch to fluff mode in an epoch after you've been forced to fluff once. But this probably has some downsides too.

This attack only works because nodes fluff if they receive a stem tx twice from _any_ connection, if this was no longer possible then the attack doesn't work.

Right now you can blackhole a tx, send it to every node you have not seen fluff recently, then for those that fluff send a test tx to see if they are fluffing. This should reveal the nodes in the stem path.

If we switched to only fluff after the same node sends a tx twice then this should no longer be possible.

> monerod does something similar, except it fluffs when any node sends the tx twice via stem. I believe that came from the original D++ paper - it was the stem loop case.

Yeah it was a footnote, one of the D++ authors made this issue related to it though: https://github.com/gfanti/bitcoin/issues/15

## vtnerd | 2024-05-25T18:26:22+00:00
> This attack only works because nodes fluff if they receive a stem tx twice from any connection, if this was no longer possible then the attack doesn't work.

I see what you mean, but your proposal also explicitly deviates from the paper - this isn't some unplanned edge case neglected by the paper. I need to think about the "fallout" some more.

> Right now you can blackhole a tx, send it to every node you have not seen fluff recently, then for those that fluff send a test tx to see if they are fluffing. This should reveal the nodes in the stem path.

The phrase "send it to every node you have not seen fluff recently" downplays the difficulty in determining whether a node is in stem or fluff epoch. You mentioned an active spam attack previously, and I think this is required to determine the state of a node.

Assuming this active attack is worth changing behavior - I think a better fix would be to change how the fluffing occurs. Make it difficult for an attacker to determine where the initial fluff originated. The rule change would be to _never_ fluff back to an upstream stem node peer. Currently a node will fluff to upstream stem node if someone else originated the fluff. I think this the big leak that needs fixing, not the stem-loop attack. We may also want to change the randomized fluff timers, again to help obfuscate the origin of the fluff.

> Yeah it was a footnote, one of the D++ authors made this issue related to it though: https://github.com/gfanti/bitcoin/issues/15

Again, I think you just confirmed that `monerod` is following the spec here.

## Boog900 | 2024-05-28T23:27:22+00:00
> The phrase "send it to every node you have not seen fluff recently" downplays the difficulty in determining whether a node is in stem or fluff epoch

Yeah my bad, it would not be as easy as I made out there.

Although that part was not necessary for the attack, that was just to weed out some of the nodes, so we have less to test.

Unless I am missing something it would still be possible to send a test tx (unknown to the network) along with the stem tx to every node, nodes in fluff state will fluff both txs and nodes in the stem path would only fluff the stem tx not the test. It would be possible that one of the stem path nodes would receive the test tx before their fluff timer fires, but then we can use the `fluff to upstream stem node if someone else originated the fluff` info leak to find out if this was the case.

This requires 1 supernode. If from a peer, the node:
- only receives the test -> the peer was in the stem path and we caused it to fluff the tx
- gets both test and stem -> the peer was not in stem path, they got fluffed from another node
- gets neither ->  the peer was not in stem path, this peer is in fluff mode.

I don't think any other state is possible, assuming all fluff txs are propagated to every node and the test tx is unknown to the network.

That should only require one test tx for each tx you want to find the nodes in the stem path for, you could probably batch stem txs together in a single message to make it less than 1 test tx per tx.

> I think this the big leak that needs fixing, not the stem-loop attack

In isolation I would say neither one is a big leak.

If the `fluff to upstream stem node if someone else originated the fluff` info leak is fixed, this is just waiting for another way to tell stem-loop peers and fluff peers apart in an efficient way. IMO we should aim to remove all information leaks.

> We may also want to change the randomized fluff timers, again to help obfuscate the origin of the fluff.

I would recommend moving to the exponential distribution, it's what Bitcoin uses and should make the fluff times a lot more random. However, it would cause some connections to go a while without fluffing, which means an even longer fluff queue for that connection, while the queue is tx bytes I don't think this would be a good idea. 

Moving to the exponential distribution _may_ reduce tx propagation time as well. 

> your proposal also explicitly deviates from the paper - this isn't some unplanned edge case neglected by the paper

> Again, I think you just confirmed that monerod is following the spec here.

It deviates from the prototype implementation documented in the paper, the footnote in question: `Our implementation enters fluff mode if there is a loop in the stem`. I wouldn't say this is part of the D++ spec.





## Rucknium | 2024-08-23T21:18:31+00:00
**TL;DR: There are existing methods to query a node's fluff-phase transaction pool. This proposal would add another one. Querying transaction pools could have privacy impacts, especially as transaction volume grows.**

## Privacy of fluff phase

This question has been asked a few times in this thread: "Would an adversary gain any useful information if an honest node revealed its fluff-phase txpool contents on demand?" IMHO, the answer is "Yes."

Diffusion, the fluff-phase spreading algorithm of Dandelion++, provides some obfuscation of the source of a transaction. Fanti & Viswanath (2017) simulate diffusion on a 2015 snapshot of the bitcoin p2p network. Nodes in this network had an average of 8 connections each. When a simulated spy node established one connection to each honest node, the probability of detecting the true source of the transaction using a first-timestamp/first-spy estimator was 30 percent (Figure 8).

The Fanti & Viswanath (2017) simulation is similar to the case where one out of nine (11 percent) of nodes are spy nodes that establish connections in the same way that honest nodes do. Theorem 2 of Venkatakrishnan, Fanti, & Viswanath (2017) says the best privacy that _any_ transaction spreading protocol can achieve is to limit the probability of an adversary detecting the true transaction source to $p$, the share of spy nodes on the network. The stem phase of Dandelion++ achieves the $p$ lower bound "for certain classes of Byzantine adversaries" (Fanti et al. 2018). 

Comparing diffusion to the Dandelion++ stem phase, with the share of malicious nodes at 11 percent, diffusion would give an adversary a 30 percent probability of detecting the source of a transaction. The stem phase would give that adversary an 11 percent probability. Diffusion isn't nearly as good as the Dandelion++ stem phase, but it doesn't give the adversary 100 probability of detecting the source of a message, either.

## Possible attacks by leveraging node txpool contents

There are at least two ways that public knowledge of fluff-phase txpool contents can help an adversary:

### Black holes forcing fluff embargo timers to fire

Fanti et al. (2018) discuss the "black-hole" attack against Dandelion++: A malicious node receives a stem-phase transaction and refuses to relay it to another node, i.e. the transaction goes into the black hole node and doesn't come out again. If a malicious node does this, the transaction will never reach an honest node in its fluff epoch and would never reach nodes throughout the network. To prevent a malicious node from stopping transaction propagation through black hole attacks, all nodes that handle stem-phase transactions (including the source node) set a random timer that eventually expires if the nodes do not see the transaction again in the fluff phase. On timer expiry, the node will broadcast the transaction in fluff phase.

Let Node $X$ be a node that relays a stem-phase transaction to a malicious node that black-holes the stem-phase transaction.  With knowledge of nodes' fluff-phase txpool contents, the adversary would know if Node $X$ was the first to broadcast the transaction in fluff phase when its embargo timer expired. Its embargo timer expiring does not necessarily mean that it was the true source of the transaction, but the expiry adds evidence to that hypothesis. Furthermore, the length of time it takes for the first embargo timer to expire reveals statistical information about the number of nodes that handled the stem-phase transaction. Earlier expiry suggests that many nodes handled the stem-phase transactions. Later expiry suggests that few or even one node handled the transaction in stem phase. @Boog900 makes the same point [here](https://github.com/monero-project/monero/pull/9295#issuecomment-2067710461). If the adversary knows that Node $X$ did _not_ broadcast the transaction in fluff phase, that's also useful information to the adversary. The adversary can rule out Node $X$ as the possible source and put the node that did broadcast the transaction in fluff phase at the top of its list of likely sources of the transaction.

### Network inference from cascades

In the last fifteen years, many papers about "network inference from cascades" have been published. In these papers, the problem of network inference is that an observer knows the nodes in the network graph, but not the edges that connect them. This is the same knowledge set about the Monero network that an adversary would have. The observer collects data on the time of arrival of a large number of messages ("cascades") at each node. From these cascades, the observer estimates which nodes are connected to each other. Prokhorenkova, Tikhonov, & Litvak (2022) has a recent summary of many of these statistical estimators.

An adversary can know the time of arrival of transactions to each node on the network if it is able to query nodes' txpools without limit. Therefore, the adversary could try to use a network inference estimator to discover the network's edges.

Knowledge of the network's edges would help an adversary learn the stem-phase subgraph. An adversary could use the stem-phase subgraph estimate to leverage more powerful de-anonymization techniques against Dandelion++ transaction privacy. See section "How much does p2p network topology discovery help an adversary link a transaction to an IP?" of my comment [here](https://github.com/monero-project/monero/pull/9218#issuecomment-2260917643). Knowledge of network topology also can make it easier to perform 0-conf double spending, network partitioning, and eclipse attacks. See Section VIII-B "Topology Inference Attacks" of Franzoni & Daza (2022) for discussion.

The network inference estimators need many cascades to reliably discover network edges. I am not sure how many transactions would be required to discover Monero's network, but I think it may be an order of magnitude higher than current transaction volume, keeping the current number of nodes and edges unchanged. According to some Monero log data, the median live time of a connection on mainnet is about 45 minutes. An adversary would have to leverage only transactions in a limited time window before the network re-arranges itself and the data becomes stale. Right now there are about 800 transactions broadcast per 45 minutes. There are about 10,000 nodes according to `monero.fail` and probably an average of 24 edges per node (two times the default number of outgoing connections).

The network inference estimators are diverse. Their models make assumptions about continuous/discrete time, message transmission probability, shape of the network, choice of estimator accuracy metric, etc. I am not ready to summarize the large literature on this, but I will take one example to get started. Pouget-Abadie & Horel (2015) propose an estimator for discrete-time models. Their estimator needed 2,000 cascades to achieve an [F1 score](https://en.wikipedia.org/wiki/F-score) of 80 percent on a network of 300 nodes with an average of 54 edges per node. Pouget-Abadie & Horel (2015) explains theoretical results (its own and of others) on the approximate number of cascades needed to reliably discover network edges. Under some conditions, an estimator needs $O(s \log(n))$ cascades, where $s$ is the number of edges of the node with the most edges in the network and $n$ is the number of nodes on the network.

The $O()$ order estimate of the number of cascades is interesting because it suggests that network inference with transaction arrival timestamps would become more feasible as transaction volume rises. Assume that the number of nodes on the network grows at the same rate as the growth of transaction volume. This assumption would be roughly true if (1) each user makes a constant number of transactions, (2) the growth of transactions is due to new users, and (3) new users boot up new nodes in the same proportion as old users. Since $s$ is roughly set by the default outgoing connections setting, it does not change. With these assumptions, the number of transactions would grow in proportion to $n$, but the number of transactions needed to infer edges would grow at a slower rate in proportion to $\log(n)$. Eventually the number of transactions would exceed the threshold to reliably estimate the network edges. If new users (with their new transactions) set up new nodes at a probability lower than old users, growing transaction volumes would make it even easier to estimate the network edges.

There is some research on this problem in the cryptocurrency setting. Neudecker, Andelfinger, & Hartenstein (2016) estimate the edges of the bitcoin network by deploying spy nodes and passively listening for the timing of transactions received from honest peers. Their technique is not the same as gathering the timestamp of arrivals at all nodes, which is the technique of the network inference from cascades set of papers. This paper does not cite the network inference from cascades literature even though their problem setting is similar. The technique of Neudecker, Andelfinger, & Hartenstein (2016) was based on bitcoin's pre-diffusion transaction propagation protocol, called "trickle". In a later paper (Grundmann, Neudecker, & Hartenstein 2019), the authors write "Furthermore, changes made to the propagation mechanism of the reference client Bitcoin Core in 2015 [to diffusion] render this method [Neudecker, Andelfinger, & Hartenstein (2016)] much more difficult nowadays." They do not elaborate about exactly how much less effective the Neudecker, Andelfinger, & Hartenstein (2016) method may be against diffusion.

I haven't found papers that specifically analyze the privacy of gossip protocols that enable pulling (instead of pushing) messages. Bellet, Guerraoui, & Hendrikx (2020) analyze push protocols and speculate on pull protocols: "Yet, we expect pull [privacy] guarantees to be even worse...because curious nodes could stop suspecting all nodes that they have pulled and that did not have the rumor."

## Querying txpool contents

A few ways to query a node's fluff-phase transaction pool already exist. The proposed `TxPoolInv` would add another one.

1) `NOTIFY_GET_TXPOOL_COMPLEMENT` was already mentioned in this thread. It requests all txpool contents of a node except for transactions explicitly listed in the `NOTIFY_GET_TXPOOL_COMPLEMENT` message. AFAIK, this is only used by nodes under normal operation when they re-join the network after rebooting. This use-case makes sense of course, because their peers would not normally send them old txpool transactions that had finished propagating.

2) The `/get_transaction_pool` JSON-RPC `monerod` endpoint. A node will respond with their txpool. When in restricted mode, the response will omit the `receive_time` field, but the approximate receive time can be determined by polling the node constantly. According to some data I collected from a few nodes' `/get_peer_list` responses, about 25 percent of nodes on the network have an RPC endpoint available.

3) The `/getblocks.bin` binary RPC monerod endpoint [allows](https://github.com/monero-project/monero/pull/8076) wallets to request txpool contents incrementally.

4) The proposed `TxPoolInv` could be used to query txpool contents as follows. An adversary deploys many spy nodes on the network. When one of the spy nodes receives a new transaction, the adversary sends a `TxPoolInv` with this fresh transaction's TXID to as many nodes as possible. If a node responds with the proposed `RequestTxPoolTxs` message that it needs the transaction, the adversary can note this fact and choose to not send the transaction. Assuming no rate limits, an adversary can constantly poll a node with `TxPoolInv` until the node says that it no longer needs the transaction. The time that the node says it no longer needs the transaction is the approximate time that the node received the transaction from an honest node for the first time.

## Options

Possibly, injecting random noise into txpool requests could thwart attempts to learn the source of fluff-phase transactions and the edges of the network graph. Nodes could add a random delay to responses. Or nodes could respond immediately, but randomly feign ignorance about some recently-received transactions.

The Erlay paper (Naumenko et al. 2019) says:

> Even though in Erlay timing attacks by observing low-fanout flooding are not feasible, an attacker would be able to perform them through reconciliations. To make timing attacks through reconciliations more expensive to perform, we enforce every peer to respond to reconciliation requests after a small random delay (in our implementation, a Poisson-distributed random variable which is on average $T_{ri}$ = 1 seconds), which is shared across reconciliation requests from all peers, and we rate-limit reconciliations per peer. This measure would make Erlay better than BTCFlood [i.e. diffusion] at withstanding timing attacks.

The effect of Erlay's reconciliation is similar to Monero's `NOTIFY_GET_TXPOOL_COMPLEMENT`, except reconciliation is bi-directional.

The magnitude of the noise to be injected in non-propagation methods like `NOTIFY_GET_TXPOOL_COMPLEMENT`, `/get_transaction_pool`, and `/getblocks.bin` could be small. It may be sufficient to set the noise size to about the length of time it takes for a transaction to propagate throughout the network. Injecting noise into methods that determine propagation time like `TxPoolInv` would be trickier.

According to my analysis of fluff-phase transaction arrival times at a sample of nodes (Rucknium 2023), "About 50 percent of all transactions arrived at all five Monero nodes within a two-second interval. 95 percent all transactions arrived at all five Monero nodes within a five-second interval." Simulations by Naumenko et al. (2019) estimate the network spreading time on a Bitcoin network with 30,000 nodes and 8 outgoing connections to be about four seconds. Manshadi & Misra (2016) and Manshadi, Misra, & Rodilitz (2020) provide differential equations that can predict spreading time on exactly $k$-[regular](https://en.wikipedia.org/wiki/Regular_graph) networks and networks with heterogeneous but bounded degrees, respectively. If all nodes were to be reachable (i.e. no nodes with closed ports) and all nodes follow the default 12 outbound connections, the Monero network would be approximately 24-regular.

These papers could help determine the amount and type of noise necessary for production-grade privacy: Bellet, Guerraoui, & Hendrikx (2020); Chakraborty, Verma, & Singh (2020); Huang, Jin, & Dai (2020); Wilinski & Lokhov (2020); Wilinski & Lokhov (2023); Woo, Ok, & Yi (2020).

An alternative, simple, but maybe not-so-optimal option to reduce bandwidth usage is to keep Monero's fluff-phase protocol, but modify it so that connection timers that exceed some threshold do not relay a transaction. Late timers would be relaying a transaction to a peer that likely already has the transaction because the transaction would have spread throughout the network already. The downside of this method is that it is possible for some poorly-connected nodes to fail to receive the transaction. (Of course, they would get the transaction when it is confirmed in a block later.) Noise could still be added to the existing ways to query a node's txpool.

Say that the non-relay threshold is set so that half of timers do not relay a transaction. For an exponential timer with rate 1/5 (i.e. on average, timers expire once every 5 seconds), timers would not relay a transaction if the timer exceeded about 3.5 seconds. Since each connection of each node would have only 50 percent probability of sending them a transaction, the probability that a node with only 12 connections would not receive the transaction from any of its connections would be about 0.02 percent. That's the probability mass at 0 of a binomial distribution: `dbinom(x = 0, size = 12, prob = 0.5)`. That may be an acceptable miss rate, but it only reduces bandwidth usage by 50 percent.

If the bandwidth usage were reduced by 75 percent (i.e. the estimated bandwidth savings in this #9334 proposal), then the miss rate would be much higher. Each node's connection would have just a 25 percent probability of relaying the transaction. Again using the binomial distribution, the probability that a node with 12 connections would miss a specific transaction would be about 3.2 percent.

## References

Bellet, A., R. Guerraoui & H. Hendrikx. (2020). Who started this rumor? Quantifying the natural differential privacy guarantees of gossip protocols. International Symposium on Distributed Computing (DISC), 2020. http://researchers.lille.inria.fr/abellet/papers/disc20.pdf

Chakraborty, B., Verma, S., & Singh, K. P. (2020). Temporal Differential Privacy in Wireless Sensor Networks. Journal of Network and Computer Applications, 155, 102548.

Fanti G & Viswanath P (2017) "Anonymity Properties of the Bitcoin P2P Network"

Fanti, G., Venkatakrishnan, S. B., Bakshi, S., Denby, B., Bhargava, S., Miller, A., & Viswanath P (2018). "Dandelion++: Lightweight cryptocurrency networking with formal anonymity guarantees."

Franzoni, F., & Daza, V. (2022). "SoK: Network-level attacks on the bitcoin p2p network." IEEE Access, 10, 94924–94962.

Grundmann M, Neudecker T, Hartenstein H (2019) "Exploiting transaction accumulation and double spends for topology inference in bitcoin."

Huang, Y., Jin, R. & Dai, H. (2020) "Differential Privacy and Prediction Uncertainty of Gossip Protocols in General Networks."" https://research.ece.ncsu.edu/wp-content/uploads/sites/25/papers/Differential_Privacy_and_Prediction_Uncertainty_of_Gossip_Protocols_in_General_Networks.pdf

Manshadi, V. &  Misra, S. (2016) "A Generalized Bass Model for Product Growth in Networks."

Manshadi, V., Misra, S., & Rodilitz, S. (2020). "Diffusion in Random Networks: Impact of Degree Distribution." Operations Research, 68(6), 1722–1741.

Naumenko, G., Maxwell, G., Wuille, P., Fedorova, A., & Beschastnikh, I. (2019), "Bandwidth-Efficient Transaction Relay for Bitcoin."

Neudecker T, Andelfinger P, Hartenstein H (2016) "Timing analysis for inferring the topology of the bitcoin peer-to-peer network."

Pouget-Abadie, J. & Horel, T. (2015), "Inferring Graphs from Cascades: A Sparse Recovery Framework." Proceedings of the 32nd International Conference on Machine
Learning, Lille, France, 2015. JMLR: W&CP volume 37.

Prokhorenkova, L., Tikhonov, A., & Litvak, N. (2022), "When Less Is More: Systematic Analysis of Cascade-Based Community Detection." ACM Transactions on Knowledge Discovery from Data (TKDD), Volume 16, Issue 4 Article No.: 78, Pages 1 - 22. https://arxiv.org/pdf/2002.00840

Rucknium (2023). "Centralized Mining Pools are Delaying Monero Transaction Confirmations by 60 Seconds." https://rucknium.me/posts/monero-pool-transaction-delay/

Venkatakrishnan, S. B., Fanti, G., & Viswanath, P. (2017). "Dandelion: Redesigning the bitcoin network for anonymity."

Wilinski, M., & Lokhov, A.Y. (2020). Prediction-Centric Learning of Independent Cascade Dynamics from Partial Observations. International Conference on Machine Learning.

Wilinski, M., Lokhov, A. Y. (2023) "Learning of networked spreading models from noisy and incomplete data."

Woo, J., Ok, J., & Yi, Y. (2020). Iterative learning of graph connectivity from partially-observed cascade samples. Proceedings of the Twenty-First International Symposium on Theory, Algorithmic Foundations, and Protocol Design for Mobile Networks and Mobile Computing.

## Boog900 | 2024-08-28T14:04:51+00:00
The numbers I use in this comment, like some of the numbers from @Rucknium's comment, are based on fluff timers using the exponential distribution, not the poisson distribution, which is currently used. I believe we should move fluff timer to the exponential distribution.

### Black holes forcing fluff embargo timers to fire

>  With knowledge of nodes' fluff-phase txpool contents, the adversary would know if Node X was the first to broadcast the transaction in fluff phase when its embargo timer expired

This is a very expensive attack, needing to probe every node in the network at a rate which would allow querying a node before it has chance for any of its fluff timers to fire. If we assume the peer has 10 outbound connections not controlled by the adversary, the node would have a 50% chance of fluffing to one of those connections in 0.18s or less and an 86% chance of fluffing under 0.5s.

To initiate the attack you would need peers to initiate outbound connections to your node and then select your node for stemming txs. To do this at scale would not be easy. 

And then the reward from this attack, extra statistical information, is IMHO not great for the cost.

### Network inference from cascades

FWIW with enough connections to a node you would receive most fluff txs in a reasonable amount of time, without needing to spam requests for the pool/specific transactions to every node. With 5 *inbound* connections you would receive 63% of the txs in under 1 second, with 10 that number jumps to 86%. Obviously this doesn't give you pin-point receiving time, but neither would spamming requests in the real world and this would still be enough to make statistical guesses about the P2P graph with enough transactions.

Although maintaining multiple connections to every node would be a challenge, these attacks already require a single connection to every node while polling every nodes tx pools at a rate to beat the fluff timers.

IMHO it would be good to get some data on how effective the current diffusion protocol is at preventing these attacks and by how much adding extra noise changes the effectiveness of them before adding extra noise.

## Querying txpool contents

Some other ways not mentioned in that comment:

1. Fluffy missing tx requests, although this was already mentioned in another comment.
2. Double spend checks, we check for tx-pool double spends before checking other consensus rules. It would be possible to create an invalid tx which uses a key-image of a tx you want to check for, send this tx to a node, then if you disconnect they didn't have the tx,  and if you stay connected they had the tx (the invalid one was ignore for being a double spend). Although this attack was added in #9218, 9218 is needed for network security and it would still be possible to perform a timing attack based on the time to disconnect. This attack also exposes the stem pool. Preventing this attack would require checking all consensus rules before checking for double spends, although this would allow a DOS, where the attacker could spam a node with double spends that wont be accepted but the node will still do all the expensive crypto checks. It's also not just a statistical attack, this can be performed on a single tx to expose the nodes in the stem path it took.

> Assuming no rate limits, an adversary can constantly poll a node with TxPoolInv until the node says that it no longer needs the transaction.

FWIW Bitcoin will only send 1 request for a tx every 60 seconds: https://github.com/bitcoin/bitcoin/blob/2c7a4231db35060fa1ab66d29e8139f04edc85a4/src/net_processing.cpp#L104 Although this attack would still be possible with `RequestTxPoolTxs` unless we limited that message as well. A simple way would just be to not allow more requests than `TxPoolInv`s that we have sent to that node.

## Options 

> The magnitude of the noise to be injected in non-propagation methods like NOTIFY_GET_TXPOOL_COMPLEMENT, /get_transaction_pool, and /getblocks.bin could be small. It may be sufficient to set the noise size to about the length of time it takes for a transaction to propagate throughout the network. 

I would agree adding some noise to `NOTIFY_GET_TXPOOL_COMPLEMENT` could be beneficial with little downsides as it's only used once when the node has caught up to the network. Adding noise to `/getblocks.bin`, when the tx-pool is requested could also be a good idea, I'm guessing the tx-pool is only requested when caught up?

> the bandwidth usage were reduced by 75 percent (i.e. the estimated bandwidth savings in this #9334 proposal), then the miss rate would be much higher. Each node's connection would have just a 25 percent probability of relaying the transaction.

This would reduce tx relay bandwidth by 75% not total P2P bandwidth by 75%. Doing some rough calculations based on the data I put in the issue comment, about 212/250 MB was used for tx relay. To reduce bandwidth usage by the same amount you would need to skip fluffing 90%+ of txs.

# Action History
- Created by: Boog900 | 2024-05-20T15:37:23+00:00
