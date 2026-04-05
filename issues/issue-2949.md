---
title: Inclusion of cpu speed in xmr benchmark
source_url: https://github.com/xmrig/xmrig/issues/2949
author: heavyarms2112
assignees: []
labels:
- question
created_at: '2022-02-28T21:13:54+00:00'
updated_at: '2022-04-03T07:58:53+00:00'
type: issue
status: closed
closed_at: '2022-04-03T07:58:53+00:00'
---

# Original Description
https://xmrig.com/benchmark is really useful to look up hw performance.
I see we already print out cpu model, mbo and ddr4 info. It would be great to have cpu speed in the benchmark report.

# Discussion History
## Spudz76 | 2022-03-01T00:54:06+00:00
This requires deeper probing than simple DMI queries.  Maybe possible but would likely also require Ring0 access and another list of per-family MSR locations to read the actual running speed.

# Action History
- Created by: heavyarms2112 | 2022-02-28T21:13:54+00:00
- Closed at: 2022-04-03T07:58:53+00:00
