---
title: List of bugs in `export_transfers`
source_url: https://github.com/monero-project/monero/issues/9360
author: kevcrumb
assignees: []
labels:
- question
- discussion
created_at: '2024-06-11T11:46:48+00:00'
updated_at: '2024-06-14T07:38:54+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Related to monero-project/monero-gui#3554 and #4236, this is an overview of problems with CLI's **export_transfers**:

1. [ ] `Do you really want to export tx_key?` even when no export of tx_keys requested (i.e. without `option=with_keys`)
2. [ ] help misleadingly indicates `option=<with_keys>` (should actually be `option=with_keys`)
3. [ ] transactions with multiple recipients cause one bad line with mostly empty fields per additional recipient (should be one line per recipient)
4. [ ] "running balance" is wrong, at least when not exporting to entire history and also seems to somehow be relative to monero max supply (??)
5. [ ] if description as set per `set_tx_note` contains a comma, it will become a new field (fields should be quoted as is done with the input field)
6. [ ] exports should contain a column "total" (amount+fee ; maybe in the first "amount" column at current field 5)
7. [ ] Trezor requests confirmation for every single tx key (60 records = roughly 60 seconds of button pressing; should be once for entire operation)


# Discussion History
# Action History
- Created by: kevcrumb | 2024-06-11T11:46:48+00:00
