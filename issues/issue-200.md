---
title: Arrows in transaction history are counter-intuitive / confusing
source_url: https://github.com/monero-project/monero-gui/issues/200
author: peanutsformonkeys
assignees: []
labels:
- resolved
created_at: '2016-11-24T21:22:59+00:00'
updated_at: '2018-11-18T13:00:26+00:00'
type: issue
status: closed
closed_at: '2018-11-18T13:00:26+00:00'
---

# Original Description
Trying the [pre-beta](https://github.com/Jaqueeee/monero-core/releases/tag/pre-beta) build. Imported an existing wallet, and checked the transaction history page. The up/down arrows preceding the Amount value are counter-intuitive / confusing.

An outgoing transfer (red) is prefixed with a downward arrow (↓):

![gui-outgoing](https://cloud.githubusercontent.com/assets/21346321/20609997/db46508c-b293-11e6-947b-0bbb087eb555.png)

And an incoming transfer (green) is prefixed with a upward arrow (↑):

![gui-incoming](https://cloud.githubusercontent.com/assets/21346321/20610001/e3d8a6c8-b293-11e6-8ee5-e2503b330969.png)

As far as I know, the UI convention is to have a downward arrow for downloads or incoming stuff. So, I would reverse the current arrow directions to make it consistent with the established metaphor in other software (such as browsers). Another example: [mobile wallet mockup](https://www.gustafgarnow.com/monerowallet/) from @Baltsar. If the arrows are intended to symbolize what happens with the balance, it should simply use "-" and "+" symbols, but I think that's not the intent here.

# Discussion History
## medusadigital | 2016-11-25T06:49:03+00:00
this was allready discussed here: https://github.com/mbg033/monero-core/issues/74

## peanutsformonkeys | 2016-11-25T22:26:57+00:00
I have looked at that discussion, and still think the logic is flawed. You are mixing up the concept of balance and direction. A single example from someone's banking website also isn't a representative sample. Look at the icons in the Coinbase app, the Jaxx app, but also more broadly the "download" (receive) and "share" (send) icons in Safari, Office365, macOS, anything basically. They can't be all wrong?

Example from Coinbase (GDAX):
![gdax-app](https://cloud.githubusercontent.com/assets/21346321/20638753/3dedae70-b3b0-11e6-92e8-276d81b253dd.png)

Example from Jaxx:
![jaxx-app](https://cloud.githubusercontent.com/assets/21346321/20638758/4d25c85a-b3b0-11e6-8c2d-ae6242b1a4ea.png)


## medusadigital | 2016-11-25T23:05:50+00:00
No its not that i dont share your view or whatever, i just linked that here. 

i really dont care after all

## peronero | 2016-11-26T04:09:59+00:00
Agree with @peanutsformonkeys - it's simply standard to use up arrows for sending/uploading and down arrows for downloading/receiving. +/- works as well, and is prevalent in online/mobile banking.

Blockchain.info is another that uses up arrows for outgoing and down for incoming transactions in cryptoland.

Perhaps othe, in the referenced discussion, was referring to changes in a user balance, but it really doesn't make sense in the context of incoming/outgoing transactions.

## peanutsformonkeys | 2016-11-26T07:42:12+00:00
@medusadigital I misinterpreted your "discussed here" as "case closed". Sorry about that. Meanwhile, I added examples from GDAX and Jaxx above for clarity.

I must say that one difference I see, is that the arrows in the Monero GUI are used in the transaction **history**, while the "Receive / Deposit" and "Withdraw / Send" arrows in Jaxx / GDAX are used to indicate the **action** to be undertaken. For the latter purpose, arrows are an obvious choice to me.

In the end, I think the question really boils down to: "What is the purpose of the symbol in the Monero GUI **transaction history**?". The more I think about it, the more I'm inclined to say it's just to visualize the **change in balance**, because there's no action be undertaken anymore. If that's the case, using "+" an "-" symbols instead may be more natural, as it avoids confusion with sending moneroj.

## rlittlefield | 2017-01-17T21:42:21+00:00
Arrows should be reversed and placed over the red/green dots (helps for the colorblind). +/- should be placed where the arrows currently are.

## erciccione | 2018-11-18T12:58:56+00:00
GUI now has a new theme with different styling. Reopen if still present in new theme

+resolved



# Action History
- Created by: peanutsformonkeys | 2016-11-24T21:22:59+00:00
- Closed at: 2018-11-18T13:00:26+00:00
