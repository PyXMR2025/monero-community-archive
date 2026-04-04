---
title: 'Cuprate Meeting #23 - Tuesday, 2024-10-01, UTC 18:00'
source_url: https://github.com/monero-project/meta/issues/1081
author: moo900
assignees: []
labels: []
created_at: '2024-09-24T18:21:32+00:00'
updated_at: '2024-10-01T18:48:34+00:00'
type: issue
status: closed
closed_at: '2024-10-01T18:48:34+00:00'
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

Previous meeting with logs: #1077

# Discussion History
## moo900 | 2024-10-01T18:48:33+00:00
## Meeting logs
```
hinto: I just restarted the VPS
```
```
hinto: hello
```
```
boog900: 2) Updates 
```
```
0xfffc: hi everyone
```
```
boog900: Me: I spent some time making some changes to the p2p crates were needed for the protocol request handler, I also fixed the Client drop bug and also a bug in `tower`
```
```
boog900: I hope to merge them into the block manager branch and have that ready today or tomorrow 
```
```
hinto: me: still working on internal RPC messages, also started working on JSON representations of `Block`/`Transaction` - I got serde working on all transaction and RCT versions yesterday
```
```
boog900: 2) Project: What is next for Cuprate?
```
```
hinto: boog900: I think changes will be needed to monero-serai and related crates if we want to map the types to our JSON types, e.g. bulletproofs data is not accessible
```
```
hinto: for now can #300 be merged without the mappings fully complete?
```
```
boog900: ah that's annoying ...
```
```
boog900: > <@hinto:monero.social> for now can #300 be merged without the mappings fully complete?

yeah sure 
```
```
boog900: I don't think kayabanerve is going to want to expose those fields - so another option is to write them out in consensus encoded byte form and have monero-serai read them 
```
```
boog900: although that is ugly + not efficient 
```
```
boog900: or define the mappings on monero-serai?
```
```
kayabanerve: Hi
```
```
kayabanerve: Give me one minute to read the issue?
```
```
kayabanerve: monero-serai has a lot of fields public. Anything private is likely private as I didn't want to commit to a public API/there's some invariant that needs maintaining/I didn't want to do the security considerations of making it public.
```
```
kayabanerve: I'm not against serde_json as a feature within monero-serai (soon to be monero-oxide) if serde_json can properly represent all existing types as they would be by MOnero.
```
```
boog900:  * or define the mappings in monero-serai?
```
```
kayabanerve: I know serde is quite flexible allowing items to be distinctly serialized from how they're typed in Rust, yet I also know monero-serai may be so opinionated that
```
```
kayabanerve:  * I know serde is quite flexible allowing items to be distinctly serialized from how they're typed in Rust, yet I also know monero-serai may be so opinionated that's a bit tricky and definitely required
```
```
kayabanerve: something something used an enum for transactions
```
```
kayabanerve: Honest Q. Can you not define a thin wrapper, then implement serde on the thin wrapper?
```
```
kayabanerve: You'd have to manually define the mapping between the two schemas.
```
```
boog900: to read JSON we would need to assign to individual (currently private) fields 
```
```
kayabanerve: You'd already have to do that if you add serde macros to all the fields in serde_json.
```
```
kayabanerve: Sorry, I didn't see those fields commented on on the issue.
```
```
kayabanerve: That's what it sounded like the problem was initially, I just missed that when I actually read the issue.
```
```
kayabanerve: Is there a list of problem children?
```
```
kayabanerve: *I also have some bitches about serde/serde_json, which I've prior somewhat raised, but I'm fine conceding its role in the ecosystem. I'd definitely prefer serde on wrapper types than serde on Monero types though (someone using bincode on a Monero TX 🤮)
```
```
kayabanerve: Also, y'all appear to be manually converting Timelock to an integer? Seems like we should impl From/Into u64 so that's done on monero-serai's end?
```
```
kayabanerve: (or whatever the underlying type technically is in the Monero codebase, I'd need to double check)
```
```
kayabanerve: It already has the logic, it just unfortunately isn't exposed :/
```
```
hinto: > <@kayabanerve:matrix.org> Is there a list of problem children?

I can compile a list after https://github.com/Cuprate/cuprate/pull/300
```
```
kayabanerve: If we have enough such nits Cuprate is blocked, I am fine making a branch that we work on while the audit undergoes. The current code freeze would remain in effect, the audit findings would be resolved, then we'd merge in this theoretical branch.
```
```
hinto: it would be any data `monerod` exposes through it's JSON representations that monero-serai / other crates don't expose
```
```
kayabanerve: Just let me know 👍️
```
```
boog900: Anything else anyone wants to discuss?
```
```
kayabanerve: Do y'all need base58?
```
```
boog900: I think there are requests to make a block template from an address, so yes 
```
```
kayabanerve: That means you need Address encode/decode, not base58 encode/decode, yet ACK
```
```
boog900: true although base58 is apart of that ... right?
```
```
kayabanerve: monero-address has a base58 encoder/decoder private and I'm planning to smash it out. If y'all end up needing that too, it'd be another nit to justify a branch, hence my Q.
```
```
kayabanerve: Yes but it doesn't require a dedicated base58 crate. Solely an address crate.
```
```
kayabanerve: That's the practical distinction I'm noting here.
```
```
kayabanerve: *I also want to try `std::simd` for it ^_^
```
```
hinto: > <@boog900:monero.social> I think there are requests to make a block template from an address, so yes

direct base58 is not needed for RPC, just an address sanity check: https://github.com/monero-project/monero/blob/a1dc85c5373a30f14aaf7dcfdd95f5a7375d3623/src/rpc/core_rpc_server.cpp#L1948-L1953
```
```
hinto: I don't think it's needed anywhere else in a node either, right?
```
```
kayabanerve: Y'all would be the experts :p
```
```
kayabanerve: But yes, I was thinking of the RPC methods.
```
```
boog900: nope I haven't had to use it anywhere else 
```
```
kayabanerve: So if those only need address, and not anything else, it's allg. I asked as the wallet cryptographic proofs use base58. I didn't know if other blobs in the RPC ever did.
```
```
kayabanerve: Also, of course, monero-address was smashed out of monero-wallet so it can be grabbed with minimal deps :)
```
```
boog900: The RPC has so many "formats" I am surprised pure base58 isn't in there just for the fun of it 
```
```
boog900: I think we can end here
```
```
boog900: Thanks everyone!
```
```
hinto: thanks
```

# Action History
- Created by: moo900 | 2024-09-24T18:21:32+00:00
- Closed at: 2024-10-01T18:48:34+00:00
