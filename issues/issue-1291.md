---
title: 'Cuprate Meeting #75 - Tuesday, 2025-11-11, UTC 18:00'
source_url: https://github.com/monero-project/meta/issues/1291
author: moo900
assignees: []
labels: []
created_at: '2025-11-04T18:28:47+00:00'
updated_at: '2025-11-11T18:43:42+00:00'
type: issue
status: closed
closed_at: '2025-11-11T18:43:42+00:00'
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

Previous meeting: #1287

# Discussion History
## moo900 | 2025-11-11T18:43:41+00:00
## Meeting logs
```
boog900: 1) greetings 
```
```
kayabanerve: 👋
```
```
boog900: 2) updates
```
```
kayabanerve: monerod has integrated FCMP++ and faced issues with the amount of small allocations, presumably in the circuit's intermediate representation. That's a long-term candidate to optimize.
```
```
boog900: me: still working on the linear tape DB, made some PRs. Final DB size is 194 GBs. 
```
```
kayabanerve: I missed the last meeting, but noted after how I opened a PR for a new Ed25519 crate which lets us continue the discussion on 1.0 for oxide.
```
```
boog900: also found out the reason HDDs was so slow was due to our inefficient LMDB integration  
```
```
boog900: pinging hinto 
```
```
boog900: 3) Project: What is next for Cuprate?
```
```
boog900: I will move on from the DB today as it is mostly ready, at least the first couple PRs can be reviewed 
```
```
syntheticbird: Hello everyone
```
```
kayabanerve: I have next for oxide discussions but nothing for Cuprate. Please let me know when I should speak up.
```
```
boog900: we can discuss that now, I have nothing I want to discuss on Cuprate 
```
```
syntheticbird: Same
```
```
kayabanerve: monero-io 1.0.0-rc.0?
```
```
kayabanerve: https://github.com/kayabaNerve/monero-oxide/blob/ed25519/monero-oxide/io/Cargo.toml has a single dependency of std-shims for MSRV reasons and alloc::io
```
```
kayabanerve: The only question would be:
1) If we want to move from functions to methods
2) What we want included in semver in general. It as-is, or it explicitly with default features, hazmatting the no-std variant? What's the relation of MSRV to semver?
```
```
boog900: for 1 we have already moved some of the functions to methods, I think I like how it currently is 
```
```
kayabanerve: Also, this assumes the merge of the ed25519 PR.
```
```
boog900: ideally we cover as much as we can under semver 
```
```
kayabanerve: I'm fine as-is. I don't think further usage of methods makes sense unless we want explicit IO traits.
```
```
kayabanerve: Eh. I'd understand not covering no-std under semver given we defer to a bespoke IO impl (std-shims) in that case.
```
```
kayabanerve: But then I'd say to semver on minor.
```
```
kayabanerve: *only bump the std-shims breaking version when we bump the monero crate's minor version
```
```
kayabanerve: As for MSRV, I'd say that should only be raised with minor versions.
```
```
kayabanerve: So it sounds like IO as presented and we in general just to hammer out the exact semver coverage.
```
```
boog900: ok yeah I am fine with that too, although it could get annoying as cargo assumes semver is followed when picking deps right? 
```
```
boog900: deps versions*
```
```
kayabanerve: I'd likely advocate for std builds, exclusion of multisig feature and MSRV, with exclusions from semver allowed to break on minor.
```
```
kayabanerve: Yeah. That means someone could update and need to update their Rust compiler, or update and need to update their multisig/no-std code _unless they pin a max version with `<1.1` or so_
```
```
kayabanerve: TBC, my argument for exceptions is we're defining a 1.0 with _exposed, < 1.0 deps_
```
```
kayabanerve: The ed25519 PR largely removes dalek but we still expose dalek-ff-group via multisig :/
```
```
boog900: yeah fair, I am happy to only include default features for semver until that gets a 1.0 
```
```
boog900: do you have a plan for std-shims 1.0?
```
```
kayabanerve: Eh, hashbrown and lack of core::io make me say even if we had a std-shims 1.0, I'd want a std-shims 2.0 at _some point_
```
```
kayabanerve: But core::io won't happen for years? and hashbrown updates every few months for whatever reason
```
```
kayabanerve: That arguably justifies a 1.0 on our end and a 2.0 in two years
```
```
kayabanerve: The more immediate solution is to exclude no-std builds from semver though
```
```
kayabanerve: Which may be worse but is acceptable
```
```
boog900: yeah I think that's acceptable, may annoy a few users but 🤷
```
```
boog900: anything else you wanted to discuss on monero-oxide?
```
```
kayabanerve: There's a couple open PRs?
```
```
kayabanerve: Can a maintainer please review and merge the new RPC client?
```
```
kayabanerve: :p
```
```
boog900: soon™️
```
```
kayabanerve: But no, nothing else, unless anyone's concerned about/wants to leave feedback on making curve25519-dalek opaque
```
```
hinto: hello sorry for being late, no updates - a heads up: I'll be spending more time on `monerod` for now
```
```
boog900: I think we can end here 
```
```
boog900: thanks everyone! 
```
```
boog900: !meeting  
```

# Action History
- Created by: moo900 | 2025-11-04T18:28:47+00:00
- Closed at: 2025-11-11T18:43:42+00:00
