---
title: Progress and Governance of the monero-serai Crate
source_url: https://github.com/Cuprate/cuprate/issues/192
author: kayabaNerve
assignees: []
labels:
- C-discussion
created_at: '2024-06-23T18:46:33+00:00'
updated_at: '2024-09-12T20:16:31+00:00'
type: issue
status: closed
closed_at: '2024-09-12T20:16:31+00:00'
---

# Original Description
`monero-serai` started as a wrapper around `monero`, by monero-rs, for me to implement a FROST-inspired multisig for Monero. I used C bindings to `libringct` to make the associated proofs necessary for the complete transaction. As `monero` was unwieldly, I removed it. As `libringct` and a C FFI was unwieldy, I removed it. Later, dangerousfreedom came along and expressed interest in using `monero-serai` for validating Bulletproofs (due to poor performance in Python at the time, a task they recently undertook at the Monerokon hackathon). And then Cuprate came along.

It's clear `monero-serai` is no longer just a way to make multisignature Monero transactions in Rust. It is a dependency of the ecosystem, more and more as wallets express interest and apps start being built around it. This raises the questions of how it should be maintained so that it's not just to my preference, and the necessary standards, yet amenable and accessible to everyone.

Recently, I've been working on getting monero-serai to a 1.0. This has involved:
- Smashing the crates, for better segmentation and clearer API boundaries (also in order to take the cleaning step by step)
- Fixing design issues, each fixing security concerns. Notably
  - `MlsagBulletproof` and `MlsagBulletproofCompactAmount` were made two distinct types to ensure detection of the `RctType` (previously, a panic would occur if it was indeterminable)
  - Removing `RctType::Null` with `Option<RctProofs>`, to remove some issues with operating on `Null` `Rct*`s
  - Making `Transaction` an enum (re-defining transactions from `(prefix, proofs)` to `(version, prefix, proofs)` from a theoretical standpoint)
- Trying to find an API I'm willing to commit to, and not break, with 1.0
- Documenting the code, with regards to both to the API and internally
- Various clean ups

I've mentioned the breaking changes in the Cuprate room, in order to let y'all know and ensure they're amenable. I don't expect a response until a PR attempting the full move-over is complete. I'll even personally note `Transaction` as an enum is annoying (though it does prevent some edge cases, which I do appreciate).

So not only do I want to discuss `monero-serai`'s 1.0, with a stable API, yet also the future of deciding how it's API (and internals) evolves. I'd also like to discuss testing `monero-serai`, as necessary for confidence in a 1.0 (potentially upstreaming tests from Cuprate? I'd also be fine writing an independent test suite).

I will note that with regards to the idea of handing over `monero-serai` to Cuprate (one potential option given Cuprate's position in the Monero Rust ecosystem, and Monero protocol ecosystem) is likely something I'm against. `monero-serai` will be the backbone of Serai's Monero integration, and accordingly responsible for its safety and proper happening. I am not at a position I'd trust that responsibility, and liability, to the Cuprate project. I'd also note I wouldn't offer a bug bounty over such a library (as I plan to do with `monero-serai` under Serai). Despite that, I'm not against potentially moving `monero-serai` out of Serai (if given sufficient reason), and I'm not against discussions of rules for its maintenance (wherever it's placed).

If the sane option is to simply agree on a 1.0 API and a length of time without breaking changes, barring security issues, that'd also be fine. Everything is on the table, and I look forward to discussing the best options :)

# Discussion History
## Boog900 | 2024-06-23T23:24:03+00:00
I'll start by saying how much I appreciate `monero-serai`, it really is a great crate. Initially Cuprate also used `monero-rs`, very soon in development we decide to move over to `monero-serai` instead.

Now, Cuprate (a Monero community project) relying on `monero-serai` as heavily as we are now is not ideal in my opinion. Although `monero-serai` is intended to be widely usable, its primary purpose is currently (and rightfully) Serai, this puts us in a pretty awkward position if a change was made to improve `monero-serai` for Serai but negatively impacts Cuprate's usage. 

IMO having monero-serai as a separate project, not under Serai, would be an improvement there. Having a separate repo for `monero-serai` also better shows it as a standalone product, although that may just be how I would see it.  

As for testing, this is also something Cuprate needs to improve on. I don't think we have any that just cover monero-serai, they would all be also testing Cuprate functionality so they can't be easily upstreamed. I would be happy to help to improve test coverage of monero-serai though.

For 1.0 API I'll probably have some ideas as I work on moving Cuprate over to the new API.

Regarding having `Transaction` as an enum, I think it might make sense to separate the proofs/ signatures out into an enum, and have `Transaction` be a struct of the prefix and the proofs enum? 

## kayabaNerve | 2024-06-24T09:21:55+00:00
> Although monero-serai is intended to be widely usable, its primary purpose is currently (and rightfully) Serai,

I disagree with this, especially since the new crate smashing kicks all the wallet code out. `monero-serai` proper should be a portable Monero library. Its safety standards/design policy does align with Serai, as it was built under Serai, yet I also chose those for a reason and can't object to them.

---

Handling Transaction/proofs like that doesn't work on my first pass. You either:
1) Have a prefix with a version distinct from the proofs
2) Use the proofs to determine the version, yet then can't determine the version of miner TXs without reintroducing RctType::Null which had its own issues

---

I'll also clarify, in case it wasn't clear_ the API I'm currently refining to _is_ my candidate for the 1.0 API. Further ideas/suggestions still suggested, of course :) Yet that isn't what I want to do _next_. It's what I'm doing _now_.

## hinto-janai | 2024-06-25T20:46:14+00:00
Discussed here: https://github.com/monero-project/meta/issues/1028.

## kayabaNerve | 2024-09-12T20:16:31+00:00
Resolved with https://github.com/monero-oxide/monero-oxide/pull/1.

# Action History
- Created by: kayabaNerve | 2024-06-23T18:46:33+00:00
- Closed at: 2024-09-12T20:16:31+00:00
