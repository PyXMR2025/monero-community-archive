---
title: '[Proposal] Short addresses'
source_url: https://github.com/monero-project/monero/issues/6686
author: tevador
assignees: []
labels: []
created_at: '2020-06-24T08:53:34+00:00'
updated_at: '2020-06-24T20:56:50+00:00'
type: issue
status: closed
closed_at: '2020-06-24T20:56:49+00:00'
---

# Original Description
Standard Monero addresses consist of two public keys, which makes them more than twice longer than addresses of other cryptocurrencies.

I propose to introduce a new (optional) wallet address type for users who don't need the functionality provided by view keys, i.e. they don't need to separate the ability to observe incoming transactions and the ability to spend them. The advantage is that the address length is decreased to roughly half.

## Private key

There is only a single private key `k`, which can be restored from the mnemonic seed as usual. It serves as both the view key and the spend key.

## Short address 

The public key is `K = k*G`, where `G` is the base point. The main short address is encoded as:

`NETWORK_BYTE [1 byte] || K [32 bytes] || CHECKSUM [4 bytes]`

The resulting address is 51 characters long when encoded in base58, for example (using network byte `65`):

`C31A3Jz8PtrevSfu7XRLEBK9JfKndyNKkRsdwYE8ZtL3Q51fzqy`

### Sending funds

Sending funds to a short address works the same way as sending to a standard Monero address with the public view key equal to the public spend key.

The sender will generate a random scalar `r` and calculate:

`R = r*G`

<code>P = H<sub>s</sub>(r\*K) + K</code>

Here `R` is the transaction public key, `P` is the output address and <code>H<sub>s</sub></code> is the hash-to-scalar function.

## Tagged short addresses

Unfortunately, subaddresses don't work with just one public key. To allow payment identification with short addresses, I propose a scheme that is a mix between subaddresses and integrated addresses. Let's call it the "payment tag". It has the following properties:

1. The payment tag doesn't take up any space in the transaction (it is encoded in the output key).
2. A transaction can have multiple tagged outputs (unlike encrypted payment IDs, which are limited to one per transaction).
2. Outside observers cannot tell if a transaction contains a payment tag. This is a stronger privacy property than encrypted payment IDs.
2. Different payment tags can be linked to the main short address. This is a weaker privacy property than subaddresses.

### Generating a tagged short address

To generate a tagged short address with index `i`, the wallet calculates:

<code>y<sub>i</sub> = H<sub>s</sub>("payment_tag"||i||K)</code>

<code>Y<sub>i</sub> = y<sub>i</sub>\*K</code>

Here `K` is the main public key, <code>y<sub>i</sub></code> is the payment tag and <code>Y<sub>i</sub></code> is the tagged public key.

The tagged short address is encoded as:

<code>NETWORK_BYTE [1 byte] || i [1+ bytes] || K [32 bytes] || CHECKSUM [4 bytes]</code>

`i` is encoded as a varint using 1 or more bytes. The resulting address length is 53 or more characters depending on the value of `i`. 55-character tagged addresses allow more than 2 million different payment tags.

Example of a tagged short address (using network byte `72` and `i = 42`):

`D57sz9iGuqG6LLAUwsxTiL2Qio3uZKP8XcPbn64CM4c32kz4DzdC6`

### Sending funds

To send funds to a tagged short address, the sender generates a random scalar `r` and calculates:

`R = r*G`

<code>y<sub>i</sub> = H<sub>s</sub>("payment_tag"||i||K)</code>

<code>Y<sub>i</sub> = y<sub>i</sub>\*K</code>

<code>P = H<sub>s</sub>(r*K)\*G + Y<sub>i</sub></code>

## Receiving funds

To test if a particular output `(R, P)` belongs to the short address, the wallet calculates:

<code>Z = P - H<sub>s</sub>(k*R)*G</code>

If `Z` is equal to `K` (main public key) or any <code>Y<sub>i</sub></code> (tagged public keys), the wallet can calculate the private transaction key as:

