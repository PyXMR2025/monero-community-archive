---
title: How to set testnet for CryptonightR
source_url: https://github.com/monero-project/monero/issues/5245
author: DinoStray
assignees: []
labels: []
created_at: '2019-03-07T03:31:42+00:00'
updated_at: '2019-03-19T14:17:55+00:00'
type: issue
status: closed
closed_at: '2019-03-19T14:17:55+00:00'
---

# Original Description
I wanna test CryptonightR for v0.14.
How to run testnet config?
Now "getblocktemplate" return
"blocktemplate_blob": "0b0bb68c82e4053d50f89f7991db941a338a20a62ade1418b3c6c48dacc552edbc25cc0ff320210000000002f6aa4701ffbaaa47018b9297bdfbc701023781552f559a7cfcd6186a3b1b644d5812be7ffda77a0ea45c46ef5145e185432b01b2b4b77c4e6dbab45b0c2dd7d43d2bc0feea05768be30ef9c86ccd15b0badeef020800000000000000000000"

the major_version is 0b -> 11, But I wanna 0a -> 10 for 0.14

# Discussion History
## moneromooo-monero | 2019-03-07T10:01:58+00:00
The public testnet is already at v11, so using CNv4 (Cryptonight-R based). v10 was active for just one day, it's a technical double fork to ensure the txpool does not get wiped out on fork, but v11 is what you want for testing CNv4.


## moneromooo-monero | 2019-03-19T14:15:49+00:00
As intended, not a bug.

+resolved

# Action History
- Created by: DinoStray | 2019-03-07T03:31:42+00:00
- Closed at: 2019-03-19T14:17:55+00:00
