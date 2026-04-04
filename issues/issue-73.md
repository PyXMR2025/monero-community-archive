---
title: Reduce scan times with 1-byte-per-output 'view tag'
source_url: https://github.com/monero-project/research-lab/issues/73
author: UkoeHB
assignees: []
labels: []
created_at: '2020-04-14T07:51:10+00:00'
updated_at: '2022-02-04T13:23:27+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
It seems important to speed up scan times, especially with Janus (Issue #62) potentially increasing scan times, and as transaction volume has started to rise. I think we can easily reduce scanning by around 50-70% with 1 additional byte per output, call it the 'view tag’, a reduction even taking into account Janus.

The principle is simple (and has likely been suggested before), make a shared secret between the sender and receiver, hash it, then record the first 1 byte in the chain (the view tag). Recipients calculate the shared secret, hash it, and check if it matches any view tags in the tx. If it does match, then continue checking for owned outputs in the normal way. It will only match about 1/256 of the time, so scan time will be primarily a function of checking view tags.

The shared secret has to be the normal one calculated, e.g. r*K^v, since there is no easy way around the subaddress problem. The view tag hash should be domain separated from the so-called ‘derivation to scalar’ used in one-time addresses, to avoid leaking any part of it on-chain. An easy way to do this, and to more generally insert view tags into the scanning process, is to just hash the derivation to scalar a second time, then compare it to the corresponding output's view tag. If it matches, continue with the checking procedure, if not skip to the next output.

Currently, to check a normal 2-output transaction (they basically all have 1 transaction public key), it takes these EC operations: 1 scalar-mult-key (shared secret with tx pub key), 2 scalar-mult-base (derivation to scalar times G, one for each output), 2 ec subtractions (each one-time key minus the H(rKv,t)*G). See [derive_subaddress_public_key()](https://github.com/monero-project/monero/blob/master/src/crypto/crypto.cpp) and [ZtM2](https://web.getmonero.org/library/Zero-to-Monero-2-0-0.pdf) sections 4.2-4.3. Five EC operations.

With Janus, it will take: 2 scalar-mult-key (shared secrets for each tx pub key), 2 scalar-mult-base (derivation to scalar times G, one for each output), 2 ec subtractions (each one-time key minus the H(rKv,t)*G). See Issue #62. Six EC operations.

With Janus and view tag it will take (in 255/256 cases): 2 scalar-mult-key (shared secrets for each tx pub key). Two EC operations.

The average output count recently (excluding miner tx) is around 2.2 per tx, so an average 50-70% reduction in scan time per tx seems reasonable. I’d say 50% is a very conservative estimate.

My recommendation is to roll this out in a hard fork alongside Janus, and in that hard fork reorganize the transaction structure to remove a lot of stuff from the tx extra field (there has been recent discussion around this). In other words, put the Janus base key, the tx pub keys (one per output), and the view tags (one per output), in the transaction structure (and possibly the encrypted payment ID).

# Discussion History
## Mitchellpkt | 2020-04-14T17:22:57+00:00
This is a neat idea, and I don't perceive any information leaks as long as the protocol enforces view key tags on all transactions.

## SarangNoether | 2020-05-27T20:16:08+00:00
I wrote up a basic timing test on [this branch](https://github.com/SarangNoether/monero/tree/view-tag) to examine the time savings from view tags and compare to the current scan functionality.

Here's a plot showing the average scan time per output as a function of tag size, on a particular test machine:
![view-tags](https://user-images.githubusercontent.com/32460187/83067752-36200380-a035-11ea-8e03-1dfa192e3c47.png)


## UkoeHB | 2020-05-27T21:50:12+00:00
Note: 2-out tx may get a bigger reduction in scan times from view tags, since they only (in practice) have 1 tx pub key so you normally only compute `generate_key_derivation()` once, then the `if (is_owned)` stuff (from @SarangNoether's code) twice for each output. If current reduction is to 75%, then 75/(100+25) = 60%. Tx with >2 outputs are only 5% of current tx, so aren't too meaningful for this granularity of analysis.

## SarangNoether | 2020-05-27T21:53:22+00:00
To be clear, the linked code does not assume anything about transaction structure, and only examines outputs as separate discrete units with their own key derivation computations. Plot data was computed using the timing results from this code, not from any particular chain data.

## jtgrassie | 2021-10-27T02:49:04+00:00
> The principle is simple (and has likely been suggested before)

Yes, similar concepts <sup>[1](https://np.reddit.com/r/Monero/comments/dxw9ov/scheme_for_reduced_wallet_scanning_time/), [2](https://medium.com/@trustedsetup/improving-transaction-scanning-speed-2fa4c54de3ca)</sup> have been suggested before, but they harmed privacy. The difference here is that the _tag_ (or grouping) is coming from the shared secret and thus doesn't leak anything that could be used for fingerprinting AFAICT. Thus, this is a great enhancement of the general idea.

## SamsungGalaxyPlayer | 2021-10-28T20:54:54+00:00
This seems like the easiest trade ever.

## aitorpazos | 2021-10-29T12:28:55+00:00
Forgive me if this is a dumb suggestion but what about adding 2 bytes? Seems like a 1/256 vs 1/65536 is a pretty good tradeoff before going into the diminishing returns field.

## sethforprivacy | 2021-10-29T14:08:05+00:00
This is... absolutely amazing, and no idea how it's been overlooked for so long.

Would gladly donate 5XMR to anyone who can get this accepted as a PR into the Monero codebase.

## sethforprivacy | 2021-10-29T14:19:40+00:00
I've opened a bounty for the implementation of this idea as well, that anyone can freely donate to to incentivize and fund the work required here:

https://bounties.monero.social/posts/28/implement-view-tags-to-decrease-wallet-sync-times-in-monero

## UkoeHB | 2021-10-29T14:29:30+00:00
@aitorpazos At 256 bits you can at most gain 1/256 = 0.4%, which is basically meaningless.

I have a working demo of view tags in my [Seraphis PoC branch](https://github.com/UkoeHB/monero/tree/seraphis_perf).
`src/mock_tx/mock_sp_core_utils.h\cpp try_get_seraphis_nominal_spend_key()`
`tests/performance_tests/view_scan.h test_view_scan_sp`

## CakeWallet | 2021-10-29T15:16:42+00:00
Hey all.. this is awesome and we just donated 10 XMR to the bounty bringing it up to 15.2 XMR.  Lets get this one done!

UkoeHB's contributions to Monero are endless!

## CakeWallet | 2021-10-29T18:27:03+00:00
so when/how does this get done?

## sethforprivacy | 2021-10-29T19:46:35+00:00
> so when/how does this get done?

Someone jumps in and proposes the code that implements this, and we include it in the upcoming hard fork for usage!

Just need someone to step in and write the code, then people to review it before inclusion. The concept seems sound enough to implement at this point, and there are no real drawbacks.

## j-berman | 2021-10-29T21:44:15+00:00
In to take this, commented on the bounty :) Shooting for PR within ~4 weeks

## CakeWallet | 2021-10-30T01:04:20+00:00
> In to take this, commented on the bounty :) Shooting for PR within ~4 weeks

OJ coming through.

(OJ as in "other Justin") 😉



# Action History
- Created by: UkoeHB | 2020-04-14T07:51:10+00:00
