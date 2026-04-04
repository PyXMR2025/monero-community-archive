---
title: '`transfer` command errors with a payment_id '
source_url: https://github.com/monero-project/monero/issues/5039
author: jacoblyles
assignees: []
labels: []
created_at: '2019-01-02T17:10:56+00:00'
updated_at: '2019-01-02T18:35:27+00:00'
type: issue
status: closed
closed_at: '2019-01-02T18:35:27+00:00'
---

# Original Description
My 3-of-5 wallet will create a transaction just fine if I don't include a `payment_id`, but I get an error if I do include a `payment_id`

```
{
    "jsonrpc": "2.0",
    "id": "0",
    "method": "transfer",
    "params": {
        "destinations": [
            {
                "address": "4GdoN7NCTi8a5gZug7PrwZNKjvHFmKeV11L6pNJPgj5QNEHsN6eeX3DaAQFwZ1ufD4LYCZKArktt113W7QjWvQ7CWCNXMnKGuKYD2K9d7Z",
                "amount": 1000000000
            }
        ],
        "mixin": 7,
        "payment_id": "355e1d4953ba856a726d7ea5ba095f5d17b4f5c60b5dfdbd9c1f42ee7bd08da9"
    }
}

{
    "error": {
        "code": -5,
        "message": "A single payment id is allowed per transaction"
    },
    "id": "0",
    "jsonrpc": "2.0"
}
```

# Discussion History
## moneromooo-monero | 2019-01-02T18:07:51+00:00
As the error says, only one per tx. You have one in the address already, it's an integrated address.

# Action History
- Created by: jacoblyles | 2019-01-02T17:10:56+00:00
- Closed at: 2019-01-02T18:35:27+00:00
