---
title: 'Cuprate Meeting #72 - Tuesday, 2025-10-21, UTC 18:00'
source_url: https://github.com/monero-project/meta/issues/1280
author: moo900
assignees: []
labels: []
created_at: '2025-10-14T15:03:39+00:00'
updated_at: '2025-10-21T19:13:13+00:00'
type: issue
status: closed
closed_at: '2025-10-21T19:13:13+00:00'
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

Previous meeting: #1260

# Discussion History
## moo900 | 2025-10-21T19:13:12+00:00
## Meeting logs
```
boog900: 1) greetings 
```
```
kayabanerve: 👋 again, everyone
```
```
hinto: hello
```
```
boog900: 2) updates
```
```
boog900: first meeting in a ~month, welcome back everyone! 
```
```
hinto: me: planning a ZMQ implementation
```
```
boog900: Me: I have been working on RPC, managed to get a wallet to sync with a Cuprate node. I have also been looking at FCMP and what changes we will need to make, which has lead me into quite a bit DB change 
```
```
boog900: quite a big*
```
```
kayabanerve: monero-oxide has had misc improvements, bug fixes, and has an open PR to rewrite its RPC client for correctness, while the first FCMP++ lib PR was signed off on pending a comment on the academic side. It also has a PR for its own non-allocating epee deserializer which doesn't require the `bytes` library.
```
```
boog900: 3) Project: What is next for Cuprate?
```
```
kayabanerve: FCMP++, the obvious comment?
```
```
kayabanerve: I'd be curious to hear more from hinto @hinto:monero.social: on zmq :)
```
```
boog900: @hinto I have made a new DB in this PR: https://github.com/Cuprate/cuprate/pull/558

Its a `LinearTape`, based on some discussion I had a while ago with kayaba. It stores values contiguously and allows indexing for them. I wrote this for the FCMP tree but have decided to move all fixed sized, index tables over to it.  
```
```
boog900: It should be faster and smaller than storing the values in LMDB 
```
```
boog900: its not ready yet, just giving you a heads up. We will still have the "old" DB for the values that can't be put in a tape 
```
```
kayabanerve: LMDB may also make sense for metadata if it provides some specific consistency guarantees not manually implemented for the tapes at this time.
```
```
hinto: Lots of the planning for ZMQ was already done by boog900 here: https://github.com/Cuprate/cuprate/issues/199

and dimalinux has already defined all(?) the types, I'm currently writing a wider proposal that includes misc impl details
```
```
hinto: I did not look too in depth although are there any concerns with ACID?
```
```
boog900: it is ACID as long as you pop and push in different txs 
```
```
boog900: so a reorg needs to be done in 2 steps 
```
```
boog900: it has 2 different writer types because of this 
```
```
hinto: Multiple data stores will be trouble if we need to synchronize a single snapshot of data
```
```
boog900: one to append one to push 
```
```
hinto: I'm talking about between the current main DB + this store
```
```
hinto: (unless this doesn't matter)
```
```
boog900: I have only moved RCT outputs over at the moment, on startup we compare the amount of outputs in the tape with the amount in the DB and pop/push outputs accordingly 
```
```
boog900: the number of rct ouputs is already stored in the block info table 
```
```
boog900: for the other tables we can do something similar 
```
```
boog900: using the amount of block blobs as the source of truth for the amount of blocks in the chain 
```
```
boog900: and rebuilding/popping from tables accordingly 
```
```
boog900: we also don't keep a global output index as it isn't used, but FCMP just gave it a use :(
```
```
boog900: so we need to store some extra data now :(
```
```
hinto: how has the wallet syncing been? I would say that this will be one of the more impactful updates
```
```
boog900: it was pretty slow ngl 
```
```
hinto: what was the bottleneck?
```
```
boog900: we don't keep pruned blobs separate like monerod so we either provide the full blob or compute the pruned blob on the fly 
```
```
boog900: whereas monerod does separate them 
```
```
boog900: I didn't do that much testing ngl
```
```
boog900: as soon as the wallet was syncing I moved onto the DB
```
```
boog900: I did do a full sync from genesis tho
```
```
boog900: anything you want to discuss on FCMP kayabanerve 
```
```
kayabanerve: Eh, I can talk more on oxide. All that's relevant re: FCMP++ right now is how you signed off on the GBPs PR, how it's just pending the resolution of the topic I posted in MRL, and how after that we'll likely target merging in helioselene?
```
```
kayabanerve: Maybe more of the arithmetic circuit code...
```
```
kayabanerve: Shall I also comment on oxide a bit more at this time?
```
```
kayabanerve: I think the most notable upcoming change is removing `curve25519_dalek` from the public APIs.
```
```
boog900: If you have something you partially want to discuss, sure
```
```
kayabanerve: I think just `monero-ed25519`. We already have `UnreducedScalar` for the cases Monero has a non-standard reduction, `CompressedPoint` for how `curve25519-dalek` has non-canonical decompression, and our own hash-to-point. The idea is to introduce `Scalar`, `Point`, not just to complete the set, yet also to remove `curve25519-dalek` from our API commitment. This is partially for flexibility, as we already don't use `curve25519-dalek` alone yet also `dalek-ff-group` (my own code which additionally exposes `FieldElement`, for which I have a PR to `curve25519-dalek` for: https://github.com/dalek-cryptography/curve25519-dalek/pull/816), but also because we're somewhat blocked on how the entire cryptography ecosystem is undergoing a new versioning after `rand 0.9`'s release.
```
```
boog900: * If you have something you particularly want to discuss, sure
```
```
kayabanerve: Owning the API lets us consolidate our existing bespoke code, removes the commitment to `curve25519-dalek 4.0` specifically (letting us upgrade to `curve25519-dalek 5.0` arbitrarily), and potentially even allows replacing `curve25519-dalek` if we ever wanted (`fiat-crypto`?).
```
```
kayabanerve: We can probably discuss a bit where we consider my epee PR in relation to Cuprate's existing library as well, but that's it from me, I think.
```
```
boog900: I do think this is a good idea FWIW 
```
```
boog900: maybe even a KeyImage type for ignoring the sign bit during comparisons? 
```
```
kayabanerve: thank you for publicly committing after privately agreeing with me we should, and now being unable to disavow my efforts
```
```
kayabanerve: :P
```
```
kayabanerve: ... you didn't hear?
```
```
kayabanerve: That change was reverted months ago, I'm not even joking
```
```
boog900: wait really 
```
```
kayabanerve: ... I hope you didn't already write the migration for that?
```
```
boog900: nah I didn't lol
```
```
boog900: it was on the TODO tho
```
```
kayabanerve: Yeah, our arithmetic circuit didn't work to the specification because we had this optimization but it was also undocumented and never formally considered.
```
```
kayabanerve: So we could've also done formal analysis, but it made sense just to take the perf hit and be correct.
```
```
kayabanerve: It increases the time to build the tree tbf
```
```
kayabanerve: But yeah, a type to represent key images which can't be torsioned, may also make sense and fit in here.
```
```
boog900: ah fair 
```
```
kayabanerve: Any public thoughts on the `epee` PR I opened? I put forth my own lib to monero-oxide which is non-allocating (to ensure no memory exhaustion attacks are possible) and zero-dep (but optionally can work with `bytes::Bytes`). It's duplicating with Cuprate and silly in that regard. It just also achieves some specific properties which may be appreciated.
```
```
kayabanerve: I think boog900 is resigned to it, if even just because they don't want to debate `bytes::Buf` vs `&[u8]` superiority with me.
```
```
boog900: I support it for monero-oxide 
```
```
boog900: I don't really want to move Cuprate over at the moment thougj 
```
```
boog900: * I don't really want to move Cuprate over at the moment though
```
```
boog900: > bytes::Buf

We are no longer going to use this FWIW 
```
```
kayabanerve: I am able to not care what Cuprate does and simply do my best to support Cuprate being able to move over 👍️
```
```
boog900: we can make better optimizations if we know the memory is contiguous so I am going to move us over to just parsing from a `Bytes` 
```
```
boog900: or it might be a `BytesMut`
```
```
boog900: I think `BytesMut` gives us more methods to work with 
```
```
kayabanerve: 😱
```
```
boog900: as it is a unique reference 
```
```
kayabanerve: On a more legitimate note, I've found `Read` an acceptable API. The issue is in how it requires copying out of the non-contiguous memory.
```
```
kayabanerve: I am surprised you can consider `BytesMut` as it'd prevent a ring buf, which I'd have assumed useful within Cuprate.
```
```
boog900: nah it doesn't prevent it you can call split on a `BytesMut` to get 2 instances 
```
```
kayabanerve: *The issue would be how...
```
```
boog900: then drop the first call reclaim on the second to get the full memory region back 
```
```
boog900: which is what happens in tokio-codec 
```
```
kayabanerve: If you have a ring buf of 1000 bytes, and are 500 bytes in, and receive a 750 byte message, it spans 500 .. 1250 % 1000, and you can not represent the messages with a `BytesMut`
```
```
boog900: ah then you get a reallocation, sure 
```
```
kayabanerve: You can with two `BytesMut`, sure.
```
```
boog900: but then it is permanently bigger 
```
```
boog900: and seen as we handle 1 message at a time it wont go above the max message size 
```
```
syntheticbird: hello
```
```
kayabanerve: Well, you either need to allow non-contiguous memory, or you need to re-alloc, or you need to copy out into a sufficiently-sized contiguous region.
```
```
syntheticbird: i'm sorry for being late
```
```
kayabanerve: For epee, I don't believe it ever copies out. The close
```
```
kayabanerve: *I don't believe it ever copies out large slices of memory. The closest would be for strings, where we return a fork of the reader for the relevant region.
```
```
kayabanerve: But then for strings, we already iterate over them to handle them, so the fact it's non-contiguous isn't too relevant/harmful to us.
```
```
kayabanerve: For the more complicated case, JSON, which I also worked on, I don't believe contiguous memory would be of any notable benefit actually as we always iterate over the bytes. The only guarantee of the amount of bytes you'll end up reading is for small items like `false` (5 characters), in which sure, reading 5 values from contiguous memory is one memcpy vs up to 5 (if stored in 5 sections of a rope for some horrific reasons).
```
```
kayabanerve: The greater benefit is in replayable memory which you can access multiple times, which you don't have with `Read` or `Iterator`, but would of course have with `Buf`.
```
```
kayabanerve: (Y'all do you, I'm just noting in my experience, I don't think contiguous memory would benefit the cases I've worked on, obv Cuprate has its own cases :) )
```
```
kayabanerve: We also _could_ remove the requirement to fork the reader to represent strings from the `epee` lib I wrote. I already demonstrated the ability to do that elsewhere... That'd also allow it to be used with `R: Read` which may be pleasant.
```
```
kayabanerve: ... how feasible would `cuprate-epee-types` be with `R: Read`? Is this a niche worth filling?
```
```
boog900: they use `Bytes` for their fields 
```
```
kayabanerve: Ah, so `R: Read` doesn't work because you fork the reader same as the lib I wrote, got it
```
```
kayabanerve: kk
```
```
boog900: it might work but it would be pretty expensive too I would think 
```
```
boog900: having all the bytes point to different allocations etx 
```
```
boog900: * having all the bytes point to different allocations etc
```
```
kayabanerve: You'd at least have to support not forking to bytes, but collecting into bytes if the input isn't already represented as a bytes
```
```
kayabanerve: Which you _can_ do with a trait for the subset of `Bytes` you need, implemented for `Bytes` or `R: Read` with ugly allocations such that the result is still a `Bytes`
```
```
kayabanerve: But yeah, that's bs best left out of Cuprate AFAICT
```
```
kayabanerve: Oh. I would like to create audit statements for monero-oxide's tree. If anyone is interested in volunteering, lmk, and I'll prioritize a PR for the infra so people can contribute their own statements.
```
```
boog900: hinto: is there anything you want to discuss on ZMQ?
```
```
hinto: Not yet, although I had other discussion points
```
```
boog900: yep sure go ahead 
```
```
hinto: Considering `cuprated` has been stable since the first release (7 months ago now) and that no critical bugs have surfaced (at least that I know of), I plan to submit a PR to remove the killswitch for the next release, any other discussion on this?: https://github.com/Cuprate/cuprate/issues/468
```
```
hinto: If wallet sync is available next release I think `cuprated 0.1.0` could be appropriate as well: https://github.com/Cuprate/cuprate/issues/467
```
```
hinto: (we'd have to decide a new release code name: https://github.com/Cuprate/cuprate/issues/477)
```
```
boog900: > <@hinto:monero.social> If wallet sync is available next release I think `cuprated 0.1.0` could be appropriate as well: https://github.com/Cuprate/cuprate/issues/467

I think I would want syncing and sending txs first 
```
```
boog900: And any other basic wallet functionality
```
```
boog900: > <@hinto:monero.social> Considering `cuprated` has been stable since the first release (7 months ago now) and that no critical bugs have surfaced (at least that I know of), I plan to submit a PR to remove the killswitch for the next release, any other discussion on this?: https://github.com/Cuprate/cuprate/issues/468

Yeah I support removing the kill switch 
```
```
syntheticbird: please enumerate them
```
```
syntheticbird: otherwise i agree on the idea
```
```
kayabanerve: With the new RPC PR in-place, it may make sense to see if Cuprate can be used in place of monerod within the monero-oxide CI boog900 
```
```
kayabanerve: If it can't fulfill the RPC to wallet2, monero-oxide, I'd agree with hesistance before 0.1.0
```
```
boog900: yeah I'll test that out once I get basic wallet2 support 
```
```
kayabanerve: Speaking of, new RPC PR, if anyone has comments, get them in. I think the PR itself is over 100 commits?
```
```
kayabanerve: Should establish a much clearer path to using parts of Cuprate within end-user apps to remove the requirement on an external RPC
```
```
kayabanerve: (instead of requesting decoys from a node, using Cuprate's linear tape DB to locally store output information)
```
```
boog900: ehh just anything I run into when I test if wallet2 works 
```
```
boog900: I don't care about niche things atm 
```
```
syntheticbird: SOUNDS CLEAR AND FORMAL. LET'S GO FOR IT 👍️👍️👍️
```
```
kayabanerve: Does Cuprate support binary strings in JSON?
```
```
kayabanerve:  /s :P
```
```
syntheticbird: binary strings?
```
```
syntheticbird: you mean garbage?
```
```
syntheticbird: nah we don't
```
```
kayabanerve: Monero has some super fucked up RPC routes which take epee, perform a bespoke string escape function on them, and shoves them into JSON.
```
```
kayabanerve: Oh, it was a joke, got it.
```
```
kayabanerve: TBF, I do know of a JSON serializer for which you could reasonably implement those fucked up RPC routes with.
```
```
kayabanerve: If anyone wants to waste their time on 100% RPC compliance, before Monero removes the RPC routes in question... talk to me 😎
```
```
boog900: the JSON dealer 
```
```
boog900: any other topics you want to discuss hinto 
```
```
syntheticbird: The parser bender
```
```
kayabanerve: Hello! I heard you hadn't reconsidered your choice of JSON library in two years. Have you seen the efficiency on our latest models? Watch, as I dump 2 GB of unrecognizable 'epee' on your floor, and how quickly we can suck it up!
```
```
hinto: I think we can move on / end
```
```
kayabanerve: Those routes are so cursed 😭 To be fair, all of epee is. Its JSON doesn't support outer arrays, nested arrays :(
```
```
boog900: Monero is held together by thoughts and prayers 
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
syntheticbird: thanks
```
```
boog900: !meeting 
```

# Action History
- Created by: moo900 | 2025-10-14T15:03:39+00:00
- Closed at: 2025-10-21T19:13:13+00:00
