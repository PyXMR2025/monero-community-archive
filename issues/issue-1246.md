---
title: 'Cuprate Meeting #67 - Tuesday, 2025-08-05, UTC 18:00'
source_url: https://github.com/monero-project/meta/issues/1246
author: moo900
assignees: []
labels: []
created_at: '2025-07-29T18:57:39+00:00'
updated_at: '2025-08-05T18:48:36+00:00'
type: issue
status: closed
closed_at: '2025-08-05T18:48:36+00:00'
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

Previous meeting: #1243

# Discussion History
## moo900 | 2025-08-05T18:48:35+00:00
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
boog900: me: made some changes to SyntheticBovinae's Tor RP and merged it. Also did some work on some smaller PRs
```
```
hinto: me: no updates, still waiting on CCS
```
```
boog900: hopefully it is merged soon 🙏
```
```
boog900: 3) Project: What is next for Cuprate?
```
```
hinto: I'd like to note if there are no discussions needed we can end meetings early
```
```
hinto: (although there are always longer term decisions that can/should be settled)
```
```
boog900: next release will contain Tor support, also I don't know if it has been mentioned but there is a new I2P Rust router: https://github.com/altonen/emissary

An I2p dev did say they were working on integrating that into cuprate ... so we may have embedded I2p support too 
```
```
boog900: I don't know how comfortable I am with embedding that router with it being so new, but I guess that discussion can wait for when a PR is made 
```
```
boog900: if you have any that we can decide now, without SyntheticBovinae sure, otherwise we can end here 
```
```
hinto: ok, we can go down the list
```
```
hinto: issue: https://github.com/Cuprate/cuprate/issues/522
```
```
hinto: solution: `fn main() -> Result<(), anyhow::Error>`?
```
```
hinto: (and replace all the `unwrap()`s)
```
```
boog900: yeah I was thinking we are probably going to need better error handling when we make cuprate usable as a lib too 
```
```
boog900: I think that is going to be a pretty big change, low priority IMO 
```
```
hinto: issue: https://github.com/Cuprate/cuprate/issues/388
```
```
hinto: solution: extend `cuprated`'s RPC API as a superset/intersect of `monerod`?
```
```
boog900: probably but I worry if that is just going to make the RPC interface even more confusing 
```
```
hinto: to some extent the API already is partial e.g. mining endpoints
```
```
boog900: I think if we are making a new API we should make sure it is done properly, which is going to take a while, for now I don't really think its the best thing to spend time on.
```
```
hinto: I would say if a "core" RPC spec and the extensions were documented properly (maybe in the user-book) then it would be fine, similar to the various specs in ethereum
```
```
hinto: agreed it would take some time
```
```
hinto: issue: https://github.com/Cuprate/cuprate/issues/470
```
```
hinto: where is this in the priority list?
```
```
boog900: I would like to see that before a beta release although I don't want to put a requirement on it 
```
```
boog900: hinto: how long would you expect that to take? 
```
```
hinto: not sure, tobtoht would probably know
```
```
hinto: are bootstrappable builds higher priority than ZMQ?
```
```
boog900: I personally would work on ZMQ first, because I think I could get it done quicker but I would rank them similarly IMO 
```
```
hinto: issue: https://github.com/Cuprate/cuprate/issues/269
```
```
hinto: I think this can be closed? the port numbers for the existing interfaces will be the same
```
```
boog900: yes
```
```
hinto: pr: https://github.com/Cuprate/cuprate/pull/367
```
```
hinto: I would prefer having this lint on, I can image `_ =>` leading to bad things
```
```
hinto: imagine*
```
```
boog900: yeah, it is a bit annoying but I agree 
```
```
boog900: it is still a draft FWIW
```
```
hinto: ok, will fix conflicts and open eventually
```
```
boog900: any more, or we can end here?
```
```
hinto: we can end
```
```
boog900: thanks hinto 
```
```
boog900: !meeting 
```

# Action History
- Created by: moo900 | 2025-07-29T18:57:39+00:00
- Closed at: 2025-08-05T18:48:36+00:00
