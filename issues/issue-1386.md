---
title: 'Cuprate Meeting #103 - Tuesday, 2026-05-19, UTC 18:00'
source_url: https://github.com/monero-project/meta/issues/1386
author: moo900
assignees: []
labels: []
created_at: '2026-05-12T19:12:26+00:00'
updated_at: '2026-05-19T18:21:12+00:00'
type: issue
status: closed
closed_at: '2026-05-19T18:21:11+00:00'
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

Previous meeting: #1383

# Discussion History
## moo900 | 2026-05-19T18:21:10+00:00
## Meeting logs
```
boog900: 1) greetings 
```
```
redsh4de: hi!
```
```
syntheticbird: hi
```
```
boog900: 2) updates
```
```
boog900: Me: Reviewed & merged some of the big PRs that have been standing for a while
```
```
boog900: One of which I needed for RPC :)
```
```
redsh4de: working on updating the service propagation PR (shutdown pt2)
```
```
syntheticbird: done some review
```
```
boog900: 3. Project: What is next for Cuprate?
```
```
boog900: This CCS could do with some comments from people: https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/676
```
```
syntheticbird: If I am not mistaken, with graceful shutdown and RPC we should be good to go for beta
```
```
boog900: we did want reproducible builds IIRC 
```
```
syntheticbird: ah right
```
```
boog900: Also I think we should have a long testing period 
```
```
boog900: after RPC is merged 
```
```
syntheticbird: you mean before releasing 0.1.0 ?
```
```
boog900: yes
```
```
syntheticbird: or between 0.1.0 and 0.1.1
```
```
syntheticbird: ok
```
```
boog900: before beta 
```
```
boog900: 0.1.0 beta would be nice
```
```
boog900: we could do 0.0.10 :)
```
```
syntheticbird: I would have imagined beta to be for this kind of long-testing period
```
```
syntheticbird: otherwise we will start advertising beta as stable
```
```
boog900: internal testing before giving it out to the world is a good idea IMO
```
```
syntheticbird: i agree but no need for an alpha release in this case
```
```
boog900: by long I mean like a month or 2 
```
```
boog900: true yeah
```
```
syntheticbird: its just semantic at the end but sure i wouldn't be against some testing before beta milestone
```
```
redsh4de: yeah makes sense to do so, big milestone after all
```
```
boog900: Does anyone have anything else they want to discuss?
```
```
redsh4de: i should have the shutdown pt2 rebased today, doing some last passes on it - after the whole series is merged i plan to organize the launch process a bit by making each subsystem own its init function
```
```
redsh4de: eventually should also add status streaming like in the original library proposal
```
```
syntheticbird: Nothing to add.
```
```
boog900: I think we can end here, remember to give thoughts on that CCS if you have any
```
```
boog900: !meeting 
```

# Action History
- Created by: moo900 | 2026-05-12T19:12:26+00:00
- Closed at: 2026-05-19T18:21:11+00:00
