---
title: 'Cuprate Meeting #56 - Tuesday, 2025-05-20, UTC 18:00'
source_url: https://github.com/monero-project/meta/issues/1203
author: moo900
assignees: []
labels: []
created_at: '2025-05-13T18:58:07+00:00'
updated_at: '2025-05-20T19:06:28+00:00'
type: issue
status: closed
closed_at: '2025-05-20T19:06:28+00:00'
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

Previous meeting: #1199

# Discussion History
## moo900 | 2025-05-20T19:06:27+00:00
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
ack-j: Hi
```
```
boog900: me: I worked on the tx-pool manager, and opened a draft pr which should be ready soon  
```
```
hinto: me: still working on / testing various RPC handler behavior in `cuprated`
```
```
ack-j: I fuzzed the harnesses written by boog for the last week using 20 cpu cores but did not discover a crash.
```
```
boog900: thank you 🙏
```
```
hinto: Ah, I should have mentioned that too - I am doing the same on 16 cores, also no crashes yet, here's `oxide_tx`:


#24656350329: cov: 1167 ft: 3924 corp: 598 exec/s: 16236 oom/timeout/crash: 0/0/0 time: 508050s job: 5204 dft_time: 0

```
```
boog900: I'll work on getting it merged today
```
```
boog900: 3) Project: What is next for Cuprate?
```
```
hinto: > windows CI is failing on randomx: https://github.com/Cuprate/cuprate/actions/runs/15056098589/job/42326414888

This will have to be fixed before next release (17 days away) since the windows release build are affected
```
```
boog900: ah yeah I looked at that but can't see anything obvious 
```
```
hinto: did anyone want to handle this? otherwise I can spend time on it
```
```
hinto: I have also been thinking that the 4-week release cycle is unnecessarily fast, I think ~6 could be a better pace 
```
```
boog900: I personally don't want to fight windows CI again 
```
```
boog900: yeah I agree 
```
```
hinto: Literally Public: agree to release every 6 weeks (after the next release)?
```
```
hinto: boog900: ok, I will handle it
```
```
hinto: also, reminder that RPC PRs are ready: 423 451
```
```
rucknium: June 4-6 there will be a conference on scientific computing in Rust: https://scientificcomputing.rs/2025/talklist
Talks will be posted on Youtube.
```
```
boog900: Literally Public: said they would be a bit late to the meeting, anything anyone wants to discuss while we wait
```
```
hinto: there are some broad issues I opened we could discuss
```
```
hinto: "Change release asset naming scheme": https://github.com/Cuprate/cuprate/issues/479
```
```
hinto: reth follow this, other broader Rust projects as well e.g. https://github.com/BurntSushi/ripgrep/releases/tag/14.1.1
```
```
boog900: yeah I think that's a good idea 
```
```
hinto: "Architecture book -> Reference book": https://github.com/Cuprate/cuprate/issues/476
```
```
hinto: it was a bit painful to write this issue although it does not seem worth it to spend time to document the "how" of Cuprate for potential future maintainers
```
```
hinto: and so I think a more precise reference instead would be more valuable considering it will likely only be us maintaining Cuprate
```
```
hinto: or alternatively: "the code is the reference" and we could skip the book altogether
```
```
rucknium: If I had a piconero for every time I read in a paper, "The bitcoin protocol does not have an official protocol specification, so we must guess what the protocol is based on the source code," I would have a lot of piconeros.
```
```
boog900: I do think some document like a book would be good to describe the big structures/flows, I do think in its current form the book is too verbose 
```
```
syntheticbird: hi
```
```
syntheticbird: sorry for being late
```
```
syntheticbird: update for me: Finished the onion addressing and tor zone definition PR, all that is left is implementing the Transport and Cuprate will be able to to connect to Tor nodes
```
```
syntheticbird: Fine for me
```
```
syntheticbird: Fwiw even the Rust reference book is outdated and lag behind updates. For naming, I would prefer "Architecture Book" just to avoid setting an unrealistic expectation.
```
```
syntheticbird: I like all the details of the current book ngl
```
```
boog900: I think it probably is too much to maintain 
```
```
boog900: the code docs are enough for most things 
```
```
boog900: anything else anyone wants to add or we can end here and decide on this another time
```
```
syntheticbird: i think hinto was writing?
```
```
syntheticbird: **hinti is typing...**
```
```
syntheticbird: epic fail
```
```
boog900: hinto can finish writing :)
```
```
hinto: I would prefer a book with less verbosity as well
```
```
hinto: although this can be decided another time
```
```
boog900: I think we can end here 
```
```
boog900: thanks everyone!
```
```
hinto: thanks
```

# Action History
- Created by: moo900 | 2025-05-13T18:58:07+00:00
- Closed at: 2025-05-20T19:06:28+00:00
