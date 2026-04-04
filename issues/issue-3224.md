---
title: No viable overload error on OSX build
source_url: https://github.com/monero-project/monero/issues/3224
author: robbsolter
assignees: []
labels:
- duplicate
created_at: '2018-02-02T03:06:13+00:00'
updated_at: '2018-02-02T08:24:29+00:00'
type: issue
status: closed
closed_at: '2018-02-02T08:24:29+00:00'
---

# Original Description
This is on OSX High Sierra, when doing a `make`

```
/monero/src/cryptonote_protocol/cryptonote_protocol_handler.inl:615:43: error: no viable overloaded '='
        missing_tx_req.missing_tx_indices = std::move(need_tx_indices);
```

# Discussion History
## moneromooo-monero | 2018-02-02T08:19:21+00:00
Use current code.

+duplicate


# Action History
- Created by: robbsolter | 2018-02-02T03:06:13+00:00
- Closed at: 2018-02-02T08:24:29+00:00
