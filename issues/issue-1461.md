---
title: Cannot send coins with new version
source_url: https://github.com/monero-project/monero/issues/1461
author: Atrides
assignees: []
labels: []
created_at: '2016-12-16T04:30:28+00:00'
updated_at: '2016-12-16T05:10:51+00:00'
type: issue
status: closed
closed_at: '2016-12-16T05:10:51+00:00'
---

# Original Description
On any transaction version 0.10.1 says:
` {u'jsonrpc': u'2.0', u'id': 0, u'error': {u'message': u'histogram reports no outputs for 30000000000, not even ours', u'code': -4}}`

In console:
```
2016-Dec-15 22:46:07.589115 [RPC0]ERROR /DISTRIBUTION-BUILD/contrib/epee/include/net/abstract_tcp_server2.inl:355 Exception at [connection<t_protocol_handler>::handle_read], what=Attempting to get output pubkey by index, but key does not exist
2016-Dec-15 22:46:44.712191 [RPC0]ERROR /DISTRIBUTION-BUILD/contrib/epee/include/net/abstract_tcp_server2.inl:355 Exception at [connection<t_protocol_handler>::handle_read], what=Attempting to get output pubkey by index, but key does not exist
2016-Dec-15 23:34:58.996479 [RPC1][on_send_raw_tx]: tx accepted, but not relayed

```

# Discussion History
## Atrides | 2016-12-16T04:46:23+00:00
Sorry, fixed. CLI used from 0.10.0 version with daemon 0.10.1

# Action History
- Created by: Atrides | 2016-12-16T04:30:28+00:00
- Closed at: 2016-12-16T05:10:51+00:00
