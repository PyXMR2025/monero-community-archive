---
title: Integrated PaymentId missing
source_url: https://github.com/monero-project/monero-gui/issues/181
author: medusadigital
assignees: []
labels: []
created_at: '2016-11-18T10:08:59+00:00'
updated_at: '2016-12-08T22:36:23+00:00'
type: issue
status: closed
closed_at: '2016-12-08T22:36:23+00:00'
---

# Original Description
If i send money from A to B's integrated Address, the payment ID doesnt show up in wallet A and neither in wallet B.

this seems to be GUI related only, the same test worked fine with the CLI wallet.

1.)

![integrated_broken_confirm](https://cloud.githubusercontent.com/assets/17108301/20426418/4e4e49b4-ad7f-11e6-8ee0-04f0a44667f0.png)

2.)

![integrated_broken_confirm_2](https://cloud.githubusercontent.com/assets/17108301/20426427/55fd4cfa-ad7f-11e6-85a7-9fa014c475e3.png)


3.)

![integrated_broken_confirm_3](https://cloud.githubusercontent.com/assets/17108301/20426429/5d1f8f48-ad7f-11e6-9f52-d6073a75451c.png)


# Discussion History
## dEBRUYNE-1 | 2016-11-18T13:09:11+00:00
I was able to reproduce this. 


## moneromooo-monero | 2016-11-18T19:19:34+00:00
https://github.com/monero-project/monero/pull/1356


## medusadigital | 2016-12-08T22:36:23+00:00
fixed -> closed

# Action History
- Created by: medusadigital | 2016-11-18T10:08:59+00:00
- Closed at: 2016-12-08T22:36:23+00:00
