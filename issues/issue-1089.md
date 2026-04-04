---
title: 'Cuprate Meeting #25 - Tuesday, 2024-10-15, UTC 18:00'
source_url: https://github.com/monero-project/meta/issues/1089
author: moo900
assignees: []
labels: []
created_at: '2024-10-08T18:33:18+00:00'
updated_at: '2024-10-15T18:38:30+00:00'
type: issue
status: closed
closed_at: '2024-10-15T18:38:29+00:00'
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

Previous meeting with logs: #1085

# Discussion History
## moo900 | 2024-10-15T18:38:28+00:00
## Meeting logs
```
boog900: 1)greetings 
```
```
syntheticbird: Hi
```
```
hinto: hello
```
```
boog900: 2) updates 
```
```
syntheticbird: Joining dev force for a little. Actually splitting context service used by `cuprate-consensus` into its own subcrate. 
```
```
boog900: Me: I've been working on the tx-pool, specifically handling new tx-pool txs and getting txs from the pool for new blocks
```
```
hinto: me: still working on json-rpc handlers, boog900: there's a few signatures/types I missed in #297, I'll be making a PR for them soon
```
```
hinto: also I finished our initial benchmarking stuff: https://github.com/Cuprate/cuprate/pull/196
```
```
hinto: now to make benchmarks for every crate...
```
```
boog900: 3) Project: What is next for Cuprate?
```
```
boog900: I should have the txpool PR ready pretty soon, hopefully in a couple hours. At that point Cuprate should be able to sync the blockchain and participate in new tx/block propagation.
```
```
boog900: Aka alpha binary
```
```
syntheticbird: Finally
```
```
syntheticbird: almost two years of efforts. finally paying
```
```
syntheticbird: (im not part of the two years)
```
```
syntheticbird: Do we have any plan at the moment regarding FCMP++/Carrot hard fork update ?
```
```
boog900: no :D
```
```
syntheticbird: well ig its something to worry about in december
```
```
boog900: December is only testnet 
```
```
syntheticbird: yeah but alpha is going to be on testnet right?
```
```
syntheticbird: or will we continue on stagenet
```
```
detherminal: Will users be able to identify if the node is cuprated or monerd
```
```
detherminal: * Will users be able to identify if the node is cuprated or monerod
```
```
boog900: > <@syntheticbird:monero.social> yeah but alpha is going to be on testnet right?

no, you will be able to set the network
```
```
boog900: > <@detherminal:monero.social> Will users be able to identify if the node is cuprated or monerod

yes
```
```
detherminal: > <@boog900:monero.social> yes

How and why?
```
```
syntheticbird: > <@boog900:monero.social> no, you will be able to set the network

ok
```
```
boog900: > <@detherminal:monero.social> How and why?

how blazingly fast it is
```
```
syntheticbird: yeah kinda inevitable. performane tracking is a good metric
```
```
boog900: only half joking but stuff like difference in response times for different requests, strictness of JSON parsing etc 
```
```
boog900: trying to make them act the same would be almost impossible 
```
```
syntheticbird: as boog said once, the important is that you can't get if it is cuprate or monerod that emitted a transaction
```
```
hinto: obvious RPC differences are enumerated here: https://architecture.cuprate.org/rpc/differences/intro.html
```
```
syntheticbird: On another note, could we investigate forcing a global allocator for Cuprate? at least on musl system. I would like to not fall into the same performance hole as monerod.
```
```
syntheticbird: we could benchmark mimalloc and jemalloc
```
```
hinto: the allocator is probably not the first thing you diagnose on perf issues
```
```
syntheticbird: > <@hinto:monero.social> the allocator is probably not the first thing you diagnose on perf issues

on musl libc it is generally the first suspicion. It is notoriously known to be bad at multi-threading. Because their is one global free list pool unlike others allocators making one pool per thread. Also I recompiled monerod with musl patched with jemalloc and observed 4x syncing speed.
```
```
hinto: does cuprate compile with musl?
```
```
syntheticbird: I would indeed be curious to test that once txpool is complete
```
```
syntheticbird: I would be devastated if I hear we rely on glibc.
```
```
hinto: literally everything does :)
```
```
syntheticbird: > <@hinto:monero.social> literally everything does :)

on Linux. no. not that much relies on gnu libc extensions. also musl kinda improves on that part tho not to parity.
```
```
syntheticbird: anyway if anyone have another point
```
```
boog900: anything else anyone wants to discuss or we can end here?
```
```
syntheticbird: hinto was writing something i think
```
```
hinto: we can end
```
```
boog900: Thanks everyone!
```

# Action History
- Created by: moo900 | 2024-10-08T18:33:18+00:00
- Closed at: 2024-10-15T18:38:29+00:00
