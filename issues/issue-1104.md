---
title: 'Cuprate Meeting #29 - Tuesday, 2024-11-12, UTC 18:00'
source_url: https://github.com/monero-project/meta/issues/1104
author: moo900
assignees: []
labels: []
created_at: '2024-11-05T19:30:25+00:00'
updated_at: '2024-11-12T18:38:25+00:00'
type: issue
status: closed
closed_at: '2024-11-12T18:38:25+00:00'
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

Previous meeting with logs: #1101

# Discussion History
## moo900 | 2024-11-12T18:38:24+00:00
## Meeting logs
```
boog900: meeting time: https://github.com/monero-project/meta/issues/1104
```
```
boog900: 1) Greetings
```
```
syntheticbird: Hello
```
```
hinto: hello
```
```
boog900: 2) Updates
```
```
boog900: Me: I have been spending most of my time working on integrating the fast sync crate into the sync process.
```
```
syntheticbird: me: Pushed a draft PR related to the Improve Address Book issue. It add rejections of unreachable peers after a period of time from the peer list. Replace the IndexMap used in the peer list by a BucketMap so that we keep subnet diversity (/16 for ipv4 and /32 prefix for ipv6). Waiting for feedback on the API before writing test coverage
```
```
hinto: me: no updates, rpc handlers and reviews
```
```
boog900: 3) Project: What is next for Cuprate?
```
```
boog900: hinto: is there anything you would like to discuss about the config?
```
```
hinto: I have not re-reviewed it after the recent changes yet - is there an ETA for when it needs to be merged? context: I'm short on time/flexibility (for now) because my CCS's milestones are tied to the RPC handlers and I think I'll already be late to finish them
```
```
syntheticbird: I can help reviewing it, if you think it can valuable.
```
```
boog900: > <@hinto:monero.social> I have not re-reviewed it after the recent changes yet - is there an ETA for when it needs to be merged? context: I'm short on time/flexibility (for now) because my CCS's milestones are tied to the RPC handlers and I think I'll already be late to finish them

After the `PeerSet` PR, it'll probably be the fast-sync PR then binary startup, which the config will be needed for. So not extremely urgent but is going to be needed kinda soon. 
```
```
boog900: > <@syntheticbird:monero.social> I can help reviewing it, if you think it can valuable.

hinto: is probably going to want to give the final sign off, however more reviews can't hurt.
```
```
syntheticbird: No one can beat hinto's review skills
```
```
hinto: okay then at least before the fast-sync PR is merged? maybe 1~2 weeks from now?
```
```
boog900: Yeah, worst case I'll just branch from the config branch for binary startup.
```
```
boog900: Anything else anyone wants to discuss?
```
```
boog900: Ok I think we can end here
```
```
boog900: Thanks everyone!
```
```
boog900: !meeting 
```

# Action History
- Created by: moo900 | 2024-11-05T19:30:25+00:00
- Closed at: 2024-11-12T18:38:25+00:00
