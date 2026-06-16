---
title: 'Cuprate Meeting #107 - Tuesday, 2026-06-16, UTC 18:00'
source_url: https://github.com/monero-project/meta/issues/1401
author: moo900
assignees: []
labels: []
created_at: '2026-06-09T18:19:53+00:00'
updated_at: '2026-06-16T18:17:54+00:00'
type: issue
status: closed
closed_at: '2026-06-16T18:17:54+00:00'
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

Previous meeting: #1400

# Discussion History
## moo900 | 2026-06-16T18:17:53+00:00
## Meeting logs
```
boog900: 1) greetings
```
```
redsh4de: Hi!
```
```
boog900: 2) updates 
```
```
boog900: I continued to work on RPC, we now have enough merged for basic wallet operations 
```
```
boog900: Still a couple more things needed for full wallet support though
```
```
redsh4de: reviewed PRs, tested the wallet sync - great performance, looking into how we can further optimize that mainly on the response time path
submitted PRs for log redaction via safelog and caching the output distribution in memory
```
```
redsh4de: rebased a couple older ones that had conflicts
```
```
boog900: 3. Project: What is next for Cuprate?
```
```
boog900: Once I finish with the rpc requests needed for wallets I might try slop a test program to test requests against monerod 
```
```
redsh4de: not strictly dev related, we have a couple of older issues that could be closed to clean up the list
```
```
redsh4de: * not strictly dev related, but we have a couple of older issues that could be closed to clean up the list
```
```
redsh4de: things pertaining to heed db and retrieving sync target which shipped with the embeddable lib PR, there are prob a couple others
```
```
boog900: > <@redsh4de:matrix.org> not strictly dev related, but we have a couple of older issues that could be closed to clean up the list

Sure, will close later 
```
```
redsh4de: other than that... not much else im working on aside from testing wallet sync, unless any PR review comments to address appear :D
```
```
boog900: Yeah sorry I have been prioritising getting RPC done, I will get to those PRs soon. 
```
```
boog900: Anything else to discuss today?
```
```
redsh4de: not at the moment
```
```
boog900: Alright we can end here 
```
```
boog900: Thanks redsh4de
```
```
boog900: !meeting 
```

# Action History
- Created by: moo900 | 2026-06-09T18:19:53+00:00
- Closed at: 2026-06-16T18:17:54+00:00
