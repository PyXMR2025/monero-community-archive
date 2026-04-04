---
title: Failure to parse Peerlist
source_url: https://github.com/monero-project/monero/issues/2892
author: medusadigital
assignees: []
labels: []
created_at: '2017-12-07T13:43:11+00:00'
updated_at: '2017-12-13T21:24:27+00:00'
type: issue
status: closed
closed_at: '2017-12-13T21:24:27+00:00'
---

# Original Description
Peerlist is unable to get parsed, resulting in new users being unable to synchronize with the network.

https://paste.fedoraproject.org/paste/eCzLLhncXl9WT-dFjoF73w
https://paste.fedoraproject.org/paste/XBLw9W2HVaBHCrKpoIeu3A

Issue does not affect Release 0.11.1.0, but current Master

# Discussion History
## brenmcma | 2017-12-09T16:33:47+00:00
@medusadigital The paste is no longer there. Could you please provide the errors?

## moneromooo-monero | 2017-12-10T00:22:38+00:00
I saw them, and I believe I fixed it in https://github.com/monero-project/monero/pull/2906

## moneromooo-monero | 2017-12-10T19:53:18+00:00
Which is now merged. Please confirm it fixes your case.

## moneromooo-monero | 2017-12-13T21:16:20+00:00
+resolved

# Action History
- Created by: medusadigital | 2017-12-07T13:43:11+00:00
- Closed at: 2017-12-13T21:24:27+00:00
