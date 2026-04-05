---
title: config.xmrig.com doesn't have a form field for PaymentID when adding a pool
source_url: https://github.com/xmrig/xmrig/issues/737
author: globeone
assignees: []
labels:
- question
- wontfix
created_at: '2018-08-19T22:37:38+00:00'
updated_at: '2018-09-22T06:05:07+00:00'
type: issue
status: closed
closed_at: '2018-09-22T06:05:07+00:00'
---

# Original Description
When mining directly to an exchange, many exchanges require a PaymentID
Unfortunately when setting up the config file using 
https://config.xmrig.com/xmrig/network 
There is no form field for the paymentID

I also couldn't find any instructions on how to add the PaymentID by hand to the config file.

Please add a PaymentID field to the config.xmrig.com add pools dialog.

![schermafdruk van 2018-08-20 00-35-05](https://user-images.githubusercontent.com/10052587/44313912-0039fe00-a411-11e8-8e2f-c90b4642bbe6.png)

![schermafdruk van 2018-08-20 00-36-43](https://user-images.githubusercontent.com/10052587/44313919-265f9e00-a411-11e8-87f7-fde9a7745023.png)



# Discussion History
## xmrig | 2018-08-20T09:41:11+00:00
2 types of payment ID possible:
* Old and now rare used, separated payment id, format for Hash Vault and many others pool is `WALLET_ADDRESS.PAYMENT_ID`, format depends of pool.
* Integrated payment id, in this case exchange give you single (but little longer) address.

In both cases special field for payment id not required.
Thank you.

# Action History
- Created by: globeone | 2018-08-19T22:37:38+00:00
- Closed at: 2018-09-22T06:05:07+00:00
