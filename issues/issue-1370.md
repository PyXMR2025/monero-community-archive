---
title: 'Cuprate Meeting #99 - Tuesday, 2026-04-21, UTC 18:00'
source_url: https://github.com/monero-project/meta/issues/1370
author: moo900
assignees: []
labels: []
created_at: '2026-04-14T18:39:17+00:00'
updated_at: '2026-04-21T19:05:48+00:00'
type: issue
status: closed
closed_at: '2026-04-21T19:05:48+00:00'
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

Previous meeting: #1367

# Discussion History
## moo900 | 2026-04-21T19:05:47+00:00
## Meeting logs
```
boog900: 1) greetings
```
```
redsh4de: hello
```
```
hinto: hello
```
```
boog900: 2) updates
```
```
boog900: me: got the tapes PR merged + more RPC work 
```
```
hinto: me: readying 0.0.9 and just now finished another batch of sync tests, here are some averaged results across a few runs:
```
```
hinto: - Default config
- Target block height: `3551183`
- `fast-sync = true`

| machine     | `target_max_memory` | `0.0.8` | `new-db` | speed increase |
|-------------|---------------------|---------|----------|----------------|
| pi 5        | 8GB                 | 25h2m   | 8h18m    | 3.02x
| mac mini m2 | 8GB                 | 12h24m  | 3h10m    | 3.92x
| vps         | 4GB                 | 2d8h33m | 4h45m    | 11.91x

```
```
boog900: nicccce :)
```
```
hinto: table formatting seems broken - `new-db` is a lot faster, especially on slower disks
```
```
hinto: Pi 5 has access to quite a fast SSD so the difference there wasn't as big as expected
```
```
syntheticbird: Hello
```
```
redsh4de: me: looked into how to resolve the ki map fixme - so far i think making consensus use a typestate pattern for all block prep stages, and passing the spent_key_images through each is the cleaner way to handle it, vs. adding an `Arc` to `VerifiedBlockInformation`. concern mix, have to construct txpool-only data in places that don't need it, etc, etc.
```
```
redsh4de: <image.png>
```
```
redsh4de: something of this sort
```
```
redsh4de: would also do away with the `bool` that marks if spent key images were checked or not that is currently used, if checking once at *some* point before constructing the final state is programmed in
```
```
boog900: hmm
```
```
boog900: we join all KIs together during batch sync, so you would need to separate them right? 
```
```
boog900: we do one big lookup during sync IIRC which is why we have the bool - so we don't need to look up if they are spent for every block 
```
```
redsh4de: dont think so, if they are joined only for checking for validity

if the batch check fails though then the entire batch would be invalid
```
```
boog900: Yeah but then we would need to create a ki map per block 
```
```
boog900: seperate from the joint one for validity 
```
```
redsh4de: that would be done in the verify_next_block stage in the graph, where it creates the spent_key_images
```
```
boog900: looking at it I don't think the current way is too bad, it was worse when we needed to do point compressions 
```
```
boog900: but now they are stored compressed 
```
```
redsh4de: yeah its not bad at all, its mostly to easily pass through the spent_key_images that are computed at seperate parts in the consensus crate, and give them to the handler
```
```
redsh4de: this is also why i had the `from_batch_prepared` there for the CheckedBlock stage - it skips the ki map check when constructing it, because the batch preparation already made sure that all key images are valid
```
```
boog900: my point was that you will have to create a new hashmap per block
```
```
boog900: just like what we currently do 
```
```
boog900: as well as the joint one for all blocks during the check 
```
```
boog900: so its the same for syncing but it is better for relay 
```
```
boog900: Or am I missing something
```
```
boog900: I think we can move on for now
```
```
boog900: hinto: do you need me to do anything at the moment for 0.0.9?
```
```
hinto: all that is left is merging 600 and the update post
```
```
boog900: alright is there anything else to discuss today? 
```
```
syntheticbird: yes
```
```
boog900: no moo pfp
```
```
syntheticbird: COME ON 
```
```
syntheticbird: no im joking on something else
```
```
hinto: In order to prevent delaying a beta release I think I'll PR reproducible builds for now, to eventually be replaced by stagex
```
```
syntheticbird: stop reading my mind
```
```
boog900: sounds good 
```
```
syntheticbird: tho seriously i was gonna ask for low-hanging easy opinion on my big paragraph of ideas i got for dependency security
```
```
syntheticbird: s/i got/i made
```
```
hinto: Also I'd like to acknowledge on the record that I won't be as available to Cuprate in the following year(s)
```
```
hinto: on PR approval or other decisions: I'm ok with letting go on I think everything
```
```
hinto: I'm not sure how future meetings will be go although I think I can keep moo online indefinitely
```
```
boog900: alright, yeah we'll have to figure it out 
```
```
syntheticbird: Sure, thanks for everything so far hoping your future projects do well and thanking you in advance for your potential time you will spent on cuprate in the future.
```
```
boog900: On that sad note, I think we can end here, unless anyone wants to discuss anything else?
```
```
redsh4de: i mean like, each block type in my graph would carry through just the raw key images in a vec like they are now

for batch verification we only would join the key images from all blocks at verification time via a copy, so they are still owned by each block. after batch verify passes we just pass the blocks + their key images and make a `PreparedBlockBatch` from it

and if we create a CheckedBlock from a BatchPreparedBlock, we dont have to re-do the ki verification, because we trust that during batch verification we already did all the required checks. idk if that clarifies what i had in mind
```
```
boog900: > carry through just the raw key images in a vec like they are now

Where are they carried through now?
```
```
boog900: AFAIK they are just created we doing the spent lookup in the DB
```
```
redsh4de: yeah mistyped
```
```
boog900: So when syncing I don't really see how this is better right?
```
```
boog900: it'll just be for relayed blocks.
```
```
redsh4de: yeah for syncing it changes nothing, only for relay which the fixme was on
```
```
redsh4de: *where the fixme was in
```
```
boog900: hmm that function is called on both relay + syncing 
```
```
boog900: we still need to removed txs from the pool when syncing 
```
```
redsh4de: you mean check_kis_unique?
```
```
boog900: `add_valid_block_to_main_chain`
```
```
boog900: rust
    pub async fn add_valid_block_to_main_chain(
        &mut self,
        verified_block: VerifiedBlockInformation,
    ) {
        // FIXME: this is pretty inefficient, we should probably return the KI map created in the consensus crate.

```
```
boog900: I think we can end here, we can keep discussing though.
```
```
boog900: !meeting 
```

# Action History
- Created by: moo900 | 2026-04-14T18:39:17+00:00
- Closed at: 2026-04-21T19:05:48+00:00
