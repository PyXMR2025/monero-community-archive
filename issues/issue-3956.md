---
title: '[Feature request] Handling barcodes'
source_url: https://github.com/monero-project/monero-gui/issues/3956
author: DorKeinath
assignees: []
labels: []
created_at: '2022-06-28T21:06:17+00:00'
updated_at: '2023-01-17T05:17:15+00:00'
type: issue
status: closed
closed_at: '2023-01-17T05:17:15+00:00'
---

# Original Description
For in-person point of sales it could be nice to have another option in the "Payment request"-Tap or in "merchant mode".: the possibility to scan a barcode. 
After taking a picture of the barcode the amount of the product an its description is filled in automatically and a payment request respectively a qr-code is generated.
Certainly this needs an option to gather and edit barcodes an its related data (price, description). (For the description it's possible to get data on the web.)

# Discussion History
## selsta | 2022-06-28T21:19:23+00:00
I don't really understand this feature request, can you explain it in more detail? In general I don't think it's likely that we will add any barcode functionality, that would be better suited for a more point of sale oriented program.

## DorKeinath | 2022-06-29T22:04:42+00:00
Accurate, I would like to see this wallet in point of sales. There is not yet a wallet nor a program that is convenient for a point of sale because it's cumbersome to track which products are sold and to type in the price. Handling barcodes is everything that's missing.
Finally it would be great, to scan all products my customer wants to buy and the prices are summarized, so that the wallet shows him the list of his products and gives him the correct payment request as QR code. 
For sure that needs a database with barcodes that can be edited. And for sure that bloats the wallet. But it would be a big step for monero if it's used in point of sales.
For the beginning it would be nice to start with scanning a single barcode and save the time to find out its price and typing in this price manually.
In the "merchant mode" is the perfect place for this options.

## plowsof | 2022-06-30T00:09:35+00:00
Realistically , barcodes are not going to contain a hard coded price , rather, some product id, to give the merchant the freedom of adjusting prices 'on the fly'. At checkout  the price of the item would be fetched from a database.  (instead of needing to remake all the barcodes)

The Monero GUI is a 'desktop wallet' first, it is not a full featured PoS system. There are certain projects which aim to perform like this such as HotShop https://hotshop.onrender.com/#/ which currently does not have scanning support but would be a nice feature (exploring NFC payments atm i believe)

Edit* The monero GUI supports 'screen grabbing' QR's , and can be compiled with support for scanning QR's using a webcam 


## selsta | 2023-01-17T05:17:15+00:00
I'll have to close this, the feature request is simply too much out of scope for monero-gui. We don't plan to build a full PoS system that supports product tracking and barcodes.

# Action History
- Created by: DorKeinath | 2022-06-28T21:06:17+00:00
- Closed at: 2023-01-17T05:17:15+00:00
