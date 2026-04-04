---
title: I have got error when i used 12.2 monerod version
source_url: https://github.com/monero-project/monero/issues/3952
author: WebCodiyapa
assignees: []
labels:
- invalid
created_at: '2018-06-07T07:49:46+00:00'
updated_at: '2018-06-10T11:48:53+00:00'
type: issue
status: closed
closed_at: '2018-06-10T11:48:53+00:00'
---

# Original Description
ERROR   cn      src/cryptonote_core/cryptonote_core.cpp:1223    Exception at [core::handle_incoming_block()], what=DB error attempting to fetch block index from hashMDB_BAD_TXN: Transaction must abort, has a child, or is invalid

# Discussion History
## moneromooo-monero | 2018-06-07T11:45:35+00:00
That looks like a corrupt DB. Did your OS crash, or computer lose power ?
Also, which OS are you using ?

## dEBRUYNE-1 | 2018-06-10T11:45:03+00:00
Going to close this in favor of #3961 

+invalid 

# Action History
- Created by: WebCodiyapa | 2018-06-07T07:49:46+00:00
- Closed at: 2018-06-10T11:48:53+00:00
