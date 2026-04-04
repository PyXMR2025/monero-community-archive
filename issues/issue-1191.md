---
title: 'Cuprate Meeting #53 - Tuesday, 2025-04-29, UTC 18:00'
source_url: https://github.com/monero-project/meta/issues/1191
author: moo900
assignees: []
labels: []
created_at: '2025-04-22T19:02:01+00:00'
updated_at: '2025-04-29T19:08:38+00:00'
type: issue
status: closed
closed_at: '2025-04-29T19:08:37+00:00'
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

Previous meeting: #1188

# Discussion History
## moo900 | 2025-04-29T19:08:36+00:00
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
syntheticbird: Will PR in a few minutes Transport trait PR
```
```
syntheticbird: While it get reviews I'll investigate tokio_io_timeout crate to write a send timeout PR for cuprate-types
```
```
syntheticbird: cuprate-helper*
```
```
boog900: me: I took a few days off, back now and will PR reversing invalid reorgs after the meeting 
```
```
hinto: me: finished initial RPC server PR, planning `v0.0.3`
```
```
boog900: 3) Project: What is next for Cuprate?
```
```
syntheticbird: hinto I suppose you tested cuprated.service ? for #444
```
```
hinto: yup, it's been running stable, I think the syscall filters can be even more restrictive but the current commit works for now
```
```
syntheticbird: great
```
```
hinto: boog900: how do you feel about https://github.com/Cuprate/cuprate/issues/432?
```
```
syntheticbird: I don't have a systemd VM on hand to test sync with it. I was afraid it would come unstable
```
```
hinto: I think we could include docker + cuprated.service in the `v0.0.3` user book
```
```
syntheticbird: agree
```
```
boog900: don't really have much opinion on it, happy to merge it though, docker isn't something I have much experience with 
```
```
hinto: any thoughts on https://github.com/Cuprate/cuprate/pull/423? I think it can be merged as is although I've left some notes
```
```
syntheticbird: I've seen the mention I was planning on answering either tonight or tomorrow
```
```
syntheticbird: and let a review ofc
```
```
boog900: does monerod support http compression?
```
```
syntheticbird: Unfortunately no
```
```
syntheticbird: monerod only understand a very few subset of headers. bare minimum i could say
```
```
syntheticbird: just what is needed to route the request
```
```
syntheticbird: so I don't expect them to support compression any time soon
```
```
syntheticbird: time soon either*
```
```
boog900: do we want to support it then? with the extra depends in pulls in/code surface.
```
```
syntheticbird: I say yes
```
```
boog900:  * do we want to support it then? with the extra depends it pulls in/code surface.
```
```
syntheticbird: Compression is definitely useful for wallet users and tor users
```
```
syntheticbird: since onion services have much lower bandwith
```
```
boog900: monerod manages currently, I always thought the blockchain data can't be compressed much anyway 
```
```
syntheticbird: it's transmitted stringified in json, so there is some room for compression
```
```
boog900: which makes up most of the RPC bandwidth 
```
```
boog900: > <@syntheticbird:monero.social> it's transmitted stringified in json, so there is some room for compression

I thought it used epee 
```
```
syntheticbird: I need to check back im not sure anymore which handler is using epee format
```
```
boog900: I know RPC supports JSON but wallets use the bin interface 
```
```
syntheticbird: oh
```
```
boog900: for the data heavy requests anyway 
```
```
syntheticbird: i see
```
```
syntheticbird: idk, worth some compression benchmark on these requests if i have time. my general sentiment is we could support gzip and zlib compression as they are the most popular
```
```
boog900: yeah maybe although for now we should just remove them IMO
```
```
syntheticbird: why?
```
```
syntheticbird: they are free improvements
```
```
boog900: at the cost of extra deps 
```
```
syntheticbird: ah i forgor
```
```
syntheticbird: ok
```
```
hinto: I am okay with either
```
```
syntheticbird: 1 for, 1 against, 1 neutral. Definitely something to decide with rock paper scisors
```
```
boog900: for now, remove; if they do provide a sufficient drop in data transferred then we can look at enabling them.
```
```
syntheticbird: waiting for benchmark, fine for me
```
```
hinto: any other thoughts?
```
```
boog900: `i_know_what_im_doing_allow_public_unrestricted_rpc` is very long 
```
```
syntheticbird: I like it
```
```
syntheticbird: its long enough that it will instigate doubt in people that ignore its consequence
```
```
syntheticbird: 10/10 game level design
```
```
boog900: ok yeah fair
```
```
boog900: hinto: why does it matter that we can't selectively enable `json_rpc` endpoints?
```
```
boog900: are some only enabled when using unrestricted RPC?
```
```
hinto: because not all `/json_rpc` methods will be complete at the same time
```
```
hinto: a subset will be ready, the rest need to return some type of error, until all are complete
```
```
boog900: IMO I think `Return error responses` is the best option 
```
```
syntheticbird: My proposition was that we return NOT_IMPLEMENTED HTTP code for valid methods that aren't yet implemented
```
```
syntheticbird: as it make more sense
```
```
syntheticbird: but if it tiresome for hinto because of the macro let's just return 404
```
```
boog900: yeah although nice, if it is complicated it isn't worth the effort 
```
```
syntheticbird: It's not complicated
```
```
syntheticbird: just annoying
```
```
syntheticbird: but yeah we can skip it and sleep without regrets
```
```
boog900: these shouldn't be not impl'd for too long, just go with the easy option 
```
```
boog900: anything else anyone wants to discuss today?
```
```
hinto: boog900: did you see https://github.com/Cuprate/cuprate/issues/431?
```
```
hinto: worth noting it happened only once and hasn't happened since
```
```
boog900: > DEBUG net{zone="ClearNet"}:connection{addr=REDACTED}: Connection task shutting down: inner service error: Transaction error: Key-image is already spent.

This line is unrelated to why the block downloader stopped, this happens when you receive a tx-pool tx that is already in a block (monerod has the same issue, I need to report it).

The block downloader stopped because you were already synced it seems.
```
```
boog900: you were synced right? 
```
```
boog900: at least your node was sending blocks which only happens once you are synced:

> DEBUG net{zone="ClearNet"}:connection{addr=REDACTED}: Sending message: [new fluffy block] to peer
```
```
hinto: hmm... I should have kept the logs
```
```
hinto: I believe it was synced
```
```
hinto: should this be ignored unless it happens again?
```
```
boog900: it didn't stop cleanly were you on v0.0.1? 
```
```
hinto: yes, this happened on v0.0.1 before switching to v0.0.2 (unrelated to the switch though, it happened independently)
```
```
boog900: hmm I thought I made it more stable in v0.0.2 but I did it in 389 for v0.0.1, so maybe you just go unlucky 
```
```
hinto: I'll keep more logs if it happens again
```
```
boog900: The issue wouldn't have effected your node, it just tried to download blocks it already had which could be because they were requested before they got sent as a new block 
```
```
boog900: anything else anyone wants to discuss today?
```
```
boog900: ok I think we can end here, thanks everyone!
```
```
hinto: thanks
```
```
boog900: !meeting 
```

# Action History
- Created by: moo900 | 2025-04-22T19:02:01+00:00
- Closed at: 2025-04-29T19:08:37+00:00
