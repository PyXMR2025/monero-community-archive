---
title: Can you return alternative blocks from the deamon using RPC?
source_url: https://github.com/monero-project/monero/issues/2080
author: moneroexamples
assignees: []
labels: []
created_at: '2017-06-09T22:37:21+00:00'
updated_at: '2017-08-07T17:36:15+00:00'
type: issue
status: closed
closed_at: '2017-08-07T17:36:15+00:00'
---

# Original Description
Currently you can get number of alternative blocks using get_info rpc command

https://github.com/monero-project/monero/blob/master/src/rpc/core_rpc_server.cpp#L127

But how do you get actual alternative blocks with txs in these blocks?



# Discussion History
## moneromooo-monero | 2017-06-10T08:29:23+00:00
getblock RPC (if you know the hash).


## moneroexamples | 2017-06-10T13:02:26+00:00
So what rpc call returns the hashes of alternative blocks?

## moneromooo-monero | 2017-06-10T15:19:33+00:00
I don't think there's one for that.

## moneroexamples | 2017-06-12T21:40:56+00:00
Ok. Thanks. I will keep the issue open for a bit.

## moneroexamples | 2017-06-15T01:01:49+00:00
I will be adding such call to my local copy of monero becasue I want to add listing of alt blocks to the onion explorer. For now there is only number of alt blocks given (http://139.162.32.245:8081/), but cant view them.

If main monero project would find such rpc call interesting, could you advice what would suit best for you. For now I'm just addint it as:

```
MAP_URI_AUTO_BIN2("/getaltblocks.bin", on_get_alt_blocks, COMMAND_RPC_GET_ALT_BLOCKS)
```

## moneromooo-monero | 2017-06-16T18:13:42+00:00
I think it'd be better to get just the hashes, or it could become a pretty heavy call on long running daemons. Actual blocks can be fetched from the hashes in a second call, possibly with the caller fetching by chunk of N.

## moneroexamples | 2017-06-16T22:36:40+00:00
Thanks for feedback. Makes sense. So I will do as suggested. Thanks.

## moneroexamples | 2017-06-23T21:38:28+00:00
I tentatively added the call. It is here: https://github.com/moneroexamples/monero/commit/ff340c5056820875b202de3d5206bab549d0e226

Any feedback appreciated. 

Its use is already being implemented in the explorer, e.g.: http://139.162.32.245:8082/altblocks

## moneromooo-monero | 2017-06-24T10:53:15+00:00
That looks good, just bump the minor RPC version though.

## moneromooo-monero | 2017-08-07T17:34:54+00:00
Added by the reporter.

+resolved

# Action History
- Created by: moneroexamples | 2017-06-09T22:37:21+00:00
- Closed at: 2017-08-07T17:36:15+00:00
