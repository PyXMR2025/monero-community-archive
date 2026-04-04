---
title: Windows NTFS compression causes crash during sync
source_url: https://github.com/monero-project/monero/issues/9617
author: selsta
assignees: []
labels:
- bug
created_at: '2024-12-13T23:03:00+00:00'
updated_at: '2025-01-18T11:04:52+00:00'
type: issue
status: closed
closed_at: '2025-01-18T11:04:52+00:00'
---

# Original Description
As reported here https://github.com/monero-project/monero/issues/9569#issuecomment-2539368523

It would be good to add a check to monerod to make sure the Windows file system, or the lmdb database does not have automatic compression enabled, otherwise it seems to crash during sync.

# Discussion History
## plowsof | 2024-12-29T21:07:02+00:00
Guest82 has expressed an interest in fixing this issue https://libera.monerologs.net/monero-dev/20241229#c481819 

## eversinc33 | 2024-12-29T21:12:19+00:00
That was me. Working on it right now.

# Action History
- Created by: selsta | 2024-12-13T23:03:00+00:00
- Closed at: 2025-01-18T11:04:52+00:00
