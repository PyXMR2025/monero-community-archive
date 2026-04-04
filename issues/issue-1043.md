---
title: 'Cuprate Meeting #14 - Tuesday, 2024-07-30, UTC 18:00'
source_url: https://github.com/monero-project/meta/issues/1043
author: moo900
assignees: []
labels: []
created_at: '2024-07-23T19:17:50+00:00'
updated_at: '2024-07-30T19:05:35+00:00'
type: issue
status: closed
closed_at: '2024-07-30T19:05:34+00:00'
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

Previous meeting with logs: #1040

# Discussion History
## moo900 | 2024-07-30T19:05:33+00:00
## Meeting logs
```
yamabiiko: Hi
```
```
hinto: hello
```
```
hinto: will try to fix moo after this meeting...
```
```
boog900: 2) Updates: What is everyone working on?
```
```
boog900: > <@hinto:monero.social> will try to fix moo after this meeting...

weird that it happened 2 meetings in a row ....
```
```
fluorescent_beige: Me: still issue #209, didn't have as much time for it as I thought but getting somewhere now
```
```
boog900: Me: I have been working on the txpool and planning out what the incoming tx flow will look like 
```
```
yamabiiko: Me: took some time off ahead of CCS,  looking to pick up some issues / expanding tests as suggested
```
```
hinto: me: I've mostly finished the RPC interface library, still need to finish testing/documentation + split into PRs
```
```
hinto: also as per last meeting, I prepared a draft CCS: https://repo.getmonero.org/hinto/ccs-proposals/-/blob/hinto-3/hinto-3.md
```
```
boog900: 3. Project: What is next for Cuprate?
```
```
yamabiiko: > <@yamabiiko:unitoo.it> Me: took some time off ahead of CCS,  looking to pick up some issues / expanding tests as suggested

Are there any specific areas where the latter is welcomed ?
```
```
boog900: > <@hinto:monero.social> also as per last meeting, I prepared a draft CCS: https://repo.getmonero.org/hinto/ccs-proposals/-/blob/hinto-3/hinto-3.md

just gave this a quick look over and it looks good
```
```
boog900: hinto: are the "raw binary in string" types serialization handled in the interface PR or is that something you will work on for your next CCS?
```
```
hinto: I'm planning to finish that within the current CCS, although I think it may bleed into handlers since we may have to make custom parsers
```
```
boog900: > <@yamabiiko:unitoo.it> Are there any specific areas where the latter is welcomed ?

There is still DB work to do after my alt block PR, if that's something you would be interested in? 

For example: https://github.com/Cuprate/cuprate/blob/b44c6b045be5ece83a539f06be69f0f8622e3f51/storage/blockchain/src/service/read.rs#L210

here is the issue tracking alt block handling: https://github.com/Cuprate/cuprate/issues/194

Or maybe this issue about the P2P address book: https://github.com/Cuprate/cuprate/issues/178
```
```
hinto: honestly an easier option may be to _not_ support binary strings in Cuprate and create PRs that replaces them in `monerod`
```
```
hinto: otherwise the only other option I see is to create/maintain a JSON (de)serializer impl from scratch
```
```
boog900: We only need to write these types ... right?
```
```
boog900: they are only response types IIRC
```
```
boog900: but yes that may be easier we would just need wallets to update
```
```
boog900: for `monerod` these types would need custom ser/de to make sure this isn't a breaking change 
```
```
boog900: actually maybe not, you could just add another field and write out both fields for now up until the next HF then we can remove the old field 
```
```
hinto: OK, it depends if we're okay with binary strings staying in `monerod` or not
```
```
hinto: if we plan to push for changes in core then only supporting serialization will definitely be easier 
```
```
yamabiiko: > <@boog900:monero.social> There is still DB work to do after my alt block PR, if that's something you would be interested in? 
> For example: https://github.com/Cuprate/cuprate/blob/b44c6b045be5ece83a539f06be69f0f8622e3f51/storage/blockchain/src/service/read.rs#L210
> here is the issue tracking alt block handling: https://github.com/Cuprate/cuprate/issues/194
> Or maybe this issue about the P2P address book: https://github.com/Cuprate/cuprate/issues/178

This includes handling the reorgs aside from adding the alt blocks right ?
```
```
boog900: > <@hinto:monero.social> if we plan to push for changes in core then only supporting serialization will definitely be easier

yeah push for changes + do serialization would be the best compromise I think 
```
```
yamabiiko: > <@hinto:monero.social> if we plan to push for changes in core then only supporting serialization will definitely be easier 

I also vote for replacing the binary strings in `monerod`
```
```
boog900: > <@yamabiiko:unitoo.it> This includes handling the reorgs aside from adding the alt blocks right ?

We already have a function to pop a block, we will need a service request to pop multiple blocks though. For now I would recommend just adding the tables in the issue and fixing the current requests that panic due to the DB not supporting alt blocks
```
```
boog900: the rest can be done in another PR
```
```
boog900: and add a request to add an alt block 
```
```
boog900: I'll add more details to the issue after the meeting 
```
```
yamabiiko: Yeah I think I can work on it
```
```
boog900: 4. Any other business
```
```
boog900: anything else anyone wants to discuss? 
```
```
boog900: hinto: are you planning to make a PR to `-site` fixing the doc mismatches? 
```
```
hinto: yes, at least all the easy fixes - although I'm not sure about the more nuanced ones like unoptimal behavior: https://github.com/Cuprate/cuprate/issues/159
```
```
hinto: I have to re-confirm some of these "undocumented" fields as well as some of them are for internal storage rather than as user input
```
```
hinto: BTW there will definitely have to be a `differences` section in the architecture book for RPC
```
```
hinto: e.g. `monerod`'s JSON parser is quite lenient, `serde_json` is pretty much to the spec, e.g. `monerod` will allow invalid JSON in some cases, like missing brackets
```
```
boog900: IMO `unoptimal behavior` on rarely used endpoints probably isn't worth the effort to fix  
```
```
boog900: > <@hinto:monero.social> BTW there will definitely have to be a `differences` section in the architecture book for RPC

yeah that's fair, we were never going to match 1 to 1, as long as we are as much a drop in replacement as possible I am happy :)
```
```
boog900: > <@hinto:monero.social> e.g. `monerod`'s JSON parser is quite lenient, `serde_json` is pretty much to the spec, e.g. `monerod` will allow invalid JSON in some cases, like missing brackets

as long as monerod isn't producing these types :p
```
```
boog900: don't think I can handle another "binary string" type issue 
```
```
hinto: there's also `monerod`-specific RPC calls, e.g. `/set_log_categories`
```
```
hinto: but yes the main RPC calls should mostly be drop in replacements
```
```
boog900: anything else anyone wants to discuss? 
```
```
boog900: or we can end here 
```
```
boog900: ok let's end here, thanks everyone!
```
```
hinto: thanks
```
```
boog900: !meeting 
```

# Action History
- Created by: moo900 | 2024-07-23T19:17:50+00:00
- Closed at: 2024-07-30T19:05:34+00:00
