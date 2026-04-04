---
title: Privacy issue with Monero wallet implementation
source_url: https://github.com/monero-project/monero-gui/issues/4399
author: ghost
assignees: []
labels: []
created_at: '2025-01-13T14:38:14+00:00'
updated_at: '2025-01-13T14:42:43+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
There is a privacy issue with how change is handled in Monero wallet implementation. When you send a transaction and get change, it always goes to your main address (the 8... address) instead of a new sub-address (or at least the sender address). This makes it easier to link your sub-addresses back to your main address, which could compromise your privacy when tracing transactions.

# Discussion History
# Action History
- Created by: ghost | 2025-01-13T14:38:14+00:00
