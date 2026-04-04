---
title: Limit blocks to 32 MB, regardless of context
source_url: https://github.com/monero-project/research-lab/issues/154
author: kayabaNerve
assignees: []
labels: []
created_at: '2025-11-30T10:22:35+00:00'
updated_at: '2026-01-23T13:12:30+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
While the block size limit may be dynamically adjusted, regardless of the dynamic block size limit, the effective block size limit is to be `min(dynamic_block_size_limit, 32 * 1024 * 1024)` if this proposal is adopted.

This is due to the effective throughput of Monero nodes being such, as per the stressnet, and various parts of the Monero node assuming blocks do not become absurdly large (RPC, P2P limits) which 32 MB complies with yet still would cause a minimal batch size (blocks < 5) if any.

This proposal is made independently to any/all of the recent proposals on scaling due to their contention, yet this is simple, directly modeled after effective bandwidth limitations currently experienced, and still >100x the current penalty-free block size. While monerod may improve in the future, the protocol will also change in the future, making this only as constant as the protocol adopting it.

A sane static limit also simplifies the checking of blocks sent over the network, due to not requiring the context of the blockchain, whereas the current limit is infinite due to the miner transaction being unbounded (its own topic). After the unbounded miner transaction, the context-free limit is absurd due to blocks being allowed to have 0x10000000 transactions, which would be 268 GB if each transaction was just 1 KB.

# Discussion History
## Har01d | 2025-12-03T17:13:16+00:00
While 32 MB may look valid today, it may be become too low in a few years, but there will be a hard limit in place which would require a hard-forking change to be removed. This just introduces a risk of repeating the biggest Bitcoin's mistake while providing no benefit. Miners can have a "sane limit" by themselves, they're not stupid.

## kayabaNerve | 2025-12-03T19:54:21+00:00
There seems to be sufficient agreement on 90 MB from the prior meeting, due to how the node's expected behavior breaks at ~100MB anyways. This limit is expected to not be reached for several years under existing candidate scaling proposals, but prevents things from breaking unexpectedly, pending the necessary reworks and improvements to the P2P layer and RPC for things to not break (allowing removing this limit, required for safe and correcr operation).

https://github.com/monero-project/monero/pull/9433 was noted as a PR required (or a PR of similar effect) to update current serialization limits to accomodate such a limit.

## tevador | 2025-12-06T18:36:43+00:00
Here is the table of outcomes when block space demand reaches 100 MB depending on whether a 90 MB hard cap is introduced and whether a future hard fork happens that fixes the problem at 100 MB:

|              | Fixed by a future HF | Not fixed by a HF |
|--------------|----------------------|-------------------|  
|**90 MB limit**   | network operates normally | network is congested |
|**No limit**   | network operates normally | network breaks down |

The outcomes differ only if 100 MB block space demand comes before the 100 MB limitation is fixed with a future hard fork. In this case, a congested network is certainly better than a broken network, which speaks in favor of the 90 MB temporary limit.

> This just introduces a risk of repeating the biggest Bitcoin's mistake

Bitcoin didn't have a P2P protocol that would break at 1 MB. That limit was completely arbitrary.

In this case, we are talking about a limit that literally prevents the network from breaking down.

## Har01d | 2025-12-11T01:33:25+00:00
> In this case, we are talking about a limit that literally prevents the network from breaking down.

The solution to this issue should be fixing the 100 MB packet limit cap bug then, not introducing a new one. Monero is currently being advertised as having unlimited block size pretty much everywhere (including getmonero.org): you're breaking the social contract.

> which speaks in favor of the 90 MB temporary limit

If you want to introduce a temporary limit to buy time to fix some bugs, it should be coded as temporary, i.e., it should have an expiration date in the near future.

## tevador | 2025-12-11T05:21:45+00:00
> The solution to this issue should be fixing the 100 MB packet limit cap bug

