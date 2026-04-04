---
title: Document `--db-sync-mode` thoroughly.
source_url: https://github.com/monero-project/monero/issues/7379
author: crocket
assignees: []
labels: []
created_at: '2021-02-12T13:23:01+00:00'
updated_at: '2021-02-12T13:40:56+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
According to various internet sources, correct values for `--db-sync-mode` seem to be
* safe
* `fast[:sync|async[:<n>blocks]<n>bytes]]`
* `fastest[:sync|async[:<n>blocks]<n>bytes]]`

After monerod is synchronized, safe mode is turned on by monerod. When it's not synchronized, it turns off safe mode.

I don't know how the value of `db-sync-mode` interacts with the fact that monerod turns safe mode on and off during runtime.

# Discussion History
# Action History
- Created by: crocket | 2021-02-12T13:23:01+00:00
