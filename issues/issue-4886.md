---
title: rpc /getblocks.bin return 404
source_url: https://github.com/monero-project/monero/issues/4886
author: meiyoung
assignees: []
labels:
- invalid
created_at: '2018-11-22T06:49:58+00:00'
updated_at: '2018-11-25T18:56:54+00:00'
type: issue
status: closed
closed_at: '2018-11-25T18:56:53+00:00'
---

# Original Description
rpc API  /getblocks.bin return 404.

I call  it like following:
```
{"start_height":1095530, "prune": true, "block_ids":[]}
```

How to fix it? 

Can someone give me an example to call this RPC?


# Discussion History
## meiyoung | 2018-11-22T09:33:29+00:00
`/get_o_indexes.bin` is 404 


## moneromooo-monero | 2018-11-22T11:21:12+00:00
It's a binary call, not a JSON call. If you want to use JSON calls, don't use the bin ones.

## meiyoung | 2018-11-23T01:27:28+00:00
I know it is a binary call, and i call it as following:

```
curl -X POST http://127.0.0.1:28081/getblocks.bin -H 'Content-Type: application/json' -d '{"start_height": 103000, "prune": true, "block_ids":[2]}'
```

nothing returns




## moneromooo-monero | 2018-11-23T01:31:44+00:00
You are sending JSON. Text.

## meiyoung | 2018-11-23T06:01:54+00:00
thank you.

can you give me an example?


## moneromooo-monero | 2018-11-23T12:44:55+00:00
You can look at wallet2.cpp, which calls those. But it's binary code, you have to send binary data, that means serialization, a fair bit of code.

Or you could use the JSON RPC, like getblockheaderbyheight, etc.


## moneromooo-monero | 2018-11-25T18:51:36+00:00
+invalid

# Action History
- Created by: meiyoung | 2018-11-22T06:49:58+00:00
- Closed at: 2018-11-25T18:56:53+00:00
