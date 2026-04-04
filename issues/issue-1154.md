---
title: 'Cuprate Meeting #43 - Tuesday, 2025-02-18, UTC 18:00'
source_url: https://github.com/monero-project/meta/issues/1154
author: moo900
assignees: []
labels: []
created_at: '2025-02-11T19:01:04+00:00'
updated_at: '2025-02-18T19:09:56+00:00'
type: issue
status: closed
closed_at: '2025-02-18T19:09:55+00:00'
---

# Original Description
[Cuprate](https://github.com/Cuprate/cuprate) is an effort to create an alternative Monero node implementation.

Location: [Libera.chat, #cuprate](https://libera.chat/) | [Matrix](https://matrix.to/#/#cuprate:monero.social?via=matrix.org&via=monero.social)

[Join the Monero Matrix server if you don't already have a Matrix account](https://www.getmonero.org/resources/user-guides/join-monero-matrix.html)

Time: 18:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html)

Moderator: @Boog900

Please comment on GitHub in advance of the meeting if you would like to propose a discussion topic.

Main discussion topics:

- Greetings
- Updates: What is everyone working on?
- Project: What is next for Cuprate?
- Any other business

Previous meeting: #1151

# Discussion History
## moo900 | 2025-02-18T19:09:54+00:00
## Meeting logs
```
boog900: 1) greetings
```
```
syntheticbird: Hello humans (im a cat)
```
```
spirobel: hello cats (I am a bird)
```
```
hinto: hello
```
```
boog900: 2) updates
```
```
boog900: Me: not much to report since last week, looking to be back full time from now 
```
```
syntheticbird: Me: have been experimenting a little with arti on some small program. Looking at p2p code and thinking about the Tor integration. I should be able to draft an idea next week, then draft a CCS proposal.
```
```
hinto: me: no major updates
```
```
boog900: 3) Project: What is next for Cuprate?
```
```
syntheticbird: alpha soon (in theory)
```
```
hinto: SyntheticBird: I'm excited to see the drafts
```
```
boog900: me too, Tor/Arti is going to make it so much easier for people to run Tor nodes 
```
```
boog900: anything anyone wants to discuss today?
```
```
syntheticbird: yes
```
```
syntheticbird: Le seed node binary, when?
```
```
hinto: I came across something interesting: https://github.com/KeystoneHQ/cuprate, it looks like this hardware wallet company is using `cuprate-cryptonight`
```
```
boog900: as soon as someone spends 30 mins to put it together :p
```
```
syntheticbird: i saw that a little while ago in my github feed
```
```
syntheticbird: thats nice
```
```
sgp_: > <@syntheticbird:monero.social> Me: have been experimenting a little with arti on some small program. Looking at p2p code and thinking about the Tor integration. I should be able to draft an idea next week, then draft a CCS proposal.

Oh hey, I'm also playing with Arti: https://github.com/truenas/apps/pull/1650
```
```
sgp_: https://github.com/MAGICGrants/arti-docker
```
```
syntheticbird: NICE
```
```
syntheticbird: I'll try to make the changes so that we can add other overlay network later on
```
```
syntheticbird: Tor is just the first
```
```
syntheticbird: I could completely see other overlay network appear in the future
```
```
syntheticbird: (i'm not rejecting i2p, it's just that their situation is pretty confusing)
```
```
boog900: We already have a `NetZone` abstraction 
```
```
boog900: having a `ClearNetArti` network zone would be cool
```
```
syntheticbird: oh you make me think
```
```
syntheticbird: can we discuss in this meeting potential changes of the address book for more protocol
```
```
syntheticbird: P2P over QUIC in mind
```
```
boog900: my honest opinion is the address book needs to be rewritten 
```
```
syntheticbird: I guess a new protocol can be defined as a whole NetZone
```
```
syntheticbird: limitations you have in mind?
```
```
boog900: > <@syntheticbird:monero.social> I guess a new protocol can be defined as a whole NetZone

yes
```
```
boog900: it doesn't handle bans properly + it's very vulnerable to spy nodes
```
```
boog900: we could just tac on extra checks like monerod's but I think it will end up a mess (like monerod) 
```
```
syntheticbird: ngl I would if its just about ban i hardly see benefits at rewriting the whole thing. I believe you, you have better vision on your crate than I have
```
```
syntheticbird: * ngl if its just about ban i hardly see benefits at rewriting the whole thing. I believe you, you have better vision on your crate than I have
```
```
boog900: realistically it's good enough for now but I don't want it to end up like this: https://github.com/monero-project/monero/blob/84df77404e8bcbe1cf409f64c81e4e4f9c84885b/src/p2p/net_node.inl#L1582
```
```
syntheticbird: HAHA
```
```
hinto: Just noting: there is a cost to making things generic, it should be weighed against the extra time needed and added complexity it (often but not always) brings. Focusing on a concrete type is easier to read/write/impl for everyone involved and in a lot of cases gets "good enough" to the point where other concerns become more important.
```
```
hinto: For anon networks (for now), I think a small-scoped impl specific to `arti` would be a better path forward than a generic impl.
```
```
boog900: I agree + the `NetZone` abstraction is already in place so I don't really know what SyntheticBird meant 
```
```
hinto: SyntheticBird: although this is ultimately up to you, just noting that it would be easier to write for you and easier to review + get merged
```
```
syntheticbird: you do good to notate it, I'm not planning on monomorphizing every single function of the p2p unless necessary. The draft will be there for that anyway.
```
```
syntheticbird: I just forgot about `NetZone` tbh
```
```
boog900: Rucknium: Currently with tx propagation monerod will only do 1 Tor hop them it will be stemmed over clear-net.

I can see it being a good idea to route over Tor multiple times what way would you recommend doing this? 

1. consecutive Tor nodes in state `stem` route over Tor, untill a node in `fluff` is reached then it stems over clear-net

2. consecutive Tor nodes in state `stem` route over Tor, flipping a potentially weighted coin to start clear-net routing 

3. some other way?
```
```
boog900: should a node which receives a stem tx over clearnet send it over Tor?
```
```
boog900: maybe for option `1` the node should set the fluff flag to cause the next node to fluff it immediately  
```
```
boog900: or for `1` the node should just fluff it over clear-net 
```
```
boog900: anything else anyone wants to discuss in this meeting?
```
```
syntheticbird: planned alpha date ?
```
```
boog900: probably looking at early March for release, will be ready late February 
```
```
hinto: I have leftover funds I am planning to buy hardware with immediately after CCS confirmation, if OK then I will buy hardware + test and if everything goes well then I'm planning to open PRs for build + release automation, otherwise we figure the problem out and/or revert to a fallback commit
```
```
rucknium: I'm not sure about which option is best, but this should probably be fixed first:
Shi, R., Ge, Y., Lan, L., Peng, Z., Lin, S., & Li, L. 2024, "Deanonymizing Transactions Originating from Monero Tor Hidden Service Nodes."
https://moneroresearch.info/index.php?action=resource_RESOURCEVIEW_CORE&id=218
```
```
boog900: it has been AFAIK https://github.com/monero-project/monero/pull/9632
```
```
rucknium: Is this the same problem?
```
```
rucknium: Check my notes in the MR.info entry
```
```
rucknium: I think #9632 fixed a more "obvious" leak, but I'm not sure
```
```
boog900: it fixes it, the time_sync includes the peer list which had the nodes onion address inserted at the end, that PR randomizes the place. 
```
```
boog900: to improve it even more txs should be sent over Tor more than once 
```
```
boog900: I am slightly leaning towards always routing stem txs over Tor at every hop in state `stem` and in state `fluff` always fluffing over clearnet 
```
```
rucknium: > <@boog900:monero.social> Rucknium: Currently with tx propagation monerod will only do 1 Tor hop them it will be stemmed over clear-net.
> 
> I can see it being a good idea to route over Tor multiple times what way would you recommend doing this? 
> 
> 1. consecutive Tor nodes in state `stem` route over Tor, untill a node in `fluff` is reached then it stems over clear-net
> 
> 2. consecutive Tor nodes in state `stem` route over Tor, flipping a potentially weighted coin to start clear-net routing 
> 
> 3. some other way?

The six-hop Tor circuit from hidden service to hidden service introduces some non-negligible latency, which may change the probability of hitting the embargo timers
```
```
rucknium: > <@boog900:monero.social> Rucknium: Currently with tx propagation monerod will only do 1 Tor hop them it will be stemmed over clear-net.
> 
> I can see it being a good idea to route over Tor multiple times what way would you recommend doing this? 
> 
> 1. consecutive Tor nodes in state `stem` route over Tor, untill a node in `fluff` is reached then it stems over clear-net
> 
> 2. consecutive Tor nodes in state `stem` route over Tor, flipping a potentially weighted coin to start clear-net routing 
> 
> 3. some other way?

But at a glance, (1) seems best
```
```
boog900: > <@rucknium:monero.social> The six-hop Tor circuit from hidden service to hidden service introduces some non-negligible latency, which may change the probability of hitting the embargo timers

yeah that would be something to check
```
```
boog900: AFAIK the current value used for "hop time" is a little more than needed so we may still be within the time but we would probably need to increase it.
```
```
boog900: anything else anybody wants to discuss today?
```
```
boog900: ok I think we can end here 
```
```
boog900: thanks everyone! 
```

# Action History
- Created by: moo900 | 2025-02-11T19:01:04+00:00
- Closed at: 2025-02-18T19:09:55+00:00
