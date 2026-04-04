---
title: Monero seed "encryption" is vulnerable to known-plaintext key recovery
source_url: https://github.com/monero-project/monero/issues/4104
author: fireice-uk
assignees: []
labels: []
created_at: '2018-07-06T18:28:21+00:00'
updated_at: '2018-07-12T22:17:01+00:00'
type: issue
status: closed
closed_at: '2018-07-12T22:17:01+00:00'
---

# Original Description
https://github.com/ryo-currency/ryo-writeups/blob/master/monero-seed-encryption.md

I know we are all having a fairly busy week, but I brought forward the publication date for that since it would be a fairly dick move to let you do a release and publish that in a few days.

# Discussion History
## anonimal | 2018-07-06T19:41:59+00:00
> since it would be a fairly dick move to let you do a release and publish that in a few days

The only dick move is this [incredibly weak claim](https://github.com/ryo-currency/ryo-writeups/blob/master/monero-seed-encryption.md#why-not-report-it-though-moneros-vrp-or-hackerone) for which everyone can read and see that you're mentally unstable.

>I don't consider the money to be worth the aggro

Bounty is optional. Bounty has nothing to do with responsible disclosure. Try actually reading the [VRP](https://github.com/monero-project/meta/blob/master/VULNERABILITY_RESPONSE_PROCESS.md).

[8/9 people haven't complained about bounty](https://hackerone.com/monero/hacktivity?sort_type=latest_disclosable_activity_at&filter=type%3Aall%20to%3Amonero&page=1&range=forever), so the excuse you're giving is a very poor one (literally).

## fireice-uk | 2018-07-06T19:44:50+00:00
> The only dick move is this incredibly weak claim for which everyone can read and see that you're mentally unstable.

Yup, that's pretty much the response I have been expecting.

## cryptochangements34 | 2018-07-06T21:20:07+00:00
Insults aside, this seems like something that should be addressed but isn't particularly high priority as this is only useful if the attacker has the encrypted key and some extra information about the target's wallet. Because users are repeatedly warned to never give away the seed and keep it stored securely, regardless of whether it is encrypted or not, I seriously doubt that anybody's funds are at risk because of this.

## moneromooo-monero | 2018-07-06T21:32:09+00:00
This is technically true, but this is not supposed to be a generic encryption system. It's for seeds, and is a kind of one time pad -ish.  Using more words would defeat the purpose of an encrypted seed looking like (and being) any other valid seed.

## moneromooo-monero | 2018-07-06T21:34:39+00:00
And yeah, the insulting's not needed, but given the linked post trolls right off the bat, well...


## fireice-uk | 2018-07-06T21:35:33+00:00
@moneromooo-monero 

I agree, **this is not some kind of sky-is-falling event** (as some people on reddit are making it out to be). Most users are not using that feature, but if someone does you will let him or her down badly. 

I posted it now so that you have the opportunity to remove it (or fix if you can come up with it in that short of a time) in the upcoming point release.

## moneromooo-monero | 2018-07-06T21:44:18+00:00
Understood, thanks for the note.

## moneromooo-monero | 2018-07-07T10:37:48+00:00
I've changed the wording from "seed encryption" to "seed offset", so people can't get confused.

## moneromooo-monero | 2018-07-12T22:14:29+00:00
+resolved

# Action History
- Created by: fireice-uk | 2018-07-06T18:28:21+00:00
- Closed at: 2018-07-12T22:17:01+00:00
