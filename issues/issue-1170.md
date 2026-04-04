---
title: 'Cuprate Meeting #47 - Tuesday, 2025-03-18, UTC 18:00'
source_url: https://github.com/monero-project/meta/issues/1170
author: moo900
assignees: []
labels: []
created_at: '2025-03-11T19:17:55+00:00'
updated_at: '2025-03-18T19:09:05+00:00'
type: issue
status: closed
closed_at: '2025-03-18T19:09:04+00:00'
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

Previous meeting: #1166

# Discussion History
## moo900 | 2025-03-18T19:09:03+00:00
## Meeting logs
```
boog900: 1) greetings
```
```
hinto: hello
```
```
boog900: 2) udates 
```
```
boog900:  * 2. updates
```
```
boog900: Cuprate had its first release 🚀
```
```
boog900: I have spent some time working on fixing the alt blocks issue, hopefully it should be full fixed now
```
```
boog900:  * I have spent some time working on fixing the alt blocks issue, hopefully it should be fully fixed now
```
```
hinto: me: I took a little time off after release. I am catching up with `monero-project` PRs - I think I will be focusing on fcmp++ related things for now.
```
```
boog900: > Project: What is next for Cuprate?
```
```
boog900:  * 3. Project: What is next for Cuprate?
```
```
syntheticbird: Hello (sorry for being late)
```
```
syntheticbird: No update on my ens
```
```
syntheticbird: end*
```
```
boog900: > <@hinto:monero.social> me: I took a little time off after release. I am catching up with `monero-project` PRs - I think I will be focusing on fcmp++ related things for now.

is your time going to be split between the 2?
```
```
hinto: yes although AFAICT the things I can help with aren't necessarily high priority / required immediately / ready, so I think it will be quick
```
```
boog900: anything anyone wants to discuss today?
```
```
hinto: SyntheticBird: in previous meetings it was noted that `cuprated` would only be using Tor for TX broadcasts, but in the gist there is `--p2p-proxy` - do you have clarification here?
```
```
hinto: this msg btw
```
```
hinto: I assume the plan is to behave like `monerod` and that `--p2p-proxy` is going to be skipped for now (the gist was created before the meeting)
```
```
syntheticbird: (just hoped on pc sry for delay)
```
```
syntheticbird: `p2p-proxy` is the general flag for any proxy use for clearnet. Main usage is actually SOCKS5.
```
```
syntheticbird: But the plan was also to support `"arti"` as a native alternative to `torsocks monerod` (which is documented in monero repo README)
```
```
syntheticbird: So there is actually a difference
```
```
syntheticbird: When using `p2p-proxy` we're connecting to clearnet nodes, not onion nodes. Onion nodes are part of Tor NetworkZone, which will only communicate tx
```
```
syntheticbird: I haven't read Rucknium linked paper yet but plan on doing so. I still didn't found the resource that was talking about block downloading over Tor. But since Monero is documenting the use of `torsocks`-wrapped monerod, I just assumed this was ok.
```
```
syntheticbird: I hope I clarified
```
```
hinto: thanks - there's a mention of something like `torsocks cuprated` in the user book, considering the cons I think I'll be removing it
```
```
spirobel: I was wondering why the sybil / eclipse attacks were discussed specifically in the context of TOR. Is it so much more expensive to do this without tor?
```
```
syntheticbird: Tor onion address are free
```
```
syntheticbird: and there are much less users on Tor
```
```
syntheticbird: so waaaaaayyyy easier to coerce
```
```
spirobel: on the other hand ip addresses are cheap too. 
```
```
boog900: We prefer IPs in different /16 subnets to make it more expensive 
```
```
boog900: LinkingLion has 40% of the IPs on the monero network but only 15% of the effective nodes due to monerod preferring different subnets 
```
```
boog900: And monerod doesn't use IPv6 by default 
```
```
boog900: anything else anyone wants to discuss? 
```
```
boog900: ok I think we can end here thanks everyone#!
```
```
hinto: thanks
```

# Action History
- Created by: moo900 | 2025-03-11T19:17:55+00:00
- Closed at: 2025-03-18T19:09:04+00:00
