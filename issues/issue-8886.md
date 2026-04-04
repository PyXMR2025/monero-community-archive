---
title: Can I save the wallet after clearing the subaddress?
source_url: https://github.com/monero-project/monero/issues/8886
author: EWIT521
assignees: []
labels:
- question
created_at: '2023-06-01T08:59:11+00:00'
updated_at: '2023-12-07T21:14:04+00:00'
type: issue
status: closed
closed_at: '2023-12-07T21:14:04+00:00'
---

# Original Description
 static serializable_unordered_map<crypto::public_key, cryptonote::subaddress_index> m_subaddresses;
 
m_subaddresses, object containing 50 million subaddresses, each time save is called.A new wallet file is generated locally.
When the wallet is loaded  It takes a long time。 Can I save the wallet after clearing the subaddress?

# Discussion History
## moneromooo-monero | 2023-06-07T16:55:52+00:00
You can erase subaddresses from the map. If you do that though, the wallet will not see any output sent to any of those erased addresses, so you gotta make sure you only erase ones you're sure will be unused in the future.
There's no code for this atm but it's a straightforward change.


## EWIT521 | 2023-06-08T12:25:22+00:00
What kind of addresses is unused in the future?if I have deleted it ,What is the impact？

# Action History
- Created by: EWIT521 | 2023-06-01T08:59:11+00:00
- Closed at: 2023-12-07T21:14:04+00:00
