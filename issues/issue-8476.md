---
title: Offline sign transactions requires "Try using export_outputs all" periodically.
source_url: https://github.com/monero-project/monero/issues/8476
author: nape-max
assignees: []
labels: []
created_at: '2022-08-01T09:41:25+00:00'
updated_at: '2022-08-15T13:19:07+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Periodically, on call 'sign_transfer', I get this message:
```
"code": -42,
"message": "Failed to sign unsigned tx: Imported outputs omit more outputs that we know of. Try using export_outputs all."
```

Context: Wallet, have 2 addresses: Primary and one subaddress. Send coins to subaddress and then try to send coins from account. All transfers correct and completed. But after 1-3 transfers, I received this message.

Offline wallet display only 'primary' address in response from call 'get_address'. I tried to call 'create_address' on view-only and offline wallet both. Got same result and same message after 1-3 transfers.

Cannot understand reasons of that.
When I'm using 'export_outputs' and 'import_outputs', I got 'num_imported': 0. But after 1-3 transactions, receive message specified above. But after 'export_outputs' with 'all': true and 'import_outputs' I got 'num_imported' with non zero value.

I think is is not correct. Can you exlplain it?

# Discussion History
## moneromooo-monero | 2022-08-12T18:09:44+00:00
Most likely ae0a840fdaa15054a7c0529869fb20df0e1605ea being broken. It can be reverted safely.

## mrtestyboy781 | 2022-08-15T13:19:06+00:00
bumping this issue, seeing it as well

# Action History
- Created by: nape-max | 2022-08-01T09:41:25+00:00
