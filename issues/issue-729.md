---
title: Improve URI `monero_wallet` standard by allowing optional <txid> string
source_url: https://github.com/monero-project/meta/issues/729
author: SamsungGalaxyPlayer
assignees: []
labels: []
created_at: '2022-09-02T14:07:21+00:00'
updated_at: '2023-03-14T20:32:35+00:00'
type: issue
status: closed
closed_at: '2023-03-14T20:32:34+00:00'
---

# Original Description
Current Monero URI documentation: https://github.com/monero-project/monero/wiki/URI-Formatting#wallet-definition-scheme

There is a [Monero gift card project](https://xmr.gift) that could benefit from including txids in the URI, now that `scan_txid` is available.

# Proposal

At a minimum, a `monero_wallet` URI requires one of `seed` or `(view_key,address)`. Additional parameters are useful to enable spending ( `seed` enables spends; `view_key` without `spend_key` does not) and for efficiency purposes.

Parameter | Type | Requires | Description
-- | -- | -- | ---
`address` | String | `view_key` | Main (95-character) address.
`spend_key` | Hex String | `address`, `view_key` | Private spend key of a wallet.
`view_key` | Hex String | `address`, absence of `seed` | Private view key of a wallet. If a `view_key` is provided but a `spend_key` is not provided, then the wallet will be view-only.
`seed` | String | Absence of `view_key` | URL encoded mnemonic seed to restore a deterministic wallet.
`height` | Long | Absence of `txid` | Block height when the wallet was created or first received funds. Only one `height` may be provided.
`txid` | String | Absence of `height` | Transaction ID(s) to scan. Multiple transaction IDs can be provided if separated by a semicolon `;`.

Example 1:

```
monero_wallet:address=467iotZU5tvG26k2xdZWkJ7gwATFVhfbuV3yDoWx5jHoPwxEi4f5BuJQwkP6GpCb1sZvUVB7nbSkgEuW8NKrh9KKRRga5qz?spend_key=029c559cd7669f14e91fd835144916009f8697ab5ac5c7f7c06e1ff869c17b0b&view_key=afaf646edbff3d3bcee8efd3383ffe5d20c947040f74e1110b70ca0fbb0ef90d&txid=715d7f44aa641d562ea649d14152f10f84f5fd087caf637295b963cbcbb05a0e
```

Example 2:

```
monero_wallet:address=58Bj65FCpfpULRXyf7mmsY1vB4qiW8qQ8X99tw783rSggPjmvUcRHycaXUQfSwMVpuUj6FWDr4fNHFYyo7f1XdtsJsXAJ1Y&spend_key=75ca1b95ee9dd8bbf059da64c6750fd500731f8775389ce089d516d46108fc05&view_key=c59b3e3182d9c665d0f3a1776a28301410283ab6ff6a9bd3abc7a5bb37758f03&txid=f8477b831a028f07d5638157afc0fbf0897066b4caa29dc48f885fba79cec814;bd20081e0d1abf05b275bcc06bc7e315bc03c57870e247c82c8a45b30f4d1b34;cdbed9b4b2f56de7cce9255610d0cae702aefb36f9a4ff15698ea448f29f6188
```

Example 3:

```
monero_wallet:address=467iotZU5tvG26k2xdZWkJ7gwATFVhfbuV3yDoWx5jHoPwxEi4f5BuJQwkP6GpCb1sZvUVB7nbSkgEuW8NKrh9KKRRga5qz?seed=python%20runway%20gossip%20lymph%20hills%20karate%20ruined%20innocent%20ought%20dual%20shipped%20shipped%20sushi%20pyramid%20guys%20entrance%20obedient%20natural%20kiwi%20wobbly%20vixen%20wipeout%20template%20typist%20innocent&height=12345676
```

## Legacy and Inconsistencies

* The Monero documentation previously referred to both `mnemonic_seed` and `seed` as interchangeable. Good wallet code should accept either `seed` or `mnemonic_seed` for the `seed` parameter.
* The Monero documentation previously indicated that `address=` was not required if the address was provided directly after `monero_wallet:`. Good wallet code should account for this possibility.

# Context/Use

There is a desire to use Monero "gift cards" with a small preloaded value on them. In situations where these cards are loaded in a single transaction, wallets can easily and near-instantly scan specific txids, for then sweeping into another seed automatically.

If only a restore height is specified, then scanning can take minutes or hours.

Scanning a monero_wallet URI with specific txids signals to the wallet that the only funds in this seed are from these specific txids.

This field serves 2 purposes:

1. Specifying txids for significantly faster scanning.
2. Indicating to wallets that this seed is for single-use only, and can be discarded (swept) once scanned.

# Questions

* Should we allow multiple txids, or just 1?: Multiple ones supported with semicolon
* Should we allow specifying both a txid and block height? What use-case would this be for, and how should a wallet handle this? No, this will not be allowed in the standard.

# Changelog

* 2022-12-29: Added semicolons for multi-txid support and added notes about required components. Added section to the proposal that covers legacy and inconsistencies.
* 2023-02-21: Fix typo

# Discussion History
## plowsof | 2022-09-21T12:04:36+00:00
Some great use cases for scan_tx (insta syncing a one-time-use gift wallet with 1 input -> to be transferred to the users own wallet via magic - ideally from a trusted node)

Sidenote: theres a bit of a bug with scan_tx where duplicates can be scanned and appear in your history list as amount "0" - probably causes issues elsewhere, jberman has a PR fixing it here https://github.com/monero-project/monero/pull/8566

## plowsof | 2022-12-04T06:28:20+00:00
1 txid , or a list separated by commas is easy to work with. proof of concept here https://github.com/plowsof/redeem_gift_poc

edit* this pull request to add multiple recipients to a payment uri uses ";" so for consistency txid should also https://github.com/monero-project/monero/pull/8665

## SamsungGalaxyPlayer | 2022-12-29T19:51:23+00:00
I believe it's ready for final review now @luigi1111 

## SamsungGalaxyPlayer | 2023-02-13T15:45:05+00:00
@luigi1111 Cake Wallet is implementing the URI standard as written above, which deviates somewhat from the listed version in the wiki.

## luigi1111 | 2023-02-13T17:50:06+00:00
Should the wiki be updated? 

## plowsof | 2023-02-13T23:43:47+00:00
to get this moving along, this needs to be a pull request to the actual wiki, then it can be reviewed conveniently before merging. thanks @SamsungGalaxyPlayer for this :1st_place_medal: ( @ofrnxmr (?) pointed out that connecting to a node as --trusted-daemon reduces network usage. in my PoC i found it reduced the time to claim a gift card from 18s to around 8s~ )

## SamsungGalaxyPlayer | 2023-02-13T23:54:24+00:00
@plowsof how can I open a pull request for the wiki? I haven't done that before

## plowsof | 2023-02-14T00:03:04+00:00
@SamsungGalaxyPlayer sorry, the feature does not exist, *removes foot from mouth* will ask around what the best course of action here is 

## plowsof | 2023-02-14T00:59:50+00:00
@SamsungGalaxyPlayer a suggestion was to make a PR to https://github.com/monero-project/meta/tree/master/api (adding a file called something like uri_formatting.md inside the api folder) because we can't make PRs/review @ the wiki 

## SamsungGalaxyPlayer | 2023-02-14T17:13:12+00:00
Well Cake is going forward with the standard above. If Core wants to update the wiki page to match this, only they can edit that page as far as I understand @luigi1111 @plowsof 

## luigi1111 | 2023-02-14T17:26:20+00:00
https://github.com/monero-project/monero/wiki/URI-Formatting/_history isn't only Core, but I don't know off-hand how to do it (for non-maintainers).

## selsta | 2023-02-14T17:28:23+00:00
We locked the wiki because people would add nonsense / malicious links.

## SamsungGalaxyPlayer | 2023-03-14T20:32:34+00:00
I will re-open with changes. Our devs have advised me, and I've learned more about URIs in the process.

# Action History
- Created by: SamsungGalaxyPlayer | 2022-09-02T14:07:21+00:00
- Closed at: 2023-03-14T20:32:34+00:00
