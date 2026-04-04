---
title: Merchant page is not using the selected address but the primary address
source_url: https://github.com/monero-project/monero-gui/issues/3036
author: dalecooper
assignees: []
labels: []
created_at: '2020-08-05T20:14:09+00:00'
updated_at: '2021-04-22T05:58:10+00:00'
type: issue
status: closed
closed_at: '2021-04-22T05:58:10+00:00'
---

# Original Description
When using the merchant page to generate a QR code with the amount, the "Currently selected address" is OK (it's the label of the sub address that I've selected in the receive page), but the address in the payment URL is always the primary address.
The QR code is also using the primary address.

# Discussion History
## garlicgambit | 2020-09-01T18:19:06+00:00
It will use the primary address of the account that you've selected. If you need to use the merchant page and need a different (sub)address you can create a new account. But it is a cumbersome workaround.

## zzaappedd | 2021-02-05T18:38:52+00:00
so why the option to change in the merchant page if the change won't apply to the merchant page?

# Action History
- Created by: dalecooper | 2020-08-05T20:14:09+00:00
- Closed at: 2021-04-22T05:58:10+00:00
