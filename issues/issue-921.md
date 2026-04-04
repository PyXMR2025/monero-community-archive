---
title: '[Enhancement] Stealth Wallets'
source_url: https://github.com/monero-project/monero/issues/921
author: needmoney90
assignees: []
labels:
- enhancement
created_at: '2016-07-21T17:27:57+00:00'
updated_at: '2017-09-25T19:06:23+00:00'
type: issue
status: closed
closed_at: '2017-09-25T19:06:23+00:00'
---

# Original Description
I've considered (starting) implementing a Trezor-style wallet scheme for simplewallet, where your actual privkey is derived from both the privkey in your wallet and the password you enter when loading it. This would allow for plausible deniability with regards to how much funds are actually contained within your wallet, as multiple different passwords can potentially lead to multiple different accounts. 

The caveat here is that you would need to rescan the blockchain whenever you load a stealth account, because any remnants on-disk of your stealth accounts would inform an adversary of their existence (and quite possibly their quantity). I don't think this is much of a problem though, as someone using stealth accounts could very easily use the base wallet for a hot wallet, and occasionally top it off from one of their stealth (cold) accounts. 


# Discussion History
## needmoney90 | 2016-07-21T17:42:06+00:00
As far as storing the wallet's historical transactions on-disk such that the blockchain wouldn't need to be rescanned, and the user _also_ has plausible deniability:  I have a few ideas on how we could do it, but it would be complicated. In effect, there would be a single fixed-size file on disk, where the size is chosen by the user, and a larger size means more plausible deniability. 

For each password, the file would store the block heights containing your historical transactions, as well as the last height that your wallet synced.  Then, an encryption scheme is performed such that when each password is used individually, the history file is decrypted to display only the history related to that password, where the rest is junk data. Truecrypt uses this style of encryption with their 'Hidden Volumes', so I know that it's not impossible to do. If someone with a better grasp on the cryptography involved could tell me whether this is possible for an arbitrary number of stealth wallets, I would appreciate your insight here.


## expez | 2016-07-21T19:20:11+00:00
If they know someone has sent you money using `$address` will this pass the test of sending a token amount to `$address` and seeing if it really shows up in the (fake) wallet you're claming is the real one?


## needmoney90 | 2016-07-21T19:27:09+00:00
It will not. If someone can associate a public address with you (say a withdrawal from an exchange on which your identity is verified), and then later, you're asked to prove that the address you withdrew to is derived from your (fake) wallet, you would be unable to provide that proof without revealing your stealth wallet. If you want plausible deniability, you would need to use your (fake) wallet as the intermediary, and transfer the funds from there to their final destination in the stealth wallet. So long as there isn't proof that the address you sent to is one under your control, plausible deniability is retained. Withdrawing slowly over time as opposed to a lump sum could also add more plausible deniability.


## ChristopherKing42 | 2016-08-04T03:37:36+00:00
This technically can be done at the file system level, I believe. Run True crypt, give each wallet a different hidden volume. The only question is if monero integration could make it more efficient (store the block chain once, and each hidden volume stores where in the block chain it's funds are).


## moneromooo-monero | 2017-08-09T11:04:59+00:00
A similar thing: https://github.com/monero-project/monero/pull/2257

## JollyMort | 2017-08-26T23:54:07+00:00
>The caveat here is that you would need to rescan the blockchain whenever you load a stealth account

You can address that: if you do sweep_all to yourself and remember the height, you don't need to scan from scratch, but just from that height. You will not see the history, but what do you care - you got all your money in the last TX =)

## moneromooo-monero | 2017-09-25T18:48:13+00:00
+resolved

# Action History
- Created by: needmoney90 | 2016-07-21T17:27:57+00:00
- Closed at: 2017-09-25T19:06:23+00:00
