---
title: 'Cuprate Meeting #70 - Tuesday, 2025-08-26, UTC 18:00'
source_url: https://github.com/monero-project/meta/issues/1259
author: moo900
assignees: []
labels: []
created_at: '2025-08-25T14:28:53+00:00'
updated_at: '2025-08-26T19:15:18+00:00'
type: issue
status: closed
closed_at: '2025-08-26T19:15:18+00:00'
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

Previous meeting: #1253

# Discussion History
## moo900 | 2025-08-26T19:15:17+00:00
## Meeting logs
```
boog900: almost missed it again with the new vuln disclosure :D 
```
```
boog900: 1) greetings 
```
```
sgp_: Hello
```
```
kayabanerve: 👋
```
```
kayabanerve: boog900 @boog900:monero.social: Is that public, or are you solely commenting how you're distracted by it?
```
```
kayabanerve: Ah. It's posted 👀
```
```
boog900: https://github.com/monero-project/monero/issues/10059
```
```
boog900: yeah 
```
```
boog900: 2) updates 
```
```
syntheticbird: hello
```
```
kayabanerve: ... monero-oxide unaffected, hail monero-oxide?
```
```
syntheticbird: me: I've completed the user book Tor page, but I'm wondering about what to precise/include in the architecture book
```
```
boog900: I am surprised how this was in the code for so longg 
```
```
boog900: when it is a problem whenever a wallet is restored 
```
```
kayabanerve: RPC privacy is really tricky, which is why monero-oxide's solution of not implementing any RPC daemons is optimal.
```
```
kayabanerve: Sure, users have to, but that's _their_ problem
```
```
boog900: lol 
```
```
kayabanerve:  /s :p
```
```
sgp_: "want to actually use monero-oxide? Out of scope" :p
```
```
boog900: Me: fixed a deadlock in our tx-pool, continuing my work on removing the reorg lock & the address book 
```
```
kayabanerve: monero-serai -> monero-oxide, I've been working on upstreaming the FCMP++ code, which now includes migrating it to monero-oxide per decisions agreed on an hour or so ago.
```
```
boog900: 3) Project: What is next for Cuprate?
```
```
syntheticbird: So I would have a question regarding Architecture book
```
```
syntheticbird: There is already a layout and an i2p.md and tor.md page to be completed. I think these two should include tor and i2p specific logic. But there are no page for explaining the concept of transports and I wonder where this should be explained. As for the address book, it's undergoing some changes so i wonder if this is worth editing regarding the minor changes tor included? (launching addressbook with a self address)
```
```
boog900: I think the transports can go under p2p 
```
```
boog900: or if you think that page might be too crowded you can make another 
```
```
boog900: this can also always be moved so I wouldn't worry too much at the moment 
```
```
syntheticbird: sounds good
```
```
boog900: It would have been good to have hinto  here for this but I wanted to being up if weekly meetings are still a good idea  
```
```
boog900: I think we can probably move to less frequent meetings 
```
```
kayabanerve: I have a counter argument premised on if monero-oxide will be discussed at these meetingsm
```
```
kayabanerve: * I have a counter argument premised on if monero-oxide will be discussed at these meetings
```
```
kayabanerve: The only just published monero-oxide provides many things to discuss, but I don't see it justified to have its own meeting at this time. I'd personally like to parasite off the Cuprate meeting as we parasite off the Cuprate room
```
```
kayabanerve: The two together may continue to justify a weekly schedule
```
```
kayabanerve: At least, for now, with the monero-oxide migration and FCMP++ rush.
```
```
syntheticbird: I mean, governements do install cctv for sport events as a "temporary" measure and then left it there claiming it cost too much to remove them. Based on that I see no issue discussing monero-oxide during cuprate meeting.
```
```
syntheticbird: it's more a matter of quantity tbh
```
```
boog900: I am ok with weekly meetings if there is stuff to discuss 
```
```
boog900: and yes we can discuss monero-oxide here 
```
```
kayabanerve: I have no objection to less frequent meeting if there's less stuff to discuss.
```
```
kayabanerve: We just may be about to swing to having sufficient things to discuss :)
```
```
boog900: fair, we can stick with weekly meetings for now then 
```
```
syntheticbird: so mhm. are we gonna address the elephant in the room?
```
```
kayabanerve: I prefer waiting for the elephant's the agenda item
```
```
kayabanerve: Which may not have been defined beforehand in which case, I assume we'll add it after all other agenda items
```
```
boog900: lets go ahead with the elephant 
```
```
kayabanerve: ... or have we already done all agenda items and this is the unstructured time for the elephant?
```
```
kayabanerve: K, what is the elephant SyntheticBovinae: 
```
```
syntheticbird: we still have no new motto
```
```
syntheticbird: https://github.com/Cuprate/cuprate/issues/498
```
```
syntheticbird: almost two months passed
```
```
syntheticbird: more ideas please
```
```
boog900: as cuprates new dictator I will decide today 
```
```
syntheticbird: its so over
```
```
syntheticbird: "Cuprate: its so over"
```
```
boog900: I do like "A Rust Monero node" or "A Monero node in Rust" 
```
```
boog900: but what if we want to be more than a node 🤔
```
```
boog900: "A Rust Monero"? 
```
```
boog900: "A Monero in Rust"
```
```
syntheticbird: what about "A rusted and powerful monero node"
```
```
boog900: A rusted Monero?
```
```
syntheticbird: yeah literally an enote with rust on it
```
```
kayabanerve: An Oxidized Monero?
```
```
kayabanerve: wtf is an enote
```
```
syntheticbird: isn't it what seraphis output were called
```
```
syntheticbird: i never played monero so idk
```
```
kayabanerve: Oh, an output? Why didn't you say an output?
```
```
kayabanerve: Monero 2?
```
```
boog900: I like monero 2 :) 
```
```
syntheticbird: Cuprate: Monero the return
```
```
kayabanerve: Reads as 2.0, true as the second Monero
```
```
syntheticbird: yeah monero 2 is good
```
```
kayabanerve: Lmao
```
```
syntheticbird: another idea i had in mind is random_motto.txt
```
```
kayabanerve: Quick, someone do a Zig rewrite so we have Monero 3
```
```
syntheticbird: and a bot changes the motto randomly every 2 hours
```
```
boog900: Monero 2: Rust edition? 
```
```
kayabanerve: cowsay fortune SyntheticBovinae: 
```
```
kayabanerve: Monero 2: Electric Boogaloo!!!
```
```
sgp_: "A Rust Monero node built for security and reliability" (and whatever else)
```
```
kayabanerve: I'm sorry but that wins
```
```
syntheticbird: If boog wasn't lead dev i would have unironically put this until we find an answer
```
```
kayabanerve: No the point is they're lead dev!
```
```
kayabanerve: BOOGaloo
```
```
kayabanerve: > <@sgp_:monero.social> "A Rust Monero node built for security and reliability" (and whatever else)

"A secure, reliable Monero node" streamlines it a bit
```
```
boog900: As dictator I can't put myself in the motto 😭
```
```
kayabanerve: Or we can go for a bit of a pun with "A safe Monero node"
```
```
syntheticbird: dictator issue
```
```
kayabanerve: boog900 @boog900:monero.social: as dictator you CAN put yourself in the motto
```
```
kayabanerve: Would Kim Jong Un ask a glorious new building not be named after himself?
```
```
syntheticbird: I so much want to Monero 2: Eletric boogaloo for a few months
```
```
kayabanerve: Until Cuprate doesn't have boog as dictator IMO
```
```
syntheticbird: rebellion is in the air
```
```
kayabanerve: sgp_: has given the only suggestion here today which isn't a joke
```
```
kayabanerve: And jokes aren't bad, but we should course correct if we don't want a joke for a motto
```
```
kayabanerve: (And I did propose a couple derivatives from SGP)
```
```
syntheticbird: there aren't middle ground for me, it's either normal or shitposting
```
```
syntheticbird: and i'm good with both
```
```
syntheticbird: i also proposed one
```
```
rucknium: The time killswitches don't say "secure and reliable" to me, yet.
```
```
rucknium: Actions speak louder than words.
```
```
syntheticbird: that's cheating sir, we're in alpha
```
```
boog900: I always had a problem with our current motto tbf 
```
```
rucknium: Just say "A Rust Monero node" and earn the other adjectives later.
```
```
boog900: 
Cuprate, an upcoming experimental, modern & secure Monero node. Written in Rust 

```
```
syntheticbird: I know
```
```
boog900: `upcoming experimental, modern & secure`
```
```
syntheticbird: i love adjectives
```
```
syntheticbird: the more the better
```
```
syntheticbird: jk tho yeah its convoluted
```
```
sgp_: _A gorgeous, stunning Monero node_
```
```
kayabanerve: A modern, safety-focused Monero node written in Rust.
```
```
kayabanerve: sgp_: Cuprate stuns in its 1.0 release
```
```
syntheticbird: im fine with this, but i remember someone was against modern
```
```
syntheticbird: idr who or why tho
```
```
boog900: I think hinto? was against it as we can't be modern forever
```
```
boog900: one day a zig node will overtake us 
```
```
syntheticbird: it's the intent that count
```
```
syntheticbird: you can't fight against time
```
```
syntheticbird: and fleeing from your goal isn't a solution
```
```
syntheticbird: you must aim to be better, to improve
```
```
syntheticbird: thx for coming to my Ted talk
```
```
sbt: > <@boog900:monero.social> one day a zig node will overtake us 

Or a go node.
```
```
syntheticbird: avoid slurs in this channel please
```
```
syntheticbird: seriously tho, i can comprehend because modern can become irrelevant in the span of 4/5 years
```
```
kayabanerve: A 2025-ish, safety-focused Monero node written in Rust.
```
```
kayabanerve: A safety-oriented composable Monero node written in Rust.
```
```
kayabanerve: A safety-focused modular Monero node written in Rust.
```
```
kayabanerve: Let's set up a ranked choice vote of everyone's top two submissions and be done.
```
```
syntheticbird: that's for this type of proposition i want a random_motto.txt
```
```
syntheticbird: I want the world to see it
```
```
rucknium: I like "modular" if that's understandable to the target audience.
```
```
kayabanerve: Have "motto" be a link and it just links to the logs of this meeting with "pick your favorite" written at the bottom
```
```
sgp_: https://civs1.civs.us/
```
```
syntheticbird: I think there is an eth node that have that
```
```
kayabanerve: It tries to highlight how Cuprate is libraries, not just a node
```
```
syntheticbird: modular and contributor-friendly...
```
```
kayabanerve: sgp_: that is the practical way to resolve this discussion, yes.
```
```
kayabanerve: Friendly reminder we have more elephants in the room
```
```
syntheticbird: shit really?
```
```
kayabanerve: SyntheticBovinae: prove that with a track record, not by claiming to do so
```
```
kayabanerve: > <@rucknium:monero.social> Actions speak louder than words.

^
```
```
syntheticbird: can i at least have a "rusted" or "rusty"
```
```
kayabanerve: monero-oxide got permission to parasite here and has yet to draw any blood
```
```
syntheticbird: at the start
```
```
kayabanerve: oxidized :C
```
```
syntheticbird: corruption
```
```
kayabanerve: According to the C++ purists
```
```
boog900: "A modular Monero node written in Rust."
anyone disagree? 
```
```
boog900: I don't really want "node" but we can cross the hurdle if we ever become a wallet too 
```
```
syntheticbird: i'm not fan but i can see you really want something very pragmatic. That's a suitable middleground were we're both frustrated ig
```
```
kayabanerve: "safe, modular" and full ACK
```
```
kayabanerve: Else regular ACK
```
```
syntheticbird: * i'm not fan but i can see you really want something very pragmatic. That's a suitable middleground where we're both frustrated ig
```
```
syntheticbird: ACK?
```
```
kayabanerve: We have acceptance even if not preference boog900 @boog900:monero.social: 
```
```
kayabanerve: SyntheticBovinae: Really? Wow
```
```
kayabanerve: https://xkcd.com/1053/
```
```
syntheticbird: I really really strongly think we don't have the same definition
```
```
boog900: New motto chosen! 
```
```
rucknium: ACK is the worst slang.
```
```
kayabanerve: It's short for "acknowledge". Here it means acknowledged, sometimes styled as " ACKd".
```
```
syntheticbird: Thx god, that's not what I thought
```
```
boog900: kayabanerve: your turn 
```
```
kayabanerve: It's common lingo for software developers, along with "NACK" and "utACK". Iirc, it's derived from the TCP protocol?
```
```
syntheticbird: oh yeah you're right
```
```
kayabanerve: utACK would be untested acknowledge
```
```
kayabanerve: It's how you sign off on a PR you didn't test but _seems fine_
```
```
kayabanerve: monero-oxide exists
```
```
syntheticbird: interesting way to spell AI slop ending in linux kernel 6.12.43
```
```
kayabanerve: It uses the Cuprate channels, per its charter
```
```
kayabanerve: It's great, 10/10, we stan monero-oxide.
```
```
kayabanerve: The current efforts, IMO, should be a 1.0 of at least monero-oxide down *and* organizing the fcmp++ effort.
```
```
boog900: yes, what is needed now for 1.0? 
```
```
kayabanerve: Per a discussion earlier today in this channel, the FCMP++ codebase formerly hosted under kayabaNerve/fcmp-plus-plus will now entirely be located under monero-oxide/monero-oxide#fcmp++. We will use monero-oxide's issue tracker and PRs.
```
```
syntheticbird: afair FCMP++ was originally planned after RPC
```
```
kayabanerve: Well, we need a motto
```
```
kayabanerve:  /s :p
```
```
boog900: monero-rs 2? 
```
```
kayabanerve: I'd appreciate a cute logo like rustls or rustsec, other candidates for cute Rust logos welcome.
```
```
kayabanerve: But what we actually need is simply agreement the libraries are ready for 1.0, which also is tricky given we currently rely on non-1.0 dependencies (rand 0.6, ff/group 0.13).
```
```
kayabanerve: Is there anything we want to change in the API? Is there anything we want to add?
```
```
kayabanerve: Can I rename key_offsets please God let me rename key_offsets I beg you
```
```
kayabanerve: Also, boog900 @boog900:monero.social: has an open PR to avoid always performing point decompression.
```
```
boog900: my PR keeping points decompressed? 
```
```
boog900: * my PR keeping points compressed? 
```
```
syntheticbird: hive mind moment
```
```
kayabanerve: Also, I would like to emphasize our panic policy:

They shouldn't be reachable unless documented. This includes integer overflows when range checks are on.

I would love for volunteers to spend time looking for potential panics. I've already done so but panics are very tricky to get all of...
```
```
kayabanerve: I also review begged regarding some changes I made just before the migration, which I'll bring up again as I don't feel those have had sufficient scrutiny.
```
```
kayabanerve: https://github.com/serai-dex/serai/pull/667/files

Please ignore the changes irrelevant to the monero libs :/ I gunked up that PR a bit.
```
```
kayabanerve: My other topic is simply regarding what functionality we want monero-oxide to have. Do we want to migrate anything from Cuprate?
```
```
kayabanerve: Should monero-rpc use Cuprate's RPC types/epee lib?
```
```
kayabanerve: monero-rpc is ABOVE monero-oxide and not included in the currently posited 1.0 discussion
```
```
boog900: probably not the RPC types yet, but our epee lib should be fine to use 
```
```
syntheticbird: One issue I have with separating RPC types from cuprate into monero-oxide is that we will feel obligated to follow the current monerod spec, without any option to add new endpoints solely usable for cuprate users
```
```
kayabanerve: Also, monero-wallet was included in the migration to monero-oxide. I historically wrote/had written various utilities, now collected under https://github.com/kayabaNerve/monero-wallet-util. Do we want to include these? Should I transfer ownership of monero-wallet-util to monero-oxide, keeping the repositories separate?
```
```
kayabanerve: SyntheticBovinae:

monero-rpc-types
cuprate-rpc-types

monero-cuprate-rpc-types
pub use monero_rpc_types::*;
pub use cuprate_rpc_types::*;
```
```
kayabanerve: Ugh, my new lines got destroyed :(
```
```
kayabanerve: TL;DR two crates and a trenchcoat most users use.
```
```
syntheticbird: yeah but i can see the "we are not going to make a proxy crates for two new endpoints" argument
```
```
kayabanerve: We have *several* organizational questions moving forward. This is solely me providing a list of the ones I can think of.
```
```
boog900: Yeah I think transferring to monero-oxide would be a good idea 
```
```
boog900: I can even lift the epee crate out of cuprate if that is something wanted 
```
```
kayabanerve: We can discuss them now, but practically, it may be best to give each their own GitHub issue?
```
```
kayabanerve: - Logo
- monero-oxide 1.0
- monero-rpc using Cuprate's RPC types
- epee lib
- monero-wallet-util
- FCMP++ future
```
```
kayabanerve: I believe we've already discussed the FCMP++ future before the meeting to a sufficient degree. I'll open the PR for generalized-bulletproofs shortly
```
```
kayabanerve: Also, cc binarybaron: to read through this, as they've been using monero-oxide and opening issues :)
```
```
kayabanerve: Also, boog900 @boog900:monero.social: https://github.com/kayabaNerve/monero-wallet-util/issues/5#issuecomment-3221516949
```
```
syntheticbird: I'll have to go, guys and gales. thx for this meeting.
```
```
kayabanerve: I'm fine dumping it @ monero-oxide but I can't flesh it out as much I would love to see it fleshed out with various amazing libs for the wallet/project ecosystem
```
```
kayabanerve: I'm concerned it would be dumping a ghost town at monero-oxide and walking away
```
```
kayabanerve: But maybe the monero-oxide org would be the place for it to be seen and participated with?
```
```
kayabanerve: Maybe community members like binarybaron will step up?
```
```
kayabanerve: Also detherminal @detherminal:monero.social: who once made a PR
```
```
kayabanerve: I'll make issue in the monero-oxide repo. Thanks for your time SyntheticBovinae: :)
```
```
boog900: I do think it would be suited for monero-oxide, I would be fine moving it across
```
```
kayabanerve: I'm still here to respond to any discussions we want to have now but I do think it's reasonable to consider the meeting ended and this unstructured general conversation, unless boog900 @boog900:monero.social: (dictator and chairperson) has something else
```
```
boog900: you can always add a disclaimer in the README or something  
```
```
boog900: yeah if that's all we can end here 
```
```
boog900: thanks everyone!
```
```
boog900: !meeting 
```

# Action History
- Created by: moo900 | 2025-08-25T14:28:53+00:00
- Closed at: 2025-08-26T19:15:18+00:00
