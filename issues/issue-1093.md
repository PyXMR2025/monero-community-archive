---
title: Connecting to dead remote nodes
source_url: https://github.com/monero-project/monero-gui/issues/1093
author: Gingeropolous
assignees: []
labels: []
created_at: '2018-01-24T03:33:39+00:00'
updated_at: '2018-01-24T12:32:15+00:00'
type: issue
status: closed
closed_at: '2018-01-24T12:32:15+00:00'
---

# Original Description
So, the existing node list providers (moneroworld and node.xmr.be) aren't perfect. For instance, as of writing, there are 5 nodes in the node.moneroworld.com list that fail my old moneriote.sh script.

unfortunately, when the GUI tries to connect to these, it doesn't indicate that its failing. I'm running it in linux, so I can see in the terminal that its just doing this over and over again

```
"initAsync: 172.245.41.237:18089"
qml: Wallet connection status changed 0
init non async
init async finished - starting refresh
Checking connection status
2018-01-24 03:28:59.968	    7fea97af5700	ERROR	net.http	contrib/epee/include/net/http_client.h:444	Unexpected recv fail
2018-01-24 03:29:14.990	    7feaad0a8700	ERROR	net.http	contrib/epee/include/net/http_client.h:444	Unexpected recv fail
refreshed
qml: >>> wallet refreshed
Checking connection status
qml: >>> wallet updated
2018-01-24 03:29:30.014	    7fea97af5700	ERROR	net.http	contrib/epee/include/net/http_client.h:444	Unexpected recv fail
```

The GUI should report to the user that the node it is trying to connect to isn't working. I think a lot of complaints we see on reddit etc are because people think the GUI is broken, but instead its the remote node. 

# Discussion History
## Gingeropolous | 2018-01-24T12:32:15+00:00
this is a duplicate of #864

# Action History
- Created by: Gingeropolous | 2018-01-24T03:33:39+00:00
- Closed at: 2018-01-24T12:32:15+00:00
