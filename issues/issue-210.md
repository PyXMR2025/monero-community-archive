---
title: 'Daemon RPC: COMMAND_RPC_IS_KEY_IMAGE_SPENT is slow w/large pool'
source_url: https://github.com/seraphis-migration/monero/issues/210
author: j-berman
assignees: []
labels:
- upstream
created_at: '2025-10-30T22:59:57+00:00'
updated_at: '2026-01-08T20:22:32+00:00'
type: issue
status: closed
closed_at: '2026-01-08T20:22:32+00:00'
---

# Original Description
Reported by @nahuhh.

It's slow because mainly because it's reading the whole pool in `get_pool_transactions_and_spent_keys_info`, even if a single key image is provided to the endpoint.

This could use `are_key_images_spent_in_pool` instead (with a little bit of plumbing work for unrestricted connections).

# Discussion History
## j-berman | 2026-01-08T20:22:32+00:00
Fixed in #281 and https://github.com/monero-project/monero/pull/10272

# Action History
- Created by: j-berman | 2025-10-30T22:59:57+00:00
- Closed at: 2026-01-08T20:22:32+00:00