<code>p = { H<sub>s</sub>(k\*R) + k</code> (main address)

<code>p = { H<sub>s</sub>(k\*R) + H<sub>s</sub>("payment_tag"||i||K)\*k</code> (tagged address)

In order to efficiently test for tagged addresses, the wallet can store a hashtable that maps <code>Y<sub>i</sub></code> to `i` (similar implementation is currently used for subaddresses).

## Disadvantages

Short addresses have these limitations:

* Unsuitable for hardware wallets because scanning the blockchain cannot be securely delegated to another device without revealing the private key.
* Unsuitable for web wallets for the same reason.
* Tagged short addresses only provide off-chain privacy similar to integrated addresses.


# Discussion History
## fluffypony | 2020-06-24T09:05:38+00:00
Ehhhh I really don't like killing off view key functionality. If we're going to argue that organisations shouldn't shove stuff into tx_extra to satisfy travel rule requirements then we have to give them an alternative, and one of those options might be to record the view key for the deposit and/or withdrawal. I'd hate to lose that option just so we can get slightly shorter addresses that are still too long to type out or memorise.

## moneromooo-monero | 2020-06-24T10:32:56+00:00
Truncated addresses seem to do the same and have fewer drawbacks (the secret view key is derived from the public spend key).

## fluffypony | 2020-06-24T10:40:47+00:00
Oh wow that's a blast from the past, I totally forgot about truncated addresses. I guess truncated addresses are fine as long as you're not publishing them anywhere, but if we made it a standard format you can bet people will just shove that in their forum signatures, which could damage the untraceability property of Monero transactions if an attacker starts collecting those.

## tevador | 2020-06-24T10:43:08+00:00
@fluffypony 
This would be an optional format for those who don't need view keys. Organizations who need view keys could still use standard addresses (or truncated addresses).

@moneromooo-monero 
A truncated address means anyone can see your incoming payments. This format offers different tradeoffs.

## fluffypony | 2020-06-24T10:45:54+00:00
I hear you, but I fear that optional formats become the standard for ease-of-use, and a person can't always know in advance that they'll need a viewkey.

## SChernykh | 2020-06-24T10:49:27+00:00
> The advantage is that the address length is decreased to roughly half.

I don't really see address length as an advantage or disadvantage. Has anyone ever typed Bitcoin address by hand? No one is going to care as long as address is longer than 8-10 characters. If it's longer than that, it doesn't matter if it's 30 or 100 characters. It's always a "copy-paste" when sending coins to someone.

## selsta | 2020-06-24T10:51:49+00:00
Explaining a user the privacy nuances between integrated address, tagged addresses and subaddresses would be difficult. IMO we should aim for address uniformity, ideally everyone would use a subaddress.

## tevador | 2020-06-24T11:04:39+00:00
> I fear that optional formats become the standard for ease-of-use

> nuances between integrated address, tagged addresses and subaddresses

Good points. An alternative may be to promote OpenAlias (it seems that most users don't know about it), but it also comes with some hurdles.


## Wegerich | 2020-06-24T11:30:49+00:00
I really like the work that has gone into this but I fully agree with @fluffypony and @SChernykh. Firstly that the length of the address is near-meaningless unless it is being manually typed (it isn't) and secondly that increasing the number of decisions required in onboarding (will i need a viewkey in the future? what even is a viewkey?) increases the barrier required for onboarding and paradoxically to this proposal, therefore decreases overall ease of use _at the point of the greatest bottleneck._

If memorising or typing addresses was necessary then _that_ would be the biggest bottleneck and I would fully support this proposal but as it stands, this worsens the bottleneck in exchange for simplifying something that does not affect any majority use-case.

## Ryo-RU | 2020-06-24T14:14:42+00:00
We call it a KURZ address in Ryo and it could be done by taking FOSS code here: https://github.com/ryo-currency/ryo-libre/blob/6c8b7b44d82018c6572ca72b56fe42dbe10e953c/src/cryptonote_basic/cryptonote_basic_impl.cpp#L58

## tevador | 2020-06-24T20:56:49+00:00
Thank you all for your feedback.

# Action History
- Created by: tevador | 2020-06-24T08:53:34+00:00
- Closed at: 2020-06-24T20:56:49+00:00
