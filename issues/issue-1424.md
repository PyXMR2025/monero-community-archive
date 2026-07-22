---
title: 'Cuprate Meeting #112 - Tuesday, 2026-07-21, UTC 18:00'
source_url: https://github.com/monero-project/meta/issues/1424
author: moo900
assignees: []
labels: []
created_at: '2026-07-14T18:20:39+00:00'
updated_at: '2026-07-21T18:23:52+00:00'
type: issue
status: closed
closed_at: '2026-07-21T18:23:52+00:00'
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

Previous meeting: #1419

# Discussion History
## moo900 | 2026-07-21T18:23:50+00:00
## Meeting logs
```
boog900: 1) greetings
```
```
redsh4de: hi
```
```
boog900: 2) updates
```
```
boog900: I worked on hacking together the txpool backlog for fees
```
```
boog900: also RPC docs
```
```
redsh4de: continued testing wallet operations, PR'ed offline mode
```
```
boog900: 3) Project: What is next for Cuprate?
```
```
boog900: I think we are getting close to a beta release, what do you think redsh4de 
```
```
redsh4de: agreed

although we could get the remaining two graceful shutdown PRs in so the functionality and error propagation is fully complete before beta i think
```
```
syntheticbird: Hi sorry for the late
```
```
syntheticbird: No update from me
```
```
redsh4de: werent reproducible builds a pre-requisite for beta too? or after
```
```
redsh4de: hii
```
```
syntheticbird: I agree with that being completed for beta
```
```
syntheticbird: Thats an important enough restructuring that I would like that out of everyone's mind during beta fixes
```
```
boog900: The PRs are pretty big though
```
```
syntheticbird: Fortunately our review skill and motivation is bigger
```
```
redsh4de: pt2 is the big behemoth, pt3 is about ~150 lines net
```
```
syntheticbird: (Let's pretend)
```
```
syntheticbird: It was marked as such in my CCS.
```
```
redsh4de: it should be carefully reviewed, as at its core its also a classifier - whether a error should be fatal or transient/request/validation error
```
```
redsh4de: fatal error -> propagates to cancellation of all tasks and shutdown
```
```
redsh4de: * it should be carefully reviewed, as at its core the new error.rs's for blockchain/txpool/p2p/rpc are also classifiers - whether a error should be fatal or transient/request/validation error
```
```
syntheticbird: textbook definition of annoying software engineering but we arent't 3 or 4 days away of being shot dead for not releasing beta imo
```
```
syntheticbird: (say the guy that hasn't contributed in MONTHS)
```
```
redsh4de: +1
```
```
boog900: We could make a preview release?
```
```
syntheticbird: "Undertrained open weight beta cuprate. Use with caution."
```
```
syntheticbird: I am not against it if the goal is technical showcase of RPC
```
```
redsh4de: yeah thats seems good
```
```
redsh4de: beta-rc1 or smth
```
```
redsh4de: * beta-pre or smth
```
```
redsh4de: i reckon for a milestone like that a cuprate.org blog post would be in order?
```
```
syntheticbird: Yes
```
```
syntheticbird: I will prepare that
```
```
syntheticbird: I haven't touched to the website for a while time to brush the dust
```
```
boog900: anything else to discuss today?
```
```
syntheticbird: Nope
```
```
redsh4de: not from me
```
```
redsh4de: (there are a couple quick to review PRs though, like 599 and 626)
```
```
boog900: will do 
```
```
boog900: we can end here 
```
```
boog900: thanks everyone!
```
```
boog900: !meeting 
```

# Action History
- Created by: moo900 | 2026-07-14T18:20:39+00:00
- Closed at: 2026-07-21T18:23:52+00:00
