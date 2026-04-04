---
title: 'History :: advanced filters not working'
source_url: https://github.com/monero-project/monero-gui/issues/173
author: M5M400
assignees: []
labels:
- resolved
created_at: '2016-11-16T11:03:25+00:00'
updated_at: '2017-08-07T20:15:07+00:00'
type: issue
status: closed
closed_at: '2017-08-07T20:15:07+00:00'
---

# Original Description
master 24a66c1, ubuntu 16.04.1 LTS amd64

I have a wallet with 33 transactions (31 incoming, 2 outgoing)

opening history, everything is OK. showing all transactions, sorted by block height desc.

![filter_all](https://cloud.githubusercontent.com/assets/22886679/20344652/e1693a0c-abf3-11e6-8766-e0b1451fbe40.png)

enabling advanced filters, selecting "sent" from the dropdown and click the "filter" button

expected behavior: shows only 2 outgoing transactions
actual behavior: shows all transactions

![sent](https://cloud.githubusercontent.com/assets/22886679/20344696/0b1b8d3c-abf4-11e6-9735-dc784b16532f.png)

adding limit from 0-1 XMR to the sent filter

expected behavior: shows all outgoing transactions <= 1XMR
actual behavior: shows ALL transactions <= 1XMR

![sent_1](https://cloud.githubusercontent.com/assets/22886679/20344738/33670b7c-abf4-11e6-9a0f-d147a9132c64.png)

uncheck "advanced filtering" and clicking "filter" button

expected behavior: reset to default date-based filter, showing all 33 transactions again
actual behavior: still showing transactions <=1 XMR

![disable_filter](https://cloud.githubusercontent.com/assets/22886679/20344819/899462b0-abf4-11e6-89a6-83fec0d71321.png)

Filter resets only on app restart.


# Discussion History
## taushet | 2016-11-16T17:39:19+00:00
Confirmed 


## moneromooo-monero | 2016-11-16T21:04:49+00:00
https://github.com/monero-project/monero-core/pull/176  (should fix all/most)


## M5M400 | 2016-11-18T10:37:08+00:00
disabling advanced filters again: works
filtering sent/received: does not work

setting advanced filter to "sent" - still showing sent+received TXs

![screenshot from 2016-11-18 11-35-57](https://cloud.githubusercontent.com/assets/22886679/20427245/45d696b6-ad83-11e6-8e74-45873754511f.png)


## medusadigital | 2016-11-18T11:24:09+00:00
i could not reproduce this behaviour unfortunately on my side. im running together with https://github.com/monero-project/monero-core/pull/178


## medusadigital | 2017-08-07T20:13:41+00:00
seems good to me by now, closing until further notice.

+resolved

# Action History
- Created by: M5M400 | 2016-11-16T11:03:25+00:00
- Closed at: 2017-08-07T20:15:07+00:00
