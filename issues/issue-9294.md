---
title: monerod memory usage on busy public node
source_url: https://github.com/monero-project/monero/issues/9294
author: Jayd603
assignees: []
labels:
- question
created_at: '2024-04-16T14:21:47+00:00'
updated_at: '2024-12-14T00:14:47+00:00'
type: issue
status: closed
closed_at: '2024-12-14T00:14:47+00:00'
---

# Original Description
I noticed that the OS was running out of memory and using swap with 32GB RAM , so I doubled it to 64GB , same thing?!   Is monerod designed to use all memory possible or is there a memory leak?

also getting errors in logs...
2024-04-16 03:00:47.092	W ge_frombytes_vartime failed at 457
2024-04-16 03:16:27.954	E Failed to parse transaction from blob

Possibly unrelated though, it does seem like the blockchain is up to date and the performance seems fine when connecting and updating from the node.



# Discussion History
## selsta | 2024-04-17T22:35:45+00:00
The tx pool was at 100MB recently, that is 300x larger than usual. This resulted in performance issues for public nodes. Is high memory usage always an issue or only the last couple days?

> 2024-04-16 03:00:47.092 W ge_frombytes_vartime failed at 457
> 2024-04-16 03:16:27.954 E Failed to parse transaction from blob

These means someone is submitting transactions that fail verification. It happens occasionally and is unrelated.

## Jayd603 | 2024-04-18T02:28:56+00:00
That makes a lot of sense.. memory usage seems a lot better now.   The node seemed to perform just fine even through the 100MB flood despite high memory usage, I was just worried about a memory leak.  This was the busiest I have witnessed, 2-3 cores pegged and max memory.

## selsta | 2024-12-14T00:14:47+00:00
https://github.com/monero-project/monero/issues/9334 is a proposal to reduce memory usage during high usage.

# Action History
- Created by: Jayd603 | 2024-04-16T14:21:47+00:00
- Closed at: 2024-12-14T00:14:47+00:00
