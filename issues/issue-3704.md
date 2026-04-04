---
title: defining send amount(s) in fiat
source_url: https://github.com/monero-project/monero-gui/issues/3704
author: chaserene
assignees: []
labels: []
created_at: '2021-09-18T16:58:41+00:00'
updated_at: '2021-10-25T01:43:41+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
to make the GUI wallet fit for everyday use, it would be very useful to be able to define amount(s) in a transaction in fiat.

currently if you want to send XMR that's worth a certain amount of dollars around the time of sending, the most intuitive way is to grab the current price from a website, make a calculation in a calculator, and paste the result. this is a lot of unnecessary overhead given that the wallet already has fiat display integrations.

making this possible presents some UI and app-level challenges, but I don't think these are insurmountable.

one way to enable this is to let users switch between XMR and fiat on the Send tab. currently the Amount field accepts input in XMR and the sum of the transaction is displayed in fiat (non-editable) at the bottom. 

* clicking on "XMR" next to the input field would switch to fiat input mode, where the amount you type in is interpreted in fiat and the XMR amount is computed based on the exchange rate, displayed where you previously had the fiat equivalent.
* each time the exchange rate updates in the wallet, the fiat amount would stay fixed and the XMR amount would update, up to the point where the wallet constructs the transaction data.
* clicking on the fiat currency symbol would switch back to XMR input mode.
* each time you switch modes, if the input field is not empty, the amount would be converted to the currency of the mode you enter, using the current exchange rate.
* preparing a transaction with multiple recipients could work along the same principles, with the differences that there are multiple input fields to handle and there is a summing taking place.

see some of my preliminary sketches below. input is welcome.

![](https://user-images.githubusercontent.com/64873595/133896264-77dfb521-18e8-4448-9346-3956289aaa17.png)

# Discussion History
## jarjarfan666 | 2021-10-24T08:05:05+00:00
The biggest problem with this will be the wallet having to call a 3rd party remote API to get the current exchange rates. That will degrade user privacy because it is unexpected behavior by the user.

## chaserene | 2021-10-25T01:43:41+00:00
@jarjarfan666 from my opening comment:

>  the wallet already has fiat display integrations.

it already does it if the feature is turned on in the settings. my proposal doesn't introduce any potential behavior that degrades privacy. if anything, it improves privacy, because people will be less prone to go to an online currency converter and give their IP, user agent and transaction amount to a website.

# Action History
- Created by: chaserene | 2021-09-18T16:58:41+00:00