Yes, everyone agrees with this. Do you volunteer? Fixing the bug requires rewriting parts of the P2P protocol, which is not a trivial fix and is a hard fork itself. The 90 MB cap is an interim solution.

I think an acceptable compromise would be to publish a bounty funded from the Monero general fund to fix the bug. If nobody takes the bounty before a specific date (e.g. March 31st, 2026), we go ahead with the hard cap at the FCMP hard fork.

> you're breaking the social contract.

The "social contract" is already broken. The fact is that monerod can't sync past a 100 MB block. We can either stick our head in the sand and pretend the problem doesn't exist, or we can introduce a temporary limit of 90 MB that prevents the network from breaking until the underlying issue is fixed.

> If you want to introduce a temporary limit to buy time to fix some bugs, it should be coded as temporary, i.e., it should have an expiration date in the near future.

What would be the benefit of a fixed expiration date that can expire before the actual bug is fixed? Then we'd be back to square one with a breakable network.


## Har01d | 2025-12-11T21:52:23+00:00
> Yes, everyone agrees with this. Do you volunteer? I think an acceptable compromise would be to publish a bounty funded from the Monero general fund to fix the bug.

Yeah, a CCS project is a good idea. I can definitely chip in. By the way, why is it that imposing a hard cap doesn't require a bounty?

> The "social contract" is already broken. The fact is that monerod can't sync past a 100 MB block.

It's not. Obviously, there's no such thing as "unlimited blocks" in practice. But the current contract is that there's no defined cap in the protocol, and miners decide on the current **safe** *soft* limit.  This proposal shifts the power balance from miners to developers and breaks the said social contract.

> What would be the benefit of a fixed expiration date that can expire before the actual bug is fixed? Then we'd be back to square one with a breakable network.

Surely it's possible to estimate the needed time to fix it? Otherwise it can stay forever, like it did on Bitcoin. You can't guarantee the limit will be lifted. It's a much larger risk than the bogus "rogue miners will suddenly decide to nuke the network" theory. And, technically, if I understand it correctly, the network wouldn't even go down; only miners mining blocks over 100 MB would.

## kayabaNerve | 2025-12-11T22:05:06+00:00
1) This already is a limit in the code. It's just thrown around and not handled properly.
2) New nodes would fail to sync the network as-is. This doesn't just mean miners of a certain size wouldn't have their blocks accepted. The RPC would also start to break.

## Har01d | 2025-12-11T23:20:46+00:00
> This already is a limit in the code

Yet you won't find any mention of this limit anywhere. All the existing articles and materials on dynamic blocks don't mention this limit. It's a bug that needs to be fixed.

Remember the 184 billion bitcoins bug? Well, the code allowed that many bitcoins! Yet not the social contract. It's the same here. It was a bug there, it it a bug here.

This proposal (and any other proposal that sets a hard cap on the block size) breaks one of the most important Monero features and further centralizes Monero around its development team.

## tevador | 2025-12-13T14:26:49+00:00
> By the way, why is it that imposing a hard cap doesn't require a bounty?

You are a developer, so it should be clear to you that adding a limit is a task for maybe 1 hour, while reworking the block sync protocol is a project for at least a few weeks.

> But the current contract is that there's no defined cap in the protocol

There is, and has been since 2014:

https://github.com/monero-project/monero/blob/296ae46ed8f8f6e5f986f978febad302e3df231a/contrib/epee/include/net/levin_base.h#L71

> Otherwise it can stay forever, like it did on Bitcoin. You can't guarantee the limit will be lifted.

There is already a limit of 100 MB. If your argument is that there is a probability that Monero will never hard fork again like Bitcoin, then the 100 MB limit will stay forever anyways, so your argument is moot.

> And, technically, if I understand it correctly, the network wouldn't even go down; only miners mining blocks over 100 MB would.

It's the other way around. Nodes that are online at the time the 100 MB block is produced will continue, but new nodes coming online won't sync past that block, possibly leading to a chain split. In any case, the result is a broken network.

