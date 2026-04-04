---
title: 'Cuprate Meeting #37 - Tuesday, 2025-01-07, UTC 18:00'
source_url: https://github.com/monero-project/meta/issues/1129
author: moo900
assignees: []
labels: []
created_at: '2024-12-19T18:13:09+00:00'
updated_at: '2025-01-07T20:04:18+00:00'
type: issue
status: closed
closed_at: '2025-01-07T20:04:18+00:00'
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

Previous meeting: #1128

# Discussion History
## moo900 | 2025-01-07T20:04:18+00:00
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
boog900: Me: I finished the `init` PR and the 32 bit support PR.  
```
```
boog900: also started reviewing the RPC handlers PR
```
```
syntheticbird: Me: let some comments on init PR
```
```
hinto: me: posted an update on my CCS as well: https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/484#note_27936
```
```
hinto: I've taken a break since then and am getting back on schedule today starting with finishing the roadmap writeup for 2025
```
```
boog900: 3) Project: What is next for Cuprate?
```
```
boog900: hinto: I did want to discuss not using `heed` instead using the LMDB bindings directly 
```
```
boog900: it will allow us to fix `get_range` and will probably make adding multi-map tables easier 
```
```
hinto: are you saying we should uphold LMDB invariants ourselves? my initial instinct is that that seems like an extreme solution compared to patching/forking heed 
```
```
boog900: We already have an abstraction layer so the upholding of invariants will be done there. IMHO `heeds` API is too restrictive, we could fork it but then we are maintaining 2 abstractions  
```
```
hinto: off the top of my head we would have to deal with raw pointers and error checking, anything else? maybe it's not too bad actually although throwing away a safe abstraction layer hurts
```
```
hinto: I agree it would be a lot less restrictive and make things like cursors and sorting a lot easier in some sense
```
```
boog900: It's not something that I plan to work on immediately, but just putting the idea out there, I do think it's the best path forward. 
```
```
boog900: especially if we plan to add multimap support 
```
```
boog900: (needed for FCMP IIRC)
```
```
boog900: we can move on if anyone has anything else they want to discuss 
```
```
syntheticbird: So if i understand correctly after Cuprate RPC handler and init PR merged, we just need another PR adding the RPC service in binary and we can test usage for wallet?
```
```
boog900: not exactly some requests for the inner services need to be added. Although some endpoints will be available: https://github.com/Cuprate/cuprate/pull/355#pullrequestreview-2518542438 
```
```
syntheticbird: alright.
i have one last discussion in mind, it's about the cuprate motto that will need to change
```
```
hinto: My current plan is for RPC integration is:

1. Create generic `monerod` <-> `cuprated` RPC testing harness
2. Focus on testing RPC calls that `wallet2` requires
3. Integrate RPC calls throughout alpha `cuprated` releases in priority order

The priority for RPC calls is:

1. Calls required by `wallet2`
2. Non-required but frequently used calls
3. Everything else

```
```
boog900: > <@syntheticbird:monero.social> alright.
> i have one last discussion in mind, it's about the cuprate motto that will need to change

any suggestions?
```
```
malori: whats the current motto already?
```
```
syntheticbird: An upcoming experimental, modern & secure monero node. Written in Rust
```
```
kayabanerve: > <@boog900:monero.social> (needed for FCMP IIRC)

Can you elaborate here please?
```
```
syntheticbird: i think it sounds great to the ear, but experimental and secure kinda don't make sense
```
```
syntheticbird: experimental was meant to signify cuprate willing to be a testing ground for new features. (we can wait on response for kayaba)
```
```
boog900: > <@kayabanerve:matrix.org> Can you elaborate here please?

In the DB a multimap table is used to store the tree (I think)
```
```
kayabanerve: Agreed, "An upcoming experimental, modern, and dangerous Monero node written in Rust"
```
```
kayabanerve: That's my suggestion ^ /s
```
```
kayabanerve: > <@boog900:monero.social> In the DB a multimap table is used to store the tree (I think)

