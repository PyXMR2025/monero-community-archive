---
title: '[Warning] Failed to open portable binary, trying unportable'
source_url: https://github.com/monero-project/monero/issues/6741
author: OxMarco
assignees: []
labels: []
created_at: '2020-08-04T17:31:50+00:00'
updated_at: '2022-07-19T20:01:38+00:00'
type: issue
status: closed
closed_at: '2022-07-19T20:01:38+00:00'
---

# Original Description
Upon calling `finalize_multisig` from a python script for a 2:3 wallet I get:

```
W Failed to open portable binary, trying unportable
monero-wallet-rpc(66007,0x7000014ad000) malloc: can't allocate region
*** mach_vm_map(size=380351428370403328) failed (error code=3)
monero-wallet-rpc(66007,0x7000014ad000) malloc: *** set a breakpoint in malloc_error_break to debug
```

The wallet seems to be successfully created as the addresses are all the same. Is the warning something to be concerned about?

# Discussion History
## selsta | 2022-04-10T20:34:52+00:00
Are you using the same version everywhere?

## selsta | 2022-07-19T20:01:38+00:00
No reply from the author and there were large changes to multisig in v0.18, closing.

# Action History
- Created by: OxMarco | 2020-08-04T17:31:50+00:00
- Closed at: 2022-07-19T20:01:38+00:00
