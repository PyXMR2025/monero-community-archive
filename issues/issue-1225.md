---
title: 'Cuprate Meeting #62 - Tuesday, 2025-07-01, UTC 18:00'
source_url: https://github.com/monero-project/meta/issues/1225
author: moo900
assignees: []
labels: []
created_at: '2025-06-24T19:33:41+00:00'
updated_at: '2025-07-01T19:07:28+00:00'
type: issue
status: closed
closed_at: '2025-07-01T19:07:28+00:00'
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

Previous meeting: #1222

# Discussion History
## moo900 | 2025-07-01T19:07:27+00:00
## Meeting logs
```
boog900: 1) greetings 
```
```
syntheticbird: Hi
```
```
fluorescent_beige: Hi
```
```
hinto: hello
```
```
boog900: 2) Updates: What is everyone working on?
```
```
boog900: Me: still finishing up the address book changes, also left comments on the PRs mentioned last week 
```
```
syntheticbird: Me: Addressed first review round on #509. Preparing in parallel a book update PR
```
```
fluorescent_beige: Got db hotswap done mostly, will test now and then mark ready for review 
```
```
hinto: no updates from me, still in-between CCSs
```
```
boog900: 3) Project: What is next for Cuprate?
```
```
hinto: SyntheticBovinae: 0.0.5 is in 16 days, do you think 509 and related will be ready and/or should be included?
```
```
syntheticbird: Yes
```
```
syntheticbird: The book might not be approved in time
```
```
syntheticbird: but I'll make sure to respond to review asap for it to be included within next release
```
```
boog900: SyntheticBovinae: https://github.com/Cuprate/cuprate/pull/509#discussion_r2175732749
```
```
boog900: doesn't monerod do this by default? 
```
```
syntheticbird: It does
```
```
basses: > <@syntheticbird:monero.social> I don't understand who rando is replying to

I think you can check some here https://github.com/Cuprate/cuprate/blob/main/misc/RELEASE_CHECKLIST.md?
```
```
basses: is this a template as reminder to releases or things to do/implement?
```
```
boog900: that is just a checklist that needs to be done on every release not a TODO for beta 
```
```
hinto: it's a template for tracking releases, here's an example: https://github.com/Cuprate/cuprate/issues/500
```
```
basses: ok, thanks.
```
```
boog900: I do think leaving it on is a good idea 
```
```
boog900: as most people would not care I would think 
```
```
syntheticbird: In 95% of the case. The node is announced, but port is block. The same user that do not care about it are the one with ports closed.
```
```
boog900: true with so few reachable nodes tho I wouldn't want to drop some because they forgot to turn this setting on 
```
```
syntheticbird: I do understand that. That's why i am saying, that personally i wouldn't like a software to listen on without me having explicitly consented to it. That's nice to have a 4% increase in incoming node, but that's also kind of playing on their ignorance.
```
```
syntheticbird: maybe i'm the only one seeing an issue here
```
```
syntheticbird: whoever is reading the meeting don't hesitate to express yourself
```
```
boog900: yeah I would more understand if listening for incoming was completely different than making outbound connections but really it is all the same protocol 
```
```
syntheticbird: very true. The threat model is the same
```
```
boog900: I think having the option to not advertise is good but we should leave it on as really there are few reasons not to 
```
```
lm: My two cents: I would expect a node to listen by default, like I expect any server software to do so
```
```
syntheticbird: fair enough.
```
```
syntheticbird: I stand convinced
```
```
syntheticbird: I will edit it to true then
```
```
syntheticbird: boog900: regarding incoming on by default
```
```
syntheticbird: As is, tor inbound is disabled by default, like monerod, because anonymous-inbound needs to be defined for it work. However, we don't need that in arti mode
```
```
syntheticbird: but the field is exactly the same
```
```
syntheticbird: since it's placed under p2p.tor_net
```
```
syntheticbird: do you think we should move inbound to arti and tor, so that arti is on by default, while tor is off?
```
```
syntheticbird: * do you think we should move inbound boolean to arti config and tor config, so that arti is on by default, while tor is off?
```
```
syntheticbird: or we could let inbound on, but actually either quit or warn on anonymous inbound being empty
```
```
syntheticbird: in daemon mode
```
```
boog900: I say we leave it on for no, with Tor disabled by default. If someone enables Tor-arti it accepts inbound, if someone enables Tor-daemon it panics telling them to add an address or disable inbound 
```
```
boog900: yes this would be my choice 
```
```
boog900: * I say we leave it on for now, with Tor disabled by default. If someone enables Tor-arti it accepts inbound, if someone enables Tor-daemon it panics telling them to add an address or disable inbound 
```
```
syntheticbird: alright
```
```
boog900: anything else anyone wants to discuss today?
```
```
hinto: SyntheticBovinae: this should fix 509 CI: https://github.com/Cuprate/cuprate/pull/513
```
```
syntheticbird: Thanks a lot
```
```
hinto: speaking of, does bringing in tor/arti really make our Cargo.lock that much larger?
```
```
hinto: are there leftover additions that weren't removed?
```
```
syntheticbird: huh
```
```
syntheticbird: I do feel an increase in cuprated compilation time
```
```
syntheticbird: compared to before
```
```
syntheticbird: but I admit I haven't checked dependency count
```
```
syntheticbird: on tor branch we're at 611 dependency declaration in Cargo.lock
```
```
boog900: that including test deps?
```
```
syntheticbird: compared to 395 on main
```
```
syntheticbird: lmoa
```
```
syntheticbird: I just checked the number of `[[package]]` occurence in Cargo.lock
```
```
boog900: yeah that is a crazy increase 
```
```
syntheticbird: lol ye no shit i felt an increase. +220 dependencies for the grinder
```
```
syntheticbird: and I've a top notch cpu
```
```
syntheticbird: Maybe this is worth feature gatekeeping tor
```
```
syntheticbird: * Maybe this is worth feature gatekeeping arti
```
```
syntheticbird: but I'll need to think it through
```
```
syntheticbird: * but I'll need to think it through because as is, it's either Tor and Arti or nothing
```
```
boog900: releasing 2 binaries is annoying though 
```
```
syntheticbird: i assume feature gatekeeping is always for advanced users
```
```
syntheticbird: so we wouldn't release 2 binaries
```
```
boog900: for now don't worry 
```
```
boog900: true 
```
```
hinto: bash
git checkout origin/main -- Cargo.lock
cargo build
git apply Cargo.lock && git commit -m 'reduce deps'

```
```
hinto: the diff should be closer to +1349
```
```
syntheticbird: processing
```
```
syntheticbird: please hold
```
```
syntheticbird: mhm
```
```
syntheticbird: `No valid patches in input`
```
```
syntheticbird: I love git
```
```
syntheticbird: hinto: nope https://github.com/Cuprate/cuprate/pull/509/files
```
```
syntheticbird: +3,398
```
```
boog900: Anything else to discuss today?
```
```
hinto: it seems to be +3398: https://github.com/Cuprate/cuprate/pull/514/files#diff-13ee4b2252c9e516a0547f2891aa2105c3ca71c6d7a1e682c69be97998dfc87e
```
```
syntheticbird: I should probably end up with the same result by cleaning cargo right?
```
```
syntheticbird: oh no cargo clean don't remove cargo.lock
```
```
syntheticbird: nvm
```
```
syntheticbird: i'll redo the commit thx hinto
```
```
boog900: I think we can end here 
```
```
boog900: Thanks everyone!
```
```
syntheticbird: thanks
```
```
hinto: thanks
```

# Action History
- Created by: moo900 | 2025-06-24T19:33:41+00:00
- Closed at: 2025-07-01T19:07:28+00:00
