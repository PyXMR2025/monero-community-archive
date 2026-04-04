---
title: 'Cuprate Meeting #63 - Tuesday, 2025-07-08, UTC 18:00'
source_url: https://github.com/monero-project/meta/issues/1230
author: moo900
assignees: []
labels: []
created_at: '2025-07-01T19:07:28+00:00'
updated_at: '2025-07-08T18:43:05+00:00'
type: issue
status: closed
closed_at: '2025-07-08T18:43:05+00:00'
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

Previous meeting: #1225

# Discussion History
## moo900 | 2025-07-08T18:43:04+00:00
## Meeting logs
```
boog900: 1) greetings 
```
```
syntheticbird: hello
```
```
syntheticbird: everyone's dead
```
```
boog900: looks like it 
```
```
boog900: 2) updates 
```
```
syntheticbird: me: No update
```
```
boog900: Me: I have been looking at the FCMP competition 
```
```
boog900: I guess we wait for hinto 
```
```
boog900: anything anyone wants to discuss today?
```
```
syntheticbird: nope
```
```
basses: how are yall doing?
```
```
hinto: hello, sorry for being late although no updates again, still in-between CCSs
```
```
syntheticbird: very fine and you rando
```
```
basses: fine
```
```
boog900: slow week for Cuprate last week then
```
```
rucknium: Any thoughts on this? https://b10c.me/observations/15-inv-to-send-queue/
> Observing ping timings across the network reveals the effect of this Denial-of-Service. Since Bitcoin Core’s message processing is single-threaded, only one message can be created or processed at a time, meaning that all other peers have to wait.
```
```
rucknium: Is Cuprate's message processing single-threaded?
```
```
syntheticbird: hell nah
```
```
syntheticbird: its multithreaded and async
```
```
rucknium: If "stale blocks" in the blog post means "orphaned blocks", then this DDoS had a big impact. A financially significant impact.
```
```
rucknium: > This 10-fold increase in the stale-block rate was likely caused by block propagation being significantly affected.
```
```
rucknium: Also, a good lesson for 0xfffc 's implementation of the new tx propagation protocol in `monerod`
```
```
boog900: bitcoind relays blocks immediately after PoW, monerod & cuprated should probably do the same 
```
```
syntheticbird: I haven't looked at the monerod PR
```
```
syntheticbird: is it single-threaded?
```
```
boog900: yes
```
```
boog900: wait no
```
```
syntheticbird: damn
```
```
syntheticbird: i would have thought not
```
```
boog900: its multi-threaded 
```
```
syntheticbird: at my understanding its direct function call from peer handler, so multi-threaded, but txpool is critical zone
```
```
syntheticbird: so at least serialized
```
```
boog900: the PR should actually help monerod to not get bogged down with txs 
```
```
boog900: we can eventually require an inv for every tx 
```
```
syntheticbird: Immediately after PoW ? They don't verify that txs are valid?
```
```
syntheticbird: before relaying
```
```
boog900: yeah they don't 
```
```
syntheticbird: I would be tempted to be against. At least in the current situation we can define honest nodes from bad nodes by checking if they send you invalid blocks, but if we choose to relay unverified blocks we won't be able to make the difference
```
```
boog900: if someone creates a huge block with unknown txs it can take a while to propagate 
```
```
boog900: if someone creates an invalid tx in a block they had to do PoW 
```
```
syntheticbird: true
```
```
rucknium: IIRC, the stressnet last year had syncing problems because not all txs were in the mempool. Then, when a node asked its peer for those missing txs (in the fluffy block), the peer _also_ did not have the missing txs, so the block "failed".
```
```
boog900: unless the peer reorged before handling the tx request that shouldn't happen ...
```
```
rucknium: A lot of weird things happened on stressnet, so it is hard to know.
```
```
boog900: anything else to discuss today or we can end here?
```
```
syntheticbird: nothing to add
```
```
boog900: thanks everyone!
```
```
boog900: !meeting 
```

# Action History
- Created by: moo900 | 2025-07-01T19:07:28+00:00
- Closed at: 2025-07-08T18:43:05+00:00
