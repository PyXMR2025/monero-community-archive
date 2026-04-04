---
title: Errors code & messages list for wallet RPC ?
source_url: https://github.com/monero-project/monero/issues/6331
author: billyadelphia
assignees: []
labels:
- invalid
created_at: '2020-02-11T04:37:34+00:00'
updated_at: '2020-02-18T16:50:01+00:00'
type: issue
status: closed
closed_at: '2020-02-18T16:50:01+00:00'
---

# Original Description
Where can I see errors code & messages list for wallet RPC ?

# Discussion History
## moneromooo-monero | 2020-02-11T17:54:55+00:00
src/wallet/wallet_rpc_server_error_codes.h

Messages are informative only, don't try to parse them (or very few known ones like "OK", but even sometimes success is not just "OK").

## moneromooo-monero | 2020-02-18T16:44:37+00:00
Not a bug

+invalid

# Action History
- Created by: billyadelphia | 2020-02-11T04:37:34+00:00
- Closed at: 2020-02-18T16:50:01+00:00
