---
title: '[PROPOSAL] Add optional `is_gift` and `txs` parameter and create a new gift
  standard'
source_url: https://github.com/monero-project/meta/issues/1100
author: detherminal
assignees: []
labels: []
created_at: '2024-10-29T17:27:48+00:00'
updated_at: '2025-04-05T17:42:17+00:00'
type: issue
status: closed
closed_at: '2025-04-05T17:42:16+00:00'
---

# Original Description
There is currently no easy and **safe** standard way to gift Monero to people around you. It is possible to gift a wallet containing money. However, malicious people can use this to trick people into using the wallet they gifted them and steal the money after the recipient puts in more money, so this is unacceptable.

So to make gifting people Monero much safer, I propose the `is_gift` parameter to the monero-project standard. This parameter tells software wallets that this wallet is a gift wallet and that the money in it should be transferred to a wallet that no one but the recipient can access. For example, if I receive a gift of Monero with a QR wallet and some money in it, the wallet software should create a new wallet and after scanning the URI (which should have `is_gift` in it), transfer the money to the newly created secure wallet. The parameter is completely optional and software should act like a normal (non-gift) wallet if this parameter is not in the URI.

This is not enough, because software will need the tx ids to know which txs to use, so I also propose using the `txs` parameter to tell software what txs they should use for this wallet. After scanning the URI, wallet software should look for the given tx hashes.

Example of a complete gift wallet:

`monero_wallet:42uytzD4HuEWRgqfJk9N5tfRax5Xfdqey3BqanxuorRKgR2Et2miYfMgPkch6mMC9WWqDD7hLcwhYWDcjGFYNJX6HMbU4To?spend_key=4fc14ab136971a0dcce371ef212548ea05f57afc8c0d96ccc55ffe789d123105&view_key=feb07134108bd548282239b624a172ef4d8f5e6dd8179d4cd944c4c218df3e0b&is_gift=true&txs=3c62fe4a6c17fd5daf6407d9e1ab2f78eca8f1ac8dc98e47ff8e5737e3274355,2f38e4dda63c237bfcc0461b8cea3aa6daadafa0f8e961e2916601258fe6988f`

Adding this to the standard will help users choose from a wider range of options for their wallet software instead of relying on a third-party standard.

# Discussion History
## plowsof | 2024-10-29T19:04:35+00:00
`txid` or `txids` is fine. and already proposed. (IIRC cakewallet where busy with or have implemented it?) (not actually PR'd to this repo though) no need for `is_gift`. the wallet software can decide what to do when it encounters/expects a string of `txids=...,...`.

you expect software to trust that a malicious person didn't remove 'is_gift' from their QR , in the hopes that someone restores the wallet and uses it as their own wallet? 

## detherminal | 2024-10-29T19:26:03+00:00
> `txid` or `txids` is fine. and already proposed. (IIRC cakewallet where busy with or have implemented it?) (not actually PR'd to this repo though) no need for `is_gift`. the wallet software can decide what to do when it encounters/expects a string of `txids=...,...`.

Standardization is needed. If proposed and accepted before, please add it to the [wiki](https://github.com/monero-project/monero/wiki/URI-Formatting). 

> you expect software to trust that a malicious person didn't remove 'is_gift' from their QR , in the hopes that someone restores the wallet and uses it as their own wallet?

You never trust any gift in the first part, that's why there is a gift standardization process. I didn't really understand what you mean.

## plowsof | 2025-04-05T15:50:15+00:00
this can be closed as completed after the recent changes to https://github.com/monero-project/monero/wiki/URI-Formatting

## selsta | 2025-04-05T17:42:16+00:00
Part of your proposal has been implemented, and in regards to the `is_gift` part there has not been anyone else who voiced support for it. The discussion can be reopened at a later date if there is a wallet provider who voices interest in implementing gift wallets.

# Action History
- Created by: detherminal | 2024-10-29T17:27:48+00:00
- Closed at: 2025-04-05T17:42:16+00:00
