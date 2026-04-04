---
title: signed binaries - trust verification
source_url: https://github.com/monero-project/monero/issues/6776
author: skironDotNet
assignees: []
labels: []
created_at: '2020-08-24T16:20:17+00:00'
updated_at: '2022-02-19T04:18:11+00:00'
type: issue
status: closed
closed_at: '2022-02-19T04:18:10+00:00'
---

# Original Description
I think any new member's key should be generated and signed by **fluffypony.asc** as trusted signature
It would be easier to trust 6 year old key. 
Now if hackers or gov got access to git repo they can upload any pgp key and sign binaries with that key, all nice and matching but how the community can be sure the whole project hasn't been corrupted recently?

gpg --verify hashes.txt
gpg: Signature made Thu 13 Aug 2020 11:39:27 AM CDT
gpg:                using RSA key 81AC591FE9C4B65C5806AFC3F0AF4D462A0BDF92
gpg: Good signature from "binaryFate <binaryfate@getmonero.org>" [unknown]
gpg: WARNING: **This key is not certified with a trusted signature!**
gpg:          **There is no indication that the signature belongs to the owner.**
Primary key fingerprint: 81AC 591F E9C4 B65C 5806  AFC3 F0AF 4D46 2A0B DF92

Something to think about... 
Thanks!



# Discussion History
## vtnerd | 2020-08-24T16:25:24+00:00
You are potentially asking these people to personally meet fluffypony for verification. So I'm not sure if this could be in practice.

## selsta | 2020-08-24T16:37:06+00:00
> but how the community be sure the whole project hasn't been corrupted recently?

By following the repo, checking commits and also participating in building reproducible binaries, see https://github.com/monero-project/gitian.sigs

## skironDotNet | 2020-08-25T05:36:17+00:00
@vtnerd I think it's possible to sign a key using his pub key, so he is not needed, but maybe I'm wrong maybe his priv key is needed, in such a case maybe emailing him about new members and signing for new members, maybe he would do... 

## moneromooo-monero | 2020-08-25T11:32:29+00:00
The commits adding the keys are signed by fluffypony's key.
Granted, it might be less secure than straight signing the key with GPG.
Still worth doing I guess if pony's up for it.

## MRXTIG | 2021-08-27T02:57:16+00:00
im a noob to xmr  been running  gui 17.1 9 succesfully, but   keep  getting messages to update , so i went to getmonero and downloaded gui 17.2.2 and went through the verification process and EVERYTHING  matches except for signing key .  my key from terminal is gpg: key 0xF0AF4D462A0BDF92 and the key from get monero is F0AF4D462A0BDF92. so its just the addition of  0x, is this  ok ,or is that a sign i have a corruped download .  again i'm only familair with the basics, meaning i know how to copy and paste code in terminal hahaha...so if this is a completly redic. question i appologize in advance. 


## selsta | 2021-08-27T02:59:21+00:00
> so its just the addition of 0x, is this ok

yes.

## MRXTIG | 2021-08-27T03:02:30+00:00
yup just  0x . awesome thanks fro the help 


## selsta | 2022-02-19T04:18:10+00:00
As moneromooo said, all commits that add a new key are signed by a maintainer. The binaries are always signed by the same key and if that would change there would be an announcement first.

Also all our builds are reproducible and every participant signs his hashes: https://github.com/monero-project/gitian.sigs

I don't think the existing keys will change, but the trusted signature is something to keep in mind for the future.

# Action History
- Created by: skironDotNet | 2020-08-24T16:20:17+00:00
- Closed at: 2022-02-19T04:18:10+00:00
