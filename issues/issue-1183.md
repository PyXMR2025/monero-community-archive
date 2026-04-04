---
title: Default wallet behaviour inconsistency
source_url: https://github.com/monero-project/monero/issues/1183
author: ghost
assignees: []
labels: []
created_at: '2016-10-05T11:30:00+00:00'
updated_at: '2016-10-06T01:44:57+00:00'
type: issue
status: closed
closed_at: '2016-10-06T01:44:57+00:00'
---

# Original Description
I'm trying to set `always_confirm_transfers` to default to `true` but have encountered difficulties...have therefore looked at `confirm_missing_payment_id` as an example and found the following:

In `wallet2.h`

Lines 95 & 98: `m_confirm_missing_payment_id(true)`

In `wallet2.cpp`

Line 1490: `m_confirm_missing_payment_id = true;`

But on line 1548: `GET_FIELD_FROM_JSON_RETURN_ON_ERROR(json, confirm_missing_payment_id, int, Int, false, false);`

Indicating that the default behaviour is to define `confirm_missing_payment_id` as `false`

Also...why is m_confirm_missing_payment_id both a private and public member of the wallet2 class, yet m_always_confirm_transfers is only private?


# Discussion History
# Action History
- Created by: ghost | 2016-10-05T11:30:00+00:00
- Closed at: 2016-10-06T01:44:57+00:00
