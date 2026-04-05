---
title: 'Multi algo support for chains like EPIC CASH '
source_url: https://github.com/xmrig/xmrig/issues/3248
author: bey0ndmo
assignees: []
labels: []
created_at: '2023-04-10T06:30:12+00:00'
updated_at: '2025-06-18T22:42:41+00:00'
type: issue
status: closed
closed_at: '2025-06-18T22:42:41+00:00'
---

# Original Description
Is it possible to add algo switching like SRBMINER has multi-algorithm-job-mode 3 that basically mines algo 0 while it's available then switches to algo 1 until algo 0 becomes available, useful for coins like EPIC CASH that mines randomx for 48% of the time which can be filled in with xmr the other 52% of the time?

# Discussion History
## Spudz76 | 2023-04-10T15:23:35+00:00
There is GhostRider which jumps around several flavors of CN, already supported.  Perhaps EPIC is similar enough to implement like that.

The [MoneroOcean fork](https://github.com/MoneroOcean/xmrig/) does auto-switching based on hashrates, but is designed for their pool which pays XMR exchange value for everything.  If EPIC sends normal headers per the algo it's using, the autoswitching might work as-is.

## Spudz76 | 2023-04-11T03:27:43+00:00
Actually algo-switching works in the regular fork too, if the implementation sends standard headers.

# Action History
- Created by: bey0ndmo | 2023-04-10T06:30:12+00:00
- Closed at: 2025-06-18T22:42:41+00:00
