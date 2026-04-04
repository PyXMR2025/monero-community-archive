---
title: Fee in testnet v8 does not change across different priority settings
source_url: https://github.com/monero-project/monero/issues/3397
author: ghost
assignees: []
labels: []
created_at: '2018-03-13T20:00:25+00:00'
updated_at: '2018-03-15T00:27:33+00:00'
type: issue
status: closed
closed_at: '2018-03-15T00:27:33+00:00'
---

# Original Description
Here is the same 0.00101 fee across priorities 1, 4, and 2: https://paste.fedoraproject.org/paste/5LaUb7jDdo5WtvzgTQEiKg

Likely this is just because the fee algorithm hasn't been created for multi input bulletproofs (or whatever the term is), but I thought I'd throw up this issue just in case.

# Discussion History
## stoffu | 2018-03-14T01:49:53+00:00
This is a bug fixed by #3398.
Thank you for reporting!

## ghost | 2018-03-14T04:02:46+00:00
@stoffu Thank you for fixing it

# Action History
- Created by: ghost | 2018-03-13T20:00:25+00:00
- Closed at: 2018-03-15T00:27:33+00:00
