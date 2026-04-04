---
title: 'Send & Receive page: educate users about Monero privacy features'
source_url: https://github.com/monero-project/monero-gui/issues/2629
author: rating89us
assignees: []
labels: []
created_at: '2019-12-18T18:06:33+00:00'
updated_at: '2020-01-22T18:32:53+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
As a Monero user that has downloaded the GUI wallet (and didn't download a multicoin wallet), I want to see how the magic is done. Even though it's really important to have a clean UI, I believe that at this moment it's even more important to educate our users about our technology. 

Giving talks and writing articles about Monero technology is nice, but it doesn't reach enough people. This could be easily done in Monero GUI when the user is sending or receiving a transaction, by displaying explanatory texts and/or animations that ilustrate in a simple way what Monero technology does under the hood.

Therefore, the Monero GUI UI/UX should educate the user about Monero privacy features:
- Private by default (use of privacy features is mandatory)
- RingCT (hidden amount)
- Ring signatures (unknown spent output)
- Stealth address (destinatary address isn't published in the blockchain)

Here are some suggestions:

**A) Send page: private by default**
- [ ] In Send page, rename the `Send` button to `Send private transaction`
- [ ] In Send page, add a checkbox `Use Monero privacy features` that is checked by default and is mandatory. If the user unchecks it, disable Send button and display an error message saying that the use of privacy features is mandatory in Monero.

![image](https://user-images.githubusercontent.com/45968869/71128211-7d26e480-21cb-11ea-85e1-0d4e1986ee0f.png)

**B) Receive page: stealth address + subaddresses**
- [ ] In Receive page, add field "Times used" or "Received transactions", which will count how many incoming transactions a single address had.
- [ ] Detect when an address is reused for the first time, and display a warning pop up: `Address reuse detected! Since your Public Monero addresses are never published in the blockchain, you can safely reuse them to receive multiple payments. However, if you want to prevent the payer(s) from linking your payouts together, you should generate a new subaddress for each payout.` Add option to not warn again about address reuse.

**C) Send page: creating/sending transaction pop up**
- [ ] In Send page, after clicking send button, display a `Creating transaction` pop up

![animation8](https://user-images.githubusercontent.com/45968869/71194577-f9bcd000-226a-11ea-907e-97b960c932df.gif)

_1) Ring Signature_
- [ ] Display 10 outputs being selected from the blockchain
- [ ] Text: `Creating Ring Signature...`

_2) RingCT (hiding amount)_
- [ ] Display an output containing spent amount (1 XMR) turning into ? XMR
- [ ] Text: `Hiding amount...`

_3) Stealth address_
- [ ] Text: `Creating stealth address...`
- [ ] Display a new stealth address being created from the receiver's public address

_4) Transaction created / send transaction_
- [ ] Display the transaction as a ring signature of 11 outputs (? XMR) being sent to a stealth address
- [ ] Display a success message: `Your transaction was sent successfully!`
- [ ] Display a `See transaction in blockchain explorer` link

# Discussion History
## erciccione | 2019-12-19T09:59:23+00:00
I strongly disagree with this proposal.
The goal of the GUI development shoould be to make the wallet as easy as possible, since it's mostly used by non-technical people. Adding complex technical information means going in the opposit way, expecially if we consider that the community is asking loudly to semplify the terminology and the tools we produce.

The average user don't care to see how Monero works under the hood, they just want to make their transactions and that action must be as smooth and straightforward as possible. There are better places where the users can go to educate themselves.

## selsta | 2019-12-20T01:30:49+00:00
Interesting idea but yep, agree with @erciccione, the GUI is not the right place to educate the user.

## xiphon | 2019-12-20T01:44:32+00:00
I like the idea of having some animation on "Creating transaction..." splash screen.
Would support using some good-looking animated GIF there.

## selsta | 2019-12-20T01:45:15+00:00
> Would support using some good-looking animated GIF there.

If someone wants to spend some time, QML supports nice animations too :)

## xiphon | 2019-12-20T01:45:38+00:00
> If someone wants to spend some time, QML supports nice animations too :)

Won't support this.

## selsta | 2019-12-20T01:46:23+00:00
Why? Performance?

## xiphon | 2019-12-20T01:47:51+00:00
> Why? Performance?

The main concern is unnecessary code bloating.

## SamsungGalaxyPlayer | 2019-12-20T18:17:54+00:00
> In Send page, rename the Send button to Send private transaction

Support

> In Send page, add a checkbox Use Monero privacy features that is checked by default and is mandatory. If the user unchecks it, disable Send button and display an error message saying that the use of privacy features is mandatory in Monero.

Do ***not*** support.

> In Receive page, add field "Times used" or "Received transactions", which will count how many incoming transactions a single address had.

I would spin this off as a separate issue. Open to its inclusion if there's a desire for the feature.

> Add explanatory Text: Since your Public Monero addresses are never published in the blockchain, you can safely reuse them to receive multiple payments. However, if you want to prevent the payer(s) from linking your payouts together, you should generate a new subaddress for each payout.

Do ***not*** support for now at least.

> In Send page, after clicking send button, display a Creating transaction pop up

Support the idea. Some gif that shows how a Monero transaction is created in a simplified way is neat. However, there are many nuances including multiple rings from multiple inputs and multiple outputs. Something really basic showing that rings are created and stealth addresses are generated, without specifics, would be cool. Example could be a gif of the ring being constructed and then sent to a generated stealth address.

> Display a See transaction in blockchain explorer link (with the transaction successful screen)

Support.

## GBKS | 2020-01-20T16:22:56+00:00
I really don't think the send flow is the place for this. Even changing the label to "Send private transaction" implies that there is a way to send non-private transactions. This effort would be much more beneficial on getmonero.org where a wider audience can see it. The one thing I've could see work out well would be small 'Learn more' links or question mark icons that link out to the guide for more info. Otherwise I would keep the transactional screens focused on the task at hand.

I brought up the option to add a link to an explorer a long time ago and it was not rejected because this would give preference to a specific website/project, which could be a potential attack vector and also would not be in the spirit of the community. It could be an option to create an interface to add information about an explorer you like (via a URL pattern maybe), but that would have to be discussed. Not sure if more conversation has happened on this, but there's definitely more to consider.

## SamsungGalaxyPlayer | 2020-01-22T18:32:52+00:00
I see the option of "Send Private Transaction" as assurance for the user, not further complication.

# Action History
- Created by: rating89us | 2019-12-18T18:06:33+00:00
