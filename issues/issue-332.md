---
title: 'wallet rpc: payment id not an input for add_address_book'
source_url: https://github.com/monero-project/monero-docs/issues/332
author: plowsof
assignees: []
labels: []
created_at: '2026-06-02T08:05:38+00:00'
updated_at: '2026-06-02T08:48:12+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
https://github.com/monero-project/monero/pull/10589#issuecomment-4599935335

there are other address_book related calls that mention payment id , e.g. edit address book has set_payment_id which might not exist anymore

the payment id is inferred when we add an integrated address* the integrated address is saved and returned as the address 

# Discussion History
# Action History
- Created by: plowsof | 2026-06-02T08:05:38+00:00
