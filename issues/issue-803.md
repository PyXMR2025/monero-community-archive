---
title: When sending to integrated address via cold signing, confirmation pop-up is
  confusing
source_url: https://github.com/monero-project/monero-gui/issues/803
author: medusadigital
assignees: []
labels: []
created_at: '2017-07-29T12:49:23+00:00'
updated_at: '2017-08-07T15:25:30+00:00'
type: issue
status: closed
closed_at: '2017-07-29T12:53:49+00:00'
---

# Original Description
When sending to integrated address via cold signing functionallity, the confirmation pop-up (after signing) inside the GUI is very confusing. It splits the integrated address into normal address + paymentId.

to verify the address is still correct, the User will need to decode the integrated address into normal address + paymentId himself, and compare with the confirmation message inside the popup. 


the desired way would be to show the original integrated address inside the confirmation pop up. 

# Discussion History
## medusadigital | 2017-07-29T12:53:49+00:00
closing in favour of https://github.com/monero-project/monero/issues/2221 , since both wallets are affected



# Action History
- Created by: medusadigital | 2017-07-29T12:49:23+00:00
- Closed at: 2017-07-29T12:53:49+00:00
