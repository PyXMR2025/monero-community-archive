---
title: Payment Id's show as 0000000000000000 after recent commits
source_url: https://github.com/monero-project/monero/issues/1279
author: medusadigital
assignees: []
labels: []
created_at: '2016-10-30T19:30:28+00:00'
updated_at: '2016-11-21T16:23:47+00:00'
type: issue
status: closed
closed_at: '2016-11-21T16:23:47+00:00'
---

# Original Description
Payment Id's show up as 0000000000000000 when using show_transfers after recent commits.

probably related to https://github.com/monero-project/monero-core/issues/87


# Discussion History
## moneromooo-monero | 2016-10-30T20:01:13+00:00
Testing here, with recent code:
Sending with integrated address (short payment id): payment id is wrong (though not 0)
Sending with full size payment id: payment id is correct


## moneromooo-monero | 2016-10-30T20:47:02+00:00
The integrated one is now fixed with https://github.com/monero-project/monero/pull/1282


# Action History
- Created by: medusadigital | 2016-10-30T19:30:28+00:00
- Closed at: 2016-11-21T16:23:47+00:00
