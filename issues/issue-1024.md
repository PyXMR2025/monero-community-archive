---
title: ' Cuprate Meeting #8 - Tuesday, 2024-06-18, 18:00 UTC '
source_url: https://github.com/monero-project/meta/issues/1024
author: Boog900
assignees: []
labels: []
created_at: '2024-06-18T00:15:17+00:00'
updated_at: '2024-06-24T01:04:50+00:00'
type: issue
status: closed
closed_at: '2024-06-24T01:04:50+00:00'
---

# Original Description
[Cuprate](https://github.com/Cuprate/cuprate) is an effort to create an alternative Monero node implementation.

Location: [Libera.chat, #cuprate](https://libera.chat/) | [Matrix](https://matrix.to/#/#cuprate:monero.social?via=matrix.org&via=monero.social)

> Note that there are currently communication issues with Matrix accounts created on the matrix.org server, consider using a different homeserver to see messages.

[Join the Monero Matrix server if you don't already have a Matrix account](https://www.getmonero.org/resources/user-guides/join-monero-matrix.html)

Time: 18:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html)

Moderator: boog900

Main discussion topics:
- Greetings
- Updates: What is everyone working on?
- Project: What is next for Cuprate?
- Any other business

Please comment on GitHub in advance of the meeting if you would like to propose a discussion topic.

Previous meeting with logs: #1021

# Discussion History
## Boog900 | 2024-06-24T01:04:48+00:00
logs:

```
18:00:56 - boog900 (@boog900:monero.social): meeting time: https://github.com/monero-project/meta/issues/1024
18:01:05 - boog900 (@boog900:monero.social): 1) Greetings 
18:01:31 - hinto (@hinto:monero.social): hi
18:04:41 - boog900 (@boog900:monero.social): 2) Updates
18:06:19 - boog900 (@boog900:monero.social): Me: I posted a CCS update and have been working on adding more docs to the p2p crates  
18:07:11 - boog900 (@boog900:monero.social): I also used the p2p crates to reproduce the monerod getting killed issue :)
18:08:00 - hinto (@hinto:monero.social): me: close to finishing initial RPC type porting PR, close to finishing DB split, also working on setting up instructions for Cuprate's benchmarks
18:08:34 - boog900 (@boog900:monero.social): ah nice!
18:09:43 - hinto (@hinto:monero.social): boog900: the DB split (https://github.com/Cuprate/cuprate/pull/160) took around as much time as I thought, the separation is quite nice but the diff looks painful to review
18:10:55 - hinto (@hinto:monero.social): I'd recommend using `cargo doc` and readme/examples for API review, there's little logic change, just moving stuff around
18:12:32 - boog900 (@boog900:monero.social): alright yeah, seems like we both have some not nice reviews to do then with my protocol book PR :)
18:12:44 - boog900 (@boog900:monero.social): 3) Project: What is next for Cuprate
18:15:15 - hinto (@hinto:monero.social): SyntheticBird: do you have thoughts on this? https://github.com/Cuprate/cuprate/pull/147#discussion_r1644546531
18:19:06 - hinto (@hinto:monero.social): boog900: I was hoping I could get away with using our epee stuff until later but it probably makes sense to include it in the RPC macro now, right?
18:19:37 - hinto (@hinto:monero.social): mostly because I think investing in some `#[derive]` stuff or plugging into serde would be better long-term
18:21:21 - boog900 (@boog900:monero.social): For my next CCS I am probably going to be focusing on the `cuprated` binary and the core services (blockchain, txpool etc) with the goal being to have a binary that can sync and stay synchronized with the network + participate in tx broadcasting. 
18:22:55 - boog900 (@boog900:monero.social): <@hinto:monero.social "mostly because I think investing..."> there was a reason serde is hard to use with epee but I can't remember it right now, originally there was a custom derive macro but it was disgusting 
18:23:23 - boog900 (@boog900:monero.social): https://github.com/Boog900/epee-encoding/blob/main/epee-encoding-derive/src/lib.rs
18:31:34 - hinto (@hinto:monero.social): lots of code will be built on-top of the current epee-encoding, is this okay?
18:34:13 - boog900 (@boog900:monero.social): should be yes, I don't expect to make any changes to it
18:34:14 - SyntheticBird: Hi, sorry for being late im on the move. Update on my side: launched new website and restarted syncing experiment
18:36:20 - boog900 (@boog900:monero.social): <@hinto:monero.social "SyntheticBird: do you have thoug..."> SyntheticBird: did you see this?
18:36:37 - SyntheticBird: <@boog900:monero.social "SyntheticBird: did you see this?"> Yes it's weird
18:36:56 - SyntheticBird: I'll recheck when home
18:41:16 - hinto (@hinto:monero.social): boog900: can we prioritize merging #132 -> #164?
18:41:51 - hinto (@hinto:monero.social): that thing is a ticking time bomb of merge conflicts
18:42:09 - boog900 (@boog900:monero.social): yeah sure 
18:44:54 - boog900 (@boog900:monero.social): Is there anything else people want to discuss? 
18:47:33 - boog900 (@boog900:monero.social): we can end the meeting here then
18:47:39 - boog900 (@boog900:monero.social): Thanks everyone 
18:49:26 - hinto (@hinto:monero.social): thanks

```

# Action History
- Created by: Boog900 | 2024-06-18T00:15:17+00:00
- Closed at: 2024-06-24T01:04:50+00:00
