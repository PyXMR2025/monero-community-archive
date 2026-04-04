---
title: 'Cuprate Meeting #31 - Tuesday, 2024-11-26, UTC 18:00'
source_url: https://github.com/monero-project/meta/issues/1111
author: moo900
assignees: []
labels: []
created_at: '2024-11-19T20:03:51+00:00'
updated_at: '2024-11-26T19:08:43+00:00'
type: issue
status: closed
closed_at: '2024-11-26T19:08:43+00:00'
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

Previous meeting with logs: #1108

# Discussion History
## moo900 | 2024-11-26T19:08:42+00:00
## Meeting logs
```
boog900: meeting time: https://github.com/monero-project/meta/issues/1111
```
```
boog900: 1) greetings 
```
```
syntheticbird: hi
```
```
hinto: hello
```
```
boog900: 2) updates
```
```
syntheticbird: me: nothing
```
```
boog900: Me: spent time on binary startup + investigating some issues in the DB.
```
```
hinto: me: Very close to finishing https://github.com/Cuprate/cuprate/pull/308, most likely ready for review this week (I did say this before though). Also finalizing RPC binary string behavior: https://github.com/Cuprate/cuprate/pull/349.
```
```
boog900: 3) Project: What is next for Cuprate?
```
```
syntheticbird: subdomain for the first public cuprate node ?
```
```
hinto: `node.cuprate.org`?
```
```
syntheticbird: > <@hinto:monero.social> `node.cuprate.org`?

yeah
```
```
hinto: boog900: do you know if #348 is a problem because of `heed` internals or `cuprate_database`'s abstraction?
```
```
boog900: almost certain it is heed's internals 
```
```
hinto: How soon does it need to be fixed? I'd like to upstream any change over forking but I need to finish #308 and reviews as well
```
```
boog900: It's needed for the alpha binary, unless we work around it by pulling values individually instead of using `get_range`, so not extremely urgent.  
```
```
hinto: That sounds quite slow although since it's temporary it may be okay for now - did you want to find a fix?
```
```
boog900: Yeah sure 
```
```
hinto: SyntheticBird: do you have time to impl https://github.com/Cuprate/cuprate/issues/336? AFAICT it seems easy to support, eventually supporting musl would be valuable too
```
```
hinto: also any thoughts on RPC API changes in #349?
```
```
boog900: I haven't been paying much attention to that issue, we need wallet support tho 
```
```
boog900: if those endpoints are used in wallets 
```
```
syntheticbird: > <@hinto:monero.social> SyntheticBird: do you have time to impl https://github.com/Cuprate/cuprate/issues/336? AFAICT it seems easy to support, eventually supporting musl would be valuable too

Yes I can implement it
```
```
hinto: ﻿`wallet2` uses `/get_output_distribution.bin` which we can support, it also uses `get_txpool_backlog` which we can't (binary string) but I assume it would be changed to use the proposed `/get_txpool_backlog.bin`, which we also can support. Other wallets may not work for a while until they update, which they eventually will have to if the 12 month deprecation -> removal plan works out.
```
```
boog900: ok yeah sounds good my recommendation would've been to not implement the bad/new types until -core changes them due to how slow stuff happens over there
```
```
hinto: sure, #349 can be kept a draft for now
```
```
boog900: does anyone have anything else they want to discuss?
```
```
boog900: I will just add that I have been running `cuprated` on and off for the last week and it has been working fine, it synced the chain and is participating in tx/block broadcast.
```
```
boog900: only thing it failed to do is allow another node to sync from it - which is because of `get_range` 
```
```
hinto: is this on a branch?
```
```
boog900: #344
```
```
boog900: I think we can end here, thanks everyone! 
```
```
syntheticbird: thanks
```
```
hinto: thanks
```

# Action History
- Created by: moo900 | 2024-11-19T20:03:51+00:00
- Closed at: 2024-11-26T19:08:43+00:00
