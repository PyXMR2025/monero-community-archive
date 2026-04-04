---
title: Double the margin beneath the Address field on Receive page
source_url: https://github.com/monero-project/monero-gui/issues/254
author: ghost
assignees: []
labels:
- resolved
created_at: '2016-12-09T03:33:43+00:00'
updated_at: '2018-11-18T19:09:33+00:00'
type: issue
status: closed
closed_at: '2018-11-18T19:09:33+00:00'
---

# Original Description
I'm not sure if I should be adding an issue request one-by-one. I'm going to try and suggest these all together since they're related to the same wallet page (Receive).

~~1. **Keep Payment IDs blank by default**. The wallet auto-populating the Payment ID field means the QR code is already including a Payment ID inside of it. This is not good for most users, since 95% of them don't use Payment IDs. Newbies will be immediately confused by this. As a result, we should probably remove an auto-populated Payment ID and keep it blank as a default setting. Thankfully, a blank PaymentID restores the QR code to simply including an address. Ideally, there would be a "Clear" button to the right of the "Generate" button on the Payment ID field. This way a user who has "messed up" their QR by generating a Payment ID can click on it to restore their QR to simply having an address.
2. **Remove the "monero:" prefix** from the QR code. 95% of users won't know what it means. They just want to QR code an address that they can paste into XMR.to or some exchange. Etc.~~ Note: see @moneromooo-monero comment below
3. **Double the margin beneath the Address field**. This gives a more prominent focus to the Address field, which is what 95% of users are clicking on anyways. Ideally we should add a darker border around this box, or do some other feature that gives it more focus. Right now it looks like all the other boxes, which is not good design.
4. ~~**Move the Payment ID field above the Integrated address field**. Users can't use an integrated address without a Payment ID anyways. The dependent field should go second.~~ Fixed in #388 

# Discussion History
## moneromooo-monero | 2016-12-09T22:13:53+00:00
The monero: scheme is here to allow a QR recognition program to pass that on to a program which accepts the monero: scheme. In the future, the GUI will. This will mean that if you have a monero: URI which gives an address, payment id, and amount, then someone scanning it will see the monero GUI open and the transaction in hte URI be pre-filled, with just having to verify it and click "send". This will allow people to easily accept monero at a shop where they have a computer with a screen which a customer can see. Also, see the new tracking line on that screen, which works with this.


## sir-pinecone | 2017-03-18T21:59:16+00:00
@xmr-eric I'm going to work on **"Keep Payment IDs blank by default"**.

Another thing, I noticed that the QR code updates when an invalid payment ID is entered. What happens if someone tries to send money using a QR that contains an invalid payment ID? If that's not supported then I'm thinking we can we hide the QR and display a message when the form is in an error state. 

## ghost | 2017-03-19T04:34:21+00:00
@sir-pinecone 

"we hide the QR and display a message when the form is in an error state."

That would be great.

## erciccione | 2018-11-18T13:06:22+00:00
not meaningful anymore

+resolved

# Action History
- Created by: ghost | 2016-12-09T03:33:43+00:00
- Closed at: 2018-11-18T19:09:33+00:00
