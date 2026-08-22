---
title: '[low priority] Can''t construct txs with custom tx extra'
source_url: https://github.com/seraphis-migration/monero/issues/459
author: j-berman
assignees: []
labels: []
created_at: '2026-08-20T18:34:36+00:00'
updated_at: '2026-08-20T18:34:36+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
`finalize_fcmps_and_range_proofs` doesn't take in the custom tx extra (any tx extra parts that are not part of the normal tx construction), and therefore the reconstructed tx used to verify the SAL proofs passed in doesn't reconstruct with custom tx extra (see `store_carrot_to_transaction_v1`). Therefore if the SAL proof was constructed with a custom tx extra, it would throw in the `verify_sal` check.

# Discussion History
# Action History
- Created by: j-berman | 2026-08-20T18:34:36+00:00
