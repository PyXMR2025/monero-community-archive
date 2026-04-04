---
title: When sending to integrated address via cold signing, confirmation shows normal
  address + paymentID
source_url: https://github.com/monero-project/monero/issues/2221
author: medusadigital
assignees: []
labels: []
created_at: '2017-07-29T12:53:13+00:00'
updated_at: '2017-08-07T18:18:17+00:00'
type: issue
status: closed
closed_at: '2017-08-07T18:18:17+00:00'
---

# Original Description
When sending to integrated address via cold signing functionallity, the confirmation (after signing) is very confusing. It splits the integrated address into normal address + paymentId.

to verify the address is still correct, the User will need to decode the integrated address into normal address + paymentId himself, and compare with the confirmation message.

the desired way would be to show the original integrated address inside the confirmation.

This affects CLI and GUI wallet in the same way

# Discussion History
## moneromooo-monero | 2017-07-29T20:38:41+00:00
That'd a bit annoying since the payment id is encrypted already, so not known at that time. It'll need passing unencrypted address manually.

## moneromooo-monero | 2017-08-07T18:15:32+00:00
+resolved

# Action History
- Created by: medusadigital | 2017-07-29T12:53:13+00:00
- Closed at: 2017-08-07T18:18:17+00:00
