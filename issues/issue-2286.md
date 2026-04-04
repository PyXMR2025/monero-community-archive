---
title: 'Donate QR code not scan-able '
source_url: https://github.com/monero-project/monero-site/issues/2286
author: plowsof
assignees: []
labels: []
created_at: '2024-04-15T22:04:09+00:00'
updated_at: '2025-04-09T23:38:16+00:00'
type: issue
status: closed
closed_at: '2025-04-09T23:38:16+00:00'
---

# Original Description
https://www.reddit.com/r/Monero/comments/1c4wybg/comment/kzqnkvu/?context=3

reproduced in monerujo and iirc cake.

clicking the QR/Payment ink opens the app fine, but, attempting to scan the QR just doesnt work.. why dont wallet apps like the QR code at https://ccs.getmonero.org/donate/ 

in fact, my generic QR scanner app can't recognise the QR 

# Discussion History
## rottenwheel | 2024-04-16T09:15:06+00:00
OP mentioned QR in https://www.getmonero.org/get-started/contributing/ works. Perhaps just swap existing image for that one and call it a day.

## plowsof | 2024-04-16T12:43:08+00:00
agreed. made a PR https://repo.getmonero.org/monero-project/ccs-front/-/merge_requests/38

## plowsof | 2024-04-16T19:40:17+00:00
now i see that the the CCS' DONATE page doesnt contain btc info... should we not just have the DONATE button take people to sites "contributing" page .. maybe add an anchor to the Donate section for convenience 

## plowsof | 2024-04-19T08:00:40+00:00
#2287 is another K.I.S.S alternative, simply linking to the getmonero contributing > donate section (which is fully featured with translated strings / working QR's of both the Monero and Bitcoin donation addresses) 

# Action History
- Created by: plowsof | 2024-04-15T22:04:09+00:00
- Closed at: 2025-04-09T23:38:16+00:00
