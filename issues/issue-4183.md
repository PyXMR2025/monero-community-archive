---
title: 'Idea: 4 factor authentication for Monero Wallet'
source_url: https://github.com/monero-project/monero/issues/4183
author: ChristopherKing42
assignees: []
labels: []
created_at: '2018-07-27T15:20:29+00:00'
updated_at: '2018-08-27T13:02:16+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
For users who want additional security (but don't care to buy a hardware wallet), I suggest adding 4 factor authentication (or 2 or 3 factor by taking a subset of the factors). The four factors would be

1. A computer
2. A smart phone
3. A password
4. One (or more) usb thumb drives

How would this work?

First, generate a random seed. This seed is written down and stored somewhere in case the user loses one of the authentication factors. This seed is then used to deterministically generate 2 of 2 multisig wallet. The first private key goes on the smartphone. The second key is encrypted by the password. Then the encrypted private key is split into two parts using a (2,2)-threshold [secret sharing scheme](https://en.wikipedia.org/wiki/Secret_sharing) (by using https://linux.die.net/man/1/ssss for example). One piece is put on the computer, and one is put on the thumbdrive. (If you are using more than one thumb drive, use a (n+1,n+1)-threshold secret sharing scheme.)

To make a transaction, the two secret sharing pieces from the computer and usb(s) are combined into the encrypted private key, which is decrypted by the password, which is used to sign the transaction. This transaction is sent to the phone, which then also signs the transaction.

Pros
- Cheap: Most users have a phone, usb, and computer already.
- Easy: If implemented correctly, most users would find it easy to use, since it only involves three easy steps to authenticate (plug in the usb, enter the password, confirm on the phone).
- Safe: The seed written down in the beginning can be used to recover the funds if one of the authentication methods are lost.
- Resistant against an evil maid attack made on one device.

Cons
- Requires designing a mobile app. (This con can be mitigated by eliminating the mobile phone from the set up, making this a 3FA. This may not be desirable due to the next con though.)
- If the computer is tampered with (instead of stolen), an adversary could steal the password and usb secret (but would *not* compromise the phone).

What do you think, is 4 factor authentication worth it?

# Discussion History
## moneromooo-monero | 2018-07-27T16:05:55+00:00
One thing I was thinking of doing was to hunt down how to use a TPM and store an encryption key there, which could decrypt the monero-wallet-cli key. SSS has also on my list for years (though that was for seed storage I wanted to do that). I suppose one might make a setup where these things are optional when creating a wallet. It is kinda niche though, but if someone does (some of) it and it doesn't rewrite loads of code, then why not.

## jonathancross | 2018-08-27T13:02:16+00:00
> though that was for seed storage I wanted to do that

I looked into using [ssss](http://point-at-infinity.org/ssss/) for a Monero seed, unfortunatly it only supports up to 128 ASCII characters.
For any secret larger than that, one must encrypt the secret with a block cipher (using openssl, gpg, etc) and apply secret sharing to just the key.

# Action History
- Created by: ChristopherKing42 | 2018-07-27T15:20:29+00:00
