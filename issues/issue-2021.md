---
title: ring_size listed as input to wallet RPC transfer method
source_url: https://github.com/monero-project/monero-site/issues/2021
author: dimalinux
assignees: []
labels:
- '📚 docs: dev guides'
created_at: '2022-08-15T01:49:23+00:00'
updated_at: '2022-12-01T07:14:24+00:00'
type: issue
status: closed
closed_at: '2022-12-01T07:14:24+00:00'
---

# Original Description
I thought the `ring_size` in Monero can no longer be changed.  Does it still belong as an input to `transfer` in the RPC documentation?
https://github.com/monero-project/monero-site/blame/28cfcdb38e735f5c35b83c067d8410ff4dc81ad4/resources/developer-guides/wallet-rpc.md#L659

# Discussion History
## plowsof | 2022-10-25T03:31:12+00:00
On mainnet yes, but devs are still able to perform tests on older versions of the blockchain. so perhaps just a few words to clarify this e.g. "Not adjustable on mainnet" or something to that effect 

## dimalinux | 2022-10-25T04:03:00+00:00
Instead of "not adjustable on mainnet", I think the phrase "the field is completely ignored on mainnet" would be more helpful. Seeing that description, client developers of libraries not intended for testing older versions will just omit the field entirely. Developers won't waste time trying to figure out if they need to set it to exactly 16 or if setting it to an arbitrary number like 13 will generate an error.  

## plowsof | 2022-11-10T11:45:04+00:00
moneromoo - "It is not ignored if sending pre rct outputs."


## dimalinux | 2022-11-10T23:25:42+00:00
@plowsof Did moneromoo give any advice on how the `ring_size` field should set for the standard use case of transferring Monero on the current mainnet? The `transfer` method only takes an `amount`.  You don't specify or easily know which outputs get used and if they are pre rct or not. I've just been leaving it unset or with a value of zero and it seems to be working.

## plowsof | 2022-11-10T23:47:43+00:00
I will ask, i share the same feelings, for now i'm using "(Unless dealing with pre rct outputs, this field is ignored on mainnet)."

# Action History
- Created by: dimalinux | 2022-08-15T01:49:23+00:00
- Closed at: 2022-12-01T07:14:24+00:00