> Remember the 184 billion bitcoins bug? Well, the code allowed that many bitcoins! Yet not the social contract. It's the same here. It was a bug there, it it a bug here.

Exactly. This proposal is for us to put a sanity limit so the "184 billion bitcoins bug" cannot be triggered maliciously (in this case, the 100 MB block bug). You are arguing that doing nothing (i.e. leaving the bug exploitable) is better than the sanity cap.

Here is the list of things to do, ordered from the best to the worst:

1. Fixing the bug (reworking the sync protocol)
2. Temporary 90 MB limit
3. Doing nothing

> This proposal (and any other proposal that sets a hard cap on the block size) breaks one of the most important Monero features and further centralizes Monero around its development team.

I fail to see how a sanity limit 10% lower than the existing breakage limit will centralize Monero, even if Monero never hard forks again.






## fluffypony | 2025-12-13T14:33:19+00:00
> Here is the list of things to do, ordered from the best to the worst:
> 
> 1. Fixing the bug (reworking the sync protocol)
> 2. Temporary 90 MB limit
> 3. Doing nothing

Is there a middle ground of sorts where we put a 90mb limit in for 2-4 years post-fork-height, and that gives enough time to flesh out changes to the sync protocol to handle larger blocks + gives the Internet time to expand? I suspect that the ongoing deployment of LEO satellites for Internet etc. will make this block size more feasible down the road, but our aim is to reduce the risk of harm in the interim.

The other way to do this is to massively increase tx fees to make such an attack prohibitively expensive for a motivated, well-resourced attacker, but I'm hopeful that the people arguing against this thread are also not arguing for a tx fee increase.

## tevador | 2025-12-13T14:54:50+00:00
@fluffypony Here is the table of possible outcomes for a 90 MB limit with and without a fixed expiration date:

|              | Fixed in 2 years | Not fixed in 2 years |
|--------------|----------------------|-------------------|  
|**90 MB for 2 years**   | OK | exploitable network |
|**90 MB until fixed**   | OK | OK but limited |

The weighted outcome is better for the limit without a fixed expiration date.

## Har01d | 2025-12-13T15:57:42+00:00
> There is, and has been since 2014:
> https://github.com/monero-project/monero/blob/296ae46ed8f8f6e5f986f978febad302e3df231a/contrib/epee/include/net/levin_base.h#L71

I've specifically asked that many times on Twitter if someone is able to present at least one (one!) article (not a line in the code) or an explainer video, or some book, or anything else mentioning that there's a 100 MB limit. And I've got no response. Yet every existing material on Monero says that there's no hard cap on the block size, and miners can go up without hitting any limits. It's everywhere like that!

https://www.getmonero.org/get-started/faq/:
> Does Monero have a block size limit?
> No, Monero does not have a hard block size limit

https://docs.getmonero.org/technical-specs/:
> Block size
> dynamic
> maximum of two times the median size of the last 100 blocks (2 * M100)

This is the social contract, not some buggy code.

If you argue that a buggy line in the code is the social contract, that also means that, according to you, splitting the chain and "a broken network" on reaching 100 MB is also the expected behavior.

I wonder if Cuprate has this "limit"?

> You are arguing that doing nothing (i.e. leaving the bug exploitable) is better than the sanity cap.

Why would miners go over the 100 MB line and break the network? They won't. The sanity cap already exists, and it's called mining incentives.

> I fail to see how a sanity limit 10% lower than the existing breakage limit will centralize Monero, even if Monero never hard forks again.

90 MB limits Monero at 12 million transactions (FCMP) per day. That's a very low number. Monero is going Bitcoin's route.

> The weighted outcome is better for the limit without a fixed expiration date.

So first you say it's a bug that requires "a few weeks" to be fixed, and here you argue that 2 years might be not enough? You want to cap Monero at 12 million transactions a day possibly forever: this is a much larger threat to Monero that imaginary miners going over a safe soft limit.

