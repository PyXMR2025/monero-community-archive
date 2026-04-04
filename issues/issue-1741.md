---
title: Would like wallet to allow optional passphrase in addition to mnemonic seed
source_url: https://github.com/monero-project/monero/issues/1741
author: Engelberg
assignees: []
labels: []
created_at: '2017-02-17T23:22:48+00:00'
updated_at: '2017-09-25T19:00:25+00:00'
type: issue
status: closed
closed_at: '2017-09-25T19:00:25+00:00'
---

# Original Description
I prefer wallet software that, upon creating the wallet, allows for the entry of an optional passphrase and then the wallet recovery becomes dependent on both the mnemonic seed and the optional passphrase.

I like this because then I can write down the mnemonic seed and not worry quite as much about someone seeing it, because it doesn't do them any good without knowing the passphrase (which is something memorable to me, but not written down).

When the recovery is based only upon information which must be written down, it feels less secure.

# Discussion History
## fluffypony | 2017-02-18T07:42:16+00:00
It's doable, but we'd have to have a longer checksum at the end to validate your password, else the seed by itself is somewhat pointless (every password would generate a different wallet).

## Engelberg | 2017-02-18T08:00:36+00:00
From a security standpoint, isn't it ideal if every wrong password generates a valid wallet that simply doesn't happen to contain anything?

## fluffypony | 2017-02-18T08:11:16+00:00
@engelberg sure, as long as you're volunteering to deal with every person that gets their password wrong when restoring:-P We have to assume that many people won't remember their password or address, and so they'll have to wait for an ENTIRE restore just to check that they put the right password in.

## ghost | 2017-02-18T21:00:03+00:00
The eternal trade-off between the perfect system and a practical one

## JollyMort | 2017-03-11T11:51:51+00:00
@Engelberg fyi, there's a quite neat external tool for this: https://xmr.llcoins.net/

> In the "CN Add" method, the key is hashed with CryptoNight, then interpreted as a private key/scalar and added to the hex seed. The resulting mnemonic looks exactly the same as an unencrypted one.

Actually I rolled 1 random seed and then used a couple of passwords to generate multiple wallets. It comes with some conveniences:

- they all look the same, so there's no way to tell they can be linked with some password
- you don't have to worry about someone stealing just the seed, and you could also plant some funds to the wallet derived from the "encrypted" seed to make someone think there's nothing beyond it
- if you use the common seed to derive it all, you can keep the seed safe for backup but you can also use any of the derived wallets (with the password) to recreate the seed!

## moneromooo-monero | 2017-08-08T11:27:10+00:00
https://github.com/monero-project/monero/pull/2257 - using the same method as luigi1111's CN_Add encryption in https://xmr.llcoins.net

Every password generates a different seed, as fluffypony mentioned above. Fair point about people forgetting the password, but, you know...

## moneromooo-monero | 2017-09-25T18:45:29+00:00
+resolved

# Action History
- Created by: Engelberg | 2017-02-17T23:22:48+00:00
- Closed at: 2017-09-25T19:00:25+00:00
