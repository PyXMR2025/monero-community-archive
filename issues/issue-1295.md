---
title: 'Cuprate Meeting #76 - Tuesday, 2025-11-18, UTC 18:00'
source_url: https://github.com/monero-project/meta/issues/1295
author: moo900
assignees: []
labels: []
created_at: '2025-11-11T18:43:42+00:00'
updated_at: '2025-11-18T18:40:38+00:00'
type: issue
status: closed
closed_at: '2025-11-18T18:40:38+00:00'
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

Previous meeting: #1291

# Discussion History
## moo900 | 2025-11-18T18:40:37+00:00
## Meeting logs
```
boog900: 1) greetings
```
```
hinto: hello
```
```
boog900: 2) updates 
```
```
boog900: Me: I started work on FCMP tree building, should have a system that is pretty efficient with the tapes DB. 
```
```
boog900: I plan to maintain a wip branch with changes that haven't been merged but are ready to use as I think there are going to be quite a few changes soon that are going to be big
```
```
hinto: me: I'm starting to port PoWER to Cuprate and have started with a small crate wallets/clients should be able to call easily: https://github.com/Cuprate/cuprate/pull/568
```
```
hinto: I've also been testing difficulty values for various hardware
```
```
boog900: 3) Project: What is next for Cuprate?
```
```
boog900: I don't have anything to discuss today,  I am still continuing with tree building 
```
```
boog900: hinto @hinto:monero.social: do you have anything you want to discuss? 
```
```
boog900: Something cool that I will mention with tree building is that because of the linear tapes DB we can impl rayon traits on the reader/writer and, in parallel, read from a child layer and write/calculate the hashes of the parent layer 
```
```
boog900: This should make it incredibly fast
```
```
boog900: > <@boog900:monero.social> Something cool that I will mention with tree building is that because of the linear tapes DB we can impl rayon traits on the reader/writer and, in parallel, read from a child layer and write/calculate the hashes of the parent layer 

*with no intermediate structure
```
```
hinto: Not specifically Cuprate although do you have any thoughts on the difficulty value for PoWER? The calculation is a bit different now although here are some rough numbers which should be similar: https://github.com/seraphis-migration/monero/pull/230#discussion_r2520157745
```
```
hinto: If we allow high-end hardware to take ~1 second, low-end hardware will take around 3.5s
```
```
hinto: ~0.3s and ~1s for the other way around
```
```
boog900: > <@hinto:monero.social> If we allow high-end hardware to take ~1 second, low-end hardware will take around 3.5s

Yeah I think that's expected, I would go with more PoW rather than less
```
```
boog900: Also for the difficulty scalar you should include the challenge bytes as well I think 
```
```
boog900: Otherwise you can precompute indices that pass the challenge scalar before even having the challenge 
```
```
hinto: noted, I've been looking at more complex inputs although don't want it to be a hassle for clients, although I guess it will be fine if functions are provided
```
```
hinto: every rust project owes niko for making parallelism so easy :)
```
```
hinto: (and also writing lots of rustc)
```
```
boog900: Anything else or can we end here?
```
```
boog900: I think we can end here 
```
```
boog900: Thanks hinto @hinto:monero.social
```
```
hinto: thanks
```
```
boog900: !meeting 
```

# Action History
- Created by: moo900 | 2025-11-11T18:43:42+00:00
- Closed at: 2025-11-18T18:40:38+00:00
