---
title: '[Proposal] New address format'
source_url: https://github.com/monero-project/monero/issues/6674
author: tevador
assignees: []
labels: []
created_at: '2020-06-21T16:55:10+00:00'
updated_at: '2020-06-24T20:57:38+00:00'
type: issue
status: closed
closed_at: '2020-06-24T20:57:38+00:00'
---

# Original Description
Currently, standard Monero addresses are encoded in base58 as 95-character strings, e.g.
`42zDXTDfErPYQDtZGE1JejQ5TsziFp5ep45afwzmjn9hAYxHUzJ5dBZ3udPZsMaQXbRFfBzBZv4CL7CGRfu17scNKXfFtiF`

While this format works reasonably well, it has some issues:

1. The address is not "human-readable" because the prefix is a base58-encoded varint as opposed to a recognizable character sequence. For example, standard and integrated addresses are not easy to distinguish at a glance because they both start with `4` in base58 encoding.

2. It is case-sensitive, which has the following implications:
   * QR codes are larger because they have to use a binary encoding
   * Addresses cannot be used as filenames in case-insensitive filesystems.
   * Addresses are impractical for reading out loud or writing down by hand (in addition to their length).

3. The hash-based checksum doesn't protect against all common errors, e.g. changing one or a few characters in an address may still produce a valid Monero address <sup>1</sup>

<sup>1</sup> Practical example of an error that still produces a valid address (replacing `n -> x`, in bold):
<code>42zDXTDfErPYQDtZGE1JejQ5TsziFp5ep45afwzmj<b>n</b>9hAYxHUzJ5dBZ3udPZsMaQXbRFfBzBZv4CL7CGRfu17scNKXfFtiF</code>
<code>42zDXTDfErPYQDtZGE1JejQ5TsziFp5ep45afwzmj<b>x</b>9hAYxHUzJ5dBZ3udPZsMaQXbRFfBzBZv4CL7CGRfu17scNKXfFtiF
</code>

I propose a solution similar to Bitcoin's bech32 format:

1. Use a human-readable prefix for addresses, e.g. `xm1` for standard mainnet addresses, `xs1` for mainnet subaddresses and `xmp1` for mainnet integrated addresses.

2. Use base32 encoding instead of base58. This allows the address to be case-insensitive. The length of a standard address would increase slightly from 95 to 112 characters, for example (top = current, bottom = proposed):
```
42zDXTDfErPYQDtZGE1JejQ5TsziFp5ep45afwzmjn9hAYxHUzJ5dBZ3udPZsMaQXbRFfBzBZv4CL7CGRfu17scNKXfFtiF
xm10qw508d6qejxtdg4y5r3zarvary0c5xw7kv8f3t4qw508d6qejxtdg4y5r3zarvxary0c5xw7kv8f3t4w7kv8f34qw508d6qearvary0c5xw7
```
However, the size of QR codes would decrease by about 20%, which is clearly visible (left = current, right = proposed):

![QR](https://i.imgur.com/5CILlcd.png)

3. Use a checksum based on [BCH codes](https://en.wikipedia.org/wiki/BCH_code), which is more suitable for symbol-based errors and can be constructed to detect *all* 3-4 character errors without false positives.

I realize that introducing a new address format has its disadvantages (e.g. concurrent use of both formats and some user confusion), but it may be advantageous in the long run.

# Discussion History
## MoneroArbo | 2020-06-22T12:25:28+00:00
What are some use cases where hand copying the address by hand might be important? Having a hard time imagining when this would be a needed / desired feature.

The smaller QR codes are nice, though I've never had issue with the current ones.

As for the prefixes, we can already easily tell between main addresses and sub addresses, while integrated addresses I think are kind of on the way out?

## tevador | 2020-06-22T12:40:03+00:00
@MoneroArbo I personally don't think there is a compelling reason to change the address format at the moment. This proposal should be considered to be a small research study / reference in case an address format change is ever considered in the future.

Issue can be closed if needed.

## rating89us | 2020-06-23T22:38:16+00:00
I agree with your proposal. A large QR code size is something that can be problematic in devices with tiny screens, like hardware wallets and smartwatches.

Also, can't we make subaddresses have the same prefix as standard (main) addresses?

## SomaticFanatic | 2020-06-24T03:10:57+00:00
I love this. I hope we are able to make these changes on a long enough timeline including the seed upgrades as well. Implementation is going to be tricky but IMO it’ll be worth it

## tevador | 2020-06-24T11:18:02+00:00
> can't we make subaddresses have the same prefix as standard (main) addresses?

The sender needs to know that they are sending to a subaddress (the transaction public key is then calculated differently). We could make the prefixes the same, but then there would have to be a flag bit somewhere else in the address that would say it's a subaddress.

# Action History
- Created by: tevador | 2020-06-21T16:55:10+00:00
- Closed at: 2020-06-24T20:57:38+00:00
