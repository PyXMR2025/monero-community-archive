---
title: Failed transaction will stay up in the transactions list.
source_url: https://github.com/monero-project/monero-gui/issues/4606
author: ModemNakata
assignees: []
labels: []
created_at: '2026-06-15T11:02:17+00:00'
updated_at: '2026-06-15T12:07:07+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I had a failed transaction using some random remote node, it was 77 days ago, but transaction still stays on top of the list, is there a way to remove this tx?

<img width="1010" height="321" alt="Image" src="https://github.com/user-attachments/assets/72a80bef-8fd4-4aa6-8fea-cdf4f364045b" />

# Discussion History
## selsta | 2026-06-15T12:07:07+00:00
Unfortunately the only way to remove it is a full rescan, which would mean you lose other information like receiving address. I'll try to improve this in a future release.

# Action History
- Created by: ModemNakata | 2026-06-15T11:02:17+00:00
