---
title: ARM64 NEON with crypto extensions has 64-bit to 128-bit multiply
source_url: https://github.com/monero-project/monero/issues/2968
author: yuhong
assignees: []
labels: []
created_at: '2017-12-20T01:51:32+00:00'
updated_at: '2026-06-24T18:32:26+00:00'
type: issue
status: closed
closed_at: '2026-06-24T18:32:26+00:00'
---

# Original Description
ARM64 NEON with crypto extensions has 64-bit to 128-bit multiply (even in AArch32 too!):
See https://pdfs.semanticscholar.org/a0cf/28bf5e72351bcad23154549501a9d5afc968.pdf 
64-bit multiply available only with crypto extensions.

# Discussion History
## hyc | 2017-12-20T17:55:05+00:00
Not sure it matters, since there is still the problem of stalling the pipeline when moving data in and out of the vector registers. You're welcome to write and benchmark a patch for it.

## moneromooo-monero | 2018-10-02T18:47:51+00:00
Keep in mind Monero is now going to use variant 2 from the 18th of october,

+hacktoberfest

## selsta | 2026-06-24T18:32:26+00:00
RandomX uses ARM64 NEON for JIT.

# Action History
- Created by: yuhong | 2017-12-20T01:51:32+00:00
- Closed at: 2026-06-24T18:32:26+00:00
