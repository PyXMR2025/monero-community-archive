---
title: 'Cuprate Meeting #116 - Tuesday, 2026-08-18, UTC 18:00'
source_url: https://github.com/monero-project/meta/issues/1441
author: moo900
assignees: []
labels: []
created_at: '2026-08-11T18:15:53+00:00'
updated_at: '2026-08-18T18:15:35+00:00'
type: issue
status: closed
closed_at: '2026-08-18T18:15:35+00:00'
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

Previous meeting: #1437

# Discussion History
## moo900 | 2026-08-18T18:15:33+00:00
## Meeting logs
```
boog900: 1) greetings 
```
```
syntheticbird: Hi
```
```
redsh4de: helloo
```
```
boog900: 2) updates
```
```
boog900: I have been working on a tx interface for the DB. Also doing some final things for pruning 
```
```
syntheticbird: been working on implementing hardening for RPC server, and preparing a blog post about it.
```
```
redsh4de: worked with le birb on some streamlining for #684, pushed ~4 new commits to #586 to standardize the fatal error semantics around a alias that's used throughout for better readability, as well as some changes to ExtendedConsensusError to make it less ugly to handle in the new error types
```
```
boog900: 3) Project: What is next for Cuprate?
```
```
redsh4de: after 684 is merged i'll dive into the next PR in the series
```
```
syntheticbird: do we feel confident in reviewing/merging rpc hardening, graceful shutdown and pruning for a next week release ?
```
```
syntheticbird: it would be about time we deal with graceful shutdown pt.2
```
```
boog900: I think we can 
```
```
redsh4de: yes plz or i'll keep expanding it with changes that can just be subsequent easier to review PRs
```
```
redsh4de: dont feed the beast
```
```
boog900: I don't have anything I want to discuss today
```
```
boog900: does anyone else?
```
```
redsh4de: nope
```
```
redsh4de: https://github.com/Cuprate/cuprate/pull/586#issuecomment-5332215134 theres just this thought i had, but yeah can discuss further in review
```
```
syntheticbird: nothing on my side
```
```
boog900: We can end here
```
```
boog900: thanks everyone
```
```
syntheticbird: thanks
```

# Action History
- Created by: moo900 | 2026-08-11T18:15:53+00:00
- Closed at: 2026-08-18T18:15:35+00:00
