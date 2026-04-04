---
title: 'Cuprate Meeting #95 - Tuesday, 2026-03-24, UTC 18:00'
source_url: https://github.com/monero-project/meta/issues/1354
author: moo900
assignees: []
labels: []
created_at: '2026-03-17T18:33:01+00:00'
updated_at: '2026-03-24T18:38:22+00:00'
type: issue
status: closed
closed_at: '2026-03-24T18:38:22+00:00'
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

Previous meeting: #1351

# Discussion History
## moo900 | 2026-03-24T18:38:21+00:00
## Meeting logs
```
boog900: 1) greetings 
```
```
hinto: hello
```
```
syntheticbird: Hi
```
```
redsh4de: helloo
```
```
boog900: 2) updates 
```
```
redsh4de: me: pushed the final changes I wanted to make for the embeddable cuprate PR just now, turned what used to be SyncNotify into Syncer/SyncerHandle, small doc nits
```
```
redsh4de: * me: pushed the final changes I wanted to make for the embeddable cuprate PR just now, turned what used to be SyncNotify into Syncer/SyncerHandle, got rid of all the remaining node statics, small doc nits
```
```
boog900: Me: working on RPC, getting the current changes ready to PR. 
```
```
hinto: me: still focusing on 587 review; the current test run is still crashing on 2GB (3 times so far), there is no good info on DEBUG level logs so I've set up journalctl to not prune as much, hopefully I can confirm that it's just memory exhaustion
```
```
boog900: Is that after sync?
```
```
hinto: yes, crashing occurs after sync
```
```
boog900: Weird 
```
```
boog900: 3) Project: What is next for Cuprate?
```
```
boog900: Does anyone have anything they want to discuss?
```
```
redsh4de: anything other issues from the wishlist i could have a look at over the week?
```
```
boog900: Reviewing the tape db :) 
```
```
redsh4de: right, that reminds me i had a bug with the tape reader with dev builds specifically
```
```
redsh4de: will note it down
```
```
boog900: Hmm was that very recent
```
```
boog900: I have fixed bugs since opening the or for review 
```
```
boog900: PR*
```
```
redsh4de: it was last week or so, i'm seeing if i can reproduce it rn
```
```
redsh4de: yeah, when running with the dev profile getting this after a few seconds of downloading blocks:

2026-03-24T18:26:20.934657Z  INFO incoming_block_batch{start_height=8099 len=3}: Successfully added block batch fast_sync=true
2026-03-24T18:26:20.935064Z  INFO incoming_block_batch{start_height=8102 len=3}: Successfully added block batch fast_sync=true
2026-03-24T18:26:20.935487Z  INFO incoming_block_batch{start_height=8105 len=3}: Successfully added block batch fast_sync=true
2026-03-24T18:26:20.935858Z ERROR blockchain_writer_thread: Failed to handle write request: NotFound

thread 'cuprated-tokio' (99044) panicked at binaries/cuprated/src/blockchain/manager/handler.rs:707:14:
A service critical to Cuprate's function returned an unexpected error.: NotFound
note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace
Aborted (core dumped)


this wasn't an issue with `--release`
```
```
syntheticbird: is this easily reproducible ?
```
```
redsh4de: * yeah, when running with the dev profile getting this after a few seconds of downloading blocks:


2026-03-24T18:26:20.934657Z  INFO incoming_block_batch{start_height=8099 len=3}: Successfully added block batch fast_sync=true
2026-03-24T18:26:20.935064Z  INFO incoming_block_batch{start_height=8102 len=3}: Successfully added block batch fast_sync=true
2026-03-24T18:26:20.935487Z  INFO incoming_block_batch{start_height=8105 len=3}: Successfully added block batch fast_sync=true
2026-03-24T18:26:20.935858Z ERROR blockchain_writer_thread: Failed to handle write request: NotFound

thread 'cuprated-tokio' (99044) panicked at binaries/cuprated/src/blockchain/manager/handler.rs:707:14:
A service critical to Cuprate's function returned an unexpected error.: NotFound
note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace
Aborted (core dumped)

went away with `--release`
```
```
syntheticbird: or did you get this once
```
```
redsh4de: yeah, just by running `cargo run --bin cuprated`

not an issue with `cargo run --bin cuprated --release`
```
```
boog900: Fun
```
```
boog900: Will debug after the meeting
```
```
boog900: Anything else to discuss?
```
```
redsh4de: nothing from my side for now
```
```
redsh4de: will rebase the shutdown branches in a bit and leave them alone until the next reviews :)
```
```
boog900: We can end here 
```
```
boog900: Thanks everyone!
```
```
boog900: !meeting 
```

# Action History
- Created by: moo900 | 2026-03-17T18:33:01+00:00
- Closed at: 2026-03-24T18:38:22+00:00
