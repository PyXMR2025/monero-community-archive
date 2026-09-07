---
title: Generalize multisig wallet creation to 1) prepare, 2) make, 3) exchange for
  N-M times
source_url: https://github.com/monero-project/monero/issues/5889
author: woodser
assignees: []
labels: []
created_at: '2019-09-06T19:44:19+00:00'
updated_at: '2026-09-05T00:00:02+00:00'
type: issue
status: closed
closed_at: '2026-09-05T00:00:02+00:00'
---

# Original Description
This issue proposes deprecating `finalize_multisig`, which is a sub-case of `exchange_multisig_keys`, as it is redundant, requires additional code paths and tests in Monero Core and dependent applications, and requires additional time to understand and apply.

# Discussion History
## selsta | 2026-09-05T00:00:02+00:00
Resolved in https://github.com/monero-project/monero/pull/10614.

# Action History
- Created by: woodser | 2019-09-06T19:44:19+00:00
- Closed at: 2026-09-05T00:00:02+00:00