Yes but you don't need to mirror monerod? So do you have a performance argument you can elaborate on?
```
```
kayabanerve: "An independent, performant reimplementation of the Monero protocol in Rust"?
```
```
kayabanerve: The only arguments against independent are libc, LMDB, RandomX, and FCMP++ until y'all rewrite that in C++.
```
```
malori: yup gonna rewrite whole libc for cuprate mate <img data-mx-emoticon height="32" src="mxc://xavi.lu/izCpcGwVRXZPiqaBlPftLNLd" alt="monerochan-thumbsup" title="monerochan-thumbsup">
```
```
syntheticbird: relibc
```
```
boog900: > <@kayabanerve:matrix.org> Yes but you don't need to mirror monerod? So do you have a performance argument you can elaborate on?

true. `monerod` also stores outputs in a multimap table, we store v1 outputs with the key being: `(amount, amount_index)`. This means for every v1 output we store the amount, whereas `monerod` is only storing each amount once.

For v2 outputs we use a separate table with the key just `amount_index`
```
```
kayabanerve: Won't those keys be deduplicated? LMDB uses a tree, no?
```
```
boog900: so it is for efficiency reasons, I guess I shouldn't have said "needed"
```
```
kayabanerve: You shouldn't actually have increased storage costs across a common prefix.
```
```
kayabanerve: I do understand LMDB isn't the sole, explicit backend, so there's performance commentary available re: other backends, I'm just saying rewriting heed doesn't seem a priority
```
```
syntheticbird: I don't like the independent, also i would to emphasize on security somehow.
```
```
malori: something like "Aa secure, performant reimplementation of the Monero protocol in Rust" then?
```
```
kayabanerve: 1) why not "independent"
2) make an argument for Cuprate's security which withstands review or don't advertise it as such
```
```
malori: I dont like the independent too, it dont mean a lot
```
```
kayabanerve: I explicitly dropped "secure" as I can't make that argument
```
```
boog900: > <@kayabanerve:matrix.org> You shouldn't actually have increased storage costs across a common prefix.

I thought LMDB stores each key per value, something has to explain our 50 GB bigger DB :p
```
```
syntheticbird: independent doesn't add real value to the description. everyone guess its independent since, well, it's another repository, another language
```
```
syntheticbird: yeah lmao same thought, i was going to say: "then where tf is the 259GB coming from"
```
```
kayabanerve: boog900 @boog900:monero.social: I may be wrong, I'm just assuming the tree achieved prefix deduplication
```
```
kayabanerve: > <@syntheticbird:monero.social> independent doesn't add real value to the description. everyone guess its independent since, well, it's another repository, another language

There are a variety of alternative nodes which aren't independent yet arguably just distinct front ends for a common core. See all of the Monero wallets, and the singular wallet2.
```
```
kayabanerve: Clarifying you don't hook into cryptonote_basic, cryptonote_core is meaningful.
```
```
boog900: LMDB returns a pointer to the key I don't know how it would do that if the key wasn't continuous
```
```
kayabanerve: (to me at least)
```
```
kayabanerve: boog900 @boog900:monero.social: By allocating a buffer for the key as it performs tree traversal and returning a pointer to that buffer? But yes, that implies key -> (key, value)
```
```
kayabanerve: I don't believe Cuprate can make a security argument other than memory safety. It is inherently a fingerprint, hasn't been audited, and has had far less review than Monero proper.
```
```
kayabanerve: (Unless you argue the monero-serai audits, as then we may have more audited functionality than Monero proper :p )
```
```
malori: > <@kayabanerve:matrix.org> I don't believe Cuprate can make a security argument other than memory safety. It is inherently a fingerprint, hasn't been audited, and has had far less review than Monero proper.

okay thats fair
```
```
hinto: boring slogan suggestion: adjectives could be removed to be more timeless e.g. `Monero node implementation in Rust.`
```
```
malori: memory safe then 
but this is implied by rust
```
```
kayabanerve: We're auditing all our proofs and TX types. Monero has only audited their proofs historically? I think?
```
```
kayabanerve: "Rust Monero node"
```
```
malori: nah need simpler
monero node rust
```
```
syntheticbird: > <@kayabanerve:matrix.org> (Unless you argue the monero-serai audits, as then we may have more audited functionality than Monero proper :p )

