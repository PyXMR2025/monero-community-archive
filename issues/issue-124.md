---
title: How monero works
source_url: https://github.com/monero-project/research-lab/issues/124
author: epoberezkin
assignees: []
labels: []
created_at: '2024-07-10T18:28:40+00:00'
updated_at: '2024-10-22T19:03:17+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Thanks a lot for your work!

I would really appreciate if you can help me understand how Monero works.

I am reading the [the CryptoNote whitepaper](https://www.getmonero.org/resources/research-lab/pubs/whitepaper_annotated.pdf), together with [the comments by Surae Noether](https://www.getmonero.org/resources/research-lab/pubs/whitepaper_review.pdf) (although the link to that document says Brandon Goodell's review [here](https://www.getmonero.org/resources/research-lab/), so not sure which is that - is there maybe another review?

Using the ring signature under the certain assumptions does provide anonymity of the sender, similar to what coinjoin transactions achieve on Bitcoin, but without the need to coordinate these transactions. What I am unable to understand is what provides the cryptographic proof of ownership of the asset at a given one-time address to the recipient of the funds (and to any subsequent recipients) - I don't see a construction here that serves as a proof equivalent to a Bitcoin chain of hashes and provide the chain of custody of a given asset.

My understanding is that the one-time address is somehow constructed from fixed recepient_key and random sender's key (using a DH construction - is it correct?).

So when an owner of the money at this address wants to send them, s/he would sign the transaction using the private key that participated in the one-time address above (the old recipient_key) together with ad-hoc group of signatures of some other random recipients seen on the blockchain and include in this transaction the source one-time address and the destination one-time addresses (the new one-time address and the change address).

I do not understand what algorithm is used to confirm that the old recipient key that is used to sign the new transaction is also the key that participated in the construction of one time address, because you cannot recover the original recipient public key from one time address.

Thank you very much - I would really appreciate any clarifications.

# Discussion History
## UkoeHB | 2024-07-10T18:44:31+00:00
@epoberezkin Zero to Monero 2nd edition is a little out of date, but still at least 95% relevant https://web.getmonero.org/library/Zero-to-Monero-2-0-0.pdf .

## jeffro256 | 2024-10-22T19:03:15+00:00
> I do not understand what algorithm is used to confirm that the old recipient key that is used to sign the new transaction is also the key that participated in the construction of one time address, because you cannot recover the original recipient public key from one time address.

This part is guaranteed by the hardness of the discrete log problem. An onetime address on-chain is constructed as `O = B + v G`, where `B` is the "spend pubkey" in the address, `v` is some secret scalar known to both the sender and the receiver, and `G` is a public generator. To spend any transaction output `O`, one needs to know `x` such that `O = x G`. For general external observers, this is hard because of the discrete log problem. However, the sender knows `O = B + v G`. In this case, `x = b + v` where `b` is the private key of the address spend pubkey. Thus to find `x` and spend `O`, the sender would need to know `b`. However, only the recipient knows private key `b` of the address spend pubkey `B = b G`. 

# Action History
- Created by: epoberezkin | 2024-07-10T18:28:40+00:00
