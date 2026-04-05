---
title: PGO support
source_url: https://github.com/xmrig/xmrig/issues/2749
author: Titaniumtown
assignees: []
labels: []
created_at: '2021-11-29T15:52:43+00:00'
updated_at: '2021-11-29T16:29:02+00:00'
type: issue
status: closed
closed_at: '2021-11-29T16:29:01+00:00'
---

# Original Description
Is there a possibility of being able to compile xmrig with PGO? PGO should provide a noticeable performance uplift and improve hashrate.

# Discussion History
## Spudz76 | 2021-11-29T16:09:42+00:00
Tried it a bunch of times and it does nothing.

Maybe makes the unimportant clerical stuff faster (pool comms, other logic, but not in the mining kernels).

## SChernykh | 2021-11-29T16:16:44+00:00
It does nothing because RandomX is 99% assembly code and compiler has no effect there. Cryptonight and Astrobwt are basically a loop without branches and PGO mostly optimizes branches.

## Titaniumtown | 2021-11-29T16:29:01+00:00
Ah ok. Thanks for your input @Spudz76 @SChernykh! I was not aware.

# Action History
- Created by: Titaniumtown | 2021-11-29T15:52:43+00:00
- Closed at: 2021-11-29T16:29:01+00:00