It was just a matter of "we value correctness and security"
```
```
syntheticbird: At the time 
```
```
syntheticbird: And its still the case :p
```
```
kayabanerve: Security minded != secure
```
```
malori: "cuprate is a memory safe thanks to rust monero node that aim to be secure because we are very secure minded, and is independent exept for all the c libs we use"
```
```
kayabanerve: And the fcmp++ code
```
```
syntheticbird: > <@malori:xavi.lu> nah need simpler
> monero node rust

Too simple
```
```
syntheticbird: Indeed
```
```
syntheticbird: "Cuprate, the modern, superconducting monero node. Written in Rust" ?
```
```
syntheticbird: Cuprate is a superconductor after all
```
```
malori: physic joke yay
```
```
kayabanerve: Proof of superconduction or gtfo
```
```
boog900: "The fastest Monero node (to sync the chain (not using fast sync))"
```
```
syntheticbird: Lmao
```
```
malori: (but at the cost of an extra 50GB )
```
```
kayabanerve: Is it fastest on an HDD?
```
```
malori: I dont even want to try
```
```
syntheticbird: HDD don't exist
```
```
malori: last time i wanted to sync monerod on an hdd one week had past and im not ever sure i was at half
```
```
kayabanerve: I'm hearing a lot of false advertising here
```
```
malori: on pruned
```
```
malori: :)
```
```
kayabanerve: Please, keep going, my lawyer appreciates it
```
```
malori: so not testing that
```
```
kayabanerve: And do I sue Mr. Bird personally or...?
```
```
kayabanerve: :p
```
```
boog900: "Cuprate: a node"
```
```
syntheticbird: ROFL
```
```
kayabanerve: "Cuprate: a node in Rust" SGTM
```
```
boog900: mostly in Rust*
```
```
kayabanerve: *primarily in Rust
```
```
kayabanerve: Yes, exactly
```
```
kayabanerve: That way you aren't liable for edge cases in implementing the Monero protocol
```
```
syntheticbird: STOP THE HIVE MIND
```
```
kayabanerve: "An independent, performant reimplementation of the Monero protocol in Rust"?
```
```
boog900: yeah I like that
```
```
syntheticbird: I don't feel like it
```
```
boog900: I think we might have to leave it for another time, anything else anyone wants to discuss today?
```
```
kayabanerve: When are y'all reimplementing FCMPs++?
```
```
kayabanerve: 👀
```
```
kayabanerve: You don't have to do it in C++ but obviously that'd preserve aesthetics
```
```
syntheticbird: Holy molly. Kayaba we are all going to end up informal cryptographer bc of u
```
```
boog900: I was thinking of doing it in zig next Tuesday 
```
```
kayabanerve: boog900 @boog900:monero.social: you're dead to me
```
```
syntheticbird: LMFAO
```
```
boog900: :)
```
```
syntheticbird: Missed the Nim trend
```
```
kayabanerve: I used to write Nim
```
```
syntheticbird: > <@kayabanerve:matrix.org> I used to write Nim

Did you enjoyed ?
```
```
kayabanerve: No
```
```
kayabanerve: It was extremely buggy and I didn't appreciate the language's stabilization policy.
```
```
kayabanerve: stabilization/versioning
```
```
hinto: I am under the assumption that there's a large enough window before FCMP++ is live on `monerod` such that there is benefit to releasing an alpha `cuprated` and associated libs/docs before FCMP integration
```
```
hinto: There's also the question of if `cuprated` will/should be FCMP++ compatible (in a practical sense, working sync, RPC, libs, etc) alongside when it is live on `monerod` or if it will be slowly added after, perhaps after the alpha moniker is dropped
```
```
boog900: If by when it's live you mean mainnet, then I definitely believe Cuprate should be ready at that point.
```
```
boog900: otherwise yeah it'll depend on how quick we finish the foundations 
```
```
syntheticbird: Agreed. Cuprate is just another project i've to take over Core (along kewbit), so i won't accept that Cuprate isn't take into account in hard forking schedule
```
```
boog900: I think we can finish here, thanks everyone!
```
```
syntheticbird: thanks
```

# Action History
- Created by: moo900 | 2024-12-19T18:13:09+00:00
- Closed at: 2025-01-07T20:04:18+00:00
