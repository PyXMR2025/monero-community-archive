---
title: 'Cuprate Meeting #50 - Tuesday, 2025-04-08, UTC 18:00'
source_url: https://github.com/monero-project/meta/issues/1181
author: moo900
assignees: []
labels: []
created_at: '2025-04-01T19:30:56+00:00'
updated_at: '2025-04-08T19:05:10+00:00'
type: issue
status: closed
closed_at: '2025-04-08T19:05:10+00:00'
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

Previous meeting: #1176

# Discussion History
## moo900 | 2025-04-08T19:05:09+00:00
## Meeting logs
```
boog900: 1) greetings 
```
```
hinto: hello
```
```
m-relay: <N​orrinRadd> Hello 
```
```
boog900: 2) updates
```
```
boog900: Me: working on the tx-pool related stuff, mainly the manager
```
```
syntheticbird: Hello
```
```
hinto: me: preparing `cuprated v0.0.2` release
```
```
syntheticbird: Me: No longer sick, preparing `Transport` trait and edits PR
```
```
boog900: 3) Project: What is next for Cuprate?
```
```
boog900: everyone ok with the new release tomorrow? 
```
```
hinto: boog900: `v0.0.2` needs to be tagged/tested/released by tomorrow: https://github.com/Cuprate/cuprate/milestone/2.

402 review is higher priority, my bad for having it ready late but can you review/merge it today? If not then I can add the docs next release.

Other than that only 403, 413 are required which should be quick.

If possible, 419, 424, 426 could be squeezed in too (if merged today).
```
```
syntheticbird: no objection
```
```
boog900: yeah I can review 402 today 
```
```
boog900: hinto:  With 419 I was thinking that the corrupt message should be posted on any error when opening the database. Currently we are mapping certain error types to corrupt but looking at all the error types I reckon a lot more could also be triggered on a corrupt DB.
```
```
boog900: just printing the corrupt warning with the error should be better
```
```
hinto: so replace `unwrap_db_init` with `.expect(DATABASE_CORRUPT_MSG)`?
```
```
boog900: we also want the error printed for debugging purposes IMO but yeah like that
```
```
rucknium: Will cuprate have a MoneroKon talk? Deadline for submissions is April 14.
```
```
hinto: I am personally interested but I do not think so, perhaps one should have been prepared?
```
```
rucknium: You just have to give a summary of the planned talk for the submission. I think MoneroKon would accept even a very basic summary statement for the submission.
```
```
rucknium: Don't you have things to show off? Architectural designs, performance, roadmap, etc?
You can do the talk remotely and/or pre-recorded.
```
```
rucknium: Anyway, your decision.
```
```
m-relay: <N​orrinRadd> Are any of the open issues candidates for being labled "E-easy"? 
```
```
boog900: We will definitely have stuff to talk about :) I am open to the idea 
```
```
boog900: NorrinRadd: not that I know hinto do you have any in mind?
```
```
m-relay: <N​orrinRadd> actually I just saw some of the mediums I can tackle 
```
```
m-relay: <N​orrinRadd> just chose one 
```
```
syntheticbird: Same I'm interested on a physical presence at MoneroKon next year.
```
```
syntheticbird: (yeah i know sorry for delay)
```
```
boog900: N​orrinRadd: maybe the `Persist banned peers` part of #178, William started that but I think they have given up on it. 
```
```
boog900: anything else anyone wants to discuss today?
```
```
boog900: ok I think we can end here, thanks everyone!
```
```
hinto: thanks
```

# Action History
- Created by: moo900 | 2025-04-01T19:30:56+00:00
- Closed at: 2025-04-08T19:05:10+00:00
