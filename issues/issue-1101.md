---
title: 'Cuprate Meeting #28 - Tuesday, 2024-11-05, UTC 18:00'
source_url: https://github.com/monero-project/meta/issues/1101
author: moo900
assignees: []
labels: []
created_at: '2024-10-29T18:47:37+00:00'
updated_at: '2024-11-05T19:30:25+00:00'
type: issue
status: closed
closed_at: '2024-11-05T19:30:25+00:00'
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
- [RPC type optimization](https://github.com/Cuprate/cuprate/pull/147#discussion_r1654912900)
- RPC testing granularity
- [Port numbers for `cuprated`](https://github.com/Cuprate/cuprate/issues/269)

- Any other business

Previous meeting with logs: #1097

# Discussion History
## moo900 | 2024-11-05T19:30:24+00:00
## Meeting logs
```
boog900: meeting time: https://github.com/monero-project/meta/issues/1101
```
```
boog900: 1) Greetings
```
```
syntheticbird: Hello
```
```
boog900: 2) updates
```
```
syntheticbird: me: P2P bucket have been merged. I'll be working on the Address Book improvement issue this week.
```
```
boog900: Me: I worked on changing our connected peers collection so we can access all connected peers data.
```
```
boog900: 3) Project: What is next for Cuprate?

```
```
boog900: hinto: ping
```
```
syntheticbird: Yeah I think we can wait for Hinto a little longer, we're only 8.
```
```
boog900: anything anyone wants to discuss while we wait?
```
```
hinto: hello
```
```
hinto: me: I posted an update on my current CCS: https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/484#note_27047
```
```
boog900: - [RPC type optimization](https://github.com/Cuprate/cuprate/pull/147#discussion_r1654912900)
```
```
syntheticbird: Is there no way to change the default stack size for all newly generated threads?
```
```
syntheticbird: I know builder can do so
```
```
syntheticbird: but maybe tokio can't
```
```
hinto: I wanted to discuss how far to take type optimizations within our crates considering tradeoffs on wider usability / pulling in less dependencies, the `rpc-types` crate is a good example but it could apply to all crates
```
```
hinto: for example, in many of `rpc-types`'s types, we could swap out fixed sized `String`s for some byte arrays and `Vec<u8>` with `bytes::Bytes`
```
```
hinto: my initial instinct on this is that instead of hyper optimizing stuff we take some middle approach so (eventual) users have more options - in the above we would do simple type swaps like that but behind `#[cfg(feature = "some_feature")]`
```
```
hinto: we could lean further toward optimization at the cost of being closer tied to Cuprate's needs or the reverse
```
```
syntheticbird: I think we can discuss that on a crate by crate basis. We know for instance that `rpc-type` is really something the community might need and feature gate seems like a reasonable approach. But I don't think it should be a basis for all other crates.
```
```
hinto: an example where I think this hyper-optimization is already done is in the `json-rpc` crate, that crate is very tied to Cuprate because of: https://github.com/Cuprate/cuprate/pull/146#issuecomment-2145734838
```
```
hinto: btw I've been spending some time the above because I really did not like the usability tradeoff both internally and to users - (un)fortunately from what I can tell the performance difference is actually pretty drastic compared to doing it the normal way
```
```
hinto: i.e the full `request` -> `axum handler` -> `deserialize json-rpc request` pipeline is a lot faster with boog900's method
```
```
boog900: IMO it should depend on how annoying the optimization is to work with, a array based string vs heap should be pretty easy right?
```
```
boog900: and also how much it gains us
```
```
boog900: I wouldn't really want to have feature flags for different field types
```
```
syntheticbird: > <@hinto:monero.social> i.e the full `request` -> `axum handler` -> `deserialize json-rpc request` pipeline is a lot faster with boog900's method

Sorry what's boog900 method exactly?
```
```
boog900: For something like `ByteArrayVec` which is annoying to work with I can see the argument of just doing `Vec<[u8; 32]>` but the answer to that is improving the `ByteArrayVec` API
```
```
hinto: yes I was going to mention that: https://github.com/Cuprate/cuprate/pull/147
```
```
hinto: err I mean: https://github.com/Cuprate/cuprate/pull/227
```
```
hinto: the tradeoff of making types as generic as possible vs optimization / tying to Cuprate's uses - is currently slightly pulled towards the latter
```
```
syntheticbird: If we had to make a choice I would still tend towards the latter.
```
```
hinto: SyntheticBird: summary is here: https://github.com/Cuprate/cuprate/pull/146#issuecomment-2148576495
```
```
syntheticbird: Oh yes i remember now. thx
```
```
boog900: > Vec<u8> with bytes::Bytes

Does this improve performance for JSON or just epee? 
```
```
syntheticbird: re: optimization/generic. My stance is that Cuprate is a node implementation, not the *most general purpose set of libraries for Monero*. No offense to the community but I don't want to sacrifice a two digits performance improvements in some benchmark for potentially all monero node operator just to avoid someone to fork the particular crate and adapt it for its need.
```
```
boog900: At the same time people using our crates for different use cases are some of the bests tests of them possible 
```
```
boog900: so I wouldn't want to discourage that 
```
```
boog900: My opinion is that for stuff like array backed strings which are easy to work with using them is fine for the more complex optimization it depends on the crate and how invasive it actually is  
```
```
boog900:  * My opinion is that for stuff like array backed strings which are easy to work with using them is fine, for the more complex optimization it depends on the crate and how invasive it actually is  
```
```
syntheticbird: fair enough
```
```
hinto: > <@boog900:monero.social> > Vec<u8> with bytes::Bytes
> 
> Does this improve performance for JSON or just epee?

presumably both - although I think the zero-copy would be the reason that type would be chosen
```
```
hinto: just a throwaway example though
```
```
hinto: > <@syntheticbird:monero.social> re: optimization/generic. My stance is that Cuprate is a node implementation, not the *most general purpose set of libraries for Monero*. No offense to the community but I don't want to sacrifice a two digits performance improvements in some benchmark for potentially all monero node operator just to avoid someone to fork the particular crate and adapt it for its need.

for transparency: I have a writeup that I'm planning to post after my CCS that includes this type of stuff, we'll have an opportunity to have deeper/wider discussion then
```
```
hinto: > <@boog900:monero.social> At the same time people using our crates for different use cases are some of the bests tests of them possible

this is a good transition into the next topic I wanted to talk about
```
```
boog900: - RPC testing granularity
```
```
hinto: I think it's safe to say we will inevitably need a `tests/` similar to https://github.com/monero-project/monero/tree/master/tests
```
```
hinto: included in this directory, we would also inevitably need tests that asserts a bunch of behavior between `monerod <-> cuprated`
```
```
hinto: one of those tests will inevitably be RPC compatibility - testing many (all?) layers of the system at once 
```
```
hinto: under this assumption, I've been thinking unit-tests testing simple type compat and (de)serialization is maybe a bad use of time in the long-term
```
```
hinto: eventually we'll create some framework that not only makes sure stuff like that is tested, but that the entire `request` -> `response` pipeline works - the framework would cover more at once and presumably scale better unlike the manual JSON tests in `rpc-types`
```
```
hinto: this concept (less fine-grained tests, more big testing frameworks) could also be applied to other crates too but RPC is a good example
```
```
hinto: this is also a very good excuse for me to delay writing epee tests even further :)
```
```
hinto: there's a lot of epee stuff I need to (and will) fix but the thoughts above are why I haven't yet started writing a bunch of epee RPC tests
```
```
syntheticbird: I'm seduced by the proposal but I struggle to understand concretely what would be a testing framework?
```
```
boog900: Yeah that does make sense, in the P2P crates I don't have static tests that check on fixed blobs of data for each type, I have tests for handshakes and other message flows.

I do think having these tests is a good idea but yeah I don't think they are necessary right now and if we can cover them in a more meta test that would also be good.
```
```
boog900: I do also have plans for some tools to generate a fake blockchain for testing, specifically using `proptest`'s state machine testing 
```
```
hinto: > <@syntheticbird:monero.social> I'm seduced by the proposal but I struggle to understand concretely what would be a testing framework?

just another program we write that somehow gets `monerod` + `cuprated` in a testable state, then a long list of tests that do stuff
```
```
hinto: not sure how exactly this will happen for stateful things like blockchain/rpc but... we'll figure it out... because we have to
```
```
syntheticbird: Ok make sense
```
```
hinto: ok next topic, fun one is left for last
```
```
boog900: - [Port numbers for cuprated](https://github.com/Cuprate/cuprate/issues/269)
```
```
hinto: first big question: to copy `monerod` or to not copy `monerod`?
```
```
hinto: answer (probably): no because then you cannot run both `monerod` and `cuprated` on the same machine...?
```
```
syntheticbird: I don't see any reason to not copy monerod.
```
```
hinto: oh boy
```
```
syntheticbird: > <@hinto:monero.social> answer (probably): no because then you cannot run both `monerod` and `cuprated` on the same machine...?

i mean. he can change one ports?
```
```
syntheticbird: > <@hinto:monero.social> answer (probably): no because then you cannot run both `monerod` and `cuprated` on the same machine...?

 * i mean. he can change one's port?
```
```
syntheticbird: > <@hinto:monero.social> oh boy

did I missed something?
```
```
boog900: I do also think we should copy `monerod`, although running both at the same time is a problem, you could just change the ports of one of them
```
```
syntheticbird: I think people that are most likely going to run both monerod and cuprate are knowledgeable enough to change the ports.
```
```
syntheticbird: Also I let you imagine the frustration of sys admins when they are going to test replacing monerod by cuprate and realize 2 hours later they needed to change their firewall
```
```
hinto: IIRC zcashd/zebra both use the same port, tor/arti do not (9050/9150)
```
```
syntheticbird: > <@hinto:monero.social> IIRC zcashd/zebra both use the same port, tor/arti do not (9050/9150)

weird. I've already seen tor daemon using 9150 before arti was a thing.
```
```
hinto: I haven't looked too deep into this, just bringing it up since we have the choice
```
```
hinto: it belongs in the bucket of fun/angry things to discuss when internal stuff is close to being ready
```
```
syntheticbird: well I stay on my stance. no need to change it
```
```
boog900: anything else anyone wants to discuss?
```
```
syntheticbird: can we have a profile picture for moo?
```
```
syntheticbird: jk
```
```
syntheticbird: i think its the end
```
```
boog900: Yeah, thanks everyone!
```
```
syntheticbird: thx
```

# Action History
- Created by: moo900 | 2024-10-29T18:47:37+00:00
- Closed at: 2024-11-05T19:30:25+00:00
