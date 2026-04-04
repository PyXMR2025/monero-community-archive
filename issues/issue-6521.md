---
title: 'Add json-rpc endpoint for monerod command: rpc_payments'
source_url: https://github.com/monero-project/monero/issues/6521
author: t-900-a
assignees: []
labels: []
created_at: '2020-05-12T18:04:49+00:00'
updated_at: '2020-05-13T17:01:21+00:00'
type: issue
status: closed
closed_at: '2020-05-13T17:01:21+00:00'
---

# Original Description
When I have rpc payments enable I can get info from the monerod daemon via command: rpc_payments

Example output is:

Client Id | Balance | Total mined | Good | Stale | Bad | Dupes | Last update
-- | -- | -- | -- | -- | -- | -- | --
exampleclientid | 666 | 666 | 100 | 0 | 0 | 0 | 40 seconds ago
1 clients with a total of 26466 credits |   |   |   |   |   |   |  
Aggregated client hash rate: 1 H/s |   |   |   |   |   |   |  

I would like to be able to query this information via rpc.

Example rpc method request:
curl -X POST 127.0.0.1:18081/json_rpc -H 'Content-Type:application/json' --data "{\"jsonrpc\":\"2.0\",\"id\":\"0\",\"method\":\"rpc_payments\"}"

Example returned output:
{
  "aggregate_client_hash_rate": "40 H/s",
  "num_clients": 1,
  "total_credits": 26466,
  "clients": [
    {
      "client_id": "exampleclientid1",
      "balance": 666,
      "total_mined": 666,
      "good": 100,
      "stale": 0,
      "bad": 0,
      "dupes": 0,
      "last_update": "2 seconds ago"
    },
    {
      "client_id": "exampleclientid2",
      "balance": 2344,
      "total_mined": 2370,
      "good": 2100,
      "stale": 0,
      "bad": 0,
      "dupes": 0,
      "last_update": "40 seconds ago"
    }
  ]
}


Edit: Also wondering what level of difficulty it would be to add this.

# Discussion History
## moneromooo-monero | 2020-05-13T14:05:25+00:00
There is one, it's called rpc_access_data.

## t-900-a | 2020-05-13T17:01:21+00:00
Thanks, I'm having issues with this so I created a post on stackexchange.
https://monero.stackexchange.com/questions/12193/using-the-rpc-access-data-method-daemon-rpc

I'll close the post as the functionality is already there.

# Action History
- Created by: t-900-a | 2020-05-12T18:04:49+00:00
- Closed at: 2020-05-13T17:01:21+00:00
