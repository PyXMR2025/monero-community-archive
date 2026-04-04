---
title: ' error: ‘get_address_from_str’ was not declared in this scope'
source_url: https://github.com/monero-project/monero/issues/1546
author: moneroexamples
assignees: []
labels: []
created_at: '2017-01-09T04:10:28+00:00'
updated_at: '2017-01-10T22:58:33+00:00'
type: issue
status: closed
closed_at: '2017-01-10T22:58:33+00:00'
---

# Original Description
Following today's merges of PRs, monero does not compile anymore:

```
/home/mwo/monero/src/simplewallet/simplewallet.cpp:3544:76: error: ‘get_address_from_str’ was not declared in this scope
     if (!get_address_from_str(args[1], address, has_payment_id, payment_id8))
```

function `get_address_from_str` does not exist in monero source code.

# Discussion History
## kenshi84 | 2017-01-09T04:14:40+00:00
Fixed by PR #1544 

## moneroexamples | 2017-01-09T04:36:17+00:00
LoL. Just prepared the same fix: https://github.com/moneroexamples/monero/commit/48be39977906d01dc040161e72ac03d286813317

Anyway, thanks for fast response :-)

## luigi1111 | 2017-01-10T22:58:33+00:00
:)

# Action History
- Created by: moneroexamples | 2017-01-09T04:10:28+00:00
- Closed at: 2017-01-10T22:58:33+00:00
