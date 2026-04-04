---
title: show_transfer <txid> command doesn't work in CLI
source_url: https://github.com/monero-project/monero/issues/8188
author: Cactii1
assignees: []
labels: []
created_at: '2022-02-19T22:43:15+00:00'
updated_at: '2022-02-22T22:11:14+00:00'
type: issue
status: closed
closed_at: '2022-02-22T22:11:14+00:00'
---

# Original Description
I tested this on two wallets. On a windows system with pre-built binaries.

First I did a show_transfers in and grabbed a txid from the list and then I tried show_transfer with a txid and it always gives the message "failed to parse txid".

I don't have the skills to follow the code to debug/fix it - sorry.

# Discussion History
## ndorf | 2022-02-22T22:00:17+00:00
I couldn't reproduce this with 0.17.3.0 on Linux. Are you sure you're copy/pasting the txid, and not some other field? The txid would be exactly 64 hexadecimal characters.

## Cactii1 | 2022-02-22T22:11:14+00:00
Oh man! I feel so dumb. Massive error on my part. I was using the encrypted payment ID.

# Action History
- Created by: Cactii1 | 2022-02-19T22:43:15+00:00
- Closed at: 2022-02-22T22:11:14+00:00
