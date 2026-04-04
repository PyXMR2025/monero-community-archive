---
title: 'Cuprate Meeting #60 - Tuesday, 2025-06-17, UTC 18:00'
source_url: https://github.com/monero-project/meta/issues/1219
author: moo900
assignees: []
labels: []
created_at: '2025-06-10T18:56:17+00:00'
updated_at: '2025-06-17T18:51:50+00:00'
type: issue
status: closed
closed_at: '2025-06-17T18:51:50+00:00'
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

Previous meeting: #1216

# Discussion History
## moo900 | 2025-06-17T18:51:48+00:00
## Meeting logs
```
boog900: 1) greetings 
```
```
syntheticbird: Hi
```
```
boog900: 2) updates
```
```
boog900: I've been working on the address book 
```
```
fluorescent_beige: I'm finishing the hotswap PR (#510)
```
```
syntheticbird: Me: At the opposite of what I said last meeting. I completely forgot to include our own onion address in the address book. Making inbound server broken. This has been fixed and tested. 509 is now open for review 
```
```
hinto: hello
```
```
hinto: me: opened a new CCS: https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/591
```
```
hinto: also started cleaning up `cuprate-helper`: https://github.com/Cuprate/cuprate/pull/511
```
```
boog900: 3) Project: What is next for Cuprate?
```
```
hinto: I think `types/` is the next target for clean up, boog900: I think you had something in mind for this?
```
```
syntheticbird: I apologize, I have to quit the meeting early. Nice day to everyone
```
```
hinto: another question: can we move library crates into `crates/`? our root is getting large, other mono-repos do this as well
```
```
boog900: I wanted to get rid of it all together and try find other places for the types in it 
```
```
boog900: I prefer how we currently have it ngl 
```
```
hinto: if there is no `cuprate-types`, what crate would hold types used between 2+ crates?
```
```
boog900: we would choose one to hold the type 
```
```
hinto: I think that leads to circular deps
```
```
boog900: I don't think so, if one crate already depends on one then the one being depended on will hold the type.

Otherwise we choose one to depend on the other 
```
```
hinto: I do remember running into circular dep issues when trying to separate things last time
```
```
hinto: do you have any specific types/modules in mind?
```
```
hinto: *that should go into new separate crates
```
```
hinto: another note is that some crates only need 1 or a few types, if it were to be located in something heavy like `cuprate-blockchain` that would have to be pulled in
```
```
hinto: e.g. https://github.com/Cuprate/cuprate/blob/main/types/types/src/address_type.rs
```
```
hinto: if this were in `cuprate-p2p`, `cuprate-rpc-types` needs to pull that in and vice-versa
```
```
boog900: it would go in cuprate-wire 
```
```
boog900: which is pretty light 
```
```
boog900: yeah in this case we would have to decide between that or a separate crate
```
```
boog900: we already have cuprate-pruning 
```
```
boog900: everything in -types 
```
```
hinto: ok, can I start with `::rpc` and `::json`? I think those should be easy to pull out
```
```
hinto: all the other types need new locations specified
```
```
boog900: yeah thats fine 
```
```
hinto: for the types associated with heavy crates, what about something like `cuprate-blockchain-types`?
```
```
boog900: I think I would have to take a deeper look at the exact types, if they can be used outside of the DB sure.
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
- Created by: moo900 | 2025-06-10T18:56:17+00:00
- Closed at: 2025-06-17T18:51:50+00:00
