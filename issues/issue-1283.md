---
title: 'Cuprate Meeting #73 - Tuesday, 2025-10-28, UTC 18:00'
source_url: https://github.com/monero-project/meta/issues/1283
author: moo900
assignees: []
labels: []
created_at: '2025-10-21T19:13:12+00:00'
updated_at: '2025-10-28T18:51:15+00:00'
type: issue
status: closed
closed_at: '2025-10-28T18:51:15+00:00'
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

Previous meeting: #1280

# Discussion History
## moo900 | 2025-10-28T18:51:14+00:00
## Meeting logs
```
boog900: 1) greetings 
```
```
hinto: hello
```
```
kayabanerve: 👋
```
```
boog900: 2) updates 
```
```
kayabanerve: Almost done with the new ed25519 code for oxide.
```
```
kayabanerve: I also sketched a const fn hash-to-point and noted a lot more algorithms can technically be batched.
```
```
hinto: me: working on PoWER (for Cuprate too); killswitch removal PR: https://github.com/Cuprate/cuprate/pull/559
```
```
boog900: Me: finished up the database changes, I went less extreme than I originally planned. I have moved our tx/block blobs into a tape and saved the index they are stored at in the info tables. 

This has shaved around 90 GBs off of our DB 
```
```
boog900: meaning our DB is now around 200 GBs 
```
```
hinto: wow, not sure if I should be amazed or embarrassed 
```
```
boog900: 3) Project: What is next for Cuprate?
```
```
boog900: tbf we are now significantly smaller than monerod
```
```
boog900: the old code is still in use for every table apart from the blobs and ringCT outputs 
```
```
boog900: the blobs tape is actually multiple tapes for each pruning stripe 
```
```
boog900: so hopefully it shouldn't be too hard to add pruning support
```
```
hinto: is this a PR just for the DB or was this related to RPC changes, or something else?
```
```
hinto: are we smaller than `monerod` when all stores are combined?
```
```
boog900: Well I made the tape for FCMPs++ as I wanted to separate it from the main DB anyway, then I changed the ringCT outputs to use it. Then while I was working on RPC I didn't like how inefficient it was for us to get a pruned blob from the DB so I changed the blob tables 
```
```
boog900: it will be its own PR 
```
```
boog900: 
4.0K	./lock.mdb
21G	./data.mdb
11G	./rct_outputs.tape
18G	./prunable/stripe2.tape
17G	./prunable/stripe1.tape
18G	./prunable/stripe6.tape
18G	./prunable/stripe3.tape
18G	./prunable/stripe7.tape
18G	./prunable/stripe5.tape
18G	./prunable/stripe8.tape
18G	./prunable/stripe4.tape
139G	./prunable
27G	./pruned.tape
196G	.


```
```
boog900: thats the whole DB
```
```
boog900: add on an few GBs as I didn't store some indexes we need there but I expect around 200
```
```
boog900: well I know around 200
```
```
hinto: wow, very nice
```
```
boog900: Getting outputs is also a lot faster when you need a lot 
```
```
boog900: when you don't need that many it is pretty mush the same 
```
```
boog900: * when you don't need that many it is pretty much the same 
```
```
boog900: hinto: anything you want to discuss on PoWER/ZMQ 
```
```
boog900: or anything really
```
```
hinto: I am thinking of removing macOS x64 support for the next release: https://github.com/Cuprate/cuprate/issues/552
```
```
hinto: CI will still work until December although I think it can be deprecated now
```
```
boog900: yeah sounds good to me
```
```
hinto: unrelated, is this waiting on other changes?: https://github.com/Cuprate/cuprate/pull/499
```
```
boog900: I remember not being sure about something ...
```
```
boog900: oh yeah the read interface doesn't resize automatically and we couldn't think of a good way to do it right? 
```
```
boog900: for now I don't think we need to worry about trying to fix that we can come back to it
```
```
hinto: hmm, I don't remember details either although in that case I think the read interface (in that PR) can just call `resize_map(None, true)`: https://github.com/Cuprate/cuprate/pull/499/files#diff-1bc510b91fbb59b2a56915f7e5976c2d36a1b5ad18dd56443063196bbcf2ce2dR225-R234
```
```
boog900: it needs to restart the tx tho 
```
```
boog900: if you think it can be done, you can give it a go
```
```
hinto: How would you handle this if we implement https://github.com/Cuprate/cuprate/issues/539?
```
```
boog900: tbf it would probably be easier to do it then as the resize error only happens when a tx starts right?
```
```
hinto: yeah, I guess the read interface will re-attempt TXs a few times upon this error before returning to caller?
```
```
syntheticbird: hi (sorry for being late i lost internet just before the meeting started)
```
```
hinto: actually, is this error possible for reads if other processes resizing is defined as a panic?
```
```
boog900: it is if another crate uses the read interface 
```
```
boog900: like a block explorer 
```
```
hinto: our write interface should be leaving the DB in a valid state, so I think reads only face this if other processes resize the DB
```
```
boog900: If the read interface is used by a block explorer Cuprate could resize the DB
```
```
boog900: the block explorer is allowed to use our read interface while cuprated is running 
```
```
boog900: so this is possible 
```
```
hinto: ah my bad I forget these aren't tied to TX commits
```
```
hinto: boog900: did you have a specific impl in mind for 539?
```
```
hinto: "Instead you should first need to call a function to start a DB tx" -> would this be a public fn like `cuprate_database::open_tx_rw() -> TxRwHandle`?
```
```
hinto: where `TxRwHandle` is the `Service` for the current request/responses?
```
```
boog900: yeah pretty much 
```
```
boog900: then the handle holds the database txs and locks 
```
```
boog900: anything else anyone wants to discuss today?
```
```
kayabanerve: There's some open PRs to oxide needing review 👀
```
```
boog900: will do :)
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
```
boog900: !meeting 
```

# Action History
- Created by: moo900 | 2025-10-21T19:13:12+00:00
- Closed at: 2025-10-28T18:51:15+00:00
