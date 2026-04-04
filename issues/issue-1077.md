---
title: 'Cuprate Meeting #22 - Tuesday, 2024-09-24, UTC 18:00'
source_url: https://github.com/monero-project/meta/issues/1077
author: moo900
assignees: []
labels: []
created_at: '2024-09-17T18:54:58+00:00'
updated_at: '2024-09-24T18:21:32+00:00'
type: issue
status: closed
closed_at: '2024-09-24T18:21:32+00:00'
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

Previous meeting with logs: #1071

# Discussion History
## moo900 | 2024-09-24T18:21:31+00:00
## Meeting logs
```
boog900: meeting time! https://github.com/monero-project/meta/issues/1077
```
```
boog900: 1) greetings 
```
```
hinto: hello
```
```
boog900: 2) updates 
```
```
boog900: me: I took it pretty slow last week, I looked into a bug where peers weren't disconnecting when they should have been, I think I found the issue I'll make a PR for it today. I also did some work on making the logging rules, I'll have an initial PR for them soon. I also planned out some changes to the P2P client pool that will need to be done for some requests 
```
```
hinto: me: starting to add internal message signatures/types for RPC: https://github.com/Cuprate/cuprate/pull/297
```
```
boog900: 3) Project: What is next for Cuprate?
```
```
kayabanerve: Update: I submitted -serai for auditing.
```
```
boog900: > <@kayabanerve:matrix.org> Update: I submitted -serai for auditing.

nice are you going to be making a CCS?
```
```
kayabanerve: Once I get a quote, a CCS will be made.
```
```
kayabanerve: I plan to submit it, but if I do, it'll be paid directly to CS so CS may submit it directly.
```
```
hinto: is the scope of the audit the entire `networks/monero` folder?
```
```
boog900: kayabanerve: 
```
```
boog900: Is there anything else anyone wants to discuss or we can end here
```
```
hinto: think we can end early
```
```
boog900: Thanks everyone!
```
```
boog900: !meeting 
```

# Action History
- Created by: moo900 | 2024-09-17T18:54:58+00:00
- Closed at: 2024-09-24T18:21:32+00:00
