---
title: walletnotify with bitmonero?
source_url: https://github.com/monero-project/monero/issues/161
author: domi771
assignees: []
labels:
- proposal
created_at: '2014-09-26T11:01:31+00:00'
updated_at: '2018-10-02T21:16:58+00:00'
type: issue
status: closed
closed_at: '2018-10-02T21:16:58+00:00'
---

# Original Description
I am looking to integrate Monero into our exchange. We normally communicate with the wallets over walletnotify. However I can not find this function in bitmonerod.

How can I communicate with bitmonerod from outside?

I would need to do this command:

Code:

```
    walletnotify=/usr/local/sbin/rabbitmqadmin publish routing_key=deposit.coin payload='{"txid":"%s", "channel_key":"monero"}
```

any help welcome!


# Discussion History
## muhammednagy | 2017-11-08T21:15:52+00:00
Peatio?


## muhammednagy | 2017-11-08T21:16:17+00:00
did you solve it?

## dEBRUYNE-1 | 2018-01-08T12:35:26+00:00
+proposal

## moneromooo-monero | 2018-09-03T14:33:04+00:00
https://github.com/monero-project/monero/pull/4333

## moneromooo-monero | 2018-10-02T21:11:31+00:00
Better late than never.

+resolved

# Action History
- Created by: domi771 | 2014-09-26T11:01:31+00:00
- Closed at: 2018-10-02T21:16:58+00:00
