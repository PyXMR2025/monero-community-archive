---
title: 'Cuprate Meeting #89 - Tuesday, 2026-02-10, UTC 18:00'
source_url: https://github.com/monero-project/meta/issues/1336
author: moo900
assignees: []
labels: []
created_at: '2026-02-03T18:25:57+00:00'
updated_at: '2026-02-10T18:46:11+00:00'
type: issue
status: closed
closed_at: '2026-02-10T18:46:11+00:00'
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

Previous meeting: #1332

# Discussion History
## moo900 | 2026-02-10T18:46:10+00:00
## Meeting logs
```
boog900: 1) greetings 
```
```
syntheticbird: hello there
```
```
redsh4de: hello
```
```
boog900: 2) updates
```
```
hinto: hello
```
```
boog900: I wasn't able to work much on Cuprate last week, however the new database is pretty much ready. It has all the functionality of the current DB I just need to clean it up a little then PR it. 
```
```
redsh4de: In PR #578, added a guard to TorMode::Auto resolution to skip the resolve step if tor is disabled to prevent a useless socks5 query
```
```
hinto: me: have been trying out docker reproducible builds perhaps as an interim; took a small break last week
```
```
boog900: 3) Project: What is next for Cuprate?
```
```
boog900: I plan to PR the new DB after the meeting, do we think we should do a new release once it is merged? 
```
```
boog900: or wait for RPC 
```
```
hinto: How long would it take to open + review RPC? 
```
```
boog900: at least a month most likely 2 
```
```
hinto: releasing after DB asap seems better in that case IMO
```
```
boog900: itll probably take a while to review too 
```
```
hinto: after DB is merged I think we'll know if/when to release
```
```
hinto: any thoughts on using docker for repro builds in the interim before (hopefully, eventually) moving onto something like StageX?
```
```
syntheticbird: i'm completely for. This is a cheap and easy solution for the short-term. I initially proposed that we built inside snapshotted debian machines since debian repository are archived
```
```
hinto: I said previously I'd prefer going straight to bootstrappable builds although having at the least reproducible builds in-time for a beta release is enticing
```
```
syntheticbird: for it
```
```
boog900: yeah I would be ok with that 
```
```
kayabanerve: Using StageX would still require using Docker, so this moves along the right path. Why can't StageX be used now?
```
```
kayabanerve: (I recently went on a Linux arc and made a bunch of PRs upstream)
```
```
kayabanerve: https://github.com/serai-dex/serai/blob/737dbcbaa78ab817cc1c435cb2b6c5d24d1c4391/orchestration/runtime/Dockerfile#L1-L11 is old code of mine to use a Debian snapshot in a container
```
```
hinto: I'd be ok with StageX right now as well, although the maintenance for just docker would probably be less complex for boog900 if changes are needed without me
```
```
kayabanerve: I mean, the pitch of StageX is that you can do FROM stagex/pallet-rust instead of FROM rust:stable and immediately be premised on StageX.
```
```
kayabanerve: The only issue with StageX is if some dep is incompatible/not yet packaged for StageX, hence my question.
```
```
kayabanerve: *should be if
```
```
hinto: yup I'd assume it would have more things to workaround and would take longer and be more of a pain to maintain
```
```
kayabanerve: Here's Serai's use of a StageX package to build one piece of our code: https://github.com/serai-dex/serai/tree/next-polkadot-sdk/orchestration/runtime/bootstrap/Containerfile
```
```
kayabanerve: Ideally, yes, it's literally just the `FROM` command.
```
```
kayabanerve: Eh, maybe, but I'd try with StageX first and go from there before deciding to start from Debian.
```
```
kayabanerve: I did have to upstream support to StageX for LLVM 21, Rust 1.93.0, to get _specific_ goals of mine achieved, but that isn't generally necessary 😅
```
```
kayabanerve: And also, I already upstreamed LLVM 21 and Rust 1.93.0 😅 So those are available now if you use the repository and not a binary release
```
```
kayabanerve: I'd try it and I'll be happy to help if anything comes up :) Heard if it does become something to work through and not in the current scope though
```
```
boog900: anything else to discuss today?
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
- Created by: moo900 | 2026-02-03T18:25:57+00:00
- Closed at: 2026-02-10T18:46:11+00:00
