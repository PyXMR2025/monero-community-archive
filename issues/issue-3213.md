---
title: 'Proposal - add optional #of outputs to sweep commands'
source_url: https://github.com/monero-project/monero/issues/3213
author: hyc
assignees: []
labels:
- proposal
created_at: '2018-01-30T17:15:28+00:00'
updated_at: '2018-09-21T21:48:52+00:00'
type: issue
status: closed
closed_at: '2018-09-21T21:48:52+00:00'
---

# Original Description
E.g.
> sweep_all [index=&lt;N1>[,&lt;N2>,...]] [&lt;priority>] [&lt;ring_size>] [&lt;outputs>] &lt;address> [&lt;payment_id>]

Cause the result to be divided into &lt;outputs> equal amounts for the generated outputs.
With &lt;outputs> defaulting to 1.

# Discussion History
## dEBRUYNE-1 | 2018-01-31T09:43:54+00:00
+proposal

## Mansarde | 2018-01-31T09:56:11+00:00
@hyc 
Just curious, would \<outputs\> at 1 then still create a zero-change output?

## hyc | 2018-01-31T16:08:53+00:00
@Mansarde probably. My point is just to provide a way to have multiple coins in the result, so you're not stuck locking your entire balance the next time you want to spend some amount.

Was also thinking we could automatically break amounts into denominations, like 1/5/10/50/100/500/1000 but that's probably more trouble than it's worth.

Alternatively we could change the default from (1 + zero-change) to 2 equal outputs.

## moneromooo-monero | 2018-09-21T21:43:28+00:00
+resolved

# Action History
- Created by: hyc | 2018-01-30T17:15:28+00:00
- Closed at: 2018-09-21T21:48:52+00:00
