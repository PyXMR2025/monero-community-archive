---
title: 'rpc daemon get_info   top_block_hash :  is allway empty'
source_url: https://github.com/monero-project/monero/issues/1210
author: perl5577
assignees: []
labels: []
created_at: '2016-10-12T02:07:05+00:00'
updated_at: '2016-12-15T16:09:14+00:00'
type: issue
status: closed
closed_at: '2016-12-15T16:09:14+00:00'
---

# Original Description
top_block_hash :  is allway empty

target_height : Why is different from many monerod in same version and same time is different.

For target_height is possible, I have not understand metrics


# Discussion History
## moneroexamples | 2016-10-12T05:11:25+00:00
A command to test this:

```
curl -X POST http://127.0.0.1:18081/json_rpc -d '{"jsonrpc":"2.0","id:"0","method":"get_info"}' -H 'Content-Type: application/json'
```

And this happens because `res.top_block_hash` is not set in `core_rpc_server::on_get_info_json()`.


## perl5577 | 2016-10-12T07:18:10+00:00
Why target_height as different value from different daemon in same time ?


## moneromooo-monero | 2016-10-12T08:09:10+00:00
target_height is the max height of seen peers, so may be different for two daemons. I think it doesn't take into account whether that chain is invalid or not though.


## moneromooo-monero | 2016-10-12T08:16:58+00:00
And I have no idea why there are two getinfo calls. The other one sets top hash. I'm guessing any change gets made to one function and the ohter one gets forgot...


## perl5577 | 2016-10-12T08:33:50+00:00
Exemple 8 Daemon started same time (  full sync and found block ).
For moment is only updated when "Sync data returned unknown top block"
If sync is ok with last peer target_block not updated

```
2016-Oct-12 10:43:02 target_height in RPC Call  1009962
2016-Oct-12 10:43:32 target_height in RPC Call  1009962
2016-Oct-12 10:44:02 target_height in RPC Call  1009962
2016-Oct-12 10:44:32 target_height in RPC Call  1009962
2016-Oct-12 10:45:02 target_height in RPC Call  1009962
2016-Oct-12 10:45:22.197402 [P2P6][104.168.99.235:18080 OUT]Sync data returned unknown top block: 1155685 -> 1155686 [1 blocks (0 days) behind] 
2016-Oct-12 10:45:32 target_height in RPC Call  1155686
2016-Oct-12 10:46:02 target_height in RPC Call  1155686
2016-Oct-12 10:46:32 target_height in RPC Call  1155686
2016-Oct-12 10:47:02 target_height in RPC Call  1155686
```

Use oneliner follow and tail on filelog of daemon for see events

```
while /bin/true ; do echo "$(date +'%Y-%h-%d %H:%M:%S') target_height in RPC Call  $(curl -s  -X POST http://XX.XX.XX.XX:XXXX/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"get_info"}' -H 'Content-Type: application/json' | jq -r '.result.target_height')" ; sleep 30 ; done
```


## moneromooo-monero | 2016-10-15T13:37:24+00:00
https://github.com/monero-project/monero/pull/1221


# Action History
- Created by: perl5577 | 2016-10-12T02:07:05+00:00
- Closed at: 2016-12-15T16:09:14+00:00
