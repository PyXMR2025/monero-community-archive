---
title: Does Monero-GUI attempt to retry failed transactions?
source_url: https://github.com/monero-project/monero/issues/6998
author: pushshift
assignees: []
labels: []
created_at: '2020-11-09T15:52:33+00:00'
updated_at: '2021-08-13T04:58:02+00:00'
type: issue
status: closed
closed_at: '2021-08-13T04:58:01+00:00'
---

# Original Description
I have several failed transactions in my history which was eventually successful for one of them. I'm worried that if I receive enough Monero, the failed transactions will auto-attempt and retry to send to the same address.

1) How to I delete failed transactions in the GUI? I tried right-clicking but there doesn't seem to be any option to remove failed transactions.

2) Do failed transactions retry automatically? If so, how can this be disabled?

Thanks!


# Discussion History
## iDunk5400 | 2020-11-09T16:05:02+00:00
Please open an issue in [Monero-GUI repo](https://github.com/monero-project/monero-gui/issues). Thank you.

## moneromooo-monero | 2020-11-10T02:32:25+00:00
Monero is not balance based. Receiving new monero will not affect previous transactions, which spend the same outputs whether or not you receive other monero later.

## selsta | 2020-11-10T07:40:37+00:00
@pushshift Please update to v0.17.1.4, it should fail less often in simple mode.

## dEBRUYNE-1 | 2020-11-10T16:26:41+00:00
Please try the recently released v0.17.1.4:

https://www.reddit.com/r/Monero/comments/jrgtca/gui_v01714_oxygen_orion_released/

Additionally, see:

https://www.reddit.com/r/Monero/comments/jrh7mv/psa_informational_thread_on_the_recently_observed/

## selsta | 2021-08-13T04:58:01+00:00
Wrong repo also Issue no longer relevant.

# Action History
- Created by: pushshift | 2020-11-09T15:52:33+00:00
- Closed at: 2021-08-13T04:58:01+00:00
