---
title: 'Cuprate Meeting #115 - Tuesday, 2026-08-11, UTC 18:00'
source_url: https://github.com/monero-project/meta/issues/1437
author: moo900
assignees: []
labels: []
created_at: '2026-08-04T18:31:34+00:00'
updated_at: '2026-08-11T18:15:54+00:00'
type: issue
status: closed
closed_at: '2026-08-11T18:15:54+00:00'
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

Previous meeting: #1432

# Discussion History
## moo900 | 2026-08-11T18:15:53+00:00
## Meeting logs
```
boog900: 1) greetings 
```
```
redsh4de: hi
```
```
theredhell: hi
```
```
syntheticbird: hi
```
```
boog900: 2) updates
```
```
boog900: I have been working on fixing bugs and other small things I have been thinking about doing for a while  
```
```
theredhell: pruning works so far as for pruning from scratch, although not thoroughly tested.
I still need to write sth to prune the chain if it's not pruned yet.
```
```
syntheticbird: Been posting on social media about the last release, answering when possible. Currently working on implementing several hardening/security improvements to the RPC server with the input boog900 and redsh4de 
```
```
redsh4de: been taking it easier this week, currently looking into the flakiness of the OpenBSD CI runs
```
```
boog900: 3) Project: What is next for Cuprate?
```
```
boog900: we will probably have a preview 2 out next week 
```
```
boog900: with all the fixes + the RPC rate limiting 
```
```
boog900: hopefully pruning too
```
```
redsh4de: shutdown changes for next one?
```
```
boog900: I just pushed a commit adding tape deleting: https://github.com/Cuprate/Tapes
```
```
boog900: I'll try
```
```
boog900: I'll post my next CCS proposal soon as well 
```
```
boog900: anything else for today?
```
```
boog900: I will just say that pruning and ZMQ are features that a lot of people have said prevents them from using Cuprate 
```
```
boog900: pruning is soon™️
```
```
boog900: But ZMQ ...
```
```
syntheticbird: pruning has been asked quite a lot
```
```
boog900: I think we can end here
```
```
boog900: thanks everyone
```
```
syntheticbird: Thanks
```
```
boog900: !meeting 
```

# Action History
- Created by: moo900 | 2026-08-04T18:31:34+00:00
- Closed at: 2026-08-11T18:15:54+00:00
