---
title: Upgrading to any 0.17.x.x version breaks ledger integration
source_url: https://github.com/monero-project/monero-gui/issues/3191
author: balboah
assignees: []
labels: []
created_at: '2020-10-25T10:35:44+00:00'
updated_at: '2020-10-25T16:02:30+00:00'
type: issue
status: closed
closed_at: '2020-10-25T16:02:29+00:00'
---

# Original Description
v0.16.0.3 works fine together with Ledger view key.
It prompts to upgrade to the latest v0.17. When you close the app to upgrade and then try to login again, you get:

- wrong device status: (didn't save the hex codes)
- if you retry, the app crashes
- if you close, the app freezes and needs force close

I tried:
- restarting ledger
- reconnecting cable
- all available v0.17 releases

Downgrading to v0.16.0.3 fixes the issue.


# Discussion History
## selsta | 2020-10-25T13:51:29+00:00
You have to update your Ledger Monero app to v1.7.4

Also make sure Ledger Live is closed when using it in combination with Monero

## balboah | 2020-10-25T16:02:29+00:00
Thanks, this fixed the issue

# Action History
- Created by: balboah | 2020-10-25T10:35:44+00:00
- Closed at: 2020-10-25T16:02:29+00:00
