---
title: 'TODO: Revert breaking changes to `wallet2::create_transactions_*()` methods
  regarding payment IDs'
source_url: https://github.com/seraphis-migration/monero/issues/70
author: jeffro256
assignees: []
labels: []
created_at: '2025-07-24T07:06:43+00:00'
updated_at: '2025-08-19T03:26:23+00:00'
type: issue
status: closed
closed_at: '2025-08-19T03:26:23+00:00'
---

# Original Description
I broke the interfaces to these functions because I needed Carrot payment IDs to be associated to a specific destination, and I mistakenly assumed that determining which destination the payment ID is associated with was impossible with the current API. I forgot about the `is_integrated` field of `cryptonote::tx_destination_entry`. This can be used to find the associated index, and the breaking API changes can be reverted. 

# Discussion History
# Action History
- Created by: jeffro256 | 2025-07-24T07:06:43+00:00
- Closed at: 2025-08-19T03:26:23+00:00
