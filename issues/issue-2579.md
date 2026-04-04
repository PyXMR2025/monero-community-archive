---
title: Merchant page redesign
source_url: https://github.com/monero-project/monero-gui/issues/2579
author: rating89us
assignees: []
labels: []
created_at: '2019-12-09T03:56:36+00:00'
updated_at: '2020-09-14T18:21:13+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
**Merchant page:**
- Make page smaller (fits smaller screen sizes) (see #2472 and #2569)
- Remove instructions to merchant (display only when opening for the first time)
- Top menu to select `Sales` and `Request payment` 
- Ask for password when exiting Merchant page (Merchant wallet usually is in a public place, and merchant doesn't want anyone snooping on it).

**Request payment page:**
- Remove selected address: it incentivizes address reuse, which has a risk of off-chain linking
- Add selected account. The merchant should only select an account to receive. A new address should be created in this account every time a payment arrives.
- Redirect back to merchant page when changing account or address (see #2571)
- Add fiat amount field
- Add fiat conversion / price
- Add fiat price source
- Add description field (optional)
![image](https://user-images.githubusercontent.com/45968869/83126243-d8dd8e00-a0d8-11ea-91ef-f46c5124234e.png)

**Awaiting payment page:**
- QR code with Monero logo
- Resizing the window should resize QR code
- Don't display Monero address to buyer
- Remove `right-click, save as` subtitle from QR code
- Add animated GIF (loading...) for awaiting payment
- Display confirmation for buyer when asked amount is received
![Awaiting2](https://user-images.githubusercontent.com/45968869/70458996-920cc500-1ab3-11ea-8d92-bdf92da9e8c8.gif)

**Sales page:**
- List all sales done using Merchant page
- Fields: Amount (XMR), Amount (USD), Date and Time, Description, Status (Paid/Canceled)
- Sort by Date, Amount, Description, Status
![image](https://user-images.githubusercontent.com/45968869/70436160-f23a4180-1a88-11ea-8198-7c85f51949d2.png)

**Currently:**
![image](https://user-images.githubusercontent.com/45968869/70404743-44547600-1a3b-11ea-9495-ff50cf710788.png)

# Discussion History
## garlicgambit | 2020-09-14T18:21:13+00:00
Looks nice.

# Action History
- Created by: rating89us | 2019-12-09T03:56:36+00:00
