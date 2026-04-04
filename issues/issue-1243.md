---
title: 'Cuprate Meeting #66 - Tuesday, 2025-07-29, UTC 18:00'
source_url: https://github.com/monero-project/meta/issues/1243
author: moo900
assignees: []
labels: []
created_at: '2025-07-22T18:47:41+00:00'
updated_at: '2025-07-29T18:57:40+00:00'
type: issue
status: closed
closed_at: '2025-07-29T18:57:39+00:00'
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

Previous meeting: #1238

# Discussion History
## moo900 | 2025-07-29T18:57:38+00:00
## Meeting logs
```
boog900: 1) greetings 
```
```
hinto: hello
```
```
syntheticbird: Hello
```
```
boog900: Had to do something sorry 
```
```
boog900: 2. Updates 
```
```
boog900: Me: continued work on PRs I have already opened, the txpool and exposing more info on p2p connections 
```
```
syntheticbird: Me: nothing unfortunately
```
```
hinto: me: nothing to report
```
```
boog900: 3. Project: What is next for Cuprate?
```
```
hinto: binarybaron: https://github.com/Cuprate/cuprate/issues/516

> I'd like to be able to listen for status events

I have been interested in defining a spec for a potential WebSocket interface, that could probably be reused here
```
```
hinto: This would be green-field, so no backwards compat concerns like RPC although I guess the handlers could also be reused for RPC which would fulfill https://github.com/Cuprate/cuprate/issues/388.
```
```
boog900: once we have ZMQ this would be covered I think  
```
```
boog900: it can give notifications on new blocks/txs
```
```
boog900: I think defining new API on cuprated could be quite a bit of work, and I don't really want to get into that, for now at least 
```
```
boog900: anything else anyone would like to discuss today? 
```
```
syntheticbird: nope
```
```
hinto: this depends on if ZMQ is a higher priority than a new interface
```
```
boog900: IMO yes
```
```
boog900: ZMQ is currently used for ZMQ and p2pool 
```
```
boog900: * ZMQ is currently used for LWS and p2pool 
```
```
syntheticbird: i don't have an opinion. I would like a new transport that's all
```
```
boog900: I think we can end here is there is nothing else to discuss 
```
```
boog900: thanks everyone!
```
```
hinto: thanks
```
```
rucknium: > Maybe for running data science experiments on the Blockchain (like what mrl does all the time). Honestly don't know if this could be useful but naively I'd think it could be useful.
```
```
rucknium: Oh wait.
```
```
rucknium: In the last few days I have been thinking to ship some cuprate parts with an R package, linking as library functions.
```
```
rucknium: Especially the p2p functions, since there is no RPC for that
```
```
rucknium: But I think I can already sort of do that, with the starting point that boog gave me. I have not tried to do it yet. Just built some standalone binaries.
```
```
rucknium: This would also work with python library-building, AFAIK.
```
```
rucknium: For example, there is no native way to get your own `peer_id` from `monerod`, as discussed in #monero-dev:monero.social 
```
```
boog900: yeah, I think would be great to make the p2p and database libs more accessible  
```
```
boog900: both fill a niche that aren't really covered elsewhere 
```
```
boog900: there are some python libs for both but they are pretty low level AFAIK 
```
```
boog900: lmk if you have any issues with cuprate crates 
```
```
boog900: !meeting 
```

# Action History
- Created by: moo900 | 2025-07-22T18:47:41+00:00
- Closed at: 2025-07-29T18:57:39+00:00
