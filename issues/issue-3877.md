---
title: Ledger Nano S Plus support
source_url: https://github.com/monero-project/monero-gui/issues/3877
author: AdamSiddique
assignees: []
labels: []
created_at: '2022-04-02T22:33:50+00:00'
updated_at: '2022-05-10T07:29:47+00:00'
type: issue
status: closed
closed_at: '2022-04-27T04:47:26+00:00'
---

# Original Description
The Ledger Nano S Plus does have a Monero Application but is not yet supported by the Monero GUI wallet, choosing the other Ledger wallets results in the device not being detected.

# Discussion History
## selsta | 2022-04-02T22:36:20+00:00
Support for it will be added once we release the next CLI / GUI release.

## AdamSiddique | 2022-04-02T22:38:05+00:00
Nice! Thanks for the quick response.

## mrusme | 2022-04-21T18:39:30+00:00
@selsta I was trying to find the related ticket for that but couldn't. Would you mind linking it? I would like to subscribe to that to get notified when this happened. Thank you!

## selsta | 2022-04-21T18:45:01+00:00
@mrusme do you mean https://github.com/monero-project/monero/pull/8239 ?

## mrusme | 2022-04-21T18:50:16+00:00
@selsta thank you, yes!

## FreddieChopin | 2022-04-21T19:25:19+00:00
So the big question remains - is there maybe some rough release schedule? (;

## selsta | 2022-04-21T21:21:32+00:00
hopefully sometime in the next days

## selsta | 2022-04-29T20:32:19+00:00
https://www.getmonero.org/2022/04/29/monero-GUI-0.17.3.2-released.html

I don't have a Ledger Nano S Plus, so I wasn't able to test it myself but we whitelisted the hardware identifier.

Inside the GUI you will have to select the regular Ledger Nano S device, I didn't add a separate entry for Ledger Nano S Plus yet.

## pchristod | 2022-04-30T09:08:52+00:00
I can give quick feedback about this and tell you that it works.
Thanks for the addition!

## jonathancross | 2022-05-09T14:52:39+00:00
@pchristod Can you please confirm?

## jonathancross | 2022-05-09T14:53:27+00:00
@AdamSiddique @FreddieChopin  Have you had a chance to test?

## selsta | 2022-05-09T14:54:06+00:00
@jonathancross confirm what? multiple people got it working

## FreddieChopin | 2022-05-09T15:13:06+00:00
New release works fine with Ledger Nano S Plus.

## jonathancross | 2022-05-10T07:29:47+00:00
> @jonathancross confirm what? multiple people got it working

I just thought it was good to loop back around to the people who had issues.

I now see all the things you've done to help fix problems and answer questions. Thanks @selsta 

# Action History
- Created by: AdamSiddique | 2022-04-02T22:33:50+00:00
- Closed at: 2022-04-27T04:47:26+00:00
