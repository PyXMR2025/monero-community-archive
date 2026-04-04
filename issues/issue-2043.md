---
title: '[BUG] integrated_address no longer allows 64 symbol hex payment_id'
source_url: https://github.com/monero-project/monero/issues/2043
author: gituser
assignees: []
labels: []
created_at: '2017-05-23T14:50:20+00:00'
updated_at: '2017-05-29T10:05:03+00:00'
type: issue
status: closed
closed_at: '2017-05-29T10:05:03+00:00'
---

# Original Description
Hi.

Testing with `v0.10.3.1-release`.

```
[wallet XXX]: integrated_address 2b71cc0ffabb1d2b16112c0eaa11f5fec465abe862789219a943bc1bee391de9
Error: failed to parse payment ID or address
[wallet XXX]: integrated_address bff59eda1e4fc2f3
XXXX_address
[wallet XXX]: integrated_address 0000000000000000
XXXX_address
```

It appears to me that only 16 symbol payment_id is supported for generating integrated addresses?

Lots of exchangers are still requiring 64 symbol payment_ids. Can this be fixed for backward compatibility?

Thank you.

# Discussion History
## moneromooo-monero | 2017-05-29T07:07:31+00:00
It never did. If you need a 256 bit payment id, you use it as is. Integrated address use 64 bit payment ids.

## gituser | 2017-05-29T10:05:03+00:00
@moneromooo-monero ok, thanks for clarifying.

# Action History
- Created by: gituser | 2017-05-23T14:50:20+00:00
- Closed at: 2017-05-29T10:05:03+00:00
