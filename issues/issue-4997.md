---
title: How do I find the PUBKEY address and SCRIPT address? Or where is it located
  in the codebase?
source_url: https://github.com/monero-project/monero/issues/4997
author: ipabz
assignees: []
labels: []
created_at: '2018-12-19T08:02:10+00:00'
updated_at: '2018-12-19T08:18:01+00:00'
type: issue
status: closed
closed_at: '2018-12-19T08:16:13+00:00'
---

# Original Description
No description

# Discussion History
## fluffypony | 2018-12-19T08:03:03+00:00
Neither of those terms make sense with Monero. Are you thinking of Bitcoin? Some context might be useful.

## ipabz | 2018-12-19T08:10:22+00:00
On bitcoin I have the pubkey and scriptkey to validate the address. Do we have something similar for monero?

## fluffypony | 2018-12-19T08:12:47+00:00
Nope. In Monero your address *is* a pair of public keys (public viewkey and public spendkey). The address is valid as long as it passes the checksum baked into it. Monero doesn’t have script or anything like it.

There are more details on Monero’s address format on the Monero StackExchange, and there’s a Monero key tools client-side JS site that has code that is worth parsing.

## ipabz | 2018-12-19T08:16:06+00:00
Thank you very much 👍 

# Action History
- Created by: ipabz | 2018-12-19T08:02:10+00:00
- Closed at: 2018-12-19T08:16:13+00:00
