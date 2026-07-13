---
title: Get_block_template Fails with reserve_size > 127 (Expected Max 255)
source_url: https://github.com/monero-project/monero/issues/9930
author: minerjed
assignees: []
labels: []
created_at: '2025-05-19T13:40:00+00:00'
updated_at: '2026-07-10T11:08:33+00:00'
type: issue
status: closed
closed_at: '2026-07-10T11:08:33+00:00'
---

# Original Description
When calling the get_block_template RPC with a reserve_size greater than 127, the daemon fails with:
{
  "code": -5,
  "message": "Internal error: failed to create block template"
}

Error is actually in add_extra_nonce_to_tx_extra. This line:

tx_extra[start_pos] = static_cast<uint8_t>(extra_nonce.size());

This silently truncates lengths >127 or causes misinterpretation during block template construction.

# Discussion History
# Action History
- Created by: minerjed | 2025-05-19T13:40:00+00:00
- Closed at: 2026-07-10T11:08:33+00:00
