---
title: 'Cuprate Meeting #55 - Tuesday, 2025-05-13, UTC 18:00'
source_url: https://github.com/monero-project/meta/issues/1199
author: moo900
assignees: []
labels: []
created_at: '2025-05-06T18:48:33+00:00'
updated_at: '2025-05-13T18:58:07+00:00'
type: issue
status: closed
closed_at: '2025-05-13T18:58:07+00:00'
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

Previous meeting: #1196

# Discussion History
## moo900 | 2025-05-13T18:58:06+00:00
## Meeting logs
```
boog900: 1) greetings 
```
```
syntheticbird: Hello
```
```
hinto: hello
```
```
boog900: 2) updates
```
```
boog900: I spent some time working on fuzz tests after the OOM I found in epee last week 
```
```
syntheticbird: Me: Finishing up the last details with io timeout pr, will pr open for review after meeting. Also continuing tor zone definition.
```
```
hinto: me: working on wiring the real RPC handlers in `cuprated` to the server, also the RPC section in the user-book
```
```
hinto: I've also made issues for the first `cuprated` beta/stable releases and will start tracking things that seem to need resolving before then: https://github.com/Cuprate/cuprate/issues/467, https://github.com/Cuprate/cuprate/issues/471
```
```
hinto: 471 may also include things that are far away although would be nice to settle before `v1.0.0`
```
```
hinto: also the question of when it is appropriate to go from `alpha` -> `beta` -> `stable` needs an answer
```
```
syntheticbird: we can pass to ".
```
```
syntheticbird: 3.*
```
```
boog900: yes
```
```
boog900: 3) Project: What is next for Cuprate?
```
```
syntheticbird: i think we should pass to beta when we're core-feature-complete
```
```
boog900: IMO beta should happen once we hit parity with monerod 
```
```
syntheticbird: yeah
```
```
syntheticbird: RPC + Tor imo
```
```
syntheticbird: maybe ZMQ depending on if someone is willing to take the work
```
```
boog900: and ZMQ if we are going for parity 
```
```
boog900: I don't think it will be as hard as RPC 
```
```
syntheticbird: if you say so
```
```
syntheticbird: I just wouldn't want us to get 1. stuck on releasing beta for 3 months and 2. not be able to work on FCMP integration
```
```
boog900: fair, we could not do ZMQ before beta if that's preferred  
```
```
syntheticbird: I would also add Guix for beta
```
```
syntheticbird: but idk would like your thoughts
```
```
boog900: yeah I think that would be good
```
```
hinto: FYI the RPC server and doc PRs are ready: 423 451, merge would be nice as other PRs will depend on them 
```
```
boog900: sure will do 
```
```
boog900: hinto: have you had a chance to look at the fuzz PR
```
```
hinto: no not yet - do you have a plan for this to be ran somewhere continuously?
```
```
syntheticbird: on my end I have an unused VPS for the job
```
```
syntheticbird: so i can repurpose it and make it run 24/7
```
```
boog900: not yet 
```
```
boog900: I ran them for quite a few hours on my PC tho
```
```
syntheticbird: Fuzzing is gambling
```
```
syntheticbird: You run only a few hours you were this 🤏 close from hitting the crash 💎
```
```
boog900: I did find 1 issue for FWIW 
```
```
hinto: I'm unsure if `cargo-fuzz` is applicable although we could use OSS-Fuzz as well: https://github.com/google/oss-fuzz/tree/master/projects/monero
```
```
boog900: IIRC don't they have a usage requirement 
```
```
syntheticbird: idk but i would be surprised if they accepted any os project passing by
```
```
hinto: I haven't looked into it deeply myself but here's info: https://google.github.io/oss-fuzz/getting-started/accepting-new-projects/
```
```
boog900: https://google.github.io/oss-fuzz/faq/#what-kind-of-projects-are-you-accepting
```
```
boog900: so no hard requirements but they probably wouldn't accept us yet 
```
```
syntheticbird: yup
```
```
syntheticbird: need more fame
```
```
syntheticbird: to keep in mind for after stable i suppose
```
```
boog900: just searched for -rs and found this: https://github.com/google/oss-fuzz/tree/master/projects/flate2-rs
```
```
boog900: it uses cargo-fuzz: https://github.com/rust-lang/flate2-rs/blob/main/fuzz/Cargo.toml
```
```
syntheticbird: awesome
```
```
boog900: anything else anyone wants to discuss today?
```
```
syntheticbird: yes
```
```
boog900: what would you like to discuss? 
```
```
syntheticbird: hinto: i would like you to inspect the io timeout PR (when its ready) and would like your opinion on whether you think it is worth applying to both RPC and P2P transports definitions.
```
```
syntheticbird: the status quo is that timeout are explicit at the moment, i would like them to be transparent and inside the transport primitive instead
```
```
syntheticbird: but boog argue this add complexity, so your input would be appreciated. if not it will probably kept as is
```
```
syntheticbird: and yeah sry i take time writing
```
```
hinto: will review when ready, we can discuss it in a later meeting too
```
```
syntheticbird: sgtm
```
```
boog900: anything else or we can end here?
```
```
syntheticbird: allg for me
```
```
boog900: ok we can end here, thanks everyone!
```
```
syntheticbird: thanks
```
```
hinto: thanks
```
```
boog900: !meeting 
```

# Action History
- Created by: moo900 | 2025-05-06T18:48:33+00:00
- Closed at: 2025-05-13T18:58:07+00:00
