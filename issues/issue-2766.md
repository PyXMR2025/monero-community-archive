---
title: 'RPC: sendrawtransaction returns status OK if tx was not relayed'
source_url: https://github.com/monero-project/monero/issues/2766
author: cryptoshrimpi
assignees: []
labels:
- invalid
created_at: '2017-11-06T09:38:14+00:00'
updated_at: '2017-11-06T10:32:24+00:00'
type: issue
status: closed
closed_at: '2017-11-06T10:29:16+00:00'
---

# Original Description
I'm working on the doc for the yet undocumented RPC call 'sendrawtransaction'. The call returns a bunch of fields:

```
double_spend: boolean;
fee_too_low: boolean;
invalid_input: boolean;
invalid_output: boolean;
low_mixin: boolean;
not_rct: boolean;
not_relayed: boolean;
overspend: boolean;
reason: string;
status: string;
too_big: boolean;
```

By digging into the [code](https://github.com/monero-project/monero/blob/54463b33b3169f9d1ed6aefcc321e3715c066bd5/src/rpc/core_rpc_server.cpp#L681) I found that the field `status` is set to `CORE_RPC_STATUS_OK` if the transaction was not relayed. I don't know if the transaction gets automatically relayed on a later time when it fails first. If not I consider this as not expected behavior. One would expect to only get the status OK if the transaction went really through. Especially when that behavior is not documented it can lead to confusion and nasty bugs for third party developers. 

Or is there a misunderstanding on my side and a rawtransaction itself can define if the tx should be relayed or not?

Edit: I think I got it wrong and there is a use case when one does intentionally not  want to relay the transaction. In that case a OK-status would be fine and expected.

# Discussion History
## moneromooo-monero | 2017-11-06T10:26:30+00:00
This is as intended.

Network failures in relaying are ignored, but that's a different problem.

+invalid


# Action History
- Created by: cryptoshrimpi | 2017-11-06T09:38:14+00:00
- Closed at: 2017-11-06T10:29:16+00:00
