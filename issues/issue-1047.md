---
title: 'Cuprate Meeting #15 - Tuesday, 2024-08-06, UTC 18:00'
source_url: https://github.com/monero-project/meta/issues/1047
author: moo900
assignees: []
labels: []
created_at: '2024-07-30T19:05:34+00:00'
updated_at: '2024-08-06T19:06:33+00:00'
type: issue
status: closed
closed_at: '2024-08-06T19:06:33+00:00'
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

Previous meeting with logs: #1043

# Discussion History
## moo900 | 2024-08-06T19:06:32+00:00
## Meeting logs
```
hinto: hello
```
```
boog900: 2) updates 
```
```
boog900: Me: I have still been working on the tx-pool, I also plan to make some changes to our D++ crate to make the pool in there more efficient 
```
```
boog900: today I started to make some issues on future tasks, still a WIP though 
```
```
fluorescent_beige: Me: wrapping up issue #209
```
```
hinto: me: finishing up the RPC section in the architecture book, upstreaming some doc fixes to `monero-site`, recently finished the interface crate - we now have a barebones "working" RPC server :) 
```
```
yamabiiko: Me: unfortunately some unexpected life event is affecting my wellbeing and I now feel unable to guarantee the time and focus commitments in the CCS needed to deliver high quality work. So I decided that it's best to close it

```
```
boog900: ah no :( hope all is ok for you 
```
```
boog900: 3) Project: What is next for Cuprate?
```
```
jbabb: I'm new this week, my immediate goal is going to be to emulate my work wrapping monero-serai for Dart here https://github.com/cypherstack/libxmr for a Cuprate-backed cross-platform Flutter node

that libxmr example is a poor example in terms of wallet API and I want to focus on upgrading it to expose a standard/unified API, or at least the same API of the lower-level crates it wraps

I'm also trying to get up to speed following the instructions and advice of regulars here that've helpfully responded to and directed me in various ways up above in the chat.
```
```
hinto: yamabiiko: this is unfortunate... I hope things improve such that you can open another CCS eventually
```
```
jbabb: (realizing of course that monero-serai is for wallets and cuprate is for nodes; I'll just be making a proof of concept for myself showing that Rust code will run fine on many platforms via Flutter/Dart)
```
```
jbabb: so not contributing directly really, just consuming and using work here so far, but I hope it will get me more up to speed so I can be more useful to others
```
```
boog900: Sounds interesting ... currently we don't have a working binary just a bunch of components which could be wrapped and used separately. You will need to come back in a couple months for a working binary :)
```
```
jbabb: for monero-serai I imported certain crates and made wrapper functions which returned more-easily-passed primitives, but in the past year I've learned better practices like passing types directly from rust over ffi instead of converting everything to strings or lists of bytes... no bin needed, should be able to use raw rust code, but need to wade in to really know.
```
```
jbabb: basically if what's here isn't easily `rust bindgen`able I just make a simpler file that is, `rust bindgen` it, and `dart ffigen` that, not rocket science, still fun to do and cool to see rust running on a phone or windows or wherever without me ever leaving my comfy linux dev env
```
```
jbabb: anyways sorry to spam.  I'll try to shut up until I have something pushed
```
```
boog900: FWIW we are also missing some major components like the txpool for the node so a wrapped node in dart is not currently possible without a lot of dev work to build them in dart 

Not trying to discourage you, just warning 
```
```
boog900: Anything else anyone wants to discuss here? 
```
```
boog900: 4) Any other business
```
```
hinto: boog900: nit on your tracking issues, the titles usually follow `Tracking Issue for ...` https://github.com/rust-lang/rust/labels/C-tracking-issue
```
```
boog900: I'll change them 
```
```
hinto: re: binary strings (https://github.com/monero-project/monero/issues/9422), I'm planning to push/implement changes for `monerod` hopefully by the end of my next CCS, if the proposal doesn't move forward, I believe Cuprate would fall back to writing a custom serialize function and not supporting deserialization
```
```
hinto: i.e. we would generate these binary strings the same as `monerod` such that `wallet2` works, although we would have no code that can actually parse it...
```
```
boog900: yeah that sounds good
```
```
hinto: another thing I've been thinking about is how these public binary RPC calls exist without any specification for what the binary is, practically meaning the only users are  Monero itself and projects that use its code
```
```
hinto: I'd like to write a detailed specification for epee one day but... this is probably a discussion for some time far in the future
```
```
boog900: the whole of epee? or just epee binary 
```
```
boog900: we have this:https://github.com/monero-project/monero/blob/master/docs/PORTABLE_STORAGE.md
```
```
hinto: ah I guess not then, although other binary forms exist in RPC output
```
```
boog900: is there anything else anyone wants to discuss? 
```
```
boog900: ok lets end here
```
```
boog900: thanks everyone!
```
```
hinto: thanks
```
```
boog900: !meeting 
```

# Action History
- Created by: moo900 | 2024-07-30T19:05:34+00:00
- Closed at: 2024-08-06T19:06:33+00:00