## tevador | 2025-12-13T22:22:42+00:00
> I've specifically asked that many times on Twitter if someone is able to present at least one (one!) article (not a line in the code) or an explainer video, or some book, or anything else mentioning that there's a 100 MB limit. And I've got no response. Yet every existing material on Monero says that there's no hard cap on the block size, and miners can go up without hitting any limits. It's everywhere like that!
> If you argue that a buggy line in the code is the social contract, that also means that, according to you, splitting the chain and "a broken network" on reaching 100 MB is also the expected behavior.

I'm not saying the 100 MB limit is a "social contract". It was probably unintentionally introduced by the original Bytecoin developers, which explains why it's not documented anywhere.

> Why would miners go over the 100 MB line and break the network? They won't.

Are you speaking for all miners (present and future ones)? All it takes is one malicious miner with the intention of destroying Monero.

> So first you say it's a bug that requires "a few weeks" to be fixed, and here you argue that 2 years might be not enough?

I said it's a project for at least a few weeks. It doesn't mean it will be done a few weeks from now. It could plausibly take years until it's implemented, tested, reviewed and merged.

> You want to cap Monero at 12 million transactions a day possibly forever: this is a much larger threat to Monero that imaginary miners going over a safe soft limit.

Straw man argument.

We both agree that the best solution is to fix the 100 MB bug. But do you agree that a 90 MB limit (in place until the 100 MB bug is fixed) is better than leaving the network vulnerable?


## Har01d | 2025-12-14T00:37:41+00:00
> It was probably unintentionally introduced by the original Bytecoin developers, which explains why it's not documented anywhere.

I'm glad that we agree that it's an undocumented leftover rather than a "feature".

> Are you speaking for all miners (present and future ones)? All it takes is one malicious miner with the intention of destroying Monero.

It's not me who's speaking for miners, it's the incentive system. The majority of miners (51%) are presumed to be honest and rational in a PoW system, otherwise it fails and "breaking the network" with a "big block" becomes a quite insignificant problem. If there's a real risk of breaking the network, miners should simply set their soft caps in a way that the median size won't cross the 50 MB mark while the bug is being fixed. That's it.

As for adversarial conditions, could you please provide a plausible scenario in which "one malicious miner" can destroy Monero? For a "big block" attack an adversary would need to have at least 51% of the total hashrate, and (if the current median is not at exactly around 50 MB) they'll have to wait for a lot of time. With the current floor level of 300 kB that would take months because of the 100k-block median. It's simply cheaper and faster to doom the network with a simple 51% attack.

> Straw man argument

If the limit is not programmed as temporary, can you guarantee it will be removed? No.

> We both agree that the best solution is to fix the 100 MB bug. But do you agree that a 90 MB limit (in place until the 100 MB bug is fixed) is better than leaving the network vulnerable?

> You are a developer, so it should be clear to you that adding a limit is a task for maybe 1 hour, while reworking the block sync protocol is a project for at least a few weeks.

It's great that we agree that the 100 MB bug should be fixed.

And I have a super simple solution: if Monero is going to hard-fork anyways, instead of imposing a block size limit below 100 MB, increase the packet size limit from 100 MB to, say, 100 GB: that would simply require fixing several constants (and their types to stay compatible with 32-bit systems I guess). That wouldn't require "years" to complete. After that, we can put a temporary block size limit of 90 GB for the next 5 years to fix the bug.

I think that'd be a nice compromise:

- Fast to code (1 hour as you specified for that kind of change?)
- It's temporary, so everyone is happy, even those who might say that 99 GB is not enough
- Lots of time to fix the bug!
- No "broken network" possibility

Or maybe we can simply use UINT64_MAX instead of 100 GB — that would be like 18 exabytes — and forget about fixing this I guess. It's even faster to code as there will be no reason to code the block size limit anymore (at least at the current scale of the Internet).

