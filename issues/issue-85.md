---
title: Move terminology away from "wallet"
source_url: https://github.com/monero-project/monero/issues/85
author: fluffypony
assignees: []
labels: []
created_at: '2014-08-03T22:15:48+00:00'
updated_at: '2021-11-13T20:12:34+00:00'
type: issue
status: closed
closed_at: '2021-11-13T20:12:34+00:00'
---

# Original Description
It's been suggested that "wallet" is a poor description for laymen, and may hinder adoption. It's also arguably sexist - men have wallets, women have purses, and whilst "moneybag" is genderless it's probably the wrong term;) Whilst Monero is quite far from a point where this terminology becomes an issue, it's the sort of change that we can make sooner rather than later.

A suggested term is "account". Whilst there might be this knee-jerk reaction from advocates of cryptocurrency that feel the term implies centralisation, I find it advantageous for several reasons:
1. It fits in with the whole "be your own bank" vibe, which is a good way to explain cryptocurrency in general to people
2. The idea of separation of accounts is already familiar to people - a married couple may have a joint account, a company will have an account (or accounts), a savings account would be separate, etc.
3. People are familiar and happy with paying a fee for moving funds between accounts, so it won't be weird for them
4. It's the most familiar path for the general public. They understand creating an account, using a strong password, password recovery, etc. It's a natural transition for them.

Discuss.


# Discussion History
## Jojatekok | 2014-08-03T23:50:27+00:00
And that's why I'm here. You, the core developers think even about the littlest parts which could matter, and considering these factors really do make sense.

Although, I'm not sure whether the term "account" is suitable, as - mentioned before - Monero could act anonymously (like fiat), and may also be transparent, (like **bank** accounts). The suggestion of yours may be misleading for new users who are familiar with the banking system.

But to be honest, that seems to be still the best alternative...


## davidlatapie | 2014-08-04T00:16:05+00:00
Presently, this goes like this:
- piece of software: _wallet_ ("download wallet", "GUI wallet")
- the most important file: _wallet.dat_ (or wallet.bin for monero)
- the "IBAN": _address_

Proposal:
- piece of software: _Monero_ (yeah, just that). The multiple account version (like what HBN has) would be _Monero Account Manager_ => "download Monero", "GUI version").
- the most important file: _wallet.bin_
- the "IBAN": _address_


## sammy007 | 2014-08-04T03:59:12+00:00
wallet.bin is not important, *.keys is important.


## dawiepoolman | 2014-08-04T06:30:23+00:00
There are unfortunate ambiguities (e.g. the term 'wallet') that got introduced by Bitcoin devs.  Andreas suggested 'Keychain' in this discussion:
https://www.youtube.com/watch?v=PdGRmshPXdo?t=2m48s

Paradigm shifts are important and sometimes we confuse people more by trying to use terms related to the legacy banking system. 

By using the word keys one can transition the laymen faster into the new crypto concepts by saying things like: "Each key unlocks access to coins associated with a public key (think of a public post box address) on the network (blockchain)"  


## fluffypony | 2014-08-04T06:44:48+00:00
@dawiepoolman Apple has already ruined that possibility with Keychain on OS X and iOS. It would have been fine - an obscure part of the OS, but with iCloud Keychain everyone has become familiar with it, as it prompts you to save website passwords to "iCloud Keychain". Remember, too, that this change is to widen the target appeal by making it more familiar to them. We're not going to have a perfectly intuitive UX at this stage, but if we have to explain concepts just for them to begin using it we're doing it wrong.

@davidlatapie @sammy007 This is a terminology change. The .bin file is less commonly named wallet.bin, mostly everyone is already giving their "wallet name" something more relevant (such as main.bin or whatever).

To be clear, this would mean everyone using Monero starts using the term "account" instead of "wallet". You have an address attached to your account. When you start using Monero for the first time you create an account. You have a 24 word mnemonic that you use to recover your account if your computer crashes or you forget your password. You can have a savings account, a transaction account, and so on. simplewallet would become simpleaccount, and rpcwallet would become rpcaccount. Command-line arguments such as --generate-new-wallet would become --generate-new-account.


## Jojatekok | 2014-08-04T16:05:41+00:00
Okay, "account" seems to be a viable alternative to me as you have described above. :)


## fluffypony | 2014-08-10T10:11:33+00:00
I think this change should be made in the next tagged release (which will be mingw64 + daemonize, blockchain DB will not be ready for the next tagged release).


## davidlatapie | 2015-03-04T01:59:38+00:00
> simplewallet would become simpleaccount, and rpcwallet would become rpcaccount. Command-line arguments such as --generate-new-wallet would become --generate-new-account.
> If this is for real, I suggest we do it as soon as possible (as we did when transitionning from MRO to XMR)


## Jojatekok | 2015-03-04T15:02:29+00:00
@davidlatapie :+1:

I keep enforcing the use of the new terminology in my GUI client.


## anonimal | 2017-08-22T21:02:28+00:00
- Women have wallets in their purse(s)
- Accounts imply sign-ups (of which we don't do)
- Accounts are usually targeted or "hacked" while wallets are usually lost or misplaced
- Accounts imply a client/server model (wallet -> daemon) - but who creates an account with their self for their self?...

## Gingeropolous | 2017-11-03T03:08:19+00:00
so it seems even when we had the chance to change the name, we stuck with monero-wallet-cli .

Is this issue dead? Or are we gonna continue to try and shift the name? Especially with the new subaddress schema, whatever we're calling that. 

## rusticbison | 2017-11-03T09:07:50+00:00
There is already a lot of inertia (dare I say consensus) with the term "wallet" in the cryptocurrency world, and I suggest we stick with this convention. Even though it really is a misnomer, and I think is misleading, I don't see how we gain anything by changing terminology. We would only further alienate newcomers. 

## 420Lord | 2017-11-17T14:25:46+00:00
I feel that it is useless to change terminology which is otherwise fine

## ghost | 2019-07-02T23:29:20+00:00
> Is this issue dead?

yes.

## elibroftw | 2021-11-13T20:04:48+00:00
Can this issue be closed then? First, this issue is subjective (wallet is not sexist but saying that no women carries a wallet is sexist). Secondly, this is software! Any solution will be semantic,  resulting in possible backwards incompatibility and inconsistency. This would further confuse people and lead to more issues being created without even adding any features! 

## selsta | 2021-11-13T20:12:34+00:00
Closing due to inactivity and "account" has a different meaning now with subaddresses.

# Action History
- Created by: fluffypony | 2014-08-03T22:15:48+00:00
- Closed at: 2021-11-13T20:12:34+00:00
