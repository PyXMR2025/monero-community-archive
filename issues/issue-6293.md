---
title: A suggestion on how to simplify PGP/GPG signature verification for beginners
source_url: https://github.com/monero-project/monero/issues/6293
author: TheFuzzStone
assignees: []
labels: []
created_at: '2020-01-13T14:56:18+00:00'
updated_at: '2020-01-20T11:20:38+00:00'
type: issue
status: closed
closed_at: '2020-01-20T11:20:37+00:00'
---

# Original Description
We all understand the importance of verifying a PGP/GPG signature, which is followed by verifying the checksum of a certain release, so I will not keep talking about it.

Also, you understand how important it is to educate the average user about the importance of these checks. If checking of the checksum is not that difficult, then the GPG-thing is more complicated, even with the good manuals that we have:

* https://web.getmonero.org/resources/user-guides/verification-windows-beginner.html
* https://web.getmonero.org/resources/user-guides/verification-allos-advanced.html

The average user doesn't have a GPG-client installed, and he doesn't understand what it is at all. And when he sees a recommendation from the community that the GPG-signature should be checked for a new release, and he sees one of these manuals... let me put it this way, the manuals are really good, but honestly, it's not a user friendly experience. What's more, you can skip these steps, and simplify the GPG-signature verification process itself to copy-paste in the browser.

