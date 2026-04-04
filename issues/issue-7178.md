---
title: Make rpc_access_data method accessible via json rpc
source_url: https://github.com/monero-project/monero/issues/7178
author: t-900-a
assignees: []
labels: []
created_at: '2020-12-20T22:06:47+00:00'
updated_at: '2020-12-20T22:06:47+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
This issue stems from the inability to call the rpc_access_data method.

**How to reproduce**
./monerod --testnet --rpc-bind-ip 127.0.0.1 --rpc-restricted-bind-port 9942 --confirm-external-bind --public-node --rpc-payment-address 9wCjDRNtPpU6ZKZVRycoovdJy2ATC7AHEPwz26tjqUAB6NnZS3swrGshQwckidpMxJi5rVBYxUM6pFGHHGmCJy47TCgETRQ --rpc-payment-credits 250 --rpc-payment-difficulty 1000

python
`import requests
import json
hdr = {'Content-Type': 'application/json'}
data = {'jsonrpc' : '2.0', 'method':'rpc_access_data', 'id': 0}
r = requests.get('http://127.0.0.1:28081/json_rpc', headers=hdr, data=json.dumps(data))
print(r.content.decode("ascii"))
`
{
  "error": {
    "code": 0,
    "message": ""
  },
  "id": 0,
  "jsonrpc": "2.0"
}

**Relevant conversation with moneromooo**
anon_ajbuhaerugh
16:14:24
Moneromooo are you here? I've got a question about this commit: https://github.com/monero-project/monero/commit/2899379791b7542e4eb920b5d9d58cf232806937#diff-eb68bc...
+moneromooo
16:16:46
What is that question ?
← woodser has left (Read error: Connection reset by peer)
→ woodser_ has joined
anon_ajbuhaerugh
16:23:33
It's about the execution path of a rpc_access_data json request.
anon_ajbuhaerugh
16:25:28
I'm not the best programmer, so I'm going to try to explain.
I see in that code, only when the json rpc is called, as apposed to the cli, the json_rpc_request function is called.
I think it is intended for this code to run: https://github.com/monero-project/monero/blob/43f91ee12ec9cd539e011b7b551d66659fb3188a/src/rpc/core_...
But in practice, I don't think it can ever be called.
The logic for rpc payments requires that the rpc server be started in restricted mode.
But, rpc_access_data is an rpc call that is restricted itself: https://github.com/monero-project/monero/blob/43f91ee12ec9cd539e011b7b551d66659fb3188a/src/rpc/core_...
So there is no way in which the previously mentioned code path can ever run.
← acceleratesats has left (Remote host closed the connection)
+moneromooo
16:30:44
I think you're correct.
anon_ajbuhaerugh
16:33:53
Is there a reason we can't have rpc_access_data, be unrestricted?
The call itself, shouldn't allow people to modify their own balance, only view everyone's balance.
It would reveal client ID's to the world, but I don't think that is a security issue. Correct me if I'm wrong.
+moneromooo
16:38:55
It's none of the business of anyone else, really.
+moneromooo
16:40:02
It should be able to be run on the restricted port, to read what's on the other one. But atm IIRC two servers are started, rather than a server listening on two ports. So that should be changed first.
anon_ajbuhaerugh
16:50:11
Ok, I hadn't realized there was that option.
I just tried using  --rpc-restricted-bind-port
anon_ajbuhaerugh
16:51:44
I first tied a jsonrpc call using sync_info i tried the restricted-bind-port, I got method not found as expected.
Then I tried the same jsonrpc call for the unrestricted port 28081 in this case, and I was able to receive data back.
I repated the same process for 'rpc_access_data', but I'm getting an error for the unrestricted port 28081. error code: 0
+moneromooo
16:54:11
When I said "It should be able to be run on the restricted port" I meant "ideally it should be..."
ie, for it to work properly, there should be either one single server for the two ports, or some data sharing.
This is not currently the case.




# Discussion History
# Action History
- Created by: t-900-a | 2020-12-20T22:06:47+00:00
