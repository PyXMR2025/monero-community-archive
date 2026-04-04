---
title: 'Cuprate Meeting #58 - Tuesday, 2025-06-03, UTC 18:00'
source_url: https://github.com/monero-project/meta/issues/1212
author: moo900
assignees: []
labels: []
created_at: '2025-05-27T18:55:58+00:00'
updated_at: '2025-06-03T18:58:57+00:00'
type: issue
status: closed
closed_at: '2025-06-03T18:58:57+00:00'
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

Previous meeting: #1207

# Discussion History
## moo900 | 2025-06-03T18:58:56+00:00
## Meeting logs
```
boog900: 1) greetings 
```
```
hinto: hello
```
```
syntheticbird: hi
```
```
boog900: 2) updates 
```
```
syntheticbird: me: nothing new. addressing nits of tor zone pr
```
```
boog900: me: finished the the tx-pool manager PR also worked on the config flatten 
```
```
sgp_: Hello
```
```
hinto: me: working on RPC endpoints for `wallet2`, preparing `cuprated v0.0.4`
```
```
boog900: 3) Project: What is next for Cuprate?
```
```
syntheticbird: the end is near
```
```
syntheticbird: the current motto must fall
```
```
hinto: also still fuzzing, no crashes yet, although a new message:

  NEW_FUNC: 0x55a958b76e20  ($HOME/cuprate/target/x86_64-unknown-linux-gnu/release/levin_codec+0x3efe20) (BuildId: 16fa4eba6d1aca4f74a70adf89e025b6bd5fefdd)

```
```
hinto: boog900: do you know what this means?
```
```
syntheticbird: new branch discovered?
```
```
boog900: the fuzzer found a new func it can hit, just a guess 
```
```
boog900: will review 450 today 
```
```
hinto: will 450 462 be merged today? the release deadline is tomorrow and I have not tested builds yet
```
```
hinto: 490 as well although I guess it's optional
```
```
syntheticbird: open 490 for review
```
```
syntheticbird: will also review 450
```
```
syntheticbird: * will also review 450 before tomorrow
```
```
hinto: my bad, they should both be ready
```
```
hinto: I will update 490 to the latest hash then open
```
```
boog900: hmm it might be best to leave 450 out of this release, do you want it to be included? 
```
```
boog900: I think we _could_ get it in 
```
```
syntheticbird: Yes
```
```
hinto: yes, otherwise there is no basic RPC for another 6 weeks
```
```
boog900: fair 
```
```
hinto: we could enable only `/get_height` as a minimum but also to be fair these are alpha releases
```
```
hinto: there will be bugs
```
```
hinto: or perhaps disable the RPC servers by default for now
```
```
boog900: true, even if we delay people will still probably stumble into issues when we release them 
```
```
boog900: I think the current setup is ok, we don't publicly advertise it over P2P
```
```
hinto: I'll put some warnings in the RPC section
```
```
boog900: anything else anyone wants to discuss today? 
```
```
syntheticbird: yes
```
```
syntheticbird: the motto
```
```
syntheticbird: >  an upcoming experimental, modern & secure Monero node. Written in Rust 
```
```
syntheticbird: We already tried to address it once in meeting last year
```
```
syntheticbird: there has been a lot of ideas
```
```
syntheticbird: wondering if you guys thought about it, got any new ideas?
```
```
hinto: I would say being descriptive would look better than any claims, e.g. 'secure'
```
```
syntheticbird: yeah kayaba already made a remark around the "secure"
```
```
sgp_: From me: MAGIC Grants improved the explorer API with a dockerfile and instructions: https://github.com/MAGICGrants/rust-monero-explorer
```
```
sgp_: I observed a crash with that program on Cuprate resizing as you suspected would happen
```
```
sgp_: otherwise, it works great
```
```
boog900: I think we are going to end up with something like: `A Rust Monero node`
```
```
hinto: sgp_: do you have the crash message?
```
```
boog900: I don't think anything more complicated is going to have support 
```
```
boog900: This crash is expected btw lmdb errors when another process resizes the DB 
```
```
sgp_: <signal-2025-06-03-115847_002.jpeg>
```
```
hinto: ah... I should mention that I can't load images
```
```
hinto: I think it's an error with monero.social: `M_NOT_FOUND`
```
```
boog900: `fix the database code! MapResized`
```
```
syntheticbird: I don't support something as simple. I need more energy 
```
```
hinto: I am unsure if we need to panic there, as long as `new_size >= current_size` does it matter that another process resized it?
```
```
syntheticbird: `Cuprate: A monero node emphasizing on performance and correctness. Written in Rust.` ?
```
```
boog900: LMDB returns an error until we resize the database in the current process  
```
```
boog900: we just panic on that error 
```
```
boog900: this happens with read txs as well btw, which makes it even more annoying 
```
```
boog900: http://www.lmdb.tech/doc/group__mdb.html#gaa2506ec8dab3d969b0e609cd82e619e5
```
```
boog900: > If the mapsize is increased by another process, and data has grown beyond the range of the current mapsize, mdb_txn_begin() will return MDB_MAP_RESIZED. This function may be called with a size of zero to adopt the new size.
```
```
boog900: The block explorer here uses the raw DB api so the best we can do for them is return the error. For the tower interface we should do the resize and do the request again.   
```
```
hinto: okay, will submit a PR
```
```
keeqler: anyone got any ideas of new features we can add to our block explorer, using what cuprate offers rn?
```
```
keeqler: we currently have a /transaction and /block endpoints
```
```
boog900: Not off of the top of my head atm. I do want to ask why you decided to go with the raw db interface over the tower interface 
```
```
boog900: not that there is anything wrong with that just that it is harder to use IMO
```
```
keeqler: I simply used what I could find, I have no idea what the tower interface is
```
```
keeqler: I'm new to both rust and the cuprate project
```
```
hinto: here's example usage of the tower interface: https://doc.cuprate.org/cuprate_blockchain/service/index.html#example
```
```
boog900: here is another example usage: https://github.com/Cuprate/cuprate/blob/e3f60cc77e2321bfc58c7ca24b13b008820766cc/binaries/cuprated/src/blockchain/interface.rs#L178-L187
```
```
boog900: you can replace giving the `ConcreteEnv` to every func and instead give a `BlockchainReadHandle` 
```
```
boog900: here are the possible requests: https://doc.cuprate.org/cuprate_types/blockchain/enum.BlockchainReadRequest.html
```
```
keeqler: very interesting, I will give that a try
```
```
keeqler: thanks :)
```
```
boog900: let us know how it goes :)
```
```
boog900: anything else to discuss today? 
```
```
hinto: I think I am going to be giving more time towards Carrot/FCMP++ in the near future
```
```
boog900: on the monerod side?
```
```
hinto: the main upstream PR + the guix PR seem like it will take a while to be ready, so I have been thinking about helping more directly
```
```
boog900: sure 👍️
```
```
boog900: I think we can end here
```
```
boog900: thanks everyone!
```
```
syntheticbird: thx
```
```
hinto: thanks
```
```
boog900: !meeting 
```

# Action History
- Created by: moo900 | 2025-05-27T18:55:58+00:00
- Closed at: 2025-06-03T18:58:57+00:00