Should I open a separate issue for this proposal? And while we're at it, we can also bump things like `CRYPTONOTE_MAX_TX_PER_BLOCK`.

## kayabaNerve | 2025-12-14T02:54:27+00:00
~~That'd presumably allow OOM killing every node on the network overnight and immediately end the network.~~ Since you're obviously qualified to speak on this, please write the PR yourself instead of further trying to convince us who simply don't understand the elegance of your solution.

@tevador I decided to bow out prior and would encourage you to not further spend your time here. Your view has already been clearly stated.

## Har01d | 2025-12-14T03:06:57+00:00
> That'd presumably allow OOM killing every node on the network

No, it won't, and you well know it, because miners will not be constructing blocks over some soft limit they will choose. Miners won't be nuking their network just for giggles.

The discussed "technical issue" was "the network will fall apart after 100 MB because there's a network packet bug", and now, when I've presented you with a simple solution to that, you're reverting to the good old "my Raspberry Pi won't handle running a node".

This is what I mean when I say that Monero is going Bitcoin's way with developers arbitrary deciding on a small scaling cap and breaking the social contract. A sad day for Monero.

## spirobel | 2025-12-14T06:23:01+00:00
[https://github.com/monero-project/monero/blob/48ad374b0d6d6e045128729534dc2508e6999afe/contrib/epee/include/net/levin\_base.h#L77](https://github.com/monero-project/monero/blob/48ad374b0d6d6e045128729534dc2508e6999afe/contrib/epee/include/net/levin_base.h#L77)

>`#define LEVIN_DEFAULT_MAX_PACKET_SIZE 100000000      //100MB by default after handshake`

  
Here is a compromise that resolves this issue: limit blocksize by 1/3 of`LEVIN_DEFAULT_MAX_PACKET_SIZE`

Notice the subtle distinction here: we don't define a constant, we make it dependent on the constant of how much the protocol can handle. 

The conversation around what LEVIN_DEFAULT_MAX_PACKET_SIZE should be, is defined by the very technical debate of how much the protocol can handle before it becomes unstable. Much different from the "blocksize debate". 

Arctic's concern of the temporary not being temporary is addressed this way. Monero's scaling is limited by the properties of its networking protocol.

That is the core part of the code base that affects scaling. All the other parameters are downstream from how much the protocol can handle. By tying the block size to levin capacity we make it explicit that once we change to a more efficient protocol, we can increase the throughput of the block chain. 

## kayabaNerve | 2025-12-14T11:58:04+00:00
@spirobel The goal is to disconnect block syncing from packets. Defining block size to fit within a packet is against that goal.

@Har01d If you allow 100 GB packets, even if i cant produce a 100 GB block, I can send you 100 GB of network traffic and demand you handle it on the spot. That's why this'd be an overnight OOM if you don't have the necessary RAM. Saying nodes shouldn't require 100 GB of RAM is distinct from saying a Pi 1 should be able to sync Monero.

The packet size, if anything, should be lowered while we sync blocks over multiple packets, that allowing raising the block size. It's shoving blocks into single packets that's the issue today and a bad design regardless tomorrow.

## vtnerd | 2025-12-14T17:29:04+00:00
One frustrating thing is I don't think people realize the engineering hours required to fix this to a satisfactory outcome. It's not simply changing a `#define` and re-compiling because of the OOM case many would experience. Every other coin (afaik) just requires more RAM for higher block sizes, but few want that outcome too.

This may require some LMDB magic (or some other file approach), but is clearly possible. Just going to take a while. I wish I put this in my latest CCS, to make it clear that I could spend cycles on this, but I didn't think about it when writing it. I guess I can call this a HackerOne/bug issue ...

## spirobel | 2025-12-17T10:37:01+00:00

https://libera.monerologs.net/monero-research-lounge/20251217#c627209

>vtnerd: @spirobel:kernal.eu: [github.com/monero-project/monero/bl…orages/levin_abstract_invoke2.h#L48](https://github.com/monero-project/monero/blob/48ad374b0d6d6e045128729534dc2508e6999afe/contrib/epee/include/storages/levin_abstract_invoke2.h#L48)
[02:45](https://libera.monerologs.net/monero-research-lounge/20251217#c627210)
br-m
vtnerd: thats probably what kaya is referencing. there are currently limits separate from total packet size in place

that means adding  another limit in the form of max blocksize can not possibly solve the problem at hand: a malicious attacker crafts a block larger than what levin will accept and put it in a chain with smaller blocks at the end. Then he mines those enough so they become the longest chain.

 honest miners try to apply the longest chain rule, but get stuck because they cant accept the block that was too large. Until there is a poc that demonstrates this, I doubt that this is even the current behavior. The code responsible for switching to the longer chain will:

1) never run 
2) will break and not apply the reorg when trying to fetch the blocks of the alt chain that is longer and contains the block that levin limits cant accept. Happy to stand corrected on this. If that is the case, the fix should be done as part of this effort to fix the checkpointing logic https://github.com/monero-project/monero/pull/10075 We walked through this code path before. When checkpointing is active, the reorg to checkpointed chain supersedes the longest chain rule.

 This code is currently not perfect as explained in the issue. If this issue really exists, it is a bug in the application of the longest chain rule and should be fixed there instead of introducing new arbitrary constants, that  produce ambiguity.  (and cant solve the problem, as the linked code by vtnerd shows, there are other limits not related to the block level) 

pasting my answer from MRL here for reference
**TLDR: https://github.com/monero-project/monero/pull/10075 if there is an issue fix it as part of this effort.** 

this constant will not address the fundamental issue

## Boog900 | 2025-12-17T15:18:31+00:00
There are 2 protocols for adding block(s) to the chain, the initial sync protocol and the new block notification protocol. If a block bigger than 100 MB is created it cannot be synced through the initial sync protocol, however it _can_ by synced through the notification system, as that uses fluffy blocks. However if the node is missing too many txs in the block it can't be synced through the notification system though (without trying to front load some of the txs in a new transaction message).

This means you can have some nodes following this chain and some nodes not.

I don't know how mixing 2 bug fixes/protocol changes together will help. 

> If this issue really exists, it is a bug in the application of the longest chain rule and should be fixed there instead of introducing new arbitrary constants

The whole point is that the fix for this is going to be a pretty big change, so for protection now we require that blocks do not go over the packet limit.

## ArticMine | 2025-12-17T15:57:28+00:00
I fail to see the need for this highly controversial approach, when we consider https://github.com/monero-project/research-lab/issues/155 and my slighter tighter proposal https://github.com/ArticMine/Monero-Documents/blob/master/MoneroScaling2025-12-03.pdf should provide ample time to address these issues. For example over 6 years for the 100 MB issue. 

There are very serious social covenant concerns  with imposing permanent fixed  blocksize caps a la Bitcoin in Monero. 

## spirobel | 2026-01-15T18:09:06+00:00
> I don't know how mixing 2 bug fixes/protocol changes together will help.

>>    If this issue really exists, it is a bug in the application of the longest chain rule and should be fixed there instead of introducing new arbitrary constants

> The whole point is that the fix for this is going to be a pretty big change, so for protection now we require that blocks do not go over the packet limit.

the point is that longest chain / latest checkpoint rule gets applied properly. The claim being made here is that this logic is broken in another subtle way other than what is documented in this issue https://github.com/monero-project/monero/pull/10075 can you link me to the code path where the notification system would allow a 100mb plus block to pass through? @Boog900 

in https://github.com/monero-project/monero/pull/10075 we discussed a solution. The block would end up at the same codepath and be allowed to reorg. The solution has to be adapted to account for the fact that the notification system would allow bigger blocks to pass through. 

Lets verify first that the blocks received through the notification system pass through the reorg logic of https://github.com/monero-project/monero/pull/10075 if that is the case, we apply levin limits before passing them into this. 

## Boog900 | 2026-01-15T21:27:47+00:00
> can you link me to the code path where the notification system would allow a 100mb plus block to pass through

Its not something I can really link to.

The fluffy block protocol allows sending just a block header and the other node can request missing txs. If the node isn't missing txs then none need to be sent. Therefor you can sync a block > 100mb if the block is sent as a fluffy block and you have the txs already as you don't need to send a single message > 100mb.


## spirobel | 2026-01-16T06:01:23+00:00
https://github.com/monero-project/monero/blob/d0d418483514d3caf79547e302937e45878eab21/src/cryptonote_protocol/cryptonote_protocol_handler.inl#L602

there is a sanity cap on this in the fluffy block notification command handler

``` cpp
  // Used by the RPC server to check the size of an incoming
  // block_blob
  bool core::check_incoming_block_size(const blobdata& block_blob) const
  {
    // note: we assume block weight is always >= block blob size, so we check incoming
    // blob size against the block weight limit, which acts as a sanity check without
    // having to parse/weigh first; in fact, since the block blob is the block header
    // plus the tx hashes, the weight will typically be much larger than the blob size
    if(block_blob.size() > m_blockchain_storage.get_current_cumulative_block_weight_limit() + BLOCK_SIZE_SANITY_LEEWAY)
    {
      LOG_PRINT_L1("WRONG BLOCK BLOB, sanity check failed on size " << block_blob.size() << ", rejected");
      return false;
    }
    return true;
  } 
```

the block blob is passed through this helper 
https://github.com/monero-project/monero/blob/d0d418483514d3caf79547e302937e45878eab21/src/cryptonote_core/cryptonote_core.cpp#L1462

this also goes the other way: if there is a different / more strict limitation in this code path it could also lead to a situation where some nodes accept the block, while others don't

## Boog900 | 2026-01-16T13:40:20+00:00
The limit you quote there moves with the median, in fact it is just a sanity check, it will always allow bigger blocks than the real block limit as it is comparing the block header size as the comment says.

The 100 MB limit is in the connection code, it does not see blocks/txs it sees packets. Did the packet contain more than 100 MB bytes? then it isn't allowed. Block catch up sync always sends the whole block in 1 message so if above 100 MB then the block can't be synced. The fluffy block allows leaving some txs, so you can not hit the limit if the peer has txs already.


## spirobel | 2026-01-18T05:35:19+00:00
so we construct a packet from the fluffy block and its txs, before passing it into the reorg handling code path

that also assures that the sub packet limits that vtnerd mentioned are honored 

## Boog900 | 2026-01-18T13:31:07+00:00
> so we construct a packet from the fluffy block and its txs, before passing it into the reorg handling code path

are you suggesting running a fully built fluffy block through the networking code again to make sure we don't accept blocks too big? it would work, but that would be a monumental hack, just smaller than fixing the issue itself.

## spirobel | 2026-01-21T12:10:13+00:00
this is the right approach. it is not just about if the blocks are too big. There are more sub packet limits that need to be respected. the only way to assure this is the case is by putting the incoming data through the same code path. 

there is no other way to fix this issue. there has to be just one code path to add new blocks & apply restrictions. 

## Boog900 | 2026-01-21T13:12:45+00:00
There will always be different code hit by blocks coming from different paths, we mostly already have the consensus code unified, which covers the other sub-packet limits. Building a received fluffy block into a full block packet and then running that full packet through the networking code will still mean fluffy blocks are taking a different code path. The fluffy block packet limit used to be 4 MB, this wouldn't be applied to blocks taking the normal path in this situation, so we would also need to turn full blocks into fluffy blocks. We would also need to run every possible fluffy block through the networking code, which would be 2^(numb txs in block), to truly make sure we are covering every possible path.

> there is no other way to fix this issue.

another solution has already been given. 

## spirobel | 2026-01-21T14:51:44+00:00
>another solution has already been given.

no

>The fluffy block packet limit used to be 4 MB, this wouldn't be applied to blocks taking the normal path in this situation, so we would also need to turn full blocks into fluffy blocks.

has this been discussed before? What I saw here was the suggestion to add another limit directly into the consensus code. But that does not address the issue that blocks can take different code paths that apply different limits, which could lead to a netsplit. 

>There will always be different code hit by blocks coming from different paths, we mostly already have the consensus code unified, which covers the other sub-packet limits. Building a received fluffy block into a full block packet and then running that full packet through the networking code will still mean fluffy blocks are taking a different code path. 

doesn't matter, overly pedantic interpretation of the word "codepath"  

## Boog900 | 2026-01-21T22:13:24+00:00
> no

🙄 

> has this been discussed before?

https://github.com/seraphis-migration/monero/pull/159

> the issue that blocks can take different code paths that apply different limits

The limit and code is the same, its the data that is different. I have already said this. The same networking code is being ran, its just the block is with and without different txs. I don't think this discussion is going anywhere and a solution has already been agreed, so I wont waste any more time.

## spirobel | 2026-01-23T06:17:10+00:00
>The limit and code is the same, its the data that is different. 

no
```  
--    return 1024 * 1024 * 4; // 4 MB, but it does not includes transaction data
++    return 1024 * 1024 * 128; // 128 MB (max packet is a bit less than 100 MB though, fluffy blocks can be full)
```

not the same

>a solution has already been agreed,

no

this is not a solution. it tries to bring the fluffy block restrictions more in line with levin, but it just matches the aesthetics instead of providing a real solution. In practice it does not matter if there was a large or small size difference in the blocks that cause the netsplit. 

the only solution is to apply the same restrictions defined in one function. Instead of doing this duct tape approach.  

## Boog900 | 2026-01-23T12:05:18+00:00
> not the same

THats the fluffy block limit _not_ the levin packet limit 😭 

https://github.com/monero-project/monero/blob/f65b2864552f855af1ef58c031dafffa58aae90c/contrib/epee/include/net/levin_base.h#L77
https://github.com/monero-project/monero/blob/f65b2864552f855af1ef58c031dafffa58aae90c/contrib/epee/include/net/levin_protocol_handler_async.h#L414

> this is not a solution. it tries to bring the fluffy block restrictions more in line with levin, but it just matches the aesthetics instead of providing a real solution.

The solution we agreed on is no hard limit, and a more restrictive underlying scaling algorithm, that means we have years warning to fix how blocks are sent around the network. 

## spirobel | 2026-01-23T13:12:30+00:00
> THats the fluffy block limit not the levin packet limit 😭

and now it is potentially bigger than the levin limit. I see no discussion in https://github.com/seraphis-migration/monero/pull/159 on how and why this new constant was picked.

Either you keep the fluffy limits more restrictive than the levin limits and fall back to syncing like the initial block sync protocol when the limits are hit, or you apply the levin limits in all cases. 

there might be other subtle differences that lead to the block being accepted on one codepath, but not on the other. That is why my suggestion is to put the fluffy blocks through the same block serialization code path they go through when syncing over the initial block sync protocol. 
you mentioned it would work but called it "a monumental hack" (for unclear reasons) 

>The solution we agreed on is no hard limit, and a more restrictive underlying scaling algorithm, that means we have years warning to fix how blocks are sent around the network.

that is not a solution. That is the agreement to kick the can down the road instead of doing this 32mb limit that does not solve the concern it raised. Which is a good thing, but not enough to address the underlying concern which has merit. 

# Action History
- Created by: kayabaNerve | 2025-11-30T10:22:35+00:00