Even when the average user understands what steps he needs to take to verify a GPG-signature correctly, this is where laziness comes in. Even in our [XMR.RU](https://xmr.ru/) community, where there are a lot of technically people, and even after the CLI binary was compromised, there were messages like, "_So, has someone already checked the GPG signature? Are the hashes correct? Does it match?_"

There is a solution, and it's called: [Keybase](https://keybase.io/)
You've probably seen it before.

The thing is, if the signer has a Keybase-account, it becomes incredibly easy to check someone's GPG-signature (just in two steps), and there is no need to download the client, create yourself a GPG-key, search and import the GPG-key that created the signature, certify it, and so on. The average user just needs to:

1. Go here: https://keybase.io/verify
2. Paste a signed message and click on the "**Verify**" button

#### What I propose

As there have been some recent changes: https://web.getmonero.org/2019/12/16/technical-responsibilities-update.html

I suggest to the community members who will sign future releases (CLI, GUI, etc) to create Keybase-accounts to make it easier for average users to verify GPG signatures.

---

P.S. To make sure yourself how easy it is to verify a GPG-signature without installing the GPG-client (which you probably have), without importing my key, etc., you see a signed message below, copy it, go to https://keybase.io/verify, paste the signed message, and click "**Verify**":

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

Hello.
I'm TheFuzzStone from XMR.RU-team and this is a test signature.

Today is: 13/01/2019

-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEERDx3gnlqI2Zj2EzGL72d6KiMLLMFAl4ceAsACgkQL72d6KiM
LLPRag/+Ln5K45w1PNq02oOkyCEC/MX6zCWay0XUPDJsEGYcL89AE3zqtbl1c+eb
X9ABAN106QoV2UrRiSRk+9eEmqGsqQOZqEah4KCfuJNjMTDaipBEbWrtuUBH+h7t
j9PqPgzPbOUvs4ITjsX6VnSxCHjh4hHjn7bHS3bNqxLlYIaZfc9dEQh7mb9c9V5x
s0QHWlc09EBPJJTatBn+no/M01hiw/1uNf/W9eNFpbb8VWkoAPBFrgT8b9NBBBHZ
3rya6twx1W2IRx3x2P9iQ92+YvXIdXspB1X7y9dOct/V1Ki12EKlcrWVaeizA2w+
P/4VVXjCjaBFQf7feurqEKEoGDgh46MBpCfmRp4mrXCmFSmgzDGKCrswYqmJgyXy
T71CmYlR0dEWCuQEZWcjKNZoExuNOHUJ8n0cZ9q9nR87evYcq/Kp3dQqNC4eBJMi
EcOoJrWxRXFsaah7ipcZ9ZNxYicvhmXRHRBYLHPd3wI8LW7McvX/4a2ppuk6vQLB
NMfW1OHFJ084Y/xzn8MeCjZoT6ZXvJXi03gHIgbsLAA3Ufim2d3sRRsJM5Bm//MQ
kqgPf81Mh/f/WVpQ8I+jIVekQMxtyzvbTn/f4csejrM1RfNkhYvj6TFSzX5CX3fw
y00IIHCBXWXcMNPiXscj1ripRkB24lpE/qrnU7MHIpZkmTpUbFM=
=798k
-----END PGP SIGNATURE-----

```

# Discussion History
## selsta | 2020-01-13T15:23:37+00:00
While this is more user friendly, it shifts the trust to a website that is out of out control. This is less secure than the current method.

## TheFuzzStone | 2020-01-13T15:28:42+00:00
> While this is more user friendly, it shifts the trust to a website that is out of out control.

According to your logic, no PGP/GPG server can be trusted, although everyone uses it.
Everyone means people who use PGP/GPG at all.

Also, no one is obligated to upload their private part of the PGP/GPG-key. 

## kerastinell | 2020-01-13T15:36:01+00:00
My problem with Keybase is that it's proprietary. In my opinion, core Monero developers shouldn't create excessive accounts on such services, it harms free/libre software ecosystem.

There is [OpenPGP.js](https://github.com/openpgpjs/openpgpjs), which can be used to verify files. All we need in this case is a free/libre _browser-based_ "offline gpg verify tool", just like the [offline Monero wallet generator](https://github.com/moneromooo-monero/monero-wallet-generator/). Being a browser app, it'll be truly cross-platform and the users won't have to install additional software. The problem is that the software doesn't exist yet.

Just my 2 cents. Apologies for my English, it's not my native language.

## TheFuzzStone | 2020-01-13T15:58:55+00:00
> My problem with Keybase is that it's proprietary.

The client is open source: https://github.com/keybase/client
The server side is proprietary, it's true. And when I was looking for information, the last thing I saw was that they didn't plan to open the code so the community could build a federation. Well, that's sad. 



## Snipa22 | 2020-01-17T01:25:30+00:00
I do happen to agree with the avoiding of centralized infrastructure, however, I've been on Keybase for awhile, and as I'm currently working on building GUI builds, it should help a bit.  I also intend on participating in Gitian builds, and the GPG key I use as lead maintainer is also the same one I've verified across the board.

This should hopefully be enough to provide at least one point of reference for the builder. :)

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA512

Hello,

I'm Alexander (Snipa) Blair, and this message is signed with my commited GPG key on the Monero Repo in MR #6253
This key is also verified to my Keybase.io identity (https://keybase.io/snipa)
This is the key that I will use for signing Monero commits to the codebase
This is also the key that I will be using to sign builds that I am part of (GUI/Gitian)

Today is 1/16/2020
Monero Block 2012854 was mined with hash e43e92ff78fd05aa870aedeae089ab8feb3a1bb353f6a6b976aebb1aa05e638e

Thanks!
-----BEGIN PGP SIGNATURE-----

iQIzBAEBCgAdFiEESHJ3qL0KIJwWtwDzxkVS2HfDJHkFAl4hDOEACgkQxkVS2HfD
JHlErxAAgmQVseUChMfm1CF+yhkOYdNyC2NahZCtc02JUbLevtjVrGtuV7xJQOQ3
PbX+SHm/aARk2RhzpMXR5UbI4rTcSMIJx5eMDCCPvHKVT2WhXP3Eey3NLRetgNsf
5lRZml9/e+xlRj3yuQvNnEv97Sc/dFJHxABFeDzIZkqR/R1r+cEGEZO1EgXv5Xnv
jl7n3JaUOnAb09rGS24uupk6r4KI/scTn/GeHZC4yll8EFZowuQq+BMZO6ofMvSx
acvZ0fELsTT1N2CeflamXdpS0iBiN9RpwKVl1ywi1zWF5R+splcAJG4qJ3AO+Bll
co11NmdtLNLGZyAHL21QWf6WvFsIx5TLWLx8T5Id5UXu4oQXvPGJGR8bBP9VaXcT
fo0xleadSBHsDfEpQ2Dn8K9mD9r8t0wSgEE7ljSB2/ynVL9/bW/Hr1WlwxL35oXK
/tsGxOaLr9wnwVpxUG/K18XiLv9XoqzKkOpvJBBJeTEYc5Fip33d/AjpXHH3M6dh
0q9RqXQ5NTs6eb9EdDOm1U2OnH6SaqN/TTqsWSvhIfljL1GIXj4T7y+r2VZF0Dc8
IhBBcVKrIAHXtAHFra0FOBa8BJCWiNooN04GJpVQkwdA8VOgF6W5tUGy8M6uxDPp
uRHdLajHrie4J+dPuJroMhf1n+hE5gvD6ttsImeJ5LwnWprWlpk=
=hx+I
-----END PGP SIGNATURE-----
```

## TheFuzzStone | 2020-01-17T08:41:57+00:00
@Snipa22, nice:

---

![2020-01-17_10-39](https://user-images.githubusercontent.com/16173361/72597166-19482680-3905-11ea-989f-b6d11a6eaf89.png)

---

Profile: https://keybase.io/snipa


## TheFuzzStone | 2020-01-20T11:20:37+00:00
It was just a suggestion.



# Action History
- Created by: TheFuzzStone | 2020-01-13T14:56:18+00:00
- Closed at: 2020-01-20T11:20:37+00:00
