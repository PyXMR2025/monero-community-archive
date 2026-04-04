---
title: 'Cuprate Meeting #78 - Tuesday, 2025-12-02, UTC 18:00'
source_url: https://github.com/monero-project/meta/issues/1302
author: moo900
assignees: []
labels: []
created_at: '2025-11-25T19:01:47+00:00'
updated_at: '2025-12-02T18:30:31+00:00'
type: issue
status: closed
closed_at: '2025-12-02T18:30:31+00:00'
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

Previous meeting: #1298

# Discussion History
## moo900 | 2025-12-02T18:30:30+00:00
## Meeting logs
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
sgp_: Hello
```
```
kayabanerve: 👋
```
```
kayabanerve: Fixed a few bugs for monero-oxide. RPC PR awaits review. Otherwise, occupied with Serai
```
```
hinto: me: I have been considering starting an org to host code that doesn't fit anywhere else cleanly (explorer, site, etc) and/or to work on things that will ultimately be upstreamed to Cuprate (bootstrappable builds, ZMQ, new subsystems)
```
```
boog900: me: created a new repo for the tapes database, continued my work on the wip branch. I haven't been able to do much for FCMP this week, I plan to keep my focus on the rest of the node. I would rather Cuprate work well for a potential RingCT stressnet than have a buggy FCMP stressnet. 
```
```
boog900: 3) Project: What is next for Cuprate?
```
```
boog900: does anyone disagree with me putting FCMP aside for now? 
```
```
boog900: the other option is putting RPC aside 
```
```
rucknium: Sounds fine to me.
```
```
hinto: I guess `cuprated` will be split from the network for a while post-FCMP?
```
```
boog900: no I was going to try get us into the next FCMP stressnet but I doubt we will make it in a good state. I do think we will make the mainnet HF though 
```
```
boog900: probably without as much lead time as monerod though 
```
```
boog900: does anyone have anything more they would like to discuss today? 
```
```
boog900: wdym by site as well, we already have a site under the cuprate org?
```
```
hinto: ah, I meant the frontend for a (theoretical) explorer daemon
```
```
boog900: tbf the Cuprate org is a bit of a mess, I don't think that would be out of place 
```
```
boog900: if there is nothing else to discuss we can end here
```
```
boog900: !meeting 
```

# Action History
- Created by: moo900 | 2025-11-25T19:01:47+00:00
- Closed at: 2025-12-02T18:30:31+00:00
