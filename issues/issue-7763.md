---
title: export_transfers wallet command truncates integrated addresses in destination
  field
source_url: https://github.com/monero-project/monero/issues/7763
author: ndorf
assignees: []
labels: []
created_at: '2021-06-24T19:12:28+00:00'
updated_at: '2021-07-10T22:01:51+00:00'
type: issue
status: closed
closed_at: '2021-07-10T22:01:51+00:00'
---

# Original Description
Subject pretty much covers it. When the `export_transfers` command is used, the resulting CSV file contains only the first 100 characters of the destination address. This is not sufficient to include a 106-character integrated address, so those are truncated.

This is unlike the `show_transfers` command, which shows the full destination address.

# Discussion History
## ndorf | 2021-06-25T22:15:01+00:00
Tested with #7764 and it looks fixed to me.

# Action History
- Created by: ndorf | 2021-06-24T19:12:28+00:00
- Closed at: 2021-07-10T22:01:51+00:00
