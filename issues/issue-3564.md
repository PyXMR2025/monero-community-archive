---
title: sending flush_txpool doesn't work
source_url: https://github.com/monero-project/monero/issues/3564
author: Gingeropolous
assignees: []
labels: []
created_at: '2018-04-06T00:27:04+00:00'
updated_at: '2018-04-15T04:14:39+00:00'
type: issue
status: closed
closed_at: '2018-04-06T02:43:00+00:00'
---

# Original Description
```
:~/conf_files$ monerod --rpc-bind-port 12345 flush_txpool
2018-04-06 00:26:02.871	    7fb38dae7740	ERROR	net.http	contrib/epee/include/storages/http_abstract_invoke.h:118	RPC call of "flush_txpool" returned error: -32601, message: Method not found
Error: Unsuccessful -- json_rpc_request: 

```



# Discussion History
## Gingeropolous | 2018-04-06T02:43:00+00:00
im special. restricted rpc was still set as a general flag

## joijuke | 2018-04-15T04:14:39+00:00
i have the same issue. and some other method isnot working, include: print_pl....

# Action History
- Created by: Gingeropolous | 2018-04-06T00:27:04+00:00
- Closed at: 2018-04-06T02:43:00+00:00
