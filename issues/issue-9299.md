---
title: Support updating the pool state in monero-wallet-rpc `refresh`
source_url: https://github.com/monero-project/monero/issues/9299
author: woodser
assignees: []
labels:
- feature
- proposal
- discussion
created_at: '2024-04-21T10:46:54+00:00'
updated_at: '2026-09-05T00:50:05+00:00'
type: issue
status: closed
closed_at: '2026-09-05T00:50:05+00:00'
---

# Original Description
Currently, monero-wallet-rpc's [`refresh`](https://www.getmonero.org/resources/developer-guides/wallet-rpc.html#refresh) call does not support fetching the latest pool state from the daemon.

This issue requests adding a parameter to monero-wallet-rpc's `refresh` call to fetch the latest pool state.

# Discussion History
## Tzadiko | 2025-03-28T00:29:29+00:00
Is this still needed / relevant? I asked in Monero-Dev, with no response. Albeit I asked 8 hours ago so OP may not have had the time to respond.

## selsta | 2026-09-05T00:50:05+00:00
This appears already supported. If not, I can reopen this issue.

# Action History
- Created by: woodser | 2024-04-21T10:46:54+00:00
- Closed at: 2026-09-05T00:50:05+00:00
