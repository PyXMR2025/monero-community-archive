---
title: jsonrpc-get_info free_space is incorrect
source_url: https://github.com/monero-project/monero/issues/9774
author: nice42q
assignees: []
labels: []
created_at: '2025-02-06T08:25:50+00:00'
updated_at: '2025-02-10T21:02:44+00:00'
type: issue
status: closed
closed_at: '2025-02-10T21:02:42+00:00'
---

# Original Description
The value is incorrect on port 18089.

`curl http://127.0.0.1:18081/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"get_info"}' -H 'Content-Type: application/json'`
`curl http://127.0.0.1:18089/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"get_info"}' -H 'Content-Type: application/json'`

database_size is also different.

# Discussion History
## SChernykh | 2025-02-06T08:38:28+00:00
Free space is not reported via restricted RPC (18089). Database size is also rounded up to the nearest 5 GB mark via restricted RPC. This works as designed.

## nice42q | 2025-02-06T09:39:43+00:00
> Free space is not reported via restricted RPC (18089).

You receive a value. Even if this is unrealistic.

## selsta | 2025-02-10T21:02:42+00:00
Closing this as intended behaviour.

# Action History
- Created by: nice42q | 2025-02-06T08:25:50+00:00
- Closed at: 2025-02-10T21:02:42+00:00
