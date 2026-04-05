---
title: Improve error messages in coin control
source_url: https://github.com/MrCyjaneK/monero_c/issues/75
author: MrCyjaneK
assignees: []
labels: []
created_at: '2024-10-16T11:06:01+00:00'
updated_at: '2025-01-13T11:41:46+00:00'
type: issue
status: closed
closed_at: '2025-01-13T11:41:45+00:00'
---

# Original Description
As reported by Ramo:
> Selected 2 * 0.001 and tried to send 0.002. As expected, the transaction was not allowed, but the error message read: "Not enough funds to transfer, available only 0.00986934; transaction amount 0.00204342 = 0.002 + 0.00004342 (fees)." The error message should ideally show the selected coins balance (or available balance) as 0.002, not the total available balance.


# Discussion History
# Action History
- Created by: MrCyjaneK | 2024-10-16T11:06:01+00:00
- Closed at: 2025-01-13T11:41:45+00:00
