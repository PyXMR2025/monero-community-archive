---
title: 'Cuprate Meeting #111 - Tuesday, 2026-07-14, UTC 18:00'
source_url: https://github.com/monero-project/meta/issues/1419
author: moo900
assignees: []
labels: []
created_at: '2026-07-07T18:20:31+00:00'
updated_at: '2026-07-14T18:20:40+00:00'
type: issue
status: closed
closed_at: '2026-07-14T18:20:40+00:00'
---

# Original Description
[Cuprate](https://github.com/Cuprate/cuprate) is an effort to create an alternative Monero node implementation.

Location: [Libera.chat, #cuprate](https://libera.chat/) | [Matrix](https://matrix.to/#/#cuprate:monero.social?via=matrix.org&via=monero.social)

[Join the Monero Matrix server if you don't already have a Matrix account](https://www.getmonero.org/resources/user-guides/join-monero-matrix.html)

Time: 18:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html)

Moderator: @Boog900

Please comment on GitHub in advance of the meeting if you would like to propose a discussion topic.

Main discussion topics:

1. Greetings
2. Updates: What is everyone working on?
3. Project: What is next for Cuprate?
4. Any other business

Previous meeting: #1414

# Discussion History
## moo900 | 2026-07-14T18:20:38+00:00
## Meeting logs
```
boog900: 1) greetings
```
```
redsh4de: hellooo
```
```
boog900: 2) updates 
```
```
boog900: Me: testing, found an issue in fjall that should be fixed soon 
```
```
boog900: Also looking at fee selection to decided if we should add a custom broken JSON writer for it 
```
```
redsh4de: me: worked on a PR that makes synchronization semantics be closer to monerod and handles peer disconnections while syncing
```
```
redsh4de: in monerod's get_info, "synchronized" isnt the actual live state, its more like - has the node caught up to the tip at least once during this run. its like a sticky flag, even if you lose all your peers or disconnect from the network, it will still be true
```
```
redsh4de: which makes sense for wallet stability, we cannot flip flop back and forth and make wallets think we are unsynced if we are just a block or smth behind
```
```
redsh4de: ported that logic over, but additionally having it reset to false if we do end up disconnecting from the network - as if we are disconnected from the network and we dont know how long we have been offline, makes sense to reset that flag to be equivalent to a cold boot, so marginal logic improvement there
```
```
redsh4de: rebased 605, thats it from me
```
```
boog900: Sounds good I'll review them soon
```
```
boog900: 3) Project: What is next for Cuprate?


```
```
boog900: Release will need to wait until the fjall fixes are in, which might delay by a little
```
```
boog900: We could do a preview though
```
```
boog900: redsh4de: have you managed to do much testing?
```
```
redsh4de: been doing some manual runs - dozens of full chain syncs, couple of back and forth transactions - as far as that goes things look great
```
```
redsh4de: havent gotten to making a automated setup just yet
```
```
boog900: Nice, that's good 
```
```
boog900: I think I might try make some benchmarks too 
```
```
redsh4de: thatd be useful
```
```
boog900: Anything else to discuss today?
```
```
redsh4de: nope
```
```
boog900: Thanks, we can end here 
```
```
boog900: !meeting 
```

# Action History
- Created by: moo900 | 2026-07-07T18:20:31+00:00
- Closed at: 2026-07-14T18:20:40+00:00
