---
title: 'Cuprate Meeting #10 - Tuesday, 2024-07-02, UTC 18:00'
source_url: https://github.com/monero-project/meta/issues/1029
author: moo900
assignees: []
labels: []
created_at: '2024-06-25T19:25:23+00:00'
updated_at: '2024-07-02T18:58:53+00:00'
type: issue
status: closed
closed_at: '2024-07-02T18:58:52+00:00'
---

# Original Description
[Cuprate](https://github.com/Cuprate/cuprate) is an effort to create an alternative Monero node implementation.

Location: [Libera.chat, #cuprate](https://libera.chat/) | [Matrix](https://matrix.to/#/#cuprate:monero.social?via=matrix.org&via=monero.social)

> Note that there are currently communication issues with Matrix accounts created on the matrix.org server, consider using a different homeserver to see messages.

[Join the Monero Matrix server if you don't already have a Matrix account](https://www.getmonero.org/resources/user-guides/join-monero-matrix.html)

Time: 18:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html)

Moderator: @Boog900

Please comment on GitHub in advance of the meeting if you would like to propose a discussion topic.

Main discussion topics:

- Greetings
- Updates: What is everyone working on?
- Project: What is next for Cuprate?
- Workspace lints
- Any other business


Previous meeting with logs: #1028

# Discussion History
## moo900 | 2024-07-02T18:58:51+00:00
## Meeting logs
```
boog900: meeting time: https://github.com/monero-project/meta/issues/1029
```
```
boog900: 1. Greetings 
```
```
syntheticbird: Hi
```
```
yamabiiko: Hi
```
```
hinto: hello
```
```
boog900: 2. Updates: What is everyone working on?
```
```
boog900: Me: I have posted a new CCS proposal. I also finished the part 1 of my improvements to the P2P API + other misc things 
```
```
syntheticbird: Me: I'll be able to start working on Cuprate starting tomorrow. I'll take a day or two to get up to speed with recent commits (38 unread last time I checked)
```
```
yamabiiko: I started going through monerod's ZMQ code and boog's proposal
```
```
hinto: me: misc fixes / repo changes, benches/lints stuff, I think I'll be starting the mass RPC type porting today
```
```
boog900: 3. Project: What is next for Cuprate?
```
```
boog900: Does anyone have any thoughts on the ZMQ proposal?
```
```
syntheticbird: May I emphase on the dev report blog post? We're under 3 months until binary release, now is a good time to post on networks about our advancements
```
```
syntheticbird: oops sorry, lets first handle your question
```
```
rucknium: Where is the ZMQ proposal?
```
```
boog900: *alpha binary (just want that to be clear) 
```
```
hinto: Rucknium: https://github.com/Cuprate/cuprate/issues/199
```
```
boog900: > <@rucknium:monero.social> Where is the ZMQ proposal?

https://github.com/Cuprate/cuprate/issues/199
```
```
yamabiiko: So far the high level design seems good, wanted to ask if you can share the code example that you wrote 
```
```
rucknium: I don't have the full view of things, but isn't ZMQ a low priority for a MVP node?
```
```
rucknium: AFAIK only P2Pool uses ZMQ
```
```
rucknium: Anything else that could be higher priority?
```
```
hinto: agreed, I think there's other stuff that could/should be done first
```
```
yamabiiko: Tor support ?
```
```
hinto: e.g. cryptonight
```
```
rucknium: I am a heavy data user. By the way, I couldn't figure out how to use monerod's ZMQ. Maybe others can figure it out 🤷
```
```
syntheticbird: if i understand correctly no one is working on binary yet? we're waiting for rpc.
```
```
boog900: This was something I did want to discuss as well .... IMO Rust cryptonight rewrite is not higher priority 
```
```
yamabiiko: > <@hinto:monero.social> e.g. cryptonight

Why not RandomX?
```
```
hinto: just an example, cryptonight is relatively small and contained so I think it's a good entry point
```
```
boog900: I think the only thing I would put higher priority is bug fixes/ closing the open issues, mainly the address book issue and maybe the DB split 
```
```
boog900: every other section is being actively worked on ...
```
```
boog900: *that could be worked on
```
```
boog900: > <@syntheticbird:monero.social> if i understand correctly no one is working on binary yet? we're waiting for rpc.

for my next CCS I will be 
```
```
hinto: isn't the DB split done by now?
```
```
boog900: ah no not split .... DB hot-swapable backends 
```
```
boog900: my bad 
```
```
hinto: ah ok, relevant issue btw: https://github.com/Cuprate/cuprate/issues/209
```
```
boog900: address book: https://github.com/Cuprate/cuprate/issues/178
```
```
hinto: I've been testing around with some stuff and have lots to share but haven't written it down yet, will do so in that issue (..eventually)
```
```
yamabiiko: > <@yamabiiko:unitoo.it> Tor support ?

Thoughts? 
```
```
syntheticbird: > <@yamabiiko:unitoo.it> Thoughts? 

Tor Peer support ? or Arti integration ?
```
```
syntheticbird: I think the first but just to be sure
```
```
boog900: Also we have SyntheticBird coming in in the next few days and I have been in contacted with a couple other people from the hackathon that would like to do a bit more. 

```
```
yamabiiko: Was thinking about arti 
```
```
boog900: > <@yamabiiko:unitoo.it> Thoughts?

IMO right now the P2P code is not stable enough 
```
```
syntheticbird: > <@yamabiiko:unitoo.it> Was thinking about arti 

I think these are parts of the original feature list back when the project started. at least mid-term priority.
```
```
boog900: the abstractions are already in place though.
```
```
syntheticbird: > <@boog900:monero.social> IMO right now the P2P code is not stable enough 

ah well that settle then
```
```
yamabiiko: I'd be happy to work on cryptonight or other Rust crypto as well, but if we value ZMQ more I'll make a CCS for it
```
```
boog900: > <@boog900:monero.social> Also we have SyntheticBird coming in in the next few days and I have been in contacted with a couple other people from the hackathon that would like to do a bit more.

So I think having yamabiiko work on ZMQ might be best for us, for a CCS though I'm unsure 
```
```
hinto: re arti: this should be a discussion issue, my initial thoughts are that Cuprate has no need to pull in `arti`, it can just support a generic SOCKS proxy 
```
```
hinto: `cuprated` itself containing code that bootstraps and connects to the Tor network is very nice but also a maintenance tradeoff
```
```
syntheticbird: > <@hinto:monero.social> re arti: this should be a discussion issue, my initial thoughts are that Cuprate has no need to pull in `arti`, it can just support a generic SOCKS proxy 

Originally I wanted arti embedded into cuprate for people to not rely on system tor daemon. 
```
```
syntheticbird: but most people setting up monerod have Tor installed
```
```
syntheticbird: exceptions would be embedding cuprate into something like MoneroGUI
```
```
syntheticbird: > <@hinto:monero.social> `cuprated` itself containing code that bootstraps and connects to the Tor network is very nice but also a maintenance tradeoff

the maintenance is fair enough. Was it hard to integrate into Gupax?
```
```
syntheticbird: > <@hinto:monero.social> `cuprated` itself containing code that bootstraps and connects to the Tor network is very nice but also a maintenance tradeoff

* the maintenance argument is fair enough. Was it hard to integrate into Gupax?
```
```
boog900: I would like both :) 
```
```
boog900: Having arti would make it significantly easier to run a Tor node 
```
```
boog900: but I haven't actually looked into it much ...
```
```
hinto: not hard to integrate at all if you only need client capabilities, just noting it comes with tradeoffs
```
```
yamabiiko: > <@boog900:monero.social> So I think having yamabiiko work on ZMQ might be best for us, for a CCS though I'm unsure 

Unsure about willingness of the community to fund another Cuprate dev or something else?
```
```
syntheticbird: > <@yamabiiko:unitoo.it> Unsure about willingness of the community to fund another Cuprate dev or something else?

never say never
```
```
syntheticbird: > <@yamabiiko:unitoo.it> Unsure about willingness of the community to fund another Cuprate dev or something else?

* never say unsure
```
```
syntheticbird: > <@syntheticbird:monero.social> May I emphase on the dev report blog post? We're under 3 months until binary release, now is a good time to post on networks about our advancements

^ ?
```
```
syntheticbird: Draft PR here: https://github.com/Cuprate/cuprate-website/pull/2
```
```
boog900: > <@yamabiiko:unitoo.it> Unsure about willingness of the community to fund another Cuprate dev or something else?

Yeah and specifically for this task (ZMQ) at this stage. 
```
```
hinto: yamabiiko: IMO I'd like a little bit more planning and/or testing ZMQ before creating a CCS
```
```
hinto: not necessarily figuring everything out but just enough to get started and have a general direction forward
```
```
yamabiiko: Yes, I will go more in depth with the design / interface before that
```
```
hinto: SyntheticBird: are you asking for review? you can open the PR
```
```
hinto: > <@yamabiiko:unitoo.it> Yes, I will go more in depth with the design / interface before that

boog900: what do you think? when should yamabiiko open a CCS and for what? IMO if they can do the work for ZMQ I think it's okay
```
```
hinto: I admit it is quite the first task though, very undocumented as well
```
```
boog900: I do think it is the best thing to currently work on, baring smaller tasks. I think it should be for the ZMQ server and the `Service` that sends requests to clients, we can discuss exact details when the design proposal is expanded.  

It lacking docs maybe a good thing, it can be something to include in the CCS
```
```
hinto: sidenote: moo has bad code again https://github.com/Cuprate/moo/blob/0682e047430f79666b36268c7de86f55cdd76bc6/src/command/handle.rs#L338
```
```
hinto: this meeting must end before 19:00 or moo won't allow it to end :)
```
```
syntheticbird: > <@hinto:monero.social> this meeting must end before 19:00 or moo won't allow it to end :)

moo the dictator
```
```
boog900: ah week long meeting anyone?
```
```
boog900: (I'm guessing that's what would happen)
```
```
boog900: quickly then...
```
```
boog900: 4. Workspace lints
```
```
hinto: relevant tracking issue: https://github.com/Cuprate/cuprate/issues/207 
```
```
hinto: The gist is:

1. Integrate lints into workspace `Cargo.toml`
2. Slowly opt crates in, tuning lints as needed
```
```
hinto: https://github.com/Cuprate/cuprate/pull/133 already does 1, and I'd like it reviewed/merged so I can get started on 2 
```
```
boog900: I did spend sometime looking over some of the lints but didn't make a comment, I will comment by next meeting 
```
```
boog900:  * I did spend some time looking over some of the lints but didn't make a comment, I will comment by next meeting 
```
```
boog900: I do want to make sure that the lints aren't too annoying 
```
```
boog900: I really don't like the idea of (ab)using `allow` too much 
```
```
hinto: yup, that's the purpose of 2), I'll submit PRs with fixes and we can discuss which ones are too annoying and can be we removed from the workspace
```
```
hinto: I'm thinking each crate will have a separate PR dedicated to opting it in / fixing
```
```
hinto: worth noting: the really big lints that will affect everything are commented out for now
```
```
hinto: e.g. `missing_docs`
```
```
syntheticbird: 5 minutes before world's doom
```
```
syntheticbird: I'll try to look an lint tomorrow
```
```
boog900: I think it may be best to just do the whole workspace at a time, I wouldn't really want different lints for different crates 
```
```
yamabiiko: > <@boog900:monero.social> I think it may be best to just do the whole workspace at a time, I wouldn't really want different lints for different crates 

Seems inconvenient to me as well
```
```
hinto: there will only be 1 set of workspace lints all crates share, the multiple PRs are so there isn't a single 999,999 diff PR
```
```
hinto: although individual crates can still specify additional lints technically 
```
```
syntheticbird: boog please end moo before the hour so I can just copy past this part of the meeting
```
```
boog900: Ok I think I understand yeah that seems like a good idea
```
```
boog900: Alright I'll end moo
```
```
boog900: !meeting 
```

# Action History
- Created by: moo900 | 2024-06-25T19:25:23+00:00
- Closed at: 2024-07-02T18:58:52+00:00
